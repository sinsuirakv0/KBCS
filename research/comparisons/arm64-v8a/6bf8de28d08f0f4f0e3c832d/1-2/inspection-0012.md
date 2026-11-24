# v16.0.1 → v16.0.2 · 要調査の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-ca157b8b52a0a750d1f77534aaf8974f"></a>

### [`00555224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md) → [`00555264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555264.md) FUN_00555264

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00555240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md#insn-00555240) · [`00555260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md#insn-00555260)
- 新版 [`00555280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555264.md#insn-00555280) · [`005552a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555264.md#insn-005552a0)

~~~diff
- 00555240 ["INT_ADD", "register:40f0:8", ["const:555240:8", "const:4:8"]]
- 00555240 ["CALL", null, ["callee:00c53da0:8"]]
+ 00555280 ["INT_ADD", "register:40f0:8", ["const:555280:8", "const:4:8"]]
+ 00555280 ["CALL", null, ["callee:00c53da0:8"]]
- 00555240 bytes b0fa1b94
+ 00555280 bytes c8fa1b94
- 00555260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00555260 ["INT_ADD", "register:40f0:8", ["const:555260:8", "const:4:8"]]
- 00555260 ["CALLIND", null, ["register:0:8"]]
+ 005552a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005552a0 ["INT_ADD", "register:40f0:8", ["const:5552a0:8", "const:4:8"]]
+ 005552a0 ["CALLIND", null, ["register:0:8"]]
- 00555260 bytes 00013fd6
+ 005552a0 bytes 00013fd6
~~~


<a id="compare-d42c787cd7040cea4514832aa2d11b1b"></a>

### [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) → [`00555cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md) FUN_00555cd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) · 呼出先 8件 [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) [`0058ffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`005599a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005599a4.md) [`0055a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a478.md) · 呼出先 8件 [`00555e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555e4c.md) [`0055b288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b288.md) [`0058ffe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00555ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md#insn-00555ce0) · [`00555cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md#insn-00555cfc) · [`00555d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md#insn-00555d38)
- 新版 [`00555d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md#insn-00555d20) · [`00555d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md#insn-00555d3c) · [`00555d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md#insn-00555d78)

~~~diff
- 00555ce0 ["INT_ADD", "register:40f0:8", ["const:555ce0:8", "const:4:8"]]
- 00555ce0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00555d20 ["INT_ADD", "register:40f0:8", ["const:555d20:8", "const:4:8"]]
+ 00555d20 ["CALL", null, ["callee:00c57f60:8"]]
- 00555ce0 bytes 6c081c94
+ 00555d20 bytes 90081c94
- 00555cfc ["INT_ADD", "register:40f0:8", ["const:555cfc:8", "const:4:8"]]
- 00555cfc ["CALL", null, ["callee:00c58160:8"]]
+ 00555d3c ["INT_ADD", "register:40f0:8", ["const:555d3c:8", "const:4:8"]]
+ 00555d3c ["CALL", null, ["callee:00c58160:8"]]
- 00555cfc bytes e5081c94
+ 00555d3c bytes 09091c94
- 00555d38 ["INT_ADD", "register:40f0:8", ["const:555d38:8", "const:4:8"]]
- 00555d38 ["CALL", null, ["callee:00555e4c:8"]]
+ 00555d78 ["INT_ADD", "register:40f0:8", ["const:555d78:8", "const:4:8"]]
+ 00555d78 ["CALL", null, ["callee:00555e4c:8"]]
- 00555d38 bytes 35000094
+ 00555d78 bytes 35000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d24182dee01939aa1063fc926474c02"></a>

### [`00559874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md) → [`005598b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005598b4.md) FUN_005598b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00555e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555e4c.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0055b288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b288.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005598f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md#insn-005598f4) · [`00559924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md#insn-00559924) · [`00559938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md#insn-00559938)
- 新版 [`00559934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005598b4.md#insn-00559934) · [`00559964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005598b4.md#insn-00559964) · [`00559978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005598b4.md#insn-00559978)

~~~diff
- 005598f4 ["INT_ADD", "register:40f0:8", ["const:5598f4:8", "const:4:8"]]
- 005598f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00559934 ["INT_ADD", "register:40f0:8", ["const:559934:8", "const:4:8"]]
+ 00559934 ["CALL", null, ["callee:00c57f60:8"]]
- 005598f4 bytes 67f91b94
+ 00559934 bytes 8bf91b94
- 00559924 ["INT_ADD", "register:40f0:8", ["const:559924:8", "const:4:8"]]
- 00559924 ["CALL", null, ["callee:00c580d0:8"]]
+ 00559964 ["INT_ADD", "register:40f0:8", ["const:559964:8", "const:4:8"]]
+ 00559964 ["CALL", null, ["callee:00c580d0:8"]]
- 00559924 bytes b7f91b94
+ 00559964 bytes dbf91b94
- 00559938 ["INT_ADD", "register:40f0:8", ["const:559938:8", "const:4:8"]]
- 00559938 ["CALL", null, ["callee:00c57f80:8"]]
+ 00559978 ["INT_ADD", "register:40f0:8", ["const:559978:8", "const:4:8"]]
+ 00559978 ["CALL", null, ["callee:00c57f80:8"]]
- 00559938 bytes 5ef91b94
+ 00559978 bytes 82f91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375d5f44eff58c724ba74dfd380ec164"></a>

### [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md) → [`0055a57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a57c.md) FUN_0055a57c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00467fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467fac.md) · 呼出先 2件 [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00467fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467fec.md) · 呼出先 2件 [`005599a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005599a4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md#insn-0055a580) · [`0055a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md#insn-0055a5a4)
- 新版 [`0055a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a57c.md#insn-0055a5c0) · [`0055a5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a57c.md#insn-0055a5e4)

~~~diff
- 0055a580 ["INT_ADD", "register:40f0:8", ["const:55a580:8", "const:4:8"]]
- 0055a580 ["CALL", null, ["callee:005599a4:8"]]
+ 0055a5c0 ["INT_ADD", "register:40f0:8", ["const:55a5c0:8", "const:4:8"]]
+ 0055a5c0 ["CALL", null, ["callee:005599a4:8"]]
- 0055a580 bytes f9fcff97
+ 0055a5c0 bytes f9fcff97
- 0055a5a4 ["INT_ADD", "register:40f0:8", ["const:55a5a4:8", "const:4:8"]]
- 0055a5a4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055a5e4 ["INT_ADD", "register:40f0:8", ["const:55a5e4:8", "const:4:8"]]
+ 0055a5e4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0055a5a4 bytes 4ff61b94
+ 0055a5e4 bytes 73f61b94
~~~


<a id="compare-ae4711be7e5dd94c22e12f614887876a"></a>

### [`0055a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a654.md) → [`0055a694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a694.md) FUN_0055a694

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00590d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590d58.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a654.md#insn-0055a670) · [`0055a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a654.md#insn-0055a690)
- 新版 [`0055a6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a694.md#insn-0055a6b0) · [`0055a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a694.md#insn-0055a6d0)

~~~diff
- 0055a670 ["INT_ADD", "register:40f0:8", ["const:55a670:8", "const:4:8"]]
- 0055a670 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055a6b0 ["INT_ADD", "register:40f0:8", ["const:55a6b0:8", "const:4:8"]]
+ 0055a6b0 ["CALL", null, ["callee:00c53da0:8"]]
- 0055a670 bytes a4e51b94
+ 0055a6b0 bytes bce51b94
- 0055a690 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055a690 ["INT_ADD", "register:40f0:8", ["const:55a690:8", "const:4:8"]]
- 0055a690 ["CALLIND", null, ["register:0:8"]]
+ 0055a6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055a6d0 ["INT_ADD", "register:40f0:8", ["const:55a6d0:8", "const:4:8"]]
+ 0055a6d0 ["CALLIND", null, ["register:0:8"]]
- 0055a690 bytes 00013fd6
+ 0055a6d0 bytes 00013fd6
~~~


<a id="compare-c80410a2376233558603845e1310f6c3"></a>

### [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) → [`0055a734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a734.md) FUN_0055a734

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00559f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559f40.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0055af78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md) [`0055b138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b138.md) [`0055b14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b14c.md) [`0055b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b160.md)
- 新版 呼出元 2件 [`005554b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005554b8.md) [`00559f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/00559f80.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0055afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055afb8.md) [`0055b178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b178.md) [`0055b18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b18c.md) [`0055b1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md#insn-0055a7ac) · [`0055a7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md#insn-0055a7c8) · [`0055a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md#insn-0055a7d8)
- 新版 [`0055a7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a734.md#insn-0055a7ec) · [`0055a808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a734.md#insn-0055a808) · [`0055a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a734.md#insn-0055a818)

~~~diff
- 0055a7ac ["INT_ADD", "register:40f0:8", ["const:55a7ac:8", "const:4:8"]]
- 0055a7ac ["CALL", null, ["callee:00c57f60:8"]]
+ 0055a7ec ["INT_ADD", "register:40f0:8", ["const:55a7ec:8", "const:4:8"]]
+ 0055a7ec ["CALL", null, ["callee:00c57f60:8"]]
- 0055a7ac bytes b9f51b94
+ 0055a7ec bytes ddf51b94
- 0055a7c8 ["INT_ADD", "register:40f0:8", ["const:55a7c8:8", "const:4:8"]]
- 0055a7c8 ["CALL", null, ["callee:00c58160:8"]]
+ 0055a808 ["INT_ADD", "register:40f0:8", ["const:55a808:8", "const:4:8"]]
+ 0055a808 ["CALL", null, ["callee:00c58160:8"]]
- 0055a7c8 bytes 32f61b94
+ 0055a808 bytes 56f61b94
- 0055a7d8 ["INT_ADD", "register:40f0:8", ["const:55a7d8:8", "const:4:8"]]
- 0055a7d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0055a818 ["INT_ADD", "register:40f0:8", ["const:55a818:8", "const:4:8"]]
+ 0055a818 ["CALL", null, ["callee:00c57f60:8"]]
- 0055a7d8 bytes aef51b94
+ 0055a818 bytes d2f51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-427624586957e6c84b7d3a2cabb9eabf"></a>

### [`0055af78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md) → [`0055afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055afb8.md) FUN_0055afb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0055a734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a734.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md#insn-0055b0a4) · [`0055b0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md#insn-0055b0d8)
- 新版 [`0055b0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055afb8.md#insn-0055b0e4) · [`0055b118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055afb8.md#insn-0055b118)

~~~diff
- 0055b0a4 ["INT_ADD", "register:40f0:8", ["const:55b0a4:8", "const:4:8"]]
- 0055b0a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0055b0e4 ["INT_ADD", "register:40f0:8", ["const:55b0e4:8", "const:4:8"]]
+ 0055b0e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0055b0a4 bytes 83f31b94
+ 0055b0e4 bytes a7f31b94
- 0055b0d8 ["INT_ADD", "register:40f0:8", ["const:55b0d8:8", "const:4:8"]]
- 0055b0d8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055b118 ["INT_ADD", "register:40f0:8", ["const:55b118:8", "const:4:8"]]
+ 0055b118 ["CALL", null, ["callee:00c57fb0:8"]]
- 0055b0d8 bytes 82f31b94
+ 0055b118 bytes a6f31b94
~~~


<a id="compare-67874b8375b6794d9697f6d48c5ca921"></a>

### [`0055b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b0dc.md) → [`0055b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b11c.md) FUN_0055b11c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b0dc.md#insn-0055b11c)
- 新版 [`0055b15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b11c.md#insn-0055b15c)

~~~diff
- 0055b11c ["INT_ADD", "register:40f0:8", ["const:55b11c:8", "const:4:8"]]
- 0055b11c ["CALL", null, ["callee:00c57f80:8"]]
+ 0055b15c ["INT_ADD", "register:40f0:8", ["const:55b15c:8", "const:4:8"]]
+ 0055b15c ["CALL", null, ["callee:00c57f80:8"]]
- 0055b11c bytes 65f31b94
+ 0055b15c bytes 89f31b94
~~~


<a id="compare-20d18d255de7892ef109bbdb11cfe327"></a>

### [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) → [`0055b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md) FUN_0055b3c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055b25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md) [`0055c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md) [`0055c324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md) · 呼出先 5件 [`0055b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md) [`0058ff58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff58.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0055b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b29c.md) [`0055c324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c324.md) [`0055c364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c364.md) · 呼出先 5件 [`0055b4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b4f8.md) [`0058ff98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff98.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md#insn-0055b3b4) · [`0055b3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md#insn-0055b3d4) · [`0055b3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md#insn-0055b3e8)
- 新版 [`0055b3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md#insn-0055b3f4) · [`0055b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md#insn-0055b414) · [`0055b428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md#insn-0055b428)

~~~diff
- 0055b3b4 ["INT_ADD", "register:40f0:8", ["const:55b3b4:8", "const:4:8"]]
- 0055b3b4 ["CALL", null, ["callee:0058ff98:8"]]
+ 0055b3f4 ["INT_ADD", "register:40f0:8", ["const:55b3f4:8", "const:4:8"]]
+ 0055b3f4 ["CALL", null, ["callee:0058ff98:8"]]
- 0055b3b4 bytes e9d20094
+ 0055b3f4 bytes e9d20094
- 0055b3d4 ["INT_ADD", "register:40f0:8", ["const:55b3d4:8", "const:4:8"]]
- 0055b3d4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055b414 ["INT_ADD", "register:40f0:8", ["const:55b414:8", "const:4:8"]]
+ 0055b414 ["CALL", null, ["callee:00c53da0:8"]]
- 0055b3d4 bytes 4be21b94
+ 0055b414 bytes 63e21b94
- 0055b3e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055b3e8 ["INT_ADD", "register:40f0:8", ["const:55b3e8:8", "const:4:8"]]
- 0055b3e8 ["CALLIND", null, ["register:0:8"]]
+ 0055b428 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055b428 ["INT_ADD", "register:40f0:8", ["const:55b428:8", "const:4:8"]]
+ 0055b428 ["CALLIND", null, ["register:0:8"]]
- 0055b3e8 bytes 00013fd6
+ 0055b428 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ecef31c891b74c2836249672e54c174"></a>

### [`0055b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md) → [`0055b4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b4f8.md) FUN_0055b4f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) · 呼出先 6件 [`0055c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6dc.md) [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0055b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md) · 呼出先 6件 [`0055c71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c71c.md) [`0055c724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c724.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md#insn-0055b504) · [`0055b524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md#insn-0055b524) · [`0055b540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md#insn-0055b540)
- 新版 [`0055b544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b4f8.md#insn-0055b544) · [`0055b564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b4f8.md#insn-0055b564) · [`0055b580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b4f8.md#insn-0055b580)

~~~diff
- 0055b504 ["INT_ADD", "register:40f0:8", ["const:55b504:8", "const:4:8"]]
- 0055b504 ["CALL", null, ["callee:00c53d70:8"]]
+ 0055b544 ["INT_ADD", "register:40f0:8", ["const:55b544:8", "const:4:8"]]
+ 0055b544 ["CALL", null, ["callee:00c53d70:8"]]
- 0055b504 bytes f3e11b94
+ 0055b544 bytes 0be21b94
- 0055b524 ["INT_ADD", "register:40f0:8", ["const:55b524:8", "const:4:8"]]
- 0055b524 ["CALL", null, ["callee:0055c71c:8"]]
+ 0055b564 ["INT_ADD", "register:40f0:8", ["const:55b564:8", "const:4:8"]]
+ 0055b564 ["CALL", null, ["callee:0055c71c:8"]]
- 0055b524 bytes 6e040094
+ 0055b564 bytes 6e040094
- 0055b540 ["INT_ADD", "register:40f0:8", ["const:55b540:8", "const:4:8"]]
- 0055b540 ["CALL", null, ["callee:0055c724:8"]]
+ 0055b580 ["INT_ADD", "register:40f0:8", ["const:55b580:8", "const:4:8"]]
+ 0055b580 ["CALL", null, ["callee:0055c724:8"]]
- 0055b540 bytes 69040094
+ 0055b580 bytes 69040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9111e24fbdd0fed5f7eebda662a01d79"></a>

### [`0055b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b810.md) → [`0055b850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b850.md) FUN_0055b850

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0055e6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b810.md#insn-0055b830)
- 新版 [`0055b870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b850.md#insn-0055b870)

~~~diff
- 0055b830 ["INT_ADD", "register:40f0:8", ["const:55b830:8", "const:4:8"]]
- 0055b830 ["CALL", null, ["callee:0055e700:8"]]
+ 0055b870 ["INT_ADD", "register:40f0:8", ["const:55b870:8", "const:4:8"]]
+ 0055b870 ["CALL", null, ["callee:0055e700:8"]]
- 0055b830 bytes a40b0094
+ 0055b870 bytes a40b0094
~~~


<a id="compare-ad7d85448e47a1a44d4ad92d17abb6bf"></a>

### [`0055b874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b874.md) → [`0055b8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b8b4.md) FUN_0055b8b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0055e6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b874.md#insn-0055b890)
- 新版 [`0055b8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b8b4.md#insn-0055b8d0)

~~~diff
- 0055b890 ["INT_ADD", "register:40f0:8", ["const:55b890:8", "const:4:8"]]
- 0055b890 ["CALL", null, ["callee:0055e700:8"]]
+ 0055b8d0 ["INT_ADD", "register:40f0:8", ["const:55b8d0:8", "const:4:8"]]
+ 0055b8d0 ["CALL", null, ["callee:0055e700:8"]]
- 0055b890 bytes 8c0b0094
+ 0055b8d0 bytes 8c0b0094
~~~


<a id="compare-aa273039de7cecf8cf76ba1d7757b39b"></a>

### [`0055c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md) → [`0055c324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c324.md) FUN_0055c324

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md) [`0055e664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e664.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md#insn-0055c300) · [`0055c30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md#insn-0055c30c)
- 新版 [`0055c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c324.md#insn-0055c340) · [`0055c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c324.md#insn-0055c34c)

~~~diff
- 0055c300 ["INT_ADD", "register:40f0:8", ["const:55c300:8", "const:4:8"]]
- 0055c300 ["CALL", null, ["callee:0055e664:8"]]
+ 0055c340 ["INT_ADD", "register:40f0:8", ["const:55c340:8", "const:4:8"]]
+ 0055c340 ["CALL", null, ["callee:0055e664:8"]]
- 0055c300 bytes c9080094
+ 0055c340 bytes c9080094
- 0055c30c ["INT_ADD", "register:40f0:8", ["const:55c30c:8", "const:4:8"]]
- 0055c30c ["CALL", null, ["callee:0055b3c0:8"]]
+ 0055c34c ["INT_ADD", "register:40f0:8", ["const:55c34c:8", "const:4:8"]]
+ 0055c34c ["CALL", null, ["callee:0055b3c0:8"]]
- 0055c30c bytes 1dfcff97
+ 0055c34c bytes 1dfcff97
~~~


<a id="compare-2a4d68404477a5a1dc11ae8b0acd5320"></a>

### [`0055c324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md) → [`0055c364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c364.md) FUN_0055c364

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055b/0055b3c0.md) [`0055e664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e664.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md#insn-0055c33c) · [`0055c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md#insn-0055c348)
- 新版 [`0055c37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c364.md#insn-0055c37c) · [`0055c388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c364.md#insn-0055c388)

~~~diff
- 0055c33c ["INT_ADD", "register:40f0:8", ["const:55c33c:8", "const:4:8"]]
- 0055c33c ["CALL", null, ["callee:0055e664:8"]]
+ 0055c37c ["INT_ADD", "register:40f0:8", ["const:55c37c:8", "const:4:8"]]
+ 0055c37c ["CALL", null, ["callee:0055e664:8"]]
- 0055c33c bytes ba080094
+ 0055c37c bytes ba080094
- 0055c348 ["INT_ADD", "register:40f0:8", ["const:55c348:8", "const:4:8"]]
- 0055c348 ["CALL", null, ["callee:0055b3c0:8"]]
+ 0055c388 ["INT_ADD", "register:40f0:8", ["const:55c388:8", "const:4:8"]]
+ 0055c388 ["CALL", null, ["callee:0055b3c0:8"]]
- 0055c348 bytes 0efcff97
+ 0055c388 bytes 0efcff97
~~~


<a id="compare-88a33413cd1080caa828e2dab5c15ebc"></a>

### [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) → [`0055c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md) FUN_0055c804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0057f86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md) [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) · 呼出先 2件 [`0055ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0057f8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md) [`005804e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md) · 呼出先 2件 [`0055ca44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055ca44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md#insn-0055c7f8) · [`0055c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md#insn-0055c81c)
- 新版 [`0055c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md#insn-0055c838) · [`0055c85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md#insn-0055c85c)

~~~diff
- 0055c7f8 ["INT_ADD", "register:40f0:8", ["const:55c7f8:8", "const:4:8"]]
- 0055c7f8 ["CALL", null, ["callee:0055ca44:8"]]
+ 0055c838 ["INT_ADD", "register:40f0:8", ["const:55c838:8", "const:4:8"]]
+ 0055c838 ["CALL", null, ["callee:0055ca44:8"]]
- 0055c7f8 bytes 83000094
+ 0055c838 bytes 83000094
- 0055c81c ["INT_ADD", "register:40f0:8", ["const:55c81c:8", "const:4:8"]]
- 0055c81c ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055c85c ["INT_ADD", "register:40f0:8", ["const:55c85c:8", "const:4:8"]]
+ 0055c85c ["CALL", null, ["callee:00c57fb0:8"]]
- 0055c81c bytes b1ed1b94
+ 0055c85c bytes d5ed1b94
~~~


<a id="compare-2f63395c3cc51dcd23b4dd41d0782536"></a>

### [`0055c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md) → [`0055c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c8c8.md) FUN_0055c8c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) [`0055ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`0055c724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c724.md) [`0055ca44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055ca44.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md#insn-0055c900) · [`0055c924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md#insn-0055c924) · [`0055c950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md#insn-0055c950)
- 新版 [`0055c940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c8c8.md#insn-0055c940) · [`0055c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c8c8.md#insn-0055c964) · [`0055c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c8c8.md#insn-0055c990)

~~~diff
- 0055c900 ["INT_ADD", "register:40f0:8", ["const:55c900:8", "const:4:8"]]
- 0055c900 ["CALL", null, ["callee:00c57f60:8"]]
+ 0055c940 ["INT_ADD", "register:40f0:8", ["const:55c940:8", "const:4:8"]]
+ 0055c940 ["CALL", null, ["callee:00c57f60:8"]]
- 0055c900 bytes 64ed1b94
+ 0055c940 bytes 88ed1b94
- 0055c924 ["INT_ADD", "register:40f0:8", ["const:55c924:8", "const:4:8"]]
- 0055c924 ["CALL", null, ["callee:00c58160:8"]]
+ 0055c964 ["INT_ADD", "register:40f0:8", ["const:55c964:8", "const:4:8"]]
+ 0055c964 ["CALL", null, ["callee:00c58160:8"]]
- 0055c924 bytes dbed1b94
+ 0055c964 bytes ffed1b94
- 0055c950 ["INT_ADD", "register:40f0:8", ["const:55c950:8", "const:4:8"]]
- 0055c950 ["CALL", null, ["callee:00c58160:8"]]
+ 0055c990 ["INT_ADD", "register:40f0:8", ["const:55c990:8", "const:4:8"]]
+ 0055c990 ["CALL", null, ["callee:00c58160:8"]]
- 0055c950 bytes d0ed1b94
+ 0055c990 bytes f4ed1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8792c8b6887bf8eb2fd17bf1935d523"></a>

### [`0055cd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd30.md) → [`0055cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cd70.md) FUN_0055cd70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055cd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd30.md#insn-0055cd4c) · [`0055cd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd30.md#insn-0055cd6c)
- 新版 [`0055cd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cd70.md#insn-0055cd8c) · [`0055cdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cd70.md#insn-0055cdac)

~~~diff
- 0055cd4c ["INT_ADD", "register:40f0:8", ["const:55cd4c:8", "const:4:8"]]
- 0055cd4c ["CALL", null, ["callee:00c53da0:8"]]
+ 0055cd8c ["INT_ADD", "register:40f0:8", ["const:55cd8c:8", "const:4:8"]]
+ 0055cd8c ["CALL", null, ["callee:00c53da0:8"]]
- 0055cd4c bytes eddb1b94
+ 0055cd8c bytes 05dc1b94
- 0055cd6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055cd6c ["INT_ADD", "register:40f0:8", ["const:55cd6c:8", "const:4:8"]]
- 0055cd6c ["CALLIND", null, ["register:0:8"]]
+ 0055cdac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055cdac ["INT_ADD", "register:40f0:8", ["const:55cdac:8", "const:4:8"]]
+ 0055cdac ["CALLIND", null, ["register:0:8"]]
- 0055cd6c bytes 00013fd6
+ 0055cdac bytes 00013fd6
~~~


<a id="compare-b7f9a004206a09c2840137ac9ad12be7"></a>

### [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) → [`0055cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md) FUN_0055cea8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0055d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md) [`0055d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md) [`0055d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md) · 呼出先 2件 [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) [`0055ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md)
- 新版 呼出元 3件 [`0055d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d070.md) [`0055d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d1d0.md) [`0055d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d330.md) · 呼出先 2件 [`0053c1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c1b8.md) [`0055de10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055de10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055cea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md#insn-0055cea0) · [`0055cef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md#insn-0055cef4)
- 新版 [`0055cee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md#insn-0055cee0) · [`0055cf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md#insn-0055cf34)

~~~diff
- 0055cea0 ["INT_ADD", "register:40f0:8", ["const:55cea0:8", "const:4:8"]]
- 0055cea0 ["CALL", null, ["callee:0055de10:8"]]
+ 0055cee0 ["INT_ADD", "register:40f0:8", ["const:55cee0:8", "const:4:8"]]
+ 0055cee0 ["CALL", null, ["callee:0055de10:8"]]
- 0055cea0 bytes cc030094
+ 0055cee0 bytes cc030094
- 0055cef4 ["INT_ADD", "register:40f0:8", ["const:55cef4:8", "const:4:8"]]
- 0055cef4 ["CALL", null, ["callee:0053c1b8:8"]]
+ 0055cf34 ["INT_ADD", "register:40f0:8", ["const:55cf34:8", "const:4:8"]]
+ 0055cf34 ["CALL", null, ["callee:0053c1b8:8"]]
- 0055cef4 bytes a17cff97
+ 0055cf34 bytes a17cff97
~~~


<a id="compare-992aea0ecb428324e9bf9affae2e5af8"></a>

### [`0055cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md) → [`0055cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cff8.md) FUN_0055cff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055cfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md#insn-0055cfdc) · [`0055cff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md#insn-0055cff4) · [`0055d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md#insn-0055d018)
- 新版 [`0055d01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cff8.md#insn-0055d01c) · [`0055d034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cff8.md#insn-0055d034) · [`0055d058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cff8.md#insn-0055d058)

~~~diff
- 0055cfdc ["INT_ADD", "register:40f0:8", ["const:55cfdc:8", "const:4:8"]]
- 0055cfdc ["CALL", null, ["callee:00c53d70:8"]]
+ 0055d01c ["INT_ADD", "register:40f0:8", ["const:55d01c:8", "const:4:8"]]
+ 0055d01c ["CALL", null, ["callee:00c53d70:8"]]
- 0055cfdc bytes 3ddb1b94
+ 0055d01c bytes 55db1b94
- 0055cff4 ["INT_ADD", "register:40f0:8", ["const:55cff4:8", "const:4:8"]]
- 0055cff4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055d034 ["INT_ADD", "register:40f0:8", ["const:55d034:8", "const:4:8"]]
+ 0055d034 ["CALL", null, ["callee:00c53da0:8"]]
- 0055cff4 bytes 43db1b94
+ 0055d034 bytes 5bdb1b94
- 0055d018 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d018 ["INT_ADD", "register:40f0:8", ["const:55d018:8", "const:4:8"]]
- 0055d018 ["CALLIND", null, ["register:0:8"]]
+ 0055d058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d058 ["INT_ADD", "register:40f0:8", ["const:55d058:8", "const:4:8"]]
+ 0055d058 ["CALLIND", null, ["register:0:8"]]
- 0055d018 bytes 00013fd6
+ 0055d058 bytes 00013fd6
~~~


<a id="compare-7110e80bbc8a9fdad22734e694e622d8"></a>

### [`0055d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md) → [`0055d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d070.md) FUN_0055d070

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md#insn-0055d078) · [`0055d09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md#insn-0055d09c) · [`0055d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md#insn-0055d0c0)
- 新版 [`0055d0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d070.md#insn-0055d0b8) · [`0055d0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d070.md#insn-0055d0dc) · [`0055d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d070.md#insn-0055d100)

~~~diff
- 0055d078 ["INT_ADD", "register:40f0:8", ["const:55d078:8", "const:4:8"]]
- 0055d078 ["CALL", null, ["callee:0055cea8:8"]]
+ 0055d0b8 ["INT_ADD", "register:40f0:8", ["const:55d0b8:8", "const:4:8"]]
+ 0055d0b8 ["CALL", null, ["callee:0055cea8:8"]]
- 0055d078 bytes 7cffff97
+ 0055d0b8 bytes 7cffff97
- 0055d09c ["INT_ADD", "register:40f0:8", ["const:55d09c:8", "const:4:8"]]
- 0055d09c ["CALL", null, ["callee:00c53d70:8"]]
+ 0055d0dc ["INT_ADD", "register:40f0:8", ["const:55d0dc:8", "const:4:8"]]
+ 0055d0dc ["CALL", null, ["callee:00c53d70:8"]]
- 0055d09c bytes 0ddb1b94
+ 0055d0dc bytes 25db1b94
- 0055d0c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d0c0 ["INT_ADD", "register:40f0:8", ["const:55d0c0:8", "const:4:8"]]
- 0055d0c0 ["CALLIND", null, ["register:0:8"]]
+ 0055d100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d100 ["INT_ADD", "register:40f0:8", ["const:55d100:8", "const:4:8"]]
+ 0055d100 ["CALLIND", null, ["register:0:8"]]
- 0055d0c0 bytes 00013fd6
+ 0055d100 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ab084b1e97796d58c3726ad17b9adda"></a>

### [`0055d140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d140.md) → [`0055d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d180.md) FUN_0055d180

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d140.md#insn-0055d15c) · [`0055d17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d140.md#insn-0055d17c)
- 新版 [`0055d19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d180.md#insn-0055d19c) · [`0055d1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d180.md#insn-0055d1bc)

~~~diff
- 0055d15c ["INT_ADD", "register:40f0:8", ["const:55d15c:8", "const:4:8"]]
- 0055d15c ["CALL", null, ["callee:00c53da0:8"]]
+ 0055d19c ["INT_ADD", "register:40f0:8", ["const:55d19c:8", "const:4:8"]]
+ 0055d19c ["CALL", null, ["callee:00c53da0:8"]]
- 0055d15c bytes e9da1b94
+ 0055d19c bytes 01db1b94
- 0055d17c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d17c ["INT_ADD", "register:40f0:8", ["const:55d17c:8", "const:4:8"]]
- 0055d17c ["CALLIND", null, ["register:0:8"]]
+ 0055d1bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d1bc ["INT_ADD", "register:40f0:8", ["const:55d1bc:8", "const:4:8"]]
+ 0055d1bc ["CALLIND", null, ["register:0:8"]]
- 0055d17c bytes 00013fd6
+ 0055d1bc bytes 00013fd6
~~~


<a id="compare-dd0c4bd64f35de3c1ac15896fd92b7f5"></a>

### [`0055d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md) → [`0055d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d1d0.md) FUN_0055d1d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md#insn-0055d1fc) · [`0055d224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md#insn-0055d224) · [`0055d264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md#insn-0055d264)
- 新版 [`0055d23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d1d0.md#insn-0055d23c) · [`0055d264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d1d0.md#insn-0055d264) · [`0055d2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d1d0.md#insn-0055d2a4)

~~~diff
- 0055d1fc ["INT_ADD", "register:40f0:8", ["const:55d1fc:8", "const:4:8"]]
- 0055d1fc ["CALL", null, ["callee:0055cea8:8"]]
+ 0055d23c ["INT_ADD", "register:40f0:8", ["const:55d23c:8", "const:4:8"]]
+ 0055d23c ["CALL", null, ["callee:0055cea8:8"]]
- 0055d1fc bytes 1bffff97
+ 0055d23c bytes 1bffff97
- 0055d224 ["INT_ADD", "register:40f0:8", ["const:55d224:8", "const:4:8"]]
- 0055d224 ["CALL", null, ["callee:00c53d70:8"]]
+ 0055d264 ["INT_ADD", "register:40f0:8", ["const:55d264:8", "const:4:8"]]
+ 0055d264 ["CALL", null, ["callee:00c53d70:8"]]
- 0055d224 bytes abda1b94
+ 0055d264 bytes c3da1b94
- 0055d264 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d264 ["INT_ADD", "register:40f0:8", ["const:55d264:8", "const:4:8"]]
- 0055d264 ["CALLIND", null, ["register:0:8"]]
+ 0055d2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d2a4 ["INT_ADD", "register:40f0:8", ["const:55d2a4:8", "const:4:8"]]
+ 0055d2a4 ["CALLIND", null, ["register:0:8"]]
- 0055d264 bytes 00013fd6
+ 0055d2a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745885f92ee3a5da5b5da0a8fb64316a"></a>

### [`0055d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md) → [`0055d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d330.md) FUN_0055d330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md#insn-0055d330) · [`0055d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md#insn-0055d354) · [`0055d374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md#insn-0055d374)
- 新版 [`0055d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d330.md#insn-0055d370) · [`0055d394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d330.md#insn-0055d394) · [`0055d3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d330.md#insn-0055d3b4)

~~~diff
- 0055d330 ["INT_ADD", "register:40f0:8", ["const:55d330:8", "const:4:8"]]
- 0055d330 ["CALL", null, ["callee:0055cea8:8"]]
+ 0055d370 ["INT_ADD", "register:40f0:8", ["const:55d370:8", "const:4:8"]]
+ 0055d370 ["CALL", null, ["callee:0055cea8:8"]]
- 0055d330 bytes cefeff97
+ 0055d370 bytes cefeff97
- 0055d354 ["INT_ADD", "register:40f0:8", ["const:55d354:8", "const:4:8"]]
- 0055d354 ["CALL", null, ["callee:00c53d70:8"]]
+ 0055d394 ["INT_ADD", "register:40f0:8", ["const:55d394:8", "const:4:8"]]
+ 0055d394 ["CALL", null, ["callee:00c53d70:8"]]
- 0055d354 bytes 5fda1b94
+ 0055d394 bytes 77da1b94
- 0055d374 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d374 ["INT_ADD", "register:40f0:8", ["const:55d374:8", "const:4:8"]]
- 0055d374 ["CALLIND", null, ["register:0:8"]]
+ 0055d3b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d3b4 ["INT_ADD", "register:40f0:8", ["const:55d3b4:8", "const:4:8"]]
+ 0055d3b4 ["CALLIND", null, ["register:0:8"]]
- 0055d374 bytes 00013fd6
+ 0055d3b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b34937553da39fb793d345d126da228a"></a>

### [`0055d598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d598.md) → [`0055d5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d5d8.md) FUN_0055d5d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d598.md#insn-0055d5b4) · [`0055d5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d598.md#insn-0055d5d4)
- 新版 [`0055d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d5d8.md#insn-0055d5f4) · [`0055d614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d5d8.md#insn-0055d614)

~~~diff
- 0055d5b4 ["INT_ADD", "register:40f0:8", ["const:55d5b4:8", "const:4:8"]]
- 0055d5b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055d5f4 ["INT_ADD", "register:40f0:8", ["const:55d5f4:8", "const:4:8"]]
+ 0055d5f4 ["CALL", null, ["callee:00c53da0:8"]]
- 0055d5b4 bytes d3d91b94
+ 0055d5f4 bytes ebd91b94
- 0055d5d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d5d4 ["INT_ADD", "register:40f0:8", ["const:55d5d4:8", "const:4:8"]]
- 0055d5d4 ["CALLIND", null, ["register:0:8"]]
+ 0055d614 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d614 ["INT_ADD", "register:40f0:8", ["const:55d614:8", "const:4:8"]]
+ 0055d614 ["CALLIND", null, ["register:0:8"]]
- 0055d5d4 bytes 00013fd6
+ 0055d614 bytes 00013fd6
~~~


<a id="compare-a10f82a036b9a0765af0cc0b2421b4f5"></a>

### [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) → [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) FUN_0055d628

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) [`0058ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md) [`0055e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md) [`0058fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md) [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md) [`0058ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md#insn-0055d630) · [`0055d660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md#insn-0055d660) · [`0055d678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md#insn-0055d678)
- 新版 [`0055d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md#insn-0055d670) · [`0055d6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md#insn-0055d6a0) · [`0055d6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md#insn-0055d6b8)

~~~diff
- 0055d630 ["INT_ADD", "register:40f0:8", ["const:55d630:8", "const:4:8"]]
- 0055d630 ["CALL", null, ["callee:0055db9c:8"]]
+ 0055d670 ["INT_ADD", "register:40f0:8", ["const:55d670:8", "const:4:8"]]
+ 0055d670 ["CALL", null, ["callee:0055db9c:8"]]
- 0055d630 bytes 4b010094
+ 0055d670 bytes 4b010094
- 0055d660 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d660 ["INT_ADD", "register:40f0:8", ["const:55d660:8", "const:4:8"]]
- 0055d660 ["CALLIND", null, ["register:0:8"]]
+ 0055d6a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d6a0 ["INT_ADD", "register:40f0:8", ["const:55d6a0:8", "const:4:8"]]
+ 0055d6a0 ["CALLIND", null, ["register:0:8"]]
- 0055d660 bytes 00013fd6
+ 0055d6a0 bytes 00013fd6
- 0055d678 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d678 ["INT_ADD", "register:40f0:8", ["const:55d678:8", "const:4:8"]]
- 0055d678 ["CALLIND", null, ["register:0:8"]]
+ 0055d6b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d6b8 ["INT_ADD", "register:40f0:8", ["const:55d6b8:8", "const:4:8"]]
+ 0055d6b8 ["CALLIND", null, ["register:0:8"]]
- 0055d678 bytes 00013fd6
+ 0055d6b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb47c4ce7bb3b26cf6c08e27494a32dc"></a>

### [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) → [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) FUN_0055d800

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) [`0058fe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0055db9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md) [`0055e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md) [`0058fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md) [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md) [`0058fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md#insn-0055d820) · [`0055d874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md#insn-0055d874) · [`0055d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md#insn-0055d880)
- 新版 [`0055d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md#insn-0055d860) · [`0055d8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md#insn-0055d8b4) · [`0055d8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md#insn-0055d8c0)

~~~diff
- 0055d820 ["INT_ADD", "register:40f0:8", ["const:55d820:8", "const:4:8"]]
- 0055d820 ["CALL", null, ["callee:0055db9c:8"]]
+ 0055d860 ["INT_ADD", "register:40f0:8", ["const:55d860:8", "const:4:8"]]
+ 0055d860 ["CALL", null, ["callee:0055db9c:8"]]
- 0055d820 bytes cf000094
+ 0055d860 bytes cf000094
- 0055d874 ["INT_ADD", "register:40f0:8", ["const:55d874:8", "const:4:8"]]
- 0055d874 ["CALL", null, ["callee:0058fddc:8"]]
+ 0055d8b4 ["INT_ADD", "register:40f0:8", ["const:55d8b4:8", "const:4:8"]]
+ 0055d8b4 ["CALL", null, ["callee:0058fddc:8"]]
- 0055d874 bytes 4ac90094
+ 0055d8b4 bytes 4ac90094
- 0055d880 ["INT_ADD", "register:40f0:8", ["const:55d880:8", "const:4:8"]]
- 0055d880 ["CALL", null, ["callee:0058ff68:8"]]
+ 0055d8c0 ["INT_ADD", "register:40f0:8", ["const:55d8c0:8", "const:4:8"]]
+ 0055d8c0 ["CALL", null, ["callee:0058ff68:8"]]
- 0055d880 bytes aac90094
+ 0055d8c0 bytes aac90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6708a5f437407c51b280b611ed7998be"></a>

### [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) → [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) FUN_0055d9dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fc40.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md) [`0055e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md) [`0058fc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc80.md) [`0058fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md) [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md#insn-0055d9d4) · [`0055da1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md#insn-0055da1c) · [`0055da24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md#insn-0055da24)
- 新版 [`0055da14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md#insn-0055da14) · [`0055da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md#insn-0055da5c) · [`0055da64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md#insn-0055da64)

~~~diff
- 0055d9d4 ["INT_ADD", "register:40f0:8", ["const:55d9d4:8", "const:4:8"]]
- 0055d9d4 ["CALL", null, ["callee:0055db9c:8"]]
+ 0055da14 ["INT_ADD", "register:40f0:8", ["const:55da14:8", "const:4:8"]]
+ 0055da14 ["CALL", null, ["callee:0055db9c:8"]]
- 0055d9d4 bytes 62000094
+ 0055da14 bytes 62000094
- 0055da1c ["INT_ADD", "register:40f0:8", ["const:55da1c:8", "const:4:8"]]
- 0055da1c ["CALL", null, ["callee:0058fddc:8"]]
+ 0055da5c ["INT_ADD", "register:40f0:8", ["const:55da5c:8", "const:4:8"]]
+ 0055da5c ["CALL", null, ["callee:0058fddc:8"]]
- 0055da1c bytes e0c80094
+ 0055da5c bytes e0c80094
- 0055da24 ["INT_ADD", "register:40f0:8", ["const:55da24:8", "const:4:8"]]
- 0055da24 ["CALL", null, ["callee:0058fc80:8"]]
+ 0055da64 ["INT_ADD", "register:40f0:8", ["const:55da64:8", "const:4:8"]]
+ 0055da64 ["CALL", null, ["callee:0058fc80:8"]]
- 0055da24 bytes 87c80094
+ 0055da64 bytes 87c80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2061780c689a7f5fe0ceb4115fd392dc"></a>

### [`0055db0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db0c.md) → [`0055db4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db4c.md) FUN_0055db4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055db28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db0c.md#insn-0055db28) · [`0055db48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db0c.md#insn-0055db48)
- 新版 [`0055db68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db4c.md#insn-0055db68) · [`0055db88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db4c.md#insn-0055db88)

~~~diff
- 0055db28 ["INT_ADD", "register:40f0:8", ["const:55db28:8", "const:4:8"]]
- 0055db28 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055db68 ["INT_ADD", "register:40f0:8", ["const:55db68:8", "const:4:8"]]
+ 0055db68 ["CALL", null, ["callee:00c53da0:8"]]
- 0055db28 bytes 76d81b94
+ 0055db68 bytes 8ed81b94
- 0055db48 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055db48 ["INT_ADD", "register:40f0:8", ["const:55db48:8", "const:4:8"]]
- 0055db48 ["CALLIND", null, ["register:0:8"]]
+ 0055db88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055db88 ["INT_ADD", "register:40f0:8", ["const:55db88:8", "const:4:8"]]
+ 0055db88 ["CALLIND", null, ["register:0:8"]]
- 0055db48 bytes 00013fd6
+ 0055db88 bytes 00013fd6
~~~


<a id="compare-d4ac3eca04cc9cac9b4818ff81b62e50"></a>

### [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) → [`0055db9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md) FUN_0055db9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 4件 [`0058ff8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff8c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 4件 [`0058ffcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffcc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md#insn-0055db94) · [`0055dbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md#insn-0055dbb4) · [`0055dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md#insn-0055dbc8)
- 新版 [`0055dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md#insn-0055dbd4) · [`0055dbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md#insn-0055dbf4) · [`0055dc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055db9c.md#insn-0055dc08)

~~~diff
- 0055db94 ["INT_ADD", "register:40f0:8", ["const:55db94:8", "const:4:8"]]
- 0055db94 ["CALL", null, ["callee:0058ffcc:8"]]
+ 0055dbd4 ["INT_ADD", "register:40f0:8", ["const:55dbd4:8", "const:4:8"]]
+ 0055dbd4 ["CALL", null, ["callee:0058ffcc:8"]]
- 0055db94 bytes fec80094
+ 0055dbd4 bytes fec80094
- 0055dbb4 ["INT_ADD", "register:40f0:8", ["const:55dbb4:8", "const:4:8"]]
- 0055dbb4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055dbf4 ["INT_ADD", "register:40f0:8", ["const:55dbf4:8", "const:4:8"]]
+ 0055dbf4 ["CALL", null, ["callee:00c53da0:8"]]
- 0055dbb4 bytes 53d81b94
+ 0055dbf4 bytes 6bd81b94
- 0055dbc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055dbc8 ["INT_ADD", "register:40f0:8", ["const:55dbc8:8", "const:4:8"]]
- 0055dbc8 ["CALLIND", null, ["register:0:8"]]
+ 0055dc08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055dc08 ["INT_ADD", "register:40f0:8", ["const:55dc08:8", "const:4:8"]]
+ 0055dc08 ["CALLIND", null, ["register:0:8"]]
- 0055dbc8 bytes 00013fd6
+ 0055dc08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02893ffe7ff5c00126c2e51f83040250"></a>

### [`0055ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md) → [`0055de10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055de10.md) FUN_0055de10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) · 呼出先 5件 [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0055cea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cea8.md) · 呼出先 5件 [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055de14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md#insn-0055de14) · [`0055de5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md#insn-0055de5c) · [`0055de84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md#insn-0055de84)
- 新版 [`0055de54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055de10.md#insn-0055de54) · [`0055de9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055de10.md#insn-0055de9c) · [`0055dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055de10.md#insn-0055dec4)

~~~diff
- 0055de14 ["INT_ADD", "register:40f0:8", ["const:55de14:8", "const:4:8"]]
- 0055de14 ["CALL", null, ["callee:00c57f80:8"]]
+ 0055de54 ["INT_ADD", "register:40f0:8", ["const:55de54:8", "const:4:8"]]
+ 0055de54 ["CALL", null, ["callee:00c57f80:8"]]
- 0055de14 bytes 27e81b94
+ 0055de54 bytes 4be81b94
- 0055de5c ["INT_ADD", "register:40f0:8", ["const:55de5c:8", "const:4:8"]]
- 0055de5c ["CALL", null, ["callee:00c57f60:8"]]
+ 0055de9c ["INT_ADD", "register:40f0:8", ["const:55de9c:8", "const:4:8"]]
+ 0055de9c ["CALL", null, ["callee:00c57f60:8"]]
- 0055de5c bytes 0de81b94
+ 0055de9c bytes 31e81b94
- 0055de84 ["INT_ADD", "register:40f0:8", ["const:55de84:8", "const:4:8"]]
- 0055de84 ["CALL", null, ["callee:00c580d0:8"]]
+ 0055dec4 ["INT_ADD", "register:40f0:8", ["const:55dec4:8", "const:4:8"]]
+ 0055dec4 ["CALL", null, ["callee:00c580d0:8"]]
- 0055de84 bytes 5fe81b94
+ 0055dec4 bytes 83e81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c20f292c780493d12a37a5f590065f89"></a>

### [`0055df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md) → [`0055df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055df40.md) FUN_0055df40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0055d508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d508.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055df74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md#insn-0055df74) · [`0055dfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md#insn-0055dfec) · [`0055e02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md#insn-0055e02c)
- 新版 [`0055dfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055df40.md#insn-0055dfb4) · [`0055e02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055df40.md#insn-0055e02c) · [`0055e06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055df40.md#insn-0055e06c)

~~~diff
- 0055df74 ["INT_ADD", "register:40f0:8", ["const:55df74:8", "const:4:8"]]
- 0055df74 ["CALL", null, ["callee:00c57f60:8"]]
+ 0055dfb4 ["INT_ADD", "register:40f0:8", ["const:55dfb4:8", "const:4:8"]]
+ 0055dfb4 ["CALL", null, ["callee:00c57f60:8"]]
- 0055df74 bytes c7e71b94
+ 0055dfb4 bytes ebe71b94
- 0055dfec ["INT_ADD", "register:40f0:8", ["const:55dfec:8", "const:4:8"]]
- 0055dfec ["CALL", null, ["callee:00c580d0:8"]]
+ 0055e02c ["INT_ADD", "register:40f0:8", ["const:55e02c:8", "const:4:8"]]
+ 0055e02c ["CALL", null, ["callee:00c580d0:8"]]
- 0055dfec bytes 05e81b94
+ 0055e02c bytes 29e81b94
- 0055e02c ["INT_ADD", "register:40f0:8", ["const:55e02c:8", "const:4:8"]]
- 0055e02c ["CALL", null, ["callee:0046c48c:8"]]
+ 0055e06c ["INT_ADD", "register:40f0:8", ["const:55e06c:8", "const:4:8"]]
+ 0055e06c ["CALL", null, ["callee:0046c48c:8"]]
- 0055e02c bytes 0839fc97
+ 0055e06c bytes 0839fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce30bcaffe10e8df06e0e2135bf1eda4"></a>

### [`0055e034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e034.md) → [`0055e074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e074.md) FUN_0055e074

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0055cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cdc0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e034.md#insn-0055e0b8) · [`0055e0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e034.md#insn-0055e0f0) · [`0055e158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e034.md#insn-0055e158)
- 新版 [`0055e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e074.md#insn-0055e0f8) · [`0055e130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e074.md#insn-0055e130) · [`0055e198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e074.md#insn-0055e198)

~~~diff
- 0055e0b8 ["INT_ADD", "register:40f0:8", ["const:55e0b8:8", "const:4:8"]]
- 0055e0b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0055e0f8 ["INT_ADD", "register:40f0:8", ["const:55e0f8:8", "const:4:8"]]
+ 0055e0f8 ["CALL", null, ["callee:00c57f60:8"]]
- 0055e0b8 bytes 76e71b94
+ 0055e0f8 bytes 9ae71b94
- 0055e0f0 ["INT_ADD", "register:40f0:8", ["const:55e0f0:8", "const:4:8"]]
- 0055e0f0 ["CALL", null, ["callee:00c58010:8"]]
+ 0055e130 ["INT_ADD", "register:40f0:8", ["const:55e130:8", "const:4:8"]]
+ 0055e130 ["CALL", null, ["callee:00c58010:8"]]
- 0055e0f0 bytes 94e71b94
+ 0055e130 bytes b8e71b94
- 0055e158 ["INT_ADD", "register:40f0:8", ["const:55e158:8", "const:4:8"]]
- 0055e158 ["CALL", null, ["callee:00c58010:8"]]
+ 0055e198 ["INT_ADD", "register:40f0:8", ["const:55e198:8", "const:4:8"]]
+ 0055e198 ["CALL", null, ["callee:00c58010:8"]]
- 0055e158 bytes 7ae71b94
+ 0055e198 bytes 9ee71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b72b7352f31d03a743cd62a4ba579cd4"></a>

### [`0055e218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e218.md) → [`0055e258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e258.md) FUN_0055e258

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0055cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cdc0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e218.md#insn-0055e2a0) · [`0055e2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e218.md#insn-0055e2dc) · [`0055e364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e218.md#insn-0055e364)
- 新版 [`0055e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e258.md#insn-0055e2e0) · [`0055e31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e258.md#insn-0055e31c) · [`0055e3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e258.md#insn-0055e3a4)

~~~diff
- 0055e2a0 ["INT_ADD", "register:40f0:8", ["const:55e2a0:8", "const:4:8"]]
- 0055e2a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0055e2e0 ["INT_ADD", "register:40f0:8", ["const:55e2e0:8", "const:4:8"]]
+ 0055e2e0 ["CALL", null, ["callee:00c57f60:8"]]
- 0055e2a0 bytes fce61b94
+ 0055e2e0 bytes 20e71b94
- 0055e2dc ["INT_ADD", "register:40f0:8", ["const:55e2dc:8", "const:4:8"]]
- 0055e2dc ["CALL", null, ["callee:00c58010:8"]]
+ 0055e31c ["INT_ADD", "register:40f0:8", ["const:55e31c:8", "const:4:8"]]
+ 0055e31c ["CALL", null, ["callee:00c58010:8"]]
- 0055e2dc bytes 19e71b94
+ 0055e31c bytes 3de71b94
- 0055e364 ["INT_ADD", "register:40f0:8", ["const:55e364:8", "const:4:8"]]
- 0055e364 ["CALL", null, ["callee:00c580d0:8"]]
+ 0055e3a4 ["INT_ADD", "register:40f0:8", ["const:55e3a4:8", "const:4:8"]]
+ 0055e3a4 ["CALL", null, ["callee:00c580d0:8"]]
- 0055e364 bytes 27e71b94
+ 0055e3a4 bytes 4be71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39cac6b89fa09aea80cfc6bf810e2a14"></a>

### [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) → [`0055e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md) FUN_0055e734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md#insn-0055e718) · [`0055e738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md#insn-0055e738)
- 新版 [`0055e758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md#insn-0055e758) · [`0055e778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e734.md#insn-0055e778)

~~~diff
- 0055e718 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e718 ["INT_ADD", "register:40f0:8", ["const:55e718:8", "const:4:8"]]
- 0055e718 ["CALLIND", null, ["register:0:8"]]
+ 0055e758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e758 ["INT_ADD", "register:40f0:8", ["const:55e758:8", "const:4:8"]]
+ 0055e758 ["CALLIND", null, ["register:0:8"]]
- 0055e718 bytes 00013fd6
+ 0055e758 bytes 00013fd6
- 0055e738 ["INT_ADD", "register:40f0:8", ["const:55e738:8", "const:4:8"]]
- 0055e738 ["CALL", null, ["callee:00c53d70:8"]]
+ 0055e778 ["INT_ADD", "register:40f0:8", ["const:55e778:8", "const:4:8"]]
+ 0055e778 ["CALL", null, ["callee:00c53d70:8"]]
- 0055e738 bytes 66d51b94
+ 0055e778 bytes 7ed51b94
~~~


<a id="compare-9112305e40a0e286dbb163e0897fd4cf"></a>

### [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) → [`0055e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md) FUN_0055e790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md) · 呼出先 4件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0048d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d3b0.md) · 呼出先 4件 [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md#insn-0055e780) · [`0055e79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md#insn-0055e79c) · [`0055e7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md#insn-0055e7b0)
- 新版 [`0055e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md#insn-0055e7c0) · [`0055e7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md#insn-0055e7dc) · [`0055e7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md#insn-0055e7f0)

~~~diff
- 0055e780 ["INT_ADD", "register:40f0:8", ["const:55e780:8", "const:4:8"]]
- 0055e780 ["CALL", null, ["callee:00581a74:8"]]
+ 0055e7c0 ["INT_ADD", "register:40f0:8", ["const:55e7c0:8", "const:4:8"]]
+ 0055e7c0 ["CALL", null, ["callee:00581a74:8"]]
- 0055e780 bytes ad8c0094
+ 0055e7c0 bytes ad8c0094
- 0055e79c ["COPY", "register:0:8", ["register:4048:8"]]
- 0055e79c ["INT_ADD", "register:40f0:8", ["const:55e79c:8", "const:4:8"]]
- 0055e79c ["CALLIND", null, ["register:0:8"]]
+ 0055e7dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e7dc ["INT_ADD", "register:40f0:8", ["const:55e7dc:8", "const:4:8"]]
+ 0055e7dc ["CALLIND", null, ["register:0:8"]]
- 0055e79c bytes 20013fd6
+ 0055e7dc bytes 20013fd6
- 0055e7b0 ["INT_ADD", "register:40f0:8", ["const:55e7b0:8", "const:4:8"]]
- 0055e7b0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055e7f0 ["INT_ADD", "register:40f0:8", ["const:55e7f0:8", "const:4:8"]]
+ 0055e7f0 ["CALL", null, ["callee:00c53da0:8"]]
- 0055e7b0 bytes 54d51b94
+ 0055e7f0 bytes 6cd51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5cbffaf97b3b608f6860866c335713"></a>

### [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) → [`0055e8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md) FUN_0055e8b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`0048d2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 4件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) [`0048d2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2fc.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 4件 [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md#insn-0055e8b0) · [`0055e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md#insn-0055e8c0) · [`0055e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md#insn-0055e8dc)
- 新版 [`0055e8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md#insn-0055e8f0) · [`0055e900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md#insn-0055e900) · [`0055e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md#insn-0055e91c)

~~~diff
- 0055e8b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e8b0 ["INT_ADD", "register:40f0:8", ["const:55e8b0:8", "const:4:8"]]
- 0055e8b0 ["CALLIND", null, ["register:0:8"]]
+ 0055e8f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e8f0 ["INT_ADD", "register:40f0:8", ["const:55e8f0:8", "const:4:8"]]
+ 0055e8f0 ["CALLIND", null, ["register:0:8"]]
- 0055e8b0 bytes 00013fd6
+ 0055e8f0 bytes 00013fd6
- 0055e8c0 ["INT_ADD", "register:40f0:8", ["const:55e8c0:8", "const:4:8"]]
- 0055e8c0 ["CALL", null, ["callee:00581a74:8"]]
+ 0055e900 ["INT_ADD", "register:40f0:8", ["const:55e900:8", "const:4:8"]]
+ 0055e900 ["CALL", null, ["callee:00581a74:8"]]
- 0055e8c0 bytes 5d8c0094
+ 0055e900 bytes 5d8c0094
- 0055e8dc ["COPY", "register:0:8", ["register:4048:8"]]
- 0055e8dc ["INT_ADD", "register:40f0:8", ["const:55e8dc:8", "const:4:8"]]
- 0055e8dc ["CALLIND", null, ["register:0:8"]]
+ 0055e91c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e91c ["INT_ADD", "register:40f0:8", ["const:55e91c:8", "const:4:8"]]
+ 0055e91c ["CALLIND", null, ["register:0:8"]]
- 0055e8dc bytes 20013fd6
+ 0055e91c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfdfe8dc5df26959a831ef75db58dadf"></a>

### [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md) → [`0055ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md) FUN_0055ea08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00765128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765128.md) [`00765728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765728.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`00765180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765180.md) [`00765780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 4件 [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ea14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md#insn-0055ea14) · [`0055ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md#insn-0055ea30) · [`0055ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md#insn-0055ea44)
- 新版 [`0055ea54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md#insn-0055ea54) · [`0055ea70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md#insn-0055ea70) · [`0055ea84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md#insn-0055ea84)

~~~diff
- 0055ea14 ["INT_ADD", "register:40f0:8", ["const:55ea14:8", "const:4:8"]]
- 0055ea14 ["CALL", null, ["callee:00581ae8:8"]]
+ 0055ea54 ["INT_ADD", "register:40f0:8", ["const:55ea54:8", "const:4:8"]]
+ 0055ea54 ["CALL", null, ["callee:00581ae8:8"]]
- 0055ea14 bytes 258c0094
+ 0055ea54 bytes 258c0094
- 0055ea30 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055ea30 ["INT_ADD", "register:40f0:8", ["const:55ea30:8", "const:4:8"]]
- 0055ea30 ["CALLIND", null, ["register:0:8"]]
+ 0055ea70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055ea70 ["INT_ADD", "register:40f0:8", ["const:55ea70:8", "const:4:8"]]
+ 0055ea70 ["CALLIND", null, ["register:0:8"]]
- 0055ea30 bytes 20013fd6
+ 0055ea70 bytes 20013fd6
- 0055ea44 ["INT_ADD", "register:40f0:8", ["const:55ea44:8", "const:4:8"]]
- 0055ea44 ["CALL", null, ["callee:00c53da0:8"]]
+ 0055ea84 ["INT_ADD", "register:40f0:8", ["const:55ea84:8", "const:4:8"]]
+ 0055ea84 ["CALL", null, ["callee:00c53da0:8"]]
- 0055ea44 bytes afd41b94
+ 0055ea84 bytes c7d41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323f01baee4f3bff0171901c0cd6fb98"></a>

### [`0055eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md) → [`0055eb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md) FUN_0055eb5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) · 呼出先 4件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0044ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044ff9c.md) · 呼出先 4件 [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md#insn-0055eb60) · [`0055eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md#insn-0055eb74) · [`0055eb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md#insn-0055eb90)
- 新版 [`0055eba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md#insn-0055eba0) · [`0055ebb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md#insn-0055ebb4) · [`0055ebd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md#insn-0055ebd0)

~~~diff
- 0055eb60 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055eb60 ["INT_ADD", "register:40f0:8", ["const:55eb60:8", "const:4:8"]]
- 0055eb60 ["CALLIND", null, ["register:0:8"]]
+ 0055eba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055eba0 ["INT_ADD", "register:40f0:8", ["const:55eba0:8", "const:4:8"]]
+ 0055eba0 ["CALLIND", null, ["register:0:8"]]
- 0055eb60 bytes 00013fd6
+ 0055eba0 bytes 00013fd6
- 0055eb74 ["INT_ADD", "register:40f0:8", ["const:55eb74:8", "const:4:8"]]
- 0055eb74 ["CALL", null, ["callee:00581ae8:8"]]
+ 0055ebb4 ["INT_ADD", "register:40f0:8", ["const:55ebb4:8", "const:4:8"]]
+ 0055ebb4 ["CALL", null, ["callee:00581ae8:8"]]
- 0055eb74 bytes cd8b0094
+ 0055ebb4 bytes cd8b0094
- 0055eb90 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055eb90 ["INT_ADD", "register:40f0:8", ["const:55eb90:8", "const:4:8"]]
- 0055eb90 ["CALLIND", null, ["register:0:8"]]
+ 0055ebd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055ebd0 ["INT_ADD", "register:40f0:8", ["const:55ebd0:8", "const:4:8"]]
+ 0055ebd0 ["CALLIND", null, ["register:0:8"]]
- 0055eb90 bytes 20013fd6
+ 0055ebd0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af1f33fafaefa778a36bb9de394b316"></a>

### [`0055ece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ece0.md) → [`0055ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ed20.md) FUN_0055ed20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ece0.md#insn-0055ecfc)
- 新版 [`0055ed3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ed20.md#insn-0055ed3c)

~~~diff
- 0055ecfc ["INT_ADD", "register:40f0:8", ["const:55ecfc:8", "const:4:8"]]
- 0055ecfc ["CALL", null, ["callee:00c53d70:8"]]
+ 0055ed3c ["INT_ADD", "register:40f0:8", ["const:55ed3c:8", "const:4:8"]]
+ 0055ed3c ["CALL", null, ["callee:00c53d70:8"]]
- 0055ecfc bytes f5d31b94
+ 0055ed3c bytes 0dd41b94
~~~


<a id="compare-424aa123a4d1075f353569d2e500a8b1"></a>

### [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) → [`0055f0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md) FUN_0055f0d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md) [`0048d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d91c.md) · 呼出先 5件 [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0048d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d85c.md) [`0048d95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d95c.md) · 呼出先 5件 [`005817a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md) [`00597658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597658.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055f0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md#insn-0055f0e0) · [`0055f0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md#insn-0055f0f8) · [`0055f114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md#insn-0055f114)
- 新版 [`0055f120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md#insn-0055f120) · [`0055f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md#insn-0055f138) · [`0055f154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md#insn-0055f154)

~~~diff
- 0055f0e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055f0e0 ["INT_ADD", "register:40f0:8", ["const:55f0e0:8", "const:4:8"]]
- 0055f0e0 ["CALLIND", null, ["register:0:8"]]
+ 0055f120 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055f120 ["INT_ADD", "register:40f0:8", ["const:55f120:8", "const:4:8"]]
+ 0055f120 ["CALLIND", null, ["register:0:8"]]
- 0055f0e0 bytes 00013fd6
+ 0055f120 bytes 00013fd6
- 0055f0f8 ["INT_ADD", "register:40f0:8", ["const:55f0f8:8", "const:4:8"]]
- 0055f0f8 ["CALL", null, ["callee:005817a4:8"]]
+ 0055f138 ["INT_ADD", "register:40f0:8", ["const:55f138:8", "const:4:8"]]
+ 0055f138 ["CALL", null, ["callee:005817a4:8"]]
- 0055f0f8 bytes 9b890094
+ 0055f138 bytes 9b890094
- 0055f114 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055f114 ["INT_ADD", "register:40f0:8", ["const:55f114:8", "const:4:8"]]
- 0055f114 ["CALLIND", null, ["register:0:8"]]
+ 0055f154 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055f154 ["INT_ADD", "register:40f0:8", ["const:55f154:8", "const:4:8"]]
+ 0055f154 ["CALLIND", null, ["register:0:8"]]
- 0055f114 bytes 20013fd6
+ 0055f154 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353736b000c90797c02265fc08806325"></a>

### [`0055fc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md) → [`0055fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fcbc.md) FUN_0055fcbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055fcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md#insn-0055fcac) · [`0055fcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md#insn-0055fcd0)
- 新版 [`0055fcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fcbc.md#insn-0055fcec) · [`0055fd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fcbc.md#insn-0055fd10)

~~~diff
- 0055fcac ["INT_ADD", "register:40f0:8", ["const:55fcac:8", "const:4:8"]]
- 0055fcac ["CALL", null, ["callee:0046db40:8"]]
+ 0055fcec ["INT_ADD", "register:40f0:8", ["const:55fcec:8", "const:4:8"]]
+ 0055fcec ["CALL", null, ["callee:0046db40:8"]]
- 0055fcac bytes 9537fc97
+ 0055fcec bytes 9537fc97
- 0055fcd0 ["INT_ADD", "register:40f0:8", ["const:55fcd0:8", "const:4:8"]]
- 0055fcd0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055fd10 ["INT_ADD", "register:40f0:8", ["const:55fd10:8", "const:4:8"]]
+ 0055fd10 ["CALL", null, ["callee:00c57fb0:8"]]
- 0055fcd0 bytes 84e01b94
+ 0055fd10 bytes a8e01b94
~~~


<a id="compare-1a83dd36afe39d002040d0bf4f7b37d6"></a>

### [`0055fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md) → [`0055fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fd14.md) FUN_0055fd14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md#insn-0055fd04) · [`0055fd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md#insn-0055fd28)
- 新版 [`0055fd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fd14.md#insn-0055fd44) · [`0055fd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fd14.md#insn-0055fd68)

~~~diff
- 0055fd04 ["INT_ADD", "register:40f0:8", ["const:55fd04:8", "const:4:8"]]
- 0055fd04 ["CALL", null, ["callee:0046db40:8"]]
+ 0055fd44 ["INT_ADD", "register:40f0:8", ["const:55fd44:8", "const:4:8"]]
+ 0055fd44 ["CALL", null, ["callee:0046db40:8"]]
- 0055fd04 bytes 7f37fc97
+ 0055fd44 bytes 7f37fc97
- 0055fd28 ["INT_ADD", "register:40f0:8", ["const:55fd28:8", "const:4:8"]]
- 0055fd28 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055fd68 ["INT_ADD", "register:40f0:8", ["const:55fd68:8", "const:4:8"]]
+ 0055fd68 ["CALL", null, ["callee:00c57fb0:8"]]
- 0055fd28 bytes 6ee01b94
+ 0055fd68 bytes 92e01b94
~~~


<a id="compare-d63c22770a13179ed0c95f43e537eb9e"></a>

### [`0055febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md) → [`0055fefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fefc.md) FUN_0055fefc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056056c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005605ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005605ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md#insn-0055fef0) · [`0055ff14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md#insn-0055ff14)
- 新版 [`0055ff30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fefc.md#insn-0055ff30) · [`0055ff54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fefc.md#insn-0055ff54)

~~~diff
- 0055fef0 ["INT_ADD", "register:40f0:8", ["const:55fef0:8", "const:4:8"]]
- 0055fef0 ["CALL", null, ["callee:005605ac:8"]]
+ 0055ff30 ["INT_ADD", "register:40f0:8", ["const:55ff30:8", "const:4:8"]]
+ 0055ff30 ["CALL", null, ["callee:005605ac:8"]]
- 0055fef0 bytes 9f010094
+ 0055ff30 bytes 9f010094
- 0055ff14 ["INT_ADD", "register:40f0:8", ["const:55ff14:8", "const:4:8"]]
- 0055ff14 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0055ff54 ["INT_ADD", "register:40f0:8", ["const:55ff54:8", "const:4:8"]]
+ 0055ff54 ["CALL", null, ["callee:00c57fb0:8"]]
- 0055ff14 bytes f3df1b94
+ 0055ff54 bytes 17e01b94
~~~


<a id="compare-ce3438faab4a6fe0478fa32c18fad7b0"></a>

### [`00560468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md) → [`005604a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a8.md) FUN_005604a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`0055f618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0055f5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5b8.md) [`0055f658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f658.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md#insn-00560484) · [`005604a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md#insn-005604a4)
- 新版 [`005604c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a8.md#insn-005604c4) · [`005604e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a8.md#insn-005604e4)

~~~diff
- 00560484 ["INT_ADD", "register:40f0:8", ["const:560484:8", "const:4:8"]]
- 00560484 ["CALL", null, ["callee:00c53da0:8"]]
+ 005604c4 ["INT_ADD", "register:40f0:8", ["const:5604c4:8", "const:4:8"]]
+ 005604c4 ["CALL", null, ["callee:00c53da0:8"]]
- 00560484 bytes 1fce1b94
+ 005604c4 bytes 37ce1b94
- 005604a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005604a4 ["INT_ADD", "register:40f0:8", ["const:5604a4:8", "const:4:8"]]
- 005604a4 ["CALLIND", null, ["register:0:8"]]
+ 005604e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005604e4 ["INT_ADD", "register:40f0:8", ["const:5604e4:8", "const:4:8"]]
+ 005604e4 ["CALLIND", null, ["register:0:8"]]
- 005604a4 bytes 00013fd6
+ 005604e4 bytes 00013fd6
~~~


<a id="compare-7056003ae796840e1b1e58449160e26c"></a>

### [`0056056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056056c.md) → [`005605ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005605ac.md) FUN_005605ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md) · 呼出先 1件 [`00c59fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59fe0.md)
- 新版 呼出元 1件 [`0055fefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fefc.md) · 呼出先 1件 [`00c5a0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056056c.md#insn-00560700)
- 新版 [`00560740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005605ac.md#insn-00560740)

~~~diff
- 00560700 ["INT_ADD", "register:40f0:8", ["const:560700:8", "const:4:8"]]
- 00560700 ["CALL", null, ["callee:00c5a0b0:8"]]
+ 00560740 ["INT_ADD", "register:40f0:8", ["const:560740:8", "const:4:8"]]
+ 00560740 ["CALL", null, ["callee:00c5a0b0:8"]]
- 00560700 bytes 38e61b94
+ 00560740 bytes 5ce61b94
~~~


<a id="compare-74ceec8edf5a98d35e49bb45cf32d3de"></a>

### [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) → [`00560b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md) FUN_00560b48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) · 呼出先 2件 [`00560ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) · 呼出先 2件 [`00560f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md#insn-00560b28) · [`00560b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md#insn-00560b38)
- 新版 [`00560b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md#insn-00560b68) · [`00560b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md#insn-00560b78)

~~~diff
- 00560b28 ["INT_ADD", "register:40f0:8", ["const:560b28:8", "const:4:8"]]
- 00560b28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00560b68 ["INT_ADD", "register:40f0:8", ["const:560b68:8", "const:4:8"]]
+ 00560b68 ["CALL", null, ["callee:00c57f60:8"]]
- 00560b28 bytes dadc1b94
+ 00560b68 bytes fedc1b94
- 00560b38 ["INT_ADD", "register:40f0:8", ["const:560b38:8", "const:4:8"]]
- 00560b38 ["CALL", null, ["callee:00560f20:8"]]
+ 00560b78 ["INT_ADD", "register:40f0:8", ["const:560b78:8", "const:4:8"]]
+ 00560b78 ["CALL", null, ["callee:00560f20:8"]]
- 00560b38 bytes ea000094
+ 00560b78 bytes ea000094
~~~


<a id="compare-546f4c3145f9a1a7bbe9b7ffaf862599"></a>

### [`00560e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e48.md) → [`00560e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560e88.md) FUN_00560e88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005608a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005608e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005608e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e48.md#insn-00560e84)
- 新版 [`00560ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560e88.md#insn-00560ec4)

~~~diff
- 00560e84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560e84 ["INT_ADD", "register:40f0:8", ["const:560e84:8", "const:4:8"]]
- 00560e84 ["CALLIND", null, ["register:0:8"]]
+ 00560ec4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560ec4 ["INT_ADD", "register:40f0:8", ["const:560ec4:8", "const:4:8"]]
+ 00560ec4 ["CALLIND", null, ["register:0:8"]]
- 00560e84 bytes 00013fd6
+ 00560ec4 bytes 00013fd6
~~~


<a id="compare-6ba8bfb7ee89c5a487ca0cc05fda0f23"></a>

### [`00560e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e98.md) → [`00560ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ed8.md) FUN_00560ed8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e98.md#insn-00560eb4)
- 新版 [`00560ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ed8.md#insn-00560ef4)

~~~diff
- 00560eb4 ["INT_ADD", "register:40f0:8", ["const:560eb4:8", "const:4:8"]]
- 00560eb4 ["CALL", null, ["callee:00459db4:8"]]
+ 00560ef4 ["INT_ADD", "register:40f0:8", ["const:560ef4:8", "const:4:8"]]
+ 00560ef4 ["CALL", null, ["callee:00459db4:8"]]
- 00560eb4 bytes b0e3fb97
+ 00560ef4 bytes b0e3fb97
~~~


<a id="compare-1765465dd69901576d9481eb643a0b2f"></a>

### [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) → [`00561054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md) FUN_00561054

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 2件 [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md)
- 新版 呼出元 1件 [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 2件 [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) [`00563008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md#insn-00561034) · [`00561048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md#insn-00561048)
- 新版 [`00561074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md#insn-00561074) · [`00561088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md#insn-00561088)

~~~diff
- 00561034 ["INT_ADD", "register:40f0:8", ["const:561034:8", "const:4:8"]]
- 00561034 ["CALL", null, ["callee:00563008:8"]]
+ 00561074 ["INT_ADD", "register:40f0:8", ["const:561074:8", "const:4:8"]]
+ 00561074 ["CALL", null, ["callee:00563008:8"]]
- 00561034 bytes e5070094
+ 00561074 bytes e5070094
- 00561048 ["INT_ADD", "register:40f0:8", ["const:561048:8", "const:4:8"]]
- 00561048 ["CALL", null, ["callee:00562dd0:8"]]
+ 00561088 ["INT_ADD", "register:40f0:8", ["const:561088:8", "const:4:8"]]
+ 00561088 ["CALL", null, ["callee:00562dd0:8"]]
- 00561048 bytes 52070094
+ 00561088 bytes 52070094
~~~


<a id="compare-a2226baee11f7fcf4b3b1dbde194cb2b"></a>

### [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) → [`005610a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md) FUN_005610a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 2件 [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md)
- 新版 呼出元 2件 [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 2件 [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) [`00563320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md#insn-00561084) · [`00561098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md#insn-00561098)
- 新版 [`005610c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md#insn-005610c4) · [`005610d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md#insn-005610d8)

~~~diff
- 00561084 ["INT_ADD", "register:40f0:8", ["const:561084:8", "const:4:8"]]
- 00561084 ["CALL", null, ["callee:00563320:8"]]
+ 005610c4 ["INT_ADD", "register:40f0:8", ["const:5610c4:8", "const:4:8"]]
+ 005610c4 ["CALL", null, ["callee:00563320:8"]]
- 00561084 bytes 97080094
+ 005610c4 bytes 97080094
- 00561098 ["INT_ADD", "register:40f0:8", ["const:561098:8", "const:4:8"]]
- 00561098 ["CALL", null, ["callee:005630d8:8"]]
+ 005610d8 ["INT_ADD", "register:40f0:8", ["const:5610d8:8", "const:4:8"]]
+ 005610d8 ["CALL", null, ["callee:005630d8:8"]]
- 00561098 bytes 00080094
+ 005610d8 bytes 00080094
~~~


<a id="compare-3c31b137fa28a092913421e003dc2f82"></a>

### [`00561f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561f8c.md) → [`00561fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561fcc.md) FUN_00561fcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561f8c.md#insn-00561fa8)
- 新版 [`00561fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561fcc.md#insn-00561fe8)

~~~diff
- 00561fa8 ["INT_ADD", "register:40f0:8", ["const:561fa8:8", "const:4:8"]]
- 00561fa8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00561fe8 ["INT_ADD", "register:40f0:8", ["const:561fe8:8", "const:4:8"]]
+ 00561fe8 ["CALL", null, ["callee:00c57f80:8"]]
- 00561fa8 bytes c2d71b94
+ 00561fe8 bytes e6d71b94
~~~


<a id="compare-6332e5c827f8d45458d3e05db3824283"></a>

### [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) → [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) FUN_00562734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006d02a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d02a4.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 20件 [`00562010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md) [`005638dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006d02fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02fc.md) · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005627d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md#insn-005627d4) · [`005627e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md#insn-005627e8) · [`00562884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md#insn-00562884)
- 新版 [`00562814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md#insn-00562814) · [`00562828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md#insn-00562828) · [`005628c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md#insn-005628c4)

~~~diff
- 005627d4 ["INT_ADD", "register:40f0:8", ["const:5627d4:8", "const:4:8"]]
- 005627d4 ["CALL", null, ["callee:00c580a0:8"]]
+ 00562814 ["INT_ADD", "register:40f0:8", ["const:562814:8", "const:4:8"]]
+ 00562814 ["CALL", null, ["callee:00c580a0:8"]]
- 005627d4 bytes ffd51b94
+ 00562814 bytes 23d61b94
- 005627e8 ["INT_ADD", "register:40f0:8", ["const:5627e8:8", "const:4:8"]]
- 005627e8 ["CALL", null, ["callee:00c58120:8"]]
+ 00562828 ["INT_ADD", "register:40f0:8", ["const:562828:8", "const:4:8"]]
+ 00562828 ["CALL", null, ["callee:00c58120:8"]]
- 005627e8 bytes 1ad61b94
+ 00562828 bytes 3ed61b94
- 00562884 ["INT_ADD", "register:40f0:8", ["const:562884:8", "const:4:8"]]
- 00562884 ["CALL", null, ["callee:00c57f60:8"]]
+ 005628c4 ["INT_ADD", "register:40f0:8", ["const:5628c4:8", "const:4:8"]]
+ 005628c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00562884 bytes 83d51b94
+ 005628c4 bytes a7d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa7b7473d2384e8ff6270ed0423f407"></a>

### [`00562c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562c84.md) → [`00562cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562cc4.md) FUN_00562cc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562c84.md#insn-00562cac)
- 新版 [`00562cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562cc4.md#insn-00562cec)

~~~diff
- 00562cac ["INT_ADD", "register:40f0:8", ["const:562cac:8", "const:4:8"]]
- 00562cac ["CALL", null, ["callee:00562d30:8"]]
+ 00562cec ["INT_ADD", "register:40f0:8", ["const:562cec:8", "const:4:8"]]
+ 00562cec ["CALL", null, ["callee:00562d30:8"]]
- 00562cac bytes 11000094
+ 00562cec bytes 11000094
~~~


<a id="compare-81e9206721221988bad5e0e8faa8a804"></a>

### [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) → [`00562d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md) FUN_00562d30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00562c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562c84.md) [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) [`00563424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563424.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00562cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562cc4.md) [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) [`00563464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563464.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md#insn-00562d28) · [`00562d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md#insn-00562d38) · [`00562d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md#insn-00562d48)
- 新版 [`00562d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md#insn-00562d68) · [`00562d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md#insn-00562d78) · [`00562d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md#insn-00562d88)

~~~diff
- 00562d28 ["INT_ADD", "register:40f0:8", ["const:562d28:8", "const:4:8"]]
- 00562d28 ["CALL", null, ["callee:00c57f80:8"]]
+ 00562d68 ["INT_ADD", "register:40f0:8", ["const:562d68:8", "const:4:8"]]
+ 00562d68 ["CALL", null, ["callee:00c57f80:8"]]
- 00562d28 bytes 62d41b94
+ 00562d68 bytes 86d41b94
- 00562d38 ["INT_ADD", "register:40f0:8", ["const:562d38:8", "const:4:8"]]
- 00562d38 ["CALL", null, ["callee:00c57f80:8"]]
+ 00562d78 ["INT_ADD", "register:40f0:8", ["const:562d78:8", "const:4:8"]]
+ 00562d78 ["CALL", null, ["callee:00c57f80:8"]]
- 00562d38 bytes 5ed41b94
+ 00562d78 bytes 82d41b94
- 00562d48 ["INT_ADD", "register:40f0:8", ["const:562d48:8", "const:4:8"]]
- 00562d48 ["CALL", null, ["callee:00c57f80:8"]]
+ 00562d88 ["INT_ADD", "register:40f0:8", ["const:562d88:8", "const:4:8"]]
+ 00562d88 ["CALL", null, ["callee:00c57f80:8"]]
- 00562d48 bytes 5ad41b94
+ 00562d88 bytes 7ed41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435e1d4afba24d0c5c73b45605083001"></a>

### [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) → [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) FUN_00562dd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00561054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00562d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md) [`00562d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md) [`00563008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md#insn-00562e54) · [`00562e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md#insn-00562e84) · [`00562f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md#insn-00562f18)
- 新版 [`00562e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md#insn-00562e94) · [`00562ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md#insn-00562ec4) · [`00562f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md#insn-00562f58)

~~~diff
- 00562e54 ["INT_ADD", "register:40f0:8", ["const:562e54:8", "const:4:8"]]
- 00562e54 ["CALL", null, ["callee:00c57f60:8"]]
+ 00562e94 ["INT_ADD", "register:40f0:8", ["const:562e94:8", "const:4:8"]]
+ 00562e94 ["CALL", null, ["callee:00c57f60:8"]]
- 00562e54 bytes 0fd41b94
+ 00562e94 bytes 33d41b94
- 00562e84 ["INT_ADD", "register:40f0:8", ["const:562e84:8", "const:4:8"]]
- 00562e84 ["CALL", null, ["callee:00563008:8"]]
+ 00562ec4 ["INT_ADD", "register:40f0:8", ["const:562ec4:8", "const:4:8"]]
+ 00562ec4 ["CALL", null, ["callee:00563008:8"]]
- 00562e84 bytes 51000094
+ 00562ec4 bytes 51000094
- 00562f18 ["INT_ADD", "register:40f0:8", ["const:562f18:8", "const:4:8"]]
- 00562f18 ["CALL", null, ["callee:00562d30:8"]]
+ 00562f58 ["INT_ADD", "register:40f0:8", ["const:562f58:8", "const:4:8"]]
+ 00562f58 ["CALL", null, ["callee:00562d30:8"]]
- 00562f18 bytes 76ffff97
+ 00562f58 bytes 76ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b100a344860d35a87bb21451c99d701d"></a>

### [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md) → [`00563008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md) FUN_00563008

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md)
- 新版 呼出元 2件 [`00561054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md) [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md#insn-00562fec) · [`00563014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md#insn-00563014) · [`00563048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md#insn-00563048)
- 新版 [`0056302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md#insn-0056302c) · [`00563054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md#insn-00563054) · [`00563088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563008.md#insn-00563088)

~~~diff
- 00562fec ["INT_ADD", "register:40f0:8", ["const:562fec:8", "const:4:8"]]
- 00562fec ["CALL", null, ["callee:00597648:8"]]
+ 0056302c ["INT_ADD", "register:40f0:8", ["const:56302c:8", "const:4:8"]]
+ 0056302c ["CALL", null, ["callee:00597648:8"]]
- 00562fec bytes 87d10094
+ 0056302c bytes 87d10094
- 00563014 ["INT_ADD", "register:40f0:8", ["const:563014:8", "const:4:8"]]
- 00563014 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563054 ["INT_ADD", "register:40f0:8", ["const:563054:8", "const:4:8"]]
+ 00563054 ["CALL", null, ["callee:0043bb60:8"]]
- 00563014 bytes c362fb97
+ 00563054 bytes c362fb97
- 00563048 ["INT_ADD", "register:40f0:8", ["const:563048:8", "const:4:8"]]
- 00563048 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563088 ["INT_ADD", "register:40f0:8", ["const:563088:8", "const:4:8"]]
+ 00563088 ["CALL", null, ["callee:0043bb60:8"]]
- 00563048 bytes b662fb97
+ 00563088 bytes b662fb97
~~~


<a id="compare-fc06628f6640a4b14061f02e57570a4d"></a>

### [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) → [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) FUN_005630d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005610a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00562d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md) [`00562d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md) [`00563320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md#insn-00563164) · [`00563198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md#insn-00563198) · [`0056322c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md#insn-0056322c)
- 新版 [`005631a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md#insn-005631a4) · [`005631d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md#insn-005631d8) · [`0056326c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md#insn-0056326c)

~~~diff
- 00563164 ["INT_ADD", "register:40f0:8", ["const:563164:8", "const:4:8"]]
- 00563164 ["CALL", null, ["callee:00c57f60:8"]]
+ 005631a4 ["INT_ADD", "register:40f0:8", ["const:5631a4:8", "const:4:8"]]
+ 005631a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00563164 bytes 4bd31b94
+ 005631a4 bytes 6fd31b94
- 00563198 ["INT_ADD", "register:40f0:8", ["const:563198:8", "const:4:8"]]
- 00563198 ["CALL", null, ["callee:00563320:8"]]
+ 005631d8 ["INT_ADD", "register:40f0:8", ["const:5631d8:8", "const:4:8"]]
+ 005631d8 ["CALL", null, ["callee:00563320:8"]]
- 00563198 bytes 52000094
+ 005631d8 bytes 52000094
- 0056322c ["INT_ADD", "register:40f0:8", ["const:56322c:8", "const:4:8"]]
- 0056322c ["CALL", null, ["callee:00562d30:8"]]
+ 0056326c ["INT_ADD", "register:40f0:8", ["const:56326c:8", "const:4:8"]]
+ 0056326c ["CALL", null, ["callee:00562d30:8"]]
- 0056322c bytes b1feff97
+ 0056326c bytes b1feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad94bc390e03e434ce76372601eda90c"></a>

### [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md) → [`00563320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md) FUN_00563320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 2件 [`005610a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md) [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md#insn-00563314) · [`0056333c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md#insn-0056333c) · [`00563364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md#insn-00563364)
- 新版 [`00563354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md#insn-00563354) · [`0056337c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md#insn-0056337c) · [`005633a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563320.md#insn-005633a4)

~~~diff
- 00563314 ["INT_ADD", "register:40f0:8", ["const:563314:8", "const:4:8"]]
- 00563314 ["CALL", null, ["callee:00c53d70:8"]]
+ 00563354 ["INT_ADD", "register:40f0:8", ["const:563354:8", "const:4:8"]]
+ 00563354 ["CALL", null, ["callee:00c53d70:8"]]
- 00563314 bytes 6fc21b94
+ 00563354 bytes 87c21b94
- 0056333c ["INT_ADD", "register:40f0:8", ["const:56333c:8", "const:4:8"]]
- 0056333c ["CALL", null, ["callee:0043bb60:8"]]
+ 0056337c ["INT_ADD", "register:40f0:8", ["const:56337c:8", "const:4:8"]]
+ 0056337c ["CALL", null, ["callee:0043bb60:8"]]
- 0056333c bytes f961fb97
+ 0056337c bytes f961fb97
- 00563364 ["INT_ADD", "register:40f0:8", ["const:563364:8", "const:4:8"]]
- 00563364 ["CALL", null, ["callee:0043bb60:8"]]
+ 005633a4 ["INT_ADD", "register:40f0:8", ["const:5633a4:8", "const:4:8"]]
+ 005633a4 ["CALL", null, ["callee:0043bb60:8"]]
- 00563364 bytes ef61fb97
+ 005633a4 bytes ef61fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d71b58cfee4784aa723ac8565c9ecc6"></a>

### [`00563424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563424.md) → [`00563464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563464.md) FUN_00563464

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056345c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563424.md#insn-0056345c)
- 新版 [`0056349c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563464.md#insn-0056349c)

~~~diff
- 0056345c ["INT_ADD", "register:40f0:8", ["const:56345c:8", "const:4:8"]]
- 0056345c ["CALL", null, ["callee:00562d30:8"]]
+ 0056349c ["INT_ADD", "register:40f0:8", ["const:56349c:8", "const:4:8"]]
+ 0056349c ["CALL", null, ["callee:00562d30:8"]]
- 0056345c bytes 25feff97
+ 0056349c bytes 25feff97
~~~


<a id="compare-e09e18a973e9d108e360836c07d70916"></a>

### [`0056370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056370c.md) → [`0056374c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056374c.md) FUN_0056374c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056370c.md#insn-00563728)
- 新版 [`00563768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056374c.md#insn-00563768)

~~~diff
- 00563728 ["INT_ADD", "register:40f0:8", ["const:563728:8", "const:4:8"]]
- 00563728 ["CALL", null, ["callee:00c57f80:8"]]
+ 00563768 ["INT_ADD", "register:40f0:8", ["const:563768:8", "const:4:8"]]
+ 00563768 ["CALL", null, ["callee:00c57f80:8"]]
- 00563728 bytes e2d11b94
+ 00563768 bytes 06d21b94
~~~


<a id="compare-06a5ee375c193c2882d05ad23d31fefb"></a>

### [`00563750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md) → [`00563790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563790.md) FUN_00563790

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md#insn-0056376c) · [`0056377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md#insn-0056377c)
- 新版 [`005637ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563790.md#insn-005637ac) · [`005637bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563790.md#insn-005637bc)

~~~diff
- 0056376c ["INT_ADD", "register:40f0:8", ["const:56376c:8", "const:4:8"]]
- 0056376c ["CALL", null, ["callee:00c57f80:8"]]
+ 005637ac ["INT_ADD", "register:40f0:8", ["const:5637ac:8", "const:4:8"]]
+ 005637ac ["CALL", null, ["callee:00c57f80:8"]]
- 0056376c bytes d1d11b94
+ 005637ac bytes f5d11b94
- 0056377c ["INT_ADD", "register:40f0:8", ["const:56377c:8", "const:4:8"]]
- 0056377c ["CALL", null, ["callee:00c57f80:8"]]
+ 005637bc ["INT_ADD", "register:40f0:8", ["const:5637bc:8", "const:4:8"]]
+ 005637bc ["CALL", null, ["callee:00c57f80:8"]]
- 0056377c bytes cdd11b94
+ 005637bc bytes f1d11b94
~~~


<a id="compare-afd12c5fc0fa436790a8351e2c369b46"></a>

### [`00563b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md) → [`00563b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md) FUN_00563b44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005638dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md#insn-00563b54) · [`00563b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md#insn-00563b80) · [`00563b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md#insn-00563b8c)
- 新版 [`00563b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md#insn-00563b94) · [`00563bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md#insn-00563bc0) · [`00563bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md#insn-00563bcc)

~~~diff
- 00563b54 ["INT_ADD", "register:40f0:8", ["const:563b54:8", "const:4:8"]]
- 00563b54 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563b94 ["INT_ADD", "register:40f0:8", ["const:563b94:8", "const:4:8"]]
+ 00563b94 ["CALL", null, ["callee:0043bb60:8"]]
- 00563b54 bytes f35ffb97
+ 00563b94 bytes f35ffb97
- 00563b80 ["INT_ADD", "register:40f0:8", ["const:563b80:8", "const:4:8"]]
- 00563b80 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563bc0 ["INT_ADD", "register:40f0:8", ["const:563bc0:8", "const:4:8"]]
+ 00563bc0 ["CALL", null, ["callee:0043bb60:8"]]
- 00563b80 bytes e85ffb97
+ 00563bc0 bytes e85ffb97
- 00563b8c ["INT_ADD", "register:40f0:8", ["const:563b8c:8", "const:4:8"]]
- 00563b8c ["CALL", null, ["callee:00549114:8"]]
+ 00563bcc ["INT_ADD", "register:40f0:8", ["const:563bcc:8", "const:4:8"]]
+ 00563bcc ["CALL", null, ["callee:00549114:8"]]
- 00563b8c bytes 5295ff97
+ 00563bcc bytes 5295ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adbb230890b1db9095ee30d3cef77f8b"></a>

### [`00563c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md) → [`00563c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563c54.md) FUN_00563c54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00547bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bf0.md) [`00564320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md#insn-00563c28) · [`00563c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md#insn-00563c44)
- 新版 [`00563c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563c54.md#insn-00563c68) · [`00563c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563c54.md#insn-00563c84)

~~~diff
- 00563c28 ["INT_ADD", "register:40f0:8", ["const:563c28:8", "const:4:8"]]
- 00563c28 ["CALL", null, ["callee:00547bf0:8"]]
+ 00563c68 ["INT_ADD", "register:40f0:8", ["const:563c68:8", "const:4:8"]]
+ 00563c68 ["CALL", null, ["callee:00547bf0:8"]]
- 00563c28 bytes e28fff97
+ 00563c68 bytes e28fff97
- 00563c44 ["INT_ADD", "register:40f0:8", ["const:563c44:8", "const:4:8"]]
- 00563c44 ["CALL", null, ["callee:00564320:8"]]
+ 00563c84 ["INT_ADD", "register:40f0:8", ["const:563c84:8", "const:4:8"]]
+ 00563c84 ["CALL", null, ["callee:00564320:8"]]
- 00563c44 bytes a7010094
+ 00563c84 bytes a7010094
~~~


<a id="compare-e94099355cbf4a67939f239d4e71646d"></a>

### [`00563c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c60.md) → [`00563ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563ca0.md) FUN_00563ca0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c60.md#insn-00563c78)
- 新版 [`00563cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563ca0.md#insn-00563cb8)

~~~diff
- 00563c78 ["INT_ADD", "register:40f0:8", ["const:563c78:8", "const:4:8"]]
- 00563c78 ["CALL", null, ["callee:00493e08:8"]]
+ 00563cb8 ["INT_ADD", "register:40f0:8", ["const:563cb8:8", "const:4:8"]]
+ 00563cb8 ["CALL", null, ["callee:00493e08:8"]]
- 00563c78 bytes 54c0fc97
+ 00563cb8 bytes 54c0fc97
~~~


<a id="compare-fef79bf91c80cd1d11f98e3596674f15"></a>

### [`00563ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563ccc.md) → [`00563d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563d0c.md) FUN_00563d0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563ccc.md#insn-00563ce4) · [`00563d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563ccc.md#insn-00563d44) · [`00563d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563ccc.md#insn-00563d58)
- 新版 [`00563d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563d0c.md#insn-00563d24) · [`00563d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563d0c.md#insn-00563d84) · [`00563d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563d0c.md#insn-00563d98)

~~~diff
- 00563ce4 ["INT_ADD", "register:40f0:8", ["const:563ce4:8", "const:4:8"]]
- 00563ce4 ["CALL", null, ["callee:005480d8:8"]]
+ 00563d24 ["INT_ADD", "register:40f0:8", ["const:563d24:8", "const:4:8"]]
+ 00563d24 ["CALL", null, ["callee:005480d8:8"]]
- 00563ce4 bytes ed90ff97
+ 00563d24 bytes ed90ff97
- 00563d44 ["INT_ADD", "register:40f0:8", ["const:563d44:8", "const:4:8"]]
- 00563d44 ["CALL", null, ["callee:00540dbc:8"]]
+ 00563d84 ["INT_ADD", "register:40f0:8", ["const:563d84:8", "const:4:8"]]
+ 00563d84 ["CALL", null, ["callee:00540dbc:8"]]
- 00563d44 bytes 0e74ff97
+ 00563d84 bytes 0e74ff97
- 00563d58 ["INT_ADD", "register:40f0:8", ["const:563d58:8", "const:4:8"]]
- 00563d58 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563d98 ["INT_ADD", "register:40f0:8", ["const:563d98:8", "const:4:8"]]
+ 00563d98 ["CALL", null, ["callee:0043bb60:8"]]
- 00563d58 bytes 725ffb97
+ 00563d98 bytes 725ffb97
~~~


<a id="compare-7e3350eada969ece1a05ef72b5cf604e"></a>

### [`00563dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563dc4.md) → [`00563e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e04.md) FUN_00563e04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00564380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005643c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005643c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563dc4.md#insn-00563dd0)
- 新版 [`00563e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e04.md#insn-00563e10)

~~~diff
- 00563dd0 ["INT_ADD", "register:40f0:8", ["const:563dd0:8", "const:4:8"]]
- 00563dd0 ["CALL", null, ["callee:005643c0:8"]]
+ 00563e10 ["INT_ADD", "register:40f0:8", ["const:563e10:8", "const:4:8"]]
+ 00563e10 ["CALL", null, ["callee:005643c0:8"]]
- 00563dd0 bytes 6c010094
+ 00563e10 bytes 6c010094
~~~


<a id="compare-c94f6989d9fd0332b4167815b6a75024"></a>

### [`00563e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md) → [`00563e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md) FUN_00563e70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00564588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`005645c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md#insn-00563ed8) · [`00563f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md#insn-00563f0c) · [`00563f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md#insn-00563f70)
- 新版 [`00563f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md#insn-00563f18) · [`00563f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md#insn-00563f4c) · [`00563fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md#insn-00563fb0)

~~~diff
- 00563ed8 ["INT_ADD", "register:40f0:8", ["const:563ed8:8", "const:4:8"]]
- 00563ed8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00563f18 ["INT_ADD", "register:40f0:8", ["const:563f18:8", "const:4:8"]]
+ 00563f18 ["CALL", null, ["callee:0043bb60:8"]]
- 00563ed8 bytes 125ffb97
+ 00563f18 bytes 125ffb97
- 00563f0c ["INT_ADD", "register:40f0:8", ["const:563f0c:8", "const:4:8"]]
- 00563f0c ["CALL", null, ["callee:0043bb60:8"]]
+ 00563f4c ["INT_ADD", "register:40f0:8", ["const:563f4c:8", "const:4:8"]]
+ 00563f4c ["CALL", null, ["callee:0043bb60:8"]]
- 00563f0c bytes 055ffb97
+ 00563f4c bytes 055ffb97
- 00563f70 ["INT_ADD", "register:40f0:8", ["const:563f70:8", "const:4:8"]]
- 00563f70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00563fb0 ["INT_ADD", "register:40f0:8", ["const:563fb0:8", "const:4:8"]]
+ 00563fb0 ["CALL", null, ["callee:00c57f60:8"]]
- 00563f70 bytes c8cf1b94
+ 00563fb0 bytes eccf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-136609beae8b1114dcfb94f33ad2b740"></a>

### [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md) → [`00564320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md) FUN_00564320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00563c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md) [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00563c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563c54.md) [`00584f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584f40.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`0088f34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md#insn-00564344) · [`00564354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md#insn-00564354) · [`00564364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md#insn-00564364)
- 新版 [`00564384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md#insn-00564384) · [`00564394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md#insn-00564394) · [`005643a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md#insn-005643a4)

~~~diff
- 00564344 ["INT_ADD", "register:40f0:8", ["const:564344:8", "const:4:8"]]
- 00564344 ["CALL", null, ["callee:00494650:8"]]
+ 00564384 ["INT_ADD", "register:40f0:8", ["const:564384:8", "const:4:8"]]
+ 00564384 ["CALL", null, ["callee:00494650:8"]]
- 00564344 bytes b3c0fc97
+ 00564384 bytes b3c0fc97
- 00564354 ["INT_ADD", "register:40f0:8", ["const:564354:8", "const:4:8"]]
- 00564354 ["CALL", null, ["callee:00c57f80:8"]]
+ 00564394 ["INT_ADD", "register:40f0:8", ["const:564394:8", "const:4:8"]]
+ 00564394 ["CALL", null, ["callee:00c57f80:8"]]
- 00564354 bytes d7ce1b94
+ 00564394 bytes fbce1b94
- 00564364 ["INT_ADD", "register:40f0:8", ["const:564364:8", "const:4:8"]]
- 00564364 ["CALL", null, ["callee:00c57f80:8"]]
+ 005643a4 ["INT_ADD", "register:40f0:8", ["const:5643a4:8", "const:4:8"]]
+ 005643a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00564364 bytes d3ce1b94
+ 005643a4 bytes f7ce1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da36121de4bf58f53e892d8a6e07c5a3"></a>

### [`00564380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md) → [`005643c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005643c0.md) FUN_005643c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00563dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563dc4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00563e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e04.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005643fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md#insn-005643fc) · [`00564424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md#insn-00564424) · [`00564490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md#insn-00564490)
- 新版 [`0056443c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005643c0.md#insn-0056443c) · [`00564464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005643c0.md#insn-00564464) · [`005644d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005643c0.md#insn-005644d0)

~~~diff
- 005643fc ["INT_ADD", "register:40f0:8", ["const:5643fc:8", "const:4:8"]]
- 005643fc ["CALL", null, ["callee:00c58120:8"]]
+ 0056443c ["INT_ADD", "register:40f0:8", ["const:56443c:8", "const:4:8"]]
+ 0056443c ["CALL", null, ["callee:00c58120:8"]]
- 005643fc bytes 15cf1b94
+ 0056443c bytes 39cf1b94
- 00564424 ["INT_ADD", "register:40f0:8", ["const:564424:8", "const:4:8"]]
- 00564424 ["CALL", null, ["callee:00c58120:8"]]
+ 00564464 ["INT_ADD", "register:40f0:8", ["const:564464:8", "const:4:8"]]
+ 00564464 ["CALL", null, ["callee:00c58120:8"]]
- 00564424 bytes 0bcf1b94
+ 00564464 bytes 2fcf1b94
- 00564490 ["INT_ADD", "register:40f0:8", ["const:564490:8", "const:4:8"]]
- 00564490 ["CALL", null, ["callee:00c58120:8"]]
+ 005644d0 ["INT_ADD", "register:40f0:8", ["const:5644d0:8", "const:4:8"]]
+ 005644d0 ["CALL", null, ["callee:00c58120:8"]]
- 00564490 bytes f0ce1b94
+ 005644d0 bytes 14cf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d0a895338587a5d3b7a9a4725ed82f"></a>

### [`005649d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005649d4.md) → [`00564a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564a14.md) FUN_00564a14

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005649d4.md#insn-00564a10) · [`00564a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005649d4.md#insn-00564a34) · [`00564a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005649d4.md#insn-00564a80)
- 新版 [`00564a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564a14.md#insn-00564a50) · [`00564a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564a14.md#insn-00564a74) · [`00564ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564a14.md#insn-00564ac0)

~~~diff
- 00564a10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00564a10 ["INT_ADD", "register:40f0:8", ["const:564a10:8", "const:4:8"]]
- 00564a10 ["CALLIND", null, ["register:0:8"]]
+ 00564a50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00564a50 ["INT_ADD", "register:40f0:8", ["const:564a50:8", "const:4:8"]]
+ 00564a50 ["CALLIND", null, ["register:0:8"]]
- 00564a10 bytes 20013fd6
+ 00564a50 bytes 20013fd6
- 00564a34 ["COPY", "register:0:8", ["register:4048:8"]]
- 00564a34 ["INT_ADD", "register:40f0:8", ["const:564a34:8", "const:4:8"]]
- 00564a34 ["CALLIND", null, ["register:0:8"]]
+ 00564a74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00564a74 ["INT_ADD", "register:40f0:8", ["const:564a74:8", "const:4:8"]]
+ 00564a74 ["CALLIND", null, ["register:0:8"]]
- 00564a34 bytes 20013fd6
+ 00564a74 bytes 20013fd6
- 00564a80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00564a80 ["INT_ADD", "register:40f0:8", ["const:564a80:8", "const:4:8"]]
- 00564a80 ["CALLIND", null, ["register:0:8"]]
+ 00564ac0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00564ac0 ["INT_ADD", "register:40f0:8", ["const:564ac0:8", "const:4:8"]]
+ 00564ac0 ["CALLIND", null, ["register:0:8"]]
- 00564a80 bytes 00013fd6
+ 00564ac0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd1c688eba7e2185542db7e1f61bc21"></a>

### [`00565144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565144.md) → [`00565184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565184.md) FUN_00565184

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565144.md#insn-00565180) · [`005651d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565144.md#insn-005651d0) · [`00565240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565144.md#insn-00565240)
- 新版 [`005651c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565184.md#insn-005651c0) · [`00565210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565184.md#insn-00565210) · [`00565280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565184.md#insn-00565280)

~~~diff
- 00565180 ["COPY", "register:0:8", ["register:4048:8"]]
- 00565180 ["INT_ADD", "register:40f0:8", ["const:565180:8", "const:4:8"]]
- 00565180 ["CALLIND", null, ["register:0:8"]]
+ 005651c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005651c0 ["INT_ADD", "register:40f0:8", ["const:5651c0:8", "const:4:8"]]
+ 005651c0 ["CALLIND", null, ["register:0:8"]]
- 00565180 bytes 20013fd6
+ 005651c0 bytes 20013fd6
- 005651d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005651d0 ["INT_ADD", "register:40f0:8", ["const:5651d0:8", "const:4:8"]]
- 005651d0 ["CALLIND", null, ["register:0:8"]]
+ 00565210 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00565210 ["INT_ADD", "register:40f0:8", ["const:565210:8", "const:4:8"]]
+ 00565210 ["CALLIND", null, ["register:0:8"]]
- 005651d0 bytes 20013fd6
+ 00565210 bytes 20013fd6
- 00565240 ["INT_ADD", "register:40f0:8", ["const:565240:8", "const:4:8"]]
- 00565240 ["CALL", null, ["callee:00c57f80:8"]]
+ 00565280 ["INT_ADD", "register:40f0:8", ["const:565280:8", "const:4:8"]]
+ 00565280 ["CALL", null, ["callee:00c57f80:8"]]
- 00565240 bytes 1ccb1b94
+ 00565280 bytes 40cb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b7b297a37d01c8739dec6b789327fda"></a>

### [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) → [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) FUN_005655c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`0056b79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md)
- 新版 呼出元 4件 [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) [`0056b7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md) [`0056ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005655a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md#insn-005655a8) · [`005655dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md#insn-005655dc) · [`005655f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md#insn-005655f4)
- 新版 [`005655e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md#insn-005655e8) · [`0056561c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md#insn-0056561c) · [`00565634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md#insn-00565634)

~~~diff
- 005655a8 ["INT_ADD", "register:40f0:8", ["const:5655a8:8", "const:4:8"]]
- 005655a8 ["CALL", null, ["callee:00c58730:8"]]
+ 005655e8 ["INT_ADD", "register:40f0:8", ["const:5655e8:8", "const:4:8"]]
+ 005655e8 ["CALL", null, ["callee:00c58730:8"]]
- 005655a8 bytes 2ecc1b94
+ 005655e8 bytes 52cc1b94
- 005655dc ["INT_ADD", "register:40f0:8", ["const:5655dc:8", "const:4:8"]]
- 005655dc ["CALL", null, ["callee:00c58730:8"]]
+ 0056561c ["INT_ADD", "register:40f0:8", ["const:56561c:8", "const:4:8"]]
+ 0056561c ["CALL", null, ["callee:00c58730:8"]]
- 005655dc bytes 21cc1b94
+ 0056561c bytes 45cc1b94
- 005655f4 ["INT_ADD", "register:40f0:8", ["const:5655f4:8", "const:4:8"]]
- 005655f4 ["CALL", null, ["callee:00c58730:8"]]
+ 00565634 ["INT_ADD", "register:40f0:8", ["const:565634:8", "const:4:8"]]
+ 00565634 ["CALL", null, ["callee:00c58730:8"]]
- 005655f4 bytes 1bcc1b94
+ 00565634 bytes 3fcc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab483c707d8afdae139c458c162249dd"></a>

### [`00568928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/00568928.md) → [`00568968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/00568968.md) FUN_00568968

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) · 呼出先 1件 [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md)
- 新版 呼出元 2件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`00569b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569b2c.md) · 呼出先 1件 [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00568964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/00568928.md#insn-00568964)
- 新版 [`005689a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/00568968.md#insn-005689a4)

~~~diff
- 00568964 ["INT_ADD", "register:40f0:8", ["const:568964:8", "const:4:8"]]
- 00568964 ["CALL", null, ["callee:00c5a120:8"]]
+ 005689a4 ["INT_ADD", "register:40f0:8", ["const:5689a4:8", "const:4:8"]]
+ 005689a4 ["CALL", null, ["callee:00c5a120:8"]]
- 00568964 bytes bbc51b94
+ 005689a4 bytes dfc51b94
~~~


<a id="compare-1527d9da6fc666deba208e91d8b9e388"></a>

### [`005692bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md) → [`005692fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md) FUN_005692fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) · 呼出先 3件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) · 呼出先 3件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566958.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005692ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md#insn-005692ec) · [`00569304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md#insn-00569304) · [`00569330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md#insn-00569330)
- 新版 [`0056932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md#insn-0056932c) · [`00569344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md#insn-00569344) · [`00569370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md#insn-00569370)

~~~diff
- 005692ec ["INT_ADD", "register:40f0:8", ["const:5692ec:8", "const:4:8"]]
- 005692ec ["CALL", null, ["callee:00565a98:8"]]
+ 0056932c ["INT_ADD", "register:40f0:8", ["const:56932c:8", "const:4:8"]]
+ 0056932c ["CALL", null, ["callee:00565a98:8"]]
- 005692ec bytes dbf1ff97
+ 0056932c bytes dbf1ff97
- 00569304 ["INT_ADD", "register:40f0:8", ["const:569304:8", "const:4:8"]]
- 00569304 ["CALL", null, ["callee:00566958:8"]]
+ 00569344 ["INT_ADD", "register:40f0:8", ["const:569344:8", "const:4:8"]]
+ 00569344 ["CALL", null, ["callee:00566958:8"]]
- 00569304 bytes 85f5ff97
+ 00569344 bytes 85f5ff97
- 00569330 ["INT_ADD", "register:40f0:8", ["const:569330:8", "const:4:8"]]
- 00569330 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00569370 ["INT_ADD", "register:40f0:8", ["const:569370:8", "const:4:8"]]
+ 00569370 ["CALL", null, ["callee:00c57fb0:8"]]
- 00569330 bytes ecba1b94
+ 00569370 bytes 10bb1b94
~~~


<a id="compare-6ce78cc6c0b8df3ccb66a07b2775eeb0"></a>

### [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) → [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) FUN_00569374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) · 呼出先 4件 [`0056d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md) [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)
- 新版 呼出元 2件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) · 呼出先 4件 [`0056d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d2b0.md) [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md#insn-00569360) · [`005693f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md#insn-005693f4) · [`00569430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md#insn-00569430)
- 新版 [`005693a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md#insn-005693a0) · [`00569434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md#insn-00569434) · [`00569470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md#insn-00569470)

~~~diff
- 00569360 ["INT_ADD", "register:40f0:8", ["const:569360:8", "const:4:8"]]
- 00569360 ["CALL", null, ["callee:0056d320:8"]]
+ 005693a0 ["INT_ADD", "register:40f0:8", ["const:5693a0:8", "const:4:8"]]
+ 005693a0 ["CALL", null, ["callee:0056d320:8"]]
- 00569360 bytes e00f0094
+ 005693a0 bytes e00f0094
- 005693f4 ["INT_ADD", "register:40f0:8", ["const:5693f4:8", "const:4:8"]]
- 005693f4 ["CALL", null, ["callee:00c5a140:8"]]
+ 00569434 ["INT_ADD", "register:40f0:8", ["const:569434:8", "const:4:8"]]
+ 00569434 ["CALL", null, ["callee:00c5a140:8"]]
- 005693f4 bytes 1fc31b94
+ 00569434 bytes 43c31b94
- 00569430 ["INT_ADD", "register:40f0:8", ["const:569430:8", "const:4:8"]]
- 00569430 ["CALL", null, ["callee:00c5a140:8"]]
+ 00569470 ["INT_ADD", "register:40f0:8", ["const:569470:8", "const:4:8"]]
+ 00569470 ["CALL", null, ["callee:00c5a140:8"]]
- 00569430 bytes 10c31b94
+ 00569470 bytes 34c31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b598e1ad14a19a0027ef3e2301affb"></a>

### [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) → [`00569520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md) FUN_00569520

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) · 呼出先 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)
- 新版 呼出元 3件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`0056b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md) [`0056c27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md) · 呼出先 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566958.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md#insn-0056956c) · [`00569588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md#insn-00569588) · [`005695c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md#insn-005695c0)
- 新版 [`005695ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md#insn-005695ac) · [`005695c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md#insn-005695c8) · [`00569600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md#insn-00569600)

~~~diff
- 0056956c ["INT_ADD", "register:40f0:8", ["const:56956c:8", "const:4:8"]]
- 0056956c ["CALL", null, ["callee:00c5a130:8"]]
+ 005695ac ["INT_ADD", "register:40f0:8", ["const:5695ac:8", "const:4:8"]]
+ 005695ac ["CALL", null, ["callee:00c5a130:8"]]
- 0056956c bytes bdc21b94
+ 005695ac bytes e1c21b94
- 00569588 ["INT_ADD", "register:40f0:8", ["const:569588:8", "const:4:8"]]
- 00569588 ["CALL", null, ["callee:00c5a130:8"]]
+ 005695c8 ["INT_ADD", "register:40f0:8", ["const:5695c8:8", "const:4:8"]]
+ 005695c8 ["CALL", null, ["callee:00c5a130:8"]]
- 00569588 bytes b6c21b94
+ 005695c8 bytes dac21b94
- 005695c0 ["INT_ADD", "register:40f0:8", ["const:5695c0:8", "const:4:8"]]
- 005695c0 ["CALL", null, ["callee:00565a98:8"]]
+ 00569600 ["INT_ADD", "register:40f0:8", ["const:569600:8", "const:4:8"]]
+ 00569600 ["CALL", null, ["callee:00565a98:8"]]
- 005695c0 bytes 26f1ff97
+ 00569600 bytes 26f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b05a711a185ea2ea674365727882028"></a>

### [`00569608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569608.md) → [`00569648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569648.md) FUN_00569648

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) · 呼出先 1件 [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)
- 新版 呼出元 2件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`00569b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569b2c.md) · 呼出先 1件 [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569608.md#insn-00569680)
- 新版 [`005696c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569648.md#insn-005696c0)

~~~diff
- 00569680 ["INT_ADD", "register:40f0:8", ["const:569680:8", "const:4:8"]]
- 00569680 ["CALL", null, ["callee:00c5a130:8"]]
+ 005696c0 ["INT_ADD", "register:40f0:8", ["const:5696c0:8", "const:4:8"]]
+ 005696c0 ["CALL", null, ["callee:00c5a130:8"]]
- 00569680 bytes 78c21b94
+ 005696c0 bytes 9cc21b94
~~~


<a id="compare-a5e41d0b445e73abd1a2c2904ff63c39"></a>

### [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) → [`005696f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md) FUN_005696f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 6件 [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)
- 新版 呼出元 2件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`0056ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md) · 呼出先 6件 [`00569b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569b2c.md) [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md#insn-00569718) · [`005697a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md#insn-005697a4) · [`005697c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md#insn-005697c0)
- 新版 [`00569758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md#insn-00569758) · [`005697e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md#insn-005697e4) · [`00569800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md#insn-00569800)

~~~diff
- 00569718 ["INT_ADD", "register:40f0:8", ["const:569718:8", "const:4:8"]]
- 00569718 ["CALL", null, ["callee:00c5a120:8"]]
+ 00569758 ["INT_ADD", "register:40f0:8", ["const:569758:8", "const:4:8"]]
+ 00569758 ["CALL", null, ["callee:00c5a120:8"]]
- 00569718 bytes 4ec21b94
+ 00569758 bytes 72c21b94
- 005697a4 ["INT_ADD", "register:40f0:8", ["const:5697a4:8", "const:4:8"]]
- 005697a4 ["CALL", null, ["callee:00c5a130:8"]]
+ 005697e4 ["INT_ADD", "register:40f0:8", ["const:5697e4:8", "const:4:8"]]
+ 005697e4 ["CALL", null, ["callee:00c5a130:8"]]
- 005697a4 bytes 2fc21b94
+ 005697e4 bytes 53c21b94
- 005697c0 ["INT_ADD", "register:40f0:8", ["const:5697c0:8", "const:4:8"]]
- 005697c0 ["CALL", null, ["callee:00c5a130:8"]]
+ 00569800 ["INT_ADD", "register:40f0:8", ["const:569800:8", "const:4:8"]]
+ 00569800 ["CALL", null, ["callee:00c5a130:8"]]
- 005697c0 bytes 28c21b94
+ 00569800 bytes 4cc21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7fc7bdc7f0ece58dd94aa88a315a9e"></a>

### [`00569f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md) → [`00569fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569fb4.md) FUN_00569fb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 2件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 2件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md#insn-00569fc8) · [`00569fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md#insn-00569fec)
- 新版 [`0056a008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569fb4.md#insn-0056a008) · [`0056a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569fb4.md#insn-0056a02c)

~~~diff
- 00569fc8 ["INT_ADD", "register:40f0:8", ["const:569fc8:8", "const:4:8"]]
- 00569fc8 ["CALL", null, ["callee:00c5a150:8"]]
+ 0056a008 ["INT_ADD", "register:40f0:8", ["const:56a008:8", "const:4:8"]]
+ 0056a008 ["CALL", null, ["callee:00c5a150:8"]]
- 00569fc8 bytes 2ec01b94
+ 0056a008 bytes 52c01b94
- 00569fec ["INT_ADD", "register:40f0:8", ["const:569fec:8", "const:4:8"]]
- 00569fec ["CALL", null, ["callee:00c580d0:8"]]
+ 0056a02c ["INT_ADD", "register:40f0:8", ["const:56a02c:8", "const:4:8"]]
+ 0056a02c ["CALL", null, ["callee:00c580d0:8"]]
- 00569fec bytes 05b81b94
+ 0056a02c bytes 29b81b94
~~~


<a id="compare-c9eaf399113ca559601b4f962ca4411d"></a>

### [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) → [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) FUN_0056a050

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) · 呼出先 1件 [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)
- 新版 呼出元 3件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`005696f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md) [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) · 呼出先 1件 [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md#insn-0056a050) · [`0056a06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md#insn-0056a06c) · [`0056a100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md#insn-0056a100)
- 新版 [`0056a090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md#insn-0056a090) · [`0056a0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md#insn-0056a0ac) · [`0056a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md#insn-0056a140)

~~~diff
- 0056a050 ["INT_ADD", "register:40f0:8", ["const:56a050:8", "const:4:8"]]
- 0056a050 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056a090 ["INT_ADD", "register:40f0:8", ["const:56a090:8", "const:4:8"]]
+ 0056a090 ["CALL", null, ["callee:00c5a140:8"]]
- 0056a050 bytes 08c01b94
+ 0056a090 bytes 2cc01b94
- 0056a06c ["INT_ADD", "register:40f0:8", ["const:56a06c:8", "const:4:8"]]
- 0056a06c ["CALL", null, ["callee:00c5a140:8"]]
+ 0056a0ac ["INT_ADD", "register:40f0:8", ["const:56a0ac:8", "const:4:8"]]
+ 0056a0ac ["CALL", null, ["callee:00c5a140:8"]]
- 0056a06c bytes 01c01b94
+ 0056a0ac bytes 25c01b94
- 0056a100 ["INT_ADD", "register:40f0:8", ["const:56a100:8", "const:4:8"]]
- 0056a100 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056a140 ["INT_ADD", "register:40f0:8", ["const:56a140:8", "const:4:8"]]
+ 0056a140 ["CALL", null, ["callee:00c5a140:8"]]
- 0056a100 bytes dcbf1b94
+ 0056a140 bytes 00c01b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b0b2093b8de3f4d0b2a43159f34e84"></a>

### [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) → [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) FUN_0056a1b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 8件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0056ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md) · 呼出先 8件 [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566958.md) [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md#insn-0056a1c0) · [`0056a210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md#insn-0056a210) · [`0056a25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md#insn-0056a25c)
- 新版 [`0056a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md#insn-0056a200) · [`0056a250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md#insn-0056a250) · [`0056a29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md#insn-0056a29c)

~~~diff
- 0056a1c0 ["INT_ADD", "register:40f0:8", ["const:56a1c0:8", "const:4:8"]]
- 0056a1c0 ["CALL", null, ["callee:00c58160:8"]]
+ 0056a200 ["INT_ADD", "register:40f0:8", ["const:56a200:8", "const:4:8"]]
+ 0056a200 ["CALL", null, ["callee:00c58160:8"]]
- 0056a1c0 bytes b4b71b94
+ 0056a200 bytes d8b71b94
- 0056a210 ["INT_ADD", "register:40f0:8", ["const:56a210:8", "const:4:8"]]
- 0056a210 ["CALL", null, ["callee:00566c40:8"]]
+ 0056a250 ["INT_ADD", "register:40f0:8", ["const:56a250:8", "const:4:8"]]
+ 0056a250 ["CALL", null, ["callee:00566c40:8"]]
- 0056a210 bytes 7cf2ff97
+ 0056a250 bytes 7cf2ff97
- 0056a25c ["INT_ADD", "register:40f0:8", ["const:56a25c:8", "const:4:8"]]
- 0056a25c ["CALL", null, ["callee:005655c4:8"]]
+ 0056a29c ["INT_ADD", "register:40f0:8", ["const:56a29c:8", "const:4:8"]]
+ 0056a29c ["CALL", null, ["callee:005655c4:8"]]
- 0056a25c bytes caecff97
+ 0056a29c bytes caecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35e55f9f088ef66e3eba0e7ff8438e8d"></a>

### [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) → [`0056a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md) FUN_0056a954

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) · 呼出先 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`0056a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a308.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0056b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md) · 呼出先 4件 [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) [`00566958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566958.md) [`0056a348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a348.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md#insn-0056a9b8) · [`0056a9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md#insn-0056a9ec) · [`0056aa04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md#insn-0056aa04)
- 新版 [`0056a9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md#insn-0056a9f8) · [`0056aa2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md#insn-0056aa2c) · [`0056aa44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md#insn-0056aa44)

~~~diff
- 0056a9b8 ["INT_ADD", "register:40f0:8", ["const:56a9b8:8", "const:4:8"]]
- 0056a9b8 ["CALL", null, ["callee:0056a348:8"]]
+ 0056a9f8 ["INT_ADD", "register:40f0:8", ["const:56a9f8:8", "const:4:8"]]
+ 0056a9f8 ["CALL", null, ["callee:0056a348:8"]]
- 0056a9b8 bytes 54feff97
+ 0056a9f8 bytes 54feff97
- 0056a9ec ["INT_ADD", "register:40f0:8", ["const:56a9ec:8", "const:4:8"]]
- 0056a9ec ["CALL", null, ["callee:00565a98:8"]]
+ 0056aa2c ["INT_ADD", "register:40f0:8", ["const:56aa2c:8", "const:4:8"]]
+ 0056aa2c ["CALL", null, ["callee:00565a98:8"]]
- 0056a9ec bytes 1becff97
+ 0056aa2c bytes 1becff97
- 0056aa04 ["INT_ADD", "register:40f0:8", ["const:56aa04:8", "const:4:8"]]
- 0056aa04 ["CALL", null, ["callee:00566958:8"]]
+ 0056aa44 ["INT_ADD", "register:40f0:8", ["const:56aa44:8", "const:4:8"]]
+ 0056aa44 ["CALL", null, ["callee:00566958:8"]]
- 0056aa04 bytes c5efff97
+ 0056aa44 bytes c5efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38623513c04826ca60c9c7f468e67793"></a>

### [`0056aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md) → [`0056ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md) FUN_0056ab10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00571284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005712c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ab1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md#insn-0056ab1c) · [`0056ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md#insn-0056ab30) · [`0056ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md#insn-0056ab38)
- 新版 [`0056ab5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md#insn-0056ab5c) · [`0056ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md#insn-0056ab70) · [`0056ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md#insn-0056ab78)

~~~diff
- 0056ab1c ["INT_ADD", "register:40f0:8", ["const:56ab1c:8", "const:4:8"]]
- 0056ab1c ["CALL", null, ["callee:00c53da0:8"]]
+ 0056ab5c ["INT_ADD", "register:40f0:8", ["const:56ab5c:8", "const:4:8"]]
+ 0056ab5c ["CALL", null, ["callee:00c53da0:8"]]
- 0056ab1c bytes 79a41b94
+ 0056ab5c bytes 91a41b94
- 0056ab30 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056ab30 ["INT_ADD", "register:40f0:8", ["const:56ab30:8", "const:4:8"]]
- 0056ab30 ["CALLIND", null, ["register:0:8"]]
+ 0056ab70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056ab70 ["INT_ADD", "register:40f0:8", ["const:56ab70:8", "const:4:8"]]
+ 0056ab70 ["CALLIND", null, ["register:0:8"]]
- 0056ab30 bytes 00013fd6
+ 0056ab70 bytes 00013fd6
- 0056ab38 ["INT_ADD", "register:40f0:8", ["const:56ab38:8", "const:4:8"]]
- 0056ab38 ["CALL", null, ["callee:00c57f50:8"]]
+ 0056ab78 ["INT_ADD", "register:40f0:8", ["const:56ab78:8", "const:4:8"]]
+ 0056ab78 ["CALL", null, ["callee:00c57f50:8"]]
- 0056ab38 bytes d2b41b94
+ 0056ab78 bytes f6b41b94
~~~


<a id="compare-3c4e92236fb3da603ae93d71c5f7c6a8"></a>

### [`0056af6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md) → [`0056afac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md) FUN_0056afac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056afa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md#insn-0056afa4) · [`0056afb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md#insn-0056afb8) · [`0056afc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md#insn-0056afc0)
- 新版 [`0056afe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md#insn-0056afe4) · [`0056aff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md#insn-0056aff8) · [`0056b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md#insn-0056b000)

~~~diff
- 0056afa4 ["INT_ADD", "register:40f0:8", ["const:56afa4:8", "const:4:8"]]
- 0056afa4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0056afe4 ["INT_ADD", "register:40f0:8", ["const:56afe4:8", "const:4:8"]]
+ 0056afe4 ["CALL", null, ["callee:00c53da0:8"]]
- 0056afa4 bytes 57a31b94
+ 0056afe4 bytes 6fa31b94
- 0056afb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056afb8 ["INT_ADD", "register:40f0:8", ["const:56afb8:8", "const:4:8"]]
- 0056afb8 ["CALLIND", null, ["register:0:8"]]
+ 0056aff8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056aff8 ["INT_ADD", "register:40f0:8", ["const:56aff8:8", "const:4:8"]]
+ 0056aff8 ["CALLIND", null, ["register:0:8"]]
- 0056afb8 bytes 00013fd6
+ 0056aff8 bytes 00013fd6
- 0056afc0 ["INT_ADD", "register:40f0:8", ["const:56afc0:8", "const:4:8"]]
- 0056afc0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0056b000 ["INT_ADD", "register:40f0:8", ["const:56b000:8", "const:4:8"]]
+ 0056b000 ["CALL", null, ["callee:00c57f50:8"]]
- 0056afc0 bytes b0b31b94
+ 0056b000 bytes d4b31b94
~~~


<a id="compare-4dbf5f3be78a8ceae0fe814d5bcf6abd"></a>

### [`0056afdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md) → [`0056b01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b01c.md) FUN_0056b01c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056aff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md#insn-0056aff8) · [`0056b018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md#insn-0056b018)
- 新版 [`0056b038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b01c.md#insn-0056b038) · [`0056b058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b01c.md#insn-0056b058)

~~~diff
- 0056aff8 ["INT_ADD", "register:40f0:8", ["const:56aff8:8", "const:4:8"]]
- 0056aff8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0056b038 ["INT_ADD", "register:40f0:8", ["const:56b038:8", "const:4:8"]]
+ 0056b038 ["CALL", null, ["callee:00c53da0:8"]]
- 0056aff8 bytes 42a31b94
+ 0056b038 bytes 5aa31b94
- 0056b018 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b018 ["INT_ADD", "register:40f0:8", ["const:56b018:8", "const:4:8"]]
- 0056b018 ["CALLIND", null, ["register:0:8"]]
+ 0056b058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b058 ["INT_ADD", "register:40f0:8", ["const:56b058:8", "const:4:8"]]
+ 0056b058 ["CALLIND", null, ["register:0:8"]]
- 0056b018 bytes 00013fd6
+ 0056b058 bytes 00013fd6
~~~


<a id="compare-2af5c671e20072e32376a8fa8207de30"></a>

### [`0056b680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b680.md) → [`0056b6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b6c0.md) FUN_0056b6c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b680.md#insn-0056b69c) · [`0056b6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b680.md#insn-0056b6bc)
- 新版 [`0056b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b6c0.md#insn-0056b6dc) · [`0056b6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b6c0.md#insn-0056b6fc)

~~~diff
- 0056b69c ["INT_ADD", "register:40f0:8", ["const:56b69c:8", "const:4:8"]]
- 0056b69c ["CALL", null, ["callee:00c53da0:8"]]
+ 0056b6dc ["INT_ADD", "register:40f0:8", ["const:56b6dc:8", "const:4:8"]]
+ 0056b6dc ["CALL", null, ["callee:00c53da0:8"]]
- 0056b69c bytes 99a11b94
+ 0056b6dc bytes b1a11b94
- 0056b6bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b6bc ["INT_ADD", "register:40f0:8", ["const:56b6bc:8", "const:4:8"]]
- 0056b6bc ["CALLIND", null, ["register:0:8"]]
+ 0056b6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b6fc ["INT_ADD", "register:40f0:8", ["const:56b6fc:8", "const:4:8"]]
+ 0056b6fc ["CALLIND", null, ["register:0:8"]]
- 0056b6bc bytes 00013fd6
+ 0056b6fc bytes 00013fd6
~~~


<a id="compare-09f78c73868cf6cdb3b80f5c64edbc18"></a>

### [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) → [`0056b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md) FUN_0056b710

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00571074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md) [`005711b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md) · 呼出先 4件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`005710b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005710b4.md) [`005711f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005711f4.md) · 呼出先 4件 [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md#insn-0056b6fc) · [`0056b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md#insn-0056b710) · [`0056b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md#insn-0056b720)
- 新版 [`0056b73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md#insn-0056b73c) · [`0056b750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md#insn-0056b750) · [`0056b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b710.md#insn-0056b760)

~~~diff
- 0056b6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b6fc ["INT_ADD", "register:40f0:8", ["const:56b6fc:8", "const:4:8"]]
- 0056b6fc ["CALLIND", null, ["register:0:8"]]
+ 0056b73c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b73c ["INT_ADD", "register:40f0:8", ["const:56b73c:8", "const:4:8"]]
+ 0056b73c ["CALLIND", null, ["register:0:8"]]
- 0056b6fc bytes 00013fd6
+ 0056b73c bytes 00013fd6
- 0056b710 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b710 ["INT_ADD", "register:40f0:8", ["const:56b710:8", "const:4:8"]]
- 0056b710 ["CALLIND", null, ["register:0:8"]]
+ 0056b750 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b750 ["INT_ADD", "register:40f0:8", ["const:56b750:8", "const:4:8"]]
+ 0056b750 ["CALLIND", null, ["register:0:8"]]
- 0056b710 bytes 00013fd6
+ 0056b750 bytes 00013fd6
- 0056b720 ["INT_ADD", "register:40f0:8", ["const:56b720:8", "const:4:8"]]
- 0056b720 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0056b760 ["INT_ADD", "register:40f0:8", ["const:56b760:8", "const:4:8"]]
+ 0056b760 ["CALL", null, ["callee:00c5a1b0:8"]]
- 0056b720 bytes 70ba1b94
+ 0056b760 bytes 94ba1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-867ea996b092287296c1b84bd1276014"></a>

### [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) → [`0056b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md) FUN_0056b94c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0056b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b614.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) · 呼出先 5件 [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) [`00c53c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53c70.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 3件 [`0056b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b654.md) [`0056ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md) [`0056c27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md) · 呼出先 5件 [`00569520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md) [`0056a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md) [`00c53d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d10.md) [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md#insn-0056b924) · [`0056b958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md#insn-0056b958) · [`0056b96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md#insn-0056b96c)
- 新版 [`0056b964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md#insn-0056b964) · [`0056b998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md#insn-0056b998) · [`0056b9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md#insn-0056b9ac)

~~~diff
- 0056b924 ["INT_ADD", "register:40f0:8", ["const:56b924:8", "const:4:8"]]
- 0056b924 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0056b964 ["INT_ADD", "register:40f0:8", ["const:56b964:8", "const:4:8"]]
+ 0056b964 ["CALL", null, ["callee:00c5a1b0:8"]]
- 0056b924 bytes efb91b94
+ 0056b964 bytes 13ba1b94
- 0056b958 ["INT_ADD", "register:40f0:8", ["const:56b958:8", "const:4:8"]]
- 0056b958 ["CALL", null, ["callee:0056a954:8"]]
+ 0056b998 ["INT_ADD", "register:40f0:8", ["const:56b998:8", "const:4:8"]]
+ 0056b998 ["CALL", null, ["callee:0056a954:8"]]
- 0056b958 bytes effbff97
+ 0056b998 bytes effbff97
- 0056b96c ["INT_ADD", "register:40f0:8", ["const:56b96c:8", "const:4:8"]]
- 0056b96c ["CALL", null, ["callee:00c53d10:8"]]
+ 0056b9ac ["INT_ADD", "register:40f0:8", ["const:56b9ac:8", "const:4:8"]]
+ 0056b9ac ["CALL", null, ["callee:00c53d10:8"]]
- 0056b96c bytes c1a01b94
+ 0056b9ac bytes d9a01b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977ee529736679868bcc45d849e8efdf"></a>

### [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) → [`0056ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md) FUN_0056ba64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) · 呼出先 12件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`0056c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c780.md) · 呼出先 12件 [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) [`005696f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005696f8.md) [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) [`0056b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ba54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md#insn-0056ba54) · [`0056ba6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md#insn-0056ba6c) · [`0056ba7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md#insn-0056ba7c)
- 新版 [`0056ba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md#insn-0056ba94) · [`0056baac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md#insn-0056baac) · [`0056babc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056ba64.md#insn-0056babc)

~~~diff
- 0056ba54 ["INT_ADD", "register:40f0:8", ["const:56ba54:8", "const:4:8"]]
- 0056ba54 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0056ba94 ["INT_ADD", "register:40f0:8", ["const:56ba94:8", "const:4:8"]]
+ 0056ba94 ["CALL", null, ["callee:00c5a1b0:8"]]
- 0056ba54 bytes a3b91b94
+ 0056ba94 bytes c7b91b94
- 0056ba6c ["INT_ADD", "register:40f0:8", ["const:56ba6c:8", "const:4:8"]]
- 0056ba6c ["CALL", null, ["callee:005655c4:8"]]
+ 0056baac ["INT_ADD", "register:40f0:8", ["const:56baac:8", "const:4:8"]]
+ 0056baac ["CALL", null, ["callee:005655c4:8"]]
- 0056ba6c bytes c6e6ff97
+ 0056baac bytes c6e6ff97
- 0056ba7c ["INT_ADD", "register:40f0:8", ["const:56ba7c:8", "const:4:8"]]
- 0056ba7c ["CALL", null, ["callee:00c58730:8"]]
+ 0056babc ["INT_ADD", "register:40f0:8", ["const:56babc:8", "const:4:8"]]
+ 0056babc ["CALL", null, ["callee:00c58730:8"]]
- 0056ba7c bytes f9b21b94
+ 0056babc bytes 1db31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-202b3aab3a4922d182e33651a07c85b9"></a>

### [`0056bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md) → [`0056bd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md) FUN_0056bd34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md) · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`0056c53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md) · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md#insn-0056bd2c) · [`0056bd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md#insn-0056bd44) · [`0056bd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md#insn-0056bd58)
- 新版 [`0056bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md#insn-0056bd6c) · [`0056bd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md#insn-0056bd84) · [`0056bd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md#insn-0056bd98)

~~~diff
- 0056bd2c ["INT_ADD", "register:40f0:8", ["const:56bd2c:8", "const:4:8"]]
- 0056bd2c ["CALL", null, ["callee:00c53d70:8"]]
+ 0056bd6c ["INT_ADD", "register:40f0:8", ["const:56bd6c:8", "const:4:8"]]
+ 0056bd6c ["CALL", null, ["callee:00c53d70:8"]]
- 0056bd2c bytes e99f1b94
+ 0056bd6c bytes 01a01b94
- 0056bd44 ["INT_ADD", "register:40f0:8", ["const:56bd44:8", "const:4:8"]]
- 0056bd44 ["CALL", null, ["callee:00c53da0:8"]]
+ 0056bd84 ["INT_ADD", "register:40f0:8", ["const:56bd84:8", "const:4:8"]]
+ 0056bd84 ["CALL", null, ["callee:00c53da0:8"]]
- 0056bd44 bytes ef9f1b94
+ 0056bd84 bytes 07a01b94
- 0056bd58 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056bd58 ["INT_ADD", "register:40f0:8", ["const:56bd58:8", "const:4:8"]]
- 0056bd58 ["CALLIND", null, ["register:0:8"]]
+ 0056bd98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056bd98 ["INT_ADD", "register:40f0:8", ["const:56bd98:8", "const:4:8"]]
+ 0056bd98 ["CALLIND", null, ["register:0:8"]]
- 0056bd58 bytes 00013fd6
+ 0056bd98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3368e2ffbc0dc8ec1d7ce70ad1da2c98"></a>

### [`0056c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c000.md) → [`0056c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c040.md) FUN_0056c040

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c584f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c584f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c000.md#insn-0056c034) · [`0056c058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c000.md#insn-0056c058) · [`0056c07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c000.md#insn-0056c07c)
- 新版 [`0056c074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c040.md#insn-0056c074) · [`0056c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c040.md#insn-0056c098) · [`0056c0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c040.md#insn-0056c0bc)

~~~diff
- 0056c034 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c034 ["INT_ADD", "register:40f0:8", ["const:56c034:8", "const:4:8"]]
- 0056c034 ["CALLIND", null, ["register:0:8"]]
+ 0056c074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c074 ["INT_ADD", "register:40f0:8", ["const:56c074:8", "const:4:8"]]
+ 0056c074 ["CALLIND", null, ["register:0:8"]]
- 0056c034 bytes 00013fd6
+ 0056c074 bytes 00013fd6
- 0056c058 ["INT_ADD", "register:40f0:8", ["const:56c058:8", "const:4:8"]]
- 0056c058 ["CALL", null, ["callee:00c584f0:8"]]
+ 0056c098 ["INT_ADD", "register:40f0:8", ["const:56c098:8", "const:4:8"]]
+ 0056c098 ["CALL", null, ["callee:00c584f0:8"]]
- 0056c058 bytes f2b01b94
+ 0056c098 bytes 16b11b94
- 0056c07c ["INT_ADD", "register:40f0:8", ["const:56c07c:8", "const:4:8"]]
- 0056c07c ["CALL", null, ["callee:00c57fb0:8"]]
+ 0056c0bc ["INT_ADD", "register:40f0:8", ["const:56c0bc:8", "const:4:8"]]
+ 0056c0bc ["CALL", null, ["callee:00c57fb0:8"]]
- 0056c07c bytes 99af1b94
+ 0056c0bc bytes bdaf1b94
~~~


<a id="compare-6a701e8968655948c40e067e679ed108"></a>

### [`0056c09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c09c.md) → [`0056c0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c0dc.md) FUN_0056c0dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c09c.md#insn-0056c0e0) · [`0056c110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c09c.md#insn-0056c110)
- 新版 [`0056c120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c0dc.md#insn-0056c120) · [`0056c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c0dc.md#insn-0056c150)

~~~diff
- 0056c0e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0056c0e0 ["INT_ADD", "register:40f0:8", ["const:56c0e0:8", "const:4:8"]]
- 0056c0e0 ["CALLIND", null, ["register:0:8"]]
+ 0056c120 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0056c120 ["INT_ADD", "register:40f0:8", ["const:56c120:8", "const:4:8"]]
+ 0056c120 ["CALLIND", null, ["register:0:8"]]
- 0056c0e0 bytes 20013fd6
+ 0056c120 bytes 20013fd6
- 0056c110 ["INT_ADD", "register:40f0:8", ["const:56c110:8", "const:4:8"]]
- 0056c110 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0056c150 ["INT_ADD", "register:40f0:8", ["const:56c150:8", "const:4:8"]]
+ 0056c150 ["CALL", null, ["callee:00c57fb0:8"]]
- 0056c110 bytes 74af1b94
+ 0056c150 bytes 98af1b94
~~~


<a id="compare-5e45e11dac304771ce096d8af5a23c5c"></a>

### [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) → [`0056c27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md) FUN_0056c27c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c45c.md) · 呼出先 4件 [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`0056c49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c49c.md) · 呼出先 4件 [`00569520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md) [`0056b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b94c.md) [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md#insn-0056c268) · [`0056c27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md#insn-0056c27c) · [`0056c28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md#insn-0056c28c)
- 新版 [`0056c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md#insn-0056c2a8) · [`0056c2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md#insn-0056c2bc) · [`0056c2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c27c.md#insn-0056c2cc)

~~~diff
- 0056c268 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c268 ["INT_ADD", "register:40f0:8", ["const:56c268:8", "const:4:8"]]
- 0056c268 ["CALLIND", null, ["register:0:8"]]
+ 0056c2a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c2a8 ["INT_ADD", "register:40f0:8", ["const:56c2a8:8", "const:4:8"]]
+ 0056c2a8 ["CALLIND", null, ["register:0:8"]]
- 0056c268 bytes 00013fd6
+ 0056c2a8 bytes 00013fd6
- 0056c27c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c27c ["INT_ADD", "register:40f0:8", ["const:56c27c:8", "const:4:8"]]
- 0056c27c ["CALLIND", null, ["register:0:8"]]
+ 0056c2bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c2bc ["INT_ADD", "register:40f0:8", ["const:56c2bc:8", "const:4:8"]]
+ 0056c2bc ["CALLIND", null, ["register:0:8"]]
- 0056c27c bytes 00013fd6
+ 0056c2bc bytes 00013fd6
- 0056c28c ["INT_ADD", "register:40f0:8", ["const:56c28c:8", "const:4:8"]]
- 0056c28c ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0056c2cc ["INT_ADD", "register:40f0:8", ["const:56c2cc:8", "const:4:8"]]
+ 0056c2cc ["CALL", null, ["callee:00c5a1b0:8"]]
- 0056c28c bytes 95b71b94
+ 0056c2cc bytes b9b71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159715801c95b05cf4cc9664870d65c7"></a>

### [`0056c2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c2fc.md) → [`0056c33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c33c.md) FUN_0056c33c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c2fc.md#insn-0056c320) · [`0056c33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c2fc.md#insn-0056c33c)
- 新版 [`0056c360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c33c.md#insn-0056c360) · [`0056c37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c33c.md#insn-0056c37c)

~~~diff
- 0056c320 ["INT_ADD", "register:40f0:8", ["const:56c320:8", "const:4:8"]]
- 0056c320 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0056c360 ["INT_ADD", "register:40f0:8", ["const:56c360:8", "const:4:8"]]
+ 0056c360 ["CALL", null, ["callee:00c5a1b0:8"]]
- 0056c320 bytes 70b71b94
+ 0056c360 bytes 94b71b94
- 0056c33c ["INT_ADD", "register:40f0:8", ["const:56c33c:8", "const:4:8"]]
- 0056c33c ["CALL", null, ["callee:005689bc:8"]]
+ 0056c37c ["INT_ADD", "register:40f0:8", ["const:56c37c:8", "const:4:8"]]
+ 0056c37c ["CALL", null, ["callee:005689bc:8"]]
- 0056c33c bytes 90f1ff97
+ 0056c37c bytes 90f1ff97
~~~


<a id="compare-1f2dc4a59ceeb706f03657fee5d25cfb"></a>

### [`0056c3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c3dc.md) → [`0056c41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c41c.md) FUN_0056c41c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a100.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c3dc.md#insn-0056c410)
- 新版 [`0056c450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c41c.md#insn-0056c450)

~~~diff
- 0056c410 ["INT_ADD", "register:40f0:8", ["const:56c410:8", "const:4:8"]]
- 0056c410 ["CALL", null, ["callee:00c5a1d0:8"]]
+ 0056c450 ["INT_ADD", "register:40f0:8", ["const:56c450:8", "const:4:8"]]
+ 0056c450 ["CALL", null, ["callee:00c5a1d0:8"]]
- 0056c410 bytes 3cb71b94
+ 0056c450 bytes 60b71b94
~~~


<a id="compare-9651f4086312a98c1307ba4ee217d0a4"></a>

### [`0056c468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c468.md) → [`0056c4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c4a8.md) FUN_0056c4a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c468.md#insn-0056c4b8) · [`0056c4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c468.md#insn-0056c4f8)
- 新版 [`0056c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c4a8.md#insn-0056c4f8) · [`0056c538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c4a8.md#insn-0056c538)

~~~diff
- 0056c4b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c4b8 ["INT_ADD", "register:40f0:8", ["const:56c4b8:8", "const:4:8"]]
- 0056c4b8 ["CALLIND", null, ["register:0:8"]]
+ 0056c4f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c4f8 ["INT_ADD", "register:40f0:8", ["const:56c4f8:8", "const:4:8"]]
+ 0056c4f8 ["CALLIND", null, ["register:0:8"]]
- 0056c4b8 bytes 00013fd6
+ 0056c4f8 bytes 00013fd6
- 0056c4f8 ["INT_ADD", "register:40f0:8", ["const:56c4f8:8", "const:4:8"]]
- 0056c4f8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0056c538 ["INT_ADD", "register:40f0:8", ["const:56c538:8", "const:4:8"]]
+ 0056c538 ["CALL", null, ["callee:00c57fb0:8"]]
- 0056c4f8 bytes 7aae1b94
+ 0056c538 bytes 9eae1b94
~~~


<a id="compare-e5bee5f7dedecd4cd275cf93056875ee"></a>

### [`0056c6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c6ec.md) → [`0056c72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c72c.md) FUN_0056c72c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c6ec.md#insn-0056c708) · [`0056c728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c6ec.md#insn-0056c728)
- 新版 [`0056c748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c72c.md#insn-0056c748) · [`0056c768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c72c.md#insn-0056c768)

~~~diff
- 0056c708 ["INT_ADD", "register:40f0:8", ["const:56c708:8", "const:4:8"]]
- 0056c708 ["CALL", null, ["callee:00c53da0:8"]]
+ 0056c748 ["INT_ADD", "register:40f0:8", ["const:56c748:8", "const:4:8"]]
+ 0056c748 ["CALL", null, ["callee:00c53da0:8"]]
- 0056c708 bytes 7e9d1b94
+ 0056c748 bytes 969d1b94
- 0056c728 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c728 ["INT_ADD", "register:40f0:8", ["const:56c728:8", "const:4:8"]]
- 0056c728 ["CALLIND", null, ["register:0:8"]]
+ 0056c768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c768 ["INT_ADD", "register:40f0:8", ["const:56c768:8", "const:4:8"]]
+ 0056c768 ["CALLIND", null, ["register:0:8"]]
- 0056c728 bytes 00013fd6
+ 0056c768 bytes 00013fd6
~~~


<a id="compare-abec2f4b6f237ad8103c1a1d6d17dda4"></a>

### [`0056c900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c900.md) → [`0056c940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c940.md) FUN_0056c940

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c900.md#insn-0056c91c) · [`0056c93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c900.md#insn-0056c93c)
- 新版 [`0056c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c940.md#insn-0056c95c) · [`0056c97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c940.md#insn-0056c97c)

~~~diff
- 0056c91c ["INT_ADD", "register:40f0:8", ["const:56c91c:8", "const:4:8"]]
- 0056c91c ["CALL", null, ["callee:00c53da0:8"]]
+ 0056c95c ["INT_ADD", "register:40f0:8", ["const:56c95c:8", "const:4:8"]]
+ 0056c95c ["CALL", null, ["callee:00c53da0:8"]]
- 0056c91c bytes f99c1b94
+ 0056c95c bytes 119d1b94
- 0056c93c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c93c ["INT_ADD", "register:40f0:8", ["const:56c93c:8", "const:4:8"]]
- 0056c93c ["CALLIND", null, ["register:0:8"]]
+ 0056c97c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c97c ["INT_ADD", "register:40f0:8", ["const:56c97c:8", "const:4:8"]]
+ 0056c97c ["CALLIND", null, ["register:0:8"]]
- 0056c93c bytes 00013fd6
+ 0056c97c bytes 00013fd6
~~~


<a id="compare-07ec3bbfac301f130d5813c43915e557"></a>

### [`0056c950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c950.md) → [`0056c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c990.md) FUN_0056c990

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c950.md#insn-0056c96c) · [`0056c98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c950.md#insn-0056c98c)
- 新版 [`0056c9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c990.md#insn-0056c9ac) · [`0056c9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c990.md#insn-0056c9cc)

~~~diff
- 0056c96c ["INT_ADD", "register:40f0:8", ["const:56c96c:8", "const:4:8"]]
- 0056c96c ["CALL", null, ["callee:00c53da0:8"]]
+ 0056c9ac ["INT_ADD", "register:40f0:8", ["const:56c9ac:8", "const:4:8"]]
+ 0056c9ac ["CALL", null, ["callee:00c53da0:8"]]
- 0056c96c bytes e59c1b94
+ 0056c9ac bytes fd9c1b94
- 0056c98c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c98c ["INT_ADD", "register:40f0:8", ["const:56c98c:8", "const:4:8"]]
- 0056c98c ["CALLIND", null, ["register:0:8"]]
+ 0056c9cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c9cc ["INT_ADD", "register:40f0:8", ["const:56c9cc:8", "const:4:8"]]
+ 0056c9cc ["CALLIND", null, ["register:0:8"]]
- 0056c98c bytes 00013fd6
+ 0056c9cc bytes 00013fd6
~~~


<a id="compare-43d3d070e005d722647ab02a4694af3f"></a>

### [`0056c9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c9a0.md) → [`0056c9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c9e0.md) FUN_0056c9e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550984.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005509c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509c4.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`0056c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c780.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c9a0.md#insn-0056c9d0) · [`0056c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c9a0.md#insn-0056c9e0) · [`0056c9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c9a0.md#insn-0056c9f4)
- 新版 [`0056ca10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c9e0.md#insn-0056ca10) · [`0056ca20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c9e0.md#insn-0056ca20) · [`0056ca34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c9e0.md#insn-0056ca34)

~~~diff
- 0056c9d0 ["INT_ADD", "register:40f0:8", ["const:56c9d0:8", "const:4:8"]]
- 0056c9d0 ["CALL", null, ["callee:00550be4:8"]]
+ 0056ca10 ["INT_ADD", "register:40f0:8", ["const:56ca10:8", "const:4:8"]]
+ 0056ca10 ["CALL", null, ["callee:00550be4:8"]]
- 0056c9d0 bytes 7590ff97
+ 0056ca10 bytes 7590ff97
- 0056c9e0 ["INT_ADD", "register:40f0:8", ["const:56c9e0:8", "const:4:8"]]
- 0056c9e0 ["CALL", null, ["callee:0056c780:8"]]
+ 0056ca20 ["INT_ADD", "register:40f0:8", ["const:56ca20:8", "const:4:8"]]
+ 0056ca20 ["CALL", null, ["callee:0056c780:8"]]
- 0056c9e0 bytes 58ffff97
+ 0056ca20 bytes 58ffff97
- 0056c9f4 ["INT_ADD", "register:40f0:8", ["const:56c9f4:8", "const:4:8"]]
- 0056c9f4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0056ca34 ["INT_ADD", "register:40f0:8", ["const:56ca34:8", "const:4:8"]]
+ 0056ca34 ["CALL", null, ["callee:00c53da0:8"]]
- 0056c9f4 bytes c39c1b94
+ 0056ca34 bytes db9c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

