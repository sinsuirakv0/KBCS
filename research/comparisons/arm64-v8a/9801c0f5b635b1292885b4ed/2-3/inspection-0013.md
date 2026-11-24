# v16.0.1 → v16.0.2 · 要調査の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-8e04aafbb870ac44249d2d5d7cad8f62"></a>

### [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) → [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) FUN_0056ce8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) · 呼出先 2件 [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)
- 新版 呼出元 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) · 呼出先 2件 [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ce90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md#insn-0056ce90) · [`0056ceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md#insn-0056ceec) · [`0056cf60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md#insn-0056cf60)
- 新版 `0056ced0`（命令位置の公開資料なし） · `0056cf2c`（命令位置の公開資料なし） · `0056cfa0`（命令位置の公開資料なし）

~~~diff
- 0056ce90 ["INT_ADD", "register:40f0:8", ["const:56ce90:8", "const:4:8"]]
- 0056ce90 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056ced0 ["INT_ADD", "register:40f0:8", ["const:56ced0:8", "const:4:8"]]
+ 0056ced0 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056ce90 bytes 77000094
+ 0056ced0 bytes 77000094
- 0056ceec ["INT_ADD", "register:40f0:8", ["const:56ceec:8", "const:4:8"]]
- 0056ceec ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056cf2c ["INT_ADD", "register:40f0:8", ["const:56cf2c:8", "const:4:8"]]
+ 0056cf2c ["CALL", null, ["callee:0056d0ac:8"]]
- 0056ceec bytes 60000094
+ 0056cf2c bytes 60000094
- 0056cf60 ["INT_ADD", "register:40f0:8", ["const:56cf60:8", "const:4:8"]]
- 0056cf60 ["CALL", null, ["local:b0:8"]]
+ 0056cfa0 ["INT_ADD", "register:40f0:8", ["const:56cfa0:8", "const:4:8"]]
+ 0056cfa0 ["CALL", null, ["local:b0:8"]]
- 0056cf60 bytes bbffff97
+ 0056cfa0 bytes bbffff97
~~~


<a id="compare-6299afba95a9d3c3e731a17519342a9e"></a>

### [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) → [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) FUN_0056d0ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) · 呼出先 2件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)
- 新版 呼出元 10件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) · 呼出先 2件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md#insn-0056d0d0) · [`0056d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md#insn-0056d170)
- 新版 `0056d110`（命令位置の公開資料なし） · `0056d1b0`（命令位置の公開資料なし）

~~~diff
- 0056d0d0 ["INT_ADD", "register:40f0:8", ["const:56d0d0:8", "const:4:8"]]
- 0056d0d0 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d110 ["INT_ADD", "register:40f0:8", ["const:56d110:8", "const:4:8"]]
+ 0056d110 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d0d0 bytes e8b31b94
+ 0056d110 bytes 0cb41b94
- 0056d170 ["INT_ADD", "register:40f0:8", ["const:56d170:8", "const:4:8"]]
- 0056d170 ["CALL", null, ["callee:0056d320:8"]]
+ 0056d1b0 ["INT_ADD", "register:40f0:8", ["const:56d1b0:8", "const:4:8"]]
+ 0056d1b0 ["CALL", null, ["callee:0056d320:8"]]
- 0056d170 bytes 5c000094
+ 0056d1b0 bytes 5c000094
~~~


<a id="compare-e0a6dd071cdc97292a596adf3f3e6b02"></a>

### [`0056d1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d1ac.md) → [`0056d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d1ec.md) FUN_0056d1ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d1ac.md#insn-0056d234)
- 新版 `0056d274`（命令位置の公開資料なし）

~~~diff
- 0056d234 ["INT_ADD", "register:40f0:8", ["const:56d234:8", "const:4:8"]]
- 0056d234 ["CALL", null, ["callee:0056d320:8"]]
+ 0056d274 ["INT_ADD", "register:40f0:8", ["const:56d274:8", "const:4:8"]]
+ 0056d274 ["CALL", null, ["callee:0056d320:8"]]
- 0056d234 bytes 2b000094
+ 0056d274 bytes 2b000094
~~~


<a id="compare-b5eb815add64898f5c03ee9631cae1ae"></a>

### [`0056d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md) → [`0056d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d2b0.md) FUN_0056d2b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) · 呼出先 1件 [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)
- 新版 呼出元 2件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) · 呼出先 1件 [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md#insn-0056d2a8)
- 新版 `0056d2e8`（命令位置の公開資料なし）

~~~diff
- 0056d2a8 ["INT_ADD", "register:40f0:8", ["const:56d2a8:8", "const:4:8"]]
- 0056d2a8 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d2e8 ["INT_ADD", "register:40f0:8", ["const:56d2e8:8", "const:4:8"]]
+ 0056d2e8 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d2a8 bytes 72b31b94
+ 0056d2e8 bytes 96b31b94
~~~


<a id="compare-5f0684871a790d4119e90bd5daebd442"></a>

### [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) → [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) FUN_0056d320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d1ac.md) · 呼出先 2件 [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)
- 新版 呼出元 6件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d1ec.md) · 呼出先 2件 [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d320) · [`0056d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d368) · [`0056d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d3b0)
- 新版 `0056d360`（命令位置の公開資料なし） · `0056d3a8`（命令位置の公開資料なし） · `0056d3f0`（命令位置の公開資料なし）

~~~diff
- 0056d320 ["INT_ADD", "register:40f0:8", ["const:56d320:8", "const:4:8"]]
- 0056d320 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d360 ["INT_ADD", "register:40f0:8", ["const:56d360:8", "const:4:8"]]
+ 0056d360 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d320 bytes 54b31b94
+ 0056d360 bytes 78b31b94
- 0056d368 ["INT_ADD", "register:40f0:8", ["const:56d368:8", "const:4:8"]]
- 0056d368 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d3a8 ["INT_ADD", "register:40f0:8", ["const:56d3a8:8", "const:4:8"]]
+ 0056d3a8 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d368 bytes 42b31b94
+ 0056d3a8 bytes 66b31b94
- 0056d3b0 ["INT_ADD", "register:40f0:8", ["const:56d3b0:8", "const:4:8"]]
- 0056d3b0 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d3f0 ["INT_ADD", "register:40f0:8", ["const:56d3f0:8", "const:4:8"]]
+ 0056d3f0 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d3b0 bytes 30b31b94
+ 0056d3f0 bytes 54b31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcba55925a874ed20141eb1eefefef06"></a>

### [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) → [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) FUN_0056d814

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) · 呼出先 1件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)
- 新版 呼出元 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) · 呼出先 1件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md#insn-0056d810)
- 新版 `0056d850`（命令位置の公開資料なし）

~~~diff
- 0056d810 ["INT_ADD", "register:40f0:8", ["const:56d810:8", "const:4:8"]]
- 0056d810 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056d850 ["INT_ADD", "register:40f0:8", ["const:56d850:8", "const:4:8"]]
+ 0056d850 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056d810 bytes 17feff97
+ 0056d850 bytes 17feff97
~~~


<a id="compare-62ac87afa236f54a01125e34e48e0daf"></a>

### [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) → [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) FUN_0056d9bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) · 呼出先 6件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) · 呼出先 6件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056db00) · [`0056dc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056dc7c) · [`0056ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056ddf0)
- 新版 `0056db40`（命令位置の公開資料なし） · `0056dcbc`（命令位置の公開資料なし） · `0056de30`（命令位置の公開資料なし）

~~~diff
- 0056db00 ["INT_ADD", "register:40f0:8", ["const:56db00:8", "const:4:8"]]
- 0056db00 ["CALL", null, ["callee:00c58160:8"]]
+ 0056db40 ["INT_ADD", "register:40f0:8", ["const:56db40:8", "const:4:8"]]
+ 0056db40 ["CALL", null, ["callee:00c58160:8"]]
- 0056db00 bytes 64a91b94
+ 0056db40 bytes 88a91b94
- 0056dc7c ["INT_ADD", "register:40f0:8", ["const:56dc7c:8", "const:4:8"]]
- 0056dc7c ["CALL", null, ["callee:0056f1e4:8"]]
+ 0056dcbc ["INT_ADD", "register:40f0:8", ["const:56dcbc:8", "const:4:8"]]
+ 0056dcbc ["CALL", null, ["callee:0056f1e4:8"]]
- 0056dc7c bytes 4a050094
+ 0056dcbc bytes 4a050094
- 0056ddf0 ["INT_ADD", "register:40f0:8", ["const:56ddf0:8", "const:4:8"]]
- 0056ddf0 ["CALL", null, ["callee:0056f1e4:8"]]
+ 0056de30 ["INT_ADD", "register:40f0:8", ["const:56de30:8", "const:4:8"]]
+ 0056de30 ["CALL", null, ["callee:0056f1e4:8"]]
- 0056ddf0 bytes ed040094
+ 0056de30 bytes ed040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3c98c9a8ed005aac04fa1a4062c08c"></a>

### [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) → [`0056ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056e/0056ef90.md) FUN_0056ef90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) · 呼出先 2件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md)
- 新版 呼出元 1件 [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) · 呼出先 2件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056efec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md#insn-0056efec) · [`0056f05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md#insn-0056f05c)
- 新版 `0056f02c`（命令位置の公開資料なし） · `0056f09c`（命令位置の公開資料なし）

~~~diff
- 0056efec ["INT_ADD", "register:40f0:8", ["const:56efec:8", "const:4:8"]]
- 0056efec ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056f02c ["INT_ADD", "register:40f0:8", ["const:56f02c:8", "const:4:8"]]
+ 0056f02c ["CALL", null, ["callee:0056d0ac:8"]]
- 0056efec bytes 20f8ff97
+ 0056f02c bytes 20f8ff97
- 0056f05c ["INT_ADD", "register:40f0:8", ["const:56f05c:8", "const:4:8"]]
- 0056f05c ["CALL", null, ["callee:0056d814:8"]]
+ 0056f09c ["INT_ADD", "register:40f0:8", ["const:56f09c:8", "const:4:8"]]
+ 0056f09c ["CALL", null, ["callee:0056d814:8"]]
- 0056f05c bytes def9ff97
+ 0056f09c bytes def9ff97
~~~


<a id="compare-4cd47f66248c35123e1338ca275ee68c"></a>

### [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) → [`0056f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f1e4.md) FUN_0056f1e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) · 呼出先 2件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md)
- 新版 呼出元 1件 [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md) · 呼出先 2件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md#insn-0056f1e8) · [`0056f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md#insn-0056f268)
- 新版 `0056f228`（命令位置の公開資料なし） · `0056f2a8`（命令位置の公開資料なし）

~~~diff
- 0056f1e8 ["INT_ADD", "register:40f0:8", ["const:56f1e8:8", "const:4:8"]]
- 0056f1e8 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056f228 ["INT_ADD", "register:40f0:8", ["const:56f228:8", "const:4:8"]]
+ 0056f228 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056f1e8 bytes a1f7ff97
+ 0056f228 bytes a1f7ff97
- 0056f268 ["INT_ADD", "register:40f0:8", ["const:56f268:8", "const:4:8"]]
- 0056f268 ["CALL", null, ["callee:0056d814:8"]]
+ 0056f2a8 ["INT_ADD", "register:40f0:8", ["const:56f2a8:8", "const:4:8"]]
+ 0056f2a8 ["CALL", null, ["callee:0056d814:8"]]
- 0056f268 bytes 5bf9ff97
+ 0056f2a8 bytes 5bf9ff97
~~~


<a id="compare-5fb6f8513fd99e551ab96318437631c1"></a>

### [`0056f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f538.md) → [`0056f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f578.md) FUN_0056f578

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f538.md#insn-0056f558)
- 新版 `0056f598`（命令位置の公開資料なし）

~~~diff
- 0056f558 ["INT_ADD", "register:40f0:8", ["const:56f558:8", "const:4:8"]]
- 0056f558 ["CALL", null, ["callee:0056d320:8"]]
+ 0056f598 ["INT_ADD", "register:40f0:8", ["const:56f598:8", "const:4:8"]]
+ 0056f598 ["CALL", null, ["callee:0056d320:8"]]
- 0056f558 bytes 62f7ff97
+ 0056f598 bytes 62f7ff97
~~~


<a id="compare-389bef2d40ab20328b574449dd60b659"></a>

### [`0056f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md) → [`0056f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f5d8.md) FUN_0056f5d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5a8) · [`0056f5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5b8) · [`0056f5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5c8)
- 新版 `0056f5e8`（命令位置の公開資料なし） · `0056f5f8`（命令位置の公開資料なし） · `0056f608`（命令位置の公開資料なし）

~~~diff
- 0056f5a8 ["INT_ADD", "register:40f0:8", ["const:56f5a8:8", "const:4:8"]]
- 0056f5a8 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056f5e8 ["INT_ADD", "register:40f0:8", ["const:56f5e8:8", "const:4:8"]]
+ 0056f5e8 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056f5a8 bytes b1f6ff97
+ 0056f5e8 bytes b1f6ff97
- 0056f5b8 ["INT_ADD", "register:40f0:8", ["const:56f5b8:8", "const:4:8"]]
- 0056f5b8 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056f5f8 ["INT_ADD", "register:40f0:8", ["const:56f5f8:8", "const:4:8"]]
+ 0056f5f8 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056f5b8 bytes adf6ff97
+ 0056f5f8 bytes adf6ff97
- 0056f5c8 ["INT_ADD", "register:40f0:8", ["const:56f5c8:8", "const:4:8"]]
- 0056f5c8 ["CALL", null, ["callee:0056d0ac:8"]]
+ 0056f608 ["INT_ADD", "register:40f0:8", ["const:56f608:8", "const:4:8"]]
+ 0056f608 ["CALL", null, ["callee:0056d0ac:8"]]
- 0056f5c8 bytes a9f6ff97
+ 0056f608 bytes a9f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5ca925ccfce8033d9bad1099837d7b"></a>

### [`0056f644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f644.md) → [`0056f684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056f684.md) FUN_0056f684

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 2件 [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 2件 [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f644.md#insn-0056f690)
- 新版 `0056f6d0`（命令位置の公開資料なし）

~~~diff
- 0056f690 ["INT_ADD", "register:40f0:8", ["const:56f690:8", "const:4:8"]]
- 0056f690 ["CALL", null, ["callee:00c5a120:8"]]
+ 0056f6d0 ["INT_ADD", "register:40f0:8", ["const:56f6d0:8", "const:4:8"]]
+ 0056f6d0 ["CALL", null, ["callee:00c5a120:8"]]
- 0056f690 bytes 70aa1b94
+ 0056f6d0 bytes 94aa1b94
~~~


<a id="compare-2e1c2ac8ad42b5ad4d85a990f2571f8d"></a>

### [`0056fbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fbfc.md) → [`0056fc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fc3c.md) FUN_0056fc3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fbfc.md#insn-0056fc1c)
- 新版 `0056fc5c`（命令位置の公開資料なし）

~~~diff
- 0056fc1c ["INT_ADD", "register:40f0:8", ["const:56fc1c:8", "const:4:8"]]
- 0056fc1c ["CALL", null, ["callee:00c58160:8"]]
+ 0056fc5c ["INT_ADD", "register:40f0:8", ["const:56fc5c:8", "const:4:8"]]
+ 0056fc5c ["CALL", null, ["callee:00c58160:8"]]
- 0056fc1c bytes 1da11b94
+ 0056fc5c bytes 41a11b94
~~~


<a id="compare-62add474ba090c02998edd7e72787386"></a>

### [`0056fcc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md) → [`0056fd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fd08.md) FUN_0056fd08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 3件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c59fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59fe0.md) [`00c5a110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a110.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 3件 [`00c58510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58510.md) [`00c5a0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0b0.md) [`00c5a1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fcec) · [`0056fcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fcf8) · [`0056fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fd20)
- 新版 `0056fd2c`（命令位置の公開資料なし） · `0056fd38`（命令位置の公開資料なし） · `0056fd60`（命令位置の公開資料なし）

~~~diff
- 0056fcec ["INT_ADD", "register:40f0:8", ["const:56fcec:8", "const:4:8"]]
- 0056fcec ["CALL", null, ["callee:00c5a0b0:8"]]
+ 0056fd2c ["INT_ADD", "register:40f0:8", ["const:56fd2c:8", "const:4:8"]]
+ 0056fd2c ["CALL", null, ["callee:00c5a0b0:8"]]
- 0056fcec bytes bda81b94
+ 0056fd2c bytes e1a81b94
- 0056fcf8 ["INT_ADD", "register:40f0:8", ["const:56fcf8:8", "const:4:8"]]
- 0056fcf8 ["CALL", null, ["callee:00c5a1e0:8"]]
+ 0056fd38 ["INT_ADD", "register:40f0:8", ["const:56fd38:8", "const:4:8"]]
+ 0056fd38 ["CALL", null, ["callee:00c5a1e0:8"]]
- 0056fcf8 bytes 06a91b94
+ 0056fd38 bytes 2aa91b94
- 0056fd20 ["INT_ADD", "register:40f0:8", ["const:56fd20:8", "const:4:8"]]
- 0056fd20 ["CALL", null, ["callee:00c58510:8"]]
+ 0056fd60 ["INT_ADD", "register:40f0:8", ["const:56fd60:8", "const:4:8"]]
+ 0056fd60 ["CALL", null, ["callee:00c58510:8"]]
- 0056fd20 bytes c8a11b94
+ 0056fd60 bytes eca11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3ff253343fbf94a668b26e359e75617"></a>

### [`00570948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md) → [`00570988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570988.md) FUN_00570988

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a010.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)
- 新版 呼出元 1件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0e0.md) [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005709a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-005709a0) · [`005709f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-005709f0) · [`00570a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-00570a84)
- 新版 `005709e0`（命令位置の公開資料なし） · `00570a30`（命令位置の公開資料なし） · `00570ac4`（命令位置の公開資料なし）

