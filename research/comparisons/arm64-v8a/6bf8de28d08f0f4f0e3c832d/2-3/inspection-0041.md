# v16.0.2 → v16.0.3 · 要調査の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-ad48c7b6e5acd2536b1e401a402c668e"></a>

### [`00c2b870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b870.md) → [`00c2c864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2c864.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b8e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2c8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2c8d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b870.md#insn-00c2b8bc)
- 新版 [`00c2c8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2c864.md#insn-00c2c8b0)

~~~diff
- 00c2b8bc ["INT_ADD", "register:40f0:8", ["const:c2b8bc:8", "const:4:8"]]
- 00c2b8bc ["CALL", null, ["callee:00c2c8d4:8"]]
+ 00c2c8b0 ["INT_ADD", "register:40f0:8", ["const:c2c8b0:8", "const:4:8"]]
+ 00c2c8b0 ["CALL", null, ["callee:00c2c8d4:8"]]
- 00c2b8bc bytes 09000094
+ 00c2c8b0 bytes 09000094
~~~


<a id="compare-ad118a09b8e5275dbd3f50969aafa978"></a>

### [`00c2bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bbd0.md) → [`00c2cbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cbc4.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d78.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c29/00c29d6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bbd0.md#insn-00c2bc1c)
- 新版 [`00c2cc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cbc4.md#insn-00c2cc10)

~~~diff
- 00c2bc1c ["INT_ADD", "register:40f0:8", ["const:c2bc1c:8", "const:4:8"]]
- 00c2bc1c ["CALL", null, ["callee:00c29d6c:8"]]
+ 00c2cc10 ["INT_ADD", "register:40f0:8", ["const:c2cc10:8", "const:4:8"]]
+ 00c2cc10 ["CALL", null, ["callee:00c29d6c:8"]]
- 00c2bc1c bytes 57f4ff97
+ 00c2cc10 bytes 57f4ff97
~~~


<a id="compare-8895a1c07f8b7756dd53b7351b91853a"></a>

### [`00c2bc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bc40.md) → [`00c2cc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cc34.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2903c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2a030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2a/00c2a030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bc40.md#insn-00c2bc8c)
- 新版 [`00c2cc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cc34.md#insn-00c2cc80)

~~~diff
- 00c2bc8c ["INT_ADD", "register:40f0:8", ["const:c2bc8c:8", "const:4:8"]]
- 00c2bc8c ["CALL", null, ["callee:00c2a030:8"]]
+ 00c2cc80 ["INT_ADD", "register:40f0:8", ["const:c2cc80:8", "const:4:8"]]
+ 00c2cc80 ["CALL", null, ["callee:00c2a030:8"]]
- 00c2bc8c bytes ecf4ff97
+ 00c2cc80 bytes ecf4ff97
~~~


<a id="compare-fd586ea2674129b90dc2edb49030edfa"></a>

### [`00c2bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd14.md) → [`00c2cd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cd08.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b648.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2c63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2c63c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd14.md#insn-00c2bd60)
- 新版 [`00c2cd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cd08.md#insn-00c2cd54)

~~~diff
- 00c2bd60 ["INT_ADD", "register:40f0:8", ["const:c2bd60:8", "const:4:8"]]
- 00c2bd60 ["CALL", null, ["callee:00c2c63c:8"]]
+ 00c2cd54 ["INT_ADD", "register:40f0:8", ["const:c2cd54:8", "const:4:8"]]
+ 00c2cd54 ["CALL", null, ["callee:00c2c63c:8"]]
- 00c2bd60 bytes 3afeff97
+ 00c2cd54 bytes 3afeff97
~~~


<a id="compare-f72d34244dec0b5d3815dfe09cf21a6f"></a>

### [`00c2bd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd84.md) → [`00c2cd78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cd78.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b8e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2c8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2c8d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd84.md#insn-00c2bdd0)
- 新版 [`00c2cdc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cd78.md#insn-00c2cdc4)

~~~diff
- 00c2bdd0 ["INT_ADD", "register:40f0:8", ["const:c2bdd0:8", "const:4:8"]]
- 00c2bdd0 ["CALL", null, ["callee:00c2c8d4:8"]]
+ 00c2cdc4 ["INT_ADD", "register:40f0:8", ["const:c2cdc4:8", "const:4:8"]]
+ 00c2cdc4 ["CALL", null, ["callee:00c2c8d4:8"]]
- 00c2bdd0 bytes c4feff97
+ 00c2cdc4 bytes c4feff97
~~~


<a id="compare-ddcd66b8c3f5e7d47cd7cbe20b58ce5c"></a>

### [`00c2be58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be58.md) → [`00c2ce4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ce4c.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eca0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be58.md#insn-00c2be6c)
- 新版 [`00c2ce60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ce4c.md#insn-00c2ce60)

~~~diff
- 00c2be6c ["INT_ADD", "register:40f0:8", ["const:c2be6c:8", "const:4:8"]]
- 00c2be6c ["CALL", null, ["callee:00c5fc70:8"]]
+ 00c2ce60 ["INT_ADD", "register:40f0:8", ["const:c2ce60:8", "const:4:8"]]
+ 00c2ce60 ["CALL", null, ["callee:00c5fc70:8"]]
- 00c2be6c bytes 8dcb0094
+ 00c2ce60 bytes 84cb0094
~~~


<a id="compare-5f64d25a3c93b6c5fc42864a94a0fa81"></a>

### [`00c2be84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be84.md) → [`00c2ce78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ce78.md) _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fc80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2be98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be84.md#insn-00c2be98)
- 新版 [`00c2ce8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ce78.md#insn-00c2ce8c)

~~~diff
- 00c2be98 ["INT_ADD", "register:40f0:8", ["const:c2be98:8", "const:4:8"]]
- 00c2be98 ["CALL", null, ["callee:00c5fc80:8"]]
+ 00c2ce8c ["INT_ADD", "register:40f0:8", ["const:c2ce8c:8", "const:4:8"]]
+ 00c2ce8c ["CALL", null, ["callee:00c5fc80:8"]]
- 00c2be98 bytes 86cb0094
+ 00c2ce8c bytes 7dcb0094
~~~


<a id="compare-5ddbb057ad3a8e6a897602ca56334a30"></a>

### [`00c2beb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2beb0.md) → [`00c2cea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cea4.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fc90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2beb0.md#insn-00c2bec4)
- 新版 [`00c2ceb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cea4.md#insn-00c2ceb8)

~~~diff
- 00c2bec4 ["INT_ADD", "register:40f0:8", ["const:c2bec4:8", "const:4:8"]]
- 00c2bec4 ["CALL", null, ["callee:00c5fc90:8"]]
+ 00c2ceb8 ["INT_ADD", "register:40f0:8", ["const:c2ceb8:8", "const:4:8"]]
+ 00c2ceb8 ["CALL", null, ["callee:00c5fc90:8"]]
- 00c2bec4 bytes 7fcb0094
+ 00c2ceb8 bytes 76cb0094
~~~


<a id="compare-3b545e5f5106e2a5c7148d7f8eb9c19b"></a>

### [`00c2bedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bedc.md) → [`00c2ced0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ced0.md) _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bedc.md#insn-00c2bef0)
- 新版 [`00c2cee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2ced0.md#insn-00c2cee4)

~~~diff
- 00c2bef0 ["INT_ADD", "register:40f0:8", ["const:c2bef0:8", "const:4:8"]]
- 00c2bef0 ["CALL", null, ["callee:00c5fca0:8"]]
+ 00c2cee4 ["INT_ADD", "register:40f0:8", ["const:c2cee4:8", "const:4:8"]]
+ 00c2cee4 ["CALL", null, ["callee:00c5fca0:8"]]
- 00c2bef0 bytes 78cb0094
+ 00c2cee4 bytes 6fcb0094
~~~


<a id="compare-aac71302ebcf713ec06648d3ab3f1a4c"></a>

### [`00c2bfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bfb4.md) → [`00c2cfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cfa8.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fcc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fcc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bfb4.md#insn-00c2bfc8)
- 新版 [`00c2cfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cfa8.md#insn-00c2cfbc)

~~~diff
- 00c2bfc8 ["INT_ADD", "register:40f0:8", ["const:c2bfc8:8", "const:4:8"]]
- 00c2bfc8 ["CALL", null, ["callee:00c5fcc0:8"]]
+ 00c2cfbc ["INT_ADD", "register:40f0:8", ["const:c2cfbc:8", "const:4:8"]]
+ 00c2cfbc ["CALL", null, ["callee:00c5fcc0:8"]]
- 00c2bfc8 bytes 4acb0094
+ 00c2cfbc bytes 41cb0094
~~~


<a id="compare-89d290bc6c5f10fbf743b1ac31716a4e"></a>

### [`00c2c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c030.md) → [`00c2d024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d024.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c030.md#insn-00c2c044)
- 新版 [`00c2d038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d024.md#insn-00c2d038)

~~~diff
- 00c2c044 ["INT_ADD", "register:40f0:8", ["const:c2c044:8", "const:4:8"]]
- 00c2c044 ["CALL", null, ["callee:00c5fce0:8"]]
+ 00c2d038 ["INT_ADD", "register:40f0:8", ["const:c2d038:8", "const:4:8"]]
+ 00c2d038 ["CALL", null, ["callee:00c5fce0:8"]]
- 00c2c044 bytes 33cb0094
+ 00c2d038 bytes 2acb0094
~~~


<a id="compare-fc4d68ceebe59cc26ba74b79800d2839"></a>

### [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) → [`00c2d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md) FUN_00c2d124

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c2e2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md) [`00c2e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md) [`00c2e50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md) [`00c2e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)
- 新版 呼出元 4件 [`00c2f2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f2e8.md) [`00c2f3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f3f4.md) [`00c2f500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f500.md) [`00c2f60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f60c.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md#insn-00c2c150) · [`00c2c1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md#insn-00c2c1a4) · [`00c2c1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md#insn-00c2c1c4)
- 新版 [`00c2d144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md#insn-00c2d144) · [`00c2d198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md#insn-00c2d198) · [`00c2d1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md#insn-00c2d1b8)

~~~diff
- 00c2c150 ["INT_ADD", "register:40f0:8", ["const:c2c150:8", "const:4:8"]]
- 00c2c150 ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00c2d144 ["INT_ADD", "register:40f0:8", ["const:c2d144:8", "const:4:8"]]
+ 00c2d144 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00c2c150 bytes e0c70094
+ 00c2d144 bytes d7c70094
- 00c2c1a4 ["INT_ADD", "register:40f0:8", ["const:c2c1a4:8", "const:4:8"]]
- 00c2c1a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c2d198 ["INT_ADD", "register:40f0:8", ["const:c2d198:8", "const:4:8"]]
+ 00c2d198 ["CALL", null, ["callee:00c58f30:8"]]
- 00c2c1a4 bytes 6faf0094
+ 00c2d198 bytes 66af0094
- 00c2c1c4 ["INT_ADD", "register:40f0:8", ["const:c2c1c4:8", "const:4:8"]]
- 00c2c1c4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c2d1b8 ["INT_ADD", "register:40f0:8", ["const:c2d1b8:8", "const:4:8"]]
+ 00c2d1b8 ["CALL", null, ["callee:00c58fe0:8"]]
- 00c2c1c4 bytes 93af0094
+ 00c2d1b8 bytes 8aaf0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866b4d17685969b8fff598a129696c35"></a>

### [`00c2c608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c608.md) → [`00c2d5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d5fc.md) _ZNSt6__ndk115numpunct_bynameIcED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c608.md#insn-00c2c61c)
- 新版 [`00c2d610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d5fc.md#insn-00c2d610)

~~~diff
- 00c2c61c ["INT_ADD", "register:40f0:8", ["const:c2c61c:8", "const:4:8"]]
- 00c2c61c ["CALL", null, ["callee:00c5fd10:8"]]
+ 00c2d610 ["INT_ADD", "register:40f0:8", ["const:c2d610:8", "const:4:8"]]
+ 00c2d610 ["CALL", null, ["callee:00c5fd10:8"]]
- 00c2c61c bytes c9c90094
+ 00c2d610 bytes c0c90094
~~~


<a id="compare-7aaca095aff35e6c129433028ae665bf"></a>

### [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md) → [`00c2d628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d628.md) FUN_00c2d628

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) [`00c3381c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md) [`00c34518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md) · 呼出先 1件 [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 3件 [`00c2d6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md) [`00c34810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34810.md) [`00c3550c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c3550c.md) · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md#insn-00c2c648)
- 新版 [`00c2d63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d628.md#insn-00c2d63c)

~~~diff
- 00c2c648 ["INT_ADD", "register:40f0:8", ["const:c2c648:8", "const:4:8"]]
- 00c2c648 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c2d63c ["INT_ADD", "register:40f0:8", ["const:c2d63c:8", "const:4:8"]]
+ 00c2d63c ["CALL", null, ["callee:00c5e270:8"]]
- 00c2c648 bytes 16c30094
+ 00c2d63c bytes 0dc30094
~~~


<a id="compare-0a55d8383ae93c54a852dea588a04562"></a>

### [`00c2c940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c940.md) → [`00c2d934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d934.md) _ZNSt6__ndk115numpunct_bynameIwED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c940.md#insn-00c2c954)
- 新版 [`00c2d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d934.md#insn-00c2d948)

~~~diff
- 00c2c954 ["INT_ADD", "register:40f0:8", ["const:c2c954:8", "const:4:8"]]
- 00c2c954 ["CALL", null, ["callee:00c5fd30:8"]]
+ 00c2d948 ["INT_ADD", "register:40f0:8", ["const:c2d948:8", "const:4:8"]]
+ 00c2d948 ["CALL", null, ["callee:00c5fd30:8"]]
- 00c2c954 bytes 03c90094
+ 00c2d948 bytes fac80094
~~~


<a id="compare-709a66f2a8560bda6f7414af5feb5f72"></a>

### [`00c2e81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e81c.md) → [`00c2f810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f810.md) _ZNSt6__ndk110__time_getD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed90.md) · 呼出先 1件 [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 1件 [`00c5fd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd60.md) · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2e82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e81c.md#insn-00c2e82c)
- 新版 [`00c2f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f810.md#insn-00c2f820)

~~~diff
- 00c2e82c ["INT_ADD", "register:40f0:8", ["const:c2e82c:8", "const:4:8"]]
- 00c2e82c ["CALL", null, ["callee:00c5e270:8"]]
+ 00c2f820 ["INT_ADD", "register:40f0:8", ["const:c2f820:8", "const:4:8"]]
+ 00c2f820 ["CALL", null, ["callee:00c5e270:8"]]
- 00c2e82c bytes 9dba0094
+ 00c2f820 bytes 94ba0094
~~~


<a id="compare-7f8d2a0856246631c344a6ce2007e7fa"></a>

### [`00c2ee28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md) → [`00c2fe1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2fe1c.md) FUN_00c2fe1c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)
- 新版 呼出元 1件 [`00c2f834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f834.md) · 呼出先 3件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2ee88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md#insn-00c2ee88) · [`00c2ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md#insn-00c2ee98) · [`00c2ef2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md#insn-00c2ef2c)
- 新版 [`00c2fe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2fe1c.md#insn-00c2fe7c) · [`00c2fe8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2fe1c.md#insn-00c2fe8c) · [`00c2ff20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2fe1c.md#insn-00c2ff20)

~~~diff
- 00c2ee88 ["INT_ADD", "register:40f0:8", ["const:c2ee88:8", "const:4:8"]]
- 00c2ee88 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c2fe7c ["INT_ADD", "register:40f0:8", ["const:c2fe7c:8", "const:4:8"]]
+ 00c2fe7c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c2ee88 bytes 9aac0094
+ 00c2fe7c bytes 91ac0094
- 00c2ee98 ["INT_ADD", "register:40f0:8", ["const:c2ee98:8", "const:4:8"]]
- 00c2ee98 ["CALL", null, ["callee:00c5f020:8"]]
+ 00c2fe8c ["INT_ADD", "register:40f0:8", ["const:c2fe8c:8", "const:4:8"]]
+ 00c2fe8c ["CALL", null, ["callee:00c5f020:8"]]
- 00c2ee98 bytes 6ebc0094
+ 00c2fe8c bytes 65bc0094
- 00c2ef2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c2ef2c ["INT_ADD", "register:40f0:8", ["const:c2ef2c:8", "const:4:8"]]
- 00c2ef2c ["CALLIND", null, ["register:0:8"]]
+ 00c2ff20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c2ff20 ["INT_ADD", "register:40f0:8", ["const:c2ff20:8", "const:4:8"]]
+ 00c2ff20 ["CALLIND", null, ["register:0:8"]]
- 00c2ef2c bytes 00013fd6
+ 00c2ff20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d8cac010684866a74ab1e4742571ce5"></a>

### [`00c307e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md) → [`00c317d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c317d4.md) FUN_00c317d4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)
- 新版 呼出元 1件 [`00c3012c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c30/00c3012c.md) · 呼出先 3件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c30840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md#insn-00c30840) · [`00c30850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md#insn-00c30850) · [`00c308f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md#insn-00c308f8)
- 新版 [`00c31834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c317d4.md#insn-00c31834) · [`00c31844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c317d4.md#insn-00c31844) · [`00c318ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c317d4.md#insn-00c318ec)

~~~diff
- 00c30840 ["INT_ADD", "register:40f0:8", ["const:c30840:8", "const:4:8"]]
- 00c30840 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c31834 ["INT_ADD", "register:40f0:8", ["const:c31834:8", "const:4:8"]]
+ 00c31834 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c30840 bytes 2ca60094
+ 00c31834 bytes 23a60094
- 00c30850 ["INT_ADD", "register:40f0:8", ["const:c30850:8", "const:4:8"]]
- 00c30850 ["CALL", null, ["callee:00c5f020:8"]]
+ 00c31844 ["INT_ADD", "register:40f0:8", ["const:c31844:8", "const:4:8"]]
+ 00c31844 ["CALL", null, ["callee:00c5f020:8"]]
- 00c30850 bytes 00b60094
+ 00c31844 bytes f7b50094
- 00c308f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c308f8 ["INT_ADD", "register:40f0:8", ["const:c308f8:8", "const:4:8"]]
- 00c308f8 ["CALLIND", null, ["register:0:8"]]
+ 00c318ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c318ec ["INT_ADD", "register:40f0:8", ["const:c318ec:8", "const:4:8"]]
+ 00c318ec ["CALLIND", null, ["register:0:8"]]
- 00c308f8 bytes 00013fd6
+ 00c318ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79f56f87fb8adb2aa0d5f46e8fbacd31"></a>

### [`00c34ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ccc.md) → [`00c35cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35cc0.md) FUN_00c35cc0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ccc.md#insn-00c34ce0)
- 新版 [`00c35cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35cc0.md#insn-00c35cd4)

~~~diff
- 00c34ce0 ["INT_ADD", "register:40f0:8", ["const:c34ce0:8", "const:4:8"]]
- 00c34ce0 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c35cd4 ["INT_ADD", "register:40f0:8", ["const:c35cd4:8", "const:4:8"]]
+ 00c35cd4 ["CALL", null, ["callee:00c5b920:8"]]
- 00c34ce0 bytes 1c970094
+ 00c35cd4 bytes 13970094
~~~


<a id="compare-12e08a6b57df29b873fb60ab5a76e066"></a>

### [`00c34cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34cf8.md) → [`00c35cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35cec.md) FUN_00c35cec

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34cf8.md#insn-00c34d0c)
- 新版 [`00c35d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35cec.md#insn-00c35d00)

~~~diff
- 00c34d0c ["INT_ADD", "register:40f0:8", ["const:c34d0c:8", "const:4:8"]]
- 00c34d0c ["CALL", null, ["callee:00c5f800:8"]]
+ 00c35d00 ["INT_ADD", "register:40f0:8", ["const:c35d00:8", "const:4:8"]]
+ 00c35d00 ["CALL", null, ["callee:00c5f800:8"]]
- 00c34d0c bytes c9a60094
+ 00c35d00 bytes c0a60094
~~~


<a id="compare-a644c7dab37cc98321d4169be7cb8f13"></a>

### [`00c34d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d24.md) → [`00c35d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d18.md) FUN_00c35d18

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d24.md#insn-00c34d38)
- 新版 [`00c35d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d18.md#insn-00c35d2c)

~~~diff
- 00c34d38 ["INT_ADD", "register:40f0:8", ["const:c34d38:8", "const:4:8"]]
- 00c34d38 ["CALL", null, ["callee:00c5f820:8"]]
+ 00c35d2c ["INT_ADD", "register:40f0:8", ["const:c35d2c:8", "const:4:8"]]
+ 00c35d2c ["CALL", null, ["callee:00c5f820:8"]]
- 00c34d38 bytes c6a60094
+ 00c35d2c bytes bda60094
~~~


<a id="compare-b84c8d0b812eeb4e524b92412f1aaca9"></a>

### [`00c34d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d50.md) → [`00c35d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d44.md) FUN_00c35d44

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d50.md#insn-00c34d64)
- 新版 [`00c35d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d44.md#insn-00c35d58)

~~~diff
- 00c34d64 ["INT_ADD", "register:40f0:8", ["const:c34d64:8", "const:4:8"]]
- 00c34d64 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c35d58 ["INT_ADD", "register:40f0:8", ["const:c35d58:8", "const:4:8"]]
+ 00c35d58 ["CALL", null, ["callee:00c5b920:8"]]
- 00c34d64 bytes fb960094
+ 00c35d58 bytes f2960094
~~~


<a id="compare-ae079569fd338fe38f8fcd60455c033b"></a>

### [`00c34d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d7c.md) → [`00c35d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d70.md) FUN_00c35d70

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d7c.md#insn-00c34d90)
- 新版 [`00c35d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d70.md#insn-00c35d84)

~~~diff
- 00c34d90 ["INT_ADD", "register:40f0:8", ["const:c34d90:8", "const:4:8"]]
- 00c34d90 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c35d84 ["INT_ADD", "register:40f0:8", ["const:c35d84:8", "const:4:8"]]
+ 00c35d84 ["CALL", null, ["callee:00c5b920:8"]]
- 00c34d90 bytes f0960094
+ 00c35d84 bytes e7960094
~~~


<a id="compare-4d5029755fe0aad9105972c45185aef3"></a>

### [`00c34da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34da8.md) → [`00c35d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d9c.md) FUN_00c35d9c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34da8.md#insn-00c34dbc)
- 新版 [`00c35db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35d9c.md#insn-00c35db0)

~~~diff
- 00c34dbc ["INT_ADD", "register:40f0:8", ["const:c34dbc:8", "const:4:8"]]
- 00c34dbc ["CALL", null, ["callee:00c5f800:8"]]
+ 00c35db0 ["INT_ADD", "register:40f0:8", ["const:c35db0:8", "const:4:8"]]
+ 00c35db0 ["CALL", null, ["callee:00c5f800:8"]]
- 00c34dbc bytes 9da60094
+ 00c35db0 bytes 94a60094
~~~


<a id="compare-c5895da195f96289248e47ba96f67a66"></a>

### [`00c34dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34dd4.md) → [`00c35dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35dc8.md) FUN_00c35dc8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34dd4.md#insn-00c34de8)
- 新版 [`00c35ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35dc8.md#insn-00c35ddc)

~~~diff
- 00c34de8 ["INT_ADD", "register:40f0:8", ["const:c34de8:8", "const:4:8"]]
- 00c34de8 ["CALL", null, ["callee:00c5f800:8"]]
+ 00c35ddc ["INT_ADD", "register:40f0:8", ["const:c35ddc:8", "const:4:8"]]
+ 00c35ddc ["CALL", null, ["callee:00c5f800:8"]]
- 00c34de8 bytes 92a60094
+ 00c35ddc bytes 89a60094
~~~


<a id="compare-14eb4cf5d082c5e03b5960097dec1ea6"></a>

### [`00c34e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e00.md) → [`00c35df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35df4.md) FUN_00c35df4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e00.md#insn-00c34e14)
- 新版 [`00c35e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35df4.md#insn-00c35e08)

~~~diff
- 00c34e14 ["INT_ADD", "register:40f0:8", ["const:c34e14:8", "const:4:8"]]
- 00c34e14 ["CALL", null, ["callee:00c5f820:8"]]
+ 00c35e08 ["INT_ADD", "register:40f0:8", ["const:c35e08:8", "const:4:8"]]
+ 00c35e08 ["CALL", null, ["callee:00c5f820:8"]]
- 00c34e14 bytes 8fa60094
+ 00c35e08 bytes 86a60094
~~~


<a id="compare-b8b1ad23c0a890768a23b07fc29057f1"></a>

### [`00c34e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e2c.md) → [`00c35e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e20.md) FUN_00c35e20

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e2c.md#insn-00c34e40)
- 新版 [`00c35e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e20.md#insn-00c35e34)

~~~diff
- 00c34e40 ["INT_ADD", "register:40f0:8", ["const:c34e40:8", "const:4:8"]]
- 00c34e40 ["CALL", null, ["callee:00c5f820:8"]]
+ 00c35e34 ["INT_ADD", "register:40f0:8", ["const:c35e34:8", "const:4:8"]]
+ 00c35e34 ["CALL", null, ["callee:00c5f820:8"]]
- 00c34e40 bytes 84a60094
+ 00c35e34 bytes 7ba60094
~~~


<a id="compare-c2db3d172b94e4022bb9443fdd097df5"></a>

### [`00c34f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f18.md) → [`00c35f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f0c.md) FUN_00c35f0c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f18.md#insn-00c34f2c)
- 新版 [`00c35f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f0c.md#insn-00c35f20)

~~~diff
- 00c34f2c ["INT_ADD", "register:40f0:8", ["const:c34f2c:8", "const:4:8"]]
- 00c34f2c ["CALL", null, ["callee:00c5b920:8"]]
+ 00c35f20 ["INT_ADD", "register:40f0:8", ["const:c35f20:8", "const:4:8"]]
+ 00c35f20 ["CALL", null, ["callee:00c5b920:8"]]
- 00c34f2c bytes 89960094
+ 00c35f20 bytes 80960094
~~~


<a id="compare-ac233a41ee5fecde7a06a65db03564f4"></a>

### [`00c34f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f44.md) → [`00c35f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f38.md) FUN_00c35f38

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f44.md#insn-00c34f58)
- 新版 [`00c35f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f38.md#insn-00c35f4c)

~~~diff
- 00c34f58 ["INT_ADD", "register:40f0:8", ["const:c34f58:8", "const:4:8"]]
- 00c34f58 ["CALL", null, ["callee:00c5f820:8"]]
+ 00c35f4c ["INT_ADD", "register:40f0:8", ["const:c35f4c:8", "const:4:8"]]
+ 00c35f4c ["CALL", null, ["callee:00c5f820:8"]]
- 00c34f58 bytes 3ea60094
+ 00c35f4c bytes 35a60094
~~~


<a id="compare-df5bd0b2aff79b7a2e591d1db1c15afa"></a>

### [`00c34f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f70.md) → [`00c35f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f64.md) FUN_00c35f64

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f70.md#insn-00c34f84)
- 新版 [`00c35f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f64.md#insn-00c35f78)

~~~diff
- 00c34f84 ["INT_ADD", "register:40f0:8", ["const:c34f84:8", "const:4:8"]]
- 00c34f84 ["CALL", null, ["callee:00c5f800:8"]]
+ 00c35f78 ["INT_ADD", "register:40f0:8", ["const:c35f78:8", "const:4:8"]]
+ 00c35f78 ["CALL", null, ["callee:00c5f800:8"]]
- 00c34f84 bytes 2ba60094
+ 00c35f78 bytes 22a60094
~~~


<a id="compare-60cd6aee2642e532530a6a7b6b164775"></a>

### [`00c34f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f9c.md) → [`00c35f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f90.md) FUN_00c35f90

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f9c.md#insn-00c34fb0)
- 新版 [`00c35fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35f90.md#insn-00c35fa4)

~~~diff
- 00c34fb0 ["INT_ADD", "register:40f0:8", ["const:c34fb0:8", "const:4:8"]]
- 00c34fb0 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c35fa4 ["INT_ADD", "register:40f0:8", ["const:c35fa4:8", "const:4:8"]]
+ 00c35fa4 ["CALL", null, ["callee:00c593a0:8"]]
- 00c34fb0 bytes 088d0094
+ 00c35fa4 bytes ff8c0094
~~~


<a id="compare-c718f68aca3b8ebaf0db3490efc8c2ed"></a>

### [`00c34fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34fc8.md) → [`00c35fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35fbc.md) FUN_00c35fbc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34fc8.md#insn-00c34fdc)
- 新版 [`00c35fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35fbc.md#insn-00c35fd0)

~~~diff
- 00c34fdc ["INT_ADD", "register:40f0:8", ["const:c34fdc:8", "const:4:8"]]
- 00c34fdc ["CALL", null, ["callee:00c593a0:8"]]
+ 00c35fd0 ["INT_ADD", "register:40f0:8", ["const:c35fd0:8", "const:4:8"]]
+ 00c35fd0 ["CALL", null, ["callee:00c593a0:8"]]
- 00c34fdc bytes fd8c0094
+ 00c35fd0 bytes f48c0094
~~~


<a id="compare-2229e3c114f9988c64e8f83e3d85ce68"></a>

### [`00c34ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ff4.md) → [`00c35fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35fe8.md) FUN_00c35fe8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ff4.md#insn-00c35008)
- 新版 [`00c35ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35fe8.md#insn-00c35ffc)

~~~diff
- 00c35008 ["INT_ADD", "register:40f0:8", ["const:c35008:8", "const:4:8"]]
- 00c35008 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c35ffc ["INT_ADD", "register:40f0:8", ["const:c35ffc:8", "const:4:8"]]
+ 00c35ffc ["CALL", null, ["callee:00c593a0:8"]]
- 00c35008 bytes f28c0094
+ 00c35ffc bytes e98c0094
~~~


<a id="compare-9ba595560572215bea4eb5ec83705f9c"></a>

### [`00c35020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35020.md) → [`00c36014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36014.md) FUN_00c36014

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35020.md#insn-00c35034)
- 新版 [`00c36028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36014.md#insn-00c36028)

~~~diff
- 00c35034 ["INT_ADD", "register:40f0:8", ["const:c35034:8", "const:4:8"]]
- 00c35034 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36028 ["INT_ADD", "register:40f0:8", ["const:c36028:8", "const:4:8"]]
+ 00c36028 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35034 bytes e78c0094
+ 00c36028 bytes de8c0094
~~~


<a id="compare-4c27ac0eb4b874dc28ac5373f79ea3d2"></a>

### [`00c35054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35054.md) → [`00c36048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36048.md) FUN_00c36048

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35054.md#insn-00c35068)
- 新版 [`00c3605c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36048.md#insn-00c3605c)

~~~diff
- 00c35068 ["INT_ADD", "register:40f0:8", ["const:c35068:8", "const:4:8"]]
- 00c35068 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c3605c ["INT_ADD", "register:40f0:8", ["const:c3605c:8", "const:4:8"]]
+ 00c3605c ["CALL", null, ["callee:00c593a0:8"]]
- 00c35068 bytes da8c0094
+ 00c3605c bytes d18c0094
~~~


<a id="compare-9e2edd2efe6d5bae49883afc7a790e7a"></a>

### [`00c35088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35088.md) → [`00c3607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3607c.md) FUN_00c3607c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3509c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35088.md#insn-00c3509c)
- 新版 [`00c36090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3607c.md#insn-00c36090)

~~~diff
- 00c3509c ["INT_ADD", "register:40f0:8", ["const:c3509c:8", "const:4:8"]]
- 00c3509c ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36090 ["INT_ADD", "register:40f0:8", ["const:c36090:8", "const:4:8"]]
+ 00c36090 ["CALL", null, ["callee:00c593a0:8"]]
- 00c3509c bytes cd8c0094
+ 00c36090 bytes c48c0094
~~~


<a id="compare-c7ec91fdbc9925a2081a081162ef1d4d"></a>

### [`00c350b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350b4.md) → [`00c360a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360a8.md) FUN_00c360a8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c37cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c350cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350b4.md#insn-00c350cc)
- 新版 [`00c360c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360a8.md#insn-00c360c0)

~~~diff
- 00c350cc ["INT_ADD", "register:40f0:8", ["const:c350cc:8", "const:4:8"]]
- 00c350cc ["CALL", null, ["callee:00c37cdc:8"]]
+ 00c360c0 ["INT_ADD", "register:40f0:8", ["const:c360c0:8", "const:4:8"]]
+ 00c360c0 ["CALL", null, ["callee:00c37cdc:8"]]
- 00c350cc bytes 07070094
+ 00c360c0 bytes 07070094
~~~


<a id="compare-071335e72df8740db40e44a05b65dbc2"></a>

### [`00c350e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md) → [`00c360d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360d8.md) FUN_00c360d8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c37cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c350fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md#insn-00c350fc) · [`00c35104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md#insn-00c35104)
- 新版 [`00c360f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360d8.md#insn-00c360f0) · [`00c360f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360d8.md#insn-00c360f8)

~~~diff
- 00c350fc ["INT_ADD", "register:40f0:8", ["const:c350fc:8", "const:4:8"]]
- 00c350fc ["CALL", null, ["callee:00c37cdc:8"]]
+ 00c360f0 ["INT_ADD", "register:40f0:8", ["const:c360f0:8", "const:4:8"]]
+ 00c360f0 ["CALL", null, ["callee:00c37cdc:8"]]
- 00c350fc bytes fb060094
+ 00c360f0 bytes fb060094
- 00c35104 ["INT_ADD", "register:40f0:8", ["const:c35104:8", "const:4:8"]]
- 00c35104 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c360f8 ["INT_ADD", "register:40f0:8", ["const:c360f8:8", "const:4:8"]]
+ 00c360f8 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35104 bytes b38c0094
+ 00c360f8 bytes aa8c0094
~~~


<a id="compare-bb236c0f1beb72892ac6a1fed2ab66dc"></a>

### [`00c351d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351d0.md) → [`00c361c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361c4.md) FUN_00c361c4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c37f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c351e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351d0.md#insn-00c351e8)
- 新版 [`00c361dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361c4.md#insn-00c361dc)

~~~diff
- 00c351e8 ["INT_ADD", "register:40f0:8", ["const:c351e8:8", "const:4:8"]]
- 00c351e8 ["CALL", null, ["callee:00c37f0c:8"]]
+ 00c361dc ["INT_ADD", "register:40f0:8", ["const:c361dc:8", "const:4:8"]]
+ 00c361dc ["CALL", null, ["callee:00c37f0c:8"]]
- 00c351e8 bytes 4c070094
+ 00c361dc bytes 4c070094
~~~


<a id="compare-bca6cc8f403039035232aef66d7adcbc"></a>

### [`00c35200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md) → [`00c361f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361f4.md) FUN_00c361f4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c37f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md#insn-00c35218) · [`00c35220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md#insn-00c35220)
- 新版 [`00c3620c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361f4.md#insn-00c3620c) · [`00c36214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361f4.md#insn-00c36214)

~~~diff
- 00c35218 ["INT_ADD", "register:40f0:8", ["const:c35218:8", "const:4:8"]]
- 00c35218 ["CALL", null, ["callee:00c37f0c:8"]]
+ 00c3620c ["INT_ADD", "register:40f0:8", ["const:c3620c:8", "const:4:8"]]
+ 00c3620c ["CALL", null, ["callee:00c37f0c:8"]]
- 00c35218 bytes 40070094
+ 00c3620c bytes 40070094
- 00c35220 ["INT_ADD", "register:40f0:8", ["const:c35220:8", "const:4:8"]]
- 00c35220 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36214 ["INT_ADD", "register:40f0:8", ["const:c36214:8", "const:4:8"]]
+ 00c36214 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35220 bytes 6c8c0094
+ 00c36214 bytes 638c0094
~~~


<a id="compare-748c9cb1e8e22cbc97bb6f89eecc77ef"></a>

### [`00c352ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c352ec.md) → [`00c362e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362e0.md) FUN_00c362e0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c352ec.md#insn-00c35304) · [`00c3530c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c352ec.md#insn-00c3530c)
- 新版 [`00c362f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362e0.md#insn-00c362f8) · [`00c36300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362e0.md#insn-00c36300)

~~~diff
- 00c35304 ["INT_ADD", "register:40f0:8", ["const:c35304:8", "const:4:8"]]
- 00c35304 ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c362f8 ["INT_ADD", "register:40f0:8", ["const:c362f8:8", "const:4:8"]]
+ 00c362f8 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c35304 bytes c7a60094
+ 00c362f8 bytes bea60094
- 00c3530c ["INT_ADD", "register:40f0:8", ["const:c3530c:8", "const:4:8"]]
- 00c3530c ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36300 ["INT_ADD", "register:40f0:8", ["const:c36300:8", "const:4:8"]]
+ 00c36300 ["CALL", null, ["callee:00c593a0:8"]]
- 00c3530c bytes 318c0094
+ 00c36300 bytes 288c0094
~~~


<a id="compare-0991701696f5b8ba421a76ce37d6fe84"></a>

### [`00c35324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35324.md) → [`00c36318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36318.md) FUN_00c36318

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3533c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35324.md#insn-00c3533c) · [`00c35344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35324.md#insn-00c35344)
- 新版 [`00c36330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36318.md#insn-00c36330) · [`00c36338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36318.md#insn-00c36338)

~~~diff
- 00c3533c ["INT_ADD", "register:40f0:8", ["const:c3533c:8", "const:4:8"]]
- 00c3533c ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c36330 ["INT_ADD", "register:40f0:8", ["const:c36330:8", "const:4:8"]]
+ 00c36330 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c3533c bytes b9a60094
+ 00c36330 bytes b0a60094
- 00c35344 ["INT_ADD", "register:40f0:8", ["const:c35344:8", "const:4:8"]]
- 00c35344 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36338 ["INT_ADD", "register:40f0:8", ["const:c36338:8", "const:4:8"]]
+ 00c36338 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35344 bytes 238c0094
+ 00c36338 bytes 1a8c0094
~~~


<a id="compare-5e429c89dc5915a7b8f8bcc11fcd4691"></a>

### [`00c3535c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3535c.md) → [`00c36350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36350.md) FUN_00c36350

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3535c.md#insn-00c35374)
- 新版 [`00c36368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36350.md#insn-00c36368)

~~~diff
- 00c35374 ["INT_ADD", "register:40f0:8", ["const:c35374:8", "const:4:8"]]
- 00c35374 ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c36368 ["INT_ADD", "register:40f0:8", ["const:c36368:8", "const:4:8"]]
+ 00c36368 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c35374 bytes aba60094
+ 00c36368 bytes a2a60094
~~~


<a id="compare-68fa595af02f3a601d8bec489541097f"></a>

### [`00c3538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3538c.md) → [`00c36380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36380.md) FUN_00c36380

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3538c.md#insn-00c353a4) · [`00c353ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3538c.md#insn-00c353ac)
- 新版 [`00c36398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36380.md#insn-00c36398) · [`00c363a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36380.md#insn-00c363a0)

~~~diff
- 00c353a4 ["INT_ADD", "register:40f0:8", ["const:c353a4:8", "const:4:8"]]
- 00c353a4 ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c36398 ["INT_ADD", "register:40f0:8", ["const:c36398:8", "const:4:8"]]
+ 00c36398 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c353a4 bytes 9fa60094
+ 00c36398 bytes 96a60094
- 00c353ac ["INT_ADD", "register:40f0:8", ["const:c353ac:8", "const:4:8"]]
- 00c353ac ["CALL", null, ["callee:00c593a0:8"]]
+ 00c363a0 ["INT_ADD", "register:40f0:8", ["const:c363a0:8", "const:4:8"]]
+ 00c363a0 ["CALL", null, ["callee:00c593a0:8"]]
- 00c353ac bytes 098c0094
+ 00c363a0 bytes 008c0094
~~~


<a id="compare-a1113e57064c66acedec32e110322a08"></a>

### [`00c353c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353c4.md) → [`00c363b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c363b8.md) FUN_00c363b8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353c4.md#insn-00c353dc)
- 新版 [`00c363d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c363b8.md#insn-00c363d0)

~~~diff
- 00c353dc ["INT_ADD", "register:40f0:8", ["const:c353dc:8", "const:4:8"]]
- 00c353dc ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c363d0 ["INT_ADD", "register:40f0:8", ["const:c363d0:8", "const:4:8"]]
+ 00c363d0 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c353dc bytes 91a60094
+ 00c363d0 bytes 88a60094
~~~


<a id="compare-51bd4e91e1305d25573c12f11fedfc16"></a>

### [`00c353f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353f4.md) → [`00c363e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c363e8.md) FUN_00c363e8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353f4.md#insn-00c3540c) · [`00c35414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353f4.md#insn-00c35414)
- 新版 [`00c36400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c363e8.md#insn-00c36400) · [`00c36408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c363e8.md#insn-00c36408)

~~~diff
- 00c3540c ["INT_ADD", "register:40f0:8", ["const:c3540c:8", "const:4:8"]]
- 00c3540c ["CALL", null, ["callee:00c5fdf0:8"]]
+ 00c36400 ["INT_ADD", "register:40f0:8", ["const:c36400:8", "const:4:8"]]
+ 00c36400 ["CALL", null, ["callee:00c5fdf0:8"]]
- 00c3540c bytes 85a60094
+ 00c36400 bytes 7ca60094
- 00c35414 ["INT_ADD", "register:40f0:8", ["const:c35414:8", "const:4:8"]]
- 00c35414 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36408 ["INT_ADD", "register:40f0:8", ["const:c36408:8", "const:4:8"]]
+ 00c36408 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35414 bytes ef8b0094
+ 00c36408 bytes e68b0094
~~~


<a id="compare-126278885c6c5bfa021712d613e6f738"></a>

### [`00c3542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3542c.md) → [`00c36420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36420.md) FUN_00c36420

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3542c.md#insn-00c35440)
- 新版 [`00c36434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36420.md#insn-00c36434)

~~~diff
- 00c35440 ["INT_ADD", "register:40f0:8", ["const:c35440:8", "const:4:8"]]
- 00c35440 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36434 ["INT_ADD", "register:40f0:8", ["const:c36434:8", "const:4:8"]]
+ 00c36434 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35440 bytes e48b0094
+ 00c36434 bytes db8b0094
~~~


<a id="compare-be51306a30ba41a9198cf08ffe2b3af7"></a>

### [`00c35458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35458.md) → [`00c3644c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3644c.md) FUN_00c3644c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35458.md#insn-00c3546c)
- 新版 [`00c36460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3644c.md#insn-00c36460)

~~~diff
- 00c3546c ["INT_ADD", "register:40f0:8", ["const:c3546c:8", "const:4:8"]]
- 00c3546c ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36460 ["INT_ADD", "register:40f0:8", ["const:c36460:8", "const:4:8"]]
+ 00c36460 ["CALL", null, ["callee:00c593a0:8"]]
- 00c3546c bytes d98b0094
+ 00c36460 bytes d08b0094
~~~


<a id="compare-5dd5af5947958229ba709ebf62dffaac"></a>

### [`00c35484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35484.md) → [`00c36478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36478.md) FUN_00c36478

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35484.md#insn-00c35498)
- 新版 [`00c3648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36478.md#insn-00c3648c)

~~~diff
- 00c35498 ["INT_ADD", "register:40f0:8", ["const:c35498:8", "const:4:8"]]
- 00c35498 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c3648c ["INT_ADD", "register:40f0:8", ["const:c3648c:8", "const:4:8"]]
+ 00c3648c ["CALL", null, ["callee:00c593a0:8"]]
- 00c35498 bytes ce8b0094
+ 00c3648c bytes c58b0094
~~~


<a id="compare-44ed47ef7d3e7fd74c2360d31a8cc778"></a>

### [`00c354b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354b0.md) → [`00c364a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364a4.md) FUN_00c364a4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c354c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354b0.md#insn-00c354c4)
- 新版 [`00c364b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364a4.md#insn-00c364b8)

~~~diff
- 00c354c4 ["INT_ADD", "register:40f0:8", ["const:c354c4:8", "const:4:8"]]
- 00c354c4 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c364b8 ["INT_ADD", "register:40f0:8", ["const:c364b8:8", "const:4:8"]]
+ 00c364b8 ["CALL", null, ["callee:00c593a0:8"]]
- 00c354c4 bytes c38b0094
+ 00c364b8 bytes ba8b0094
~~~


<a id="compare-a21d8dbf9bdd14c97b55762cbfa6b1fa"></a>

### [`00c35570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35570.md) → [`00c36564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36564.md) FUN_00c36564

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c354dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c364d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35570.md#insn-00c35584)
- 新版 [`00c36578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36564.md#insn-00c36578)

~~~diff
- 00c35584 ["INT_ADD", "register:40f0:8", ["const:c35584:8", "const:4:8"]]
- 00c35584 ["CALL", null, ["callee:00c364d0:8"]]
+ 00c36578 ["INT_ADD", "register:40f0:8", ["const:c36578:8", "const:4:8"]]
+ 00c36578 ["CALL", null, ["callee:00c364d0:8"]]
- 00c35584 bytes d6ffff97
+ 00c36578 bytes d6ffff97
~~~


<a id="compare-54b9304eb15e638c5a147c09a741cfe5"></a>

### [`00c35630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35630.md) → [`00c36624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36624.md) FUN_00c36624

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36590.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35630.md#insn-00c35644)
- 新版 [`00c36638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36624.md#insn-00c36638)

~~~diff
- 00c35644 ["INT_ADD", "register:40f0:8", ["const:c35644:8", "const:4:8"]]
- 00c35644 ["CALL", null, ["callee:00c36590:8"]]
+ 00c36638 ["INT_ADD", "register:40f0:8", ["const:c36638:8", "const:4:8"]]
+ 00c36638 ["CALL", null, ["callee:00c36590:8"]]
- 00c35644 bytes d6ffff97
+ 00c36638 bytes d6ffff97
~~~


<a id="compare-12faf10ca59ff372efd9f5d492453046"></a>

### [`00c356f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c356f0.md) → [`00c366e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c366e4.md) FUN_00c366e4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36650.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c356f0.md#insn-00c35704)
- 新版 [`00c366f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c366e4.md#insn-00c366f8)

~~~diff
- 00c35704 ["INT_ADD", "register:40f0:8", ["const:c35704:8", "const:4:8"]]
- 00c35704 ["CALL", null, ["callee:00c36650:8"]]
+ 00c366f8 ["INT_ADD", "register:40f0:8", ["const:c366f8:8", "const:4:8"]]
+ 00c366f8 ["CALL", null, ["callee:00c36650:8"]]
- 00c35704 bytes d6ffff97
+ 00c366f8 bytes d6ffff97
~~~


<a id="compare-108c2ff356159e10da5103da6368a353"></a>

### [`00c357b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357b0.md) → [`00c367a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367a4.md) FUN_00c367a4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3571c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36710.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c357c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357b0.md#insn-00c357c4)
- 新版 [`00c367b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367a4.md#insn-00c367b8)

~~~diff
- 00c357c4 ["INT_ADD", "register:40f0:8", ["const:c357c4:8", "const:4:8"]]
- 00c357c4 ["CALL", null, ["callee:00c36710:8"]]
+ 00c367b8 ["INT_ADD", "register:40f0:8", ["const:c367b8:8", "const:4:8"]]
+ 00c367b8 ["CALL", null, ["callee:00c36710:8"]]
- 00c357c4 bytes d6ffff97
+ 00c367b8 bytes d6ffff97
~~~


<a id="compare-397381da4bca536fc45c7209f5add86f"></a>

### [`00c357dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357dc.md) → [`00c367d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367d0.md) FUN_00c367d0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c357f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357dc.md#insn-00c357f0)
- 新版 [`00c367e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367d0.md#insn-00c367e4)

~~~diff
- 00c357f0 ["INT_ADD", "register:40f0:8", ["const:c357f0:8", "const:4:8"]]
- 00c357f0 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c367e4 ["INT_ADD", "register:40f0:8", ["const:c367e4:8", "const:4:8"]]
+ 00c367e4 ["CALL", null, ["callee:00c593a0:8"]]
- 00c357f0 bytes f88a0094
+ 00c367e4 bytes ef8a0094
~~~


<a id="compare-1d95e6c7cef96b0c17c904c6c5e0da5e"></a>

### [`00c35808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35808.md) → [`00c367fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367fc.md) FUN_00c367fc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35808.md#insn-00c3581c)
- 新版 [`00c36810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c367fc.md#insn-00c36810)

~~~diff
- 00c3581c ["INT_ADD", "register:40f0:8", ["const:c3581c:8", "const:4:8"]]
- 00c3581c ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36810 ["INT_ADD", "register:40f0:8", ["const:c36810:8", "const:4:8"]]
+ 00c36810 ["CALL", null, ["callee:00c593a0:8"]]
- 00c3581c bytes ed8a0094
+ 00c36810 bytes e48a0094
~~~


<a id="compare-33d0db2067511ee0026b5c8b174768ec"></a>

### [`00c35834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35834.md) → [`00c36828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36828.md) FUN_00c36828

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35834.md#insn-00c35848)
- 新版 [`00c3683c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36828.md#insn-00c3683c)

~~~diff
- 00c35848 ["INT_ADD", "register:40f0:8", ["const:c35848:8", "const:4:8"]]
- 00c35848 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c3683c ["INT_ADD", "register:40f0:8", ["const:c3683c:8", "const:4:8"]]
+ 00c3683c ["CALL", null, ["callee:00c593a0:8"]]
- 00c35848 bytes e28a0094
+ 00c3683c bytes d98a0094
~~~


<a id="compare-85b08c33c2fce8a7473d1bf40391d914"></a>

### [`00c35860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35860.md) → [`00c36854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36854.md) FUN_00c36854

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35860.md#insn-00c35874)
- 新版 [`00c36868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36854.md#insn-00c36868)

~~~diff
- 00c35874 ["INT_ADD", "register:40f0:8", ["const:c35874:8", "const:4:8"]]
- 00c35874 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36868 ["INT_ADD", "register:40f0:8", ["const:c36868:8", "const:4:8"]]
+ 00c36868 ["CALL", null, ["callee:00c593a0:8"]]
- 00c35874 bytes d78a0094
+ 00c36868 bytes ce8a0094
~~~


<a id="compare-c84970581e54914372b3e06e72c1a803"></a>

### [`00c3588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3588c.md) → [`00c36880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36880.md) FUN_00c36880

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c358a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3588c.md#insn-00c358a0)
- 新版 [`00c36894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36880.md#insn-00c36894)

~~~diff
- 00c358a0 ["INT_ADD", "register:40f0:8", ["const:c358a0:8", "const:4:8"]]
- 00c358a0 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36894 ["INT_ADD", "register:40f0:8", ["const:c36894:8", "const:4:8"]]
+ 00c36894 ["CALL", null, ["callee:00c593a0:8"]]
- 00c358a0 bytes cc8a0094
+ 00c36894 bytes c38a0094
~~~


<a id="compare-f0a102011e178e6358c818364b02ff83"></a>

### [`00c358b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358b8.md) → [`00c368ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c368ac.md) FUN_00c368ac

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c358cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358b8.md#insn-00c358cc)
- 新版 [`00c368c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c368ac.md#insn-00c368c0)

~~~diff
- 00c358cc ["INT_ADD", "register:40f0:8", ["const:c358cc:8", "const:4:8"]]
- 00c358cc ["CALL", null, ["callee:00c593a0:8"]]
+ 00c368c0 ["INT_ADD", "register:40f0:8", ["const:c368c0:8", "const:4:8"]]
+ 00c368c0 ["CALL", null, ["callee:00c593a0:8"]]
- 00c358cc bytes c18a0094
+ 00c368c0 bytes b88a0094
~~~


<a id="compare-7b9a659bd843493135490c1cb1e90a09"></a>

### [`00c358e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358e4.md) → [`00c368d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c368d8.md) FUN_00c368d8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c358f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358e4.md#insn-00c358f8)
- 新版 [`00c368ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c368d8.md#insn-00c368ec)

~~~diff
- 00c358f8 ["INT_ADD", "register:40f0:8", ["const:c358f8:8", "const:4:8"]]
- 00c358f8 ["CALL", null, ["callee:00c593a0:8"]]
+ 00c368ec ["INT_ADD", "register:40f0:8", ["const:c368ec:8", "const:4:8"]]
+ 00c368ec ["CALL", null, ["callee:00c593a0:8"]]
- 00c358f8 bytes b68a0094
+ 00c368ec bytes ad8a0094
~~~


<a id="compare-138d55c94c33e5a78340188a7651e1fa"></a>

### [`00c35918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35918.md) → [`00c3690c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3690c.md) FUN_00c3690c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3592c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35918.md#insn-00c3592c)
- 新版 [`00c36920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3690c.md#insn-00c36920)

~~~diff
- 00c3592c ["INT_ADD", "register:40f0:8", ["const:c3592c:8", "const:4:8"]]
- 00c3592c ["CALL", null, ["callee:00c593a0:8"]]
+ 00c36920 ["INT_ADD", "register:40f0:8", ["const:c36920:8", "const:4:8"]]
+ 00c36920 ["CALL", null, ["callee:00c593a0:8"]]
- 00c3592c bytes a98a0094
+ 00c36920 bytes a08a0094
~~~


<a id="compare-c617ca07bc661383f114553474654fc7"></a>

### [`00c35944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35944.md) → [`00c36938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36938.md) FUN_00c36938

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35944.md#insn-00c35958)
- 新版 [`00c3694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36938.md#insn-00c3694c)

~~~diff
- 00c35958 ["INT_ADD", "register:40f0:8", ["const:c35958:8", "const:4:8"]]
- 00c35958 ["CALL", null, ["callee:00c5f610:8"]]
+ 00c3694c ["INT_ADD", "register:40f0:8", ["const:c3694c:8", "const:4:8"]]
+ 00c3694c ["CALL", null, ["callee:00c5f610:8"]]
- 00c35958 bytes 3aa30094
+ 00c3694c bytes 31a30094
~~~


<a id="compare-80b160e0d2b907b6f2aa0886276c8943"></a>

### [`00c35984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md) → [`00c36978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md) FUN_00c36978

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) · 呼出先 4件 [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 4件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) [`00c25964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md) · 呼出先 4件 [`00c36960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c359d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md#insn-00c359d4) · [`00c35a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md#insn-00c35a04) · [`00c35a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md#insn-00c35a90)
- 新版 [`00c369c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md#insn-00c369c8) · [`00c369f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md#insn-00c369f8) · [`00c36a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md#insn-00c36a84)

~~~diff
- 00c359d4 ["INT_ADD", "register:40f0:8", ["const:c359d4:8", "const:4:8"]]
- 00c359d4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c369c8 ["INT_ADD", "register:40f0:8", ["const:c369c8:8", "const:4:8"]]
+ 00c369c8 ["CALL", null, ["callee:00c58f50:8"]]
- 00c359d4 bytes 6b890094
+ 00c369c8 bytes 62890094
- 00c35a04 ["INT_ADD", "register:40f0:8", ["const:c35a04:8", "const:4:8"]]
- 00c35a04 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c369f8 ["INT_ADD", "register:40f0:8", ["const:c369f8:8", "const:4:8"]]
+ 00c369f8 ["CALL", null, ["callee:00c58fe0:8"]]
- 00c35a04 bytes 83890094
+ 00c369f8 bytes 7a890094
- 00c35a90 ["INT_ADD", "register:40f0:8", ["const:c35a90:8", "const:4:8"]]
- 00c35a90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c36a84 ["INT_ADD", "register:40f0:8", ["const:c36a84:8", "const:4:8"]]
+ 00c36a84 ["CALL", null, ["callee:00c58f30:8"]]
- 00c35a90 bytes 34890094
+ 00c36a84 bytes 2b890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a617cb5fc28af07f6ba25d586f770f"></a>

### [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) → [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) FUN_00c36ad4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`00c1d738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md) [`00c1fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md) [`00c1fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) [`00c1fec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md) [`00c1fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 54件 [`00c1e72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e72c.md) [`00c20c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md) [`00c20d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md) [`00c20eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md) [`00c20fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c36960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md#insn-00c35b80) · [`00c35ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md#insn-00c35ba8) · [`00c35bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md#insn-00c35bc8)
- 新版 [`00c36b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md#insn-00c36b74) · [`00c36b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md#insn-00c36b9c) · [`00c36bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md#insn-00c36bbc)

~~~diff
- 00c35b80 ["INT_ADD", "register:40f0:8", ["const:c35b80:8", "const:4:8"]]
- 00c35b80 ["CALL", null, ["callee:00c59130:8"]]
+ 00c36b74 ["INT_ADD", "register:40f0:8", ["const:c36b74:8", "const:4:8"]]
+ 00c36b74 ["CALL", null, ["callee:00c59130:8"]]
- 00c35b80 bytes 78890094
+ 00c36b74 bytes 6f890094
- 00c35ba8 ["INT_ADD", "register:40f0:8", ["const:c35ba8:8", "const:4:8"]]
- 00c35ba8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c36b9c ["INT_ADD", "register:40f0:8", ["const:c36b9c:8", "const:4:8"]]
+ 00c36b9c ["CALL", null, ["callee:00c58f30:8"]]
- 00c35ba8 bytes ee880094
+ 00c36b9c bytes e5880094
- 00c35bc8 ["INT_ADD", "register:40f0:8", ["const:c35bc8:8", "const:4:8"]]
- 00c35bc8 ["CALL", null, ["callee:00c59130:8"]]
+ 00c36bbc ["INT_ADD", "register:40f0:8", ["const:c36bbc:8", "const:4:8"]]
+ 00c36bbc ["CALL", null, ["callee:00c59130:8"]]
- 00c35bc8 bytes 66890094
+ 00c36bbc bytes 5d890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94bda2808dfd079cd413dd12b9a5846"></a>

### [`00c36154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md) → [`00c37148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37148.md) FUN_00c37148

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c32f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32f08.md) · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md)
- 新版 呼出元 1件 [`00c33efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33efc.md) · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00bf2c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md#insn-00c36190) · [`00c361a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md#insn-00c361a8)
- 新版 [`00c37184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37148.md#insn-00c37184) · [`00c3719c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37148.md#insn-00c3719c)

~~~diff
- 00c36190 ["INT_ADD", "register:40f0:8", ["const:c36190:8", "const:4:8"]]
- 00c36190 ["CALL", null, ["callee:00bf2c9c:8"]]
+ 00c37184 ["INT_ADD", "register:40f0:8", ["const:c37184:8", "const:4:8"]]
+ 00c37184 ["CALL", null, ["callee:00bf2c9c:8"]]
- 00c36190 bytes c6eefe97
+ 00c37184 bytes c6eefe97
- 00c361a8 ["INT_ADD", "register:40f0:8", ["const:c361a8:8", "const:4:8"]]
- 00c361a8 ["CALL", null, ["callee:00442c7c:8"]]
+ 00c3719c ["INT_ADD", "register:40f0:8", ["const:c3719c:8", "const:4:8"]]
+ 00c3719c ["CALL", null, ["callee:00442c7c:8"]]
- 00c361a8 bytes ed31e097
+ 00c3719c bytes b82ee097
~~~


<a id="compare-f88adbb1aa5f7af062cf72f8fa2a3c98"></a>

### [`00c361ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md) → [`00c371a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371a0.md) FUN_00c371a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c33fd0.md) · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md)
- 新版 呼出元 1件 [`00c34fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34fc4.md) · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00bf50b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf50b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c361ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md#insn-00c361ec) · [`00c36204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md#insn-00c36204)
- 新版 [`00c371e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371a0.md#insn-00c371e0) · [`00c371f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371a0.md#insn-00c371f8)

~~~diff
- 00c361ec ["INT_ADD", "register:40f0:8", ["const:c361ec:8", "const:4:8"]]
- 00c361ec ["CALL", null, ["callee:00bf50b0:8"]]
+ 00c371e0 ["INT_ADD", "register:40f0:8", ["const:c371e0:8", "const:4:8"]]
+ 00c371e0 ["CALL", null, ["callee:00bf50b0:8"]]
- 00c361ec bytes b4f7fe97
+ 00c371e0 bytes b4f7fe97
- 00c36204 ["INT_ADD", "register:40f0:8", ["const:c36204:8", "const:4:8"]]
- 00c36204 ["CALL", null, ["callee:00bf3968:8"]]
+ 00c371f8 ["INT_ADD", "register:40f0:8", ["const:c371f8:8", "const:4:8"]]
+ 00c371f8 ["CALL", null, ["callee:00bf3968:8"]]
- 00c36204 bytes dcf1fe97
+ 00c371f8 bytes dcf1fe97
~~~


<a id="compare-3cc16a611150d909492993140b91b005"></a>

### [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) → [`00c37cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md) FUN_00c37cdc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c350b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350b4.md) [`00c350e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 2件 [`00c360a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360a8.md) [`00c360d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c360d8.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md#insn-00c36d30) · [`00c36d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md#insn-00c36d54) · [`00c36dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md#insn-00c36dd0)
- 新版 [`00c37d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md#insn-00c37d24) · [`00c37d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md#insn-00c37d48) · [`00c37dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37cdc.md#insn-00c37dc4)

~~~diff
- 00c36d30 ["INT_ADD", "register:40f0:8", ["const:c36d30:8", "const:4:8"]]
- 00c36d30 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37d24 ["INT_ADD", "register:40f0:8", ["const:c37d24:8", "const:4:8"]]
+ 00c37d24 ["CALL", null, ["callee:00c58f50:8"]]
- 00c36d30 bytes 94840094
+ 00c37d24 bytes 8b840094
- 00c36d54 ["INT_ADD", "register:40f0:8", ["const:c36d54:8", "const:4:8"]]
- 00c36d54 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37d48 ["INT_ADD", "register:40f0:8", ["const:c37d48:8", "const:4:8"]]
+ 00c37d48 ["CALL", null, ["callee:00c58f50:8"]]
- 00c36d54 bytes 8b840094
+ 00c37d48 bytes 82840094
- 00c36dd0 ["INT_ADD", "register:40f0:8", ["const:c36dd0:8", "const:4:8"]]
- 00c36dd0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37dc4 ["INT_ADD", "register:40f0:8", ["const:c37dc4:8", "const:4:8"]]
+ 00c37dc4 ["CALL", null, ["callee:00c58f50:8"]]
- 00c36dd0 bytes 6c840094
+ 00c37dc4 bytes 63840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fb4bfcb39bff2d9a50389c0b13bad9"></a>

### [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) → [`00c37f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md) FUN_00c37f0c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c351d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351d0.md) [`00c35200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 2件 [`00c361c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361c4.md) [`00c361f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361f4.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md#insn-00c36f60) · [`00c36f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md#insn-00c36f84) · [`00c37000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md#insn-00c37000)
- 新版 [`00c37f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md#insn-00c37f54) · [`00c37f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md#insn-00c37f78) · [`00c37ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37f0c.md#insn-00c37ff4)

~~~diff
- 00c36f60 ["INT_ADD", "register:40f0:8", ["const:c36f60:8", "const:4:8"]]
- 00c36f60 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37f54 ["INT_ADD", "register:40f0:8", ["const:c37f54:8", "const:4:8"]]
+ 00c37f54 ["CALL", null, ["callee:00c58f50:8"]]
- 00c36f60 bytes 08840094
+ 00c37f54 bytes ff830094
- 00c36f84 ["INT_ADD", "register:40f0:8", ["const:c36f84:8", "const:4:8"]]
- 00c36f84 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37f78 ["INT_ADD", "register:40f0:8", ["const:c37f78:8", "const:4:8"]]
+ 00c37f78 ["CALL", null, ["callee:00c58f50:8"]]
- 00c36f84 bytes ff830094
+ 00c37f78 bytes f6830094
- 00c37000 ["INT_ADD", "register:40f0:8", ["const:c37000:8", "const:4:8"]]
- 00c37000 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c37ff4 ["INT_ADD", "register:40f0:8", ["const:c37ff4:8", "const:4:8"]]
+ 00c37ff4 ["CALL", null, ["callee:00c58f50:8"]]
- 00c37000 bytes e0830094
+ 00c37ff4 bytes d7830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c2fe25e83718c229d2b8b4e6bb39eea"></a>

### [`00c3732c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3732c.md) → [`00c38320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38320.md) _ZNSt6__ndk111regex_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a890.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3732c.md#insn-00c37340)
- 新版 [`00c38334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38320.md#insn-00c38334)

~~~diff
- 00c37340 ["INT_ADD", "register:40f0:8", ["const:c37340:8", "const:4:8"]]
- 00c37340 ["CALL", null, ["callee:00c5b860:8"]]
+ 00c38334 ["INT_ADD", "register:40f0:8", ["const:c38334:8", "const:4:8"]]
+ 00c38334 ["CALL", null, ["callee:00c5b860:8"]]
- 00c37340 bytes 548d0094
+ 00c38334 bytes 4b8d0094
~~~


<a id="compare-b0a1adc815ac075ff4fa958b21e392cf"></a>

### [`00c37c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c48.md) → [`00c38c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c3c.md) _ZNSt9exceptionD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eed0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c48.md#insn-00c37c5c)
- 新版 [`00c38c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c3c.md#insn-00c38c50)

~~~diff
- 00c37c5c ["INT_ADD", "register:40f0:8", ["const:c37c5c:8", "const:4:8"]]
- 00c37c5c ["CALL", null, ["callee:00c5fea0:8"]]
+ 00c38c50 ["INT_ADD", "register:40f0:8", ["const:c38c50:8", "const:4:8"]]
+ 00c38c50 ["CALL", null, ["callee:00c5fea0:8"]]
- 00c37c5c bytes 9d9c0094
+ 00c38c50 bytes 949c0094
~~~


<a id="compare-26d26bb36ab344ce19959fdf391f64cd"></a>

### [`00c37c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c84.md) → [`00c38c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c78.md) _ZNSt13bad_exceptionD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5feb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5feb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c84.md#insn-00c37c98)
- 新版 [`00c38c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c78.md#insn-00c38c8c)

~~~diff
- 00c37c98 ["INT_ADD", "register:40f0:8", ["const:c37c98:8", "const:4:8"]]
- 00c37c98 ["CALL", null, ["callee:00c5feb0:8"]]
+ 00c38c8c ["INT_ADD", "register:40f0:8", ["const:c38c8c:8", "const:4:8"]]
+ 00c38c8c ["CALL", null, ["callee:00c5feb0:8"]]
- 00c37c98 bytes 929c0094
+ 00c38c8c bytes 899c0094
~~~


<a id="compare-1fecefcc5f5fbf863c318ab06c4e31a9"></a>

### [`00c37cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cd8.md) → [`00c38ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ccc.md) _ZNSt9bad_allocD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59af0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cd8.md#insn-00c37cec)
- 新版 [`00c38ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ccc.md#insn-00c38ce0)

~~~diff
- 00c37cec ["INT_ADD", "register:40f0:8", ["const:c37cec:8", "const:4:8"]]
- 00c37cec ["CALL", null, ["callee:00c59af0:8"]]
+ 00c38ce0 ["INT_ADD", "register:40f0:8", ["const:c38ce0:8", "const:4:8"]]
+ 00c38ce0 ["CALL", null, ["callee:00c59af0:8"]]
- 00c37cec bytes 8d830094
+ 00c38ce0 bytes 84830094
~~~


<a id="compare-e140002609c4ed439ff5e211e0441843"></a>

### [`00c37d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d2c.md) → [`00c38d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d20.md) _ZNSt20bad_array_new_lengthD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58110.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d2c.md#insn-00c37d40)
- 新版 [`00c38d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d20.md#insn-00c38d34)

~~~diff
- 00c37d40 ["INT_ADD", "register:40f0:8", ["const:c37d40:8", "const:4:8"]]
- 00c37d40 ["CALL", null, ["callee:00c590e0:8"]]
+ 00c38d34 ["INT_ADD", "register:40f0:8", ["const:c38d34:8", "const:4:8"]]
+ 00c38d34 ["CALL", null, ["callee:00c590e0:8"]]
- 00c37d40 bytes f4800094
+ 00c38d34 bytes eb800094
~~~


<a id="compare-55de61406bb682675e1c64a842335065"></a>

### [`00c37dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37dc0.md) → [`00c38db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38db4.md) _ZNSt11logic_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eef0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37dc0.md#insn-00c37dd4)
- 新版 [`00c38dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38db4.md#insn-00c38dc8)

~~~diff
- 00c37dd4 ["INT_ADD", "register:40f0:8", ["const:c37dd4:8", "const:4:8"]]
- 00c37dd4 ["CALL", null, ["callee:00c5fec0:8"]]
+ 00c38dc8 ["INT_ADD", "register:40f0:8", ["const:c38dc8:8", "const:4:8"]]
+ 00c38dc8 ["CALL", null, ["callee:00c5fec0:8"]]
- 00c37dd4 bytes 479c0094
+ 00c38dc8 bytes 3e9c0094
~~~


<a id="compare-f96f2184c0442ec17a4cfeffb7cfda50"></a>

### [`00c37e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e50.md) → [`00c38e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38e44.md) _ZNSt13runtime_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e50.md#insn-00c37e64)
- 新版 [`00c38e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38e44.md#insn-00c38e58)

~~~diff
- 00c37e64 ["INT_ADD", "register:40f0:8", ["const:c37e64:8", "const:4:8"]]
- 00c37e64 ["CALL", null, ["callee:00c5f070:8"]]
+ 00c38e58 ["INT_ADD", "register:40f0:8", ["const:c38e58:8", "const:4:8"]]
+ 00c38e58 ["CALL", null, ["callee:00c5f070:8"]]
- 00c37e64 bytes 8f980094
+ 00c38e58 bytes 86980094
~~~


<a id="compare-a85641cde08c560e643b2481a1ef4e3d"></a>

### [`00c37e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e88.md) → [`00c38e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38e7c.md) _ZNSt12domain_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e88.md#insn-00c37e9c)
- 新版 [`00c38e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38e7c.md#insn-00c38e90)

~~~diff
- 00c37e9c ["INT_ADD", "register:40f0:8", ["const:c37e9c:8", "const:4:8"]]
- 00c37e9c ["CALL", null, ["callee:00c5fed0:8"]]
+ 00c38e90 ["INT_ADD", "register:40f0:8", ["const:c38e90:8", "const:4:8"]]
+ 00c38e90 ["CALL", null, ["callee:00c5fed0:8"]]
- 00c37e9c bytes 199c0094
+ 00c38e90 bytes 109c0094
~~~


<a id="compare-1136941adf2933408c2709132234b3d6"></a>

### [`00c37eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37eb4.md) → [`00c38ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ea8.md) _ZNSt16invalid_argumentD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37eb4.md#insn-00c37ec8)
- 新版 [`00c38ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ea8.md#insn-00c38ebc)

~~~diff
- 00c37ec8 ["INT_ADD", "register:40f0:8", ["const:c37ec8:8", "const:4:8"]]
- 00c37ec8 ["CALL", null, ["callee:00c5f1d0:8"]]
+ 00c38ebc ["INT_ADD", "register:40f0:8", ["const:c38ebc:8", "const:4:8"]]
+ 00c38ebc ["CALL", null, ["callee:00c5f1d0:8"]]
- 00c37ec8 bytes ce980094
+ 00c38ebc bytes c5980094
~~~


<a id="compare-c503fcf55669d512fd83fd8716219efd"></a>

### [`00c37ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37ee0.md) → [`00c38ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ed4.md) _ZNSt12length_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37ee0.md#insn-00c37ef4)
- 新版 [`00c38ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ed4.md#insn-00c38ee8)

~~~diff
- 00c37ef4 ["INT_ADD", "register:40f0:8", ["const:c37ef4:8", "const:4:8"]]
- 00c37ef4 ["CALL", null, ["callee:00c58fa0:8"]]
+ 00c38ee8 ["INT_ADD", "register:40f0:8", ["const:c38ee8:8", "const:4:8"]]
+ 00c38ee8 ["CALL", null, ["callee:00c58fa0:8"]]
- 00c37ef4 bytes 37800094
+ 00c38ee8 bytes 2e800094
~~~


<a id="compare-6077b34d4259f7ea44ca15a91a5d91a0"></a>

### [`00c37f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f0c.md) → [`00c38f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f00.md) _ZNSt12out_of_rangeD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f0c.md#insn-00c37f20)
- 新版 [`00c38f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f00.md#insn-00c38f14)

~~~diff
- 00c37f20 ["INT_ADD", "register:40f0:8", ["const:c37f20:8", "const:4:8"]]
- 00c37f20 ["CALL", null, ["callee:00c59140:8"]]
+ 00c38f14 ["INT_ADD", "register:40f0:8", ["const:c38f14:8", "const:4:8"]]
+ 00c38f14 ["CALL", null, ["callee:00c59140:8"]]
- 00c37f20 bytes 94800094
+ 00c38f14 bytes 8b800094
~~~


<a id="compare-b6e8522b72e52a4c190f9173de7d4f2f"></a>

### [`00c37f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f38.md) → [`00c38f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f2c.md) _ZNSt11range_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a990.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f38.md#insn-00c37f4c)
- 新版 [`00c38f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f2c.md#insn-00c38f40)

~~~diff
- 00c37f4c ["INT_ADD", "register:40f0:8", ["const:c37f4c:8", "const:4:8"]]
- 00c37f4c ["CALL", null, ["callee:00c5b960:8"]]
+ 00c38f40 ["INT_ADD", "register:40f0:8", ["const:c38f40:8", "const:4:8"]]
+ 00c38f40 ["CALL", null, ["callee:00c5b960:8"]]
- 00c37f4c bytes 918a0094
+ 00c38f40 bytes 888a0094
~~~


<a id="compare-1867887e4047c1e342f38fcc7277e48e"></a>

### [`00c37f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f64.md) → [`00c38f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f58.md) _ZNSt14overflow_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f64.md#insn-00c37f78)
- 新版 [`00c38f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f58.md#insn-00c38f6c)

~~~diff
- 00c37f78 ["INT_ADD", "register:40f0:8", ["const:c37f78:8", "const:4:8"]]
- 00c37f78 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c38f6c ["INT_ADD", "register:40f0:8", ["const:c38f6c:8", "const:4:8"]]
+ 00c38f6c ["CALL", null, ["callee:00c5f010:8"]]
- 00c37f78 bytes 32980094
+ 00c38f6c bytes 29980094
~~~


<a id="compare-611b38b3feb7d9f8d754a122bfd92e0f"></a>

### [`00c37f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f90.md) → [`00c38f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f84.md) _ZNSt15underflow_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f90.md#insn-00c37fa4)
- 新版 [`00c38f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38f84.md#insn-00c38f98)

~~~diff
- 00c37fa4 ["INT_ADD", "register:40f0:8", ["const:c37fa4:8", "const:4:8"]]
- 00c37fa4 ["CALL", null, ["callee:00c5fee0:8"]]
+ 00c38f98 ["INT_ADD", "register:40f0:8", ["const:c38f98:8", "const:4:8"]]
+ 00c38f98 ["CALL", null, ["callee:00c5fee0:8"]]
- 00c37fa4 bytes db9b0094
+ 00c38f98 bytes d29b0094
~~~


<a id="compare-dbdf5175ae8f9ad142feb60ba7200c4d"></a>

### [`00c37fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37fc4.md) → [`00c38fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38fb8.md) _ZNSt9type_infoD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ff00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37fc4.md#insn-00c37fd8)
- 新版 [`00c38fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38fb8.md#insn-00c38fcc)

~~~diff
- 00c37fd8 ["INT_ADD", "register:40f0:8", ["const:c37fd8:8", "const:4:8"]]
- 00c37fd8 ["CALL", null, ["callee:00c5ff00:8"]]
+ 00c38fcc ["INT_ADD", "register:40f0:8", ["const:c38fcc:8", "const:4:8"]]
+ 00c38fcc ["CALL", null, ["callee:00c5ff00:8"]]
- 00c37fd8 bytes d69b0094
+ 00c38fcc bytes cd9b0094
~~~


<a id="compare-7cf245eb1d129a7df69974a8cee3bf96"></a>

### [`00c38010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38010.md) → [`00c39004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39004.md) _ZNSt8bad_castD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e560.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38010.md#insn-00c38024)
- 新版 [`00c39018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39004.md#insn-00c39018)

~~~diff
- 00c38024 ["INT_ADD", "register:40f0:8", ["const:c38024:8", "const:4:8"]]
- 00c38024 ["CALL", null, ["callee:00c5f530:8"]]
+ 00c39018 ["INT_ADD", "register:40f0:8", ["const:c39018:8", "const:4:8"]]
+ 00c39018 ["CALL", null, ["callee:00c5f530:8"]]
- 00c38024 bytes 4f990094
+ 00c39018 bytes 46990094
~~~


<a id="compare-57c391b9e713de9a6944459c4eb73bf1"></a>

### [`00c3806c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3806c.md) → [`00c39060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39060.md) _ZNSt10bad_typeidD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ee50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fe20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3806c.md#insn-00c38080)
- 新版 [`00c39074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39060.md#insn-00c39074)

~~~diff
- 00c38080 ["INT_ADD", "register:40f0:8", ["const:c38080:8", "const:4:8"]]
- 00c38080 ["CALL", null, ["callee:00c5fe20:8"]]
+ 00c39074 ["INT_ADD", "register:40f0:8", ["const:c39074:8", "const:4:8"]]
+ 00c39074 ["CALL", null, ["callee:00c5fe20:8"]]
- 00c38080 bytes 749b0094
+ 00c39074 bytes 6b9b0094
~~~


<a id="compare-04a2f334a88afff7cbb3795303aeeb7a"></a>

### [`00c381cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381cc.md) → [`00c391c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c391c0.md) FUN_00c391c0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c381e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381cc.md#insn-00c381e0)
- 新版 [`00c391d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c391c0.md#insn-00c391d4)

~~~diff
- 00c381e0 ["INT_ADD", "register:40f0:8", ["const:c381e0:8", "const:4:8"]]
- 00c381e0 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c391d4 ["INT_ADD", "register:40f0:8", ["const:c391d4:8", "const:4:8"]]
+ 00c391d4 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c381e0 bytes 509b0094
+ 00c391d4 bytes 479b0094
~~~


<a id="compare-20c98946ad7f19364e1ba983aefea580"></a>

### [`00c381f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381f8.md) → [`00c391ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c391ec.md) FUN_00c391ec

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381f8.md#insn-00c3820c)
- 新版 [`00c39200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c391ec.md#insn-00c39200)

~~~diff
- 00c3820c ["INT_ADD", "register:40f0:8", ["const:c3820c:8", "const:4:8"]]
- 00c3820c ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39200 ["INT_ADD", "register:40f0:8", ["const:c39200:8", "const:4:8"]]
+ 00c39200 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c3820c bytes 459b0094
+ 00c39200 bytes 3c9b0094
~~~


<a id="compare-71a625827211324276d14db0b34baec9"></a>

### [`00c38224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38224.md) → [`00c39218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39218.md) FUN_00c39218

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38224.md#insn-00c38238)
- 新版 [`00c3922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39218.md#insn-00c3922c)

~~~diff
- 00c38238 ["INT_ADD", "register:40f0:8", ["const:c38238:8", "const:4:8"]]
- 00c38238 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c3922c ["INT_ADD", "register:40f0:8", ["const:c3922c:8", "const:4:8"]]
+ 00c3922c ["CALL", null, ["callee:00c5fef0:8"]]
- 00c38238 bytes 3a9b0094
+ 00c3922c bytes 319b0094
~~~


<a id="compare-9767c1d2fc381970eaa8cd207ae85d5d"></a>

### [`00c38250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38250.md) → [`00c39244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39244.md) FUN_00c39244

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38250.md#insn-00c38264)
- 新版 [`00c39258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39244.md#insn-00c39258)

~~~diff
- 00c38264 ["INT_ADD", "register:40f0:8", ["const:c38264:8", "const:4:8"]]
- 00c38264 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39258 ["INT_ADD", "register:40f0:8", ["const:c39258:8", "const:4:8"]]
+ 00c39258 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c38264 bytes 2f9b0094
+ 00c39258 bytes 269b0094
~~~


<a id="compare-7085343974942e148c3ceeea7d4def15"></a>

### [`00c3827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3827c.md) → [`00c39270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39270.md) FUN_00c39270

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3827c.md#insn-00c38290)
- 新版 [`00c39284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39270.md#insn-00c39284)

~~~diff
- 00c38290 ["INT_ADD", "register:40f0:8", ["const:c38290:8", "const:4:8"]]
- 00c38290 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39284 ["INT_ADD", "register:40f0:8", ["const:c39284:8", "const:4:8"]]
+ 00c39284 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c38290 bytes 249b0094
+ 00c39284 bytes 1b9b0094
~~~


<a id="compare-2eaab37f1da01825613339b31bfd9b8b"></a>

### [`00c382a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382a8.md) → [`00c3929c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3929c.md) FUN_00c3929c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c382bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382a8.md#insn-00c382bc)
- 新版 [`00c392b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3929c.md#insn-00c392b0)

~~~diff
- 00c382bc ["INT_ADD", "register:40f0:8", ["const:c382bc:8", "const:4:8"]]
- 00c382bc ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c392b0 ["INT_ADD", "register:40f0:8", ["const:c392b0:8", "const:4:8"]]
+ 00c392b0 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c382bc bytes 199b0094
+ 00c392b0 bytes 109b0094
~~~


<a id="compare-43665545cfbd0e30ce22ceb2930de2c5"></a>

### [`00c382d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382d4.md) → [`00c392c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c392c8.md) FUN_00c392c8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c382e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382d4.md#insn-00c382e8)
- 新版 [`00c392dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c392c8.md#insn-00c392dc)

~~~diff
- 00c382e8 ["INT_ADD", "register:40f0:8", ["const:c382e8:8", "const:4:8"]]
- 00c382e8 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c392dc ["INT_ADD", "register:40f0:8", ["const:c392dc:8", "const:4:8"]]
+ 00c392dc ["CALL", null, ["callee:00c5fef0:8"]]
- 00c382e8 bytes 0e9b0094
+ 00c392dc bytes 059b0094
~~~


<a id="compare-5276afce245a2859688f40b43509febb"></a>

### [`00c38300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38300.md) → [`00c392f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c392f4.md) FUN_00c392f4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38300.md#insn-00c38314)
- 新版 [`00c39308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c392f4.md#insn-00c39308)

~~~diff
- 00c38314 ["INT_ADD", "register:40f0:8", ["const:c38314:8", "const:4:8"]]
- 00c38314 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39308 ["INT_ADD", "register:40f0:8", ["const:c39308:8", "const:4:8"]]
+ 00c39308 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c38314 bytes 039b0094
+ 00c39308 bytes fa9a0094
~~~


<a id="compare-a8311274ed14359ee6304379b0d356bb"></a>

### [`00c3832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3832c.md) → [`00c39320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39320.md) FUN_00c39320

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3832c.md#insn-00c38340)
- 新版 [`00c39334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39320.md#insn-00c39334)

~~~diff
- 00c38340 ["INT_ADD", "register:40f0:8", ["const:c38340:8", "const:4:8"]]
- 00c38340 ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39334 ["INT_ADD", "register:40f0:8", ["const:c39334:8", "const:4:8"]]
+ 00c39334 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c38340 bytes f89a0094
+ 00c39334 bytes ef9a0094
~~~


<a id="compare-ac06d3b1663be7334e09584ee20104b7"></a>

### [`00c38358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38358.md) → [`00c3934c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3934c.md) FUN_00c3934c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5fef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3836c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38358.md#insn-00c3836c)
- 新版 [`00c39360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3934c.md#insn-00c39360)

~~~diff
- 00c3836c ["INT_ADD", "register:40f0:8", ["const:c3836c:8", "const:4:8"]]
- 00c3836c ["CALL", null, ["callee:00c5fef0:8"]]
+ 00c39360 ["INT_ADD", "register:40f0:8", ["const:c39360:8", "const:4:8"]]
+ 00c39360 ["CALL", null, ["callee:00c5fef0:8"]]
- 00c3836c bytes ed9a0094
+ 00c39360 bytes e49a0094
~~~


<a id="compare-aa5aceb729e9d90fbbb8503adfb52f56"></a>

### [`00c384b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c384b8.md) → [`00c394ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c394ac.md) __dynamic_cast

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3855c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c384b8.md#insn-00c3855c) · [`00c385bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c384b8.md#insn-00c385bc) · [`00c38694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c384b8.md#insn-00c38694)
- 新版 [`00c39550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c394ac.md#insn-00c39550) · [`00c395b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c394ac.md#insn-00c395b0) · [`00c39688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c394ac.md#insn-00c39688)

~~~diff
- 00c3855c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3855c ["INT_ADD", "register:40f0:8", ["const:c3855c:8", "const:4:8"]]
- 00c3855c ["CALLIND", null, ["register:0:8"]]
+ 00c39550 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c39550 ["INT_ADD", "register:40f0:8", ["const:c39550:8", "const:4:8"]]
+ 00c39550 ["CALLIND", null, ["register:0:8"]]
- 00c3855c bytes 20013fd6
+ 00c39550 bytes 20013fd6
- 00c385bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c385bc ["INT_ADD", "register:40f0:8", ["const:c385bc:8", "const:4:8"]]
- 00c385bc ["CALLIND", null, ["register:0:8"]]
+ 00c395b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c395b0 ["INT_ADD", "register:40f0:8", ["const:c395b0:8", "const:4:8"]]
+ 00c395b0 ["CALLIND", null, ["register:0:8"]]
- 00c385bc bytes 00013fd6
+ 00c395b0 bytes 00013fd6
- 00c38694 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c38694 ["INT_ADD", "register:40f0:8", ["const:c38694:8", "const:4:8"]]
- 00c38694 ["CALLIND", null, ["register:0:8"]]
+ 00c39688 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c39688 ["INT_ADD", "register:40f0:8", ["const:c39688:8", "const:4:8"]]
+ 00c39688 ["CALLIND", null, ["register:0:8"]]
- 00c38694 bytes 00013fd6
+ 00c39688 bytes 00013fd6
~~~


<a id="compare-34b76de89eed21d498272d036a94e04a"></a>

### [`00c387e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c387e0.md) → [`00c397d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c397d4.md) FUN_00c397d4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c388e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c387e0.md#insn-00c388e8) · [`00c3896c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c387e0.md#insn-00c3896c)
- 新版 [`00c398dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c397d4.md#insn-00c398dc) · [`00c39960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c397d4.md#insn-00c39960)

~~~diff
- 00c388e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c388e8 ["INT_ADD", "register:40f0:8", ["const:c388e8:8", "const:4:8"]]
- 00c388e8 ["CALLIND", null, ["register:0:8"]]
+ 00c398dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c398dc ["INT_ADD", "register:40f0:8", ["const:c398dc:8", "const:4:8"]]
+ 00c398dc ["CALLIND", null, ["register:0:8"]]
- 00c388e8 bytes 00013fd6
+ 00c398dc bytes 00013fd6
- 00c3896c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3896c ["INT_ADD", "register:40f0:8", ["const:c3896c:8", "const:4:8"]]
- 00c3896c ["CALLIND", null, ["register:0:8"]]
+ 00c39960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c39960 ["INT_ADD", "register:40f0:8", ["const:c39960:8", "const:4:8"]]
+ 00c39960 ["CALLIND", null, ["register:0:8"]]
- 00c3896c bytes 00013fd6
+ 00c39960 bytes 00013fd6
~~~


<a id="compare-4d34c5c230ba48c342a3188827975559"></a>

### [`00c39018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39018.md) → [`00c3a00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a00c.md) FUN_00c3a00c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39018.md#insn-00c39068) · [`00c39084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39018.md#insn-00c39084) · [`00c39134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39018.md#insn-00c39134)
- 新版 [`00c3a05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a00c.md#insn-00c3a05c) · [`00c3a078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a00c.md#insn-00c3a078) · [`00c3a128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a00c.md#insn-00c3a128)

~~~diff
- 00c39068 ["INT_ADD", "register:40f0:8", ["const:c39068:8", "const:4:8"]]
- 00c39068 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a05c ["INT_ADD", "register:40f0:8", ["const:c3a05c:8", "const:4:8"]]
+ 00c3a05c ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39068 bytes 2e8a0094
+ 00c3a05c bytes 258a0094
- 00c39084 ["INT_ADD", "register:40f0:8", ["const:c39084:8", "const:4:8"]]
- 00c39084 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a078 ["INT_ADD", "register:40f0:8", ["const:c3a078:8", "const:4:8"]]
+ 00c3a078 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39084 bytes 278a0094
+ 00c3a078 bytes 1e8a0094
- 00c39134 ["COPY", "register:0:8", ["register:4050:8"]]
- 00c39134 ["INT_ADD", "register:40f0:8", ["const:c39134:8", "const:4:8"]]
- 00c39134 ["CALLIND", null, ["register:0:8"]]
+ 00c3a128 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00c3a128 ["INT_ADD", "register:40f0:8", ["const:c3a128:8", "const:4:8"]]
+ 00c3a128 ["CALLIND", null, ["register:0:8"]]
- 00c39134 bytes 40013fd6
+ 00c3a128 bytes 40013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06ed2a30062abe34826ee3d62816d91"></a>

### [`00c393c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md) → [`00c3a3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a3bc.md) FUN_00c3a3bc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39410) · [`00c39430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39430) · [`00c39488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39488)
- 新版 [`00c3a404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a3bc.md#insn-00c3a404) · [`00c3a424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a3bc.md#insn-00c3a424) · [`00c3a47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a3bc.md#insn-00c3a47c)

~~~diff
- 00c39410 ["INT_ADD", "register:40f0:8", ["const:c39410:8", "const:4:8"]]
- 00c39410 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a404 ["INT_ADD", "register:40f0:8", ["const:c3a404:8", "const:4:8"]]
+ 00c3a404 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39410 bytes 44890094
+ 00c3a404 bytes 3b890094
- 00c39430 ["INT_ADD", "register:40f0:8", ["const:c39430:8", "const:4:8"]]
- 00c39430 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a424 ["INT_ADD", "register:40f0:8", ["const:c3a424:8", "const:4:8"]]
+ 00c3a424 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39430 bytes 3c890094
+ 00c3a424 bytes 33890094
- 00c39488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c39488 ["INT_ADD", "register:40f0:8", ["const:c39488:8", "const:4:8"]]
- 00c39488 ["CALLIND", null, ["register:0:8"]]
+ 00c3a47c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3a47c ["INT_ADD", "register:40f0:8", ["const:c3a47c:8", "const:4:8"]]
+ 00c3a47c ["CALLIND", null, ["register:0:8"]]
- 00c39488 bytes 00013fd6
+ 00c3a47c bytes 00013fd6
~~~


