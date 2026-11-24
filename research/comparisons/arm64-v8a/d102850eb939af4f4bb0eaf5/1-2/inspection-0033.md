# v16.0.2 → v16.0.3 · 要調査の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-90dc18730340120985e826fd7fd23579"></a>

### [`00b6ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6ced0.md) → [`00b6dec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6dec4.md) _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md) · 呼出先 1件 [`00c5ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba80.md)
- 新版 呼出元 1件 [`00c5ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca40.md) · 呼出先 1件 [`00c5ca50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6ced0.md#insn-00b6d03c)
- 新版 [`00b6e030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6dec4.md#insn-00b6e030)

~~~diff
- 00b6d03c ["INT_ADD", "register:40f0:8", ["const:b6d03c:8", "const:4:8"]]
- 00b6d03c ["CALL", null, ["callee:00c5ca50:8"]]
+ 00b6e030 ["INT_ADD", "register:40f0:8", ["const:b6e030:8", "const:4:8"]]
+ 00b6e030 ["CALL", null, ["callee:00c5ca50:8"]]
- 00b6d03c bytes 91ba0394
+ 00b6e030 bytes 88ba0394
~~~


<a id="compare-f50b292b0e2c0fcd39a8aa9699bbb25f"></a>

### [`00b6d218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d218.md) → [`00b6e20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e20c.md) _ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba10.md) · 呼出先 1件 [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md)
- 新版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9e0.md) · 呼出先 1件 [`00c5ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d218.md#insn-00b6d548)
- 新版 [`00b6e53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e20c.md#insn-00b6e53c)

~~~diff
- 00b6d548 ["INT_ADD", "register:40f0:8", ["const:b6d548:8", "const:4:8"]]
- 00b6d548 ["CALL", null, ["callee:00c5ca40:8"]]
+ 00b6e53c ["INT_ADD", "register:40f0:8", ["const:b6e53c:8", "const:4:8"]]
+ 00b6e53c ["CALL", null, ["callee:00c5ca40:8"]]
- 00b6d548 bytes 4ab90394
+ 00b6e53c bytes 41b90394
~~~


<a id="compare-de947b19bc40743fbc10079f249a30d7"></a>

### [`00b6d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md) → [`00b6e56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e56c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9c0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md)
- 新版 呼出元 1件 [`00c5c990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c990.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cab0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md#insn-00b6d598) · [`00b6d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md#insn-00b6d5a0) · [`00b6d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md#insn-00b6d5c0)
- 新版 [`00b6e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e56c.md#insn-00b6e58c) · [`00b6e594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e56c.md#insn-00b6e594) · [`00b6e5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e56c.md#insn-00b6e5b4)

~~~diff
- 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
- 00b6d598 ["CALL", null, ["callee:00c5cab0:8"]]
+ 00b6e58c ["INT_ADD", "register:40f0:8", ["const:b6e58c:8", "const:4:8"]]
+ 00b6e58c ["CALL", null, ["callee:00c5cab0:8"]]
- 00b6d598 bytes 52b90394
+ 00b6e58c bytes 49b90394
- 00b6d5a0 ["INT_ADD", "register:40f0:8", ["const:b6d5a0:8", "const:4:8"]]
- 00b6d5a0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e594 ["INT_ADD", "register:40f0:8", ["const:b6e594:8", "const:4:8"]]
+ 00b6e594 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d5a0 bytes 78aa0394
+ 00b6e594 bytes 6faa0394
- 00b6d5c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d5c0 ["INT_ADD", "register:40f0:8", ["const:b6d5c0:8", "const:4:8"]]
- 00b6d5c0 ["CALLIND", null, ["register:0:8"]]
+ 00b6e5b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e5b4 ["INT_ADD", "register:40f0:8", ["const:b6e5b4:8", "const:4:8"]]
+ 00b6e5b4 ["CALLIND", null, ["register:0:8"]]
- 00b6d5c0 bytes 00013fd6
+ 00b6e5b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8abc4b574685ae428665b0eb6a93059"></a>

### [`00b6d604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d604.md) → [`00b6e5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e5f8.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b980.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md) [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md)
- 新版 呼出元 1件 [`00c5c950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c950.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c910.md) [`00c5cad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cad0.md) [`00c5cb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d604.md#insn-00b6d634) · [`00b6d65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d604.md#insn-00b6d65c) · [`00b6d664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d604.md#insn-00b6d664)
- 新版 [`00b6e628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e5f8.md#insn-00b6e628) · [`00b6e650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e5f8.md#insn-00b6e650) · [`00b6e658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e5f8.md#insn-00b6e658)

~~~diff
- 00b6d634 ["INT_ADD", "register:40f0:8", ["const:b6d634:8", "const:4:8"]]
- 00b6d634 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e628 ["INT_ADD", "register:40f0:8", ["const:b6e628:8", "const:4:8"]]
+ 00b6e628 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d634 bytes 53aa0394
+ 00b6e628 bytes 4aaa0394
- 00b6d65c ["INT_ADD", "register:40f0:8", ["const:b6d65c:8", "const:4:8"]]
- 00b6d65c ["CALL", null, ["callee:00c5cb20:8"]]
+ 00b6e650 ["INT_ADD", "register:40f0:8", ["const:b6e650:8", "const:4:8"]]
+ 00b6e650 ["CALL", null, ["callee:00c5cb20:8"]]
- 00b6d65c bytes 3db90394
+ 00b6e650 bytes 34b90394
- 00b6d664 ["INT_ADD", "register:40f0:8", ["const:b6d664:8", "const:4:8"]]
- 00b6d664 ["CALL", null, ["callee:00c5c910:8"]]
+ 00b6e658 ["INT_ADD", "register:40f0:8", ["const:b6e658:8", "const:4:8"]]
+ 00b6e658 ["CALL", null, ["callee:00c5c910:8"]]
- 00b6d664 bytes b7b80394
+ 00b6e658 bytes aeb80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a76e3ba470abae536595db3d9535bc6"></a>

### [`00b6d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md) → [`00b6e6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e6e0.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b990.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md) [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md) [`00c5bb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb40.md)
- 新版 呼出元 1件 [`00c5c960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c960.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c910.md) [`00c5c9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9c0.md) [`00c5cb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb00.md) [`00c5cb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md#insn-00b6d71c) · [`00b6d744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md#insn-00b6d744) · [`00b6d74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md#insn-00b6d74c)
- 新版 [`00b6e710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e6e0.md#insn-00b6e710) · [`00b6e738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e6e0.md#insn-00b6e738) · [`00b6e740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e6e0.md#insn-00b6e740)

~~~diff
- 00b6d71c ["INT_ADD", "register:40f0:8", ["const:b6d71c:8", "const:4:8"]]
- 00b6d71c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e710 ["INT_ADD", "register:40f0:8", ["const:b6e710:8", "const:4:8"]]
+ 00b6e710 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d71c bytes 19aa0394
+ 00b6e710 bytes 10aa0394
- 00b6d744 ["INT_ADD", "register:40f0:8", ["const:b6d744:8", "const:4:8"]]
- 00b6d744 ["CALL", null, ["callee:00c5cb10:8"]]
+ 00b6e738 ["INT_ADD", "register:40f0:8", ["const:b6e738:8", "const:4:8"]]
+ 00b6e738 ["CALL", null, ["callee:00c5cb10:8"]]
- 00b6d744 bytes ffb80394
+ 00b6e738 bytes f6b80394
- 00b6d74c ["INT_ADD", "register:40f0:8", ["const:b6d74c:8", "const:4:8"]]
- 00b6d74c ["CALL", null, ["callee:00c5c910:8"]]
+ 00b6e740 ["INT_ADD", "register:40f0:8", ["const:b6e740:8", "const:4:8"]]
+ 00b6e740 ["CALL", null, ["callee:00c5c910:8"]]
- 00b6d74c bytes 7db80394
+ 00b6e740 bytes 74b80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a504a8feba8da894d37ea8004d55335"></a>

### [`00b6d7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md) → [`00b6e7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e7c8.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9b0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5b9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9a0.md) [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md)
- 新版 呼出元 1件 [`00c5c980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c980.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c910.md) [`00c5c970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c970.md) [`00c5cb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md#insn-00b6d800) · [`00b6d820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md#insn-00b6d820) · [`00b6d828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md#insn-00b6d828)
- 新版 [`00b6e7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e7c8.md#insn-00b6e7f4) · [`00b6e814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e7c8.md#insn-00b6e814) · [`00b6e81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e7c8.md#insn-00b6e81c)

~~~diff
- 00b6d800 ["INT_ADD", "register:40f0:8", ["const:b6d800:8", "const:4:8"]]
- 00b6d800 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e7f4 ["INT_ADD", "register:40f0:8", ["const:b6e7f4:8", "const:4:8"]]
+ 00b6e7f4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d800 bytes e0a90394
+ 00b6e7f4 bytes d7a90394
- 00b6d820 ["INT_ADD", "register:40f0:8", ["const:b6d820:8", "const:4:8"]]
- 00b6d820 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e814 ["INT_ADD", "register:40f0:8", ["const:b6e814:8", "const:4:8"]]
+ 00b6e814 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d820 bytes d8a90394
+ 00b6e814 bytes cfa90394
- 00b6d828 ["INT_ADD", "register:40f0:8", ["const:b6d828:8", "const:4:8"]]
- 00b6d828 ["CALL", null, ["callee:00c5c970:8"]]
+ 00b6e81c ["INT_ADD", "register:40f0:8", ["const:b6e81c:8", "const:4:8"]]
+ 00b6e81c ["CALL", null, ["callee:00c5c970:8"]]
- 00b6d828 bytes 5eb80394
+ 00b6e81c bytes 55b80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0e6b088eb8b2119452b4415cd7cf5f"></a>

### [`00b6d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md) → [`00b6e884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e884.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5baf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baf0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md) [`00c5baf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baf0.md)
- 新版 呼出元 1件 [`00c5cac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cac0.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5caa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caa0.md) [`00c5cac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8ac) · [`00b6d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8b8) · [`00b6d8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8c4)
- 新版 [`00b6e8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e884.md#insn-00b6e8a0) · [`00b6e8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e884.md#insn-00b6e8ac) · [`00b6e8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e884.md#insn-00b6e8b8)

~~~diff
- 00b6d8ac ["INT_ADD", "register:40f0:8", ["const:b6d8ac:8", "const:4:8"]]
- 00b6d8ac ["CALL", null, ["callee:00c5cac0:8"]]
+ 00b6e8a0 ["INT_ADD", "register:40f0:8", ["const:b6e8a0:8", "const:4:8"]]
+ 00b6e8a0 ["CALL", null, ["callee:00c5cac0:8"]]
- 00b6d8ac bytes 91b80394
+ 00b6e8a0 bytes 88b80394
- 00b6d8b8 ["INT_ADD", "register:40f0:8", ["const:b6d8b8:8", "const:4:8"]]
- 00b6d8b8 ["CALL", null, ["callee:00c5cac0:8"]]
+ 00b6e8ac ["INT_ADD", "register:40f0:8", ["const:b6e8ac:8", "const:4:8"]]
+ 00b6e8ac ["CALL", null, ["callee:00c5cac0:8"]]
- 00b6d8b8 bytes 8eb80394
+ 00b6e8ac bytes 85b80394
- 00b6d8c4 ["INT_ADD", "register:40f0:8", ["const:b6d8c4:8", "const:4:8"]]
- 00b6d8c4 ["CALL", null, ["callee:00c5caa0:8"]]
+ 00b6e8b8 ["INT_ADD", "register:40f0:8", ["const:b6e8b8:8", "const:4:8"]]
+ 00b6e8b8 ["CALL", null, ["callee:00c5caa0:8"]]
- 00b6d8c4 bytes 83b80394
+ 00b6e8b8 bytes 7ab80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1289f6ce81d31fc2f2ccb2590259411b"></a>

### [`00b6d8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md) → [`00b6e8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e8e0.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md)
- 新版 呼出元 1件 [`00c5caa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caa0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5caa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d908) · [`00b6d914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d914) · [`00b6d924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d924)
- 新版 [`00b6e8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e8e0.md#insn-00b6e8fc) · [`00b6e908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e8e0.md#insn-00b6e908) · [`00b6e918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e8e0.md#insn-00b6e918)

~~~diff
- 00b6d908 ["INT_ADD", "register:40f0:8", ["const:b6d908:8", "const:4:8"]]
- 00b6d908 ["CALL", null, ["callee:00c5caa0:8"]]
+ 00b6e8fc ["INT_ADD", "register:40f0:8", ["const:b6e8fc:8", "const:4:8"]]
+ 00b6e8fc ["CALL", null, ["callee:00c5caa0:8"]]
- 00b6d908 bytes 72b80394
+ 00b6e8fc bytes 69b80394
- 00b6d914 ["INT_ADD", "register:40f0:8", ["const:b6d914:8", "const:4:8"]]
- 00b6d914 ["CALL", null, ["callee:00c5caa0:8"]]
+ 00b6e908 ["INT_ADD", "register:40f0:8", ["const:b6e908:8", "const:4:8"]]
+ 00b6e908 ["CALL", null, ["callee:00c5caa0:8"]]
- 00b6d914 bytes 6fb80394
+ 00b6e908 bytes 66b80394
- 00b6d924 ["INT_ADD", "register:40f0:8", ["const:b6d924:8", "const:4:8"]]
- 00b6d924 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e918 ["INT_ADD", "register:40f0:8", ["const:b6e918:8", "const:4:8"]]
+ 00b6e918 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d924 bytes 97a90394
+ 00b6e918 bytes 8ea90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea530c28d057cd869a005bd76aa46ed"></a>

### [`00b6d94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md) → [`00b6e940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e940.md) _ZNSt6__ndk16__treeINS_12__value_typeImNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareImS8_NS_4lessImEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb80.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb80.md)
- 新版 呼出元 1件 [`00c5cb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb50.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d968) · [`00b6d974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d974) · [`00b6d984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d984)
- 新版 [`00b6e95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e940.md#insn-00b6e95c) · [`00b6e968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e940.md#insn-00b6e968) · [`00b6e978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e940.md#insn-00b6e978)

~~~diff
- 00b6d968 ["INT_ADD", "register:40f0:8", ["const:b6d968:8", "const:4:8"]]
- 00b6d968 ["CALL", null, ["callee:00c5cb50:8"]]
+ 00b6e95c ["INT_ADD", "register:40f0:8", ["const:b6e95c:8", "const:4:8"]]
+ 00b6e95c ["CALL", null, ["callee:00c5cb50:8"]]
- 00b6d968 bytes 86b80394
+ 00b6e95c bytes 7db80394
- 00b6d974 ["INT_ADD", "register:40f0:8", ["const:b6d974:8", "const:4:8"]]
- 00b6d974 ["CALL", null, ["callee:00c5cb50:8"]]
+ 00b6e968 ["INT_ADD", "register:40f0:8", ["const:b6e968:8", "const:4:8"]]
+ 00b6e968 ["CALL", null, ["callee:00c5cb50:8"]]
- 00b6d974 bytes 83b80394
+ 00b6e968 bytes 7ab80394
- 00b6d984 ["INT_ADD", "register:40f0:8", ["const:b6d984:8", "const:4:8"]]
- 00b6d984 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6e978 ["INT_ADD", "register:40f0:8", ["const:b6e978:8", "const:4:8"]]
+ 00b6e978 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6d984 bytes 7fa90394
+ 00b6e978 bytes 76a90394
~~~


<a id="compare-1952d6c7792231b12f8d54155ed85c25"></a>

### [`00b6d99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md) → [`00b6e990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e990.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb90.md)
- 新版 呼出元 1件 [`00c5cb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb60.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md#insn-00b6d9b8) · [`00b6d9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md#insn-00b6d9c4)
- 新版 [`00b6e9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e990.md#insn-00b6e9ac) · [`00b6e9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e990.md#insn-00b6e9b8)

~~~diff
- 00b6d9b8 ["INT_ADD", "register:40f0:8", ["const:b6d9b8:8", "const:4:8"]]
- 00b6d9b8 ["CALL", null, ["callee:00c5cb60:8"]]
+ 00b6e9ac ["INT_ADD", "register:40f0:8", ["const:b6e9ac:8", "const:4:8"]]
+ 00b6e9ac ["CALL", null, ["callee:00c5cb60:8"]]
- 00b6d9b8 bytes 76b80394
+ 00b6e9ac bytes 6db80394
- 00b6d9c4 ["INT_ADD", "register:40f0:8", ["const:b6d9c4:8", "const:4:8"]]
- 00b6d9c4 ["CALL", null, ["callee:00c5cb60:8"]]
+ 00b6e9b8 ["INT_ADD", "register:40f0:8", ["const:b6e9b8:8", "const:4:8"]]
+ 00b6e9b8 ["CALL", null, ["callee:00c5cb60:8"]]
- 00b6d9c4 bytes 73b80394
+ 00b6e9b8 bytes 6ab80394
~~~


<a id="compare-20aee2c57a803aa62a06e2593af9818c"></a>

### [`00b6d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md) → [`00b6e9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e9d0.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bba0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bba0.md)
- 新版 呼出元 1件 [`00c5cb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb70.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md#insn-00b6d9f8) · [`00b6da04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md#insn-00b6da04)
- 新版 [`00b6e9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e9d0.md#insn-00b6e9ec) · [`00b6e9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6e9d0.md#insn-00b6e9f8)

~~~diff
- 00b6d9f8 ["INT_ADD", "register:40f0:8", ["const:b6d9f8:8", "const:4:8"]]
- 00b6d9f8 ["CALL", null, ["callee:00c5cb70:8"]]
+ 00b6e9ec ["INT_ADD", "register:40f0:8", ["const:b6e9ec:8", "const:4:8"]]
+ 00b6e9ec ["CALL", null, ["callee:00c5cb70:8"]]
- 00b6d9f8 bytes 6ab80394
+ 00b6e9ec bytes 61b80394
- 00b6da04 ["INT_ADD", "register:40f0:8", ["const:b6da04:8", "const:4:8"]]
- 00b6da04 ["CALL", null, ["callee:00c5cb70:8"]]
+ 00b6e9f8 ["INT_ADD", "register:40f0:8", ["const:b6e9f8:8", "const:4:8"]]
+ 00b6e9f8 ["CALL", null, ["callee:00c5cb70:8"]]
- 00b6da04 bytes 67b80394
+ 00b6e9f8 bytes 5eb80394
~~~


<a id="compare-1975303fb5d3645c3aa3e0fd6ef721bf"></a>

### [`00b6da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md) → [`00b6ea10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea10.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md)
- 新版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cab0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6da38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md#insn-00b6da38) · [`00b6da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md#insn-00b6da44)
- 新版 [`00b6ea2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea10.md#insn-00b6ea2c) · [`00b6ea38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea10.md#insn-00b6ea38)

~~~diff
- 00b6da38 ["INT_ADD", "register:40f0:8", ["const:b6da38:8", "const:4:8"]]
- 00b6da38 ["CALL", null, ["callee:00c5cab0:8"]]
+ 00b6ea2c ["INT_ADD", "register:40f0:8", ["const:b6ea2c:8", "const:4:8"]]
+ 00b6ea2c ["CALL", null, ["callee:00c5cab0:8"]]
- 00b6da38 bytes 2ab80394
+ 00b6ea2c bytes 21b80394
- 00b6da44 ["INT_ADD", "register:40f0:8", ["const:b6da44:8", "const:4:8"]]
- 00b6da44 ["CALL", null, ["callee:00c5cab0:8"]]
+ 00b6ea38 ["INT_ADD", "register:40f0:8", ["const:b6ea38:8", "const:4:8"]]
+ 00b6ea38 ["CALL", null, ["callee:00c5cab0:8"]]
- 00b6da44 bytes 27b80394
+ 00b6ea38 bytes 1eb80394
~~~


<a id="compare-872f70c29b485fd3e702dbe202551bd4"></a>

### [`00b6da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md) → [`00b6ea50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea50.md) _ZN11flatbuffers10DefinitionD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)
- 新版 呼出元 1件 [`00c5c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c910.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5caf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6da88) · [`00b6da94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6da94) · [`00b6dad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6dad0)
- 新版 [`00b6ea7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea50.md#insn-00b6ea7c) · [`00b6ea88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea50.md#insn-00b6ea88) · [`00b6eac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ea50.md#insn-00b6eac4)

~~~diff
- 00b6da88 ["INT_ADD", "register:40f0:8", ["const:b6da88:8", "const:4:8"]]
- 00b6da88 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ea7c ["INT_ADD", "register:40f0:8", ["const:b6ea7c:8", "const:4:8"]]
+ 00b6ea7c ["CALL", null, ["callee:00c58f50:8"]]
- 00b6da88 bytes 3ea90394
+ 00b6ea7c bytes 35a90394
- 00b6da94 ["INT_ADD", "register:40f0:8", ["const:b6da94:8", "const:4:8"]]
- 00b6da94 ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b6ea88 ["INT_ADD", "register:40f0:8", ["const:b6ea88:8", "const:4:8"]]
+ 00b6ea88 ["CALL", null, ["callee:00c5caf0:8"]]
- 00b6da94 bytes 23b80394
+ 00b6ea88 bytes 1ab80394
- 00b6dad0 ["INT_ADD", "register:40f0:8", ["const:b6dad0:8", "const:4:8"]]
- 00b6dad0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6eac4 ["INT_ADD", "register:40f0:8", ["const:b6eac4:8", "const:4:8"]]
+ 00b6eac4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dad0 bytes 2ca90394
+ 00b6eac4 bytes 23a90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab1c96f2355bcfc8d1ca8351345f5654"></a>

### [`00b6db70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md) → [`00b6eb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eb64.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md)
- 新版 呼出元 1件 [`00c5cb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb20.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6db8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6db8c) · [`00b6db98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6db98) · [`00b6dba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6dba8)
- 新版 [`00b6eb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eb64.md#insn-00b6eb80) · [`00b6eb8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eb64.md#insn-00b6eb8c) · [`00b6eb9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eb64.md#insn-00b6eb9c)

~~~diff
- 00b6db8c ["INT_ADD", "register:40f0:8", ["const:b6db8c:8", "const:4:8"]]
- 00b6db8c ["CALL", null, ["callee:00c5cb20:8"]]
+ 00b6eb80 ["INT_ADD", "register:40f0:8", ["const:b6eb80:8", "const:4:8"]]
+ 00b6eb80 ["CALL", null, ["callee:00c5cb20:8"]]
- 00b6db8c bytes f1b70394
+ 00b6eb80 bytes e8b70394
- 00b6db98 ["INT_ADD", "register:40f0:8", ["const:b6db98:8", "const:4:8"]]
- 00b6db98 ["CALL", null, ["callee:00c5cb20:8"]]
+ 00b6eb8c ["INT_ADD", "register:40f0:8", ["const:b6eb8c:8", "const:4:8"]]
+ 00b6eb8c ["CALL", null, ["callee:00c5cb20:8"]]
- 00b6db98 bytes eeb70394
+ 00b6eb8c bytes e5b70394
- 00b6dba8 ["INT_ADD", "register:40f0:8", ["const:b6dba8:8", "const:4:8"]]
- 00b6dba8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6eb9c ["INT_ADD", "register:40f0:8", ["const:b6eb9c:8", "const:4:8"]]
+ 00b6eb9c ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dba8 bytes f6a80394
+ 00b6eb9c bytes eda80394
~~~


<a id="compare-9e54707da076377ec2ebd170ad9f4610"></a>

### [`00b6dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dbc0.md) → [`00b6ebb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ebb4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)
- 新版 呼出元 1件 [`00c5caf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caf0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5caf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dbc0.md#insn-00b6dbdc) · [`00b6dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dbc0.md#insn-00b6dbe8) · [`00b6dbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dbc0.md#insn-00b6dbf8)
- 新版 [`00b6ebd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ebb4.md#insn-00b6ebd0) · [`00b6ebdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ebb4.md#insn-00b6ebdc) · [`00b6ebec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ebb4.md#insn-00b6ebec)

~~~diff
- 00b6dbdc ["INT_ADD", "register:40f0:8", ["const:b6dbdc:8", "const:4:8"]]
- 00b6dbdc ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b6ebd0 ["INT_ADD", "register:40f0:8", ["const:b6ebd0:8", "const:4:8"]]
+ 00b6ebd0 ["CALL", null, ["callee:00c5caf0:8"]]
- 00b6dbdc bytes d1b70394
+ 00b6ebd0 bytes c8b70394
- 00b6dbe8 ["INT_ADD", "register:40f0:8", ["const:b6dbe8:8", "const:4:8"]]
- 00b6dbe8 ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b6ebdc ["INT_ADD", "register:40f0:8", ["const:b6ebdc:8", "const:4:8"]]
+ 00b6ebdc ["CALL", null, ["callee:00c5caf0:8"]]
- 00b6dbe8 bytes ceb70394
+ 00b6ebdc bytes c5b70394
- 00b6dbf8 ["INT_ADD", "register:40f0:8", ["const:b6dbf8:8", "const:4:8"]]
- 00b6dbf8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ebec ["INT_ADD", "register:40f0:8", ["const:b6ebec:8", "const:4:8"]]
+ 00b6ebec ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dbf8 bytes e2a80394
+ 00b6ebec bytes d9a80394
~~~


<a id="compare-e0027ceffca7c77357570bc008d3b77e"></a>

### [`00b6dc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc10.md) → [`00b6ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec04.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md)
- 新版 呼出元 1件 [`00c5cad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cad0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc10.md#insn-00b6dc2c) · [`00b6dc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc10.md#insn-00b6dc38) · [`00b6dc48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc10.md#insn-00b6dc48)
- 新版 [`00b6ec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec04.md#insn-00b6ec20) · [`00b6ec2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec04.md#insn-00b6ec2c) · [`00b6ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec04.md#insn-00b6ec3c)

~~~diff
- 00b6dc2c ["INT_ADD", "register:40f0:8", ["const:b6dc2c:8", "const:4:8"]]
- 00b6dc2c ["CALL", null, ["callee:00c5cad0:8"]]
+ 00b6ec20 ["INT_ADD", "register:40f0:8", ["const:b6ec20:8", "const:4:8"]]
+ 00b6ec20 ["CALL", null, ["callee:00c5cad0:8"]]
- 00b6dc2c bytes b5b70394
+ 00b6ec20 bytes acb70394
- 00b6dc38 ["INT_ADD", "register:40f0:8", ["const:b6dc38:8", "const:4:8"]]
- 00b6dc38 ["CALL", null, ["callee:00c5cad0:8"]]
+ 00b6ec2c ["INT_ADD", "register:40f0:8", ["const:b6ec2c:8", "const:4:8"]]
+ 00b6ec2c ["CALL", null, ["callee:00c5cad0:8"]]
- 00b6dc38 bytes b2b70394
+ 00b6ec2c bytes a9b70394
- 00b6dc48 ["INT_ADD", "register:40f0:8", ["const:b6dc48:8", "const:4:8"]]
- 00b6dc48 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ec3c ["INT_ADD", "register:40f0:8", ["const:b6ec3c:8", "const:4:8"]]
+ 00b6ec3c ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dc48 bytes cea80394
+ 00b6ec3c bytes c5a80394
~~~


<a id="compare-9f0e3846da46b0b8f5785e334475aab1"></a>

### [`00b6dc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc60.md) → [`00b6ec54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec54.md) _ZN11flatbuffers7EnumValD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)
- 新版 呼出元 1件 [`00c5c9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9c0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5caf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5caf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc60.md#insn-00b6dc8c) · [`00b6dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc60.md#insn-00b6dc98) · [`00b6dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc60.md#insn-00b6dcd4)
- 新版 [`00b6ec80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec54.md#insn-00b6ec80) · [`00b6ec8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec54.md#insn-00b6ec8c) · [`00b6ecc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ec54.md#insn-00b6ecc8)

~~~diff
- 00b6dc8c ["INT_ADD", "register:40f0:8", ["const:b6dc8c:8", "const:4:8"]]
- 00b6dc8c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ec80 ["INT_ADD", "register:40f0:8", ["const:b6ec80:8", "const:4:8"]]
+ 00b6ec80 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dc8c bytes bda80394
+ 00b6ec80 bytes b4a80394
- 00b6dc98 ["INT_ADD", "register:40f0:8", ["const:b6dc98:8", "const:4:8"]]
- 00b6dc98 ["CALL", null, ["callee:00c5caf0:8"]]
+ 00b6ec8c ["INT_ADD", "register:40f0:8", ["const:b6ec8c:8", "const:4:8"]]
+ 00b6ec8c ["CALL", null, ["callee:00c5caf0:8"]]
- 00b6dc98 bytes a2b70394
+ 00b6ec8c bytes 99b70394
- 00b6dcd4 ["INT_ADD", "register:40f0:8", ["const:b6dcd4:8", "const:4:8"]]
- 00b6dcd4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ecc8 ["INT_ADD", "register:40f0:8", ["const:b6ecc8:8", "const:4:8"]]
+ 00b6ecc8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dcd4 bytes aba80394
+ 00b6ecc8 bytes a2a80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f3efd315de7a4adb5c9e1291c4f1056"></a>

### [`00b6dd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dd5c.md) → [`00b6ed50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ed50.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb40.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb40.md)
- 新版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb10.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dd5c.md#insn-00b6dd78) · [`00b6dd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dd5c.md#insn-00b6dd84) · [`00b6dd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dd5c.md#insn-00b6dd94)
- 新版 [`00b6ed6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ed50.md#insn-00b6ed6c) · [`00b6ed78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ed50.md#insn-00b6ed78) · [`00b6ed88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ed50.md#insn-00b6ed88)

~~~diff
- 00b6dd78 ["INT_ADD", "register:40f0:8", ["const:b6dd78:8", "const:4:8"]]
- 00b6dd78 ["CALL", null, ["callee:00c5cb10:8"]]
+ 00b6ed6c ["INT_ADD", "register:40f0:8", ["const:b6ed6c:8", "const:4:8"]]
+ 00b6ed6c ["CALL", null, ["callee:00c5cb10:8"]]
- 00b6dd78 bytes 72b70394
+ 00b6ed6c bytes 69b70394
- 00b6dd84 ["INT_ADD", "register:40f0:8", ["const:b6dd84:8", "const:4:8"]]
- 00b6dd84 ["CALL", null, ["callee:00c5cb10:8"]]
+ 00b6ed78 ["INT_ADD", "register:40f0:8", ["const:b6ed78:8", "const:4:8"]]
+ 00b6ed78 ["CALL", null, ["callee:00c5cb10:8"]]
- 00b6dd84 bytes 6fb70394
+ 00b6ed78 bytes 66b70394
- 00b6dd94 ["INT_ADD", "register:40f0:8", ["const:b6dd94:8", "const:4:8"]]
- 00b6dd94 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ed88 ["INT_ADD", "register:40f0:8", ["const:b6ed88:8", "const:4:8"]]
+ 00b6ed88 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dd94 bytes 7ba80394
+ 00b6ed88 bytes 72a80394
~~~


<a id="compare-a0362015e93b43be57b89a90983aea89"></a>

### [`00b6ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddac.md) → [`00b6eda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eda0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md)
- 新版 呼出元 1件 [`00c5cb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb00.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ddc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddac.md#insn-00b6ddc8) · [`00b6ddd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddac.md#insn-00b6ddd4) · [`00b6dde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddac.md#insn-00b6dde4)
- 新版 [`00b6edbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eda0.md#insn-00b6edbc) · [`00b6edc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eda0.md#insn-00b6edc8) · [`00b6edd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eda0.md#insn-00b6edd8)

~~~diff
- 00b6ddc8 ["INT_ADD", "register:40f0:8", ["const:b6ddc8:8", "const:4:8"]]
- 00b6ddc8 ["CALL", null, ["callee:00c5cb00:8"]]
+ 00b6edbc ["INT_ADD", "register:40f0:8", ["const:b6edbc:8", "const:4:8"]]
+ 00b6edbc ["CALL", null, ["callee:00c5cb00:8"]]
- 00b6ddc8 bytes 5ab70394
+ 00b6edbc bytes 51b70394
- 00b6ddd4 ["INT_ADD", "register:40f0:8", ["const:b6ddd4:8", "const:4:8"]]
- 00b6ddd4 ["CALL", null, ["callee:00c5cb00:8"]]
+ 00b6edc8 ["INT_ADD", "register:40f0:8", ["const:b6edc8:8", "const:4:8"]]
+ 00b6edc8 ["CALL", null, ["callee:00c5cb00:8"]]
- 00b6ddd4 bytes 57b70394
+ 00b6edc8 bytes 4eb70394
- 00b6dde4 ["INT_ADD", "register:40f0:8", ["const:b6dde4:8", "const:4:8"]]
- 00b6dde4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6edd8 ["INT_ADD", "register:40f0:8", ["const:b6edd8:8", "const:4:8"]]
+ 00b6edd8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dde4 bytes 67a80394
+ 00b6edd8 bytes 5ea80394
~~~


<a id="compare-c120d63d7f8b0d8217f81f836f47df7a"></a>

### [`00b6ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md) → [`00b6edf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6edf0.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9a0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md)
- 新版 呼出元 1件 [`00c5c970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c970.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c910.md) [`00c5cb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de28) · [`00b6de48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de48) · [`00b6de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de50)
- 新版 [`00b6ee1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6edf0.md#insn-00b6ee1c) · [`00b6ee3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6edf0.md#insn-00b6ee3c) · [`00b6ee44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6edf0.md#insn-00b6ee44)

~~~diff
- 00b6de28 ["INT_ADD", "register:40f0:8", ["const:b6de28:8", "const:4:8"]]
- 00b6de28 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ee1c ["INT_ADD", "register:40f0:8", ["const:b6ee1c:8", "const:4:8"]]
+ 00b6ee1c ["CALL", null, ["callee:00c58f50:8"]]
- 00b6de28 bytes 56a80394
+ 00b6ee1c bytes 4da80394
- 00b6de48 ["INT_ADD", "register:40f0:8", ["const:b6de48:8", "const:4:8"]]
- 00b6de48 ["CALL", null, ["callee:00c5c910:8"]]
+ 00b6ee3c ["INT_ADD", "register:40f0:8", ["const:b6ee3c:8", "const:4:8"]]
+ 00b6ee3c ["CALL", null, ["callee:00c5c910:8"]]
- 00b6de48 bytes beb60394
+ 00b6ee3c bytes b5b60394
- 00b6de50 ["INT_ADD", "register:40f0:8", ["const:b6de50:8", "const:4:8"]]
- 00b6de50 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ee44 ["INT_ADD", "register:40f0:8", ["const:b6ee44:8", "const:4:8"]]
+ 00b6ee44 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6de50 bytes 4ca80394
+ 00b6ee44 bytes 43a80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f962d9ebd112093a1a2184788be9f6a9"></a>

### [`00b6de8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md) → [`00b6ee80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ee80.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md)
- 新版 呼出元 1件 [`00c5cb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb30.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6dea8) · [`00b6deb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6deb4) · [`00b6dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6dec4)
- 新版 [`00b6ee9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ee80.md#insn-00b6ee9c) · [`00b6eea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ee80.md#insn-00b6eea8) · [`00b6eeb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ee80.md#insn-00b6eeb8)

~~~diff
- 00b6dea8 ["INT_ADD", "register:40f0:8", ["const:b6dea8:8", "const:4:8"]]
- 00b6dea8 ["CALL", null, ["callee:00c5cb30:8"]]
+ 00b6ee9c ["INT_ADD", "register:40f0:8", ["const:b6ee9c:8", "const:4:8"]]
+ 00b6ee9c ["CALL", null, ["callee:00c5cb30:8"]]
- 00b6dea8 bytes 2eb70394
+ 00b6ee9c bytes 25b70394
- 00b6deb4 ["INT_ADD", "register:40f0:8", ["const:b6deb4:8", "const:4:8"]]
- 00b6deb4 ["CALL", null, ["callee:00c5cb30:8"]]
+ 00b6eea8 ["INT_ADD", "register:40f0:8", ["const:b6eea8:8", "const:4:8"]]
+ 00b6eea8 ["CALL", null, ["callee:00c5cb30:8"]]
- 00b6deb4 bytes 2bb70394
+ 00b6eea8 bytes 22b70394
- 00b6dec4 ["INT_ADD", "register:40f0:8", ["const:b6dec4:8", "const:4:8"]]
- 00b6dec4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6eeb8 ["INT_ADD", "register:40f0:8", ["const:b6eeb8:8", "const:4:8"]]
+ 00b6eeb8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6dec4 bytes 2fa80394
+ 00b6eeb8 bytes 26a80394
~~~


<a id="compare-aeba241622574de385296e08dc541f85"></a>

### [`00b6dedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md) → [`00b6eed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eed0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md)
- 新版 呼出元 1件 [`00c5cb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb40.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6def8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6def8) · [`00b6df04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6df04) · [`00b6df14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6df14)
- 新版 [`00b6eeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eed0.md#insn-00b6eeec) · [`00b6eef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eed0.md#insn-00b6eef8) · [`00b6ef08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eed0.md#insn-00b6ef08)

~~~diff
- 00b6def8 ["INT_ADD", "register:40f0:8", ["const:b6def8:8", "const:4:8"]]
- 00b6def8 ["CALL", null, ["callee:00c5cb40:8"]]
+ 00b6eeec ["INT_ADD", "register:40f0:8", ["const:b6eeec:8", "const:4:8"]]
+ 00b6eeec ["CALL", null, ["callee:00c5cb40:8"]]
- 00b6def8 bytes 1eb70394
+ 00b6eeec bytes 15b70394
- 00b6df04 ["INT_ADD", "register:40f0:8", ["const:b6df04:8", "const:4:8"]]
- 00b6df04 ["CALL", null, ["callee:00c5cb40:8"]]
+ 00b6eef8 ["INT_ADD", "register:40f0:8", ["const:b6eef8:8", "const:4:8"]]
+ 00b6eef8 ["CALL", null, ["callee:00c5cb40:8"]]
- 00b6df04 bytes 1bb70394
+ 00b6eef8 bytes 12b70394
- 00b6df14 ["INT_ADD", "register:40f0:8", ["const:b6df14:8", "const:4:8"]]
- 00b6df14 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ef08 ["INT_ADD", "register:40f0:8", ["const:b6ef08:8", "const:4:8"]]
+ 00b6ef08 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6df14 bytes 1ba80394
+ 00b6ef08 bytes 12a80394
~~~


<a id="compare-d2e69a522cdf02379a2f30b25ffaef99"></a>

### [`00b6df2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md) → [`00b6ef20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef20.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb10.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb10.md)
- 新版 呼出元 1件 [`00c5cae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cae0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6df48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df48) · [`00b6df54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df54) · [`00b6df64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df64)
- 新版 [`00b6ef3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef20.md#insn-00b6ef3c) · [`00b6ef48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef20.md#insn-00b6ef48) · [`00b6ef58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef20.md#insn-00b6ef58)

~~~diff
- 00b6df48 ["INT_ADD", "register:40f0:8", ["const:b6df48:8", "const:4:8"]]
- 00b6df48 ["CALL", null, ["callee:00c5cae0:8"]]
+ 00b6ef3c ["INT_ADD", "register:40f0:8", ["const:b6ef3c:8", "const:4:8"]]
+ 00b6ef3c ["CALL", null, ["callee:00c5cae0:8"]]
- 00b6df48 bytes f2b60394
+ 00b6ef3c bytes e9b60394
- 00b6df54 ["INT_ADD", "register:40f0:8", ["const:b6df54:8", "const:4:8"]]
- 00b6df54 ["CALL", null, ["callee:00c5cae0:8"]]
+ 00b6ef48 ["INT_ADD", "register:40f0:8", ["const:b6ef48:8", "const:4:8"]]
+ 00b6ef48 ["CALL", null, ["callee:00c5cae0:8"]]
- 00b6df54 bytes efb60394
+ 00b6ef48 bytes e6b60394
- 00b6df64 ["INT_ADD", "register:40f0:8", ["const:b6df64:8", "const:4:8"]]
- 00b6df64 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6ef58 ["INT_ADD", "register:40f0:8", ["const:b6ef58:8", "const:4:8"]]
+ 00b6ef58 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6df64 bytes 07a80394
+ 00b6ef58 bytes fea70394
~~~


<a id="compare-85e841efa4777ddcd526ab38b8d4e9b6"></a>

### [`00b6e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md) → [`00b6f6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f6c4.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5c010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c010.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cfe0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6e744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md#insn-00b6e744) · [`00b6e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md#insn-00b6e768)
- 新版 [`00b6f738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f6c4.md#insn-00b6f738) · [`00b6f75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f6c4.md#insn-00b6f75c)

~~~diff
- 00b6e744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e744 ["INT_ADD", "register:40f0:8", ["const:b6e744:8", "const:4:8"]]
- 00b6e744 ["CALLIND", null, ["register:0:8"]]
+ 00b6f738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6f738 ["INT_ADD", "register:40f0:8", ["const:b6f738:8", "const:4:8"]]
+ 00b6f738 ["CALLIND", null, ["register:0:8"]]
- 00b6e744 bytes 00013fd6
+ 00b6f738 bytes 00013fd6
- 00b6e768 ["INT_ADD", "register:40f0:8", ["const:b6e768:8", "const:4:8"]]
- 00b6e768 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b6f75c ["INT_ADD", "register:40f0:8", ["const:b6f75c:8", "const:4:8"]]
+ 00b6f75c ["CALL", null, ["callee:00c58f80:8"]]
- 00b6e768 bytes 12a60394
+ 00b6f75c bytes 09a60394
~~~


<a id="compare-42dbf3da4d6f2a6aa8dc16e856a77a79"></a>

### [`00b6f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md) → [`00b7005c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7005c.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f094) · [`00b6f0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f0e8) · [`00b6f110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f110)
- 新版 [`00b70088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7005c.md#insn-00b70088) · [`00b700dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7005c.md#insn-00b700dc) · [`00b70104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7005c.md#insn-00b70104)

~~~diff
- 00b6f094 ["INT_ADD", "register:40f0:8", ["const:b6f094:8", "const:4:8"]]
- 00b6f094 ["CALL", null, ["callee:00c59080:8"]]
+ 00b70088 ["INT_ADD", "register:40f0:8", ["const:b70088:8", "const:4:8"]]
+ 00b70088 ["CALL", null, ["callee:00c59080:8"]]
- 00b6f094 bytes 07a40394
+ 00b70088 bytes fea30394
- 00b6f0e8 ["INT_ADD", "register:40f0:8", ["const:b6f0e8:8", "const:4:8"]]
- 00b6f0e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b700dc ["INT_ADD", "register:40f0:8", ["const:b700dc:8", "const:4:8"]]
+ 00b700dc ["CALL", null, ["callee:00c58f30:8"]]
- 00b6f0e8 bytes 9ea30394
+ 00b700dc bytes 95a30394
- 00b6f110 ["INT_ADD", "register:40f0:8", ["const:b6f110:8", "const:4:8"]]
- 00b6f110 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b70104 ["INT_ADD", "register:40f0:8", ["const:b70104:8", "const:4:8"]]
+ 00b70104 ["CALL", null, ["callee:00c590a0:8"]]
- 00b6f110 bytes f0a30394
+ 00b70104 bytes e7a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15168dde60917d83eac5a94f4e425cc2"></a>

### [`00b6f380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md) → [`00b70374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70374.md) _ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3bc) · [`00b6f3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3d0) · [`00b6f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3e0)
- 新版 [`00b703b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70374.md#insn-00b703b0) · [`00b703c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70374.md#insn-00b703c4) · [`00b703d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70374.md#insn-00b703d4)

~~~diff
- 00b6f3bc ["INT_ADD", "register:40f0:8", ["const:b6f3bc:8", "const:4:8"]]
- 00b6f3bc ["CALL", null, ["callee:0054a974:8"]]
+ 00b703b0 ["INT_ADD", "register:40f0:8", ["const:b703b0:8", "const:4:8"]]
+ 00b703b0 ["CALL", null, ["callee:0054a974:8"]]
- 00b6f3bc bytes a66ce797
+ 00b703b0 bytes 7169e797
- 00b6f3d0 ["INT_ADD", "register:40f0:8", ["const:b6f3d0:8", "const:4:8"]]
- 00b6f3d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b703c4 ["INT_ADD", "register:40f0:8", ["const:b703c4:8", "const:4:8"]]
+ 00b703c4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b6f3d0 bytes e4a20394
+ 00b703c4 bytes dba20394
- 00b6f3e0 ["INT_ADD", "register:40f0:8", ["const:b6f3e0:8", "const:4:8"]]
- 00b6f3e0 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b703d4 ["INT_ADD", "register:40f0:8", ["const:b703d4:8", "const:4:8"]]
+ 00b703d4 ["CALL", null, ["callee:00c5c650:8"]]
- 00b6f3e0 bytes a8b00394
+ 00b703d4 bytes 9fb00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb320244cb2fbec6504b50fa4adddb2f"></a>

### [`00b6f454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md) → [`00b70448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70448.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb10.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5dae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dae0.md) · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f53c) · [`00b6f588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f588) · [`00b6f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f5b0)
- 新版 [`00b70530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70448.md#insn-00b70530) · [`00b7057c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70448.md#insn-00b7057c) · [`00b705a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70448.md#insn-00b705a4)

~~~diff
- 00b6f53c ["INT_ADD", "register:40f0:8", ["const:b6f53c:8", "const:4:8"]]
- 00b6f53c ["CALL", null, ["callee:00c59020:8"]]
+ 00b70530 ["INT_ADD", "register:40f0:8", ["const:b70530:8", "const:4:8"]]
+ 00b70530 ["CALL", null, ["callee:00c59020:8"]]
- 00b6f53c bytes c5a20394
+ 00b70530 bytes bca20394
- 00b6f588 ["INT_ADD", "register:40f0:8", ["const:b6f588:8", "const:4:8"]]
- 00b6f588 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b7057c ["INT_ADD", "register:40f0:8", ["const:b7057c:8", "const:4:8"]]
+ 00b7057c ["CALL", null, ["callee:00c5b980:8"]]
- 00b6f588 bytes 0aad0394
+ 00b7057c bytes 01ad0394
- 00b6f5b0 ["INT_ADD", "register:40f0:8", ["const:b6f5b0:8", "const:4:8"]]
- 00b6f5b0 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b705a4 ["INT_ADD", "register:40f0:8", ["const:b705a4:8", "const:4:8"]]
+ 00b705a4 ["CALL", null, ["callee:00c5c650:8"]]
- 00b6f5b0 bytes 34b00394
+ 00b705a4 bytes 2bb00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d58e2980921411975027928e879b8a7"></a>

### [`00b70f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b70/00b70f98.md) → [`00b71f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b71/00b71f8c.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8c0.md) · 呼出先 1件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)
- 新版 呼出元 1件 [`00c5d890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d890.md) · 呼出先 1件 [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b70/00b70f98.md#insn-00b71084) · [`00b71150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b70/00b70f98.md#insn-00b71150)
- 新版 [`00b72078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b71/00b71f8c.md#insn-00b72078) · [`00b72144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b71/00b71f8c.md#insn-00b72144)

~~~diff
- 00b71084 ["INT_ADD", "register:40f0:8", ["const:b71084:8", "const:4:8"]]
- 00b71084 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b72078 ["INT_ADD", "register:40f0:8", ["const:b72078:8", "const:4:8"]]
+ 00b72078 ["CALL", null, ["callee:00c5b980:8"]]
- 00b71084 bytes 4ba60394
+ 00b72078 bytes 42a60394
- 00b71150 ["INT_ADD", "register:40f0:8", ["const:b71150:8", "const:4:8"]]
- 00b71150 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b72144 ["INT_ADD", "register:40f0:8", ["const:b72144:8", "const:4:8"]]
+ 00b72144 ["CALL", null, ["callee:00c5b980:8"]]
- 00b71150 bytes 18a60394
+ 00b72144 bytes 0fa60394
~~~


<a id="compare-9923dbe88c45a2dc70799bf922128fb0"></a>

### [`00b711a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md) → [`00b72198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72198.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b711c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b711c8) · [`00b7120c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b7120c) · [`00b71234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b71234)
- 新版 [`00b721bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72198.md#insn-00b721bc) · [`00b72200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72198.md#insn-00b72200) · [`00b72228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72198.md#insn-00b72228)

~~~diff
- 00b711c8 ["INT_ADD", "register:40f0:8", ["const:b711c8:8", "const:4:8"]]
- 00b711c8 ["CALL", null, ["callee:00c59080:8"]]
+ 00b721bc ["INT_ADD", "register:40f0:8", ["const:b721bc:8", "const:4:8"]]
+ 00b721bc ["CALL", null, ["callee:00c59080:8"]]
- 00b711c8 bytes ba9b0394
+ 00b721bc bytes b19b0394
- 00b7120c ["INT_ADD", "register:40f0:8", ["const:b7120c:8", "const:4:8"]]
- 00b7120c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b72200 ["INT_ADD", "register:40f0:8", ["const:b72200:8", "const:4:8"]]
+ 00b72200 ["CALL", null, ["callee:00c590f0:8"]]
- 00b7120c bytes c59b0394
+ 00b72200 bytes bc9b0394
- 00b71234 ["INT_ADD", "register:40f0:8", ["const:b71234:8", "const:4:8"]]
- 00b71234 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b72228 ["INT_ADD", "register:40f0:8", ["const:b72228:8", "const:4:8"]]
+ 00b72228 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b71234 bytes f7a70394
+ 00b72228 bytes eea70394
~~~


<a id="compare-b911838384b8ed5efc49570553dba555"></a>

### [`00b716f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b716f8.md) → [`00b726ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b726ec.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c520.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)
- 新版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d4f0.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b716f8.md#insn-00b71798) · [`00b717e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b716f8.md#insn-00b717e4) · [`00b7184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b716f8.md#insn-00b7184c)
- 新版 [`00b7278c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b726ec.md#insn-00b7278c) · [`00b727d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b726ec.md#insn-00b727d8) · [`00b72840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b726ec.md#insn-00b72840)

~~~diff
- 00b71798 ["INT_ADD", "register:40f0:8", ["const:b71798:8", "const:4:8"]]
- 00b71798 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7278c ["INT_ADD", "register:40f0:8", ["const:b7278c:8", "const:4:8"]]
+ 00b7278c ["CALL", null, ["callee:00c59020:8"]]
- 00b71798 bytes 2e9a0394
+ 00b7278c bytes 259a0394
- 00b717e4 ["INT_ADD", "register:40f0:8", ["const:b717e4:8", "const:4:8"]]
- 00b717e4 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b727d8 ["INT_ADD", "register:40f0:8", ["const:b727d8:8", "const:4:8"]]
+ 00b727d8 ["CALL", null, ["callee:00c5b980:8"]]
- 00b717e4 bytes 73a40394
+ 00b727d8 bytes 6aa40394
- 00b7184c ["INT_ADD", "register:40f0:8", ["const:b7184c:8", "const:4:8"]]
- 00b7184c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00b72840 ["INT_ADD", "register:40f0:8", ["const:b72840:8", "const:4:8"]]
+ 00b72840 ["CALL", null, ["callee:00c5cf10:8"]]
- 00b7184c bytes bda90394
+ 00b72840 bytes b4a90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1403e5acef75823ac27809db1b92822"></a>

### [`00b7199c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b7199c.md) → [`00b72990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72990.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5db50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b719b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b7199c.md#insn-00b719b0)
- 新版 [`00b729a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72990.md#insn-00b729a4)

~~~diff
- 00b719b0 ["INT_ADD", "register:40f0:8", ["const:b719b0:8", "const:4:8"]]
- 00b719b0 ["CALL", null, ["callee:00c5db50:8"]]
+ 00b729a4 ["INT_ADD", "register:40f0:8", ["const:b729a4:8", "const:4:8"]]
+ 00b729a4 ["CALL", null, ["callee:00c5db50:8"]]
- 00b719b0 bytes 74ac0394
+ 00b729a4 bytes 6bac0394
~~~


<a id="compare-b0f02bb27288c6f80046fc91f4c8e5b9"></a>

### [`00b719e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b719e8.md) → [`00b729dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b729dc.md) _ZNK11flatbuffers6Parser32LookupStructThruParentNamespacesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cab0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)
- 新版 呼出元 1件 [`00c5da80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da80.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b719e8.md#insn-00b71ab8) · [`00b71b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b719e8.md#insn-00b71b04) · [`00b71b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b719e8.md#insn-00b71b48)
- 新版 [`00b72aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b729dc.md#insn-00b72aac) · [`00b72af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b729dc.md#insn-00b72af8) · [`00b72b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b729dc.md#insn-00b72b3c)

~~~diff
- 00b71ab8 ["INT_ADD", "register:40f0:8", ["const:b71ab8:8", "const:4:8"]]
- 00b71ab8 ["CALL", null, ["callee:00c59020:8"]]
+ 00b72aac ["INT_ADD", "register:40f0:8", ["const:b72aac:8", "const:4:8"]]
+ 00b72aac ["CALL", null, ["callee:00c59020:8"]]
- 00b71ab8 bytes 66990394
+ 00b72aac bytes 5d990394
- 00b71b04 ["INT_ADD", "register:40f0:8", ["const:b71b04:8", "const:4:8"]]
- 00b71b04 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b72af8 ["INT_ADD", "register:40f0:8", ["const:b72af8:8", "const:4:8"]]
+ 00b72af8 ["CALL", null, ["callee:00c5b980:8"]]
- 00b71b04 bytes aba30394
+ 00b72af8 bytes a2a30394
- 00b71b48 ["INT_ADD", "register:40f0:8", ["const:b71b48:8", "const:4:8"]]
- 00b71b48 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00b72b3c ["INT_ADD", "register:40f0:8", ["const:b72b3c:8", "const:4:8"]]
+ 00b72b3c ["CALL", null, ["callee:00c5cf10:8"]]
- 00b71b48 bytes fea80394
+ 00b72b3c bytes f5a80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f18da5cff5713a6830a709f526e9b76"></a>

### [`00b71ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71ca8.md) → [`00b72c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72c9c.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c670.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d640.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71ca8.md#insn-00b71d40) · [`00b71d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71ca8.md#insn-00b71d60) · [`00b71d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71ca8.md#insn-00b71d74)
- 新版 [`00b72d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72c9c.md#insn-00b72d34) · [`00b72d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72c9c.md#insn-00b72d54) · [`00b72d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72c9c.md#insn-00b72d68)

~~~diff
- 00b71d40 ["INT_ADD", "register:40f0:8", ["const:b71d40:8", "const:4:8"]]
- 00b71d40 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b72d34 ["INT_ADD", "register:40f0:8", ["const:b72d34:8", "const:4:8"]]
+ 00b72d34 ["CALL", null, ["callee:00c58f30:8"]]
- 00b71d40 bytes 88980394
+ 00b72d34 bytes 7f980394
- 00b71d60 ["INT_ADD", "register:40f0:8", ["const:b71d60:8", "const:4:8"]]
- 00b71d60 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b72d54 ["INT_ADD", "register:40f0:8", ["const:b72d54:8", "const:4:8"]]
+ 00b72d54 ["CALL", null, ["callee:00c590a0:8"]]
- 00b71d60 bytes dc980394
+ 00b72d54 bytes d3980394
- 00b71d74 ["INT_ADD", "register:40f0:8", ["const:b71d74:8", "const:4:8"]]
- 00b71d74 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b72d68 ["INT_ADD", "register:40f0:8", ["const:b72d68:8", "const:4:8"]]
+ 00b72d68 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b71d74 bytes abaa0394
+ 00b72d68 bytes a2aa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca685b7f1e1c3d3d2eb2f0bb6ee919fc"></a>

### [`00b72e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72e40.md) → [`00b73e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73e34.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c170.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d140.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72e40.md#insn-00b72ed0) · [`00b72edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72e40.md#insn-00b72edc) · [`00b72f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72e40.md#insn-00b72f04)
- 新版 [`00b73ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73e34.md#insn-00b73ec4) · [`00b73ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73e34.md#insn-00b73ed0) · [`00b73ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73e34.md#insn-00b73ef8)

~~~diff
- 00b72ed0 ["INT_ADD", "register:40f0:8", ["const:b72ed0:8", "const:4:8"]]
- 00b72ed0 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b73ec4 ["INT_ADD", "register:40f0:8", ["const:b73ec4:8", "const:4:8"]]
+ 00b73ec4 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b72ed0 bytes d0a00394
+ 00b73ec4 bytes c7a00394
- 00b72edc ["INT_ADD", "register:40f0:8", ["const:b72edc:8", "const:4:8"]]
- 00b72edc ["CALL", null, ["callee:00c58f30:8"]]
+ 00b73ed0 ["INT_ADD", "register:40f0:8", ["const:b73ed0:8", "const:4:8"]]
+ 00b73ed0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b72edc bytes 21940394
+ 00b73ed0 bytes 18940394
- 00b72f04 ["INT_ADD", "register:40f0:8", ["const:b72f04:8", "const:4:8"]]
- 00b72f04 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b73ef8 ["INT_ADD", "register:40f0:8", ["const:b73ef8:8", "const:4:8"]]
+ 00b73ef8 ["CALL", null, ["callee:00c590a0:8"]]
- 00b72f04 bytes 73940394
+ 00b73ef8 bytes 6a940394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0ecdecf8a85106380457347776814c"></a>

### [`00b76ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md) → [`00b77acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77acc.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cac0.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c280.md) [`00c5c290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c290.md)
- 新版 呼出元 1件 [`00c5da90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da90.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d250.md) [`00c5d260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76b28) · [`00b76b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76b7c) · [`00b76c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76c0c)
- 新版 [`00b77b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77acc.md#insn-00b77b1c) · [`00b77b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77acc.md#insn-00b77b70) · [`00b77c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77acc.md#insn-00b77c00)

~~~diff
- 00b76b28 ["INT_ADD", "register:40f0:8", ["const:b76b28:8", "const:4:8"]]
- 00b76b28 ["CALL", null, ["callee:00c5d260:8"]]
+ 00b77b1c ["INT_ADD", "register:40f0:8", ["const:b77b1c:8", "const:4:8"]]
+ 00b77b1c ["CALL", null, ["callee:00c5d260:8"]]
- 00b76b28 bytes da950394
+ 00b77b1c bytes d1950394
- 00b76b7c ["INT_ADD", "register:40f0:8", ["const:b76b7c:8", "const:4:8"]]
- 00b76b7c ["CALL", null, ["callee:00c5d250:8"]]
+ 00b77b70 ["INT_ADD", "register:40f0:8", ["const:b77b70:8", "const:4:8"]]
+ 00b77b70 ["CALL", null, ["callee:00c5d250:8"]]
- 00b76b7c bytes c1950394
+ 00b77b70 bytes b8950394
- 00b76c0c ["INT_ADD", "register:40f0:8", ["const:b76c0c:8", "const:4:8"]]
- 00b76c0c ["CALL", null, ["callee:00c58f80:8"]]
+ 00b77c00 ["INT_ADD", "register:40f0:8", ["const:b77c00:8", "const:4:8"]]
+ 00b77c00 ["CALL", null, ["callee:00c58f80:8"]]
- 00b76c0c bytes e9840394
+ 00b77c00 bytes e0840394
~~~


<a id="compare-be433c684c2c874bcdc5bfecc7535df7"></a>

### [`00b76c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md) → [`00b77c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77c04.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c130.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d100.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76ca0) · [`00b76cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76cac) · [`00b76cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76cd4)
- 新版 [`00b77c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77c04.md#insn-00b77c94) · [`00b77ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77c04.md#insn-00b77ca0) · [`00b77cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77c04.md#insn-00b77cc8)

~~~diff
- 00b76ca0 ["INT_ADD", "register:40f0:8", ["const:b76ca0:8", "const:4:8"]]
- 00b76ca0 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b77c94 ["INT_ADD", "register:40f0:8", ["const:b77c94:8", "const:4:8"]]
+ 00b77c94 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b76ca0 bytes 5c910394
+ 00b77c94 bytes 53910394
- 00b76cac ["INT_ADD", "register:40f0:8", ["const:b76cac:8", "const:4:8"]]
- 00b76cac ["CALL", null, ["callee:00c58f30:8"]]
+ 00b77ca0 ["INT_ADD", "register:40f0:8", ["const:b77ca0:8", "const:4:8"]]
+ 00b77ca0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b76cac bytes ad840394
+ 00b77ca0 bytes a4840394
- 00b76cd4 ["INT_ADD", "register:40f0:8", ["const:b76cd4:8", "const:4:8"]]
- 00b76cd4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b77cc8 ["INT_ADD", "register:40f0:8", ["const:b77cc8:8", "const:4:8"]]
+ 00b77cc8 ["CALL", null, ["callee:00c590a0:8"]]
- 00b76cd4 bytes ff840394
+ 00b77cc8 bytes f6840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38176ddb9b7f0036f01472314e9e081f"></a>

### [`00b7722c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md) → [`00b78220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78220.md) _ZN11flatbuffers6Parser11ParseStringERNS_5ValueEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5a0.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d570.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b772cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b772cc) · [`00b772ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b772ec) · [`00b77300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b77300)
- 新版 [`00b782c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78220.md#insn-00b782c0) · [`00b782e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78220.md#insn-00b782e0) · [`00b782f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78220.md#insn-00b782f4)

~~~diff
- 00b772cc ["INT_ADD", "register:40f0:8", ["const:b772cc:8", "const:4:8"]]
- 00b772cc ["CALL", null, ["callee:00c58f30:8"]]
+ 00b782c0 ["INT_ADD", "register:40f0:8", ["const:b782c0:8", "const:4:8"]]
+ 00b782c0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b772cc bytes 25830394
+ 00b782c0 bytes 1c830394
- 00b772ec ["INT_ADD", "register:40f0:8", ["const:b772ec:8", "const:4:8"]]
- 00b772ec ["CALL", null, ["callee:00c590a0:8"]]
+ 00b782e0 ["INT_ADD", "register:40f0:8", ["const:b782e0:8", "const:4:8"]]
+ 00b782e0 ["CALL", null, ["callee:00c590a0:8"]]
- 00b772ec bytes 79830394
+ 00b782e0 bytes 70830394
- 00b77300 ["INT_ADD", "register:40f0:8", ["const:b77300:8", "const:4:8"]]
- 00b77300 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b782f4 ["INT_ADD", "register:40f0:8", ["const:b782f4:8", "const:4:8"]]
+ 00b782f4 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b77300 bytes 48950394
+ 00b782f4 bytes 3f950394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ddc4738bede1e59a80ef22bbc8c07ba"></a>

### [`00b77584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77584.md) → [`00b78578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78578.md) _ZN11flatbuffers6Parser10ParseCommaEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b775a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77584.md#insn-00b775a4)
- 新版 [`00b78598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b78578.md#insn-00b78598)

~~~diff
- 00b775a4 ["INT_ADD", "register:40f0:8", ["const:b775a4:8", "const:4:8"]]
- 00b775a4 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b78598 ["INT_ADD", "register:40f0:8", ["const:b78598:8", "const:4:8"]]
+ 00b78598 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b775a4 bytes 9f940394
+ 00b78598 bytes 96940394
~~~


<a id="compare-3dfd2cc81c260b0140aec0d185bad29d"></a>

### [`00b7cf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md) → [`00b7df64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7df64.md) _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c690.md) · 呼出先 2件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d660.md) · 呼出先 2件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7cfd0) · [`00b7d054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7d054) · [`00b7d078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7d078)
- 新版 [`00b7dfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7df64.md#insn-00b7dfc4) · [`00b7e048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7df64.md#insn-00b7e048) · [`00b7e06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7df64.md#insn-00b7e06c)

~~~diff
- 00b7cfd0 ["INT_ADD", "register:40f0:8", ["const:b7cfd0:8", "const:4:8"]]
- 00b7cfd0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7dfc4 ["INT_ADD", "register:40f0:8", ["const:b7dfc4:8", "const:4:8"]]
+ 00b7dfc4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7cfd0 bytes a87c0394
+ 00b7dfc4 bytes 9f7c0394
- 00b7d054 ["INT_ADD", "register:40f0:8", ["const:b7d054:8", "const:4:8"]]
- 00b7d054 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7e048 ["INT_ADD", "register:40f0:8", ["const:b7e048:8", "const:4:8"]]
+ 00b7e048 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d054 bytes 877c0394
+ 00b7e048 bytes 7e7c0394
- 00b7d078 ["INT_ADD", "register:40f0:8", ["const:b7d078:8", "const:4:8"]]
- 00b7d078 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b7e06c ["INT_ADD", "register:40f0:8", ["const:b7e06c:8", "const:4:8"]]
+ 00b7e06c ["CALL", null, ["callee:00c590a0:8"]]
- 00b7d078 bytes 166c0394
+ 00b7e06c bytes 0d6c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca1a450400ceff64a4784b799ed852f"></a>

### [`00b7d0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md) → [`00b7e0dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e0dc.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIhEEvtT_S3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2b0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d280.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md#insn-00b7d140) · [`00b7d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md#insn-00b7d180)
- 新版 [`00b7e134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e0dc.md#insn-00b7e134) · [`00b7e174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e0dc.md#insn-00b7e174)

~~~diff
- 00b7d140 ["INT_ADD", "register:40f0:8", ["const:b7d140:8", "const:4:8"]]
- 00b7d140 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7e134 ["INT_ADD", "register:40f0:8", ["const:b7e134:8", "const:4:8"]]
+ 00b7e134 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d140 bytes 4c7c0394
+ 00b7e134 bytes 437c0394
- 00b7d180 ["INT_ADD", "register:40f0:8", ["const:b7d180:8", "const:4:8"]]
- 00b7d180 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7e174 ["INT_ADD", "register:40f0:8", ["const:b7e174:8", "const:4:8"]]
+ 00b7e174 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d180 bytes 3c7c0394
+ 00b7e174 bytes 337c0394
~~~


<a id="compare-4d0dc24e6c20fe2e1ff54863a9c5589a"></a>

### [`00b7d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d640.md) → [`00b7e634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e634.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIaEEvtT_S3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2a0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d270.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d640.md#insn-00b7d698) · [`00b7d6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d640.md#insn-00b7d6d8)
- 新版 [`00b7e68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e634.md#insn-00b7e68c) · [`00b7e6cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e634.md#insn-00b7e6cc)

~~~diff
- 00b7d698 ["INT_ADD", "register:40f0:8", ["const:b7d698:8", "const:4:8"]]
- 00b7d698 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7e68c ["INT_ADD", "register:40f0:8", ["const:b7e68c:8", "const:4:8"]]
+ 00b7e68c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d698 bytes f67a0394
+ 00b7e68c bytes ed7a0394
- 00b7d6d8 ["INT_ADD", "register:40f0:8", ["const:b7d6d8:8", "const:4:8"]]
- 00b7d6d8 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7e6cc ["INT_ADD", "register:40f0:8", ["const:b7e6cc:8", "const:4:8"]]
+ 00b7e6cc ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d6d8 bytes e67a0394
+ 00b7e6cc bytes dd7a0394
~~~


<a id="compare-924932189f557c47e77bd1a7efa3bf38"></a>

### [`00b7db98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7db98.md) → [`00b7eb8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eb8c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2c0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d290.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7db98.md#insn-00b7dbf0) · [`00b7dc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7db98.md#insn-00b7dc28) · [`00b7dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7db98.md#insn-00b7dc5c)
- 新版 [`00b7ebe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eb8c.md#insn-00b7ebe4) · [`00b7ec1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eb8c.md#insn-00b7ec1c) · [`00b7ec50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eb8c.md#insn-00b7ec50)

~~~diff
- 00b7dbf0 ["INT_ADD", "register:40f0:8", ["const:b7dbf0:8", "const:4:8"]]
- 00b7dbf0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ebe4 ["INT_ADD", "register:40f0:8", ["const:b7ebe4:8", "const:4:8"]]
+ 00b7ebe4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dbf0 bytes a0790394
+ 00b7ebe4 bytes 97790394
- 00b7dc28 ["INT_ADD", "register:40f0:8", ["const:b7dc28:8", "const:4:8"]]
- 00b7dc28 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ec1c ["INT_ADD", "register:40f0:8", ["const:b7ec1c:8", "const:4:8"]]
+ 00b7ec1c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dc28 bytes 92790394
+ 00b7ec1c bytes 89790394
- 00b7dc5c ["INT_ADD", "register:40f0:8", ["const:b7dc5c:8", "const:4:8"]]
- 00b7dc5c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ec50 ["INT_ADD", "register:40f0:8", ["const:b7ec50:8", "const:4:8"]]
+ 00b7ec50 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dc5c bytes 85790394
+ 00b7ec50 bytes 7c790394
~~~


<a id="compare-4b6f2e996c5404f6b42d10004e37fb92"></a>

### [`00b7dcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md) → [`00b7eca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eca0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2d0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2a0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd04) · [`00b7dd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd3c) · [`00b7dd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd70)
- 新版 [`00b7ecf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eca0.md#insn-00b7ecf8) · [`00b7ed30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eca0.md#insn-00b7ed30) · [`00b7ed64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eca0.md#insn-00b7ed64)

~~~diff
- 00b7dd04 ["INT_ADD", "register:40f0:8", ["const:b7dd04:8", "const:4:8"]]
- 00b7dd04 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ecf8 ["INT_ADD", "register:40f0:8", ["const:b7ecf8:8", "const:4:8"]]
+ 00b7ecf8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dd04 bytes 5b790394
+ 00b7ecf8 bytes 52790394
- 00b7dd3c ["INT_ADD", "register:40f0:8", ["const:b7dd3c:8", "const:4:8"]]
- 00b7dd3c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ed30 ["INT_ADD", "register:40f0:8", ["const:b7ed30:8", "const:4:8"]]
+ 00b7ed30 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dd3c bytes 4d790394
+ 00b7ed30 bytes 44790394
- 00b7dd70 ["INT_ADD", "register:40f0:8", ["const:b7dd70:8", "const:4:8"]]
- 00b7dd70 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ed64 ["INT_ADD", "register:40f0:8", ["const:b7ed64:8", "const:4:8"]]
+ 00b7ed64 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7dd70 bytes 40790394
+ 00b7ed64 bytes 37790394
~~~


<a id="compare-1487af19b3d75f4e7f3649a394ce3350"></a>

### [`00b7ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md) → [`00b7edb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7edb4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_S3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2e0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2b0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de2c) · [`00b7de64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de64) · [`00b7de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de98)
- 新版 [`00b7ee20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7edb4.md#insn-00b7ee20) · [`00b7ee58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7edb4.md#insn-00b7ee58) · [`00b7ee8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7edb4.md#insn-00b7ee8c)

~~~diff
- 00b7de2c ["INT_ADD", "register:40f0:8", ["const:b7de2c:8", "const:4:8"]]
- 00b7de2c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ee20 ["INT_ADD", "register:40f0:8", ["const:b7ee20:8", "const:4:8"]]
+ 00b7ee20 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7de2c bytes 11790394
+ 00b7ee20 bytes 08790394
- 00b7de64 ["INT_ADD", "register:40f0:8", ["const:b7de64:8", "const:4:8"]]
- 00b7de64 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ee58 ["INT_ADD", "register:40f0:8", ["const:b7ee58:8", "const:4:8"]]
+ 00b7ee58 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7de64 bytes 03790394
+ 00b7ee58 bytes fa780394
- 00b7de98 ["INT_ADD", "register:40f0:8", ["const:b7de98:8", "const:4:8"]]
- 00b7de98 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7ee8c ["INT_ADD", "register:40f0:8", ["const:b7ee8c:8", "const:4:8"]]
+ 00b7ee8c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7de98 bytes f6780394
+ 00b7ee8c bytes ed780394
~~~


<a id="compare-4f4fe3f1544b9465b294a4139d1bb516"></a>

### [`00b7e35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e35c.md) → [`00b7f350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f350.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIijEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2e0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e35c.md#insn-00b7e3b4) · [`00b7e410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e35c.md#insn-00b7e410)
- 新版 [`00b7f3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f350.md#insn-00b7f3a8) · [`00b7f404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f350.md#insn-00b7f404)

~~~diff
- 00b7e3b4 ["INT_ADD", "register:40f0:8", ["const:b7e3b4:8", "const:4:8"]]
- 00b7e3b4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
+ 00b7f3a8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e3b4 bytes af770394
+ 00b7f3a8 bytes a6770394
- 00b7e410 ["INT_ADD", "register:40f0:8", ["const:b7e410:8", "const:4:8"]]
- 00b7e410 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f404 ["INT_ADD", "register:40f0:8", ["const:b7f404:8", "const:4:8"]]
+ 00b7f404 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e410 bytes 98770394
+ 00b7f404 bytes 8f770394
~~~


<a id="compare-f3fdae9542d6be6835c902c531fac8c6"></a>

### [`00b7e444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e444.md) → [`00b7f438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f438.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e444.md#insn-00b7e49c) · [`00b7e4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e444.md#insn-00b7e4f8)
- 新版 [`00b7f490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f438.md#insn-00b7f490) · [`00b7f4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f438.md#insn-00b7f4ec)

~~~diff
- 00b7e49c ["INT_ADD", "register:40f0:8", ["const:b7e49c:8", "const:4:8"]]
- 00b7e49c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f490 ["INT_ADD", "register:40f0:8", ["const:b7f490:8", "const:4:8"]]
+ 00b7f490 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e49c bytes 75770394
+ 00b7f490 bytes 6c770394
- 00b7e4f8 ["INT_ADD", "register:40f0:8", ["const:b7e4f8:8", "const:4:8"]]
- 00b7e4f8 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f4ec ["INT_ADD", "register:40f0:8", ["const:b7f4ec:8", "const:4:8"]]
+ 00b7f4ec ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e4f8 bytes 5e770394
+ 00b7f4ec bytes 55770394
~~~


<a id="compare-75b964d44fd65bd370ae119e966a3898"></a>

### [`00b7e90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md) → [`00b7f900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f900.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIljEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c330.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d300.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md#insn-00b7e964) · [`00b7e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md#insn-00b7e9c0)
- 新版 [`00b7f958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f900.md#insn-00b7f958) · [`00b7f9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f900.md#insn-00b7f9b4)

~~~diff
- 00b7e964 ["INT_ADD", "register:40f0:8", ["const:b7e964:8", "const:4:8"]]
- 00b7e964 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f958 ["INT_ADD", "register:40f0:8", ["const:b7f958:8", "const:4:8"]]
+ 00b7f958 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e964 bytes 43760394
+ 00b7f958 bytes 3a760394
- 00b7e9c0 ["INT_ADD", "register:40f0:8", ["const:b7e9c0:8", "const:4:8"]]
- 00b7e9c0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7f9b4 ["INT_ADD", "register:40f0:8", ["const:b7f9b4:8", "const:4:8"]]
+ 00b7f9b4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7e9c0 bytes 2c760394
+ 00b7f9b4 bytes 23760394
~~~


<a id="compare-d9d65df410376db4f2c64349defdf77a"></a>

### [`00b7ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md) → [`00b7fe14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fe14.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementImjEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c340.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d310.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md#insn-00b7ee78) · [`00b7eed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md#insn-00b7eed4)
- 新版 [`00b7fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fe14.md#insn-00b7fe6c) · [`00b7fec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fe14.md#insn-00b7fec8)

~~~diff
- 00b7ee78 ["INT_ADD", "register:40f0:8", ["const:b7ee78:8", "const:4:8"]]
- 00b7ee78 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7fe6c ["INT_ADD", "register:40f0:8", ["const:b7fe6c:8", "const:4:8"]]
+ 00b7fe6c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7ee78 bytes fe740394
+ 00b7fe6c bytes f5740394
- 00b7eed4 ["INT_ADD", "register:40f0:8", ["const:b7eed4:8", "const:4:8"]]
- 00b7eed4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b7fec8 ["INT_ADD", "register:40f0:8", ["const:b7fec8:8", "const:4:8"]]
+ 00b7fec8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7eed4 bytes e7740394
+ 00b7fec8 bytes de740394
~~~


<a id="compare-74fd907c6b8cac7a605cd3bac63bd9b7"></a>

### [`00b7f100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md) → [`00b800f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b800f4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIfjEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c300.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2d0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md#insn-00b7f158) · [`00b7f1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md#insn-00b7f1b4)
- 新版 [`00b8014c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b800f4.md#insn-00b8014c) · [`00b801a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b800f4.md#insn-00b801a8)

~~~diff
- 00b7f158 ["INT_ADD", "register:40f0:8", ["const:b7f158:8", "const:4:8"]]
- 00b7f158 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b8014c ["INT_ADD", "register:40f0:8", ["const:b8014c:8", "const:4:8"]]
+ 00b8014c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f158 bytes 46740394
+ 00b8014c bytes 3d740394
- 00b7f1b4 ["INT_ADD", "register:40f0:8", ["const:b7f1b4:8", "const:4:8"]]
- 00b7f1b4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b801a8 ["INT_ADD", "register:40f0:8", ["const:b801a8:8", "const:4:8"]]
+ 00b801a8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f1b4 bytes 2f740394
+ 00b801a8 bytes 26740394
~~~


<a id="compare-6a84884fa43297c0ea62b34e3063ae70"></a>

### [`00b7f3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md) → [`00b803e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b803e0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIdjEET0_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2f0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2c0.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md#insn-00b7f444) · [`00b7f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md#insn-00b7f4a0)
- 新版 [`00b80438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b803e0.md#insn-00b80438) · [`00b80494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b803e0.md#insn-00b80494)

~~~diff
- 00b7f444 ["INT_ADD", "register:40f0:8", ["const:b7f444:8", "const:4:8"]]
- 00b7f444 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80438 ["INT_ADD", "register:40f0:8", ["const:b80438:8", "const:4:8"]]
+ 00b80438 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f444 bytes 8b730394
+ 00b80438 bytes 82730394
- 00b7f4a0 ["INT_ADD", "register:40f0:8", ["const:b7f4a0:8", "const:4:8"]]
- 00b7f4a0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80494 ["INT_ADD", "register:40f0:8", ["const:b80494:8", "const:4:8"]]
+ 00b80494 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f4a0 bytes 74730394
+ 00b80494 bytes 6b730394
~~~


<a id="compare-8db0dc761d8532afa41939acfeb29ed9"></a>

### [`00b7f4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md) → [`00b804c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b804c4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_8Offset64IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4f0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c340.md)
- 新版 呼出元 1件 [`00c5d4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d4c0.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f530) · [`00b7f58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f58c) · [`00b7f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f5b0)
- 新版 [`00b80524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b804c4.md#insn-00b80524) · [`00b80580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b804c4.md#insn-00b80580) · [`00b805a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b804c4.md#insn-00b805a4)

~~~diff
- 00b7f530 ["INT_ADD", "register:40f0:8", ["const:b7f530:8", "const:4:8"]]
- 00b7f530 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80524 ["INT_ADD", "register:40f0:8", ["const:b80524:8", "const:4:8"]]
+ 00b80524 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f530 bytes 50730394
+ 00b80524 bytes 47730394
- 00b7f58c ["INT_ADD", "register:40f0:8", ["const:b7f58c:8", "const:4:8"]]
- 00b7f58c ["CALL", null, ["callee:00c5d310:8"]]
+ 00b80580 ["INT_ADD", "register:40f0:8", ["const:b80580:8", "const:4:8"]]
+ 00b80580 ["CALL", null, ["callee:00c5d310:8"]]
- 00b7f58c bytes 6d730394
+ 00b80580 bytes 64730394
- 00b7f5b0 ["INT_ADD", "register:40f0:8", ["const:b7f5b0:8", "const:4:8"]]
- 00b7f5b0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b805a4 ["INT_ADD", "register:40f0:8", ["const:b805a4:8", "const:4:8"]]
+ 00b805a4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f5b0 bytes 30730394
+ 00b805a4 bytes 27730394
~~~


<a id="compare-a54dabcae0fee47969965b803d116824"></a>

### [`00b7f600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md) → [`00b805f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b805f4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4e0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d4b0.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f660) · [`00b7f6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f6bc) · [`00b7f6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f6e0)
- 新版 [`00b80654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b805f4.md#insn-00b80654) · [`00b806b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b805f4.md#insn-00b806b0) · [`00b806d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b805f4.md#insn-00b806d4)

~~~diff
- 00b7f660 ["INT_ADD", "register:40f0:8", ["const:b7f660:8", "const:4:8"]]
- 00b7f660 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80654 ["INT_ADD", "register:40f0:8", ["const:b80654:8", "const:4:8"]]
+ 00b80654 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f660 bytes 04730394
+ 00b80654 bytes fb720394
- 00b7f6bc ["INT_ADD", "register:40f0:8", ["const:b7f6bc:8", "const:4:8"]]
- 00b7f6bc ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b806b0 ["INT_ADD", "register:40f0:8", ["const:b806b0:8", "const:4:8"]]
+ 00b806b0 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b7f6bc bytes 19730394
+ 00b806b0 bytes 10730394
- 00b7f6e0 ["INT_ADD", "register:40f0:8", ["const:b7f6e0:8", "const:4:8"]]
- 00b7f6e0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b806d4 ["INT_ADD", "register:40f0:8", ["const:b806d4:8", "const:4:8"]]
+ 00b806d4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f6e0 bytes e4720394
+ 00b806d4 bytes db720394
~~~


<a id="compare-2f6364ee4fd3efd9c9843362b5990baf"></a>

### [`00b7f730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md) → [`00b80724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80724.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE8EndTableEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md)
- 新版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3e0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f758) · [`00b7f79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f79c) · [`00b7f7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f7c0)
- 新版 [`00b8074c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80724.md#insn-00b8074c) · [`00b80790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80724.md#insn-00b80790) · [`00b807b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80724.md#insn-00b807b4)

~~~diff
- 00b7f758 ["INT_ADD", "register:40f0:8", ["const:b7f758:8", "const:4:8"]]
- 00b7f758 ["CALL", null, ["callee:00c5d2e0:8"]]
+ 00b8074c ["INT_ADD", "register:40f0:8", ["const:b8074c:8", "const:4:8"]]
+ 00b8074c ["CALL", null, ["callee:00c5d2e0:8"]]
- 00b7f758 bytes ee720394
+ 00b8074c bytes e5720394
- 00b7f79c ["INT_ADD", "register:40f0:8", ["const:b7f79c:8", "const:4:8"]]
- 00b7f79c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80790 ["INT_ADD", "register:40f0:8", ["const:b80790:8", "const:4:8"]]
+ 00b80790 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7f79c bytes b5720394
+ 00b80790 bytes ac720394
- 00b7f7c0 ["INT_ADD", "register:40f0:8", ["const:b7f7c0:8", "const:4:8"]]
- 00b7f7c0 ["CALL", null, ["callee:00c59130:8"]]
+ 00b807b4 ["INT_ADD", "register:40f0:8", ["const:b807b4:8", "const:4:8"]]
+ 00b807b4 ["CALL", null, ["callee:00c59130:8"]]
- 00b7f7c0 bytes 68620394
+ 00b807b4 bytes 5f620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4d7f4f975ae935bbd2b385cb986b51"></a>

### [`00b7fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md) → [`00b80d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80d8c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c350.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5d320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d320.md) · 呼出先 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7fe04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md#insn-00b7fe04) · [`00b7fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md#insn-00b7fe88)
- 新版 [`00b80df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80d8c.md#insn-00b80df8) · [`00b80e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80d8c.md#insn-00b80e7c)

~~~diff
- 00b7fe04 ["INT_ADD", "register:40f0:8", ["const:b7fe04:8", "const:4:8"]]
- 00b7fe04 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80df8 ["INT_ADD", "register:40f0:8", ["const:b80df8:8", "const:4:8"]]
+ 00b80df8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b7fe04 bytes 1b710394
+ 00b80df8 bytes 12710394
- 00b7fe88 ["INT_ADD", "register:40f0:8", ["const:b7fe88:8", "const:4:8"]]
- 00b7fe88 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b80e7c ["INT_ADD", "register:40f0:8", ["const:b80e7c:8", "const:4:8"]]
+ 00b80e7c ["CALL", null, ["callee:00c5d240:8"]]
- 00b7fe88 bytes fa700394
+ 00b80e7c bytes f1700394
~~~


<a id="compare-ab17915ad9eb0a06479e87699f35d476"></a>

### [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) → [`00b81108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81108.md) FUN_00b81108

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) · 呼出先 2件 [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b81108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81108.md) · 呼出先 2件 [`00b81108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81108.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md#insn-00b80184) · [`00b8023c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md#insn-00b8023c)
- 新版 [`00b81178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81108.md#insn-00b81178) · [`00b81230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81108.md#insn-00b81230)

~~~diff
- 00b80184 ["INT_ADD", "register:40f0:8", ["const:b80184:8", "const:4:8"]]
- 00b80184 ["CALL", null, ["local:b0:8"]]
+ 00b81178 ["INT_ADD", "register:40f0:8", ["const:b81178:8", "const:4:8"]]
+ 00b81178 ["CALL", null, ["local:b0:8"]]
- 00b80184 bytes e4ffff97
+ 00b81178 bytes e4ffff97
- 00b8023c ["INT_ADD", "register:40f0:8", ["const:b8023c:8", "const:4:8"]]
- 00b8023c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b81230 ["INT_ADD", "register:40f0:8", ["const:b81230:8", "const:4:8"]]
+ 00b81230 ["CALL", null, ["callee:00c590f0:8"]]
- 00b8023c bytes b95f0394
+ 00b81230 bytes b05f0394
~~~


<a id="compare-696162e3e00cf9c971ff9cc3d7d78c1a"></a>

### [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) → [`00b812a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b812a8.md) FUN_00b812a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) · 呼出先 2件 [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) [`00baafa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baafa8.md)
- 新版 呼出元 2件 [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b812a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b812a8.md) · 呼出先 2件 [`00b812a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b812a8.md) [`00babf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babf9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md#insn-00b80318) · [`00b803b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md#insn-00b803b4)
- 新版 [`00b8130c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b812a8.md#insn-00b8130c) · [`00b813a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b812a8.md#insn-00b813a8)

~~~diff
- 00b80318 ["INT_ADD", "register:40f0:8", ["const:b80318:8", "const:4:8"]]
- 00b80318 ["CALL", null, ["local:b0:8"]]
+ 00b8130c ["INT_ADD", "register:40f0:8", ["const:b8130c:8", "const:4:8"]]
+ 00b8130c ["CALL", null, ["local:b0:8"]]
- 00b80318 bytes e7ffff97
+ 00b8130c bytes e7ffff97
- 00b803b4 ["INT_ADD", "register:40f0:8", ["const:b803b4:8", "const:4:8"]]
- 00b803b4 ["CALL", null, ["callee:00babf9c:8"]]
+ 00b813a8 ["INT_ADD", "register:40f0:8", ["const:b813a8:8", "const:4:8"]]
+ 00b813a8 ["CALL", null, ["callee:00babf9c:8"]]
- 00b803b4 bytes fdaa0094
+ 00b813a8 bytes fdaa0094
~~~


<a id="compare-1ddf547e72eb8b55a75e07d8f636b425"></a>

### [`00b80860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md) → [`00b81854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81854.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c070.md) · 呼出先 2件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md)
- 新版 呼出元 1件 [`00c5d040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d040.md) · 呼出先 2件 [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b808ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b808ac) · [`00b808d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b808d0) · [`00b80904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b80904)
- 新版 [`00b818a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81854.md#insn-00b818a0) · [`00b818c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81854.md#insn-00b818c4) · [`00b818f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81854.md#insn-00b818f8)

~~~diff
- 00b808ac ["INT_ADD", "register:40f0:8", ["const:b808ac:8", "const:4:8"]]
- 00b808ac ["CALL", null, ["callee:00c5c150:8"]]
+ 00b818a0 ["INT_ADD", "register:40f0:8", ["const:b818a0:8", "const:4:8"]]
+ 00b818a0 ["CALL", null, ["callee:00c5c150:8"]]
- 00b808ac bytes 356a0394
+ 00b818a0 bytes 2c6a0394
- 00b808d0 ["INT_ADD", "register:40f0:8", ["const:b808d0:8", "const:4:8"]]
- 00b808d0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b818c4 ["INT_ADD", "register:40f0:8", ["const:b818c4:8", "const:4:8"]]
+ 00b818c4 ["CALL", null, ["callee:00c5c150:8"]]
- 00b808d0 bytes 2c6a0394
+ 00b818c4 bytes 236a0394
- 00b80904 ["INT_ADD", "register:40f0:8", ["const:b80904:8", "const:4:8"]]
- 00b80904 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b818f8 ["INT_ADD", "register:40f0:8", ["const:b818f8:8", "const:4:8"]]
+ 00b818f8 ["CALL", null, ["callee:00c5c150:8"]]
- 00b80904 bytes 1f6a0394
+ 00b818f8 bytes 166a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dba7ab0ddf342ace39a4988b6436d03"></a>

### [`00b80c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md) → [`00b81c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81c78.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfe0.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md) [`00c5c770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c770.md) [`00c5c890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c890.md) [`00c5c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9b0.md)
- 新版 呼出元 1件 [`00c5cfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cfb0.md) · 呼出先 5件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d650.md) [`00c5d740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d740.md) [`00c5d860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d860.md) [`00c5d980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80cbc) · [`00b80ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80ce0) · [`00b80cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80cfc)
- 新版 [`00b81cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81c78.md#insn-00b81cb0) · [`00b81cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81c78.md#insn-00b81cd4) · [`00b81cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81c78.md#insn-00b81cf0)

~~~diff
- 00b80cbc ["INT_ADD", "register:40f0:8", ["const:b80cbc:8", "const:4:8"]]
- 00b80cbc ["CALL", null, ["callee:00c5d650:8"]]
+ 00b81cb0 ["INT_ADD", "register:40f0:8", ["const:b81cb0:8", "const:4:8"]]
+ 00b81cb0 ["CALL", null, ["callee:00c5d650:8"]]
- 00b80cbc bytes 716e0394
+ 00b81cb0 bytes 686e0394
- 00b80ce0 ["INT_ADD", "register:40f0:8", ["const:b80ce0:8", "const:4:8"]]
- 00b80ce0 ["CALL", null, ["callee:00c5d740:8"]]
+ 00b81cd4 ["INT_ADD", "register:40f0:8", ["const:b81cd4:8", "const:4:8"]]
+ 00b81cd4 ["CALL", null, ["callee:00c5d740:8"]]
- 00b80ce0 bytes a46e0394
+ 00b81cd4 bytes 9b6e0394
- 00b80cfc ["INT_ADD", "register:40f0:8", ["const:b80cfc:8", "const:4:8"]]
- 00b80cfc ["CALL", null, ["callee:00c5d860:8"]]
+ 00b81cf0 ["INT_ADD", "register:40f0:8", ["const:b81cf0:8", "const:4:8"]]
+ 00b81cf0 ["CALL", null, ["callee:00c5d860:8"]]
- 00b80cfc bytes e56e0394
+ 00b81cf0 bytes dc6e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1047c806922b8f026ae8b702df8b93"></a>

### [`00b80d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md) → [`00b81d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81d38.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE12CreateVectorIhNS_6OffsetENS_6VectorEEET0_IJT1_IJT_EEEEPKS7_m

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c360.md) · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d330.md) · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80db0) · [`00b80e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80e1c) · [`00b80e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80e40)
- 新版 [`00b81da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81d38.md#insn-00b81da4) · [`00b81e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81d38.md#insn-00b81e10) · [`00b81e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81d38.md#insn-00b81e34)

~~~diff
- 00b80db0 ["INT_ADD", "register:40f0:8", ["const:b80db0:8", "const:4:8"]]
- 00b80db0 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b81da4 ["INT_ADD", "register:40f0:8", ["const:b81da4:8", "const:4:8"]]
+ 00b81da4 ["CALL", null, ["callee:00c5d240:8"]]
- 00b80db0 bytes 306d0394
+ 00b81da4 bytes 276d0394
- 00b80e1c ["INT_ADD", "register:40f0:8", ["const:b80e1c:8", "const:4:8"]]
- 00b80e1c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b81e10 ["INT_ADD", "register:40f0:8", ["const:b81e10:8", "const:4:8"]]
+ 00b81e10 ["CALL", null, ["callee:00c5d240:8"]]
- 00b80e1c bytes 156d0394
+ 00b81e10 bytes 0c6d0394
- 00b80e40 ["INT_ADD", "register:40f0:8", ["const:b80e40:8", "const:4:8"]]
- 00b80e40 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b81e34 ["INT_ADD", "register:40f0:8", ["const:b81e34:8", "const:4:8"]]
+ 00b81e34 ["CALL", null, ["callee:00c590a0:8"]]
- 00b80e40 bytes a45c0394
+ 00b81e34 bytes 9b5c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac4ff044eeb41d01bf717e16b456068"></a>

### [`00b82818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md) → [`00b8380c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8380c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbb0.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5db80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db80.md) · 呼出先 4件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b828a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828a4) · [`00b828d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828d8) · [`00b828e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828e8)
- 新版 [`00b83898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8380c.md#insn-00b83898) · [`00b838cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8380c.md#insn-00b838cc) · [`00b838dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8380c.md#insn-00b838dc)

~~~diff
- 00b828a4 ["INT_ADD", "register:40f0:8", ["const:b828a4:8", "const:4:8"]]
- 00b828a4 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b83898 ["INT_ADD", "register:40f0:8", ["const:b83898:8", "const:4:8"]]
+ 00b83898 ["CALL", null, ["callee:00c5b980:8"]]
- 00b828a4 bytes 43600394
+ 00b83898 bytes 3a600394
- 00b828d8 ["INT_ADD", "register:40f0:8", ["const:b828d8:8", "const:4:8"]]
- 00b828d8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b838cc ["INT_ADD", "register:40f0:8", ["const:b838cc:8", "const:4:8"]]
+ 00b838cc ["CALL", null, ["callee:00c58fe0:8"]]
- 00b828d8 bytes ce550394
+ 00b838cc bytes c5550394
- 00b828e8 ["INT_ADD", "register:40f0:8", ["const:b828e8:8", "const:4:8"]]
- 00b828e8 ["CALL", null, ["callee:00c59130:8"]]
+ 00b838dc ["INT_ADD", "register:40f0:8", ["const:b838dc:8", "const:4:8"]]
+ 00b838dc ["CALL", null, ["callee:00c59130:8"]]
- 00b828e8 bytes 1e560394
+ 00b838dc bytes 15560394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27ccab05eeb61c87695e26e169165614"></a>

### [`00b82928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md) → [`00b8391c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8391c.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c180.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d150.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b829b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829b8) · [`00b829c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829c4) · [`00b829ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829ec)
- 新版 [`00b839ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8391c.md#insn-00b839ac) · [`00b839b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8391c.md#insn-00b839b8) · [`00b839e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b8391c.md#insn-00b839e0)

~~~diff
- 00b829b8 ["INT_ADD", "register:40f0:8", ["const:b829b8:8", "const:4:8"]]
- 00b829b8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b839ac ["INT_ADD", "register:40f0:8", ["const:b839ac:8", "const:4:8"]]
+ 00b839ac ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b829b8 bytes 16620394
+ 00b839ac bytes 0d620394
- 00b829c4 ["INT_ADD", "register:40f0:8", ["const:b829c4:8", "const:4:8"]]
- 00b829c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b839b8 ["INT_ADD", "register:40f0:8", ["const:b839b8:8", "const:4:8"]]
+ 00b839b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b829c4 bytes 67550394
+ 00b839b8 bytes 5e550394
- 00b829ec ["INT_ADD", "register:40f0:8", ["const:b829ec:8", "const:4:8"]]
- 00b829ec ["CALL", null, ["callee:00c590a0:8"]]
+ 00b839e0 ["INT_ADD", "register:40f0:8", ["const:b839e0:8", "const:4:8"]]
+ 00b839e0 ["CALL", null, ["callee:00c590a0:8"]]
- 00b829ec bytes b9550394
+ 00b839e0 bytes b0550394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107118c3e1ba909d690cdc8070bb3a92"></a>

### [`00b82c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md) → [`00b83c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83c08.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8e0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md)
- 新版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d8b0.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5c9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md#insn-00b82c88) · [`00b82c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md#insn-00b82c90) · [`00b82d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md#insn-00b82d34)
- 新版 [`00b83c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83c08.md#insn-00b83c7c) · [`00b83c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83c08.md#insn-00b83c84) · [`00b83d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83c08.md#insn-00b83d28)

~~~diff
- 00b82c88 ["INT_ADD", "register:40f0:8", ["const:b82c88:8", "const:4:8"]]
- 00b82c88 ["CALL", null, ["callee:00c5c9c0:8"]]
+ 00b83c7c ["INT_ADD", "register:40f0:8", ["const:b83c7c:8", "const:4:8"]]
+ 00b83c7c ["CALL", null, ["callee:00c5c9c0:8"]]
- 00b82c88 bytes 5a630394
+ 00b83c7c bytes 51630394
- 00b82c90 ["INT_ADD", "register:40f0:8", ["const:b82c90:8", "const:4:8"]]
- 00b82c90 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b83c84 ["INT_ADD", "register:40f0:8", ["const:b83c84:8", "const:4:8"]]
+ 00b83c84 ["CALL", null, ["callee:00c58f50:8"]]
- 00b82c90 bytes bc540394
+ 00b83c84 bytes b3540394
- 00b82d34 ["INT_ADD", "register:40f0:8", ["const:b82d34:8", "const:4:8"]]
- 00b82d34 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b83d28 ["INT_ADD", "register:40f0:8", ["const:b83d28:8", "const:4:8"]]
+ 00b83d28 ["CALL", null, ["callee:00c58fe0:8"]]
- 00b82d34 bytes b7540394
+ 00b83d28 bytes ae540394
~~~


<a id="compare-c71a8b7c8dcd415e198e1a2a4a81d0b7"></a>

### [`00b845d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b845d8.md) → [`00b855cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b855cc.md) _ZN11flatbuffers6Parser16ParseProtoOptionEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6f0.md) · 呼出先 3件 [`00c5c630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c630.md) [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)
- 新版 呼出元 1件 [`00c5d6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d6c0.md) · 呼出先 3件 [`00c5d600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d600.md) [`00c5d790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d790.md) [`00c5d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b845f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b845d8.md#insn-00b845f0) · [`00b8460c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b845d8.md#insn-00b8460c) · [`00b84628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b845d8.md#insn-00b84628)
- 新版 [`00b855e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b855cc.md#insn-00b855e4) · [`00b85600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b855cc.md#insn-00b85600) · [`00b8561c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b855cc.md#insn-00b8561c)

~~~diff
- 00b845f0 ["INT_ADD", "register:40f0:8", ["const:b845f0:8", "const:4:8"]]
- 00b845f0 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b855e4 ["INT_ADD", "register:40f0:8", ["const:b855e4:8", "const:4:8"]]
+ 00b855e4 ["CALL", null, ["callee:00c5d790:8"]]
- 00b845f0 bytes 74600394
+ 00b855e4 bytes 6b600394
- 00b8460c ["INT_ADD", "register:40f0:8", ["const:b8460c:8", "const:4:8"]]
- 00b8460c ["CALL", null, ["callee:00c5d600:8"]]
+ 00b85600 ["INT_ADD", "register:40f0:8", ["const:b85600:8", "const:4:8"]]
+ 00b85600 ["CALL", null, ["callee:00c5d600:8"]]
- 00b8460c bytes 09600394
+ 00b85600 bytes 00600394
- 00b84628 ["INT_ADD", "register:40f0:8", ["const:b84628:8", "const:4:8"]]
- 00b84628 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b8561c ["INT_ADD", "register:40f0:8", ["const:b8561c:8", "const:4:8"]]
+ 00b8561c ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b84628 bytes 7e600394
+ 00b8561c bytes 75600394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c3ed322f13ca2495749351ba212a8a1"></a>

### [`00b848a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md) → [`00b85898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85898.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c120.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0f0.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md#insn-00b84934) · [`00b84940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md#insn-00b84940) · [`00b84968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md#insn-00b84968)
- 新版 [`00b85928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85898.md#insn-00b85928) · [`00b85934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85898.md#insn-00b85934) · [`00b8595c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85898.md#insn-00b8595c)

~~~diff
- 00b84934 ["INT_ADD", "register:40f0:8", ["const:b84934:8", "const:4:8"]]
- 00b84934 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b85928 ["INT_ADD", "register:40f0:8", ["const:b85928:8", "const:4:8"]]
+ 00b85928 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b84934 bytes 375a0394
+ 00b85928 bytes 2e5a0394
- 00b84940 ["INT_ADD", "register:40f0:8", ["const:b84940:8", "const:4:8"]]
- 00b84940 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b85934 ["INT_ADD", "register:40f0:8", ["const:b85934:8", "const:4:8"]]
+ 00b85934 ["CALL", null, ["callee:00c58f30:8"]]
- 00b84940 bytes 884d0394
+ 00b85934 bytes 7f4d0394
- 00b84968 ["INT_ADD", "register:40f0:8", ["const:b84968:8", "const:4:8"]]
- 00b84968 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b8595c ["INT_ADD", "register:40f0:8", ["const:b8595c:8", "const:4:8"]]
+ 00b8595c ["CALL", null, ["callee:00c590a0:8"]]
- 00b84968 bytes da4d0394
+ 00b8595c bytes d14d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18284c8ccdb9e2f01da0ed1ff13cb98a"></a>

### [`00b84f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f20.md) → [`00b85f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f14.md) _ZNK11flatbuffers6Parser16GetIncludedFilesEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5cb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb30.md) [`00c5d0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db00.md) [`00c5e090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f20.md#insn-00b84f3c)
- 新版 [`00b85f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f14.md#insn-00b85f30)

~~~diff
- 00b84f3c ["INT_ADD", "register:40f0:8", ["const:b84f3c:8", "const:4:8"]]
- 00b84f3c ["CALL", null, ["callee:00c5db00:8"]]
+ 00b85f30 ["INT_ADD", "register:40f0:8", ["const:b85f30:8", "const:4:8"]]
+ 00b85f30 ["CALL", null, ["callee:00c5db00:8"]]
- 00b84f3c bytes fd5e0394
+ 00b85f30 bytes f45e0394
~~~


<a id="compare-3e5f7e2b4a141e8386fdb0557a9d76ca"></a>

### [`00b84f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f78.md) → [`00b85f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f6c.md) _ZNSt6__ndk16vectorIN11flatbuffers12IncludedFileENS_9allocatorIS2_EEEC2INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEET_NS_9en

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0c0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5e090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e090.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8502c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f78.md#insn-00b8502c) · [`00b8505c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f78.md#insn-00b8505c) · [`00b85068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84f78.md#insn-00b85068)
- 新版 [`00b86020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f6c.md#insn-00b86020) · [`00b86050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f6c.md#insn-00b86050) · [`00b8605c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85f6c.md#insn-00b8605c)

~~~diff
- 00b8502c ["INT_ADD", "register:40f0:8", ["const:b8502c:8", "const:4:8"]]
- 00b8502c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b86020 ["INT_ADD", "register:40f0:8", ["const:b86020:8", "const:4:8"]]
+ 00b86020 ["CALL", null, ["callee:00c58f30:8"]]
- 00b8502c bytes cd4b0394
+ 00b86020 bytes c44b0394
- 00b8505c ["INT_ADD", "register:40f0:8", ["const:b8505c:8", "const:4:8"]]
- 00b8505c ["CALL", null, ["callee:00c5c650:8"]]
+ 00b86050 ["INT_ADD", "register:40f0:8", ["const:b86050:8", "const:4:8"]]
+ 00b86050 ["CALL", null, ["callee:00c5c650:8"]]
- 00b8505c bytes 89590394
+ 00b86050 bytes 80590394
- 00b85068 ["INT_ADD", "register:40f0:8", ["const:b85068:8", "const:4:8"]]
- 00b85068 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b8605c ["INT_ADD", "register:40f0:8", ["const:b8605c:8", "const:4:8"]]
+ 00b8605c ["CALL", null, ["callee:00c5c650:8"]]
- 00b85068 bytes 86590394
+ 00b8605c bytes 7d590394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4354b9088ef5fd78bb876d79daa78f8"></a>

### [`00b850f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md) → [`00b860ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b860ec.md) _ZN11flatbuffers6Parser15UniqueNamespaceEPNS_9NamespaceE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6a0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d670.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b851fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md#insn-00b851fc) · [`00b85260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md#insn-00b85260) · [`00b852a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md#insn-00b852a4)
- 新版 [`00b861f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b860ec.md#insn-00b861f0) · [`00b86254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b860ec.md#insn-00b86254) · [`00b86298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b860ec.md#insn-00b86298)

~~~diff
- 00b851fc ["INT_ADD", "register:40f0:8", ["const:b851fc:8", "const:4:8"]]
- 00b851fc ["CALL", null, ["callee:00c590f0:8"]]
+ 00b861f0 ["INT_ADD", "register:40f0:8", ["const:b861f0:8", "const:4:8"]]
+ 00b861f0 ["CALL", null, ["callee:00c590f0:8"]]
- 00b851fc bytes c94b0394
+ 00b861f0 bytes c04b0394
- 00b85260 ["INT_ADD", "register:40f0:8", ["const:b85260:8", "const:4:8"]]
- 00b85260 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b86254 ["INT_ADD", "register:40f0:8", ["const:b86254:8", "const:4:8"]]
+ 00b86254 ["CALL", null, ["callee:00c58f50:8"]]
- 00b85260 bytes 484b0394
+ 00b86254 bytes 3f4b0394
- 00b852a4 ["INT_ADD", "register:40f0:8", ["const:b852a4:8", "const:4:8"]]
- 00b852a4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b86298 ["INT_ADD", "register:40f0:8", ["const:b86298:8", "const:4:8"]]
+ 00b86298 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b852a4 bytes db570394
+ 00b86298 bytes d2570394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f311659ee7d70e32f55c56ce0965157"></a>

### [`00b85348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b85348.md) → [`00b8633c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b8633c.md) _ZN11flatbuffers6Parser15UnqualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6b0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c5b720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b720.md)
- 新版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d680.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md) [`00c5c6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b85348.md#insn-00b85380) · [`00b853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b85348.md#insn-00b853b4) · [`00b853e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b85348.md#insn-00b853e4)
- 新版 [`00b86374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b8633c.md#insn-00b86374) · [`00b863a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b8633c.md#insn-00b863a8) · [`00b863d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b8633c.md#insn-00b863d8)

~~~diff
- 00b85380 ["INT_ADD", "register:40f0:8", ["const:b85380:8", "const:4:8"]]
- 00b85380 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b86374 ["INT_ADD", "register:40f0:8", ["const:b86374:8", "const:4:8"]]
+ 00b86374 ["CALL", null, ["callee:00c58f30:8"]]
- 00b85380 bytes f84a0394
+ 00b86374 bytes ef4a0394
- 00b853b4 ["INT_ADD", "register:40f0:8", ["const:b853b4:8", "const:4:8"]]
- 00b853b4 ["CALL", null, ["callee:00c59070:8"]]
+ 00b863a8 ["INT_ADD", "register:40f0:8", ["const:b863a8:8", "const:4:8"]]
+ 00b863a8 ["CALL", null, ["callee:00c59070:8"]]
- 00b853b4 bytes 3b4b0394
+ 00b863a8 bytes 324b0394
- 00b853e4 ["INT_ADD", "register:40f0:8", ["const:b853e4:8", "const:4:8"]]
- 00b853e4 ["CALL", null, ["callee:00c5c890:8"]]
+ 00b863d8 ["INT_ADD", "register:40f0:8", ["const:b863d8:8", "const:4:8"]]
+ 00b863d8 ["CALL", null, ["callee:00c5c890:8"]]
- 00b853e4 bytes 37590394
+ 00b863d8 bytes 2e590394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5592c2f037277d77edb2a4f5633df62"></a>

### [`00b86348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md) → [`00b8733c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b8733c.md) FUN_00b8733c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b854d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aa00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa00.md) [`00c5cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb40.md)
- 新版 呼出元 1件 [`00b864cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b864cc.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9d0.md) [`00c5db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b86394) · [`00b863c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b863c8) · [`00b863dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b863dc)
- 新版 [`00b87388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b8733c.md#insn-00b87388) · [`00b873bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b8733c.md#insn-00b873bc) · [`00b873d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b8733c.md#insn-00b873d0)

~~~diff
- 00b86394 ["INT_ADD", "register:40f0:8", ["const:b86394:8", "const:4:8"]]
- 00b86394 ["CALL", null, ["callee:00c5db10:8"]]
+ 00b87388 ["INT_ADD", "register:40f0:8", ["const:b87388:8", "const:4:8"]]
+ 00b87388 ["CALL", null, ["callee:00c5db10:8"]]
- 00b86394 bytes eb590394
+ 00b87388 bytes e2590394
- 00b863c8 ["INT_ADD", "register:40f0:8", ["const:b863c8:8", "const:4:8"]]
- 00b863c8 ["CALL", null, ["callee:00c5b9d0:8"]]
+ 00b873bc ["INT_ADD", "register:40f0:8", ["const:b873bc:8", "const:4:8"]]
+ 00b873bc ["CALL", null, ["callee:00c5b9d0:8"]]
- 00b863c8 bytes 8e510394
+ 00b873bc bytes 85510394
- 00b863dc ["INT_ADD", "register:40f0:8", ["const:b863dc:8", "const:4:8"]]
- 00b863dc ["CALL", null, ["callee:00c58f50:8"]]
+ 00b873d0 ["INT_ADD", "register:40f0:8", ["const:b873d0:8", "const:4:8"]]
+ 00b873d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00b863dc bytes e9460394
+ 00b873d0 bytes e0460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cf20c43b288c910c3ecdb6980571fcd"></a>

### [`00b86ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86ee0.md) → [`00b87ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87ed4.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c110.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0e0.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86ee0.md#insn-00b86f70) · [`00b86f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86ee0.md#insn-00b86f7c) · [`00b86fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86ee0.md#insn-00b86fa4)
- 新版 [`00b87f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87ed4.md#insn-00b87f64) · [`00b87f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87ed4.md#insn-00b87f70) · [`00b87f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87ed4.md#insn-00b87f98)

~~~diff
- 00b86f70 ["INT_ADD", "register:40f0:8", ["const:b86f70:8", "const:4:8"]]
- 00b86f70 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b87f64 ["INT_ADD", "register:40f0:8", ["const:b87f64:8", "const:4:8"]]
+ 00b87f64 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b86f70 bytes a8500394
+ 00b87f64 bytes 9f500394
- 00b86f7c ["INT_ADD", "register:40f0:8", ["const:b86f7c:8", "const:4:8"]]
- 00b86f7c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b87f70 ["INT_ADD", "register:40f0:8", ["const:b87f70:8", "const:4:8"]]
+ 00b87f70 ["CALL", null, ["callee:00c58f30:8"]]
- 00b86f7c bytes f9430394
+ 00b87f70 bytes f0430394
- 00b86fa4 ["INT_ADD", "register:40f0:8", ["const:b86fa4:8", "const:4:8"]]
- 00b86fa4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b87f98 ["INT_ADD", "register:40f0:8", ["const:b87f98:8", "const:4:8"]]
+ 00b87f98 ["CALL", null, ["callee:00c590a0:8"]]
- 00b86fa4 bytes 4b440394
+ 00b87f98 bytes 42440394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739611ebd26b37c622a32154fbcf0156"></a>

### [`00b87098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87098.md) → [`00b8808c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b8808c.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c160.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d130.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87098.md#insn-00b87128) · [`00b87134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87098.md#insn-00b87134) · [`00b8715c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87098.md#insn-00b8715c)
- 新版 [`00b8811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b8808c.md#insn-00b8811c) · [`00b88128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b8808c.md#insn-00b88128) · [`00b88150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b8808c.md#insn-00b88150)

~~~diff
- 00b87128 ["INT_ADD", "register:40f0:8", ["const:b87128:8", "const:4:8"]]
- 00b87128 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b8811c ["INT_ADD", "register:40f0:8", ["const:b8811c:8", "const:4:8"]]
+ 00b8811c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b87128 bytes 3a500394
+ 00b8811c bytes 31500394
- 00b87134 ["INT_ADD", "register:40f0:8", ["const:b87134:8", "const:4:8"]]
- 00b87134 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b88128 ["INT_ADD", "register:40f0:8", ["const:b88128:8", "const:4:8"]]
+ 00b88128 ["CALL", null, ["callee:00c58f30:8"]]
- 00b87134 bytes 8b430394
+ 00b88128 bytes 82430394
- 00b8715c ["INT_ADD", "register:40f0:8", ["const:b8715c:8", "const:4:8"]]
- 00b8715c ["CALL", null, ["callee:00c590a0:8"]]
+ 00b88150 ["INT_ADD", "register:40f0:8", ["const:b88150:8", "const:4:8"]]
+ 00b88150 ["CALL", null, ["callee:00c590a0:8"]]
- 00b8715c bytes dd430394
+ 00b88150 bytes d4430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad13502834324355dfa9e969d179def5"></a>

### [`00b87250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md) → [`00b88244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88244.md) _ZN11flatbuffers6Parser11SetRootTypeEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5c0.md) · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d590.md) · 呼出先 8件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b87290) · [`00b872cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b872cc) · [`00b872ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b872ec)
- 新版 [`00b88284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88244.md#insn-00b88284) · [`00b882c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88244.md#insn-00b882c0) · [`00b882e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88244.md#insn-00b882e0)

~~~diff
- 00b87290 ["INT_ADD", "register:40f0:8", ["const:b87290:8", "const:4:8"]]
- 00b87290 ["CALL", null, ["callee:00c59080:8"]]
+ 00b88284 ["INT_ADD", "register:40f0:8", ["const:b88284:8", "const:4:8"]]
+ 00b88284 ["CALL", null, ["callee:00c59080:8"]]
- 00b87290 bytes 88430394
+ 00b88284 bytes 7f430394
- 00b872cc ["INT_ADD", "register:40f0:8", ["const:b872cc:8", "const:4:8"]]
- 00b872cc ["CALL", null, ["callee:00c58f30:8"]]
+ 00b882c0 ["INT_ADD", "register:40f0:8", ["const:b882c0:8", "const:4:8"]]
+ 00b882c0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b872cc bytes 25430394
+ 00b882c0 bytes 1c430394
- 00b872ec ["INT_ADD", "register:40f0:8", ["const:b872ec:8", "const:4:8"]]
- 00b872ec ["CALL", null, ["callee:00c590a0:8"]]
+ 00b882e0 ["INT_ADD", "register:40f0:8", ["const:b882e0:8", "const:4:8"]]
+ 00b882e0 ["CALL", null, ["callee:00c590a0:8"]]
- 00b872ec bytes 79430394
+ 00b882e0 bytes 70430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ddbbc9790a188be4f822e59b833bcb"></a>

### [`00b87580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87580.md) → [`00b88574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88574.md) _ZN11flatbuffers6Parser14ParseNamespaceEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c650.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5d620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d620.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b875a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87580.md#insn-00b875a4) · [`00b875d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87580.md#insn-00b875d8) · [`00b87640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87580.md#insn-00b87640)
- 新版 [`00b88598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88574.md#insn-00b88598) · [`00b885cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88574.md#insn-00b885cc) · [`00b88634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88574.md#insn-00b88634)

~~~diff
- 00b875a4 ["INT_ADD", "register:40f0:8", ["const:b875a4:8", "const:4:8"]]
- 00b875a4 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b88598 ["INT_ADD", "register:40f0:8", ["const:b88598:8", "const:4:8"]]
+ 00b88598 ["CALL", null, ["callee:00c5d790:8"]]
- 00b875a4 bytes 87540394
+ 00b88598 bytes 7e540394
- 00b875d8 ["INT_ADD", "register:40f0:8", ["const:b875d8:8", "const:4:8"]]
- 00b875d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b885cc ["INT_ADD", "register:40f0:8", ["const:b885cc:8", "const:4:8"]]
+ 00b885cc ["CALL", null, ["callee:00c58f30:8"]]
- 00b875d8 bytes 62420394
+ 00b885cc bytes 59420394
- 00b87640 ["INT_ADD", "register:40f0:8", ["const:b87640:8", "const:4:8"]]
- 00b87640 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b88634 ["INT_ADD", "register:40f0:8", ["const:b88634:8", "const:4:8"]]
+ 00b88634 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b87640 bytes f44e0394
+ 00b88634 bytes eb4e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067d32e3c75aab844dcea44f1dddc279"></a>

### [`00b89a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md) → [`00b8aa00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa00.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md#insn-00b89a28) · [`00b89a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md#insn-00b89a60)
- 新版 [`00b8aa1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa00.md#insn-00b8aa1c) · [`00b8aa54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa00.md#insn-00b8aa54)

~~~diff
- 00b89a28 ["INT_ADD", "register:40f0:8", ["const:b89a28:8", "const:4:8"]]
- 00b89a28 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b8aa1c ["INT_ADD", "register:40f0:8", ["const:b8aa1c:8", "const:4:8"]]
+ 00b8aa1c ["CALL", null, ["callee:00c5d790:8"]]
- 00b89a28 bytes 664b0394
+ 00b8aa1c bytes 5d4b0394
- 00b89a60 ["INT_ADD", "register:40f0:8", ["const:b89a60:8", "const:4:8"]]
- 00b89a60 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b8aa54 ["INT_ADD", "register:40f0:8", ["const:b8aa54:8", "const:4:8"]]
+ 00b8aa54 ["CALL", null, ["callee:00c5d790:8"]]
- 00b89a60 bytes 584b0394
+ 00b8aa54 bytes 4f4b0394
~~~


<a id="compare-fcf7b22793972ecc7974222e39aa321a"></a>

### [`00b89aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89aa8.md) → [`00b8aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa9c.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c140.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d110.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89aa8.md#insn-00b89b38) · [`00b89b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89aa8.md#insn-00b89b44) · [`00b89b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89aa8.md#insn-00b89b6c)
- 新版 [`00b8ab2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa9c.md#insn-00b8ab2c) · [`00b8ab38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa9c.md#insn-00b8ab38) · [`00b8ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8aa9c.md#insn-00b8ab60)

~~~diff
- 00b89b38 ["INT_ADD", "register:40f0:8", ["const:b89b38:8", "const:4:8"]]
- 00b89b38 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b8ab2c ["INT_ADD", "register:40f0:8", ["const:b8ab2c:8", "const:4:8"]]
+ 00b8ab2c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b89b38 bytes b6450394
+ 00b8ab2c bytes ad450394
- 00b89b44 ["INT_ADD", "register:40f0:8", ["const:b89b44:8", "const:4:8"]]
- 00b89b44 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8ab38 ["INT_ADD", "register:40f0:8", ["const:b8ab38:8", "const:4:8"]]
+ 00b8ab38 ["CALL", null, ["callee:00c58f30:8"]]
- 00b89b44 bytes 07390394
+ 00b8ab38 bytes fe380394
- 00b89b6c ["INT_ADD", "register:40f0:8", ["const:b89b6c:8", "const:4:8"]]
- 00b89b6c ["CALL", null, ["callee:00c590a0:8"]]
+ 00b8ab60 ["INT_ADD", "register:40f0:8", ["const:b8ab60:8", "const:4:8"]]
+ 00b8ab60 ["CALL", null, ["callee:00c590a0:8"]]
- 00b89b6c bytes 59390394
+ 00b8ab60 bytes 50390394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e23830eb522e3ad5b74caf8eaeb1b9e"></a>

### [`00b8a294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a294.md) → [`00b8b288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b288.md) _ZN11flatbuffers6Parser13ParseProtoKeyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c630.md) · 呼出先 2件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)
- 新版 呼出元 1件 [`00c5d600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d600.md) · 呼出先 2件 [`00c5d790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d790.md) [`00c5d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a294.md#insn-00b8a2c0) · [`00b8a2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a294.md#insn-00b8a2e0) · [`00b8a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a294.md#insn-00b8a310)
- 新版 [`00b8b2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b288.md#insn-00b8b2b4) · [`00b8b2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b288.md#insn-00b8b2d4) · [`00b8b304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b288.md#insn-00b8b304)

~~~diff
- 00b8a2c0 ["INT_ADD", "register:40f0:8", ["const:b8a2c0:8", "const:4:8"]]
- 00b8a2c0 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b8b2b4 ["INT_ADD", "register:40f0:8", ["const:b8b2b4:8", "const:4:8"]]
+ 00b8b2b4 ["CALL", null, ["callee:00c5d790:8"]]
- 00b8a2c0 bytes 40490394
+ 00b8b2b4 bytes 37490394
- 00b8a2e0 ["INT_ADD", "register:40f0:8", ["const:b8a2e0:8", "const:4:8"]]
- 00b8a2e0 ["CALL", null, ["callee:00c5d790:8"]]
+ 00b8b2d4 ["INT_ADD", "register:40f0:8", ["const:b8b2d4:8", "const:4:8"]]
+ 00b8b2d4 ["CALL", null, ["callee:00c5d790:8"]]
- 00b8a2e0 bytes 38490394
+ 00b8b2d4 bytes 2f490394
- 00b8a310 ["INT_ADD", "register:40f0:8", ["const:b8a310:8", "const:4:8"]]
- 00b8a310 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b8b304 ["INT_ADD", "register:40f0:8", ["const:b8b304:8", "const:4:8"]]
+ 00b8b304 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b8a310 bytes 44490394
+ 00b8b304 bytes 3b490394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec03600d9db38ddcc29d31d12abc6fc"></a>

### [`00b8aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8aed0.md) → [`00b8bec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8bec4.md) _ZN11flexbuffers7Builder6EndMapEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9a0.md) · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d970.md) · 呼出先 8件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8af40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8aed0.md#insn-00b8af40) · [`00b8af60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8aed0.md#insn-00b8af60) · [`00b8af84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8aed0.md#insn-00b8af84)
- 新版 [`00b8bf34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8bec4.md#insn-00b8bf34) · [`00b8bf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8bec4.md#insn-00b8bf54) · [`00b8bf78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8bec4.md#insn-00b8bf78)

~~~diff
- 00b8af40 ["INT_ADD", "register:40f0:8", ["const:b8af40:8", "const:4:8"]]
- 00b8af40 ["CALL", null, ["callee:00c5deb0:8"]]
+ 00b8bf34 ["INT_ADD", "register:40f0:8", ["const:b8bf34:8", "const:4:8"]]
+ 00b8bf34 ["CALL", null, ["callee:00c5deb0:8"]]
- 00b8af40 bytes e8470394
+ 00b8bf34 bytes df470394
- 00b8af60 ["INT_ADD", "register:40f0:8", ["const:b8af60:8", "const:4:8"]]
- 00b8af60 ["CALL", null, ["callee:00c5d950:8"]]
+ 00b8bf54 ["INT_ADD", "register:40f0:8", ["const:b8bf54:8", "const:4:8"]]
+ 00b8bf54 ["CALL", null, ["callee:00c5d950:8"]]
- 00b8af60 bytes 88460394
+ 00b8bf54 bytes 7f460394
- 00b8af84 ["INT_ADD", "register:40f0:8", ["const:b8af84:8", "const:4:8"]]
- 00b8af84 ["CALL", null, ["callee:00c5d950:8"]]
+ 00b8bf78 ["INT_ADD", "register:40f0:8", ["const:b8bf78:8", "const:4:8"]]
+ 00b8bf78 ["CALL", null, ["callee:00c5d950:8"]]
- 00b8af84 bytes 7f460394
+ 00b8bf78 bytes 76460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403d0171ff049a44a9ab3b63d5467694"></a>

### [`00b8b0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md) → [`00b8c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c0a0.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9e0.md) · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c980.md)
- 新版 呼出元 1件 [`00c5d9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9b0.md) · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5d950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md#insn-00b8b0f8) · [`00b8b124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md#insn-00b8b124) · [`00b8b194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md#insn-00b8b194)
- 新版 [`00b8c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c0a0.md#insn-00b8c0ec) · [`00b8c118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c0a0.md#insn-00b8c118) · [`00b8c188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c0a0.md#insn-00b8c188)

~~~diff
- 00b8b0f8 ["INT_ADD", "register:40f0:8", ["const:b8b0f8:8", "const:4:8"]]
- 00b8b0f8 ["CALL", null, ["callee:00c5d950:8"]]
+ 00b8c0ec ["INT_ADD", "register:40f0:8", ["const:b8c0ec:8", "const:4:8"]]
+ 00b8c0ec ["CALL", null, ["callee:00c5d950:8"]]
- 00b8b0f8 bytes 22460394
+ 00b8c0ec bytes 19460394
- 00b8b124 ["INT_ADD", "register:40f0:8", ["const:b8b124:8", "const:4:8"]]
- 00b8b124 ["CALL", null, ["callee:00c5e0b0:8"]]
+ 00b8c118 ["INT_ADD", "register:40f0:8", ["const:b8c118:8", "const:4:8"]]
+ 00b8c118 ["CALL", null, ["callee:00c5e0b0:8"]]
- 00b8b124 bytes ef470394
+ 00b8c118 bytes e6470394
- 00b8b194 ["INT_ADD", "register:40f0:8", ["const:b8b194:8", "const:4:8"]]
- 00b8b194 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b8c188 ["INT_ADD", "register:40f0:8", ["const:b8c188:8", "const:4:8"]]
+ 00b8c188 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b8b194 bytes 1f400394
+ 00b8c188 bytes 16400394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08fb311c667e93bf47892fb287dc4c7"></a>

### [`00b8b208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md) → [`00b8c1fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c1fc.md) _ZN11flatbuffers6Parser15ParseFlexBufferEPKcS2_PN11flexbuffers7BuilderE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md) [`00c5c770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c770.md) [`00c5c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d650.md) [`00c5d740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d740.md) [`00c5d980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b234) · [`00b8b254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b254) · [`00b8b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b28c)
- 新版 [`00b8c228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c1fc.md#insn-00b8c228) · [`00b8c248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c1fc.md#insn-00b8c248) · [`00b8c280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c1fc.md#insn-00b8c280)

~~~diff
- 00b8b234 ["INT_ADD", "register:40f0:8", ["const:b8b234:8", "const:4:8"]]
- 00b8b234 ["CALL", null, ["callee:00c5d650:8"]]
+ 00b8c228 ["INT_ADD", "register:40f0:8", ["const:b8c228:8", "const:4:8"]]
+ 00b8c228 ["CALL", null, ["callee:00c5d650:8"]]
- 00b8b234 bytes 13450394
+ 00b8c228 bytes 0a450394
- 00b8b254 ["INT_ADD", "register:40f0:8", ["const:b8b254:8", "const:4:8"]]
- 00b8b254 ["CALL", null, ["callee:00c5d740:8"]]
+ 00b8c248 ["INT_ADD", "register:40f0:8", ["const:b8c248:8", "const:4:8"]]
+ 00b8c248 ["CALL", null, ["callee:00c5d740:8"]]
- 00b8b254 bytes 47450394
+ 00b8c248 bytes 3e450394
- 00b8b28c ["INT_ADD", "register:40f0:8", ["const:b8b28c:8", "const:4:8"]]
- 00b8b28c ["CALL", null, ["callee:00c5d980:8"]]
+ 00b8c280 ["INT_ADD", "register:40f0:8", ["const:b8c280:8", "const:4:8"]]
+ 00b8c280 ["CALL", null, ["callee:00c5d980:8"]]
- 00b8b28c bytes c9450394
+ 00b8c280 bytes c0450394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c70a48dcb8269bb5d5813bc9214383a"></a>

### [`00b8b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b414.md) → [`00b8c408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c408.md) _ZN11flexbuffers7Builder6FinishEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9b0.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9d0.md) [`00c5d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d140.md) [`00c5d150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d150.md)
- 新版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d980.md) · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9a0.md) [`00c5e110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b414.md#insn-00b8b4e0) · [`00b8b4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b414.md#insn-00b8b4f0) · [`00b8b544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b414.md#insn-00b8b544)
- 新版 [`00b8c4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c408.md#insn-00b8c4d4) · [`00b8c4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c408.md#insn-00b8c4e4) · [`00b8c538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c408.md#insn-00b8c538)

~~~diff
- 00b8b4e0 ["INT_ADD", "register:40f0:8", ["const:b8b4e0:8", "const:4:8"]]
- 00b8b4e0 ["CALL", null, ["callee:00c5e110:8"]]
+ 00b8c4d4 ["INT_ADD", "register:40f0:8", ["const:b8c4d4:8", "const:4:8"]]
+ 00b8c4d4 ["CALL", null, ["callee:00c5e110:8"]]
- 00b8b4e0 bytes 18470394
+ 00b8c4d4 bytes 0f470394
- 00b8b4f0 ["INT_ADD", "register:40f0:8", ["const:b8b4f0:8", "const:4:8"]]
- 00b8b4f0 ["CALL", null, ["callee:00c5d9a0:8"]]
+ 00b8c4e4 ["INT_ADD", "register:40f0:8", ["const:b8c4e4:8", "const:4:8"]]
+ 00b8c4e4 ["CALL", null, ["callee:00c5d9a0:8"]]
- 00b8b4f0 bytes 38450394
+ 00b8c4e4 bytes 2f450394
- 00b8b544 ["INT_ADD", "register:40f0:8", ["const:b8b544:8", "const:4:8"]]
- 00b8b544 ["CALL", null, ["callee:00c5e120:8"]]
+ 00b8c538 ["INT_ADD", "register:40f0:8", ["const:b8c538:8", "const:4:8"]]
+ 00b8c538 ["CALL", null, ["callee:00c5e120:8"]]
- 00b8b544 bytes 03470394
+ 00b8c538 bytes fa460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8300fdcf81752e3faac5b33c6c77cceb"></a>

### [`00b8bc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md) → [`00b8cbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cbfc.md) _ZN11flatbuffers6Parser9ParseJsonEPKcS2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) [`00c5c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c580.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5cab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cab0.md) [`00c5d550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d550.md) [`00c5d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md#insn-00b8bc9c) · [`00b8bcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md#insn-00b8bcbc) · [`00b8bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md#insn-00b8bcdc)
- 新版 [`00b8cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cbfc.md#insn-00b8cc90) · [`00b8ccb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cbfc.md#insn-00b8ccb0) · [`00b8ccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cbfc.md#insn-00b8ccd0)

~~~diff
- 00b8bc9c ["INT_ADD", "register:40f0:8", ["const:b8bc9c:8", "const:4:8"]]
- 00b8bc9c ["CALL", null, ["callee:00c5cab0:8"]]
+ 00b8cc90 ["INT_ADD", "register:40f0:8", ["const:b8cc90:8", "const:4:8"]]
+ 00b8cc90 ["CALL", null, ["callee:00c5cab0:8"]]
- 00b8bc9c bytes 913f0394
+ 00b8cc90 bytes 883f0394
- 00b8bcbc ["INT_ADD", "register:40f0:8", ["const:b8bcbc:8", "const:4:8"]]
- 00b8bcbc ["CALL", null, ["callee:00c5d650:8"]]
+ 00b8ccb0 ["INT_ADD", "register:40f0:8", ["const:b8ccb0:8", "const:4:8"]]
+ 00b8ccb0 ["CALL", null, ["callee:00c5d650:8"]]
- 00b8bcbc bytes 71420394
+ 00b8ccb0 bytes 68420394
- 00b8bcdc ["INT_ADD", "register:40f0:8", ["const:b8bcdc:8", "const:4:8"]]
- 00b8bcdc ["CALL", null, ["callee:00c5d550:8"]]
+ 00b8ccd0 ["INT_ADD", "register:40f0:8", ["const:b8ccd0:8", "const:4:8"]]
+ 00b8ccd0 ["CALL", null, ["callee:00c5d550:8"]]
- 00b8bcdc bytes 29420394
+ 00b8ccd0 bytes 20420394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d9dcb1cf56cb677cd7de35ebf2b264"></a>

### [`00b8d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md) → [`00b8e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e850.md) _ZN11flatbuffers6Parser16CheckPrivateLeakEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6c0.md) · 呼出先 1件 [`00c5c7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7a0.md)
- 新版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d690.md) · 呼出先 1件 [`00c5d770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8d8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md#insn-00b8d8c4) · [`00b8d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md#insn-00b8d960)
- 新版 [`00b8e8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e850.md#insn-00b8e8b8) · [`00b8e954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e850.md#insn-00b8e954)

~~~diff
- 00b8d8c4 ["INT_ADD", "register:40f0:8", ["const:b8d8c4:8", "const:4:8"]]
- 00b8d8c4 ["CALL", null, ["callee:00c5d770:8"]]
+ 00b8e8b8 ["INT_ADD", "register:40f0:8", ["const:b8e8b8:8", "const:4:8"]]
+ 00b8e8b8 ["CALL", null, ["callee:00c5d770:8"]]
- 00b8d8c4 bytes b73b0394
+ 00b8e8b8 bytes ae3b0394
- 00b8d960 ["INT_ADD", "register:40f0:8", ["const:b8d960:8", "const:4:8"]]
- 00b8d960 ["CALL", null, ["callee:00c5d770:8"]]
+ 00b8e954 ["INT_ADD", "register:40f0:8", ["const:b8e954:8", "const:4:8"]]
+ 00b8e954 ["CALL", null, ["callee:00c5d770:8"]]
- 00b8d960 bytes 903b0394
+ 00b8e954 bytes 873b0394
~~~


<a id="compare-46df81639632b61954f26f7a407d9f41"></a>

### [`00b8db54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8db54.md) → [`00b8eb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8eb48.md) FUN_00b8eb48

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00b8cf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8db54.md#insn-00b8dba4) · [`00b8dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8db54.md#insn-00b8dbe0) · [`00b8dc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8db54.md#insn-00b8dc00)
- 新版 [`00b8eb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8eb48.md#insn-00b8eb98) · [`00b8ebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8eb48.md#insn-00b8ebd4) · [`00b8ebf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8eb48.md#insn-00b8ebf4)

~~~diff
- 00b8dba4 ["INT_ADD", "register:40f0:8", ["const:b8dba4:8", "const:4:8"]]
- 00b8dba4 ["CALL", null, ["callee:00c59080:8"]]
+ 00b8eb98 ["INT_ADD", "register:40f0:8", ["const:b8eb98:8", "const:4:8"]]
+ 00b8eb98 ["CALL", null, ["callee:00c59080:8"]]
- 00b8dba4 bytes 43290394
+ 00b8eb98 bytes 3a290394
- 00b8dbe0 ["INT_ADD", "register:40f0:8", ["const:b8dbe0:8", "const:4:8"]]
- 00b8dbe0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8ebd4 ["INT_ADD", "register:40f0:8", ["const:b8ebd4:8", "const:4:8"]]
+ 00b8ebd4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b8dbe0 bytes e0280394
+ 00b8ebd4 bytes d7280394
- 00b8dc00 ["INT_ADD", "register:40f0:8", ["const:b8dc00:8", "const:4:8"]]
- 00b8dc00 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b8ebf4 ["INT_ADD", "register:40f0:8", ["const:b8ebf4:8", "const:4:8"]]
+ 00b8ebf4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b8dc00 bytes 34290394
+ 00b8ebf4 bytes 2b290394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fffdc15bb55e7712a4089a6137e6519b"></a>

### [`00b8dcf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8dcf4.md) → [`00b8ece8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8ece8.md) _ZNK11flatbuffers6Parser25GetIncludedFilesRecursiveERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`0054dc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054dc90.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`0054dfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054dfb0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8dcf4.md#insn-00b8dd68) · [`00b8dd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8dcf4.md#insn-00b8dd78) · [`00b8de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8dcf4.md#insn-00b8de24)
- 新版 [`00b8ed5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8ece8.md#insn-00b8ed5c) · [`00b8ed6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8ece8.md#insn-00b8ed6c) · [`00b8ee18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8ece8.md#insn-00b8ee18)

~~~diff
- 00b8dd68 ["INT_ADD", "register:40f0:8", ["const:b8dd68:8", "const:4:8"]]
- 00b8dd68 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8ed5c ["INT_ADD", "register:40f0:8", ["const:b8ed5c:8", "const:4:8"]]
+ 00b8ed5c ["CALL", null, ["callee:00c58f30:8"]]
- 00b8dd68 bytes 7e280394
+ 00b8ed5c bytes 75280394
- 00b8dd78 ["INT_ADD", "register:40f0:8", ["const:b8dd78:8", "const:4:8"]]
- 00b8dd78 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b8ed6c ["INT_ADD", "register:40f0:8", ["const:b8ed6c:8", "const:4:8"]]
+ 00b8ed6c ["CALL", null, ["callee:00c5c650:8"]]
- 00b8dd78 bytes 42360394
+ 00b8ed6c bytes 39360394
- 00b8de24 ["INT_ADD", "register:40f0:8", ["const:b8de24:8", "const:4:8"]]
- 00b8de24 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8ee18 ["INT_ADD", "register:40f0:8", ["const:b8ee18:8", "const:4:8"]]
+ 00b8ee18 ["CALL", null, ["callee:00c58f30:8"]]
- 00b8de24 bytes 4f280394
+ 00b8ee18 bytes 46280394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f8c228834c92c5ef5a793d6a96adb1"></a>

### [`00b8ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md) → [`00b8fe00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8fe00.md) _ZNK11flatbuffers9StructDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb20.md) · 呼出先 13件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5daf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5daf0.md) · 呼出先 13件 [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ee84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8ee84) · [`00b8eee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8eee8) · [`00b8ef10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8ef10)
- 新版 [`00b8fe78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8fe00.md#insn-00b8fe78) · [`00b8fedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8fe00.md#insn-00b8fedc) · [`00b8ff04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8fe00.md#insn-00b8ff04)

~~~diff
- 00b8ee84 ["INT_ADD", "register:40f0:8", ["const:b8ee84:8", "const:4:8"]]
- 00b8ee84 ["CALL", null, ["callee:00c5dad0:8"]]
+ 00b8fe78 ["INT_ADD", "register:40f0:8", ["const:b8fe78:8", "const:4:8"]]
+ 00b8fe78 ["CALL", null, ["callee:00c5dad0:8"]]
- 00b8ee84 bytes 1f370394
+ 00b8fe78 bytes 16370394
- 00b8eee8 ["INT_ADD", "register:40f0:8", ["const:b8eee8:8", "const:4:8"]]
- 00b8eee8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8fedc ["INT_ADD", "register:40f0:8", ["const:b8fedc:8", "const:4:8"]]
+ 00b8fedc ["CALL", null, ["callee:00c58f30:8"]]
- 00b8eee8 bytes 1e240394
+ 00b8fedc bytes 15240394
- 00b8ef10 ["INT_ADD", "register:40f0:8", ["const:b8ef10:8", "const:4:8"]]
- 00b8ef10 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b8ff04 ["INT_ADD", "register:40f0:8", ["const:b8ff04:8", "const:4:8"]]
+ 00b8ff04 ["CALL", null, ["callee:00c590a0:8"]]
- 00b8ef10 bytes 70240394
+ 00b8ff04 bytes 67240394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3925ddf560a85de5dd51383e9ef5eb3e"></a>

### [`00b9016c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b9016c.md) → [`00b91160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91160.md) _ZN10reflection12CreateSchemaERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6VectorINS4_INS_6ObjectEEEjEEEENS4_INS5_INS4_INS_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c050.md) · 呼出先 9件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c340.md) [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) [`00c5c430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c430.md) [`00c5c440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c440.md)
- 新版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d020.md) · 呼出先 9件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d310.md) [`00c5d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3e0.md) [`00c5d400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d400.md) [`00c5d410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b901c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b9016c.md#insn-00b901c8) · [`00b901ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b9016c.md#insn-00b901ec) · [`00b90238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b9016c.md#insn-00b90238)
- 新版 [`00b911bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91160.md#insn-00b911bc) · [`00b911e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91160.md#insn-00b911e0) · [`00b9122c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91160.md#insn-00b9122c)

~~~diff
- 00b901c8 ["INT_ADD", "register:40f0:8", ["const:b901c8:8", "const:4:8"]]
- 00b901c8 ["CALL", null, ["callee:00c5d310:8"]]
+ 00b911bc ["INT_ADD", "register:40f0:8", ["const:b911bc:8", "const:4:8"]]
+ 00b911bc ["CALL", null, ["callee:00c5d310:8"]]
- 00b901c8 bytes 5e300394
+ 00b911bc bytes 55300394
- 00b901ec ["INT_ADD", "register:40f0:8", ["const:b901ec:8", "const:4:8"]]
- 00b901ec ["CALL", null, ["callee:00c5d240:8"]]
+ 00b911e0 ["INT_ADD", "register:40f0:8", ["const:b911e0:8", "const:4:8"]]
+ 00b911e0 ["CALL", null, ["callee:00c5d240:8"]]
- 00b901ec bytes 21300394
+ 00b911e0 bytes 18300394
- 00b90238 ["INT_ADD", "register:40f0:8", ["const:b90238:8", "const:4:8"]]
- 00b90238 ["CALL", null, ["callee:00c5d420:8"]]
+ 00b9122c ["INT_ADD", "register:40f0:8", ["const:b9122c:8", "const:4:8"]]
+ 00b9122c ["CALL", null, ["callee:00c5d420:8"]]
- 00b90238 bytes 86300394
+ 00b9122c bytes 7d300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f453f152780156f319ae4fac41f801a9"></a>

### [`00b906c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906c8.md) → [`00b916bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916bc.md) _ZNK11flatbuffers10Definition19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b906d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906c8.md#insn-00b906d4)
- 新版 [`00b916c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916bc.md#insn-00b916c8)

~~~diff
- 00b906d4 ["INT_ADD", "register:40f0:8", ["const:b906d4:8", "const:4:8"]]
- 00b906d4 ["CALL", null, ["callee:00b93f28:8"]]
+ 00b916c8 ["INT_ADD", "register:40f0:8", ["const:b916c8:8", "const:4:8"]]
+ 00b916c8 ["CALL", null, ["callee:00b93f28:8"]]
- 00b906d4 bytes 180a0094
+ 00b916c8 bytes 180a0094
~~~


<a id="compare-fcc1cb92a48d0c6151cab05611945a61"></a>

### [`00b906e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906e4.md) → [`00b916d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916d8.md) _ZN10reflection12CreateObjectERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEENS4_INS0_6VectorINS4_INS_5FieldEEEjEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c040.md) · 呼出先 8件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2b0.md) [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md) [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) [`00c5c440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c440.md)
- 新版 呼出元 1件 [`00c5d010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d010.md) · 呼出先 8件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d280.md) [`00c5d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2e0.md) [`00c5d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3e0.md) [`00c5d410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b90734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906e4.md#insn-00b90734) · [`00b90744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906e4.md#insn-00b90744) · [`00b90754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906e4.md#insn-00b90754)
- 新版 [`00b91728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916d8.md#insn-00b91728) · [`00b91738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916d8.md#insn-00b91738) · [`00b91748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916d8.md#insn-00b91748)

~~~diff
- 00b90734 ["INT_ADD", "register:40f0:8", ["const:b90734:8", "const:4:8"]]
- 00b90734 ["CALL", null, ["callee:00c5d410:8"]]
+ 00b91728 ["INT_ADD", "register:40f0:8", ["const:b91728:8", "const:4:8"]]
+ 00b91728 ["CALL", null, ["callee:00c5d410:8"]]
- 00b90734 bytes 432f0394
+ 00b91728 bytes 3a2f0394
- 00b90744 ["INT_ADD", "register:40f0:8", ["const:b90744:8", "const:4:8"]]
- 00b90744 ["CALL", null, ["callee:00c5d4a0:8"]]
+ 00b91738 ["INT_ADD", "register:40f0:8", ["const:b91738:8", "const:4:8"]]
+ 00b91738 ["CALL", null, ["callee:00c5d4a0:8"]]
- 00b90744 bytes 632f0394
+ 00b91738 bytes 5a2f0394
- 00b90754 ["INT_ADD", "register:40f0:8", ["const:b90754:8", "const:4:8"]]
- 00b90754 ["CALL", null, ["callee:00c5d490:8"]]
+ 00b91748 ["INT_ADD", "register:40f0:8", ["const:b91748:8", "const:4:8"]]
+ 00b91748 ["CALL", null, ["callee:00c5d490:8"]]
- 00b90754 bytes 5b2f0394
+ 00b91748 bytes 522f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b626e4d0ee18416a67f90be740ee47"></a>

### [`00b91630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91630.md) → [`00b92624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92624.md) _ZN10reflection11CreateFieldERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEENS4_INS_4TypeEEEttldbbbNS4_INS0_6VectorI

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c030.md) · 呼出先 10件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2b0.md) [`00c5c2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2e0.md) [`00c5c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2f0.md) [`00c5c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c330.md)
- 新版 呼出元 1件 [`00c5d000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d000.md) · 呼出先 10件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d280.md) [`00c5d2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2b0.md) [`00c5d2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2c0.md) [`00c5d300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b91698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91630.md#insn-00b91698) · [`00b916bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91630.md#insn-00b916bc) · [`00b91720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91630.md#insn-00b91720)
- 新版 [`00b9268c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92624.md#insn-00b9268c) · [`00b926b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92624.md#insn-00b926b0) · [`00b92714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92624.md#insn-00b92714)

~~~diff
- 00b91698 ["INT_ADD", "register:40f0:8", ["const:b91698:8", "const:4:8"]]
- 00b91698 ["CALL", null, ["callee:00c5d2c0:8"]]
+ 00b9268c ["INT_ADD", "register:40f0:8", ["const:b9268c:8", "const:4:8"]]
+ 00b9268c ["CALL", null, ["callee:00c5d2c0:8"]]
- 00b91698 bytes 162b0394
+ 00b9268c bytes 0d2b0394
- 00b916bc ["INT_ADD", "register:40f0:8", ["const:b916bc:8", "const:4:8"]]
- 00b916bc ["CALL", null, ["callee:00c5d240:8"]]
+ 00b926b0 ["INT_ADD", "register:40f0:8", ["const:b926b0:8", "const:4:8"]]
+ 00b926b0 ["CALL", null, ["callee:00c5d240:8"]]
- 00b916bc bytes ed2a0394
+ 00b926b0 bytes e42a0394
- 00b91720 ["INT_ADD", "register:40f0:8", ["const:b91720:8", "const:4:8"]]
- 00b91720 ["CALL", null, ["callee:00c5d300:8"]]
+ 00b92714 ["INT_ADD", "register:40f0:8", ["const:b92714:8", "const:4:8"]]
+ 00b92714 ["CALL", null, ["callee:00c5d300:8"]]
- 00b91720 bytes 042b0394
+ 00b92714 bytes fb2a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2416be6150e861582e3491dee2e801f7"></a>

### [`00b91c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91c1c.md) → [`00b92c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92c10.md) _ZNK11flatbuffers7RPCCall9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5caf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5caf0.md) · 呼出先 8件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md) [`00c5c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c370.md) [`00c5c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c390.md) [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) [`00c5c430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c430.md)
- 新版 呼出元 1件 [`00c5dac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dac0.md) · 呼出先 8件 [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md) [`00c5d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d340.md) [`00c5d360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d360.md) [`00c5d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3e0.md) [`00c5d400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b91c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91c1c.md#insn-00b91c58) · [`00b91c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91c1c.md#insn-00b91c6c) · [`00b91c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91c1c.md#insn-00b91c8c)
- 新版 [`00b92c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92c10.md#insn-00b92c4c) · [`00b92c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92c10.md#insn-00b92c60) · [`00b92c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92c10.md#insn-00b92c80)

~~~diff
- 00b91c58 ["INT_ADD", "register:40f0:8", ["const:b91c58:8", "const:4:8"]]
- 00b91c58 ["CALL", null, ["callee:00c5d340:8"]]
+ 00b92c4c ["INT_ADD", "register:40f0:8", ["const:b92c4c:8", "const:4:8"]]
+ 00b92c4c ["CALL", null, ["callee:00c5d340:8"]]
- 00b91c58 bytes c6290394
+ 00b92c4c bytes bd290394
- 00b91c6c ["INT_ADD", "register:40f0:8", ["const:b91c6c:8", "const:4:8"]]
- 00b91c6c ["CALL", null, ["callee:00b93f28:8"]]
+ 00b92c60 ["INT_ADD", "register:40f0:8", ["const:b92c60:8", "const:4:8"]]
+ 00b92c60 ["CALL", null, ["callee:00b93f28:8"]]
- 00b91c6c bytes b2040094
+ 00b92c60 bytes b2040094
- 00b91c8c ["INT_ADD", "register:40f0:8", ["const:b91c8c:8", "const:4:8"]]
- 00b91c8c ["CALL", null, ["callee:00c5d360:8"]]
+ 00b92c80 ["INT_ADD", "register:40f0:8", ["const:b92c80:8", "const:4:8"]]
+ 00b92c80 ["CALL", null, ["callee:00c5d360:8"]]
- 00b91c8c bytes c1290394
+ 00b92c80 bytes b8290394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e55289783c5577519d84e726687cd175"></a>

### [`00b91d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91d24.md) → [`00b92d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92d18.md) _ZN11flatbuffers7RPCCall11DeserializeERNS_6ParserEPKN10reflection7RPCCallE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c900.md) · 呼出先 7件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d8d0.md) · 呼出先 7件 [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b91dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91d24.md#insn-00b91dac) · [`00b91dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91d24.md#insn-00b91dcc) · [`00b91dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91d24.md#insn-00b91dfc)
- 新版 [`00b92da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92d18.md#insn-00b92da0) · [`00b92dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92d18.md#insn-00b92dc0) · [`00b92df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92d18.md#insn-00b92df0)

~~~diff
- 00b91dac ["INT_ADD", "register:40f0:8", ["const:b91dac:8", "const:4:8"]]
- 00b91dac ["CALL", null, ["callee:00c58f30:8"]]
+ 00b92da0 ["INT_ADD", "register:40f0:8", ["const:b92da0:8", "const:4:8"]]
+ 00b92da0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b91dac bytes 6d180394
+ 00b92da0 bytes 64180394
- 00b91dcc ["INT_ADD", "register:40f0:8", ["const:b91dcc:8", "const:4:8"]]
- 00b91dcc ["CALL", null, ["callee:00c590a0:8"]]
+ 00b92dc0 ["INT_ADD", "register:40f0:8", ["const:b92dc0:8", "const:4:8"]]
+ 00b92dc0 ["CALL", null, ["callee:00c590a0:8"]]
- 00b91dcc bytes c1180394
+ 00b92dc0 bytes b8180394
- 00b91dfc ["INT_ADD", "register:40f0:8", ["const:b91dfc:8", "const:4:8"]]
- 00b91dfc ["CALL", null, ["callee:00c58f50:8"]]
+ 00b92df0 ["INT_ADD", "register:40f0:8", ["const:b92df0:8", "const:4:8"]]
+ 00b92df0 ["CALL", null, ["callee:00c58f50:8"]]
- 00b91dfc bytes 61180394
+ 00b92df0 bytes 58180394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-575207837d96dd38ba113438d269c92f"></a>

### [`00b92580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92580.md) → [`00b93574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93574.md) _ZNK11flatbuffers7EnumVal9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cae0.md) · 呼出先 5件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md) [`00c5c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c060.md) [`00c5c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c370.md) [`00c5c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c390.md) [`00c5caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5caa0.md)
- 新版 呼出元 1件 [`00c5dab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dab0.md) · 呼出先 5件 [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md) [`00c5d030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d030.md) [`00c5d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d340.md) [`00c5d360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d360.md) [`00c5da70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b925bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92580.md#insn-00b925bc) · [`00b925cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92580.md#insn-00b925cc) · [`00b925e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92580.md#insn-00b925e0)
- 新版 [`00b935b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93574.md#insn-00b935b0) · [`00b935c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93574.md#insn-00b935c0) · [`00b935d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93574.md#insn-00b935d4)

~~~diff
- 00b925bc ["INT_ADD", "register:40f0:8", ["const:b925bc:8", "const:4:8"]]
- 00b925bc ["CALL", null, ["callee:00c5d340:8"]]
+ 00b935b0 ["INT_ADD", "register:40f0:8", ["const:b935b0:8", "const:4:8"]]
+ 00b935b0 ["CALL", null, ["callee:00c5d340:8"]]
- 00b925bc bytes 6d270394
+ 00b935b0 bytes 64270394
- 00b925cc ["INT_ADD", "register:40f0:8", ["const:b925cc:8", "const:4:8"]]
- 00b925cc ["CALL", null, ["callee:00c5da70:8"]]
+ 00b935c0 ["INT_ADD", "register:40f0:8", ["const:b935c0:8", "const:4:8"]]
+ 00b935c0 ["CALL", null, ["callee:00c5da70:8"]]
- 00b925cc bytes 35290394
+ 00b935c0 bytes 2c290394
- 00b925e0 ["INT_ADD", "register:40f0:8", ["const:b925e0:8", "const:4:8"]]
- 00b925e0 ["CALL", null, ["callee:00b93f28:8"]]
+ 00b935d4 ["INT_ADD", "register:40f0:8", ["const:b935d4:8", "const:4:8"]]
+ 00b935d4 ["CALL", null, ["callee:00b93f28:8"]]
- 00b925e0 bytes 55020094
+ 00b935d4 bytes 55020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656f34d7f4b8dbdca04f87c6a17d4d82"></a>

### [`00b92640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92640.md) → [`00b93634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93634.md) _ZN11flatbuffers7EnumDef11DeserializeERNS_6ParserEPKN10reflection4EnumE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8d0.md) · 呼出先 11件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d8a0.md) · 呼出先 11件 [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b926c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92640.md#insn-00b926c8) · [`00b926e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92640.md#insn-00b926e8) · [`00b926fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92640.md#insn-00b926fc)
- 新版 [`00b936bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93634.md#insn-00b936bc) · [`00b936dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93634.md#insn-00b936dc) · [`00b936f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93634.md#insn-00b936f0)

~~~diff
- 00b926c8 ["INT_ADD", "register:40f0:8", ["const:b926c8:8", "const:4:8"]]
- 00b926c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b936bc ["INT_ADD", "register:40f0:8", ["const:b936bc:8", "const:4:8"]]
+ 00b936bc ["CALL", null, ["callee:00c58f30:8"]]
- 00b926c8 bytes 26160394
+ 00b936bc bytes 1d160394
- 00b926e8 ["INT_ADD", "register:40f0:8", ["const:b926e8:8", "const:4:8"]]
- 00b926e8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b936dc ["INT_ADD", "register:40f0:8", ["const:b936dc:8", "const:4:8"]]
+ 00b936dc ["CALL", null, ["callee:00c590a0:8"]]
- 00b926e8 bytes 7a160394
+ 00b936dc bytes 71160394
- 00b926fc ["INT_ADD", "register:40f0:8", ["const:b926fc:8", "const:4:8"]]
- 00b926fc ["CALL", null, ["callee:00c5d680:8"]]
+ 00b936f0 ["INT_ADD", "register:40f0:8", ["const:b936f0:8", "const:4:8"]]
+ 00b936f0 ["CALL", null, ["callee:00c5d680:8"]]
- 00b926fc bytes ed270394
+ 00b936f0 bytes e4270394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b59d50ad8658c94906c2410e6b6710"></a>

### [`00b92a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md) → [`00b93a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93a54.md) _ZN11flatbuffers7EnumVal11DeserializeERNS_6ParserEPKN10reflection7EnumValE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8f0.md) · 呼出先 7件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d8c0.md) · 呼出先 7件 [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92ae8) · [`00b92b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92b08) · [`00b92b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92b38)
- 新版 [`00b93adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93a54.md#insn-00b93adc) · [`00b93afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93a54.md#insn-00b93afc) · [`00b93b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93a54.md#insn-00b93b2c)

~~~diff
- 00b92ae8 ["INT_ADD", "register:40f0:8", ["const:b92ae8:8", "const:4:8"]]
- 00b92ae8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b93adc ["INT_ADD", "register:40f0:8", ["const:b93adc:8", "const:4:8"]]
+ 00b93adc ["CALL", null, ["callee:00c58f30:8"]]
- 00b92ae8 bytes 1e150394
+ 00b93adc bytes 15150394
- 00b92b08 ["INT_ADD", "register:40f0:8", ["const:b92b08:8", "const:4:8"]]
- 00b92b08 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b93afc ["INT_ADD", "register:40f0:8", ["const:b93afc:8", "const:4:8"]]
+ 00b93afc ["CALL", null, ["callee:00c590a0:8"]]
- 00b92b08 bytes 72150394
+ 00b93afc bytes 69150394
- 00b92b38 ["INT_ADD", "register:40f0:8", ["const:b92b38:8", "const:4:8"]]
- 00b92b38 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b93b2c ["INT_ADD", "register:40f0:8", ["const:b93b2c:8", "const:4:8"]]
+ 00b93b2c ["CALL", null, ["callee:00c58f50:8"]]
- 00b92b38 bytes 12150394
+ 00b93b2c bytes 09150394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14ec4482d9408303c96be9d7d6cab5e9"></a>

### [`00b92d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md) → [`00b93d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93d54.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c150.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d120.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md#insn-00b92df0) · [`00b92dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md#insn-00b92dfc) · [`00b92e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md#insn-00b92e24)
- 新版 [`00b93de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93d54.md#insn-00b93de4) · [`00b93df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93d54.md#insn-00b93df0) · [`00b93e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93d54.md#insn-00b93e18)

~~~diff
- 00b92df0 ["INT_ADD", "register:40f0:8", ["const:b92df0:8", "const:4:8"]]
- 00b92df0 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b93de4 ["INT_ADD", "register:40f0:8", ["const:b93de4:8", "const:4:8"]]
+ 00b93de4 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b92df0 bytes 08210394
+ 00b93de4 bytes ff200394
- 00b92dfc ["INT_ADD", "register:40f0:8", ["const:b92dfc:8", "const:4:8"]]
- 00b92dfc ["CALL", null, ["callee:00c58f30:8"]]
+ 00b93df0 ["INT_ADD", "register:40f0:8", ["const:b93df0:8", "const:4:8"]]
+ 00b93df0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b92dfc bytes 59140394
+ 00b93df0 bytes 50140394
- 00b92e24 ["INT_ADD", "register:40f0:8", ["const:b92e24:8", "const:4:8"]]
- 00b92e24 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b93e18 ["INT_ADD", "register:40f0:8", ["const:b93e18:8", "const:4:8"]]
+ 00b93e18 ["CALL", null, ["callee:00c590a0:8"]]
- 00b92e24 bytes ab140394
+ 00b93e18 bytes a2140394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e92eab09f6973c6bc9c32d261dee898a"></a>

### [`00b92f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f18.md) → [`00b93f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f0c.md) _ZNK11flatbuffers7EnumVal19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f18.md#insn-00b92f24)
- 新版 [`00b93f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f0c.md#insn-00b93f18)

~~~diff
- 00b92f24 ["INT_ADD", "register:40f0:8", ["const:b92f24:8", "const:4:8"]]
- 00b92f24 ["CALL", null, ["callee:00b93f28:8"]]
+ 00b93f18 ["INT_ADD", "register:40f0:8", ["const:b93f18:8", "const:4:8"]]
+ 00b93f18 ["CALL", null, ["callee:00b93f28:8"]]
- 00b92f24 bytes 04000094
+ 00b93f18 bytes 04000094
~~~


<a id="compare-4c228718e2981f3a6a8fd16867431b1b"></a>

### [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md) → [`00b93f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md) FUN_00b93f28

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b8ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md) [`00b8f154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8f/00b8f154.md) [`00b8f5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8f/00b8f5d0.md) [`00b902c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b902c8.md) [`00b906c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906c8.md) · 呼出先 10件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 8件 [`00b8fe00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8fe00.md) [`00b90148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b90/00b90148.md) [`00b905c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b90/00b905c4.md) [`00b912bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b912bc.md) [`00b916bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b916bc.md) · 呼出先 10件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md#insn-00b92fb4) · [`00b92fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md#insn-00b92fe0) · [`00b9300c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md#insn-00b9300c)
- 新版 [`00b93fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md#insn-00b93fa8) · [`00b93fd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md#insn-00b93fd4) · [`00b94000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b93f28.md#insn-00b94000)

~~~diff
- 00b92fb4 ["INT_ADD", "register:40f0:8", ["const:b92fb4:8", "const:4:8"]]
- 00b92fb4 ["CALL", null, ["callee:00c5db60:8"]]
+ 00b93fa8 ["INT_ADD", "register:40f0:8", ["const:b93fa8:8", "const:4:8"]]
+ 00b93fa8 ["CALL", null, ["callee:00c5db60:8"]]
- 00b92fb4 bytes f7260394
+ 00b93fa8 bytes ee260394
- 00b92fe0 ["INT_ADD", "register:40f0:8", ["const:b92fe0:8", "const:4:8"]]
- 00b92fe0 ["CALL", null, ["callee:00c5d340:8"]]
+ 00b93fd4 ["INT_ADD", "register:40f0:8", ["const:b93fd4:8", "const:4:8"]]
+ 00b93fd4 ["CALL", null, ["callee:00c5d340:8"]]
- 00b92fe0 bytes e4240394
+ 00b93fd4 bytes db240394
- 00b9300c ["INT_ADD", "register:40f0:8", ["const:b9300c:8", "const:4:8"]]
- 00b9300c ["CALL", null, ["callee:00c5d340:8"]]
+ 00b94000 ["INT_ADD", "register:40f0:8", ["const:b94000:8", "const:4:8"]]
+ 00b94000 ["CALL", null, ["callee:00c5d340:8"]]
- 00b9300c bytes d9240394
+ 00b94000 bytes d0240394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4545027890f99cf5a8eec101d4a2dcde"></a>

### [`00b935a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md) → [`00b94594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94594.md) _ZN10reflection13CreateEnumValERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEElNS4_INS_4TypeEEENS4_INS0_6VectorIS6_j

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c060.md) · 呼出先 7件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c330.md) [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) [`00c5c420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c420.md) [`00c5c440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c440.md)
- 新版 呼出元 1件 [`00c5d030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d030.md) · 呼出先 7件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d300.md) [`00c5d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3e0.md) [`00c5d3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3f0.md) [`00c5d410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b935ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b935ec) · [`00b93610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b93610) · [`00b9365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b9365c)
- 新版 [`00b945e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94594.md#insn-00b945e0) · [`00b94604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94594.md#insn-00b94604) · [`00b94650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94594.md#insn-00b94650)

~~~diff
- 00b935ec ["INT_ADD", "register:40f0:8", ["const:b935ec:8", "const:4:8"]]
- 00b935ec ["CALL", null, ["callee:00c5d300:8"]]
+ 00b945e0 ["INT_ADD", "register:40f0:8", ["const:b945e0:8", "const:4:8"]]
+ 00b945e0 ["CALL", null, ["callee:00c5d300:8"]]
- 00b935ec bytes 51230394
+ 00b945e0 bytes 48230394
- 00b93610 ["INT_ADD", "register:40f0:8", ["const:b93610:8", "const:4:8"]]
- 00b93610 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b94604 ["INT_ADD", "register:40f0:8", ["const:b94604:8", "const:4:8"]]
+ 00b94604 ["CALL", null, ["callee:00c5d240:8"]]
- 00b93610 bytes 18230394
+ 00b94604 bytes 0f230394
- 00b9365c ["INT_ADD", "register:40f0:8", ["const:b9365c:8", "const:4:8"]]
- 00b9365c ["CALL", null, ["callee:00c5d490:8"]]
+ 00b94650 ["INT_ADD", "register:40f0:8", ["const:b94650:8", "const:4:8"]]
+ 00b94650 ["CALL", null, ["callee:00c5d490:8"]]
- 00b9365c bytes 99230394
+ 00b94650 bytes 90230394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b187e7e0468ae19f36908b87c50385a"></a>

### [`00b936b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md) → [`00b946ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b946ac.md) _ZN10reflection10CreateTypeERN11flatbuffers21FlatBufferBuilderImplILb0EEENS_8BaseTypeES4_itjj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c020.md) · 呼出先 6件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2a0.md) [`00c5c2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2e0.md) [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5cff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cff0.md) · 呼出先 6件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d270.md) [`00c5d2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2b0.md) [`00c5d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2e0.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b93708) · [`00b9372c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b9372c) · [`00b93790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b93790)
- 新版 [`00b946fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b946ac.md#insn-00b946fc) · [`00b94720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b946ac.md#insn-00b94720) · [`00b94784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b946ac.md#insn-00b94784)

~~~diff
- 00b93708 ["INT_ADD", "register:40f0:8", ["const:b93708:8", "const:4:8"]]
- 00b93708 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b946fc ["INT_ADD", "register:40f0:8", ["const:b946fc:8", "const:4:8"]]
+ 00b946fc ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b93708 bytes 06230394
+ 00b946fc bytes fd220394
- 00b9372c ["INT_ADD", "register:40f0:8", ["const:b9372c:8", "const:4:8"]]
- 00b9372c ["CALL", null, ["callee:00c5d240:8"]]
+ 00b94720 ["INT_ADD", "register:40f0:8", ["const:b94720:8", "const:4:8"]]
+ 00b94720 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9372c bytes d1220394
+ 00b94720 bytes c8220394
- 00b93790 ["INT_ADD", "register:40f0:8", ["const:b93790:8", "const:4:8"]]
- 00b93790 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b94784 ["INT_ADD", "register:40f0:8", ["const:b94784:8", "const:4:8"]]
+ 00b94784 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b93790 bytes e4220394
+ 00b94784 bytes db220394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7cd2507f324585651535bb91efc4538"></a>

### [`00b94ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md) → [`00b95dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b95/00b95dd0.md) FUN_00b95dd0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b93b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93b00.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00b94af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94af4.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b94ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94ea4) · [`00b94ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94ec4) · [`00b94f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94f2c)
- 新版 [`00b95e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b95/00b95dd0.md#insn-00b95e98) · [`00b95eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b95/00b95dd0.md#insn-00b95eb8) · [`00b95f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b95/00b95dd0.md#insn-00b95f20)

~~~diff
- 00b94ea4 ["INT_ADD", "register:40f0:8", ["const:b94ea4:8", "const:4:8"]]
- 00b94ea4 ["CALL", null, ["callee:00c5e000:8"]]
+ 00b95e98 ["INT_ADD", "register:40f0:8", ["const:b95e98:8", "const:4:8"]]
+ 00b95e98 ["CALL", null, ["callee:00c5e000:8"]]
- 00b94ea4 bytes 63200394
+ 00b95e98 bytes 5a200394
- 00b94ec4 ["INT_ADD", "register:40f0:8", ["const:b94ec4:8", "const:4:8"]]
- 00b94ec4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b95eb8 ["INT_ADD", "register:40f0:8", ["const:b95eb8:8", "const:4:8"]]
+ 00b95eb8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b94ec4 bytes 270c0394
+ 00b95eb8 bytes 1e0c0394
- 00b94f2c ["INT_ADD", "register:40f0:8", ["const:b94f2c:8", "const:4:8"]]
- 00b94f2c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b95f20 ["INT_ADD", "register:40f0:8", ["const:b95f20:8", "const:4:8"]]
+ 00b95f20 ["CALL", null, ["callee:00c58f30:8"]]
- 00b94f2c bytes 0d0c0394
+ 00b95f20 bytes 040c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