~~~diff
- 005709a0 ["INT_ADD", "register:40f0:8", ["const:5709a0:8", "const:4:8"]]
- 005709a0 ["CALL", null, ["callee:00c5a120:8"]]
+ 005709e0 ["INT_ADD", "register:40f0:8", ["const:5709e0:8", "const:4:8"]]
+ 005709e0 ["CALL", null, ["callee:00c5a120:8"]]
- 005709a0 bytes aca51b94
+ 005709e0 bytes d0a51b94
- 005709f0 ["INT_ADD", "register:40f0:8", ["const:5709f0:8", "const:4:8"]]
- 005709f0 ["CALL", null, ["callee:00c5a150:8"]]
+ 00570a30 ["INT_ADD", "register:40f0:8", ["const:570a30:8", "const:4:8"]]
+ 00570a30 ["CALL", null, ["callee:00c5a150:8"]]
- 005709f0 bytes a4a51b94
+ 00570a30 bytes c8a51b94
- 00570a84 ["INT_ADD", "register:40f0:8", ["const:570a84:8", "const:4:8"]]
- 00570a84 ["CALL", null, ["callee:00c5a200:8"]]
+ 00570ac4 ["INT_ADD", "register:40f0:8", ["const:570ac4:8", "const:4:8"]]
+ 00570ac4 ["CALL", null, ["callee:00c5a200:8"]]
- 00570a84 bytes aba51b94
+ 00570ac4 bytes cfa51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70915f75f411e8f9f35928bca0ed1b98"></a>

### [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md) → [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md) FUN_00570e84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00570fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00570fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570eb0) · [`00570edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570edc) · [`00570f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570f3c)
- 新版 `00570ef0`（命令位置の公開資料なし） · `00570f1c`（命令位置の公開資料なし） · `00570f7c`（命令位置の公開資料なし）

~~~diff
- 00570eb0 ["INT_ADD", "register:40f0:8", ["const:570eb0:8", "const:4:8"]]
- 00570eb0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00570ef0 ["INT_ADD", "register:40f0:8", ["const:570ef0:8", "const:4:8"]]
+ 00570ef0 ["CALL", null, ["callee:00c57f60:8"]]
- 00570eb0 bytes f89b1b94
+ 00570ef0 bytes 1c9c1b94
- 00570edc ["INT_ADD", "register:40f0:8", ["const:570edc:8", "const:4:8"]]
- 00570edc ["CALL", null, ["callee:00c53d70:8"]]
+ 00570f1c ["INT_ADD", "register:40f0:8", ["const:570f1c:8", "const:4:8"]]
+ 00570f1c ["CALL", null, ["callee:00c53d70:8"]]
- 00570edc bytes 7d8b1b94
+ 00570f1c bytes 958b1b94
- 00570f3c ["INT_ADD", "register:40f0:8", ["const:570f3c:8", "const:4:8"]]
- 00570f3c ["CALL", null, ["callee:00c53da0:8"]]
+ 00570f7c ["INT_ADD", "register:40f0:8", ["const:570f7c:8", "const:4:8"]]
+ 00570f7c ["CALL", null, ["callee:00c53da0:8"]]
- 00570f3c bytes 718b1b94
+ 00570f7c bytes 898b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c394297c09b7f5e9c14cfeac45cdbd"></a>

### [`00571074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md) → [`005710b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md) FUN_005710b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-00571088) · [`0057109c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-0057109c) · [`005710bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-005710bc)
- 新版 `005710c8`（命令位置の公開資料なし） · `005710dc`（命令位置の公開資料なし） · `005710fc`（命令位置の公開資料なし）

~~~diff
- 00571088 ["INT_ADD", "register:40f0:8", ["const:571088:8", "const:4:8"]]
- 00571088 ["CALL", null, ["callee:0056b710:8"]]
+ 005710c8 ["INT_ADD", "register:40f0:8", ["const:5710c8:8", "const:4:8"]]
+ 005710c8 ["CALL", null, ["callee:0056b710:8"]]
- 00571088 bytes 92e9ff97
+ 005710c8 bytes 92e9ff97
- 0057109c ["INT_ADD", "register:40f0:8", ["const:57109c:8", "const:4:8"]]
- 0057109c ["CALL", null, ["callee:00c53da0:8"]]
+ 005710dc ["INT_ADD", "register:40f0:8", ["const:5710dc:8", "const:4:8"]]
+ 005710dc ["CALL", null, ["callee:00c53da0:8"]]
- 0057109c bytes 198b1b94
+ 005710dc bytes 318b1b94
- 005710bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005710bc ["INT_ADD", "register:40f0:8", ["const:5710bc:8", "const:4:8"]]
- 005710bc ["CALLIND", null, ["register:0:8"]]
+ 005710fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005710fc ["INT_ADD", "register:40f0:8", ["const:5710fc:8", "const:4:8"]]
+ 005710fc ["CALLIND", null, ["register:0:8"]]
- 005710bc bytes 00013fd6
+ 005710fc bytes 00013fd6
~~~


<a id="compare-849f3c0f81f13b3a175d60e20be463a8"></a>

### [`005711b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md) → [`005711f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md) FUN_005711f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005711c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711c8) · [`005711dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711dc) · [`005711fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711fc)
- 新版 `00571208`（命令位置の公開資料なし） · `0057121c`（命令位置の公開資料なし） · `0057123c`（命令位置の公開資料なし）

~~~diff
- 005711c8 ["INT_ADD", "register:40f0:8", ["const:5711c8:8", "const:4:8"]]
- 005711c8 ["CALL", null, ["callee:0056b710:8"]]
+ 00571208 ["INT_ADD", "register:40f0:8", ["const:571208:8", "const:4:8"]]
+ 00571208 ["CALL", null, ["callee:0056b710:8"]]
- 005711c8 bytes 42e9ff97
+ 00571208 bytes 42e9ff97
- 005711dc ["INT_ADD", "register:40f0:8", ["const:5711dc:8", "const:4:8"]]
- 005711dc ["CALL", null, ["callee:00c53da0:8"]]
+ 0057121c ["INT_ADD", "register:40f0:8", ["const:57121c:8", "const:4:8"]]
+ 0057121c ["CALL", null, ["callee:00c53da0:8"]]
- 005711dc bytes c98a1b94
+ 0057121c bytes e18a1b94
- 005711fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005711fc ["INT_ADD", "register:40f0:8", ["const:5711fc:8", "const:4:8"]]
- 005711fc ["CALLIND", null, ["register:0:8"]]
+ 0057123c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057123c ["INT_ADD", "register:40f0:8", ["const:57123c:8", "const:4:8"]]
+ 0057123c ["CALLIND", null, ["register:0:8"]]
- 005711fc bytes 00013fd6
+ 0057123c bytes 00013fd6
~~~


<a id="compare-f8262dd0a02c5e939880f8920e44b901"></a>

### [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) → [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) FUN_00571840

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055098c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/0055098c.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509cc.md) · 呼出先 8件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-00571820) · [`00571828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-00571828) · [`0057186c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-0057186c)
- 新版 `00571860`（命令位置の公開資料なし） · `00571868`（命令位置の公開資料なし） · `005718ac`（命令位置の公開資料なし）

~~~diff
- 00571820 ["INT_ADD", "register:40f0:8", ["const:571820:8", "const:4:8"]]
- 00571820 ["CALL", null, ["callee:00588eac:8"]]
+ 00571860 ["INT_ADD", "register:40f0:8", ["const:571860:8", "const:4:8"]]
+ 00571860 ["CALL", null, ["callee:00588eac:8"]]
- 00571820 bytes 935d0094
+ 00571860 bytes 935d0094
- 00571828 ["INT_ADD", "register:40f0:8", ["const:571828:8", "const:4:8"]]
- 00571828 ["CALL", null, ["callee:0058919c:8"]]
+ 00571868 ["INT_ADD", "register:40f0:8", ["const:571868:8", "const:4:8"]]
+ 00571868 ["CALL", null, ["callee:0058919c:8"]]
- 00571828 bytes 4d5e0094
+ 00571868 bytes 4d5e0094
- 0057186c ["INT_ADD", "register:40f0:8", ["const:57186c:8", "const:4:8"]]
- 0057186c ["CALL", null, ["callee:00589360:8"]]
+ 005718ac ["INT_ADD", "register:40f0:8", ["const:5718ac:8", "const:4:8"]]
+ 005718ac ["CALL", null, ["callee:00589360:8"]]
- 0057186c bytes ad5e0094
+ 005718ac bytes ad5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c92b74a1664865ccc88e6d40548b827"></a>

### [`00572864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md) → [`005728a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728a4.md) FUN_005728a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00572880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md#insn-00572880) · [`005728a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md#insn-005728a0)
- 新版 `005728c0`（命令位置の公開資料なし） · `005728e0`（命令位置の公開資料なし）

~~~diff
- 00572880 ["INT_ADD", "register:40f0:8", ["const:572880:8", "const:4:8"]]
- 00572880 ["CALL", null, ["callee:00c53da0:8"]]
+ 005728c0 ["INT_ADD", "register:40f0:8", ["const:5728c0:8", "const:4:8"]]
+ 005728c0 ["CALL", null, ["callee:00c53da0:8"]]
- 00572880 bytes 20851b94
+ 005728c0 bytes 38851b94
- 005728a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005728a0 ["INT_ADD", "register:40f0:8", ["const:5728a0:8", "const:4:8"]]
- 005728a0 ["CALLIND", null, ["register:0:8"]]
+ 005728e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005728e0 ["INT_ADD", "register:40f0:8", ["const:5728e0:8", "const:4:8"]]
+ 005728e0 ["CALLIND", null, ["register:0:8"]]
- 005728a0 bytes 00013fd6
+ 005728e0 bytes 00013fd6
~~~


<a id="compare-269ec103278a7c9d58c516ca2f9b3e2b"></a>

### [`00574424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md) → [`00574464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md) FUN_00574464

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057444c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md#insn-0057444c) · [`00574470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md#insn-00574470)
- 新版 `0057448c`（命令位置の公開資料なし） · `005744b0`（命令位置の公開資料なし）

~~~diff
- 0057444c ["INT_ADD", "register:40f0:8", ["const:57444c:8", "const:4:8"]]
- 0057444c ["CALL", null, ["callee:00574768:8"]]
+ 0057448c ["INT_ADD", "register:40f0:8", ["const:57448c:8", "const:4:8"]]
+ 0057448c ["CALL", null, ["callee:00574768:8"]]
- 0057444c bytes b7000094
+ 0057448c bytes b7000094
- 00574470 ["INT_ADD", "register:40f0:8", ["const:574470:8", "const:4:8"]]
- 00574470 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005744b0 ["INT_ADD", "register:40f0:8", ["const:5744b0:8", "const:4:8"]]
+ 005744b0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00574470 bytes 9c8e1b94
+ 005744b0 bytes c08e1b94
~~~


<a id="compare-04d3e99b0794b7765786deff71a10393"></a>

### [`00574808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md) → [`00574848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md) FUN_00574848

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md#insn-00574830) · [`00574854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md#insn-00574854)
- 新版 `00574870`（命令位置の公開資料なし） · `00574894`（命令位置の公開資料なし）

~~~diff
- 00574830 ["INT_ADD", "register:40f0:8", ["const:574830:8", "const:4:8"]]
- 00574830 ["CALL", null, ["callee:00574b0c:8"]]
+ 00574870 ["INT_ADD", "register:40f0:8", ["const:574870:8", "const:4:8"]]
+ 00574870 ["CALL", null, ["callee:00574b0c:8"]]
- 00574830 bytes a7000094
+ 00574870 bytes a7000094
- 00574854 ["INT_ADD", "register:40f0:8", ["const:574854:8", "const:4:8"]]
- 00574854 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00574894 ["INT_ADD", "register:40f0:8", ["const:574894:8", "const:4:8"]]
+ 00574894 ["CALL", null, ["callee:00c57fb0:8"]]
- 00574854 bytes a38d1b94
+ 00574894 bytes c78d1b94
~~~


<a id="compare-87fbe202d62bd6554df19444fd42742e"></a>

### [`00574a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a6c.md) → [`00574aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574aac.md) FUN_00574aac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a6c.md#insn-00574a88)
- 新版 `00574ac8`（命令位置の公開資料なし）

~~~diff
- 00574a88 ["INT_ADD", "register:40f0:8", ["const:574a88:8", "const:4:8"]]
- 00574a88 ["CALL", null, ["callee:00c53d70:8"]]
+ 00574ac8 ["INT_ADD", "register:40f0:8", ["const:574ac8:8", "const:4:8"]]
+ 00574ac8 ["CALL", null, ["callee:00c53d70:8"]]
- 00574a88 bytes 927c1b94
+ 00574ac8 bytes aa7c1b94
~~~


<a id="compare-5ab6bcd39b5dc58fcabbce6cb8a1c43b"></a>

### [`00574a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a94.md) → [`00574ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574ad4.md) FUN_00574ad4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a94.md#insn-00574ab0)
- 新版 `00574af0`（命令位置の公開資料なし）

~~~diff
- 00574ab0 ["INT_ADD", "register:40f0:8", ["const:574ab0:8", "const:4:8"]]
- 00574ab0 ["CALL", null, ["callee:00c53d70:8"]]
+ 00574af0 ["INT_ADD", "register:40f0:8", ["const:574af0:8", "const:4:8"]]
+ 00574af0 ["CALL", null, ["callee:00c53d70:8"]]
- 00574ab0 bytes 887c1b94
+ 00574af0 bytes a07c1b94
~~~


<a id="compare-f8d51655136c32bc81d1aa34a1314b91"></a>

### [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) → [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) FUN_00574cbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005717f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717f8.md) [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) · 呼出先 2件 [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00571838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571838.md) [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) · 呼出先 2件 [`00574cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574cbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574c98) · [`00574ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574ca4) · [`00574cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574cd8)
- 新版 `00574cd8`（命令位置の公開資料なし） · `00574ce4`（命令位置の公開資料なし） · `00574d18`（命令位置の公開資料なし）

~~~diff
- 00574c98 ["INT_ADD", "register:40f0:8", ["const:574c98:8", "const:4:8"]]
- 00574c98 ["CALL", null, ["local:b0:8"]]
+ 00574cd8 ["INT_ADD", "register:40f0:8", ["const:574cd8:8", "const:4:8"]]
+ 00574cd8 ["CALL", null, ["local:b0:8"]]
- 00574c98 bytes f9ffff97
+ 00574cd8 bytes f9ffff97
- 00574ca4 ["INT_ADD", "register:40f0:8", ["const:574ca4:8", "const:4:8"]]
- 00574ca4 ["CALL", null, ["local:b0:8"]]
+ 00574ce4 ["INT_ADD", "register:40f0:8", ["const:574ce4:8", "const:4:8"]]
+ 00574ce4 ["CALL", null, ["local:b0:8"]]
- 00574ca4 bytes f6ffff97
+ 00574ce4 bytes f6ffff97
- 00574cd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574cd8 ["INT_ADD", "register:40f0:8", ["const:574cd8:8", "const:4:8"]]
- 00574cd8 ["CALLIND", null, ["register:0:8"]]
+ 00574d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574d18 ["INT_ADD", "register:40f0:8", ["const:574d18:8", "const:4:8"]]
+ 00574d18 ["CALLIND", null, ["register:0:8"]]
- 00574cd8 bytes 00013fd6
+ 00574d18 bytes 00013fd6
~~~


<a id="compare-27af9ee5a64de4da2917b03662bdc2ab"></a>

### [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) → [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) FUN_00574d2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 96件 [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 96件 [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md#insn-00574d60) · [`00574d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md#insn-00574d84)
- 新版 `00574da0`（命令位置の公開資料なし） · `00574dc4`（命令位置の公開資料なし）

