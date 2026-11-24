# v16.0.2 → v16.0.3 · 要調査の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-024252ba57097dec7287af5afc9c2fc7"></a>

### [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) → [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md) FUN_0056d1ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) · 呼出先 2件 [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)
- 新版 呼出元 4件 [`00565db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md) [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) [`0056cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056cdc0.md) [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md) · 呼出先 2件 [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md) [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md#insn-0056ced0) · [`0056cf2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md#insn-0056cf2c) · [`0056cfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md#insn-0056cfa0)
- 新版 [`0056d1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md#insn-0056d1f0) · [`0056d24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md#insn-0056d24c) · [`0056d2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md#insn-0056d2c0)

~~~diff
- 0056ced0 ["INT_ADD", "register:40f0:8", ["const:56ced0:8", "const:4:8"]]
- 0056ced0 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056d1f0 ["INT_ADD", "register:40f0:8", ["const:56d1f0:8", "const:4:8"]]
+ 0056d1f0 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056ced0 bytes 77000094
+ 0056d1f0 bytes 77000094
- 0056cf2c ["INT_ADD", "register:40f0:8", ["const:56cf2c:8", "const:4:8"]]
- 0056cf2c ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056d24c ["INT_ADD", "register:40f0:8", ["const:56d24c:8", "const:4:8"]]
+ 0056d24c ["CALL", null, ["callee:0056d3cc:8"]]
- 0056cf2c bytes 60000094
+ 0056d24c bytes 60000094
- 0056cfa0 ["INT_ADD", "register:40f0:8", ["const:56cfa0:8", "const:4:8"]]
- 0056cfa0 ["CALL", null, ["local:b0:8"]]
+ 0056d2c0 ["INT_ADD", "register:40f0:8", ["const:56d2c0:8", "const:4:8"]]
+ 0056d2c0 ["CALL", null, ["local:b0:8"]]
- 0056cfa0 bytes bbffff97
+ 0056d2c0 bytes bbffff97
~~~


<a id="compare-9289c0d39566fef314b4423e87070fba"></a>

### [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) → [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) FUN_0056d3cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) · 呼出先 2件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)
- 新版 呼出元 10件 [`00565db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md) [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) [`00568cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00568/00568cdc.md) [`0056cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056cdc0.md) [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md) · 呼出先 2件 [`0056d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md) [`00c5b110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md#insn-0056d110) · [`0056d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md#insn-0056d1b0)
- 新版 [`0056d430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md#insn-0056d430) · [`0056d4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md#insn-0056d4d0)

~~~diff
- 0056d110 ["INT_ADD", "register:40f0:8", ["const:56d110:8", "const:4:8"]]
- 0056d110 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d430 ["INT_ADD", "register:40f0:8", ["const:56d430:8", "const:4:8"]]
+ 0056d430 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d110 bytes 0cb41b94
+ 0056d430 bytes 38b71b94
- 0056d1b0 ["INT_ADD", "register:40f0:8", ["const:56d1b0:8", "const:4:8"]]
- 0056d1b0 ["CALL", null, ["callee:0056d640:8"]]
+ 0056d4d0 ["INT_ADD", "register:40f0:8", ["const:56d4d0:8", "const:4:8"]]
+ 0056d4d0 ["CALL", null, ["callee:0056d640:8"]]
- 0056d1b0 bytes 5c000094
+ 0056d4d0 bytes 5c000094
~~~


<a id="compare-26f5bfdd14fcd1230ed9adb817277c9d"></a>

### [`0056d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d1ec.md) → [`0056d50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d50c.md) FUN_0056d50c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 1件 [`0056d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d1ec.md#insn-0056d274)
- 新版 [`0056d594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d50c.md#insn-0056d594)

~~~diff
- 0056d274 ["INT_ADD", "register:40f0:8", ["const:56d274:8", "const:4:8"]]
- 0056d274 ["CALL", null, ["callee:0056d640:8"]]
+ 0056d594 ["INT_ADD", "register:40f0:8", ["const:56d594:8", "const:4:8"]]
+ 0056d594 ["CALL", null, ["callee:0056d640:8"]]
- 0056d274 bytes 2b000094
+ 0056d594 bytes 2b000094
~~~


<a id="compare-c2d2a42808bb277277ecf65cd62cc6d3"></a>

### [`0056d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d2b0.md) → [`0056d5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d5d0.md) FUN_0056d5d0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) · 呼出先 1件 [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)
- 新版 呼出元 2件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) [`00569694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00569/00569694.md) · 呼出先 1件 [`00c5b110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d2b0.md#insn-0056d2e8)
- 新版 [`0056d608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d5d0.md#insn-0056d608)

~~~diff
- 0056d2e8 ["INT_ADD", "register:40f0:8", ["const:56d2e8:8", "const:4:8"]]
- 0056d2e8 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d608 ["INT_ADD", "register:40f0:8", ["const:56d608:8", "const:4:8"]]
+ 0056d608 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d2e8 bytes 96b31b94
+ 0056d608 bytes c2b61b94
~~~


<a id="compare-db2441d6a4fca2dd778b97fef7e87ee5"></a>

### [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) → [`0056d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md) FUN_0056d640

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d1ec.md) · 呼出先 2件 [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)
- 新版 呼出元 6件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) [`00568cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00568/00568cdc.md) [`00569694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00569/00569694.md) [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) [`0056d50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d50c.md) · 呼出先 2件 [`0056d798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d798.md) [`00c5b110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md#insn-0056d360) · [`0056d3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md#insn-0056d3a8) · [`0056d3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md#insn-0056d3f0)
- 新版 [`0056d680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md#insn-0056d680) · [`0056d6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md#insn-0056d6c8) · [`0056d710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md#insn-0056d710)

~~~diff
- 0056d360 ["INT_ADD", "register:40f0:8", ["const:56d360:8", "const:4:8"]]
- 0056d360 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d680 ["INT_ADD", "register:40f0:8", ["const:56d680:8", "const:4:8"]]
+ 0056d680 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d360 bytes 78b31b94
+ 0056d680 bytes a4b61b94
- 0056d3a8 ["INT_ADD", "register:40f0:8", ["const:56d3a8:8", "const:4:8"]]
- 0056d3a8 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d6c8 ["INT_ADD", "register:40f0:8", ["const:56d6c8:8", "const:4:8"]]
+ 0056d6c8 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d3a8 bytes 66b31b94
+ 0056d6c8 bytes 92b61b94
- 0056d3f0 ["INT_ADD", "register:40f0:8", ["const:56d3f0:8", "const:4:8"]]
- 0056d3f0 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d710 ["INT_ADD", "register:40f0:8", ["const:56d710:8", "const:4:8"]]
+ 0056d710 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d3f0 bytes 54b31b94
+ 0056d710 bytes 80b61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28ef85687bc2c66736bd57a306603a1"></a>

### [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) → [`0056db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md) FUN_0056db34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) · 呼出先 1件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)
- 新版 呼出元 4件 [`00565db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md) [`0056dcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md) [`0056f2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f2b0.md) [`0056f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f504.md) · 呼出先 1件 [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md#insn-0056d850)
- 新版 [`0056db70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md#insn-0056db70)

~~~diff
- 0056d850 ["INT_ADD", "register:40f0:8", ["const:56d850:8", "const:4:8"]]
- 0056d850 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056db70 ["INT_ADD", "register:40f0:8", ["const:56db70:8", "const:4:8"]]
+ 0056db70 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056d850 bytes 17feff97
+ 0056db70 bytes 17feff97
~~~


<a id="compare-a3066156bfb85054393e859b93231de5"></a>

### [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) → [`0056dcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md) FUN_0056dcdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) · 呼出先 6件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00565db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md) · 呼出先 6件 [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) [`0056db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md) [`0056f2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f2b0.md) [`0056f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f504.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md#insn-0056db40) · [`0056dcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md#insn-0056dcbc) · [`0056de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md#insn-0056de30)
- 新版 [`0056de60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md#insn-0056de60) · [`0056dfdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md#insn-0056dfdc) · [`0056e150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md#insn-0056e150)

~~~diff
- 0056db40 ["INT_ADD", "register:40f0:8", ["const:56db40:8", "const:4:8"]]
- 0056db40 ["CALL", null, ["callee:00c59130:8"]]
+ 0056de60 ["INT_ADD", "register:40f0:8", ["const:56de60:8", "const:4:8"]]
+ 0056de60 ["CALL", null, ["callee:00c59130:8"]]
- 0056db40 bytes 88a91b94
+ 0056de60 bytes b4ac1b94
- 0056dcbc ["INT_ADD", "register:40f0:8", ["const:56dcbc:8", "const:4:8"]]
- 0056dcbc ["CALL", null, ["callee:0056f504:8"]]
+ 0056dfdc ["INT_ADD", "register:40f0:8", ["const:56dfdc:8", "const:4:8"]]
+ 0056dfdc ["CALL", null, ["callee:0056f504:8"]]
- 0056dcbc bytes 4a050094
+ 0056dfdc bytes 4a050094
- 0056de30 ["INT_ADD", "register:40f0:8", ["const:56de30:8", "const:4:8"]]
- 0056de30 ["CALL", null, ["callee:0056f504:8"]]
+ 0056e150 ["INT_ADD", "register:40f0:8", ["const:56e150:8", "const:4:8"]]
+ 0056e150 ["CALL", null, ["callee:0056f504:8"]]
- 0056de30 bytes ed040094
+ 0056e150 bytes ed040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f0d834cd53d0a8afc13538ae3916619"></a>

### [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) → [`0056f2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f2b0.md) FUN_0056f2b0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) · 呼出先 2件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md)
- 新版 呼出元 1件 [`0056dcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md) · 呼出先 2件 [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) [`0056db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md#insn-0056f02c) · [`0056f09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md#insn-0056f09c)
- 新版 [`0056f34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f2b0.md#insn-0056f34c) · [`0056f3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f2b0.md#insn-0056f3bc)

~~~diff
- 0056f02c ["INT_ADD", "register:40f0:8", ["const:56f02c:8", "const:4:8"]]
- 0056f02c ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056f34c ["INT_ADD", "register:40f0:8", ["const:56f34c:8", "const:4:8"]]
+ 0056f34c ["CALL", null, ["callee:0056d3cc:8"]]
- 0056f02c bytes 20f8ff97
+ 0056f34c bytes 20f8ff97
- 0056f09c ["INT_ADD", "register:40f0:8", ["const:56f09c:8", "const:4:8"]]
- 0056f09c ["CALL", null, ["callee:0056db34:8"]]
+ 0056f3bc ["INT_ADD", "register:40f0:8", ["const:56f3bc:8", "const:4:8"]]
+ 0056f3bc ["CALL", null, ["callee:0056db34:8"]]
- 0056f09c bytes def9ff97
+ 0056f3bc bytes def9ff97
~~~


<a id="compare-2730e4fa6dbc5ee73bc961df02db8b04"></a>

### [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) → [`0056f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f504.md) FUN_0056f504

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) · 呼出先 2件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md)
- 新版 呼出元 1件 [`0056dcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md) · 呼出先 2件 [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) [`0056db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md#insn-0056f228) · [`0056f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md#insn-0056f2a8)
- 新版 [`0056f548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f504.md#insn-0056f548) · [`0056f5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f504.md#insn-0056f5c8)

~~~diff
- 0056f228 ["INT_ADD", "register:40f0:8", ["const:56f228:8", "const:4:8"]]
- 0056f228 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056f548 ["INT_ADD", "register:40f0:8", ["const:56f548:8", "const:4:8"]]
+ 0056f548 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056f228 bytes a1f7ff97
+ 0056f548 bytes a1f7ff97
- 0056f2a8 ["INT_ADD", "register:40f0:8", ["const:56f2a8:8", "const:4:8"]]
- 0056f2a8 ["CALL", null, ["callee:0056db34:8"]]
+ 0056f5c8 ["INT_ADD", "register:40f0:8", ["const:56f5c8:8", "const:4:8"]]
+ 0056f5c8 ["CALL", null, ["callee:0056db34:8"]]
- 0056f2a8 bytes 5bf9ff97
+ 0056f5c8 bytes 5bf9ff97
~~~


<a id="compare-2ddcc294d1ffac8ed3065efe8e58c196"></a>

### [`0056f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f578.md) → [`0056f898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f898.md) FUN_0056f898

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 1件 [`0056d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f578.md#insn-0056f598)
- 新版 [`0056f8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f898.md#insn-0056f8b8)

~~~diff
- 0056f598 ["INT_ADD", "register:40f0:8", ["const:56f598:8", "const:4:8"]]
- 0056f598 ["CALL", null, ["callee:0056d640:8"]]
+ 0056f8b8 ["INT_ADD", "register:40f0:8", ["const:56f8b8:8", "const:4:8"]]
+ 0056f8b8 ["CALL", null, ["callee:0056d640:8"]]
- 0056f598 bytes 62f7ff97
+ 0056f8b8 bytes 62f7ff97
~~~


<a id="compare-55e2a992eebad8ca7685c4fee879cd45"></a>

### [`0056f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f5d8.md) → [`0056f8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f8f8.md) FUN_0056f8f8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 1件 [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f5d8.md#insn-0056f5e8) · [`0056f5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f5d8.md#insn-0056f5f8) · [`0056f608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f5d8.md#insn-0056f608)
- 新版 [`0056f908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f8f8.md#insn-0056f908) · [`0056f918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f8f8.md#insn-0056f918) · [`0056f928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f8f8.md#insn-0056f928)

~~~diff
- 0056f5e8 ["INT_ADD", "register:40f0:8", ["const:56f5e8:8", "const:4:8"]]
- 0056f5e8 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056f908 ["INT_ADD", "register:40f0:8", ["const:56f908:8", "const:4:8"]]
+ 0056f908 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056f5e8 bytes b1f6ff97
+ 0056f908 bytes b1f6ff97
- 0056f5f8 ["INT_ADD", "register:40f0:8", ["const:56f5f8:8", "const:4:8"]]
- 0056f5f8 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056f918 ["INT_ADD", "register:40f0:8", ["const:56f918:8", "const:4:8"]]
+ 0056f918 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056f5f8 bytes adf6ff97
+ 0056f918 bytes adf6ff97
- 0056f608 ["INT_ADD", "register:40f0:8", ["const:56f608:8", "const:4:8"]]
- 0056f608 ["CALL", null, ["callee:0056d3cc:8"]]
+ 0056f928 ["INT_ADD", "register:40f0:8", ["const:56f928:8", "const:4:8"]]
+ 0056f928 ["CALL", null, ["callee:0056d3cc:8"]]
- 0056f608 bytes a9f6ff97
+ 0056f928 bytes a9f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a68dd72052d7a96cf74207b260f477"></a>

### [`0056f684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f684.md) → [`0056f9a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f9a4.md) FUN_0056f9a4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 2件 [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 2件 [`00c5b0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0f0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f684.md#insn-0056f6d0)
- 新版 [`0056f9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056f9a4.md#insn-0056f9f0)

~~~diff
- 0056f6d0 ["INT_ADD", "register:40f0:8", ["const:56f6d0:8", "const:4:8"]]
- 0056f6d0 ["CALL", null, ["callee:00c5b0f0:8"]]
+ 0056f9f0 ["INT_ADD", "register:40f0:8", ["const:56f9f0:8", "const:4:8"]]
+ 0056f9f0 ["CALL", null, ["callee:00c5b0f0:8"]]
- 0056f6d0 bytes 94aa1b94
+ 0056f9f0 bytes c0ad1b94
~~~


<a id="compare-46fc6bd463492cf727337268547648e5"></a>

### [`0056fc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fc3c.md) → [`0056ff5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056ff5c.md) FUN_0056ff5c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 1件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fc3c.md#insn-0056fc5c)
- 新版 [`0056ff7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056f/0056ff5c.md#insn-0056ff7c)

~~~diff
- 0056fc5c ["INT_ADD", "register:40f0:8", ["const:56fc5c:8", "const:4:8"]]
- 0056fc5c ["CALL", null, ["callee:00c59130:8"]]
+ 0056ff7c ["INT_ADD", "register:40f0:8", ["const:56ff7c:8", "const:4:8"]]
+ 0056ff7c ["CALL", null, ["callee:00c59130:8"]]
- 0056fc5c bytes 41a11b94
+ 0056ff7c bytes 6da41b94
~~~


<a id="compare-9c25f88c900cd746376a59a883f83a09"></a>

### [`0056fd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fd08.md) → [`00570028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570028.md) FUN_00570028

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 3件 [`00c58510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58510.md) [`00c5a0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0b0.md) [`00c5a1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1e0.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 3件 [`00c594e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594e0.md) [`00c5b080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b080.md) [`00c5b1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fd2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fd08.md#insn-0056fd2c) · [`0056fd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fd08.md#insn-0056fd38) · [`0056fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fd08.md#insn-0056fd60)
- 新版 [`0057004c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570028.md#insn-0057004c) · [`00570058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570028.md#insn-00570058) · [`00570080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570028.md#insn-00570080)

~~~diff
- 0056fd2c ["INT_ADD", "register:40f0:8", ["const:56fd2c:8", "const:4:8"]]
- 0056fd2c ["CALL", null, ["callee:00c5b080:8"]]
+ 0057004c ["INT_ADD", "register:40f0:8", ["const:57004c:8", "const:4:8"]]
+ 0057004c ["CALL", null, ["callee:00c5b080:8"]]
- 0056fd2c bytes e1a81b94
+ 0057004c bytes 0dac1b94
- 0056fd38 ["INT_ADD", "register:40f0:8", ["const:56fd38:8", "const:4:8"]]
- 0056fd38 ["CALL", null, ["callee:00c5b1b0:8"]]
+ 00570058 ["INT_ADD", "register:40f0:8", ["const:570058:8", "const:4:8"]]
+ 00570058 ["CALL", null, ["callee:00c5b1b0:8"]]
- 0056fd38 bytes 2aa91b94
+ 00570058 bytes 56ac1b94
- 0056fd60 ["INT_ADD", "register:40f0:8", ["const:56fd60:8", "const:4:8"]]
- 0056fd60 ["CALL", null, ["callee:00c594e0:8"]]
+ 00570080 ["INT_ADD", "register:40f0:8", ["const:570080:8", "const:4:8"]]
+ 00570080 ["CALL", null, ["callee:00c594e0:8"]]
- 0056fd60 bytes eca11b94
+ 00570080 bytes 18a51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd16a6052a9de2c044810833ea02350d"></a>

### [`00570988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570988.md) → [`00570ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570ca8.md) FUN_00570ca8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0e0.md) [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)
- 新版 呼出元 1件 [`00568cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00568/00568cdc.md) · 呼出先 6件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0b0.md) [`00c5b0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0f0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005709e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570988.md#insn-005709e0) · [`00570a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570988.md#insn-00570a30) · [`00570ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570988.md#insn-00570ac4)
- 新版 [`00570d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570ca8.md#insn-00570d00) · [`00570d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570ca8.md#insn-00570d50) · [`00570de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570ca8.md#insn-00570de4)

~~~diff
- 005709e0 ["INT_ADD", "register:40f0:8", ["const:5709e0:8", "const:4:8"]]
- 005709e0 ["CALL", null, ["callee:00c5b0f0:8"]]
+ 00570d00 ["INT_ADD", "register:40f0:8", ["const:570d00:8", "const:4:8"]]
+ 00570d00 ["CALL", null, ["callee:00c5b0f0:8"]]
- 005709e0 bytes d0a51b94
+ 00570d00 bytes fca81b94
- 00570a30 ["INT_ADD", "register:40f0:8", ["const:570a30:8", "const:4:8"]]
- 00570a30 ["CALL", null, ["callee:00c5b120:8"]]
+ 00570d50 ["INT_ADD", "register:40f0:8", ["const:570d50:8", "const:4:8"]]
+ 00570d50 ["CALL", null, ["callee:00c5b120:8"]]
- 00570a30 bytes c8a51b94
+ 00570d50 bytes f4a81b94
- 00570ac4 ["INT_ADD", "register:40f0:8", ["const:570ac4:8", "const:4:8"]]
- 00570ac4 ["CALL", null, ["callee:00c5b1d0:8"]]
+ 00570de4 ["INT_ADD", "register:40f0:8", ["const:570de4:8", "const:4:8"]]
+ 00570de4 ["CALL", null, ["callee:00c5b1d0:8"]]
- 00570ac4 bytes cfa51b94
+ 00570de4 bytes fba81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d825112e75722b0c743ebc39a1158d0"></a>

### [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md) → [`005711a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md) FUN_005711a4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00570fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0056aec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00571300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571300.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md#insn-00570ef0) · [`00570f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md#insn-00570f1c) · [`00570f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md#insn-00570f7c)
- 新版 [`00571210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md#insn-00571210) · [`0057123c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md#insn-0057123c) · [`0057129c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md#insn-0057129c)

~~~diff
- 00570ef0 ["INT_ADD", "register:40f0:8", ["const:570ef0:8", "const:4:8"]]
- 00570ef0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00571210 ["INT_ADD", "register:40f0:8", ["const:571210:8", "const:4:8"]]
+ 00571210 ["CALL", null, ["callee:00c58f30:8"]]
- 00570ef0 bytes 1c9c1b94
+ 00571210 bytes 489f1b94
- 00570f1c ["INT_ADD", "register:40f0:8", ["const:570f1c:8", "const:4:8"]]
- 00570f1c ["CALL", null, ["callee:00c54d60:8"]]
+ 0057123c ["INT_ADD", "register:40f0:8", ["const:57123c:8", "const:4:8"]]
+ 0057123c ["CALL", null, ["callee:00c54d60:8"]]
- 00570f1c bytes 958b1b94
+ 0057123c bytes c98e1b94
- 00570f7c ["INT_ADD", "register:40f0:8", ["const:570f7c:8", "const:4:8"]]
- 00570f7c ["CALL", null, ["callee:00c54d90:8"]]
+ 0057129c ["INT_ADD", "register:40f0:8", ["const:57129c:8", "const:4:8"]]
+ 0057129c ["CALL", null, ["callee:00c54d90:8"]]
- 00570f7c bytes 898b1b94
+ 0057129c bytes bd8e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-964c0baf9186cd53fe6022711a7f3e7b"></a>

### [`005710b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md) → [`005713d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005713d4.md) FUN_005713d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056ba30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056ba30.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005710c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md#insn-005710c8) · [`005710dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md#insn-005710dc) · [`005710fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md#insn-005710fc)
- 新版 [`005713e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005713d4.md#insn-005713e8) · [`005713fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005713d4.md#insn-005713fc) · [`0057141c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005713d4.md#insn-0057141c)

~~~diff
- 005710c8 ["INT_ADD", "register:40f0:8", ["const:5710c8:8", "const:4:8"]]
- 005710c8 ["CALL", null, ["callee:0056ba30:8"]]
+ 005713e8 ["INT_ADD", "register:40f0:8", ["const:5713e8:8", "const:4:8"]]
+ 005713e8 ["CALL", null, ["callee:0056ba30:8"]]
- 005710c8 bytes 92e9ff97
+ 005713e8 bytes 92e9ff97
- 005710dc ["INT_ADD", "register:40f0:8", ["const:5710dc:8", "const:4:8"]]
- 005710dc ["CALL", null, ["callee:00c54d90:8"]]
+ 005713fc ["INT_ADD", "register:40f0:8", ["const:5713fc:8", "const:4:8"]]
+ 005713fc ["CALL", null, ["callee:00c54d90:8"]]
- 005710dc bytes 318b1b94
+ 005713fc bytes 658e1b94
- 005710fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005710fc ["INT_ADD", "register:40f0:8", ["const:5710fc:8", "const:4:8"]]
- 005710fc ["CALLIND", null, ["register:0:8"]]
+ 0057141c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057141c ["INT_ADD", "register:40f0:8", ["const:57141c:8", "const:4:8"]]
+ 0057141c ["CALLIND", null, ["register:0:8"]]
- 005710fc bytes 00013fd6
+ 0057141c bytes 00013fd6
~~~


<a id="compare-0f6fce18761479321356e694ef9cc8cf"></a>

### [`005711f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md) → [`00571514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571514.md) FUN_00571514

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056ba30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056ba30.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md#insn-00571208) · [`0057121c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md#insn-0057121c) · [`0057123c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md#insn-0057123c)
- 新版 [`00571528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571514.md#insn-00571528) · [`0057153c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571514.md#insn-0057153c) · [`0057155c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571514.md#insn-0057155c)

~~~diff
- 00571208 ["INT_ADD", "register:40f0:8", ["const:571208:8", "const:4:8"]]
- 00571208 ["CALL", null, ["callee:0056ba30:8"]]
+ 00571528 ["INT_ADD", "register:40f0:8", ["const:571528:8", "const:4:8"]]
+ 00571528 ["CALL", null, ["callee:0056ba30:8"]]
- 00571208 bytes 42e9ff97
+ 00571528 bytes 42e9ff97
- 0057121c ["INT_ADD", "register:40f0:8", ["const:57121c:8", "const:4:8"]]
- 0057121c ["CALL", null, ["callee:00c54d90:8"]]
+ 0057153c ["INT_ADD", "register:40f0:8", ["const:57153c:8", "const:4:8"]]
+ 0057153c ["CALL", null, ["callee:00c54d90:8"]]
- 0057121c bytes e18a1b94
+ 0057153c bytes 158e1b94
- 0057123c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057123c ["INT_ADD", "register:40f0:8", ["const:57123c:8", "const:4:8"]]
- 0057123c ["CALLIND", null, ["register:0:8"]]
+ 0057155c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057155c ["INT_ADD", "register:40f0:8", ["const:57155c:8", "const:4:8"]]
+ 0057155c ["CALLIND", null, ["register:0:8"]]
- 0057123c bytes 00013fd6
+ 0057155c bytes 00013fd6
~~~


<a id="compare-44f3fcba544966de5bc2513cebbf26b6"></a>

### [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) → [`00571b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md) FUN_00571b60

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509cc.md) · 呼出先 8件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550cec.md) · 呼出先 8件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md#insn-00571860) · [`00571868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md#insn-00571868) · [`005718ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md#insn-005718ac)
- 新版 [`00571b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md#insn-00571b80) · [`00571b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md#insn-00571b88) · [`00571bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md#insn-00571bcc)

~~~diff
- 00571860 ["INT_ADD", "register:40f0:8", ["const:571860:8", "const:4:8"]]
- 00571860 ["CALL", null, ["callee:005891cc:8"]]
+ 00571b80 ["INT_ADD", "register:40f0:8", ["const:571b80:8", "const:4:8"]]
+ 00571b80 ["CALL", null, ["callee:005891cc:8"]]
- 00571860 bytes 935d0094
+ 00571b80 bytes 935d0094
- 00571868 ["INT_ADD", "register:40f0:8", ["const:571868:8", "const:4:8"]]
- 00571868 ["CALL", null, ["callee:005894bc:8"]]
+ 00571b88 ["INT_ADD", "register:40f0:8", ["const:571b88:8", "const:4:8"]]
+ 00571b88 ["CALL", null, ["callee:005894bc:8"]]
- 00571868 bytes 4d5e0094
+ 00571b88 bytes 4d5e0094
- 005718ac ["INT_ADD", "register:40f0:8", ["const:5718ac:8", "const:4:8"]]
- 005718ac ["CALL", null, ["callee:00589680:8"]]
+ 00571bcc ["INT_ADD", "register:40f0:8", ["const:571bcc:8", "const:4:8"]]
+ 00571bcc ["CALL", null, ["callee:00589680:8"]]
- 005718ac bytes ad5e0094
+ 00571bcc bytes ad5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b61bde59bbd2bc3c883f6ea5e462e2"></a>

### [`005728a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728a4.md) → [`00572bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572bc4.md) FUN_00572bc4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005728c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728a4.md#insn-005728c0) · [`005728e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728a4.md#insn-005728e0)
- 新版 [`00572be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572bc4.md#insn-00572be0) · [`00572c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572bc4.md#insn-00572c00)

~~~diff
- 005728c0 ["INT_ADD", "register:40f0:8", ["const:5728c0:8", "const:4:8"]]
- 005728c0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00572be0 ["INT_ADD", "register:40f0:8", ["const:572be0:8", "const:4:8"]]
+ 00572be0 ["CALL", null, ["callee:00c54d90:8"]]
- 005728c0 bytes 38851b94
+ 00572be0 bytes 6c881b94
- 005728e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005728e0 ["INT_ADD", "register:40f0:8", ["const:5728e0:8", "const:4:8"]]
- 005728e0 ["CALLIND", null, ["register:0:8"]]
+ 00572c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572c00 ["INT_ADD", "register:40f0:8", ["const:572c00:8", "const:4:8"]]
+ 00572c00 ["CALLIND", null, ["register:0:8"]]
- 005728e0 bytes 00013fd6
+ 00572c00 bytes 00013fd6
~~~


<a id="compare-079d97425a182b51d8329a0e35b5a184"></a>

### [`00574464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md) → [`00574784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574784.md) FUN_00574784

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574a88.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057448c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md#insn-0057448c) · [`005744b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md#insn-005744b0)
- 新版 [`005747ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574784.md#insn-005747ac) · [`005747d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574784.md#insn-005747d0)

~~~diff
- 0057448c ["INT_ADD", "register:40f0:8", ["const:57448c:8", "const:4:8"]]
- 0057448c ["CALL", null, ["callee:00574a88:8"]]
+ 005747ac ["INT_ADD", "register:40f0:8", ["const:5747ac:8", "const:4:8"]]
+ 005747ac ["CALL", null, ["callee:00574a88:8"]]
- 0057448c bytes b7000094
+ 005747ac bytes b7000094
- 005744b0 ["INT_ADD", "register:40f0:8", ["const:5744b0:8", "const:4:8"]]
- 005744b0 ["CALL", null, ["callee:00c58f80:8"]]
+ 005747d0 ["INT_ADD", "register:40f0:8", ["const:5747d0:8", "const:4:8"]]
+ 005747d0 ["CALL", null, ["callee:00c58f80:8"]]
- 005744b0 bytes c08e1b94
+ 005747d0 bytes ec911b94
~~~


<a id="compare-4a12c2ff7fa6a89009a1bb5cfb0ea07e"></a>

### [`00574848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md) → [`00574b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b68.md) FUN_00574b68

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574e2c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md#insn-00574870) · [`00574894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md#insn-00574894)
- 新版 [`00574b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b68.md#insn-00574b90) · [`00574bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b68.md#insn-00574bb4)

~~~diff
- 00574870 ["INT_ADD", "register:40f0:8", ["const:574870:8", "const:4:8"]]
- 00574870 ["CALL", null, ["callee:00574e2c:8"]]
+ 00574b90 ["INT_ADD", "register:40f0:8", ["const:574b90:8", "const:4:8"]]
+ 00574b90 ["CALL", null, ["callee:00574e2c:8"]]
- 00574870 bytes a7000094
+ 00574b90 bytes a7000094
- 00574894 ["INT_ADD", "register:40f0:8", ["const:574894:8", "const:4:8"]]
- 00574894 ["CALL", null, ["callee:00c58f80:8"]]
+ 00574bb4 ["INT_ADD", "register:40f0:8", ["const:574bb4:8", "const:4:8"]]
+ 00574bb4 ["CALL", null, ["callee:00c58f80:8"]]
- 00574894 bytes c78d1b94
+ 00574bb4 bytes f3901b94
~~~


<a id="compare-3332353b70dd2f71b67fa4c60ff62545"></a>

### [`00574aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574aac.md) → [`00574dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574dcc.md) FUN_00574dcc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574aac.md#insn-00574ac8)
- 新版 [`00574de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574dcc.md#insn-00574de8)

~~~diff
- 00574ac8 ["INT_ADD", "register:40f0:8", ["const:574ac8:8", "const:4:8"]]
- 00574ac8 ["CALL", null, ["callee:00c54d60:8"]]
+ 00574de8 ["INT_ADD", "register:40f0:8", ["const:574de8:8", "const:4:8"]]
+ 00574de8 ["CALL", null, ["callee:00c54d60:8"]]
- 00574ac8 bytes aa7c1b94
+ 00574de8 bytes de7f1b94
~~~


<a id="compare-c91a88385f98b5e7b837afd76729f95a"></a>

### [`00574ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574ad4.md) → [`00574df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574df4.md) FUN_00574df4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574ad4.md#insn-00574af0)
- 新版 [`00574e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574df4.md#insn-00574e10)

~~~diff
- 00574af0 ["INT_ADD", "register:40f0:8", ["const:574af0:8", "const:4:8"]]
- 00574af0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00574e10 ["INT_ADD", "register:40f0:8", ["const:574e10:8", "const:4:8"]]
+ 00574e10 ["CALL", null, ["callee:00c54d60:8"]]
- 00574af0 bytes a07c1b94
+ 00574e10 bytes d47f1b94
~~~


<a id="compare-d41773587b13dd35f0263b9892253cb5"></a>

### [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) → [`00574fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md) FUN_00574fdc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00571838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571838.md) [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) · 呼出先 2件 [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00571b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b58.md) [`00574fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md) · 呼出先 2件 [`00574fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md#insn-00574cd8) · [`00574ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md#insn-00574ce4) · [`00574d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md#insn-00574d18)
- 新版 [`00574ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md#insn-00574ff8) · [`00575004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md#insn-00575004) · [`00575038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574fdc.md#insn-00575038)

~~~diff
- 00574cd8 ["INT_ADD", "register:40f0:8", ["const:574cd8:8", "const:4:8"]]
- 00574cd8 ["CALL", null, ["local:b0:8"]]
+ 00574ff8 ["INT_ADD", "register:40f0:8", ["const:574ff8:8", "const:4:8"]]
+ 00574ff8 ["CALL", null, ["local:b0:8"]]
- 00574cd8 bytes f9ffff97
+ 00574ff8 bytes f9ffff97
- 00574ce4 ["INT_ADD", "register:40f0:8", ["const:574ce4:8", "const:4:8"]]
- 00574ce4 ["CALL", null, ["local:b0:8"]]
+ 00575004 ["INT_ADD", "register:40f0:8", ["const:575004:8", "const:4:8"]]
+ 00575004 ["CALL", null, ["local:b0:8"]]
- 00574ce4 bytes f6ffff97
+ 00575004 bytes f6ffff97
- 00574d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574d18 ["INT_ADD", "register:40f0:8", ["const:574d18:8", "const:4:8"]]
- 00574d18 ["CALLIND", null, ["register:0:8"]]
+ 00575038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575038 ["INT_ADD", "register:40f0:8", ["const:575038:8", "const:4:8"]]
+ 00575038 ["CALLIND", null, ["register:0:8"]]
- 00574d18 bytes 00013fd6
+ 00575038 bytes 00013fd6
~~~


<a id="compare-f3725c91de9e6295a8c9b3d5d0a513b7"></a>

### [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) → [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) FUN_0057504c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 96件 [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 96件 [`00571e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571e54.md) [`00572178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572178.md) [`00572458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md) [`0057260c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md) [`005727c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md#insn-00574da0) · [`00574dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md#insn-00574dc4)
- 新版 [`005750c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md#insn-005750c0) · [`005750e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md#insn-005750e4)

~~~diff
- 00574da0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574da0 ["INT_ADD", "register:40f0:8", ["const:574da0:8", "const:4:8"]]
- 00574da0 ["CALLIND", null, ["register:0:8"]]
+ 005750c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005750c0 ["INT_ADD", "register:40f0:8", ["const:5750c0:8", "const:4:8"]]
+ 005750c0 ["CALLIND", null, ["register:0:8"]]
- 00574da0 bytes 00013fd6
+ 005750c0 bytes 00013fd6
- 00574dc4 ["INT_ADD", "register:40f0:8", ["const:574dc4:8", "const:4:8"]]
- 00574dc4 ["CALL", null, ["callee:00c58f80:8"]]
+ 005750e4 ["INT_ADD", "register:40f0:8", ["const:5750e4:8", "const:4:8"]]
+ 005750e4 ["CALL", null, ["callee:00c58f80:8"]]
- 00574dc4 bytes 7b8c1b94
+ 005750e4 bytes a78f1b94
~~~


<a id="compare-adbe675da35ebf23c3d7bd7f0b021cdd"></a>

### [`00574dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md) → [`005750e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005750e8.md) FUN_005750e8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`005727c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md#insn-00574e34) · [`00574e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md#insn-00574e44) · [`00574e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md#insn-00574e64)
- 新版 [`00575154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005750e8.md#insn-00575154) · [`00575164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005750e8.md#insn-00575164) · [`00575184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005750e8.md#insn-00575184)

~~~diff
- 00574e34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574e34 ["INT_ADD", "register:40f0:8", ["const:574e34:8", "const:4:8"]]
- 00574e34 ["CALLIND", null, ["register:0:8"]]
+ 00575154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575154 ["INT_ADD", "register:40f0:8", ["const:575154:8", "const:4:8"]]
+ 00575154 ["CALLIND", null, ["register:0:8"]]
- 00574e34 bytes 00013fd6
+ 00575154 bytes 00013fd6
- 00574e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574e44 ["INT_ADD", "register:40f0:8", ["const:574e44:8", "const:4:8"]]
- 00574e44 ["CALLIND", null, ["register:0:8"]]
+ 00575164 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575164 ["INT_ADD", "register:40f0:8", ["const:575164:8", "const:4:8"]]
+ 00575164 ["CALLIND", null, ["register:0:8"]]
- 00574e44 bytes 00013fd6
+ 00575164 bytes 00013fd6
- 00574e64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574e64 ["INT_ADD", "register:40f0:8", ["const:574e64:8", "const:4:8"]]
- 00574e64 ["CALLIND", null, ["register:0:8"]]
+ 00575184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575184 ["INT_ADD", "register:40f0:8", ["const:575184:8", "const:4:8"]]
+ 00575184 ["CALLIND", null, ["register:0:8"]]
- 00574e64 bytes 00013fd6
+ 00575184 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c36d71a337c6118488f467051a2d4d7f"></a>

### [`00574f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md) → [`00575250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575250.md) FUN_00575250

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00572f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572f00.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md#insn-00574f9c) · [`00574fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md#insn-00574fac) · [`00574fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md#insn-00574fcc)
- 新版 [`005752bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575250.md#insn-005752bc) · [`005752cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575250.md#insn-005752cc) · [`005752ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575250.md#insn-005752ec)

~~~diff
- 00574f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f9c ["INT_ADD", "register:40f0:8", ["const:574f9c:8", "const:4:8"]]
- 00574f9c ["CALLIND", null, ["register:0:8"]]
+ 005752bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005752bc ["INT_ADD", "register:40f0:8", ["const:5752bc:8", "const:4:8"]]
+ 005752bc ["CALLIND", null, ["register:0:8"]]
- 00574f9c bytes 00013fd6
+ 005752bc bytes 00013fd6
- 00574fac ["COPY", "register:0:8", ["register:4040:8"]]
- 00574fac ["INT_ADD", "register:40f0:8", ["const:574fac:8", "const:4:8"]]
- 00574fac ["CALLIND", null, ["register:0:8"]]
+ 005752cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005752cc ["INT_ADD", "register:40f0:8", ["const:5752cc:8", "const:4:8"]]
+ 005752cc ["CALLIND", null, ["register:0:8"]]
- 00574fac bytes 00013fd6
+ 005752cc bytes 00013fd6
- 00574fcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00574fcc ["INT_ADD", "register:40f0:8", ["const:574fcc:8", "const:4:8"]]
- 00574fcc ["CALLIND", null, ["register:0:8"]]
+ 005752ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005752ec ["INT_ADD", "register:40f0:8", ["const:5752ec:8", "const:4:8"]]
+ 005752ec ["CALLIND", null, ["register:0:8"]]
- 00574fcc bytes 00013fd6
+ 005752ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a048980b8f8433c7af2e3d08ca77de"></a>

### [`00575098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575098.md) → [`005753b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005753b8.md) FUN_005753b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005750ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575098.md#insn-005750ec) · [`00575100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575098.md#insn-00575100) · [`00575108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575098.md#insn-00575108)
- 新版 [`0057540c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005753b8.md#insn-0057540c) · [`00575420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005753b8.md#insn-00575420) · [`00575428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005753b8.md#insn-00575428)

~~~diff
- 005750ec ["INT_ADD", "register:40f0:8", ["const:5750ec:8", "const:4:8"]]
- 005750ec ["CALL", null, ["callee:00c54d90:8"]]
+ 0057540c ["INT_ADD", "register:40f0:8", ["const:57540c:8", "const:4:8"]]
+ 0057540c ["CALL", null, ["callee:00c54d90:8"]]
- 005750ec bytes 2d7b1b94
+ 0057540c bytes 617e1b94
- 00575100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00575100 ["INT_ADD", "register:40f0:8", ["const:575100:8", "const:4:8"]]
- 00575100 ["CALLIND", null, ["register:0:8"]]
+ 00575420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575420 ["INT_ADD", "register:40f0:8", ["const:575420:8", "const:4:8"]]
+ 00575420 ["CALLIND", null, ["register:0:8"]]
- 00575100 bytes 00013fd6
+ 00575420 bytes 00013fd6
- 00575108 ["INT_ADD", "register:40f0:8", ["const:575108:8", "const:4:8"]]
- 00575108 ["CALL", null, ["callee:00c58f20:8"]]
+ 00575428 ["INT_ADD", "register:40f0:8", ["const:575428:8", "const:4:8"]]
+ 00575428 ["CALL", null, ["callee:00c58f20:8"]]
- 00575108 bytes 928b1b94
+ 00575428 bytes be8e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2648993ca96567d8dcc985a82f97262"></a>

### [`00575140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575140.md) → [`00575460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575460.md) FUN_00575460

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575140.md#insn-00575150)
- 新版 [`00575470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575460.md#insn-00575470)

~~~diff
- 00575150 ["INT_ADD", "register:40f0:8", ["const:575150:8", "const:4:8"]]
- 00575150 ["CALL", null, ["callee:00c58f40:8"]]
+ 00575470 ["INT_ADD", "register:40f0:8", ["const:575470:8", "const:4:8"]]
+ 00575470 ["CALL", null, ["callee:00c58f40:8"]]
- 00575150 bytes 888b1b94
+ 00575470 bytes b48e1b94
~~~


<a id="compare-5ad6f68d1a8882f80e88c382562b92d4"></a>

### [`00575164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md) → [`00575484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575484.md) FUN_00575484

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005751b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md#insn-005751b4) · [`005751c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md#insn-005751c8) · [`005751d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md#insn-005751d0)
- 新版 [`005754d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575484.md#insn-005754d4) · [`005754e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575484.md#insn-005754e8) · [`005754f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575484.md#insn-005754f0)

~~~diff
- 005751b4 ["INT_ADD", "register:40f0:8", ["const:5751b4:8", "const:4:8"]]
- 005751b4 ["CALL", null, ["callee:00c54d90:8"]]
+ 005754d4 ["INT_ADD", "register:40f0:8", ["const:5754d4:8", "const:4:8"]]
+ 005754d4 ["CALL", null, ["callee:00c54d90:8"]]
- 005751b4 bytes fb7a1b94
+ 005754d4 bytes 2f7e1b94
- 005751c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005751c8 ["INT_ADD", "register:40f0:8", ["const:5751c8:8", "const:4:8"]]
- 005751c8 ["CALLIND", null, ["register:0:8"]]
+ 005754e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005754e8 ["INT_ADD", "register:40f0:8", ["const:5754e8:8", "const:4:8"]]
+ 005754e8 ["CALLIND", null, ["register:0:8"]]
- 005751c8 bytes 00013fd6
+ 005754e8 bytes 00013fd6
- 005751d0 ["INT_ADD", "register:40f0:8", ["const:5751d0:8", "const:4:8"]]
- 005751d0 ["CALL", null, ["callee:00c58f20:8"]]
+ 005754f0 ["INT_ADD", "register:40f0:8", ["const:5754f0:8", "const:4:8"]]
+ 005754f0 ["CALL", null, ["callee:00c58f20:8"]]
- 005751d0 bytes 608b1b94
+ 005754f0 bytes 8c8e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36e7616e847130217bd18f4a8206e08"></a>

### [`00575228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md) → [`00575548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575548.md) FUN_00575548

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00575384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005756a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756a4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md#insn-00575294) · [`005752c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md#insn-005752c0) · [`00575320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md#insn-00575320)
- 新版 [`005755b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575548.md#insn-005755b4) · [`005755e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575548.md#insn-005755e0) · [`00575640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575548.md#insn-00575640)

~~~diff
- 00575294 ["INT_ADD", "register:40f0:8", ["const:575294:8", "const:4:8"]]
- 00575294 ["CALL", null, ["callee:00c58f30:8"]]
+ 005755b4 ["INT_ADD", "register:40f0:8", ["const:5755b4:8", "const:4:8"]]
+ 005755b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00575294 bytes 338b1b94
+ 005755b4 bytes 5f8e1b94
- 005752c0 ["INT_ADD", "register:40f0:8", ["const:5752c0:8", "const:4:8"]]
- 005752c0 ["CALL", null, ["callee:00c54d60:8"]]
+ 005755e0 ["INT_ADD", "register:40f0:8", ["const:5755e0:8", "const:4:8"]]
+ 005755e0 ["CALL", null, ["callee:00c54d60:8"]]
- 005752c0 bytes ac7a1b94
+ 005755e0 bytes e07d1b94
- 00575320 ["INT_ADD", "register:40f0:8", ["const:575320:8", "const:4:8"]]
- 00575320 ["CALL", null, ["callee:00c54d90:8"]]
+ 00575640 ["INT_ADD", "register:40f0:8", ["const:575640:8", "const:4:8"]]
+ 00575640 ["CALL", null, ["callee:00c54d90:8"]]
- 00575320 bytes a07a1b94
+ 00575640 bytes d47d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300a31a09565afe47a044bd258785032"></a>

### [`00575dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md) → [`005760ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005760ec.md) FUN_005760ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`005758e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md#insn-00575e00) · [`00575e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md#insn-00575e48) · [`00575e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md#insn-00575e68)
- 新版 [`00576120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005760ec.md#insn-00576120) · [`00576168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005760ec.md#insn-00576168) · [`00576188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005760ec.md#insn-00576188)

~~~diff
- 00575e00 ["INT_ADD", "register:40f0:8", ["const:575e00:8", "const:4:8"]]
- 00575e00 ["CALL", null, ["callee:00c59080:8"]]
+ 00576120 ["INT_ADD", "register:40f0:8", ["const:576120:8", "const:4:8"]]
+ 00576120 ["CALL", null, ["callee:00c59080:8"]]
- 00575e00 bytes ac881b94
+ 00576120 bytes d88b1b94
- 00575e48 ["INT_ADD", "register:40f0:8", ["const:575e48:8", "const:4:8"]]
- 00575e48 ["CALL", null, ["callee:00c58f30:8"]]
+ 00576168 ["INT_ADD", "register:40f0:8", ["const:576168:8", "const:4:8"]]
+ 00576168 ["CALL", null, ["callee:00c58f30:8"]]
- 00575e48 bytes 46881b94
+ 00576168 bytes 728b1b94
- 00575e68 ["INT_ADD", "register:40f0:8", ["const:575e68:8", "const:4:8"]]
- 00575e68 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00576188 ["INT_ADD", "register:40f0:8", ["const:576188:8", "const:4:8"]]
+ 00576188 ["CALL", null, ["callee:00c58fe0:8"]]
- 00575e68 bytes 6a881b94
+ 00576188 bytes 968b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6db9f79b774e2894f622853002407e0"></a>

### [`00575fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md) → [`005762f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005762f8.md) FUN_005762f8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`005758e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md#insn-0057600c) · [`00576054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md#insn-00576054) · [`00576074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md#insn-00576074)
- 新版 [`0057632c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005762f8.md#insn-0057632c) · [`00576374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005762f8.md#insn-00576374) · [`00576394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005762f8.md#insn-00576394)

~~~diff
- 0057600c ["INT_ADD", "register:40f0:8", ["const:57600c:8", "const:4:8"]]
- 0057600c ["CALL", null, ["callee:00c59080:8"]]
+ 0057632c ["INT_ADD", "register:40f0:8", ["const:57632c:8", "const:4:8"]]
+ 0057632c ["CALL", null, ["callee:00c59080:8"]]
- 0057600c bytes 29881b94
+ 0057632c bytes 558b1b94
- 00576054 ["INT_ADD", "register:40f0:8", ["const:576054:8", "const:4:8"]]
- 00576054 ["CALL", null, ["callee:00c58f30:8"]]
+ 00576374 ["INT_ADD", "register:40f0:8", ["const:576374:8", "const:4:8"]]
+ 00576374 ["CALL", null, ["callee:00c58f30:8"]]
- 00576054 bytes c3871b94
+ 00576374 bytes ef8a1b94
- 00576074 ["INT_ADD", "register:40f0:8", ["const:576074:8", "const:4:8"]]
- 00576074 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00576394 ["INT_ADD", "register:40f0:8", ["const:576394:8", "const:4:8"]]
+ 00576394 ["CALL", null, ["callee:00c58fe0:8"]]
- 00576074 bytes e7871b94
+ 00576394 bytes 138b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143485316d941fa0301f418792c46078"></a>

### [`00576190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md) → [`005764b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005764b0.md) FUN_005764b0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00575810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00575b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575b30.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005761fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md#insn-005761fc) · [`0057620c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md#insn-0057620c) · [`0057622c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md#insn-0057622c)
- 新版 [`0057651c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005764b0.md#insn-0057651c) · [`0057652c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005764b0.md#insn-0057652c) · [`0057654c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005764b0.md#insn-0057654c)

~~~diff
- 005761fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005761fc ["INT_ADD", "register:40f0:8", ["const:5761fc:8", "const:4:8"]]
- 005761fc ["CALLIND", null, ["register:0:8"]]
+ 0057651c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057651c ["INT_ADD", "register:40f0:8", ["const:57651c:8", "const:4:8"]]
+ 0057651c ["CALLIND", null, ["register:0:8"]]
- 005761fc bytes 00013fd6
+ 0057651c bytes 00013fd6
- 0057620c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057620c ["INT_ADD", "register:40f0:8", ["const:57620c:8", "const:4:8"]]
- 0057620c ["CALLIND", null, ["register:0:8"]]
+ 0057652c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057652c ["INT_ADD", "register:40f0:8", ["const:57652c:8", "const:4:8"]]
+ 0057652c ["CALLIND", null, ["register:0:8"]]
- 0057620c bytes 00013fd6
+ 0057652c bytes 00013fd6
- 0057622c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057622c ["INT_ADD", "register:40f0:8", ["const:57622c:8", "const:4:8"]]
- 0057622c ["CALLIND", null, ["register:0:8"]]
+ 0057654c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057654c ["INT_ADD", "register:40f0:8", ["const:57654c:8", "const:4:8"]]
+ 0057654c ["CALLIND", null, ["register:0:8"]]
- 0057622c bytes 00013fd6
+ 0057654c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b1b511b036401006b801258ad7e89c"></a>

### [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) → [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) FUN_00576618

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) [`0057a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 26件 [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) [`00577678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md) [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) [`0057aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057aa9c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057636c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md#insn-0057636c) · [`00576390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md#insn-00576390)
- 新版 [`0057668c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md#insn-0057668c) · [`005766b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md#insn-005766b0)

~~~diff
- 0057636c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057636c ["INT_ADD", "register:40f0:8", ["const:57636c:8", "const:4:8"]]
- 0057636c ["CALLIND", null, ["register:0:8"]]
+ 0057668c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057668c ["INT_ADD", "register:40f0:8", ["const:57668c:8", "const:4:8"]]
+ 0057668c ["CALLIND", null, ["register:0:8"]]
- 0057636c bytes 00013fd6
+ 0057668c bytes 00013fd6
- 00576390 ["INT_ADD", "register:40f0:8", ["const:576390:8", "const:4:8"]]
- 00576390 ["CALL", null, ["callee:00c58f80:8"]]
+ 005766b0 ["INT_ADD", "register:40f0:8", ["const:5766b0:8", "const:4:8"]]
+ 005766b0 ["CALL", null, ["callee:00c58f80:8"]]
- 00576390 bytes 08871b94
+ 005766b0 bytes 348a1b94
~~~


<a id="compare-a013e554af45b3c560b785793f32e599"></a>

### [`00576868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576868.md) → [`00576b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576b88.md) FUN_00576b88

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00576740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00576a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a60.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00576878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576868.md#insn-00576878)
- 新版 [`00576b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576b88.md#insn-00576b98)

~~~diff
- 00576878 ["INT_ADD", "register:40f0:8", ["const:576878:8", "const:4:8"]]
- 00576878 ["CALL", null, ["callee:00576a60:8"]]
+ 00576b98 ["INT_ADD", "register:40f0:8", ["const:576b98:8", "const:4:8"]]
+ 00576b98 ["CALL", null, ["callee:00576a60:8"]]
- 00576878 bytes b2ffff97
+ 00576b98 bytes b2ffff97
~~~


<a id="compare-3cc91ff918695da1bf3ba16992486baf"></a>

### [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) → [`005773e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md) FUN_005773e0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 2件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`00577678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md) [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) · 呼出先 2件 [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005770fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md#insn-005770fc) · [`00577128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md#insn-00577128) · [`00577138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md#insn-00577138)
- 新版 [`0057741c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md#insn-0057741c) · [`00577448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md#insn-00577448) · [`00577458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md#insn-00577458)

~~~diff
- 005770fc ["COPY", "register:0:8", ["register:4048:8"]]
- 005770fc ["INT_ADD", "register:40f0:8", ["const:5770fc:8", "const:4:8"]]
- 005770fc ["CALLIND", null, ["register:0:8"]]
+ 0057741c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057741c ["INT_ADD", "register:40f0:8", ["const:57741c:8", "const:4:8"]]
+ 0057741c ["CALLIND", null, ["register:0:8"]]
- 005770fc bytes 20013fd6
+ 0057741c bytes 20013fd6
- 00577128 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577128 ["INT_ADD", "register:40f0:8", ["const:577128:8", "const:4:8"]]
- 00577128 ["CALLIND", null, ["register:0:8"]]
+ 00577448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577448 ["INT_ADD", "register:40f0:8", ["const:577448:8", "const:4:8"]]
+ 00577448 ["CALLIND", null, ["register:0:8"]]
- 00577128 bytes 00013fd6
+ 00577448 bytes 00013fd6
- 00577138 ["INT_ADD", "register:40f0:8", ["const:577138:8", "const:4:8"]]
- 00577138 ["CALL", null, ["callee:0057c208:8"]]
+ 00577458 ["INT_ADD", "register:40f0:8", ["const:577458:8", "const:4:8"]]
+ 00577458 ["CALL", null, ["callee:0057c208:8"]]
- 00577138 bytes 6c130094
+ 00577458 bytes 6c130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70ad4c4af46cc0cab7f370be0bd6e016"></a>

### [`00577308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577308.md) → [`00577628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577628.md) FUN_00577628

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00577324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577308.md#insn-00577324) · [`00577344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577308.md#insn-00577344)
- 新版 [`00577644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577628.md#insn-00577644) · [`00577664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577628.md#insn-00577664)

~~~diff
- 00577324 ["INT_ADD", "register:40f0:8", ["const:577324:8", "const:4:8"]]
- 00577324 ["CALL", null, ["callee:00c54d90:8"]]
+ 00577644 ["INT_ADD", "register:40f0:8", ["const:577644:8", "const:4:8"]]
+ 00577644 ["CALL", null, ["callee:00c54d90:8"]]
- 00577324 bytes 9f721b94
+ 00577644 bytes d3751b94
- 00577344 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577344 ["INT_ADD", "register:40f0:8", ["const:577344:8", "const:4:8"]]
- 00577344 ["CALLIND", null, ["register:0:8"]]
+ 00577664 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577664 ["INT_ADD", "register:40f0:8", ["const:577664:8", "const:4:8"]]
+ 00577664 ["CALLIND", null, ["register:0:8"]]
- 00577344 bytes 00013fd6
+ 00577664 bytes 00013fd6
~~~


<a id="compare-e9fb9dbcfbe6a7cdb21f33661f1b6800"></a>

### [`005778d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005778d0.md) → [`00577bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577bf0.md) FUN_00577bf0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005778ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005778d0.md#insn-005778ec) · [`0057790c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005778d0.md#insn-0057790c)
- 新版 [`00577c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577bf0.md#insn-00577c0c) · [`00577c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577bf0.md#insn-00577c2c)

~~~diff
- 005778ec ["INT_ADD", "register:40f0:8", ["const:5778ec:8", "const:4:8"]]
- 005778ec ["CALL", null, ["callee:00c54d90:8"]]
+ 00577c0c ["INT_ADD", "register:40f0:8", ["const:577c0c:8", "const:4:8"]]
+ 00577c0c ["CALL", null, ["callee:00c54d90:8"]]
- 005778ec bytes 2d711b94
+ 00577c0c bytes 61741b94
- 0057790c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057790c ["INT_ADD", "register:40f0:8", ["const:57790c:8", "const:4:8"]]
- 0057790c ["CALLIND", null, ["register:0:8"]]
+ 00577c2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577c2c ["INT_ADD", "register:40f0:8", ["const:577c2c:8", "const:4:8"]]
+ 00577c2c ["CALLIND", null, ["register:0:8"]]
- 0057790c bytes 00013fd6
+ 00577c2c bytes 00013fd6
~~~


<a id="compare-6f52f128dc1d860ab584dabb8d3da114"></a>

### [`00578204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578204.md) → [`00578524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578524.md) FUN_00578524

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00578380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00578214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578204.md#insn-00578214)
- 新版 [`00578534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578524.md#insn-00578534)

~~~diff
- 00578214 ["INT_ADD", "register:40f0:8", ["const:578214:8", "const:4:8"]]
- 00578214 ["CALL", null, ["callee:00578380:8"]]
+ 00578534 ["INT_ADD", "register:40f0:8", ["const:578534:8", "const:4:8"]]
+ 00578534 ["CALL", null, ["callee:00578380:8"]]
- 00578214 bytes 93ffff97
+ 00578534 bytes 93ffff97
~~~


<a id="compare-d1ed07296af292b309cf66d67f4f1ff1"></a>

### [`0057a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a2e4.md) → [`0057a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a604.md) FUN_0057a604

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a2e4.md#insn-0057a338)
- 新版 [`0057a658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a604.md#insn-0057a658)

~~~diff
- 0057a338 ["INT_ADD", "register:40f0:8", ["const:57a338:8", "const:4:8"]]
- 0057a338 ["CALL", null, ["callee:0057c67c:8"]]
+ 0057a658 ["INT_ADD", "register:40f0:8", ["const:57a658:8", "const:4:8"]]
+ 0057a658 ["CALL", null, ["callee:0057c67c:8"]]
- 0057a338 bytes 09080094
+ 0057a658 bytes 09080094
~~~


<a id="compare-ecc1303ec04dd98ea182f639dd1977df"></a>

### [`0057a33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a33c.md) → [`0057a65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a65c.md) FUN_0057a65c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a33c.md#insn-0057a380)
- 新版 [`0057a6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a65c.md#insn-0057a6a0)

~~~diff
- 0057a380 ["INT_ADD", "register:40f0:8", ["const:57a380:8", "const:4:8"]]
- 0057a380 ["CALL", null, ["callee:0057c67c:8"]]
+ 0057a6a0 ["INT_ADD", "register:40f0:8", ["const:57a6a0:8", "const:4:8"]]
+ 0057a6a0 ["CALL", null, ["callee:0057c67c:8"]]
- 0057a380 bytes f7070094
+ 0057a6a0 bytes f7070094
~~~


<a id="compare-b5a5ae0a4256ec5d0d1feebae3413832"></a>

### [`0057a384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a384.md) → [`0057a6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6a4.md) FUN_0057a6a4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a384.md#insn-0057a3c8)
- 新版 [`0057a6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6a4.md#insn-0057a6e8)

~~~diff
- 0057a3c8 ["INT_ADD", "register:40f0:8", ["const:57a3c8:8", "const:4:8"]]
- 0057a3c8 ["CALL", null, ["callee:0057c67c:8"]]
+ 0057a6e8 ["INT_ADD", "register:40f0:8", ["const:57a6e8:8", "const:4:8"]]
+ 0057a6e8 ["CALL", null, ["callee:0057c67c:8"]]
- 0057a3c8 bytes e5070094
+ 0057a6e8 bytes e5070094
~~~


<a id="compare-7948f38a217b94fcc4c156bcc6c285ba"></a>

### [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) → [`0057bfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md) FUN_0057bfec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005765ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765ec.md) [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) · 呼出先 2件 [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0057690c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057690c.md) [`0057bfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md) · 呼出先 2件 [`0057bfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md#insn-0057bce8) · [`0057bcf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md#insn-0057bcf4) · [`0057bd2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md#insn-0057bd2c)
- 新版 [`0057c008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md#insn-0057c008) · [`0057c014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md#insn-0057c014) · [`0057c04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bfec.md#insn-0057c04c)

~~~diff
- 0057bce8 ["INT_ADD", "register:40f0:8", ["const:57bce8:8", "const:4:8"]]
- 0057bce8 ["CALL", null, ["local:b0:8"]]
+ 0057c008 ["INT_ADD", "register:40f0:8", ["const:57c008:8", "const:4:8"]]
+ 0057c008 ["CALL", null, ["local:b0:8"]]
- 0057bce8 bytes f9ffff97
+ 0057c008 bytes f9ffff97
- 0057bcf4 ["INT_ADD", "register:40f0:8", ["const:57bcf4:8", "const:4:8"]]
- 0057bcf4 ["CALL", null, ["local:b0:8"]]
+ 0057c014 ["INT_ADD", "register:40f0:8", ["const:57c014:8", "const:4:8"]]
+ 0057c014 ["CALL", null, ["local:b0:8"]]
- 0057bcf4 bytes f6ffff97
+ 0057c014 bytes f6ffff97
- 0057bd2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bd2c ["INT_ADD", "register:40f0:8", ["const:57bd2c:8", "const:4:8"]]
- 0057bd2c ["CALLIND", null, ["register:0:8"]]
+ 0057c04c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c04c ["INT_ADD", "register:40f0:8", ["const:57c04c:8", "const:4:8"]]
+ 0057c04c ["CALLIND", null, ["register:0:8"]]
- 0057bd2c bytes 00013fd6
+ 0057c04c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c93c6309c6b64156ef1c1ab1cc6c75"></a>

### [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) → [`0057c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md) FUN_0057c08c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005765f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765f4.md) [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) · 呼出先 2件 [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00576914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576914.md) [`0057c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md) · 呼出先 2件 [`0057c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md#insn-0057bd88) · [`0057bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md#insn-0057bd94) · [`0057bdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md#insn-0057bdc8)
- 新版 [`0057c0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md#insn-0057c0a8) · [`0057c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md#insn-0057c0b4) · [`0057c0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c08c.md#insn-0057c0e8)

~~~diff
- 0057bd88 ["INT_ADD", "register:40f0:8", ["const:57bd88:8", "const:4:8"]]
- 0057bd88 ["CALL", null, ["local:b0:8"]]
+ 0057c0a8 ["INT_ADD", "register:40f0:8", ["const:57c0a8:8", "const:4:8"]]
+ 0057c0a8 ["CALL", null, ["local:b0:8"]]
- 0057bd88 bytes f9ffff97
+ 0057c0a8 bytes f9ffff97
- 0057bd94 ["INT_ADD", "register:40f0:8", ["const:57bd94:8", "const:4:8"]]
- 0057bd94 ["CALL", null, ["local:b0:8"]]
+ 0057c0b4 ["INT_ADD", "register:40f0:8", ["const:57c0b4:8", "const:4:8"]]
+ 0057c0b4 ["CALL", null, ["local:b0:8"]]
- 0057bd94 bytes f6ffff97
+ 0057c0b4 bytes f6ffff97
- 0057bdc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bdc8 ["INT_ADD", "register:40f0:8", ["const:57bdc8:8", "const:4:8"]]
- 0057bdc8 ["CALLIND", null, ["register:0:8"]]
+ 0057c0e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c0e8 ["INT_ADD", "register:40f0:8", ["const:57c0e8:8", "const:4:8"]]
+ 0057c0e8 ["CALLIND", null, ["register:0:8"]]
- 0057bdc8 bytes 00013fd6
+ 0057c0e8 bytes 00013fd6
~~~


<a id="compare-47837f416174c94f92b1adb76ac5647f"></a>

### [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) → [`0057c0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md) FUN_0057c0fc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00576738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576738.md) [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) · 呼出先 4件 [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00576a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a58.md) [`0057c0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md) · 呼出先 4件 [`0057c0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md#insn-0057bdf8) · [`0057be04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md#insn-0057be04) · [`0057be18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md#insn-0057be18)
- 新版 [`0057c118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md#insn-0057c118) · [`0057c124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md#insn-0057c124) · [`0057c138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c0fc.md#insn-0057c138)

~~~diff
- 0057bdf8 ["INT_ADD", "register:40f0:8", ["const:57bdf8:8", "const:4:8"]]
- 0057bdf8 ["CALL", null, ["local:b0:8"]]
+ 0057c118 ["INT_ADD", "register:40f0:8", ["const:57c118:8", "const:4:8"]]
+ 0057c118 ["CALL", null, ["local:b0:8"]]
- 0057bdf8 bytes f9ffff97
+ 0057c118 bytes f9ffff97
- 0057be04 ["INT_ADD", "register:40f0:8", ["const:57be04:8", "const:4:8"]]
- 0057be04 ["CALL", null, ["local:b0:8"]]
+ 0057c124 ["INT_ADD", "register:40f0:8", ["const:57c124:8", "const:4:8"]]
+ 0057c124 ["CALL", null, ["local:b0:8"]]
- 0057be04 bytes f6ffff97
+ 0057c124 bytes f6ffff97
- 0057be18 ["INT_ADD", "register:40f0:8", ["const:57be18:8", "const:4:8"]]
- 0057be18 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057c138 ["INT_ADD", "register:40f0:8", ["const:57c138:8", "const:4:8"]]
+ 0057c138 ["CALL", null, ["callee:00c54d90:8"]]
- 0057be18 bytes e25f1b94
+ 0057c138 bytes 16631b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3377b965969ba76fbc99b931b51ed97e"></a>

### [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) → [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) FUN_0057c16c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`0057ed30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ed30.md) [`0057eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md) [`0057f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md) [`0057f19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 11件 [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) [`0057f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f050.md) [`0057f1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f1c8.md) [`0057f33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f33c.md) [`0057f4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f4bc.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md#insn-0057bec0) · [`0057bee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md#insn-0057bee4)
- 新版 [`0057c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md#insn-0057c1e0) · [`0057c204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md#insn-0057c204)

~~~diff
- 0057bec0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bec0 ["INT_ADD", "register:40f0:8", ["const:57bec0:8", "const:4:8"]]
- 0057bec0 ["CALLIND", null, ["register:0:8"]]
+ 0057c1e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c1e0 ["INT_ADD", "register:40f0:8", ["const:57c1e0:8", "const:4:8"]]
+ 0057c1e0 ["CALLIND", null, ["register:0:8"]]
- 0057bec0 bytes 00013fd6
+ 0057c1e0 bytes 00013fd6
- 0057bee4 ["INT_ADD", "register:40f0:8", ["const:57bee4:8", "const:4:8"]]
- 0057bee4 ["CALL", null, ["callee:00c58f80:8"]]
+ 0057c204 ["INT_ADD", "register:40f0:8", ["const:57c204:8", "const:4:8"]]
+ 0057c204 ["CALL", null, ["callee:00c58f80:8"]]
- 0057bee4 bytes 33701b94
+ 0057c204 bytes 5f731b94
~~~


<a id="compare-c368efe677ea052bfc0755951a375efc"></a>

### [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) → [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) FUN_0057c208

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) [`0057a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md) [`0058c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md) [`006c3cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md) [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 16件 [`005773e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md) [`0057ad14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057ad14.md) [`0058cb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cb24.md) [`006c408c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c408c.md) [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md#insn-0057bf54) · [`0057bf64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md#insn-0057bf64) · [`0057bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md#insn-0057bf84)
- 新版 [`0057c274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md#insn-0057c274) · [`0057c284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md#insn-0057c284) · [`0057c2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md#insn-0057c2a4)

~~~diff
- 0057bf54 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf54 ["INT_ADD", "register:40f0:8", ["const:57bf54:8", "const:4:8"]]
- 0057bf54 ["CALLIND", null, ["register:0:8"]]
+ 0057c274 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c274 ["INT_ADD", "register:40f0:8", ["const:57c274:8", "const:4:8"]]
+ 0057c274 ["CALLIND", null, ["register:0:8"]]
- 0057bf54 bytes 00013fd6
+ 0057c274 bytes 00013fd6
- 0057bf64 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf64 ["INT_ADD", "register:40f0:8", ["const:57bf64:8", "const:4:8"]]
- 0057bf64 ["CALLIND", null, ["register:0:8"]]
+ 0057c284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c284 ["INT_ADD", "register:40f0:8", ["const:57c284:8", "const:4:8"]]
+ 0057c284 ["CALLIND", null, ["register:0:8"]]
- 0057bf64 bytes 00013fd6
+ 0057c284 bytes 00013fd6
- 0057bf84 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf84 ["INT_ADD", "register:40f0:8", ["const:57bf84:8", "const:4:8"]]
- 0057bf84 ["CALLIND", null, ["register:0:8"]]
+ 0057c2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c2a4 ["INT_ADD", "register:40f0:8", ["const:57c2a4:8", "const:4:8"]]
+ 0057c2a4 ["CALLIND", null, ["register:0:8"]]
- 0057bf84 bytes 00013fd6
+ 0057c2a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8283c4b86465b284c93bcc4ab537b85"></a>

### [`0057c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md) → [`0057c410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c410.md) FUN_0057c410

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0057c56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md#insn-0057c15c) · [`0057c188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md#insn-0057c188) · [`0057c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md#insn-0057c1e8)
- 新版 [`0057c47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c410.md#insn-0057c47c) · [`0057c4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c410.md#insn-0057c4a8) · [`0057c508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c410.md#insn-0057c508)

~~~diff
- 0057c15c ["INT_ADD", "register:40f0:8", ["const:57c15c:8", "const:4:8"]]
- 0057c15c ["CALL", null, ["callee:00c58f30:8"]]
+ 0057c47c ["INT_ADD", "register:40f0:8", ["const:57c47c:8", "const:4:8"]]
+ 0057c47c ["CALL", null, ["callee:00c58f30:8"]]
- 0057c15c bytes 816f1b94
+ 0057c47c bytes ad721b94
- 0057c188 ["INT_ADD", "register:40f0:8", ["const:57c188:8", "const:4:8"]]
- 0057c188 ["CALL", null, ["callee:00c54d60:8"]]
+ 0057c4a8 ["INT_ADD", "register:40f0:8", ["const:57c4a8:8", "const:4:8"]]
+ 0057c4a8 ["CALL", null, ["callee:00c54d60:8"]]
- 0057c188 bytes fa5e1b94
+ 0057c4a8 bytes 2e621b94
- 0057c1e8 ["INT_ADD", "register:40f0:8", ["const:57c1e8:8", "const:4:8"]]
- 0057c1e8 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057c508 ["INT_ADD", "register:40f0:8", ["const:57c508:8", "const:4:8"]]
+ 0057c508 ["CALL", null, ["callee:00c54d90:8"]]
- 0057c1e8 bytes ee5e1b94
+ 0057c508 bytes 22621b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a403adccb9411ab9a1d1ce49bac23a"></a>

### [`0057c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md) → [`0057c580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c580.md) FUN_0057c580

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) · 呼出先 4件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00578380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md) · 呼出先 4件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md#insn-0057c310) · [`0057c324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md#insn-0057c324) · [`0057c338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md#insn-0057c338)
- 新版 [`0057c630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c580.md#insn-0057c630) · [`0057c644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c580.md#insn-0057c644) · [`0057c658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c580.md#insn-0057c658)

~~~diff
- 0057c310 ["INT_ADD", "register:40f0:8", ["const:57c310:8", "const:4:8"]]
- 0057c310 ["CALL", null, ["callee:00494970:8"]]
+ 0057c630 ["INT_ADD", "register:40f0:8", ["const:57c630:8", "const:4:8"]]
+ 0057c630 ["CALL", null, ["callee:00494970:8"]]
- 0057c310 bytes d060fc97
+ 0057c630 bytes d060fc97
- 0057c324 ["INT_ADD", "register:40f0:8", ["const:57c324:8", "const:4:8"]]
- 0057c324 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057c644 ["INT_ADD", "register:40f0:8", ["const:57c644:8", "const:4:8"]]
+ 0057c644 ["CALL", null, ["callee:00c54d90:8"]]
- 0057c324 bytes 9f5e1b94
+ 0057c644 bytes d3611b94
- 0057c338 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c338 ["INT_ADD", "register:40f0:8", ["const:57c338:8", "const:4:8"]]
- 0057c338 ["CALLIND", null, ["register:0:8"]]
+ 0057c658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c658 ["INT_ADD", "register:40f0:8", ["const:57c658:8", "const:4:8"]]
+ 0057c658 ["CALLIND", null, ["register:0:8"]]
- 0057c338 bytes 00013fd6
+ 0057c658 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6388223f0aef5d7f746989d0968ee31"></a>

### [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) → [`0057c690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md) FUN_0057c690

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0057a95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a95c.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0057c56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md#insn-0057c3dc) · [`0057c408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md#insn-0057c408) · [`0057c468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md#insn-0057c468)
- 新版 [`0057c6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md#insn-0057c6fc) · [`0057c728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md#insn-0057c728) · [`0057c788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md#insn-0057c788)

~~~diff
- 0057c3dc ["INT_ADD", "register:40f0:8", ["const:57c3dc:8", "const:4:8"]]
- 0057c3dc ["CALL", null, ["callee:00c58f30:8"]]
+ 0057c6fc ["INT_ADD", "register:40f0:8", ["const:57c6fc:8", "const:4:8"]]
+ 0057c6fc ["CALL", null, ["callee:00c58f30:8"]]
- 0057c3dc bytes e16e1b94
+ 0057c6fc bytes 0d721b94
- 0057c408 ["INT_ADD", "register:40f0:8", ["const:57c408:8", "const:4:8"]]
- 0057c408 ["CALL", null, ["callee:00c54d60:8"]]
+ 0057c728 ["INT_ADD", "register:40f0:8", ["const:57c728:8", "const:4:8"]]
+ 0057c728 ["CALL", null, ["callee:00c54d60:8"]]
- 0057c408 bytes 5a5e1b94
+ 0057c728 bytes 8e611b94
- 0057c468 ["INT_ADD", "register:40f0:8", ["const:57c468:8", "const:4:8"]]
- 0057c468 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057c788 ["INT_ADD", "register:40f0:8", ["const:57c788:8", "const:4:8"]]
+ 0057c788 ["CALL", null, ["callee:00c54d90:8"]]
- 0057c468 bytes 4e5e1b94
+ 0057c788 bytes 82611b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed30572ce3516ca810086d00133b0822"></a>

### [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) → [`0057c88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md) FUN_0057c88c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0057a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a990.md) [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) · 呼出先 2件 [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0057acb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acb0.md) [`0057c88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md) · 呼出先 2件 [`0057c88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md#insn-0057c588) · [`0057c594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md#insn-0057c594) · [`0057c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md#insn-0057c5c8)
- 新版 [`0057c8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md#insn-0057c8a8) · [`0057c8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md#insn-0057c8b4) · [`0057c8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c88c.md#insn-0057c8e8)

~~~diff
- 0057c588 ["INT_ADD", "register:40f0:8", ["const:57c588:8", "const:4:8"]]
- 0057c588 ["CALL", null, ["local:b0:8"]]
+ 0057c8a8 ["INT_ADD", "register:40f0:8", ["const:57c8a8:8", "const:4:8"]]
+ 0057c8a8 ["CALL", null, ["local:b0:8"]]
- 0057c588 bytes f9ffff97
+ 0057c8a8 bytes f9ffff97
- 0057c594 ["INT_ADD", "register:40f0:8", ["const:57c594:8", "const:4:8"]]
- 0057c594 ["CALL", null, ["local:b0:8"]]
+ 0057c8b4 ["INT_ADD", "register:40f0:8", ["const:57c8b4:8", "const:4:8"]]
+ 0057c8b4 ["CALL", null, ["local:b0:8"]]
- 0057c594 bytes f6ffff97
+ 0057c8b4 bytes f6ffff97
- 0057c5c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c5c8 ["INT_ADD", "register:40f0:8", ["const:57c5c8:8", "const:4:8"]]
- 0057c5c8 ["CALLIND", null, ["register:0:8"]]
+ 0057c8e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c8e8 ["INT_ADD", "register:40f0:8", ["const:57c8e8:8", "const:4:8"]]
+ 0057c8e8 ["CALLIND", null, ["register:0:8"]]
- 0057c5c8 bytes 00013fd6
+ 0057c8e8 bytes 00013fd6
~~~


<a id="compare-c964dd699bab013b7f0c0c4ab8a7de88"></a>

### [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) → [`0057c8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md) FUN_0057c8fc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057a998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a998.md) [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`0058c468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md) · 呼出先 2件 [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0057acb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acb8.md) [`0057c8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md) [`0058c788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c788.md) · 呼出先 2件 [`0057c8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md#insn-0057c5f8) · [`0057c604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md#insn-0057c604) · [`0057c638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md#insn-0057c638)
- 新版 [`0057c918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md#insn-0057c918) · [`0057c924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md#insn-0057c924) · [`0057c958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md#insn-0057c958)

~~~diff
- 0057c5f8 ["INT_ADD", "register:40f0:8", ["const:57c5f8:8", "const:4:8"]]
- 0057c5f8 ["CALL", null, ["local:b0:8"]]
+ 0057c918 ["INT_ADD", "register:40f0:8", ["const:57c918:8", "const:4:8"]]
+ 0057c918 ["CALL", null, ["local:b0:8"]]
- 0057c5f8 bytes f9ffff97
+ 0057c918 bytes f9ffff97
- 0057c604 ["INT_ADD", "register:40f0:8", ["const:57c604:8", "const:4:8"]]
- 0057c604 ["CALL", null, ["local:b0:8"]]
+ 0057c924 ["INT_ADD", "register:40f0:8", ["const:57c924:8", "const:4:8"]]
+ 0057c924 ["CALL", null, ["local:b0:8"]]
- 0057c604 bytes f6ffff97
+ 0057c924 bytes f6ffff97
- 0057c638 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c638 ["INT_ADD", "register:40f0:8", ["const:57c638:8", "const:4:8"]]
- 0057c638 ["CALLIND", null, ["register:0:8"]]
+ 0057c958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c958 ["INT_ADD", "register:40f0:8", ["const:57c958:8", "const:4:8"]]
+ 0057c958 ["CALLIND", null, ["register:0:8"]]
- 0057c638 bytes 00013fd6
+ 0057c958 bytes 00013fd6
~~~


<a id="compare-da33ded63b7ed2ff904cd5f499b6a7a5"></a>

### [`0057c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md) → [`0057c9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c9b4.md) FUN_0057c9b4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) [`00935e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935e90.md) [`00ac8bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8bb8.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0057b4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md) [`00936e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00936/00936e3c.md) [`00ac9bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9bac.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md#insn-0057c700) · [`0057c710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md#insn-0057c710) · [`0057c730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md#insn-0057c730)
- 新版 [`0057ca20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c9b4.md#insn-0057ca20) · [`0057ca30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c9b4.md#insn-0057ca30) · [`0057ca50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c9b4.md#insn-0057ca50)

~~~diff
- 0057c700 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c700 ["INT_ADD", "register:40f0:8", ["const:57c700:8", "const:4:8"]]
- 0057c700 ["CALLIND", null, ["register:0:8"]]
+ 0057ca20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057ca20 ["INT_ADD", "register:40f0:8", ["const:57ca20:8", "const:4:8"]]
+ 0057ca20 ["CALLIND", null, ["register:0:8"]]
- 0057c700 bytes 00013fd6
+ 0057ca20 bytes 00013fd6
- 0057c710 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c710 ["INT_ADD", "register:40f0:8", ["const:57c710:8", "const:4:8"]]
- 0057c710 ["CALLIND", null, ["register:0:8"]]
+ 0057ca30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057ca30 ["INT_ADD", "register:40f0:8", ["const:57ca30:8", "const:4:8"]]
+ 0057ca30 ["CALLIND", null, ["register:0:8"]]
- 0057c710 bytes 00013fd6
+ 0057ca30 bytes 00013fd6
- 0057c730 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c730 ["INT_ADD", "register:40f0:8", ["const:57c730:8", "const:4:8"]]
- 0057c730 ["CALLIND", null, ["register:0:8"]]
+ 0057ca50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057ca50 ["INT_ADD", "register:40f0:8", ["const:57ca50:8", "const:4:8"]]
+ 0057ca50 ["CALLIND", null, ["register:0:8"]]
- 0057c730 bytes 00013fd6
+ 0057ca50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618d58e02ce3678d818062768ca22293"></a>

### [`0057cd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cd14.md) → [`0057d034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d034.md) FUN_0057d034

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057cd2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cd14.md#insn-0057cd2c)
- 新版 [`0057d04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d034.md#insn-0057d04c)

~~~diff
- 0057cd2c ["INT_ADD", "register:40f0:8", ["const:57cd2c:8", "const:4:8"]]
- 0057cd2c ["CALL", null, ["callee:00c5b1e0:8"]]
+ 0057d04c ["INT_ADD", "register:40f0:8", ["const:57d04c:8", "const:4:8"]]
+ 0057d04c ["CALL", null, ["callee:00c5b1e0:8"]]
- 0057cd2c bytes 39751b94
+ 0057d04c bytes 65781b94
~~~


<a id="compare-d747a9216230f2a705d3b2e54d9be0a3"></a>

### [`0057cda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cda0.md) → [`0057d0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d0c0.md) FUN_0057d0c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cda0.md#insn-0057cdc0) · [`0057cdd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cda0.md#insn-0057cdd4)
- 新版 [`0057d0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d0c0.md#insn-0057d0e0) · [`0057d0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d0c0.md#insn-0057d0f4)

~~~diff
- 0057cdc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cdc0 ["INT_ADD", "register:40f0:8", ["const:57cdc0:8", "const:4:8"]]
- 0057cdc0 ["CALLIND", null, ["register:0:8"]]
+ 0057d0e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d0e0 ["INT_ADD", "register:40f0:8", ["const:57d0e0:8", "const:4:8"]]
+ 0057d0e0 ["CALLIND", null, ["register:0:8"]]
- 0057cdc0 bytes 00013fd6
+ 0057d0e0 bytes 00013fd6
- 0057cdd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cdd4 ["INT_ADD", "register:40f0:8", ["const:57cdd4:8", "const:4:8"]]
- 0057cdd4 ["CALLIND", null, ["register:0:8"]]
+ 0057d0f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d0f4 ["INT_ADD", "register:40f0:8", ["const:57d0f4:8", "const:4:8"]]
+ 0057d0f4 ["CALLIND", null, ["register:0:8"]]
- 0057cdd4 bytes 00013fd6
+ 0057d0f4 bytes 00013fd6
~~~


<a id="compare-bfbe1dc8805787e90699197da60ad1fd"></a>

### [`0057cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cea8.md) → [`0057d1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d1c8.md) FUN_0057d1c8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cea8.md#insn-0057cec4)
- 新版 [`0057d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d1c8.md#insn-0057d1e4)

~~~diff
- 0057cec4 ["INT_ADD", "register:40f0:8", ["const:57cec4:8", "const:4:8"]]
- 0057cec4 ["CALL", null, ["callee:00c5b210:8"]]
+ 0057d1e4 ["INT_ADD", "register:40f0:8", ["const:57d1e4:8", "const:4:8"]]
+ 0057d1e4 ["CALL", null, ["callee:00c5b210:8"]]
- 0057cec4 bytes df741b94
+ 0057d1e4 bytes 0b781b94
~~~


<a id="compare-18be8aeef68df1f3b01fe037a728b183"></a>

### [`0057d16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d16c.md) → [`0057d48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d48c.md) FUN_0057d48c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a220.md) [`00c5a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a240.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1f0.md) [`00c5b210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d16c.md#insn-0057d184) · [`0057d194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d16c.md#insn-0057d194)
- 新版 [`0057d4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d48c.md#insn-0057d4a4) · [`0057d4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d48c.md#insn-0057d4b4)

~~~diff
- 0057d184 ["INT_ADD", "register:40f0:8", ["const:57d184:8", "const:4:8"]]
- 0057d184 ["CALL", null, ["callee:00c5b1f0:8"]]
+ 0057d4a4 ["INT_ADD", "register:40f0:8", ["const:57d4a4:8", "const:4:8"]]
+ 0057d4a4 ["CALL", null, ["callee:00c5b1f0:8"]]
- 0057d184 bytes 27741b94
+ 0057d4a4 bytes 53771b94
- 0057d194 ["INT_ADD", "register:40f0:8", ["const:57d194:8", "const:4:8"]]
- 0057d194 ["CALL", null, ["callee:00c5b210:8"]]
+ 0057d4b4 ["INT_ADD", "register:40f0:8", ["const:57d4b4:8", "const:4:8"]]
+ 0057d4b4 ["CALL", null, ["callee:00c5b210:8"]]
- 0057d194 bytes 2b741b94
+ 0057d4b4 bytes 57771b94
~~~


<a id="compare-608b21898e98bcd0214472aa89fc7bb4"></a>

### [`0057d1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d1f8.md) → [`0057d518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d518.md) FUN_0057d518

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d1f8.md#insn-0057d210)
- 新版 [`0057d530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d518.md#insn-0057d530)

~~~diff
- 0057d210 ["INT_ADD", "register:40f0:8", ["const:57d210:8", "const:4:8"]]
- 0057d210 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 0057d530 ["INT_ADD", "register:40f0:8", ["const:57d530:8", "const:4:8"]]
+ 0057d530 ["CALL", null, ["callee:00c5b0a0:8"]]
- 0057d210 bytes b0731b94
+ 0057d530 bytes dc761b94
~~~


<a id="compare-5b362e765830cf9a844b5caa8d439be0"></a>

### [`0057d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d22c.md) → [`0057d54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d54c.md) FUN_0057d54c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5b260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b260.md) [`00c5b270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d22c.md#insn-0057d244) · [`0057d258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d22c.md#insn-0057d258) · [`0057d25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d22c.md#insn-0057d25c)
- 新版 [`0057d564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d54c.md#insn-0057d564) · [`0057d578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d54c.md#insn-0057d578) · [`0057d57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d54c.md#insn-0057d57c)

~~~diff
- 0057d244 ["INT_ADD", "register:40f0:8", ["const:57d244:8", "const:4:8"]]
- 0057d244 ["CALL", null, ["callee:00c5b250:8"]]
+ 0057d564 ["INT_ADD", "register:40f0:8", ["const:57d564:8", "const:4:8"]]
+ 0057d564 ["CALL", null, ["callee:00c5b250:8"]]
- 0057d244 bytes 0f741b94
+ 0057d564 bytes 3b771b94
- 0057d258 ["INT_ADD", "register:40f0:8", ["const:57d258:8", "const:4:8"]]
- 0057d258 ["CALL", null, ["callee:00c5b260:8"]]
+ 0057d578 ["INT_ADD", "register:40f0:8", ["const:57d578:8", "const:4:8"]]
+ 0057d578 ["CALL", null, ["callee:00c5b260:8"]]
- 0057d258 bytes 0e741b94
+ 0057d578 bytes 3a771b94
- 0057d25c ["INT_ADD", "register:40f0:8", ["const:57d25c:8", "const:4:8"]]
- 0057d25c ["CALL", null, ["callee:00c5b270:8"]]
+ 0057d57c ["INT_ADD", "register:40f0:8", ["const:57d57c:8", "const:4:8"]]
+ 0057d57c ["CALL", null, ["callee:00c5b270:8"]]
- 0057d25c bytes 11741b94
+ 0057d57c bytes 3d771b94
~~~


<a id="compare-032d75f5e29ffb650418f308926b7f28"></a>

### [`0057d274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d274.md) → [`0057d594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d594.md) FUN_0057d594

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b260.md) [`00c5b280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d274.md#insn-0057d298) · [`0057d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d274.md#insn-0057d2a0) · [`0057d2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d274.md#insn-0057d2d4)
- 新版 [`0057d5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d594.md#insn-0057d5b8) · [`0057d5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d594.md#insn-0057d5c0) · [`0057d5f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d594.md#insn-0057d5f4)

~~~diff
- 0057d298 ["INT_ADD", "register:40f0:8", ["const:57d298:8", "const:4:8"]]
- 0057d298 ["CALL", null, ["callee:00c5b260:8"]]
+ 0057d5b8 ["INT_ADD", "register:40f0:8", ["const:57d5b8:8", "const:4:8"]]
+ 0057d5b8 ["CALL", null, ["callee:00c5b260:8"]]
- 0057d298 bytes fe731b94
+ 0057d5b8 bytes 2a771b94
- 0057d2a0 ["INT_ADD", "register:40f0:8", ["const:57d2a0:8", "const:4:8"]]
- 0057d2a0 ["CALL", null, ["callee:00c5b280:8"]]
+ 0057d5c0 ["INT_ADD", "register:40f0:8", ["const:57d5c0:8", "const:4:8"]]
+ 0057d5c0 ["CALL", null, ["callee:00c5b280:8"]]
- 0057d2a0 bytes 04741b94
+ 0057d5c0 bytes 30771b94
- 0057d2d4 ["INT_ADD", "register:40f0:8", ["const:57d2d4:8", "const:4:8"]]
- 0057d2d4 ["CALL", null, ["callee:00c58f80:8"]]
+ 0057d5f4 ["INT_ADD", "register:40f0:8", ["const:57d5f4:8", "const:4:8"]]
+ 0057d5f4 ["CALL", null, ["callee:00c58f80:8"]]
- 0057d2d4 bytes 376b1b94
+ 0057d5f4 bytes 636e1b94
~~~


<a id="compare-c4b7be26b320481dabb8f6df573cc9ee"></a>

### [`0057d30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d30c.md) → [`0057d62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d62c.md) FUN_0057d62c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b260.md) [`00c5b280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d30c.md#insn-0057d330) · [`0057d338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d30c.md#insn-0057d338) · [`0057d360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d30c.md#insn-0057d360)
- 新版 [`0057d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d62c.md#insn-0057d650) · [`0057d658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d62c.md#insn-0057d658) · [`0057d680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d62c.md#insn-0057d680)

~~~diff
- 0057d330 ["INT_ADD", "register:40f0:8", ["const:57d330:8", "const:4:8"]]
- 0057d330 ["CALL", null, ["callee:00c5b260:8"]]
+ 0057d650 ["INT_ADD", "register:40f0:8", ["const:57d650:8", "const:4:8"]]
+ 0057d650 ["CALL", null, ["callee:00c5b260:8"]]
- 0057d330 bytes d8731b94
+ 0057d650 bytes 04771b94
- 0057d338 ["INT_ADD", "register:40f0:8", ["const:57d338:8", "const:4:8"]]
- 0057d338 ["CALL", null, ["callee:00c5b280:8"]]
+ 0057d658 ["INT_ADD", "register:40f0:8", ["const:57d658:8", "const:4:8"]]
+ 0057d658 ["CALL", null, ["callee:00c5b280:8"]]
- 0057d338 bytes de731b94
+ 0057d658 bytes 0a771b94
- 0057d360 ["INT_ADD", "register:40f0:8", ["const:57d360:8", "const:4:8"]]
- 0057d360 ["CALL", null, ["callee:00c58f80:8"]]
+ 0057d680 ["INT_ADD", "register:40f0:8", ["const:57d680:8", "const:4:8"]]
+ 0057d680 ["CALL", null, ["callee:00c58f80:8"]]
- 0057d360 bytes 146b1b94
+ 0057d680 bytes 406e1b94
~~~


<a id="compare-566b0dcc1a6cf78d7aad6450b8111744"></a>

### [`0057d45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d45c.md) → [`0057d77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d77c.md) FUN_0057d77c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d45c.md#insn-0057d484) · [`0057d498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d45c.md#insn-0057d498)
- 新版 [`0057d7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d77c.md#insn-0057d7a4) · [`0057d7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d77c.md#insn-0057d7b8)

~~~diff
- 0057d484 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d484 ["INT_ADD", "register:40f0:8", ["const:57d484:8", "const:4:8"]]
- 0057d484 ["CALLIND", null, ["register:0:8"]]
+ 0057d7a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d7a4 ["INT_ADD", "register:40f0:8", ["const:57d7a4:8", "const:4:8"]]
+ 0057d7a4 ["CALLIND", null, ["register:0:8"]]
- 0057d484 bytes 00013fd6
+ 0057d7a4 bytes 00013fd6
- 0057d498 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d498 ["INT_ADD", "register:40f0:8", ["const:57d498:8", "const:4:8"]]
- 0057d498 ["CALLIND", null, ["register:0:8"]]
+ 0057d7b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d7b8 ["INT_ADD", "register:40f0:8", ["const:57d7b8:8", "const:4:8"]]
+ 0057d7b8 ["CALLIND", null, ["register:0:8"]]
- 0057d498 bytes 00013fd6
+ 0057d7b8 bytes 00013fd6
~~~


<a id="compare-fa7f92a93ce8a322ec053e6d99a3802c"></a>

### [`0057d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d724.md) → [`0057da44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057da44.md) FUN_0057da44

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d724.md#insn-0057d734)
- 新版 [`0057da54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057da44.md#insn-0057da54)

~~~diff
- 0057d734 ["INT_ADD", "register:40f0:8", ["const:57d734:8", "const:4:8"]]
- 0057d734 ["CALL", null, ["callee:00c5b100:8"]]
+ 0057da54 ["INT_ADD", "register:40f0:8", ["const:57da54:8", "const:4:8"]]
+ 0057da54 ["CALL", null, ["callee:00c5b100:8"]]
- 0057d734 bytes 7f721b94
+ 0057da54 bytes ab751b94
~~~


<a id="compare-a5deb7569c906c488c56fc1b8c6af0dd"></a>

### [`0057d748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d748.md) → [`0057da68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057da68.md) FUN_0057da68

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d748.md#insn-0057d764)
- 新版 [`0057da84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057da68.md#insn-0057da84)

~~~diff
- 0057d764 ["INT_ADD", "register:40f0:8", ["const:57d764:8", "const:4:8"]]
- 0057d764 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 0057da84 ["INT_ADD", "register:40f0:8", ["const:57da84:8", "const:4:8"]]
+ 0057da84 ["CALL", null, ["callee:00c5b2a0:8"]]
- 0057d764 bytes db721b94
+ 0057da84 bytes 07761b94
~~~


<a id="compare-49dc70184825f02c2af649db037ecc9a"></a>

### [`0057d804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d804.md) → [`0057db24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057db24.md) FUN_0057db24

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d804.md#insn-0057d840)
- 新版 [`0057db60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057db24.md#insn-0057db60)

~~~diff
- 0057d840 ["INT_ADD", "register:40f0:8", ["const:57d840:8", "const:4:8"]]
- 0057d840 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 0057db60 ["INT_ADD", "register:40f0:8", ["const:57db60:8", "const:4:8"]]
+ 0057db60 ["CALL", null, ["callee:00c5b2c0:8"]]
- 0057d840 bytes ac721b94
+ 0057db60 bytes d8751b94
~~~


<a id="compare-a195bd4b97a1908f6737422d97c939c0"></a>

### [`0057d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d860.md) → [`0057db80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057db80.md) FUN_0057db80

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d860.md#insn-0057d888)
- 新版 [`0057dba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057db80.md#insn-0057dba8)

~~~diff
- 0057d888 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d888 ["INT_ADD", "register:40f0:8", ["const:57d888:8", "const:4:8"]]
- 0057d888 ["CALLIND", null, ["register:0:8"]]
+ 0057dba8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057dba8 ["INT_ADD", "register:40f0:8", ["const:57dba8:8", "const:4:8"]]
+ 0057dba8 ["CALLIND", null, ["register:0:8"]]
- 0057d888 bytes 20013fd6
+ 0057dba8 bytes 20013fd6
~~~


<a id="compare-8b5683fd32d2976c99044ffef35a1ceb"></a>

### [`0057d8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d8b4.md) → [`0057dbd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dbd4.md) FUN_0057dbd4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d8b4.md#insn-0057d8e4) · [`0057d908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d8b4.md#insn-0057d908) · [`0057d918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d8b4.md#insn-0057d918)
- 新版 [`0057dc04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dbd4.md#insn-0057dc04) · [`0057dc28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dbd4.md#insn-0057dc28) · [`0057dc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dbd4.md#insn-0057dc38)

~~~diff
- 0057d8e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d8e4 ["INT_ADD", "register:40f0:8", ["const:57d8e4:8", "const:4:8"]]
- 0057d8e4 ["CALLIND", null, ["register:0:8"]]
+ 0057dc04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057dc04 ["INT_ADD", "register:40f0:8", ["const:57dc04:8", "const:4:8"]]
+ 0057dc04 ["CALLIND", null, ["register:0:8"]]
- 0057d8e4 bytes 20013fd6
+ 0057dc04 bytes 20013fd6
- 0057d908 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d908 ["INT_ADD", "register:40f0:8", ["const:57d908:8", "const:4:8"]]
- 0057d908 ["CALLIND", null, ["register:0:8"]]
+ 0057dc28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057dc28 ["INT_ADD", "register:40f0:8", ["const:57dc28:8", "const:4:8"]]
+ 0057dc28 ["CALLIND", null, ["register:0:8"]]
- 0057d908 bytes 20013fd6
+ 0057dc28 bytes 20013fd6
- 0057d918 ["INT_ADD", "register:40f0:8", ["const:57d918:8", "const:4:8"]]
- 0057d918 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 0057dc38 ["INT_ADD", "register:40f0:8", ["const:57dc38:8", "const:4:8"]]
+ 0057dc38 ["CALL", null, ["callee:00c5b2c0:8"]]
- 0057d918 bytes 76721b94
+ 0057dc38 bytes a2751b94
~~~


<a id="compare-1d8112587d53ae5b071106925ce34d39"></a>

### [`0057d944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d944.md) → [`0057dc64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dc64.md) FUN_0057dc64

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d944.md#insn-0057d964)
- 新版 [`0057dc84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dc64.md#insn-0057dc84)

~~~diff
- 0057d964 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d964 ["INT_ADD", "register:40f0:8", ["const:57d964:8", "const:4:8"]]
- 0057d964 ["CALLIND", null, ["register:0:8"]]
+ 0057dc84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057dc84 ["INT_ADD", "register:40f0:8", ["const:57dc84:8", "const:4:8"]]
+ 0057dc84 ["CALLIND", null, ["register:0:8"]]
- 0057d964 bytes 00013fd6
+ 0057dc84 bytes 00013fd6
~~~


<a id="compare-4c83f2ab83a211b2ca19f96e3aaae959"></a>

### [`0057d994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d994.md) → [`0057dcb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dcb4.md) FUN_0057dcb4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d994.md#insn-0057d9b8)
- 新版 [`0057dcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dcb4.md#insn-0057dcd8)

~~~diff
- 0057d9b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d9b8 ["INT_ADD", "register:40f0:8", ["const:57d9b8:8", "const:4:8"]]
- 0057d9b8 ["CALLIND", null, ["register:0:8"]]
+ 0057dcd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057dcd8 ["INT_ADD", "register:40f0:8", ["const:57dcd8:8", "const:4:8"]]
+ 0057dcd8 ["CALLIND", null, ["register:0:8"]]
- 0057d9b8 bytes 00013fd6
+ 0057dcd8 bytes 00013fd6
~~~


<a id="compare-bbfab6fe1ee8e3fc55257fba9bd59e62"></a>

### [`0057dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dd14.md) → [`0057e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e034.md) FUN_0057e034

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a300.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057dd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dd14.md#insn-0057dd3c) · [`0057ddb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dd14.md#insn-0057ddb0) · [`0057ddd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dd14.md#insn-0057ddd0)
- 新版 [`0057e05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e034.md#insn-0057e05c) · [`0057e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e034.md#insn-0057e0d0) · [`0057e0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e034.md#insn-0057e0f0)

~~~diff
- 0057dd3c ["INT_ADD", "register:40f0:8", ["const:57dd3c:8", "const:4:8"]]
- 0057dd3c ["CALL", null, ["callee:00c5b2d0:8"]]
+ 0057e05c ["INT_ADD", "register:40f0:8", ["const:57e05c:8", "const:4:8"]]
+ 0057e05c ["CALL", null, ["callee:00c5b2d0:8"]]
- 0057dd3c bytes 71711b94
+ 0057e05c bytes 9d741b94
- 0057ddb0 ["INT_ADD", "register:40f0:8", ["const:57ddb0:8", "const:4:8"]]
- 0057ddb0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0057e0d0 ["INT_ADD", "register:40f0:8", ["const:57e0d0:8", "const:4:8"]]
+ 0057e0d0 ["CALL", null, ["callee:00c58f30:8"]]
- 0057ddb0 bytes 6c681b94
+ 0057e0d0 bytes 986b1b94
- 0057ddd0 ["INT_ADD", "register:40f0:8", ["const:57ddd0:8", "const:4:8"]]
- 0057ddd0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0057e0f0 ["INT_ADD", "register:40f0:8", ["const:57e0f0:8", "const:4:8"]]
+ 0057e0f0 ["CALL", null, ["callee:00c58fe0:8"]]
- 0057ddd0 bytes 90681b94
+ 0057e0f0 bytes bc6b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9acd667abdb3bc5ec9f4fd98664f65c2"></a>

### [`0057de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de28.md) → [`0057e148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e148.md) FUN_0057e148

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005804e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`00580804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580804.md) · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057de44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de28.md#insn-0057de44)
- 新版 [`0057e164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e148.md#insn-0057e164)

~~~diff
- 0057de44 ["INT_ADD", "register:40f0:8", ["const:57de44:8", "const:4:8"]]
- 0057de44 ["CALL", null, ["callee:00c54d60:8"]]
+ 0057e164 ["INT_ADD", "register:40f0:8", ["const:57e164:8", "const:4:8"]]
+ 0057e164 ["CALL", null, ["callee:00c54d60:8"]]
- 0057de44 bytes cb571b94
+ 0057e164 bytes ff5a1b94
~~~


<a id="compare-2f1a10c0263cafc31d39131beba533f6"></a>

### [`0057e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e080.md) → [`0057e3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3a0.md) FUN_0057e3a0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e080.md#insn-0057e09c) · [`0057e0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e080.md#insn-0057e0bc)
- 新版 [`0057e3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3a0.md#insn-0057e3bc) · [`0057e3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3a0.md#insn-0057e3dc)

~~~diff
- 0057e09c ["INT_ADD", "register:40f0:8", ["const:57e09c:8", "const:4:8"]]
- 0057e09c ["CALL", null, ["callee:00c54d90:8"]]
+ 0057e3bc ["INT_ADD", "register:40f0:8", ["const:57e3bc:8", "const:4:8"]]
+ 0057e3bc ["CALL", null, ["callee:00c54d90:8"]]
- 0057e09c bytes 41571b94
+ 0057e3bc bytes 755a1b94
- 0057e0bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0057e0bc ["INT_ADD", "register:40f0:8", ["const:57e0bc:8", "const:4:8"]]
- 0057e0bc ["CALLIND", null, ["register:0:8"]]
+ 0057e3dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057e3dc ["INT_ADD", "register:40f0:8", ["const:57e3dc:8", "const:4:8"]]
+ 0057e3dc ["CALLIND", null, ["register:0:8"]]
- 0057e0bc bytes 00013fd6
+ 0057e3dc bytes 00013fd6
~~~


<a id="compare-ee6cf7251f3d0d472025da0fe30cd243"></a>

### [`0057e428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e428.md) → [`0057e748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e748.md) FUN_0057e748

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c5c.md) · 呼出先 1件 [`00c5a320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a320.md)
- 新版 呼出元 1件 [`00550f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f7c.md) · 呼出先 1件 [`00c5b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e428.md#insn-0057e444)
- 新版 [`0057e764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e748.md#insn-0057e764)

~~~diff
- 0057e444 ["INT_ADD", "register:40f0:8", ["const:57e444:8", "const:4:8"]]
- 0057e444 ["CALL", null, ["callee:00c5b2f0:8"]]
+ 0057e764 ["INT_ADD", "register:40f0:8", ["const:57e764:8", "const:4:8"]]
+ 0057e764 ["CALL", null, ["callee:00c5b2f0:8"]]
- 0057e444 bytes b76f1b94
+ 0057e764 bytes e3721b94
~~~


<a id="compare-d78a6ecc92c6bfe111d2e51ce6b2359a"></a>

### [`0057e458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e458.md) → [`0057e778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e778.md) FUN_0057e778

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59930.md)
- 新版 呼出元 1件 [`00550f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f80.md) · 呼出先 5件 [`00550f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f04.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e458.md#insn-0057e490) · [`0057e4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e458.md#insn-0057e4a4) · [`0057e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e458.md#insn-0057e4c0)
- 新版 [`0057e7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e778.md#insn-0057e7b0) · [`0057e7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e778.md#insn-0057e7c4) · [`0057e7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e778.md#insn-0057e7e0)

~~~diff
- 0057e490 ["INT_ADD", "register:40f0:8", ["const:57e490:8", "const:4:8"]]
- 0057e490 ["CALL", null, ["callee:00c5a900:8"]]
+ 0057e7b0 ["INT_ADD", "register:40f0:8", ["const:57e7b0:8", "const:4:8"]]
+ 0057e7b0 ["CALL", null, ["callee:00c5a900:8"]]
- 0057e490 bytes 286d1b94
+ 0057e7b0 bytes 54701b94
- 0057e4a4 ["INT_ADD", "register:40f0:8", ["const:57e4a4:8", "const:4:8"]]
- 0057e4a4 ["CALL", null, ["callee:00550f04:8"]]
+ 0057e7c4 ["INT_ADD", "register:40f0:8", ["const:57e7c4:8", "const:4:8"]]
+ 0057e7c4 ["CALL", null, ["callee:00550f04:8"]]
- 0057e4a4 bytes d049ff97
+ 0057e7c4 bytes d049ff97
- 0057e4c0 ["INT_ADD", "register:40f0:8", ["const:57e4c0:8", "const:4:8"]]
- 0057e4c0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057e7e0 ["INT_ADD", "register:40f0:8", ["const:57e7e0:8", "const:4:8"]]
+ 0057e7e0 ["CALL", null, ["callee:00c54d90:8"]]
- 0057e4c0 bytes 38561b94
+ 0057e7e0 bytes 6c591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-752bc176bb6a320193b19835d36b0e4b"></a>

### [`0057ebcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ebcc.md) → [`0057eeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eeec.md) FUN_0057eeec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c70.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59930.md)
- 新版 呼出元 1件 [`00550f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f90.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ebfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ebcc.md#insn-0057ebfc) · [`0057ec2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ebcc.md#insn-0057ec2c)
- 新版 [`0057ef1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eeec.md#insn-0057ef1c) · [`0057ef4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eeec.md#insn-0057ef4c)

~~~diff
- 0057ebfc ["INT_ADD", "register:40f0:8", ["const:57ebfc:8", "const:4:8"]]
- 0057ebfc ["CALL", null, ["callee:00c5a900:8"]]
+ 0057ef1c ["INT_ADD", "register:40f0:8", ["const:57ef1c:8", "const:4:8"]]
+ 0057ef1c ["CALL", null, ["callee:00c5a900:8"]]
- 0057ebfc bytes 4d6b1b94
+ 0057ef1c bytes 796e1b94
- 0057ec2c ["INT_ADD", "register:40f0:8", ["const:57ec2c:8", "const:4:8"]]
- 0057ec2c ["CALL", null, ["callee:00c58f80:8"]]
+ 0057ef4c ["INT_ADD", "register:40f0:8", ["const:57ef4c:8", "const:4:8"]]
+ 0057ef4c ["CALL", null, ["callee:00c58f80:8"]]
- 0057ec2c bytes e1641b94
+ 0057ef4c bytes 0d681b94
~~~


<a id="compare-4cc0ea8a174ece8b6d570d75f6ea7b88"></a>

### [`0057ec34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec34.md) → [`0057ef54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057ef54.md) FUN_0057ef54

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d6c.md) · 呼出先 1件 [`00c5a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a330.md)
- 新版 呼出元 1件 [`0055108c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/0055108c.md) · 呼出先 1件 [`00c5b300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec34.md#insn-0057ec4c)
- 新版 [`0057ef6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057ef54.md#insn-0057ef6c)

~~~diff
- 0057ec4c ["INT_ADD", "register:40f0:8", ["const:57ec4c:8", "const:4:8"]]
- 0057ec4c ["CALL", null, ["callee:00c5b300:8"]]
+ 0057ef6c ["INT_ADD", "register:40f0:8", ["const:57ef6c:8", "const:4:8"]]
+ 0057ef6c ["CALL", null, ["callee:00c5b300:8"]]
- 0057ec4c bytes b96d1b94
+ 0057ef6c bytes e5701b94
~~~


<a id="compare-a338caa7faa165aa960800ceb76adb27"></a>

### [`0057ec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec60.md) → [`0057ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057ef80.md) FUN_0057ef80

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d70.md) · 呼出先 1件 [`00c5a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a360.md)
- 新版 呼出元 1件 [`00551090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551090.md) · 呼出先 1件 [`00c5b330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec60.md#insn-0057ec88)
- 新版 [`0057efa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057ef80.md#insn-0057efa8)

~~~diff
- 0057ec88 ["INT_ADD", "register:40f0:8", ["const:57ec88:8", "const:4:8"]]
- 0057ec88 ["CALL", null, ["callee:00c5b330:8"]]
+ 0057efa8 ["INT_ADD", "register:40f0:8", ["const:57efa8:8", "const:4:8"]]
+ 0057efa8 ["CALL", null, ["callee:00c5b330:8"]]
- 0057ec88 bytes b66d1b94
+ 0057efa8 bytes e2701b94
~~~


<a id="compare-396b85c3b89c9dc38e63fcf2cfa317dd"></a>

### [`0057ec9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec9c.md) → [`0057efbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057efbc.md) FUN_0057efbc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d74.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a370.md)
- 新版 呼出元 1件 [`00551094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551094.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057eccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec9c.md#insn-0057eccc) · [`0057ed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec9c.md#insn-0057ed04)
- 新版 [`0057efec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057efbc.md#insn-0057efec) · [`0057f024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057efbc.md#insn-0057f024)

~~~diff
- 0057eccc ["INT_ADD", "register:40f0:8", ["const:57eccc:8", "const:4:8"]]
- 0057eccc ["CALL", null, ["callee:00c5b340:8"]]
+ 0057efec ["INT_ADD", "register:40f0:8", ["const:57efec:8", "const:4:8"]]
+ 0057efec ["CALL", null, ["callee:00c5b340:8"]]
- 0057eccc bytes a96d1b94
+ 0057efec bytes d5701b94
- 0057ed04 ["INT_ADD", "register:40f0:8", ["const:57ed04:8", "const:4:8"]]
- 0057ed04 ["CALL", null, ["callee:00c58f80:8"]]
+ 0057f024 ["INT_ADD", "register:40f0:8", ["const:57f024:8", "const:4:8"]]
+ 0057f024 ["CALL", null, ["callee:00c58f80:8"]]
- 0057ed04 bytes ab641b94
+ 0057f024 bytes d7671b94
~~~


<a id="compare-9b862bbcbd6bf957cc4f185458120611"></a>

### [`0057ed0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ed0c.md) → [`0057f02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f02c.md) FUN_0057f02c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005552d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552d4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005555f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555f4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ed0c.md#insn-0057ed1c)
- 新版 [`0057f03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f02c.md#insn-0057f03c)

~~~diff
- 0057ed1c ["INT_ADD", "register:40f0:8", ["const:57ed1c:8", "const:4:8"]]
- 0057ed1c ["CALL", null, ["callee:005555f4:8"]]
+ 0057f03c ["INT_ADD", "register:40f0:8", ["const:57f03c:8", "const:4:8"]]
+ 0057f03c ["CALL", null, ["callee:005555f4:8"]]
- 0057ed1c bytes 6e59ff97
+ 0057f03c bytes 6e59ff97
~~~


<a id="compare-6bc06524182e19e90cdcc82afaeb6fcf"></a>

### [`0057fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md) → [`00580080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580080.md) FUN_00580080

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005552dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552dc.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`005555fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555fc.md) · 呼出先 3件 [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057fd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md#insn-0057fd84) · [`0057fd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md#insn-0057fd94) · [`0057fde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md#insn-0057fde4)
- 新版 [`005800a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580080.md#insn-005800a4) · [`005800b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580080.md#insn-005800b4) · [`00580104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580080.md#insn-00580104)

~~~diff
- 0057fd84 ["INT_ADD", "register:40f0:8", ["const:57fd84:8", "const:4:8"]]
- 0057fd84 ["CALL", null, ["callee:0057fe6c:8"]]
+ 005800a4 ["INT_ADD", "register:40f0:8", ["const:5800a4:8", "const:4:8"]]
+ 005800a4 ["CALL", null, ["callee:0057fe6c:8"]]
- 0057fd84 bytes 72ffff97
+ 005800a4 bytes 72ffff97
- 0057fd94 ["INT_ADD", "register:40f0:8", ["const:57fd94:8", "const:4:8"]]
- 0057fd94 ["CALL", null, ["callee:00c58f50:8"]]
+ 005800b4 ["INT_ADD", "register:40f0:8", ["const:5800b4:8", "const:4:8"]]
+ 005800b4 ["CALL", null, ["callee:00c58f50:8"]]
- 0057fd94 bytes 7b601b94
+ 005800b4 bytes a7631b94
- 0057fde4 ["INT_ADD", "register:40f0:8", ["const:57fde4:8", "const:4:8"]]
- 0057fde4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00580104 ["INT_ADD", "register:40f0:8", ["const:580104:8", "const:4:8"]]
+ 00580104 ["CALL", null, ["callee:00c58f80:8"]]
- 0057fde4 bytes 73601b94
+ 00580104 bytes 9f631b94
~~~


<a id="compare-25026c818b5a45141bcd56f0907b1c87"></a>

### [`0057ff3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md) → [`0058025c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/0058025c.md) FUN_0058025c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005552e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e8.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00555608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/00555608.md) · 呼出先 3件 [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ff7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md#insn-0057ff7c) · [`0057ff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md#insn-0057ff8c) · [`0057ffdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md#insn-0057ffdc)
- 新版 [`0058029c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/0058025c.md#insn-0058029c) · [`005802ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/0058025c.md#insn-005802ac) · [`005802fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/0058025c.md#insn-005802fc)

~~~diff
- 0057ff7c ["INT_ADD", "register:40f0:8", ["const:57ff7c:8", "const:4:8"]]
- 0057ff7c ["CALL", null, ["callee:0057fe6c:8"]]
+ 0058029c ["INT_ADD", "register:40f0:8", ["const:58029c:8", "const:4:8"]]
+ 0058029c ["CALL", null, ["callee:0057fe6c:8"]]
- 0057ff7c bytes f4feff97
+ 0058029c bytes f4feff97
- 0057ff8c ["INT_ADD", "register:40f0:8", ["const:57ff8c:8", "const:4:8"]]
- 0057ff8c ["CALL", null, ["callee:00c58f50:8"]]
+ 005802ac ["INT_ADD", "register:40f0:8", ["const:5802ac:8", "const:4:8"]]
+ 005802ac ["CALL", null, ["callee:00c58f50:8"]]
- 0057ff8c bytes fd5f1b94
+ 005802ac bytes 29631b94
- 0057ffdc ["INT_ADD", "register:40f0:8", ["const:57ffdc:8", "const:4:8"]]
- 0057ffdc ["CALL", null, ["callee:00c58f80:8"]]
+ 005802fc ["INT_ADD", "register:40f0:8", ["const:5802fc:8", "const:4:8"]]
+ 005802fc ["CALL", null, ["callee:00c58f80:8"]]
- 0057ffdc bytes f55f1b94
+ 005802fc bytes 21631b94
~~~


<a id="compare-b650de8b479d451c0b9e288afacf7f1b"></a>

### [`00580828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580828.md) → [`00580b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b48.md) FUN_00580b48

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580828.md#insn-00580844) · [`00580864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580828.md#insn-00580864)
- 新版 [`00580b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b48.md#insn-00580b64) · [`00580b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b48.md#insn-00580b84)

~~~diff
- 00580844 ["INT_ADD", "register:40f0:8", ["const:580844:8", "const:4:8"]]
- 00580844 ["CALL", null, ["callee:00c54d90:8"]]
+ 00580b64 ["INT_ADD", "register:40f0:8", ["const:580b64:8", "const:4:8"]]
+ 00580b64 ["CALL", null, ["callee:00c54d90:8"]]
- 00580844 bytes 574d1b94
+ 00580b64 bytes 8b501b94
- 00580864 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580864 ["INT_ADD", "register:40f0:8", ["const:580864:8", "const:4:8"]]
- 00580864 ["CALLIND", null, ["register:0:8"]]
+ 00580b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580b84 ["INT_ADD", "register:40f0:8", ["const:580b84:8", "const:4:8"]]
+ 00580b84 ["CALLIND", null, ["register:0:8"]]
- 00580864 bytes 00013fd6
+ 00580b84 bytes 00013fd6
~~~


<a id="compare-c93d25f278ac237c4349917463ebc1a3"></a>

### [`00580878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580878.md) → [`00580b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b98.md) FUN_00580b98

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580878.md#insn-00580894) · [`005808b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580878.md#insn-005808b4)
- 新版 [`00580bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b98.md#insn-00580bb4) · [`00580bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580b98.md#insn-00580bd4)

~~~diff
- 00580894 ["INT_ADD", "register:40f0:8", ["const:580894:8", "const:4:8"]]
- 00580894 ["CALL", null, ["callee:00c54d90:8"]]
+ 00580bb4 ["INT_ADD", "register:40f0:8", ["const:580bb4:8", "const:4:8"]]
+ 00580bb4 ["CALL", null, ["callee:00c54d90:8"]]
- 00580894 bytes 434d1b94
+ 00580bb4 bytes 77501b94
- 005808b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005808b4 ["INT_ADD", "register:40f0:8", ["const:5808b4:8", "const:4:8"]]
- 005808b4 ["CALLIND", null, ["register:0:8"]]
+ 00580bd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580bd4 ["INT_ADD", "register:40f0:8", ["const:580bd4:8", "const:4:8"]]
+ 00580bd4 ["CALLIND", null, ["register:0:8"]]
- 005808b4 bytes 00013fd6
+ 00580bd4 bytes 00013fd6
~~~


<a id="compare-cefcf141ffb4e9d4ce354a0fc236a5a8"></a>

### [`00580ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ac8.md) → [`00580de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580de8.md) FUN_00580de8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) · 呼出先 2件 [`00c58c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c70.md) [`00c58ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md)
- 新版 呼出元 1件 [`005607b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607b8.md) · 呼出先 2件 [`00c59c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c40.md) [`00c59c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ac8.md#insn-00580af4) · [`00580b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ac8.md#insn-00580b08) · [`00580b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ac8.md#insn-00580b20)
- 新版 [`00580e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580de8.md#insn-00580e14) · [`00580e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580de8.md#insn-00580e28) · [`00580e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580de8.md#insn-00580e40)

~~~diff
- 00580af4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580af4 ["INT_ADD", "register:40f0:8", ["const:580af4:8", "const:4:8"]]
- 00580af4 ["CALLIND", null, ["register:0:8"]]
+ 00580e14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580e14 ["INT_ADD", "register:40f0:8", ["const:580e14:8", "const:4:8"]]
+ 00580e14 ["CALLIND", null, ["register:0:8"]]
- 00580af4 bytes 00013fd6
+ 00580e14 bytes 00013fd6
- 00580b08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580b08 ["INT_ADD", "register:40f0:8", ["const:580b08:8", "const:4:8"]]
- 00580b08 ["CALLIND", null, ["register:0:8"]]
+ 00580e28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580e28 ["INT_ADD", "register:40f0:8", ["const:580e28:8", "const:4:8"]]
+ 00580e28 ["CALLIND", null, ["register:0:8"]]
- 00580b08 bytes 00013fd6
+ 00580e28 bytes 00013fd6
- 00580b20 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580b20 ["INT_ADD", "register:40f0:8", ["const:580b20:8", "const:4:8"]]
- 00580b20 ["CALLIND", null, ["register:0:8"]]
+ 00580e40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580e40 ["INT_ADD", "register:40f0:8", ["const:580e40:8", "const:4:8"]]
+ 00580e40 ["CALLIND", null, ["register:0:8"]]
- 00580b20 bytes 20013fd6
+ 00580e40 bytes 20013fd6
~~~


<a id="compare-2907783a321732d5c79c330dfd8417d0"></a>

### [`00580fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580fe8.md) → [`00581308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581308.md) FUN_00581308

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580fe8.md#insn-00581004) · [`00581024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580fe8.md#insn-00581024)
- 新版 [`00581324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581308.md#insn-00581324) · [`00581344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581308.md#insn-00581344)

~~~diff
- 00581004 ["INT_ADD", "register:40f0:8", ["const:581004:8", "const:4:8"]]
- 00581004 ["CALL", null, ["callee:00c54d90:8"]]
+ 00581324 ["INT_ADD", "register:40f0:8", ["const:581324:8", "const:4:8"]]
+ 00581324 ["CALL", null, ["callee:00c54d90:8"]]
- 00581004 bytes 674b1b94
+ 00581324 bytes 9b4e1b94
- 00581024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00581024 ["INT_ADD", "register:40f0:8", ["const:581024:8", "const:4:8"]]
- 00581024 ["CALLIND", null, ["register:0:8"]]
+ 00581344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00581344 ["INT_ADD", "register:40f0:8", ["const:581344:8", "const:4:8"]]
+ 00581344 ["CALLIND", null, ["register:0:8"]]
- 00581024 bytes 00013fd6
+ 00581344 bytes 00013fd6
~~~


<a id="compare-5cd01599fc74d41072ecd73b94dd8f3c"></a>

### [`00581038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581038.md) → [`00581358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581358.md) FUN_00581358

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581038.md#insn-00581054) · [`00581074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581038.md#insn-00581074)
- 新版 [`00581374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581358.md#insn-00581374) · [`00581394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581358.md#insn-00581394)

~~~diff
- 00581054 ["INT_ADD", "register:40f0:8", ["const:581054:8", "const:4:8"]]
- 00581054 ["CALL", null, ["callee:00c54d90:8"]]
+ 00581374 ["INT_ADD", "register:40f0:8", ["const:581374:8", "const:4:8"]]
+ 00581374 ["CALL", null, ["callee:00c54d90:8"]]
- 00581054 bytes 534b1b94
+ 00581374 bytes 874e1b94
- 00581074 ["COPY", "register:0:8", ["register:4040:8"]]
- 00581074 ["INT_ADD", "register:40f0:8", ["const:581074:8", "const:4:8"]]
- 00581074 ["CALLIND", null, ["register:0:8"]]
+ 00581394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00581394 ["INT_ADD", "register:40f0:8", ["const:581394:8", "const:4:8"]]
+ 00581394 ["CALLIND", null, ["register:0:8"]]
- 00581074 bytes 00013fd6
+ 00581394 bytes 00013fd6
~~~


<a id="compare-eae6c17a5e824181d441e860d7aa2309"></a>

### [`00581c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581c38.md) → [`00581f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581f58.md) FUN_00581f58

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005604a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a4.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)
- 新版 呼出元 1件 [`005607c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607c4.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59100.md) [`00c596a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581c38.md#insn-00581cb4) · [`00581d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581c38.md#insn-00581d74) · [`00581d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581c38.md#insn-00581d80)
- 新版 [`00581fd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581f58.md#insn-00581fd4) · [`00582094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581f58.md#insn-00582094) · [`005820a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581f58.md#insn-005820a0)

~~~diff
- 00581cb4 ["INT_ADD", "register:40f0:8", ["const:581cb4:8", "const:4:8"]]
- 00581cb4 ["CALL", null, ["callee:00c596a0:8"]]
+ 00581fd4 ["INT_ADD", "register:40f0:8", ["const:581fd4:8", "const:4:8"]]
+ 00581fd4 ["CALL", null, ["callee:00c596a0:8"]]
- 00581cb4 bytes 875a1b94
+ 00581fd4 bytes b35d1b94
- 00581d74 ["INT_ADD", "register:40f0:8", ["const:581d74:8", "const:4:8"]]
- 00581d74 ["CALL", null, ["callee:00c59100:8"]]
+ 00582094 ["INT_ADD", "register:40f0:8", ["const:582094:8", "const:4:8"]]
+ 00582094 ["CALL", null, ["callee:00c59100:8"]]
- 00581d74 bytes ef581b94
+ 00582094 bytes 1b5c1b94
- 00581d80 ["INT_ADD", "register:40f0:8", ["const:581d80:8", "const:4:8"]]
- 00581d80 ["CALL", null, ["callee:00c596a0:8"]]
+ 005820a0 ["INT_ADD", "register:40f0:8", ["const:5820a0:8", "const:4:8"]]
+ 005820a0 ["CALL", null, ["callee:00c596a0:8"]]
- 00581d80 bytes 545a1b94
+ 005820a0 bytes 805d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc5cae1a28273e10aafe2db9baa49d0"></a>

### [`00581f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f74.md) → [`00582294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582294.md) FUN_00582294

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f74.md#insn-00581f94)
- 新版 [`005822b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582294.md#insn-005822b4)

~~~diff
- 00581f94 ["COPY", "register:0:8", ["register:4050:8"]]
- 00581f94 ["INT_ADD", "register:40f0:8", ["const:581f94:8", "const:4:8"]]
- 00581f94 ["CALLIND", null, ["register:0:8"]]
+ 005822b4 ["COPY", "register:0:8", ["register:4050:8"]]
+ 005822b4 ["INT_ADD", "register:40f0:8", ["const:5822b4:8", "const:4:8"]]
+ 005822b4 ["CALLIND", null, ["register:0:8"]]
- 00581f94 bytes 40013fd6
+ 005822b4 bytes 40013fd6
~~~


<a id="compare-00f3a72eceddf92d11558a367156cfe4"></a>

### [`00582b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582b78.md) → [`00582e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582e98.md) FUN_00582e98

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0059796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059796c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00582bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582b78.md#insn-00582bb0) · [`00582bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582b78.md#insn-00582bcc) · [`00582be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582b78.md#insn-00582be8)
- 新版 [`00582ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582e98.md#insn-00582ed0) · [`00582eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582e98.md#insn-00582eec) · [`00582f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582e98.md#insn-00582f08)

~~~diff
- 00582bb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00582bb0 ["INT_ADD", "register:40f0:8", ["const:582bb0:8", "const:4:8"]]
- 00582bb0 ["CALLIND", null, ["register:0:8"]]
+ 00582ed0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582ed0 ["INT_ADD", "register:40f0:8", ["const:582ed0:8", "const:4:8"]]
+ 00582ed0 ["CALLIND", null, ["register:0:8"]]
- 00582bb0 bytes 20013fd6
+ 00582ed0 bytes 20013fd6
- 00582bcc ["INT_ADD", "register:40f0:8", ["const:582bcc:8", "const:4:8"]]
- 00582bcc ["CALL", null, ["callee:00c58f30:8"]]
+ 00582eec ["INT_ADD", "register:40f0:8", ["const:582eec:8", "const:4:8"]]
+ 00582eec ["CALL", null, ["callee:00c58f30:8"]]
- 00582bcc bytes e5541b94
+ 00582eec bytes 11581b94
- 00582be8 ["INT_ADD", "register:40f0:8", ["const:582be8:8", "const:4:8"]]
- 00582be8 ["CALL", null, ["callee:00c59130:8"]]
+ 00582f08 ["INT_ADD", "register:40f0:8", ["const:582f08:8", "const:4:8"]]
+ 00582f08 ["CALL", null, ["callee:00c59130:8"]]
- 00582be8 bytes 5e551b94
+ 00582f08 bytes 8a581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe7fbf038286ef74162909e7b652357"></a>

### [`00583204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583204.md) → [`00583524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583524.md) FUN_00583524

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0059796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059796c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058323c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583204.md#insn-0058323c) · [`00583258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583204.md#insn-00583258) · [`00583274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583204.md#insn-00583274)
- 新版 [`0058355c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583524.md#insn-0058355c) · [`00583578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583524.md#insn-00583578) · [`00583594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583524.md#insn-00583594)

~~~diff
- 0058323c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058323c ["INT_ADD", "register:40f0:8", ["const:58323c:8", "const:4:8"]]
- 0058323c ["CALLIND", null, ["register:0:8"]]
+ 0058355c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058355c ["INT_ADD", "register:40f0:8", ["const:58355c:8", "const:4:8"]]
+ 0058355c ["CALLIND", null, ["register:0:8"]]
- 0058323c bytes 20013fd6
+ 0058355c bytes 20013fd6
- 00583258 ["INT_ADD", "register:40f0:8", ["const:583258:8", "const:4:8"]]
- 00583258 ["CALL", null, ["callee:00c58f30:8"]]
+ 00583578 ["INT_ADD", "register:40f0:8", ["const:583578:8", "const:4:8"]]
+ 00583578 ["CALL", null, ["callee:00c58f30:8"]]
- 00583258 bytes 42531b94
+ 00583578 bytes 6e561b94
- 00583274 ["INT_ADD", "register:40f0:8", ["const:583274:8", "const:4:8"]]
- 00583274 ["CALL", null, ["callee:00c59130:8"]]
+ 00583594 ["INT_ADD", "register:40f0:8", ["const:583594:8", "const:4:8"]]
+ 00583594 ["CALL", null, ["callee:00c59130:8"]]
- 00583274 bytes bb531b94
+ 00583594 bytes e7561b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0718c2ef6403fca8cc2e845d82f3340"></a>

### [`005833dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833dc.md) → [`005836fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836fc.md) FUN_005836fc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c5a3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c5b380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058342c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833dc.md#insn-0058342c) · [`00583468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833dc.md#insn-00583468)
- 新版 [`0058374c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836fc.md#insn-0058374c) · [`00583788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836fc.md#insn-00583788)

~~~diff
- 0058342c ["INT_ADD", "register:40f0:8", ["const:58342c:8", "const:4:8"]]
- 0058342c ["CALL", null, ["callee:00c5b380:8"]]
+ 0058374c ["INT_ADD", "register:40f0:8", ["const:58374c:8", "const:4:8"]]
+ 0058374c ["CALL", null, ["callee:00c5b380:8"]]
- 0058342c bytes e15b1b94
+ 0058374c bytes 0d5f1b94
- 00583468 ["INT_ADD", "register:40f0:8", ["const:583468:8", "const:4:8"]]
- 00583468 ["CALL", null, ["callee:00c5b380:8"]]
+ 00583788 ["INT_ADD", "register:40f0:8", ["const:583788:8", "const:4:8"]]
+ 00583788 ["CALL", null, ["callee:00c5b380:8"]]
- 00583468 bytes d25b1b94
+ 00583788 bytes fe5e1b94
~~~


<a id="compare-46dffb74dbe888784453b1afc27bdda7"></a>

### [`005836fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005836fc.md) → [`00583a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a1c.md) FUN_00583a1c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00583718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005836fc.md#insn-00583718) · [`00583738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005836fc.md#insn-00583738)
- 新版 [`00583a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a1c.md#insn-00583a38) · [`00583a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a1c.md#insn-00583a58)

~~~diff
- 00583718 ["INT_ADD", "register:40f0:8", ["const:583718:8", "const:4:8"]]
- 00583718 ["CALL", null, ["callee:00c54d90:8"]]
+ 00583a38 ["INT_ADD", "register:40f0:8", ["const:583a38:8", "const:4:8"]]
+ 00583a38 ["CALL", null, ["callee:00c54d90:8"]]
- 00583718 bytes a2411b94
+ 00583a38 bytes d6441b94
- 00583738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00583738 ["INT_ADD", "register:40f0:8", ["const:583738:8", "const:4:8"]]
- 00583738 ["CALLIND", null, ["register:0:8"]]
+ 00583a58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00583a58 ["INT_ADD", "register:40f0:8", ["const:583a58:8", "const:4:8"]]
+ 00583a58 ["CALLIND", null, ["register:0:8"]]
- 00583738 bytes 00013fd6
+ 00583a58 bytes 00013fd6
~~~


<a id="compare-f5c54ef5344975ace56845311cea209e"></a>

### [`0058374c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058374c.md) → [`00583a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a6c.md) FUN_00583a6c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00549434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549434.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058379c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058374c.md#insn-0058379c) · [`005837c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058374c.md#insn-005837c8) · [`005837d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058374c.md#insn-005837d4)
- 新版 [`00583abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a6c.md#insn-00583abc) · [`00583ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a6c.md#insn-00583ae8) · [`00583af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583a6c.md#insn-00583af4)

~~~diff
- 0058379c ["INT_ADD", "register:40f0:8", ["const:58379c:8", "const:4:8"]]
- 0058379c ["CALL", null, ["callee:0043be80:8"]]
+ 00583abc ["INT_ADD", "register:40f0:8", ["const:583abc:8", "const:4:8"]]
+ 00583abc ["CALL", null, ["callee:0043be80:8"]]
- 0058379c bytes f1e0fa97
+ 00583abc bytes f1e0fa97
- 005837c8 ["INT_ADD", "register:40f0:8", ["const:5837c8:8", "const:4:8"]]
- 005837c8 ["CALL", null, ["callee:0043be80:8"]]
+ 00583ae8 ["INT_ADD", "register:40f0:8", ["const:583ae8:8", "const:4:8"]]
+ 00583ae8 ["CALL", null, ["callee:0043be80:8"]]
- 005837c8 bytes e6e0fa97
+ 00583ae8 bytes e6e0fa97
- 005837d4 ["INT_ADD", "register:40f0:8", ["const:5837d4:8", "const:4:8"]]
- 005837d4 ["CALL", null, ["callee:00549434:8"]]
+ 00583af4 ["INT_ADD", "register:40f0:8", ["const:583af4:8", "const:4:8"]]
+ 00583af4 ["CALL", null, ["callee:00549434:8"]]
- 005837d4 bytes 5016ff97
+ 00583af4 bytes 5016ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63cb9d59eb5327e6fb9703a6d51e39aa"></a>

### [`0058385c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058385c.md) → [`00583b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583b7c.md) FUN_00583b7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00583878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058385c.md#insn-00583878)
- 新版 [`00583b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583b7c.md#insn-00583b98)

~~~diff
- 00583878 ["INT_ADD", "register:40f0:8", ["const:583878:8", "const:4:8"]]
- 00583878 ["CALL", null, ["callee:00c54d60:8"]]
+ 00583b98 ["INT_ADD", "register:40f0:8", ["const:583b98:8", "const:4:8"]]
+ 00583b98 ["CALL", null, ["callee:00c54d60:8"]]
- 00583878 bytes 3e411b94
+ 00583b98 bytes 72441b94
~~~


<a id="compare-6155c6399bb5f8674a13f6b26231346b"></a>

### [`00584810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584810.md) → [`00584b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584b30.md) FUN_00584b30

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584810.md#insn-0058484c) · [`00584880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584810.md#insn-00584880)
- 新版 [`00584b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584b30.md#insn-00584b6c) · [`00584ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584b30.md#insn-00584ba0)

~~~diff
- 0058484c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058484c ["INT_ADD", "register:40f0:8", ["const:58484c:8", "const:4:8"]]
- 0058484c ["CALLIND", null, ["register:0:8"]]
+ 00584b6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584b6c ["INT_ADD", "register:40f0:8", ["const:584b6c:8", "const:4:8"]]
+ 00584b6c ["CALLIND", null, ["register:0:8"]]
- 0058484c bytes 00013fd6
+ 00584b6c bytes 00013fd6
- 00584880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584880 ["INT_ADD", "register:40f0:8", ["const:584880:8", "const:4:8"]]
- 00584880 ["CALLIND", null, ["register:0:8"]]
+ 00584ba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584ba0 ["INT_ADD", "register:40f0:8", ["const:584ba0:8", "const:4:8"]]
+ 00584ba0 ["CALLIND", null, ["register:0:8"]]
- 00584880 bytes 00013fd6
+ 00584ba0 bytes 00013fd6
~~~


<a id="compare-e38fa5bbb66c4a21c2123314d04ba376"></a>

### [`00584c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c00.md) → [`00584f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f20.md) FUN_00584f20

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c00.md#insn-00584c1c) · [`00584c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c00.md#insn-00584c3c)
- 新版 [`00584f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f20.md#insn-00584f3c) · [`00584f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f20.md#insn-00584f5c)

~~~diff
- 00584c1c ["INT_ADD", "register:40f0:8", ["const:584c1c:8", "const:4:8"]]
- 00584c1c ["CALL", null, ["callee:00c54d90:8"]]
+ 00584f3c ["INT_ADD", "register:40f0:8", ["const:584f3c:8", "const:4:8"]]
+ 00584f3c ["CALL", null, ["callee:00c54d90:8"]]
- 00584c1c bytes 613c1b94
+ 00584f3c bytes 953f1b94
- 00584c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00584c3c ["INT_ADD", "register:40f0:8", ["const:584c3c:8", "const:4:8"]]
- 00584c3c ["CALLIND", null, ["register:0:8"]]
+ 00584f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584f5c ["INT_ADD", "register:40f0:8", ["const:584f5c:8", "const:4:8"]]
+ 00584f5c ["CALLIND", null, ["register:0:8"]]
- 00584c3c bytes 00013fd6
+ 00584f5c bytes 00013fd6
~~~


<a id="compare-9ee003144425180bf8d1252795f576fc"></a>

### [`00584c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c50.md) → [`00584f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f70.md) FUN_00584f70

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c50.md#insn-00584c6c) · [`00584c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c50.md#insn-00584c8c)
- 新版 [`00584f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f70.md#insn-00584f8c) · [`00584fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584f70.md#insn-00584fac)

~~~diff
- 00584c6c ["INT_ADD", "register:40f0:8", ["const:584c6c:8", "const:4:8"]]
- 00584c6c ["CALL", null, ["callee:00c54d90:8"]]
+ 00584f8c ["INT_ADD", "register:40f0:8", ["const:584f8c:8", "const:4:8"]]
+ 00584f8c ["CALL", null, ["callee:00c54d90:8"]]
- 00584c6c bytes 4d3c1b94
+ 00584f8c bytes 813f1b94
- 00584c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00584c8c ["INT_ADD", "register:40f0:8", ["const:584c8c:8", "const:4:8"]]
- 00584c8c ["CALLIND", null, ["register:0:8"]]
+ 00584fac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584fac ["INT_ADD", "register:40f0:8", ["const:584fac:8", "const:4:8"]]
+ 00584fac ["CALLIND", null, ["register:0:8"]]
- 00584c8c bytes 00013fd6
+ 00584fac bytes 00013fd6
~~~


<a id="compare-db54f7a86cd97a0f54dbf33c9b90dc18"></a>

### [`00584ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ca0.md) → [`00584fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584fc0.md) FUN_00584fc0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ca0.md#insn-00584cc4) · [`00584cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ca0.md#insn-00584cdc) · [`00584d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ca0.md#insn-00584d00)
- 新版 [`00584fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584fc0.md#insn-00584fe4) · [`00584ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584fc0.md#insn-00584ffc) · [`00585020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584fc0.md#insn-00585020)

~~~diff
- 00584cc4 ["INT_ADD", "register:40f0:8", ["const:584cc4:8", "const:4:8"]]
- 00584cc4 ["CALL", null, ["callee:00c54d60:8"]]
+ 00584fe4 ["INT_ADD", "register:40f0:8", ["const:584fe4:8", "const:4:8"]]
+ 00584fe4 ["CALL", null, ["callee:00c54d60:8"]]
- 00584cc4 bytes 2b3c1b94
+ 00584fe4 bytes 5f3f1b94
- 00584cdc ["INT_ADD", "register:40f0:8", ["const:584cdc:8", "const:4:8"]]
- 00584cdc ["CALL", null, ["callee:00c54d90:8"]]
+ 00584ffc ["INT_ADD", "register:40f0:8", ["const:584ffc:8", "const:4:8"]]
+ 00584ffc ["CALL", null, ["callee:00c54d90:8"]]
- 00584cdc bytes 313c1b94
+ 00584ffc bytes 653f1b94
- 00584d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584d00 ["INT_ADD", "register:40f0:8", ["const:584d00:8", "const:4:8"]]
- 00584d00 ["CALLIND", null, ["register:0:8"]]
+ 00585020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00585020 ["INT_ADD", "register:40f0:8", ["const:585020:8", "const:4:8"]]
+ 00585020 ["CALLIND", null, ["register:0:8"]]
- 00584d00 bytes 00013fd6
+ 00585020 bytes 00013fd6
~~~


