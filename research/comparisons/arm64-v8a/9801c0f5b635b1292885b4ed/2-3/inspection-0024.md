# v16.0.1 → v16.0.2 · 要調査の変更候補 (24)

[一覧の目次](README.md)

<a id="compare-24d0bd040f85f696cac3f082606d494f"></a>

### [`00803d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803d48.md) → [`00803da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803da0.md) FUN_00803da0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md)
- 新版 呼出元 7件 [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 1件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00803d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803d48.md#insn-00803d54)
- 新版 `00803dac`（命令位置の公開資料なし）

~~~diff
- 00803d54 ["INT_ADD", "register:40f0:8", ["const:803d54:8", "const:4:8"]]
- 00803d54 ["CALL", null, ["callee:00802710:8"]]
+ 00803dac ["INT_ADD", "register:40f0:8", ["const:803dac:8", "const:4:8"]]
+ 00803dac ["CALL", null, ["callee:00802710:8"]]
- 00803d54 bytes 59faff97
+ 00803dac bytes 59faff97
~~~


<a id="compare-11f2a9efb39c62c2416e982e84edff75"></a>

### [`00807d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md) → [`00807db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807db8.md) FUN_00807db8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0080b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b37c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00807d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md#insn-00807d7c) · [`00807d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md#insn-00807d94)
- 新版 `00807dd4`（命令位置の公開資料なし） · `00807dec`（命令位置の公開資料なし）

~~~diff
- 00807d7c ["INT_ADD", "register:40f0:8", ["const:807d7c:8", "const:4:8"]]
- 00807d7c ["CALL", null, ["callee:005c17dc:8"]]
+ 00807dd4 ["INT_ADD", "register:40f0:8", ["const:807dd4:8", "const:4:8"]]
+ 00807dd4 ["CALL", null, ["callee:005c17dc:8"]]
- 00807d7c bytes 88e6f697
+ 00807dd4 bytes 82e6f697
- 00807d94 ["INT_ADD", "register:40f0:8", ["const:807d94:8", "const:4:8"]]
- 00807d94 ["CALL", null, ["callee:0080b37c:8"]]
+ 00807dec ["INT_ADD", "register:40f0:8", ["const:807dec:8", "const:4:8"]]
+ 00807dec ["CALL", null, ["callee:0080b37c:8"]]
- 00807d94 bytes 640d0094
+ 00807dec bytes 640d0094
~~~


<a id="compare-cc2a3bcc1fc86d7983fbb18806097338"></a>

### [`008099d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md) → [`00809a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00809/00809a30.md) FUN_00809a30

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00809a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md#insn-00809a24) · [`00809a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md#insn-00809a34) · [`00809a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md#insn-00809a38)
- 新版 `00809a7c`（命令位置の公開資料なし） · `00809a8c`（命令位置の公開資料なし） · `00809a90`（命令位置の公開資料なし）

~~~diff
- 00809a24 ["INT_ADD", "register:40f0:8", ["const:809a24:8", "const:4:8"]]
- 00809a24 ["CALL", null, ["callee:0080b37c:8"]]
+ 00809a7c ["INT_ADD", "register:40f0:8", ["const:809a7c:8", "const:4:8"]]
+ 00809a7c ["CALL", null, ["callee:0080b37c:8"]]
- 00809a24 bytes 40060094
+ 00809a7c bytes 40060094
- 00809a34 ["INT_ADD", "register:40f0:8", ["const:809a34:8", "const:4:8"]]
- 00809a34 ["CALL", null, ["callee:00a35bec:8"]]
+ 00809a8c ["INT_ADD", "register:40f0:8", ["const:809a8c:8", "const:4:8"]]
+ 00809a8c ["CALL", null, ["callee:00a35bec:8"]]
- 00809a34 bytes 59b00894
+ 00809a8c bytes 58b00894
- 00809a38 ["INT_ADD", "register:40f0:8", ["const:809a38:8", "const:4:8"]]
- 00809a38 ["CALL", null, ["callee:00a38bc0:8"]]
+ 00809a90 ["INT_ADD", "register:40f0:8", ["const:809a90:8", "const:4:8"]]
+ 00809a90 ["CALL", null, ["callee:00a38bc0:8"]]
- 00809a38 bytes 4dbc0894
+ 00809a90 bytes 4cbc0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e76b485929331be6e2a8e5b05ca3f42d"></a>

### [`0080aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080aefc.md) → [`0080af54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080a/0080af54.md) FUN_0080af54

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a87ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a87ad0.md) · 呼出先 1件 [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md)
- 新版 呼出元 1件 [`00a87b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87b40.md) · 呼出先 1件 [`0080b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b37c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080af14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080aefc.md#insn-0080af14)
- 新版 `0080af6c`（命令位置の公開資料なし）

~~~diff
- 0080af14 ["INT_ADD", "register:40f0:8", ["const:80af14:8", "const:4:8"]]
- 0080af14 ["CALL", null, ["callee:0080b37c:8"]]
+ 0080af6c ["INT_ADD", "register:40f0:8", ["const:80af6c:8", "const:4:8"]]
+ 0080af6c ["CALL", null, ["callee:0080b37c:8"]]
- 0080af14 bytes 04010094
+ 0080af6c bytes 04010094
~~~


<a id="compare-9e59168d4eac7c920ab0817872b56375"></a>

### [`0080af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080af2c.md) → [`0080af84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080a/0080af84.md) FUN_0080af84

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007c7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7978.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`007c79d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c79d0.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080afc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080af2c.md#insn-0080afc4) · [`0080b010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080af2c.md#insn-0080b010)
- 新版 `0080b01c`（命令位置の公開資料なし） · `0080b068`（命令位置の公開資料なし）

~~~diff
- 0080afc4 ["INT_ADD", "register:40f0:8", ["const:80afc4:8", "const:4:8"]]
- 0080afc4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080b01c ["INT_ADD", "register:40f0:8", ["const:80b01c:8", "const:4:8"]]
+ 0080b01c ["CALL", null, ["callee:00c57f60:8"]]
- 0080afc4 bytes b3331194
+ 0080b01c bytes d1331194
- 0080b010 ["INT_ADD", "register:40f0:8", ["const:80b010:8", "const:4:8"]]
- 0080b010 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080b068 ["INT_ADD", "register:40f0:8", ["const:80b068:8", "const:4:8"]]
+ 0080b068 ["CALL", null, ["callee:0043bbe4:8"]]
- 0080b010 bytes e5c2f097
+ 0080b068 bytes dfc2f097
~~~


<a id="compare-93a378cefba49596f7aba03f275a056f"></a>

### [`0080b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md) → [`0080b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b098.md) FUN_0080b098

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00937ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md) [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 4件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00937b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00937/00937b14.md) [`00938104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/00938104.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md#insn-0080b0d8) · [`0080b114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md#insn-0080b114)
- 新版 `0080b130`（命令位置の公開資料なし） · `0080b16c`（命令位置の公開資料なし）

~~~diff
- 0080b0d8 ["INT_ADD", "register:40f0:8", ["const:80b0d8:8", "const:4:8"]]
- 0080b0d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080b130 ["INT_ADD", "register:40f0:8", ["const:80b130:8", "const:4:8"]]
+ 0080b130 ["CALL", null, ["callee:00c57f60:8"]]
- 0080b0d8 bytes 6e331194
+ 0080b130 bytes 8c331194
- 0080b114 ["INT_ADD", "register:40f0:8", ["const:80b114:8", "const:4:8"]]
- 0080b114 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080b16c ["INT_ADD", "register:40f0:8", ["const:80b16c:8", "const:4:8"]]
+ 0080b16c ["CALL", null, ["callee:0043bbe4:8"]]
- 0080b114 bytes a4c2f097
+ 0080b16c bytes 9ec2f097
~~~


<a id="compare-20215154d656a71cdfb286014744bc79"></a>

### [`0080b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b144.md) → [`0080b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b19c.md) FUN_0080b19c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b144.md#insn-0080b170) · [`0080b188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b144.md#insn-0080b188) · [`0080b1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b144.md#insn-0080b1ac)
- 新版 `0080b1c8`（命令位置の公開資料なし） · `0080b1e0`（命令位置の公開資料なし） · `0080b204`（命令位置の公開資料なし）

~~~diff
- 0080b170 ["INT_ADD", "register:40f0:8", ["const:80b170:8", "const:4:8"]]
- 0080b170 ["CALL", null, ["callee:00480218:8"]]
+ 0080b1c8 ["INT_ADD", "register:40f0:8", ["const:80b1c8:8", "const:4:8"]]
+ 0080b1c8 ["CALL", null, ["callee:00480218:8"]]
- 0080b170 bytes 1ad4f197
+ 0080b1c8 bytes 14d4f197
- 0080b188 ["INT_ADD", "register:40f0:8", ["const:80b188:8", "const:4:8"]]
- 0080b188 ["CALL", null, ["callee:005c17dc:8"]]
+ 0080b1e0 ["INT_ADD", "register:40f0:8", ["const:80b1e0:8", "const:4:8"]]
+ 0080b1e0 ["CALL", null, ["callee:005c17dc:8"]]
- 0080b188 bytes 85d9f697
+ 0080b1e0 bytes 7fd9f697
- 0080b1ac ["INT_ADD", "register:40f0:8", ["const:80b1ac:8", "const:4:8"]]
- 0080b1ac ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080b204 ["INT_ADD", "register:40f0:8", ["const:80b204:8", "const:4:8"]]
+ 0080b204 ["CALL", null, ["callee:0043bbe4:8"]]
- 0080b1ac bytes 7ec2f097
+ 0080b204 bytes 78c2f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebadd726267bf11839e8e05198510fcd"></a>

### [`0080b288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b288.md) → [`0080b2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b2e0.md) FUN_0080b2e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 1件 [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b288.md#insn-0080b2ac) · [`0080b2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b288.md#insn-0080b2e4) · [`0080b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b288.md#insn-0080b2f0)
- 新版 `0080b304`（命令位置の公開資料なし） · `0080b33c`（命令位置の公開資料なし） · `0080b348`（命令位置の公開資料なし）

~~~diff
- 0080b2ac ["INT_ADD", "register:40f0:8", ["const:80b2ac:8", "const:4:8"]]
- 0080b2ac ["CALL", null, ["callee:00480c28:8"]]
+ 0080b304 ["INT_ADD", "register:40f0:8", ["const:80b304:8", "const:4:8"]]
+ 0080b304 ["CALL", null, ["callee:00480c28:8"]]
- 0080b2ac bytes 4fd6f197
+ 0080b304 bytes 49d6f197
- 0080b2e4 ["INT_ADD", "register:40f0:8", ["const:80b2e4:8", "const:4:8"]]
- 0080b2e4 ["CALL", null, ["callee:00480c28:8"]]
+ 0080b33c ["INT_ADD", "register:40f0:8", ["const:80b33c:8", "const:4:8"]]
+ 0080b33c ["CALL", null, ["callee:00480c28:8"]]
- 0080b2e4 bytes 41d6f197
+ 0080b33c bytes 3bd6f197
- 0080b2f0 ["INT_ADD", "register:40f0:8", ["const:80b2f0:8", "const:4:8"]]
- 0080b2f0 ["CALL", null, ["callee:00480c28:8"]]
+ 0080b348 ["INT_ADD", "register:40f0:8", ["const:80b348:8", "const:4:8"]]
+ 0080b348 ["CALL", null, ["callee:00480c28:8"]]
- 0080b2f0 bytes 3ed6f197
+ 0080b348 bytes 38d6f197
~~~


<a id="compare-9d5b724c53ee1d2f0981f74b1be97dd1"></a>

### [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) → [`0080b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b37c.md) FUN_0080b37c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00807d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md) [`008099d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md) [`0080aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080aefc.md) [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`00807db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807db8.md) [`00809a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00809/00809a30.md) [`0080af54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080a/0080af54.md) [`0080b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b37c.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 2件 [`0080b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b37c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md#insn-0080b344) · [`0080b350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md#insn-0080b350)
- 新版 `0080b39c`（命令位置の公開資料なし） · `0080b3a8`（命令位置の公開資料なし）

~~~diff
- 0080b344 ["INT_ADD", "register:40f0:8", ["const:80b344:8", "const:4:8"]]
- 0080b344 ["CALL", null, ["local:b0:8"]]
+ 0080b39c ["INT_ADD", "register:40f0:8", ["const:80b39c:8", "const:4:8"]]
+ 0080b39c ["CALL", null, ["local:b0:8"]]
- 0080b344 bytes f8ffff97
+ 0080b39c bytes f8ffff97
- 0080b350 ["INT_ADD", "register:40f0:8", ["const:80b350:8", "const:4:8"]]
- 0080b350 ["CALL", null, ["local:b0:8"]]
+ 0080b3a8 ["INT_ADD", "register:40f0:8", ["const:80b3a8:8", "const:4:8"]]
+ 0080b3a8 ["CALL", null, ["local:b0:8"]]
- 0080b350 bytes f5ffff97
+ 0080b3a8 bytes f5ffff97
~~~


<a id="compare-7f50a95a5e14245f0dbf9c9a0c2b96c6"></a>

### [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) → [`0080b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b3c0.md) FUN_0080b3c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00807dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807dac.md) [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008491a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008491a4.md) · 呼出先 2件 [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00807e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807e04.md) [`0080b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b3c0.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008491fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008491fc.md) · 呼出先 2件 [`0080b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b3c0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md#insn-0080b384) · [`0080b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md#insn-0080b390) · [`0080b3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md#insn-0080b3a0)
- 新版 `0080b3dc`（命令位置の公開資料なし） · `0080b3e8`（命令位置の公開資料なし） · `0080b3f8`（命令位置の公開資料なし）

~~~diff
- 0080b384 ["INT_ADD", "register:40f0:8", ["const:80b384:8", "const:4:8"]]
- 0080b384 ["CALL", null, ["local:b0:8"]]
+ 0080b3dc ["INT_ADD", "register:40f0:8", ["const:80b3dc:8", "const:4:8"]]
+ 0080b3dc ["CALL", null, ["local:b0:8"]]
- 0080b384 bytes f9ffff97
+ 0080b3dc bytes f9ffff97
- 0080b390 ["INT_ADD", "register:40f0:8", ["const:80b390:8", "const:4:8"]]
- 0080b390 ["CALL", null, ["local:b0:8"]]
+ 0080b3e8 ["INT_ADD", "register:40f0:8", ["const:80b3e8:8", "const:4:8"]]
+ 0080b3e8 ["CALL", null, ["local:b0:8"]]
- 0080b390 bytes f6ffff97
+ 0080b3e8 bytes f6ffff97
- 0080b3a0 ["INT_ADD", "register:40f0:8", ["const:80b3a0:8", "const:4:8"]]
- 0080b3a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080b3f8 ["INT_ADD", "register:40f0:8", ["const:80b3f8:8", "const:4:8"]]
+ 0080b3f8 ["CALL", null, ["callee:00c57f80:8"]]
- 0080b3a0 bytes c4321194
+ 0080b3f8 bytes e2321194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991c7f278c0813bc604276ef09644a92"></a>

### [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) → [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) FUN_0080bd30

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 11件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0080dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md) [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) [`0080e298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e298.md) [`0080e2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 11件 [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) [`0080dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dc8c.md) [`0080deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080deac.md) [`0080e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2f0.md) [`0080e304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e304.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080bd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md#insn-0080bd4c) · [`0080bd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md#insn-0080bd88) · [`0080bdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md#insn-0080bdc0)
- 新版 `0080bda4`（命令位置の公開資料なし） · `0080bde0`（命令位置の公開資料なし） · `0080be18`（命令位置の公開資料なし）

~~~diff
- 0080bd4c ["INT_ADD", "register:40f0:8", ["const:80bd4c:8", "const:4:8"]]
- 0080bd4c ["CALL", null, ["callee:0080dc8c:8"]]
+ 0080bda4 ["INT_ADD", "register:40f0:8", ["const:80bda4:8", "const:4:8"]]
+ 0080bda4 ["CALL", null, ["callee:0080dc8c:8"]]
- 0080bd4c bytes ba070094
+ 0080bda4 bytes ba070094
- 0080bd88 ["INT_ADD", "register:40f0:8", ["const:80bd88:8", "const:4:8"]]
- 0080bd88 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080bde0 ["INT_ADD", "register:40f0:8", ["const:80bde0:8", "const:4:8"]]
+ 0080bde0 ["CALL", null, ["callee:00c57f80:8"]]
- 0080bd88 bytes 4a301194
+ 0080bde0 bytes 68301194
- 0080bdc0 ["INT_ADD", "register:40f0:8", ["const:80bdc0:8", "const:4:8"]]
- 0080bdc0 ["CALL", null, ["callee:0080dc8c:8"]]
+ 0080be18 ["INT_ADD", "register:40f0:8", ["const:80be18:8", "const:4:8"]]
+ 0080be18 ["CALL", null, ["callee:0080dc8c:8"]]
- 0080bdc0 bytes 9d070094
+ 0080be18 bytes 9d070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d047f227e60c2503eeb9455078c07b"></a>

### [`0080c458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c458.md) → [`0080c4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c4b0.md) FUN_0080c4b0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c458.md#insn-0080c550)
- 新版 `0080c5a8`（命令位置の公開資料なし）

~~~diff
- 0080c550 ["INT_ADD", "register:40f0:8", ["const:80c550:8", "const:4:8"]]
- 0080c550 ["CALL", null, ["callee:00c58160:8"]]
+ 0080c5a8 ["INT_ADD", "register:40f0:8", ["const:80c5a8:8", "const:4:8"]]
+ 0080c5a8 ["CALL", null, ["callee:00c58160:8"]]
- 0080c550 bytes d02e1194
+ 0080c5a8 bytes ee2e1194
~~~


<a id="compare-29b81dc320b484041e3451160c33bb15"></a>

### [`0080c570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c570.md) → [`0080c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c5c8.md) FUN_0080c5c8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c570.md#insn-0080c5b0) · [`0080c5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c570.md#insn-0080c5fc) · [`0080c620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c570.md#insn-0080c620)
- 新版 `0080c608`（命令位置の公開資料なし） · `0080c654`（命令位置の公開資料なし） · `0080c678`（命令位置の公開資料なし）

~~~diff
- 0080c5b0 ["INT_ADD", "register:40f0:8", ["const:80c5b0:8", "const:4:8"]]
- 0080c5b0 ["CALL", null, ["callee:00480bd0:8"]]
+ 0080c608 ["INT_ADD", "register:40f0:8", ["const:80c608:8", "const:4:8"]]
+ 0080c608 ["CALL", null, ["callee:00480bd0:8"]]
- 0080c5b0 bytes 78d1f197
+ 0080c608 bytes 72d1f197
- 0080c5fc ["INT_ADD", "register:40f0:8", ["const:80c5fc:8", "const:4:8"]]
- 0080c5fc ["CALL", null, ["callee:00480b78:8"]]
+ 0080c654 ["INT_ADD", "register:40f0:8", ["const:80c654:8", "const:4:8"]]
+ 0080c654 ["CALL", null, ["callee:00480b78:8"]]
- 0080c5fc bytes 4fd1f197
+ 0080c654 bytes 49d1f197
- 0080c620 ["INT_ADD", "register:40f0:8", ["const:80c620:8", "const:4:8"]]
- 0080c620 ["CALL", null, ["callee:00480b78:8"]]
+ 0080c678 ["INT_ADD", "register:40f0:8", ["const:80c678:8", "const:4:8"]]
+ 0080c678 ["CALL", null, ["callee:00480b78:8"]]
- 0080c620 bytes 46d1f197
+ 0080c678 bytes 40d1f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec4c682e7c09a719c8524ed6f460a68"></a>

### [`0080c728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c728.md) → [`0080c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c780.md) FUN_0080c780

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c728.md#insn-0080c754) · [`0080c788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c728.md#insn-0080c788) · [`0080c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c728.md#insn-0080c798)
- 新版 `0080c7ac`（命令位置の公開資料なし） · `0080c7e0`（命令位置の公開資料なし） · `0080c7f0`（命令位置の公開資料なし）

~~~diff
- 0080c754 ["INT_ADD", "register:40f0:8", ["const:80c754:8", "const:4:8"]]
- 0080c754 ["CALL", null, ["callee:004801b8:8"]]
+ 0080c7ac ["INT_ADD", "register:40f0:8", ["const:80c7ac:8", "const:4:8"]]
+ 0080c7ac ["CALL", null, ["callee:004801b8:8"]]
- 0080c754 bytes 89cef197
+ 0080c7ac bytes 83cef197
- 0080c788 ["INT_ADD", "register:40f0:8", ["const:80c788:8", "const:4:8"]]
- 0080c788 ["CALL", null, ["callee:00480158:8"]]
+ 0080c7e0 ["INT_ADD", "register:40f0:8", ["const:80c7e0:8", "const:4:8"]]
+ 0080c7e0 ["CALL", null, ["callee:00480158:8"]]
- 0080c788 bytes 64cef197
+ 0080c7e0 bytes 5ecef197
- 0080c798 ["INT_ADD", "register:40f0:8", ["const:80c798:8", "const:4:8"]]
- 0080c798 ["CALL", null, ["callee:00480158:8"]]
+ 0080c7f0 ["INT_ADD", "register:40f0:8", ["const:80c7f0:8", "const:4:8"]]
+ 0080c7f0 ["CALL", null, ["callee:00480158:8"]]
- 0080c798 bytes 60cef197
+ 0080c7f0 bytes 5acef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5037dd0da94b00bfed54fd6514805520"></a>

### [`0080c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c878.md) → [`0080c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c8d0.md) FUN_0080c8d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 1件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md)
- 新版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 1件 [`0080e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e798.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c878.md#insn-0080c890)
- 新版 `0080c8e8`（命令位置の公開資料なし）

~~~diff
- 0080c890 ["INT_ADD", "register:40f0:8", ["const:80c890:8", "const:4:8"]]
- 0080c890 ["CALL", null, ["callee:0080e798:8"]]
+ 0080c8e8 ["INT_ADD", "register:40f0:8", ["const:80c8e8:8", "const:4:8"]]
+ 0080c8e8 ["CALL", null, ["callee:0080e798:8"]]
- 0080c890 bytes ac070094
+ 0080c8e8 bytes ac070094
~~~


<a id="compare-05ce4ebe1b26b421a34cd2d4b4fb3d98"></a>

### [`0080d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md) → [`0080d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d8b8.md) FUN_0080d8b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0080b824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b824.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) [`00b1b7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1b/00b1b7e8.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0080b87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b87c.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) [`00b1b884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1b/00b1b884.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00794bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md) [`0080dab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dab4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080d904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md#insn-0080d904) · [`0080d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md#insn-0080d950) · [`0080d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md#insn-0080d974)
- 新版 `0080d95c`（命令位置の公開資料なし） · `0080d9a8`（命令位置の公開資料なし） · `0080d9cc`（命令位置の公開資料なし）

~~~diff
- 0080d904 ["INT_ADD", "register:40f0:8", ["const:80d904:8", "const:4:8"]]
- 0080d904 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080d95c ["INT_ADD", "register:40f0:8", ["const:80d95c:8", "const:4:8"]]
+ 0080d95c ["CALL", null, ["callee:00c57f60:8"]]
- 0080d904 bytes 63291194
+ 0080d95c bytes 81291194
- 0080d950 ["INT_ADD", "register:40f0:8", ["const:80d950:8", "const:4:8"]]
- 0080d950 ["CALL", null, ["callee:0080dab4:8"]]
+ 0080d9a8 ["INT_ADD", "register:40f0:8", ["const:80d9a8:8", "const:4:8"]]
+ 0080d9a8 ["CALL", null, ["callee:0080dab4:8"]]
- 0080d950 bytes 43000094
+ 0080d9a8 bytes 43000094
- 0080d974 ["INT_ADD", "register:40f0:8", ["const:80d974:8", "const:4:8"]]
- 0080d974 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080d9cc ["INT_ADD", "register:40f0:8", ["const:80d9cc:8", "const:4:8"]]
+ 0080d9cc ["CALL", null, ["callee:00c57f80:8"]]
- 0080d974 bytes 4f291194
+ 0080d9cc bytes 6d291194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751473fcf0cdd04a1f3f73b76a2f215f"></a>

### [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) → [`0080dab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dab4.md) FUN_0080dab4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md) [`00b2abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0080d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d8b8.md) [`00b2ac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080dad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md#insn-0080dad8) · [`0080db20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md#insn-0080db20)
- 新版 `0080db30`（命令位置の公開資料なし） · `0080db78`（命令位置の公開資料なし）

~~~diff
- 0080dad8 ["INT_ADD", "register:40f0:8", ["const:80dad8:8", "const:4:8"]]
- 0080dad8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080db30 ["INT_ADD", "register:40f0:8", ["const:80db30:8", "const:4:8"]]
+ 0080db30 ["CALL", null, ["callee:00c57f80:8"]]
- 0080dad8 bytes f6281194
+ 0080db30 bytes 14291194
- 0080db20 ["INT_ADD", "register:40f0:8", ["const:80db20:8", "const:4:8"]]
- 0080db20 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080db78 ["INT_ADD", "register:40f0:8", ["const:80db78:8", "const:4:8"]]
+ 0080db78 ["CALL", null, ["callee:00c57f80:8"]]
- 0080db20 bytes e4281194
+ 0080db78 bytes 02291194
~~~


<a id="compare-fe6ddd0361b4b8c1d75349cb6ab84658"></a>

### [`0080db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080db78.md) → [`0080dbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dbd0.md) FUN_0080dbd0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080dbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080db78.md#insn-0080dbac) · [`0080dbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080db78.md#insn-0080dbfc)
- 新版 `0080dc04`（命令位置の公開資料なし） · `0080dc54`（命令位置の公開資料なし）

~~~diff
- 0080dbac ["INT_ADD", "register:40f0:8", ["const:80dbac:8", "const:4:8"]]
- 0080dbac ["CALL", null, ["callee:00c57f80:8"]]
+ 0080dc04 ["INT_ADD", "register:40f0:8", ["const:80dc04:8", "const:4:8"]]
+ 0080dc04 ["CALL", null, ["callee:00c57f80:8"]]
- 0080dbac bytes c1281194
+ 0080dc04 bytes df281194
- 0080dbfc ["INT_ADD", "register:40f0:8", ["const:80dbfc:8", "const:4:8"]]
- 0080dbfc ["CALL", null, ["callee:00c57f80:8"]]
+ 0080dc54 ["INT_ADD", "register:40f0:8", ["const:80dc54:8", "const:4:8"]]
+ 0080dc54 ["CALL", null, ["callee:00c57f80:8"]]
- 0080dbfc bytes ad281194
+ 0080dc54 bytes cb281194
~~~


<a id="compare-05c8bdcdd025430256f6e4d1f10b5533"></a>

### [`0080dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md) → [`0080dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dc8c.md) FUN_0080dc8c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de40.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080de98.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md#insn-0080dce0) · [`0080dd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md#insn-0080dd24) · [`0080dd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md#insn-0080dd68)
- 新版 `0080dd38`（命令位置の公開資料なし） · `0080dd7c`（命令位置の公開資料なし） · `0080ddc0`（命令位置の公開資料なし）

~~~diff
- 0080dce0 ["INT_ADD", "register:40f0:8", ["const:80dce0:8", "const:4:8"]]
- 0080dce0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080dd38 ["INT_ADD", "register:40f0:8", ["const:80dd38:8", "const:4:8"]]
+ 0080dd38 ["CALL", null, ["callee:00c57f60:8"]]
- 0080dce0 bytes 6c281194
+ 0080dd38 bytes 8a281194
- 0080dd24 ["INT_ADD", "register:40f0:8", ["const:80dd24:8", "const:4:8"]]
- 0080dd24 ["CALL", null, ["callee:00c58160:8"]]
+ 0080dd7c ["INT_ADD", "register:40f0:8", ["const:80dd7c:8", "const:4:8"]]
+ 0080dd7c ["CALL", null, ["callee:00c58160:8"]]
- 0080dd24 bytes db281194
+ 0080dd7c bytes f9281194
- 0080dd68 ["INT_ADD", "register:40f0:8", ["const:80dd68:8", "const:4:8"]]
- 0080dd68 ["CALL", null, ["callee:00c58160:8"]]
+ 0080ddc0 ["INT_ADD", "register:40f0:8", ["const:80ddc0:8", "const:4:8"]]
+ 0080ddc0 ["CALL", null, ["callee:00c58160:8"]]
- 0080dd68 bytes ca281194
+ 0080ddc0 bytes e8281194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcbc7de1252fa1d375e4c3ce2fab40e3"></a>

### [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) → [`0080deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080deac.md) FUN_0080deac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md) [`0080e284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e284.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e104.md) [`0080e2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e2dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080df14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md#insn-0080df14) · [`0080df4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md#insn-0080df4c) · [`0080df98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md#insn-0080df98)
- 新版 `0080df6c`（命令位置の公開資料なし） · `0080dfa4`（命令位置の公開資料なし） · `0080dff0`（命令位置の公開資料なし）

~~~diff
- 0080df14 ["INT_ADD", "register:40f0:8", ["const:80df14:8", "const:4:8"]]
- 0080df14 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080df6c ["INT_ADD", "register:40f0:8", ["const:80df6c:8", "const:4:8"]]
+ 0080df6c ["CALL", null, ["callee:00c57f60:8"]]
- 0080df14 bytes df271194
+ 0080df6c bytes fd271194
- 0080df4c ["INT_ADD", "register:40f0:8", ["const:80df4c:8", "const:4:8"]]
- 0080df4c ["CALL", null, ["callee:00c58160:8"]]
+ 0080dfa4 ["INT_ADD", "register:40f0:8", ["const:80dfa4:8", "const:4:8"]]
+ 0080dfa4 ["CALL", null, ["callee:00c58160:8"]]
- 0080df4c bytes 51281194
+ 0080dfa4 bytes 6f281194
- 0080df98 ["INT_ADD", "register:40f0:8", ["const:80df98:8", "const:4:8"]]
- 0080df98 ["CALL", null, ["callee:00c58160:8"]]
+ 0080dff0 ["INT_ADD", "register:40f0:8", ["const:80dff0:8", "const:4:8"]]
+ 0080dff0 ["CALL", null, ["callee:00c58160:8"]]
- 0080df98 bytes 3e281194
+ 0080dff0 bytes 5c281194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250a17d566c2a824ad5cb986daa4d480"></a>

### [`0080e0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md) → [`0080e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e104.md) FUN_0080e104

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0080deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080deac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md#insn-0080e128) · [`0080e170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md#insn-0080e170)
- 新版 `0080e180`（命令位置の公開資料なし） · `0080e1c8`（命令位置の公開資料なし）

~~~diff
- 0080e128 ["INT_ADD", "register:40f0:8", ["const:80e128:8", "const:4:8"]]
- 0080e128 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080e180 ["INT_ADD", "register:40f0:8", ["const:80e180:8", "const:4:8"]]
+ 0080e180 ["CALL", null, ["callee:00c57f80:8"]]
- 0080e128 bytes 62271194
+ 0080e180 bytes 80271194
- 0080e170 ["INT_ADD", "register:40f0:8", ["const:80e170:8", "const:4:8"]]
- 0080e170 ["CALL", null, ["callee:00c57f80:8"]]
+ 0080e1c8 ["INT_ADD", "register:40f0:8", ["const:80e1c8:8", "const:4:8"]]
+ 0080e1c8 ["CALL", null, ["callee:00c57f80:8"]]
- 0080e170 bytes 50271194
+ 0080e1c8 bytes 6e271194
~~~


<a id="compare-b3a534fc091ecbe738e0e7c9c19b2a17"></a>

### [`0080e1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e1c8.md) → [`0080e220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e220.md) FUN_0080e220

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e1c8.md#insn-0080e1fc) · [`0080e24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e1c8.md#insn-0080e24c)
- 新版 `0080e254`（命令位置の公開資料なし） · `0080e2a4`（命令位置の公開資料なし）

~~~diff
- 0080e1fc ["INT_ADD", "register:40f0:8", ["const:80e1fc:8", "const:4:8"]]
- 0080e1fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0080e254 ["INT_ADD", "register:40f0:8", ["const:80e254:8", "const:4:8"]]
+ 0080e254 ["CALL", null, ["callee:00c57f80:8"]]
- 0080e1fc bytes 2d271194
+ 0080e254 bytes 4b271194
- 0080e24c ["INT_ADD", "register:40f0:8", ["const:80e24c:8", "const:4:8"]]
- 0080e24c ["CALL", null, ["callee:00c57f80:8"]]
+ 0080e2a4 ["INT_ADD", "register:40f0:8", ["const:80e2a4:8", "const:4:8"]]
+ 0080e2a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0080e24c bytes 19271194
+ 0080e2a4 bytes 37271194
~~~


<a id="compare-5466fdeab52df705341690ea154af0bb"></a>

### [`0080e2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md) → [`0080e304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e304.md) FUN_0080e304

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e430.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md#insn-0080e324) · [`0080e348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md#insn-0080e348) · [`0080e374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md#insn-0080e374)
- 新版 `0080e37c`（命令位置の公開資料なし） · `0080e3a0`（命令位置の公開資料なし） · `0080e3cc`（命令位置の公開資料なし）

~~~diff
- 0080e324 ["INT_ADD", "register:40f0:8", ["const:80e324:8", "const:4:8"]]
- 0080e324 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080e37c ["INT_ADD", "register:40f0:8", ["const:80e37c:8", "const:4:8"]]
+ 0080e37c ["CALL", null, ["callee:00c57f60:8"]]
- 0080e324 bytes db261194
+ 0080e37c bytes f9261194
- 0080e348 ["INT_ADD", "register:40f0:8", ["const:80e348:8", "const:4:8"]]
- 0080e348 ["CALL", null, ["callee:00c58160:8"]]
+ 0080e3a0 ["INT_ADD", "register:40f0:8", ["const:80e3a0:8", "const:4:8"]]
+ 0080e3a0 ["CALL", null, ["callee:00c58160:8"]]
- 0080e348 bytes 52271194
+ 0080e3a0 bytes 70271194
- 0080e374 ["INT_ADD", "register:40f0:8", ["const:80e374:8", "const:4:8"]]
- 0080e374 ["CALL", null, ["callee:00c58160:8"]]
+ 0080e3cc ["INT_ADD", "register:40f0:8", ["const:80e3cc:8", "const:4:8"]]
+ 0080e3cc ["CALL", null, ["callee:00c58160:8"]]
- 0080e374 bytes 47271194
+ 0080e3cc bytes 65271194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6760a6deb27f5077ef2f3d466170f3f"></a>

### [`0080e3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3ec.md) → [`0080e444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e444.md) FUN_0080e444

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e5f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080e650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e650.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3ec.md#insn-0080e498) · [`0080e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3ec.md#insn-0080e4dc) · [`0080e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3ec.md#insn-0080e520)
- 新版 `0080e4f0`（命令位置の公開資料なし） · `0080e534`（命令位置の公開資料なし） · `0080e578`（命令位置の公開資料なし）

~~~diff
- 0080e498 ["INT_ADD", "register:40f0:8", ["const:80e498:8", "const:4:8"]]
- 0080e498 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080e4f0 ["INT_ADD", "register:40f0:8", ["const:80e4f0:8", "const:4:8"]]
+ 0080e4f0 ["CALL", null, ["callee:00c57f60:8"]]
- 0080e498 bytes 7e261194
+ 0080e4f0 bytes 9c261194
- 0080e4dc ["INT_ADD", "register:40f0:8", ["const:80e4dc:8", "const:4:8"]]
- 0080e4dc ["CALL", null, ["callee:00c58160:8"]]
+ 0080e534 ["INT_ADD", "register:40f0:8", ["const:80e534:8", "const:4:8"]]
+ 0080e534 ["CALL", null, ["callee:00c58160:8"]]
- 0080e4dc bytes ed261194
+ 0080e534 bytes 0b271194
- 0080e520 ["INT_ADD", "register:40f0:8", ["const:80e520:8", "const:4:8"]]
- 0080e520 ["CALL", null, ["callee:00c58160:8"]]
+ 0080e578 ["INT_ADD", "register:40f0:8", ["const:80e578:8", "const:4:8"]]
+ 0080e578 ["CALL", null, ["callee:00c58160:8"]]
- 0080e520 bytes dc261194
+ 0080e578 bytes fa261194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fbf50d5d189befa2ed465730b83372"></a>

### [`0080e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e60c.md) → [`0080e664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e664.md) FUN_0080e664

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e72c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0080e784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e784.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e60c.md#insn-0080e678) · [`0080e69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e60c.md#insn-0080e69c) · [`0080e6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e60c.md#insn-0080e6c8)
- 新版 `0080e6d0`（命令位置の公開資料なし） · `0080e6f4`（命令位置の公開資料なし） · `0080e720`（命令位置の公開資料なし）

~~~diff
- 0080e678 ["INT_ADD", "register:40f0:8", ["const:80e678:8", "const:4:8"]]
- 0080e678 ["CALL", null, ["callee:00c57f60:8"]]
+ 0080e6d0 ["INT_ADD", "register:40f0:8", ["const:80e6d0:8", "const:4:8"]]
+ 0080e6d0 ["CALL", null, ["callee:00c57f60:8"]]
- 0080e678 bytes 06261194
+ 0080e6d0 bytes 24261194
- 0080e69c ["INT_ADD", "register:40f0:8", ["const:80e69c:8", "const:4:8"]]
- 0080e69c ["CALL", null, ["callee:00c58160:8"]]
+ 0080e6f4 ["INT_ADD", "register:40f0:8", ["const:80e6f4:8", "const:4:8"]]
+ 0080e6f4 ["CALL", null, ["callee:00c58160:8"]]
- 0080e69c bytes 7d261194
+ 0080e6f4 bytes 9b261194
- 0080e6c8 ["INT_ADD", "register:40f0:8", ["const:80e6c8:8", "const:4:8"]]
- 0080e6c8 ["CALL", null, ["callee:00c58160:8"]]
+ 0080e720 ["INT_ADD", "register:40f0:8", ["const:80e720:8", "const:4:8"]]
+ 0080e720 ["CALL", null, ["callee:00c58160:8"]]
- 0080e6c8 bytes 72261194
+ 0080e720 bytes 90261194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2439641ff4f972f7235b5a5918672265"></a>

### [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) → [`0080e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e798.md) FUN_0080e798

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0080c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c878.md) [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0080c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c8d0.md) [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`0080e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e798.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849cf0.md) · 呼出先 2件 [`0080e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e798.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md#insn-0080e760) · [`0080e76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md#insn-0080e76c)
- 新版 `0080e7b8`（命令位置の公開資料なし） · `0080e7c4`（命令位置の公開資料なし）

~~~diff
- 0080e760 ["INT_ADD", "register:40f0:8", ["const:80e760:8", "const:4:8"]]
- 0080e760 ["CALL", null, ["local:b0:8"]]
+ 0080e7b8 ["INT_ADD", "register:40f0:8", ["const:80e7b8:8", "const:4:8"]]
+ 0080e7b8 ["CALL", null, ["local:b0:8"]]
- 0080e760 bytes f8ffff97
+ 0080e7b8 bytes f8ffff97
- 0080e76c ["INT_ADD", "register:40f0:8", ["const:80e76c:8", "const:4:8"]]
- 0080e76c ["CALL", null, ["local:b0:8"]]
+ 0080e7c4 ["INT_ADD", "register:40f0:8", ["const:80e7c4:8", "const:4:8"]]
+ 0080e7c4 ["CALL", null, ["local:b0:8"]]
- 0080e76c bytes f5ffff97
+ 0080e7c4 bytes f5ffff97
~~~


<a id="compare-c53ab8f5339a6b31cdd87eb12e753500"></a>

### [`0080e784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e784.md) → [`0080e7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e7dc.md) FUN_0080e7dc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`00a66524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66524.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e784.md#insn-0080e82c) · [`0080e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e784.md#insn-0080e874)
- 新版 `0080e884`（命令位置の公開資料なし） · `0080e8cc`（命令位置の公開資料なし）

~~~diff
- 0080e82c ["INT_ADD", "register:40f0:8", ["const:80e82c:8", "const:4:8"]]
- 0080e82c ["CALL", null, ["callee:00c57f60:8"]]
+ 0080e884 ["INT_ADD", "register:40f0:8", ["const:80e884:8", "const:4:8"]]
+ 0080e884 ["CALL", null, ["callee:00c57f60:8"]]
- 0080e82c bytes 99251194
+ 0080e884 bytes b7251194
- 0080e874 ["INT_ADD", "register:40f0:8", ["const:80e874:8", "const:4:8"]]
- 0080e874 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080e8cc ["INT_ADD", "register:40f0:8", ["const:80e8cc:8", "const:4:8"]]
+ 0080e8cc ["CALL", null, ["callee:0043bbe4:8"]]
- 0080e874 bytes ccb4f097
+ 0080e8cc bytes c6b4f097
~~~


<a id="compare-925245f14621d8716ab69afe3c104dbd"></a>

### [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) → [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) FUN_0080e8f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849cf0.md) · 呼出先 2件 [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md#insn-0080e8c0) · [`0080e8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md#insn-0080e8cc)
- 新版 `0080e918`（命令位置の公開資料なし） · `0080e924`（命令位置の公開資料なし）

~~~diff
- 0080e8c0 ["INT_ADD", "register:40f0:8", ["const:80e8c0:8", "const:4:8"]]
- 0080e8c0 ["CALL", null, ["local:b0:8"]]
+ 0080e918 ["INT_ADD", "register:40f0:8", ["const:80e918:8", "const:4:8"]]
+ 0080e918 ["CALL", null, ["local:b0:8"]]
- 0080e8c0 bytes f8ffff97
+ 0080e918 bytes f8ffff97
- 0080e8cc ["INT_ADD", "register:40f0:8", ["const:80e8cc:8", "const:4:8"]]
- 0080e8cc ["CALL", null, ["local:b0:8"]]
+ 0080e924 ["INT_ADD", "register:40f0:8", ["const:80e924:8", "const:4:8"]]
+ 0080e924 ["CALL", null, ["local:b0:8"]]
- 0080e8cc bytes f5ffff97
+ 0080e924 bytes f5ffff97
~~~


<a id="compare-af8c0236fdee11dd1d72adfbe49aeeba"></a>

### [`0080e8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8e4.md) → [`0080e93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e93c.md) FUN_0080e93c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a670bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a670bc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`00a6712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a6712c.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8e4.md#insn-0080e98c) · [`0080e9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8e4.md#insn-0080e9d4)
- 新版 `0080e9e4`（命令位置の公開資料なし） · `0080ea2c`（命令位置の公開資料なし）

~~~diff
- 0080e98c ["INT_ADD", "register:40f0:8", ["const:80e98c:8", "const:4:8"]]
- 0080e98c ["CALL", null, ["callee:00c57f60:8"]]
+ 0080e9e4 ["INT_ADD", "register:40f0:8", ["const:80e9e4:8", "const:4:8"]]
+ 0080e9e4 ["CALL", null, ["callee:00c57f60:8"]]
- 0080e98c bytes 41251194
+ 0080e9e4 bytes 5f251194
- 0080e9d4 ["INT_ADD", "register:40f0:8", ["const:80e9d4:8", "const:4:8"]]
- 0080e9d4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080ea2c ["INT_ADD", "register:40f0:8", ["const:80ea2c:8", "const:4:8"]]
+ 0080ea2c ["CALL", null, ["callee:0043bbe4:8"]]
- 0080e9d4 bytes 74b4f097
+ 0080ea2c bytes 6eb4f097
~~~


<a id="compare-4a98855d7eb08e61b84a0887e2438dff"></a>

### [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) → [`0080ea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ea58.md) FUN_0080ea58

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`0080ea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ea58.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849cf0.md) · 呼出先 2件 [`0080ea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ea58.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080ea20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md#insn-0080ea20) · [`0080ea2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md#insn-0080ea2c)
- 新版 `0080ea78`（命令位置の公開資料なし） · `0080ea84`（命令位置の公開資料なし）

~~~diff
- 0080ea20 ["INT_ADD", "register:40f0:8", ["const:80ea20:8", "const:4:8"]]
- 0080ea20 ["CALL", null, ["local:b0:8"]]
+ 0080ea78 ["INT_ADD", "register:40f0:8", ["const:80ea78:8", "const:4:8"]]
+ 0080ea78 ["CALL", null, ["local:b0:8"]]
- 0080ea20 bytes f8ffff97
+ 0080ea78 bytes f8ffff97
- 0080ea2c ["INT_ADD", "register:40f0:8", ["const:80ea2c:8", "const:4:8"]]
- 0080ea2c ["CALL", null, ["local:b0:8"]]
+ 0080ea84 ["INT_ADD", "register:40f0:8", ["const:80ea84:8", "const:4:8"]]
+ 0080ea84 ["CALL", null, ["local:b0:8"]]
- 0080ea2c bytes f5ffff97
+ 0080ea84 bytes f5ffff97
~~~


<a id="compare-346fa94330ccf3f8eda135619863fadf"></a>

### [`0080ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea44.md) → [`0080ea9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ea9c.md) FUN_0080ea9c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a676e0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0080d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d560.md) [`00a67750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67750.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080eaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea44.md#insn-0080eaec) · [`0080eb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea44.md#insn-0080eb34)
- 新版 `0080eb44`（命令位置の公開資料なし） · `0080eb8c`（命令位置の公開資料なし）

~~~diff
- 0080eaec ["INT_ADD", "register:40f0:8", ["const:80eaec:8", "const:4:8"]]
- 0080eaec ["CALL", null, ["callee:00c57f60:8"]]
+ 0080eb44 ["INT_ADD", "register:40f0:8", ["const:80eb44:8", "const:4:8"]]
+ 0080eb44 ["CALL", null, ["callee:00c57f60:8"]]
- 0080eaec bytes e9241194
+ 0080eb44 bytes 07251194
- 0080eb34 ["INT_ADD", "register:40f0:8", ["const:80eb34:8", "const:4:8"]]
- 0080eb34 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0080eb8c ["INT_ADD", "register:40f0:8", ["const:80eb8c:8", "const:4:8"]]
+ 0080eb8c ["CALL", null, ["callee:0043bbe4:8"]]
- 0080eb34 bytes 1cb4f097
+ 0080eb8c bytes 16b4f097
~~~


<a id="compare-ce5f4beb404f9055efc57c3b878919ce"></a>

### [`0080eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md) → [`0080ef48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ef48.md) FUN_0080ef48

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007c7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007c7c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7c18.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`007f1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1efc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080ef30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md#insn-0080ef30) · [`0080ef4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md#insn-0080ef4c) · [`0080ef78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md#insn-0080ef78)
- 新版 `0080ef88`（命令位置の公開資料なし） · `0080efa4`（命令位置の公開資料なし） · `0080efd0`（命令位置の公開資料なし）

~~~diff
- 0080ef30 ["INT_ADD", "register:40f0:8", ["const:80ef30:8", "const:4:8"]]
- 0080ef30 ["CALL", null, ["callee:0048797c:8"]]
+ 0080ef88 ["INT_ADD", "register:40f0:8", ["const:80ef88:8", "const:4:8"]]
+ 0080ef88 ["CALL", null, ["callee:0048797c:8"]]
- 0080ef30 bytes 83e2f197
+ 0080ef88 bytes 7de2f197
- 0080ef4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0080ef4c ["INT_ADD", "register:40f0:8", ["const:80ef4c:8", "const:4:8"]]
- 0080ef4c ["CALLIND", null, ["register:0:8"]]
+ 0080efa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0080efa4 ["INT_ADD", "register:40f0:8", ["const:80efa4:8", "const:4:8"]]
+ 0080efa4 ["CALLIND", null, ["register:0:8"]]
- 0080ef4c bytes 00013fd6
+ 0080efa4 bytes 00013fd6
- 0080ef78 ["INT_ADD", "register:40f0:8", ["const:80ef78:8", "const:4:8"]]
- 0080ef78 ["CALL", null, ["callee:0048797c:8"]]
+ 0080efd0 ["INT_ADD", "register:40f0:8", ["const:80efd0:8", "const:4:8"]]
+ 0080efd0 ["CALL", null, ["callee:0048797c:8"]]
- 0080ef78 bytes 71e2f197
+ 0080efd0 bytes 6be2f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d5ddac39be29912784ddbb8a4a36f12"></a>

### [`0080facc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080facc.md) → [`0080fb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fb24.md) FUN_0080fb24

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007859bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859bc.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) · 呼出先 1件 [`0081084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/0081084c.md)
- 新版 呼出元 9件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00785a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785a14.md) [`00787570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md) · 呼出先 1件 [`008108a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080facc.md#insn-0080fb10)
- 新版 `0080fb68`（命令位置の公開資料なし）

~~~diff
- 0080fb10 ["INT_ADD", "register:40f0:8", ["const:80fb10:8", "const:4:8"]]
- 0080fb10 ["CALL", null, ["callee:008108a4:8"]]
+ 0080fb68 ["INT_ADD", "register:40f0:8", ["const:80fb68:8", "const:4:8"]]
+ 0080fb68 ["CALL", null, ["callee:008108a4:8"]]
- 0080fb10 bytes 4f030094
+ 0080fb68 bytes 4f030094
~~~


<a id="compare-0532f0921ba831ed6256589337430266"></a>

### [`0080fb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb14.md) → [`0080fb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fb6c.md) FUN_0080fb6c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0081084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/0081084c.md) [`00810860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810860.md)
- 新版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`008108a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108a4.md) [`008108b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb14.md#insn-0080fb68) · [`0080fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb14.md#insn-0080fb6c)
- 新版 `0080fbc0`（命令位置の公開資料なし） · `0080fbc4`（命令位置の公開資料なし）

~~~diff
- 0080fb68 ["INT_ADD", "register:40f0:8", ["const:80fb68:8", "const:4:8"]]
- 0080fb68 ["CALL", null, ["callee:008108a4:8"]]
+ 0080fbc0 ["INT_ADD", "register:40f0:8", ["const:80fbc0:8", "const:4:8"]]
+ 0080fbc0 ["CALL", null, ["callee:008108a4:8"]]
- 0080fb68 bytes 39030094
+ 0080fbc0 bytes 39030094
- 0080fb6c ["INT_ADD", "register:40f0:8", ["const:80fb6c:8", "const:4:8"]]
- 0080fb6c ["CALL", null, ["callee:008108b8:8"]]
+ 0080fbc4 ["INT_ADD", "register:40f0:8", ["const:80fbc4:8", "const:4:8"]]
+ 0080fbc4 ["CALL", null, ["callee:008108b8:8"]]
- 0080fb6c bytes 3d030094
+ 0080fbc4 bytes 3d030094
~~~


<a id="compare-5f522779f9745b944bbaed817c3f8c7a"></a>

### [`0080fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb80.md) → [`0080fbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fbd8.md) FUN_0080fbd8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00810874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810874.md)
- 新版 呼出元 3件 [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 1件 [`008108cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb80.md#insn-0080fba8)
- 新版 `0080fc00`（命令位置の公開資料なし）

~~~diff
- 0080fba8 ["INT_ADD", "register:40f0:8", ["const:80fba8:8", "const:4:8"]]
- 0080fba8 ["CALL", null, ["callee:008108cc:8"]]
+ 0080fc00 ["INT_ADD", "register:40f0:8", ["const:80fc00:8", "const:4:8"]]
+ 0080fc00 ["CALL", null, ["callee:008108cc:8"]]
- 0080fba8 bytes 33030094
+ 0080fc00 bytes 33030094
~~~


<a id="compare-8322fb7d7a07149a9aeb77ac7ccd6c6e"></a>

### [`00810550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md) → [`008105a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008105a8.md) FUN_008105a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080f128.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`008107c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008107c8.md) [`00810838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810838.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`0080f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080f180.md) · 呼出先 9件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007f1f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f10.md) [`00810820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810820.md) [`00810890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810890.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008105fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md#insn-008105fc) · [`00810648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md#insn-00810648) · [`00810660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md#insn-00810660)
- 新版 `00810654`（命令位置の公開資料なし） · `008106a0`（命令位置の公開資料なし） · `008106b8`（命令位置の公開資料なし）

~~~diff
- 008105fc ["INT_ADD", "register:40f0:8", ["const:8105fc:8", "const:4:8"]]
- 008105fc ["CALL", null, ["callee:00c57f60:8"]]
+ 00810654 ["INT_ADD", "register:40f0:8", ["const:810654:8", "const:4:8"]]
+ 00810654 ["CALL", null, ["callee:00c57f60:8"]]
- 008105fc bytes 251e1194
+ 00810654 bytes 431e1194
- 00810648 ["INT_ADD", "register:40f0:8", ["const:810648:8", "const:4:8"]]
- 00810648 ["CALL", null, ["callee:00c57f60:8"]]
+ 008106a0 ["INT_ADD", "register:40f0:8", ["const:8106a0:8", "const:4:8"]]
+ 008106a0 ["CALL", null, ["callee:00c57f60:8"]]
- 00810648 bytes 121e1194
+ 008106a0 bytes 301e1194
- 00810660 ["INT_ADD", "register:40f0:8", ["const:810660:8", "const:4:8"]]
- 00810660 ["CALL", null, ["callee:00c580d0:8"]]
+ 008106b8 ["INT_ADD", "register:40f0:8", ["const:8106b8:8", "const:4:8"]]
+ 008106b8 ["CALL", null, ["callee:00c580d0:8"]]
- 00810660 bytes 681e1194
+ 008106b8 bytes 861e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ebe0eeb2065d0d6c6a52b27e80a55e5"></a>

### [`008107c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008107c8.md) → [`00810820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810820.md) FUN_00810820

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00810550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008105a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008105a8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008107ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008107c8.md#insn-008107ec)
- 新版 `00810844`（命令位置の公開資料なし）

~~~diff
- 008107ec ["INT_ADD", "register:40f0:8", ["const:8107ec:8", "const:4:8"]]
- 008107ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00810844 ["INT_ADD", "register:40f0:8", ["const:810844:8", "const:4:8"]]
+ 00810844 ["CALL", null, ["callee:00c57f80:8"]]
- 008107ec bytes b11d1194
+ 00810844 bytes cf1d1194
~~~


<a id="compare-8c230623740bd0550d2f75165b7ed81b"></a>

### [`00810888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md) → [`008108e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108e0.md) FUN_008108e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fbac.md) · 呼出先 5件 [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0080fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc04.md) · 呼出先 5件 [`007f1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1efc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008108cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md#insn-008108cc) · [`00810914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md#insn-00810914) · [`0081093c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md#insn-0081093c)
- 新版 `00810924`（命令位置の公開資料なし） · `0081096c`（命令位置の公開資料なし） · `00810994`（命令位置の公開資料なし）

~~~diff
- 008108cc ["INT_ADD", "register:40f0:8", ["const:8108cc:8", "const:4:8"]]
- 008108cc ["CALL", null, ["callee:00c57f80:8"]]
+ 00810924 ["INT_ADD", "register:40f0:8", ["const:810924:8", "const:4:8"]]
+ 00810924 ["CALL", null, ["callee:00c57f80:8"]]
- 008108cc bytes 791d1194
+ 00810924 bytes 971d1194
- 00810914 ["INT_ADD", "register:40f0:8", ["const:810914:8", "const:4:8"]]
- 00810914 ["CALL", null, ["callee:00c57f60:8"]]
+ 0081096c ["INT_ADD", "register:40f0:8", ["const:81096c:8", "const:4:8"]]
+ 0081096c ["CALL", null, ["callee:00c57f60:8"]]
- 00810914 bytes 5f1d1194
+ 0081096c bytes 7d1d1194
- 0081093c ["INT_ADD", "register:40f0:8", ["const:81093c:8", "const:4:8"]]
- 0081093c ["CALL", null, ["callee:00c580d0:8"]]
+ 00810994 ["INT_ADD", "register:40f0:8", ["const:810994:8", "const:4:8"]]
+ 00810994 ["CALL", null, ["callee:00c580d0:8"]]
- 0081093c bytes b11d1194
+ 00810994 bytes cf1d1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a0c55091f0317727d74eec298d81ff7"></a>

### [`008109b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008109b8.md) → [`00810a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810a10.md) FUN_00810a10

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fbcc.md) · 呼出先 5件 [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0080fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc24.md) · 呼出先 5件 [`007f1f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f10.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008109fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008109b8.md#insn-008109fc) · [`00810a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008109b8.md#insn-00810a44) · [`00810a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008109b8.md#insn-00810a6c)
- 新版 `00810a54`（命令位置の公開資料なし） · `00810a9c`（命令位置の公開資料なし） · `00810ac4`（命令位置の公開資料なし）

~~~diff
- 008109fc ["INT_ADD", "register:40f0:8", ["const:8109fc:8", "const:4:8"]]
- 008109fc ["CALL", null, ["callee:00c57f80:8"]]
+ 00810a54 ["INT_ADD", "register:40f0:8", ["const:810a54:8", "const:4:8"]]
+ 00810a54 ["CALL", null, ["callee:00c57f80:8"]]
- 008109fc bytes 2d1d1194
+ 00810a54 bytes 4b1d1194
- 00810a44 ["INT_ADD", "register:40f0:8", ["const:810a44:8", "const:4:8"]]
- 00810a44 ["CALL", null, ["callee:00c57f60:8"]]
+ 00810a9c ["INT_ADD", "register:40f0:8", ["const:810a9c:8", "const:4:8"]]
+ 00810a9c ["CALL", null, ["callee:00c57f60:8"]]
- 00810a44 bytes 131d1194
+ 00810a9c bytes 311d1194
- 00810a6c ["INT_ADD", "register:40f0:8", ["const:810a6c:8", "const:4:8"]]
- 00810a6c ["CALL", null, ["callee:00c580d0:8"]]
+ 00810ac4 ["INT_ADD", "register:40f0:8", ["const:810ac4:8", "const:4:8"]]
+ 00810ac4 ["CALL", null, ["callee:00c580d0:8"]]
- 00810a6c bytes 651d1194
+ 00810ac4 bytes 831d1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9a2d9a84072e001a0237a16ce8ab09"></a>

### [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) → [`00810b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810b40.md) FUN_00810b40

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080fc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fc08.md) [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848390.md) · 呼出先 2件 [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0080fc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc60.md) [`00810b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810b40.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008483e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008483e8.md) · 呼出先 2件 [`00810b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810b40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00810b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md#insn-00810b08) · [`00810b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md#insn-00810b14) · [`00810b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md#insn-00810b50)
- 新版 `00810b60`（命令位置の公開資料なし） · `00810b6c`（命令位置の公開資料なし） · `00810ba8`（命令位置の公開資料なし）

~~~diff
- 00810b08 ["INT_ADD", "register:40f0:8", ["const:810b08:8", "const:4:8"]]
- 00810b08 ["CALL", null, ["local:b0:8"]]
+ 00810b60 ["INT_ADD", "register:40f0:8", ["const:810b60:8", "const:4:8"]]
+ 00810b60 ["CALL", null, ["local:b0:8"]]
- 00810b08 bytes f8ffff97
+ 00810b60 bytes f8ffff97
- 00810b14 ["INT_ADD", "register:40f0:8", ["const:810b14:8", "const:4:8"]]
- 00810b14 ["CALL", null, ["local:b0:8"]]
+ 00810b6c ["INT_ADD", "register:40f0:8", ["const:810b6c:8", "const:4:8"]]
+ 00810b6c ["CALL", null, ["local:b0:8"]]
- 00810b14 bytes f5ffff97
+ 00810b6c bytes f5ffff97
- 00810b50 ["INT_ADD", "register:40f0:8", ["const:810b50:8", "const:4:8"]]
- 00810b50 ["CALL", null, ["callee:00c57f80:8"]]
+ 00810ba8 ["INT_ADD", "register:40f0:8", ["const:810ba8:8", "const:4:8"]]
+ 00810ba8 ["CALL", null, ["callee:00c57f80:8"]]
- 00810b50 bytes d81c1194
+ 00810ba8 bytes f61c1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7927f87764063f4592832188d731aec"></a>

### [`00810b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810b7c.md) → [`00810bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810bd4.md) FUN_00810bd4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fc08.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00810d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810d24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0080fc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fc60.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00810d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/00810d7c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00810c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810b7c.md#insn-00810c08) · [`00810cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810b7c.md#insn-00810cdc) · [`00810cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810b7c.md#insn-00810cf8)
- 新版 `00810c60`（命令位置の公開資料なし） · `00810d34`（命令位置の公開資料なし） · `00810d50`（命令位置の公開資料なし）

~~~diff
- 00810c08 ["INT_ADD", "register:40f0:8", ["const:810c08:8", "const:4:8"]]
- 00810c08 ["CALL", null, ["callee:00c57f60:8"]]
+ 00810c60 ["INT_ADD", "register:40f0:8", ["const:810c60:8", "const:4:8"]]
+ 00810c60 ["CALL", null, ["callee:00c57f60:8"]]
- 00810c08 bytes a21c1194
+ 00810c60 bytes c01c1194
- 00810cdc ["INT_ADD", "register:40f0:8", ["const:810cdc:8", "const:4:8"]]
- 00810cdc ["CALL", null, ["callee:00c57f80:8"]]
+ 00810d34 ["INT_ADD", "register:40f0:8", ["const:810d34:8", "const:4:8"]]
+ 00810d34 ["CALL", null, ["callee:00c57f80:8"]]
- 00810cdc bytes 751c1194
+ 00810d34 bytes 931c1194
- 00810cf8 ["INT_ADD", "register:40f0:8", ["const:810cf8:8", "const:4:8"]]
- 00810cf8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00810d50 ["INT_ADD", "register:40f0:8", ["const:810d50:8", "const:4:8"]]
+ 00810d50 ["CALL", null, ["callee:00c57f80:8"]]
- 00810cf8 bytes 6e1c1194
+ 00810d50 bytes 8c1c1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6012c849b9c611757cd2c88beb9a2e"></a>

### [`00813954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813954.md) → [`008139ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/008139ac.md) FUN_008139ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813954.md#insn-00813970) · [`00813980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813954.md#insn-00813980)
- 新版 `008139c8`（命令位置の公開資料なし） · `008139d8`（命令位置の公開資料なし）

~~~diff
- 00813970 ["INT_ADD", "register:40f0:8", ["const:813970:8", "const:4:8"]]
- 00813970 ["CALL", null, ["callee:00c57f80:8"]]
+ 008139c8 ["INT_ADD", "register:40f0:8", ["const:8139c8:8", "const:4:8"]]
+ 008139c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00813970 bytes 50111194
+ 008139c8 bytes 6e111194
- 00813980 ["INT_ADD", "register:40f0:8", ["const:813980:8", "const:4:8"]]
- 00813980 ["CALL", null, ["callee:00c57f80:8"]]
+ 008139d8 ["INT_ADD", "register:40f0:8", ["const:8139d8:8", "const:4:8"]]
+ 008139d8 ["CALL", null, ["callee:00c57f80:8"]]
- 00813980 bytes 4c111194
+ 008139d8 bytes 6a111194
~~~


<a id="compare-a62b716cc290bc734a5ed22dd94d09c4"></a>

### [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) → [`00813a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813a00.md) FUN_00813a00

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md)
- 新版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`00813ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813ea8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md#insn-00813a50) · [`00813a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md#insn-00813a74) · [`00813a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md#insn-00813a88)
- 新版 `00813aa8`（命令位置の公開資料なし） · `00813acc`（命令位置の公開資料なし） · `00813ae0`（命令位置の公開資料なし）

~~~diff
- 00813a50 ["INT_ADD", "register:40f0:8", ["const:813a50:8", "const:4:8"]]
- 00813a50 ["CALL", null, ["callee:00813ea8:8"]]
+ 00813aa8 ["INT_ADD", "register:40f0:8", ["const:813aa8:8", "const:4:8"]]
+ 00813aa8 ["CALL", null, ["callee:00813ea8:8"]]
- 00813a50 bytes 00010094
+ 00813aa8 bytes 00010094
- 00813a74 ["INT_ADD", "register:40f0:8", ["const:813a74:8", "const:4:8"]]
- 00813a74 ["CALL", null, ["callee:00814030:8"]]
+ 00813acc ["INT_ADD", "register:40f0:8", ["const:813acc:8", "const:4:8"]]
+ 00813acc ["CALL", null, ["callee:00814030:8"]]
- 00813a74 bytes 59010094
+ 00813acc bytes 59010094
- 00813a88 ["INT_ADD", "register:40f0:8", ["const:813a88:8", "const:4:8"]]
- 00813a88 ["CALL", null, ["callee:00814030:8"]]
+ 00813ae0 ["INT_ADD", "register:40f0:8", ["const:813ae0:8", "const:4:8"]]
+ 00813ae0 ["CALL", null, ["callee:00814030:8"]]
- 00813a88 bytes 54010094
+ 00813ae0 bytes 54010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59e1cf06d275666313e1031a96ace15"></a>

### [`00813dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813dfc.md) → [`00813e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813e54.md) FUN_00813e54

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813dfc.md#insn-00813e18) · [`00813e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813dfc.md#insn-00813e28)
- 新版 `00813e70`（命令位置の公開資料なし） · `00813e80`（命令位置の公開資料なし）

~~~diff
- 00813e18 ["INT_ADD", "register:40f0:8", ["const:813e18:8", "const:4:8"]]
- 00813e18 ["CALL", null, ["callee:00c57f80:8"]]
+ 00813e70 ["INT_ADD", "register:40f0:8", ["const:813e70:8", "const:4:8"]]
+ 00813e70 ["CALL", null, ["callee:00c57f80:8"]]
- 00813e18 bytes 26101194
+ 00813e70 bytes 44101194
- 00813e28 ["INT_ADD", "register:40f0:8", ["const:813e28:8", "const:4:8"]]
- 00813e28 ["CALL", null, ["callee:00c57f80:8"]]
+ 00813e80 ["INT_ADD", "register:40f0:8", ["const:813e80:8", "const:4:8"]]
+ 00813e80 ["CALL", null, ["callee:00c57f80:8"]]
- 00813e28 bytes 22101194
+ 00813e80 bytes 40101194
~~~


<a id="compare-f851d8d7278bca08860bf1aa064d0560"></a>

### [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md) → [`00813ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813ea8.md) FUN_00813ea8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) · 呼出先 4件 [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00813a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813a00.md) · 呼出先 4件 [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md#insn-00813e98) · [`00813eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md#insn-00813eb0) · [`00813ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md#insn-00813ed8)
- 新版 `00813ef0`（命令位置の公開資料なし） · `00813f08`（命令位置の公開資料なし） · `00813f30`（命令位置の公開資料なし）

~~~diff
- 00813e98 ["INT_ADD", "register:40f0:8", ["const:813e98:8", "const:4:8"]]
- 00813e98 ["CALL", null, ["callee:00c57f60:8"]]
+ 00813ef0 ["INT_ADD", "register:40f0:8", ["const:813ef0:8", "const:4:8"]]
+ 00813ef0 ["CALL", null, ["callee:00c57f60:8"]]
- 00813e98 bytes fe0f1194
+ 00813ef0 bytes 1c101194
- 00813eb0 ["INT_ADD", "register:40f0:8", ["const:813eb0:8", "const:4:8"]]
- 00813eb0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00813f08 ["INT_ADD", "register:40f0:8", ["const:813f08:8", "const:4:8"]]
+ 00813f08 ["CALL", null, ["callee:00c580d0:8"]]
- 00813eb0 bytes 54101194
+ 00813f08 bytes 72101194
- 00813ed8 ["INT_ADD", "register:40f0:8", ["const:813ed8:8", "const:4:8"]]
- 00813ed8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00813f30 ["INT_ADD", "register:40f0:8", ["const:813f30:8", "const:4:8"]]
+ 00813f30 ["CALL", null, ["callee:00c57f60:8"]]
- 00813ed8 bytes ee0f1194
+ 00813f30 bytes 0c101194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71cbe191f0903c06cf99fbd38cc848ef"></a>

### [`00813fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md) → [`00814030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md) FUN_00814030

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) [`008b6ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ec4.md) · 呼出先 5件 [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00813a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813a00.md) [`008b6f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f1c.md) · 呼出先 5件 [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081401c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md#insn-0081401c) · [`00814064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md#insn-00814064) · [`0081408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md#insn-0081408c)
- 新版 `00814074`（命令位置の公開資料なし） · `008140bc`（命令位置の公開資料なし） · `008140e4`（命令位置の公開資料なし）

~~~diff
- 0081401c ["INT_ADD", "register:40f0:8", ["const:81401c:8", "const:4:8"]]
- 0081401c ["CALL", null, ["callee:00c57f80:8"]]
+ 00814074 ["INT_ADD", "register:40f0:8", ["const:814074:8", "const:4:8"]]
+ 00814074 ["CALL", null, ["callee:00c57f80:8"]]
- 0081401c bytes a50f1194
+ 00814074 bytes c30f1194
- 00814064 ["INT_ADD", "register:40f0:8", ["const:814064:8", "const:4:8"]]
- 00814064 ["CALL", null, ["callee:00c57f60:8"]]
+ 008140bc ["INT_ADD", "register:40f0:8", ["const:8140bc:8", "const:4:8"]]
+ 008140bc ["CALL", null, ["callee:00c57f60:8"]]
- 00814064 bytes 8b0f1194
+ 008140bc bytes a90f1194
- 0081408c ["INT_ADD", "register:40f0:8", ["const:81408c:8", "const:4:8"]]
- 0081408c ["CALL", null, ["callee:00c580d0:8"]]
+ 008140e4 ["INT_ADD", "register:40f0:8", ["const:8140e4:8", "const:4:8"]]
+ 008140e4 ["CALL", null, ["callee:00c580d0:8"]]
- 0081408c bytes dd0f1194
+ 008140e4 bytes fb0f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac1531827700c78c5205ebbc994a0b4"></a>

### [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) → [`00814160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814160.md) FUN_00814160

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00812f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00812/00812f24.md) [`00814160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814160.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 2件 [`00814160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814160.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00814124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md#insn-00814124) · [`00814130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md#insn-00814130) · [`00814140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md#insn-00814140)
- 新版 `0081417c`（命令位置の公開資料なし） · `00814188`（命令位置の公開資料なし） · `00814198`（命令位置の公開資料なし）

~~~diff
- 00814124 ["INT_ADD", "register:40f0:8", ["const:814124:8", "const:4:8"]]
- 00814124 ["CALL", null, ["local:b0:8"]]
+ 0081417c ["INT_ADD", "register:40f0:8", ["const:81417c:8", "const:4:8"]]
+ 0081417c ["CALL", null, ["local:b0:8"]]
- 00814124 bytes f9ffff97
+ 0081417c bytes f9ffff97
- 00814130 ["INT_ADD", "register:40f0:8", ["const:814130:8", "const:4:8"]]
- 00814130 ["CALL", null, ["local:b0:8"]]
+ 00814188 ["INT_ADD", "register:40f0:8", ["const:814188:8", "const:4:8"]]
+ 00814188 ["CALL", null, ["local:b0:8"]]
- 00814130 bytes f6ffff97
+ 00814188 bytes f6ffff97
- 00814140 ["INT_ADD", "register:40f0:8", ["const:814140:8", "const:4:8"]]
- 00814140 ["CALL", null, ["callee:00c57f80:8"]]
+ 00814198 ["INT_ADD", "register:40f0:8", ["const:814198:8", "const:4:8"]]
+ 00814198 ["CALL", null, ["callee:00c57f80:8"]]
- 00814140 bytes 5c0f1194
+ 00814198 bytes 7a0f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82aed1e08c3c035072786f76b4e3d33"></a>

### [`0081560c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/0081560c.md) → [`00815664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00815/00815664.md) FUN_00815664

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008157a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/008157a4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008157fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00815/008157fc.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081564c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/0081560c.md#insn-0081564c) · [`0081565c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/0081560c.md#insn-0081565c) · [`0081566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/0081560c.md#insn-0081566c)
- 新版 `008156a4`（命令位置の公開資料なし） · `008156b4`（命令位置の公開資料なし） · `008156c4`（命令位置の公開資料なし）

~~~diff
- 0081564c ["INT_ADD", "register:40f0:8", ["const:81564c:8", "const:4:8"]]
- 0081564c ["CALL", null, ["callee:0048797c:8"]]
+ 008156a4 ["INT_ADD", "register:40f0:8", ["const:8156a4:8", "const:4:8"]]
+ 008156a4 ["CALL", null, ["callee:0048797c:8"]]
- 0081564c bytes bcc8f197
+ 008156a4 bytes b6c8f197
- 0081565c ["INT_ADD", "register:40f0:8", ["const:81565c:8", "const:4:8"]]
- 0081565c ["CALL", null, ["callee:0048797c:8"]]
+ 008156b4 ["INT_ADD", "register:40f0:8", ["const:8156b4:8", "const:4:8"]]
+ 008156b4 ["CALL", null, ["callee:0048797c:8"]]
- 0081565c bytes b8c8f197
+ 008156b4 bytes b2c8f197
- 0081566c ["INT_ADD", "register:40f0:8", ["const:81566c:8", "const:4:8"]]
- 0081566c ["CALL", null, ["callee:0048797c:8"]]
+ 008156c4 ["INT_ADD", "register:40f0:8", ["const:8156c4:8", "const:4:8"]]
+ 008156c4 ["CALL", null, ["callee:0048797c:8"]]
- 0081566c bytes b4c8f197
+ 008156c4 bytes aec8f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf4da11f47ced69f0335f2a0c400d8e"></a>

### [`008173a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00817/008173a0.md) → [`008173f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00817/008173f8.md) FUN_008173f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`006b8c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00817/008173a0.md#insn-00817424) · [`00817450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00817/008173a0.md#insn-00817450) · [`00817498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00817/008173a0.md#insn-00817498)
- 新版 `0081747c`（命令位置の公開資料なし） · `008174a8`（命令位置の公開資料なし） · `008174f0`（命令位置の公開資料なし）

~~~diff
- 00817424 ["INT_ADD", "register:40f0:8", ["const:817424:8", "const:4:8"]]
- 00817424 ["CALL", null, ["callee:004410cc:8"]]
+ 0081747c ["INT_ADD", "register:40f0:8", ["const:81747c:8", "const:4:8"]]
+ 0081747c ["CALL", null, ["callee:004410cc:8"]]
- 00817424 bytes 1aa7f097
+ 0081747c bytes 14a7f097
- 00817450 ["INT_ADD", "register:40f0:8", ["const:817450:8", "const:4:8"]]
- 00817450 ["CALL", null, ["callee:00c57f80:8"]]
+ 008174a8 ["INT_ADD", "register:40f0:8", ["const:8174a8:8", "const:4:8"]]
+ 008174a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00817450 bytes 98021194
+ 008174a8 bytes b6021194
- 00817498 ["COPY", "register:0:8", ["register:4040:8"]]
- 00817498 ["INT_ADD", "register:40f0:8", ["const:817498:8", "const:4:8"]]
- 00817498 ["CALLIND", null, ["register:0:8"]]
+ 008174f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008174f0 ["INT_ADD", "register:40f0:8", ["const:8174f0:8", "const:4:8"]]
+ 008174f0 ["CALLIND", null, ["register:0:8"]]
- 00817498 bytes 00013fd6
+ 008174f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d639a2c97feb82caaad889a9d847602c"></a>

### [`008199ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/008199ac.md) → [`00819a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819a04.md) FUN_00819a04

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008199c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/008199ac.md#insn-008199c8) · [`008199d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/008199ac.md#insn-008199d8) · [`008199e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/008199ac.md#insn-008199e8)
- 新版 `00819a20`（命令位置の公開資料なし） · `00819a30`（命令位置の公開資料なし） · `00819a40`（命令位置の公開資料なし）

~~~diff
- 008199c8 ["INT_ADD", "register:40f0:8", ["const:8199c8:8", "const:4:8"]]
- 008199c8 ["CALL", null, ["callee:0048797c:8"]]
+ 00819a20 ["INT_ADD", "register:40f0:8", ["const:819a20:8", "const:4:8"]]
+ 00819a20 ["CALL", null, ["callee:0048797c:8"]]
- 008199c8 bytes ddb7f197
+ 00819a20 bytes d7b7f197
- 008199d8 ["INT_ADD", "register:40f0:8", ["const:8199d8:8", "const:4:8"]]
- 008199d8 ["CALL", null, ["callee:0048797c:8"]]
+ 00819a30 ["INT_ADD", "register:40f0:8", ["const:819a30:8", "const:4:8"]]
+ 00819a30 ["CALL", null, ["callee:0048797c:8"]]
- 008199d8 bytes d9b7f197
+ 00819a30 bytes d3b7f197
- 008199e8 ["INT_ADD", "register:40f0:8", ["const:8199e8:8", "const:4:8"]]
- 008199e8 ["CALL", null, ["callee:0048797c:8"]]
+ 00819a40 ["INT_ADD", "register:40f0:8", ["const:819a40:8", "const:4:8"]]
+ 00819a40 ["CALL", null, ["callee:0048797c:8"]]
- 008199e8 bytes d5b7f197
+ 00819a40 bytes cfb7f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53229428fbd39d8630e6e1efaba7cec4"></a>

### [`00819a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819a7c.md) → [`00819ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819ad4.md) FUN_00819ad4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819a7c.md#insn-00819ae4) · [`00819af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819a7c.md#insn-00819af4) · [`00819b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819a7c.md#insn-00819b04)
- 新版 `00819b3c`（命令位置の公開資料なし） · `00819b4c`（命令位置の公開資料なし） · `00819b5c`（命令位置の公開資料なし）

~~~diff
- 00819ae4 ["INT_ADD", "register:40f0:8", ["const:819ae4:8", "const:4:8"]]
- 00819ae4 ["CALL", null, ["callee:0048797c:8"]]
+ 00819b3c ["INT_ADD", "register:40f0:8", ["const:819b3c:8", "const:4:8"]]
+ 00819b3c ["CALL", null, ["callee:0048797c:8"]]
- 00819ae4 bytes 96b7f197
+ 00819b3c bytes 90b7f197
- 00819af4 ["INT_ADD", "register:40f0:8", ["const:819af4:8", "const:4:8"]]
- 00819af4 ["CALL", null, ["callee:0048797c:8"]]
+ 00819b4c ["INT_ADD", "register:40f0:8", ["const:819b4c:8", "const:4:8"]]
+ 00819b4c ["CALL", null, ["callee:0048797c:8"]]
- 00819af4 bytes 92b7f197
+ 00819b4c bytes 8cb7f197
- 00819b04 ["INT_ADD", "register:40f0:8", ["const:819b04:8", "const:4:8"]]
- 00819b04 ["CALL", null, ["callee:0048797c:8"]]
+ 00819b5c ["INT_ADD", "register:40f0:8", ["const:819b5c:8", "const:4:8"]]
+ 00819b5c ["CALL", null, ["callee:0048797c:8"]]
- 00819b04 bytes 8eb7f197
+ 00819b5c bytes 88b7f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376b6ab0a5156020b850325efa1a4bb1"></a>

### [`00819cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md) → [`00819d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819d34.md) FUN_00819d34

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0081c5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c5a8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md#insn-00819d28) · [`00819d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md#insn-00819d3c) · [`00819d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md#insn-00819d44)
- 新版 `00819d80`（命令位置の公開資料なし） · `00819d94`（命令位置の公開資料なし） · `00819d9c`（命令位置の公開資料なし）

~~~diff
- 00819d28 ["INT_ADD", "register:40f0:8", ["const:819d28:8", "const:4:8"]]
- 00819d28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00819d80 ["INT_ADD", "register:40f0:8", ["const:819d80:8", "const:4:8"]]
+ 00819d80 ["CALL", null, ["callee:00c53da0:8"]]
- 00819d28 bytes f6e71094
+ 00819d80 bytes 08e81094
- 00819d3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00819d3c ["INT_ADD", "register:40f0:8", ["const:819d3c:8", "const:4:8"]]
- 00819d3c ["CALLIND", null, ["register:0:8"]]
+ 00819d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819d94 ["INT_ADD", "register:40f0:8", ["const:819d94:8", "const:4:8"]]
+ 00819d94 ["CALLIND", null, ["register:0:8"]]
- 00819d3c bytes 00013fd6
+ 00819d94 bytes 00013fd6
- 00819d44 ["INT_ADD", "register:40f0:8", ["const:819d44:8", "const:4:8"]]
- 00819d44 ["CALL", null, ["callee:00c57f50:8"]]
+ 00819d9c ["INT_ADD", "register:40f0:8", ["const:819d9c:8", "const:4:8"]]
+ 00819d9c ["CALL", null, ["callee:00c57f50:8"]]
- 00819d44 bytes 4ff81094
+ 00819d9c bytes 6df81094
~~~


<a id="compare-94345c1dd36abc0ce80bb11838d8ce40"></a>

### [`00819d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md) → [`00819dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819dcc.md) FUN_00819dcc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md#insn-00819d90) · [`00819db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md#insn-00819db0)
- 新版 `00819de8`（命令位置の公開資料なし） · `00819e08`（命令位置の公開資料なし）

~~~diff
- 00819d90 ["INT_ADD", "register:40f0:8", ["const:819d90:8", "const:4:8"]]
- 00819d90 ["CALL", null, ["callee:00c53da0:8"]]
+ 00819de8 ["INT_ADD", "register:40f0:8", ["const:819de8:8", "const:4:8"]]
+ 00819de8 ["CALL", null, ["callee:00c53da0:8"]]
- 00819d90 bytes dce71094
+ 00819de8 bytes eee71094
- 00819db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00819db0 ["INT_ADD", "register:40f0:8", ["const:819db0:8", "const:4:8"]]
- 00819db0 ["CALLIND", null, ["register:0:8"]]
+ 00819e08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819e08 ["INT_ADD", "register:40f0:8", ["const:819e08:8", "const:4:8"]]
+ 00819e08 ["CALLIND", null, ["register:0:8"]]
- 00819db0 bytes 00013fd6
+ 00819e08 bytes 00013fd6
~~~


<a id="compare-6f4ab1ecab0daa4ce9e931668bbae493"></a>

### [`00819dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md) → [`00819e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819e1c.md) FUN_00819e1c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0081a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a5e8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md#insn-00819e28) · [`00819e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md#insn-00819e3c) · [`00819e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md#insn-00819e50)
- 新版 `00819e80`（命令位置の公開資料なし） · `00819e94`（命令位置の公開資料なし） · `00819ea8`（命令位置の公開資料なし）

~~~diff
- 00819e28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00819e28 ["INT_ADD", "register:40f0:8", ["const:819e28:8", "const:4:8"]]
- 00819e28 ["CALLIND", null, ["register:0:8"]]
+ 00819e80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819e80 ["INT_ADD", "register:40f0:8", ["const:819e80:8", "const:4:8"]]
+ 00819e80 ["CALLIND", null, ["register:0:8"]]
- 00819e28 bytes 00013fd6
+ 00819e80 bytes 00013fd6
- 00819e3c ["INT_ADD", "register:40f0:8", ["const:819e3c:8", "const:4:8"]]
- 00819e3c ["CALL", null, ["callee:0048797c:8"]]
+ 00819e94 ["INT_ADD", "register:40f0:8", ["const:819e94:8", "const:4:8"]]
+ 00819e94 ["CALL", null, ["callee:0048797c:8"]]
- 00819e3c bytes c0b6f197
+ 00819e94 bytes bab6f197
- 00819e50 ["INT_ADD", "register:40f0:8", ["const:819e50:8", "const:4:8"]]
- 00819e50 ["CALL", null, ["callee:0048797c:8"]]
+ 00819ea8 ["INT_ADD", "register:40f0:8", ["const:819ea8:8", "const:4:8"]]
+ 00819ea8 ["CALL", null, ["callee:0048797c:8"]]
- 00819e50 bytes bbb6f197
+ 00819ea8 bytes b5b6f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-898df9d64888e8905e41fbebd6545535"></a>

### [`0081a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md) → [`0081a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a5e8.md) FUN_0081a5e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 4件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00819dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 4件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00819e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819e1c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md#insn-0081a5f8) · [`0081a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md#insn-0081a608) · [`0081a618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md#insn-0081a618)
- 新版 `0081a650`（命令位置の公開資料なし） · `0081a660`（命令位置の公開資料なし） · `0081a670`（命令位置の公開資料なし）

~~~diff
- 0081a5f8 ["INT_ADD", "register:40f0:8", ["const:81a5f8:8", "const:4:8"]]
- 0081a5f8 ["CALL", null, ["callee:0048797c:8"]]
+ 0081a650 ["INT_ADD", "register:40f0:8", ["const:81a650:8", "const:4:8"]]
+ 0081a650 ["CALL", null, ["callee:0048797c:8"]]
- 0081a5f8 bytes d1b4f197
+ 0081a650 bytes cbb4f197
- 0081a608 ["INT_ADD", "register:40f0:8", ["const:81a608:8", "const:4:8"]]
- 0081a608 ["CALL", null, ["callee:0048797c:8"]]
+ 0081a660 ["INT_ADD", "register:40f0:8", ["const:81a660:8", "const:4:8"]]
+ 0081a660 ["CALL", null, ["callee:0048797c:8"]]
- 0081a608 bytes cdb4f197
+ 0081a660 bytes c7b4f197
- 0081a618 ["INT_ADD", "register:40f0:8", ["const:81a618:8", "const:4:8"]]
- 0081a618 ["CALL", null, ["callee:0048797c:8"]]
+ 0081a670 ["INT_ADD", "register:40f0:8", ["const:81a670:8", "const:4:8"]]
+ 0081a670 ["CALL", null, ["callee:0048797c:8"]]
- 0081a618 bytes c9b4f197
+ 0081a670 bytes c3b4f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b59a64b32ee44bae73003714e1f06a"></a>

### [`0081a6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a6e4.md) → [`0081a73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a73c.md) FUN_0081a73c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a6e4.md#insn-0081a730) · [`0081a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a6e4.md#insn-0081a744) · [`0081a74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a6e4.md#insn-0081a74c)
- 新版 `0081a788`（命令位置の公開資料なし） · `0081a79c`（命令位置の公開資料なし） · `0081a7a4`（命令位置の公開資料なし）

~~~diff
- 0081a730 ["INT_ADD", "register:40f0:8", ["const:81a730:8", "const:4:8"]]
- 0081a730 ["CALL", null, ["callee:00c53da0:8"]]
+ 0081a788 ["INT_ADD", "register:40f0:8", ["const:81a788:8", "const:4:8"]]
+ 0081a788 ["CALL", null, ["callee:00c53da0:8"]]
- 0081a730 bytes 74e51094
+ 0081a788 bytes 86e51094
- 0081a744 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081a744 ["INT_ADD", "register:40f0:8", ["const:81a744:8", "const:4:8"]]
- 0081a744 ["CALLIND", null, ["register:0:8"]]
+ 0081a79c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081a79c ["INT_ADD", "register:40f0:8", ["const:81a79c:8", "const:4:8"]]
+ 0081a79c ["CALLIND", null, ["register:0:8"]]
- 0081a744 bytes 00013fd6
+ 0081a79c bytes 00013fd6
- 0081a74c ["INT_ADD", "register:40f0:8", ["const:81a74c:8", "const:4:8"]]
- 0081a74c ["CALL", null, ["callee:00c57f50:8"]]
+ 0081a7a4 ["INT_ADD", "register:40f0:8", ["const:81a7a4:8", "const:4:8"]]
+ 0081a7a4 ["CALL", null, ["callee:00c57f50:8"]]
- 0081a74c bytes cdf51094
+ 0081a7a4 bytes ebf51094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40035aaddcb06f0366089a6157d9f1c9"></a>

### [`0081a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md) → [`0081a81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a81c.md) FUN_0081a81c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md#insn-0081a7e0) · [`0081a800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md#insn-0081a800)
- 新版 `0081a838`（命令位置の公開資料なし） · `0081a858`（命令位置の公開資料なし）

~~~diff
- 0081a7e0 ["INT_ADD", "register:40f0:8", ["const:81a7e0:8", "const:4:8"]]
- 0081a7e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0081a838 ["INT_ADD", "register:40f0:8", ["const:81a838:8", "const:4:8"]]
+ 0081a838 ["CALL", null, ["callee:00c53da0:8"]]
- 0081a7e0 bytes 48e51094
+ 0081a838 bytes 5ae51094
- 0081a800 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081a800 ["INT_ADD", "register:40f0:8", ["const:81a800:8", "const:4:8"]]
- 0081a800 ["CALLIND", null, ["register:0:8"]]
+ 0081a858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081a858 ["INT_ADD", "register:40f0:8", ["const:81a858:8", "const:4:8"]]
+ 0081a858 ["CALLIND", null, ["register:0:8"]]
- 0081a800 bytes 00013fd6
+ 0081a858 bytes 00013fd6
~~~


<a id="compare-0d8be99070e4730259139797f8f1d213"></a>

### [`0081c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2a4.md) → [`0081c2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c2fc.md) FUN_0081c2fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2a4.md#insn-0081c2c0) · [`0081c2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2a4.md#insn-0081c2e0)
- 新版 `0081c318`（命令位置の公開資料なし） · `0081c338`（命令位置の公開資料なし）

~~~diff
- 0081c2c0 ["INT_ADD", "register:40f0:8", ["const:81c2c0:8", "const:4:8"]]
- 0081c2c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0081c318 ["INT_ADD", "register:40f0:8", ["const:81c318:8", "const:4:8"]]
+ 0081c318 ["CALL", null, ["callee:00c53da0:8"]]
- 0081c2c0 bytes 90de1094
+ 0081c318 bytes a2de1094
- 0081c2e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c2e0 ["INT_ADD", "register:40f0:8", ["const:81c2e0:8", "const:4:8"]]
- 0081c2e0 ["CALLIND", null, ["register:0:8"]]
+ 0081c338 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c338 ["INT_ADD", "register:40f0:8", ["const:81c338:8", "const:4:8"]]
+ 0081c338 ["CALLIND", null, ["register:0:8"]]
- 0081c2e0 bytes 00013fd6
+ 0081c338 bytes 00013fd6
~~~


<a id="compare-873ca058395e4a0f393a4937a92756e9"></a>

### [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) → [`0081c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c34c.md) FUN_0081c34c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`00830658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830658.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`0082d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d800.md) [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md) [`008306b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md#insn-0081c314) · [`0081c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md#insn-0081c350) · [`0081c364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md#insn-0081c364)
- 新版 `0081c36c`（命令位置の公開資料なし） · `0081c3a8`（命令位置の公開資料なし） · `0081c3bc`（命令位置の公開資料なし）

~~~diff
- 0081c314 ["INT_ADD", "register:40f0:8", ["const:81c314:8", "const:4:8"]]
- 0081c314 ["CALL", null, ["callee:00c57f80:8"]]
+ 0081c36c ["INT_ADD", "register:40f0:8", ["const:81c36c:8", "const:4:8"]]
+ 0081c36c ["CALL", null, ["callee:00c57f80:8"]]
- 0081c314 bytes e7ee1094
+ 0081c36c bytes 05ef1094
- 0081c350 ["INT_ADD", "register:40f0:8", ["const:81c350:8", "const:4:8"]]
- 0081c350 ["CALL", null, ["callee:00c53da0:8"]]
+ 0081c3a8 ["INT_ADD", "register:40f0:8", ["const:81c3a8:8", "const:4:8"]]
+ 0081c3a8 ["CALL", null, ["callee:00c53da0:8"]]
- 0081c350 bytes 6cde1094
+ 0081c3a8 bytes 7ede1094
- 0081c364 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c364 ["INT_ADD", "register:40f0:8", ["const:81c364:8", "const:4:8"]]
- 0081c364 ["CALLIND", null, ["register:0:8"]]
+ 0081c3bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c3bc ["INT_ADD", "register:40f0:8", ["const:81c3bc:8", "const:4:8"]]
+ 0081c3bc ["CALLIND", null, ["register:0:8"]]
- 0081c364 bytes 00013fd6
+ 0081c3bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e59a2aa987fef106d63eb37d019baff0"></a>

### [`0081c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c40c.md) → [`0081c464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c464.md) FUN_0081c464

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c40c.md#insn-0081c444) · [`0081c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c40c.md#insn-0081c48c) · [`0081c4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c40c.md#insn-0081c4a0)
- 新版 `0081c49c`（命令位置の公開資料なし） · `0081c4e4`（命令位置の公開資料なし） · `0081c4f8`（命令位置の公開資料なし）

~~~diff
- 0081c444 ["INT_ADD", "register:40f0:8", ["const:81c444:8", "const:4:8"]]
- 0081c444 ["CALL", null, ["callee:00c57f80:8"]]
+ 0081c49c ["INT_ADD", "register:40f0:8", ["const:81c49c:8", "const:4:8"]]
+ 0081c49c ["CALL", null, ["callee:00c57f80:8"]]
- 0081c444 bytes 9bee1094
+ 0081c49c bytes b9ee1094
- 0081c48c ["INT_ADD", "register:40f0:8", ["const:81c48c:8", "const:4:8"]]
- 0081c48c ["CALL", null, ["callee:00c53da0:8"]]
+ 0081c4e4 ["INT_ADD", "register:40f0:8", ["const:81c4e4:8", "const:4:8"]]
+ 0081c4e4 ["CALL", null, ["callee:00c53da0:8"]]
- 0081c48c bytes 1dde1094
+ 0081c4e4 bytes 2fde1094
- 0081c4a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c4a0 ["INT_ADD", "register:40f0:8", ["const:81c4a0:8", "const:4:8"]]
- 0081c4a0 ["CALLIND", null, ["register:0:8"]]
+ 0081c4f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c4f8 ["INT_ADD", "register:40f0:8", ["const:81c4f8:8", "const:4:8"]]
+ 0081c4f8 ["CALLIND", null, ["register:0:8"]]
- 0081c4a0 bytes 00013fd6
+ 0081c4f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2532993fa30599eab7309f744ebb515a"></a>

### [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) → [`0081c5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c5a8.md) FUN_0081c5a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 10件 [`00819cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md) [`0082fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 10件 [`00819d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819d34.md) [`0082fdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fdc4.md) [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md#insn-0081c5a4) · [`0081c5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md#insn-0081c5ec) · [`0081c620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md#insn-0081c620)
- 新版 `0081c5fc`（命令位置の公開資料なし） · `0081c644`（命令位置の公開資料なし） · `0081c678`（命令位置の公開資料なし）

~~~diff
- 0081c5a4 ["INT_ADD", "register:40f0:8", ["const:81c5a4:8", "const:4:8"]]
- 0081c5a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0081c5fc ["INT_ADD", "register:40f0:8", ["const:81c5fc:8", "const:4:8"]]
+ 0081c5fc ["CALL", null, ["callee:00c57f60:8"]]
- 0081c5a4 bytes 3bee1094
+ 0081c5fc bytes 59ee1094
- 0081c5ec ["INT_ADD", "register:40f0:8", ["const:81c5ec:8", "const:4:8"]]
- 0081c5ec ["CALL", null, ["callee:00c53d70:8"]]
+ 0081c644 ["INT_ADD", "register:40f0:8", ["const:81c644:8", "const:4:8"]]
+ 0081c644 ["CALL", null, ["callee:00c53d70:8"]]
- 0081c5ec bytes b9dd1094
+ 0081c644 bytes cbdd1094
- 0081c620 ["INT_ADD", "register:40f0:8", ["const:81c620:8", "const:4:8"]]
- 0081c620 ["CALL", null, ["callee:0082fdc4:8"]]
+ 0081c678 ["INT_ADD", "register:40f0:8", ["const:81c678:8", "const:4:8"]]
+ 0081c678 ["CALL", null, ["callee:0082fdc4:8"]]
- 0081c620 bytes d34d0094
+ 0081c678 bytes d34d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c70a4f944740ca7c0ba53084cf907d"></a>

### [`0081c708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c708.md) → [`0081c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c760.md) FUN_0081c760

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00821634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00821/00821634.md) · 呼出先 5件 [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0082168c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00821/0082168c.md) · 呼出先 5件 [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c708.md#insn-0081c7a8) · [`0081c7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c708.md#insn-0081c7c0) · [`0081c7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c708.md#insn-0081c7d0)
- 新版 `0081c800`（命令位置の公開資料なし） · `0081c818`（命令位置の公開資料なし） · `0081c828`（命令位置の公開資料なし）

~~~diff
- 0081c7a8 ["INT_ADD", "register:40f0:8", ["const:81c7a8:8", "const:4:8"]]
- 0081c7a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0081c800 ["INT_ADD", "register:40f0:8", ["const:81c800:8", "const:4:8"]]
+ 0081c800 ["CALL", null, ["callee:00c57f60:8"]]
- 0081c7a8 bytes baed1094
+ 0081c800 bytes d8ed1094
- 0081c7c0 ["INT_ADD", "register:40f0:8", ["const:81c7c0:8", "const:4:8"]]
- 0081c7c0 ["CALL", null, ["callee:00c580d0:8"]]
+ 0081c818 ["INT_ADD", "register:40f0:8", ["const:81c818:8", "const:4:8"]]
+ 0081c818 ["CALL", null, ["callee:00c580d0:8"]]
- 0081c7c0 bytes 10ee1094
+ 0081c818 bytes 2eee1094
- 0081c7d0 ["INT_ADD", "register:40f0:8", ["const:81c7d0:8", "const:4:8"]]
- 0081c7d0 ["CALL", null, ["callee:008302cc:8"]]
+ 0081c828 ["INT_ADD", "register:40f0:8", ["const:81c828:8", "const:4:8"]]
+ 0081c828 ["CALL", null, ["callee:008302cc:8"]]
- 0081c7d0 bytes a94e0094
+ 0081c828 bytes a94e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68af4606d0059eab3b1f155e8a81b4f3"></a>

### [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) → [`0081c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c84c.md) FUN_0081c84c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00822df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md) [`00822f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00822e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822e48.md) [`00822f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822f88.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md#insn-0081c8a8) · [`0081c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md#insn-0081c8dc)
- 新版 `0081c900`（命令位置の公開資料なし） · `0081c934`（命令位置の公開資料なし）

~~~diff
- 0081c8a8 ["INT_ADD", "register:40f0:8", ["const:81c8a8:8", "const:4:8"]]
- 0081c8a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0081c900 ["INT_ADD", "register:40f0:8", ["const:81c900:8", "const:4:8"]]
+ 0081c900 ["CALL", null, ["callee:00c57f60:8"]]
- 0081c8a8 bytes 7aed1094
+ 0081c900 bytes 98ed1094
- 0081c8dc ["INT_ADD", "register:40f0:8", ["const:81c8dc:8", "const:4:8"]]
- 0081c8dc ["CALL", null, ["callee:0043bbe4:8"]]
+ 0081c934 ["INT_ADD", "register:40f0:8", ["const:81c934:8", "const:4:8"]]
+ 0081c934 ["CALL", null, ["callee:0043bbe4:8"]]
- 0081c8dc bytes b27cf097
+ 0081c934 bytes ac7cf097
~~~


<a id="compare-09ae7e8bc9f3ed742941340a7ebdaeba"></a>

### [`0081d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1cc.md) → [`0081d224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d224.md) FUN_0081d224

採用 · 移動量 `+0x58` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0072b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b144.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md)
- 新版 呼出元 3件 [`0072b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072b/0072b19c.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b3e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1cc.md#insn-0081d1d4)
- 新版 `0081d22c`（命令位置の公開資料なし）

~~~diff
- 0081d1d4 ["INT_ADD", "register:40f0:8", ["const:81d1d4:8", "const:4:8"]]
- 0081d1d4 ["CALL", null, ["callee:00851550:8"]]
+ 0081d22c ["INT_ADD", "register:40f0:8", ["const:81d22c:8", "const:4:8"]]
+ 0081d22c ["CALL", null, ["callee:00851550:8"]]
- 0081d1d4 bytes c9d00094
+ 0081d22c bytes c9d00094
~~~


<a id="compare-d7bb4220b39788029f3a7add4fbca7ee"></a>

### [`0081d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md) → [`0081d244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d244.md) FUN_0081d244

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00816b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00816/00816b30.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`007addb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00aa3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa3e94.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081d254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md#insn-0081d254) · [`0081d288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md#insn-0081d288) · [`0081d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md#insn-0081d318)
- 新版 `0081d2ac`（命令位置の公開資料なし） · `0081d2e0`（命令位置の公開資料なし） · `0081d370`（命令位置の公開資料なし）

~~~diff
- 0081d254 ["INT_ADD", "register:40f0:8", ["const:81d254:8", "const:4:8"]]
- 0081d254 ["CALL", null, ["callee:00c57f60:8"]]
+ 0081d2ac ["INT_ADD", "register:40f0:8", ["const:81d2ac:8", "const:4:8"]]
+ 0081d2ac ["CALL", null, ["callee:00c57f60:8"]]
- 0081d254 bytes 0feb1094
+ 0081d2ac bytes 2deb1094
- 0081d288 ["INT_ADD", "register:40f0:8", ["const:81d288:8", "const:4:8"]]
- 0081d288 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0081d2e0 ["INT_ADD", "register:40f0:8", ["const:81d2e0:8", "const:4:8"]]
+ 0081d2e0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0081d288 bytes 477af097
+ 0081d2e0 bytes 417af097
- 0081d318 ["INT_ADD", "register:40f0:8", ["const:81d318:8", "const:4:8"]]
- 0081d318 ["CALL", null, ["callee:00851550:8"]]
+ 0081d370 ["INT_ADD", "register:40f0:8", ["const:81d370:8", "const:4:8"]]
+ 0081d370 ["CALL", null, ["callee:00851550:8"]]
- 0081d318 bytes 78d00094
+ 0081d370 bytes 78d00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-347fdcd8045c8ea5c06f85fdfa183fb4"></a>

### [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) → [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) FUN_00820774

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00820298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/00820298.md) [`00822c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822c98.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) · 呼出先 10件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00819d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00830170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 4件 [`008202f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/008202f0.md) [`00822cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822cf0.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) · 呼出先 10件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00819dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00819/00819dcc.md) [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) [`008301c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00820774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md#insn-00820774) · [`0082078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md#insn-0082078c) · [`008207b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md#insn-008207b8)
- 新版 `008207cc`（命令位置の公開資料なし） · `008207e4`（命令位置の公開資料なし） · `00820810`（命令位置の公開資料なし）

~~~diff
- 00820774 ["INT_ADD", "register:40f0:8", ["const:820774:8", "const:4:8"]]
- 00820774 ["CALL", null, ["callee:00c57f60:8"]]
+ 008207cc ["INT_ADD", "register:40f0:8", ["const:8207cc:8", "const:4:8"]]
+ 008207cc ["CALL", null, ["callee:00c57f60:8"]]
- 00820774 bytes c7dd1094
+ 008207cc bytes e5dd1094
- 0082078c ["INT_ADD", "register:40f0:8", ["const:82078c:8", "const:4:8"]]
- 0082078c ["CALL", null, ["callee:00c580d0:8"]]
+ 008207e4 ["INT_ADD", "register:40f0:8", ["const:8207e4:8", "const:4:8"]]
+ 008207e4 ["CALL", null, ["callee:00c580d0:8"]]
- 0082078c bytes 1dde1094
+ 008207e4 bytes 3bde1094
- 008207b8 ["INT_ADD", "register:40f0:8", ["const:8207b8:8", "const:4:8"]]
- 008207b8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00820810 ["INT_ADD", "register:40f0:8", ["const:820810:8", "const:4:8"]]
+ 00820810 ["CALL", null, ["callee:00c53d70:8"]]
- 008207b8 bytes 46cd1094
+ 00820810 bytes 58cd1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7d8fafae20ef19048e7de9bfe24c255"></a>

### [`00822df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md) → [`00822e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822e48.md) FUN_00822e48

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) · 呼出先 3件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`0081c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c84c.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00822e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md#insn-00822e60) · [`00822e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md#insn-00822e94) · [`00822f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md#insn-00822f2c)
- 新版 `00822eb8`（命令位置の公開資料なし） · `00822eec`（命令位置の公開資料なし） · `00822f84`（命令位置の公開資料なし）

~~~diff
- 00822e60 ["INT_ADD", "register:40f0:8", ["const:822e60:8", "const:4:8"]]
- 00822e60 ["CALL", null, ["callee:00c58520:8"]]
+ 00822eb8 ["INT_ADD", "register:40f0:8", ["const:822eb8:8", "const:4:8"]]
+ 00822eb8 ["CALL", null, ["callee:00c58520:8"]]
- 00822e60 bytes 7cd51094
+ 00822eb8 bytes 9ad51094
- 00822e94 ["INT_ADD", "register:40f0:8", ["const:822e94:8", "const:4:8"]]
- 00822e94 ["CALL", null, ["callee:00c58520:8"]]
+ 00822eec ["INT_ADD", "register:40f0:8", ["const:822eec:8", "const:4:8"]]
+ 00822eec ["CALL", null, ["callee:00c58520:8"]]
- 00822e94 bytes 6fd51094
+ 00822eec bytes 8dd51094
- 00822f2c ["INT_ADD", "register:40f0:8", ["const:822f2c:8", "const:4:8"]]
- 00822f2c ["CALL", null, ["callee:0049f430:8"]]
+ 00822f84 ["INT_ADD", "register:40f0:8", ["const:822f84:8", "const:4:8"]]
+ 00822f84 ["CALL", null, ["callee:0049f430:8"]]
- 00822f2c bytes 31f1f197
+ 00822f84 bytes 2bf1f197
~~~


<a id="compare-344f67787d790fee66fb2496b701f321"></a>

### [`00822f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md) → [`00822f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822f88.md) FUN_00822f88

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) · 呼出先 3件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`0081c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c84c.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00822fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md#insn-00822fc0) · [`0082300c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md#insn-0082300c)
- 新版 `00823018`（命令位置の公開資料なし） · `00823064`（命令位置の公開資料なし）