~~~diff
- 00574d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574d60 ["INT_ADD", "register:40f0:8", ["const:574d60:8", "const:4:8"]]
- 00574d60 ["CALLIND", null, ["register:0:8"]]
+ 00574da0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574da0 ["INT_ADD", "register:40f0:8", ["const:574da0:8", "const:4:8"]]
+ 00574da0 ["CALLIND", null, ["register:0:8"]]
- 00574d60 bytes 00013fd6
+ 00574da0 bytes 00013fd6
- 00574d84 ["INT_ADD", "register:40f0:8", ["const:574d84:8", "const:4:8"]]
- 00574d84 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00574dc4 ["INT_ADD", "register:40f0:8", ["const:574dc4:8", "const:4:8"]]
+ 00574dc4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00574d84 bytes 578c1b94
+ 00574dc4 bytes 7b8c1b94
~~~


<a id="compare-f26d7ff85fe0b3655b9adc656e56d03a"></a>

### [`00574d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md) → [`00574dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md) FUN_00574dc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574df4) · [`00574e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574e04) · [`00574e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574e24)
- 新版 `00574e34`（命令位置の公開資料なし） · `00574e44`（命令位置の公開資料なし） · `00574e64`（命令位置の公開資料なし）

~~~diff
- 00574df4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574df4 ["INT_ADD", "register:40f0:8", ["const:574df4:8", "const:4:8"]]
- 00574df4 ["CALLIND", null, ["register:0:8"]]
+ 00574e34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574e34 ["INT_ADD", "register:40f0:8", ["const:574e34:8", "const:4:8"]]
+ 00574e34 ["CALLIND", null, ["register:0:8"]]
- 00574df4 bytes 00013fd6
+ 00574e34 bytes 00013fd6
- 00574e04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574e04 ["INT_ADD", "register:40f0:8", ["const:574e04:8", "const:4:8"]]
- 00574e04 ["CALLIND", null, ["register:0:8"]]
+ 00574e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574e44 ["INT_ADD", "register:40f0:8", ["const:574e44:8", "const:4:8"]]
+ 00574e44 ["CALLIND", null, ["register:0:8"]]
- 00574e04 bytes 00013fd6
+ 00574e44 bytes 00013fd6
- 00574e24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574e24 ["INT_ADD", "register:40f0:8", ["const:574e24:8", "const:4:8"]]
- 00574e24 ["CALLIND", null, ["register:0:8"]]
+ 00574e64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574e64 ["INT_ADD", "register:40f0:8", ["const:574e64:8", "const:4:8"]]
+ 00574e64 ["CALLIND", null, ["register:0:8"]]
- 00574e24 bytes 00013fd6
+ 00574e64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86bf4e7897f7889a7c5dee1321742c7"></a>

### [`00574ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md) → [`00574f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md) FUN_00574f30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00572be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f5c) · [`00574f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f6c) · [`00574f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f8c)
- 新版 `00574f9c`（命令位置の公開資料なし） · `00574fac`（命令位置の公開資料なし） · `00574fcc`（命令位置の公開資料なし）

~~~diff
- 00574f5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f5c ["INT_ADD", "register:40f0:8", ["const:574f5c:8", "const:4:8"]]
- 00574f5c ["CALLIND", null, ["register:0:8"]]
+ 00574f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f9c ["INT_ADD", "register:40f0:8", ["const:574f9c:8", "const:4:8"]]
+ 00574f9c ["CALLIND", null, ["register:0:8"]]
- 00574f5c bytes 00013fd6
+ 00574f9c bytes 00013fd6
- 00574f6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f6c ["INT_ADD", "register:40f0:8", ["const:574f6c:8", "const:4:8"]]
- 00574f6c ["CALLIND", null, ["register:0:8"]]
+ 00574fac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574fac ["INT_ADD", "register:40f0:8", ["const:574fac:8", "const:4:8"]]
+ 00574fac ["CALLIND", null, ["register:0:8"]]
- 00574f6c bytes 00013fd6
+ 00574fac bytes 00013fd6
- 00574f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f8c ["INT_ADD", "register:40f0:8", ["const:574f8c:8", "const:4:8"]]
- 00574f8c ["CALLIND", null, ["register:0:8"]]
+ 00574fcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574fcc ["INT_ADD", "register:40f0:8", ["const:574fcc:8", "const:4:8"]]
+ 00574fcc ["CALLIND", null, ["register:0:8"]]
- 00574f8c bytes 00013fd6
+ 00574fcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc6cbd21ff5d010a34fd7cdafa101765"></a>

### [`00575058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md) → [`00575098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575098.md) FUN_00575098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005750ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750ac) · [`005750c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750c0) · [`005750c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750c8)
- 新版 `005750ec`（命令位置の公開資料なし） · `00575100`（命令位置の公開資料なし） · `00575108`（命令位置の公開資料なし）

~~~diff
- 005750ac ["INT_ADD", "register:40f0:8", ["const:5750ac:8", "const:4:8"]]
- 005750ac ["CALL", null, ["callee:00c53da0:8"]]
+ 005750ec ["INT_ADD", "register:40f0:8", ["const:5750ec:8", "const:4:8"]]
+ 005750ec ["CALL", null, ["callee:00c53da0:8"]]
- 005750ac bytes 157b1b94
+ 005750ec bytes 2d7b1b94
- 005750c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005750c0 ["INT_ADD", "register:40f0:8", ["const:5750c0:8", "const:4:8"]]
- 005750c0 ["CALLIND", null, ["register:0:8"]]
+ 00575100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575100 ["INT_ADD", "register:40f0:8", ["const:575100:8", "const:4:8"]]
+ 00575100 ["CALLIND", null, ["register:0:8"]]
- 005750c0 bytes 00013fd6
+ 00575100 bytes 00013fd6
- 005750c8 ["INT_ADD", "register:40f0:8", ["const:5750c8:8", "const:4:8"]]
- 005750c8 ["CALL", null, ["callee:00c57f50:8"]]
+ 00575108 ["INT_ADD", "register:40f0:8", ["const:575108:8", "const:4:8"]]
+ 00575108 ["CALL", null, ["callee:00c57f50:8"]]
- 005750c8 bytes 6e8b1b94
+ 00575108 bytes 928b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58639c767ae03a88a2cfe1655e28c2f5"></a>

### [`00575100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575100.md) → [`00575140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575140.md) FUN_00575140

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575100.md#insn-00575110)
- 新版 `00575150`（命令位置の公開資料なし）

~~~diff
- 00575110 ["INT_ADD", "register:40f0:8", ["const:575110:8", "const:4:8"]]
- 00575110 ["CALL", null, ["callee:00c57f70:8"]]
+ 00575150 ["INT_ADD", "register:40f0:8", ["const:575150:8", "const:4:8"]]
+ 00575150 ["CALL", null, ["callee:00c57f70:8"]]
- 00575110 bytes 648b1b94
+ 00575150 bytes 888b1b94
~~~


<a id="compare-4115ad33307b7e9257a712063588016e"></a>

### [`00575124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md) → [`00575164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md) FUN_00575164

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575174) · [`00575188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575188) · [`00575190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575190)
- 新版 `005751b4`（命令位置の公開資料なし） · `005751c8`（命令位置の公開資料なし） · `005751d0`（命令位置の公開資料なし）

~~~diff
- 00575174 ["INT_ADD", "register:40f0:8", ["const:575174:8", "const:4:8"]]
- 00575174 ["CALL", null, ["callee:00c53da0:8"]]
+ 005751b4 ["INT_ADD", "register:40f0:8", ["const:5751b4:8", "const:4:8"]]
+ 005751b4 ["CALL", null, ["callee:00c53da0:8"]]
- 00575174 bytes e37a1b94
+ 005751b4 bytes fb7a1b94
- 00575188 ["COPY", "register:0:8", ["register:4040:8"]]
- 00575188 ["INT_ADD", "register:40f0:8", ["const:575188:8", "const:4:8"]]
- 00575188 ["CALLIND", null, ["register:0:8"]]
+ 005751c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005751c8 ["INT_ADD", "register:40f0:8", ["const:5751c8:8", "const:4:8"]]
+ 005751c8 ["CALLIND", null, ["register:0:8"]]
- 00575188 bytes 00013fd6
+ 005751c8 bytes 00013fd6
- 00575190 ["INT_ADD", "register:40f0:8", ["const:575190:8", "const:4:8"]]
- 00575190 ["CALL", null, ["callee:00c57f50:8"]]
+ 005751d0 ["INT_ADD", "register:40f0:8", ["const:5751d0:8", "const:4:8"]]
+ 005751d0 ["CALL", null, ["callee:00c57f50:8"]]
- 00575190 bytes 3c8b1b94
+ 005751d0 bytes 608b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ace7c8c9463f07c73182decbca6e370"></a>

### [`005751e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md) → [`00575228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md) FUN_00575228

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00575344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00575384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-00575254) · [`00575280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-00575280) · [`005752e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-005752e0)
- 新版 `00575294`（命令位置の公開資料なし） · `005752c0`（命令位置の公開資料なし） · `00575320`（命令位置の公開資料なし）

~~~diff
- 00575254 ["INT_ADD", "register:40f0:8", ["const:575254:8", "const:4:8"]]
- 00575254 ["CALL", null, ["callee:00c57f60:8"]]
+ 00575294 ["INT_ADD", "register:40f0:8", ["const:575294:8", "const:4:8"]]
+ 00575294 ["CALL", null, ["callee:00c57f60:8"]]
- 00575254 bytes 0f8b1b94
+ 00575294 bytes 338b1b94
- 00575280 ["INT_ADD", "register:40f0:8", ["const:575280:8", "const:4:8"]]
- 00575280 ["CALL", null, ["callee:00c53d70:8"]]
+ 005752c0 ["INT_ADD", "register:40f0:8", ["const:5752c0:8", "const:4:8"]]
+ 005752c0 ["CALL", null, ["callee:00c53d70:8"]]
- 00575280 bytes 947a1b94
+ 005752c0 bytes ac7a1b94
- 005752e0 ["INT_ADD", "register:40f0:8", ["const:5752e0:8", "const:4:8"]]
- 005752e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00575320 ["INT_ADD", "register:40f0:8", ["const:575320:8", "const:4:8"]]
+ 00575320 ["CALL", null, ["callee:00c53da0:8"]]
- 005752e0 bytes 887a1b94
+ 00575320 bytes a07a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab77be4a39c573d8a61315453e3eee9"></a>

### [`00575d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md) → [`00575dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md) FUN_00575dcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575dc0) · [`00575e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575e08) · [`00575e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575e28)
- 新版 `00575e00`（命令位置の公開資料なし） · `00575e48`（命令位置の公開資料なし） · `00575e68`（命令位置の公開資料なし）

~~~diff
- 00575dc0 ["INT_ADD", "register:40f0:8", ["const:575dc0:8", "const:4:8"]]
- 00575dc0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00575e00 ["INT_ADD", "register:40f0:8", ["const:575e00:8", "const:4:8"]]
+ 00575e00 ["CALL", null, ["callee:00c580b0:8"]]
- 00575dc0 bytes 88881b94
+ 00575e00 bytes ac881b94
- 00575e08 ["INT_ADD", "register:40f0:8", ["const:575e08:8", "const:4:8"]]
- 00575e08 ["CALL", null, ["callee:00c57f60:8"]]
+ 00575e48 ["INT_ADD", "register:40f0:8", ["const:575e48:8", "const:4:8"]]
+ 00575e48 ["CALL", null, ["callee:00c57f60:8"]]
- 00575e08 bytes 22881b94
+ 00575e48 bytes 46881b94
- 00575e28 ["INT_ADD", "register:40f0:8", ["const:575e28:8", "const:4:8"]]
- 00575e28 ["CALL", null, ["callee:00c58010:8"]]
+ 00575e68 ["INT_ADD", "register:40f0:8", ["const:575e68:8", "const:4:8"]]
+ 00575e68 ["CALL", null, ["callee:00c58010:8"]]
- 00575e28 bytes 46881b94
+ 00575e68 bytes 6a881b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16345aa7fc6c42420fd6b3df9be4f6a6"></a>

### [`00575f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md) → [`00575fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md) FUN_00575fd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00575fcc) · [`00576014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00576014) · [`00576034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00576034)
- 新版 `0057600c`（命令位置の公開資料なし） · `00576054`（命令位置の公開資料なし） · `00576074`（命令位置の公開資料なし）

~~~diff
- 00575fcc ["INT_ADD", "register:40f0:8", ["const:575fcc:8", "const:4:8"]]
- 00575fcc ["CALL", null, ["callee:00c580b0:8"]]
+ 0057600c ["INT_ADD", "register:40f0:8", ["const:57600c:8", "const:4:8"]]
+ 0057600c ["CALL", null, ["callee:00c580b0:8"]]
- 00575fcc bytes 05881b94
+ 0057600c bytes 29881b94
- 00576014 ["INT_ADD", "register:40f0:8", ["const:576014:8", "const:4:8"]]
- 00576014 ["CALL", null, ["callee:00c57f60:8"]]
+ 00576054 ["INT_ADD", "register:40f0:8", ["const:576054:8", "const:4:8"]]
+ 00576054 ["CALL", null, ["callee:00c57f60:8"]]
- 00576014 bytes 9f871b94
+ 00576054 bytes c3871b94
- 00576034 ["INT_ADD", "register:40f0:8", ["const:576034:8", "const:4:8"]]
- 00576034 ["CALL", null, ["callee:00c58010:8"]]
+ 00576074 ["INT_ADD", "register:40f0:8", ["const:576074:8", "const:4:8"]]
+ 00576074 ["CALL", null, ["callee:00c58010:8"]]
- 00576034 bytes c3871b94
+ 00576074 bytes e7871b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f813477e8f4d8e57479d4c4d70f1cb7c"></a>

### [`00576150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md) → [`00576190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md) FUN_00576190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005757d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00575810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005761bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761bc) · [`005761cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761cc) · [`005761ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761ec)
- 新版 `005761fc`（命令位置の公開資料なし） · `0057620c`（命令位置の公開資料なし） · `0057622c`（命令位置の公開資料なし）

~~~diff
- 005761bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005761bc ["INT_ADD", "register:40f0:8", ["const:5761bc:8", "const:4:8"]]
- 005761bc ["CALLIND", null, ["register:0:8"]]
+ 005761fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005761fc ["INT_ADD", "register:40f0:8", ["const:5761fc:8", "const:4:8"]]
+ 005761fc ["CALLIND", null, ["register:0:8"]]
- 005761bc bytes 00013fd6
+ 005761fc bytes 00013fd6
- 005761cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005761cc ["INT_ADD", "register:40f0:8", ["const:5761cc:8", "const:4:8"]]
- 005761cc ["CALLIND", null, ["register:0:8"]]
+ 0057620c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057620c ["INT_ADD", "register:40f0:8", ["const:57620c:8", "const:4:8"]]
+ 0057620c ["CALLIND", null, ["register:0:8"]]
- 005761cc bytes 00013fd6
+ 0057620c bytes 00013fd6
- 005761ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005761ec ["INT_ADD", "register:40f0:8", ["const:5761ec:8", "const:4:8"]]
- 005761ec ["CALLIND", null, ["register:0:8"]]
+ 0057622c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057622c ["INT_ADD", "register:40f0:8", ["const:57622c:8", "const:4:8"]]
+ 0057622c ["CALLIND", null, ["register:0:8"]]
- 005761ec bytes 00013fd6
+ 0057622c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e87a482a162b3dbfdebd1fe3b390d2f"></a>

### [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) → [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) FUN_005762f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) [`0057a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 26件 [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) [`0057a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md#insn-0057632c) · [`00576350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md#insn-00576350)
- 新版 `0057636c`（命令位置の公開資料なし） · `00576390`（命令位置の公開資料なし）

~~~diff
- 0057632c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057632c ["INT_ADD", "register:40f0:8", ["const:57632c:8", "const:4:8"]]
- 0057632c ["CALLIND", null, ["register:0:8"]]
+ 0057636c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057636c ["INT_ADD", "register:40f0:8", ["const:57636c:8", "const:4:8"]]
+ 0057636c ["CALLIND", null, ["register:0:8"]]
- 0057632c bytes 00013fd6
+ 0057636c bytes 00013fd6
- 00576350 ["INT_ADD", "register:40f0:8", ["const:576350:8", "const:4:8"]]
- 00576350 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00576390 ["INT_ADD", "register:40f0:8", ["const:576390:8", "const:4:8"]]
+ 00576390 ["CALL", null, ["callee:00c57fb0:8"]]
- 00576350 bytes e4861b94
+ 00576390 bytes 08871b94
~~~


<a id="compare-07a06852494078e37a9154da8a7ef65d"></a>

### [`00576828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md) → [`00576868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576868.md) FUN_00576868

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00576700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00576740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00576838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md#insn-00576838)
- 新版 `00576878`（命令位置の公開資料なし）

~~~diff
- 00576838 ["INT_ADD", "register:40f0:8", ["const:576838:8", "const:4:8"]]
- 00576838 ["CALL", null, ["callee:00576740:8"]]
+ 00576878 ["INT_ADD", "register:40f0:8", ["const:576878:8", "const:4:8"]]
+ 00576878 ["CALL", null, ["callee:00576740:8"]]
- 00576838 bytes b2ffff97
+ 00576878 bytes b2ffff97
~~~


