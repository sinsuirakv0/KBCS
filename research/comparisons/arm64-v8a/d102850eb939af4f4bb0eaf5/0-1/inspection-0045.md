# v16.0.1 → v16.0.2 · 要調査の変更候補 (45)

[一覧の目次](README.md)

<a id="compare-344db3fb2f295c97f2d0c5e02766d280"></a>

### [`00c3932c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md) → [`00c393c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md) FUN_00c393c8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c39374) · [`00c39394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c39394) · [`00c393ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c393ec)
- 新版 [`00c39410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39410) · [`00c39430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39430) · [`00c39488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c393c8.md#insn-00c39488)

~~~diff
- 00c39374 ["INT_ADD", "register:40f0:8", ["const:c39374:8", "const:4:8"]]
- 00c39374 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39410 ["INT_ADD", "register:40f0:8", ["const:c39410:8", "const:4:8"]]
+ 00c39410 ["CALL", null, ["callee:00c5b920:8"]]
- 00c39374 bytes 37890094
+ 00c39410 bytes 44890094
- 00c39394 ["INT_ADD", "register:40f0:8", ["const:c39394:8", "const:4:8"]]
- 00c39394 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39430 ["INT_ADD", "register:40f0:8", ["const:c39430:8", "const:4:8"]]
+ 00c39430 ["CALL", null, ["callee:00c5b920:8"]]
- 00c39394 bytes 2f890094
+ 00c39430 bytes 3c890094
- 00c393ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00c393ec ["INT_ADD", "register:40f0:8", ["const:c393ec:8", "const:4:8"]]
- 00c393ec ["CALLIND", null, ["register:0:8"]]
+ 00c39488 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c39488 ["INT_ADD", "register:40f0:8", ["const:c39488:8", "const:4:8"]]
+ 00c39488 ["CALLIND", null, ["register:0:8"]]
- 00c393ec bytes 00013fd6
+ 00c39488 bytes 00013fd6
~~~


<a id="compare-783219a051fe68f140ae7a39b965cbee"></a>

### [`00c394dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md) → [`00c39578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md) FUN_00c39578

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md#insn-00c39520) · [`00c3953c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md#insn-00c3953c)
- 新版 [`00c395bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md#insn-00c395bc) · [`00c395d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md#insn-00c395d8)

~~~diff
- 00c39520 ["INT_ADD", "register:40f0:8", ["const:c39520:8", "const:4:8"]]
- 00c39520 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c395bc ["INT_ADD", "register:40f0:8", ["const:c395bc:8", "const:4:8"]]
+ 00c395bc ["CALL", null, ["callee:00c5b920:8"]]
- 00c39520 bytes cc880094
+ 00c395bc bytes d9880094
- 00c3953c ["INT_ADD", "register:40f0:8", ["const:c3953c:8", "const:4:8"]]
- 00c3953c ["CALL", null, ["callee:00c5b920:8"]]
+ 00c395d8 ["INT_ADD", "register:40f0:8", ["const:c395d8:8", "const:4:8"]]
+ 00c395d8 ["CALL", null, ["callee:00c5b920:8"]]
- 00c3953c bytes c5880094
+ 00c395d8 bytes d2880094
~~~


<a id="compare-42194b70d5d43bf403ea14620019741d"></a>

### [`00c39838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39838.md) → [`00c398d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c398d4.md) FUN_00c398d4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39838.md#insn-00c39888)
- 新版 [`00c39924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c398d4.md#insn-00c39924)

~~~diff
- 00c39888 ["INT_ADD", "register:40f0:8", ["const:c39888:8", "const:4:8"]]
- 00c39888 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39924 ["INT_ADD", "register:40f0:8", ["const:c39924:8", "const:4:8"]]
+ 00c39924 ["CALL", null, ["callee:00c5b920:8"]]
- 00c39888 bytes f2870094
+ 00c39924 bytes ff870094
~~~


<a id="compare-71a2cbc4bbf7dc0c1c088303ce360045"></a>

### [`00c3997c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3997c.md) → [`00c39a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39a18.md) FUN_00c39a18

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c399c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3997c.md#insn-00c399c0)
- 新版 [`00c39a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39a18.md#insn-00c39a5c)

~~~diff
- 00c399c0 ["INT_ADD", "register:40f0:8", ["const:c399c0:8", "const:4:8"]]
- 00c399c0 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39a5c ["INT_ADD", "register:40f0:8", ["const:c39a5c:8", "const:4:8"]]
+ 00c39a5c ["CALL", null, ["callee:00c5b920:8"]]
- 00c399c0 bytes a4870094
+ 00c39a5c bytes b1870094
~~~


<a id="compare-9dd5649bdd13c4ce77746480e671ed43"></a>

### [`00c3a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md) → [`00c3a0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md) FUN_00c3a0e4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3a06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a06c) · [`00c3a0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a0a8) · [`00c3a0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a0bc)
- 新版 [`00c3a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a108) · [`00c3a144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a144) · [`00c3a158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a158)

~~~diff
- 00c3a06c ["INT_ADD", "register:40f0:8", ["const:c3a06c:8", "const:4:8"]]
- 00c3a06c ["CALL", null, ["callee:00c58730:8"]]
+ 00c3a108 ["INT_ADD", "register:40f0:8", ["const:c3a108:8", "const:4:8"]]
+ 00c3a108 ["CALL", null, ["callee:00c58730:8"]]
- 00c3a06c bytes 7d790094
+ 00c3a108 bytes 8a790094
- 00c3a0a8 ["INT_ADD", "register:40f0:8", ["const:c3a0a8:8", "const:4:8"]]
- 00c3a0a8 ["CALL", null, ["callee:00c58730:8"]]
+ 00c3a144 ["INT_ADD", "register:40f0:8", ["const:c3a144:8", "const:4:8"]]
+ 00c3a144 ["CALL", null, ["callee:00c58730:8"]]
- 00c3a0a8 bytes 6e790094
+ 00c3a144 bytes 7b790094
- 00c3a0bc ["INT_ADD", "register:40f0:8", ["const:c3a0bc:8", "const:4:8"]]
- 00c3a0bc ["CALL", null, ["callee:00c58730:8"]]
+ 00c3a158 ["INT_ADD", "register:40f0:8", ["const:c3a158:8", "const:4:8"]]
+ 00c3a158 ["CALL", null, ["callee:00c58730:8"]]
- 00c3a0bc bytes 69790094
+ 00c3a158 bytes 76790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75f4392517f1797ae92810e036b9103f"></a>

### [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) → [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) FUN_00c3a1b4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3a148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md#insn-00c3a148)
- 新版 [`00c3a1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md#insn-00c3a1e4)

~~~diff
- 00c3a148 ["INT_ADD", "register:40f0:8", ["const:c3a148:8", "const:4:8"]]
- 00c3a148 ["CALL", null, ["callee:00c58120:8"]]
+ 00c3a1e4 ["INT_ADD", "register:40f0:8", ["const:c3a1e4:8", "const:4:8"]]
+ 00c3a1e4 ["CALL", null, ["callee:00c58120:8"]]
- 00c3a148 bytes c2770094
+ 00c3a1e4 bytes cf770094
~~~


<a id="compare-6a631c3589524c7d681232f74dcfe3ae"></a>

### [`00c3c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md) → [`00c3c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md) FUN_00c3c100

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 2件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3c100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c100) · [`00c3c17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c17c) · [`00c3c19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c19c)
- 新版 [`00c3c19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c19c) · [`00c3c218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c218) · [`00c3c238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c238)

~~~diff
- 00c3c100 ["INT_ADD", "register:40f0:8", ["const:c3c100:8", "const:4:8"]]
- 00c3c100 ["CALL", null, ["callee:00c58010:8"]]
+ 00c3c19c ["INT_ADD", "register:40f0:8", ["const:c3c19c:8", "const:4:8"]]
+ 00c3c19c ["CALL", null, ["callee:00c58010:8"]]
- 00c3c100 bytes 906f0094
+ 00c3c19c bytes 9d6f0094
- 00c3c17c ["INT_ADD", "register:40f0:8", ["const:c3c17c:8", "const:4:8"]]
- 00c3c17c ["CALL", null, ["callee:00c58730:8"]]
+ 00c3c218 ["INT_ADD", "register:40f0:8", ["const:c3c218:8", "const:4:8"]]
+ 00c3c218 ["CALL", null, ["callee:00c58730:8"]]
- 00c3c17c bytes 39710094
+ 00c3c218 bytes 46710094
- 00c3c19c ["INT_ADD", "register:40f0:8", ["const:c3c19c:8", "const:4:8"]]
- 00c3c19c ["CALL", null, ["callee:00c58010:8"]]
+ 00c3c238 ["INT_ADD", "register:40f0:8", ["const:c3c238:8", "const:4:8"]]
+ 00c3c238 ["CALL", null, ["callee:00c58010:8"]]
- 00c3c19c bytes 696f0094
+ 00c3c238 bytes 766f0094
~~~


<a id="compare-77d94ecdb670822e4504cbe688540f74"></a>

### [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md) → [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md) FUN_00c3cd04

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3ccb0) · [`00c3ccc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3ccc4) · [`00c3cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3cccc)
- 新版 [`00c3cd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd4c) · [`00c3cd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd60) · [`00c3cd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd68)

~~~diff
- 00c3ccb0 ["INT_ADD", "register:40f0:8", ["const:c3ccb0:8", "const:4:8"]]
- 00c3ccb0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3cd4c ["INT_ADD", "register:40f0:8", ["const:c3cd4c:8", "const:4:8"]]
+ 00c3cd4c ["CALL", null, ["callee:00c5a170:8"]]
- 00c3ccb0 bytes fc740094
+ 00c3cd4c bytes 09750094
- 00c3ccc4 ["INT_ADD", "register:40f0:8", ["const:c3ccc4:8", "const:4:8"]]
- 00c3ccc4 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c3cd60 ["INT_ADD", "register:40f0:8", ["const:c3cd60:8", "const:4:8"]]
+ 00c3cd60 ["CALL", null, ["callee:00c5b210:8"]]
- 00c3ccc4 bytes 1f790094
+ 00c3cd60 bytes 2c790094
- 00c3cccc ["INT_ADD", "register:40f0:8", ["const:c3cccc:8", "const:4:8"]]
- 00c3cccc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3cd68 ["INT_ADD", "register:40f0:8", ["const:c3cd68:8", "const:4:8"]]
+ 00c3cd68 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3cccc bytes d5740094
+ 00c3cd68 bytes e2740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8f2008b7b7f47867c847267cbc45bb7"></a>

### [`00c3d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md) → [`00c3d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md) FUN_00c3d0cc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 2件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d0a4) · [`00c3d0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d0cc) · [`00c3d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d160)
- 新版 [`00c3d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d140) · [`00c3d168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d168) · [`00c3d1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d1fc)

~~~diff
- 00c3d0a4 ["INT_ADD", "register:40f0:8", ["const:c3d0a4:8", "const:4:8"]]
- 00c3d0a4 ["CALL", null, ["callee:00c58730:8"]]
+ 00c3d140 ["INT_ADD", "register:40f0:8", ["const:c3d140:8", "const:4:8"]]
+ 00c3d140 ["CALL", null, ["callee:00c58730:8"]]
- 00c3d0a4 bytes 6f6d0094
+ 00c3d140 bytes 7c6d0094
- 00c3d0cc ["INT_ADD", "register:40f0:8", ["const:c3d0cc:8", "const:4:8"]]
- 00c3d0cc ["CALL", null, ["callee:00c58010:8"]]
+ 00c3d168 ["INT_ADD", "register:40f0:8", ["const:c3d168:8", "const:4:8"]]
+ 00c3d168 ["CALL", null, ["callee:00c58010:8"]]
- 00c3d0cc bytes 9d6b0094
+ 00c3d168 bytes aa6b0094
- 00c3d160 ["INT_ADD", "register:40f0:8", ["const:c3d160:8", "const:4:8"]]
- 00c3d160 ["CALL", null, ["callee:00c58730:8"]]
+ 00c3d1fc ["INT_ADD", "register:40f0:8", ["const:c3d1fc:8", "const:4:8"]]
+ 00c3d1fc ["CALL", null, ["callee:00c58730:8"]]
- 00c3d160 bytes 406d0094
+ 00c3d1fc bytes 4d6d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b585d378703cb5b748d2e9f450e38f3"></a>

### [`00c3dd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md) → [`00c3ddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md) FUN_00c3ddcc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3dd80) · [`00c3dd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3dd9c) · [`00c3ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3ddc0)
- 新版 [`00c3de1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de1c) · [`00c3de38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de38) · [`00c3de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de5c)

~~~diff
- 00c3dd80 ["INT_ADD", "register:40f0:8", ["const:c3dd80:8", "const:4:8"]]
- 00c3dd80 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3de1c ["INT_ADD", "register:40f0:8", ["const:c3de1c:8", "const:4:8"]]
+ 00c3de1c ["CALL", null, ["callee:00c5a170:8"]]
- 00c3dd80 bytes c8700094
+ 00c3de1c bytes d5700094
- 00c3dd9c ["INT_ADD", "register:40f0:8", ["const:c3dd9c:8", "const:4:8"]]
- 00c3dd9c ["CALL", null, ["callee:00c580d0:8"]]
+ 00c3de38 ["INT_ADD", "register:40f0:8", ["const:c3de38:8", "const:4:8"]]
+ 00c3de38 ["CALL", null, ["callee:00c580d0:8"]]
- 00c3dd9c bytes 99680094
+ 00c3de38 bytes a6680094
- 00c3ddc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3ddc0 ["INT_ADD", "register:40f0:8", ["const:c3ddc0:8", "const:4:8"]]
- 00c3ddc0 ["CALLIND", null, ["register:0:8"]]
+ 00c3de5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3de5c ["INT_ADD", "register:40f0:8", ["const:c3de5c:8", "const:4:8"]]
+ 00c3de5c ["CALLIND", null, ["register:0:8"]]
- 00c3ddc0 bytes 00013fd6
+ 00c3de5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8526b5f5f5d570c7ca2d544fd184d362"></a>

### [`00c3e27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md) → [`00c3e318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md) FUN_00c3e318

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3e2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e2cc) · [`00c3e2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e2e8) · [`00c3e30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e30c)
- 新版 [`00c3e368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e368) · [`00c3e384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e384) · [`00c3e3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e3a8)

~~~diff
- 00c3e2cc ["INT_ADD", "register:40f0:8", ["const:c3e2cc:8", "const:4:8"]]
- 00c3e2cc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3e368 ["INT_ADD", "register:40f0:8", ["const:c3e368:8", "const:4:8"]]
+ 00c3e368 ["CALL", null, ["callee:00c5a170:8"]]
- 00c3e2cc bytes 756f0094
+ 00c3e368 bytes 826f0094
- 00c3e2e8 ["INT_ADD", "register:40f0:8", ["const:c3e2e8:8", "const:4:8"]]
- 00c3e2e8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c3e384 ["INT_ADD", "register:40f0:8", ["const:c3e384:8", "const:4:8"]]
+ 00c3e384 ["CALL", null, ["callee:00c580d0:8"]]
- 00c3e2e8 bytes 46670094
+ 00c3e384 bytes 53670094
- 00c3e30c ["INT_ADD", "register:40f0:8", ["const:c3e30c:8", "const:4:8"]]
- 00c3e30c ["CALL", null, ["callee:00c5b210:8"]]
+ 00c3e3a8 ["INT_ADD", "register:40f0:8", ["const:c3e3a8:8", "const:4:8"]]
+ 00c3e3a8 ["CALL", null, ["callee:00c5b210:8"]]
- 00c3e30c bytes 8d730094
+ 00c3e3a8 bytes 9a730094
~~~


<a id="compare-65cbd11a0bf75af40b432c3d92a67dec"></a>

### [`00c3e328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md) → [`00c3e3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md) FUN_00c3e3c4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3e35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e35c) · [`00c3e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e380) · [`00c3e3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e3cc)
- 新版 [`00c3e3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e3f8) · [`00c3e41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e41c) · [`00c3e468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e468)

~~~diff
- 00c3e35c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3e35c ["INT_ADD", "register:40f0:8", ["const:c3e35c:8", "const:4:8"]]
- 00c3e35c ["CALLIND", null, ["register:0:8"]]
+ 00c3e3f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3e3f8 ["INT_ADD", "register:40f0:8", ["const:c3e3f8:8", "const:4:8"]]
+ 00c3e3f8 ["CALLIND", null, ["register:0:8"]]
- 00c3e35c bytes 00013fd6
+ 00c3e3f8 bytes 00013fd6
- 00c3e380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3e380 ["INT_ADD", "register:40f0:8", ["const:c3e380:8", "const:4:8"]]
- 00c3e380 ["CALLIND", null, ["register:0:8"]]
+ 00c3e41c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3e41c ["INT_ADD", "register:40f0:8", ["const:c3e41c:8", "const:4:8"]]
+ 00c3e41c ["CALLIND", null, ["register:0:8"]]
- 00c3e380 bytes 00013fd6
+ 00c3e41c bytes 00013fd6
- 00c3e3cc ["INT_ADD", "register:40f0:8", ["const:c3e3cc:8", "const:4:8"]]
- 00c3e3cc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3e468 ["INT_ADD", "register:40f0:8", ["const:c3e468:8", "const:4:8"]]
+ 00c3e468 ["CALL", null, ["callee:00c5a170:8"]]
- 00c3e3cc bytes 356f0094
+ 00c3e468 bytes 426f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c976864033f10512e9cd3b2b735ff3"></a>

### [`00c3f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md) → [`00c3fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) FUN_00c3fa0c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9b8) · [`00c3f9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9cc) · [`00c3f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9d4)
- 新版 [`00c3fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa54) · [`00c3fa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa68) · [`00c3fa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa70)

~~~diff
- 00c3f9b8 ["INT_ADD", "register:40f0:8", ["const:c3f9b8:8", "const:4:8"]]
- 00c3f9b8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3fa54 ["INT_ADD", "register:40f0:8", ["const:c3fa54:8", "const:4:8"]]
+ 00c3fa54 ["CALL", null, ["callee:00c5a170:8"]]
- 00c3f9b8 bytes ba690094
+ 00c3fa54 bytes c7690094
- 00c3f9cc ["INT_ADD", "register:40f0:8", ["const:c3f9cc:8", "const:4:8"]]
- 00c3f9cc ["CALL", null, ["callee:00c5b210:8"]]
+ 00c3fa68 ["INT_ADD", "register:40f0:8", ["const:c3fa68:8", "const:4:8"]]
+ 00c3fa68 ["CALL", null, ["callee:00c5b210:8"]]
- 00c3f9cc bytes dd6d0094
+ 00c3fa68 bytes ea6d0094
- 00c3f9d4 ["INT_ADD", "register:40f0:8", ["const:c3f9d4:8", "const:4:8"]]
- 00c3f9d4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3fa70 ["INT_ADD", "register:40f0:8", ["const:c3fa70:8", "const:4:8"]]
+ 00c3fa70 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3f9d4 bytes 93690094
+ 00c3fa70 bytes a0690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be90ac67cabbbc68eae41a8c33b8f4c2"></a>

### [`00c3faf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3faf4.md) → [`00c3fb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fb90.md) FUN_00c3fb90

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3faf4.md#insn-00c3fb40)
- 新版 [`00c3fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fb90.md#insn-00c3fbdc)

~~~diff
- 00c3fb40 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
- 00c3fb40 ["CALLIND", null, ["register:0:8"]]
+ 00c3fbdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fbdc ["INT_ADD", "register:40f0:8", ["const:c3fbdc:8", "const:4:8"]]
+ 00c3fbdc ["CALLIND", null, ["register:0:8"]]
- 00c3fb40 bytes 20013fd6
+ 00c3fbdc bytes 20013fd6
~~~


<a id="compare-9aec6523b810e8e8b8d9e47a476a6432"></a>

### [`00c3fb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fb78.md) → [`00c3fc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc14.md) FUN_00c3fc14

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fb78.md#insn-00c3fbc4)
- 新版 [`00c3fc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc14.md#insn-00c3fc60)

~~~diff
- 00c3fbc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fbc4 ["INT_ADD", "register:40f0:8", ["const:c3fbc4:8", "const:4:8"]]
- 00c3fbc4 ["CALLIND", null, ["register:0:8"]]
+ 00c3fc60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fc60 ["INT_ADD", "register:40f0:8", ["const:c3fc60:8", "const:4:8"]]
+ 00c3fc60 ["CALLIND", null, ["register:0:8"]]
- 00c3fbc4 bytes 20013fd6
+ 00c3fc60 bytes 20013fd6
~~~


<a id="compare-243da58965fd549b4e31bb6895d81758"></a>

### [`00c3fbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fbfc.md) → [`00c3fc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc98.md) FUN_00c3fc98

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fbfc.md#insn-00c3fc48)
- 新版 [`00c3fce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc98.md#insn-00c3fce4)

~~~diff
- 00c3fc48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fc48 ["INT_ADD", "register:40f0:8", ["const:c3fc48:8", "const:4:8"]]
- 00c3fc48 ["CALLIND", null, ["register:0:8"]]
+ 00c3fce4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fce4 ["INT_ADD", "register:40f0:8", ["const:c3fce4:8", "const:4:8"]]
+ 00c3fce4 ["CALLIND", null, ["register:0:8"]]
- 00c3fc48 bytes 20013fd6
+ 00c3fce4 bytes 20013fd6
~~~


<a id="compare-d099ceb64f5409f3ce4a347494318aa5"></a>

### [`00c3fc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fc80.md) → [`00c3fd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd1c.md) FUN_00c3fd1c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fc80.md#insn-00c3fcb4)
- 新版 [`00c3fd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd1c.md#insn-00c3fd50)

~~~diff
- 00c3fcb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fcb4 ["INT_ADD", "register:40f0:8", ["const:c3fcb4:8", "const:4:8"]]
- 00c3fcb4 ["CALLIND", null, ["register:0:8"]]
+ 00c3fd50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fd50 ["INT_ADD", "register:40f0:8", ["const:c3fd50:8", "const:4:8"]]
+ 00c3fd50 ["CALLIND", null, ["register:0:8"]]
- 00c3fcb4 bytes 20013fd6
+ 00c3fd50 bytes 20013fd6
~~~


<a id="compare-252203d2b524c8cd06cd8cb8229e4408"></a>

### [`00c3fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fcd4.md) → [`00c3fd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd70.md) FUN_00c3fd70

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fcd4.md#insn-00c3fd04)
- 新版 [`00c3fda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd70.md#insn-00c3fda0)

~~~diff
- 00c3fd04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3fd04 ["INT_ADD", "register:40f0:8", ["const:c3fd04:8", "const:4:8"]]
- 00c3fd04 ["CALLIND", null, ["register:0:8"]]
+ 00c3fda0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3fda0 ["INT_ADD", "register:40f0:8", ["const:c3fda0:8", "const:4:8"]]
+ 00c3fda0 ["CALLIND", null, ["register:0:8"]]
- 00c3fd04 bytes 00013fd6
+ 00c3fda0 bytes 00013fd6
~~~


<a id="compare-e23979de7dc4f0bf8d1a36c18a31a466"></a>

### [`00c3fd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd24.md) → [`00c3fdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fdc0.md) FUN_00c3fdc0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd24.md#insn-00c3fd54)
- 新版 [`00c3fdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fdc0.md#insn-00c3fdf0)

~~~diff
- 00c3fd54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3fd54 ["INT_ADD", "register:40f0:8", ["const:c3fd54:8", "const:4:8"]]
- 00c3fd54 ["CALLIND", null, ["register:0:8"]]
+ 00c3fdf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3fdf0 ["INT_ADD", "register:40f0:8", ["const:c3fdf0:8", "const:4:8"]]
+ 00c3fdf0 ["CALLIND", null, ["register:0:8"]]
- 00c3fd54 bytes 00013fd6
+ 00c3fdf0 bytes 00013fd6
~~~


<a id="compare-9ca7d46c1dbdda695f5f3f598bf15081"></a>

### [`00c43dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md) → [`00c43e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md) FUN_00c43e48

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c43e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e20) · [`00c43e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e44) · [`00c43e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e80)
- 新版 [`00c43ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43ebc) · [`00c43ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43ee0) · [`00c43f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43f1c)

~~~diff
- 00c43e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c43e20 ["INT_ADD", "register:40f0:8", ["const:c43e20:8", "const:4:8"]]
- 00c43e20 ["CALLIND", null, ["register:0:8"]]
+ 00c43ebc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c43ebc ["INT_ADD", "register:40f0:8", ["const:c43ebc:8", "const:4:8"]]
+ 00c43ebc ["CALLIND", null, ["register:0:8"]]
- 00c43e20 bytes 00013fd6
+ 00c43ebc bytes 00013fd6
- 00c43e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c43e44 ["INT_ADD", "register:40f0:8", ["const:c43e44:8", "const:4:8"]]
- 00c43e44 ["CALLIND", null, ["register:0:8"]]
+ 00c43ee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c43ee0 ["INT_ADD", "register:40f0:8", ["const:c43ee0:8", "const:4:8"]]
+ 00c43ee0 ["CALLIND", null, ["register:0:8"]]
- 00c43e44 bytes 00013fd6
+ 00c43ee0 bytes 00013fd6
- 00c43e80 ["INT_ADD", "register:40f0:8", ["const:c43e80:8", "const:4:8"]]
- 00c43e80 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c43f1c ["INT_ADD", "register:40f0:8", ["const:c43f1c:8", "const:4:8"]]
+ 00c43f1c ["CALL", null, ["callee:00c5a170:8"]]
- 00c43e80 bytes 88580094
+ 00c43f1c bytes 95580094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57db5fb90b2974fbd784eba7aecd2f06"></a>

### [`00c44380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md) → [`00c4441c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md) FUN_00c4441c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c443d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c443d0) · [`00c443ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c443ec) · [`00c44428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c44428)
- 新版 [`00c4446c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c4446c) · [`00c44488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c44488) · [`00c444c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c444c4)

~~~diff
- 00c443d0 ["INT_ADD", "register:40f0:8", ["const:c443d0:8", "const:4:8"]]
- 00c443d0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4446c ["INT_ADD", "register:40f0:8", ["const:c4446c:8", "const:4:8"]]
+ 00c4446c ["CALL", null, ["callee:00c5a170:8"]]
- 00c443d0 bytes 34570094
+ 00c4446c bytes 41570094
- 00c443ec ["INT_ADD", "register:40f0:8", ["const:c443ec:8", "const:4:8"]]
- 00c443ec ["CALL", null, ["callee:00c580d0:8"]]
+ 00c44488 ["INT_ADD", "register:40f0:8", ["const:c44488:8", "const:4:8"]]
+ 00c44488 ["CALL", null, ["callee:00c580d0:8"]]
- 00c443ec bytes 054f0094
+ 00c44488 bytes 124f0094
- 00c44428 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44428 ["INT_ADD", "register:40f0:8", ["const:c44428:8", "const:4:8"]]
- 00c44428 ["CALLIND", null, ["register:0:8"]]
+ 00c444c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c444c4 ["INT_ADD", "register:40f0:8", ["const:c444c4:8", "const:4:8"]]
+ 00c444c4 ["CALLIND", null, ["register:0:8"]]
- 00c44428 bytes 00013fd6
+ 00c444c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d464461d6ccc088a8cb20e8a4565905e"></a>

### [`00c44568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md) → [`00c44604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md) FUN_00c44604

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c445b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c445b4) · [`00c445d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c445d8) · [`00c4461c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c4461c)
- 新版 [`00c44650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c44650) · [`00c44674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c44674) · [`00c446b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c446b8)

~~~diff
- 00c445b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c445b4 ["INT_ADD", "register:40f0:8", ["const:c445b4:8", "const:4:8"]]
- 00c445b4 ["CALLIND", null, ["register:0:8"]]
+ 00c44650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44650 ["INT_ADD", "register:40f0:8", ["const:c44650:8", "const:4:8"]]
+ 00c44650 ["CALLIND", null, ["register:0:8"]]
- 00c445b4 bytes 00013fd6
+ 00c44650 bytes 00013fd6
- 00c445d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c445d8 ["INT_ADD", "register:40f0:8", ["const:c445d8:8", "const:4:8"]]
- 00c445d8 ["CALLIND", null, ["register:0:8"]]
+ 00c44674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44674 ["INT_ADD", "register:40f0:8", ["const:c44674:8", "const:4:8"]]
+ 00c44674 ["CALLIND", null, ["register:0:8"]]
- 00c445d8 bytes 00013fd6
+ 00c44674 bytes 00013fd6
- 00c4461c ["INT_ADD", "register:40f0:8", ["const:c4461c:8", "const:4:8"]]
- 00c4461c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c446b8 ["INT_ADD", "register:40f0:8", ["const:c446b8:8", "const:4:8"]]
+ 00c446b8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4461c bytes a1560094
+ 00c446b8 bytes ae560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc795deaf0c1f7e6ddb035fec6c204a"></a>

### [`00c44750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md) → [`00c447ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md) FUN_00c447ec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c44798) · [`00c447bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c447bc) · [`00c447f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c447f8)
- 新版 [`00c44834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44834) · [`00c44858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44858) · [`00c44894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44894)

~~~diff
- 00c44798 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44798 ["INT_ADD", "register:40f0:8", ["const:c44798:8", "const:4:8"]]
- 00c44798 ["CALLIND", null, ["register:0:8"]]
+ 00c44834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44834 ["INT_ADD", "register:40f0:8", ["const:c44834:8", "const:4:8"]]
+ 00c44834 ["CALLIND", null, ["register:0:8"]]
- 00c44798 bytes 00013fd6
+ 00c44834 bytes 00013fd6
- 00c447bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c447bc ["INT_ADD", "register:40f0:8", ["const:c447bc:8", "const:4:8"]]
- 00c447bc ["CALLIND", null, ["register:0:8"]]
+ 00c44858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44858 ["INT_ADD", "register:40f0:8", ["const:c44858:8", "const:4:8"]]
+ 00c44858 ["CALLIND", null, ["register:0:8"]]
- 00c447bc bytes 00013fd6
+ 00c44858 bytes 00013fd6
- 00c447f8 ["INT_ADD", "register:40f0:8", ["const:c447f8:8", "const:4:8"]]
- 00c447f8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c44894 ["INT_ADD", "register:40f0:8", ["const:c44894:8", "const:4:8"]]
+ 00c44894 ["CALL", null, ["callee:00c5a170:8"]]
- 00c447f8 bytes 2a560094
+ 00c44894 bytes 37560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e303106857fcd2b31e09ed6158b888de"></a>

### [`00c44ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md) → [`00c44b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md) FUN_00c44b4c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44afc) · [`00c44b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44b20) · [`00c44b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44b64)
- 新版 [`00c44b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44b98) · [`00c44bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44bbc) · [`00c44c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44c00)

~~~diff
- 00c44afc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44afc ["INT_ADD", "register:40f0:8", ["const:c44afc:8", "const:4:8"]]
- 00c44afc ["CALLIND", null, ["register:0:8"]]
+ 00c44b98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44b98 ["INT_ADD", "register:40f0:8", ["const:c44b98:8", "const:4:8"]]
+ 00c44b98 ["CALLIND", null, ["register:0:8"]]
- 00c44afc bytes 00013fd6
+ 00c44b98 bytes 00013fd6
- 00c44b20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44b20 ["INT_ADD", "register:40f0:8", ["const:c44b20:8", "const:4:8"]]
- 00c44b20 ["CALLIND", null, ["register:0:8"]]
+ 00c44bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44bbc ["INT_ADD", "register:40f0:8", ["const:c44bbc:8", "const:4:8"]]
+ 00c44bbc ["CALLIND", null, ["register:0:8"]]
- 00c44b20 bytes 00013fd6
+ 00c44bbc bytes 00013fd6
- 00c44b64 ["INT_ADD", "register:40f0:8", ["const:c44b64:8", "const:4:8"]]
- 00c44b64 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c44c00 ["INT_ADD", "register:40f0:8", ["const:c44c00:8", "const:4:8"]]
+ 00c44c00 ["CALL", null, ["callee:00c5a170:8"]]
- 00c44b64 bytes 4f550094
+ 00c44c00 bytes 5c550094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8697b9e9168b091d0c97f4eb565cfe9e"></a>

### [`00c44de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md) → [`00c44e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md) FUN_00c44e80

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44e34) · [`00c44e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44e80) · [`00c44ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44ee0)
- 新版 [`00c44ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44ed0) · [`00c44f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44f1c) · [`00c44f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44f7c)

~~~diff
- 00c44e34 ["INT_ADD", "register:40f0:8", ["const:c44e34:8", "const:4:8"]]
- 00c44e34 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c44ed0 ["INT_ADD", "register:40f0:8", ["const:c44ed0:8", "const:4:8"]]
+ 00c44ed0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c44e34 bytes 9b540094
+ 00c44ed0 bytes a8540094
- 00c44e80 ["INT_ADD", "register:40f0:8", ["const:c44e80:8", "const:4:8"]]
- 00c44e80 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c44f1c ["INT_ADD", "register:40f0:8", ["const:c44f1c:8", "const:4:8"]]
+ 00c44f1c ["CALL", null, ["callee:00c5a170:8"]]
- 00c44e80 bytes 88540094
+ 00c44f1c bytes 95540094
- 00c44ee0 ["INT_ADD", "register:40f0:8", ["const:c44ee0:8", "const:4:8"]]
- 00c44ee0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c44f7c ["INT_ADD", "register:40f0:8", ["const:c44f7c:8", "const:4:8"]]
+ 00c44f7c ["CALL", null, ["callee:00c5a170:8"]]
- 00c44ee0 bytes 70540094
+ 00c44f7c bytes 7d540094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944345ec5ca3abc315d4912c46f58224"></a>

### [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) → [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) FUN_00c451e0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00c44de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md) [`00c4554c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md) [`00c45678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md) [`00c48a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md) [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 15件 [`00c44e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md) [`00c455e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md) [`00c45714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md) [`00c48b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c451d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c451d4) · [`00c45224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c45224) · [`00c45248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c45248)
- 新版 [`00c45270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c45270) · [`00c452c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c452c0) · [`00c452e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c452e4)

~~~diff
- 00c451d4 ["INT_ADD", "register:40f0:8", ["const:c451d4:8", "const:4:8"]]
- 00c451d4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c45270 ["INT_ADD", "register:40f0:8", ["const:c45270:8", "const:4:8"]]
+ 00c45270 ["CALL", null, ["callee:00c5a170:8"]]
- 00c451d4 bytes b3530094
+ 00c45270 bytes c0530094
- 00c45224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45224 ["INT_ADD", "register:40f0:8", ["const:c45224:8", "const:4:8"]]
- 00c45224 ["CALLIND", null, ["register:0:8"]]
+ 00c452c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c452c0 ["INT_ADD", "register:40f0:8", ["const:c452c0:8", "const:4:8"]]
+ 00c452c0 ["CALLIND", null, ["register:0:8"]]
- 00c45224 bytes 00013fd6
+ 00c452c0 bytes 00013fd6
- 00c45248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45248 ["INT_ADD", "register:40f0:8", ["const:c45248:8", "const:4:8"]]
- 00c45248 ["CALLIND", null, ["register:0:8"]]
+ 00c452e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c452e4 ["INT_ADD", "register:40f0:8", ["const:c452e4:8", "const:4:8"]]
+ 00c452e4 ["CALLIND", null, ["register:0:8"]]
- 00c45248 bytes 00013fd6
+ 00c452e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49119d4286a99d946e6581bf71bafb68"></a>

### [`00c45374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md) → [`00c45410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md) FUN_00c45410

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c453c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c453c0) · [`00c4540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c4540c) · [`00c45470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c45470)
- 新版 [`00c4545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c4545c) · [`00c454a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c454a8) · [`00c4550c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c4550c)

~~~diff
- 00c453c0 ["INT_ADD", "register:40f0:8", ["const:c453c0:8", "const:4:8"]]
- 00c453c0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4545c ["INT_ADD", "register:40f0:8", ["const:c4545c:8", "const:4:8"]]
+ 00c4545c ["CALL", null, ["callee:00c5a170:8"]]
- 00c453c0 bytes 38530094
+ 00c4545c bytes 45530094
- 00c4540c ["INT_ADD", "register:40f0:8", ["const:c4540c:8", "const:4:8"]]
- 00c4540c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c454a8 ["INT_ADD", "register:40f0:8", ["const:c454a8:8", "const:4:8"]]
+ 00c454a8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4540c bytes 25530094
+ 00c454a8 bytes 32530094
- 00c45470 ["INT_ADD", "register:40f0:8", ["const:c45470:8", "const:4:8"]]
- 00c45470 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4550c ["INT_ADD", "register:40f0:8", ["const:c4550c:8", "const:4:8"]]
+ 00c4550c ["CALL", null, ["callee:00c5a170:8"]]
- 00c45470 bytes 0c530094
+ 00c4550c bytes 19530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9994d76a8571d6124fbdbcba2e2df45"></a>

### [`00c4554c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md) → [`00c455e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md) FUN_00c455e8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c45578) · [`00c4559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c4559c) · [`00c455d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c455d4)
- 新版 [`00c45614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45614) · [`00c45638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45638) · [`00c45670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45670)

~~~diff
- 00c45578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45578 ["INT_ADD", "register:40f0:8", ["const:c45578:8", "const:4:8"]]
- 00c45578 ["CALLIND", null, ["register:0:8"]]
+ 00c45614 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45614 ["INT_ADD", "register:40f0:8", ["const:c45614:8", "const:4:8"]]
+ 00c45614 ["CALLIND", null, ["register:0:8"]]
- 00c45578 bytes 00013fd6
+ 00c45614 bytes 00013fd6
- 00c4559c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4559c ["INT_ADD", "register:40f0:8", ["const:c4559c:8", "const:4:8"]]
- 00c4559c ["CALLIND", null, ["register:0:8"]]
+ 00c45638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45638 ["INT_ADD", "register:40f0:8", ["const:c45638:8", "const:4:8"]]
+ 00c45638 ["CALLIND", null, ["register:0:8"]]
- 00c4559c bytes 00013fd6
+ 00c45638 bytes 00013fd6
- 00c455d4 ["INT_ADD", "register:40f0:8", ["const:c455d4:8", "const:4:8"]]
- 00c455d4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c45670 ["INT_ADD", "register:40f0:8", ["const:c45670:8", "const:4:8"]]
+ 00c45670 ["CALL", null, ["callee:00c5a170:8"]]
- 00c455d4 bytes b3520094
+ 00c45670 bytes c0520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a52cbca70da0d79c2c87605072edebfb"></a>

### [`00c45678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md) → [`00c45714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md) FUN_00c45714

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c456c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c456c8) · [`00c456fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c456fc) · [`00c45720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c45720)
- 新版 [`00c45764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c45764) · [`00c45798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c45798) · [`00c457bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c457bc)

~~~diff
- 00c456c8 ["INT_ADD", "register:40f0:8", ["const:c456c8:8", "const:4:8"]]
- 00c456c8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c45764 ["INT_ADD", "register:40f0:8", ["const:c45764:8", "const:4:8"]]
+ 00c45764 ["CALL", null, ["callee:00c5a170:8"]]
- 00c456c8 bytes 76520094
+ 00c45764 bytes 83520094
- 00c456fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c456fc ["INT_ADD", "register:40f0:8", ["const:c456fc:8", "const:4:8"]]
- 00c456fc ["CALLIND", null, ["register:0:8"]]
+ 00c45798 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45798 ["INT_ADD", "register:40f0:8", ["const:c45798:8", "const:4:8"]]
+ 00c45798 ["CALLIND", null, ["register:0:8"]]
- 00c456fc bytes 00013fd6
+ 00c45798 bytes 00013fd6
- 00c45720 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45720 ["INT_ADD", "register:40f0:8", ["const:c45720:8", "const:4:8"]]
- 00c45720 ["CALLIND", null, ["register:0:8"]]
+ 00c457bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c457bc ["INT_ADD", "register:40f0:8", ["const:c457bc:8", "const:4:8"]]
+ 00c457bc ["CALLIND", null, ["register:0:8"]]
- 00c45720 bytes 00013fd6
+ 00c457bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f81ea0478c3ff1ac8b8223e6a1bfdd8"></a>

### [`00c45858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md) → [`00c458f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md) FUN_00c458f4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c458a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c458a0) · [`00c458c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c458c4) · [`00c45900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c45900)
- 新版 [`00c4593c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c4593c) · [`00c45960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c45960) · [`00c4599c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c4599c)

~~~diff
- 00c458a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c458a0 ["INT_ADD", "register:40f0:8", ["const:c458a0:8", "const:4:8"]]
- 00c458a0 ["CALLIND", null, ["register:0:8"]]
+ 00c4593c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4593c ["INT_ADD", "register:40f0:8", ["const:c4593c:8", "const:4:8"]]
+ 00c4593c ["CALLIND", null, ["register:0:8"]]
- 00c458a0 bytes 00013fd6
+ 00c4593c bytes 00013fd6
- 00c458c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c458c4 ["INT_ADD", "register:40f0:8", ["const:c458c4:8", "const:4:8"]]
- 00c458c4 ["CALLIND", null, ["register:0:8"]]
+ 00c45960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45960 ["INT_ADD", "register:40f0:8", ["const:c45960:8", "const:4:8"]]
+ 00c45960 ["CALLIND", null, ["register:0:8"]]
- 00c458c4 bytes 00013fd6
+ 00c45960 bytes 00013fd6
- 00c45900 ["INT_ADD", "register:40f0:8", ["const:c45900:8", "const:4:8"]]
- 00c45900 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4599c ["INT_ADD", "register:40f0:8", ["const:c4599c:8", "const:4:8"]]
+ 00c4599c ["CALL", null, ["callee:00c5a170:8"]]
- 00c45900 bytes e8510094
+ 00c4599c bytes f5510094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70f3411b93ab8c9e2952b27e23fcf549"></a>

### [`00c45d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md) → [`00c45da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md) FUN_00c45da0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45d58) · [`00c45d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45d74) · [`00c45db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45db4)
- 新版 [`00c45df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45df4) · [`00c45e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45e10) · [`00c45e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45e50)

~~~diff
- 00c45d58 ["INT_ADD", "register:40f0:8", ["const:c45d58:8", "const:4:8"]]
- 00c45d58 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c45df4 ["INT_ADD", "register:40f0:8", ["const:c45df4:8", "const:4:8"]]
+ 00c45df4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c45d58 bytes d2500094
+ 00c45df4 bytes df500094
- 00c45d74 ["INT_ADD", "register:40f0:8", ["const:c45d74:8", "const:4:8"]]
- 00c45d74 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c45e10 ["INT_ADD", "register:40f0:8", ["const:c45e10:8", "const:4:8"]]
+ 00c45e10 ["CALL", null, ["callee:00c580d0:8"]]
- 00c45d74 bytes a3480094
+ 00c45e10 bytes b0480094
- 00c45db4 ["INT_ADD", "register:40f0:8", ["const:c45db4:8", "const:4:8"]]
- 00c45db4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c45e50 ["INT_ADD", "register:40f0:8", ["const:c45e50:8", "const:4:8"]]
+ 00c45e50 ["CALL", null, ["callee:00c5a170:8"]]
- 00c45db4 bytes bb500094
+ 00c45e50 bytes c8500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619f76db6fc04708d24c11b5f68eca73"></a>

### [`00c46048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md) → [`00c460e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md) FUN_00c460e4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4609c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c4609c) · [`00c460b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c460b8) · [`00c460fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c460fc)
- 新版 [`00c46138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46138) · [`00c46154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46154) · [`00c46198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46198)

~~~diff
- 00c4609c ["INT_ADD", "register:40f0:8", ["const:c4609c:8", "const:4:8"]]
- 00c4609c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c46138 ["INT_ADD", "register:40f0:8", ["const:c46138:8", "const:4:8"]]
+ 00c46138 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4609c bytes 01500094
+ 00c46138 bytes 0e500094
- 00c460b8 ["INT_ADD", "register:40f0:8", ["const:c460b8:8", "const:4:8"]]
- 00c460b8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c46154 ["INT_ADD", "register:40f0:8", ["const:c46154:8", "const:4:8"]]
+ 00c46154 ["CALL", null, ["callee:00c580d0:8"]]
- 00c460b8 bytes d2470094
+ 00c46154 bytes df470094
- 00c460fc ["INT_ADD", "register:40f0:8", ["const:c460fc:8", "const:4:8"]]
- 00c460fc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c46198 ["INT_ADD", "register:40f0:8", ["const:c46198:8", "const:4:8"]]
+ 00c46198 ["CALL", null, ["callee:00c5a170:8"]]
- 00c460fc bytes e94f0094
+ 00c46198 bytes f64f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d7ed646c9811a0ae4a2421284587d5"></a>

### [`00c46dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md) → [`00c46e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md) FUN_00c46e88

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c46e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46e4c) · [`00c46ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46ea4) · [`00c46ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46ec0)
- 新版 [`00c46ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46ee8) · [`00c46f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46f40) · [`00c46f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46f5c)

~~~diff
- 00c46e4c ["INT_ADD", "register:40f0:8", ["const:c46e4c:8", "const:4:8"]]
- 00c46e4c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c46ee8 ["INT_ADD", "register:40f0:8", ["const:c46ee8:8", "const:4:8"]]
+ 00c46ee8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c46e4c bytes 954c0094
+ 00c46ee8 bytes a24c0094
- 00c46ea4 ["INT_ADD", "register:40f0:8", ["const:c46ea4:8", "const:4:8"]]
- 00c46ea4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c46f40 ["INT_ADD", "register:40f0:8", ["const:c46f40:8", "const:4:8"]]
+ 00c46f40 ["CALL", null, ["callee:00c5a170:8"]]
- 00c46ea4 bytes 7f4c0094
+ 00c46f40 bytes 8c4c0094
- 00c46ec0 ["INT_ADD", "register:40f0:8", ["const:c46ec0:8", "const:4:8"]]
- 00c46ec0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c46f5c ["INT_ADD", "register:40f0:8", ["const:c46f5c:8", "const:4:8"]]
+ 00c46f5c ["CALL", null, ["callee:00c580d0:8"]]
- 00c46ec0 bytes 50440094
+ 00c46f5c bytes 5d440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54367543f6bcdc6321950befda5bb06b"></a>

### [`00c47720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md) → [`00c477bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md) FUN_00c477bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c47764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c47764) · [`00c477a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c477a0) · [`00c477c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c477c4)
- 新版 [`00c47800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c47800) · [`00c4783c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c4783c) · [`00c47860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c47860)

~~~diff
- 00c47764 ["INT_ADD", "register:40f0:8", ["const:c47764:8", "const:4:8"]]
- 00c47764 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c47800 ["INT_ADD", "register:40f0:8", ["const:c47800:8", "const:4:8"]]
+ 00c47800 ["CALL", null, ["callee:00c5a170:8"]]
- 00c47764 bytes 4f4a0094
+ 00c47800 bytes 5c4a0094
- 00c477a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c477a0 ["INT_ADD", "register:40f0:8", ["const:c477a0:8", "const:4:8"]]
- 00c477a0 ["CALLIND", null, ["register:0:8"]]
+ 00c4783c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4783c ["INT_ADD", "register:40f0:8", ["const:c4783c:8", "const:4:8"]]
+ 00c4783c ["CALLIND", null, ["register:0:8"]]
- 00c477a0 bytes 00013fd6
+ 00c4783c bytes 00013fd6
- 00c477c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c477c4 ["INT_ADD", "register:40f0:8", ["const:c477c4:8", "const:4:8"]]
- 00c477c4 ["CALLIND", null, ["register:0:8"]]
+ 00c47860 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c47860 ["INT_ADD", "register:40f0:8", ["const:c47860:8", "const:4:8"]]
+ 00c47860 ["CALLIND", null, ["register:0:8"]]
- 00c477c4 bytes 00013fd6
+ 00c47860 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fb3c5d768db51bda3f926b221543275"></a>

### [`00c482fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md) → [`00c48398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md) FUN_00c48398

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c48344) · [`00c483ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c483ac) · [`00c483c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c483c8)
- 新版 [`00c483e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c483e0) · [`00c48448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c48448) · [`00c48464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c48464)

~~~diff
- 00c48344 ["INT_ADD", "register:40f0:8", ["const:c48344:8", "const:4:8"]]
- 00c48344 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c483e0 ["INT_ADD", "register:40f0:8", ["const:c483e0:8", "const:4:8"]]
+ 00c483e0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c48344 bytes 57470094
+ 00c483e0 bytes 64470094
- 00c483ac ["INT_ADD", "register:40f0:8", ["const:c483ac:8", "const:4:8"]]
- 00c483ac ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48448 ["INT_ADD", "register:40f0:8", ["const:c48448:8", "const:4:8"]]
+ 00c48448 ["CALL", null, ["callee:00c5a170:8"]]
- 00c483ac bytes 3d470094
+ 00c48448 bytes 4a470094
- 00c483c8 ["INT_ADD", "register:40f0:8", ["const:c483c8:8", "const:4:8"]]
- 00c483c8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c48464 ["INT_ADD", "register:40f0:8", ["const:c48464:8", "const:4:8"]]
+ 00c48464 ["CALL", null, ["callee:00c580d0:8"]]
- 00c483c8 bytes 0e3f0094
+ 00c48464 bytes 1b3f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715f6605313453ade4a2aaf93d9f66a2"></a>

### [`00c484ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md) → [`00c48588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md) FUN_00c48588

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c48558) · [`00c485b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c485b0) · [`00c48610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c48610)
- 新版 [`00c485f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c485f4) · [`00c4864c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c4864c) · [`00c486ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c486ac)

~~~diff
- 00c48558 ["INT_ADD", "register:40f0:8", ["const:c48558:8", "const:4:8"]]
- 00c48558 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c485f4 ["INT_ADD", "register:40f0:8", ["const:c485f4:8", "const:4:8"]]
+ 00c485f4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c48558 bytes d2460094
+ 00c485f4 bytes df460094
- 00c485b0 ["INT_ADD", "register:40f0:8", ["const:c485b0:8", "const:4:8"]]
- 00c485b0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4864c ["INT_ADD", "register:40f0:8", ["const:c4864c:8", "const:4:8"]]
+ 00c4864c ["CALL", null, ["callee:00c5a170:8"]]
- 00c485b0 bytes bc460094
+ 00c4864c bytes c9460094
- 00c48610 ["INT_ADD", "register:40f0:8", ["const:c48610:8", "const:4:8"]]
- 00c48610 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c486ac ["INT_ADD", "register:40f0:8", ["const:c486ac:8", "const:4:8"]]
+ 00c486ac ["CALL", null, ["callee:00c5a170:8"]]
- 00c48610 bytes a4460094
+ 00c486ac bytes b1460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced5ece7bdd68fc3eea16a2771f29e64"></a>

### [`00c487a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c487a8.md) → [`00c48844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48844.md) FUN_00c48844

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c487cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c487a8.md#insn-00c487cc)
- 新版 [`00c48868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48844.md#insn-00c48868)

~~~diff
- 00c487cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c487cc ["INT_ADD", "register:40f0:8", ["const:c487cc:8", "const:4:8"]]
- 00c487cc ["CALLIND", null, ["register:0:8"]]
+ 00c48868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48868 ["INT_ADD", "register:40f0:8", ["const:c48868:8", "const:4:8"]]
+ 00c48868 ["CALLIND", null, ["register:0:8"]]
- 00c487cc bytes 00013fd6
+ 00c48868 bytes 00013fd6
~~~


<a id="compare-0ad2b124dc66ceaeaba43551fed8a501"></a>

### [`00c48818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md) → [`00c488b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md) FUN_00c488b4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c4883c) · [`00c48860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c48860) · [`00c4888c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c4888c)
- 新版 [`00c488d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c488d8) · [`00c488fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c488fc) · [`00c48928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c48928)

~~~diff
- 00c4883c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4883c ["INT_ADD", "register:40f0:8", ["const:c4883c:8", "const:4:8"]]
- 00c4883c ["CALLIND", null, ["register:0:8"]]
+ 00c488d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c488d8 ["INT_ADD", "register:40f0:8", ["const:c488d8:8", "const:4:8"]]
+ 00c488d8 ["CALLIND", null, ["register:0:8"]]
- 00c4883c bytes 00013fd6
+ 00c488d8 bytes 00013fd6
- 00c48860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48860 ["INT_ADD", "register:40f0:8", ["const:c48860:8", "const:4:8"]]
- 00c48860 ["CALLIND", null, ["register:0:8"]]
+ 00c488fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c488fc ["INT_ADD", "register:40f0:8", ["const:c488fc:8", "const:4:8"]]
+ 00c488fc ["CALLIND", null, ["register:0:8"]]
- 00c48860 bytes 00013fd6
+ 00c488fc bytes 00013fd6
- 00c4888c ["INT_ADD", "register:40f0:8", ["const:c4888c:8", "const:4:8"]]
- 00c4888c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48928 ["INT_ADD", "register:40f0:8", ["const:c48928:8", "const:4:8"]]
+ 00c48928 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4888c bytes 05460094
+ 00c48928 bytes 12460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11284d55afd353a16b7163c0c4fcae0b"></a>

### [`00c48934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md) → [`00c489d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md) FUN_00c489d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c48958) · [`00c4897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c4897c) · [`00c489b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c489b8)
- 新版 [`00c489f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c489f4) · [`00c48a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c48a18) · [`00c48a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c48a54)

~~~diff
- 00c48958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48958 ["INT_ADD", "register:40f0:8", ["const:c48958:8", "const:4:8"]]
- 00c48958 ["CALLIND", null, ["register:0:8"]]
+ 00c489f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c489f4 ["INT_ADD", "register:40f0:8", ["const:c489f4:8", "const:4:8"]]
+ 00c489f4 ["CALLIND", null, ["register:0:8"]]
- 00c48958 bytes 00013fd6
+ 00c489f4 bytes 00013fd6
- 00c4897c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4897c ["INT_ADD", "register:40f0:8", ["const:c4897c:8", "const:4:8"]]
- 00c4897c ["CALLIND", null, ["register:0:8"]]
+ 00c48a18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48a18 ["INT_ADD", "register:40f0:8", ["const:c48a18:8", "const:4:8"]]
+ 00c48a18 ["CALLIND", null, ["register:0:8"]]
- 00c4897c bytes 00013fd6
+ 00c48a18 bytes 00013fd6
- 00c489b8 ["INT_ADD", "register:40f0:8", ["const:c489b8:8", "const:4:8"]]
- 00c489b8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48a54 ["INT_ADD", "register:40f0:8", ["const:c48a54:8", "const:4:8"]]
+ 00c48a54 ["CALL", null, ["callee:00c5a170:8"]]
- 00c489b8 bytes ba450094
+ 00c48a54 bytes c7450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6925e0ab2ba83813cadaf5ca233d6d87"></a>

### [`00c489f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c489f0.md) → [`00c48a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md) FUN_00c48a8c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c489f0.md#insn-00c48a1c) · [`00c48a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c489f0.md#insn-00c48a40)
- 新版 [`00c48ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md#insn-00c48ab8) · [`00c48adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md#insn-00c48adc)

~~~diff
- 00c48a1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48a1c ["INT_ADD", "register:40f0:8", ["const:c48a1c:8", "const:4:8"]]
- 00c48a1c ["CALLIND", null, ["register:0:8"]]
+ 00c48ab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48ab8 ["INT_ADD", "register:40f0:8", ["const:c48ab8:8", "const:4:8"]]
+ 00c48ab8 ["CALLIND", null, ["register:0:8"]]
- 00c48a1c bytes 00013fd6
+ 00c48ab8 bytes 00013fd6
- 00c48a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48a40 ["INT_ADD", "register:40f0:8", ["const:c48a40:8", "const:4:8"]]
- 00c48a40 ["CALLIND", null, ["register:0:8"]]
+ 00c48adc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48adc ["INT_ADD", "register:40f0:8", ["const:c48adc:8", "const:4:8"]]
+ 00c48adc ["CALLIND", null, ["register:0:8"]]
- 00c48a40 bytes 00013fd6
+ 00c48adc bytes 00013fd6
~~~


<a id="compare-2cd8041cf804ff4d08ac278bbdf5df77"></a>

### [`00c48cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48cb4.md) → [`00c48d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md) FUN_00c48d50

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48cb4.md#insn-00c48cd4) · [`00c48d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48cb4.md#insn-00c48d00) · [`00c48d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48cb4.md#insn-00c48d40)
- 新版 [`00c48d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48d70) · [`00c48d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48d9c) · [`00c48ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48ddc)

~~~diff
- 00c48cd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48cd4 ["INT_ADD", "register:40f0:8", ["const:c48cd4:8", "const:4:8"]]
- 00c48cd4 ["CALLIND", null, ["register:0:8"]]
+ 00c48d70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48d70 ["INT_ADD", "register:40f0:8", ["const:c48d70:8", "const:4:8"]]
+ 00c48d70 ["CALLIND", null, ["register:0:8"]]
- 00c48cd4 bytes 00013fd6
+ 00c48d70 bytes 00013fd6
- 00c48d00 ["INT_ADD", "register:40f0:8", ["const:c48d00:8", "const:4:8"]]
- 00c48d00 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48d9c ["INT_ADD", "register:40f0:8", ["const:c48d9c:8", "const:4:8"]]
+ 00c48d9c ["CALL", null, ["callee:00c5a170:8"]]
- 00c48d00 bytes e8440094
+ 00c48d9c bytes f5440094
- 00c48d40 ["INT_ADD", "register:40f0:8", ["const:c48d40:8", "const:4:8"]]
- 00c48d40 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c48ddc ["INT_ADD", "register:40f0:8", ["const:c48ddc:8", "const:4:8"]]
+ 00c48ddc ["CALL", null, ["callee:00c5b210:8"]]
- 00c48d40 bytes 00490094
+ 00c48ddc bytes 0d490094
~~~


<a id="compare-168a3efaf36b5b827507cf2f4550c42d"></a>

### [`00c48d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d60.md) → [`00c48dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md) FUN_00c48dfc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d60.md#insn-00c48da8) · [`00c48e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d60.md#insn-00c48e18) · [`00c48e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d60.md#insn-00c48e34)
- 新版 [`00c48e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48e44) · [`00c48eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48eb4) · [`00c48ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48ed0)

~~~diff
- 00c48da8 ["INT_ADD", "register:40f0:8", ["const:c48da8:8", "const:4:8"]]
- 00c48da8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48e44 ["INT_ADD", "register:40f0:8", ["const:c48e44:8", "const:4:8"]]
+ 00c48e44 ["CALL", null, ["callee:00c5a170:8"]]
- 00c48da8 bytes be440094
+ 00c48e44 bytes cb440094
- 00c48e18 ["INT_ADD", "register:40f0:8", ["const:c48e18:8", "const:4:8"]]
- 00c48e18 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48eb4 ["INT_ADD", "register:40f0:8", ["const:c48eb4:8", "const:4:8"]]
+ 00c48eb4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c48e18 bytes a2440094
+ 00c48eb4 bytes af440094
- 00c48e34 ["INT_ADD", "register:40f0:8", ["const:c48e34:8", "const:4:8"]]
- 00c48e34 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c48ed0 ["INT_ADD", "register:40f0:8", ["const:c48ed0:8", "const:4:8"]]
+ 00c48ed0 ["CALL", null, ["callee:00c580d0:8"]]
- 00c48e34 bytes 733c0094
+ 00c48ed0 bytes 803c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b38a6af8f4061285bd7811e3db80cbef"></a>

### [`00c49220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49220.md) → [`00c492bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md) FUN_00c492bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49220.md#insn-00c49264) · [`00c492a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49220.md#insn-00c492a0) · [`00c492d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49220.md#insn-00c492d0)
- 新版 [`00c49300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c49300) · [`00c4933c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c4933c) · [`00c4936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c4936c)

~~~diff
- 00c49264 ["INT_ADD", "register:40f0:8", ["const:c49264:8", "const:4:8"]]
- 00c49264 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c49300 ["INT_ADD", "register:40f0:8", ["const:c49300:8", "const:4:8"]]
+ 00c49300 ["CALL", null, ["callee:00c5a170:8"]]
- 00c49264 bytes 8f430094
+ 00c49300 bytes 9c430094
- 00c492a0 ["INT_ADD", "register:40f0:8", ["const:c492a0:8", "const:4:8"]]
- 00c492a0 ["CALL", null, ["callee:00c48f5c:8"]]
+ 00c4933c ["INT_ADD", "register:40f0:8", ["const:c4933c:8", "const:4:8"]]
+ 00c4933c ["CALL", null, ["callee:00c48f5c:8"]]
- 00c492a0 bytes 08ffff97
+ 00c4933c bytes 08ffff97
- 00c492d0 ["INT_ADD", "register:40f0:8", ["const:c492d0:8", "const:4:8"]]
- 00c492d0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4936c ["INT_ADD", "register:40f0:8", ["const:c4936c:8", "const:4:8"]]
+ 00c4936c ["CALL", null, ["callee:00c5a170:8"]]
- 00c492d0 bytes 74430094
+ 00c4936c bytes 81430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c8df224c8c76fa3ba9bf7a8b709dad"></a>

### [`00c49324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49324.md) → [`00c493c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md) FUN_00c493c0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49324.md#insn-00c49374) · [`00c493a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49324.md#insn-00c493a8) · [`00c493cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49324.md#insn-00c493cc)
- 新版 [`00c49410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49410) · [`00c49444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49444) · [`00c49468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49468)

~~~diff
- 00c49374 ["INT_ADD", "register:40f0:8", ["const:c49374:8", "const:4:8"]]
- 00c49374 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c49410 ["INT_ADD", "register:40f0:8", ["const:c49410:8", "const:4:8"]]
+ 00c49410 ["CALL", null, ["callee:00c5a170:8"]]
- 00c49374 bytes 4b430094
+ 00c49410 bytes 58430094
- 00c493a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c493a8 ["INT_ADD", "register:40f0:8", ["const:c493a8:8", "const:4:8"]]
- 00c493a8 ["CALLIND", null, ["register:0:8"]]
+ 00c49444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49444 ["INT_ADD", "register:40f0:8", ["const:c49444:8", "const:4:8"]]
+ 00c49444 ["CALLIND", null, ["register:0:8"]]
- 00c493a8 bytes 00013fd6
+ 00c49444 bytes 00013fd6
- 00c493cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c493cc ["INT_ADD", "register:40f0:8", ["const:c493cc:8", "const:4:8"]]
- 00c493cc ["CALLIND", null, ["register:0:8"]]
+ 00c49468 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49468 ["INT_ADD", "register:40f0:8", ["const:c49468:8", "const:4:8"]]
+ 00c49468 ["CALLIND", null, ["register:0:8"]]
- 00c493cc bytes 00013fd6
+ 00c49468 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db3c132a47ac458130ae0a52c6f369e"></a>

### [`00c495fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c495fc.md) → [`00c49698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md) FUN_00c49698

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c495fc.md#insn-00c49644) · [`00c496a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c495fc.md#insn-00c496a0) · [`00c496bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c495fc.md#insn-00c496bc)
- 新版 [`00c496e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c496e0) · [`00c4973c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c4973c) · [`00c49758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c49758)

~~~diff
- 00c49644 ["INT_ADD", "register:40f0:8", ["const:c49644:8", "const:4:8"]]
- 00c49644 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c496e0 ["INT_ADD", "register:40f0:8", ["const:c496e0:8", "const:4:8"]]
+ 00c496e0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c49644 bytes 97420094
+ 00c496e0 bytes a4420094
- 00c496a0 ["INT_ADD", "register:40f0:8", ["const:c496a0:8", "const:4:8"]]
- 00c496a0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4973c ["INT_ADD", "register:40f0:8", ["const:c4973c:8", "const:4:8"]]
+ 00c4973c ["CALL", null, ["callee:00c5a170:8"]]
- 00c496a0 bytes 80420094
+ 00c4973c bytes 8d420094
- 00c496bc ["INT_ADD", "register:40f0:8", ["const:c496bc:8", "const:4:8"]]
- 00c496bc ["CALL", null, ["callee:00c580d0:8"]]
+ 00c49758 ["INT_ADD", "register:40f0:8", ["const:c49758:8", "const:4:8"]]
+ 00c49758 ["CALL", null, ["callee:00c580d0:8"]]
- 00c496bc bytes 513a0094
+ 00c49758 bytes 5e3a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c9eead384c325ece5439146a83c5781"></a>

### [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) → [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) FUN_00c49f10

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c496f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md) [`00c4b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md) · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 2件 [`00c4978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) [`00c4b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md#insn-00c49eb8) · [`00c49edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md#insn-00c49edc) · [`00c49f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md#insn-00c49f38)
- 新版 [`00c49f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49f54) · [`00c49f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49f78) · [`00c49fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49fd4)

~~~diff
- 00c49eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49eb8 ["INT_ADD", "register:40f0:8", ["const:c49eb8:8", "const:4:8"]]
- 00c49eb8 ["CALLIND", null, ["register:0:8"]]
+ 00c49f54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49f54 ["INT_ADD", "register:40f0:8", ["const:c49f54:8", "const:4:8"]]
+ 00c49f54 ["CALLIND", null, ["register:0:8"]]
- 00c49eb8 bytes 00013fd6
+ 00c49f54 bytes 00013fd6
- 00c49edc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49edc ["INT_ADD", "register:40f0:8", ["const:c49edc:8", "const:4:8"]]
- 00c49edc ["CALLIND", null, ["register:0:8"]]
+ 00c49f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49f78 ["INT_ADD", "register:40f0:8", ["const:c49f78:8", "const:4:8"]]
+ 00c49f78 ["CALLIND", null, ["register:0:8"]]
- 00c49edc bytes 00013fd6
+ 00c49f78 bytes 00013fd6
- 00c49f38 ["INT_ADD", "register:40f0:8", ["const:c49f38:8", "const:4:8"]]
- 00c49f38 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c49fd4 ["INT_ADD", "register:40f0:8", ["const:c49fd4:8", "const:4:8"]]
+ 00c49fd4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c49f38 bytes 5a400094
+ 00c49fd4 bytes 67400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53f156e1db61857d5fd9bf6f9875f2e2"></a>

### [`00c4a034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a034.md) → [`00c4a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md) FUN_00c4a0d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a034.md#insn-00c4a080) · [`00c4a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a034.md#insn-00c4a0b4) · [`00c4a0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a034.md#insn-00c4a0d8)
- 新版 [`00c4a11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a11c) · [`00c4a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a150) · [`00c4a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a174)

~~~diff
- 00c4a080 ["INT_ADD", "register:40f0:8", ["const:c4a080:8", "const:4:8"]]
- 00c4a080 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a11c ["INT_ADD", "register:40f0:8", ["const:c4a11c:8", "const:4:8"]]
+ 00c4a11c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a080 bytes 08400094
+ 00c4a11c bytes 15400094
- 00c4a0b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a0b4 ["INT_ADD", "register:40f0:8", ["const:c4a0b4:8", "const:4:8"]]
- 00c4a0b4 ["CALLIND", null, ["register:0:8"]]
+ 00c4a150 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a150 ["INT_ADD", "register:40f0:8", ["const:c4a150:8", "const:4:8"]]
+ 00c4a150 ["CALLIND", null, ["register:0:8"]]
- 00c4a0b4 bytes 00013fd6
+ 00c4a150 bytes 00013fd6
- 00c4a0d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a0d8 ["INT_ADD", "register:40f0:8", ["const:c4a0d8:8", "const:4:8"]]
- 00c4a0d8 ["CALLIND", null, ["register:0:8"]]
+ 00c4a174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a174 ["INT_ADD", "register:40f0:8", ["const:c4a174:8", "const:4:8"]]
+ 00c4a174 ["CALLIND", null, ["register:0:8"]]
- 00c4a0d8 bytes 00013fd6
+ 00c4a174 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7467b604fe94ece0dbb7fa1a27f8a12d"></a>

### [`00c4a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a280.md) → [`00c4a31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md) FUN_00c4a31c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a280.md#insn-00c4a2c8) · [`00c4a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a280.md#insn-00c4a300) · [`00c4a324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a280.md#insn-00c4a324)
- 新版 [`00c4a364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a364) · [`00c4a39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a39c) · [`00c4a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a3c0)

~~~diff
- 00c4a2c8 ["INT_ADD", "register:40f0:8", ["const:c4a2c8:8", "const:4:8"]]
- 00c4a2c8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a364 ["INT_ADD", "register:40f0:8", ["const:c4a364:8", "const:4:8"]]
+ 00c4a364 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a2c8 bytes 763f0094
+ 00c4a364 bytes 833f0094
- 00c4a300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a300 ["INT_ADD", "register:40f0:8", ["const:c4a300:8", "const:4:8"]]
- 00c4a300 ["CALLIND", null, ["register:0:8"]]
+ 00c4a39c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a39c ["INT_ADD", "register:40f0:8", ["const:c4a39c:8", "const:4:8"]]
+ 00c4a39c ["CALLIND", null, ["register:0:8"]]
- 00c4a300 bytes 00013fd6
+ 00c4a39c bytes 00013fd6
- 00c4a324 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a324 ["INT_ADD", "register:40f0:8", ["const:c4a324:8", "const:4:8"]]
- 00c4a324 ["CALLIND", null, ["register:0:8"]]
+ 00c4a3c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a3c0 ["INT_ADD", "register:40f0:8", ["const:c4a3c0:8", "const:4:8"]]
+ 00c4a3c0 ["CALLIND", null, ["register:0:8"]]
- 00c4a324 bytes 00013fd6
+ 00c4a3c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cf3b19de33d68399973801a2024c3e5"></a>

### [`00c4a4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a4ec.md) → [`00c4a588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md) FUN_00c4a588

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a4ec.md#insn-00c4a520) · [`00c4a544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a4ec.md#insn-00c4a544) · [`00c4a570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a4ec.md#insn-00c4a570)
- 新版 [`00c4a5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a5bc) · [`00c4a5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a5e0) · [`00c4a60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a60c)

~~~diff
- 00c4a520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a520 ["INT_ADD", "register:40f0:8", ["const:c4a520:8", "const:4:8"]]
- 00c4a520 ["CALLIND", null, ["register:0:8"]]
+ 00c4a5bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a5bc ["INT_ADD", "register:40f0:8", ["const:c4a5bc:8", "const:4:8"]]
+ 00c4a5bc ["CALLIND", null, ["register:0:8"]]
- 00c4a520 bytes 00013fd6
+ 00c4a5bc bytes 00013fd6
- 00c4a544 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a544 ["INT_ADD", "register:40f0:8", ["const:c4a544:8", "const:4:8"]]
- 00c4a544 ["CALLIND", null, ["register:0:8"]]
+ 00c4a5e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a5e0 ["INT_ADD", "register:40f0:8", ["const:c4a5e0:8", "const:4:8"]]
+ 00c4a5e0 ["CALLIND", null, ["register:0:8"]]
- 00c4a544 bytes 00013fd6
+ 00c4a5e0 bytes 00013fd6
- 00c4a570 ["INT_ADD", "register:40f0:8", ["const:c4a570:8", "const:4:8"]]
- 00c4a570 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a60c ["INT_ADD", "register:40f0:8", ["const:c4a60c:8", "const:4:8"]]
+ 00c4a60c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a570 bytes cc3e0094
+ 00c4a60c bytes d93e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a70314d005740deca58bb58a0fb7b42"></a>

### [`00c4a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a608.md) → [`00c4a6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md) FUN_00c4a6a4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a608.md#insn-00c4a658) · [`00c4a68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a608.md#insn-00c4a68c) · [`00c4a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a608.md#insn-00c4a6b0)
- 新版 [`00c4a6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a6f4) · [`00c4a728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a728) · [`00c4a74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a74c)

~~~diff
- 00c4a658 ["INT_ADD", "register:40f0:8", ["const:c4a658:8", "const:4:8"]]
- 00c4a658 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a6f4 ["INT_ADD", "register:40f0:8", ["const:c4a6f4:8", "const:4:8"]]
+ 00c4a6f4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a658 bytes 923e0094
+ 00c4a6f4 bytes 9f3e0094
- 00c4a68c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a68c ["INT_ADD", "register:40f0:8", ["const:c4a68c:8", "const:4:8"]]
- 00c4a68c ["CALLIND", null, ["register:0:8"]]
+ 00c4a728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a728 ["INT_ADD", "register:40f0:8", ["const:c4a728:8", "const:4:8"]]
+ 00c4a728 ["CALLIND", null, ["register:0:8"]]
- 00c4a68c bytes 00013fd6
+ 00c4a728 bytes 00013fd6
- 00c4a6b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a6b0 ["INT_ADD", "register:40f0:8", ["const:c4a6b0:8", "const:4:8"]]
- 00c4a6b0 ["CALLIND", null, ["register:0:8"]]
+ 00c4a74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a74c ["INT_ADD", "register:40f0:8", ["const:c4a74c:8", "const:4:8"]]
+ 00c4a74c ["CALLIND", null, ["register:0:8"]]
- 00c4a6b0 bytes 00013fd6
+ 00c4a74c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9078735e091c7d97b034ee08a4226664"></a>

### [`00c4ad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ad4c.md) → [`00c4ade8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md) FUN_00c4ade8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ad94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ad4c.md#insn-00c4ad94) · [`00c4adf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ad4c.md#insn-00c4adf8) · [`00c4ae4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ad4c.md#insn-00c4ae4c)
- 新版 [`00c4ae30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4ae30) · [`00c4ae94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4ae94) · [`00c4aee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4aee8)

~~~diff
- 00c4ad94 ["INT_ADD", "register:40f0:8", ["const:c4ad94:8", "const:4:8"]]
- 00c4ad94 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ae30 ["INT_ADD", "register:40f0:8", ["const:c4ae30:8", "const:4:8"]]
+ 00c4ae30 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ad94 bytes c33c0094
+ 00c4ae30 bytes d03c0094
- 00c4adf8 ["INT_ADD", "register:40f0:8", ["const:c4adf8:8", "const:4:8"]]
- 00c4adf8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ae94 ["INT_ADD", "register:40f0:8", ["const:c4ae94:8", "const:4:8"]]
+ 00c4ae94 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4adf8 bytes aa3c0094
+ 00c4ae94 bytes b73c0094
- 00c4ae4c ["INT_ADD", "register:40f0:8", ["const:c4ae4c:8", "const:4:8"]]
- 00c4ae4c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4aee8 ["INT_ADD", "register:40f0:8", ["const:c4aee8:8", "const:4:8"]]
+ 00c4aee8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ae4c bytes 953c0094
+ 00c4aee8 bytes a23c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44554712741b58371c7f9b430ce6b929"></a>

### [`00c4b548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b548.md) → [`00c4b5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md) FUN_00c4b5e4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b548.md#insn-00c4b58c) · [`00c4b5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b548.md#insn-00c4b5d8) · [`00c4b61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b548.md#insn-00c4b61c)
- 新版 [`00c4b628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b628) · [`00c4b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b674) · [`00c4b6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b6b8)

~~~diff
- 00c4b58c ["INT_ADD", "register:40f0:8", ["const:c4b58c:8", "const:4:8"]]
- 00c4b58c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4b628 ["INT_ADD", "register:40f0:8", ["const:c4b628:8", "const:4:8"]]
+ 00c4b628 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4b58c bytes c53a0094
+ 00c4b628 bytes d23a0094
- 00c4b5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b5d8 ["INT_ADD", "register:40f0:8", ["const:c4b5d8:8", "const:4:8"]]
- 00c4b5d8 ["CALLIND", null, ["register:0:8"]]
+ 00c4b674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b674 ["INT_ADD", "register:40f0:8", ["const:c4b674:8", "const:4:8"]]
+ 00c4b674 ["CALLIND", null, ["register:0:8"]]
- 00c4b5d8 bytes 00013fd6
+ 00c4b674 bytes 00013fd6
- 00c4b61c ["INT_ADD", "register:40f0:8", ["const:c4b61c:8", "const:4:8"]]
- 00c4b61c ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4b6b8 ["INT_ADD", "register:40f0:8", ["const:c4b6b8:8", "const:4:8"]]
+ 00c4b6b8 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4b61c bytes c93e0094
+ 00c4b6b8 bytes d63e0094
~~~


<a id="compare-b04a26207d4004fedcecb2f4e54bac01"></a>

### [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) → [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) FUN_00c4b6c4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) · 呼出先 8件 [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 8件 [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md#insn-00c4b664) · [`00c4b698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md#insn-00c4b698) · [`00c4b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md#insn-00c4b6a8)
- 新版 [`00c4b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b700) · [`00c4b734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b734) · [`00c4b744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b744)

~~~diff
- 00c4b664 ["INT_ADD", "register:40f0:8", ["const:c4b664:8", "const:4:8"]]
- 00c4b664 ["CALL", null, ["callee:00c3ebd8:8"]]
+ 00c4b700 ["INT_ADD", "register:40f0:8", ["const:c4b700:8", "const:4:8"]]
+ 00c4b700 ["CALL", null, ["callee:00c3ebd8:8"]]
- 00c4b664 bytes 36cdff97
+ 00c4b700 bytes 36cdff97
- 00c4b698 ["INT_ADD", "register:40f0:8", ["const:c4b698:8", "const:4:8"]]
- 00c4b698 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4b734 ["INT_ADD", "register:40f0:8", ["const:c4b734:8", "const:4:8"]]
+ 00c4b734 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4b698 bytes 823a0094
+ 00c4b734 bytes 8f3a0094
- 00c4b6a8 ["INT_ADD", "register:40f0:8", ["const:c4b6a8:8", "const:4:8"]]
- 00c4b6a8 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4b744 ["INT_ADD", "register:40f0:8", ["const:c4b744:8", "const:4:8"]]
+ 00c4b744 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4b6a8 bytes a63e0094
+ 00c4b744 bytes b33e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0873b05ff4b3c0a80ae895bf093964d9"></a>

### [`00c4ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4ba3c.md) → [`00c4bad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md) FUN_00c4bad8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ba68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4ba3c.md#insn-00c4ba68) · [`00c4ba8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4ba3c.md#insn-00c4ba8c) · [`00c4bab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4ba3c.md#insn-00c4bab8)
- 新版 [`00c4bb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb04) · [`00c4bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb28) · [`00c4bb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb54)

~~~diff
- 00c4ba68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ba68 ["INT_ADD", "register:40f0:8", ["const:c4ba68:8", "const:4:8"]]
- 00c4ba68 ["CALLIND", null, ["register:0:8"]]
+ 00c4bb04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4bb04 ["INT_ADD", "register:40f0:8", ["const:c4bb04:8", "const:4:8"]]
+ 00c4bb04 ["CALLIND", null, ["register:0:8"]]
- 00c4ba68 bytes 00013fd6
+ 00c4bb04 bytes 00013fd6
- 00c4ba8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ba8c ["INT_ADD", "register:40f0:8", ["const:c4ba8c:8", "const:4:8"]]
- 00c4ba8c ["CALLIND", null, ["register:0:8"]]
+ 00c4bb28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4bb28 ["INT_ADD", "register:40f0:8", ["const:c4bb28:8", "const:4:8"]]
+ 00c4bb28 ["CALLIND", null, ["register:0:8"]]
- 00c4ba8c bytes 00013fd6
+ 00c4bb28 bytes 00013fd6
- 00c4bab8 ["INT_ADD", "register:40f0:8", ["const:c4bab8:8", "const:4:8"]]
- 00c4bab8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4bb54 ["INT_ADD", "register:40f0:8", ["const:c4bb54:8", "const:4:8"]]
+ 00c4bb54 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4bab8 bytes 7a390094
+ 00c4bb54 bytes 87390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9f69236ada7c286e4b9d51dd30e9ed7"></a>

### [`00c4bedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bedc.md) → [`00c4bf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md) FUN_00c4bf78

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4bf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bedc.md#insn-00c4bf24) · [`00c4bf6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bedc.md#insn-00c4bf6c)
- 新版 [`00c4bfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md#insn-00c4bfc0) · [`00c4c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md#insn-00c4c008)

~~~diff
- 00c4bf24 ["INT_ADD", "register:40f0:8", ["const:c4bf24:8", "const:4:8"]]
- 00c4bf24 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4bfc0 ["INT_ADD", "register:40f0:8", ["const:c4bfc0:8", "const:4:8"]]
+ 00c4bfc0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4bf24 bytes 5f380094
+ 00c4bfc0 bytes 6c380094
- 00c4bf6c ["INT_ADD", "register:40f0:8", ["const:c4bf6c:8", "const:4:8"]]
- 00c4bf6c ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4c008 ["INT_ADD", "register:40f0:8", ["const:c4c008:8", "const:4:8"]]
+ 00c4c008 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4bf6c bytes 753c0094
+ 00c4c008 bytes 823c0094
~~~


<a id="compare-4a9bb448617eb059e7cba39f474910de"></a>

### [`00c4c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c144.md) → [`00c4c1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md) FUN_00c4c1e0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c144.md#insn-00c4c188) · [`00c4c1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c144.md#insn-00c4c1c4) · [`00c4c208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c144.md#insn-00c4c208)
- 新版 [`00c4c224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c224) · [`00c4c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c260) · [`00c4c2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c2a4)

~~~diff
- 00c4c188 ["INT_ADD", "register:40f0:8", ["const:c4c188:8", "const:4:8"]]
- 00c4c188 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c224 ["INT_ADD", "register:40f0:8", ["const:c4c224:8", "const:4:8"]]
+ 00c4c224 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c188 bytes c6370094
+ 00c4c224 bytes d3370094
- 00c4c1c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c1c4 ["INT_ADD", "register:40f0:8", ["const:c4c1c4:8", "const:4:8"]]
- 00c4c1c4 ["CALLIND", null, ["register:0:8"]]
+ 00c4c260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c260 ["INT_ADD", "register:40f0:8", ["const:c4c260:8", "const:4:8"]]
+ 00c4c260 ["CALLIND", null, ["register:0:8"]]
- 00c4c1c4 bytes 00013fd6
+ 00c4c260 bytes 00013fd6
- 00c4c208 ["INT_ADD", "register:40f0:8", ["const:c4c208:8", "const:4:8"]]
- 00c4c208 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4c2a4 ["INT_ADD", "register:40f0:8", ["const:c4c2a4:8", "const:4:8"]]
+ 00c4c2a4 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4c208 bytes ce3b0094
+ 00c4c2a4 bytes db3b0094
~~~


<a id="compare-0087929f2437ad270e5781506560f7e8"></a>

### [`00c4c840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c840.md) → [`00c4c8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8dc.md) FUN_00c4c8dc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c4c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c228.md) · 呼出先 1件 [`00c3e15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e15c.md)
- 新版 呼出元 1件 [`00c4c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) · 呼出先 1件 [`00c3e1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e1f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c840.md#insn-00c4c85c)
- 新版 [`00c4c8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8dc.md#insn-00c4c8f8)

~~~diff
- 00c4c85c ["INT_ADD", "register:40f0:8", ["const:c4c85c:8", "const:4:8"]]
- 00c4c85c ["CALL", null, ["callee:00c3e1f8:8"]]
+ 00c4c8f8 ["INT_ADD", "register:40f0:8", ["const:c4c8f8:8", "const:4:8"]]
+ 00c4c8f8 ["CALL", null, ["callee:00c3e1f8:8"]]
- 00c4c85c bytes 40c6ff97
+ 00c4c8f8 bytes 40c6ff97
~~~


<a id="compare-496619aba23328494fa4529f49fe3177"></a>

### [`00c4c8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c8a8.md) → [`00c4c944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md) FUN_00c4c944

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c8a8.md#insn-00c4c8d0) · [`00c4c8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c8a8.md#insn-00c4c8fc) · [`00c4c964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c8a8.md#insn-00c4c964)
- 新版 [`00c4c96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4c96c) · [`00c4c998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4c998) · [`00c4ca00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4ca00)

~~~diff
- 00c4c8d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c8d0 ["INT_ADD", "register:40f0:8", ["const:c4c8d0:8", "const:4:8"]]
- 00c4c8d0 ["CALLIND", null, ["register:0:8"]]
+ 00c4c96c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c96c ["INT_ADD", "register:40f0:8", ["const:c4c96c:8", "const:4:8"]]
+ 00c4c96c ["CALLIND", null, ["register:0:8"]]
- 00c4c8d0 bytes 00013fd6
+ 00c4c96c bytes 00013fd6
- 00c4c8fc ["INT_ADD", "register:40f0:8", ["const:c4c8fc:8", "const:4:8"]]
- 00c4c8fc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c998 ["INT_ADD", "register:40f0:8", ["const:c4c998:8", "const:4:8"]]
+ 00c4c998 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c8fc bytes e9350094
+ 00c4c998 bytes f6350094
- 00c4c964 ["INT_ADD", "register:40f0:8", ["const:c4c964:8", "const:4:8"]]
- 00c4c964 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ca00 ["INT_ADD", "register:40f0:8", ["const:c4ca00:8", "const:4:8"]]
+ 00c4ca00 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c964 bytes cf350094
+ 00c4ca00 bytes dc350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e866a6e1a1c274ea5d8913c4cd5e00ee"></a>

### [`00c4ca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ca18.md) → [`00c4cab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md) FUN_00c4cab4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ca64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ca18.md#insn-00c4ca64) · [`00c4ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ca18.md#insn-00c4ca8c) · [`00c4cac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ca18.md#insn-00c4cac4)
- 新版 [`00c4cb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb00) · [`00c4cb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb28) · [`00c4cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb60)

~~~diff
- 00c4ca64 ["INT_ADD", "register:40f0:8", ["const:c4ca64:8", "const:4:8"]]
- 00c4ca64 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4cb00 ["INT_ADD", "register:40f0:8", ["const:c4cb00:8", "const:4:8"]]
+ 00c4cb00 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ca64 bytes 8f350094
+ 00c4cb00 bytes 9c350094
- 00c4ca8c ["INT_ADD", "register:40f0:8", ["const:c4ca8c:8", "const:4:8"]]
- 00c4ca8c ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4cb28 ["INT_ADD", "register:40f0:8", ["const:c4cb28:8", "const:4:8"]]
+ 00c4cb28 ["CALL", null, ["callee:00c451e0:8"]]
- 00c4ca8c bytes aee1ff97
+ 00c4cb28 bytes aee1ff97
- 00c4cac4 ["INT_ADD", "register:40f0:8", ["const:c4cac4:8", "const:4:8"]]
- 00c4cac4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4cb60 ["INT_ADD", "register:40f0:8", ["const:c4cb60:8", "const:4:8"]]
+ 00c4cb60 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4cac4 bytes 77350094
+ 00c4cb60 bytes 84350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81975305527865dbac588495f64c4c0d"></a>

### [`00c4cbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cbc4.md) → [`00c4cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md) FUN_00c4cc60

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cbc4.md#insn-00c4cc14) · [`00c4cc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cbc4.md#insn-00c4cc48) · [`00c4cc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cbc4.md#insn-00c4cc80)
- 新版 [`00c4ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4ccb0) · [`00c4cce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4cce4) · [`00c4cd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4cd1c)

~~~diff
- 00c4cc14 ["INT_ADD", "register:40f0:8", ["const:c4cc14:8", "const:4:8"]]
- 00c4cc14 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ccb0 ["INT_ADD", "register:40f0:8", ["const:c4ccb0:8", "const:4:8"]]
+ 00c4ccb0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4cc14 bytes 23350094
+ 00c4ccb0 bytes 30350094
- 00c4cc48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cc48 ["INT_ADD", "register:40f0:8", ["const:c4cc48:8", "const:4:8"]]
- 00c4cc48 ["CALLIND", null, ["register:0:8"]]
+ 00c4cce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cce4 ["INT_ADD", "register:40f0:8", ["const:c4cce4:8", "const:4:8"]]
+ 00c4cce4 ["CALLIND", null, ["register:0:8"]]
- 00c4cc48 bytes 00013fd6
+ 00c4cce4 bytes 00013fd6
- 00c4cc80 ["INT_ADD", "register:40f0:8", ["const:c4cc80:8", "const:4:8"]]
- 00c4cc80 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4cd1c ["INT_ADD", "register:40f0:8", ["const:c4cd1c:8", "const:4:8"]]
+ 00c4cd1c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4cc80 bytes 08350094
+ 00c4cd1c bytes 15350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cea9eaf174aab2c4a0b9977adc396ce5"></a>

### [`00c4ccd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ccd0.md) → [`00c4cd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md) FUN_00c4cd6c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ccd0.md#insn-00c4ccfc) · [`00c4cd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ccd0.md#insn-00c4cd20) · [`00c4cd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ccd0.md#insn-00c4cd4c)
- 新版 [`00c4cd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cd98) · [`00c4cdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cdbc) · [`00c4cde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cde8)

~~~diff
- 00c4ccfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ccfc ["INT_ADD", "register:40f0:8", ["const:c4ccfc:8", "const:4:8"]]
- 00c4ccfc ["CALLIND", null, ["register:0:8"]]
+ 00c4cd98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cd98 ["INT_ADD", "register:40f0:8", ["const:c4cd98:8", "const:4:8"]]
+ 00c4cd98 ["CALLIND", null, ["register:0:8"]]
- 00c4ccfc bytes 00013fd6
+ 00c4cd98 bytes 00013fd6
- 00c4cd20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cd20 ["INT_ADD", "register:40f0:8", ["const:c4cd20:8", "const:4:8"]]
- 00c4cd20 ["CALLIND", null, ["register:0:8"]]
+ 00c4cdbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cdbc ["INT_ADD", "register:40f0:8", ["const:c4cdbc:8", "const:4:8"]]
+ 00c4cdbc ["CALLIND", null, ["register:0:8"]]
- 00c4cd20 bytes 00013fd6
+ 00c4cdbc bytes 00013fd6
- 00c4cd4c ["INT_ADD", "register:40f0:8", ["const:c4cd4c:8", "const:4:8"]]
- 00c4cd4c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4cde8 ["INT_ADD", "register:40f0:8", ["const:c4cde8:8", "const:4:8"]]
+ 00c4cde8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4cd4c bytes d5340094
+ 00c4cde8 bytes e2340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d7e1b71af743535e016c3280cc3f9f0"></a>

### [`00c4cf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md) → [`00c4cfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md) FUN_00c4cfbc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md#insn-00c4cf4c) · [`00c4cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md#insn-00c4cf70) · [`00c4cf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md#insn-00c4cf9c)
- 新版 [`00c4cfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4cfe8) · [`00c4d00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4d00c) · [`00c4d038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4d038)

~~~diff
- 00c4cf4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cf4c ["INT_ADD", "register:40f0:8", ["const:c4cf4c:8", "const:4:8"]]
- 00c4cf4c ["CALLIND", null, ["register:0:8"]]
+ 00c4cfe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cfe8 ["INT_ADD", "register:40f0:8", ["const:c4cfe8:8", "const:4:8"]]
+ 00c4cfe8 ["CALLIND", null, ["register:0:8"]]
- 00c4cf4c bytes 00013fd6
+ 00c4cfe8 bytes 00013fd6
- 00c4cf70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cf70 ["INT_ADD", "register:40f0:8", ["const:c4cf70:8", "const:4:8"]]
- 00c4cf70 ["CALLIND", null, ["register:0:8"]]
+ 00c4d00c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d00c ["INT_ADD", "register:40f0:8", ["const:c4d00c:8", "const:4:8"]]
+ 00c4d00c ["CALLIND", null, ["register:0:8"]]
- 00c4cf70 bytes 00013fd6
+ 00c4d00c bytes 00013fd6
- 00c4cf9c ["INT_ADD", "register:40f0:8", ["const:c4cf9c:8", "const:4:8"]]
- 00c4cf9c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d038 ["INT_ADD", "register:40f0:8", ["const:c4d038:8", "const:4:8"]]
+ 00c4d038 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4cf9c bytes 41340094
+ 00c4d038 bytes 4e340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580454ed0b403702c0df36d409b764d4"></a>

### [`00c4d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d244.md) → [`00c4d2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md) FUN_00c4d2e0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d244.md#insn-00c4d270) · [`00c4d294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d244.md#insn-00c4d294) · [`00c4d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d244.md#insn-00c4d2c0)
- 新版 [`00c4d30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d30c) · [`00c4d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d330) · [`00c4d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d35c)

~~~diff
- 00c4d270 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
- 00c4d270 ["CALLIND", null, ["register:0:8"]]
+ 00c4d30c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d30c ["INT_ADD", "register:40f0:8", ["const:c4d30c:8", "const:4:8"]]
+ 00c4d30c ["CALLIND", null, ["register:0:8"]]
- 00c4d270 bytes 00013fd6
+ 00c4d30c bytes 00013fd6
- 00c4d294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d294 ["INT_ADD", "register:40f0:8", ["const:c4d294:8", "const:4:8"]]
- 00c4d294 ["CALLIND", null, ["register:0:8"]]
+ 00c4d330 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d330 ["INT_ADD", "register:40f0:8", ["const:c4d330:8", "const:4:8"]]
+ 00c4d330 ["CALLIND", null, ["register:0:8"]]
- 00c4d294 bytes 00013fd6
+ 00c4d330 bytes 00013fd6
- 00c4d2c0 ["INT_ADD", "register:40f0:8", ["const:c4d2c0:8", "const:4:8"]]
- 00c4d2c0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d35c ["INT_ADD", "register:40f0:8", ["const:c4d35c:8", "const:4:8"]]
+ 00c4d35c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4d2c0 bytes 78330094
+ 00c4d35c bytes 85330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07ad437f4d80c6445ee85d8aebafbca"></a>

### [`00c4d580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d580.md) → [`00c4d61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md) FUN_00c4d61c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d580.md#insn-00c4d5cc) · [`00c4d5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d580.md#insn-00c4d5f8) · [`00c4d624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d580.md#insn-00c4d624)
- 新版 [`00c4d668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d668) · [`00c4d694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d694) · [`00c4d6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d6c0)

~~~diff
- 00c4d5cc ["INT_ADD", "register:40f0:8", ["const:c4d5cc:8", "const:4:8"]]
- 00c4d5cc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d668 ["INT_ADD", "register:40f0:8", ["const:c4d668:8", "const:4:8"]]
+ 00c4d668 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4d5cc bytes b5320094
+ 00c4d668 bytes c2320094
- 00c4d5f8 ["INT_ADD", "register:40f0:8", ["const:c4d5f8:8", "const:4:8"]]
- 00c4d5f8 ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4d694 ["INT_ADD", "register:40f0:8", ["const:c4d694:8", "const:4:8"]]
+ 00c4d694 ["CALL", null, ["callee:00c451e0:8"]]
- 00c4d5f8 bytes d3deff97
+ 00c4d694 bytes d3deff97
- 00c4d624 ["INT_ADD", "register:40f0:8", ["const:c4d624:8", "const:4:8"]]
- 00c4d624 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d6c0 ["INT_ADD", "register:40f0:8", ["const:c4d6c0:8", "const:4:8"]]
+ 00c4d6c0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4d624 bytes 9f320094
+ 00c4d6c0 bytes ac320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eee8d6373b1259ab445b5ba67aee68a"></a>

### [`00c4d678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d678.md) → [`00c4d714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md) FUN_00c4d714

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d678.md#insn-00c4d6a4) · [`00c4d6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d678.md#insn-00c4d6c8) · [`00c4d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d678.md#insn-00c4d6e0)
- 新版 [`00c4d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d740) · [`00c4d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d764) · [`00c4d77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d77c)

~~~diff
- 00c4d6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d6a4 ["INT_ADD", "register:40f0:8", ["const:c4d6a4:8", "const:4:8"]]
- 00c4d6a4 ["CALLIND", null, ["register:0:8"]]
+ 00c4d740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d740 ["INT_ADD", "register:40f0:8", ["const:c4d740:8", "const:4:8"]]
+ 00c4d740 ["CALLIND", null, ["register:0:8"]]
- 00c4d6a4 bytes 00013fd6
+ 00c4d740 bytes 00013fd6
- 00c4d6c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d6c8 ["INT_ADD", "register:40f0:8", ["const:c4d6c8:8", "const:4:8"]]
- 00c4d6c8 ["CALLIND", null, ["register:0:8"]]
+ 00c4d764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d764 ["INT_ADD", "register:40f0:8", ["const:c4d764:8", "const:4:8"]]
+ 00c4d764 ["CALLIND", null, ["register:0:8"]]
- 00c4d6c8 bytes 00013fd6
+ 00c4d764 bytes 00013fd6
- 00c4d6e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d6e0 ["INT_ADD", "register:40f0:8", ["const:c4d6e0:8", "const:4:8"]]
- 00c4d6e0 ["CALLIND", null, ["register:0:8"]]
+ 00c4d77c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d77c ["INT_ADD", "register:40f0:8", ["const:c4d77c:8", "const:4:8"]]
+ 00c4d77c ["CALLIND", null, ["register:0:8"]]
- 00c4d6e0 bytes 00013fd6
+ 00c4d77c bytes 00013fd6
~~~


<a id="compare-fc133d02f817f124912e54fbbbf71baa"></a>

### [`00c4d8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d8c4.md) → [`00c4d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md) FUN_00c4d960

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d8c4.md#insn-00c4d908) · [`00c4d954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d8c4.md#insn-00c4d954) · [`00c4d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d8c4.md#insn-00c4d998)
- 新版 [`00c4d9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4d9a4) · [`00c4d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4d9f0) · [`00c4da34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4da34)

~~~diff
- 00c4d908 ["INT_ADD", "register:40f0:8", ["const:c4d908:8", "const:4:8"]]
- 00c4d908 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d9a4 ["INT_ADD", "register:40f0:8", ["const:c4d9a4:8", "const:4:8"]]
+ 00c4d9a4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4d908 bytes e6310094
+ 00c4d9a4 bytes f3310094
- 00c4d954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d954 ["INT_ADD", "register:40f0:8", ["const:c4d954:8", "const:4:8"]]
- 00c4d954 ["CALLIND", null, ["register:0:8"]]
+ 00c4d9f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d9f0 ["INT_ADD", "register:40f0:8", ["const:c4d9f0:8", "const:4:8"]]
+ 00c4d9f0 ["CALLIND", null, ["register:0:8"]]
- 00c4d954 bytes 00013fd6
+ 00c4d9f0 bytes 00013fd6
- 00c4d998 ["INT_ADD", "register:40f0:8", ["const:c4d998:8", "const:4:8"]]
- 00c4d998 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4da34 ["INT_ADD", "register:40f0:8", ["const:c4da34:8", "const:4:8"]]
+ 00c4da34 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4d998 bytes ea350094
+ 00c4da34 bytes f7350094
~~~


<a id="compare-cf7f15aa901fac2ca313899d048f79e3"></a>

### [`00c4d9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9bc.md) → [`00c4da58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md) FUN_00c4da58

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9bc.md#insn-00c4d9e8) · [`00c4da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9bc.md#insn-00c4da0c) · [`00c4da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9bc.md#insn-00c4da48)
- 新版 [`00c4da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4da84) · [`00c4daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4daa8) · [`00c4dae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4dae4)

~~~diff
- 00c4d9e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d9e8 ["INT_ADD", "register:40f0:8", ["const:c4d9e8:8", "const:4:8"]]
- 00c4d9e8 ["CALLIND", null, ["register:0:8"]]
+ 00c4da84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4da84 ["INT_ADD", "register:40f0:8", ["const:c4da84:8", "const:4:8"]]
+ 00c4da84 ["CALLIND", null, ["register:0:8"]]
- 00c4d9e8 bytes 00013fd6
+ 00c4da84 bytes 00013fd6
- 00c4da0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4da0c ["INT_ADD", "register:40f0:8", ["const:c4da0c:8", "const:4:8"]]
- 00c4da0c ["CALLIND", null, ["register:0:8"]]
+ 00c4daa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4daa8 ["INT_ADD", "register:40f0:8", ["const:c4daa8:8", "const:4:8"]]
+ 00c4daa8 ["CALLIND", null, ["register:0:8"]]
- 00c4da0c bytes 00013fd6
+ 00c4daa8 bytes 00013fd6
- 00c4da48 ["INT_ADD", "register:40f0:8", ["const:c4da48:8", "const:4:8"]]
- 00c4da48 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4dae4 ["INT_ADD", "register:40f0:8", ["const:c4dae4:8", "const:4:8"]]
+ 00c4dae4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4da48 bytes 96310094
+ 00c4dae4 bytes a3310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1c59125ea0502b98a9f12b4fe5cea8f"></a>

### [`00c4decc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4decc.md) → [`00c4df68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md) FUN_00c4df68

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4def8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4decc.md#insn-00c4def8) · [`00c4df1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4decc.md#insn-00c4df1c) · [`00c4df48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4decc.md#insn-00c4df48)
- 新版 [`00c4df94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4df94) · [`00c4dfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4dfb8) · [`00c4dfe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4dfe4)

~~~diff
- 00c4def8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4def8 ["INT_ADD", "register:40f0:8", ["const:c4def8:8", "const:4:8"]]
- 00c4def8 ["CALLIND", null, ["register:0:8"]]
+ 00c4df94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4df94 ["INT_ADD", "register:40f0:8", ["const:c4df94:8", "const:4:8"]]
+ 00c4df94 ["CALLIND", null, ["register:0:8"]]
- 00c4def8 bytes 00013fd6
+ 00c4df94 bytes 00013fd6
- 00c4df1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4df1c ["INT_ADD", "register:40f0:8", ["const:c4df1c:8", "const:4:8"]]
- 00c4df1c ["CALLIND", null, ["register:0:8"]]
+ 00c4dfb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4dfb8 ["INT_ADD", "register:40f0:8", ["const:c4dfb8:8", "const:4:8"]]
+ 00c4dfb8 ["CALLIND", null, ["register:0:8"]]
- 00c4df1c bytes 00013fd6
+ 00c4dfb8 bytes 00013fd6
- 00c4df48 ["INT_ADD", "register:40f0:8", ["const:c4df48:8", "const:4:8"]]
- 00c4df48 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4dfe4 ["INT_ADD", "register:40f0:8", ["const:c4dfe4:8", "const:4:8"]]
+ 00c4dfe4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4df48 bytes 56300094
+ 00c4dfe4 bytes 63300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f4eb9d6d8be4dc23bd78b3d2fab615"></a>

### [`00c4f53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f53c.md) → [`00c4f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md) FUN_00c4f5d8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f53c.md#insn-00c4f580) · [`00c4f5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f53c.md#insn-00c4f5e4) · [`00c4f628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f53c.md#insn-00c4f628)
- 新版 [`00c4f61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f61c) · [`00c4f680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f680) · [`00c4f6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f6c4)

~~~diff
- 00c4f580 ["INT_ADD", "register:40f0:8", ["const:c4f580:8", "const:4:8"]]
- 00c4f580 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4f61c ["INT_ADD", "register:40f0:8", ["const:c4f61c:8", "const:4:8"]]
+ 00c4f61c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f580 bytes c82a0094
+ 00c4f61c bytes d52a0094
- 00c4f5e4 ["INT_ADD", "register:40f0:8", ["const:c4f5e4:8", "const:4:8"]]
- 00c4f5e4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4f680 ["INT_ADD", "register:40f0:8", ["const:c4f680:8", "const:4:8"]]
+ 00c4f680 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f5e4 bytes af2a0094
+ 00c4f680 bytes bc2a0094
- 00c4f628 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f628 ["INT_ADD", "register:40f0:8", ["const:c4f628:8", "const:4:8"]]
- 00c4f628 ["CALLIND", null, ["register:0:8"]]
+ 00c4f6c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f6c4 ["INT_ADD", "register:40f0:8", ["const:c4f6c4:8", "const:4:8"]]
+ 00c4f6c4 ["CALLIND", null, ["register:0:8"]]
- 00c4f628 bytes 00013fd6
+ 00c4f6c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba1fa3c5d7fbfa8880daf44f718c06af"></a>

### [`00c4f7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f7b4.md) → [`00c4f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md) FUN_00c4f850

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f7b4.md#insn-00c4f7f8) · [`00c4f860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f7b4.md#insn-00c4f860) · [`00c4f888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f7b4.md#insn-00c4f888)
- 新版 [`00c4f894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f894) · [`00c4f8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f8fc) · [`00c4f924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f924)

~~~diff
- 00c4f7f8 ["INT_ADD", "register:40f0:8", ["const:c4f7f8:8", "const:4:8"]]
- 00c4f7f8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4f894 ["INT_ADD", "register:40f0:8", ["const:c4f894:8", "const:4:8"]]
+ 00c4f894 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f7f8 bytes 2a2a0094
+ 00c4f894 bytes 372a0094
- 00c4f860 ["INT_ADD", "register:40f0:8", ["const:c4f860:8", "const:4:8"]]
- 00c4f860 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4f8fc ["INT_ADD", "register:40f0:8", ["const:c4f8fc:8", "const:4:8"]]
+ 00c4f8fc ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f860 bytes 102a0094
+ 00c4f8fc bytes 1d2a0094
- 00c4f888 ["INT_ADD", "register:40f0:8", ["const:c4f888:8", "const:4:8"]]
- 00c4f888 ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4f924 ["INT_ADD", "register:40f0:8", ["const:c4f924:8", "const:4:8"]]
+ 00c4f924 ["CALL", null, ["callee:00c451e0:8"]]
- 00c4f888 bytes 2fd6ff97
+ 00c4f924 bytes 2fd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148bcb204a63077e28ed31f3bd5c2998"></a>

### [`00c4f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f91c.md) → [`00c4f9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md) FUN_00c4f9b8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f91c.md#insn-00c4f93c) · [`00c4f968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f91c.md#insn-00c4f968) · [`00c4f99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f91c.md#insn-00c4f99c)
- 新版 [`00c4f9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4f9d8) · [`00c4fa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4fa04) · [`00c4fa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4fa38)

~~~diff
- 00c4f93c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f93c ["INT_ADD", "register:40f0:8", ["const:c4f93c:8", "const:4:8"]]
- 00c4f93c ["CALLIND", null, ["register:0:8"]]
+ 00c4f9d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f9d8 ["INT_ADD", "register:40f0:8", ["const:c4f9d8:8", "const:4:8"]]
+ 00c4f9d8 ["CALLIND", null, ["register:0:8"]]
- 00c4f93c bytes 00013fd6
+ 00c4f9d8 bytes 00013fd6
- 00c4f968 ["INT_ADD", "register:40f0:8", ["const:c4f968:8", "const:4:8"]]
- 00c4f968 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4fa04 ["INT_ADD", "register:40f0:8", ["const:c4fa04:8", "const:4:8"]]
+ 00c4fa04 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f968 bytes ce290094
+ 00c4fa04 bytes db290094
- 00c4f99c ["INT_ADD", "register:40f0:8", ["const:c4f99c:8", "const:4:8"]]
- 00c4f99c ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4fa38 ["INT_ADD", "register:40f0:8", ["const:c4fa38:8", "const:4:8"]]
+ 00c4fa38 ["CALL", null, ["callee:00c5b210:8"]]
- 00c4f99c bytes e92d0094
+ 00c4fa38 bytes f62d0094
~~~


<a id="compare-1dc5a1d5f6c0042a60f002e1749b41a6"></a>

### [`00c4fd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4fd3c.md) → [`00c4fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md) FUN_00c4fdd8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4fd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4fd3c.md#insn-00c4fd68) · [`00c4fd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4fd3c.md#insn-00c4fd8c) · [`00c4fdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4fd3c.md#insn-00c4fdb8)
- 新版 [`00c4fe04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe04) · [`00c4fe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe28) · [`00c4fe54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe54)

~~~diff
- 00c4fd68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fd68 ["INT_ADD", "register:40f0:8", ["const:c4fd68:8", "const:4:8"]]
- 00c4fd68 ["CALLIND", null, ["register:0:8"]]
+ 00c4fe04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fe04 ["INT_ADD", "register:40f0:8", ["const:c4fe04:8", "const:4:8"]]
+ 00c4fe04 ["CALLIND", null, ["register:0:8"]]
- 00c4fd68 bytes 00013fd6
+ 00c4fe04 bytes 00013fd6
- 00c4fd8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fd8c ["INT_ADD", "register:40f0:8", ["const:c4fd8c:8", "const:4:8"]]
- 00c4fd8c ["CALLIND", null, ["register:0:8"]]
+ 00c4fe28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fe28 ["INT_ADD", "register:40f0:8", ["const:c4fe28:8", "const:4:8"]]
+ 00c4fe28 ["CALLIND", null, ["register:0:8"]]
- 00c4fd8c bytes 00013fd6
+ 00c4fe28 bytes 00013fd6
- 00c4fdb8 ["INT_ADD", "register:40f0:8", ["const:c4fdb8:8", "const:4:8"]]
- 00c4fdb8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4fe54 ["INT_ADD", "register:40f0:8", ["const:c4fe54:8", "const:4:8"]]
+ 00c4fe54 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4fdb8 bytes ba280094
+ 00c4fe54 bytes c7280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58f590b573b93bd491c91dbce4aa694"></a>

### [`00c4feb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4feb0.md) → [`00c4ff4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md) FUN_00c4ff4c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4fedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4feb0.md#insn-00c4fedc) · [`00c4ff00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4feb0.md#insn-00c4ff00) · [`00c4ff2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4feb0.md#insn-00c4ff2c)
- 新版 [`00c4ff78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ff78) · [`00c4ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ff9c) · [`00c4ffc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ffc8)

~~~diff
- 00c4fedc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fedc ["INT_ADD", "register:40f0:8", ["const:c4fedc:8", "const:4:8"]]
- 00c4fedc ["CALLIND", null, ["register:0:8"]]
+ 00c4ff78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ff78 ["INT_ADD", "register:40f0:8", ["const:c4ff78:8", "const:4:8"]]
+ 00c4ff78 ["CALLIND", null, ["register:0:8"]]
- 00c4fedc bytes 00013fd6
+ 00c4ff78 bytes 00013fd6
- 00c4ff00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ff00 ["INT_ADD", "register:40f0:8", ["const:c4ff00:8", "const:4:8"]]
- 00c4ff00 ["CALLIND", null, ["register:0:8"]]
+ 00c4ff9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ff9c ["INT_ADD", "register:40f0:8", ["const:c4ff9c:8", "const:4:8"]]
+ 00c4ff9c ["CALLIND", null, ["register:0:8"]]
- 00c4ff00 bytes 00013fd6
+ 00c4ff9c bytes 00013fd6
- 00c4ff2c ["INT_ADD", "register:40f0:8", ["const:c4ff2c:8", "const:4:8"]]
- 00c4ff2c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ffc8 ["INT_ADD", "register:40f0:8", ["const:c4ffc8:8", "const:4:8"]]
+ 00c4ffc8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ff2c bytes 5d280094
+ 00c4ffc8 bytes 6a280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2169d6691b79640d8ca570d6d1227704"></a>

### [`00c50248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50248.md) → [`00c502e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md) FUN_00c502e4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5029c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50248.md#insn-00c5029c) · [`00c502b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50248.md#insn-00c502b8) · [`00c502f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50248.md#insn-00c502f0)
- 新版 [`00c50338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c50338) · [`00c50354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c50354) · [`00c5038c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c5038c)

~~~diff
- 00c5029c ["INT_ADD", "register:40f0:8", ["const:c5029c:8", "const:4:8"]]
- 00c5029c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50338 ["INT_ADD", "register:40f0:8", ["const:c50338:8", "const:4:8"]]
+ 00c50338 ["CALL", null, ["callee:00c5a170:8"]]
- 00c5029c bytes 81270094
+ 00c50338 bytes 8e270094
- 00c502b8 ["INT_ADD", "register:40f0:8", ["const:c502b8:8", "const:4:8"]]
- 00c502b8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c50354 ["INT_ADD", "register:40f0:8", ["const:c50354:8", "const:4:8"]]
+ 00c50354 ["CALL", null, ["callee:00c580d0:8"]]
- 00c502b8 bytes 521f0094
+ 00c50354 bytes 5f1f0094
- 00c502f0 ["INT_ADD", "register:40f0:8", ["const:c502f0:8", "const:4:8"]]
- 00c502f0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c5038c ["INT_ADD", "register:40f0:8", ["const:c5038c:8", "const:4:8"]]
+ 00c5038c ["CALL", null, ["callee:00c5a170:8"]]
- 00c502f0 bytes 6c270094
+ 00c5038c bytes 79270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eff9e4f066cb4e9b6363fa94ddd470d8"></a>

### [`00c503bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c503bc.md) → [`00c50458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md) FUN_00c50458

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c503bc.md#insn-00c50400) · [`00c5044c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c503bc.md#insn-00c5044c) · [`00c50490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c503bc.md#insn-00c50490)
- 新版 [`00c5049c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c5049c) · [`00c504e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c504e8) · [`00c5052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c5052c)

~~~diff
- 00c50400 ["INT_ADD", "register:40f0:8", ["const:c50400:8", "const:4:8"]]
- 00c50400 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c5049c ["INT_ADD", "register:40f0:8", ["const:c5049c:8", "const:4:8"]]
+ 00c5049c ["CALL", null, ["callee:00c5a170:8"]]
- 00c50400 bytes 28270094
+ 00c5049c bytes 35270094
- 00c5044c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5044c ["INT_ADD", "register:40f0:8", ["const:c5044c:8", "const:4:8"]]
- 00c5044c ["CALLIND", null, ["register:0:8"]]
+ 00c504e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c504e8 ["INT_ADD", "register:40f0:8", ["const:c504e8:8", "const:4:8"]]
+ 00c504e8 ["CALLIND", null, ["register:0:8"]]
- 00c5044c bytes 00013fd6
+ 00c504e8 bytes 00013fd6
- 00c50490 ["INT_ADD", "register:40f0:8", ["const:c50490:8", "const:4:8"]]
- 00c50490 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c5052c ["INT_ADD", "register:40f0:8", ["const:c5052c:8", "const:4:8"]]
+ 00c5052c ["CALL", null, ["callee:00c5b210:8"]]
- 00c50490 bytes 2c2b0094
+ 00c5052c bytes 392b0094
~~~


<a id="compare-cd7254cdbc39f3503d7bb80d060ff9a8"></a>

### [`00c50784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50784.md) → [`00c50820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md) FUN_00c50820

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c507ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50784.md#insn-00c507ac) · [`00c507e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50784.md#insn-00c507e4) · [`00c50800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50784.md#insn-00c50800)
- 新版 [`00c50848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c50848) · [`00c50880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c50880) · [`00c5089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c5089c)

~~~diff
- 00c507ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00c507ac ["INT_ADD", "register:40f0:8", ["const:c507ac:8", "const:4:8"]]
- 00c507ac ["CALLIND", null, ["register:0:8"]]
+ 00c50848 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50848 ["INT_ADD", "register:40f0:8", ["const:c50848:8", "const:4:8"]]
+ 00c50848 ["CALLIND", null, ["register:0:8"]]
- 00c507ac bytes 00013fd6
+ 00c50848 bytes 00013fd6
- 00c507e4 ["INT_ADD", "register:40f0:8", ["const:c507e4:8", "const:4:8"]]
- 00c507e4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50880 ["INT_ADD", "register:40f0:8", ["const:c50880:8", "const:4:8"]]
+ 00c50880 ["CALL", null, ["callee:00c5a170:8"]]
- 00c507e4 bytes 2f260094
+ 00c50880 bytes 3c260094
- 00c50800 ["INT_ADD", "register:40f0:8", ["const:c50800:8", "const:4:8"]]
- 00c50800 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c5089c ["INT_ADD", "register:40f0:8", ["const:c5089c:8", "const:4:8"]]
+ 00c5089c ["CALL", null, ["callee:00c580d0:8"]]
- 00c50800 bytes 001e0094
+ 00c5089c bytes 0d1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74ff6cb95ec14d5673d7759e1585c15"></a>

### [`00c50aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50aa0.md) → [`00c50b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md) FUN_00c50b3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50aa0.md#insn-00c50acc) · [`00c50af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50aa0.md#insn-00c50af0) · [`00c50b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50aa0.md#insn-00c50b1c)
- 新版 [`00c50b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50b68) · [`00c50b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50b8c) · [`00c50bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50bb8)

~~~diff
- 00c50acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50acc ["INT_ADD", "register:40f0:8", ["const:c50acc:8", "const:4:8"]]
- 00c50acc ["CALLIND", null, ["register:0:8"]]
+ 00c50b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50b68 ["INT_ADD", "register:40f0:8", ["const:c50b68:8", "const:4:8"]]
+ 00c50b68 ["CALLIND", null, ["register:0:8"]]
- 00c50acc bytes 00013fd6
+ 00c50b68 bytes 00013fd6
- 00c50af0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50af0 ["INT_ADD", "register:40f0:8", ["const:c50af0:8", "const:4:8"]]
- 00c50af0 ["CALLIND", null, ["register:0:8"]]
+ 00c50b8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50b8c ["INT_ADD", "register:40f0:8", ["const:c50b8c:8", "const:4:8"]]
+ 00c50b8c ["CALLIND", null, ["register:0:8"]]
- 00c50af0 bytes 00013fd6
+ 00c50b8c bytes 00013fd6
- 00c50b1c ["INT_ADD", "register:40f0:8", ["const:c50b1c:8", "const:4:8"]]
- 00c50b1c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50bb8 ["INT_ADD", "register:40f0:8", ["const:c50bb8:8", "const:4:8"]]
+ 00c50bb8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c50b1c bytes 61250094
+ 00c50bb8 bytes 6e250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-076fc3d94bedb0019ddbe482acde5ad6"></a>

### [`00c50f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50f5c.md) → [`00c50ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md) FUN_00c50ff8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50f5c.md#insn-00c50f80) · [`00c50fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50f5c.md#insn-00c50fa8) · [`00c50fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50f5c.md#insn-00c50fd8)
- 新版 [`00c5101c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c5101c) · [`00c51044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c51044) · [`00c51074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c51074)

~~~diff
- 00c50f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50f80 ["INT_ADD", "register:40f0:8", ["const:c50f80:8", "const:4:8"]]
- 00c50f80 ["CALLIND", null, ["register:0:8"]]
+ 00c5101c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5101c ["INT_ADD", "register:40f0:8", ["const:c5101c:8", "const:4:8"]]
+ 00c5101c ["CALLIND", null, ["register:0:8"]]
- 00c50f80 bytes 00013fd6
+ 00c5101c bytes 00013fd6
- 00c50fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50fa8 ["INT_ADD", "register:40f0:8", ["const:c50fa8:8", "const:4:8"]]
- 00c50fa8 ["CALLIND", null, ["register:0:8"]]
+ 00c51044 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51044 ["INT_ADD", "register:40f0:8", ["const:c51044:8", "const:4:8"]]
+ 00c51044 ["CALLIND", null, ["register:0:8"]]
- 00c50fa8 bytes 00013fd6
+ 00c51044 bytes 00013fd6
- 00c50fd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50fd8 ["INT_ADD", "register:40f0:8", ["const:c50fd8:8", "const:4:8"]]
- 00c50fd8 ["CALLIND", null, ["register:0:8"]]
+ 00c51074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51074 ["INT_ADD", "register:40f0:8", ["const:c51074:8", "const:4:8"]]
+ 00c51074 ["CALLIND", null, ["register:0:8"]]
- 00c50fd8 bytes 00013fd6
+ 00c51074 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e8e57009852cb70d033272aae0d84e"></a>

### [`00c5111c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5111c.md) → [`00c511b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md) FUN_00c511b8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5111c.md#insn-00c51158) · [`00c51188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5111c.md#insn-00c51188) · [`00c511b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5111c.md#insn-00c511b8)
- 新版 [`00c511f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c511f4) · [`00c51224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c51224) · [`00c51254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c51254)

~~~diff
- 00c51158 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51158 ["INT_ADD", "register:40f0:8", ["const:c51158:8", "const:4:8"]]
- 00c51158 ["CALLIND", null, ["register:0:8"]]
+ 00c511f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c511f4 ["INT_ADD", "register:40f0:8", ["const:c511f4:8", "const:4:8"]]
+ 00c511f4 ["CALLIND", null, ["register:0:8"]]
- 00c51158 bytes 00013fd6
+ 00c511f4 bytes 00013fd6
- 00c51188 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51188 ["INT_ADD", "register:40f0:8", ["const:c51188:8", "const:4:8"]]
- 00c51188 ["CALLIND", null, ["register:0:8"]]
+ 00c51224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51224 ["INT_ADD", "register:40f0:8", ["const:c51224:8", "const:4:8"]]
+ 00c51224 ["CALLIND", null, ["register:0:8"]]
- 00c51188 bytes 00013fd6
+ 00c51224 bytes 00013fd6
- 00c511b8 ["INT_ADD", "register:40f0:8", ["const:c511b8:8", "const:4:8"]]
- 00c511b8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c51254 ["INT_ADD", "register:40f0:8", ["const:c51254:8", "const:4:8"]]
+ 00c51254 ["CALL", null, ["callee:00c5a170:8"]]
- 00c511b8 bytes ba230094
+ 00c51254 bytes c7230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c2de1b3ac1b547301a4141a0dd8e769"></a>

### [`00c51208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51208.md) → [`00c512a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md) FUN_00c512a4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51208.md#insn-00c5125c) · [`00c51278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51208.md#insn-00c51278) · [`00c512b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51208.md#insn-00c512b0)
- 新版 [`00c512f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c512f8) · [`00c51314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c51314) · [`00c5134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c5134c)

~~~diff
- 00c5125c ["INT_ADD", "register:40f0:8", ["const:c5125c:8", "const:4:8"]]
- 00c5125c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c512f8 ["INT_ADD", "register:40f0:8", ["const:c512f8:8", "const:4:8"]]
+ 00c512f8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c5125c bytes 91230094
+ 00c512f8 bytes 9e230094
- 00c51278 ["INT_ADD", "register:40f0:8", ["const:c51278:8", "const:4:8"]]
- 00c51278 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c51314 ["INT_ADD", "register:40f0:8", ["const:c51314:8", "const:4:8"]]
+ 00c51314 ["CALL", null, ["callee:00c580d0:8"]]
- 00c51278 bytes 621b0094
+ 00c51314 bytes 6f1b0094
- 00c512b0 ["INT_ADD", "register:40f0:8", ["const:c512b0:8", "const:4:8"]]
- 00c512b0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c5134c ["INT_ADD", "register:40f0:8", ["const:c5134c:8", "const:4:8"]]
+ 00c5134c ["CALL", null, ["callee:00c5a170:8"]]
- 00c512b0 bytes 7c230094
+ 00c5134c bytes 89230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1868002f0db9ac569050298eac4234b5"></a>

### [`00c51370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51370.md) → [`00c5140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md) FUN_00c5140c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c513fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51370.md#insn-00c513fc) · [`00c51424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51370.md#insn-00c51424) · [`00c51454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51370.md#insn-00c51454)
- 新版 [`00c51498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c51498) · [`00c514c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c514c0) · [`00c514f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c514f0)

~~~diff
- 00c513fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c513fc ["INT_ADD", "register:40f0:8", ["const:c513fc:8", "const:4:8"]]
- 00c513fc ["CALLIND", null, ["register:0:8"]]
+ 00c51498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51498 ["INT_ADD", "register:40f0:8", ["const:c51498:8", "const:4:8"]]
+ 00c51498 ["CALLIND", null, ["register:0:8"]]
- 00c513fc bytes 00013fd6
+ 00c51498 bytes 00013fd6
- 00c51424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51424 ["INT_ADD", "register:40f0:8", ["const:c51424:8", "const:4:8"]]
- 00c51424 ["CALLIND", null, ["register:0:8"]]
+ 00c514c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c514c0 ["INT_ADD", "register:40f0:8", ["const:c514c0:8", "const:4:8"]]
+ 00c514c0 ["CALLIND", null, ["register:0:8"]]
- 00c51424 bytes 00013fd6
+ 00c514c0 bytes 00013fd6
- 00c51454 ["INT_ADD", "register:40f0:8", ["const:c51454:8", "const:4:8"]]
- 00c51454 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c514f0 ["INT_ADD", "register:40f0:8", ["const:c514f0:8", "const:4:8"]]
+ 00c514f0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c51454 bytes 13230094
+ 00c514f0 bytes 20230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f5e05ffe977bb656deafde7a804224"></a>

### [`00c516b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c516b0.md) → [`00c5174c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md) FUN_00c5174c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5174c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c516b0.md#insn-00c5174c) · [`00c5177c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c516b0.md#insn-00c5177c) · [`00c517ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c516b0.md#insn-00c517ac)
- 新版 [`00c517e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c517e8) · [`00c51818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c51818) · [`00c51848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c51848)

~~~diff
- 00c5174c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5174c ["INT_ADD", "register:40f0:8", ["const:c5174c:8", "const:4:8"]]
- 00c5174c ["CALLIND", null, ["register:0:8"]]
+ 00c517e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c517e8 ["INT_ADD", "register:40f0:8", ["const:c517e8:8", "const:4:8"]]
+ 00c517e8 ["CALLIND", null, ["register:0:8"]]
- 00c5174c bytes 00013fd6
+ 00c517e8 bytes 00013fd6
- 00c5177c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5177c ["INT_ADD", "register:40f0:8", ["const:c5177c:8", "const:4:8"]]
- 00c5177c ["CALLIND", null, ["register:0:8"]]
+ 00c51818 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51818 ["INT_ADD", "register:40f0:8", ["const:c51818:8", "const:4:8"]]
+ 00c51818 ["CALLIND", null, ["register:0:8"]]
- 00c5177c bytes 00013fd6
+ 00c51818 bytes 00013fd6
- 00c517ac ["INT_ADD", "register:40f0:8", ["const:c517ac:8", "const:4:8"]]
- 00c517ac ["CALL", null, ["callee:00c5a170:8"]]
+ 00c51848 ["INT_ADD", "register:40f0:8", ["const:c51848:8", "const:4:8"]]
+ 00c51848 ["CALL", null, ["callee:00c5a170:8"]]
- 00c517ac bytes 3d220094
+ 00c51848 bytes 4a220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aad642d4beb93e2f7d53d1a9bb68d43"></a>

### [`00c51a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md) → [`00c51ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md) FUN_00c51ae8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md#insn-00c51a78) · [`00c51aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md#insn-00c51aa8) · [`00c51ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md#insn-00c51ad8)
- 新版 [`00c51b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b14) · [`00c51b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b44) · [`00c51b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b74)

~~~diff
- 00c51a78 ["INT_ADD", "register:40f0:8", ["const:c51a78:8", "const:4:8"]]
- 00c51a78 ["CALL", null, ["callee:00c51c10:8"]]
+ 00c51b14 ["INT_ADD", "register:40f0:8", ["const:c51b14:8", "const:4:8"]]
+ 00c51b14 ["CALL", null, ["callee:00c51c10:8"]]
- 00c51a78 bytes 3f000094
+ 00c51b14 bytes 3f000094
- 00c51aa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51aa8 ["INT_ADD", "register:40f0:8", ["const:c51aa8:8", "const:4:8"]]
- 00c51aa8 ["CALLIND", null, ["register:0:8"]]
+ 00c51b44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51b44 ["INT_ADD", "register:40f0:8", ["const:c51b44:8", "const:4:8"]]
+ 00c51b44 ["CALLIND", null, ["register:0:8"]]
- 00c51aa8 bytes 00013fd6
+ 00c51b44 bytes 00013fd6
- 00c51ad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51ad8 ["INT_ADD", "register:40f0:8", ["const:c51ad8:8", "const:4:8"]]
- 00c51ad8 ["CALLIND", null, ["register:0:8"]]
+ 00c51b74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51b74 ["INT_ADD", "register:40f0:8", ["const:c51b74:8", "const:4:8"]]
+ 00c51b74 ["CALLIND", null, ["register:0:8"]]
- 00c51ad8 bytes 00013fd6
+ 00c51b74 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9d6fe28175f7a774e97a6989316a8e6"></a>

### [`00c51d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d20.md) → [`00c51dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dbc.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5a920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a920.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d20.md#insn-00c51d2c)
- 新版 [`00c51dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dbc.md#insn-00c51dc8)

~~~diff
- 00c51d2c ["INT_ADD", "register:40f0:8", ["const:c51d2c:8", "const:4:8"]]
- 00c51d2c ["CALL", null, ["callee:00c57f60:8"]]
+ 00c51dc8 ["INT_ADD", "register:40f0:8", ["const:c51dc8:8", "const:4:8"]]
+ 00c51dc8 ["CALL", null, ["callee:00c57f60:8"]]
- 00c51d2c bytes 59180094
+ 00c51dc8 bytes 66180094
~~~


<a id="compare-390462c02aaae0275beee2b83f14e6da"></a>

### [`00c51d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d50.md) → [`00c51dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dec.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d50.md#insn-00c51d5c)
- 新版 [`00c51df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dec.md#insn-00c51df8)

~~~diff
- 00c51d5c ["INT_ADD", "register:40f0:8", ["const:c51d5c:8", "const:4:8"]]
- 00c51d5c ["CALL", null, ["callee:00c5bf20:8"]]
+ 00c51df8 ["INT_ADD", "register:40f0:8", ["const:c51df8:8", "const:4:8"]]
+ 00c51df8 ["CALL", null, ["callee:00c5bf20:8"]]
- 00c51d5c bytes 3d280094
+ 00c51df8 bytes 4a280094
~~~


<a id="compare-60467e674d466b40367f4da8d4af4080"></a>

### [`00c51db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51db0.md) → [`00c51e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e4c.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eec0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51db0.md#insn-00c51dbc)
- 新版 [`00c51e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e4c.md#insn-00c51e58)

~~~diff
- 00c51dbc ["INT_ADD", "register:40f0:8", ["const:c51dbc:8", "const:4:8"]]
- 00c51dbc ["CALL", null, ["callee:00c5ef90:8"]]
+ 00c51e58 ["INT_ADD", "register:40f0:8", ["const:c51e58:8", "const:4:8"]]
+ 00c51e58 ["CALL", null, ["callee:00c5ef90:8"]]
- 00c51dbc bytes 41340094
+ 00c51e58 bytes 4e340094
~~~


<a id="compare-a95f03041329cbf5cc235a62e9089792"></a>

### [`00c51de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51de0.md) → [`00c51e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e7c.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5efb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51de0.md#insn-00c51dec)
- 新版 [`00c51e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e7c.md#insn-00c51e88)

~~~diff
- 00c51dec ["INT_ADD", "register:40f0:8", ["const:c51dec:8", "const:4:8"]]
- 00c51dec ["CALL", null, ["callee:00c5efb0:8"]]
+ 00c51e88 ["INT_ADD", "register:40f0:8", ["const:c51e88:8", "const:4:8"]]
+ 00c51e88 ["CALL", null, ["callee:00c5efb0:8"]]
- 00c51dec bytes 3d340094
+ 00c51e88 bytes 4a340094
~~~


<a id="compare-32be5d2e8044d073998b9423f4056901"></a>

### [`00c51e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md) → [`00c51f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md) __cxa_allocate_exception

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) · 呼出先 3件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) · 呼出先 3件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md#insn-00c51e90) · [`00c51ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md#insn-00c51ea8) · [`00c51ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md#insn-00c51ec0)
- 新版 [`00c51f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f2c) · [`00c51f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f44) · [`00c51f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f5c)

~~~diff
- 00c51e90 ["INT_ADD", "register:40f0:8", ["const:c51e90:8", "const:4:8"]]
- 00c51e90 ["CALL", null, ["callee:00c526e0:8"]]
+ 00c51f2c ["INT_ADD", "register:40f0:8", ["const:c51f2c:8", "const:4:8"]]
+ 00c51f2c ["CALL", null, ["callee:00c526e0:8"]]
- 00c51e90 bytes ed010094
+ 00c51f2c bytes ed010094
- 00c51ea8 ["INT_ADD", "register:40f0:8", ["const:c51ea8:8", "const:4:8"]]
- 00c51ea8 ["CALL", null, ["callee:00c58160:8"]]
+ 00c51f44 ["INT_ADD", "register:40f0:8", ["const:c51f44:8", "const:4:8"]]
+ 00c51f44 ["CALL", null, ["callee:00c58160:8"]]
- 00c51ea8 bytes 7a180094
+ 00c51f44 bytes 87180094
- 00c51ec0 ["INT_ADD", "register:40f0:8", ["const:c51ec0:8", "const:4:8"]]
- 00c51ec0 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c51f5c ["INT_ADD", "register:40f0:8", ["const:c51f5c:8", "const:4:8"]]
+ 00c51f5c ["CALL", null, ["callee:00c580f0:8"]]
- 00c51ec0 bytes 58180094
+ 00c51f5c bytes 65180094
~~~


<a id="compare-5b83628ff3c96dca93431454fbee192d"></a>

### [`00c51ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ec8.md) → [`00c51f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md) __cxa_begin_catch

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58010.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)
- 新版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580e0.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ec8.md#insn-00c51edc) · [`00c51f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ec8.md#insn-00c51f5c)
- 新版 [`00c51f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md#insn-00c51f78) · [`00c51ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md#insn-00c51ff8)

~~~diff
- 00c51edc ["INT_ADD", "register:40f0:8", ["const:c51edc:8", "const:4:8"]]
- 00c51edc ["CALL", null, ["callee:00c5ee60:8"]]
+ 00c51f78 ["INT_ADD", "register:40f0:8", ["const:c51f78:8", "const:4:8"]]
+ 00c51f78 ["CALL", null, ["callee:00c5ee60:8"]]
- 00c51edc bytes ad330094
+ 00c51f78 bytes ba330094
- 00c51f5c ["INT_ADD", "register:40f0:8", ["const:c51f5c:8", "const:4:8"]]
- 00c51f5c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c51ff8 ["INT_ADD", "register:40f0:8", ["const:c51ff8:8", "const:4:8"]]
+ 00c51ff8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c51f5c bytes 31180094
+ 00c51ff8 bytes 3e180094
~~~


<a id="compare-94187534f4f14ac0cd064c0ca7a946d4"></a>

### [`00c52060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md) → [`00c520fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md#insn-00c52070) · [`00c52098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md#insn-00c52098)
- 新版 [`00c5210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md#insn-00c5210c) · [`00c52134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md#insn-00c52134)

~~~diff
- 00c52070 ["INT_ADD", "register:40f0:8", ["const:c52070:8", "const:4:8"]]
- 00c52070 ["CALL", null, ["callee:00c526e0:8"]]
+ 00c5210c ["INT_ADD", "register:40f0:8", ["const:c5210c:8", "const:4:8"]]
+ 00c5210c ["CALL", null, ["callee:00c526e0:8"]]
- 00c52070 bytes 75010094
+ 00c5210c bytes 75010094
- 00c52098 ["INT_ADD", "register:40f0:8", ["const:c52098:8", "const:4:8"]]
- 00c52098 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c52134 ["INT_ADD", "register:40f0:8", ["const:c52134:8", "const:4:8"]]
+ 00c52134 ["CALL", null, ["callee:00c580f0:8"]]
- 00c52098 bytes e2170094
+ 00c52134 bytes ef170094
~~~


<a id="compare-a7735d7aca3c41db146f13132f0e7835"></a>

### [`00c520a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md) → [`00c52140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md) __cxa_throw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) · 呼出先 4件 [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c58330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58330.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)
- 新版 呼出元 1件 [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) · 呼出先 4件 [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c58400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58400.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c520c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md#insn-00c520c4) · [`00c520e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md#insn-00c520e0) · [`00c520f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md#insn-00c520f4)
- 新版 [`00c52160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c52160) · [`00c5217c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c5217c) · [`00c52190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c52190)

~~~diff
- 00c520c4 ["INT_ADD", "register:40f0:8", ["const:c520c4:8", "const:4:8"]]
- 00c520c4 ["CALL", null, ["callee:00c5ee60:8"]]
+ 00c52160 ["INT_ADD", "register:40f0:8", ["const:c52160:8", "const:4:8"]]
+ 00c52160 ["CALL", null, ["callee:00c5ee60:8"]]
- 00c520c4 bytes 33330094
+ 00c52160 bytes 40330094
- 00c520e0 ["INT_ADD", "register:40f0:8", ["const:c520e0:8", "const:4:8"]]
- 00c520e0 ["CALL", null, ["callee:00c58400:8"]]
+ 00c5217c ["INT_ADD", "register:40f0:8", ["const:c5217c:8", "const:4:8"]]
+ 00c5217c ["CALL", null, ["callee:00c58400:8"]]
- 00c520e0 bytes 94180094
+ 00c5217c bytes a1180094
- 00c520f4 ["INT_ADD", "register:40f0:8", ["const:c520f4:8", "const:4:8"]]
- 00c520f4 ["CALL", null, ["callee:00c53dd0:8"]]
+ 00c52190 ["INT_ADD", "register:40f0:8", ["const:c52190:8", "const:4:8"]]
+ 00c52190 ["CALL", null, ["callee:00c53dd0:8"]]
- 00c520f4 bytes 0f070094
+ 00c52190 bytes 10070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-003d421ce1a86598ab91ecb5b788630e"></a>

### [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) → [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) FUN_00c5219c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c520a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md) · 呼出先 2件 [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c58010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c52140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md) · 呼出先 2件 [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c580e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md#insn-00c52118) · [`00c52120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md#insn-00c52120)
- 新版 [`00c521b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md#insn-00c521b4) · [`00c521bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md#insn-00c521bc)

~~~diff
- 00c52118 ["INT_ADD", "register:40f0:8", ["const:c52118:8", "const:4:8"]]
- 00c52118 ["CALL", null, ["callee:00c580e0:8"]]
+ 00c521b4 ["INT_ADD", "register:40f0:8", ["const:c521b4:8", "const:4:8"]]
+ 00c521b4 ["CALL", null, ["callee:00c580e0:8"]]
- 00c52118 bytes be170094
+ 00c521b4 bytes cb170094
- 00c52120 ["INT_ADD", "register:40f0:8", ["const:c52120:8", "const:4:8"]]
- 00c52120 ["CALL", null, ["callee:00c3797c:8"]]
+ 00c521bc ["INT_ADD", "register:40f0:8", ["const:c521bc:8", "const:4:8"]]
+ 00c521bc ["CALL", null, ["callee:00c3797c:8"]]
- 00c52120 bytes f095ff97
+ 00c521bc bytes f095ff97
~~~


<a id="compare-c92a1d03823d8161e3e9ec37e4c0020c"></a>

### [`00c52278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52278.md) → [`00c52314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52314.md) __cxa_current_exception_type

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52278.md#insn-00c52284)
- 新版 [`00c52320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52314.md#insn-00c52320)

~~~diff
- 00c52284 ["INT_ADD", "register:40f0:8", ["const:c52284:8", "const:4:8"]]
- 00c52284 ["CALL", null, ["callee:00c5ee70:8"]]
+ 00c52320 ["INT_ADD", "register:40f0:8", ["const:c52320:8", "const:4:8"]]
+ 00c52320 ["CALL", null, ["callee:00c5ee70:8"]]
- 00c52284 bytes c7320094
+ 00c52320 bytes d4320094
~~~


<a id="compare-cd9b35db3a154c771354e0e9fc91d47f"></a>

### [`00c522c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md) → [`00c52364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md) __cxa_rethrow

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md) · 呼出先 5件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)
- 新版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md) · 呼出先 5件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c522dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md#insn-00c522dc) · [`00c522e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md#insn-00c522e8) · [`00c52334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md#insn-00c52334)
- 新版 [`00c52378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c52378) · [`00c52384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c52384) · [`00c523d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c523d0)

~~~diff
- 00c522dc ["INT_ADD", "register:40f0:8", ["const:c522dc:8", "const:4:8"]]
- 00c522dc ["CALL", null, ["callee:00c5ee60:8"]]
+ 00c52378 ["INT_ADD", "register:40f0:8", ["const:c52378:8", "const:4:8"]]
+ 00c52378 ["CALL", null, ["callee:00c5ee60:8"]]
- 00c522dc bytes ad320094
+ 00c52378 bytes ba320094
- 00c522e8 ["INT_ADD", "register:40f0:8", ["const:c522e8:8", "const:4:8"]]
- 00c522e8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c52384 ["INT_ADD", "register:40f0:8", ["const:c52384:8", "const:4:8"]]
+ 00c52384 ["CALL", null, ["callee:00c580f0:8"]]
- 00c522e8 bytes 4e170094
+ 00c52384 bytes 5b170094
- 00c52334 ["INT_ADD", "register:40f0:8", ["const:c52334:8", "const:4:8"]]
- 00c52334 ["CALL", null, ["callee:00c53dd0:8"]]
+ 00c523d0 ["INT_ADD", "register:40f0:8", ["const:c523d0:8", "const:4:8"]]
+ 00c523d0 ["CALL", null, ["callee:00c53dd0:8"]]
- 00c52334 bytes 7f060094
+ 00c523d0 bytes 80060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dda405882d1cdff4355c208dca059c3"></a>

### [`00c523ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523ac.md) → [`00c52448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52448.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df20.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dff0.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c523c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523ac.md#insn-00c523c8)
- 新版 [`00c52464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52448.md#insn-00c52464)

~~~diff
- 00c523c8 ["INT_ADD", "register:40f0:8", ["const:c523c8:8", "const:4:8"]]
- 00c523c8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00c52464 ["INT_ADD", "register:40f0:8", ["const:c52464:8", "const:4:8"]]
+ 00c52464 ["CALL", null, ["callee:00c53da0:8"]]
- 00c523c8 bytes 4e060094
+ 00c52464 bytes 4f060094
~~~


<a id="compare-a556650aeda7bb2e5d0ea4fd7c663df8"></a>

### [`00c523d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523d8.md) → [`00c52474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md) __cxa_current_primary_exception

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c523e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523d8.md#insn-00c523e8) · [`00c52434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523d8.md#insn-00c52434)
- 新版 [`00c52484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md#insn-00c52484) · [`00c524d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md#insn-00c524d0)

~~~diff
- 00c523e8 ["INT_ADD", "register:40f0:8", ["const:c523e8:8", "const:4:8"]]
- 00c523e8 ["CALL", null, ["callee:00c5ee70:8"]]
+ 00c52484 ["INT_ADD", "register:40f0:8", ["const:c52484:8", "const:4:8"]]
+ 00c52484 ["CALL", null, ["callee:00c5ee70:8"]]
- 00c523e8 bytes 6e320094
+ 00c52484 bytes 7b320094
- 00c52434 ["INT_ADD", "register:40f0:8", ["const:c52434:8", "const:4:8"]]
- 00c52434 ["CALL", null, ["callee:00c53da0:8"]]
+ 00c524d0 ["INT_ADD", "register:40f0:8", ["const:c524d0:8", "const:4:8"]]
+ 00c524d0 ["CALL", null, ["callee:00c53da0:8"]]
- 00c52434 bytes 33060094
+ 00c524d0 bytes 34060094
~~~


<a id="compare-769566a7e64732118d41a3bebd89e6eb"></a>

### [`00c525ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c525ec.md) → [`00c52688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52688.md) __cxa_uncaught_exception

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c525f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c525ec.md#insn-00c525f8)
- 新版 [`00c52694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52688.md#insn-00c52694)

~~~diff
- 00c525f8 ["INT_ADD", "register:40f0:8", ["const:c525f8:8", "const:4:8"]]
- 00c525f8 ["CALL", null, ["callee:00c5ee70:8"]]
+ 00c52694 ["INT_ADD", "register:40f0:8", ["const:c52694:8", "const:4:8"]]
+ 00c52694 ["CALL", null, ["callee:00c5ee70:8"]]
- 00c525f8 bytes ea310094
+ 00c52694 bytes f7310094
~~~


<a id="compare-8b33df2e4421a1298a282e5bd740964c"></a>

### [`00c5261c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5261c.md) → [`00c526b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526b8.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df00.md) · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 1件 [`00c5dfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfd0.md) · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5261c.md#insn-00c52628)
- 新版 [`00c526c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526b8.md#insn-00c526c4)

~~~diff
- 00c52628 ["INT_ADD", "register:40f0:8", ["const:c52628:8", "const:4:8"]]
- 00c52628 ["CALL", null, ["callee:00c5ee70:8"]]
+ 00c526c4 ["INT_ADD", "register:40f0:8", ["const:c526c4:8", "const:4:8"]]
+ 00c526c4 ["CALL", null, ["callee:00c5ee70:8"]]
- 00c52628 bytes de310094
+ 00c526c4 bytes eb310094
~~~


<a id="compare-3e6e6f10b5518eb144c2ad89d8521a01"></a>

### [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) → [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) FUN_00c526e0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c51e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md) [`00c52060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md) [`00c52458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52458.md) · 呼出先 2件 [`00c52690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md) [`00c5eed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eed0.md)
- 新版 呼出元 3件 [`00c51f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md) [`00c520fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md) [`00c524f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c524f4.md) · 呼出先 2件 [`00c5272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md) [`00c5efa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5266c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md#insn-00c5266c) · [`00c5267c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md#insn-00c5267c)
- 新版 [`00c52708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md#insn-00c52708) · [`00c52718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md#insn-00c52718)

~~~diff
- 00c5266c ["INT_ADD", "register:40f0:8", ["const:c5266c:8", "const:4:8"]]
- 00c5266c ["CALL", null, ["callee:00c5efa0:8"]]
+ 00c52708 ["INT_ADD", "register:40f0:8", ["const:c52708:8", "const:4:8"]]
+ 00c52708 ["CALL", null, ["callee:00c5efa0:8"]]
- 00c5266c bytes 19320094
+ 00c52708 bytes 26320094
- 00c5267c ["INT_ADD", "register:40f0:8", ["const:c5267c:8", "const:4:8"]]
- 00c5267c ["CALL", null, ["callee:00c5272c:8"]]
+ 00c52718 ["INT_ADD", "register:40f0:8", ["const:c52718:8", "const:4:8"]]
+ 00c52718 ["CALL", null, ["callee:00c5272c:8"]]
- 00c5267c bytes 05000094
+ 00c52718 bytes 05000094
~~~


<a id="compare-ac444373b3284855b50f00e7cf38dffb"></a>

### [`00c53100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md) → [`00c5319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md) FUN_00c5319c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) [`00c532a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c532a8.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 3件 [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) [`00c53344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53344.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c532a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md#insn-00c532a0) · [`00c532a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md#insn-00c532a4)
- 新版 [`00c5333c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md#insn-00c5333c) · [`00c53340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md#insn-00c53340)

~~~diff
- 00c532a0 ["INT_ADD", "register:40f0:8", ["const:c532a0:8", "const:4:8"]]
- 00c532a0 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c5333c ["INT_ADD", "register:40f0:8", ["const:c5333c:8", "const:4:8"]]
+ 00c5333c ["CALL", null, ["callee:00c5b210:8"]]
- 00c532a0 bytes a81f0094
+ 00c5333c bytes b51f0094
- 00c532a4 ["INT_ADD", "register:40f0:8", ["const:c532a4:8", "const:4:8"]]
- 00c532a4 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c53340 ["INT_ADD", "register:40f0:8", ["const:c53340:8", "const:4:8"]]
+ 00c53340 ["CALL", null, ["callee:00c5b210:8"]]
- 00c532a4 bytes a71f0094
+ 00c53340 bytes b41f0094
~~~


