# v16.0.2 → v16.0.3 · 要調査の変更候補 (35)

[一覧の目次](README.md)

<a id="compare-e2da6d0b31850caf3a244e644430b1ba"></a>

### [`00ba9858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9858.md) → [`00baa84c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa84c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE16CreateStringImplEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c370.md) · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d340.md) · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba98c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9858.md#insn-00ba98c0) · [`00ba9918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9858.md#insn-00ba9918) · [`00ba9958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9858.md#insn-00ba9958)
- 新版 [`00baa8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa84c.md#insn-00baa8b4) · [`00baa90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa84c.md#insn-00baa90c) · [`00baa94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa84c.md#insn-00baa94c)

~~~diff
- 00ba98c0 ["INT_ADD", "register:40f0:8", ["const:ba98c0:8", "const:4:8"]]
- 00ba98c0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00baa8b4 ["INT_ADD", "register:40f0:8", ["const:baa8b4:8", "const:4:8"]]
+ 00baa8b4 ["CALL", null, ["callee:00c5d240:8"]]
- 00ba98c0 bytes 6cca0294
+ 00baa8b4 bytes 63ca0294
- 00ba9918 ["INT_ADD", "register:40f0:8", ["const:ba9918:8", "const:4:8"]]
- 00ba9918 ["CALL", null, ["callee:00c5d240:8"]]
+ 00baa90c ["INT_ADD", "register:40f0:8", ["const:baa90c:8", "const:4:8"]]
+ 00baa90c ["CALL", null, ["callee:00c5d240:8"]]
- 00ba9918 bytes 56ca0294
+ 00baa90c bytes 4dca0294
- 00ba9958 ["INT_ADD", "register:40f0:8", ["const:ba9958:8", "const:4:8"]]
- 00ba9958 ["CALL", null, ["callee:00c5d240:8"]]
+ 00baa94c ["INT_ADD", "register:40f0:8", ["const:baa94c:8", "const:4:8"]]
+ 00baa94c ["CALL", null, ["callee:00c5d240:8"]]
- 00ba9958 bytes 46ca0294
+ 00baa94c bytes 3dca0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012bae21e13335e85ce358f280361c0e"></a>

### [`00ba9998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9998.md) → [`00baa98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa98c.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE25__empla

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf10.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5dee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dee0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9998.md#insn-00ba9a08) · [`00ba9a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9998.md#insn-00ba9a50) · [`00ba9aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9998.md#insn-00ba9aa0)
- 新版 [`00baa9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa98c.md#insn-00baa9fc) · [`00baaa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa98c.md#insn-00baaa44) · [`00baaa94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa98c.md#insn-00baaa94)

~~~diff
- 00ba9a08 ["INT_ADD", "register:40f0:8", ["const:ba9a08:8", "const:4:8"]]
- 00ba9a08 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa9fc ["INT_ADD", "register:40f0:8", ["const:baa9fc:8", "const:4:8"]]
+ 00baa9fc ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9a08 bytes c6b90294
+ 00baa9fc bytes bdb90294
- 00ba9a50 ["INT_ADD", "register:40f0:8", ["const:ba9a50:8", "const:4:8"]]
- 00ba9a50 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baaa44 ["INT_ADD", "register:40f0:8", ["const:baaa44:8", "const:4:8"]]
+ 00baaa44 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9a50 bytes b4b90294
+ 00baaa44 bytes abb90294
- 00ba9aa0 ["INT_ADD", "register:40f0:8", ["const:ba9aa0:8", "const:4:8"]]
- 00ba9aa0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00baaa94 ["INT_ADD", "register:40f0:8", ["const:baaa94:8", "const:4:8"]]
+ 00baaa94 ["CALL", null, ["callee:00c58f30:8"]]
- 00ba9aa0 bytes 30b90294
+ 00baaa94 bytes 27b90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673836e5514fa4aab8ec55da2d82cfad"></a>

### [`00ba9cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9cc4.md) → [`00baacb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baacb8.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb70.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db40.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9cc4.md#insn-00ba9d5c) · [`00ba9da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9cc4.md#insn-00ba9da4)
- 新版 [`00baad50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baacb8.md#insn-00baad50) · [`00baad98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baacb8.md#insn-00baad98)

~~~diff
- 00ba9d5c ["INT_ADD", "register:40f0:8", ["const:ba9d5c:8", "const:4:8"]]
- 00ba9d5c ["CALL", null, ["callee:00c590f0:8"]]
+ 00baad50 ["INT_ADD", "register:40f0:8", ["const:baad50:8", "const:4:8"]]
+ 00baad50 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9d5c bytes f1b80294
+ 00baad50 bytes e8b80294
- 00ba9da4 ["INT_ADD", "register:40f0:8", ["const:ba9da4:8", "const:4:8"]]
- 00ba9da4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baad98 ["INT_ADD", "register:40f0:8", ["const:baad98:8", "const:4:8"]]
+ 00baad98 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9da4 bytes dfb80294
+ 00baad98 bytes d6b80294
~~~


<a id="compare-cc1a6016e647904ac027b0ae0c5e53ca"></a>

### [`00baa44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa44c.md) → [`00bab440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab440.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE6insertENS_11__wrap_iterIPKS6_EEOS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d120.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5cc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc40.md)
- 新版 呼出元 1件 [`00c5e0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0f0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5dc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa44c.md#insn-00baa5d0) · [`00baa6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa44c.md#insn-00baa6a4) · [`00baa6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa44c.md#insn-00baa6c4)
- 新版 [`00bab5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab440.md#insn-00bab5c4) · [`00bab698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab440.md#insn-00bab698) · [`00bab6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab440.md#insn-00bab6b8)

~~~diff
- 00baa5d0 ["INT_ADD", "register:40f0:8", ["const:baa5d0:8", "const:4:8"]]
- 00baa5d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bab5c4 ["INT_ADD", "register:40f0:8", ["const:bab5c4:8", "const:4:8"]]
+ 00bab5c4 ["CALL", null, ["callee:00c58f50:8"]]
- 00baa5d0 bytes 6cb60294
+ 00bab5c4 bytes 63b60294
- 00baa6a4 ["INT_ADD", "register:40f0:8", ["const:baa6a4:8", "const:4:8"]]
- 00baa6a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bab698 ["INT_ADD", "register:40f0:8", ["const:bab698:8", "const:4:8"]]
+ 00bab698 ["CALL", null, ["callee:00c58f30:8"]]
- 00baa6a4 bytes 2fb60294
+ 00bab698 bytes 26b60294
- 00baa6c4 ["INT_ADD", "register:40f0:8", ["const:baa6c4:8", "const:4:8"]]
- 00baa6c4 ["CALL", null, ["callee:00c5dc10:8"]]
+ 00bab6b8 ["INT_ADD", "register:40f0:8", ["const:bab6b8:8", "const:4:8"]]
+ 00bab6b8 ["CALL", null, ["callee:00c5dc10:8"]]
- 00baa6c4 bytes 5fc90294
+ 00bab6b8 bytes 56c90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b267ab2ca0fb77895f865cc387c2b909"></a>

### [`00baa8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa8e8.md) → [`00bab8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab8dc.md) _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc40.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5dc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc10.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa8e8.md#insn-00baa9dc) · [`00baaa34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa8e8.md#insn-00baaa34) · [`00baab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa8e8.md#insn-00baab1c)
- 新版 [`00bab9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab8dc.md#insn-00bab9d0) · [`00baba28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab8dc.md#insn-00baba28) · [`00babb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00bab8dc.md#insn-00babb10)

~~~diff
- 00baa9dc ["INT_ADD", "register:40f0:8", ["const:baa9dc:8", "const:4:8"]]
- 00baa9dc ["CALL", null, ["callee:00c58f50:8"]]
+ 00bab9d0 ["INT_ADD", "register:40f0:8", ["const:bab9d0:8", "const:4:8"]]
+ 00bab9d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00baa9dc bytes 69b50294
+ 00bab9d0 bytes 60b50294
- 00baaa34 ["INT_ADD", "register:40f0:8", ["const:baaa34:8", "const:4:8"]]
- 00baaa34 ["CALL", null, ["callee:00c58f30:8"]]
+ 00baba28 ["INT_ADD", "register:40f0:8", ["const:baba28:8", "const:4:8"]]
+ 00baba28 ["CALL", null, ["callee:00c58f30:8"]]
- 00baaa34 bytes 4bb50294
+ 00baba28 bytes 42b50294
- 00baab1c ["INT_ADD", "register:40f0:8", ["const:baab1c:8", "const:4:8"]]
- 00baab1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00babb10 ["INT_ADD", "register:40f0:8", ["const:babb10:8", "const:4:8"]]
+ 00babb10 ["CALL", null, ["callee:00c58f50:8"]]
- 00baab1c bytes 19b50294
+ 00babb10 bytes 10b50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9b13b41809fc91b3f54734ef6247af"></a>

### [`00baaba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baaba0.md) → [`00babb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babb94.md) FUN_00babb94

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baac3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baaba0.md#insn-00baac3c) · [`00baac58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baaba0.md#insn-00baac58) · [`00baacfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baaba0.md#insn-00baacfc)
- 新版 [`00babc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babb94.md#insn-00babc30) · [`00babc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babb94.md#insn-00babc4c) · [`00babcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babb94.md#insn-00babcf0)

~~~diff
- 00baac3c ["INT_ADD", "register:40f0:8", ["const:baac3c:8", "const:4:8"]]
- 00baac3c ["CALL", null, ["callee:00c5d5d0:8"]]
+ 00babc30 ["INT_ADD", "register:40f0:8", ["const:babc30:8", "const:4:8"]]
+ 00babc30 ["CALL", null, ["callee:00c5d5d0:8"]]
- 00baac3c bytes 71c60294
+ 00babc30 bytes 68c60294
- 00baac58 ["INT_ADD", "register:40f0:8", ["const:baac58:8", "const:4:8"]]
- 00baac58 ["CALL", null, ["callee:00c58f50:8"]]
+ 00babc4c ["INT_ADD", "register:40f0:8", ["const:babc4c:8", "const:4:8"]]
+ 00babc4c ["CALL", null, ["callee:00c58f50:8"]]
- 00baac58 bytes cab40294
+ 00babc4c bytes c1b40294
- 00baacfc ["INT_ADD", "register:40f0:8", ["const:baacfc:8", "const:4:8"]]
- 00baacfc ["CALL", null, ["callee:00c58f30:8"]]
+ 00babcf0 ["INT_ADD", "register:40f0:8", ["const:babcf0:8", "const:4:8"]]
+ 00babcf0 ["CALL", null, ["callee:00c58f30:8"]]
- 00baacfc bytes 99b40294
+ 00babcf0 bytes 90b40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582a8694debe8fdc6812fe4404489e8e"></a>

### [`00baadf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md) → [`00babdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babdec.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d110.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0e0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md#insn-00baae8c) · [`00baaf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md#insn-00baaf84) · [`00baafa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md#insn-00baafa4)
- 新版 [`00babe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babdec.md#insn-00babe80) · [`00babf78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babdec.md#insn-00babf78) · [`00babf98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babdec.md#insn-00babf98)

~~~diff
- 00baae8c ["INT_ADD", "register:40f0:8", ["const:baae8c:8", "const:4:8"]]
- 00baae8c ["CALL", null, ["callee:00c58f30:8"]]
+ 00babe80 ["INT_ADD", "register:40f0:8", ["const:babe80:8", "const:4:8"]]
+ 00babe80 ["CALL", null, ["callee:00c58f30:8"]]
- 00baae8c bytes 35b40294
+ 00babe80 bytes 2cb40294
- 00baaf84 ["INT_ADD", "register:40f0:8", ["const:baaf84:8", "const:4:8"]]
- 00baaf84 ["CALL", null, ["callee:00c58f50:8"]]
+ 00babf78 ["INT_ADD", "register:40f0:8", ["const:babf78:8", "const:4:8"]]
+ 00babf78 ["CALL", null, ["callee:00c58f50:8"]]
- 00baaf84 bytes ffb30294
+ 00babf78 bytes f6b30294
- 00baafa4 ["INT_ADD", "register:40f0:8", ["const:baafa4:8", "const:4:8"]]
- 00baafa4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00babf98 ["INT_ADD", "register:40f0:8", ["const:babf98:8", "const:4:8"]]
+ 00babf98 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00baafa4 bytes 9bc00294
+ 00babf98 bytes 92c00294
~~~


<a id="compare-827a67374b18d7c9e7591c318dc0fb84"></a>

### [`00bab8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00bab8c4.md) → [`00bac8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bac8b8.md) FUN_00bac8b8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c550.md) [`00c5c700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c700.md) [`00c5d0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0d0.md)
- 新版 呼出元 1件 [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d520.md) [`00c5d6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d6d0.md) [`00c5e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00bab8c4.md#insn-00bab974) · [`00bab984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00bab8c4.md#insn-00bab984) · [`00bab9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00bab8c4.md#insn-00bab9d0)
- 新版 [`00bac968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bac8b8.md#insn-00bac968) · [`00bac978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bac8b8.md#insn-00bac978) · [`00bac9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bac8b8.md#insn-00bac9c4)

~~~diff
- 00bab974 ["INT_ADD", "register:40f0:8", ["const:bab974:8", "const:4:8"]]
- 00bab974 ["CALL", null, ["callee:00c5e0a0:8"]]
+ 00bac968 ["INT_ADD", "register:40f0:8", ["const:bac968:8", "const:4:8"]]
+ 00bac968 ["CALL", null, ["callee:00c5e0a0:8"]]
- 00bab974 bytes d7c50294
+ 00bac968 bytes cec50294
- 00bab984 ["INT_ADD", "register:40f0:8", ["const:bab984:8", "const:4:8"]]
- 00bab984 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bac978 ["INT_ADD", "register:40f0:8", ["const:bac978:8", "const:4:8"]]
+ 00bac978 ["CALL", null, ["callee:00c58f50:8"]]
- 00bab984 bytes 7fb10294
+ 00bac978 bytes 76b10294
- 00bab9d0 ["INT_ADD", "register:40f0:8", ["const:bab9d0:8", "const:4:8"]]
- 00bab9d0 ["CALL", null, ["callee:00c5d520:8"]]
+ 00bac9c4 ["INT_ADD", "register:40f0:8", ["const:bac9c4:8", "const:4:8"]]
+ 00bac9c4 ["CALL", null, ["callee:00c5d520:8"]]
- 00bab9d0 bytes e0c20294
+ 00bac9c4 bytes d7c20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f83a3c45a23a37b56e41c16499eff9"></a>

### [`00baba2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00baba2c.md) → [`00baca20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00baca20.md) _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0d0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0a0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baba88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00baba2c.md#insn-00baba88) · [`00baba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00baba2c.md#insn-00baba94) · [`00babb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00baba2c.md#insn-00babb70)
- 新版 [`00baca7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00baca20.md#insn-00baca7c) · [`00baca88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00baca20.md#insn-00baca88) · [`00bacb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00baca20.md#insn-00bacb64)

~~~diff
- 00baba88 ["INT_ADD", "register:40f0:8", ["const:baba88:8", "const:4:8"]]
- 00baba88 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00baca7c ["INT_ADD", "register:40f0:8", ["const:baca7c:8", "const:4:8"]]
+ 00baca7c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00baba88 bytes e2bd0294
+ 00baca7c bytes d9bd0294
- 00baba94 ["INT_ADD", "register:40f0:8", ["const:baba94:8", "const:4:8"]]
- 00baba94 ["CALL", null, ["callee:00c58f30:8"]]
+ 00baca88 ["INT_ADD", "register:40f0:8", ["const:baca88:8", "const:4:8"]]
+ 00baca88 ["CALL", null, ["callee:00c58f30:8"]]
- 00baba94 bytes 33b10294
+ 00baca88 bytes 2ab10294
- 00babb70 ["INT_ADD", "register:40f0:8", ["const:babb70:8", "const:4:8"]]
- 00babb70 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bacb64 ["INT_ADD", "register:40f0:8", ["const:bacb64:8", "const:4:8"]]
+ 00bacb64 ["CALL", null, ["callee:00c58f50:8"]]
- 00babb70 bytes 04b10294
+ 00bacb64 bytes fbb00294
~~~


<a id="compare-3c1621421885baba8b6efc1d48f1aa18"></a>

### [`00babf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babf18.md) → [`00bacf0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bacf0c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d050.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5e020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e020.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babf18.md#insn-00babfb4) · [`00babff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babf18.md#insn-00babff4)
- 新版 [`00bacfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bacf0c.md#insn-00bacfa8) · [`00bacfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00bacf0c.md#insn-00bacfe8)

~~~diff
- 00babfb4 ["INT_ADD", "register:40f0:8", ["const:babfb4:8", "const:4:8"]]
- 00babfb4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bacfa8 ["INT_ADD", "register:40f0:8", ["const:bacfa8:8", "const:4:8"]]
+ 00bacfa8 ["CALL", null, ["callee:00c590f0:8"]]
- 00babfb4 bytes 5bb00294
+ 00bacfa8 bytes 52b00294
- 00babff4 ["INT_ADD", "register:40f0:8", ["const:babff4:8", "const:4:8"]]
- 00babff4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bacfe8 ["INT_ADD", "register:40f0:8", ["const:bacfe8:8", "const:4:8"]]
+ 00bacfe8 ["CALL", null, ["callee:00c590f0:8"]]
- 00babff4 bytes 4bb00294
+ 00bacfe8 bytes 42b00294
~~~


<a id="compare-328362bc79c95113131986635d41c836"></a>

### [`00bac9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac9ec.md) → [`00bad9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md) FUN_00bad9e0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bac038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac038.md) [`00bacc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md) [`00bad180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad180.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00bad02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad02c.md) [`00badc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md) [`00bae174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae174.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac9ec.md#insn-00baca78) · [`00bacaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac9ec.md#insn-00bacaf8) · [`00bacb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac9ec.md#insn-00bacb78)
- 新版 [`00bada6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md#insn-00bada6c) · [`00badaec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md#insn-00badaec) · [`00badb6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md#insn-00badb6c)

~~~diff
- 00baca78 ["INT_ADD", "register:40f0:8", ["const:baca78:8", "const:4:8"]]
- 00baca78 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bada6c ["INT_ADD", "register:40f0:8", ["const:bada6c:8", "const:4:8"]]
+ 00bada6c ["CALL", null, ["callee:00c590f0:8"]]
- 00baca78 bytes aaad0294
+ 00bada6c bytes a1ad0294
- 00bacaf8 ["INT_ADD", "register:40f0:8", ["const:bacaf8:8", "const:4:8"]]
- 00bacaf8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00badaec ["INT_ADD", "register:40f0:8", ["const:badaec:8", "const:4:8"]]
+ 00badaec ["CALL", null, ["callee:00c590f0:8"]]
- 00bacaf8 bytes 8aad0294
+ 00badaec bytes 81ad0294
- 00bacb78 ["INT_ADD", "register:40f0:8", ["const:bacb78:8", "const:4:8"]]
- 00bacb78 ["CALL", null, ["callee:00c590f0:8"]]
+ 00badb6c ["INT_ADD", "register:40f0:8", ["const:badb6c:8", "const:4:8"]]
+ 00badb6c ["CALL", null, ["callee:00c590f0:8"]]
- 00bacb78 bytes 6aad0294
+ 00badb6c bytes 61ad0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2765dc1975509b5088d41f9a07cdd8"></a>

### [`00bacc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md) → [`00badc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md) FUN_00badc8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bac038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac038.md) [`00bacea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacea0.md) [`00bad180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad180.md) · 呼出先 2件 [`00bac9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac9ec.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00bad02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad02c.md) [`00bade94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md) [`00bae174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae174.md) · 呼出先 2件 [`00bad9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baccc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md#insn-00baccc4) · [`00bacd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md#insn-00bacd34) · [`00bacdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md#insn-00bacdc4)
- 新版 [`00badcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md#insn-00badcb8) · [`00badd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md#insn-00badd28) · [`00baddb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md#insn-00baddb8)

~~~diff
- 00baccc4 ["INT_ADD", "register:40f0:8", ["const:baccc4:8", "const:4:8"]]
- 00baccc4 ["CALL", null, ["callee:00bad9e0:8"]]
+ 00badcb8 ["INT_ADD", "register:40f0:8", ["const:badcb8:8", "const:4:8"]]
+ 00badcb8 ["CALL", null, ["callee:00bad9e0:8"]]
- 00baccc4 bytes 4affff97
+ 00badcb8 bytes 4affff97
- 00bacd34 ["INT_ADD", "register:40f0:8", ["const:bacd34:8", "const:4:8"]]
- 00bacd34 ["CALL", null, ["callee:00c590f0:8"]]
+ 00badd28 ["INT_ADD", "register:40f0:8", ["const:badd28:8", "const:4:8"]]
+ 00badd28 ["CALL", null, ["callee:00c590f0:8"]]
- 00bacd34 bytes fbac0294
+ 00badd28 bytes f2ac0294
- 00bacdc4 ["INT_ADD", "register:40f0:8", ["const:bacdc4:8", "const:4:8"]]
- 00bacdc4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baddb8 ["INT_ADD", "register:40f0:8", ["const:baddb8:8", "const:4:8"]]
+ 00baddb8 ["CALL", null, ["callee:00c590f0:8"]]
- 00bacdc4 bytes d7ac0294
+ 00baddb8 bytes ceac0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9641250429acf2914f9ba8d1339a2f96"></a>

### [`00bacea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacea0.md) → [`00bade94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md) FUN_00bade94

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bac038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac038.md) [`00bad180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad180.md) · 呼出先 2件 [`00bacc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00bad02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad02c.md) [`00bae174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae174.md) · 呼出先 2件 [`00badc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00badc8c.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baced4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacea0.md#insn-00baced4) · [`00bacf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacea0.md#insn-00bacf58) · [`00bad010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacea0.md#insn-00bad010)
- 新版 [`00badec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md#insn-00badec8) · [`00badf4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md#insn-00badf4c) · [`00bae004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md#insn-00bae004)

~~~diff
- 00baced4 ["INT_ADD", "register:40f0:8", ["const:baced4:8", "const:4:8"]]
- 00baced4 ["CALL", null, ["callee:00badc8c:8"]]
+ 00badec8 ["INT_ADD", "register:40f0:8", ["const:badec8:8", "const:4:8"]]
+ 00badec8 ["CALL", null, ["callee:00badc8c:8"]]
- 00baced4 bytes 71ffff97
+ 00badec8 bytes 71ffff97
- 00bacf58 ["INT_ADD", "register:40f0:8", ["const:bacf58:8", "const:4:8"]]
- 00bacf58 ["CALL", null, ["callee:00c590f0:8"]]
+ 00badf4c ["INT_ADD", "register:40f0:8", ["const:badf4c:8", "const:4:8"]]
+ 00badf4c ["CALL", null, ["callee:00c590f0:8"]]
- 00bacf58 bytes 72ac0294
+ 00badf4c bytes 69ac0294
- 00bad010 ["INT_ADD", "register:40f0:8", ["const:bad010:8", "const:4:8"]]
- 00bad010 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bae004 ["INT_ADD", "register:40f0:8", ["const:bae004:8", "const:4:8"]]
+ 00bae004 ["CALL", null, ["callee:00c590f0:8"]]
- 00bad010 bytes 44ac0294
+ 00bae004 bytes 3bac0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03aab7f5d5dacafaee3cf7ce6d0f759"></a>

### [`00bade60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md) → [`00baee54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md) FUN_00baee54

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bad494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad494.md) [`00bae10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md) [`00bae5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00bae488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae488.md) [`00baf100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md) [`00baf5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00badeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md#insn-00badeec) · [`00badf6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md#insn-00badf6c) · [`00badfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md#insn-00badfec)
- 新版 [`00baeee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md#insn-00baeee0) · [`00baef60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md#insn-00baef60) · [`00baefe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md#insn-00baefe0)

~~~diff
- 00badeec ["INT_ADD", "register:40f0:8", ["const:badeec:8", "const:4:8"]]
- 00badeec ["CALL", null, ["callee:00c590f0:8"]]
+ 00baeee0 ["INT_ADD", "register:40f0:8", ["const:baeee0:8", "const:4:8"]]
+ 00baeee0 ["CALL", null, ["callee:00c590f0:8"]]
- 00badeec bytes 8da80294
+ 00baeee0 bytes 84a80294
- 00badf6c ["INT_ADD", "register:40f0:8", ["const:badf6c:8", "const:4:8"]]
- 00badf6c ["CALL", null, ["callee:00c590f0:8"]]
+ 00baef60 ["INT_ADD", "register:40f0:8", ["const:baef60:8", "const:4:8"]]
+ 00baef60 ["CALL", null, ["callee:00c590f0:8"]]
- 00badf6c bytes 6da80294
+ 00baef60 bytes 64a80294
- 00badfec ["INT_ADD", "register:40f0:8", ["const:badfec:8", "const:4:8"]]
- 00badfec ["CALL", null, ["callee:00c590f0:8"]]
+ 00baefe0 ["INT_ADD", "register:40f0:8", ["const:baefe0:8", "const:4:8"]]
+ 00baefe0 ["CALL", null, ["callee:00c590f0:8"]]
- 00badfec bytes 4da80294
+ 00baefe0 bytes 44a80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5793c09e025c7b06fb535ffd78cf3da2"></a>

### [`00bae10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md) → [`00baf100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md) FUN_00baf100

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bad494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad494.md) [`00bae314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md) [`00bae5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md) · 呼出先 2件 [`00bade60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00bae488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae488.md) [`00baf308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md) [`00baf5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md) · 呼出先 2件 [`00baee54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md#insn-00bae138) · [`00bae1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md#insn-00bae1a8) · [`00bae238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md#insn-00bae238)
- 新版 [`00baf12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md#insn-00baf12c) · [`00baf19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md#insn-00baf19c) · [`00baf22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md#insn-00baf22c)

~~~diff
- 00bae138 ["INT_ADD", "register:40f0:8", ["const:bae138:8", "const:4:8"]]
- 00bae138 ["CALL", null, ["callee:00baee54:8"]]
+ 00baf12c ["INT_ADD", "register:40f0:8", ["const:baf12c:8", "const:4:8"]]
+ 00baf12c ["CALL", null, ["callee:00baee54:8"]]
- 00bae138 bytes 4affff97
+ 00baf12c bytes 4affff97
- 00bae1a8 ["INT_ADD", "register:40f0:8", ["const:bae1a8:8", "const:4:8"]]
- 00bae1a8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf19c ["INT_ADD", "register:40f0:8", ["const:baf19c:8", "const:4:8"]]
+ 00baf19c ["CALL", null, ["callee:00c590f0:8"]]
- 00bae1a8 bytes dea70294
+ 00baf19c bytes d5a70294
- 00bae238 ["INT_ADD", "register:40f0:8", ["const:bae238:8", "const:4:8"]]
- 00bae238 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf22c ["INT_ADD", "register:40f0:8", ["const:baf22c:8", "const:4:8"]]
+ 00baf22c ["CALL", null, ["callee:00c590f0:8"]]
- 00bae238 bytes baa70294
+ 00baf22c bytes b1a70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6dd2da19b6de4cee4b9d0867dd39466"></a>

### [`00bae314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md) → [`00baf308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md) FUN_00baf308

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bad494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad494.md) [`00bae5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md) · 呼出先 2件 [`00bae10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00bae488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae488.md) [`00baf5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md) · 呼出先 2件 [`00baf100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md#insn-00bae348) · [`00bae3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md#insn-00bae3cc) · [`00bae484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md#insn-00bae484)
- 新版 [`00baf33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md#insn-00baf33c) · [`00baf3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md#insn-00baf3c0) · [`00baf478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md#insn-00baf478)

~~~diff
- 00bae348 ["INT_ADD", "register:40f0:8", ["const:bae348:8", "const:4:8"]]
- 00bae348 ["CALL", null, ["callee:00baf100:8"]]
+ 00baf33c ["INT_ADD", "register:40f0:8", ["const:baf33c:8", "const:4:8"]]
+ 00baf33c ["CALL", null, ["callee:00baf100:8"]]
- 00bae348 bytes 71ffff97
+ 00baf33c bytes 71ffff97
- 00bae3cc ["INT_ADD", "register:40f0:8", ["const:bae3cc:8", "const:4:8"]]
- 00bae3cc ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf3c0 ["INT_ADD", "register:40f0:8", ["const:baf3c0:8", "const:4:8"]]
+ 00baf3c0 ["CALL", null, ["callee:00c590f0:8"]]
- 00bae3cc bytes 55a70294
+ 00baf3c0 bytes 4ca70294
- 00bae484 ["INT_ADD", "register:40f0:8", ["const:bae484:8", "const:4:8"]]
- 00bae484 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf478 ["INT_ADD", "register:40f0:8", ["const:baf478:8", "const:4:8"]]
+ 00baf478 ["CALL", null, ["callee:00c590f0:8"]]
- 00bae484 bytes 27a70294
+ 00baf478 bytes 1ea70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f7d8abc49f8ce231375fa30d75d0ab"></a>

### [`00bae908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md) → [`00baf8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf8fc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfe0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dfb0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md#insn-00bae9a0) · [`00bae9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md#insn-00bae9e8)
- 新版 [`00baf994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf8fc.md#insn-00baf994) · [`00baf9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf8fc.md#insn-00baf9dc)

~~~diff
- 00bae9a0 ["INT_ADD", "register:40f0:8", ["const:bae9a0:8", "const:4:8"]]
- 00bae9a0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf994 ["INT_ADD", "register:40f0:8", ["const:baf994:8", "const:4:8"]]
+ 00baf994 ["CALL", null, ["callee:00c590f0:8"]]
- 00bae9a0 bytes e0a50294
+ 00baf994 bytes d7a50294
- 00bae9e8 ["INT_ADD", "register:40f0:8", ["const:bae9e8:8", "const:4:8"]]
- 00bae9e8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf9dc ["INT_ADD", "register:40f0:8", ["const:baf9dc:8", "const:4:8"]]
+ 00baf9dc ["CALL", null, ["callee:00c590f0:8"]]
- 00bae9e8 bytes cea50294
+ 00baf9dc bytes c5a50294
~~~


<a id="compare-e82fa86c12de9a5f6ba8660563c76084"></a>

### [`00baea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md) → [`00bafa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafa10.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfd0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dfa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dfa0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md#insn-00baeab8) · [`00baeaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md#insn-00baeaf8)
- 新版 [`00bafaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafa10.md#insn-00bafaac) · [`00bafaec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafa10.md#insn-00bafaec)

~~~diff
- 00baeab8 ["INT_ADD", "register:40f0:8", ["const:baeab8:8", "const:4:8"]]
- 00baeab8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafaac ["INT_ADD", "register:40f0:8", ["const:bafaac:8", "const:4:8"]]
+ 00bafaac ["CALL", null, ["callee:00c590f0:8"]]
- 00baeab8 bytes 9aa50294
+ 00bafaac bytes 91a50294
- 00baeaf8 ["INT_ADD", "register:40f0:8", ["const:baeaf8:8", "const:4:8"]]
- 00baeaf8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafaec ["INT_ADD", "register:40f0:8", ["const:bafaec:8", "const:4:8"]]
+ 00bafaec ["CALL", null, ["callee:00c590f0:8"]]
- 00baeaf8 bytes 8aa50294
+ 00bafaec bytes 81a50294
~~~


<a id="compare-1a54fa52fa3e394018b59282db2cb94f"></a>

### [`00baeb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md) → [`00bafb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb30.md) _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d080.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d080.md)
- 新版 呼出元 1件 [`00c5e050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e050.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md#insn-00baeb58) · [`00baeb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md#insn-00baeb64)
- 新版 [`00bafb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb30.md#insn-00bafb4c) · [`00bafb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb30.md#insn-00bafb58)

~~~diff
- 00baeb58 ["INT_ADD", "register:40f0:8", ["const:baeb58:8", "const:4:8"]]
- 00baeb58 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bafb4c ["INT_ADD", "register:40f0:8", ["const:bafb4c:8", "const:4:8"]]
+ 00bafb4c ["CALL", null, ["callee:00c5e050:8"]]
- 00baeb58 bytes 4ab90294
+ 00bafb4c bytes 41b90294
- 00baeb64 ["INT_ADD", "register:40f0:8", ["const:baeb64:8", "const:4:8"]]
- 00baeb64 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bafb58 ["INT_ADD", "register:40f0:8", ["const:bafb58:8", "const:4:8"]]
+ 00bafb58 ["CALL", null, ["callee:00c5e050:8"]]
- 00baeb64 bytes 47b90294
+ 00bafb58 bytes 3eb90294
~~~


<a id="compare-d92e6b7c2ac7289194ec5f93c9518f8f"></a>

### [`00baeb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb7c.md) → [`00bafb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb70.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf60.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df30.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb7c.md#insn-00baec14) · [`00baec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb7c.md#insn-00baec5c)
- 新版 [`00bafc08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb70.md#insn-00bafc08) · [`00bafc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb70.md#insn-00bafc50)

~~~diff
- 00baec14 ["INT_ADD", "register:40f0:8", ["const:baec14:8", "const:4:8"]]
- 00baec14 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafc08 ["INT_ADD", "register:40f0:8", ["const:bafc08:8", "const:4:8"]]
+ 00bafc08 ["CALL", null, ["callee:00c590f0:8"]]
- 00baec14 bytes 43a50294
+ 00bafc08 bytes 3aa50294
- 00baec5c ["INT_ADD", "register:40f0:8", ["const:baec5c:8", "const:4:8"]]
- 00baec5c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafc50 ["INT_ADD", "register:40f0:8", ["const:bafc50:8", "const:4:8"]]
+ 00bafc50 ["CALL", null, ["callee:00c590f0:8"]]
- 00baec5c bytes 31a50294
+ 00bafc50 bytes 28a50294
~~~


<a id="compare-98b9eabad4a34862a717dffff3bec34f"></a>

### [`00baec90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md) → [`00bafc84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafc84.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf50.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df20.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baed2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md#insn-00baed2c) · [`00baed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md#insn-00baed6c)
- 新版 [`00bafd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafc84.md#insn-00bafd20) · [`00bafd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafc84.md#insn-00bafd60)

~~~diff
- 00baed2c ["INT_ADD", "register:40f0:8", ["const:baed2c:8", "const:4:8"]]
- 00baed2c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafd20 ["INT_ADD", "register:40f0:8", ["const:bafd20:8", "const:4:8"]]
+ 00bafd20 ["CALL", null, ["callee:00c590f0:8"]]
- 00baed2c bytes fda40294
+ 00bafd20 bytes f4a40294
- 00baed6c ["INT_ADD", "register:40f0:8", ["const:baed6c:8", "const:4:8"]]
- 00baed6c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafd60 ["INT_ADD", "register:40f0:8", ["const:bafd60:8", "const:4:8"]]
+ 00bafd60 ["CALL", null, ["callee:00c590f0:8"]]
- 00baed6c bytes eda40294
+ 00bafd60 bytes e4a40294
~~~


<a id="compare-b16a36579a70997bfb9f13fe7181d885"></a>

### [`00baedb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md) → [`00bafda4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafda4.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4le

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb30.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db00.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baee48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md#insn-00baee48) · [`00baee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md#insn-00baee90)
- 新版 [`00bafe3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafda4.md#insn-00bafe3c) · [`00bafe84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafda4.md#insn-00bafe84)

~~~diff
- 00baee48 ["INT_ADD", "register:40f0:8", ["const:baee48:8", "const:4:8"]]
- 00baee48 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafe3c ["INT_ADD", "register:40f0:8", ["const:bafe3c:8", "const:4:8"]]
+ 00bafe3c ["CALL", null, ["callee:00c590f0:8"]]
- 00baee48 bytes b6a40294
+ 00bafe3c bytes ada40294
- 00baee90 ["INT_ADD", "register:40f0:8", ["const:baee90:8", "const:4:8"]]
- 00baee90 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bafe84 ["INT_ADD", "register:40f0:8", ["const:bafe84:8", "const:4:8"]]
+ 00bafe84 ["CALL", null, ["callee:00c590f0:8"]]
- 00baee90 bytes a4a40294
+ 00bafe84 bytes 9ba40294
~~~


<a id="compare-f67336d8f7e665523661e6d03f0eeea8"></a>

### [`00baf3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md) → [`00bb03d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb03d0.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e150.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf410) · [`00baf428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf428) · [`00baf46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf46c)
- 新版 [`00bb0404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb03d0.md#insn-00bb0404) · [`00bb041c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb03d0.md#insn-00bb041c) · [`00bb0460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb03d0.md#insn-00bb0460)

~~~diff
- 00baf410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf410 ["INT_ADD", "register:40f0:8", ["const:baf410:8", "const:4:8"]]
- 00baf410 ["CALLIND", null, ["register:0:8"]]
+ 00bb0404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb0404 ["INT_ADD", "register:40f0:8", ["const:bb0404:8", "const:4:8"]]
+ 00bb0404 ["CALLIND", null, ["register:0:8"]]
- 00baf410 bytes 00013fd6
+ 00bb0404 bytes 00013fd6
- 00baf428 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf428 ["INT_ADD", "register:40f0:8", ["const:baf428:8", "const:4:8"]]
- 00baf428 ["CALLIND", null, ["register:0:8"]]
+ 00bb041c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb041c ["INT_ADD", "register:40f0:8", ["const:bb041c:8", "const:4:8"]]
+ 00bb041c ["CALLIND", null, ["register:0:8"]]
- 00baf428 bytes 20013fd6
+ 00bb041c bytes 20013fd6
- 00baf46c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf46c ["INT_ADD", "register:40f0:8", ["const:baf46c:8", "const:4:8"]]
- 00baf46c ["CALLIND", null, ["register:0:8"]]
+ 00bb0460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb0460 ["INT_ADD", "register:40f0:8", ["const:bb0460:8", "const:4:8"]]
+ 00bb0460 ["CALLIND", null, ["register:0:8"]]
- 00baf46c bytes 00013fd6
+ 00bb0460 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3b551f6b752dba524d2ed86ad784fe"></a>

### [`00baf560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md) → [`00bb0554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md) FUN_00bb0554

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00baeec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md) [`00baf7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md) · 呼出先 1件 [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md)
- 新版 呼出元 2件 [`00bafeb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md) [`00bb07b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb07b8.md) · 呼出先 1件 [`00c5e150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf594) · [`00baf5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf5ac) · [`00baf5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf5d0)
- 新版 [`00bb0588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md#insn-00bb0588) · [`00bb05a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md#insn-00bb05a0) · [`00bb05c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md#insn-00bb05c4)

~~~diff
- 00baf594 ["INT_ADD", "register:40f0:8", ["const:baf594:8", "const:4:8"]]
- 00baf594 ["CALL", null, ["callee:00c5e150:8"]]
+ 00bb0588 ["INT_ADD", "register:40f0:8", ["const:bb0588:8", "const:4:8"]]
+ 00bb0588 ["CALL", null, ["callee:00c5e150:8"]]
- 00baf594 bytes fbb60294
+ 00bb0588 bytes f2b60294
- 00baf5ac ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf5ac ["INT_ADD", "register:40f0:8", ["const:baf5ac:8", "const:4:8"]]
- 00baf5ac ["CALLIND", null, ["register:0:8"]]
+ 00bb05a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb05a0 ["INT_ADD", "register:40f0:8", ["const:bb05a0:8", "const:4:8"]]
+ 00bb05a0 ["CALLIND", null, ["register:0:8"]]
- 00baf5ac bytes 20013fd6
+ 00bb05a0 bytes 20013fd6
- 00baf5d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf5d0 ["INT_ADD", "register:40f0:8", ["const:baf5d0:8", "const:4:8"]]
- 00baf5d0 ["CALLIND", null, ["register:0:8"]]
+ 00bb05c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb05c4 ["INT_ADD", "register:40f0:8", ["const:bb05c4:8", "const:4:8"]]
+ 00bb05c4 ["CALLIND", null, ["register:0:8"]]
- 00baf5d0 bytes 00013fd6
+ 00bb05c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a358644bc38062d7dd7b38955535bceb"></a>

### [`00baf668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md) → [`00bb065c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb065c.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccc0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc90.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf698) · [`00baf6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf6b4) · [`00baf6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf6f0)
- 新版 [`00bb068c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb065c.md#insn-00bb068c) · [`00bb06a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb065c.md#insn-00bb06a8) · [`00bb06e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb065c.md#insn-00bb06e4)

~~~diff
- 00baf698 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf698 ["INT_ADD", "register:40f0:8", ["const:baf698:8", "const:4:8"]]
- 00baf698 ["CALLIND", null, ["register:0:8"]]
+ 00bb068c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb068c ["INT_ADD", "register:40f0:8", ["const:bb068c:8", "const:4:8"]]
+ 00bb068c ["CALLIND", null, ["register:0:8"]]
- 00baf698 bytes 20013fd6
+ 00bb068c bytes 20013fd6
- 00baf6b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf6b4 ["INT_ADD", "register:40f0:8", ["const:baf6b4:8", "const:4:8"]]
- 00baf6b4 ["CALLIND", null, ["register:0:8"]]
+ 00bb06a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb06a8 ["INT_ADD", "register:40f0:8", ["const:bb06a8:8", "const:4:8"]]
+ 00bb06a8 ["CALLIND", null, ["register:0:8"]]
- 00baf6b4 bytes 20013fd6
+ 00bb06a8 bytes 20013fd6
- 00baf6f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf6f0 ["INT_ADD", "register:40f0:8", ["const:baf6f0:8", "const:4:8"]]
- 00baf6f0 ["CALLIND", null, ["register:0:8"]]
+ 00bb06e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb06e4 ["INT_ADD", "register:40f0:8", ["const:bb06e4:8", "const:4:8"]]
+ 00bb06e4 ["CALLIND", null, ["register:0:8"]]
- 00baf6f0 bytes 00013fd6
+ 00bb06e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ac5f41d4810f84f36ae9b0051ef913"></a>

### [`00bafa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafa74.md) → [`00bb0a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0a68.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df10.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafa74.md#insn-00bafb0c) · [`00bafb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafa74.md#insn-00bafb54)
- 新版 [`00bb0b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0a68.md#insn-00bb0b00) · [`00bb0b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0a68.md#insn-00bb0b48)

~~~diff
- 00bafb0c ["INT_ADD", "register:40f0:8", ["const:bafb0c:8", "const:4:8"]]
- 00bafb0c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0b00 ["INT_ADD", "register:40f0:8", ["const:bb0b00:8", "const:4:8"]]
+ 00bb0b00 ["CALL", null, ["callee:00c590f0:8"]]
- 00bafb0c bytes 85a10294
+ 00bb0b00 bytes 7ca10294
- 00bafb54 ["INT_ADD", "register:40f0:8", ["const:bafb54:8", "const:4:8"]]
- 00bafb54 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0b48 ["INT_ADD", "register:40f0:8", ["const:bb0b48:8", "const:4:8"]]
+ 00bb0b48 ["CALL", null, ["callee:00c590f0:8"]]
- 00bafb54 bytes 73a10294
+ 00bb0b48 bytes 6aa10294
~~~


<a id="compare-9fd25e7c8818f611be359f446ead24f6"></a>

### [`00bafb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafb88.md) → [`00bb0b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0b7c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf30.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df00.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafb88.md#insn-00bafc24) · [`00bafc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafb88.md#insn-00bafc64)
- 新版 [`00bb0c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0b7c.md#insn-00bb0c18) · [`00bb0c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0b7c.md#insn-00bb0c58)

~~~diff
- 00bafc24 ["INT_ADD", "register:40f0:8", ["const:bafc24:8", "const:4:8"]]
- 00bafc24 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0c18 ["INT_ADD", "register:40f0:8", ["const:bb0c18:8", "const:4:8"]]
+ 00bb0c18 ["CALL", null, ["callee:00c590f0:8"]]
- 00bafc24 bytes 3fa10294
+ 00bb0c18 bytes 36a10294
- 00bafc64 ["INT_ADD", "register:40f0:8", ["const:bafc64:8", "const:4:8"]]
- 00bafc64 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0c58 ["INT_ADD", "register:40f0:8", ["const:bb0c58:8", "const:4:8"]]
+ 00bb0c58 ["CALL", null, ["callee:00c590f0:8"]]
- 00bafc64 bytes 2fa10294
+ 00bb0c58 bytes 26a10294
~~~


<a id="compare-a1a7144b9c8a2c852fc565e84d25319c"></a>

### [`00bafca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md) → [`00bb0c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0c9c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d000.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dfd0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md#insn-00bafd40) · [`00bafd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md#insn-00bafd88)
- 新版 [`00bb0d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0c9c.md#insn-00bb0d34) · [`00bb0d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0c9c.md#insn-00bb0d7c)

~~~diff
- 00bafd40 ["INT_ADD", "register:40f0:8", ["const:bafd40:8", "const:4:8"]]
- 00bafd40 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0d34 ["INT_ADD", "register:40f0:8", ["const:bb0d34:8", "const:4:8"]]
+ 00bb0d34 ["CALL", null, ["callee:00c590f0:8"]]
- 00bafd40 bytes f8a00294
+ 00bb0d34 bytes efa00294
- 00bafd88 ["INT_ADD", "register:40f0:8", ["const:bafd88:8", "const:4:8"]]
- 00bafd88 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0d7c ["INT_ADD", "register:40f0:8", ["const:bb0d7c:8", "const:4:8"]]
+ 00bb0d7c ["CALL", null, ["callee:00c590f0:8"]]
- 00bafd88 bytes e6a00294
+ 00bb0d7c bytes dda00294
~~~


<a id="compare-883d59301c28bae9a8bffb7a33d0a37b"></a>

### [`00bafdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafdbc.md) → [`00bb0db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0db0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cff0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dfc0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafe58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafdbc.md#insn-00bafe58) · [`00bafe98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafdbc.md#insn-00bafe98)
- 新版 [`00bb0e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0db0.md#insn-00bb0e4c) · [`00bb0e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0db0.md#insn-00bb0e8c)

~~~diff
- 00bafe58 ["INT_ADD", "register:40f0:8", ["const:bafe58:8", "const:4:8"]]
- 00bafe58 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0e4c ["INT_ADD", "register:40f0:8", ["const:bb0e4c:8", "const:4:8"]]
+ 00bb0e4c ["CALL", null, ["callee:00c590f0:8"]]
- 00bafe58 bytes b2a00294
+ 00bb0e4c bytes a9a00294
- 00bafe98 ["INT_ADD", "register:40f0:8", ["const:bafe98:8", "const:4:8"]]
- 00bafe98 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0e8c ["INT_ADD", "register:40f0:8", ["const:bb0e8c:8", "const:4:8"]]
+ 00bb0e8c ["CALL", null, ["callee:00c590f0:8"]]
- 00bafe98 bytes a2a00294
+ 00bb0e8c bytes 99a00294
~~~


<a id="compare-db76076d808c3df7e29742e748c7eb2a"></a>

### [`00bafedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafedc.md) → [`00bb0ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0ed0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfc0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df90.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baff74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafedc.md#insn-00baff74) · [`00baffbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafedc.md#insn-00baffbc)
- 新版 [`00bb0f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0ed0.md#insn-00bb0f68) · [`00bb0fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0ed0.md#insn-00bb0fb0)

~~~diff
- 00baff74 ["INT_ADD", "register:40f0:8", ["const:baff74:8", "const:4:8"]]
- 00baff74 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0f68 ["INT_ADD", "register:40f0:8", ["const:bb0f68:8", "const:4:8"]]
+ 00bb0f68 ["CALL", null, ["callee:00c590f0:8"]]
- 00baff74 bytes 6ba00294
+ 00bb0f68 bytes 62a00294
- 00baffbc ["INT_ADD", "register:40f0:8", ["const:baffbc:8", "const:4:8"]]
- 00baffbc ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb0fb0 ["INT_ADD", "register:40f0:8", ["const:bb0fb0:8", "const:4:8"]]
+ 00bb0fb0 ["CALL", null, ["callee:00c590f0:8"]]
- 00baffbc bytes 59a00294
+ 00bb0fb0 bytes 50a00294
~~~


<a id="compare-82709b8ecf6b160daf97d786fda37761"></a>

### [`00bafff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafff0.md) → [`00bb0fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0fe4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf90.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df60.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafff0.md#insn-00bb008c) · [`00bb00cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafff0.md#insn-00bb00cc)
- 新版 [`00bb1080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0fe4.md#insn-00bb1080) · [`00bb10c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0fe4.md#insn-00bb10c0)

~~~diff
- 00bb008c ["INT_ADD", "register:40f0:8", ["const:bb008c:8", "const:4:8"]]
- 00bb008c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb1080 ["INT_ADD", "register:40f0:8", ["const:bb1080:8", "const:4:8"]]
+ 00bb1080 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb008c bytes 25a00294
+ 00bb1080 bytes 1ca00294
- 00bb00cc ["INT_ADD", "register:40f0:8", ["const:bb00cc:8", "const:4:8"]]
- 00bb00cc ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb10c0 ["INT_ADD", "register:40f0:8", ["const:bb10c0:8", "const:4:8"]]
+ 00bb10c0 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb00cc bytes 15a00294
+ 00bb10c0 bytes 0ca00294
~~~


<a id="compare-cdfabe863c0436b876196b4d76c44642"></a>

### [`00bb0260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md) → [`00bb1254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1254.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_ite

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0b0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 1件 [`00c5e080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e080.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb02b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb02b0) · [`00bb02d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb02d4) · [`00bb0314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb0314)
- 新版 [`00bb12a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1254.md#insn-00bb12a4) · [`00bb12c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1254.md#insn-00bb12c8) · [`00bb1308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1254.md#insn-00bb1308)

~~~diff
- 00bb02b0 ["INT_ADD", "register:40f0:8", ["const:bb02b0:8", "const:4:8"]]
- 00bb02b0 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00bb12a4 ["INT_ADD", "register:40f0:8", ["const:bb12a4:8", "const:4:8"]]
+ 00bb12a4 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00bb02b0 bytes 9cad0294
+ 00bb12a4 bytes 93ad0294
- 00bb02d4 ["INT_ADD", "register:40f0:8", ["const:bb02d4:8", "const:4:8"]]
- 00bb02d4 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00bb12c8 ["INT_ADD", "register:40f0:8", ["const:bb12c8:8", "const:4:8"]]
+ 00bb12c8 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00bb02d4 bytes 93ad0294
+ 00bb12c8 bytes 8aad0294
- 00bb0314 ["INT_ADD", "register:40f0:8", ["const:bb0314:8", "const:4:8"]]
- 00bb0314 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb1308 ["INT_ADD", "register:40f0:8", ["const:bb1308:8", "const:4:8"]]
+ 00bb1308 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb0314 bytes 139f0294
+ 00bb1308 bytes 0a9f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750643946bdb4314bdface28e77b402c"></a>

### [`00bb0380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md) → [`00bb1374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1374.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d060.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5e030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e030.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md#insn-00bb0418) · [`00bb0460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md#insn-00bb0460)
- 新版 [`00bb140c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1374.md#insn-00bb140c) · [`00bb1454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1374.md#insn-00bb1454)

~~~diff
- 00bb0418 ["INT_ADD", "register:40f0:8", ["const:bb0418:8", "const:4:8"]]
- 00bb0418 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb140c ["INT_ADD", "register:40f0:8", ["const:bb140c:8", "const:4:8"]]
+ 00bb140c ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0418 bytes 429f0294
+ 00bb140c bytes 399f0294
- 00bb0460 ["INT_ADD", "register:40f0:8", ["const:bb0460:8", "const:4:8"]]
- 00bb0460 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb1454 ["INT_ADD", "register:40f0:8", ["const:bb1454:8", "const:4:8"]]
+ 00bb1454 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0460 bytes 309f0294
+ 00bb1454 bytes 279f0294
~~~


<a id="compare-b6222208e80614d1b09a8fa95e5bf033"></a>

### [`00bb0494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md) → [`00bb1488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1488.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf20.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5def0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5def0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md#insn-00bb0530) · [`00bb0570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md#insn-00bb0570)
- 新版 [`00bb1524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1488.md#insn-00bb1524) · [`00bb1564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1488.md#insn-00bb1564)

~~~diff
- 00bb0530 ["INT_ADD", "register:40f0:8", ["const:bb0530:8", "const:4:8"]]
- 00bb0530 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb1524 ["INT_ADD", "register:40f0:8", ["const:bb1524:8", "const:4:8"]]
+ 00bb1524 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0530 bytes fc9e0294
+ 00bb1524 bytes f39e0294
- 00bb0570 ["INT_ADD", "register:40f0:8", ["const:bb0570:8", "const:4:8"]]
- 00bb0570 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb1564 ["INT_ADD", "register:40f0:8", ["const:bb1564:8", "const:4:8"]]
+ 00bb1564 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0570 bytes ec9e0294
+ 00bb1564 bytes e39e0294
~~~


<a id="compare-5a54674caa20b3e8b20487f51a7ab746"></a>

### [`00bb05b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md) → [`00bb15a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb15a8.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0f0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0c0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb0634) · [`00bb064c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb064c) · [`00bb06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb06c8)
- 新版 [`00bb1628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb15a8.md#insn-00bb1628) · [`00bb1640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb15a8.md#insn-00bb1640) · [`00bb16bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb15a8.md#insn-00bb16bc)

~~~diff
- 00bb0634 ["INT_ADD", "register:40f0:8", ["const:bb0634:8", "const:4:8"]]
- 00bb0634 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb1628 ["INT_ADD", "register:40f0:8", ["const:bb1628:8", "const:4:8"]]
+ 00bb1628 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb0634 bytes 4b9e0294
+ 00bb1628 bytes 429e0294
- 00bb064c ["INT_ADD", "register:40f0:8", ["const:bb064c:8", "const:4:8"]]
- 00bb064c ["CALL", null, ["callee:00c5c650:8"]]
+ 00bb1640 ["INT_ADD", "register:40f0:8", ["const:bb1640:8", "const:4:8"]]
+ 00bb1640 ["CALL", null, ["callee:00c5c650:8"]]
- 00bb064c bytes 0dac0294
+ 00bb1640 bytes 04ac0294
- 00bb06c8 ["INT_ADD", "register:40f0:8", ["const:bb06c8:8", "const:4:8"]]
- 00bb06c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb16bc ["INT_ADD", "register:40f0:8", ["const:bb16bc:8", "const:4:8"]]
+ 00bb16bc ["CALL", null, ["callee:00c58f50:8"]]
- 00bb06c8 bytes 2e9e0294
+ 00bb16bc bytes 259e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c3d251c1591ac00919b5ae17ddb197"></a>

### [`00bb0704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0704.md) → [`00bb16f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb16f8.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__t

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf00.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5cef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cef0.md)
- 新版 呼出元 1件 [`00c5ded0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ded0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5dec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0704.md#insn-00bb0738) · [`00bb0754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0704.md#insn-00bb0754) · [`00bb0764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0704.md#insn-00bb0764)
- 新版 [`00bb172c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb16f8.md#insn-00bb172c) · [`00bb1748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb16f8.md#insn-00bb1748) · [`00bb1758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb16f8.md#insn-00bb1758)

~~~diff
- 00bb0738 ["INT_ADD", "register:40f0:8", ["const:bb0738:8", "const:4:8"]]
- 00bb0738 ["CALL", null, ["callee:00c5dec0:8"]]
+ 00bb172c ["INT_ADD", "register:40f0:8", ["const:bb172c:8", "const:4:8"]]
+ 00bb172c ["CALL", null, ["callee:00c5dec0:8"]]
- 00bb0738 bytes eeb10294
+ 00bb172c bytes e5b10294
- 00bb0754 ["INT_ADD", "register:40f0:8", ["const:bb0754:8", "const:4:8"]]
- 00bb0754 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb1748 ["INT_ADD", "register:40f0:8", ["const:bb1748:8", "const:4:8"]]
+ 00bb1748 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb0754 bytes 039e0294
+ 00bb1748 bytes fa9d0294
- 00bb0764 ["INT_ADD", "register:40f0:8", ["const:bb0764:8", "const:4:8"]]
- 00bb0764 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bb1758 ["INT_ADD", "register:40f0:8", ["const:bb1758:8", "const:4:8"]]
+ 00bb1758 ["CALL", null, ["callee:00c5c650:8"]]
- 00bb0764 bytes c7ab0294
+ 00bb1758 bytes beab0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a97b179329454f54e4fc8971b72aa3"></a>

### [`00bb07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md) → [`00bb17dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb17dc.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE12__find_equalIS2_EERPNS_16__tree_node_baseIPvEERPNS_15__

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cef0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dec0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md#insn-00bb0888) · [`00bb08c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md#insn-00bb08c8)
- 新版 [`00bb187c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb17dc.md#insn-00bb187c) · [`00bb18bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb17dc.md#insn-00bb18bc)

~~~diff
- 00bb0888 ["INT_ADD", "register:40f0:8", ["const:bb0888:8", "const:4:8"]]
- 00bb0888 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb187c ["INT_ADD", "register:40f0:8", ["const:bb187c:8", "const:4:8"]]
+ 00bb187c ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0888 bytes 269e0294
+ 00bb187c bytes 1d9e0294
- 00bb08c8 ["INT_ADD", "register:40f0:8", ["const:bb08c8:8", "const:4:8"]]
- 00bb08c8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb18bc ["INT_ADD", "register:40f0:8", ["const:bb18bc:8", "const:4:8"]]
+ 00bb18bc ["CALL", null, ["callee:00c590f0:8"]]
- 00bb08c8 bytes 169e0294
+ 00bb18bc bytes 0d9e0294
~~~


<a id="compare-beb13a2fbd565d7f65df52647ee79cb3"></a>

### [`00bb090c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb090c.md) → [`00bb1900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1900.md) _ZNSt6__ndk16__treeINS_12__value_typeImNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareImS8_NS_4lessImEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d070.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5e040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e040.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb09cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb090c.md#insn-00bb09cc) · [`00bb09dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb090c.md#insn-00bb09dc) · [`00bb09e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb090c.md#insn-00bb09e4)
- 新版 [`00bb19c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1900.md#insn-00bb19c0) · [`00bb19d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1900.md#insn-00bb19d0) · [`00bb19d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1900.md#insn-00bb19d8)

~~~diff
- 00bb09cc ["INT_ADD", "register:40f0:8", ["const:bb09cc:8", "const:4:8"]]
- 00bb09cc ["CALL", null, ["callee:00c5c670:8"]]
+ 00bb19c0 ["INT_ADD", "register:40f0:8", ["const:bb19c0:8", "const:4:8"]]
+ 00bb19c0 ["CALL", null, ["callee:00c5c670:8"]]
- 00bb09cc bytes 35ab0294
+ 00bb19c0 bytes 2cab0294
- 00bb09dc ["INT_ADD", "register:40f0:8", ["const:bb09dc:8", "const:4:8"]]
- 00bb09dc ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb19d0 ["INT_ADD", "register:40f0:8", ["const:bb19d0:8", "const:4:8"]]
+ 00bb19d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb09dc bytes 699d0294
+ 00bb19d0 bytes 609d0294
- 00bb09e4 ["INT_ADD", "register:40f0:8", ["const:bb09e4:8", "const:4:8"]]
- 00bb09e4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb19d8 ["INT_ADD", "register:40f0:8", ["const:bb19d8:8", "const:4:8"]]
+ 00bb19d8 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb09e4 bytes 679d0294
+ 00bb19d8 bytes 5e9d0294
~~~


<a id="compare-62967c5fb1771771c6cc0eb13aa64640"></a>

### [`00bb09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb09f8.md) → [`00bb19ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb19ec.md) FUN_00bb19ec

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8e178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb10.md)
- 新版 呼出元 1件 [`00b8f16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb09f8.md#insn-00bb0a3c) · [`00bb0a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb09f8.md#insn-00bb0a54) · [`00bb0ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb09f8.md#insn-00bb0ab0)
- 新版 [`00bb1a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb19ec.md#insn-00bb1a30) · [`00bb1a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb19ec.md#insn-00bb1a48) · [`00bb1aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb19ec.md#insn-00bb1aa4)

~~~diff
- 00bb0a3c ["INT_ADD", "register:40f0:8", ["const:bb0a3c:8", "const:4:8"]]
- 00bb0a3c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00bb1a30 ["INT_ADD", "register:40f0:8", ["const:bb1a30:8", "const:4:8"]]
+ 00bb1a30 ["CALL", null, ["callee:00c5dae0:8"]]
- 00bb0a3c bytes 35b00294
+ 00bb1a30 bytes 2cb00294
- 00bb0a54 ["INT_ADD", "register:40f0:8", ["const:bb0a54:8", "const:4:8"]]
- 00bb0a54 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00bb1a48 ["INT_ADD", "register:40f0:8", ["const:bb1a48:8", "const:4:8"]]
+ 00bb1a48 ["CALL", null, ["callee:00c5dae0:8"]]
- 00bb0a54 bytes 2fb00294
+ 00bb1a48 bytes 26b00294
- 00bb0ab0 ["INT_ADD", "register:40f0:8", ["const:bb0ab0:8", "const:4:8"]]
- 00bb0ab0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb1aa4 ["INT_ADD", "register:40f0:8", ["const:bb1aa4:8", "const:4:8"]]
+ 00bb1aa4 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb0ab0 bytes 9c9d0294
+ 00bb1aa4 bytes 939d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc746f79412504f272f047499c8a4d10"></a>

### [`00bb1044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md) → [`00bb2038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2038.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e160.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb1078) · [`00bb1090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb1090) · [`00bb10d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb10d4)
- 新版 [`00bb206c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2038.md#insn-00bb206c) · [`00bb2084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2038.md#insn-00bb2084) · [`00bb20c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2038.md#insn-00bb20c8)

~~~diff
- 00bb1078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1078 ["INT_ADD", "register:40f0:8", ["const:bb1078:8", "const:4:8"]]
- 00bb1078 ["CALLIND", null, ["register:0:8"]]
+ 00bb206c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb206c ["INT_ADD", "register:40f0:8", ["const:bb206c:8", "const:4:8"]]
+ 00bb206c ["CALLIND", null, ["register:0:8"]]
- 00bb1078 bytes 00013fd6
+ 00bb206c bytes 00013fd6
- 00bb1090 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1090 ["INT_ADD", "register:40f0:8", ["const:bb1090:8", "const:4:8"]]
- 00bb1090 ["CALLIND", null, ["register:0:8"]]
+ 00bb2084 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2084 ["INT_ADD", "register:40f0:8", ["const:bb2084:8", "const:4:8"]]
+ 00bb2084 ["CALLIND", null, ["register:0:8"]]
- 00bb1090 bytes 20013fd6
+ 00bb2084 bytes 20013fd6
- 00bb10d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb10d4 ["INT_ADD", "register:40f0:8", ["const:bb10d4:8", "const:4:8"]]
- 00bb10d4 ["CALLIND", null, ["register:0:8"]]
+ 00bb20c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb20c8 ["INT_ADD", "register:40f0:8", ["const:bb20c8:8", "const:4:8"]]
+ 00bb20c8 ["CALLIND", null, ["register:0:8"]]
- 00bb10d4 bytes 00013fd6
+ 00bb20c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7133c17e96a81331856ae354f95b6785"></a>

### [`00bb11c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md) → [`00bb21bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md) FUN_00bb21bc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bb0b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md) [`00bb142c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md) · 呼出先 1件 [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md)
- 新版 呼出元 2件 [`00bb1b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1b20.md) [`00bb2420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2420.md) · 呼出先 1件 [`00c5e160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb11fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb11fc) · [`00bb1214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb1214) · [`00bb1238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb1238)
- 新版 [`00bb21f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md#insn-00bb21f0) · [`00bb2208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md#insn-00bb2208) · [`00bb222c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md#insn-00bb222c)

~~~diff
- 00bb11fc ["INT_ADD", "register:40f0:8", ["const:bb11fc:8", "const:4:8"]]
- 00bb11fc ["CALL", null, ["callee:00c5e160:8"]]
+ 00bb21f0 ["INT_ADD", "register:40f0:8", ["const:bb21f0:8", "const:4:8"]]
+ 00bb21f0 ["CALL", null, ["callee:00c5e160:8"]]
- 00bb11fc bytes e5af0294
+ 00bb21f0 bytes dcaf0294
- 00bb1214 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1214 ["INT_ADD", "register:40f0:8", ["const:bb1214:8", "const:4:8"]]
- 00bb1214 ["CALLIND", null, ["register:0:8"]]
+ 00bb2208 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2208 ["INT_ADD", "register:40f0:8", ["const:bb2208:8", "const:4:8"]]
+ 00bb2208 ["CALLIND", null, ["register:0:8"]]
- 00bb1214 bytes 20013fd6
+ 00bb2208 bytes 20013fd6
- 00bb1238 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1238 ["INT_ADD", "register:40f0:8", ["const:bb1238:8", "const:4:8"]]
- 00bb1238 ["CALLIND", null, ["register:0:8"]]
+ 00bb222c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb222c ["INT_ADD", "register:40f0:8", ["const:bb222c:8", "const:4:8"]]
+ 00bb222c ["CALLIND", null, ["register:0:8"]]
- 00bb1238 bytes 00013fd6
+ 00bb222c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ab1394d049fb7dfa0ff06d0296f5244"></a>

### [`00bb12d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb12d0.md) → [`00bb22c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb22c4.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ccd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccd0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dca0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb12d0.md#insn-00bb1300) · [`00bb131c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb12d0.md#insn-00bb131c) · [`00bb1358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb12d0.md#insn-00bb1358)
- 新版 [`00bb22f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb22c4.md#insn-00bb22f4) · [`00bb2310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb22c4.md#insn-00bb2310) · [`00bb234c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb22c4.md#insn-00bb234c)

~~~diff
- 00bb1300 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1300 ["INT_ADD", "register:40f0:8", ["const:bb1300:8", "const:4:8"]]
- 00bb1300 ["CALLIND", null, ["register:0:8"]]
+ 00bb22f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb22f4 ["INT_ADD", "register:40f0:8", ["const:bb22f4:8", "const:4:8"]]
+ 00bb22f4 ["CALLIND", null, ["register:0:8"]]
- 00bb1300 bytes 20013fd6
+ 00bb22f4 bytes 20013fd6
- 00bb131c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb131c ["INT_ADD", "register:40f0:8", ["const:bb131c:8", "const:4:8"]]
- 00bb131c ["CALLIND", null, ["register:0:8"]]
+ 00bb2310 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2310 ["INT_ADD", "register:40f0:8", ["const:bb2310:8", "const:4:8"]]
+ 00bb2310 ["CALLIND", null, ["register:0:8"]]
- 00bb131c bytes 20013fd6
+ 00bb2310 bytes 20013fd6
- 00bb1358 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1358 ["INT_ADD", "register:40f0:8", ["const:bb1358:8", "const:4:8"]]
- 00bb1358 ["CALLIND", null, ["register:0:8"]]
+ 00bb234c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb234c ["INT_ADD", "register:40f0:8", ["const:bb234c:8", "const:4:8"]]
+ 00bb234c ["CALLIND", null, ["register:0:8"]]
- 00bb1358 bytes 00013fd6
+ 00bb234c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b2d426c1116748fd6a08e86cf25472"></a>

### [`00bb16dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md) → [`00bb26d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb26d0.md) FUN_00bb26d0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8e178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb10.md)
- 新版 呼出元 1件 [`00b8f16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md#insn-00bb1720) · [`00bb1738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md#insn-00bb1738) · [`00bb1794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md#insn-00bb1794)
- 新版 [`00bb2714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb26d0.md#insn-00bb2714) · [`00bb272c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb26d0.md#insn-00bb272c) · [`00bb2788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb26d0.md#insn-00bb2788)

~~~diff
- 00bb1720 ["INT_ADD", "register:40f0:8", ["const:bb1720:8", "const:4:8"]]
- 00bb1720 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00bb2714 ["INT_ADD", "register:40f0:8", ["const:bb2714:8", "const:4:8"]]
+ 00bb2714 ["CALL", null, ["callee:00c5dae0:8"]]
- 00bb1720 bytes fcac0294
+ 00bb2714 bytes f3ac0294
- 00bb1738 ["INT_ADD", "register:40f0:8", ["const:bb1738:8", "const:4:8"]]
- 00bb1738 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00bb272c ["INT_ADD", "register:40f0:8", ["const:bb272c:8", "const:4:8"]]
+ 00bb272c ["CALL", null, ["callee:00c5dae0:8"]]
- 00bb1738 bytes f6ac0294
+ 00bb272c bytes edac0294
- 00bb1794 ["INT_ADD", "register:40f0:8", ["const:bb1794:8", "const:4:8"]]
- 00bb1794 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb2788 ["INT_ADD", "register:40f0:8", ["const:bb2788:8", "const:4:8"]]
+ 00bb2788 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb1794 bytes 639a0294
+ 00bb2788 bytes 5a9a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfdb337b097275000879d97b6466018"></a>

### [`00bb1d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1d28.md) → [`00bb2d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2d1c.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d170.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e140.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1d28.md#insn-00bb1d5c) · [`00bb1d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1d28.md#insn-00bb1d74) · [`00bb1db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1d28.md#insn-00bb1db8)
- 新版 [`00bb2d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2d1c.md#insn-00bb2d50) · [`00bb2d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2d1c.md#insn-00bb2d68) · [`00bb2dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2d1c.md#insn-00bb2dac)

~~~diff
- 00bb1d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1d5c ["INT_ADD", "register:40f0:8", ["const:bb1d5c:8", "const:4:8"]]
- 00bb1d5c ["CALLIND", null, ["register:0:8"]]
+ 00bb2d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb2d50 ["INT_ADD", "register:40f0:8", ["const:bb2d50:8", "const:4:8"]]
+ 00bb2d50 ["CALLIND", null, ["register:0:8"]]
- 00bb1d5c bytes 00013fd6
+ 00bb2d50 bytes 00013fd6
- 00bb1d74 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1d74 ["INT_ADD", "register:40f0:8", ["const:bb1d74:8", "const:4:8"]]
- 00bb1d74 ["CALLIND", null, ["register:0:8"]]
+ 00bb2d68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2d68 ["INT_ADD", "register:40f0:8", ["const:bb2d68:8", "const:4:8"]]
+ 00bb2d68 ["CALLIND", null, ["register:0:8"]]
- 00bb1d74 bytes 20013fd6
+ 00bb2d68 bytes 20013fd6
- 00bb1db8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1db8 ["INT_ADD", "register:40f0:8", ["const:bb1db8:8", "const:4:8"]]
- 00bb1db8 ["CALLIND", null, ["register:0:8"]]
+ 00bb2dac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb2dac ["INT_ADD", "register:40f0:8", ["const:bb2dac:8", "const:4:8"]]
+ 00bb2dac ["CALLIND", null, ["register:0:8"]]
- 00bb1db8 bytes 00013fd6
+ 00bb2dac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28efa0be6dc68d9a6652ab0cda67bfc9"></a>

### [`00bb1eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md) → [`00bb2ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md) FUN_00bb2ea0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bb1810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1810.md) [`00bb2110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2110.md) · 呼出先 1件 [`00c5d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d170.md)
- 新版 呼出元 2件 [`00bb2804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2804.md) [`00bb3104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3104.md) · 呼出先 1件 [`00c5e140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md#insn-00bb1ee0) · [`00bb1ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md#insn-00bb1ef8) · [`00bb1f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md#insn-00bb1f1c)
- 新版 [`00bb2ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md#insn-00bb2ed4) · [`00bb2eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md#insn-00bb2eec) · [`00bb2f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md#insn-00bb2f10)

~~~diff
- 00bb1ee0 ["INT_ADD", "register:40f0:8", ["const:bb1ee0:8", "const:4:8"]]
- 00bb1ee0 ["CALL", null, ["callee:00c5e140:8"]]
+ 00bb2ed4 ["INT_ADD", "register:40f0:8", ["const:bb2ed4:8", "const:4:8"]]
+ 00bb2ed4 ["CALL", null, ["callee:00c5e140:8"]]
- 00bb1ee0 bytes a4ac0294
+ 00bb2ed4 bytes 9bac0294
- 00bb1ef8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1ef8 ["INT_ADD", "register:40f0:8", ["const:bb1ef8:8", "const:4:8"]]
- 00bb1ef8 ["CALLIND", null, ["register:0:8"]]
+ 00bb2eec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2eec ["INT_ADD", "register:40f0:8", ["const:bb2eec:8", "const:4:8"]]
+ 00bb2eec ["CALLIND", null, ["register:0:8"]]
- 00bb1ef8 bytes 20013fd6
+ 00bb2eec bytes 20013fd6
- 00bb1f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1f1c ["INT_ADD", "register:40f0:8", ["const:bb1f1c:8", "const:4:8"]]
- 00bb1f1c ["CALLIND", null, ["register:0:8"]]
+ 00bb2f10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb2f10 ["INT_ADD", "register:40f0:8", ["const:bb2f10:8", "const:4:8"]]
+ 00bb2f10 ["CALLIND", null, ["register:0:8"]]
- 00bb1f1c bytes 00013fd6
+ 00bb2f10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa7bd733cd8cb7800deb970ab2f0b78"></a>

### [`00bb1fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1fb4.md) → [`00bb2fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2fa8.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc80.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1fb4.md#insn-00bb1fe4) · [`00bb2000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1fb4.md#insn-00bb2000) · [`00bb203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1fb4.md#insn-00bb203c)
- 新版 [`00bb2fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2fa8.md#insn-00bb2fd8) · [`00bb2ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2fa8.md#insn-00bb2ff4) · [`00bb3030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2fa8.md#insn-00bb3030)

~~~diff
- 00bb1fe4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1fe4 ["INT_ADD", "register:40f0:8", ["const:bb1fe4:8", "const:4:8"]]
- 00bb1fe4 ["CALLIND", null, ["register:0:8"]]
+ 00bb2fd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2fd8 ["INT_ADD", "register:40f0:8", ["const:bb2fd8:8", "const:4:8"]]
+ 00bb2fd8 ["CALLIND", null, ["register:0:8"]]
- 00bb1fe4 bytes 20013fd6
+ 00bb2fd8 bytes 20013fd6
- 00bb2000 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb2000 ["INT_ADD", "register:40f0:8", ["const:bb2000:8", "const:4:8"]]
- 00bb2000 ["CALLIND", null, ["register:0:8"]]
+ 00bb2ff4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb2ff4 ["INT_ADD", "register:40f0:8", ["const:bb2ff4:8", "const:4:8"]]
+ 00bb2ff4 ["CALLIND", null, ["register:0:8"]]
- 00bb2000 bytes 20013fd6
+ 00bb2ff4 bytes 20013fd6
- 00bb203c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb203c ["INT_ADD", "register:40f0:8", ["const:bb203c:8", "const:4:8"]]
- 00bb203c ["CALLIND", null, ["register:0:8"]]
+ 00bb3030 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb3030 ["INT_ADD", "register:40f0:8", ["const:bb3030:8", "const:4:8"]]
+ 00bb3030 ["CALLIND", null, ["register:0:8"]]
- 00bb203c bytes 00013fd6
+ 00bb3030 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07fac69d41a25d4a63f369fa70b5183c"></a>

### [`00bb23c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb23c0.md) → [`00bb33b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb33b4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE21CreateVectorOfStringsINSt6__ndk111__wrap_iterIPKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c390.md) · 呼出先 4件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md) [`00c5c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c350.md) [`00c5c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c370.md)
- 新版 呼出元 1件 [`00c5d360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d360.md) · 呼出先 4件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md) [`00c5d320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d320.md) [`00c5d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb23c0.md#insn-00bb2418) · [`00bb245c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb23c0.md#insn-00bb245c) · [`00bb2480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb23c0.md#insn-00bb2480)
- 新版 [`00bb340c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb33b4.md#insn-00bb340c) · [`00bb3450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb33b4.md#insn-00bb3450) · [`00bb3474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb33b4.md#insn-00bb3474)

~~~diff
- 00bb2418 ["INT_ADD", "register:40f0:8", ["const:bb2418:8", "const:4:8"]]
- 00bb2418 ["CALL", null, ["callee:00c5d240:8"]]
+ 00bb340c ["INT_ADD", "register:40f0:8", ["const:bb340c:8", "const:4:8"]]
+ 00bb340c ["CALL", null, ["callee:00c5d240:8"]]
- 00bb2418 bytes 96a70294
+ 00bb340c bytes 8da70294
- 00bb245c ["INT_ADD", "register:40f0:8", ["const:bb245c:8", "const:4:8"]]
- 00bb245c ["CALL", null, ["callee:00c5d340:8"]]
+ 00bb3450 ["INT_ADD", "register:40f0:8", ["const:bb3450:8", "const:4:8"]]
+ 00bb3450 ["CALL", null, ["callee:00c5d340:8"]]
- 00bb245c bytes c5a70294
+ 00bb3450 bytes bca70294
- 00bb2480 ["INT_ADD", "register:40f0:8", ["const:bb2480:8", "const:4:8"]]
- 00bb2480 ["CALL", null, ["callee:00c5d240:8"]]
+ 00bb3474 ["INT_ADD", "register:40f0:8", ["const:bb3474:8", "const:4:8"]]
+ 00bb3474 ["CALL", null, ["callee:00c5d240:8"]]
- 00bb2480 bytes 7ca70294
+ 00bb3474 bytes 73a70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5c4932a6390c92242b68f5c4ceb3a1"></a>

### [`00bb2590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2590.md) → [`00bb3584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3584.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d040.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d040.md)
- 新版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e010.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb25ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2590.md#insn-00bb25ac) · [`00bb25b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2590.md#insn-00bb25b8) · [`00bb25c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2590.md#insn-00bb25c8)
- 新版 [`00bb35a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3584.md#insn-00bb35a0) · [`00bb35ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3584.md#insn-00bb35ac) · [`00bb35bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3584.md#insn-00bb35bc)

~~~diff
- 00bb25ac ["INT_ADD", "register:40f0:8", ["const:bb25ac:8", "const:4:8"]]
- 00bb25ac ["CALL", null, ["callee:00c5e010:8"]]
+ 00bb35a0 ["INT_ADD", "register:40f0:8", ["const:bb35a0:8", "const:4:8"]]
+ 00bb35a0 ["CALL", null, ["callee:00c5e010:8"]]
- 00bb25ac bytes a5aa0294
+ 00bb35a0 bytes 9caa0294
- 00bb25b8 ["INT_ADD", "register:40f0:8", ["const:bb25b8:8", "const:4:8"]]
- 00bb25b8 ["CALL", null, ["callee:00c5e010:8"]]
+ 00bb35ac ["INT_ADD", "register:40f0:8", ["const:bb35ac:8", "const:4:8"]]
+ 00bb35ac ["CALL", null, ["callee:00c5e010:8"]]
- 00bb25b8 bytes a2aa0294
+ 00bb35ac bytes 99aa0294
- 00bb25c8 ["INT_ADD", "register:40f0:8", ["const:bb25c8:8", "const:4:8"]]
- 00bb25c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb35bc ["INT_ADD", "register:40f0:8", ["const:bb35bc:8", "const:4:8"]]
+ 00bb35bc ["CALL", null, ["callee:00c58f50:8"]]
- 00bb25c8 bytes 6e960294
+ 00bb35bc bytes 65960294
~~~


<a id="compare-6bda918e587e1e9c4e71e78ab7cc6e73"></a>

### [`00bb25e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb25e0.md) → [`00bb35d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb35d4.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb50.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db20.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb25e0.md#insn-00bb2678) · [`00bb26c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb25e0.md#insn-00bb26c0)
- 新版 [`00bb366c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb35d4.md#insn-00bb366c) · [`00bb36b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb35d4.md#insn-00bb36b4)

~~~diff
- 00bb2678 ["INT_ADD", "register:40f0:8", ["const:bb2678:8", "const:4:8"]]
- 00bb2678 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb366c ["INT_ADD", "register:40f0:8", ["const:bb366c:8", "const:4:8"]]
+ 00bb366c ["CALL", null, ["callee:00c590f0:8"]]
- 00bb2678 bytes aa960294
+ 00bb366c bytes a1960294
- 00bb26c0 ["INT_ADD", "register:40f0:8", ["const:bb26c0:8", "const:4:8"]]
- 00bb26c0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bb36b4 ["INT_ADD", "register:40f0:8", ["const:bb36b4:8", "const:4:8"]]
+ 00bb36b4 ["CALL", null, ["callee:00c590f0:8"]]
- 00bb26c0 bytes 98960294
+ 00bb36b4 bytes 8f960294
~~~


<a id="compare-17510d894dde441f3cffa4136464abb6"></a>

### [`00bb26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb26f4.md) → [`00bb36e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb36e8.md) _ZNSt6__ndk16__treeIPN11flatbuffers8FieldDefENS_4lessIS3_EENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0a0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0a0.md)
- 新版 呼出元 1件 [`00c5e070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e070.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb26f4.md#insn-00bb2710) · [`00bb271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb26f4.md#insn-00bb271c)
- 新版 [`00bb3704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb36e8.md#insn-00bb3704) · [`00bb3710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb36e8.md#insn-00bb3710)

~~~diff
- 00bb2710 ["INT_ADD", "register:40f0:8", ["const:bb2710:8", "const:4:8"]]
- 00bb2710 ["CALL", null, ["callee:00c5e070:8"]]
+ 00bb3704 ["INT_ADD", "register:40f0:8", ["const:bb3704:8", "const:4:8"]]
+ 00bb3704 ["CALL", null, ["callee:00c5e070:8"]]
- 00bb2710 bytes 64aa0294
+ 00bb3704 bytes 5baa0294
- 00bb271c ["INT_ADD", "register:40f0:8", ["const:bb271c:8", "const:4:8"]]
- 00bb271c ["CALL", null, ["callee:00c5e070:8"]]
+ 00bb3710 ["INT_ADD", "register:40f0:8", ["const:bb3710:8", "const:4:8"]]
+ 00bb3710 ["CALL", null, ["callee:00c5e070:8"]]
- 00bb271c bytes 61aa0294
+ 00bb3710 bytes 58aa0294
~~~


<a id="compare-5ebf25b9214587c0b6830952b5f85473"></a>

### [`00bb2750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2750.md) → [`00bb3744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3744.md) _ZN11flatbuffers9DirExistsEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2750.md#insn-00bb2760)
- 新版 [`00bb3754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3744.md#insn-00bb3754)

~~~diff
- 00bb2760 ["INT_ADD", "register:40f0:8", ["const:bb2760:8", "const:4:8"]]
- 00bb2760 ["CALL", null, ["callee:00c5a900:8"]]
+ 00bb3754 ["INT_ADD", "register:40f0:8", ["const:bb3754:8", "const:4:8"]]
+ 00bb3754 ["CALL", null, ["callee:00c5a900:8"]]
- 00bb2760 bytes 749c0294
+ 00bb3754 bytes 6b9c0294
~~~


<a id="compare-62a0981f3907199d5a3b840a374590f4"></a>

### [`00bb2e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2e80.md) → [`00bb3e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3e74.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d40.md) · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)
- 新版 呼出元 1件 [`00c59d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d10.md) · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md) [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2e80.md#insn-00bb2ecc) · [`00bb2eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2e80.md#insn-00bb2eec) · [`00bb2f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2e80.md#insn-00bb2f0c)
- 新版 [`00bb3ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3e74.md#insn-00bb3ec0) · [`00bb3ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3e74.md#insn-00bb3ee0) · [`00bb3f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3e74.md#insn-00bb3f00)

~~~diff
- 00bb2ecc ["INT_ADD", "register:40f0:8", ["const:bb2ecc:8", "const:4:8"]]
- 00bb2ecc ["CALL", null, ["callee:00c5e190:8"]]
+ 00bb3ec0 ["INT_ADD", "register:40f0:8", ["const:bb3ec0:8", "const:4:8"]]
+ 00bb3ec0 ["CALL", null, ["callee:00c5e190:8"]]
- 00bb2ecc bytes bda80294
+ 00bb3ec0 bytes b4a80294
- 00bb2eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb2eec ["INT_ADD", "register:40f0:8", ["const:bb2eec:8", "const:4:8"]]
- 00bb2eec ["CALLIND", null, ["register:0:8"]]
+ 00bb3ee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb3ee0 ["INT_ADD", "register:40f0:8", ["const:bb3ee0:8", "const:4:8"]]
+ 00bb3ee0 ["CALLIND", null, ["register:0:8"]]
- 00bb2eec bytes 00013fd6
+ 00bb3ee0 bytes 00013fd6
- 00bb2f0c ["INT_ADD", "register:40f0:8", ["const:bb2f0c:8", "const:4:8"]]
- 00bb2f0c ["CALL", null, ["callee:00c59340:8"]]
+ 00bb3f00 ["INT_ADD", "register:40f0:8", ["const:bb3f00:8", "const:4:8"]]
+ 00bb3f00 ["CALL", null, ["callee:00c59340:8"]]
- 00bb2f0c bytes 19950294
+ 00bb3f00 bytes 10950294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b625f9fa69ef34427a628e66a1f4aaac"></a>

### [`00bb31c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb31c8.md) → [`00bb41bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb41bc.md) _ZN11flatbuffers11StripPrefixERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c890.md) [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb320c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb31c8.md#insn-00bb320c)
- 新版 [`00bb4200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb41bc.md#insn-00bb4200)

~~~diff
- 00bb320c ["INT_ADD", "register:40f0:8", ["const:bb320c:8", "const:4:8"]]
- 00bb320c ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00bb4200 ["INT_ADD", "register:40f0:8", ["const:bb4200:8", "const:4:8"]]
+ 00bb4200 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00bb320c bytes fda70294
+ 00bb4200 bytes f4a70294
~~~


<a id="compare-4fad0446ee804e19592e822615ba35da"></a>

### [`00bb3250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3250.md) → [`00bb4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4244.md) _ZN11flatbuffers18ConCatPathFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c810.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7e0.md) · 呼出先 4件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb3270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3250.md#insn-00bb3270) · [`00bb3304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3250.md#insn-00bb3304) · [`00bb3354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3250.md#insn-00bb3354)
- 新版 [`00bb4264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4244.md#insn-00bb4264) · [`00bb42f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4244.md#insn-00bb42f8) · [`00bb4348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4244.md#insn-00bb4348)

~~~diff
- 00bb3270 ["INT_ADD", "register:40f0:8", ["const:bb3270:8", "const:4:8"]]
- 00bb3270 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bb4264 ["INT_ADD", "register:40f0:8", ["const:bb4264:8", "const:4:8"]]
+ 00bb4264 ["CALL", null, ["callee:00c5c650:8"]]
- 00bb3270 bytes 04a10294
+ 00bb4264 bytes fba00294
- 00bb3304 ["INT_ADD", "register:40f0:8", ["const:bb3304:8", "const:4:8"]]
- 00bb3304 ["CALL", null, ["callee:00c5b980:8"]]
+ 00bb42f8 ["INT_ADD", "register:40f0:8", ["const:bb42f8:8", "const:4:8"]]
+ 00bb42f8 ["CALL", null, ["callee:00c5b980:8"]]
- 00bb3304 bytes ab9d0294
+ 00bb42f8 bytes a29d0294
- 00bb3354 ["INT_ADD", "register:40f0:8", ["const:bb3354:8", "const:4:8"]]
- 00bb3354 ["CALL", null, ["callee:00c59020:8"]]
+ 00bb4348 ["INT_ADD", "register:40f0:8", ["const:bb4348:8", "const:4:8"]]
+ 00bb4348 ["CALL", null, ["callee:00c59020:8"]]
- 00bb3354 bytes 3f930294
+ 00bb4348 bytes 36930294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-681723e7662c172b0905ad6e93fc8543"></a>

### [`00bb33e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb33e0.md) → [`00bb43d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb43d4.md) _ZN11flatbuffers9PosixPathEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c940.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5d910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d910.md) · 呼出先 1件 [`00c5c660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb33f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb33e0.md#insn-00bb33f8)
- 新版 [`00bb43ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb43d4.md#insn-00bb43ec)

~~~diff
- 00bb33f8 ["INT_ADD", "register:40f0:8", ["const:bb33f8:8", "const:4:8"]]
- 00bb33f8 ["CALL", null, ["callee:00c5c660:8"]]
+ 00bb43ec ["INT_ADD", "register:40f0:8", ["const:bb43ec:8", "const:4:8"]]
+ 00bb43ec ["CALL", null, ["callee:00c5c660:8"]]
- 00bb33f8 bytes a6a00294
+ 00bb43ec bytes 9da00294
~~~


<a id="compare-9eb5dbad5331a2579b1225f114a54c32"></a>

### [`00bb3534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3534.md) → [`00bb4528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4528.md) _ZN11flatbuffers9PosixPathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb3558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3534.md#insn-00bb3558)
- 新版 [`00bb454c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4528.md#insn-00bb454c)

~~~diff
- 00bb3558 ["INT_ADD", "register:40f0:8", ["const:bb3558:8", "const:4:8"]]
- 00bb3558 ["CALL", null, ["callee:00c5c660:8"]]
+ 00bb454c ["INT_ADD", "register:40f0:8", ["const:bb454c:8", "const:4:8"]]
+ 00bb454c ["CALL", null, ["callee:00c5c660:8"]]
- 00bb3558 bytes 4ea00294
+ 00bb454c bytes 45a00294
~~~


<a id="compare-7ae23b8d41f1280decf5a79f7de0328b"></a>

### [`00bb37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb37b8.md) → [`00bb47ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb47ac.md) _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7f0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7c0.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb37f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb37b8.md#insn-00bb37f4) · [`00bb380c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb37b8.md#insn-00bb380c) · [`00bb381c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb37b8.md#insn-00bb381c)
- 新版 [`00bb47e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb47ac.md#insn-00bb47e8) · [`00bb4800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb47ac.md#insn-00bb4800) · [`00bb4810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb47ac.md#insn-00bb4810)

~~~diff
- 00bb37f4 ["INT_ADD", "register:40f0:8", ["const:bb37f4:8", "const:4:8"]]
- 00bb37f4 ["CALL", null, ["callee:00c5e2d0:8"]]
+ 00bb47e8 ["INT_ADD", "register:40f0:8", ["const:bb47e8:8", "const:4:8"]]
+ 00bb47e8 ["CALL", null, ["callee:00c5e2d0:8"]]
- 00bb37f4 bytes c3a60294
+ 00bb47e8 bytes baa60294
- 00bb380c ["INT_ADD", "register:40f0:8", ["const:bb380c:8", "const:4:8"]]
- 00bb380c ["CALL", null, ["callee:00c59080:8"]]
+ 00bb4800 ["INT_ADD", "register:40f0:8", ["const:bb4800:8", "const:4:8"]]
+ 00bb4800 ["CALL", null, ["callee:00c59080:8"]]
- 00bb380c bytes 29920294
+ 00bb4800 bytes 20920294
- 00bb381c ["INT_ADD", "register:40f0:8", ["const:bb381c:8", "const:4:8"]]
- 00bb381c ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb4810 ["INT_ADD", "register:40f0:8", ["const:bb4810:8", "const:4:8"]]
+ 00bb4810 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb381c bytes 599e0294
+ 00bb4810 bytes 509e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5e35c9d638b38117bb52dce7c5a7f9"></a>

### [`00bb3eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3eb4.md) → [`00bb4ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4ea8.md) _ZN11flatbuffers19SetGlobalTestLocaleEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb3ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3eb4.md#insn-00bb3ed8) · [`00bb3ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3eb4.md#insn-00bb3ef0) · [`00bb3f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3eb4.md#insn-00bb3f2c)
- 新版 [`00bb4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4ea8.md#insn-00bb4ecc) · [`00bb4ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4ea8.md#insn-00bb4ee4) · [`00bb4f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4ea8.md#insn-00bb4f20)

~~~diff
- 00bb3ed8 ["INT_ADD", "register:40f0:8", ["const:bb3ed8:8", "const:4:8"]]
- 00bb3ed8 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bb4ecc ["INT_ADD", "register:40f0:8", ["const:bb4ecc:8", "const:4:8"]]
+ 00bb4ecc ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bb3ed8 bytes 0ea50294
+ 00bb4ecc bytes 05a50294
- 00bb3ef0 ["INT_ADD", "register:40f0:8", ["const:bb3ef0:8", "const:4:8"]]
- 00bb3ef0 ["CALL", null, ["callee:00c59080:8"]]
+ 00bb4ee4 ["INT_ADD", "register:40f0:8", ["const:bb4ee4:8", "const:4:8"]]
+ 00bb4ee4 ["CALL", null, ["callee:00c59080:8"]]
- 00bb3ef0 bytes 70900294
+ 00bb4ee4 bytes 67900294
- 00bb3f2c ["INT_ADD", "register:40f0:8", ["const:bb3f2c:8", "const:4:8"]]
- 00bb3f2c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb4f20 ["INT_ADD", "register:40f0:8", ["const:bb4f20:8", "const:4:8"]]
+ 00bb4f20 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb3f2c bytes 0d900294
+ 00bb4f20 bytes 04900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa9661cc69c1af472fe8b9541cfb736"></a>

### [`00bb3fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3fb4.md) → [`00bb4fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4fa8.md) _ZN11flatbuffers23ReadEnvironmentVariableEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c59970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59970.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5a940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb3fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3fb4.md#insn-00bb3fd0) · [`00bb3fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3fb4.md#insn-00bb3fe8) · [`00bb4024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3fb4.md#insn-00bb4024)
- 新版 [`00bb4fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4fa8.md#insn-00bb4fc4) · [`00bb4fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4fa8.md#insn-00bb4fdc) · [`00bb5018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4fa8.md#insn-00bb5018)

~~~diff
- 00bb3fd0 ["INT_ADD", "register:40f0:8", ["const:bb3fd0:8", "const:4:8"]]
- 00bb3fd0 ["CALL", null, ["callee:00c5a940:8"]]
+ 00bb4fc4 ["INT_ADD", "register:40f0:8", ["const:bb4fc4:8", "const:4:8"]]
+ 00bb4fc4 ["CALL", null, ["callee:00c5a940:8"]]
- 00bb3fd0 bytes 68960294
+ 00bb4fc4 bytes 5f960294
- 00bb3fe8 ["INT_ADD", "register:40f0:8", ["const:bb3fe8:8", "const:4:8"]]
- 00bb3fe8 ["CALL", null, ["callee:00c59080:8"]]
+ 00bb4fdc ["INT_ADD", "register:40f0:8", ["const:bb4fdc:8", "const:4:8"]]
+ 00bb4fdc ["CALL", null, ["callee:00c59080:8"]]
- 00bb3fe8 bytes 32900294
+ 00bb4fdc bytes 29900294
- 00bb4024 ["INT_ADD", "register:40f0:8", ["const:bb4024:8", "const:4:8"]]
- 00bb4024 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb5018 ["INT_ADD", "register:40f0:8", ["const:bb5018:8", "const:4:8"]]
+ 00bb5018 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb4024 bytes cf8f0294
+ 00bb5018 bytes c68f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71784b5832003ff84c2c6c7e9eff8031"></a>

### [`00bb4e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb4e20.md) → [`00bb5e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb5e14.md) FUN_00bb5e14

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) · 呼出先 3件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d320.md) [`00c5d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d330.md)
- 新版 呼出元 1件 [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) · 呼出先 3件 [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5e2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2f0.md) [`00c5e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb4efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb4e20.md#insn-00bb4efc) · [`00bb4f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb4e20.md#insn-00bb4f98) · [`00bb4fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb4e20.md#insn-00bb4fb8)
- 新版 [`00bb5ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb5e14.md#insn-00bb5ef0) · [`00bb5f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb5e14.md#insn-00bb5f8c) · [`00bb5fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb5e14.md#insn-00bb5fac)

~~~diff
- 00bb4efc ["INT_ADD", "register:40f0:8", ["const:bb4efc:8", "const:4:8"]]
- 00bb4efc ["CALL", null, ["callee:00c5e300:8"]]
+ 00bb5ef0 ["INT_ADD", "register:40f0:8", ["const:bb5ef0:8", "const:4:8"]]
+ 00bb5ef0 ["CALL", null, ["callee:00c5e300:8"]]
- 00bb4efc bytes 0da10294
+ 00bb5ef0 bytes 04a10294
- 00bb4f98 ["INT_ADD", "register:40f0:8", ["const:bb4f98:8", "const:4:8"]]
- 00bb4f98 ["CALL", null, ["callee:00c5b980:8"]]
+ 00bb5f8c ["INT_ADD", "register:40f0:8", ["const:bb5f8c:8", "const:4:8"]]
+ 00bb5f8c ["CALL", null, ["callee:00c5b980:8"]]
- 00bb4f98 bytes 86960294
+ 00bb5f8c bytes 7d960294
- 00bb4fb8 ["INT_ADD", "register:40f0:8", ["const:bb4fb8:8", "const:4:8"]]
- 00bb4fb8 ["CALL", null, ["callee:00c5e300:8"]]
+ 00bb5fac ["INT_ADD", "register:40f0:8", ["const:bb5fac:8", "const:4:8"]]
+ 00bb5fac ["CALL", null, ["callee:00c5e300:8"]]
- 00bb4fb8 bytes dea00294
+ 00bb5fac bytes d5a00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65702c11fbc30e84baa42dc10271d3cb"></a>

### [`00bb51ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb51ec.md) → [`00bb61e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61e0.md) _ZN11flatbuffers11CharToUpperEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) · 呼出先 1件 [`00c5d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d330.md)
- 新版 呼出元 1件 [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) · 呼出先 1件 [`00c5e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb51f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb51ec.md#insn-00bb51f8)
- 新版 [`00bb61ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61e0.md#insn-00bb61ec)

~~~diff
- 00bb51f8 ["INT_ADD", "register:40f0:8", ["const:bb51f8:8", "const:4:8"]]
- 00bb51f8 ["CALL", null, ["callee:00c5e300:8"]]
+ 00bb61ec ["INT_ADD", "register:40f0:8", ["const:bb61ec:8", "const:4:8"]]
+ 00bb61ec ["CALL", null, ["callee:00c5e300:8"]]
- 00bb51f8 bytes 4ea00294
+ 00bb61ec bytes 45a00294
~~~


<a id="compare-611ffe17a4aa279c5e49ed9c0633e6c8"></a>

### [`00bb5204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5204.md) → [`00bb61f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61f8.md) _ZN11flatbuffers11CharToLowerEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) · 呼出先 1件 [`00c5d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d320.md)
- 新版 呼出元 1件 [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) · 呼出先 1件 [`00c5e2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5204.md#insn-00bb5210)
- 新版 [`00bb6204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61f8.md#insn-00bb6204)

~~~diff
- 00bb5210 ["INT_ADD", "register:40f0:8", ["const:bb5210:8", "const:4:8"]]
- 00bb5210 ["CALL", null, ["callee:00c5e2f0:8"]]
+ 00bb6204 ["INT_ADD", "register:40f0:8", ["const:bb6204:8", "const:4:8"]]
+ 00bb6204 ["CALL", null, ["callee:00c5e2f0:8"]]
- 00bb5210 bytes 44a00294
+ 00bb6204 bytes 3ba00294
~~~


<a id="compare-8a8cea5b7ef4ae780100b8df2d989e78"></a>

### [`00bb521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb521c.md) → [`00bb6210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6210.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598c0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)
- 新版 呼出元 1件 [`00c5a890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a890.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb521c.md#insn-00bb5250) · [`00bb5278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb521c.md#insn-00bb5278) · [`00bb52ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb521c.md#insn-00bb52ac)
- 新版 [`00bb6244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6210.md#insn-00bb6244) · [`00bb626c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6210.md#insn-00bb626c) · [`00bb62a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6210.md#insn-00bb62a0)

~~~diff
- 00bb5250 ["INT_ADD", "register:40f0:8", ["const:bb5250:8", "const:4:8"]]
- 00bb5250 ["CALL", null, ["callee:00c59340:8"]]
+ 00bb6244 ["INT_ADD", "register:40f0:8", ["const:bb6244:8", "const:4:8"]]
+ 00bb6244 ["CALL", null, ["callee:00c59340:8"]]
- 00bb5250 bytes 488c0294
+ 00bb6244 bytes 3f8c0294
- 00bb5278 ["INT_ADD", "register:40f0:8", ["const:bb5278:8", "const:4:8"]]
- 00bb5278 ["CALL", null, ["callee:00c59f90:8"]]
+ 00bb626c ["INT_ADD", "register:40f0:8", ["const:bb626c:8", "const:4:8"]]
+ 00bb626c ["CALL", null, ["callee:00c59f90:8"]]
- 00bb5278 bytes 528f0294
+ 00bb626c bytes 498f0294
- 00bb52ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb52ac ["INT_ADD", "register:40f0:8", ["const:bb52ac:8", "const:4:8"]]
- 00bb52ac ["CALLIND", null, ["register:0:8"]]
+ 00bb62a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb62a0 ["INT_ADD", "register:40f0:8", ["const:bb62a0:8", "const:4:8"]]
+ 00bb62a0 ["CALLIND", null, ["register:0:8"]]
- 00bb52ac bytes 00013fd6
+ 00bb62a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f81b938efe059fd72374b0ff45322da3"></a>

### [`00bb52e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb52e8.md) → [`00bb62dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb62dc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5tellgEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598b0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)
- 新版 呼出元 1件 [`00c5a880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a880.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb52e8.md#insn-00bb5310) · [`00bb5328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb52e8.md#insn-00bb5328) · [`00bb535c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb52e8.md#insn-00bb535c)
- 新版 [`00bb6304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb62dc.md#insn-00bb6304) · [`00bb631c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb62dc.md#insn-00bb631c) · [`00bb6350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb62dc.md#insn-00bb6350)

~~~diff
- 00bb5310 ["INT_ADD", "register:40f0:8", ["const:bb5310:8", "const:4:8"]]
- 00bb5310 ["CALL", null, ["callee:00c59340:8"]]
+ 00bb6304 ["INT_ADD", "register:40f0:8", ["const:bb6304:8", "const:4:8"]]
+ 00bb6304 ["CALL", null, ["callee:00c59340:8"]]
- 00bb5310 bytes 188c0294
+ 00bb6304 bytes 0f8c0294
- 00bb5328 ["INT_ADD", "register:40f0:8", ["const:bb5328:8", "const:4:8"]]
- 00bb5328 ["CALL", null, ["callee:00c59f90:8"]]
+ 00bb631c ["INT_ADD", "register:40f0:8", ["const:bb631c:8", "const:4:8"]]
+ 00bb631c ["CALL", null, ["callee:00c59f90:8"]]
- 00bb5328 bytes 268f0294
+ 00bb631c bytes 1d8f0294
- 00bb535c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb535c ["INT_ADD", "register:40f0:8", ["const:bb535c:8", "const:4:8"]]
- 00bb535c ["CALLIND", null, ["register:0:8"]]
+ 00bb6350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6350 ["INT_ADD", "register:40f0:8", ["const:bb6350:8", "const:4:8"]]
+ 00bb6350 ["CALLIND", null, ["register:0:8"]]
- 00bb535c bytes 00013fd6
+ 00bb6350 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e421be515f72e38a516980cd12d75853"></a>

### [`00bb5394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5394.md) → [`00bb6388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6388.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d290.md) · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)
- 新版 呼出元 1件 [`00c5e260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e260.md) · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md) [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb53c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5394.md#insn-00bb53c8) · [`00bb53f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5394.md#insn-00bb53f4) · [`00bb5414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5394.md#insn-00bb5414)
- 新版 [`00bb63bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6388.md#insn-00bb63bc) · [`00bb63e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6388.md#insn-00bb63e8) · [`00bb6408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6388.md#insn-00bb6408)

~~~diff
- 00bb53c8 ["INT_ADD", "register:40f0:8", ["const:bb53c8:8", "const:4:8"]]
- 00bb53c8 ["CALL", null, ["callee:00c59f90:8"]]
+ 00bb63bc ["INT_ADD", "register:40f0:8", ["const:bb63bc:8", "const:4:8"]]
+ 00bb63bc ["CALL", null, ["callee:00c59f90:8"]]
- 00bb53c8 bytes fe8e0294
+ 00bb63bc bytes f58e0294
- 00bb53f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb53f4 ["INT_ADD", "register:40f0:8", ["const:bb53f4:8", "const:4:8"]]
- 00bb53f4 ["CALLIND", null, ["register:0:8"]]
+ 00bb63e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb63e8 ["INT_ADD", "register:40f0:8", ["const:bb63e8:8", "const:4:8"]]
+ 00bb63e8 ["CALLIND", null, ["register:0:8"]]
- 00bb53f4 bytes 00013fd6
+ 00bb63e8 bytes 00013fd6
- 00bb5414 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5414 ["INT_ADD", "register:40f0:8", ["const:bb5414:8", "const:4:8"]]
- 00bb5414 ["CALLIND", null, ["register:0:8"]]
+ 00bb6408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6408 ["INT_ADD", "register:40f0:8", ["const:bb6408:8", "const:4:8"]]
+ 00bb6408 ["CALLIND", null, ["register:0:8"]]
- 00bb5414 bytes 00013fd6
+ 00bb6408 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5306fc4601d0353434d329c30aaa0f07"></a>

### [`00bb5948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5948.md) → [`00bb693c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb693c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5948.md#insn-00bb5958)
- 新版 [`00bb694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb693c.md#insn-00bb694c)

~~~diff
- 00bb5958 ["INT_ADD", "register:40f0:8", ["const:bb5958:8", "const:4:8"]]
- 00bb5958 ["CALL", null, ["callee:00c5e250:8"]]
+ 00bb694c ["INT_ADD", "register:40f0:8", ["const:bb694c:8", "const:4:8"]]
+ 00bb694c ["CALL", null, ["callee:00c5e250:8"]]
- 00bb5958 bytes 4a9e0294
+ 00bb694c bytes 419e0294
~~~


<a id="compare-dea82e4034aaa260671de58122a8d071"></a>

### [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) → [`00bb6a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE6setbufEPcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb5584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md) [`00bb58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md) [`00c05728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05728.md) [`00c059e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c059e0.md) · 呼出先 2件 [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)
- 新版 呼出元 4件 [`00bb6578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6578.md) [`00bb68a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb68a0.md) [`00c0671c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c0671c.md) [`00c069d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c069d4.md) · 呼出先 2件 [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5a94) · [`00bb5aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5aa8) · [`00bb5afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5afc)
- 新版 [`00bb6a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md#insn-00bb6a88) · [`00bb6a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md#insn-00bb6a9c) · [`00bb6af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md#insn-00bb6af0)

~~~diff
- 00bb5a94 ["INT_ADD", "register:40f0:8", ["const:bb5a94:8", "const:4:8"]]
- 00bb5a94 ["CALL", null, ["callee:00c5cee0:8"]]
+ 00bb6a88 ["INT_ADD", "register:40f0:8", ["const:bb6a88:8", "const:4:8"]]
+ 00bb6a88 ["CALL", null, ["callee:00c5cee0:8"]]
- 00bb5a94 bytes 1f990294
+ 00bb6a88 bytes 16990294
- 00bb5aa8 ["INT_ADD", "register:40f0:8", ["const:bb5aa8:8", "const:4:8"]]
- 00bb5aa8 ["CALL", null, ["callee:00c5cee0:8"]]
+ 00bb6a9c ["INT_ADD", "register:40f0:8", ["const:bb6a9c:8", "const:4:8"]]
+ 00bb6a9c ["CALL", null, ["callee:00c5cee0:8"]]
- 00bb5aa8 bytes 1a990294
+ 00bb6a9c bytes 11990294
- 00bb5afc ["INT_ADD", "register:40f0:8", ["const:bb5afc:8", "const:4:8"]]
- 00bb5afc ["CALL", null, ["callee:00c5cef0:8"]]
+ 00bb6af0 ["INT_ADD", "register:40f0:8", ["const:bb6af0:8", "const:4:8"]]
+ 00bb6af0 ["CALL", null, ["callee:00c5cef0:8"]]
- 00bb5afc bytes 09990294
+ 00bb6af0 bytes 00990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43b111fac61dbf9f59c2b151c7495a87"></a>

### [`00bb5b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md) → [`00bb6b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6b48.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c5d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2b0.md) [`00c5d2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md) [`00c5e280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e280.md) [`00c5e290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md#insn-00bb5b80) · [`00bb5ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md#insn-00bb5ba8) · [`00bb5bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md#insn-00bb5bd8)
- 新版 [`00bb6b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6b48.md#insn-00bb6b74) · [`00bb6b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6b48.md#insn-00bb6b9c) · [`00bb6bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6b48.md#insn-00bb6bcc)

~~~diff
- 00bb5b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5b80 ["INT_ADD", "register:40f0:8", ["const:bb5b80:8", "const:4:8"]]
- 00bb5b80 ["CALLIND", null, ["register:0:8"]]
+ 00bb6b74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6b74 ["INT_ADD", "register:40f0:8", ["const:bb6b74:8", "const:4:8"]]
+ 00bb6b74 ["CALLIND", null, ["register:0:8"]]
- 00bb5b80 bytes 00013fd6
+ 00bb6b74 bytes 00013fd6
- 00bb5ba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5ba8 ["INT_ADD", "register:40f0:8", ["const:bb5ba8:8", "const:4:8"]]
- 00bb5ba8 ["CALLIND", null, ["register:0:8"]]
+ 00bb6b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6b9c ["INT_ADD", "register:40f0:8", ["const:bb6b9c:8", "const:4:8"]]
+ 00bb6b9c ["CALLIND", null, ["register:0:8"]]
- 00bb5ba8 bytes 00013fd6
+ 00bb6b9c bytes 00013fd6
- 00bb5bd8 ["INT_ADD", "register:40f0:8", ["const:bb5bd8:8", "const:4:8"]]
- 00bb5bd8 ["CALL", null, ["callee:00c5e280:8"]]
+ 00bb6bcc ["INT_ADD", "register:40f0:8", ["const:bb6bcc:8", "const:4:8"]]
+ 00bb6bcc ["CALL", null, ["callee:00c5e280:8"]]
- 00bb5bd8 bytes b69d0294
+ 00bb6bcc bytes ad9d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a277b98bdfe9e9759b4527f648b6532"></a>

### [`00bb5c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c14.md) → [`00bb6c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c08.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekposENS_4fposI9mbstate_tEEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c14.md#insn-00bb5c40) · [`00bb5c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c14.md#insn-00bb5c54)
- 新版 [`00bb6c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c08.md#insn-00bb6c34) · [`00bb6c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c08.md#insn-00bb6c48)

~~~diff
- 00bb5c40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5c40 ["INT_ADD", "register:40f0:8", ["const:bb5c40:8", "const:4:8"]]
- 00bb5c40 ["CALLIND", null, ["register:0:8"]]
+ 00bb6c34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6c34 ["INT_ADD", "register:40f0:8", ["const:bb6c34:8", "const:4:8"]]
+ 00bb6c34 ["CALLIND", null, ["register:0:8"]]
- 00bb5c40 bytes 00013fd6
+ 00bb6c34 bytes 00013fd6
- 00bb5c54 ["INT_ADD", "register:40f0:8", ["const:bb5c54:8", "const:4:8"]]
- 00bb5c54 ["CALL", null, ["callee:00c5e280:8"]]
+ 00bb6c48 ["INT_ADD", "register:40f0:8", ["const:bb6c48:8", "const:4:8"]]
+ 00bb6c48 ["CALL", null, ["callee:00c5e280:8"]]
- 00bb5c54 bytes 979d0294
+ 00bb6c48 bytes 8e9d0294
~~~


<a id="compare-c599b86cab942b9d1ddc01d3e997c525"></a>

### [`00bb5c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md) → [`00bb6c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c78.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d260.md) · 呼出先 5件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2b0.md)
- 新版 呼出元 1件 [`00c5e230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e230.md) · 呼出先 5件 [`00bb737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md) [`00c5e280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md#insn-00bb5d08) · [`00bb5d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md#insn-00bb5d38) · [`00bb5d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md#insn-00bb5d58)
- 新版 [`00bb6cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c78.md#insn-00bb6cfc) · [`00bb6d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c78.md#insn-00bb6d2c) · [`00bb6d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c78.md#insn-00bb6d4c)

~~~diff
- 00bb5d08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5d08 ["INT_ADD", "register:40f0:8", ["const:bb5d08:8", "const:4:8"]]
- 00bb5d08 ["CALLIND", null, ["register:0:8"]]
+ 00bb6cfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6cfc ["INT_ADD", "register:40f0:8", ["const:bb6cfc:8", "const:4:8"]]
+ 00bb6cfc ["CALLIND", null, ["register:0:8"]]
- 00bb5d08 bytes 00013fd6
+ 00bb6cfc bytes 00013fd6
- 00bb5d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5d38 ["INT_ADD", "register:40f0:8", ["const:bb5d38:8", "const:4:8"]]
- 00bb5d38 ["CALLIND", null, ["register:0:8"]]
+ 00bb6d2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6d2c ["INT_ADD", "register:40f0:8", ["const:bb6d2c:8", "const:4:8"]]
+ 00bb6d2c ["CALLIND", null, ["register:0:8"]]
- 00bb5d38 bytes 00013fd6
+ 00bb6d2c bytes 00013fd6
- 00bb5d58 ["INT_ADD", "register:40f0:8", ["const:bb5d58:8", "const:4:8"]]
- 00bb5d58 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00bb6d4c ["INT_ADD", "register:40f0:8", ["const:bb6d4c:8", "const:4:8"]]
+ 00bb6d4c ["CALL", null, ["callee:00c5b2c0:8"]]
- 00bb5d58 bytes 66910294
+ 00bb6d4c bytes 5d910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d652070b69a2143837f5ece3535118"></a>

### [`00bb5e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md) → [`00bb6e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6e68.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9underflowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bb737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md#insn-00bb5f70) · [`00bb5f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md#insn-00bb5f98) · [`00bb5fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md#insn-00bb5fc8)
- 新版 [`00bb6f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6e68.md#insn-00bb6f64) · [`00bb6f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6e68.md#insn-00bb6f8c) · [`00bb6fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6e68.md#insn-00bb6fbc)

~~~diff
- 00bb5f70 ["INT_ADD", "register:40f0:8", ["const:bb5f70:8", "const:4:8"]]
- 00bb5f70 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb6f64 ["INT_ADD", "register:40f0:8", ["const:bb6f64:8", "const:4:8"]]
+ 00bb6f64 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb5f70 bytes 28880294
+ 00bb6f64 bytes 1f880294
- 00bb5f98 ["INT_ADD", "register:40f0:8", ["const:bb5f98:8", "const:4:8"]]
- 00bb5f98 ["CALL", null, ["callee:00c5b120:8"]]
+ 00bb6f8c ["INT_ADD", "register:40f0:8", ["const:bb6f8c:8", "const:4:8"]]
+ 00bb6f8c ["CALL", null, ["callee:00c5b120:8"]]
- 00bb5f98 bytes 6e900294
+ 00bb6f8c bytes 65900294
- 00bb5fc8 ["INT_ADD", "register:40f0:8", ["const:bb5fc8:8", "const:4:8"]]
- 00bb5fc8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb6fbc ["INT_ADD", "register:40f0:8", ["const:bb6fbc:8", "const:4:8"]]
+ 00bb6fbc ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb5fc8 bytes 12880294
+ 00bb6fbc bytes 09880294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83ccf10fef949fb770bd71a701fa5bad"></a>

### [`00bb6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md) → [`00bb7144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7144.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE8overflowEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md#insn-00bb6244) · [`00bb6294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md#insn-00bb6294) · [`00bb62d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md#insn-00bb62d4)
- 新版 [`00bb7238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7144.md#insn-00bb7238) · [`00bb7288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7144.md#insn-00bb7288) · [`00bb72c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7144.md#insn-00bb72c8)

~~~diff
- 00bb6244 ["INT_ADD", "register:40f0:8", ["const:bb6244:8", "const:4:8"]]
- 00bb6244 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00bb7238 ["INT_ADD", "register:40f0:8", ["const:bb7238:8", "const:4:8"]]
+ 00bb7238 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00bb6244 bytes 2b900294
+ 00bb7238 bytes 22900294
- 00bb6294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb6294 ["INT_ADD", "register:40f0:8", ["const:bb6294:8", "const:4:8"]]
- 00bb6294 ["CALLIND", null, ["register:0:8"]]
+ 00bb7288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb7288 ["INT_ADD", "register:40f0:8", ["const:bb7288:8", "const:4:8"]]
+ 00bb7288 ["CALLIND", null, ["register:0:8"]]
- 00bb6294 bytes 00013fd6
+ 00bb7288 bytes 00013fd6
- 00bb62d4 ["INT_ADD", "register:40f0:8", ["const:bb62d4:8", "const:4:8"]]
- 00bb62d4 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00bb72c8 ["INT_ADD", "register:40f0:8", ["const:bb72c8:8", "const:4:8"]]
+ 00bb72c8 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00bb62d4 bytes 07900294
+ 00bb72c8 bytes fe8f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32faac143b35145180e219e6a55649b3"></a>

### [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) → [`00bb737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md) FUN_00bb737c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb5b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md) [`00bb5c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md) [`00bb5e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md) [`00bb6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 4件 [`00bb6b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6b48.md) [`00bb6c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6c78.md) [`00bb6e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6e68.md) [`00bb7144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7144.md) · 呼出先 1件 [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md#insn-00bb6390)
- 新版 [`00bb7384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb737c.md#insn-00bb7384)

~~~diff
- 00bb6390 ["INT_ADD", "register:40f0:8", ["const:bb6390:8", "const:4:8"]]
- 00bb6390 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00bb7384 ["INT_ADD", "register:40f0:8", ["const:bb7384:8", "const:4:8"]]
+ 00bb7384 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00bb6390 bytes a0930294
+ 00bb7384 bytes 97930294
~~~


<a id="compare-fd037105c176ffbe56376ba59ad234c7"></a>

### [`00bb639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb639c.md) → [`00bb7390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7390.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb63b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb639c.md#insn-00bb63b0)
- 新版 [`00bb73a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7390.md#insn-00bb73a4)

~~~diff
- 00bb63b0 ["INT_ADD", "register:40f0:8", ["const:bb63b0:8", "const:4:8"]]
- 00bb63b0 ["CALL", null, ["callee:00c5e180:8"]]
+ 00bb73a4 ["INT_ADD", "register:40f0:8", ["const:bb73a4:8", "const:4:8"]]
+ 00bb73a4 ["CALL", null, ["callee:00c5e180:8"]]
- 00bb63b0 bytes 809b0294
+ 00bb73a4 bytes 779b0294
~~~


<a id="compare-f0a082ed5ac86747cc5e5f9de315cd07"></a>

### [`00bb63d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb63d8.md) → [`00bb73cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb73cc.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb63d8.md#insn-00bb63f4)
- 新版 [`00bb73e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb73cc.md#insn-00bb73e8)

~~~diff
- 00bb63f4 ["INT_ADD", "register:40f0:8", ["const:bb63f4:8", "const:4:8"]]
- 00bb63f4 ["CALL", null, ["callee:00c5e180:8"]]
+ 00bb73e8 ["INT_ADD", "register:40f0:8", ["const:bb73e8:8", "const:4:8"]]
+ 00bb73e8 ["CALL", null, ["callee:00c5e180:8"]]
- 00bb63f4 bytes 6f9b0294
+ 00bb73e8 bytes 669b0294
~~~


<a id="compare-7afcedde6f0d95ee398c4836e7f8798a"></a>

### [`00bb6740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6740.md) → [`00bb7734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7734.md) FUN_00bb7734

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) · 呼出先 2件 [`00c5aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aba0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00bb9c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md) · 呼出先 2件 [`00c5bb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb70.md) [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6740.md#insn-00bb6750)
- 新版 [`00bb7744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7734.md#insn-00bb7744)

~~~diff
- 00bb6750 ["INT_ADD", "register:40f0:8", ["const:bb6750:8", "const:4:8"]]
- 00bb6750 ["CALL", null, ["callee:00c5bd00:8"]]
+ 00bb7744 ["INT_ADD", "register:40f0:8", ["const:bb7744:8", "const:4:8"]]
+ 00bb7744 ["CALL", null, ["callee:00c5bd00:8"]]
- 00bb6750 bytes 78910294
+ 00bb7744 bytes 6f910294
~~~


<a id="compare-db9838d05731d4c4ed8a2fd690ecfee7"></a>

### [`00bb6780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md) → [`00bb7774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7774.md) FUN_00bb7774

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) · 呼出先 2件 [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md) [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md)
- 新版 呼出元 1件 [`00bb9c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md) · 呼出先 2件 [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md) [`00c5e4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md#insn-00bb6790)
- 新版 [`00bb7784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7774.md#insn-00bb7784)

~~~diff
- 00bb6790 ["INT_ADD", "register:40f0:8", ["const:bb6790:8", "const:4:8"]]
- 00bb6790 ["CALL", null, ["callee:00c5bd00:8"]]
+ 00bb7784 ["INT_ADD", "register:40f0:8", ["const:bb7784:8", "const:4:8"]]
+ 00bb7784 ["CALL", null, ["callee:00c5bd00:8"]]
- 00bb6790 bytes 68910294
+ 00bb7784 bytes 5f910294
~~~


<a id="compare-58b6c47f075879098a57127dbebd4dbb"></a>

### [`00bb6e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md) → [`00bb7e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e8c.md) _ZN8firebase9messaging20PollableListenerImplD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d530.md)
- 新版 呼出元 1件 [`00c5e420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e420.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md) [`00c5e500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md#insn-00bb6eb4) · [`00bb6ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md#insn-00bb6ec8) · [`00bb6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md#insn-00bb6efc)
- 新版 [`00bb7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e8c.md#insn-00bb7ea8) · [`00bb7ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e8c.md#insn-00bb7ebc) · [`00bb7ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e8c.md#insn-00bb7ef0)

~~~diff
- 00bb6eb4 ["INT_ADD", "register:40f0:8", ["const:bb6eb4:8", "const:4:8"]]
- 00bb6eb4 ["CALL", null, ["callee:00c5e500:8"]]
+ 00bb7ea8 ["INT_ADD", "register:40f0:8", ["const:bb7ea8:8", "const:4:8"]]
+ 00bb7ea8 ["CALL", null, ["callee:00c5e500:8"]]
- 00bb6eb4 bytes 9f990294
+ 00bb7ea8 bytes 96990294
- 00bb6ec8 ["INT_ADD", "register:40f0:8", ["const:bb6ec8:8", "const:4:8"]]
- 00bb6ec8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb7ebc ["INT_ADD", "register:40f0:8", ["const:bb7ebc:8", "const:4:8"]]
+ 00bb7ebc ["CALL", null, ["callee:00c58f50:8"]]
- 00bb6ec8 bytes 2e840294
+ 00bb7ebc bytes 25840294
- 00bb6efc ["INT_ADD", "register:40f0:8", ["const:bb6efc:8", "const:4:8"]]
- 00bb6efc ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb7ef0 ["INT_ADD", "register:40f0:8", ["const:bb7ef0:8", "const:4:8"]]
+ 00bb7ef0 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb6efc bytes 21840294
+ 00bb7ef0 bytes 18840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e58e2c1b1faae0da7f6f6b67c339c0"></a>

### [`00bb6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6fb0.md) → [`00bb7fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7fa4.md) _ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d440.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4b0.md) [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md)
- 新版 呼出元 1件 [`00c5e410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e410.md) · 呼出先 6件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e480.md) [`00c5e490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6fb0.md#insn-00bb6fd8) · [`00bb6fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6fb0.md#insn-00bb6fe0) · [`00bb700c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6fb0.md#insn-00bb700c)
- 新版 [`00bb7fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7fa4.md#insn-00bb7fcc) · [`00bb7fd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7fa4.md#insn-00bb7fd4) · [`00bb8000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7fa4.md#insn-00bb8000)

~~~diff
- 00bb6fd8 ["INT_ADD", "register:40f0:8", ["const:bb6fd8:8", "const:4:8"]]
- 00bb6fd8 ["CALL", null, ["callee:00c5e480:8"]]
+ 00bb7fcc ["INT_ADD", "register:40f0:8", ["const:bb7fcc:8", "const:4:8"]]
+ 00bb7fcc ["CALL", null, ["callee:00c5e480:8"]]
- 00bb6fd8 bytes 36990294
+ 00bb7fcc bytes 2d990294
- 00bb6fe0 ["INT_ADD", "register:40f0:8", ["const:bb6fe0:8", "const:4:8"]]
- 00bb6fe0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7fd4 ["INT_ADD", "register:40f0:8", ["const:bb7fd4:8", "const:4:8"]]
+ 00bb7fd4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6fe0 bytes bc8e0294
+ 00bb7fd4 bytes b38e0294
- 00bb700c ["INT_ADD", "register:40f0:8", ["const:bb700c:8", "const:4:8"]]
- 00bb700c ["CALL", null, ["callee:00c5e550:8"]]
+ 00bb8000 ["INT_ADD", "register:40f0:8", ["const:bb8000:8", "const:4:8"]]
+ 00bb8000 ["CALL", null, ["callee:00c5e550:8"]]
- 00bb700c bytes 5d990294
+ 00bb8000 bytes 54990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c536f7c9959463283bdced47e196a91"></a>

### [`00bb70c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb70c4.md) → [`00bb80b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb80b8.md) _ZN8firebase9messaging20PollableListenerImpl15OnTokenReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3e0.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3b0.md) · 呼出先 4件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb70dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb70c4.md#insn-00bb70dc) · [`00bb70e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb70c4.md#insn-00bb70e8) · [`00bb70f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb70c4.md#insn-00bb70f8)
- 新版 [`00bb80d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb80b8.md#insn-00bb80d0) · [`00bb80dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb80b8.md#insn-00bb80dc) · [`00bb80ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb80b8.md#insn-00bb80ec)

~~~diff
- 00bb70dc ["INT_ADD", "register:40f0:8", ["const:bb70dc:8", "const:4:8"]]
- 00bb70dc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb80d0 ["INT_ADD", "register:40f0:8", ["const:bb80d0:8", "const:4:8"]]
+ 00bb80d0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb70dc bytes 7d8e0294
+ 00bb80d0 bytes 748e0294
- 00bb70e8 ["INT_ADD", "register:40f0:8", ["const:bb70e8:8", "const:4:8"]]
- 00bb70e8 ["CALL", null, ["callee:00c59080:8"]]
+ 00bb80dc ["INT_ADD", "register:40f0:8", ["const:bb80dc:8", "const:4:8"]]
+ 00bb80dc ["CALL", null, ["callee:00c59080:8"]]
- 00bb70e8 bytes f2830294
+ 00bb80dc bytes e9830294
- 00bb70f8 ["INT_ADD", "register:40f0:8", ["const:bb70f8:8", "const:4:8"]]
- 00bb70f8 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb80ec ["INT_ADD", "register:40f0:8", ["const:bb80ec:8", "const:4:8"]]
+ 00bb80ec ["CALL", null, ["callee:00c5c150:8"]]
- 00bb70f8 bytes 22900294
+ 00bb80ec bytes 19900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a4ac4b3ca45c8f812c049f9be402de"></a>

### [`00bb7138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7138.md) → [`00bb812c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb812c.md) _ZN8firebase9messaging20PollableListenerImpl22OnRegistrationReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d420.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3f0.md) · 呼出先 4件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7138.md#insn-00bb7150) · [`00bb715c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7138.md#insn-00bb715c) · [`00bb716c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7138.md#insn-00bb716c)
- 新版 [`00bb8144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb812c.md#insn-00bb8144) · [`00bb8150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb812c.md#insn-00bb8150) · [`00bb8160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb812c.md#insn-00bb8160)

~~~diff
- 00bb7150 ["INT_ADD", "register:40f0:8", ["const:bb7150:8", "const:4:8"]]
- 00bb7150 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb8144 ["INT_ADD", "register:40f0:8", ["const:bb8144:8", "const:4:8"]]
+ 00bb8144 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb7150 bytes 608e0294
+ 00bb8144 bytes 578e0294
- 00bb715c ["INT_ADD", "register:40f0:8", ["const:bb715c:8", "const:4:8"]]
- 00bb715c ["CALL", null, ["callee:00c59080:8"]]
+ 00bb8150 ["INT_ADD", "register:40f0:8", ["const:bb8150:8", "const:4:8"]]
+ 00bb8150 ["CALL", null, ["callee:00c59080:8"]]
- 00bb715c bytes d5830294
+ 00bb8150 bytes cc830294
- 00bb716c ["INT_ADD", "register:40f0:8", ["const:bb716c:8", "const:4:8"]]
- 00bb716c ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb8160 ["INT_ADD", "register:40f0:8", ["const:bb8160:8", "const:4:8"]]
+ 00bb8160 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb716c bytes 05900294
+ 00bb8160 bytes fc8f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfaddf95232e741107fde88a58d4d601"></a>

### [`00bb71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb71ac.md) → [`00bb81a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb81a0.md) _ZN8firebase9messaging20PollableListenerImpl24OnUnregistrationReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d430.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e400.md) · 呼出先 4件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb71ac.md#insn-00bb71c4) · [`00bb71d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb71ac.md#insn-00bb71d0) · [`00bb71e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb71ac.md#insn-00bb71e0)
- 新版 [`00bb81b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb81a0.md#insn-00bb81b8) · [`00bb81c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb81a0.md#insn-00bb81c4) · [`00bb81d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb81a0.md#insn-00bb81d4)

~~~diff
- 00bb71c4 ["INT_ADD", "register:40f0:8", ["const:bb71c4:8", "const:4:8"]]
- 00bb71c4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb81b8 ["INT_ADD", "register:40f0:8", ["const:bb81b8:8", "const:4:8"]]
+ 00bb81b8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb71c4 bytes 438e0294
+ 00bb81b8 bytes 3a8e0294
- 00bb71d0 ["INT_ADD", "register:40f0:8", ["const:bb71d0:8", "const:4:8"]]
- 00bb71d0 ["CALL", null, ["callee:00c59080:8"]]
+ 00bb81c4 ["INT_ADD", "register:40f0:8", ["const:bb81c4:8", "const:4:8"]]
+ 00bb81c4 ["CALL", null, ["callee:00c59080:8"]]
- 00bb71d0 bytes b8830294
+ 00bb81c4 bytes af830294
- 00bb71e0 ["INT_ADD", "register:40f0:8", ["const:bb71e0:8", "const:4:8"]]
- 00bb71e0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb81d4 ["INT_ADD", "register:40f0:8", ["const:bb81d4:8", "const:4:8"]]
+ 00bb81d4 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb71e0 bytes e88f0294
+ 00bb81d4 bytes df8f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa11772778fc592014ce58e2d373f74"></a>

### [`00bb7310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7310.md) → [`00bb8304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8304.md) _ZN8firebase9messaging16PollableListener21PollRegistrationTokenEPb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d410.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7310.md#insn-00bb7334)
- 新版 [`00bb8328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8304.md#insn-00bb8328)

~~~diff
- 00bb7334 ["INT_ADD", "register:40f0:8", ["const:bb7334:8", "const:4:8"]]
- 00bb7334 ["CALL", null, ["callee:00c5e3e0:8"]]
+ 00bb8328 ["INT_ADD", "register:40f0:8", ["const:bb8328:8", "const:4:8"]]
+ 00bb8328 ["CALL", null, ["callee:00c5e3e0:8"]]
- 00bb7334 bytes 37980294
+ 00bb8328 bytes 2e980294
~~~


<a id="compare-8b9dfede1fd121e061256e9ea071abb0"></a>

### [`00bb7368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7368.md) → [`00bb835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb835c.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d410.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3e0.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7368.md#insn-00bb7380) · [`00bb73b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7368.md#insn-00bb73b8) · [`00bb73f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7368.md#insn-00bb73f0)
- 新版 [`00bb8374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb835c.md#insn-00bb8374) · [`00bb83ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb835c.md#insn-00bb83ac) · [`00bb83e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb835c.md#insn-00bb83e4)

~~~diff
- 00bb7380 ["INT_ADD", "register:40f0:8", ["const:bb7380:8", "const:4:8"]]
- 00bb7380 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb8374 ["INT_ADD", "register:40f0:8", ["const:bb8374:8", "const:4:8"]]
+ 00bb8374 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb7380 bytes d48d0294
+ 00bb8374 bytes cb8d0294
- 00bb73b8 ["INT_ADD", "register:40f0:8", ["const:bb73b8:8", "const:4:8"]]
- 00bb73b8 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb83ac ["INT_ADD", "register:40f0:8", ["const:bb83ac:8", "const:4:8"]]
+ 00bb83ac ["CALL", null, ["callee:00c5c150:8"]]
- 00bb73b8 bytes 728f0294
+ 00bb83ac bytes 698f0294
- 00bb73f0 ["INT_ADD", "register:40f0:8", ["const:bb73f0:8", "const:4:8"]]
- 00bb73f0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bb83e4 ["INT_ADD", "register:40f0:8", ["const:bb83e4:8", "const:4:8"]]
+ 00bb83e4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bb73f0 bytes bc8d0294
+ 00bb83e4 bytes b38d0294
~~~


<a id="compare-7f7edad73ad5f538ac3b9ef95530a166"></a>

### [`00bb7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7424.md) → [`00bb8418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8418.md) _ZN8firebase9messaging16PollableListener16PollRegistrationEPb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7424.md#insn-00bb7448)
- 新版 [`00bb843c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8418.md#insn-00bb843c)

~~~diff
- 00bb7448 ["INT_ADD", "register:40f0:8", ["const:bb7448:8", "const:4:8"]]
- 00bb7448 ["CALL", null, ["callee:00c5e3c0:8"]]
+ 00bb843c ["INT_ADD", "register:40f0:8", ["const:bb843c:8", "const:4:8"]]
+ 00bb843c ["CALL", null, ["callee:00c5e3c0:8"]]
- 00bb7448 bytes ea970294
+ 00bb843c bytes e1970294
~~~


<a id="compare-076e81d1a19c0ede006f245efe1d6650"></a>

### [`00bb747c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb747c.md) → [`00bb8470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8470.md) _ZN8firebase9messaging20PollableListenerImpl16PollRegistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3f0.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3c0.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb747c.md#insn-00bb7494) · [`00bb74cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb747c.md#insn-00bb74cc) · [`00bb7504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb747c.md#insn-00bb7504)
- 新版 [`00bb8488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8470.md#insn-00bb8488) · [`00bb84c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8470.md#insn-00bb84c0) · [`00bb84f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8470.md#insn-00bb84f8)

~~~diff
- 00bb7494 ["INT_ADD", "register:40f0:8", ["const:bb7494:8", "const:4:8"]]
- 00bb7494 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb8488 ["INT_ADD", "register:40f0:8", ["const:bb8488:8", "const:4:8"]]
+ 00bb8488 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb7494 bytes 8f8d0294
+ 00bb8488 bytes 868d0294
- 00bb74cc ["INT_ADD", "register:40f0:8", ["const:bb74cc:8", "const:4:8"]]
- 00bb74cc ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb84c0 ["INT_ADD", "register:40f0:8", ["const:bb84c0:8", "const:4:8"]]
+ 00bb84c0 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb74cc bytes 2d8f0294
+ 00bb84c0 bytes 248f0294
- 00bb7504 ["INT_ADD", "register:40f0:8", ["const:bb7504:8", "const:4:8"]]
- 00bb7504 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bb84f8 ["INT_ADD", "register:40f0:8", ["const:bb84f8:8", "const:4:8"]]
+ 00bb84f8 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bb7504 bytes 778d0294
+ 00bb84f8 bytes 6e8d0294
~~~


<a id="compare-74d10322e5c487fc4ab942d46549199d"></a>

### [`00bb7538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7538.md) → [`00bb852c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb852c.md) _ZN8firebase9messaging16PollableListener18PollUnregistrationEPb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d400.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb755c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7538.md#insn-00bb755c)
- 新版 [`00bb8550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb852c.md#insn-00bb8550)

~~~diff
- 00bb755c ["INT_ADD", "register:40f0:8", ["const:bb755c:8", "const:4:8"]]
- 00bb755c ["CALL", null, ["callee:00c5e3d0:8"]]
+ 00bb8550 ["INT_ADD", "register:40f0:8", ["const:bb8550:8", "const:4:8"]]
+ 00bb8550 ["CALL", null, ["callee:00c5e3d0:8"]]
- 00bb755c bytes a9970294
+ 00bb8550 bytes a0970294
~~~


<a id="compare-4be2556b0371742796f1edc4bf9af821"></a>

### [`00bb7590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7590.md) → [`00bb8584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8584.md) _ZN8firebase9messaging20PollableListenerImpl18PollUnregistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d400.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e3d0.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb75a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7590.md#insn-00bb75a8) · [`00bb75e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7590.md#insn-00bb75e0) · [`00bb7618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7590.md#insn-00bb7618)
- 新版 [`00bb859c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8584.md#insn-00bb859c) · [`00bb85d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8584.md#insn-00bb85d4) · [`00bb860c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8584.md#insn-00bb860c)

~~~diff
- 00bb75a8 ["INT_ADD", "register:40f0:8", ["const:bb75a8:8", "const:4:8"]]
- 00bb75a8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb859c ["INT_ADD", "register:40f0:8", ["const:bb859c:8", "const:4:8"]]
+ 00bb859c ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb75a8 bytes 4a8d0294
+ 00bb859c bytes 418d0294
- 00bb75e0 ["INT_ADD", "register:40f0:8", ["const:bb75e0:8", "const:4:8"]]
- 00bb75e0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb85d4 ["INT_ADD", "register:40f0:8", ["const:bb85d4:8", "const:4:8"]]
+ 00bb85d4 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb75e0 bytes e88e0294
+ 00bb85d4 bytes df8e0294
- 00bb7618 ["INT_ADD", "register:40f0:8", ["const:bb7618:8", "const:4:8"]]
- 00bb7618 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bb860c ["INT_ADD", "register:40f0:8", ["const:bb860c:8", "const:4:8"]]
+ 00bb860c ["CALL", null, ["callee:00c5bab0:8"]]
- 00bb7618 bytes 328d0294
+ 00bb860c bytes 298d0294
~~~


<a id="compare-6bcef854398dd787510e197d69367105"></a>

### [`00bb7714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7714.md) → [`00bb8708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8708.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d530.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md)
- 新版 呼出元 1件 [`00c5e500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e500.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7714.md#insn-00bb7794) · [`00bb77d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7714.md#insn-00bb77d8)
- 新版 [`00bb8788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8708.md#insn-00bb8788) · [`00bb87cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8708.md#insn-00bb87cc)

~~~diff
- 00bb7794 ["INT_ADD", "register:40f0:8", ["const:bb7794:8", "const:4:8"]]
- 00bb7794 ["CALL", null, ["callee:00c5e490:8"]]
+ 00bb8788 ["INT_ADD", "register:40f0:8", ["const:bb8788:8", "const:4:8"]]
+ 00bb8788 ["CALL", null, ["callee:00c5e490:8"]]
- 00bb7794 bytes 4b970294
+ 00bb8788 bytes 42970294
- 00bb77d8 ["INT_ADD", "register:40f0:8", ["const:bb77d8:8", "const:4:8"]]
- 00bb77d8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb87cc ["INT_ADD", "register:40f0:8", ["const:bb87cc:8", "const:4:8"]]
+ 00bb87cc ["CALL", null, ["callee:00c58f50:8"]]
- 00bb77d8 bytes ea810294
+ 00bb87cc bytes e1810294
~~~


<a id="compare-a9fc866d72465e3b330c74e2a7052373"></a>

### [`00bb782c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb782c.md) → [`00bb8820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8820.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md) · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3a0.md)
- 新版 呼出元 1件 [`00c5e490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e490.md) · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb782c.md#insn-00bb7848) · [`00bb7850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb782c.md#insn-00bb7850) · [`00bb7898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb782c.md#insn-00bb7898)
- 新版 [`00bb883c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8820.md#insn-00bb883c) · [`00bb8844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8820.md#insn-00bb8844) · [`00bb888c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8820.md#insn-00bb888c)

~~~diff
- 00bb7848 ["INT_ADD", "register:40f0:8", ["const:bb7848:8", "const:4:8"]]
- 00bb7848 ["CALL", null, ["callee:00c5e370:8"]]
+ 00bb883c ["INT_ADD", "register:40f0:8", ["const:bb883c:8", "const:4:8"]]
+ 00bb883c ["CALL", null, ["callee:00c5e370:8"]]
- 00bb7848 bytes d6960294
+ 00bb883c bytes cd960294
- 00bb7850 ["INT_ADD", "register:40f0:8", ["const:bb7850:8", "const:4:8"]]
- 00bb7850 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb8844 ["INT_ADD", "register:40f0:8", ["const:bb8844:8", "const:4:8"]]
+ 00bb8844 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb7850 bytes cc810294
+ 00bb8844 bytes c3810294
- 00bb7898 ["INT_ADD", "register:40f0:8", ["const:bb7898:8", "const:4:8"]]
- 00bb7898 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb888c ["INT_ADD", "register:40f0:8", ["const:bb888c:8", "const:4:8"]]
+ 00bb888c ["CALL", null, ["callee:00c58f50:8"]]
- 00bb7898 bytes ba810294
+ 00bb888c bytes b1810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d549574e4a9e709071a5eaac2dc8500"></a>

### [`00bb7970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7970.md) → [`00bb8964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8964.md) _ZN8firebase9messaging12NotificationD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3a0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5e370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e370.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7970.md#insn-00bb7998) · [`00bb79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7970.md#insn-00bb79a0) · [`00bb79dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7970.md#insn-00bb79dc)
- 新版 [`00bb898c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8964.md#insn-00bb898c) · [`00bb8994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8964.md#insn-00bb8994) · [`00bb89d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8964.md#insn-00bb89d0)

~~~diff
- 00bb7998 ["INT_ADD", "register:40f0:8", ["const:bb7998:8", "const:4:8"]]
- 00bb7998 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb898c ["INT_ADD", "register:40f0:8", ["const:bb898c:8", "const:4:8"]]
+ 00bb898c ["CALL", null, ["callee:00c58f50:8"]]
- 00bb7998 bytes 7a810294
+ 00bb898c bytes 71810294
- 00bb79a0 ["INT_ADD", "register:40f0:8", ["const:bb79a0:8", "const:4:8"]]
- 00bb79a0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb8994 ["INT_ADD", "register:40f0:8", ["const:bb8994:8", "const:4:8"]]
+ 00bb8994 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb79a0 bytes 78810294
+ 00bb8994 bytes 6f810294
- 00bb79dc ["INT_ADD", "register:40f0:8", ["const:bb79dc:8", "const:4:8"]]
- 00bb79dc ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb89d0 ["INT_ADD", "register:40f0:8", ["const:bb89d0:8", "const:4:8"]]
+ 00bb89d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb79dc bytes 69810294
+ 00bb89d0 bytes 60810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c3ca11b59de0ed23eda530ca880e02"></a>

### [`00bb7b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7b48.md) → [`00bb8b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8b3c.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4b0.md) · 呼出先 1件 [`00c5d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4d0.md)
- 新版 呼出元 1件 [`00c5e480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e480.md) · 呼出先 1件 [`00c5e4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7b48.md#insn-00bb7bb8)
- 新版 [`00bb8bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8b3c.md#insn-00bb8bac)

~~~diff
- 00bb7bb8 ["INT_ADD", "register:40f0:8", ["const:bb7bb8:8", "const:4:8"]]
- 00bb7bb8 ["CALL", null, ["callee:00c5e4a0:8"]]
+ 00bb8bac ["INT_ADD", "register:40f0:8", ["const:bb8bac:8", "const:4:8"]]
+ 00bb8bac ["CALL", null, ["callee:00c5e4a0:8"]]
- 00bb7bb8 bytes 46960294
+ 00bb8bac bytes 3d960294
~~~


<a id="compare-8af222353c2558815b69855fa570b0e7"></a>

### [`00bb7cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7cec.md) → [`00bb8ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8ce0.md) _ZN8firebase9messaging7MessageaSERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4d0.md) · 呼出先 7件 [`0053b7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b7bc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d390.md)
- 新版 呼出元 1件 [`00c5e4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4a0.md) · 呼出先 7件 [`0053badc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053badc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5e360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7cec.md#insn-00bb7d28) · [`00bb7d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7cec.md#insn-00bb7d4c) · [`00bb7d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7cec.md#insn-00bb7d70)
- 新版 [`00bb8d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8ce0.md#insn-00bb8d1c) · [`00bb8d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8ce0.md#insn-00bb8d40) · [`00bb8d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8ce0.md#insn-00bb8d64)

~~~diff
- 00bb7d28 ["INT_ADD", "register:40f0:8", ["const:bb7d28:8", "const:4:8"]]
- 00bb7d28 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb8d1c ["INT_ADD", "register:40f0:8", ["const:bb8d1c:8", "const:4:8"]]
+ 00bb8d1c ["CALL", null, ["callee:00c5c150:8"]]
- 00bb7d28 bytes 168d0294
+ 00bb8d1c bytes 0d8d0294
- 00bb7d4c ["INT_ADD", "register:40f0:8", ["const:bb7d4c:8", "const:4:8"]]
- 00bb7d4c ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb8d40 ["INT_ADD", "register:40f0:8", ["const:bb8d40:8", "const:4:8"]]
+ 00bb8d40 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb7d4c bytes 0d8d0294
+ 00bb8d40 bytes 048d0294
- 00bb7d70 ["INT_ADD", "register:40f0:8", ["const:bb7d70:8", "const:4:8"]]
- 00bb7d70 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb8d64 ["INT_ADD", "register:40f0:8", ["const:bb8d64:8", "const:4:8"]]
+ 00bb8d64 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb7d70 bytes 048d0294
+ 00bb8d64 bytes fb8c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ea87ed7302f7f0dc74f71cf9f58d5a"></a>

### [`00bb7f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7f1c.md) → [`00bb8f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8f10.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d390.md) · 呼出先 1件 [`00c5d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3b0.md)
- 新版 呼出元 1件 [`00c5e360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e360.md) · 呼出先 1件 [`00c5e380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7f1c.md#insn-00bb7f5c)
- 新版 [`00bb8f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8f10.md#insn-00bb8f50)

~~~diff
- 00bb7f5c ["INT_ADD", "register:40f0:8", ["const:bb7f5c:8", "const:4:8"]]
- 00bb7f5c ["CALL", null, ["callee:00c5e380:8"]]
+ 00bb8f50 ["INT_ADD", "register:40f0:8", ["const:bb8f50:8", "const:4:8"]]
+ 00bb8f50 ["CALL", null, ["callee:00c5e380:8"]]
- 00bb7f5c bytes 15950294
+ 00bb8f50 bytes 0c950294
~~~


<a id="compare-18aa2d26869d1b17595d3207c6aa1378"></a>

### [`00bb810c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb810c.md) → [`00bb9100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9100.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d590.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5e560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e560.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb810c.md#insn-00bb8150) · [`00bb81ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb810c.md#insn-00bb81ac) · [`00bb81d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb810c.md#insn-00bb81d4)
- 新版 [`00bb9144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9100.md#insn-00bb9144) · [`00bb91a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9100.md#insn-00bb91a0) · [`00bb91c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9100.md#insn-00bb91c8)

~~~diff
- 00bb8150 ["INT_ADD", "register:40f0:8", ["const:bb8150:8", "const:4:8"]]
- 00bb8150 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bb9144 ["INT_ADD", "register:40f0:8", ["const:bb9144:8", "const:4:8"]]
+ 00bb9144 ["CALL", null, ["callee:00c58f50:8"]]
- 00bb8150 bytes 8c7f0294
+ 00bb9144 bytes 837f0294
- 00bb81ac ["INT_ADD", "register:40f0:8", ["const:bb81ac:8", "const:4:8"]]
- 00bb81ac ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb91a0 ["INT_ADD", "register:40f0:8", ["const:bb91a0:8", "const:4:8"]]
+ 00bb91a0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb81ac bytes 997f0294
+ 00bb91a0 bytes 907f0294
- 00bb81d4 ["INT_ADD", "register:40f0:8", ["const:bb81d4:8", "const:4:8"]]
- 00bb81d4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bb91c8 ["INT_ADD", "register:40f0:8", ["const:bb91c8:8", "const:4:8"]]
+ 00bb91c8 ["CALL", null, ["callee:00c590a0:8"]]
- 00bb81d4 bytes bf7f0294
+ 00bb91c8 bytes b67f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed53f062f320656488ea9d724fb8b8b3"></a>

### [`00bb823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb823c.md) → [`00bb9230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9230.md) _ZN8firebase9messaging12NotificationaSERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3b0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md)
- 新版 呼出元 1件 [`00c5e380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e380.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb823c.md#insn-00bb8278) · [`00bb829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb823c.md#insn-00bb829c) · [`00bb82c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb823c.md#insn-00bb82c0)
- 新版 [`00bb926c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9230.md#insn-00bb926c) · [`00bb9290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9230.md#insn-00bb9290) · [`00bb92b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9230.md#insn-00bb92b4)

~~~diff
- 00bb8278 ["INT_ADD", "register:40f0:8", ["const:bb8278:8", "const:4:8"]]
- 00bb8278 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb926c ["INT_ADD", "register:40f0:8", ["const:bb926c:8", "const:4:8"]]
+ 00bb926c ["CALL", null, ["callee:00c5c150:8"]]
- 00bb8278 bytes c28b0294
+ 00bb926c bytes b98b0294
- 00bb829c ["INT_ADD", "register:40f0:8", ["const:bb829c:8", "const:4:8"]]
- 00bb829c ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb9290 ["INT_ADD", "register:40f0:8", ["const:bb9290:8", "const:4:8"]]
+ 00bb9290 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb829c bytes b98b0294
+ 00bb9290 bytes b08b0294
- 00bb82c0 ["INT_ADD", "register:40f0:8", ["const:bb82c0:8", "const:4:8"]]
- 00bb82c0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bb92b4 ["INT_ADD", "register:40f0:8", ["const:bb92b4:8", "const:4:8"]]
+ 00bb92b4 ["CALL", null, ["callee:00c5c150:8"]]
- 00bb82c0 bytes b08b0294
+ 00bb92b4 bytes a78b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d4b4a86550009aa6930eb982d7ae42"></a>

### [`00bb96d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb96d4.md) → [`00bba6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba6c8.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb96f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb96d4.md#insn-00bb96f4)
- 新版 [`00bba6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba6c8.md#insn-00bba6e8)

~~~diff
- 00bb96f4 ["INT_ADD", "register:40f0:8", ["const:bb96f4:8", "const:4:8"]]
- 00bb96f4 ["CALL", null, ["callee:00c5e620:8"]]
+ 00bba6e8 ["INT_ADD", "register:40f0:8", ["const:bba6e8:8", "const:4:8"]]
+ 00bba6e8 ["CALL", null, ["callee:00c5e620:8"]]
- 00bb96f4 bytes d78f0294
+ 00bba6e8 bytes ce8f0294
~~~


<a id="compare-4722b768005a7160228ec861ebf2b6e5"></a>

### [`00bbd4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md) → [`00bbe4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md) FUN_00bbe4f0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 2件 [`00bbc72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md) [`00bbccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbd534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md#insn-00bbd534) · [`00bbd544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md#insn-00bbd544) · [`00bbd55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md#insn-00bbd55c)
- 新版 [`00bbe528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md#insn-00bbe528) · [`00bbe538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md#insn-00bbe538) · [`00bbe550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md#insn-00bbe550)

~~~diff
- 00bbd534 ["INT_ADD", "register:40f0:8", ["const:bbd534:8", "const:4:8"]]
- 00bbd534 ["CALL", null, ["callee:00c5e310:8"]]
+ 00bbe528 ["INT_ADD", "register:40f0:8", ["const:bbe528:8", "const:4:8"]]
+ 00bbe528 ["CALL", null, ["callee:00c5e310:8"]]
- 00bbd534 bytes 837f0294
+ 00bbe528 bytes 7a7f0294
- 00bbd544 ["INT_ADD", "register:40f0:8", ["const:bbd544:8", "const:4:8"]]
- 00bbd544 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bbe538 ["INT_ADD", "register:40f0:8", ["const:bbe538:8", "const:4:8"]]
+ 00bbe538 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bbd544 bytes 63760294
+ 00bbe538 bytes 5a760294
- 00bbd55c ["INT_ADD", "register:40f0:8", ["const:bbd55c:8", "const:4:8"]]
- 00bbd55c ["CALL", null, ["callee:00c5be40:8"]]
+ 00bbe550 ["INT_ADD", "register:40f0:8", ["const:bbe550:8", "const:4:8"]]
+ 00bbe550 ["CALL", null, ["callee:00c5be40:8"]]
- 00bbd55c bytes 45760294
+ 00bbe550 bytes 3c760294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e79b18999fe0527547bbe14488ee2b"></a>

### [`00bbd5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md) → [`00bbe5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe5ac.md) _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6a0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd30.md)
- 新版 呼出元 1件 [`00c5e670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e670.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md) [`00c5cd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbd640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md#insn-00bbd640) · [`00bbd670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md#insn-00bbd670) · [`00bbd6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md#insn-00bbd6b4)
- 新版 [`00bbe634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe5ac.md#insn-00bbe634) · [`00bbe664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe5ac.md#insn-00bbe664) · [`00bbe6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe5ac.md#insn-00bbe6a8)

~~~diff
- 00bbd640 ["INT_ADD", "register:40f0:8", ["const:bbd640:8", "const:4:8"]]
- 00bbd640 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bbe634 ["INT_ADD", "register:40f0:8", ["const:bbe634:8", "const:4:8"]]
+ 00bbe634 ["CALL", null, ["callee:00c58f30:8"]]
- 00bbd640 bytes 486a0294
+ 00bbe634 bytes 3f6a0294
- 00bbd670 ["INT_ADD", "register:40f0:8", ["const:bbd670:8", "const:4:8"]]
- 00bbd670 ["CALL", null, ["callee:00c5cd00:8"]]
+ 00bbe664 ["INT_ADD", "register:40f0:8", ["const:bbe664:8", "const:4:8"]]
+ 00bbe664 ["CALL", null, ["callee:00c5cd00:8"]]
- 00bbd670 bytes b0790294
+ 00bbe664 bytes a7790294
- 00bbd6b4 ["INT_ADD", "register:40f0:8", ["const:bbd6b4:8", "const:4:8"]]
- 00bbd6b4 ["CALL", null, ["callee:00c5cd00:8"]]
+ 00bbe6a8 ["INT_ADD", "register:40f0:8", ["const:bbe6a8:8", "const:4:8"]]
+ 00bbe6a8 ["CALL", null, ["callee:00c5cd00:8"]]
- 00bbd6b4 bytes 9f790294
+ 00bbe6a8 bytes 96790294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeebfd69bbc129b03864e4ad23ca4166"></a>

### [`00bbea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md) → [`00bbfa4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfa4c.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valu

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d640.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5e610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e610.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbea9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md#insn-00bbea9c) · [`00bbeb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md#insn-00bbeb00) · [`00bbecb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md#insn-00bbecb4)
- 新版 [`00bbfa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfa4c.md#insn-00bbfa90) · [`00bbfaf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfa4c.md#insn-00bbfaf4) · [`00bbfca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfa4c.md#insn-00bbfca8)

~~~diff
- 00bbea9c ["INT_ADD", "register:40f0:8", ["const:bbea9c:8", "const:4:8"]]
- 00bbea9c ["CALL", null, ["callee:00c58f50:8"]]
+ 00bbfa90 ["INT_ADD", "register:40f0:8", ["const:bbfa90:8", "const:4:8"]]
+ 00bbfa90 ["CALL", null, ["callee:00c58f50:8"]]
- 00bbea9c bytes 39650294
+ 00bbfa90 bytes 30650294
- 00bbeb00 ["INT_ADD", "register:40f0:8", ["const:bbeb00:8", "const:4:8"]]
- 00bbeb00 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bbfaf4 ["INT_ADD", "register:40f0:8", ["const:bbfaf4:8", "const:4:8"]]
+ 00bbfaf4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bbeb00 bytes 18650294
+ 00bbfaf4 bytes 0f650294
- 00bbecb4 ["INT_ADD", "register:40f0:8", ["const:bbecb4:8", "const:4:8"]]
- 00bbecb4 ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bbfca8 ["INT_ADD", "register:40f0:8", ["const:bbfca8:8", "const:4:8"]]
+ 00bbfca8 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bbecb4 bytes 4b700294
+ 00bbfca8 bytes 42700294
~~~