<a id="compare-ede3ff3c25d5c91012e2b79ae4a26b5a"></a>

### [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) → [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) FUN_005770c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 2件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 2件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005770bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770bc) · [`005770e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770e8) · [`005770f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770f8)
- 新版 `005770fc`（命令位置の公開資料なし） · `00577128`（命令位置の公開資料なし） · `00577138`（命令位置の公開資料なし）

~~~diff
- 005770bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005770bc ["INT_ADD", "register:40f0:8", ["const:5770bc:8", "const:4:8"]]
- 005770bc ["CALLIND", null, ["register:0:8"]]
+ 005770fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005770fc ["INT_ADD", "register:40f0:8", ["const:5770fc:8", "const:4:8"]]
+ 005770fc ["CALLIND", null, ["register:0:8"]]
- 005770bc bytes 20013fd6
+ 005770fc bytes 20013fd6
- 005770e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005770e8 ["INT_ADD", "register:40f0:8", ["const:5770e8:8", "const:4:8"]]
- 005770e8 ["CALLIND", null, ["register:0:8"]]
+ 00577128 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577128 ["INT_ADD", "register:40f0:8", ["const:577128:8", "const:4:8"]]
+ 00577128 ["CALLIND", null, ["register:0:8"]]
- 005770e8 bytes 00013fd6
+ 00577128 bytes 00013fd6
- 005770f8 ["INT_ADD", "register:40f0:8", ["const:5770f8:8", "const:4:8"]]
- 005770f8 ["CALL", null, ["callee:0057bee8:8"]]
+ 00577138 ["INT_ADD", "register:40f0:8", ["const:577138:8", "const:4:8"]]
+ 00577138 ["CALL", null, ["callee:0057bee8:8"]]
- 005770f8 bytes 6c130094
+ 00577138 bytes 6c130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e605904140f6fd8c505d54ee64425e"></a>

### [`005772c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md) → [`00577308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577308.md) FUN_00577308

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005772e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md#insn-005772e4) · [`00577304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md#insn-00577304)
- 新版 `00577324`（命令位置の公開資料なし） · `00577344`（命令位置の公開資料なし）

~~~diff
- 005772e4 ["INT_ADD", "register:40f0:8", ["const:5772e4:8", "const:4:8"]]
- 005772e4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00577324 ["INT_ADD", "register:40f0:8", ["const:577324:8", "const:4:8"]]
+ 00577324 ["CALL", null, ["callee:00c53da0:8"]]
- 005772e4 bytes 87721b94
+ 00577324 bytes 9f721b94
- 00577304 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577304 ["INT_ADD", "register:40f0:8", ["const:577304:8", "const:4:8"]]
- 00577304 ["CALLIND", null, ["register:0:8"]]
+ 00577344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577344 ["INT_ADD", "register:40f0:8", ["const:577344:8", "const:4:8"]]
+ 00577344 ["CALLIND", null, ["register:0:8"]]
- 00577304 bytes 00013fd6
+ 00577344 bytes 00013fd6
~~~


<a id="compare-705f0492a6055d329db8e1b6175ed009"></a>

### [`00577890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md) → [`005778d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005778d0.md) FUN_005778d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005778ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md#insn-005778ac) · [`005778cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md#insn-005778cc)
- 新版 `005778ec`（命令位置の公開資料なし） · `0057790c`（命令位置の公開資料なし）

~~~diff
- 005778ac ["INT_ADD", "register:40f0:8", ["const:5778ac:8", "const:4:8"]]
- 005778ac ["CALL", null, ["callee:00c53da0:8"]]
+ 005778ec ["INT_ADD", "register:40f0:8", ["const:5778ec:8", "const:4:8"]]
+ 005778ec ["CALL", null, ["callee:00c53da0:8"]]
- 005778ac bytes 15711b94
+ 005778ec bytes 2d711b94
- 005778cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005778cc ["INT_ADD", "register:40f0:8", ["const:5778cc:8", "const:4:8"]]
- 005778cc ["CALLIND", null, ["register:0:8"]]
+ 0057790c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057790c ["INT_ADD", "register:40f0:8", ["const:57790c:8", "const:4:8"]]
+ 0057790c ["CALLIND", null, ["register:0:8"]]
- 005778cc bytes 00013fd6
+ 0057790c bytes 00013fd6
~~~


<a id="compare-de184093459843bc85dbaba71dfc1010"></a>

### [`005781c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md) → [`00578204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578204.md) FUN_00578204

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005781d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md#insn-005781d4)
- 新版 `00578214`（命令位置の公開資料なし）

~~~diff
- 005781d4 ["INT_ADD", "register:40f0:8", ["const:5781d4:8", "const:4:8"]]
- 005781d4 ["CALL", null, ["callee:00578060:8"]]
+ 00578214 ["INT_ADD", "register:40f0:8", ["const:578214:8", "const:4:8"]]
+ 00578214 ["CALL", null, ["callee:00578060:8"]]
- 005781d4 bytes 93ffff97
+ 00578214 bytes 93ffff97
~~~


<a id="compare-0f0eafa3f31c07d1403c025a821eaed0"></a>

### [`0057a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md) → [`0057a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a2e4.md) FUN_0057a2e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md#insn-0057a2f8)
- 新版 `0057a338`（命令位置の公開資料なし）

~~~diff
- 0057a2f8 ["INT_ADD", "register:40f0:8", ["const:57a2f8:8", "const:4:8"]]
- 0057a2f8 ["CALL", null, ["callee:0057c35c:8"]]
+ 0057a338 ["INT_ADD", "register:40f0:8", ["const:57a338:8", "const:4:8"]]
+ 0057a338 ["CALL", null, ["callee:0057c35c:8"]]
- 0057a2f8 bytes 09080094
+ 0057a338 bytes 09080094
~~~


<a id="compare-2716325925250c58d7ce6f0aa319b512"></a>

### [`0057a2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md) → [`0057a33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a33c.md) FUN_0057a33c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md#insn-0057a340)
- 新版 `0057a380`（命令位置の公開資料なし）

~~~diff
- 0057a340 ["INT_ADD", "register:40f0:8", ["const:57a340:8", "const:4:8"]]
- 0057a340 ["CALL", null, ["callee:0057c35c:8"]]
+ 0057a380 ["INT_ADD", "register:40f0:8", ["const:57a380:8", "const:4:8"]]
+ 0057a380 ["CALL", null, ["callee:0057c35c:8"]]
- 0057a340 bytes f7070094
+ 0057a380 bytes f7070094
~~~


<a id="compare-f401d8a24a6260d8492417aa6d5ff451"></a>

### [`0057a344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md) → [`0057a384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a384.md) FUN_0057a384

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md#insn-0057a388)
- 新版 `0057a3c8`（命令位置の公開資料なし）

~~~diff
- 0057a388 ["INT_ADD", "register:40f0:8", ["const:57a388:8", "const:4:8"]]
- 0057a388 ["CALL", null, ["callee:0057c35c:8"]]
+ 0057a3c8 ["INT_ADD", "register:40f0:8", ["const:57a3c8:8", "const:4:8"]]
+ 0057a3c8 ["CALL", null, ["callee:0057c35c:8"]]
- 0057a388 bytes e5070094
+ 0057a3c8 bytes e5070094
~~~


<a id="compare-73b1a4ef2fbd6ae9b6fe25c04f505ba6"></a>

### [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) → [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) FUN_0057bccc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005765ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765ac.md) [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) · 呼出先 2件 [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005765ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765ec.md) [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) · 呼出先 2件 [`0057bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bccc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bca8) · [`0057bcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bcb4) · [`0057bcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bcec)
- 新版 `0057bce8`（命令位置の公開資料なし） · `0057bcf4`（命令位置の公開資料なし） · `0057bd2c`（命令位置の公開資料なし）

~~~diff
- 0057bca8 ["INT_ADD", "register:40f0:8", ["const:57bca8:8", "const:4:8"]]
- 0057bca8 ["CALL", null, ["local:b0:8"]]
+ 0057bce8 ["INT_ADD", "register:40f0:8", ["const:57bce8:8", "const:4:8"]]
+ 0057bce8 ["CALL", null, ["local:b0:8"]]
- 0057bca8 bytes f9ffff97
+ 0057bce8 bytes f9ffff97
- 0057bcb4 ["INT_ADD", "register:40f0:8", ["const:57bcb4:8", "const:4:8"]]
- 0057bcb4 ["CALL", null, ["local:b0:8"]]
+ 0057bcf4 ["INT_ADD", "register:40f0:8", ["const:57bcf4:8", "const:4:8"]]
+ 0057bcf4 ["CALL", null, ["local:b0:8"]]
- 0057bcb4 bytes f6ffff97
+ 0057bcf4 bytes f6ffff97
- 0057bcec ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bcec ["INT_ADD", "register:40f0:8", ["const:57bcec:8", "const:4:8"]]
- 0057bcec ["CALLIND", null, ["register:0:8"]]
+ 0057bd2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bd2c ["INT_ADD", "register:40f0:8", ["const:57bd2c:8", "const:4:8"]]
+ 0057bd2c ["CALLIND", null, ["register:0:8"]]
- 0057bcec bytes 00013fd6
+ 0057bd2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69fbe31182ab69fc20552efeb15e884"></a>

### [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) → [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) FUN_0057bd6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005765b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765b4.md) [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) · 呼出先 2件 [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005765f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765f4.md) [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) · 呼出先 2件 [`0057bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bd6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd48) · [`0057bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd54) · [`0057bd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd88)
- 新版 `0057bd88`（命令位置の公開資料なし） · `0057bd94`（命令位置の公開資料なし） · `0057bdc8`（命令位置の公開資料なし）

~~~diff
- 0057bd48 ["INT_ADD", "register:40f0:8", ["const:57bd48:8", "const:4:8"]]
- 0057bd48 ["CALL", null, ["local:b0:8"]]
+ 0057bd88 ["INT_ADD", "register:40f0:8", ["const:57bd88:8", "const:4:8"]]
+ 0057bd88 ["CALL", null, ["local:b0:8"]]
- 0057bd48 bytes f9ffff97
+ 0057bd88 bytes f9ffff97
- 0057bd54 ["INT_ADD", "register:40f0:8", ["const:57bd54:8", "const:4:8"]]
- 0057bd54 ["CALL", null, ["local:b0:8"]]
+ 0057bd94 ["INT_ADD", "register:40f0:8", ["const:57bd94:8", "const:4:8"]]
+ 0057bd94 ["CALL", null, ["local:b0:8"]]
- 0057bd54 bytes f6ffff97
+ 0057bd94 bytes f6ffff97
- 0057bd88 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bd88 ["INT_ADD", "register:40f0:8", ["const:57bd88:8", "const:4:8"]]
- 0057bd88 ["CALLIND", null, ["register:0:8"]]
+ 0057bdc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bdc8 ["INT_ADD", "register:40f0:8", ["const:57bdc8:8", "const:4:8"]]
+ 0057bdc8 ["CALLIND", null, ["register:0:8"]]
- 0057bd88 bytes 00013fd6
+ 0057bdc8 bytes 00013fd6
~~~


<a id="compare-88c62ec31323600c5505be4885e71e1a"></a>

### [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) → [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) FUN_0057bddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005766f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766f8.md) [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) · 呼出先 4件 [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00576738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576738.md) [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) · 呼出先 4件 [`0057bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bddc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdb8) · [`0057bdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdc4) · [`0057bdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdd8)
- 新版 `0057bdf8`（命令位置の公開資料なし） · `0057be04`（命令位置の公開資料なし） · `0057be18`（命令位置の公開資料なし）

~~~diff
- 0057bdb8 ["INT_ADD", "register:40f0:8", ["const:57bdb8:8", "const:4:8"]]
- 0057bdb8 ["CALL", null, ["local:b0:8"]]
+ 0057bdf8 ["INT_ADD", "register:40f0:8", ["const:57bdf8:8", "const:4:8"]]
+ 0057bdf8 ["CALL", null, ["local:b0:8"]]
- 0057bdb8 bytes f9ffff97
+ 0057bdf8 bytes f9ffff97
- 0057bdc4 ["INT_ADD", "register:40f0:8", ["const:57bdc4:8", "const:4:8"]]
- 0057bdc4 ["CALL", null, ["local:b0:8"]]
+ 0057be04 ["INT_ADD", "register:40f0:8", ["const:57be04:8", "const:4:8"]]
+ 0057be04 ["CALL", null, ["local:b0:8"]]
- 0057bdc4 bytes f6ffff97
+ 0057be04 bytes f6ffff97
- 0057bdd8 ["INT_ADD", "register:40f0:8", ["const:57bdd8:8", "const:4:8"]]
- 0057bdd8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057be18 ["INT_ADD", "register:40f0:8", ["const:57be18:8", "const:4:8"]]
+ 0057be18 ["CALL", null, ["callee:00c53da0:8"]]
- 0057bdd8 bytes ca5f1b94
+ 0057be18 bytes e25f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68fe77567c073659b40c4abf764040df"></a>

### [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) → [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) FUN_0057be4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`0057ecf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ecf0.md) [`0057ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md) [`0057efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md) [`0057f15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 11件 [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`0057ed30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ed30.md) [`0057eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md) [`0057f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md) [`0057f19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057be80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md#insn-0057be80) · [`0057bea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md#insn-0057bea4)
- 新版 `0057bec0`（命令位置の公開資料なし） · `0057bee4`（命令位置の公開資料なし）

~~~diff
- 0057be80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057be80 ["INT_ADD", "register:40f0:8", ["const:57be80:8", "const:4:8"]]
- 0057be80 ["CALLIND", null, ["register:0:8"]]
+ 0057bec0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bec0 ["INT_ADD", "register:40f0:8", ["const:57bec0:8", "const:4:8"]]
+ 0057bec0 ["CALLIND", null, ["register:0:8"]]
- 0057be80 bytes 00013fd6
+ 0057bec0 bytes 00013fd6
- 0057bea4 ["INT_ADD", "register:40f0:8", ["const:57bea4:8", "const:4:8"]]
- 0057bea4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057bee4 ["INT_ADD", "register:40f0:8", ["const:57bee4:8", "const:4:8"]]
+ 0057bee4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0057bea4 bytes 0f701b94
+ 0057bee4 bytes 33701b94
~~~


<a id="compare-4f09e9e91c23b45a299554d0e0bf589b"></a>

### [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) → [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) FUN_0057bee8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) [`0057a9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md) [`0058c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md) [`006c3c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3c84.md) [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 16件 [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) [`0057a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md) [`0058c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md) [`006c3cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md) [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf14) · [`0057bf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf24) · [`0057bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf44)
- 新版 `0057bf54`（命令位置の公開資料なし） · `0057bf64`（命令位置の公開資料なし） · `0057bf84`（命令位置の公開資料なし）

~~~diff
- 0057bf14 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf14 ["INT_ADD", "register:40f0:8", ["const:57bf14:8", "const:4:8"]]
- 0057bf14 ["CALLIND", null, ["register:0:8"]]
+ 0057bf54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf54 ["INT_ADD", "register:40f0:8", ["const:57bf54:8", "const:4:8"]]
+ 0057bf54 ["CALLIND", null, ["register:0:8"]]
- 0057bf14 bytes 00013fd6
+ 0057bf54 bytes 00013fd6
- 0057bf24 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf24 ["INT_ADD", "register:40f0:8", ["const:57bf24:8", "const:4:8"]]
- 0057bf24 ["CALLIND", null, ["register:0:8"]]
+ 0057bf64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf64 ["INT_ADD", "register:40f0:8", ["const:57bf64:8", "const:4:8"]]
+ 0057bf64 ["CALLIND", null, ["register:0:8"]]
- 0057bf24 bytes 00013fd6
+ 0057bf64 bytes 00013fd6
- 0057bf44 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf44 ["INT_ADD", "register:40f0:8", ["const:57bf44:8", "const:4:8"]]
- 0057bf44 ["CALLIND", null, ["register:0:8"]]
+ 0057bf84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf84 ["INT_ADD", "register:40f0:8", ["const:57bf84:8", "const:4:8"]]
+ 0057bf84 ["CALLIND", null, ["register:0:8"]]
- 0057bf44 bytes 00013fd6
+ 0057bf84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8284514ce2147c0d15c1d8106cd431ba"></a>

### [`0057c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md) → [`0057c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md) FUN_0057c0f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c11c) · [`0057c148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c148) · [`0057c1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c1a8)
- 新版 `0057c15c`（命令位置の公開資料なし） · `0057c188`（命令位置の公開資料なし） · `0057c1e8`（命令位置の公開資料なし）

