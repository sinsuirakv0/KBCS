# v16.0.2 → v16.0.3 · 要調査の変更候補 (34)

[一覧の目次](README.md)

<a id="compare-fc0069443a86f9db08d5f45c80dc167d"></a>

### [`00b95a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95a4c.md) → [`00b96a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96a40.md) _ZN11flatbuffers11EqualByNameERKNS_4TypeES2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0a0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5d070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d070.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95a4c.md#insn-00b95b18) · [`00b95bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95a4c.md#insn-00b95bcc)
- 新版 [`00b96b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96a40.md#insn-00b96b0c) · [`00b96bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96a40.md#insn-00b96bc0)

~~~diff
- 00b95b18 ["INT_ADD", "register:40f0:8", ["const:b95b18:8", "const:4:8"]]
- 00b95b18 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b96b0c ["INT_ADD", "register:40f0:8", ["const:b96b0c:8", "const:4:8"]]
+ 00b96b0c ["CALL", null, ["callee:00c590f0:8"]]
- 00b95b18 bytes 82090394
+ 00b96b0c bytes 79090394
- 00b95bcc ["INT_ADD", "register:40f0:8", ["const:b95bcc:8", "const:4:8"]]
- 00b95bcc ["CALL", null, ["callee:00c590f0:8"]]
+ 00b96bc0 ["INT_ADD", "register:40f0:8", ["const:b96bc0:8", "const:4:8"]]
+ 00b96bc0 ["CALL", null, ["callee:00c590f0:8"]]
- 00b95bcc bytes 55090394
+ 00b96bc0 bytes 4c090394
~~~


<a id="compare-4856ba20e1086e36475414057315db44"></a>

### [`00b95be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md) → [`00b96bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96bd8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) · 呼出先 2件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)
- 新版 呼出元 1件 [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) · 呼出先 2件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md#insn-00b95c50) · [`00b95c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md#insn-00b95c74)
- 新版 [`00b96c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96bd8.md#insn-00b96c44) · [`00b96c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96bd8.md#insn-00b96c68)

~~~diff
- 00b95c50 ["INT_ADD", "register:40f0:8", ["const:b95c50:8", "const:4:8"]]
- 00b95c50 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b96c44 ["INT_ADD", "register:40f0:8", ["const:b96c44:8", "const:4:8"]]
+ 00b96c44 ["CALL", null, ["callee:00c5b980:8"]]
- 00b95c50 bytes 58130394
+ 00b96c44 bytes 4f130394
- 00b95c74 ["INT_ADD", "register:40f0:8", ["const:b95c74:8", "const:4:8"]]
- 00b95c74 ["CALL", null, ["callee:00c59130:8"]]
+ 00b96c68 ["INT_ADD", "register:40f0:8", ["const:b96c68:8", "const:4:8"]]
+ 00b96c68 ["CALL", null, ["callee:00c59130:8"]]
- 00b95c74 bytes 3b090394
+ 00b96c68 bytes 32090394
~~~


<a id="compare-e71459ac9c10b1bd27340554e3cb33ea"></a>

### [`00b95f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95f6c.md) → [`00b96f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96f60.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb60.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db30.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95f6c.md#insn-00b96004) · [`00b9604c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95f6c.md#insn-00b9604c)
- 新版 [`00b96ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96f60.md#insn-00b96ff8) · [`00b97040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96f60.md#insn-00b97040)

~~~diff
- 00b96004 ["INT_ADD", "register:40f0:8", ["const:b96004:8", "const:4:8"]]
- 00b96004 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b96ff8 ["INT_ADD", "register:40f0:8", ["const:b96ff8:8", "const:4:8"]]
+ 00b96ff8 ["CALL", null, ["callee:00c590f0:8"]]
- 00b96004 bytes 47080394
+ 00b96ff8 bytes 3e080394
- 00b9604c ["INT_ADD", "register:40f0:8", ["const:b9604c:8", "const:4:8"]]
- 00b9604c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b97040 ["INT_ADD", "register:40f0:8", ["const:b97040:8", "const:4:8"]]
+ 00b97040 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9604c bytes 35080394
+ 00b97040 bytes 2c080394
~~~


<a id="compare-f9deabdd952c185d7045205da0aa5bb4"></a>

### [`00b96080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96080.md) → [`00b97074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97074.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfa0.md) · 呼出先 5件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md) [`00c5cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfb0.md)
- 新版 呼出元 1件 [`00c5df70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df70.md) · 呼出先 5件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5cb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb00.md) [`00c5df80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9617c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96080.md#insn-00b9617c) · [`00b961f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96080.md#insn-00b961f8) · [`00b96268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96080.md#insn-00b96268)
- 新版 [`00b97170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97074.md#insn-00b97170) · [`00b971ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97074.md#insn-00b971ec) · [`00b9725c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97074.md#insn-00b9725c)

~~~diff
- 00b9617c ["INT_ADD", "register:40f0:8", ["const:b9617c:8", "const:4:8"]]
- 00b9617c ["CALL", null, ["callee:00c5c150:8"]]
+ 00b97170 ["INT_ADD", "register:40f0:8", ["const:b97170:8", "const:4:8"]]
+ 00b97170 ["CALL", null, ["callee:00c5c150:8"]]
- 00b9617c bytes 01140394
+ 00b97170 bytes f8130394
- 00b961f8 ["INT_ADD", "register:40f0:8", ["const:b961f8:8", "const:4:8"]]
- 00b961f8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b971ec ["INT_ADD", "register:40f0:8", ["const:b971ec:8", "const:4:8"]]
+ 00b971ec ["CALL", null, ["callee:00c590f0:8"]]
- 00b961f8 bytes ca070394
+ 00b971ec bytes c1070394
- 00b96268 ["INT_ADD", "register:40f0:8", ["const:b96268:8", "const:4:8"]]
- 00b96268 ["CALL", null, ["callee:00c5c680:8"]]
+ 00b9725c ["INT_ADD", "register:40f0:8", ["const:b9725c:8", "const:4:8"]]
+ 00b9725c ["CALL", null, ["callee:00c5c680:8"]]
- 00b96268 bytes 12150394
+ 00b9725c bytes 09150394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0422c8c35a310754048519fb828b4a1d"></a>

### [`00b9640c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b9640c.md) → [`00b97400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97400.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfb0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df80.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9642c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b9640c.md#insn-00b9642c) · [`00b9643c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b9640c.md#insn-00b9643c) · [`00b964b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b9640c.md#insn-00b964b4)
- 新版 [`00b97420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97400.md#insn-00b97420) · [`00b97430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97400.md#insn-00b97430) · [`00b974a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97400.md#insn-00b974a8)

~~~diff
- 00b9642c ["INT_ADD", "register:40f0:8", ["const:b9642c:8", "const:4:8"]]
- 00b9642c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b97420 ["INT_ADD", "register:40f0:8", ["const:b97420:8", "const:4:8"]]
+ 00b97420 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9642c bytes cd060394
+ 00b97420 bytes c4060394
- 00b9643c ["INT_ADD", "register:40f0:8", ["const:b9643c:8", "const:4:8"]]
- 00b9643c ["CALL", null, ["callee:00c5c650:8"]]
+ 00b97430 ["INT_ADD", "register:40f0:8", ["const:b97430:8", "const:4:8"]]
+ 00b97430 ["CALL", null, ["callee:00c5c650:8"]]
- 00b9643c bytes 91140394
+ 00b97430 bytes 88140394
- 00b964b4 ["INT_ADD", "register:40f0:8", ["const:b964b4:8", "const:4:8"]]
- 00b964b4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b974a8 ["INT_ADD", "register:40f0:8", ["const:b974a8:8", "const:4:8"]]
+ 00b974a8 ["CALL", null, ["callee:00c590f0:8"]]
- 00b964b4 bytes 1b070394
+ 00b974a8 bytes 12070394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40df3e056e60014bdcab70ae6b5c2735"></a>

### [`00b96540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96540.md) → [`00b97534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97534.md) _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_co

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d130.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e100.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96540.md#insn-00b96588) · [`00b965c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96540.md#insn-00b965c4) · [`00b965f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96540.md#insn-00b965f8)
- 新版 [`00b9757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97534.md#insn-00b9757c) · [`00b975b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97534.md#insn-00b975b8) · [`00b975ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97534.md#insn-00b975ec)

~~~diff
- 00b96588 ["INT_ADD", "register:40f0:8", ["const:b96588:8", "const:4:8"]]
- 00b96588 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b9757c ["INT_ADD", "register:40f0:8", ["const:b9757c:8", "const:4:8"]]
+ 00b9757c ["CALL", null, ["callee:00c58f50:8"]]
- 00b96588 bytes 7e060394
+ 00b9757c bytes 75060394
- 00b965c4 ["INT_ADD", "register:40f0:8", ["const:b965c4:8", "const:4:8"]]
- 00b965c4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b975b8 ["INT_ADD", "register:40f0:8", ["const:b975b8:8", "const:4:8"]]
+ 00b975b8 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b965c4 bytes 13130394
+ 00b975b8 bytes 0a130394
- 00b965f8 ["INT_ADD", "register:40f0:8", ["const:b965f8:8", "const:4:8"]]
- 00b965f8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b975ec ["INT_ADD", "register:40f0:8", ["const:b975ec:8", "const:4:8"]]
+ 00b975ec ["CALL", null, ["callee:00c58fe0:8"]]
- 00b965f8 bytes 86060394
+ 00b975ec bytes 7d060394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5118f92e7b8ad37b91c5fbf93f0ef73"></a>

### [`00b98ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ca4.md) → [`00b99c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99c98.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ca4.md#insn-00b98cb8)
- 新版 [`00b99cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99c98.md#insn-00b99cac)

~~~diff
- 00b98cb8 ["INT_ADD", "register:40f0:8", ["const:b98cb8:8", "const:4:8"]]
- 00b98cb8 ["CALL", null, ["callee:00c5e180:8"]]
+ 00b99cac ["INT_ADD", "register:40f0:8", ["const:b99cac:8", "const:4:8"]]
+ 00b99cac ["CALL", null, ["callee:00c5e180:8"]]
- 00b98cb8 bytes 3e110394
+ 00b99cac bytes 35110394
~~~


<a id="compare-f8f956dd8e276cfa365ba523130ecd86"></a>

### [`00b98ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ce0.md) → [`00b99cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99cd4.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ce0.md#insn-00b98cfc)
- 新版 [`00b99cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99cd4.md#insn-00b99cf0)

~~~diff
- 00b98cfc ["INT_ADD", "register:40f0:8", ["const:b98cfc:8", "const:4:8"]]
- 00b98cfc ["CALL", null, ["callee:00c5e180:8"]]
+ 00b99cf0 ["INT_ADD", "register:40f0:8", ["const:b99cf0:8", "const:4:8"]]
+ 00b99cf0 ["CALL", null, ["callee:00c5e180:8"]]
- 00b98cfc bytes 2d110394
+ 00b99cf0 bytes 24110394
~~~


<a id="compare-008d207d86f34b5bbeebde5d06986db7"></a>

### [`00b99160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md) → [`00b9a154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a154.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b991e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md#insn-00b991e0) · [`00b991f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md#insn-00b991f4)
- 新版 [`00b9a1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a154.md#insn-00b9a1d4) · [`00b9a1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a154.md#insn-00b9a1e8)

~~~diff
- 00b991e0 ["INT_ADD", "register:40f0:8", ["const:b991e0:8", "const:4:8"]]
- 00b991e0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9a1d4 ["INT_ADD", "register:40f0:8", ["const:b9a1d4:8", "const:4:8"]]
+ 00b9a1d4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b991e0 bytes bcfb0294
+ 00b9a1d4 bytes b3fb0294
- 00b991f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b991f4 ["INT_ADD", "register:40f0:8", ["const:b991f4:8", "const:4:8"]]
- 00b991f4 ["CALLIND", null, ["register:0:8"]]
+ 00b9a1e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a1e8 ["INT_ADD", "register:40f0:8", ["const:b9a1e8:8", "const:4:8"]]
+ 00b9a1e8 ["CALLIND", null, ["register:0:8"]]
- 00b991f4 bytes 00013fd6
+ 00b9a1e8 bytes 00013fd6
~~~


<a id="compare-9f2338721b5714cf9bff379f4d6b15f0"></a>

### [`00b99278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99278.md) → [`00b9a26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a26c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99278.md#insn-00b99290)
- 新版 [`00b9a284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a26c.md#insn-00b9a284)

~~~diff
- 00b99290 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99290 ["INT_ADD", "register:40f0:8", ["const:b99290:8", "const:4:8"]]
- 00b99290 ["CALLIND", null, ["register:0:8"]]
+ 00b9a284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a284 ["INT_ADD", "register:40f0:8", ["const:b9a284:8", "const:4:8"]]
+ 00b9a284 ["CALLIND", null, ["register:0:8"]]
- 00b99290 bytes 00013fd6
+ 00b9a284 bytes 00013fd6
~~~


<a id="compare-fe00fd627ccb926b64218bf2dcd1c44c"></a>

### [`00b99328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md) → [`00b9a31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a31c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9939c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md#insn-00b9939c) · [`00b993b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md#insn-00b993b4)
- 新版 [`00b9a390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a31c.md#insn-00b9a390) · [`00b9a3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a31c.md#insn-00b9a3a8)

~~~diff
- 00b9939c ["INT_ADD", "register:40f0:8", ["const:b9939c:8", "const:4:8"]]
- 00b9939c ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9a390 ["INT_ADD", "register:40f0:8", ["const:b9a390:8", "const:4:8"]]
+ 00b9a390 ["CALL", null, ["callee:00c590a0:8"]]
- 00b9939c bytes 4dfb0294
+ 00b9a390 bytes 44fb0294
- 00b993b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b993b4 ["INT_ADD", "register:40f0:8", ["const:b993b4:8", "const:4:8"]]
- 00b993b4 ["CALLIND", null, ["register:0:8"]]
+ 00b9a3a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a3a8 ["INT_ADD", "register:40f0:8", ["const:b9a3a8:8", "const:4:8"]]
+ 00b9a3a8 ["CALLIND", null, ["register:0:8"]]
- 00b993b4 bytes 00013fd6
+ 00b9a3a8 bytes 00013fd6
~~~


<a id="compare-6d226b2276192de53fc4c3cd8c8df2f1"></a>

### [`00b993f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md) → [`00b9a3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a3e4.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b994a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md#insn-00b994a0) · [`00b9951c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md#insn-00b9951c)
- 新版 [`00b9a494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a3e4.md#insn-00b9a494) · [`00b9a510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a3e4.md#insn-00b9a510)

~~~diff
- 00b994a0 ["INT_ADD", "register:40f0:8", ["const:b994a0:8", "const:4:8"]]
- 00b994a0 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b9a494 ["INT_ADD", "register:40f0:8", ["const:b9a494:8", "const:4:8"]]
+ 00b9a494 ["CALL", null, ["callee:00c5b980:8"]]
- 00b994a0 bytes 44050394
+ 00b9a494 bytes 3b050394
- 00b9951c ["INT_ADD", "register:40f0:8", ["const:b9951c:8", "const:4:8"]]
- 00b9951c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00b9a510 ["INT_ADD", "register:40f0:8", ["const:b9a510:8", "const:4:8"]]
+ 00b9a510 ["CALL", null, ["callee:00c5cf10:8"]]
- 00b9951c bytes 890a0394
+ 00b9a510 bytes 800a0394
~~~


<a id="compare-d562f4704b5e785eee97ba3c426456e6"></a>

### [`00b9968c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9968c.md) → [`00b9a680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a680.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md) · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)
- 新版 呼出元 1件 [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md) · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md) [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b996c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9968c.md#insn-00b996c4) · [`00b996e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9968c.md#insn-00b996e0) · [`00b99700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9968c.md#insn-00b99700)
- 新版 [`00b9a6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a680.md#insn-00b9a6b8) · [`00b9a6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a680.md#insn-00b9a6d4) · [`00b9a6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a680.md#insn-00b9a6f4)

~~~diff
- 00b996c4 ["INT_ADD", "register:40f0:8", ["const:b996c4:8", "const:4:8"]]
- 00b996c4 ["CALL", null, ["callee:00c59f90:8"]]
+ 00b9a6b8 ["INT_ADD", "register:40f0:8", ["const:b9a6b8:8", "const:4:8"]]
+ 00b9a6b8 ["CALL", null, ["callee:00c59f90:8"]]
- 00b996c4 bytes 3ffe0294
+ 00b9a6b8 bytes 36fe0294
- 00b996e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b996e0 ["INT_ADD", "register:40f0:8", ["const:b996e0:8", "const:4:8"]]
- 00b996e0 ["CALLIND", null, ["register:0:8"]]
+ 00b9a6d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a6d4 ["INT_ADD", "register:40f0:8", ["const:b9a6d4:8", "const:4:8"]]
+ 00b9a6d4 ["CALLIND", null, ["register:0:8"]]
- 00b996e0 bytes 00013fd6
+ 00b9a6d4 bytes 00013fd6
- 00b99700 ["INT_ADD", "register:40f0:8", ["const:b99700:8", "const:4:8"]]
- 00b99700 ["CALL", null, ["callee:00c59340:8"]]
+ 00b9a6f4 ["INT_ADD", "register:40f0:8", ["const:b9a6f4:8", "const:4:8"]]
+ 00b9a6f4 ["CALL", null, ["callee:00c59340:8"]]
- 00b99700 bytes 1cfb0294
+ 00b9a6f4 bytes 13fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd00c4543cf52b113a86c0adec695df"></a>

### [`00b9977c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9977c.md) → [`00b9a770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a770.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9977c.md#insn-00b99854) · [`00b9989c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9977c.md#insn-00b9989c) · [`00b99984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9977c.md#insn-00b99984)
- 新版 [`00b9a848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a770.md#insn-00b9a848) · [`00b9a890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a770.md#insn-00b9a890) · [`00b9a978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a770.md#insn-00b9a978)

~~~diff
- 00b99854 ["INT_ADD", "register:40f0:8", ["const:b99854:8", "const:4:8"]]
- 00b99854 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9a848 ["INT_ADD", "register:40f0:8", ["const:b9a848:8", "const:4:8"]]
+ 00b9a848 ["CALL", null, ["callee:00c58f30:8"]]
- 00b99854 bytes c3f90294
+ 00b9a848 bytes baf90294
- 00b9989c ["INT_ADD", "register:40f0:8", ["const:b9989c:8", "const:4:8"]]
- 00b9989c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9a890 ["INT_ADD", "register:40f0:8", ["const:b9a890:8", "const:4:8"]]
+ 00b9a890 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9989c bytes b1f90294
+ 00b9a890 bytes a8f90294
- 00b99984 ["INT_ADD", "register:40f0:8", ["const:b99984:8", "const:4:8"]]
- 00b99984 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b9a978 ["INT_ADD", "register:40f0:8", ["const:b9a978:8", "const:4:8"]]
+ 00b9a978 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b99984 bytes 23060394
+ 00b9a978 bytes 1a060394
~~~


<a id="compare-04152e062939127d57d86f7e5c2757f3"></a>

### [`00b99988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md) → [`00b9a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md) FUN_00b9a97c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00b8a49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a49c.md) [`00b8a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md) [`00b9b798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b798.md) [`00bb0110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0110.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 4件 [`00b8b490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b490.md) [`00b8b5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md) [`00b9c78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c78c.md) [`00bb1104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1104.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md#insn-00b99a08) · [`00b99a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md#insn-00b99a14) · [`00b99a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md#insn-00b99a44)
- 新版 [`00b9a9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md#insn-00b9a9fc) · [`00b9aa08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md#insn-00b9aa08) · [`00b9aa38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md#insn-00b9aa38)

~~~diff
- 00b99a08 ["INT_ADD", "register:40f0:8", ["const:b99a08:8", "const:4:8"]]
- 00b99a08 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b9a9fc ["INT_ADD", "register:40f0:8", ["const:b9a9fc:8", "const:4:8"]]
+ 00b9a9fc ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b99a08 bytes 02060394
+ 00b9a9fc bytes f9050394
- 00b99a14 ["INT_ADD", "register:40f0:8", ["const:b99a14:8", "const:4:8"]]
- 00b99a14 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9aa08 ["INT_ADD", "register:40f0:8", ["const:b9aa08:8", "const:4:8"]]
+ 00b9aa08 ["CALL", null, ["callee:00c58f30:8"]]
- 00b99a14 bytes 53f90294
+ 00b9aa08 bytes 4af90294
- 00b99a44 ["INT_ADD", "register:40f0:8", ["const:b99a44:8", "const:4:8"]]
- 00b99a44 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9aa38 ["INT_ADD", "register:40f0:8", ["const:b9aa38:8", "const:4:8"]]
+ 00b9aa38 ["CALL", null, ["callee:00c590a0:8"]]
- 00b99a44 bytes a3f90294
+ 00b9aa38 bytes 9af90294
~~~


<a id="compare-cd6f5a3357249426013ba59c2f680dc6"></a>

### [`00b9a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a5a0.md) → [`00b9b594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b594.md) _ZNSt6__ndk17__sort3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEjT0_S9_S9_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d160.md) · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 1件 [`00c5e130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e130.md) · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a5a0.md#insn-00b9a5e4) · [`00b9a610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a5a0.md#insn-00b9a610) · [`00b9a684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a5a0.md#insn-00b9a684)
- 新版 [`00b9b5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b594.md#insn-00b9b5d8) · [`00b9b604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b594.md#insn-00b9b604) · [`00b9b678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b594.md#insn-00b9b678)

~~~diff
- 00b9a5e4 ["INT_ADD", "register:40f0:8", ["const:b9a5e4:8", "const:4:8"]]
- 00b9a5e4 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b5d8 ["INT_ADD", "register:40f0:8", ["const:b9b5d8:8", "const:4:8"]]
+ 00b9b5d8 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a5e4 bytes cf040394
+ 00b9b5d8 bytes c6040394
- 00b9a610 ["INT_ADD", "register:40f0:8", ["const:b9a610:8", "const:4:8"]]
- 00b9a610 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b604 ["INT_ADD", "register:40f0:8", ["const:b9b604:8", "const:4:8"]]
+ 00b9b604 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a610 bytes c4040394
+ 00b9b604 bytes bb040394
- 00b9a684 ["INT_ADD", "register:40f0:8", ["const:b9a684:8", "const:4:8"]]
- 00b9a684 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b678 ["INT_ADD", "register:40f0:8", ["const:b9b678:8", "const:4:8"]]
+ 00b9b678 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a684 bytes a7040394
+ 00b9b678 bytes 9e040394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e29fd5fcdf37f98c24fffea7517ca599"></a>

### [`00b9a758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a758.md) → [`00b9b74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b74c.md) _ZNSt6__ndk17__sort4IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEjT0_S9_S9_S9_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1a0.md) · 呼出先 2件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d160.md)
- 新版 呼出元 1件 [`00c5e170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e170.md) · 呼出先 2件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md) [`00c5e130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a758.md#insn-00b9a78c) · [`00b9a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a758.md#insn-00b9a7b0) · [`00b9a804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a758.md#insn-00b9a804)
- 新版 [`00b9b780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b74c.md#insn-00b9b780) · [`00b9b7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b74c.md#insn-00b9b7a4) · [`00b9b7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b74c.md#insn-00b9b7f8)

~~~diff
- 00b9a78c ["INT_ADD", "register:40f0:8", ["const:b9a78c:8", "const:4:8"]]
- 00b9a78c ["CALL", null, ["callee:00c5e130:8"]]
+ 00b9b780 ["INT_ADD", "register:40f0:8", ["const:b9b780:8", "const:4:8"]]
+ 00b9b780 ["CALL", null, ["callee:00c5e130:8"]]
- 00b9a78c bytes 750a0394
+ 00b9b780 bytes 6c0a0394
- 00b9a7b0 ["INT_ADD", "register:40f0:8", ["const:b9a7b0:8", "const:4:8"]]
- 00b9a7b0 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b7a4 ["INT_ADD", "register:40f0:8", ["const:b9b7a4:8", "const:4:8"]]
+ 00b9b7a4 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a7b0 bytes 5c040394
+ 00b9b7a4 bytes 53040394
- 00b9a804 ["INT_ADD", "register:40f0:8", ["const:b9a804:8", "const:4:8"]]
- 00b9a804 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b7f8 ["INT_ADD", "register:40f0:8", ["const:b9b7f8:8", "const:4:8"]]
+ 00b9b7f8 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a804 bytes 47040394
+ 00b9b7f8 bytes 3e040394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2925bf26e85e1e75a4ef4acea47e7e5f"></a>

### [`00b9a8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a8b4.md) → [`00b9b8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b8a8.md) FUN_00b9b8a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b99fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99fc0.md) [`00b9ab94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9ab94.md) · 呼出先 2件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5d1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1a0.md)
- 新版 呼出元 2件 [`00b9afb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9afb4.md) [`00b9bb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9bb88.md) · 呼出先 2件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md) [`00c5e170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a8b4.md#insn-00b9a8f0) · [`00b9a914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a8b4.md#insn-00b9a914) · [`00b9a968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9a8b4.md#insn-00b9a968)
- 新版 [`00b9b8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b8a8.md#insn-00b9b8e4) · [`00b9b908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b8a8.md#insn-00b9b908) · [`00b9b95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9b8a8.md#insn-00b9b95c)

~~~diff
- 00b9a8f0 ["INT_ADD", "register:40f0:8", ["const:b9a8f0:8", "const:4:8"]]
- 00b9a8f0 ["CALL", null, ["callee:00c5e170:8"]]
+ 00b9b8e4 ["INT_ADD", "register:40f0:8", ["const:b9b8e4:8", "const:4:8"]]
+ 00b9b8e4 ["CALL", null, ["callee:00c5e170:8"]]
- 00b9a8f0 bytes 2c0a0394
+ 00b9b8e4 bytes 230a0394
- 00b9a914 ["INT_ADD", "register:40f0:8", ["const:b9a914:8", "const:4:8"]]
- 00b9a914 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b908 ["INT_ADD", "register:40f0:8", ["const:b9b908:8", "const:4:8"]]
+ 00b9b908 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a914 bytes 03040394
+ 00b9b908 bytes fa030394
- 00b9a968 ["INT_ADD", "register:40f0:8", ["const:b9a968:8", "const:4:8"]]
- 00b9a968 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9b95c ["INT_ADD", "register:40f0:8", ["const:b9b95c:8", "const:4:8"]]
+ 00b9b95c ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9a968 bytes ee030394
+ 00b9b95c bytes e5030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-156f442ca7b3d6070158c2f17929fe3a"></a>

### [`00b9aa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md) → [`00b9ba64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9ba64.md) _ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cce0.md) · 呼出先 2件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d160.md)
- 新版 呼出元 1件 [`00c5dcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcb0.md) · 呼出先 2件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md) [`00c5e130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9aaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9aaa8) · [`00b9aaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9aaf8) · [`00b9ab3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9ab3c)
- 新版 [`00b9ba9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9ba64.md#insn-00b9ba9c) · [`00b9baec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9ba64.md#insn-00b9baec) · [`00b9bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9ba64.md#insn-00b9bb30)

~~~diff
- 00b9aaa8 ["INT_ADD", "register:40f0:8", ["const:b9aaa8:8", "const:4:8"]]
- 00b9aaa8 ["CALL", null, ["callee:00c5e130:8"]]
+ 00b9ba9c ["INT_ADD", "register:40f0:8", ["const:b9ba9c:8", "const:4:8"]]
+ 00b9ba9c ["CALL", null, ["callee:00c5e130:8"]]
- 00b9aaa8 bytes ae090394
+ 00b9ba9c bytes a5090394
- 00b9aaf8 ["INT_ADD", "register:40f0:8", ["const:b9aaf8:8", "const:4:8"]]
- 00b9aaf8 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9baec ["INT_ADD", "register:40f0:8", ["const:b9baec:8", "const:4:8"]]
+ 00b9baec ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9aaf8 bytes 8a030394
+ 00b9baec bytes 81030394
- 00b9ab3c ["INT_ADD", "register:40f0:8", ["const:b9ab3c:8", "const:4:8"]]
- 00b9ab3c ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b9bb30 ["INT_ADD", "register:40f0:8", ["const:b9bb30:8", "const:4:8"]]
+ 00b9bb30 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b9ab3c bytes 79030394
+ 00b9bb30 bytes 70030394
~~~


<a id="compare-fe444f84712d231215d79054c062a9fd"></a>

### [`00b9aea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aea8.md) → [`00b9be9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9be9c.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d140.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e110.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9af64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aea8.md#insn-00b9af64) · [`00b9b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aea8.md#insn-00b9b000) · [`00b9b024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aea8.md#insn-00b9b024)
- 新版 [`00b9bf58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9be9c.md#insn-00b9bf58) · [`00b9bff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9be9c.md#insn-00b9bff4) · [`00b9c018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9b/00b9be9c.md#insn-00b9c018)

~~~diff
- 00b9af64 ["INT_ADD", "register:40f0:8", ["const:b9af64:8", "const:4:8"]]
- 00b9af64 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9bf58 ["INT_ADD", "register:40f0:8", ["const:b9bf58:8", "const:4:8"]]
+ 00b9bf58 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9af64 bytes fff30294
+ 00b9bf58 bytes f6f30294
- 00b9b000 ["INT_ADD", "register:40f0:8", ["const:b9b000:8", "const:4:8"]]
- 00b9b000 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9bff4 ["INT_ADD", "register:40f0:8", ["const:b9bff4:8", "const:4:8"]]
+ 00b9bff4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b9b000 bytes 34f40294
+ 00b9bff4 bytes 2bf40294
- 00b9b024 ["INT_ADD", "register:40f0:8", ["const:b9b024:8", "const:4:8"]]
- 00b9b024 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9c018 ["INT_ADD", "register:40f0:8", ["const:b9c018:8", "const:4:8"]]
+ 00b9c018 ["CALL", null, ["callee:00c590a0:8"]]
- 00b9b024 bytes 2bf40294
+ 00b9c018 bytes 22f40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2589ca758773dc7d6d8376aa50c8253"></a>

### [`00b9b214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b214.md) → [`00b9c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c208.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d150.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e120.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b214.md#insn-00b9b2c8) · [`00b9b2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b214.md#insn-00b9b2ec) · [`00b9b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b214.md#insn-00b9b39c)
- 新版 [`00b9c2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c208.md#insn-00b9c2bc) · [`00b9c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c208.md#insn-00b9c2e0) · [`00b9c390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c208.md#insn-00b9c390)

~~~diff
- 00b9b2c8 ["INT_ADD", "register:40f0:8", ["const:b9b2c8:8", "const:4:8"]]
- 00b9b2c8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9c2bc ["INT_ADD", "register:40f0:8", ["const:b9c2bc:8", "const:4:8"]]
+ 00b9c2bc ["CALL", null, ["callee:00c590a0:8"]]
- 00b9b2c8 bytes 82f30294
+ 00b9c2bc bytes 79f30294
- 00b9b2ec ["INT_ADD", "register:40f0:8", ["const:b9b2ec:8", "const:4:8"]]
- 00b9b2ec ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9c2e0 ["INT_ADD", "register:40f0:8", ["const:b9c2e0:8", "const:4:8"]]
+ 00b9c2e0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9b2ec bytes 1df30294
+ 00b9c2e0 bytes 14f30294
- 00b9b39c ["INT_ADD", "register:40f0:8", ["const:b9b39c:8", "const:4:8"]]
- 00b9b39c ["CALL", null, ["callee:00c590a0:8"]]
+ 00b9c390 ["INT_ADD", "register:40f0:8", ["const:b9c390:8", "const:4:8"]]
+ 00b9c390 ["CALL", null, ["callee:00c590a0:8"]]
- 00b9b39c bytes 4df30294
+ 00b9c390 bytes 44f30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a07fb809f83ac26302e67455b5a8b6d"></a>

### [`00b9b4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b4e4.md) → [`00b9c4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c4d8.md) _ZNSt6__ndk16vectorIN11flexbuffers7Builder5ValueENS_9allocatorIS3_EEE8__appendEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0e0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5e0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0b0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b4e4.md#insn-00b9b554) · [`00b9b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b4e4.md#insn-00b9b590) · [`00b9b5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b4e4.md#insn-00b9b5ac)
- 新版 [`00b9c548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c4d8.md#insn-00b9c548) · [`00b9c584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c4d8.md#insn-00b9c584) · [`00b9c5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c4d8.md#insn-00b9c5a0)

~~~diff
- 00b9b554 ["INT_ADD", "register:40f0:8", ["const:b9b554:8", "const:4:8"]]
- 00b9b554 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b9c548 ["INT_ADD", "register:40f0:8", ["const:b9c548:8", "const:4:8"]]
+ 00b9c548 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b9b554 bytes 2fff0294
+ 00b9c548 bytes 26ff0294
- 00b9b590 ["INT_ADD", "register:40f0:8", ["const:b9b590:8", "const:4:8"]]
- 00b9b590 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9c584 ["INT_ADD", "register:40f0:8", ["const:b9c584:8", "const:4:8"]]
+ 00b9c584 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9b590 bytes 74f20294
+ 00b9c584 bytes 6bf20294
- 00b9b5ac ["INT_ADD", "register:40f0:8", ["const:b9b5ac:8", "const:4:8"]]
- 00b9b5ac ["CALL", null, ["callee:00c59130:8"]]
+ 00b9c5a0 ["INT_ADD", "register:40f0:8", ["const:b9c5a0:8", "const:4:8"]]
+ 00b9c5a0 ["CALL", null, ["callee:00c59130:8"]]
- 00b9b5ac bytes edf20294
+ 00b9c5a0 bytes e4f20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef43c968a48ef9cfa30118061fd0fbc"></a>

### [`00b9b610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b610.md) → [`00b9c604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c604.md) _ZN11flexbuffers7Builder6StringEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9c0.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b730.md) [`00c5c970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c970.md) [`00c5d090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d090.md)
- 新版 呼出元 1件 [`00c5d990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c700.md) [`00c5d940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d940.md) [`00c5e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b610.md#insn-00b9b650) · [`00b9b6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b610.md#insn-00b9b6b8) · [`00b9b6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b610.md#insn-00b9b6f8)
- 新版 [`00b9c644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c604.md#insn-00b9c644) · [`00b9c6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c604.md#insn-00b9c6ac) · [`00b9c6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c604.md#insn-00b9c6ec)

~~~diff
- 00b9b650 ["INT_ADD", "register:40f0:8", ["const:b9b650:8", "const:4:8"]]
- 00b9b650 ["CALL", null, ["callee:00c5d940:8"]]
+ 00b9c644 ["INT_ADD", "register:40f0:8", ["const:b9c644:8", "const:4:8"]]
+ 00b9c644 ["CALL", null, ["callee:00c5d940:8"]]
- 00b9b650 bytes c8040394
+ 00b9c644 bytes bf040394
- 00b9b6b8 ["INT_ADD", "register:40f0:8", ["const:b9b6b8:8", "const:4:8"]]
- 00b9b6b8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9c6ac ["INT_ADD", "register:40f0:8", ["const:b9c6ac:8", "const:4:8"]]
+ 00b9c6ac ["CALL", null, ["callee:00c590f0:8"]]
- 00b9b6b8 bytes 9af20294
+ 00b9c6ac bytes 91f20294
- 00b9b6f8 ["INT_ADD", "register:40f0:8", ["const:b9b6f8:8", "const:4:8"]]
- 00b9b6f8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9c6ec ["INT_ADD", "register:40f0:8", ["const:b9c6ec:8", "const:4:8"]]
+ 00b9c6ec ["CALL", null, ["callee:00c590f0:8"]]
- 00b9b6f8 bytes 8af20294
+ 00b9c6ec bytes 81f20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd22085dd7488f45dbd5157edcc1a5eb"></a>

### [`00b9b798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b798.md) → [`00b9c78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c78c.md) _ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c970.md) · 呼出先 4件 [`00b99988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d140.md) [`00c5d150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d150.md)
- 新版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d940.md) · 呼出先 4件 [`00b9a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5e110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b798.md#insn-00b9b830) · [`00b9b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b798.md#insn-00b9b848) · [`00b9b864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b798.md#insn-00b9b864)
- 新版 [`00b9c824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c78c.md#insn-00b9c824) · [`00b9c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c78c.md#insn-00b9c83c) · [`00b9c858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c78c.md#insn-00b9c858)

~~~diff
- 00b9b830 ["INT_ADD", "register:40f0:8", ["const:b9b830:8", "const:4:8"]]
- 00b9b830 ["CALL", null, ["callee:00c5e110:8"]]
+ 00b9c824 ["INT_ADD", "register:40f0:8", ["const:b9c824:8", "const:4:8"]]
+ 00b9c824 ["CALL", null, ["callee:00c5e110:8"]]
- 00b9b830 bytes 44060394
+ 00b9c824 bytes 3b060394
- 00b9b848 ["INT_ADD", "register:40f0:8", ["const:b9b848:8", "const:4:8"]]
- 00b9b848 ["CALL", null, ["callee:00c5e120:8"]]
+ 00b9c83c ["INT_ADD", "register:40f0:8", ["const:b9c83c:8", "const:4:8"]]
+ 00b9c83c ["CALL", null, ["callee:00c5e120:8"]]
- 00b9b848 bytes 42060394
+ 00b9c83c bytes 39060394
- 00b9b864 ["INT_ADD", "register:40f0:8", ["const:b9b864:8", "const:4:8"]]
- 00b9b864 ["CALL", null, ["callee:00c5e120:8"]]
+ 00b9c858 ["INT_ADD", "register:40f0:8", ["const:b9c858:8", "const:4:8"]]
+ 00b9c858 ["CALL", null, ["callee:00c5e120:8"]]
- 00b9b864 bytes 3b060394
+ 00b9c858 bytes 32060394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b73b8cc51f3a368e74840d8ade71dd71"></a>

### [`00b9b8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md) → [`00b9c8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c8a8.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS1

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d090.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e060.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b918) · [`00b9b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b954) · [`00b9b9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b9a4)
- 新版 [`00b9c90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c8a8.md#insn-00b9c90c) · [`00b9c948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c8a8.md#insn-00b9c948) · [`00b9c998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9c8a8.md#insn-00b9c998)

~~~diff
- 00b9b918 ["INT_ADD", "register:40f0:8", ["const:b9b918:8", "const:4:8"]]
- 00b9b918 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9c90c ["INT_ADD", "register:40f0:8", ["const:b9c90c:8", "const:4:8"]]
+ 00b9c90c ["CALL", null, ["callee:00c590f0:8"]]
- 00b9b918 bytes 02f20294
+ 00b9c90c bytes f9f10294
- 00b9b954 ["INT_ADD", "register:40f0:8", ["const:b9b954:8", "const:4:8"]]
- 00b9b954 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9c948 ["INT_ADD", "register:40f0:8", ["const:b9c948:8", "const:4:8"]]
+ 00b9c948 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9b954 bytes f3f10294
+ 00b9c948 bytes eaf10294
- 00b9b9a4 ["INT_ADD", "register:40f0:8", ["const:b9b9a4:8", "const:4:8"]]
- 00b9b9a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b9c998 ["INT_ADD", "register:40f0:8", ["const:b9c998:8", "const:4:8"]]
+ 00b9c998 ["CALL", null, ["callee:00c58f30:8"]]
- 00b9b9a4 bytes 6ff10294
+ 00b9c998 bytes 66f10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80080d421594e62061b5186e4df28dc"></a>

### [`00b9ba14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9ba14.md) → [`00b9ca08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9ca08.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetINS_6StringEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4d0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d4a0.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9ba74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9ba14.md#insn-00b9ba74) · [`00b9bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9ba14.md#insn-00b9bad0) · [`00b9baf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9ba14.md#insn-00b9baf4)
- 新版 [`00b9ca68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9ca08.md#insn-00b9ca68) · [`00b9cac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9ca08.md#insn-00b9cac4) · [`00b9cae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9ca08.md#insn-00b9cae8)

~~~diff
- 00b9ba74 ["INT_ADD", "register:40f0:8", ["const:b9ba74:8", "const:4:8"]]
- 00b9ba74 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9ca68 ["INT_ADD", "register:40f0:8", ["const:b9ca68:8", "const:4:8"]]
+ 00b9ca68 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9ba74 bytes ff010394
+ 00b9ca68 bytes f6010394
- 00b9bad0 ["INT_ADD", "register:40f0:8", ["const:b9bad0:8", "const:4:8"]]
- 00b9bad0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9cac4 ["INT_ADD", "register:40f0:8", ["const:b9cac4:8", "const:4:8"]]
+ 00b9cac4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9bad0 bytes 14020394
+ 00b9cac4 bytes 0b020394
- 00b9baf4 ["INT_ADD", "register:40f0:8", ["const:b9baf4:8", "const:4:8"]]
- 00b9baf4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cae8 ["INT_ADD", "register:40f0:8", ["const:b9cae8:8", "const:4:8"]]
+ 00b9cae8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9baf4 bytes df010394
+ 00b9cae8 bytes d6010394
~~~


<a id="compare-04e41f10259986d1ea8d3ed97dc4cf07"></a>

### [`00b9bb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bb44.md) → [`00b9cb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cb38.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6StringEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c440.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d410.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9bba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bb44.md#insn-00b9bba4) · [`00b9bc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bb44.md#insn-00b9bc00) · [`00b9bc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bb44.md#insn-00b9bc24)
- 新版 [`00b9cb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cb38.md#insn-00b9cb98) · [`00b9cbf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cb38.md#insn-00b9cbf4) · [`00b9cc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cb38.md#insn-00b9cc18)

~~~diff
- 00b9bba4 ["INT_ADD", "register:40f0:8", ["const:b9bba4:8", "const:4:8"]]
- 00b9bba4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cb98 ["INT_ADD", "register:40f0:8", ["const:b9cb98:8", "const:4:8"]]
+ 00b9cb98 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bba4 bytes b3010394
+ 00b9cb98 bytes aa010394
- 00b9bc00 ["INT_ADD", "register:40f0:8", ["const:b9bc00:8", "const:4:8"]]
- 00b9bc00 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9cbf4 ["INT_ADD", "register:40f0:8", ["const:b9cbf4:8", "const:4:8"]]
+ 00b9cbf4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9bc00 bytes c8010394
+ 00b9cbf4 bytes bf010394
- 00b9bc24 ["INT_ADD", "register:40f0:8", ["const:b9bc24:8", "const:4:8"]]
- 00b9bc24 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cc18 ["INT_ADD", "register:40f0:8", ["const:b9cc18:8", "const:4:8"]]
+ 00b9cc18 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bc24 bytes 93010394
+ 00b9cc18 bytes 8a010394
~~~


<a id="compare-a02d232d1182530e1f026942abeef6d7"></a>

### [`00b9bc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bc74.md) → [`00b9cc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cc68.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection10SchemaFileEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c450.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d420.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9bcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bc74.md#insn-00b9bcd4) · [`00b9bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bc74.md#insn-00b9bd30) · [`00b9bd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bc74.md#insn-00b9bd54)
- 新版 [`00b9ccc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cc68.md#insn-00b9ccc8) · [`00b9cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cc68.md#insn-00b9cd24) · [`00b9cd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cc68.md#insn-00b9cd48)

~~~diff
- 00b9bcd4 ["INT_ADD", "register:40f0:8", ["const:b9bcd4:8", "const:4:8"]]
- 00b9bcd4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9ccc8 ["INT_ADD", "register:40f0:8", ["const:b9ccc8:8", "const:4:8"]]
+ 00b9ccc8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bcd4 bytes 67010394
+ 00b9ccc8 bytes 5e010394
- 00b9bd30 ["INT_ADD", "register:40f0:8", ["const:b9bd30:8", "const:4:8"]]
- 00b9bd30 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9cd24 ["INT_ADD", "register:40f0:8", ["const:b9cd24:8", "const:4:8"]]
+ 00b9cd24 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9bd30 bytes 7c010394
+ 00b9cd24 bytes 73010394
- 00b9bd54 ["INT_ADD", "register:40f0:8", ["const:b9bd54:8", "const:4:8"]]
- 00b9bd54 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cd48 ["INT_ADD", "register:40f0:8", ["const:b9cd48:8", "const:4:8"]]
+ 00b9cd48 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bd54 bytes 47010394
+ 00b9cd48 bytes 3e010394
~~~


<a id="compare-b740fae5aa8e62259286363f0fb0603b"></a>

### [`00b9bda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bda4.md) → [`00b9cd98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cd98.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection7ServiceEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4b0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d480.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9be04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bda4.md#insn-00b9be04) · [`00b9be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bda4.md#insn-00b9be60) · [`00b9be84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bda4.md#insn-00b9be84)
- 新版 [`00b9cdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cd98.md#insn-00b9cdf8) · [`00b9ce54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cd98.md#insn-00b9ce54) · [`00b9ce78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cd98.md#insn-00b9ce78)

~~~diff
- 00b9be04 ["INT_ADD", "register:40f0:8", ["const:b9be04:8", "const:4:8"]]
- 00b9be04 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cdf8 ["INT_ADD", "register:40f0:8", ["const:b9cdf8:8", "const:4:8"]]
+ 00b9cdf8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9be04 bytes 1b010394
+ 00b9cdf8 bytes 12010394
- 00b9be60 ["INT_ADD", "register:40f0:8", ["const:b9be60:8", "const:4:8"]]
- 00b9be60 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9ce54 ["INT_ADD", "register:40f0:8", ["const:b9ce54:8", "const:4:8"]]
+ 00b9ce54 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9be60 bytes 30010394
+ 00b9ce54 bytes 27010394
- 00b9be84 ["INT_ADD", "register:40f0:8", ["const:b9be84:8", "const:4:8"]]
- 00b9be84 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9ce78 ["INT_ADD", "register:40f0:8", ["const:b9ce78:8", "const:4:8"]]
+ 00b9ce78 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9be84 bytes fb000394
+ 00b9ce78 bytes f2000394
~~~


<a id="compare-18a75918fe5a554e04ea18a0586c43cf"></a>

### [`00b9bed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bed4.md) → [`00b9cec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cec8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIN10reflection6ObjectEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c430.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d400.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9bf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bed4.md#insn-00b9bf34) · [`00b9bf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bed4.md#insn-00b9bf90) · [`00b9bfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9bed4.md#insn-00b9bfb4)
- 新版 [`00b9cf28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cec8.md#insn-00b9cf28) · [`00b9cf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cec8.md#insn-00b9cf84) · [`00b9cfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cec8.md#insn-00b9cfa8)

~~~diff
- 00b9bf34 ["INT_ADD", "register:40f0:8", ["const:b9bf34:8", "const:4:8"]]
- 00b9bf34 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cf28 ["INT_ADD", "register:40f0:8", ["const:b9cf28:8", "const:4:8"]]
+ 00b9cf28 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bf34 bytes cf000394
+ 00b9cf28 bytes c6000394
- 00b9bf90 ["INT_ADD", "register:40f0:8", ["const:b9bf90:8", "const:4:8"]]
- 00b9bf90 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9cf84 ["INT_ADD", "register:40f0:8", ["const:b9cf84:8", "const:4:8"]]
+ 00b9cf84 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9bf90 bytes e4000394
+ 00b9cf84 bytes db000394
- 00b9bfb4 ["INT_ADD", "register:40f0:8", ["const:b9bfb4:8", "const:4:8"]]
- 00b9bfb4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9cfa8 ["INT_ADD", "register:40f0:8", ["const:b9cfa8:8", "const:4:8"]]
+ 00b9cfa8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9bfb4 bytes af000394
+ 00b9cfa8 bytes a6000394
~~~


<a id="compare-9fcd705fad2955a7974e0da5b02999d3"></a>

### [`00b9c004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c004.md) → [`00b9cff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cff8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection4EnumEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c460.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d430.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c004.md#insn-00b9c064) · [`00b9c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c004.md#insn-00b9c0c0) · [`00b9c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c004.md#insn-00b9c0e4)
- 新版 [`00b9d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cff8.md#insn-00b9d058) · [`00b9d0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cff8.md#insn-00b9d0b4) · [`00b9d0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9c/00b9cff8.md#insn-00b9d0d8)

~~~diff
- 00b9c064 ["INT_ADD", "register:40f0:8", ["const:b9c064:8", "const:4:8"]]
- 00b9c064 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d058 ["INT_ADD", "register:40f0:8", ["const:b9d058:8", "const:4:8"]]
+ 00b9d058 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c064 bytes 83000394
+ 00b9d058 bytes 7a000394
- 00b9c0c0 ["INT_ADD", "register:40f0:8", ["const:b9c0c0:8", "const:4:8"]]
- 00b9c0c0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d0b4 ["INT_ADD", "register:40f0:8", ["const:b9d0b4:8", "const:4:8"]]
+ 00b9d0b4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c0c0 bytes 98000394
+ 00b9d0b4 bytes 8f000394
- 00b9c0e4 ["INT_ADD", "register:40f0:8", ["const:b9c0e4:8", "const:4:8"]]
- 00b9c0e4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d0d8 ["INT_ADD", "register:40f0:8", ["const:b9d0d8:8", "const:4:8"]]
+ 00b9d0d8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c0e4 bytes 63000394
+ 00b9d0d8 bytes 5a000394
~~~


<a id="compare-e6c12af62c9d8d8bd20958bbbac5f40a"></a>

### [`00b9c134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c134.md) → [`00b9d128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d128.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection6ObjectEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c480.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d450.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c134.md#insn-00b9c194) · [`00b9c1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c134.md#insn-00b9c1f0) · [`00b9c214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c134.md#insn-00b9c214)
- 新版 [`00b9d188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d128.md#insn-00b9d188) · [`00b9d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d128.md#insn-00b9d1e4) · [`00b9d208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d128.md#insn-00b9d208)

~~~diff
- 00b9c194 ["INT_ADD", "register:40f0:8", ["const:b9c194:8", "const:4:8"]]
- 00b9c194 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d188 ["INT_ADD", "register:40f0:8", ["const:b9d188:8", "const:4:8"]]
+ 00b9d188 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c194 bytes 37000394
+ 00b9d188 bytes 2e000394
- 00b9c1f0 ["INT_ADD", "register:40f0:8", ["const:b9c1f0:8", "const:4:8"]]
- 00b9c1f0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d1e4 ["INT_ADD", "register:40f0:8", ["const:b9d1e4:8", "const:4:8"]]
+ 00b9d1e4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c1f0 bytes 4c000394
+ 00b9d1e4 bytes 43000394
- 00b9c214 ["INT_ADD", "register:40f0:8", ["const:b9c214:8", "const:4:8"]]
- 00b9c214 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d208 ["INT_ADD", "register:40f0:8", ["const:b9d208:8", "const:4:8"]]
+ 00b9d208 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c214 bytes 17000394
+ 00b9d208 bytes 0e000394
~~~


<a id="compare-f53cdb360048a2ae321bf8000fb33ee9"></a>

### [`00b9c264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c264.md) → [`00b9d258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d258.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection8KeyValueEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4c0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d490.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c264.md#insn-00b9c2c4) · [`00b9c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c264.md#insn-00b9c320) · [`00b9c344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c264.md#insn-00b9c344)
- 新版 [`00b9d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d258.md#insn-00b9d2b8) · [`00b9d314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d258.md#insn-00b9d314) · [`00b9d338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d258.md#insn-00b9d338)

~~~diff
- 00b9c2c4 ["INT_ADD", "register:40f0:8", ["const:b9c2c4:8", "const:4:8"]]
- 00b9c2c4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d2b8 ["INT_ADD", "register:40f0:8", ["const:b9d2b8:8", "const:4:8"]]
+ 00b9d2b8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c2c4 bytes ebff0294
+ 00b9d2b8 bytes e2ff0294
- 00b9c320 ["INT_ADD", "register:40f0:8", ["const:b9c320:8", "const:4:8"]]
- 00b9c320 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d314 ["INT_ADD", "register:40f0:8", ["const:b9d314:8", "const:4:8"]]
+ 00b9d314 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c320 bytes 00000394
+ 00b9d314 bytes f7ff0294
- 00b9c344 ["INT_ADD", "register:40f0:8", ["const:b9c344:8", "const:4:8"]]
- 00b9c344 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d338 ["INT_ADD", "register:40f0:8", ["const:b9d338:8", "const:4:8"]]
+ 00b9d338 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c344 bytes cbff0294
+ 00b9d338 bytes c2ff0294
~~~


<a id="compare-f5b3c520f051deef4e437b254c7da378"></a>

### [`00b9c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c394.md) → [`00b9d388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d388.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection5FieldEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c470.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d440.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c394.md#insn-00b9c3f4) · [`00b9c450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c394.md#insn-00b9c450) · [`00b9c474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c394.md#insn-00b9c474)
- 新版 [`00b9d3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d388.md#insn-00b9d3e8) · [`00b9d444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d388.md#insn-00b9d444) · [`00b9d468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d388.md#insn-00b9d468)

~~~diff
- 00b9c3f4 ["INT_ADD", "register:40f0:8", ["const:b9c3f4:8", "const:4:8"]]
- 00b9c3f4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d3e8 ["INT_ADD", "register:40f0:8", ["const:b9d3e8:8", "const:4:8"]]
+ 00b9d3e8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c3f4 bytes 9fff0294
+ 00b9d3e8 bytes 96ff0294
- 00b9c450 ["INT_ADD", "register:40f0:8", ["const:b9c450:8", "const:4:8"]]
- 00b9c450 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d444 ["INT_ADD", "register:40f0:8", ["const:b9d444:8", "const:4:8"]]
+ 00b9d444 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c450 bytes b4ff0294
+ 00b9d444 bytes abff0294
- 00b9c474 ["INT_ADD", "register:40f0:8", ["const:b9c474:8", "const:4:8"]]
- 00b9c474 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d468 ["INT_ADD", "register:40f0:8", ["const:b9d468:8", "const:4:8"]]
+ 00b9d468 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c474 bytes 7fff0294
+ 00b9d468 bytes 76ff0294
~~~


<a id="compare-ef0d3dc0e8ff04e41129f5bda4260254"></a>

### [`00b9c4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c4c4.md) → [`00b9d4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d4b8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIN10reflection4TypeEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c420.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3f0.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c4c4.md#insn-00b9c524) · [`00b9c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c4c4.md#insn-00b9c580) · [`00b9c5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c4c4.md#insn-00b9c5a4)
- 新版 [`00b9d518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d4b8.md#insn-00b9d518) · [`00b9d574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d4b8.md#insn-00b9d574) · [`00b9d598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d4b8.md#insn-00b9d598)

~~~diff
- 00b9c524 ["INT_ADD", "register:40f0:8", ["const:b9c524:8", "const:4:8"]]
- 00b9c524 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d518 ["INT_ADD", "register:40f0:8", ["const:b9d518:8", "const:4:8"]]
+ 00b9d518 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c524 bytes 53ff0294
+ 00b9d518 bytes 4aff0294
- 00b9c580 ["INT_ADD", "register:40f0:8", ["const:b9c580:8", "const:4:8"]]
- 00b9c580 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d574 ["INT_ADD", "register:40f0:8", ["const:b9d574:8", "const:4:8"]]
+ 00b9d574 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c580 bytes 68ff0294
+ 00b9d574 bytes 5fff0294
- 00b9c5a4 ["INT_ADD", "register:40f0:8", ["const:b9c5a4:8", "const:4:8"]]
- 00b9c5a4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d598 ["INT_ADD", "register:40f0:8", ["const:b9d598:8", "const:4:8"]]
+ 00b9d598 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c5a4 bytes 33ff0294
+ 00b9d598 bytes 2aff0294
~~~


<a id="compare-cdb6069047e753a96fc4ab3bedba2e75"></a>

### [`00b9c5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c5f4.md) → [`00b9d5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d5e8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection7RPCCallEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4a0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d470.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c5f4.md#insn-00b9c654) · [`00b9c6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c5f4.md#insn-00b9c6b0) · [`00b9c6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c5f4.md#insn-00b9c6d4)
- 新版 [`00b9d648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d5e8.md#insn-00b9d648) · [`00b9d6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d5e8.md#insn-00b9d6a4) · [`00b9d6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d5e8.md#insn-00b9d6c8)

~~~diff
- 00b9c654 ["INT_ADD", "register:40f0:8", ["const:b9c654:8", "const:4:8"]]
- 00b9c654 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d648 ["INT_ADD", "register:40f0:8", ["const:b9d648:8", "const:4:8"]]
+ 00b9d648 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c654 bytes 07ff0294
+ 00b9d648 bytes fefe0294
- 00b9c6b0 ["INT_ADD", "register:40f0:8", ["const:b9c6b0:8", "const:4:8"]]
- 00b9c6b0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d6a4 ["INT_ADD", "register:40f0:8", ["const:b9d6a4:8", "const:4:8"]]
+ 00b9d6a4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c6b0 bytes 1cff0294
+ 00b9d6a4 bytes 13ff0294
- 00b9c6d4 ["INT_ADD", "register:40f0:8", ["const:b9c6d4:8", "const:4:8"]]
- 00b9c6d4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d6c8 ["INT_ADD", "register:40f0:8", ["const:b9d6c8:8", "const:4:8"]]
+ 00b9d6c8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c6d4 bytes e7fe0294
+ 00b9d6c8 bytes defe0294
~~~


<a id="compare-de4f1e3a191b56502c30e35385f3a546"></a>

### [`00b9c724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c724.md) → [`00b9d718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d718.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection7EnumValEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c490.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d460.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c724.md#insn-00b9c784) · [`00b9c7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c724.md#insn-00b9c7e0) · [`00b9c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9c724.md#insn-00b9c804)
- 新版 [`00b9d778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d718.md#insn-00b9d778) · [`00b9d7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d718.md#insn-00b9d7d4) · [`00b9d7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9d718.md#insn-00b9d7f8)

~~~diff
- 00b9c784 ["INT_ADD", "register:40f0:8", ["const:b9c784:8", "const:4:8"]]
- 00b9c784 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d778 ["INT_ADD", "register:40f0:8", ["const:b9d778:8", "const:4:8"]]
+ 00b9d778 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c784 bytes bbfe0294
+ 00b9d778 bytes b2fe0294
- 00b9c7e0 ["INT_ADD", "register:40f0:8", ["const:b9c7e0:8", "const:4:8"]]
- 00b9c7e0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00b9d7d4 ["INT_ADD", "register:40f0:8", ["const:b9d7d4:8", "const:4:8"]]
+ 00b9d7d4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00b9c7e0 bytes d0fe0294
+ 00b9d7d4 bytes c7fe0294
- 00b9c804 ["INT_ADD", "register:40f0:8", ["const:b9c804:8", "const:4:8"]]
- 00b9c804 ["CALL", null, ["callee:00c5d240:8"]]
+ 00b9d7f8 ["INT_ADD", "register:40f0:8", ["const:b9d7f8:8", "const:4:8"]]
+ 00b9d7f8 ["CALL", null, ["callee:00c5d240:8"]]
- 00b9c804 bytes 9bfe0294
+ 00b9d7f8 bytes 92fe0294
~~~


<a id="compare-d0857eb1b3f8e298fb3004ed02427ea6"></a>

### [`00b9ca2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9ca2c.md) → [`00b9da20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9da20.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb90.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db60.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9ca2c.md#insn-00b9cac4) · [`00b9cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9ca2c.md#insn-00b9cb0c)
- 新版 [`00b9dab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9da20.md#insn-00b9dab8) · [`00b9db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9da20.md#insn-00b9db00)

~~~diff
- 00b9cac4 ["INT_ADD", "register:40f0:8", ["const:b9cac4:8", "const:4:8"]]
- 00b9cac4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9dab8 ["INT_ADD", "register:40f0:8", ["const:b9dab8:8", "const:4:8"]]
+ 00b9dab8 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9cac4 bytes 97ed0294
+ 00b9dab8 bytes 8eed0294
- 00b9cb0c ["INT_ADD", "register:40f0:8", ["const:b9cb0c:8", "const:4:8"]]
- 00b9cb0c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9db00 ["INT_ADD", "register:40f0:8", ["const:b9db00:8", "const:4:8"]]
+ 00b9db00 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9cb0c bytes 85ed0294
+ 00b9db00 bytes 7ced0294
~~~


<a id="compare-f5b423a2c9ff6a2088a4b103319ed411"></a>

### [`00b9cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md) → [`00b9db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9db34.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_EEEEvT

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc10.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc10.md) [`00c5cca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cca0.md) [`00c5cd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd40.md)
- 新版 呼出元 1件 [`00c5dbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbe0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbe0.md) [`00c5dc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc70.md) [`00c5dd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9cbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9cbdc) · [`00b9ccc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9ccc8) · [`00b9cd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9cd30)
- 新版 [`00b9dbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9db34.md#insn-00b9dbd0) · [`00b9dcbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9db34.md#insn-00b9dcbc) · [`00b9dd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9d/00b9db34.md#insn-00b9dd24)

~~~diff
- 00b9cbdc ["INT_ADD", "register:40f0:8", ["const:b9cbdc:8", "const:4:8"]]
- 00b9cbdc ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9dbd0 ["INT_ADD", "register:40f0:8", ["const:b9dbd0:8", "const:4:8"]]
+ 00b9dbd0 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9cbdc bytes 51ed0294
+ 00b9dbd0 bytes 48ed0294
- 00b9ccc8 ["INT_ADD", "register:40f0:8", ["const:b9ccc8:8", "const:4:8"]]
- 00b9ccc8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9dcbc ["INT_ADD", "register:40f0:8", ["const:b9dcbc:8", "const:4:8"]]
+ 00b9dcbc ["CALL", null, ["callee:00c590f0:8"]]
- 00b9ccc8 bytes 16ed0294
+ 00b9dcbc bytes 0ded0294
- 00b9cd30 ["INT_ADD", "register:40f0:8", ["const:b9cd30:8", "const:4:8"]]
- 00b9cd30 ["CALL", null, ["callee:00c5dbe0:8"]]
+ 00b9dd24 ["INT_ADD", "register:40f0:8", ["const:b9dd24:8", "const:4:8"]]
+ 00b9dd24 ["CALL", null, ["callee:00c5dbe0:8"]]
- 00b9cd30 bytes b8ff0294
+ 00b9dd24 bytes afff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb2706dfc8b116c831229636165ed87"></a>

### [`00b9d00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d00c.md) → [`00b9e000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e000.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd40.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc10.md) [`00c5ce00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce00.md)
- 新版 呼出元 1件 [`00c5dd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd10.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbe0.md) [`00c5ddd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9d0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d00c.md#insn-00b9d0c0) · [`00b9d174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d00c.md#insn-00b9d174) · [`00b9d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d00c.md#insn-00b9d190)
- 新版 [`00b9e0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e000.md#insn-00b9e0b4) · [`00b9e168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e000.md#insn-00b9e168) · [`00b9e184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e000.md#insn-00b9e184)

~~~diff
- 00b9d0c0 ["INT_ADD", "register:40f0:8", ["const:b9d0c0:8", "const:4:8"]]
- 00b9d0c0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e0b4 ["INT_ADD", "register:40f0:8", ["const:b9e0b4:8", "const:4:8"]]
+ 00b9e0b4 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d0c0 bytes 18ec0294
+ 00b9e0b4 bytes 0fec0294
- 00b9d174 ["INT_ADD", "register:40f0:8", ["const:b9d174:8", "const:4:8"]]
- 00b9d174 ["CALL", null, ["callee:00c5dbe0:8"]]
+ 00b9e168 ["INT_ADD", "register:40f0:8", ["const:b9e168:8", "const:4:8"]]
+ 00b9e168 ["CALL", null, ["callee:00c5dbe0:8"]]
- 00b9d174 bytes a7fe0294
+ 00b9e168 bytes 9efe0294
- 00b9d190 ["INT_ADD", "register:40f0:8", ["const:b9d190:8", "const:4:8"]]
- 00b9d190 ["CALL", null, ["callee:00c5dbe0:8"]]
+ 00b9e184 ["INT_ADD", "register:40f0:8", ["const:b9e184:8", "const:4:8"]]
+ 00b9e184 ["CALL", null, ["callee:00c5dbe0:8"]]
- 00b9d190 bytes a0fe0294
+ 00b9e184 bytes 97fe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b127fc8dc28b30aeea7d381206b646ec"></a>

### [`00b9d3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md) → [`00b9e3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e3ac.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cca0.md) · 呼出先 4件 [`00b9ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cca0.md) [`00c5ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce60.md)
- 新版 呼出元 1件 [`00c5dc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc70.md) · 呼出先 4件 [`00b9eda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9eda0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc70.md) [`00c5de30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9d484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md#insn-00b9d484) · [`00b9d55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md#insn-00b9d55c) · [`00b9d648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md#insn-00b9d648)
- 新版 [`00b9e478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e3ac.md#insn-00b9e478) · [`00b9e550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e3ac.md#insn-00b9e550) · [`00b9e63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e3ac.md#insn-00b9e63c)

~~~diff
- 00b9d484 ["INT_ADD", "register:40f0:8", ["const:b9d484:8", "const:4:8"]]
- 00b9d484 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e478 ["INT_ADD", "register:40f0:8", ["const:b9e478:8", "const:4:8"]]
+ 00b9e478 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d484 bytes 27eb0294
+ 00b9e478 bytes 1eeb0294
- 00b9d55c ["INT_ADD", "register:40f0:8", ["const:b9d55c:8", "const:4:8"]]
- 00b9d55c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e550 ["INT_ADD", "register:40f0:8", ["const:b9e550:8", "const:4:8"]]
+ 00b9e550 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d55c bytes f1ea0294
+ 00b9e550 bytes e8ea0294
- 00b9d648 ["INT_ADD", "register:40f0:8", ["const:b9d648:8", "const:4:8"]]
- 00b9d648 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e63c ["INT_ADD", "register:40f0:8", ["const:b9e63c:8", "const:4:8"]]
+ 00b9e63c ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d648 bytes b6ea0294
+ 00b9e63c bytes adea0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb6e7281a3b263daab62b7c3994634ad"></a>

### [`00b9d7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d7e0.md) → [`00b9e7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e7d4.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce00.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ddd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddd0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d7e0.md#insn-00b9d890) · [`00b9d918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d7e0.md#insn-00b9d918)
- 新版 [`00b9e884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e7d4.md#insn-00b9e884) · [`00b9e90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e7d4.md#insn-00b9e90c)

~~~diff
- 00b9d890 ["INT_ADD", "register:40f0:8", ["const:b9d890:8", "const:4:8"]]
- 00b9d890 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e884 ["INT_ADD", "register:40f0:8", ["const:b9e884:8", "const:4:8"]]
+ 00b9e884 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d890 bytes 24ea0294
+ 00b9e884 bytes 1bea0294
- 00b9d918 ["INT_ADD", "register:40f0:8", ["const:b9d918:8", "const:4:8"]]
- 00b9d918 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9e90c ["INT_ADD", "register:40f0:8", ["const:b9e90c:8", "const:4:8"]]
+ 00b9e90c ["CALL", null, ["callee:00c590f0:8"]]
- 00b9d918 bytes 02ea0294
+ 00b9e90c bytes f9e90294
~~~


<a id="compare-cfe17f369b8d08eceddee7edb04948c0"></a>

### [`00b9d998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d998.md) → [`00b9e98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e98c.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6Offse

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce60.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cda0.md)
- 新版 呼出元 1件 [`00c5de30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de30.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9db24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d998.md#insn-00b9db24) · [`00b9dc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d998.md#insn-00b9dc14) · [`00b9dc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d998.md#insn-00b9dc70)
- 新版 [`00b9eb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e98c.md#insn-00b9eb18) · [`00b9ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e98c.md#insn-00b9ec08) · [`00b9ec64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e98c.md#insn-00b9ec64)

~~~diff
- 00b9db24 ["INT_ADD", "register:40f0:8", ["const:b9db24:8", "const:4:8"]]
- 00b9db24 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9eb18 ["INT_ADD", "register:40f0:8", ["const:b9eb18:8", "const:4:8"]]
+ 00b9eb18 ["CALL", null, ["callee:00c590f0:8"]]
- 00b9db24 bytes 7fe90294
+ 00b9eb18 bytes 76e90294
- 00b9dc14 ["INT_ADD", "register:40f0:8", ["const:b9dc14:8", "const:4:8"]]
- 00b9dc14 ["CALL", null, ["callee:00c5dd70:8"]]
+ 00b9ec08 ["INT_ADD", "register:40f0:8", ["const:b9ec08:8", "const:4:8"]]
+ 00b9ec08 ["CALL", null, ["callee:00c5dd70:8"]]
- 00b9dc14 bytes 63fc0294
+ 00b9ec08 bytes 5afc0294
- 00b9dc70 ["INT_ADD", "register:40f0:8", ["const:b9dc70:8", "const:4:8"]]
- 00b9dc70 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b9ec64 ["INT_ADD", "register:40f0:8", ["const:b9ec64:8", "const:4:8"]]
+ 00b9ec64 ["CALL", null, ["callee:00c58f80:8"]]
- 00b9dc70 bytes d0e80294
+ 00b9ec64 bytes c7e80294
~~~


<a id="compare-996405fb3e9117131c704161d0289fc4"></a>

### [`00b9dc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9dc74.md) → [`00b9ec68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ec68.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cda0.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd70.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9dd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9dc74.md#insn-00b9dd38)
- 新版 [`00b9ed2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ec68.md#insn-00b9ed2c)

~~~diff
- 00b9dd38 ["INT_ADD", "register:40f0:8", ["const:b9dd38:8", "const:4:8"]]
- 00b9dd38 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b9ed2c ["INT_ADD", "register:40f0:8", ["const:b9ed2c:8", "const:4:8"]]
+ 00b9ed2c ["CALL", null, ["callee:00c590f0:8"]]
- 00b9dd38 bytes fae80294
+ 00b9ed2c bytes f1e80294
~~~


<a id="compare-944aa2e8d34f43895111ad8e83b479bc"></a>

### [`00b9ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md) → [`00b9eda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9eda0.md) FUN_00b9eda0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9d3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00b9e3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9e3ac.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9de6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md#insn-00b9de6c) · [`00b9de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md#insn-00b9de98)
- 新版 [`00b9ee60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9eda0.md#insn-00b9ee60) · [`00b9ee8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9eda0.md#insn-00b9ee8c)

~~~diff
- 00b9de6c ["INT_ADD", "register:40f0:8", ["const:b9de6c:8", "const:4:8"]]
- 00b9de6c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b9ee60 ["INT_ADD", "register:40f0:8", ["const:b9ee60:8", "const:4:8"]]
+ 00b9ee60 ["CALL", null, ["callee:00c58fe0:8"]]
- 00b9de6c bytes 69e80294
+ 00b9ee60 bytes 60e80294
- 00b9de98 ["INT_ADD", "register:40f0:8", ["const:b9de98:8", "const:4:8"]]
- 00b9de98 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b9ee8c ["INT_ADD", "register:40f0:8", ["const:b9ee8c:8", "const:4:8"]]
+ 00b9ee8c ["CALL", null, ["callee:00c58fe0:8"]]
- 00b9de98 bytes 5ee80294
+ 00b9ee8c bytes 55e80294
~~~


<a id="compare-f6eb52ccd304d76f5d75719c3562ab2a"></a>

### [`00b9df74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9df74.md) → [`00b9ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ef68.md) _ZNK10reflection6Schema6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca40.md) · 呼出先 4件 [`00c5c9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9f0.md) [`00c5ca00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca00.md) [`00c5ca30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca30.md) [`00c5ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca70.md)
- 新版 呼出元 1件 [`00c5da10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da10.md) · 呼出先 4件 [`00c5d9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9c0.md) [`00c5d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9d0.md) [`00c5da00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da00.md) [`00c5da40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9e150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9df74.md#insn-00b9e150) · [`00b9e27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9df74.md#insn-00b9e27c) · [`00b9e510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9df74.md#insn-00b9e510)
- 新版 [`00b9f144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ef68.md#insn-00b9f144) · [`00b9f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ef68.md#insn-00b9f270) · [`00b9f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9ef68.md#insn-00b9f504)

~~~diff
- 00b9e150 ["INT_ADD", "register:40f0:8", ["const:b9e150:8", "const:4:8"]]
- 00b9e150 ["CALL", null, ["callee:00c5da00:8"]]
+ 00b9f144 ["INT_ADD", "register:40f0:8", ["const:b9f144:8", "const:4:8"]]
+ 00b9f144 ["CALL", null, ["callee:00c5da00:8"]]
- 00b9e150 bytes 38fa0294
+ 00b9f144 bytes 2ffa0294
- 00b9e27c ["INT_ADD", "register:40f0:8", ["const:b9e27c:8", "const:4:8"]]
- 00b9e27c ["CALL", null, ["callee:00c5d9d0:8"]]
+ 00b9f270 ["INT_ADD", "register:40f0:8", ["const:b9f270:8", "const:4:8"]]
+ 00b9f270 ["CALL", null, ["callee:00c5d9d0:8"]]
- 00b9e27c bytes e1f90294
+ 00b9f270 bytes d8f90294
- 00b9e510 ["INT_ADD", "register:40f0:8", ["const:b9e510:8", "const:4:8"]]
- 00b9e510 ["CALL", null, ["callee:00c5da00:8"]]
+ 00b9f504 ["INT_ADD", "register:40f0:8", ["const:b9f504:8", "const:4:8"]]
+ 00b9f504 ["CALL", null, ["callee:00c5da00:8"]]
- 00b9e510 bytes 48f90294
+ 00b9f504 bytes 3ff90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4308f63ff286c14f5cbd00067dfa3664"></a>

### [`00b9e7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9e7ec.md) → [`00b9f7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9f7e0.md) _ZNK10reflection6Object6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca30.md) · 呼出先 2件 [`00c5ca20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca20.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5da00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da00.md) · 呼出先 2件 [`00c5d9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9f0.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9eab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9e7ec.md#insn-00b9eab0) · [`00b9ecd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9e7ec.md#insn-00b9ecd0)
- 新版 [`00b9faa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9f7e0.md#insn-00b9faa4) · [`00b9fcc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9f7e0.md#insn-00b9fcc4)

~~~diff
- 00b9eab0 ["INT_ADD", "register:40f0:8", ["const:b9eab0:8", "const:4:8"]]
- 00b9eab0 ["CALL", null, ["callee:00c5d9f0:8"]]
+ 00b9faa4 ["INT_ADD", "register:40f0:8", ["const:b9faa4:8", "const:4:8"]]
+ 00b9faa4 ["CALL", null, ["callee:00c5d9f0:8"]]
- 00b9eab0 bytes dcf70294
+ 00b9faa4 bytes d3f70294
- 00b9ecd0 ["INT_ADD", "register:40f0:8", ["const:b9ecd0:8", "const:4:8"]]
- 00b9ecd0 ["CALL", null, ["callee:00c5da50:8"]]
+ 00b9fcc4 ["INT_ADD", "register:40f0:8", ["const:b9fcc4:8", "const:4:8"]]
+ 00b9fcc4 ["CALL", null, ["callee:00c5da50:8"]]
- 00b9ecd0 bytes 6cf70294
+ 00b9fcc4 bytes 63f70294
~~~


<a id="compare-c74611154fcd36aae5abfc39c4cd9f5e"></a>

### [`00b9efb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9efb0.md) → [`00b9ffa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9ffa4.md) _ZNK10reflection5Field6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca20.md) · 呼出先 2件 [`00c5ca10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca10.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9f0.md) · 呼出先 2件 [`00c5d9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9e0.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9f1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9efb0.md#insn-00b9f1f0) · [`00b9f55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9e/00b9efb0.md#insn-00b9f55c)
- 新版 [`00ba01e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9ffa4.md#insn-00ba01e4) · [`00ba0550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9f/00b9ffa4.md#insn-00ba0550)

~~~diff
- 00b9f1f0 ["INT_ADD", "register:40f0:8", ["const:b9f1f0:8", "const:4:8"]]
- 00b9f1f0 ["CALL", null, ["callee:00c5d9e0:8"]]
+ 00ba01e4 ["INT_ADD", "register:40f0:8", ["const:ba01e4:8", "const:4:8"]]
+ 00ba01e4 ["CALL", null, ["callee:00c5d9e0:8"]]
- 00b9f1f0 bytes 08f60294
+ 00ba01e4 bytes fff50294
- 00b9f55c ["INT_ADD", "register:40f0:8", ["const:b9f55c:8", "const:4:8"]]
- 00b9f55c ["CALL", null, ["callee:00c5da50:8"]]
+ 00ba0550 ["INT_ADD", "register:40f0:8", ["const:ba0550:8", "const:4:8"]]
+ 00ba0550 ["CALL", null, ["callee:00c5da50:8"]]
- 00b9f55c bytes 49f50294
+ 00ba0550 bytes 40f50294
~~~


<a id="compare-92bf9454504cc773957f44b2e5483fdb"></a>

### [`00b9fc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9f/00b9fc90.md) → [`00ba0c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba0/00ba0c84.md) _ZNK10reflection4Enum6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca00.md) · 呼出先 3件 [`00c5ca10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca10.md) [`00c5ca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca50.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9d0.md) · 呼出先 3件 [`00c5d9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9e0.md) [`00c5da20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da20.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9f/00b9fc90.md#insn-00b9ff68) · [`00ba0078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9f/00b9fc90.md#insn-00ba0078) · [`00ba01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9f/00b9fc90.md#insn-00ba01c8)
- 新版 [`00ba0f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba0/00ba0c84.md#insn-00ba0f5c) · [`00ba106c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba0/00ba0c84.md#insn-00ba106c) · [`00ba11bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba0/00ba0c84.md#insn-00ba11bc)

~~~diff
- 00b9ff68 ["INT_ADD", "register:40f0:8", ["const:b9ff68:8", "const:4:8"]]
- 00b9ff68 ["CALL", null, ["callee:00c5da20:8"]]
+ 00ba0f5c ["INT_ADD", "register:40f0:8", ["const:ba0f5c:8", "const:4:8"]]
+ 00ba0f5c ["CALL", null, ["callee:00c5da20:8"]]
- 00b9ff68 bytes baf20294
+ 00ba0f5c bytes b1f20294
- 00ba0078 ["INT_ADD", "register:40f0:8", ["const:ba0078:8", "const:4:8"]]
- 00ba0078 ["CALL", null, ["callee:00c5d9e0:8"]]
+ 00ba106c ["INT_ADD", "register:40f0:8", ["const:ba106c:8", "const:4:8"]]
+ 00ba106c ["CALL", null, ["callee:00c5d9e0:8"]]
- 00ba0078 bytes 66f20294
+ 00ba106c bytes 5df20294
- 00ba01c8 ["INT_ADD", "register:40f0:8", ["const:ba01c8:8", "const:4:8"]]
- 00ba01c8 ["CALL", null, ["callee:00c5da50:8"]]
+ 00ba11bc ["INT_ADD", "register:40f0:8", ["const:ba11bc:8", "const:4:8"]]
+ 00ba11bc ["CALL", null, ["callee:00c5da50:8"]]
- 00ba01c8 bytes 2ef20294
+ 00ba11bc bytes 25f20294
~~~


<a id="compare-4805bb0f46e769bb5dd693e4e2a04604"></a>

### [`00ba04e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba04e0.md) → [`00ba14d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba14d4.md) _ZNK10reflection7EnumVal6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca50.md) · 呼出先 2件 [`00c5ca10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca10.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5da20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da20.md) · 呼出先 2件 [`00c5d9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d9e0.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba04e0.md#insn-00ba0748) · [`00ba0a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba04e0.md#insn-00ba0a04)
- 新版 [`00ba173c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba14d4.md#insn-00ba173c) · [`00ba19f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba14d4.md#insn-00ba19f8)

~~~diff
- 00ba0748 ["INT_ADD", "register:40f0:8", ["const:ba0748:8", "const:4:8"]]
- 00ba0748 ["CALL", null, ["callee:00c5d9e0:8"]]
+ 00ba173c ["INT_ADD", "register:40f0:8", ["const:ba173c:8", "const:4:8"]]
+ 00ba173c ["CALL", null, ["callee:00c5d9e0:8"]]
- 00ba0748 bytes b2f00294
+ 00ba173c bytes a9f00294
- 00ba0a04 ["INT_ADD", "register:40f0:8", ["const:ba0a04:8", "const:4:8"]]
- 00ba0a04 ["CALL", null, ["callee:00c5da50:8"]]
+ 00ba19f8 ["INT_ADD", "register:40f0:8", ["const:ba19f8:8", "const:4:8"]]
+ 00ba19f8 ["CALL", null, ["callee:00c5da50:8"]]
- 00ba0a04 bytes 1ff00294
+ 00ba19f8 bytes 16f00294
~~~


<a id="compare-90ecb574a5dcadd39514e49a7018347b"></a>

### [`00ba0a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba0a34.md) → [`00ba1a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba1a28.md) _ZNK10reflection7Service6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca70.md) · 呼出先 2件 [`00c5ca60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca60.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da40.md) · 呼出先 2件 [`00c5da30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da30.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba0a34.md#insn-00ba0ce8) · [`00ba0e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba0/00ba0a34.md#insn-00ba0e24)
- 新版 [`00ba1cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba1a28.md#insn-00ba1cdc) · [`00ba1e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba1/00ba1a28.md#insn-00ba1e18)

~~~diff
- 00ba0ce8 ["INT_ADD", "register:40f0:8", ["const:ba0ce8:8", "const:4:8"]]
- 00ba0ce8 ["CALL", null, ["callee:00c5da30:8"]]
+ 00ba1cdc ["INT_ADD", "register:40f0:8", ["const:ba1cdc:8", "const:4:8"]]
+ 00ba1cdc ["CALL", null, ["callee:00c5da30:8"]]
- 00ba0ce8 bytes 5eef0294
+ 00ba1cdc bytes 55ef0294
- 00ba0e24 ["INT_ADD", "register:40f0:8", ["const:ba0e24:8", "const:4:8"]]
- 00ba0e24 ["CALL", null, ["callee:00c5da50:8"]]
+ 00ba1e18 ["INT_ADD", "register:40f0:8", ["const:ba1e18:8", "const:4:8"]]
+ 00ba1e18 ["CALL", null, ["callee:00c5da50:8"]]
- 00ba0e24 bytes 17ef0294
+ 00ba1e18 bytes 0eef0294
~~~


<a id="compare-d8f2667a52021daf60d36adc75c7b772"></a>

### [`00ba10ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba10ec.md) → [`00ba20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba20e0.md) _ZNK10reflection7RPCCall6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca60.md) · 呼出先 2件 [`00c5ca30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca30.md) [`00c5ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca80.md)
- 新版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da30.md) · 呼出先 2件 [`00c5da00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da00.md) [`00c5da50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba10ec.md#insn-00ba132c) · [`00ba13e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba10ec.md#insn-00ba13e0) · [`00ba1530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba10ec.md#insn-00ba1530)
- 新版 [`00ba2320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba20e0.md#insn-00ba2320) · [`00ba23d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba20e0.md#insn-00ba23d4) · [`00ba2524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba20e0.md#insn-00ba2524)

~~~diff
- 00ba132c ["INT_ADD", "register:40f0:8", ["const:ba132c:8", "const:4:8"]]
- 00ba132c ["CALL", null, ["callee:00c5da00:8"]]
+ 00ba2320 ["INT_ADD", "register:40f0:8", ["const:ba2320:8", "const:4:8"]]
+ 00ba2320 ["CALL", null, ["callee:00c5da00:8"]]
- 00ba132c bytes c1ed0294
+ 00ba2320 bytes b8ed0294
- 00ba13e0 ["INT_ADD", "register:40f0:8", ["const:ba13e0:8", "const:4:8"]]
- 00ba13e0 ["CALL", null, ["callee:00c5da00:8"]]
+ 00ba23d4 ["INT_ADD", "register:40f0:8", ["const:ba23d4:8", "const:4:8"]]
+ 00ba23d4 ["CALL", null, ["callee:00c5da00:8"]]
- 00ba13e0 bytes 94ed0294
+ 00ba23d4 bytes 8bed0294
- 00ba1530 ["INT_ADD", "register:40f0:8", ["const:ba1530:8", "const:4:8"]]
- 00ba1530 ["CALL", null, ["callee:00c5da50:8"]]
+ 00ba2524 ["INT_ADD", "register:40f0:8", ["const:ba2524:8", "const:4:8"]]
+ 00ba2524 ["CALL", null, ["callee:00c5da50:8"]]
- 00ba1530 bytes 54ed0294
+ 00ba2524 bytes 4bed0294
~~~


<a id="compare-ac57608066a697362eaa61aadf210b7a"></a>

### [`00ba1a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md) → [`00ba2a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba2a2c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d030.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5e000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e000.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba1ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md#insn-00ba1ad4) · [`00ba1b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md#insn-00ba1b14)
- 新版 [`00ba2ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba2a2c.md#insn-00ba2ac8) · [`00ba2b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba2/00ba2a2c.md#insn-00ba2b08)

~~~diff
- 00ba1ad4 ["INT_ADD", "register:40f0:8", ["const:ba1ad4:8", "const:4:8"]]
- 00ba1ad4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba2ac8 ["INT_ADD", "register:40f0:8", ["const:ba2ac8:8", "const:4:8"]]
+ 00ba2ac8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba1ad4 bytes 93d90294
+ 00ba2ac8 bytes 8ad90294
- 00ba1b14 ["INT_ADD", "register:40f0:8", ["const:ba1b14:8", "const:4:8"]]
- 00ba1b14 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba2b08 ["INT_ADD", "register:40f0:8", ["const:ba2b08:8", "const:4:8"]]
+ 00ba2b08 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba1b14 bytes 83d90294
+ 00ba2b08 bytes 7ad90294
~~~


<a id="compare-706128c0e54978be91b2965ed4142cc6"></a>

### [`00ba2248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2248.md) → [`00ba323c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba323c.md) _ZN11flatbuffers15vector_downwardIjE10reallocateEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)
- 新版 呼出元 1件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba22d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2248.md#insn-00ba22d8) · [`00ba22f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2248.md#insn-00ba22f0) · [`00ba22fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2248.md#insn-00ba22fc)
- 新版 [`00ba32cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba323c.md#insn-00ba32cc) · [`00ba32e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba323c.md#insn-00ba32e4) · [`00ba32f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba323c.md#insn-00ba32f0)

~~~diff
- 00ba22d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba22d8 ["INT_ADD", "register:40f0:8", ["const:ba22d8:8", "const:4:8"]]
- 00ba22d8 ["CALLIND", null, ["register:0:8"]]
+ 00ba32cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba32cc ["INT_ADD", "register:40f0:8", ["const:ba32cc:8", "const:4:8"]]
+ 00ba32cc ["CALLIND", null, ["register:0:8"]]
- 00ba22d8 bytes 00013fd6
+ 00ba32cc bytes 00013fd6
- 00ba22f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba22f0 ["INT_ADD", "register:40f0:8", ["const:ba22f0:8", "const:4:8"]]
- 00ba22f0 ["CALLIND", null, ["register:0:8"]]
+ 00ba32e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba32e4 ["INT_ADD", "register:40f0:8", ["const:ba32e4:8", "const:4:8"]]
+ 00ba32e4 ["CALLIND", null, ["register:0:8"]]
- 00ba22f0 bytes 00013fd6
+ 00ba32e4 bytes 00013fd6
- 00ba22fc ["INT_ADD", "register:40f0:8", ["const:ba22fc:8", "const:4:8"]]
- 00ba22fc ["CALL", null, ["callee:00c5cef0:8"]]
+ 00ba32f0 ["INT_ADD", "register:40f0:8", ["const:ba32f0:8", "const:4:8"]]
+ 00ba32f0 ["CALL", null, ["callee:00c5cef0:8"]]
- 00ba22fc bytes 09e70294
+ 00ba32f0 bytes 00e70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c46bb7178a73b85d6803a8bd208193d"></a>

### [`00ba2374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2374.md) → [`00ba3368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3368.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_S

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbe0.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbe0.md) [`00c5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc70.md) [`00c5cd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd10.md)
- 新版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbb0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbb0.md) [`00c5dc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc40.md) [`00c5dce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba2410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2374.md#insn-00ba2410) · [`00ba24fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2374.md#insn-00ba24fc) · [`00ba2564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2374.md#insn-00ba2564)
- 新版 [`00ba3404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3368.md#insn-00ba3404) · [`00ba34f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3368.md#insn-00ba34f0) · [`00ba3558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3368.md#insn-00ba3558)

~~~diff
- 00ba2410 ["INT_ADD", "register:40f0:8", ["const:ba2410:8", "const:4:8"]]
- 00ba2410 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba3404 ["INT_ADD", "register:40f0:8", ["const:ba3404:8", "const:4:8"]]
+ 00ba3404 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba2410 bytes 44d70294
+ 00ba3404 bytes 3bd70294
- 00ba24fc ["INT_ADD", "register:40f0:8", ["const:ba24fc:8", "const:4:8"]]
- 00ba24fc ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba34f0 ["INT_ADD", "register:40f0:8", ["const:ba34f0:8", "const:4:8"]]
+ 00ba34f0 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba24fc bytes 09d70294
+ 00ba34f0 bytes 00d70294
- 00ba2564 ["INT_ADD", "register:40f0:8", ["const:ba2564:8", "const:4:8"]]
- 00ba2564 ["CALL", null, ["callee:00c5dbb0:8"]]
+ 00ba3558 ["INT_ADD", "register:40f0:8", ["const:ba3558:8", "const:4:8"]]
+ 00ba3558 ["CALL", null, ["callee:00c5dbb0:8"]]
- 00ba2564 bytes 9fe90294
+ 00ba3558 bytes 96e90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa36fb9c6a0ab03e1f896b860a63a07"></a>

### [`00ba2840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2840.md) → [`00ba3834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3834.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd10.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbe0.md) [`00c5cdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 1件 [`00c5dce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dce0.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbb0.md) [`00c5dda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba28f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2840.md#insn-00ba28f4) · [`00ba29a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2840.md#insn-00ba29a8) · [`00ba29c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2840.md#insn-00ba29c4)
- 新版 [`00ba38e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3834.md#insn-00ba38e8) · [`00ba399c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3834.md#insn-00ba399c) · [`00ba39b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3834.md#insn-00ba39b8)

~~~diff
- 00ba28f4 ["INT_ADD", "register:40f0:8", ["const:ba28f4:8", "const:4:8"]]
- 00ba28f4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba38e8 ["INT_ADD", "register:40f0:8", ["const:ba38e8:8", "const:4:8"]]
+ 00ba38e8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba28f4 bytes 0bd60294
+ 00ba38e8 bytes 02d60294
- 00ba29a8 ["INT_ADD", "register:40f0:8", ["const:ba29a8:8", "const:4:8"]]
- 00ba29a8 ["CALL", null, ["callee:00c5dbb0:8"]]
+ 00ba399c ["INT_ADD", "register:40f0:8", ["const:ba399c:8", "const:4:8"]]
+ 00ba399c ["CALL", null, ["callee:00c5dbb0:8"]]
- 00ba29a8 bytes 8ee80294
+ 00ba399c bytes 85e80294
- 00ba29c4 ["INT_ADD", "register:40f0:8", ["const:ba29c4:8", "const:4:8"]]
- 00ba29c4 ["CALL", null, ["callee:00c5dbb0:8"]]
+ 00ba39b8 ["INT_ADD", "register:40f0:8", ["const:ba39b8:8", "const:4:8"]]
+ 00ba39b8 ["CALL", null, ["callee:00c5dbb0:8"]]
- 00ba29c4 bytes 87e80294
+ 00ba39b8 bytes 7ee80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a8f56a66ed438bee101f9eee44fc2b6"></a>

### [`00ba2bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md) → [`00ba3be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc70.md) · 呼出先 4件 [`00ba35e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba35e0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc70.md) [`00c5ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce30.md)
- 新版 呼出元 1件 [`00c5dc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc40.md) · 呼出先 4件 [`00ba45d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba45d4.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc40.md) [`00c5de00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba2cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2cb8) · [`00ba2d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2d90) · [`00ba2e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2e7c)
- 新版 [`00ba3cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md#insn-00ba3cac) · [`00ba3d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md#insn-00ba3d84) · [`00ba3e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md#insn-00ba3e70)

~~~diff
- 00ba2cb8 ["INT_ADD", "register:40f0:8", ["const:ba2cb8:8", "const:4:8"]]
- 00ba2cb8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba3cac ["INT_ADD", "register:40f0:8", ["const:ba3cac:8", "const:4:8"]]
+ 00ba3cac ["CALL", null, ["callee:00c590f0:8"]]
- 00ba2cb8 bytes 1ad50294
+ 00ba3cac bytes 11d50294
- 00ba2d90 ["INT_ADD", "register:40f0:8", ["const:ba2d90:8", "const:4:8"]]
- 00ba2d90 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba3d84 ["INT_ADD", "register:40f0:8", ["const:ba3d84:8", "const:4:8"]]
+ 00ba3d84 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba2d90 bytes e4d40294
+ 00ba3d84 bytes dbd40294
- 00ba2e7c ["INT_ADD", "register:40f0:8", ["const:ba2e7c:8", "const:4:8"]]
- 00ba2e7c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba3e70 ["INT_ADD", "register:40f0:8", ["const:ba3e70:8", "const:4:8"]]
+ 00ba3e70 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba2e7c bytes a9d40294
+ 00ba3e70 bytes a0d40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577379fe190eb75a468c857bc80890ea"></a>

### [`00ba3014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3014.md) → [`00ba4008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4008.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdd0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dda0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba30c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3014.md#insn-00ba30c4) · [`00ba314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3014.md#insn-00ba314c)
- 新版 [`00ba40b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4008.md#insn-00ba40b8) · [`00ba4140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4008.md#insn-00ba4140)

~~~diff
- 00ba30c4 ["INT_ADD", "register:40f0:8", ["const:ba30c4:8", "const:4:8"]]
- 00ba30c4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba40b8 ["INT_ADD", "register:40f0:8", ["const:ba40b8:8", "const:4:8"]]
+ 00ba40b8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba30c4 bytes 17d40294
+ 00ba40b8 bytes 0ed40294
- 00ba314c ["INT_ADD", "register:40f0:8", ["const:ba314c:8", "const:4:8"]]
- 00ba314c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba4140 ["INT_ADD", "register:40f0:8", ["const:ba4140:8", "const:4:8"]]
+ 00ba4140 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba314c bytes f5d30294
+ 00ba4140 bytes ecd30294
~~~


<a id="compare-498cf64c6c8f8910b571b228d1ac71f4"></a>

### [`00ba31cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba31cc.md) → [`00ba41c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba41c0.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce30.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd70.md)
- 新版 呼出元 1件 [`00c5de00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de00.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba3358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba31cc.md#insn-00ba3358) · [`00ba3448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba31cc.md#insn-00ba3448) · [`00ba34a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba31cc.md#insn-00ba34a4)
- 新版 [`00ba434c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba41c0.md#insn-00ba434c) · [`00ba443c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba41c0.md#insn-00ba443c) · [`00ba4498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba41c0.md#insn-00ba4498)

~~~diff
- 00ba3358 ["INT_ADD", "register:40f0:8", ["const:ba3358:8", "const:4:8"]]
- 00ba3358 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba434c ["INT_ADD", "register:40f0:8", ["const:ba434c:8", "const:4:8"]]
+ 00ba434c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba3358 bytes 72d30294
+ 00ba434c bytes 69d30294
- 00ba3448 ["INT_ADD", "register:40f0:8", ["const:ba3448:8", "const:4:8"]]
- 00ba3448 ["CALL", null, ["callee:00c5dd40:8"]]
+ 00ba443c ["INT_ADD", "register:40f0:8", ["const:ba443c:8", "const:4:8"]]
+ 00ba443c ["CALL", null, ["callee:00c5dd40:8"]]
- 00ba3448 bytes 4ae60294
+ 00ba443c bytes 41e60294
- 00ba34a4 ["INT_ADD", "register:40f0:8", ["const:ba34a4:8", "const:4:8"]]
- 00ba34a4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00ba4498 ["INT_ADD", "register:40f0:8", ["const:ba4498:8", "const:4:8"]]
+ 00ba4498 ["CALL", null, ["callee:00c58f80:8"]]
- 00ba34a4 bytes c3d20294
+ 00ba4498 bytes bad20294
~~~


<a id="compare-4dbf08e5fd9e784942cb6716fbd7ceb8"></a>

### [`00ba34a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba34a8.md) → [`00ba449c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba449c.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EES

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd70.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd40.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba356c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba34a8.md#insn-00ba356c)
- 新版 [`00ba4560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba449c.md#insn-00ba4560)

~~~diff
- 00ba356c ["INT_ADD", "register:40f0:8", ["const:ba356c:8", "const:4:8"]]
- 00ba356c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba4560 ["INT_ADD", "register:40f0:8", ["const:ba4560:8", "const:4:8"]]
+ 00ba4560 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba356c bytes edd20294
+ 00ba4560 bytes e4d20294
~~~


<a id="compare-ee1b41f2b885ca5c5d6433df177bb29e"></a>

### [`00ba35e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba35e0.md) → [`00ba45d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba45d4.md) FUN_00ba45d4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ba2bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00ba3be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba36a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba35e0.md#insn-00ba36a0) · [`00ba36cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba35e0.md#insn-00ba36cc)
- 新版 [`00ba4694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba45d4.md#insn-00ba4694) · [`00ba46c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba45d4.md#insn-00ba46c0)

~~~diff
- 00ba36a0 ["INT_ADD", "register:40f0:8", ["const:ba36a0:8", "const:4:8"]]
- 00ba36a0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba4694 ["INT_ADD", "register:40f0:8", ["const:ba4694:8", "const:4:8"]]
+ 00ba4694 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba36a0 bytes 5cd20294
+ 00ba4694 bytes 53d20294
- 00ba36cc ["INT_ADD", "register:40f0:8", ["const:ba36cc:8", "const:4:8"]]
- 00ba36cc ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba46c0 ["INT_ADD", "register:40f0:8", ["const:ba46c0:8", "const:4:8"]]
+ 00ba46c0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba36cc bytes 51d20294
+ 00ba46c0 bytes 48d20294
~~~


<a id="compare-c3b59234cb1924257ebe25d7728e6440"></a>

### [`00ba37a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba37a8.md) → [`00ba479c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba479c.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_EEEEvT0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbf0.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbf0.md) [`00c5cc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc80.md) [`00c5cd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd20.md)
- 新版 呼出元 1件 [`00c5dbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbc0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbc0.md) [`00c5dc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc50.md) [`00c5dcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba3844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba37a8.md#insn-00ba3844) · [`00ba3930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba37a8.md#insn-00ba3930) · [`00ba3998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba37a8.md#insn-00ba3998)
- 新版 [`00ba4838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba479c.md#insn-00ba4838) · [`00ba4924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba479c.md#insn-00ba4924) · [`00ba498c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba479c.md#insn-00ba498c)

~~~diff
- 00ba3844 ["INT_ADD", "register:40f0:8", ["const:ba3844:8", "const:4:8"]]
- 00ba3844 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba4838 ["INT_ADD", "register:40f0:8", ["const:ba4838:8", "const:4:8"]]
+ 00ba4838 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba3844 bytes 37d20294
+ 00ba4838 bytes 2ed20294
- 00ba3930 ["INT_ADD", "register:40f0:8", ["const:ba3930:8", "const:4:8"]]
- 00ba3930 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba4924 ["INT_ADD", "register:40f0:8", ["const:ba4924:8", "const:4:8"]]
+ 00ba4924 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba3930 bytes fcd10294
+ 00ba4924 bytes f3d10294
- 00ba3998 ["INT_ADD", "register:40f0:8", ["const:ba3998:8", "const:4:8"]]
- 00ba3998 ["CALL", null, ["callee:00c5dbc0:8"]]
+ 00ba498c ["INT_ADD", "register:40f0:8", ["const:ba498c:8", "const:4:8"]]
+ 00ba498c ["CALL", null, ["callee:00c5dbc0:8"]]
- 00ba3998 bytes 96e40294
+ 00ba498c bytes 8de40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0159eccaca61695271a59b6c20b2ba49"></a>

### [`00ba3c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3c74.md) → [`00ba4c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4c68.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd20.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbf0.md) [`00c5cde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cde0.md)
- 新版 呼出元 1件 [`00c5dcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcf0.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbc0.md) [`00c5ddb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba3d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3c74.md#insn-00ba3d28) · [`00ba3ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3c74.md#insn-00ba3ddc) · [`00ba3df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba3c74.md#insn-00ba3df8)
- 新版 [`00ba4d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4c68.md#insn-00ba4d1c) · [`00ba4dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4c68.md#insn-00ba4dd0) · [`00ba4dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba4/00ba4c68.md#insn-00ba4dec)

~~~diff
- 00ba3d28 ["INT_ADD", "register:40f0:8", ["const:ba3d28:8", "const:4:8"]]
- 00ba3d28 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba4d1c ["INT_ADD", "register:40f0:8", ["const:ba4d1c:8", "const:4:8"]]
+ 00ba4d1c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba3d28 bytes fed00294
+ 00ba4d1c bytes f5d00294
- 00ba3ddc ["INT_ADD", "register:40f0:8", ["const:ba3ddc:8", "const:4:8"]]
- 00ba3ddc ["CALL", null, ["callee:00c5dbc0:8"]]
+ 00ba4dd0 ["INT_ADD", "register:40f0:8", ["const:ba4dd0:8", "const:4:8"]]
+ 00ba4dd0 ["CALL", null, ["callee:00c5dbc0:8"]]
- 00ba3ddc bytes 85e30294
+ 00ba4dd0 bytes 7ce30294
- 00ba3df8 ["INT_ADD", "register:40f0:8", ["const:ba3df8:8", "const:4:8"]]
- 00ba3df8 ["CALL", null, ["callee:00c5dbc0:8"]]
+ 00ba4dec ["INT_ADD", "register:40f0:8", ["const:ba4dec:8", "const:4:8"]]
+ 00ba4dec ["CALL", null, ["callee:00c5dbc0:8"]]
- 00ba3df8 bytes 7ee30294
+ 00ba4dec bytes 75e30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8c311f99398c9d8dafb08507368db6"></a>

### [`00ba4020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4020.md) → [`00ba5014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5014.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_EEEEvT

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc80.md) · 呼出先 4件 [`00ba4a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4a14.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc80.md) [`00c5ce40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce40.md)
- 新版 呼出元 1件 [`00c5dc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc50.md) · 呼出先 4件 [`00ba5a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5a08.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc50.md) [`00c5de10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba40ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4020.md#insn-00ba40ec) · [`00ba41c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4020.md#insn-00ba41c4) · [`00ba42b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4020.md#insn-00ba42b0)
- 新版 [`00ba50e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5014.md#insn-00ba50e0) · [`00ba51b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5014.md#insn-00ba51b8) · [`00ba52a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5014.md#insn-00ba52a4)

~~~diff
- 00ba40ec ["INT_ADD", "register:40f0:8", ["const:ba40ec:8", "const:4:8"]]
- 00ba40ec ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba50e0 ["INT_ADD", "register:40f0:8", ["const:ba50e0:8", "const:4:8"]]
+ 00ba50e0 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba40ec bytes 0dd00294
+ 00ba50e0 bytes 04d00294
- 00ba41c4 ["INT_ADD", "register:40f0:8", ["const:ba41c4:8", "const:4:8"]]
- 00ba41c4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba51b8 ["INT_ADD", "register:40f0:8", ["const:ba51b8:8", "const:4:8"]]
+ 00ba51b8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba41c4 bytes d7cf0294
+ 00ba51b8 bytes cecf0294
- 00ba42b0 ["INT_ADD", "register:40f0:8", ["const:ba42b0:8", "const:4:8"]]
- 00ba42b0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba52a4 ["INT_ADD", "register:40f0:8", ["const:ba52a4:8", "const:4:8"]]
+ 00ba52a4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba42b0 bytes 9ccf0294
+ 00ba52a4 bytes 93cf0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7cb050507ba9005cea5e8c9e298f46"></a>

### [`00ba4448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4448.md) → [`00ba543c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba543c.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cde0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ddb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddb0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba44f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4448.md#insn-00ba44f8) · [`00ba4580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4448.md#insn-00ba4580)
- 新版 [`00ba54ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba543c.md#insn-00ba54ec) · [`00ba5574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba543c.md#insn-00ba5574)

~~~diff
- 00ba44f8 ["INT_ADD", "register:40f0:8", ["const:ba44f8:8", "const:4:8"]]
- 00ba44f8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba54ec ["INT_ADD", "register:40f0:8", ["const:ba54ec:8", "const:4:8"]]
+ 00ba54ec ["CALL", null, ["callee:00c590f0:8"]]
- 00ba44f8 bytes 0acf0294
+ 00ba54ec bytes 01cf0294
- 00ba4580 ["INT_ADD", "register:40f0:8", ["const:ba4580:8", "const:4:8"]]
- 00ba4580 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba5574 ["INT_ADD", "register:40f0:8", ["const:ba5574:8", "const:4:8"]]
+ 00ba5574 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba4580 bytes e8ce0294
+ 00ba5574 bytes dfce0294
~~~


<a id="compare-7c937c7ae11175d48f3c73d75613284b"></a>

### [`00ba4600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4600.md) → [`00ba55f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba55f4.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetI

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce40.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd80.md)
- 新版 呼出元 1件 [`00c5de10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de10.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba478c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4600.md#insn-00ba478c) · [`00ba487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4600.md#insn-00ba487c) · [`00ba48d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4600.md#insn-00ba48d8)
- 新版 [`00ba5780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba55f4.md#insn-00ba5780) · [`00ba5870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba55f4.md#insn-00ba5870) · [`00ba58cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba55f4.md#insn-00ba58cc)

~~~diff
- 00ba478c ["INT_ADD", "register:40f0:8", ["const:ba478c:8", "const:4:8"]]
- 00ba478c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba5780 ["INT_ADD", "register:40f0:8", ["const:ba5780:8", "const:4:8"]]
+ 00ba5780 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba478c bytes 65ce0294
+ 00ba5780 bytes 5cce0294
- 00ba487c ["INT_ADD", "register:40f0:8", ["const:ba487c:8", "const:4:8"]]
- 00ba487c ["CALL", null, ["callee:00c5dd50:8"]]
+ 00ba5870 ["INT_ADD", "register:40f0:8", ["const:ba5870:8", "const:4:8"]]
+ 00ba5870 ["CALL", null, ["callee:00c5dd50:8"]]
- 00ba487c bytes 41e10294
+ 00ba5870 bytes 38e10294
- 00ba48d8 ["INT_ADD", "register:40f0:8", ["const:ba48d8:8", "const:4:8"]]
- 00ba48d8 ["CALL", null, ["callee:00c58f80:8"]]
+ 00ba58cc ["INT_ADD", "register:40f0:8", ["const:ba58cc:8", "const:4:8"]]
+ 00ba58cc ["CALL", null, ["callee:00c58f80:8"]]
- 00ba48d8 bytes b6cd0294
+ 00ba58cc bytes adcd0294
~~~


<a id="compare-43e0b0ebe93b77725978c46c891b5807"></a>

### [`00ba48dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba48dc.md) → [`00ba58d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba58d0.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd80.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd50.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba49a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba48dc.md#insn-00ba49a0)
- 新版 [`00ba5994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba58d0.md#insn-00ba5994)

~~~diff
- 00ba49a0 ["INT_ADD", "register:40f0:8", ["const:ba49a0:8", "const:4:8"]]
- 00ba49a0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba5994 ["INT_ADD", "register:40f0:8", ["const:ba5994:8", "const:4:8"]]
+ 00ba5994 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba49a0 bytes e0cd0294
+ 00ba5994 bytes d7cd0294
~~~


<a id="compare-3742c575f84b405c8ecb3131115200ad"></a>

### [`00ba4a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4a14.md) → [`00ba5a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5a08.md) FUN_00ba5a08

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ba4020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4020.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00ba5014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5014.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba4ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4a14.md#insn-00ba4ad4) · [`00ba4b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4a14.md#insn-00ba4b00)
- 新版 [`00ba5ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5a08.md#insn-00ba5ac8) · [`00ba5af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5a08.md#insn-00ba5af4)

~~~diff
- 00ba4ad4 ["INT_ADD", "register:40f0:8", ["const:ba4ad4:8", "const:4:8"]]
- 00ba4ad4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba5ac8 ["INT_ADD", "register:40f0:8", ["const:ba5ac8:8", "const:4:8"]]
+ 00ba5ac8 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba4ad4 bytes 4fcd0294
+ 00ba5ac8 bytes 46cd0294
- 00ba4b00 ["INT_ADD", "register:40f0:8", ["const:ba4b00:8", "const:4:8"]]
- 00ba4b00 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba5af4 ["INT_ADD", "register:40f0:8", ["const:ba5af4:8", "const:4:8"]]
+ 00ba5af4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba4b00 bytes 44cd0294
+ 00ba5af4 bytes 3bcd0294
~~~


<a id="compare-030fad3d7bb9cc01cf9de143e6a50b88"></a>

### [`00ba4bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4bdc.md) → [`00ba5bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5bd0.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbd0.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbd0.md) [`00c5cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc60.md) [`00c5cd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd00.md)
- 新版 呼出元 1件 [`00c5dba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dba0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dba0.md) [`00c5dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc30.md) [`00c5dcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba4c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4bdc.md#insn-00ba4c78) · [`00ba4d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4bdc.md#insn-00ba4d64) · [`00ba4dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba4/00ba4bdc.md#insn-00ba4dcc)
- 新版 [`00ba5c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5bd0.md#insn-00ba5c6c) · [`00ba5d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5bd0.md#insn-00ba5d58) · [`00ba5dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5bd0.md#insn-00ba5dc0)

~~~diff
- 00ba4c78 ["INT_ADD", "register:40f0:8", ["const:ba4c78:8", "const:4:8"]]
- 00ba4c78 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba5c6c ["INT_ADD", "register:40f0:8", ["const:ba5c6c:8", "const:4:8"]]
+ 00ba5c6c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba4c78 bytes 2acd0294
+ 00ba5c6c bytes 21cd0294
- 00ba4d64 ["INT_ADD", "register:40f0:8", ["const:ba4d64:8", "const:4:8"]]
- 00ba4d64 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba5d58 ["INT_ADD", "register:40f0:8", ["const:ba5d58:8", "const:4:8"]]
+ 00ba5d58 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba4d64 bytes efcc0294
+ 00ba5d58 bytes e6cc0294
- 00ba4dcc ["INT_ADD", "register:40f0:8", ["const:ba4dcc:8", "const:4:8"]]
- 00ba4dcc ["CALL", null, ["callee:00c5dba0:8"]]
+ 00ba5dc0 ["INT_ADD", "register:40f0:8", ["const:ba5dc0:8", "const:4:8"]]
+ 00ba5dc0 ["CALL", null, ["callee:00c5dba0:8"]]
- 00ba4dcc bytes 81df0294
+ 00ba5dc0 bytes 78df0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e73f863a58de3312101f7b49719630"></a>

### [`00ba50a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba50a8.md) → [`00ba609c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba609c.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd00.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbd0.md) [`00c5cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdc0.md)
- 新版 呼出元 1件 [`00c5dcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcd0.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dba0.md) [`00c5dd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba515c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba50a8.md#insn-00ba515c) · [`00ba5210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba50a8.md#insn-00ba5210) · [`00ba522c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba50a8.md#insn-00ba522c)
- 新版 [`00ba6150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba609c.md#insn-00ba6150) · [`00ba6204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba609c.md#insn-00ba6204) · [`00ba6220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba609c.md#insn-00ba6220)

~~~diff
- 00ba515c ["INT_ADD", "register:40f0:8", ["const:ba515c:8", "const:4:8"]]
- 00ba515c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba6150 ["INT_ADD", "register:40f0:8", ["const:ba6150:8", "const:4:8"]]
+ 00ba6150 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba515c bytes f1cb0294
+ 00ba6150 bytes e8cb0294
- 00ba5210 ["INT_ADD", "register:40f0:8", ["const:ba5210:8", "const:4:8"]]
- 00ba5210 ["CALL", null, ["callee:00c5dba0:8"]]
+ 00ba6204 ["INT_ADD", "register:40f0:8", ["const:ba6204:8", "const:4:8"]]
+ 00ba6204 ["CALL", null, ["callee:00c5dba0:8"]]
- 00ba5210 bytes 70de0294
+ 00ba6204 bytes 67de0294
- 00ba522c ["INT_ADD", "register:40f0:8", ["const:ba522c:8", "const:4:8"]]
- 00ba522c ["CALL", null, ["callee:00c5dba0:8"]]
+ 00ba6220 ["INT_ADD", "register:40f0:8", ["const:ba6220:8", "const:4:8"]]
+ 00ba6220 ["CALL", null, ["callee:00c5dba0:8"]]
- 00ba522c bytes 69de0294
+ 00ba6220 bytes 60de0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2857d72b6cae10223bf5c93aa1227d01"></a>

### [`00ba5454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5454.md) → [`00ba6448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6448.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc60.md) · 呼出先 4件 [`00ba5e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5e48.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc60.md) [`00c5ce20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc30.md) · 呼出先 4件 [`00ba6e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6e3c.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc30.md) [`00c5ddf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba5520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5454.md#insn-00ba5520) · [`00ba55f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5454.md#insn-00ba55f8) · [`00ba56e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5454.md#insn-00ba56e4)
- 新版 [`00ba6514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6448.md#insn-00ba6514) · [`00ba65ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6448.md#insn-00ba65ec) · [`00ba66d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6448.md#insn-00ba66d8)

~~~diff
- 00ba5520 ["INT_ADD", "register:40f0:8", ["const:ba5520:8", "const:4:8"]]
- 00ba5520 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba6514 ["INT_ADD", "register:40f0:8", ["const:ba6514:8", "const:4:8"]]
+ 00ba6514 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba5520 bytes 00cb0294
+ 00ba6514 bytes f7ca0294
- 00ba55f8 ["INT_ADD", "register:40f0:8", ["const:ba55f8:8", "const:4:8"]]
- 00ba55f8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba65ec ["INT_ADD", "register:40f0:8", ["const:ba65ec:8", "const:4:8"]]
+ 00ba65ec ["CALL", null, ["callee:00c590f0:8"]]
- 00ba55f8 bytes caca0294
+ 00ba65ec bytes c1ca0294
- 00ba56e4 ["INT_ADD", "register:40f0:8", ["const:ba56e4:8", "const:4:8"]]
- 00ba56e4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba66d8 ["INT_ADD", "register:40f0:8", ["const:ba66d8:8", "const:4:8"]]
+ 00ba66d8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba56e4 bytes 8fca0294
+ 00ba66d8 bytes 86ca0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9317d25e4c1d5cf9d5b0c5e7a5f2df39"></a>

### [`00ba587c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba587c.md) → [`00ba6870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6870.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdc0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd90.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba592c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba587c.md#insn-00ba592c) · [`00ba59b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba587c.md#insn-00ba59b4)
- 新版 [`00ba6920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6870.md#insn-00ba6920) · [`00ba69a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6870.md#insn-00ba69a8)

~~~diff
- 00ba592c ["INT_ADD", "register:40f0:8", ["const:ba592c:8", "const:4:8"]]
- 00ba592c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba6920 ["INT_ADD", "register:40f0:8", ["const:ba6920:8", "const:4:8"]]
+ 00ba6920 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba592c bytes fdc90294
+ 00ba6920 bytes f4c90294
- 00ba59b4 ["INT_ADD", "register:40f0:8", ["const:ba59b4:8", "const:4:8"]]
- 00ba59b4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba69a8 ["INT_ADD", "register:40f0:8", ["const:ba69a8:8", "const:4:8"]]
+ 00ba69a8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba59b4 bytes dbc90294
+ 00ba69a8 bytes d2c90294
~~~


<a id="compare-bbf361d1f29167561b51e4a5587f6303"></a>

### [`00ba5a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5a34.md) → [`00ba6a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6a28.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce20.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd60.md)
- 新版 呼出元 1件 [`00c5ddf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddf0.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba5bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5a34.md#insn-00ba5bc0) · [`00ba5cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5a34.md#insn-00ba5cb0) · [`00ba5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5a34.md#insn-00ba5d0c)
- 新版 [`00ba6bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6a28.md#insn-00ba6bb4) · [`00ba6ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6a28.md#insn-00ba6ca4) · [`00ba6d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6a28.md#insn-00ba6d00)

~~~diff
- 00ba5bc0 ["INT_ADD", "register:40f0:8", ["const:ba5bc0:8", "const:4:8"]]
- 00ba5bc0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba6bb4 ["INT_ADD", "register:40f0:8", ["const:ba6bb4:8", "const:4:8"]]
+ 00ba6bb4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba5bc0 bytes 58c90294
+ 00ba6bb4 bytes 4fc90294
- 00ba5cb0 ["INT_ADD", "register:40f0:8", ["const:ba5cb0:8", "const:4:8"]]
- 00ba5cb0 ["CALL", null, ["callee:00c5dd30:8"]]
+ 00ba6ca4 ["INT_ADD", "register:40f0:8", ["const:ba6ca4:8", "const:4:8"]]
+ 00ba6ca4 ["CALL", null, ["callee:00c5dd30:8"]]
- 00ba5cb0 bytes 2cdc0294
+ 00ba6ca4 bytes 23dc0294
- 00ba5d0c ["INT_ADD", "register:40f0:8", ["const:ba5d0c:8", "const:4:8"]]
- 00ba5d0c ["CALL", null, ["callee:00c58f80:8"]]
+ 00ba6d00 ["INT_ADD", "register:40f0:8", ["const:ba6d00:8", "const:4:8"]]
+ 00ba6d00 ["CALL", null, ["callee:00c58f80:8"]]
- 00ba5d0c bytes a9c80294
+ 00ba6d00 bytes a0c80294
~~~


<a id="compare-ba7518148a15d83cc5fd2fc907c48f58"></a>

### [`00ba5d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5d10.md) → [`00ba6d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6d04.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EESA

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd60.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd30.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba5dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5d10.md#insn-00ba5dd4)
- 新版 [`00ba6dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6d04.md#insn-00ba6dc8)

~~~diff
- 00ba5dd4 ["INT_ADD", "register:40f0:8", ["const:ba5dd4:8", "const:4:8"]]
- 00ba5dd4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba6dc8 ["INT_ADD", "register:40f0:8", ["const:ba6dc8:8", "const:4:8"]]
+ 00ba6dc8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba5dd4 bytes d3c80294
+ 00ba6dc8 bytes cac80294
~~~


<a id="compare-63caca071f9f1ee4ae4a066a31ed8061"></a>

### [`00ba5e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5e48.md) → [`00ba6e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6e3c.md) FUN_00ba6e3c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ba5454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5454.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00ba6448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6448.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba5f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5e48.md#insn-00ba5f08) · [`00ba5f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba5/00ba5e48.md#insn-00ba5f34)
- 新版 [`00ba6efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6e3c.md#insn-00ba6efc) · [`00ba6f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba6/00ba6e3c.md#insn-00ba6f28)

~~~diff
- 00ba5f08 ["INT_ADD", "register:40f0:8", ["const:ba5f08:8", "const:4:8"]]
- 00ba5f08 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba6efc ["INT_ADD", "register:40f0:8", ["const:ba6efc:8", "const:4:8"]]
+ 00ba6efc ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba5f08 bytes 42c80294
+ 00ba6efc bytes 39c80294
- 00ba5f34 ["INT_ADD", "register:40f0:8", ["const:ba5f34:8", "const:4:8"]]
- 00ba5f34 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba6f28 ["INT_ADD", "register:40f0:8", ["const:ba6f28:8", "const:4:8"]]
+ 00ba6f28 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba5f34 bytes 37c80294
+ 00ba6f28 bytes 2ec80294
~~~


<a id="compare-0f1f30d7a26e330c609f0c6c04e1eef2"></a>

### [`00ba6010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6010.md) → [`00ba7004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7004.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEvT0

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc00.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc00.md) [`00c5cc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc90.md) [`00c5cd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd30.md)
- 新版 呼出元 1件 [`00c5dbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbd0.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbd0.md) [`00c5dc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc60.md) [`00c5dd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba60ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6010.md#insn-00ba60ac) · [`00ba6198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6010.md#insn-00ba6198) · [`00ba6200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6010.md#insn-00ba6200)
- 新版 [`00ba70a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7004.md#insn-00ba70a0) · [`00ba718c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7004.md#insn-00ba718c) · [`00ba71f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7004.md#insn-00ba71f4)

~~~diff
- 00ba60ac ["INT_ADD", "register:40f0:8", ["const:ba60ac:8", "const:4:8"]]
- 00ba60ac ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba70a0 ["INT_ADD", "register:40f0:8", ["const:ba70a0:8", "const:4:8"]]
+ 00ba70a0 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba60ac bytes 1dc80294
+ 00ba70a0 bytes 14c80294
- 00ba6198 ["INT_ADD", "register:40f0:8", ["const:ba6198:8", "const:4:8"]]
- 00ba6198 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba718c ["INT_ADD", "register:40f0:8", ["const:ba718c:8", "const:4:8"]]
+ 00ba718c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6198 bytes e2c70294
+ 00ba718c bytes d9c70294
- 00ba6200 ["INT_ADD", "register:40f0:8", ["const:ba6200:8", "const:4:8"]]
- 00ba6200 ["CALL", null, ["callee:00c5dbd0:8"]]
+ 00ba71f4 ["INT_ADD", "register:40f0:8", ["const:ba71f4:8", "const:4:8"]]
+ 00ba71f4 ["CALL", null, ["callee:00c5dbd0:8"]]
- 00ba6200 bytes 80da0294
+ 00ba71f4 bytes 77da0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b4ffeb7d128c8a76739ca9a0ae4dde"></a>

### [`00ba64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba64dc.md) → [`00ba74d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba74d0.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd30.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc00.md) [`00c5cdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdf0.md)
- 新版 呼出元 1件 [`00c5dd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd00.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dbd0.md) [`00c5ddc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba6590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba64dc.md#insn-00ba6590) · [`00ba6644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba64dc.md#insn-00ba6644) · [`00ba6660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba64dc.md#insn-00ba6660)
- 新版 [`00ba7584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba74d0.md#insn-00ba7584) · [`00ba7638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba74d0.md#insn-00ba7638) · [`00ba7654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba74d0.md#insn-00ba7654)

~~~diff
- 00ba6590 ["INT_ADD", "register:40f0:8", ["const:ba6590:8", "const:4:8"]]
- 00ba6590 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7584 ["INT_ADD", "register:40f0:8", ["const:ba7584:8", "const:4:8"]]
+ 00ba7584 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6590 bytes e4c60294
+ 00ba7584 bytes dbc60294
- 00ba6644 ["INT_ADD", "register:40f0:8", ["const:ba6644:8", "const:4:8"]]
- 00ba6644 ["CALL", null, ["callee:00c5dbd0:8"]]
+ 00ba7638 ["INT_ADD", "register:40f0:8", ["const:ba7638:8", "const:4:8"]]
+ 00ba7638 ["CALL", null, ["callee:00c5dbd0:8"]]
- 00ba6644 bytes 6fd90294
+ 00ba7638 bytes 66d90294
- 00ba6660 ["INT_ADD", "register:40f0:8", ["const:ba6660:8", "const:4:8"]]
- 00ba6660 ["CALL", null, ["callee:00c5dbd0:8"]]
+ 00ba7654 ["INT_ADD", "register:40f0:8", ["const:ba7654:8", "const:4:8"]]
+ 00ba7654 ["CALL", null, ["callee:00c5dbd0:8"]]
- 00ba6660 bytes 68d90294
+ 00ba7654 bytes 5fd90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d11c67d28749642153ea9004dcdb3aa8"></a>

### [`00ba6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6888.md) → [`00ba787c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba787c.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc90.md) · 呼出先 4件 [`00ba727c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba727c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc90.md) [`00c5ce50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce50.md)
- 新版 呼出元 1件 [`00c5dc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc60.md) · 呼出先 4件 [`00ba8270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8270.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc60.md) [`00c5de20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba6954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6888.md#insn-00ba6954) · [`00ba6a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6888.md#insn-00ba6a2c) · [`00ba6b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6888.md#insn-00ba6b18)
- 新版 [`00ba7948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba787c.md#insn-00ba7948) · [`00ba7a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba787c.md#insn-00ba7a20) · [`00ba7b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba787c.md#insn-00ba7b0c)

~~~diff
- 00ba6954 ["INT_ADD", "register:40f0:8", ["const:ba6954:8", "const:4:8"]]
- 00ba6954 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7948 ["INT_ADD", "register:40f0:8", ["const:ba7948:8", "const:4:8"]]
+ 00ba7948 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6954 bytes f3c50294
+ 00ba7948 bytes eac50294
- 00ba6a2c ["INT_ADD", "register:40f0:8", ["const:ba6a2c:8", "const:4:8"]]
- 00ba6a2c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7a20 ["INT_ADD", "register:40f0:8", ["const:ba7a20:8", "const:4:8"]]
+ 00ba7a20 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6a2c bytes bdc50294
+ 00ba7a20 bytes b4c50294
- 00ba6b18 ["INT_ADD", "register:40f0:8", ["const:ba6b18:8", "const:4:8"]]
- 00ba6b18 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7b0c ["INT_ADD", "register:40f0:8", ["const:ba7b0c:8", "const:4:8"]]
+ 00ba7b0c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6b18 bytes 82c50294
+ 00ba7b0c bytes 79c50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-356d235a3f3d98d037efadddf90b5b36"></a>

### [`00ba6cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6cb0.md) → [`00ba7ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7ca4.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdf0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ddc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5ddc0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba6d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6cb0.md#insn-00ba6d60) · [`00ba6de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6cb0.md#insn-00ba6de8)
- 新版 [`00ba7d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7ca4.md#insn-00ba7d54) · [`00ba7ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7ca4.md#insn-00ba7ddc)

~~~diff
- 00ba6d60 ["INT_ADD", "register:40f0:8", ["const:ba6d60:8", "const:4:8"]]
- 00ba6d60 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7d54 ["INT_ADD", "register:40f0:8", ["const:ba7d54:8", "const:4:8"]]
+ 00ba7d54 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6d60 bytes f0c40294
+ 00ba7d54 bytes e7c40294
- 00ba6de8 ["INT_ADD", "register:40f0:8", ["const:ba6de8:8", "const:4:8"]]
- 00ba6de8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7ddc ["INT_ADD", "register:40f0:8", ["const:ba7ddc:8", "const:4:8"]]
+ 00ba7ddc ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6de8 bytes cec40294
+ 00ba7ddc bytes c5c40294
~~~


<a id="compare-f4256addee21390e69a24133b120960c"></a>

### [`00ba6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6e68.md) → [`00ba7e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7e5c.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6Offset

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce50.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd90.md)
- 新版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de20.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba6ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6e68.md#insn-00ba6ff4) · [`00ba70e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6e68.md#insn-00ba70e4) · [`00ba7140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6e68.md#insn-00ba7140)
- 新版 [`00ba7fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7e5c.md#insn-00ba7fe8) · [`00ba80d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7e5c.md#insn-00ba80d8) · [`00ba8134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba7e5c.md#insn-00ba8134)

~~~diff
- 00ba6ff4 ["INT_ADD", "register:40f0:8", ["const:ba6ff4:8", "const:4:8"]]
- 00ba6ff4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba7fe8 ["INT_ADD", "register:40f0:8", ["const:ba7fe8:8", "const:4:8"]]
+ 00ba7fe8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba6ff4 bytes 4bc40294
+ 00ba7fe8 bytes 42c40294
- 00ba70e4 ["INT_ADD", "register:40f0:8", ["const:ba70e4:8", "const:4:8"]]
- 00ba70e4 ["CALL", null, ["callee:00c5dd60:8"]]
+ 00ba80d8 ["INT_ADD", "register:40f0:8", ["const:ba80d8:8", "const:4:8"]]
+ 00ba80d8 ["CALL", null, ["callee:00c5dd60:8"]]
- 00ba70e4 bytes 2bd70294
+ 00ba80d8 bytes 22d70294
- 00ba7140 ["INT_ADD", "register:40f0:8", ["const:ba7140:8", "const:4:8"]]
- 00ba7140 ["CALL", null, ["callee:00c58f80:8"]]
+ 00ba8134 ["INT_ADD", "register:40f0:8", ["const:ba8134:8", "const:4:8"]]
+ 00ba8134 ["CALL", null, ["callee:00c58f80:8"]]
- 00ba7140 bytes 9cc30294
+ 00ba8134 bytes 93c30294
~~~


<a id="compare-2c78665e604ff37dcb037eb58d4e27d5"></a>

### [`00ba7144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7144.md) → [`00ba8138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8138.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd90.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd60.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba7208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7144.md#insn-00ba7208)
- 新版 [`00ba81fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8138.md#insn-00ba81fc)

~~~diff
- 00ba7208 ["INT_ADD", "register:40f0:8", ["const:ba7208:8", "const:4:8"]]
- 00ba7208 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba81fc ["INT_ADD", "register:40f0:8", ["const:ba81fc:8", "const:4:8"]]
+ 00ba81fc ["CALL", null, ["callee:00c590f0:8"]]
- 00ba7208 bytes c6c30294
+ 00ba81fc bytes bdc30294
~~~


<a id="compare-d6c9579f5f93a202790349e62a5034b4"></a>

### [`00ba727c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba727c.md) → [`00ba8270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8270.md) FUN_00ba8270

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ba6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6888.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00ba787c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba7/00ba787c.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba733c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba727c.md#insn-00ba733c) · [`00ba7368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba727c.md#insn-00ba7368)
- 新版 [`00ba8330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8270.md#insn-00ba8330) · [`00ba835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8270.md#insn-00ba835c)

~~~diff
- 00ba733c ["INT_ADD", "register:40f0:8", ["const:ba733c:8", "const:4:8"]]
- 00ba733c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba8330 ["INT_ADD", "register:40f0:8", ["const:ba8330:8", "const:4:8"]]
+ 00ba8330 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba733c bytes 35c30294
+ 00ba8330 bytes 2cc30294
- 00ba7368 ["INT_ADD", "register:40f0:8", ["const:ba7368:8", "const:4:8"]]
- 00ba7368 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba835c ["INT_ADD", "register:40f0:8", ["const:ba835c:8", "const:4:8"]]
+ 00ba835c ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba7368 bytes 2ac30294
+ 00ba835c bytes 21c30294
~~~


<a id="compare-9a7c3ee974337124b350b0cb2e50e2e5"></a>

### [`00ba7444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7444.md) → [`00ba8438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8438.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbc0.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbc0.md) [`00c5cc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc50.md) [`00c5ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccf0.md)
- 新版 呼出元 1件 [`00c5db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db90.md) · 呼出先 4件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db90.md) [`00c5dc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc20.md) [`00c5dcc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba74e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7444.md#insn-00ba74e0) · [`00ba75cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7444.md#insn-00ba75cc) · [`00ba7634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7444.md#insn-00ba7634)
- 新版 [`00ba84d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8438.md#insn-00ba84d4) · [`00ba85c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8438.md#insn-00ba85c0) · [`00ba8628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8438.md#insn-00ba8628)

~~~diff
- 00ba74e0 ["INT_ADD", "register:40f0:8", ["const:ba74e0:8", "const:4:8"]]
- 00ba74e0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba84d4 ["INT_ADD", "register:40f0:8", ["const:ba84d4:8", "const:4:8"]]
+ 00ba84d4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba74e0 bytes 10c30294
+ 00ba84d4 bytes 07c30294
- 00ba75cc ["INT_ADD", "register:40f0:8", ["const:ba75cc:8", "const:4:8"]]
- 00ba75cc ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba85c0 ["INT_ADD", "register:40f0:8", ["const:ba85c0:8", "const:4:8"]]
+ 00ba85c0 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba75cc bytes d5c20294
+ 00ba85c0 bytes ccc20294
- 00ba7634 ["INT_ADD", "register:40f0:8", ["const:ba7634:8", "const:4:8"]]
- 00ba7634 ["CALL", null, ["callee:00c5db90:8"]]
+ 00ba8628 ["INT_ADD", "register:40f0:8", ["const:ba8628:8", "const:4:8"]]
+ 00ba8628 ["CALL", null, ["callee:00c5db90:8"]]
- 00ba7634 bytes 63d50294
+ 00ba8628 bytes 5ad50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede4c2ad581194edcd9ab31095063c40"></a>

### [`00ba7910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7910.md) → [`00ba8904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8904.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccf0.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbc0.md) [`00c5cdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 1件 [`00c5dcc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dcc0.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db90.md) [`00c5dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba79c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7910.md#insn-00ba79c4) · [`00ba7a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7910.md#insn-00ba7a78) · [`00ba7a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7910.md#insn-00ba7a94)
- 新版 [`00ba89b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8904.md#insn-00ba89b8) · [`00ba8a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8904.md#insn-00ba8a6c) · [`00ba8a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8904.md#insn-00ba8a88)

~~~diff
- 00ba79c4 ["INT_ADD", "register:40f0:8", ["const:ba79c4:8", "const:4:8"]]
- 00ba79c4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba89b8 ["INT_ADD", "register:40f0:8", ["const:ba89b8:8", "const:4:8"]]
+ 00ba89b8 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba79c4 bytes d7c10294
+ 00ba89b8 bytes cec10294
- 00ba7a78 ["INT_ADD", "register:40f0:8", ["const:ba7a78:8", "const:4:8"]]
- 00ba7a78 ["CALL", null, ["callee:00c5db90:8"]]
+ 00ba8a6c ["INT_ADD", "register:40f0:8", ["const:ba8a6c:8", "const:4:8"]]
+ 00ba8a6c ["CALL", null, ["callee:00c5db90:8"]]
- 00ba7a78 bytes 52d40294
+ 00ba8a6c bytes 49d40294
- 00ba7a94 ["INT_ADD", "register:40f0:8", ["const:ba7a94:8", "const:4:8"]]
- 00ba7a94 ["CALL", null, ["callee:00c5db90:8"]]
+ 00ba8a88 ["INT_ADD", "register:40f0:8", ["const:ba8a88:8", "const:4:8"]]
+ 00ba8a88 ["CALL", null, ["callee:00c5db90:8"]]
- 00ba7a94 bytes 4bd40294
+ 00ba8a88 bytes 42d40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c37b22c9d1b7abe79c9e7ac7988e7e4"></a>

### [`00ba7cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7cbc.md) → [`00ba8cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc50.md) · 呼出先 4件 [`00ba86b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba86b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc50.md) [`00c5ce10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce10.md)
- 新版 呼出元 1件 [`00c5dc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc20.md) · 呼出先 4件 [`00ba96a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba96a4.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc20.md) [`00c5dde0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dde0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba7d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7cbc.md#insn-00ba7d88) · [`00ba7e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7cbc.md#insn-00ba7e60) · [`00ba7f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7cbc.md#insn-00ba7f4c)
- 新版 [`00ba8d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md#insn-00ba8d7c) · [`00ba8e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md#insn-00ba8e54) · [`00ba8f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md#insn-00ba8f40)

~~~diff
- 00ba7d88 ["INT_ADD", "register:40f0:8", ["const:ba7d88:8", "const:4:8"]]
- 00ba7d88 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba8d7c ["INT_ADD", "register:40f0:8", ["const:ba8d7c:8", "const:4:8"]]
+ 00ba8d7c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba7d88 bytes e6c00294
+ 00ba8d7c bytes ddc00294
- 00ba7e60 ["INT_ADD", "register:40f0:8", ["const:ba7e60:8", "const:4:8"]]
- 00ba7e60 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba8e54 ["INT_ADD", "register:40f0:8", ["const:ba8e54:8", "const:4:8"]]
+ 00ba8e54 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba7e60 bytes b0c00294
+ 00ba8e54 bytes a7c00294
- 00ba7f4c ["INT_ADD", "register:40f0:8", ["const:ba7f4c:8", "const:4:8"]]
- 00ba7f4c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba8f40 ["INT_ADD", "register:40f0:8", ["const:ba8f40:8", "const:4:8"]]
+ 00ba8f40 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba7f4c bytes 75c00294
+ 00ba8f40 bytes 6cc00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63a25dcc3e6a4786b1f762e3e894c09"></a>

### [`00ba80e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba80e4.md) → [`00ba90d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba90d8.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6Offse

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cdb0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd80.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba80e4.md#insn-00ba8194) · [`00ba821c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba80e4.md#insn-00ba821c)
- 新版 [`00ba9188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba90d8.md#insn-00ba9188) · [`00ba9210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba90d8.md#insn-00ba9210)

~~~diff
- 00ba8194 ["INT_ADD", "register:40f0:8", ["const:ba8194:8", "const:4:8"]]
- 00ba8194 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9188 ["INT_ADD", "register:40f0:8", ["const:ba9188:8", "const:4:8"]]
+ 00ba9188 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8194 bytes e3bf0294
+ 00ba9188 bytes dabf0294
- 00ba821c ["INT_ADD", "register:40f0:8", ["const:ba821c:8", "const:4:8"]]
- 00ba821c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9210 ["INT_ADD", "register:40f0:8", ["const:ba9210:8", "const:4:8"]]
+ 00ba9210 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba821c bytes c1bf0294
+ 00ba9210 bytes b8bf0294
~~~


<a id="compare-abac5d99052d212ea364520be8920dfb"></a>

### [`00ba829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba829c.md) → [`00ba9290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9290.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6Of

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce10.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd50.md)
- 新版 呼出元 1件 [`00c5dde0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dde0.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5dd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba829c.md#insn-00ba8428) · [`00ba8518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba829c.md#insn-00ba8518) · [`00ba8574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba829c.md#insn-00ba8574)
- 新版 [`00ba941c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9290.md#insn-00ba941c) · [`00ba950c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9290.md#insn-00ba950c) · [`00ba9568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9290.md#insn-00ba9568)

~~~diff
- 00ba8428 ["INT_ADD", "register:40f0:8", ["const:ba8428:8", "const:4:8"]]
- 00ba8428 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba941c ["INT_ADD", "register:40f0:8", ["const:ba941c:8", "const:4:8"]]
+ 00ba941c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8428 bytes 3ebf0294
+ 00ba941c bytes 35bf0294
- 00ba8518 ["INT_ADD", "register:40f0:8", ["const:ba8518:8", "const:4:8"]]
- 00ba8518 ["CALL", null, ["callee:00c5dd20:8"]]
+ 00ba950c ["INT_ADD", "register:40f0:8", ["const:ba950c:8", "const:4:8"]]
+ 00ba950c ["CALL", null, ["callee:00c5dd20:8"]]
- 00ba8518 bytes 0ed20294
+ 00ba950c bytes 05d20294
- 00ba8574 ["INT_ADD", "register:40f0:8", ["const:ba8574:8", "const:4:8"]]
- 00ba8574 ["CALL", null, ["callee:00c58f80:8"]]
+ 00ba9568 ["INT_ADD", "register:40f0:8", ["const:ba9568:8", "const:4:8"]]
+ 00ba9568 ["CALL", null, ["callee:00c58f80:8"]]
- 00ba8574 bytes 8fbe0294
+ 00ba9568 bytes 86be0294
~~~


<a id="compare-f94e1e54e78db49d8723996877364a7a"></a>

### [`00ba8578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8578.md) → [`00ba956c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba956c.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetI

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd50.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dd20.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba863c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8578.md#insn-00ba863c)
- 新版 [`00ba9630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba956c.md#insn-00ba9630)

~~~diff
- 00ba863c ["INT_ADD", "register:40f0:8", ["const:ba863c:8", "const:4:8"]]
- 00ba863c ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9630 ["INT_ADD", "register:40f0:8", ["const:ba9630:8", "const:4:8"]]
+ 00ba9630 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba863c bytes b9be0294
+ 00ba9630 bytes b0be0294
~~~


<a id="compare-b73ca1b99401bb3ca75b54a9ecabce41"></a>

### [`00ba86b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba86b0.md) → [`00ba96a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba96a4.md) FUN_00ba96a4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ba7cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba7cbc.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00ba8cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba86b0.md#insn-00ba8770) · [`00ba879c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba86b0.md#insn-00ba879c)
- 新版 [`00ba9764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba96a4.md#insn-00ba9764) · [`00ba9790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba96a4.md#insn-00ba9790)

~~~diff
- 00ba8770 ["INT_ADD", "register:40f0:8", ["const:ba8770:8", "const:4:8"]]
- 00ba8770 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba9764 ["INT_ADD", "register:40f0:8", ["const:ba9764:8", "const:4:8"]]
+ 00ba9764 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba8770 bytes 28be0294
+ 00ba9764 bytes 1fbe0294
- 00ba879c ["INT_ADD", "register:40f0:8", ["const:ba879c:8", "const:4:8"]]
- 00ba879c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba9790 ["INT_ADD", "register:40f0:8", ["const:ba9790:8", "const:4:8"]]
+ 00ba9790 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba879c bytes 1dbe0294
+ 00ba9790 bytes 14be0294
~~~


<a id="compare-3c43f2676f5d3499275a7418ea36ea02"></a>

### [`00ba8878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8878.md) → [`00ba986c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba986c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE6FinishEjPKcb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c400.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)
- 新版 呼出元 1件 [`00c5d3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3d0.md) · 呼出先 2件 [`00c5d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d240.md) [`00c5d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8878.md#insn-00ba8904) · [`00ba8964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8878.md#insn-00ba8964) · [`00ba89c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8878.md#insn-00ba89c8)
- 新版 [`00ba98f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba986c.md#insn-00ba98f8) · [`00ba9958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba986c.md#insn-00ba9958) · [`00ba99bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba986c.md#insn-00ba99bc)

~~~diff
- 00ba8904 ["INT_ADD", "register:40f0:8", ["const:ba8904:8", "const:4:8"]]
- 00ba8904 ["CALL", null, ["callee:00c5d240:8"]]
+ 00ba98f8 ["INT_ADD", "register:40f0:8", ["const:ba98f8:8", "const:4:8"]]
+ 00ba98f8 ["CALL", null, ["callee:00c5d240:8"]]
- 00ba8904 bytes 5bce0294
+ 00ba98f8 bytes 52ce0294
- 00ba8964 ["INT_ADD", "register:40f0:8", ["const:ba8964:8", "const:4:8"]]
- 00ba8964 ["CALL", null, ["callee:00c5d240:8"]]
+ 00ba9958 ["INT_ADD", "register:40f0:8", ["const:ba9958:8", "const:4:8"]]
+ 00ba9958 ["CALL", null, ["callee:00c5d240:8"]]
- 00ba8964 bytes 43ce0294
+ 00ba9958 bytes 3ace0294
- 00ba89c8 ["INT_ADD", "register:40f0:8", ["const:ba89c8:8", "const:4:8"]]
- 00ba89c8 ["CALL", null, ["callee:00c5d240:8"]]
+ 00ba99bc ["INT_ADD", "register:40f0:8", ["const:ba99bc:8", "const:4:8"]]
+ 00ba99bc ["CALL", null, ["callee:00c5d240:8"]]
- 00ba89c8 bytes 2ace0294
+ 00ba99bc bytes 21ce0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa0d342b24f6fe25a55e19bd1fd4bc38"></a>

### [`00ba8a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8a48.md) → [`00ba9a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9a3c.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_co

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db10.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8a48.md#insn-00ba8ae0) · [`00ba8b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8a48.md#insn-00ba8b28)
- 新版 [`00ba9ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9a3c.md#insn-00ba9ad4) · [`00ba9b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9a3c.md#insn-00ba9b1c)

~~~diff
- 00ba8ae0 ["INT_ADD", "register:40f0:8", ["const:ba8ae0:8", "const:4:8"]]
- 00ba8ae0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9ad4 ["INT_ADD", "register:40f0:8", ["const:ba9ad4:8", "const:4:8"]]
+ 00ba9ad4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8ae0 bytes 90bd0294
+ 00ba9ad4 bytes 87bd0294
- 00ba8b28 ["INT_ADD", "register:40f0:8", ["const:ba8b28:8", "const:4:8"]]
- 00ba8b28 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9b1c ["INT_ADD", "register:40f0:8", ["const:ba9b1c:8", "const:4:8"]]
+ 00ba9b1c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8b28 bytes 7ebd0294
+ 00ba9b1c bytes 75bd0294
~~~


<a id="compare-e59700144b267c41f7ad2184a18f4591"></a>

### [`00ba8b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8b5c.md) → [`00ba9b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9b50.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) · 呼出先 3件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) · 呼出先 3件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8b5c.md#insn-00ba8b94) · [`00ba8be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8b5c.md#insn-00ba8be8) · [`00ba8c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8b5c.md#insn-00ba8c30)
- 新版 [`00ba9b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9b50.md#insn-00ba9b88) · [`00ba9bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9b50.md#insn-00ba9bdc) · [`00ba9c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9b50.md#insn-00ba9c24)

~~~diff
- 00ba8b94 ["INT_ADD", "register:40f0:8", ["const:ba8b94:8", "const:4:8"]]
- 00ba8b94 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00ba9b88 ["INT_ADD", "register:40f0:8", ["const:ba9b88:8", "const:4:8"]]
+ 00ba9b88 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00ba8b94 bytes 9fc90294
+ 00ba9b88 bytes 96c90294
- 00ba8be8 ["INT_ADD", "register:40f0:8", ["const:ba8be8:8", "const:4:8"]]
- 00ba8be8 ["CALL", null, ["callee:00c5c140:8"]]
+ 00ba9bdc ["INT_ADD", "register:40f0:8", ["const:ba9bdc:8", "const:4:8"]]
+ 00ba9bdc ["CALL", null, ["callee:00c5c140:8"]]
- 00ba8be8 bytes 62c90294
+ 00ba9bdc bytes 59c90294
- 00ba8c30 ["INT_ADD", "register:40f0:8", ["const:ba8c30:8", "const:4:8"]]
- 00ba8c30 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00ba9c24 ["INT_ADD", "register:40f0:8", ["const:ba9c24:8", "const:4:8"]]
+ 00ba9c24 ["CALL", null, ["callee:00c58fe0:8"]]
- 00ba8c30 bytes f8bc0294
+ 00ba9c24 bytes efbc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134ef890b4a04262c718459e5c5f9ec4"></a>

### [`00ba8c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8c7c.md) → [`00ba9c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9c70.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cba0.md) · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)
- 新版 呼出元 1件 [`00c5db70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db70.md) · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8c7c.md#insn-00ba8d78) · [`00ba8e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8c7c.md#insn-00ba8e3c) · [`00ba8ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8c7c.md#insn-00ba8ec4)
- 新版 [`00ba9d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9c70.md#insn-00ba9d6c) · [`00ba9e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9c70.md#insn-00ba9e30) · [`00ba9eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9c70.md#insn-00ba9eb8)

~~~diff
- 00ba8d78 ["INT_ADD", "register:40f0:8", ["const:ba8d78:8", "const:4:8"]]
- 00ba8d78 ["CALL", null, ["callee:00c5b980:8"]]
+ 00ba9d6c ["INT_ADD", "register:40f0:8", ["const:ba9d6c:8", "const:4:8"]]
+ 00ba9d6c ["CALL", null, ["callee:00c5b980:8"]]
- 00ba8d78 bytes 0ec70294
+ 00ba9d6c bytes 05c70294
- 00ba8e3c ["INT_ADD", "register:40f0:8", ["const:ba8e3c:8", "const:4:8"]]
- 00ba8e3c ["CALL", null, ["callee:00c58f30:8"]]
+ 00ba9e30 ["INT_ADD", "register:40f0:8", ["const:ba9e30:8", "const:4:8"]]
+ 00ba9e30 ["CALL", null, ["callee:00c58f30:8"]]
- 00ba8e3c bytes 49bc0294
+ 00ba9e30 bytes 40bc0294
- 00ba8ec4 ["INT_ADD", "register:40f0:8", ["const:ba8ec4:8", "const:4:8"]]
- 00ba8ec4 ["CALL", null, ["callee:00c59020:8"]]
+ 00ba9eb8 ["INT_ADD", "register:40f0:8", ["const:ba9eb8:8", "const:4:8"]]
+ 00ba9eb8 ["CALL", null, ["callee:00c59020:8"]]
- 00ba8ec4 bytes 63bc0294
+ 00ba9eb8 bytes 5abc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd12a62ea394262016cdd2a0016d96b2"></a>

### [`00ba8f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8f0c.md) → [`00ba9f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9f00.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb80.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5db50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5db50.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8f0c.md#insn-00ba8fa4) · [`00ba8fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba8/00ba8f0c.md#insn-00ba8fec)
- 新版 [`00ba9f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9f00.md#insn-00ba9f98) · [`00ba9fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba9/00ba9f00.md#insn-00ba9fe0)

~~~diff
- 00ba8fa4 ["INT_ADD", "register:40f0:8", ["const:ba8fa4:8", "const:4:8"]]
- 00ba8fa4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9f98 ["INT_ADD", "register:40f0:8", ["const:ba9f98:8", "const:4:8"]]
+ 00ba9f98 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8fa4 bytes 5fbc0294
+ 00ba9f98 bytes 56bc0294
- 00ba8fec ["INT_ADD", "register:40f0:8", ["const:ba8fec:8", "const:4:8"]]
- 00ba8fec ["CALL", null, ["callee:00c590f0:8"]]
+ 00ba9fe0 ["INT_ADD", "register:40f0:8", ["const:ba9fe0:8", "const:4:8"]]
+ 00ba9fe0 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba8fec bytes 4dbc0294
+ 00ba9fe0 bytes 44bc0294
~~~


<a id="compare-814df527ea3f8afb36ed252f67f234b6"></a>

### [`00ba9020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9020.md) → [`00baa014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa014.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d020.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dff0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba90b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9020.md#insn-00ba90b8) · [`00ba9100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9020.md#insn-00ba9100)
- 新版 [`00baa0ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa014.md#insn-00baa0ac) · [`00baa0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa014.md#insn-00baa0f4)

~~~diff
- 00ba90b8 ["INT_ADD", "register:40f0:8", ["const:ba90b8:8", "const:4:8"]]
- 00ba90b8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa0ac ["INT_ADD", "register:40f0:8", ["const:baa0ac:8", "const:4:8"]]
+ 00baa0ac ["CALL", null, ["callee:00c590f0:8"]]
- 00ba90b8 bytes 1abc0294
+ 00baa0ac bytes 11bc0294
- 00ba9100 ["INT_ADD", "register:40f0:8", ["const:ba9100:8", "const:4:8"]]
- 00ba9100 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa0f4 ["INT_ADD", "register:40f0:8", ["const:baa0f4:8", "const:4:8"]]
+ 00baa0f4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9100 bytes 08bc0294
+ 00baa0f4 bytes ffbb0294
~~~


<a id="compare-809bfd13955d543f5ebf1342c59193ec"></a>

### [`00ba9134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9134.md) → [`00baa128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa128.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d010.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dfe0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9134.md#insn-00ba91d0) · [`00ba9210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9134.md#insn-00ba9210)
- 新版 [`00baa1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa128.md#insn-00baa1c4) · [`00baa204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa128.md#insn-00baa204)

~~~diff
- 00ba91d0 ["INT_ADD", "register:40f0:8", ["const:ba91d0:8", "const:4:8"]]
- 00ba91d0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa1c4 ["INT_ADD", "register:40f0:8", ["const:baa1c4:8", "const:4:8"]]
+ 00baa1c4 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba91d0 bytes d4bb0294
+ 00baa1c4 bytes cbbb0294
- 00ba9210 ["INT_ADD", "register:40f0:8", ["const:ba9210:8", "const:4:8"]]
- 00ba9210 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa204 ["INT_ADD", "register:40f0:8", ["const:baa204:8", "const:4:8"]]
+ 00baa204 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9210 bytes c4bb0294
+ 00baa204 bytes bbbb0294
~~~


<a id="compare-bb569dfea8fb31fdebe38199c628e3b4"></a>

### [`00ba9254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9254.md) → [`00baa248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa248.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6assignIPS6_EENS_9enable_ifIXaasr21__is_forward_ite

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0d0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba92dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9254.md#insn-00ba92dc) · [`00ba9324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9254.md#insn-00ba9324) · [`00ba9374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9254.md#insn-00ba9374)
- 新版 [`00baa2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa248.md#insn-00baa2d0) · [`00baa318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa248.md#insn-00baa318) · [`00baa368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa248.md#insn-00baa368)

~~~diff
- 00ba92dc ["INT_ADD", "register:40f0:8", ["const:ba92dc:8", "const:4:8"]]
- 00ba92dc ["CALL", null, ["callee:00c58f50:8"]]
+ 00baa2d0 ["INT_ADD", "register:40f0:8", ["const:baa2d0:8", "const:4:8"]]
+ 00baa2d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00ba92dc bytes 29bb0294
+ 00baa2d0 bytes 20bb0294
- 00ba9324 ["INT_ADD", "register:40f0:8", ["const:ba9324:8", "const:4:8"]]
- 00ba9324 ["CALL", null, ["callee:00c5c650:8"]]
+ 00baa318 ["INT_ADD", "register:40f0:8", ["const:baa318:8", "const:4:8"]]
+ 00baa318 ["CALL", null, ["callee:00c5c650:8"]]
- 00ba9324 bytes d7c80294
+ 00baa318 bytes cec80294
- 00ba9374 ["INT_ADD", "register:40f0:8", ["const:ba9374:8", "const:4:8"]]
- 00ba9374 ["CALL", null, ["callee:00c5c150:8"]]
+ 00baa368 ["INT_ADD", "register:40f0:8", ["const:baa368:8", "const:4:8"]]
+ 00baa368 ["CALL", null, ["callee:00c5c150:8"]]
- 00ba9374 bytes 83c70294
+ 00baa368 bytes 7ac70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e333e5f39f6831e19c4a5cb9f9d23a7"></a>

### [`00ba9478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9478.md) → [`00baa46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa46c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf80.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df50.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9478.md#insn-00ba9510) · [`00ba9558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9478.md#insn-00ba9558)
- 新版 [`00baa504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa46c.md#insn-00baa504) · [`00baa54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa46c.md#insn-00baa54c)

~~~diff
- 00ba9510 ["INT_ADD", "register:40f0:8", ["const:ba9510:8", "const:4:8"]]
- 00ba9510 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa504 ["INT_ADD", "register:40f0:8", ["const:baa504:8", "const:4:8"]]
+ 00baa504 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9510 bytes 04bb0294
+ 00baa504 bytes fbba0294
- 00ba9558 ["INT_ADD", "register:40f0:8", ["const:ba9558:8", "const:4:8"]]
- 00ba9558 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa54c ["INT_ADD", "register:40f0:8", ["const:baa54c:8", "const:4:8"]]
+ 00baa54c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9558 bytes f2ba0294
+ 00baa54c bytes e9ba0294
~~~


<a id="compare-7751d34bd5ee8dfe293ba5324966d1df"></a>

### [`00ba958c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba958c.md) → [`00baa580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa580.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf70.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5df40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5df40.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba958c.md#insn-00ba9628) · [`00ba9668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba958c.md#insn-00ba9668)
- 新版 [`00baa61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa580.md#insn-00baa61c) · [`00baa65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa580.md#insn-00baa65c)

~~~diff
- 00ba9628 ["INT_ADD", "register:40f0:8", ["const:ba9628:8", "const:4:8"]]
- 00ba9628 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa61c ["INT_ADD", "register:40f0:8", ["const:baa61c:8", "const:4:8"]]
+ 00baa61c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9628 bytes beba0294
+ 00baa61c bytes b5ba0294
- 00ba9668 ["INT_ADD", "register:40f0:8", ["const:ba9668:8", "const:4:8"]]
- 00ba9668 ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa65c ["INT_ADD", "register:40f0:8", ["const:baa65c:8", "const:4:8"]]
+ 00baa65c ["CALL", null, ["callee:00c590f0:8"]]
- 00ba9668 bytes aeba0294
+ 00baa65c bytes a5ba0294
~~~


<a id="compare-c060a7344f39b6e1cb5775fe3f284370"></a>

### [`00ba96ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba96ac.md) → [`00baa6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa6a0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE18CreateSharedStringEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c380.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c370.md) [`00c5cf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf10.md)
- 新版 呼出元 1件 [`00c5d350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d350.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d340.md) [`00c5dee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba96ac.md#insn-00ba96f0) · [`00ba971c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba96ac.md#insn-00ba971c) · [`00ba977c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba96ac.md#insn-00ba977c)
- 新版 [`00baa6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa6a0.md#insn-00baa6e4) · [`00baa710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa6a0.md#insn-00baa710) · [`00baa770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baa6a0.md#insn-00baa770)

~~~diff
- 00ba96f0 ["INT_ADD", "register:40f0:8", ["const:ba96f0:8", "const:4:8"]]
- 00ba96f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00baa6e4 ["INT_ADD", "register:40f0:8", ["const:baa6e4:8", "const:4:8"]]
+ 00baa6e4 ["CALL", null, ["callee:00c58f30:8"]]
- 00ba96f0 bytes 1cba0294
+ 00baa6e4 bytes 13ba0294
- 00ba971c ["INT_ADD", "register:40f0:8", ["const:ba971c:8", "const:4:8"]]
- 00ba971c ["CALL", null, ["callee:00c5d340:8"]]
+ 00baa710 ["INT_ADD", "register:40f0:8", ["const:baa710:8", "const:4:8"]]
+ 00baa710 ["CALL", null, ["callee:00c5d340:8"]]
- 00ba971c bytes 15cb0294
+ 00baa710 bytes 0ccb0294
- 00ba977c ["INT_ADD", "register:40f0:8", ["const:ba977c:8", "const:4:8"]]
- 00ba977c ["CALL", null, ["callee:00c590f0:8"]]
+ 00baa770 ["INT_ADD", "register:40f0:8", ["const:baa770:8", "const:4:8"]]
+ 00baa770 ["CALL", null, ["callee:00c590f0:8"]]
- 00ba977c bytes 69ba0294
+ 00baa770 bytes 60ba0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