~~~diff
- 00822fc0 ["INT_ADD", "register:40f0:8", ["const:822fc0:8", "const:4:8"]]
- 00822fc0 ["CALL", null, ["callee:00c58520:8"]]
+ 00823018 ["INT_ADD", "register:40f0:8", ["const:823018:8", "const:4:8"]]
+ 00823018 ["CALL", null, ["callee:00c58520:8"]]
- 00822fc0 bytes 24d51094
+ 00823018 bytes 42d51094
- 0082300c ["INT_ADD", "register:40f0:8", ["const:82300c:8", "const:4:8"]]
- 0082300c ["CALL", null, ["callee:0049f430:8"]]
+ 00823064 ["INT_ADD", "register:40f0:8", ["const:823064:8", "const:4:8"]]
+ 00823064 ["CALL", null, ["callee:0049f430:8"]]
- 0082300c bytes f9f0f197
+ 00823064 bytes f3f0f197
~~~


<a id="compare-81fc7887deec165bab1b379c090bc314"></a>

### [`00824330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md) → [`00824388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824388.md) FUN_00824388

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) · 呼出先 2件 [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) · 呼出先 2件 [`008023e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/008023e4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00824340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md#insn-00824340) · [`00824354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md#insn-00824354) · [`00824360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md#insn-00824360)
- 新版 `00824398`（命令位置の公開資料なし） · `008243ac`（命令位置の公開資料なし） · `008243b8`（命令位置の公開資料なし）

~~~diff
- 00824340 ["INT_ADD", "register:40f0:8", ["const:824340:8", "const:4:8"]]
- 00824340 ["CALL", null, ["callee:00851550:8"]]
+ 00824398 ["INT_ADD", "register:40f0:8", ["const:824398:8", "const:4:8"]]
+ 00824398 ["CALL", null, ["callee:00851550:8"]]
- 00824340 bytes 6eb40094
+ 00824398 bytes 6eb40094
- 00824354 ["INT_ADD", "register:40f0:8", ["const:824354:8", "const:4:8"]]
- 00824354 ["CALL", null, ["callee:008023e4:8"]]
+ 008243ac ["INT_ADD", "register:40f0:8", ["const:8243ac:8", "const:4:8"]]
+ 008243ac ["CALL", null, ["callee:008023e4:8"]]
- 00824354 bytes 0e78ff97
+ 008243ac bytes 0e78ff97
- 00824360 ["INT_ADD", "register:40f0:8", ["const:824360:8", "const:4:8"]]
- 00824360 ["CALL", null, ["callee:00851550:8"]]
+ 008243b8 ["INT_ADD", "register:40f0:8", ["const:8243b8:8", "const:4:8"]]
+ 008243b8 ["CALL", null, ["callee:00851550:8"]]
- 00824360 bytes 66b40094
+ 008243b8 bytes 66b40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b49a2b1588ddf3a77c2d476781a743"></a>

### [`008244dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md) → [`00824534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824534.md) FUN_00824534

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) · 呼出先 2件 [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) · 呼出先 2件 [`008023e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/008023e4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008244ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md#insn-008244ec) · [`00824504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md#insn-00824504) · [`0082450c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md#insn-0082450c)
- 新版 `00824544`（命令位置の公開資料なし） · `0082455c`（命令位置の公開資料なし） · `00824564`（命令位置の公開資料なし）

~~~diff
- 008244ec ["INT_ADD", "register:40f0:8", ["const:8244ec:8", "const:4:8"]]
- 008244ec ["CALL", null, ["callee:00851550:8"]]
+ 00824544 ["INT_ADD", "register:40f0:8", ["const:824544:8", "const:4:8"]]
+ 00824544 ["CALL", null, ["callee:00851550:8"]]
- 008244ec bytes 03b40094
+ 00824544 bytes 03b40094
- 00824504 ["INT_ADD", "register:40f0:8", ["const:824504:8", "const:4:8"]]
- 00824504 ["CALL", null, ["callee:008023e4:8"]]
+ 0082455c ["INT_ADD", "register:40f0:8", ["const:82455c:8", "const:4:8"]]
+ 0082455c ["CALL", null, ["callee:008023e4:8"]]
- 00824504 bytes a277ff97
+ 0082455c bytes a277ff97
- 0082450c ["INT_ADD", "register:40f0:8", ["const:82450c:8", "const:4:8"]]
- 0082450c ["CALL", null, ["callee:00851550:8"]]
+ 00824564 ["INT_ADD", "register:40f0:8", ["const:824564:8", "const:4:8"]]
+ 00824564 ["CALL", null, ["callee:00851550:8"]]
- 0082450c bytes fbb30094
+ 00824564 bytes fbb30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593b14420b1d8ae5f8673d4291302407"></a>

### [`0082b4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b4f8.md) → [`0082b550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082b550.md) FUN_0082b550

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00831af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831af8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00831b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831b50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082b548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b4f8.md#insn-0082b548) · [`0082b578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b4f8.md#insn-0082b578) · [`0082b58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b4f8.md#insn-0082b58c)
- 新版 `0082b5a0`（命令位置の公開資料なし） · `0082b5d0`（命令位置の公開資料なし） · `0082b5e4`（命令位置の公開資料なし）

~~~diff
- 0082b548 ["INT_ADD", "register:40f0:8", ["const:82b548:8", "const:4:8"]]
- 0082b548 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0082b5a0 ["INT_ADD", "register:40f0:8", ["const:82b5a0:8", "const:4:8"]]
+ 0082b5a0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0082b548 bytes 9741f097
+ 0082b5a0 bytes 9141f097
- 0082b578 ["INT_ADD", "register:40f0:8", ["const:82b578:8", "const:4:8"]]
- 0082b578 ["CALL", null, ["callee:00831b50:8"]]
+ 0082b5d0 ["INT_ADD", "register:40f0:8", ["const:82b5d0:8", "const:4:8"]]
+ 0082b5d0 ["CALL", null, ["callee:00831b50:8"]]
- 0082b578 bytes 60190094
+ 0082b5d0 bytes 60190094
- 0082b58c ["INT_ADD", "register:40f0:8", ["const:82b58c:8", "const:4:8"]]
- 0082b58c ["CALL", null, ["callee:00c57f60:8"]]
+ 0082b5e4 ["INT_ADD", "register:40f0:8", ["const:82b5e4:8", "const:4:8"]]
+ 0082b5e4 ["CALL", null, ["callee:00c57f60:8"]]
- 0082b58c bytes 41b21094
+ 0082b5e4 bytes 5fb21094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0615e0e3172c8eb1975770e5cc45537"></a>

### [`0082ccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082ccfc.md) → [`0082cd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd54.md) FUN_0082cd54

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009dcfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md)
- 新版 呼出元 1件 [`009dd02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ac86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082cd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082ccfc.md#insn-0082cd04)
- 新版 `0082cd5c`（命令位置の公開資料なし）

~~~diff
- 0082cd04 ["INT_ADD", "register:40f0:8", ["const:82cd04:8", "const:4:8"]]
- 0082cd04 ["CALL", null, ["callee:00851550:8"]]
+ 0082cd5c ["INT_ADD", "register:40f0:8", ["const:82cd5c:8", "const:4:8"]]
+ 0082cd5c ["CALL", null, ["callee:00851550:8"]]
- 0082cd04 bytes fd910094
+ 0082cd5c bytes fd910094
~~~


<a id="compare-537b1d696426e44d2abb3eaadc50e191"></a>

### [`0082d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) → [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) FUN_0082d2e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`00831ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md) [`00838ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 5件 [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) [`0082f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082f180.md) [`0083204c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md) [`00838bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md#insn-0082d298) · [`0082d2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md#insn-0082d2a8) · [`0082d2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md#insn-0082d2b0)
- 新版 `0082d2f0`（命令位置の公開資料なし） · `0082d300`（命令位置の公開資料なし） · `0082d308`（命令位置の公開資料なし）

~~~diff
- 0082d298 ["INT_ADD", "register:40f0:8", ["const:82d298:8", "const:4:8"]]
- 0082d298 ["CALL", null, ["callee:00851550:8"]]
+ 0082d2f0 ["INT_ADD", "register:40f0:8", ["const:82d2f0:8", "const:4:8"]]
+ 0082d2f0 ["CALL", null, ["callee:00851550:8"]]
- 0082d298 bytes 98900094
+ 0082d2f0 bytes 98900094
- 0082d2a8 ["INT_ADD", "register:40f0:8", ["const:82d2a8:8", "const:4:8"]]
- 0082d2a8 ["CALL", null, ["callee:008b7a20:8"]]
+ 0082d300 ["INT_ADD", "register:40f0:8", ["const:82d300:8", "const:4:8"]]
+ 0082d300 ["CALL", null, ["callee:008b7a20:8"]]
- 0082d2a8 bytes c8290294
+ 0082d300 bytes c8290294
- 0082d2b0 ["INT_ADD", "register:40f0:8", ["const:82d2b0:8", "const:4:8"]]
- 0082d2b0 ["CALL", null, ["callee:00851550:8"]]
+ 0082d308 ["INT_ADD", "register:40f0:8", ["const:82d308:8", "const:4:8"]]
+ 0082d308 ["CALL", null, ["callee:00851550:8"]]
- 0082d2b0 bytes 92900094
+ 0082d308 bytes 92900094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a872511e93db8c7567154ab0a9ac2ffd"></a>

### [`0082d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md) → [`0082d538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d538.md) FUN_0082d538

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`00838a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a74.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f50.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 2件 [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) [`00838acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838acc.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b6fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa8.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md#insn-0082d4ec) · [`0082d4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md#insn-0082d4fc) · [`0082d504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md#insn-0082d504)
- 新版 `0082d544`（命令位置の公開資料なし） · `0082d554`（命令位置の公開資料なし） · `0082d55c`（命令位置の公開資料なし）

~~~diff
- 0082d4ec ["INT_ADD", "register:40f0:8", ["const:82d4ec:8", "const:4:8"]]
- 0082d4ec ["CALL", null, ["callee:00851550:8"]]
+ 0082d544 ["INT_ADD", "register:40f0:8", ["const:82d544:8", "const:4:8"]]
+ 0082d544 ["CALL", null, ["callee:00851550:8"]]
- 0082d4ec bytes 03900094
+ 0082d544 bytes 03900094
- 0082d4fc ["INT_ADD", "register:40f0:8", ["const:82d4fc:8", "const:4:8"]]
- 0082d4fc ["CALL", null, ["callee:008b7a20:8"]]
+ 0082d554 ["INT_ADD", "register:40f0:8", ["const:82d554:8", "const:4:8"]]
+ 0082d554 ["CALL", null, ["callee:008b7a20:8"]]
- 0082d4fc bytes 33290294
+ 0082d554 bytes 33290294
- 0082d504 ["INT_ADD", "register:40f0:8", ["const:82d504:8", "const:4:8"]]
- 0082d504 ["CALL", null, ["callee:00851550:8"]]
+ 0082d55c ["INT_ADD", "register:40f0:8", ["const:82d55c:8", "const:4:8"]]
+ 0082d55c ["CALL", null, ["callee:00851550:8"]]
- 0082d504 bytes fd8f0094
+ 0082d55c bytes fd8f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-837e6e3bc5ff75943c678e3dc6d51f7f"></a>

### [`0082d758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d758.md) → [`0082d7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d7b0.md) FUN_0082d7b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d758.md#insn-0082d774) · [`0082d794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d758.md#insn-0082d794)
- 新版 `0082d7cc`（命令位置の公開資料なし） · `0082d7ec`（命令位置の公開資料なし）

~~~diff
- 0082d774 ["INT_ADD", "register:40f0:8", ["const:82d774:8", "const:4:8"]]
- 0082d774 ["CALL", null, ["callee:00c53da0:8"]]
+ 0082d7cc ["INT_ADD", "register:40f0:8", ["const:82d7cc:8", "const:4:8"]]
+ 0082d7cc ["CALL", null, ["callee:00c53da0:8"]]
- 0082d774 bytes 63991094
+ 0082d7cc bytes 75991094
- 0082d794 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082d794 ["INT_ADD", "register:40f0:8", ["const:82d794:8", "const:4:8"]]
- 0082d794 ["CALLIND", null, ["register:0:8"]]
+ 0082d7ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082d7ec ["INT_ADD", "register:40f0:8", ["const:82d7ec:8", "const:4:8"]]
+ 0082d7ec ["CALLIND", null, ["register:0:8"]]
- 0082d794 bytes 00013fd6
+ 0082d7ec bytes 00013fd6
~~~


<a id="compare-c78df93959ebd5f15d1606c6e64d22be"></a>

### [`0082dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dd20.md) → [`0082dd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082dd78.md) FUN_0082dd78

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 1件 [`0082fbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fbc4.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082dd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dd20.md#insn-0082dd28) · [`0082dd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dd20.md#insn-0082dd38) · [`0082dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dd20.md#insn-0082dd40)
- 新版 `0082dd80`（命令位置の公開資料なし） · `0082dd90`（命令位置の公開資料なし） · `0082dd98`（命令位置の公開資料なし）

~~~diff
- 0082dd28 ["INT_ADD", "register:40f0:8", ["const:82dd28:8", "const:4:8"]]
- 0082dd28 ["CALL", null, ["callee:00851550:8"]]
+ 0082dd80 ["INT_ADD", "register:40f0:8", ["const:82dd80:8", "const:4:8"]]
+ 0082dd80 ["CALL", null, ["callee:00851550:8"]]
- 0082dd28 bytes f48d0094
+ 0082dd80 bytes f48d0094
- 0082dd38 ["INT_ADD", "register:40f0:8", ["const:82dd38:8", "const:4:8"]]
- 0082dd38 ["CALL", null, ["callee:008b7a20:8"]]
+ 0082dd90 ["INT_ADD", "register:40f0:8", ["const:82dd90:8", "const:4:8"]]
+ 0082dd90 ["CALL", null, ["callee:008b7a20:8"]]
- 0082dd38 bytes 24270294
+ 0082dd90 bytes 24270294
- 0082dd40 ["INT_ADD", "register:40f0:8", ["const:82dd40:8", "const:4:8"]]
- 0082dd40 ["CALL", null, ["callee:00851550:8"]]
+ 0082dd98 ["INT_ADD", "register:40f0:8", ["const:82dd98:8", "const:4:8"]]
+ 0082dd98 ["CALL", null, ["callee:00851550:8"]]
- 0082dd40 bytes ee8d0094
+ 0082dd98 bytes ee8d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0c41f96302602180c3627958865971"></a>

### [`0082dda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md) → [`0082ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082ddfc.md) FUN_0082ddfc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`00838b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b10.md) · 呼出先 3件 [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) [`0082a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md) [`0082aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082aa78.md)
- 新版 呼出元 2件 [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`00838b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b68.md) · 呼出先 3件 [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) [`0082a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082a7f8.md) [`0082aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082aad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md#insn-0082de10) · [`0082de7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md#insn-0082de7c) · [`0082dedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md#insn-0082dedc)
- 新版 `0082de68`（命令位置の公開資料なし） · `0082ded4`（命令位置の公開資料なし） · `0082df34`（命令位置の公開資料なし）

~~~diff
- 0082de10 ["INT_ADD", "register:40f0:8", ["const:82de10:8", "const:4:8"]]
- 0082de10 ["CALL", null, ["callee:0082aad0:8"]]
+ 0082de68 ["INT_ADD", "register:40f0:8", ["const:82de68:8", "const:4:8"]]
+ 0082de68 ["CALL", null, ["callee:0082aad0:8"]]
- 0082de10 bytes 1af3ff97
+ 0082de68 bytes 1af3ff97
- 0082de7c ["INT_ADD", "register:40f0:8", ["const:82de7c:8", "const:4:8"]]
- 0082de7c ["CALL", null, ["callee:008295cc:8"]]
+ 0082ded4 ["INT_ADD", "register:40f0:8", ["const:82ded4:8", "const:4:8"]]
+ 0082ded4 ["CALL", null, ["callee:008295cc:8"]]
- 0082de7c bytes beedff97
+ 0082ded4 bytes beedff97
- 0082dedc ["INT_ADD", "register:40f0:8", ["const:82dedc:8", "const:4:8"]]
- 0082dedc ["CALL", null, ["callee:0082a7f8:8"]]
+ 0082df34 ["INT_ADD", "register:40f0:8", ["const:82df34:8", "const:4:8"]]
+ 0082df34 ["CALL", null, ["callee:0082a7f8:8"]]
- 0082dedc bytes 31f2ff97
+ 0082df34 bytes 31f2ff97
~~~


<a id="compare-ebcdaafa0b2fab670aac5013c85a6455"></a>

### [`0082df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df00.md) → [`0082df58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082df58.md) FUN_0082df58

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)
- 新版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082df14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df00.md#insn-0082df14) · [`0082df1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df00.md#insn-0082df1c)
- 新版 `0082df6c`（命令位置の公開資料なし） · `0082df74`（命令位置の公開資料なし）

~~~diff
- 0082df14 ["INT_ADD", "register:40f0:8", ["const:82df14:8", "const:4:8"]]
- 0082df14 ["CALL", null, ["callee:0046ef38:8"]]
+ 0082df6c ["INT_ADD", "register:40f0:8", ["const:82df6c:8", "const:4:8"]]
+ 0082df6c ["CALL", null, ["callee:0046ef38:8"]]
- 0082df14 bytes f903f197
+ 0082df6c bytes f303f197
- 0082df1c ["INT_ADD", "register:40f0:8", ["const:82df1c:8", "const:4:8"]]
- 0082df1c ["CALL", null, ["callee:0046e804:8"]]
+ 0082df74 ["INT_ADD", "register:40f0:8", ["const:82df74:8", "const:4:8"]]
+ 0082df74 ["CALL", null, ["callee:0046e804:8"]]
- 0082df1c bytes 2a02f197
+ 0082df74 bytes 2402f197
~~~


<a id="compare-1c6e49adcbd95a6c93dc847dccd49d8b"></a>

### [`0082eaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eaf8.md) → [`0082eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eb50.md) FUN_0082eb50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 21件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0062710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/0062710c.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006adf30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006adf30.md) [`006ee740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md) · 呼出先 2件 [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 21件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`0062714c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00627/0062714c.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006adf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf88.md) [`006ee798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006ee798.md) · 呼出先 2件 [`008238b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/008238b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082eb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eaf8.md#insn-0082eb0c)
- 新版 `0082eb64`（命令位置の公開資料なし）

~~~diff
- 0082eb0c ["INT_ADD", "register:40f0:8", ["const:82eb0c:8", "const:4:8"]]
- 0082eb0c ["CALL", null, ["callee:00851550:8"]]
+ 0082eb64 ["INT_ADD", "register:40f0:8", ["const:82eb64:8", "const:4:8"]]
+ 0082eb64 ["CALL", null, ["callee:00851550:8"]]
- 0082eb0c bytes 7b8a0094
+ 0082eb64 bytes 7b8a0094
~~~


<a id="compare-4571dc952508f74c0b3f3a97f0601817"></a>

### [`0082eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md) → [`0082eb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eb84.md) FUN_0082eb84

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006a700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a700c.md) · 呼出先 5件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 17件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00664a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664a2c.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006a7064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md) · 呼出先 5件 [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082eb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md#insn-0082eb68) · [`0082eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md#insn-0082eb74) · [`0082eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md#insn-0082eba0)
- 新版 `0082ebc0`（命令位置の公開資料なし） · `0082ebcc`（命令位置の公開資料なし） · `0082ebf8`（命令位置の公開資料なし）

~~~diff
- 0082eb68 ["INT_ADD", "register:40f0:8", ["const:82eb68:8", "const:4:8"]]
- 0082eb68 ["CALL", null, ["callee:00851550:8"]]
+ 0082ebc0 ["INT_ADD", "register:40f0:8", ["const:82ebc0:8", "const:4:8"]]
+ 0082ebc0 ["CALL", null, ["callee:00851550:8"]]
- 0082eb68 bytes 648a0094
+ 0082ebc0 bytes 648a0094
- 0082eb74 ["INT_ADD", "register:40f0:8", ["const:82eb74:8", "const:4:8"]]
- 0082eb74 ["CALL", null, ["callee:00c57f60:8"]]
+ 0082ebcc ["INT_ADD", "register:40f0:8", ["const:82ebcc:8", "const:4:8"]]
+ 0082ebcc ["CALL", null, ["callee:00c57f60:8"]]
- 0082eb74 bytes c7a41094
+ 0082ebcc bytes e5a41094
- 0082eba0 ["INT_ADD", "register:40f0:8", ["const:82eba0:8", "const:4:8"]]
- 0082eba0 ["CALL", null, ["callee:00823068:8"]]
+ 0082ebf8 ["INT_ADD", "register:40f0:8", ["const:82ebf8:8", "const:4:8"]]
+ 0082ebf8 ["CALL", null, ["callee:00823068:8"]]
- 0082eba0 bytes 1cd1ff97
+ 0082ebf8 bytes 1cd1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5eff90c28ddb980fede7f6f5b487540"></a>

### [`0082ec14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md) → [`0082ec6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ec6c.md) FUN_0082ec6c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 7件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 7件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md#insn-0082ec48) · [`0082ec6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md#insn-0082ec6c) · [`0082ec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md#insn-0082ec84)
- 新版 `0082eca0`（命令位置の公開資料なし） · `0082ecc4`（命令位置の公開資料なし） · `0082ecdc`（命令位置の公開資料なし）

~~~diff
- 0082ec48 ["INT_ADD", "register:40f0:8", ["const:82ec48:8", "const:4:8"]]
- 0082ec48 ["CALL", null, ["callee:00851550:8"]]
+ 0082eca0 ["INT_ADD", "register:40f0:8", ["const:82eca0:8", "const:4:8"]]
+ 0082eca0 ["CALL", null, ["callee:00851550:8"]]
- 0082ec48 bytes 2c8a0094
+ 0082eca0 bytes 2c8a0094
- 0082ec6c ["INT_ADD", "register:40f0:8", ["const:82ec6c:8", "const:4:8"]]
- 0082ec6c ["CALL", null, ["callee:00c57f60:8"]]
+ 0082ecc4 ["INT_ADD", "register:40f0:8", ["const:82ecc4:8", "const:4:8"]]
+ 0082ecc4 ["CALL", null, ["callee:00c57f60:8"]]
- 0082ec6c bytes 89a41094
+ 0082ecc4 bytes a7a41094
- 0082ec84 ["INT_ADD", "register:40f0:8", ["const:82ec84:8", "const:4:8"]]
- 0082ec84 ["CALL", null, ["callee:00c580d0:8"]]
+ 0082ecdc ["INT_ADD", "register:40f0:8", ["const:82ecdc:8", "const:4:8"]]
+ 0082ecdc ["CALL", null, ["callee:00c580d0:8"]]
- 0082ec84 bytes dfa41094
+ 0082ecdc bytes fda41094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eec121fa6f23fe37f3dbe0df818535b"></a>

### [`0082ed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ed38.md) → [`0082ed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ed90.md) FUN_0082ed90

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) · 呼出先 5件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 5件 [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ed38.md#insn-0082ed6c) · [`0082ed78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ed38.md#insn-0082ed78) · [`0082edac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ed38.md#insn-0082edac)
- 新版 `0082edc4`（命令位置の公開資料なし） · `0082edd0`（命令位置の公開資料なし） · `0082ee04`（命令位置の公開資料なし）

~~~diff
- 0082ed6c ["INT_ADD", "register:40f0:8", ["const:82ed6c:8", "const:4:8"]]
- 0082ed6c ["CALL", null, ["callee:00851550:8"]]
+ 0082edc4 ["INT_ADD", "register:40f0:8", ["const:82edc4:8", "const:4:8"]]
+ 0082edc4 ["CALL", null, ["callee:00851550:8"]]
- 0082ed6c bytes e3890094
+ 0082edc4 bytes e3890094
- 0082ed78 ["INT_ADD", "register:40f0:8", ["const:82ed78:8", "const:4:8"]]
- 0082ed78 ["CALL", null, ["callee:00c57f60:8"]]
+ 0082edd0 ["INT_ADD", "register:40f0:8", ["const:82edd0:8", "const:4:8"]]
+ 0082edd0 ["CALL", null, ["callee:00c57f60:8"]]
- 0082ed78 bytes 46a41094
+ 0082edd0 bytes 64a41094
- 0082edac ["INT_ADD", "register:40f0:8", ["const:82edac:8", "const:4:8"]]
- 0082edac ["CALL", null, ["callee:00823068:8"]]
+ 0082ee04 ["INT_ADD", "register:40f0:8", ["const:82ee04:8", "const:4:8"]]
+ 0082ee04 ["CALL", null, ["callee:00823068:8"]]
- 0082edac bytes 99d0ff97
+ 0082ee04 bytes 99d0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79857d11fa1b7c6562e840300bb74395"></a>

### [`0082fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md) → [`0082fdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fdc4.md) FUN_0082fdc4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) · 呼出先 6件 [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0081c5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c5a8.md) · 呼出先 6件 [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082fddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md#insn-0082fddc) · [`0082fdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md#insn-0082fdf0) · [`0082fdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md#insn-0082fdf8)
- 新版 `0082fe34`（命令位置の公開資料なし） · `0082fe48`（命令位置の公開資料なし） · `0082fe50`（命令位置の公開資料なし）

~~~diff
- 0082fddc ["INT_ADD", "register:40f0:8", ["const:82fddc:8", "const:4:8"]]
- 0082fddc ["CALL", null, ["callee:00c53da0:8"]]
+ 0082fe34 ["INT_ADD", "register:40f0:8", ["const:82fe34:8", "const:4:8"]]
+ 0082fe34 ["CALL", null, ["callee:00c53da0:8"]]
- 0082fddc bytes c98f1094
+ 0082fe34 bytes db8f1094
- 0082fdf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082fdf0 ["INT_ADD", "register:40f0:8", ["const:82fdf0:8", "const:4:8"]]
- 0082fdf0 ["CALLIND", null, ["register:0:8"]]
+ 0082fe48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082fe48 ["INT_ADD", "register:40f0:8", ["const:82fe48:8", "const:4:8"]]
+ 0082fe48 ["CALLIND", null, ["register:0:8"]]
- 0082fdf0 bytes 00013fd6
+ 0082fe48 bytes 00013fd6
- 0082fdf8 ["INT_ADD", "register:40f0:8", ["const:82fdf8:8", "const:4:8"]]
- 0082fdf8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0082fe50 ["INT_ADD", "register:40f0:8", ["const:82fe50:8", "const:4:8"]]
+ 0082fe50 ["CALL", null, ["callee:00c57f50:8"]]
- 0082fdf8 bytes 22a01094
+ 0082fe50 bytes 40a01094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d10bee894b69c63e8bc8a569a5e024"></a>

### [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) → [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) FUN_008300b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) · 呼出先 7件 [`0081a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md) [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 2件 [`0082d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d800.md) [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) · 呼出先 7件 [`0081a81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a81c.md) [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008300a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md#insn-008300a4) · [`008300b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md#insn-008300b0) · [`008300fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md#insn-008300fc)
- 新版 `008300fc`（命令位置の公開資料なし） · `00830108`（命令位置の公開資料なし） · `00830154`（命令位置の公開資料なし）

~~~diff
- 008300a4 ["INT_ADD", "register:40f0:8", ["const:8300a4:8", "const:4:8"]]
- 008300a4 ["CALL", null, ["callee:00c53d70:8"]]
+ 008300fc ["INT_ADD", "register:40f0:8", ["const:8300fc:8", "const:4:8"]]
+ 008300fc ["CALL", null, ["callee:00c53d70:8"]]
- 008300a4 bytes 0b8f1094
+ 008300fc bytes 1d8f1094
- 008300b0 ["INT_ADD", "register:40f0:8", ["const:8300b0:8", "const:4:8"]]
- 008300b0 ["CALL", null, ["callee:00820774:8"]]
+ 00830108 ["INT_ADD", "register:40f0:8", ["const:830108:8", "const:4:8"]]
+ 00830108 ["CALL", null, ["callee:00820774:8"]]
- 008300b0 bytes 9bc1ff97
+ 00830108 bytes 9bc1ff97
- 008300fc ["INT_ADD", "register:40f0:8", ["const:8300fc:8", "const:4:8"]]
- 008300fc ["CALL", null, ["callee:00c57f60:8"]]
+ 00830154 ["INT_ADD", "register:40f0:8", ["const:830154:8", "const:4:8"]]
+ 00830154 ["CALL", null, ["callee:00c57f60:8"]]
- 008300fc bytes 659f1094
+ 00830154 bytes 839f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c605daac174a35fb929df0709cea7735"></a>

### [`00830170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md) → [`008301c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008301c8.md) FUN_008301c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008301e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md#insn-008301e0) · [`008301f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md#insn-008301f4) · [`008301fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md#insn-008301fc)
- 新版 `00830238`（命令位置の公開資料なし） · `0083024c`（命令位置の公開資料なし） · `00830254`（命令位置の公開資料なし）

~~~diff
- 008301e0 ["INT_ADD", "register:40f0:8", ["const:8301e0:8", "const:4:8"]]
- 008301e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00830238 ["INT_ADD", "register:40f0:8", ["const:830238:8", "const:4:8"]]
+ 00830238 ["CALL", null, ["callee:00c53da0:8"]]
- 008301e0 bytes c88e1094
+ 00830238 bytes da8e1094
- 008301f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008301f4 ["INT_ADD", "register:40f0:8", ["const:8301f4:8", "const:4:8"]]
- 008301f4 ["CALLIND", null, ["register:0:8"]]
+ 0083024c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0083024c ["INT_ADD", "register:40f0:8", ["const:83024c:8", "const:4:8"]]
+ 0083024c ["CALLIND", null, ["register:0:8"]]
- 008301f4 bytes 00013fd6
+ 0083024c bytes 00013fd6
- 008301fc ["INT_ADD", "register:40f0:8", ["const:8301fc:8", "const:4:8"]]
- 008301fc ["CALL", null, ["callee:00c57f50:8"]]
+ 00830254 ["INT_ADD", "register:40f0:8", ["const:830254:8", "const:4:8"]]
+ 00830254 ["CALL", null, ["callee:00c57f50:8"]]
- 008301fc bytes 219f1094
+ 00830254 bytes 3f9f1094
~~~


<a id="compare-8fbc33fc703dd4ca77b3a17e0423bc2b"></a>

### [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) → [`0083027c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083027c.md) FUN_0083027c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008157a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/008157a4.md) [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 2件 [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`008157fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00815/008157fc.md) [`0083027c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083027c.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 2件 [`0083027c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083027c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md#insn-00830240) · [`0083024c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md#insn-0083024c) · [`0083025c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md#insn-0083025c)
- 新版 `00830298`（命令位置の公開資料なし） · `008302a4`（命令位置の公開資料なし） · `008302b4`（命令位置の公開資料なし）

~~~diff
- 00830240 ["INT_ADD", "register:40f0:8", ["const:830240:8", "const:4:8"]]
- 00830240 ["CALL", null, ["local:b0:8"]]
+ 00830298 ["INT_ADD", "register:40f0:8", ["const:830298:8", "const:4:8"]]
+ 00830298 ["CALL", null, ["local:b0:8"]]
- 00830240 bytes f9ffff97
+ 00830298 bytes f9ffff97
- 0083024c ["INT_ADD", "register:40f0:8", ["const:83024c:8", "const:4:8"]]
- 0083024c ["CALL", null, ["local:b0:8"]]
+ 008302a4 ["INT_ADD", "register:40f0:8", ["const:8302a4:8", "const:4:8"]]
+ 008302a4 ["CALL", null, ["local:b0:8"]]
- 0083024c bytes f6ffff97
+ 008302a4 bytes f6ffff97
- 0083025c ["INT_ADD", "register:40f0:8", ["const:83025c:8", "const:4:8"]]
- 0083025c ["CALL", null, ["callee:00c57f80:8"]]
+ 008302b4 ["INT_ADD", "register:40f0:8", ["const:8302b4:8", "const:4:8"]]
+ 008302b4 ["CALL", null, ["callee:00c57f80:8"]]
- 0083025c bytes 159f1094
+ 008302b4 bytes 339f1094
~~~


<a id="compare-dcb4c534aacb65e66fd5851bd1a4ea88"></a>

### [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) → [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) FUN_008302e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 4件 [`008302e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008302a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md#insn-008302a4) · [`008302b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md#insn-008302b0) · [`008302c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md#insn-008302c4)
- 新版 `008302fc`（命令位置の公開資料なし） · `00830308`（命令位置の公開資料なし） · `0083031c`（命令位置の公開資料なし）

~~~diff
- 008302a4 ["INT_ADD", "register:40f0:8", ["const:8302a4:8", "const:4:8"]]
- 008302a4 ["CALL", null, ["local:b0:8"]]
+ 008302fc ["INT_ADD", "register:40f0:8", ["const:8302fc:8", "const:4:8"]]
+ 008302fc ["CALL", null, ["local:b0:8"]]
- 008302a4 bytes f9ffff97
+ 008302fc bytes f9ffff97
- 008302b0 ["INT_ADD", "register:40f0:8", ["const:8302b0:8", "const:4:8"]]
- 008302b0 ["CALL", null, ["local:b0:8"]]
+ 00830308 ["INT_ADD", "register:40f0:8", ["const:830308:8", "const:4:8"]]
+ 00830308 ["CALL", null, ["local:b0:8"]]
- 008302b0 bytes f6ffff97
+ 00830308 bytes f6ffff97
- 008302c4 ["INT_ADD", "register:40f0:8", ["const:8302c4:8", "const:4:8"]]
- 008302c4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0083031c ["INT_ADD", "register:40f0:8", ["const:83031c:8", "const:4:8"]]
+ 0083031c ["CALL", null, ["callee:00c53da0:8"]]
- 008302c4 bytes 8f8e1094
+ 0083031c bytes a18e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-558dcd18126dd2a3d1474664b0440266"></a>

### [`00830338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830338.md) → [`00830390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830390.md) FUN_00830390

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830338.md#insn-00830354) · [`00830364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830338.md#insn-00830364)
- 新版 `008303ac`（命令位置の公開資料なし） · `008303bc`（命令位置の公開資料なし）

~~~diff
- 00830354 ["INT_ADD", "register:40f0:8", ["const:830354:8", "const:4:8"]]
- 00830354 ["CALL", null, ["callee:00c57f80:8"]]
+ 008303ac ["INT_ADD", "register:40f0:8", ["const:8303ac:8", "const:4:8"]]
+ 008303ac ["CALL", null, ["callee:00c57f80:8"]]
- 00830354 bytes d79e1094
+ 008303ac bytes f59e1094
- 00830364 ["INT_ADD", "register:40f0:8", ["const:830364:8", "const:4:8"]]
- 00830364 ["CALL", null, ["callee:00c57f80:8"]]
+ 008303bc ["INT_ADD", "register:40f0:8", ["const:8303bc:8", "const:4:8"]]
+ 008303bc ["CALL", null, ["callee:00c57f80:8"]]
- 00830364 bytes d39e1094
+ 008303bc bytes f19e1094
~~~


<a id="compare-75406475c646c64322e10e70dd73ed6b"></a>

### [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) → [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) FUN_008303e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 4件 [`008303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008303e8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008303ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md#insn-008303ac) · [`008303b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md#insn-008303b8) · [`008303cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md#insn-008303cc)
- 新版 `00830404`（命令位置の公開資料なし） · `00830410`（命令位置の公開資料なし） · `00830424`（命令位置の公開資料なし）

~~~diff
- 008303ac ["INT_ADD", "register:40f0:8", ["const:8303ac:8", "const:4:8"]]
- 008303ac ["CALL", null, ["local:b0:8"]]
+ 00830404 ["INT_ADD", "register:40f0:8", ["const:830404:8", "const:4:8"]]
+ 00830404 ["CALL", null, ["local:b0:8"]]
- 008303ac bytes f9ffff97
+ 00830404 bytes f9ffff97
- 008303b8 ["INT_ADD", "register:40f0:8", ["const:8303b8:8", "const:4:8"]]
- 008303b8 ["CALL", null, ["local:b0:8"]]
+ 00830410 ["INT_ADD", "register:40f0:8", ["const:830410:8", "const:4:8"]]
+ 00830410 ["CALL", null, ["local:b0:8"]]
- 008303b8 bytes f6ffff97
+ 00830410 bytes f6ffff97
- 008303cc ["INT_ADD", "register:40f0:8", ["const:8303cc:8", "const:4:8"]]
- 008303cc ["CALL", null, ["callee:00c53da0:8"]]
+ 00830424 ["INT_ADD", "register:40f0:8", ["const:830424:8", "const:4:8"]]
+ 00830424 ["CALL", null, ["callee:00c53da0:8"]]
- 008303cc bytes 4d8e1094
+ 00830424 bytes 5f8e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe478b08b943061cc97a26e420b9f5a8"></a>

### [`0083044c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083044c.md) → [`008304a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008304a4.md) FUN_008304a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00830440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830440.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00830498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830498.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083044c.md#insn-00830468) · [`00830478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083044c.md#insn-00830478) · [`00830488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083044c.md#insn-00830488)
- 新版 `008304c0`（命令位置の公開資料なし） · `008304d0`（命令位置の公開資料なし） · `008304e0`（命令位置の公開資料なし）

~~~diff
- 00830468 ["INT_ADD", "register:40f0:8", ["const:830468:8", "const:4:8"]]
- 00830468 ["CALL", null, ["callee:00c57f80:8"]]
+ 008304c0 ["INT_ADD", "register:40f0:8", ["const:8304c0:8", "const:4:8"]]
+ 008304c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00830468 bytes 929e1094
+ 008304c0 bytes b09e1094
- 00830478 ["INT_ADD", "register:40f0:8", ["const:830478:8", "const:4:8"]]
- 00830478 ["CALL", null, ["callee:00c57f80:8"]]
+ 008304d0 ["INT_ADD", "register:40f0:8", ["const:8304d0:8", "const:4:8"]]
+ 008304d0 ["CALL", null, ["callee:00c57f80:8"]]
- 00830478 bytes 8e9e1094
+ 008304d0 bytes ac9e1094
- 00830488 ["INT_ADD", "register:40f0:8", ["const:830488:8", "const:4:8"]]
- 00830488 ["CALL", null, ["callee:00c57f80:8"]]
+ 008304e0 ["INT_ADD", "register:40f0:8", ["const:8304e0:8", "const:4:8"]]
+ 008304e0 ["CALL", null, ["callee:00c57f80:8"]]
- 00830488 bytes 8a9e1094
+ 008304e0 bytes a89e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0cd5b226b731e44121cb3f035ab7d4"></a>

### [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) → [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) FUN_00830568

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 2件 [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 2件 [`00830568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830568.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md#insn-00830530) · [`0083053c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md#insn-0083053c)
- 新版 `00830588`（命令位置の公開資料なし） · `00830594`（命令位置の公開資料なし）

~~~diff
- 00830530 ["INT_ADD", "register:40f0:8", ["const:830530:8", "const:4:8"]]
- 00830530 ["CALL", null, ["local:b0:8"]]
+ 00830588 ["INT_ADD", "register:40f0:8", ["const:830588:8", "const:4:8"]]
+ 00830588 ["CALL", null, ["local:b0:8"]]
- 00830530 bytes f8ffff97
+ 00830588 bytes f8ffff97
- 0083053c ["INT_ADD", "register:40f0:8", ["const:83053c:8", "const:4:8"]]
- 0083053c ["CALL", null, ["local:b0:8"]]
+ 00830594 ["INT_ADD", "register:40f0:8", ["const:830594:8", "const:4:8"]]
+ 00830594 ["CALL", null, ["local:b0:8"]]
- 0083053c bytes f5ffff97
+ 00830594 bytes f5ffff97
~~~


<a id="compare-0c158a0870f2228f72eb3d4e3ce71029"></a>

### [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) → [`008305ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008305ac.md) FUN_008305ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`008305ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008305ac.md) [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) · 呼出先 4件 [`008305ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008305ac.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md#insn-00830570) · [`0083057c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md#insn-0083057c) · [`00830590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md#insn-00830590)
- 新版 `008305c8`（命令位置の公開資料なし） · `008305d4`（命令位置の公開資料なし） · `008305e8`（命令位置の公開資料なし）

~~~diff
- 00830570 ["INT_ADD", "register:40f0:8", ["const:830570:8", "const:4:8"]]
- 00830570 ["CALL", null, ["local:b0:8"]]
+ 008305c8 ["INT_ADD", "register:40f0:8", ["const:8305c8:8", "const:4:8"]]
+ 008305c8 ["CALL", null, ["local:b0:8"]]
- 00830570 bytes f9ffff97
+ 008305c8 bytes f9ffff97
- 0083057c ["INT_ADD", "register:40f0:8", ["const:83057c:8", "const:4:8"]]
- 0083057c ["CALL", null, ["local:b0:8"]]
+ 008305d4 ["INT_ADD", "register:40f0:8", ["const:8305d4:8", "const:4:8"]]
+ 008305d4 ["CALL", null, ["local:b0:8"]]
- 0083057c bytes f6ffff97
+ 008305d4 bytes f6ffff97
- 00830590 ["INT_ADD", "register:40f0:8", ["const:830590:8", "const:4:8"]]
- 00830590 ["CALL", null, ["callee:00c53da0:8"]]
+ 008305e8 ["INT_ADD", "register:40f0:8", ["const:8305e8:8", "const:4:8"]]
+ 008305e8 ["CALL", null, ["callee:00c53da0:8"]]
- 00830590 bytes dc8d1094
+ 008305e8 bytes ee8d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0db64312e7f77662e0589f16b022644"></a>

### [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) → [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md) FUN_00830664

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0081c904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c904.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`00829394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md) · 呼出先 3件 [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 11件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`0081c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c95c.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`008238b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/008238b8.md) [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) · 呼出先 3件 [`0081c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c34c.md) [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md#insn-0083062c) · [`00830638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md#insn-00830638) · [`00830640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md#insn-00830640)
- 新版 `00830684`（命令位置の公開資料なし） · `00830690`（命令位置の公開資料なし） · `00830698`（命令位置の公開資料なし）

~~~diff
- 0083062c ["INT_ADD", "register:40f0:8", ["const:83062c:8", "const:4:8"]]
- 0083062c ["CALL", null, ["local:b0:8"]]
+ 00830684 ["INT_ADD", "register:40f0:8", ["const:830684:8", "const:4:8"]]
+ 00830684 ["CALL", null, ["local:b0:8"]]
- 0083062c bytes f8ffff97
+ 00830684 bytes f8ffff97
- 00830638 ["INT_ADD", "register:40f0:8", ["const:830638:8", "const:4:8"]]
- 00830638 ["CALL", null, ["local:b0:8"]]
+ 00830690 ["INT_ADD", "register:40f0:8", ["const:830690:8", "const:4:8"]]
+ 00830690 ["CALL", null, ["local:b0:8"]]
- 00830638 bytes f5ffff97
+ 00830690 bytes f5ffff97
- 00830640 ["INT_ADD", "register:40f0:8", ["const:830640:8", "const:4:8"]]
- 00830640 ["CALL", null, ["callee:0081c34c:8"]]
+ 00830698 ["INT_ADD", "register:40f0:8", ["const:830698:8", "const:4:8"]]
+ 00830698 ["CALL", null, ["callee:0081c34c:8"]]
- 00830640 bytes 2dafff97
+ 00830698 bytes 2dafff97
~~~


<a id="compare-e9ef03f6f9c581a270c6516496550ce9"></a>

### [`00830658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830658.md) → [`008306b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306b0.md) FUN_008306b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0081c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c34c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083067c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830658.md#insn-0083067c)
- 新版 `008306d4`（命令位置の公開資料なし）

~~~diff
- 0083067c ["INT_ADD", "register:40f0:8", ["const:83067c:8", "const:4:8"]]
- 0083067c ["CALL", null, ["callee:0081c34c:8"]]
+ 008306d4 ["INT_ADD", "register:40f0:8", ["const:8306d4:8", "const:4:8"]]
+ 008306d4 ["CALL", null, ["callee:0081c34c:8"]]
- 0083067c bytes 1eafff97
+ 008306d4 bytes 1eafff97
~~~


<a id="compare-d747dca090e8172dfaabc8e90a26e629"></a>

### [`0083069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md) → [`008306f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md) FUN_008306f4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md#insn-00830708) · [`00830734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md#insn-00830734) · [`00830794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md#insn-00830794)
- 新版 `00830760`（命令位置の公開資料なし） · `0083078c`（命令位置の公開資料なし） · `008307ec`（命令位置の公開資料なし）

~~~diff
- 00830708 ["INT_ADD", "register:40f0:8", ["const:830708:8", "const:4:8"]]
- 00830708 ["CALL", null, ["callee:00c57f60:8"]]
+ 00830760 ["INT_ADD", "register:40f0:8", ["const:830760:8", "const:4:8"]]
+ 00830760 ["CALL", null, ["callee:00c57f60:8"]]
- 00830708 bytes e29d1094
+ 00830760 bytes 009e1094
- 00830734 ["INT_ADD", "register:40f0:8", ["const:830734:8", "const:4:8"]]
- 00830734 ["CALL", null, ["callee:00c53d70:8"]]
+ 0083078c ["INT_ADD", "register:40f0:8", ["const:83078c:8", "const:4:8"]]
+ 0083078c ["CALL", null, ["callee:00c53d70:8"]]
- 00830734 bytes 678d1094
+ 0083078c bytes 798d1094
- 00830794 ["INT_ADD", "register:40f0:8", ["const:830794:8", "const:4:8"]]
- 00830794 ["CALL", null, ["callee:00c53da0:8"]]
+ 008307ec ["INT_ADD", "register:40f0:8", ["const:8307ec:8", "const:4:8"]]
+ 008307ec ["CALL", null, ["callee:00c53da0:8"]]
- 00830794 bytes 5b8d1094
+ 008307ec bytes 6d8d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce791e41ed64a006d077cb32721d0ceb"></a>

### [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) → [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) FUN_00830850

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0081c904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c904.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`00829394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md) [`0082c384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) [`00830908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830908.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 8件 [`0081c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c95c.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) [`008238b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/008238b8.md) [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) [`0082c3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c3dc.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`008300b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300b8.md) [`00830960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830960.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md#insn-00830830) · [`00830850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md#insn-00830850) · [`00830870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md#insn-00830870)
- 新版 `00830888`（命令位置の公開資料なし） · `008308a8`（命令位置の公開資料なし） · `008308c8`（命令位置の公開資料なし）

~~~diff
- 00830830 ["INT_ADD", "register:40f0:8", ["const:830830:8", "const:4:8"]]
- 00830830 ["CALL", null, ["callee:00830960:8"]]
+ 00830888 ["INT_ADD", "register:40f0:8", ["const:830888:8", "const:4:8"]]
+ 00830888 ["CALL", null, ["callee:00830960:8"]]
- 00830830 bytes 36000094
+ 00830888 bytes 36000094
- 00830850 ["INT_ADD", "register:40f0:8", ["const:830850:8", "const:4:8"]]
- 00830850 ["CALL", null, ["callee:00c57f60:8"]]
+ 008308a8 ["INT_ADD", "register:40f0:8", ["const:8308a8:8", "const:4:8"]]
+ 008308a8 ["CALL", null, ["callee:00c57f60:8"]]
- 00830850 bytes 909d1094
+ 008308a8 bytes ae9d1094
- 00830870 ["INT_ADD", "register:40f0:8", ["const:830870:8", "const:4:8"]]
- 00830870 ["CALL", null, ["callee:008300b8:8"]]
+ 008308c8 ["INT_ADD", "register:40f0:8", ["const:8308c8:8", "const:4:8"]]
+ 008308c8 ["CALL", null, ["callee:008300b8:8"]]
- 00830870 bytes fcfdff97
+ 008308c8 bytes fcfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5abe86023bc6d426fd912071ba2ccc2"></a>

### [`00830e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e4c.md) → [`00830ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ea4.md) FUN_00830ea4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e4c.md#insn-00830e88)
- 新版 `00830ee0`（命令位置の公開資料なし）

~~~diff
- 00830e88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830e88 ["INT_ADD", "register:40f0:8", ["const:830e88:8", "const:4:8"]]
- 00830e88 ["CALLIND", null, ["register:0:8"]]
+ 00830ee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00830ee0 ["INT_ADD", "register:40f0:8", ["const:830ee0:8", "const:4:8"]]
+ 00830ee0 ["CALLIND", null, ["register:0:8"]]
- 00830e88 bytes 00013fd6
+ 00830ee0 bytes 00013fd6
~~~


<a id="compare-f031e1785f264458254759a33c097a65"></a>

### [`00831118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831118.md) → [`00831170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831170.md) FUN_00831170

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00831154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831118.md#insn-00831154)
- 新版 `008311ac`（命令位置の公開資料なし）

~~~diff
- 00831154 ["COPY", "register:0:8", ["register:4040:8"]]
- 00831154 ["INT_ADD", "register:40f0:8", ["const:831154:8", "const:4:8"]]
- 00831154 ["CALLIND", null, ["register:0:8"]]
+ 008311ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008311ac ["INT_ADD", "register:40f0:8", ["const:8311ac:8", "const:4:8"]]
+ 008311ac ["CALLIND", null, ["register:0:8"]]
- 00831154 bytes 00013fd6
+ 008311ac bytes 00013fd6
~~~


<a id="compare-a5d18a526aabeefb7a9bb21f8d545346"></a>

### [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) → [`00831cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831cf8.md) FUN_00831cf8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) · 呼出先 2件 [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) [`00831cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831cf8.md) · 呼出先 2件 [`00831cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831cf8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00831cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md#insn-00831cc0) · [`00831ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md#insn-00831ccc)
- 新版 `00831d18`（命令位置の公開資料なし） · `00831d24`（命令位置の公開資料なし）

~~~diff
- 00831cc0 ["INT_ADD", "register:40f0:8", ["const:831cc0:8", "const:4:8"]]
- 00831cc0 ["CALL", null, ["local:b0:8"]]
+ 00831d18 ["INT_ADD", "register:40f0:8", ["const:831d18:8", "const:4:8"]]
+ 00831d18 ["CALL", null, ["local:b0:8"]]
- 00831cc0 bytes f8ffff97
+ 00831d18 bytes f8ffff97
- 00831ccc ["INT_ADD", "register:40f0:8", ["const:831ccc:8", "const:4:8"]]
- 00831ccc ["CALL", null, ["local:b0:8"]]
+ 00831d24 ["INT_ADD", "register:40f0:8", ["const:831d24:8", "const:4:8"]]
+ 00831d24 ["CALL", null, ["local:b0:8"]]
- 00831ccc bytes f5ffff97
+ 00831d24 bytes f5ffff97
~~~


<a id="compare-18961bc1b2261c9356bafe88ba309eca"></a>

### [`00833314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md) → [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) FUN_0083336c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) [`00833314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md) [`008336c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/008336c4.md) · 呼出先 5件 [`0081d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d508.md) [`00833314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md) [`008336c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/008336c4.md) [`00833a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833a3c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) · 呼出先 5件 [`0081d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d560.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00833368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md#insn-00833368) · [`0083337c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md#insn-0083337c) · [`00833384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00833/00833314.md#insn-00833384)
- 新版 `008333c0`（命令位置の公開資料なし） · `008333d4`（命令位置の公開資料なし） · `008333dc`（命令位置の公開資料なし）

~~~diff
- 00833368 ["INT_ADD", "register:40f0:8", ["const:833368:8", "const:4:8"]]
- 00833368 ["CALL", null, ["callee:00851550:8"]]
+ 008333c0 ["INT_ADD", "register:40f0:8", ["const:8333c0:8", "const:4:8"]]
+ 008333c0 ["CALL", null, ["callee:00851550:8"]]
- 00833368 bytes 64780094
+ 008333c0 bytes 64780094
- 0083337c ["INT_ADD", "register:40f0:8", ["const:83337c:8", "const:4:8"]]
- 0083337c ["CALL", null, ["callee:0081d560:8"]]
+ 008333d4 ["INT_ADD", "register:40f0:8", ["const:8333d4:8", "const:4:8"]]
+ 008333d4 ["CALL", null, ["callee:0081d560:8"]]
- 0083337c bytes 63a8ff97
+ 008333d4 bytes 63a8ff97
- 00833384 ["INT_ADD", "register:40f0:8", ["const:833384:8", "const:4:8"]]
- 00833384 ["CALL", null, ["callee:00851550:8"]]
+ 008333dc ["INT_ADD", "register:40f0:8", ["const:8333dc:8", "const:4:8"]]
+ 008333dc ["CALL", null, ["callee:00851550:8"]]
- 00833384 bytes 5d780094
+ 008333dc bytes 5d780094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