~~~diff
- 0057c11c ["INT_ADD", "register:40f0:8", ["const:57c11c:8", "const:4:8"]]
- 0057c11c ["CALL", null, ["callee:00c57f60:8"]]
+ 0057c15c ["INT_ADD", "register:40f0:8", ["const:57c15c:8", "const:4:8"]]
+ 0057c15c ["CALL", null, ["callee:00c57f60:8"]]
- 0057c11c bytes 5d6f1b94
+ 0057c15c bytes 816f1b94
- 0057c148 ["INT_ADD", "register:40f0:8", ["const:57c148:8", "const:4:8"]]
- 0057c148 ["CALL", null, ["callee:00c53d70:8"]]
+ 0057c188 ["INT_ADD", "register:40f0:8", ["const:57c188:8", "const:4:8"]]
+ 0057c188 ["CALL", null, ["callee:00c53d70:8"]]
- 0057c148 bytes e25e1b94
+ 0057c188 bytes fa5e1b94
- 0057c1a8 ["INT_ADD", "register:40f0:8", ["const:57c1a8:8", "const:4:8"]]
- 0057c1a8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057c1e8 ["INT_ADD", "register:40f0:8", ["const:57c1e8:8", "const:4:8"]]
+ 0057c1e8 ["CALL", null, ["callee:00c53da0:8"]]
- 0057c1a8 bytes d65e1b94
+ 0057c1e8 bytes ee5e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a762957f2fbd88ddfd56a71571854509"></a>

### [`0057c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md) → [`0057c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md) FUN_0057c260

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) · 呼出先 4件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2d0) · [`0057c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2e4) · [`0057c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2f8)
- 新版 `0057c310`（命令位置の公開資料なし） · `0057c324`（命令位置の公開資料なし） · `0057c338`（命令位置の公開資料なし）

~~~diff
- 0057c2d0 ["INT_ADD", "register:40f0:8", ["const:57c2d0:8", "const:4:8"]]
- 0057c2d0 ["CALL", null, ["callee:00494650:8"]]
+ 0057c310 ["INT_ADD", "register:40f0:8", ["const:57c310:8", "const:4:8"]]
+ 0057c310 ["CALL", null, ["callee:00494650:8"]]
- 0057c2d0 bytes d060fc97
+ 0057c310 bytes d060fc97
- 0057c2e4 ["INT_ADD", "register:40f0:8", ["const:57c2e4:8", "const:4:8"]]
- 0057c2e4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057c324 ["INT_ADD", "register:40f0:8", ["const:57c324:8", "const:4:8"]]
+ 0057c324 ["CALL", null, ["callee:00c53da0:8"]]
- 0057c2e4 bytes 875e1b94
+ 0057c324 bytes 9f5e1b94
- 0057c2f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c2f8 ["INT_ADD", "register:40f0:8", ["const:57c2f8:8", "const:4:8"]]
- 0057c2f8 ["CALLIND", null, ["register:0:8"]]
+ 0057c338 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c338 ["INT_ADD", "register:40f0:8", ["const:57c338:8", "const:4:8"]]
+ 0057c338 ["CALLIND", null, ["register:0:8"]]
- 0057c2f8 bytes 00013fd6
+ 0057c338 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5468534ef400d6503f2e9b0f2a7071bf"></a>

### [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) → [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) FUN_0057c370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0057a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c39c) · [`0057c3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c3c8) · [`0057c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c428)
- 新版 `0057c3dc`（命令位置の公開資料なし） · `0057c408`（命令位置の公開資料なし） · `0057c468`（命令位置の公開資料なし）

~~~diff
- 0057c39c ["INT_ADD", "register:40f0:8", ["const:57c39c:8", "const:4:8"]]
- 0057c39c ["CALL", null, ["callee:00c57f60:8"]]
+ 0057c3dc ["INT_ADD", "register:40f0:8", ["const:57c3dc:8", "const:4:8"]]
+ 0057c3dc ["CALL", null, ["callee:00c57f60:8"]]
- 0057c39c bytes bd6e1b94
+ 0057c3dc bytes e16e1b94
- 0057c3c8 ["INT_ADD", "register:40f0:8", ["const:57c3c8:8", "const:4:8"]]
- 0057c3c8 ["CALL", null, ["callee:00c53d70:8"]]
+ 0057c408 ["INT_ADD", "register:40f0:8", ["const:57c408:8", "const:4:8"]]
+ 0057c408 ["CALL", null, ["callee:00c53d70:8"]]
- 0057c3c8 bytes 425e1b94
+ 0057c408 bytes 5a5e1b94
- 0057c428 ["INT_ADD", "register:40f0:8", ["const:57c428:8", "const:4:8"]]
- 0057c428 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057c468 ["INT_ADD", "register:40f0:8", ["const:57c468:8", "const:4:8"]]
+ 0057c468 ["CALL", null, ["callee:00c53da0:8"]]
- 0057c428 bytes 365e1b94
+ 0057c468 bytes 4e5e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69581782842462efcd8c8b5dfa968c2e"></a>

### [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) → [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) FUN_0057c56c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0057a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a950.md) [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) · 呼出先 2件 [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0057a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a990.md) [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) · 呼出先 2件 [`0057c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c56c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c548) · [`0057c554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c554) · [`0057c588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c588)
- 新版 `0057c588`（命令位置の公開資料なし） · `0057c594`（命令位置の公開資料なし） · `0057c5c8`（命令位置の公開資料なし）

~~~diff
- 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
- 0057c548 ["CALL", null, ["local:b0:8"]]
+ 0057c588 ["INT_ADD", "register:40f0:8", ["const:57c588:8", "const:4:8"]]
+ 0057c588 ["CALL", null, ["local:b0:8"]]
- 0057c548 bytes f9ffff97
+ 0057c588 bytes f9ffff97
- 0057c554 ["INT_ADD", "register:40f0:8", ["const:57c554:8", "const:4:8"]]
- 0057c554 ["CALL", null, ["local:b0:8"]]
+ 0057c594 ["INT_ADD", "register:40f0:8", ["const:57c594:8", "const:4:8"]]
+ 0057c594 ["CALL", null, ["local:b0:8"]]
- 0057c554 bytes f6ffff97
+ 0057c594 bytes f6ffff97
- 0057c588 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c588 ["INT_ADD", "register:40f0:8", ["const:57c588:8", "const:4:8"]]
- 0057c588 ["CALLIND", null, ["register:0:8"]]
+ 0057c5c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c5c8 ["INT_ADD", "register:40f0:8", ["const:57c5c8:8", "const:4:8"]]
+ 0057c5c8 ["CALLIND", null, ["register:0:8"]]
- 0057c588 bytes 00013fd6
+ 0057c5c8 bytes 00013fd6
~~~


<a id="compare-15733dd355b0a0186a32dcc74114e367"></a>

### [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) → [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) FUN_0057c5dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a958.md) [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`0058c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md) · 呼出先 2件 [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0057a998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a998.md) [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`0058c468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md) · 呼出先 2件 [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5b8) · [`0057c5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5c4) · [`0057c5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5f8)
- 新版 `0057c5f8`（命令位置の公開資料なし） · `0057c604`（命令位置の公開資料なし） · `0057c638`（命令位置の公開資料なし）

~~~diff
- 0057c5b8 ["INT_ADD", "register:40f0:8", ["const:57c5b8:8", "const:4:8"]]
- 0057c5b8 ["CALL", null, ["local:b0:8"]]
+ 0057c5f8 ["INT_ADD", "register:40f0:8", ["const:57c5f8:8", "const:4:8"]]
+ 0057c5f8 ["CALL", null, ["local:b0:8"]]
- 0057c5b8 bytes f9ffff97
+ 0057c5f8 bytes f9ffff97
- 0057c5c4 ["INT_ADD", "register:40f0:8", ["const:57c5c4:8", "const:4:8"]]
- 0057c5c4 ["CALL", null, ["local:b0:8"]]
+ 0057c604 ["INT_ADD", "register:40f0:8", ["const:57c604:8", "const:4:8"]]
+ 0057c604 ["CALL", null, ["local:b0:8"]]
- 0057c5c4 bytes f6ffff97
+ 0057c604 bytes f6ffff97
- 0057c5f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c5f8 ["INT_ADD", "register:40f0:8", ["const:57c5f8:8", "const:4:8"]]
- 0057c5f8 ["CALLIND", null, ["register:0:8"]]
+ 0057c638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c638 ["INT_ADD", "register:40f0:8", ["const:57c638:8", "const:4:8"]]
+ 0057c638 ["CALLIND", null, ["register:0:8"]]
- 0057c5f8 bytes 00013fd6
+ 0057c638 bytes 00013fd6
~~~


<a id="compare-31002ae686310c27c18490fe141a3baf"></a>

### [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) → [`0057c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md) FUN_0057c694

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`00935e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md) [`00ac8b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8b48.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) [`00935e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935e90.md) [`00ac8bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8bb8.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6c0) · [`0057c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6d0) · [`0057c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6f0)
- 新版 `0057c700`（命令位置の公開資料なし） · `0057c710`（命令位置の公開資料なし） · `0057c730`（命令位置の公開資料なし）

~~~diff
- 0057c6c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c6c0 ["INT_ADD", "register:40f0:8", ["const:57c6c0:8", "const:4:8"]]
- 0057c6c0 ["CALLIND", null, ["register:0:8"]]
+ 0057c700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c700 ["INT_ADD", "register:40f0:8", ["const:57c700:8", "const:4:8"]]
+ 0057c700 ["CALLIND", null, ["register:0:8"]]
- 0057c6c0 bytes 00013fd6
+ 0057c700 bytes 00013fd6
- 0057c6d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c6d0 ["INT_ADD", "register:40f0:8", ["const:57c6d0:8", "const:4:8"]]
- 0057c6d0 ["CALLIND", null, ["register:0:8"]]
+ 0057c710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c710 ["INT_ADD", "register:40f0:8", ["const:57c710:8", "const:4:8"]]
+ 0057c710 ["CALLIND", null, ["register:0:8"]]
- 0057c6d0 bytes 00013fd6
+ 0057c710 bytes 00013fd6
- 0057c6f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c6f0 ["INT_ADD", "register:40f0:8", ["const:57c6f0:8", "const:4:8"]]
- 0057c6f0 ["CALLIND", null, ["register:0:8"]]
+ 0057c730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c730 ["INT_ADD", "register:40f0:8", ["const:57c730:8", "const:4:8"]]
+ 0057c730 ["CALLIND", null, ["register:0:8"]]
- 0057c6f0 bytes 00013fd6
+ 0057c730 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b2687b8b44ce205acc038e94e04723"></a>

### [`0057ccd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ccd4.md) → [`0057cd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cd14.md) FUN_0057cd14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ccec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ccd4.md#insn-0057ccec)
- 新版 `0057cd2c`（命令位置の公開資料なし）

~~~diff
- 0057ccec ["INT_ADD", "register:40f0:8", ["const:57ccec:8", "const:4:8"]]
- 0057ccec ["CALL", null, ["callee:00c5a210:8"]]
+ 0057cd2c ["INT_ADD", "register:40f0:8", ["const:57cd2c:8", "const:4:8"]]
+ 0057cd2c ["CALL", null, ["callee:00c5a210:8"]]
- 0057ccec bytes 15751b94
+ 0057cd2c bytes 39751b94
~~~


<a id="compare-aa48b8b3025e2885cf8ceedd3966540b"></a>

### [`0057cd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md) → [`0057cda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cda0.md) FUN_0057cda0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md#insn-0057cd80) · [`0057cd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md#insn-0057cd94)
- 新版 `0057cdc0`（命令位置の公開資料なし） · `0057cdd4`（命令位置の公開資料なし）

~~~diff
- 0057cd80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cd80 ["INT_ADD", "register:40f0:8", ["const:57cd80:8", "const:4:8"]]
- 0057cd80 ["CALLIND", null, ["register:0:8"]]
+ 0057cdc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cdc0 ["INT_ADD", "register:40f0:8", ["const:57cdc0:8", "const:4:8"]]
+ 0057cdc0 ["CALLIND", null, ["register:0:8"]]
- 0057cd80 bytes 00013fd6
+ 0057cdc0 bytes 00013fd6
- 0057cd94 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cd94 ["INT_ADD", "register:40f0:8", ["const:57cd94:8", "const:4:8"]]
- 0057cd94 ["CALLIND", null, ["register:0:8"]]
+ 0057cdd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cdd4 ["INT_ADD", "register:40f0:8", ["const:57cdd4:8", "const:4:8"]]
+ 0057cdd4 ["CALLIND", null, ["register:0:8"]]
- 0057cd94 bytes 00013fd6
+ 0057cdd4 bytes 00013fd6
~~~


<a id="compare-c15bb8cda22ce9d831abca524d63499f"></a>

### [`0057ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ce68.md) → [`0057cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cea8.md) FUN_0057cea8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ce68.md#insn-0057ce84)
- 新版 `0057cec4`（命令位置の公開資料なし）

~~~diff
- 0057ce84 ["INT_ADD", "register:40f0:8", ["const:57ce84:8", "const:4:8"]]
- 0057ce84 ["CALL", null, ["callee:00c5a240:8"]]
+ 0057cec4 ["INT_ADD", "register:40f0:8", ["const:57cec4:8", "const:4:8"]]
+ 0057cec4 ["CALL", null, ["callee:00c5a240:8"]]
- 0057ce84 bytes bb741b94
+ 0057cec4 bytes df741b94
~~~


<a id="compare-1854b6ff7d345541aa087faf4283cf3d"></a>

### [`0057d12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md) → [`0057d16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d16c.md) FUN_0057d16c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a150.md) [`00c5a170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a220.md) [`00c5a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md#insn-0057d144) · [`0057d154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md#insn-0057d154)
- 新版 `0057d184`（命令位置の公開資料なし） · `0057d194`（命令位置の公開資料なし）

~~~diff
- 0057d144 ["INT_ADD", "register:40f0:8", ["const:57d144:8", "const:4:8"]]
- 0057d144 ["CALL", null, ["callee:00c5a220:8"]]
+ 0057d184 ["INT_ADD", "register:40f0:8", ["const:57d184:8", "const:4:8"]]
+ 0057d184 ["CALL", null, ["callee:00c5a220:8"]]
- 0057d144 bytes 03741b94
+ 0057d184 bytes 27741b94
- 0057d154 ["INT_ADD", "register:40f0:8", ["const:57d154:8", "const:4:8"]]
- 0057d154 ["CALL", null, ["callee:00c5a240:8"]]
+ 0057d194 ["INT_ADD", "register:40f0:8", ["const:57d194:8", "const:4:8"]]
+ 0057d194 ["CALL", null, ["callee:00c5a240:8"]]
- 0057d154 bytes 07741b94
+ 0057d194 bytes 2b741b94
~~~


<a id="compare-2892f5d3c5ab06b50eb408548ddc21b2"></a>

### [`0057d1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1b8.md) → [`0057d1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d1f8.md) FUN_0057d1f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1b8.md#insn-0057d1d0)
- 新版 `0057d210`（命令位置の公開資料なし）

~~~diff
- 0057d1d0 ["INT_ADD", "register:40f0:8", ["const:57d1d0:8", "const:4:8"]]
- 0057d1d0 ["CALL", null, ["callee:00c5a0d0:8"]]
+ 0057d210 ["INT_ADD", "register:40f0:8", ["const:57d210:8", "const:4:8"]]
+ 0057d210 ["CALL", null, ["callee:00c5a0d0:8"]]
- 0057d1d0 bytes 8c731b94
+ 0057d210 bytes b0731b94
~~~


<a id="compare-bdc90d473a6a85f3948d1f15c60fa1a3"></a>

### [`0057d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md) → [`0057d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d22c.md) FUN_0057d22c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d204) · [`0057d218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d218) · [`0057d21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d21c)
- 新版 `0057d244`（命令位置の公開資料なし） · `0057d258`（命令位置の公開資料なし） · `0057d25c`（命令位置の公開資料なし）

~~~diff
- 0057d204 ["INT_ADD", "register:40f0:8", ["const:57d204:8", "const:4:8"]]
- 0057d204 ["CALL", null, ["callee:00c5a280:8"]]
+ 0057d244 ["INT_ADD", "register:40f0:8", ["const:57d244:8", "const:4:8"]]
+ 0057d244 ["CALL", null, ["callee:00c5a280:8"]]
- 0057d204 bytes eb731b94
+ 0057d244 bytes 0f741b94
- 0057d218 ["INT_ADD", "register:40f0:8", ["const:57d218:8", "const:4:8"]]
- 0057d218 ["CALL", null, ["callee:00c5a290:8"]]
+ 0057d258 ["INT_ADD", "register:40f0:8", ["const:57d258:8", "const:4:8"]]
+ 0057d258 ["CALL", null, ["callee:00c5a290:8"]]
- 0057d218 bytes ea731b94
+ 0057d258 bytes 0e741b94
- 0057d21c ["INT_ADD", "register:40f0:8", ["const:57d21c:8", "const:4:8"]]
- 0057d21c ["CALL", null, ["callee:00c5a2a0:8"]]
+ 0057d25c ["INT_ADD", "register:40f0:8", ["const:57d25c:8", "const:4:8"]]
+ 0057d25c ["CALL", null, ["callee:00c5a2a0:8"]]
- 0057d21c bytes ed731b94
+ 0057d25c bytes 11741b94
~~~


<a id="compare-09afb02485a37af690ab42a2a0efd634"></a>

### [`0057d234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md) → [`0057d274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d274.md) FUN_0057d274

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d258) · [`0057d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d260) · [`0057d294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d294)
- 新版 `0057d298`（命令位置の公開資料なし） · `0057d2a0`（命令位置の公開資料なし） · `0057d2d4`（命令位置の公開資料なし）

~~~diff
- 0057d258 ["INT_ADD", "register:40f0:8", ["const:57d258:8", "const:4:8"]]
- 0057d258 ["CALL", null, ["callee:00c5a290:8"]]
+ 0057d298 ["INT_ADD", "register:40f0:8", ["const:57d298:8", "const:4:8"]]
+ 0057d298 ["CALL", null, ["callee:00c5a290:8"]]
- 0057d258 bytes da731b94
+ 0057d298 bytes fe731b94
- 0057d260 ["INT_ADD", "register:40f0:8", ["const:57d260:8", "const:4:8"]]
- 0057d260 ["CALL", null, ["callee:00c5a2b0:8"]]
+ 0057d2a0 ["INT_ADD", "register:40f0:8", ["const:57d2a0:8", "const:4:8"]]
+ 0057d2a0 ["CALL", null, ["callee:00c5a2b0:8"]]
- 0057d260 bytes e0731b94
+ 0057d2a0 bytes 04741b94
- 0057d294 ["INT_ADD", "register:40f0:8", ["const:57d294:8", "const:4:8"]]
- 0057d294 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057d2d4 ["INT_ADD", "register:40f0:8", ["const:57d2d4:8", "const:4:8"]]
+ 0057d2d4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0057d294 bytes 136b1b94
+ 0057d2d4 bytes 376b1b94
~~~


<a id="compare-c724308838f6e1071d557887fad74eca"></a>

### [`0057d2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md) → [`0057d30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d30c.md) FUN_0057d30c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md) [`00c5a2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d2f0) · [`0057d2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d2f8) · [`0057d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d320)
- 新版 `0057d330`（命令位置の公開資料なし） · `0057d338`（命令位置の公開資料なし） · `0057d360`（命令位置の公開資料なし）

~~~diff
- 0057d2f0 ["INT_ADD", "register:40f0:8", ["const:57d2f0:8", "const:4:8"]]
- 0057d2f0 ["CALL", null, ["callee:00c5a290:8"]]
+ 0057d330 ["INT_ADD", "register:40f0:8", ["const:57d330:8", "const:4:8"]]
+ 0057d330 ["CALL", null, ["callee:00c5a290:8"]]
- 0057d2f0 bytes b4731b94
+ 0057d330 bytes d8731b94
- 0057d2f8 ["INT_ADD", "register:40f0:8", ["const:57d2f8:8", "const:4:8"]]
- 0057d2f8 ["CALL", null, ["callee:00c5a2b0:8"]]
+ 0057d338 ["INT_ADD", "register:40f0:8", ["const:57d338:8", "const:4:8"]]
+ 0057d338 ["CALL", null, ["callee:00c5a2b0:8"]]
- 0057d2f8 bytes ba731b94
+ 0057d338 bytes de731b94
- 0057d320 ["INT_ADD", "register:40f0:8", ["const:57d320:8", "const:4:8"]]
- 0057d320 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057d360 ["INT_ADD", "register:40f0:8", ["const:57d360:8", "const:4:8"]]
+ 0057d360 ["CALL", null, ["callee:00c57fb0:8"]]
- 0057d320 bytes f06a1b94
+ 0057d360 bytes 146b1b94
~~~


<a id="compare-891de99002c9c59dc43e4b8d66c278fe"></a>

### [`0057d41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md) → [`0057d45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d45c.md) FUN_0057d45c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md#insn-0057d444) · [`0057d458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md#insn-0057d458)
- 新版 `0057d484`（命令位置の公開資料なし） · `0057d498`（命令位置の公開資料なし）

~~~diff
- 0057d444 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d444 ["INT_ADD", "register:40f0:8", ["const:57d444:8", "const:4:8"]]
- 0057d444 ["CALLIND", null, ["register:0:8"]]
+ 0057d484 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d484 ["INT_ADD", "register:40f0:8", ["const:57d484:8", "const:4:8"]]
+ 0057d484 ["CALLIND", null, ["register:0:8"]]
- 0057d444 bytes 00013fd6
+ 0057d484 bytes 00013fd6
- 0057d458 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d458 ["INT_ADD", "register:40f0:8", ["const:57d458:8", "const:4:8"]]
- 0057d458 ["CALLIND", null, ["register:0:8"]]
+ 0057d498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d498 ["INT_ADD", "register:40f0:8", ["const:57d498:8", "const:4:8"]]
+ 0057d498 ["CALLIND", null, ["register:0:8"]]
- 0057d458 bytes 00013fd6
+ 0057d498 bytes 00013fd6
~~~


<a id="compare-4fd2b9aae69a36c8e49d4e79e25cc5ae"></a>

### [`0057d6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d6e4.md) → [`0057d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d724.md) FUN_0057d724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d6e4.md#insn-0057d6f4)
- 新版 `0057d734`（命令位置の公開資料なし）

~~~diff
- 0057d6f4 ["INT_ADD", "register:40f0:8", ["const:57d6f4:8", "const:4:8"]]
- 0057d6f4 ["CALL", null, ["callee:00c5a130:8"]]
+ 0057d734 ["INT_ADD", "register:40f0:8", ["const:57d734:8", "const:4:8"]]
+ 0057d734 ["CALL", null, ["callee:00c5a130:8"]]
- 0057d6f4 bytes 5b721b94
+ 0057d734 bytes 7f721b94
~~~


<a id="compare-aa98612a7663eab862daa471e13d11d9"></a>

### [`0057d708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d708.md) → [`0057d748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d748.md) FUN_0057d748

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a200.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d708.md#insn-0057d724)
- 新版 `0057d764`（命令位置の公開資料なし）

~~~diff
- 0057d724 ["INT_ADD", "register:40f0:8", ["const:57d724:8", "const:4:8"]]
- 0057d724 ["CALL", null, ["callee:00c5a2d0:8"]]
+ 0057d764 ["INT_ADD", "register:40f0:8", ["const:57d764:8", "const:4:8"]]
+ 0057d764 ["CALL", null, ["callee:00c5a2d0:8"]]
- 0057d724 bytes b7721b94
+ 0057d764 bytes db721b94
~~~


<a id="compare-a57629c53cdb8a56d531fdb6c6389350"></a>

### [`0057d7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d7c4.md) → [`0057d804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d804.md) FUN_0057d804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d7c4.md#insn-0057d800)
- 新版 `0057d840`（命令位置の公開資料なし）

~~~diff
- 0057d800 ["INT_ADD", "register:40f0:8", ["const:57d800:8", "const:4:8"]]
- 0057d800 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 0057d840 ["INT_ADD", "register:40f0:8", ["const:57d840:8", "const:4:8"]]
+ 0057d840 ["CALL", null, ["callee:00c5a2f0:8"]]
- 0057d800 bytes 88721b94
+ 0057d840 bytes ac721b94
~~~


<a id="compare-8c420ac4c35350dc954be998498b262c"></a>

### [`0057d820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d820.md) → [`0057d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d860.md) FUN_0057d860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d820.md#insn-0057d848)
- 新版 `0057d888`（命令位置の公開資料なし）

~~~diff
- 0057d848 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d848 ["INT_ADD", "register:40f0:8", ["const:57d848:8", "const:4:8"]]
- 0057d848 ["CALLIND", null, ["register:0:8"]]
+ 0057d888 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d888 ["INT_ADD", "register:40f0:8", ["const:57d888:8", "const:4:8"]]
+ 0057d888 ["CALLIND", null, ["register:0:8"]]
- 0057d848 bytes 20013fd6
+ 0057d888 bytes 20013fd6
~~~


<a id="compare-0658bb412f09532cea892ff7af57e1eb"></a>

### [`0057d874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md) → [`0057d8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d8b4.md) FUN_0057d8b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8a4) · [`0057d8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8c8) · [`0057d8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8d8)
- 新版 `0057d8e4`（命令位置の公開資料なし） · `0057d908`（命令位置の公開資料なし） · `0057d918`（命令位置の公開資料なし）

~~~diff
- 0057d8a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d8a4 ["INT_ADD", "register:40f0:8", ["const:57d8a4:8", "const:4:8"]]
- 0057d8a4 ["CALLIND", null, ["register:0:8"]]
+ 0057d8e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d8e4 ["INT_ADD", "register:40f0:8", ["const:57d8e4:8", "const:4:8"]]
+ 0057d8e4 ["CALLIND", null, ["register:0:8"]]
- 0057d8a4 bytes 20013fd6
+ 0057d8e4 bytes 20013fd6
- 0057d8c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d8c8 ["INT_ADD", "register:40f0:8", ["const:57d8c8:8", "const:4:8"]]
- 0057d8c8 ["CALLIND", null, ["register:0:8"]]
+ 0057d908 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d908 ["INT_ADD", "register:40f0:8", ["const:57d908:8", "const:4:8"]]
+ 0057d908 ["CALLIND", null, ["register:0:8"]]
- 0057d8c8 bytes 20013fd6
+ 0057d908 bytes 20013fd6
- 0057d8d8 ["INT_ADD", "register:40f0:8", ["const:57d8d8:8", "const:4:8"]]
- 0057d8d8 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 0057d918 ["INT_ADD", "register:40f0:8", ["const:57d918:8", "const:4:8"]]
+ 0057d918 ["CALL", null, ["callee:00c5a2f0:8"]]
- 0057d8d8 bytes 52721b94
+ 0057d918 bytes 76721b94
~~~


<a id="compare-e5f94677b0fda93b7db0392f61c21899"></a>

### [`0057d904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d904.md) → [`0057d944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d944.md) FUN_0057d944

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d904.md#insn-0057d924)
- 新版 `0057d964`（命令位置の公開資料なし）

~~~diff
- 0057d924 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d924 ["INT_ADD", "register:40f0:8", ["const:57d924:8", "const:4:8"]]
- 0057d924 ["CALLIND", null, ["register:0:8"]]
+ 0057d964 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d964 ["INT_ADD", "register:40f0:8", ["const:57d964:8", "const:4:8"]]
+ 0057d964 ["CALLIND", null, ["register:0:8"]]
- 0057d924 bytes 00013fd6
+ 0057d964 bytes 00013fd6
~~~


<a id="compare-52080484f9e23b13050f1a3daccf4e40"></a>

### [`0057d954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d954.md) → [`0057d994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d994.md) FUN_0057d994

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d954.md#insn-0057d978)
- 新版 `0057d9b8`（命令位置の公開資料なし）

~~~diff
- 0057d978 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d978 ["INT_ADD", "register:40f0:8", ["const:57d978:8", "const:4:8"]]
- 0057d978 ["CALLIND", null, ["register:0:8"]]
+ 0057d9b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d9b8 ["INT_ADD", "register:40f0:8", ["const:57d9b8:8", "const:4:8"]]
+ 0057d9b8 ["CALLIND", null, ["register:0:8"]]
- 0057d978 bytes 00013fd6
+ 0057d9b8 bytes 00013fd6
~~~


<a id="compare-7ad53679f6f4875a7dd986def19dc778"></a>

### [`0057dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md) → [`0057dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dd14.md) FUN_0057dd14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a230.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dcfc) · [`0057dd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dd70) · [`0057dd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dd90)
- 新版 `0057dd3c`（命令位置の公開資料なし） · `0057ddb0`（命令位置の公開資料なし） · `0057ddd0`（命令位置の公開資料なし）

~~~diff
- 0057dcfc ["INT_ADD", "register:40f0:8", ["const:57dcfc:8", "const:4:8"]]
- 0057dcfc ["CALL", null, ["callee:00c5a300:8"]]
+ 0057dd3c ["INT_ADD", "register:40f0:8", ["const:57dd3c:8", "const:4:8"]]
+ 0057dd3c ["CALL", null, ["callee:00c5a300:8"]]
- 0057dcfc bytes 4d711b94
+ 0057dd3c bytes 71711b94
- 0057dd70 ["INT_ADD", "register:40f0:8", ["const:57dd70:8", "const:4:8"]]
- 0057dd70 ["CALL", null, ["callee:00c57f60:8"]]
+ 0057ddb0 ["INT_ADD", "register:40f0:8", ["const:57ddb0:8", "const:4:8"]]
+ 0057ddb0 ["CALL", null, ["callee:00c57f60:8"]]
- 0057dd70 bytes 48681b94
+ 0057ddb0 bytes 6c681b94
- 0057dd90 ["INT_ADD", "register:40f0:8", ["const:57dd90:8", "const:4:8"]]
- 0057dd90 ["CALL", null, ["callee:00c58010:8"]]
+ 0057ddd0 ["INT_ADD", "register:40f0:8", ["const:57ddd0:8", "const:4:8"]]
+ 0057ddd0 ["CALL", null, ["callee:00c58010:8"]]
- 0057dd90 bytes 6c681b94
+ 0057ddd0 bytes 90681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5855474afee7e4a2261bc61c55933aec"></a>

### [`0057dde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md) → [`0057de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de28.md) FUN_0057de28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`005804e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md#insn-0057de04)
- 新版 `0057de44`（命令位置の公開資料なし）

~~~diff
- 0057de04 ["INT_ADD", "register:40f0:8", ["const:57de04:8", "const:4:8"]]
- 0057de04 ["CALL", null, ["callee:00c53d70:8"]]
+ 0057de44 ["INT_ADD", "register:40f0:8", ["const:57de44:8", "const:4:8"]]
+ 0057de44 ["CALL", null, ["callee:00c53d70:8"]]
- 0057de04 bytes b3571b94
+ 0057de44 bytes cb571b94
~~~


<a id="compare-7e8b06776a0a8796e321c4f1e9978f16"></a>

### [`0057e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md) → [`0057e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e080.md) FUN_0057e080

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md#insn-0057e05c) · [`0057e07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md#insn-0057e07c)
- 新版 `0057e09c`（命令位置の公開資料なし） · `0057e0bc`（命令位置の公開資料なし）

~~~diff
- 0057e05c ["INT_ADD", "register:40f0:8", ["const:57e05c:8", "const:4:8"]]
- 0057e05c ["CALL", null, ["callee:00c53da0:8"]]
+ 0057e09c ["INT_ADD", "register:40f0:8", ["const:57e09c:8", "const:4:8"]]
+ 0057e09c ["CALL", null, ["callee:00c53da0:8"]]
- 0057e05c bytes 29571b94
+ 0057e09c bytes 41571b94
- 0057e07c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057e07c ["INT_ADD", "register:40f0:8", ["const:57e07c:8", "const:4:8"]]
- 0057e07c ["CALLIND", null, ["register:0:8"]]
+ 0057e0bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057e0bc ["INT_ADD", "register:40f0:8", ["const:57e0bc:8", "const:4:8"]]
+ 0057e0bc ["CALLIND", null, ["register:0:8"]]
- 0057e07c bytes 00013fd6
+ 0057e0bc bytes 00013fd6
~~~


<a id="compare-43bf89d7b6bfba915da2da5802c63a73"></a>

### [`0057e3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e3e8.md) → [`0057e428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e428.md) FUN_0057e428

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c1c.md) · 呼出先 1件 [`00c5a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a250.md)
- 新版 呼出元 1件 [`00550c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c5c.md) · 呼出先 1件 [`00c5a320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e3e8.md#insn-0057e404)
- 新版 `0057e444`（命令位置の公開資料なし）

~~~diff
- 0057e404 ["INT_ADD", "register:40f0:8", ["const:57e404:8", "const:4:8"]]
- 0057e404 ["CALL", null, ["callee:00c5a320:8"]]
+ 0057e444 ["INT_ADD", "register:40f0:8", ["const:57e444:8", "const:4:8"]]
+ 0057e444 ["CALL", null, ["callee:00c5a320:8"]]
- 0057e404 bytes 936f1b94
+ 0057e444 bytes b76f1b94
~~~


<a id="compare-58c88e843aa7212e64384c54a96bc304"></a>

### [`0057e418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md) → [`0057e458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e458.md) FUN_0057e458

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59860.md)
- 新版 呼出元 1件 [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e450) · [`0057e464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e464) · [`0057e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e480)
- 新版 `0057e490`（命令位置の公開資料なし） · `0057e4a4`（命令位置の公開資料なし） · `0057e4c0`（命令位置の公開資料なし）

~~~diff
- 0057e450 ["INT_ADD", "register:40f0:8", ["const:57e450:8", "const:4:8"]]
- 0057e450 ["CALL", null, ["callee:00c59930:8"]]
+ 0057e490 ["INT_ADD", "register:40f0:8", ["const:57e490:8", "const:4:8"]]
+ 0057e490 ["CALL", null, ["callee:00c59930:8"]]
- 0057e450 bytes 046d1b94
+ 0057e490 bytes 286d1b94
- 0057e464 ["INT_ADD", "register:40f0:8", ["const:57e464:8", "const:4:8"]]
- 0057e464 ["CALL", null, ["callee:00550be4:8"]]
+ 0057e4a4 ["INT_ADD", "register:40f0:8", ["const:57e4a4:8", "const:4:8"]]
+ 0057e4a4 ["CALL", null, ["callee:00550be4:8"]]
- 0057e464 bytes d049ff97
+ 0057e4a4 bytes d049ff97
- 0057e480 ["INT_ADD", "register:40f0:8", ["const:57e480:8", "const:4:8"]]
- 0057e480 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057e4c0 ["INT_ADD", "register:40f0:8", ["const:57e4c0:8", "const:4:8"]]
+ 0057e4c0 ["CALL", null, ["callee:00c53da0:8"]]
- 0057e480 bytes 20561b94
+ 0057e4c0 bytes 38561b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-374a77c0859cf63db0fc37d6a9d3d0e1"></a>

### [`0057eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md) → [`0057ebcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ebcc.md) FUN_0057ebcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c30.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59860.md)
- 新版 呼出元 1件 [`00550c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c70.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md#insn-0057ebbc) · [`0057ebec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md#insn-0057ebec)
- 新版 `0057ebfc`（命令位置の公開資料なし） · `0057ec2c`（命令位置の公開資料なし）

~~~diff
- 0057ebbc ["INT_ADD", "register:40f0:8", ["const:57ebbc:8", "const:4:8"]]
- 0057ebbc ["CALL", null, ["callee:00c59930:8"]]
+ 0057ebfc ["INT_ADD", "register:40f0:8", ["const:57ebfc:8", "const:4:8"]]
+ 0057ebfc ["CALL", null, ["callee:00c59930:8"]]
- 0057ebbc bytes 296b1b94
+ 0057ebfc bytes 4d6b1b94
- 0057ebec ["INT_ADD", "register:40f0:8", ["const:57ebec:8", "const:4:8"]]
- 0057ebec ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057ec2c ["INT_ADD", "register:40f0:8", ["const:57ec2c:8", "const:4:8"]]
+ 0057ec2c ["CALL", null, ["callee:00c57fb0:8"]]
- 0057ebec bytes bd641b94
+ 0057ec2c bytes e1641b94
~~~


<a id="compare-a6b507edd76fac98dd63bec20f7a1abc"></a>

### [`0057ebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf4.md) → [`0057ec34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec34.md) FUN_0057ec34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d2c.md) · 呼出先 1件 [`00c5a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a260.md)
- 新版 呼出元 1件 [`00550d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d6c.md) · 呼出先 1件 [`00c5a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf4.md#insn-0057ec0c)
- 新版 `0057ec4c`（命令位置の公開資料なし）

~~~diff
- 0057ec0c ["INT_ADD", "register:40f0:8", ["const:57ec0c:8", "const:4:8"]]
- 0057ec0c ["CALL", null, ["callee:00c5a330:8"]]
+ 0057ec4c ["INT_ADD", "register:40f0:8", ["const:57ec4c:8", "const:4:8"]]
+ 0057ec4c ["CALL", null, ["callee:00c5a330:8"]]
- 0057ec0c bytes 956d1b94
+ 0057ec4c bytes b96d1b94
~~~


<a id="compare-f3c625c8778815d26c796ad55d4863df"></a>

### [`0057ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec20.md) → [`0057ec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec60.md) FUN_0057ec60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d30.md) · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a290.md)
- 新版 呼出元 1件 [`00550d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d70.md) · 呼出先 1件 [`00c5a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec20.md#insn-0057ec48)
- 新版 `0057ec88`（命令位置の公開資料なし）

~~~diff
- 0057ec48 ["INT_ADD", "register:40f0:8", ["const:57ec48:8", "const:4:8"]]
- 0057ec48 ["CALL", null, ["callee:00c5a360:8"]]
+ 0057ec88 ["INT_ADD", "register:40f0:8", ["const:57ec88:8", "const:4:8"]]
+ 0057ec88 ["CALL", null, ["callee:00c5a360:8"]]
- 0057ec48 bytes 926d1b94
+ 0057ec88 bytes b66d1b94
~~~


<a id="compare-8c8058c6dbeb361741c3233e2ed0ed96"></a>

### [`0057ec5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md) → [`0057ec9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec9c.md) FUN_0057ec9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d34.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2a0.md)
- 新版 呼出元 1件 [`00550d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d74.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md#insn-0057ec8c) · [`0057ecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md#insn-0057ecc4)
- 新版 `0057eccc`（命令位置の公開資料なし） · `0057ed04`（命令位置の公開資料なし）

~~~diff
- 0057ec8c ["INT_ADD", "register:40f0:8", ["const:57ec8c:8", "const:4:8"]]
- 0057ec8c ["CALL", null, ["callee:00c5a370:8"]]
+ 0057eccc ["INT_ADD", "register:40f0:8", ["const:57eccc:8", "const:4:8"]]
+ 0057eccc ["CALL", null, ["callee:00c5a370:8"]]
- 0057ec8c bytes 856d1b94
+ 0057eccc bytes a96d1b94
- 0057ecc4 ["INT_ADD", "register:40f0:8", ["const:57ecc4:8", "const:4:8"]]
- 0057ecc4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057ed04 ["INT_ADD", "register:40f0:8", ["const:57ed04:8", "const:4:8"]]
+ 0057ed04 ["CALL", null, ["callee:00c57fb0:8"]]
- 0057ecc4 bytes 87641b94
+ 0057ed04 bytes ab641b94
~~~


<a id="compare-9932d8de7f1932bddf2c3a1982649d35"></a>

### [`0057eccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eccc.md) → [`0057ed0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ed0c.md) FUN_0057ed0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555294.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005552d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552d4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eccc.md#insn-0057ecdc)
- 新版 `0057ed1c`（命令位置の公開資料なし）

~~~diff
- 0057ecdc ["INT_ADD", "register:40f0:8", ["const:57ecdc:8", "const:4:8"]]
- 0057ecdc ["CALL", null, ["callee:005552d4:8"]]
+ 0057ed1c ["INT_ADD", "register:40f0:8", ["const:57ed1c:8", "const:4:8"]]
+ 0057ed1c ["CALL", null, ["callee:005552d4:8"]]
- 0057ecdc bytes 6e59ff97
+ 0057ed1c bytes 6e59ff97
~~~


<a id="compare-5e9a810d01e76b700fb70043a95f4936"></a>

### [`0057fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md) → [`0057fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md) FUN_0057fd60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055529c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/0055529c.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005552dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552dc.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057fd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fd44) · [`0057fd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fd54) · [`0057fda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fda4)
- 新版 `0057fd84`（命令位置の公開資料なし） · `0057fd94`（命令位置の公開資料なし） · `0057fde4`（命令位置の公開資料なし）

~~~diff
- 0057fd44 ["INT_ADD", "register:40f0:8", ["const:57fd44:8", "const:4:8"]]
- 0057fd44 ["CALL", null, ["callee:0057fb4c:8"]]
+ 0057fd84 ["INT_ADD", "register:40f0:8", ["const:57fd84:8", "const:4:8"]]
+ 0057fd84 ["CALL", null, ["callee:0057fb4c:8"]]
- 0057fd44 bytes 72ffff97
+ 0057fd84 bytes 72ffff97
- 0057fd54 ["INT_ADD", "register:40f0:8", ["const:57fd54:8", "const:4:8"]]
- 0057fd54 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057fd94 ["INT_ADD", "register:40f0:8", ["const:57fd94:8", "const:4:8"]]
+ 0057fd94 ["CALL", null, ["callee:00c57f80:8"]]
- 0057fd54 bytes 57601b94
+ 0057fd94 bytes 7b601b94
- 0057fda4 ["INT_ADD", "register:40f0:8", ["const:57fda4:8", "const:4:8"]]
- 0057fda4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057fde4 ["INT_ADD", "register:40f0:8", ["const:57fde4:8", "const:4:8"]]
+ 0057fde4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0057fda4 bytes 4f601b94
+ 0057fde4 bytes 73601b94
~~~


<a id="compare-e3018b0f12218b696e88dd069085c90f"></a>

### [`0057fefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md) → [`0057ff3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md) FUN_0057ff3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005552a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a8.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005552e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e8.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff3c) · [`0057ff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff4c) · [`0057ff9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff9c)
- 新版 `0057ff7c`（命令位置の公開資料なし） · `0057ff8c`（命令位置の公開資料なし） · `0057ffdc`（命令位置の公開資料なし）

~~~diff
- 0057ff3c ["INT_ADD", "register:40f0:8", ["const:57ff3c:8", "const:4:8"]]
- 0057ff3c ["CALL", null, ["callee:0057fb4c:8"]]
+ 0057ff7c ["INT_ADD", "register:40f0:8", ["const:57ff7c:8", "const:4:8"]]
+ 0057ff7c ["CALL", null, ["callee:0057fb4c:8"]]
- 0057ff3c bytes f4feff97
+ 0057ff7c bytes f4feff97
- 0057ff4c ["INT_ADD", "register:40f0:8", ["const:57ff4c:8", "const:4:8"]]
- 0057ff4c ["CALL", null, ["callee:00c57f80:8"]]
+ 0057ff8c ["INT_ADD", "register:40f0:8", ["const:57ff8c:8", "const:4:8"]]
+ 0057ff8c ["CALL", null, ["callee:00c57f80:8"]]
- 0057ff4c bytes d95f1b94
+ 0057ff8c bytes fd5f1b94
- 0057ff9c ["INT_ADD", "register:40f0:8", ["const:57ff9c:8", "const:4:8"]]
- 0057ff9c ["CALL", null, ["callee:00c57fb0:8"]]
+ 0057ffdc ["INT_ADD", "register:40f0:8", ["const:57ffdc:8", "const:4:8"]]
+ 0057ffdc ["CALL", null, ["callee:00c57fb0:8"]]
- 0057ff9c bytes d15f1b94
+ 0057ffdc bytes f55f1b94
~~~


<a id="compare-ad881795e423f62ecdf506f0739654d5"></a>

### [`005807e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md) → [`00580828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580828.md) FUN_00580828

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md#insn-00580804) · [`00580824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md#insn-00580824)
- 新版 `00580844`（命令位置の公開資料なし） · `00580864`（命令位置の公開資料なし）

~~~diff
- 00580804 ["INT_ADD", "register:40f0:8", ["const:580804:8", "const:4:8"]]
- 00580804 ["CALL", null, ["callee:00c53da0:8"]]
+ 00580844 ["INT_ADD", "register:40f0:8", ["const:580844:8", "const:4:8"]]
+ 00580844 ["CALL", null, ["callee:00c53da0:8"]]
- 00580804 bytes 3f4d1b94
+ 00580844 bytes 574d1b94
- 00580824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580824 ["INT_ADD", "register:40f0:8", ["const:580824:8", "const:4:8"]]
- 00580824 ["CALLIND", null, ["register:0:8"]]
+ 00580864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580864 ["INT_ADD", "register:40f0:8", ["const:580864:8", "const:4:8"]]
+ 00580864 ["CALLIND", null, ["register:0:8"]]
- 00580824 bytes 00013fd6
+ 00580864 bytes 00013fd6
~~~


<a id="compare-91ee54d1093df11ec603473a16c45ef2"></a>

### [`00580838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md) → [`00580878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580878.md) FUN_00580878

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md#insn-00580854) · [`00580874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md#insn-00580874)
- 新版 `00580894`（命令位置の公開資料なし） · `005808b4`（命令位置の公開資料なし）

~~~diff
- 00580854 ["INT_ADD", "register:40f0:8", ["const:580854:8", "const:4:8"]]
- 00580854 ["CALL", null, ["callee:00c53da0:8"]]
+ 00580894 ["INT_ADD", "register:40f0:8", ["const:580894:8", "const:4:8"]]
+ 00580894 ["CALL", null, ["callee:00c53da0:8"]]
- 00580854 bytes 2b4d1b94
+ 00580894 bytes 434d1b94
- 00580874 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580874 ["INT_ADD", "register:40f0:8", ["const:580874:8", "const:4:8"]]
- 00580874 ["CALLIND", null, ["register:0:8"]]
+ 005808b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005808b4 ["INT_ADD", "register:40f0:8", ["const:5808b4:8", "const:4:8"]]
+ 005808b4 ["CALLIND", null, ["register:0:8"]]
- 00580874 bytes 00013fd6
+ 005808b4 bytes 00013fd6
~~~


<a id="compare-fb7185656f2cb1c6e765b2bdd5be0c6f"></a>

### [`00580a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md) → [`00580ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ac8.md) FUN_00580ac8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) · 呼出先 2件 [`00c58ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ba0.md) [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md)
- 新版 呼出元 1件 [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) · 呼出先 2件 [`00c58c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c70.md) [`00c58ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ab4) · [`00580ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ac8) · [`00580ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ae0)
- 新版 `00580af4`（命令位置の公開資料なし） · `00580b08`（命令位置の公開資料なし） · `00580b20`（命令位置の公開資料なし）

~~~diff
- 00580ab4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580ab4 ["INT_ADD", "register:40f0:8", ["const:580ab4:8", "const:4:8"]]
- 00580ab4 ["CALLIND", null, ["register:0:8"]]
+ 00580af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580af4 ["INT_ADD", "register:40f0:8", ["const:580af4:8", "const:4:8"]]
+ 00580af4 ["CALLIND", null, ["register:0:8"]]
- 00580ab4 bytes 00013fd6
+ 00580af4 bytes 00013fd6
- 00580ac8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580ac8 ["INT_ADD", "register:40f0:8", ["const:580ac8:8", "const:4:8"]]
- 00580ac8 ["CALLIND", null, ["register:0:8"]]
+ 00580b08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580b08 ["INT_ADD", "register:40f0:8", ["const:580b08:8", "const:4:8"]]
+ 00580b08 ["CALLIND", null, ["register:0:8"]]
- 00580ac8 bytes 00013fd6
+ 00580b08 bytes 00013fd6
- 00580ae0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580ae0 ["INT_ADD", "register:40f0:8", ["const:580ae0:8", "const:4:8"]]
- 00580ae0 ["CALLIND", null, ["register:0:8"]]
+ 00580b20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580b20 ["INT_ADD", "register:40f0:8", ["const:580b20:8", "const:4:8"]]
+ 00580b20 ["CALLIND", null, ["register:0:8"]]
- 00580ae0 bytes 20013fd6
+ 00580b20 bytes 20013fd6
~~~


<a id="compare-8bdaa2f1db37bcc495f276c0666dc008"></a>

### [`00580fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md) → [`00580fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580fe8.md) FUN_00580fe8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md#insn-00580fc4) · [`00580fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md#insn-00580fe4)
- 新版 `00581004`（命令位置の公開資料なし） · `00581024`（命令位置の公開資料なし）

~~~diff
- 00580fc4 ["INT_ADD", "register:40f0:8", ["const:580fc4:8", "const:4:8"]]
- 00580fc4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00581004 ["INT_ADD", "register:40f0:8", ["const:581004:8", "const:4:8"]]
+ 00581004 ["CALL", null, ["callee:00c53da0:8"]]
- 00580fc4 bytes 4f4b1b94
+ 00581004 bytes 674b1b94
- 00580fe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580fe4 ["INT_ADD", "register:40f0:8", ["const:580fe4:8", "const:4:8"]]
- 00580fe4 ["CALLIND", null, ["register:0:8"]]
+ 00581024 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00581024 ["INT_ADD", "register:40f0:8", ["const:581024:8", "const:4:8"]]
+ 00581024 ["CALLIND", null, ["register:0:8"]]
- 00580fe4 bytes 00013fd6
+ 00581024 bytes 00013fd6
~~~


<a id="compare-5f6891ab01d64d423a004135ffce5399"></a>

### [`00580ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md) → [`00581038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581038.md) FUN_00581038

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md#insn-00581014) · [`00581034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md#insn-00581034)
- 新版 `00581054`（命令位置の公開資料なし） · `00581074`（命令位置の公開資料なし）

~~~diff
- 00581014 ["INT_ADD", "register:40f0:8", ["const:581014:8", "const:4:8"]]
- 00581014 ["CALL", null, ["callee:00c53da0:8"]]
+ 00581054 ["INT_ADD", "register:40f0:8", ["const:581054:8", "const:4:8"]]
+ 00581054 ["CALL", null, ["callee:00c53da0:8"]]
- 00581014 bytes 3b4b1b94
+ 00581054 bytes 534b1b94
- 00581034 ["COPY", "register:0:8", ["register:4040:8"]]
- 00581034 ["INT_ADD", "register:40f0:8", ["const:581034:8", "const:4:8"]]
- 00581034 ["CALLIND", null, ["register:0:8"]]
+ 00581074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00581074 ["INT_ADD", "register:40f0:8", ["const:581074:8", "const:4:8"]]
+ 00581074 ["CALLIND", null, ["register:0:8"]]
- 00581034 bytes 00013fd6
+ 00581074 bytes 00013fd6
~~~


<a id="compare-417a2891ad9ecdba45751397590d5ec9"></a>

### [`00581bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md) → [`00581c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581c38.md) FUN_00581c38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00560464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560464.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)
- 新版 呼出元 1件 [`005604a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a4.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581c74) · [`00581d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581d34) · [`00581d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581d40)
- 新版 `00581cb4`（命令位置の公開資料なし） · `00581d74`（命令位置の公開資料なし） · `00581d80`（命令位置の公開資料なし）

~~~diff
- 00581c74 ["INT_ADD", "register:40f0:8", ["const:581c74:8", "const:4:8"]]
- 00581c74 ["CALL", null, ["callee:00c586d0:8"]]
+ 00581cb4 ["INT_ADD", "register:40f0:8", ["const:581cb4:8", "const:4:8"]]
+ 00581cb4 ["CALL", null, ["callee:00c586d0:8"]]
- 00581c74 bytes 635a1b94
+ 00581cb4 bytes 875a1b94
- 00581d34 ["INT_ADD", "register:40f0:8", ["const:581d34:8", "const:4:8"]]
- 00581d34 ["CALL", null, ["callee:00c58130:8"]]
+ 00581d74 ["INT_ADD", "register:40f0:8", ["const:581d74:8", "const:4:8"]]
+ 00581d74 ["CALL", null, ["callee:00c58130:8"]]
- 00581d34 bytes cb581b94
+ 00581d74 bytes ef581b94
- 00581d40 ["INT_ADD", "register:40f0:8", ["const:581d40:8", "const:4:8"]]
- 00581d40 ["CALL", null, ["callee:00c586d0:8"]]
+ 00581d80 ["INT_ADD", "register:40f0:8", ["const:581d80:8", "const:4:8"]]
+ 00581d80 ["CALL", null, ["callee:00c586d0:8"]]
- 00581d40 bytes 305a1b94
+ 00581d80 bytes 545a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16c897c529841ef931aa16a41f12393"></a>

### [`00581f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f34.md) → [`00581f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f74.md) FUN_00581f74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f34.md#insn-00581f54)
- 新版 `00581f94`（命令位置の公開資料なし）

~~~diff
- 00581f54 ["COPY", "register:0:8", ["register:4050:8"]]
- 00581f54 ["INT_ADD", "register:40f0:8", ["const:581f54:8", "const:4:8"]]
- 00581f54 ["CALLIND", null, ["register:0:8"]]
+ 00581f94 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00581f94 ["INT_ADD", "register:40f0:8", ["const:581f94:8", "const:4:8"]]
+ 00581f94 ["CALLIND", null, ["register:0:8"]]
- 00581f54 bytes 40013fd6
+ 00581f94 bytes 40013fd6
~~~


<a id="compare-0bcee9c3005b35a08b313f0709bdd37b"></a>

### [`00582b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md) → [`00582b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582b78.md) FUN_00582b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00582b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582b70) · [`00582b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582b8c) · [`00582ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582ba8)
- 新版 `00582bb0`（命令位置の公開資料なし） · `00582bcc`（命令位置の公開資料なし） · `00582be8`（命令位置の公開資料なし）

~~~diff
- 00582b70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00582b70 ["INT_ADD", "register:40f0:8", ["const:582b70:8", "const:4:8"]]
- 00582b70 ["CALLIND", null, ["register:0:8"]]
+ 00582bb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582bb0 ["INT_ADD", "register:40f0:8", ["const:582bb0:8", "const:4:8"]]
+ 00582bb0 ["CALLIND", null, ["register:0:8"]]
- 00582b70 bytes 20013fd6
+ 00582bb0 bytes 20013fd6
- 00582b8c ["INT_ADD", "register:40f0:8", ["const:582b8c:8", "const:4:8"]]
- 00582b8c ["CALL", null, ["callee:00c57f60:8"]]
+ 00582bcc ["INT_ADD", "register:40f0:8", ["const:582bcc:8", "const:4:8"]]
+ 00582bcc ["CALL", null, ["callee:00c57f60:8"]]
- 00582b8c bytes c1541b94
+ 00582bcc bytes e5541b94
- 00582ba8 ["INT_ADD", "register:40f0:8", ["const:582ba8:8", "const:4:8"]]
- 00582ba8 ["CALL", null, ["callee:00c58160:8"]]
+ 00582be8 ["INT_ADD", "register:40f0:8", ["const:582be8:8", "const:4:8"]]
+ 00582be8 ["CALL", null, ["callee:00c58160:8"]]
- 00582ba8 bytes 3a551b94
+ 00582be8 bytes 5e551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0abae71516e6ec777b5b996a0afce6a2"></a>

### [`005831c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md) → [`00583204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583204.md) FUN_00583204

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005831fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-005831fc) · [`00583218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-00583218) · [`00583234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-00583234)
- 新版 `0058323c`（命令位置の公開資料なし） · `00583258`（命令位置の公開資料なし） · `00583274`（命令位置の公開資料なし）

~~~diff
- 005831fc ["COPY", "register:0:8", ["register:4048:8"]]
- 005831fc ["INT_ADD", "register:40f0:8", ["const:5831fc:8", "const:4:8"]]
- 005831fc ["CALLIND", null, ["register:0:8"]]
+ 0058323c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058323c ["INT_ADD", "register:40f0:8", ["const:58323c:8", "const:4:8"]]
+ 0058323c ["CALLIND", null, ["register:0:8"]]
- 005831fc bytes 20013fd6
+ 0058323c bytes 20013fd6
- 00583218 ["INT_ADD", "register:40f0:8", ["const:583218:8", "const:4:8"]]
- 00583218 ["CALL", null, ["callee:00c57f60:8"]]
+ 00583258 ["INT_ADD", "register:40f0:8", ["const:583258:8", "const:4:8"]]
+ 00583258 ["CALL", null, ["callee:00c57f60:8"]]
- 00583218 bytes 1e531b94
+ 00583258 bytes 42531b94
- 00583234 ["INT_ADD", "register:40f0:8", ["const:583234:8", "const:4:8"]]
- 00583234 ["CALL", null, ["callee:00c58160:8"]]
+ 00583274 ["INT_ADD", "register:40f0:8", ["const:583274:8", "const:4:8"]]
+ 00583274 ["CALL", null, ["callee:00c58160:8"]]
- 00583234 bytes 97531b94
+ 00583274 bytes bb531b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ecedd7d5d1b322276bcf9f540dde05"></a>

### [`0058339c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md) → [`005833dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833dc.md) FUN_005833dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c5a2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c5a3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005833ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md#insn-005833ec) · [`00583428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md#insn-00583428)
- 新版 `0058342c`（命令位置の公開資料なし） · `00583468`（命令位置の公開資料なし）

~~~diff
- 005833ec ["INT_ADD", "register:40f0:8", ["const:5833ec:8", "const:4:8"]]
- 005833ec ["CALL", null, ["callee:00c5a3b0:8"]]
+ 0058342c ["INT_ADD", "register:40f0:8", ["const:58342c:8", "const:4:8"]]
+ 0058342c ["CALL", null, ["callee:00c5a3b0:8"]]
- 005833ec bytes bd5b1b94
+ 0058342c bytes e15b1b94
- 00583428 ["INT_ADD", "register:40f0:8", ["const:583428:8", "const:4:8"]]
- 00583428 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00583468 ["INT_ADD", "register:40f0:8", ["const:583468:8", "const:4:8"]]
+ 00583468 ["CALL", null, ["callee:00c5a3b0:8"]]
- 00583428 bytes ae5b1b94
+ 00583468 bytes d25b1b94
~~~


<a id="compare-10f52aa64f392e4fb710071fb1c99c9b"></a>

### [`005836bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md) → [`005836fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005836fc.md) FUN_005836fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005836d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md#insn-005836d8) · [`005836f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md#insn-005836f8)
- 新版 `00583718`（命令位置の公開資料なし） · `00583738`（命令位置の公開資料なし）

~~~diff
- 005836d8 ["INT_ADD", "register:40f0:8", ["const:5836d8:8", "const:4:8"]]
- 005836d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00583718 ["INT_ADD", "register:40f0:8", ["const:583718:8", "const:4:8"]]
+ 00583718 ["CALL", null, ["callee:00c53da0:8"]]
- 005836d8 bytes 8a411b94
+ 00583718 bytes a2411b94
- 005836f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005836f8 ["INT_ADD", "register:40f0:8", ["const:5836f8:8", "const:4:8"]]
- 005836f8 ["CALLIND", null, ["register:0:8"]]
+ 00583738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00583738 ["INT_ADD", "register:40f0:8", ["const:583738:8", "const:4:8"]]
+ 00583738 ["CALLIND", null, ["register:0:8"]]
- 005836f8 bytes 00013fd6
+ 00583738 bytes 00013fd6
~~~


<a id="compare-9ad70ffe9dd5f90217aba92faeba7212"></a>

### [`0058370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md) → [`0058374c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058374c.md) FUN_0058374c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058375c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-0058375c) · [`00583788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-00583788) · [`00583794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-00583794)
- 新版 `0058379c`（命令位置の公開資料なし） · `005837c8`（命令位置の公開資料なし） · `005837d4`（命令位置の公開資料なし）

~~~diff
- 0058375c ["INT_ADD", "register:40f0:8", ["const:58375c:8", "const:4:8"]]
- 0058375c ["CALL", null, ["callee:0043bb60:8"]]
+ 0058379c ["INT_ADD", "register:40f0:8", ["const:58379c:8", "const:4:8"]]
+ 0058379c ["CALL", null, ["callee:0043bb60:8"]]
- 0058375c bytes f1e0fa97
+ 0058379c bytes f1e0fa97
- 00583788 ["INT_ADD", "register:40f0:8", ["const:583788:8", "const:4:8"]]
- 00583788 ["CALL", null, ["callee:0043bb60:8"]]
+ 005837c8 ["INT_ADD", "register:40f0:8", ["const:5837c8:8", "const:4:8"]]
+ 005837c8 ["CALL", null, ["callee:0043bb60:8"]]
- 00583788 bytes e6e0fa97
+ 005837c8 bytes e6e0fa97
- 00583794 ["INT_ADD", "register:40f0:8", ["const:583794:8", "const:4:8"]]
- 00583794 ["CALL", null, ["callee:00549114:8"]]
+ 005837d4 ["INT_ADD", "register:40f0:8", ["const:5837d4:8", "const:4:8"]]
+ 005837d4 ["CALL", null, ["callee:00549114:8"]]
- 00583794 bytes 5016ff97
+ 005837d4 bytes 5016ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5732b69ad2f732fb1ee6129137516a27"></a>

### [`0058381c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058381c.md) → [`0058385c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058385c.md) FUN_0058385c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00583838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058381c.md#insn-00583838)
- 新版 `00583878`（命令位置の公開資料なし）

~~~diff
- 00583838 ["INT_ADD", "register:40f0:8", ["const:583838:8", "const:4:8"]]
- 00583838 ["CALL", null, ["callee:00c53d70:8"]]
+ 00583878 ["INT_ADD", "register:40f0:8", ["const:583878:8", "const:4:8"]]
+ 00583878 ["CALL", null, ["callee:00c53d70:8"]]
- 00583838 bytes 26411b94
+ 00583878 bytes 3e411b94
~~~


<a id="compare-35536857a2bae1266d274b3d6558c838"></a>

### [`005847d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md) → [`00584810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584810.md) FUN_00584810

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058480c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md#insn-0058480c) · [`00584840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md#insn-00584840)
- 新版 `0058484c`（命令位置の公開資料なし） · `00584880`（命令位置の公開資料なし）

~~~diff
- 0058480c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058480c ["INT_ADD", "register:40f0:8", ["const:58480c:8", "const:4:8"]]
- 0058480c ["CALLIND", null, ["register:0:8"]]
+ 0058484c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058484c ["INT_ADD", "register:40f0:8", ["const:58484c:8", "const:4:8"]]
+ 0058484c ["CALLIND", null, ["register:0:8"]]
- 0058480c bytes 00013fd6
+ 0058484c bytes 00013fd6
- 00584840 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584840 ["INT_ADD", "register:40f0:8", ["const:584840:8", "const:4:8"]]
- 00584840 ["CALLIND", null, ["register:0:8"]]
+ 00584880 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584880 ["INT_ADD", "register:40f0:8", ["const:584880:8", "const:4:8"]]
+ 00584880 ["CALLIND", null, ["register:0:8"]]
- 00584840 bytes 00013fd6
+ 00584880 bytes 00013fd6
~~~


<a id="compare-94e1dd90ac947a8858bbffe664407cda"></a>

### [`00584bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md) → [`00584c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c00.md) FUN_00584c00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md#insn-00584bdc) · [`00584bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md#insn-00584bfc)
- 新版 `00584c1c`（命令位置の公開資料なし） · `00584c3c`（命令位置の公開資料なし）

~~~diff
- 00584bdc ["INT_ADD", "register:40f0:8", ["const:584bdc:8", "const:4:8"]]
- 00584bdc ["CALL", null, ["callee:00c53da0:8"]]
+ 00584c1c ["INT_ADD", "register:40f0:8", ["const:584c1c:8", "const:4:8"]]
+ 00584c1c ["CALL", null, ["callee:00c53da0:8"]]
- 00584bdc bytes 493c1b94
+ 00584c1c bytes 613c1b94
- 00584bfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00584bfc ["INT_ADD", "register:40f0:8", ["const:584bfc:8", "const:4:8"]]
- 00584bfc ["CALLIND", null, ["register:0:8"]]
+ 00584c3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584c3c ["INT_ADD", "register:40f0:8", ["const:584c3c:8", "const:4:8"]]
+ 00584c3c ["CALLIND", null, ["register:0:8"]]
- 00584bfc bytes 00013fd6
+ 00584c3c bytes 00013fd6
~~~


<a id="compare-75174262907a68d03e9d0df96c1d033e"></a>

### [`00584c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md) → [`00584c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584c50.md) FUN_00584c50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md#insn-00584c2c) · [`00584c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md#insn-00584c4c)
- 新版 `00584c6c`（命令位置の公開資料なし） · `00584c8c`（命令位置の公開資料なし）

~~~diff
- 00584c2c ["INT_ADD", "register:40f0:8", ["const:584c2c:8", "const:4:8"]]
- 00584c2c ["CALL", null, ["callee:00c53da0:8"]]
+ 00584c6c ["INT_ADD", "register:40f0:8", ["const:584c6c:8", "const:4:8"]]
+ 00584c6c ["CALL", null, ["callee:00c53da0:8"]]
- 00584c2c bytes 353c1b94
+ 00584c6c bytes 4d3c1b94
- 00584c4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00584c4c ["INT_ADD", "register:40f0:8", ["const:584c4c:8", "const:4:8"]]
- 00584c4c ["CALLIND", null, ["register:0:8"]]
+ 00584c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584c8c ["INT_ADD", "register:40f0:8", ["const:584c8c:8", "const:4:8"]]
+ 00584c8c ["CALLIND", null, ["register:0:8"]]
- 00584c4c bytes 00013fd6
+ 00584c8c bytes 00013fd6
~~~


<a id="compare-1ae62343c6780f2443c1596e299cd938"></a>

### [`00584c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md) → [`00584ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ca0.md) FUN_00584ca0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584c84) · [`00584c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584c9c) · [`00584cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584cc0)
- 新版 `00584cc4`（命令位置の公開資料なし） · `00584cdc`（命令位置の公開資料なし） · `00584d00`（命令位置の公開資料なし）

~~~diff
- 00584c84 ["INT_ADD", "register:40f0:8", ["const:584c84:8", "const:4:8"]]
- 00584c84 ["CALL", null, ["callee:00c53d70:8"]]
+ 00584cc4 ["INT_ADD", "register:40f0:8", ["const:584cc4:8", "const:4:8"]]
+ 00584cc4 ["CALL", null, ["callee:00c53d70:8"]]
- 00584c84 bytes 133c1b94
+ 00584cc4 bytes 2b3c1b94
- 00584c9c ["INT_ADD", "register:40f0:8", ["const:584c9c:8", "const:4:8"]]
- 00584c9c ["CALL", null, ["callee:00c53da0:8"]]
+ 00584cdc ["INT_ADD", "register:40f0:8", ["const:584cdc:8", "const:4:8"]]
+ 00584cdc ["CALL", null, ["callee:00c53da0:8"]]
- 00584c9c bytes 193c1b94
+ 00584cdc bytes 313c1b94
- 00584cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584cc0 ["INT_ADD", "register:40f0:8", ["const:584cc0:8", "const:4:8"]]
- 00584cc0 ["CALLIND", null, ["register:0:8"]]
+ 00584d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584d00 ["INT_ADD", "register:40f0:8", ["const:584d00:8", "const:4:8"]]
+ 00584d00 ["CALLIND", null, ["register:0:8"]]
- 00584cc0 bytes 00013fd6
+ 00584d00 bytes 00013fd6
~~~


