# v16.0.1 → v16.0.2 · 要調査の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-cec341e820b3057240a8295f3a8d8d5c"></a>

### [`004cb350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb350.md) → [`004cb390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb390.md) _ZN5Botan13Threaded_Fork4sendEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c59130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59130.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c59200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb350.md#insn-004cb388) · [`004cb398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb350.md#insn-004cb398) · [`004cb568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb350.md#insn-004cb568)
- 新版 [`004cb3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb390.md#insn-004cb3c8) · [`004cb3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb390.md#insn-004cb3d8) · [`004cb5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb390.md#insn-004cb5a8)

~~~diff
- 004cb388 ["INT_ADD", "register:40f0:8", ["const:4cb388:8", "const:4:8"]]
- 004cb388 ["CALL", null, ["callee:00c59200:8"]]
+ 004cb3c8 ["INT_ADD", "register:40f0:8", ["const:4cb3c8:8", "const:4:8"]]
+ 004cb3c8 ["CALL", null, ["callee:00c59200:8"]]
- 004cb388 bytes 6a371e94
+ 004cb3c8 bytes 8e371e94
- 004cb398 ["INT_ADD", "register:40f0:8", ["const:4cb398:8", "const:4:8"]]
- 004cb398 ["CALL", null, ["callee:00c59200:8"]]
+ 004cb3d8 ["INT_ADD", "register:40f0:8", ["const:4cb3d8:8", "const:4:8"]]
+ 004cb3d8 ["CALL", null, ["callee:00c59200:8"]]
- 004cb398 bytes 66371e94
+ 004cb3d8 bytes 8a371e94
- 004cb568 ["INT_ADD", "register:40f0:8", ["const:4cb568:8", "const:4:8"]]
- 004cb568 ["CALL", null, ["callee:0054052c:8"]]
+ 004cb5a8 ["INT_ADD", "register:40f0:8", ["const:4cb5a8:8", "const:4:8"]]
+ 004cb5a8 ["CALL", null, ["callee:0054052c:8"]]
- 004cb568 bytes e1d30194
+ 004cb5a8 bytes e1d30194
~~~


<a id="compare-e2fffb16f00371a26604c30a00053578"></a>

### [`004cb5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb5c0.md) → [`004cb600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb600.md) _ZN5Botan13Threaded_Fork20thread_delegate_workEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59130.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`00c59200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59200.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb5c0.md#insn-004cb604) · [`004cb61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb5c0.md#insn-004cb61c) · [`004cb63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb5c0.md#insn-004cb63c)
- 新版 [`004cb644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb600.md#insn-004cb644) · [`004cb65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb600.md#insn-004cb65c) · [`004cb67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb600.md#insn-004cb67c)

~~~diff
- 004cb604 ["INT_ADD", "register:40f0:8", ["const:4cb604:8", "const:4:8"]]
- 004cb604 ["CALL", null, ["callee:00c581b0:8"]]
+ 004cb644 ["INT_ADD", "register:40f0:8", ["const:4cb644:8", "const:4:8"]]
+ 004cb644 ["CALL", null, ["callee:00c581b0:8"]]
- 004cb604 bytes b7321e94
+ 004cb644 bytes db321e94
- 004cb61c ["INT_ADD", "register:40f0:8", ["const:4cb61c:8", "const:4:8"]]
- 004cb61c ["CALL", null, ["callee:00c581c0:8"]]
+ 004cb65c ["INT_ADD", "register:40f0:8", ["const:4cb65c:8", "const:4:8"]]
+ 004cb65c ["CALL", null, ["callee:00c581c0:8"]]
- 004cb61c bytes b5321e94
+ 004cb65c bytes d9321e94
- 004cb63c ["INT_ADD", "register:40f0:8", ["const:4cb63c:8", "const:4:8"]]
- 004cb63c ["CALL", null, ["callee:00c581c0:8"]]
+ 004cb67c ["INT_ADD", "register:40f0:8", ["const:4cb67c:8", "const:4:8"]]
+ 004cb67c ["CALL", null, ["callee:00c581c0:8"]]
- 004cb63c bytes ad321e94
+ 004cb67c bytes d1321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af915102e602e85dc242ff849cc2cc9"></a>

### [`004cbe80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md) → [`004cbec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbec0.md) _ZN5Botan12HashFunction9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004cc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004cc08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc08c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cbf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md#insn-004cbf10) · [`004cbf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md#insn-004cbf20) · [`004cbf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md#insn-004cbf5c)
- 新版 [`004cbf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbec0.md#insn-004cbf50) · [`004cbf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbec0.md#insn-004cbf60) · [`004cbf9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbec0.md#insn-004cbf9c)

~~~diff
- 004cbf10 ["INT_ADD", "register:40f0:8", ["const:4cbf10:8", "const:4:8"]]
- 004cbf10 ["CALL", null, ["callee:00473580:8"]]
+ 004cbf50 ["INT_ADD", "register:40f0:8", ["const:4cbf50:8", "const:4:8"]]
+ 004cbf50 ["CALL", null, ["callee:00473580:8"]]
- 004cbf10 bytes 8c9dfe97
+ 004cbf50 bytes 8c9dfe97
- 004cbf20 ["INT_ADD", "register:40f0:8", ["const:4cbf20:8", "const:4:8"]]
- 004cbf20 ["CALL", null, ["callee:004cc08c:8"]]
+ 004cbf60 ["INT_ADD", "register:40f0:8", ["const:4cbf60:8", "const:4:8"]]
+ 004cbf60 ["CALL", null, ["callee:004cc08c:8"]]
- 004cbf20 bytes 4b000094
+ 004cbf60 bytes 4b000094
- 004cbf5c ["INT_ADD", "register:40f0:8", ["const:4cbf5c:8", "const:4:8"]]
- 004cbf5c ["CALL", null, ["callee:00c57f80:8"]]
+ 004cbf9c ["INT_ADD", "register:40f0:8", ["const:4cbf9c:8", "const:4:8"]]
+ 004cbf9c ["CALL", null, ["callee:00c57f80:8"]]
- 004cbf5c bytes d52f1e94
+ 004cbf9c bytes f92f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bbf7afb9d536e0002cb1b803274d40a"></a>

### [`004cc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md) → [`004cc08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc08c.md) FUN_004cc08c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004cbe80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)
- 新版 呼出元 1件 [`004cbec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbec0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md#insn-004cc09c) · [`004cc0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md#insn-004cc0b0) · [`004cc0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md#insn-004cc0cc)
- 新版 [`004cc0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc08c.md#insn-004cc0dc) · [`004cc0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc08c.md#insn-004cc0f0) · [`004cc10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc08c.md#insn-004cc10c)

~~~diff
- 004cc09c ["INT_ADD", "register:40f0:8", ["const:4cc09c:8", "const:4:8"]]
- 004cc09c ["CALL", null, ["callee:00540dbc:8"]]
+ 004cc0dc ["INT_ADD", "register:40f0:8", ["const:4cc0dc:8", "const:4:8"]]
+ 004cc0dc ["CALL", null, ["callee:00540dbc:8"]]
- 004cc09c bytes 38d30194
+ 004cc0dc bytes 38d30194
- 004cc0b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cc0b0 ["INT_ADD", "register:40f0:8", ["const:4cc0b0:8", "const:4:8"]]
- 004cc0b0 ["CALLIND", null, ["register:0:8"]]
+ 004cc0f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cc0f0 ["INT_ADD", "register:40f0:8", ["const:4cc0f0:8", "const:4:8"]]
+ 004cc0f0 ["CALLIND", null, ["register:0:8"]]
- 004cc0b0 bytes 00013fd6
+ 004cc0f0 bytes 00013fd6
- 004cc0cc ["INT_ADD", "register:40f0:8", ["const:4cc0cc:8", "const:4:8"]]
- 004cc0cc ["CALL", null, ["callee:00c58ec0:8"]]
+ 004cc10c ["INT_ADD", "register:40f0:8", ["const:4cc10c:8", "const:4:8"]]
+ 004cc10c ["CALL", null, ["callee:00c58ec0:8"]]
- 004cc0cc bytes 49331e94
+ 004cc10c bytes 6d331e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd4a40bc70db1cc1eae3e77b1195f2de"></a>

### [`004cc18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md) → [`004cc1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md) FUN_004cc1cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c0be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`004c0c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md#insn-004cc1bc) · [`004cc1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md#insn-004cc1d4) · [`004cc1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md#insn-004cc1f0)
- 新版 [`004cc1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md#insn-004cc1fc) · [`004cc214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md#insn-004cc214) · [`004cc230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md#insn-004cc230)

~~~diff
- 004cc1bc ["INT_ADD", "register:40f0:8", ["const:4cc1bc:8", "const:4:8"]]
- 004cc1bc ["CALL", null, ["callee:00c57f60:8"]]
+ 004cc1fc ["INT_ADD", "register:40f0:8", ["const:4cc1fc:8", "const:4:8"]]
+ 004cc1fc ["CALL", null, ["callee:00c57f60:8"]]
- 004cc1bc bytes 352f1e94
+ 004cc1fc bytes 592f1e94
- 004cc1d4 ["INT_ADD", "register:40f0:8", ["const:4cc1d4:8", "const:4:8"]]
- 004cc1d4 ["CALL", null, ["callee:00c580d0:8"]]
+ 004cc214 ["INT_ADD", "register:40f0:8", ["const:4cc214:8", "const:4:8"]]
+ 004cc214 ["CALL", null, ["callee:00c580d0:8"]]
- 004cc1d4 bytes 8b2f1e94
+ 004cc214 bytes af2f1e94
- 004cc1f0 ["INT_ADD", "register:40f0:8", ["const:4cc1f0:8", "const:4:8"]]
- 004cc1f0 ["CALL", null, ["callee:0049f46c:8"]]
+ 004cc230 ["INT_ADD", "register:40f0:8", ["const:4cc230:8", "const:4:8"]]
+ 004cc230 ["CALL", null, ["callee:0049f46c:8"]]
- 004cc1f0 bytes 8f4cff97
+ 004cc230 bytes 8f4cff97
~~~


<a id="compare-1cc452554b9fd3869c84f08ed224b512"></a>

### [`004cc75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc75c.md) → [`004cc79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc79c.md) _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc75c.md#insn-004cc798) · [`004cc7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc75c.md#insn-004cc7ac) · [`004cc7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc75c.md#insn-004cc7c4)
- 新版 [`004cc7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc79c.md#insn-004cc7d8) · [`004cc7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc79c.md#insn-004cc7ec) · [`004cc804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc79c.md#insn-004cc804)

~~~diff
- 004cc798 ["INT_ADD", "register:40f0:8", ["const:4cc798:8", "const:4:8"]]
- 004cc798 ["CALL", null, ["callee:004b3548:8"]]
+ 004cc7d8 ["INT_ADD", "register:40f0:8", ["const:4cc7d8:8", "const:4:8"]]
+ 004cc7d8 ["CALL", null, ["callee:004b3548:8"]]
- 004cc798 bytes 5c9bff97
+ 004cc7d8 bytes 5c9bff97
- 004cc7ac ["INT_ADD", "register:40f0:8", ["const:4cc7ac:8", "const:4:8"]]
- 004cc7ac ["CALL", null, ["callee:00c58bb0:8"]]
+ 004cc7ec ["INT_ADD", "register:40f0:8", ["const:4cc7ec:8", "const:4:8"]]
+ 004cc7ec ["CALL", null, ["callee:00c58bb0:8"]]
- 004cc7ac bytes cd301e94
+ 004cc7ec bytes f1301e94
- 004cc7c4 ["INT_ADD", "register:40f0:8", ["const:4cc7c4:8", "const:4:8"]]
- 004cc7c4 ["CALL", null, ["callee:0054052c:8"]]
+ 004cc804 ["INT_ADD", "register:40f0:8", ["const:4cc804:8", "const:4:8"]]
+ 004cc804 ["CALL", null, ["callee:0054052c:8"]]
- 004cc7c4 bytes 4acf0194
+ 004cc804 bytes 4acf0194
~~~


<a id="compare-d036a222cfc1c435ffe7cc2312fa871b"></a>

### [`004cc7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc7fc.md) → [`004cc83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc83c.md) _ZN5Botan10hex_decodeEPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59150.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c59220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59220.md) · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc7fc.md#insn-004cc83c) · [`004cc858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc7fc.md#insn-004cc858) · [`004cc870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc7fc.md#insn-004cc870)
- 新版 [`004cc87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc83c.md#insn-004cc87c) · [`004cc898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc83c.md#insn-004cc898) · [`004cc8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc83c.md#insn-004cc8b0)

~~~diff
- 004cc83c ["INT_ADD", "register:40f0:8", ["const:4cc83c:8", "const:4:8"]]
- 004cc83c ["CALL", null, ["callee:00c57f60:8"]]
+ 004cc87c ["INT_ADD", "register:40f0:8", ["const:4cc87c:8", "const:4:8"]]
+ 004cc87c ["CALL", null, ["callee:00c57f60:8"]]
- 004cc83c bytes 952d1e94
+ 004cc87c bytes b92d1e94
- 004cc858 ["INT_ADD", "register:40f0:8", ["const:4cc858:8", "const:4:8"]]
- 004cc858 ["CALL", null, ["callee:00c58160:8"]]
+ 004cc898 ["INT_ADD", "register:40f0:8", ["const:4cc898:8", "const:4:8"]]
+ 004cc898 ["CALL", null, ["callee:00c58160:8"]]
- 004cc858 bytes 0e2e1e94
+ 004cc898 bytes 322e1e94
- 004cc870 ["INT_ADD", "register:40f0:8", ["const:4cc870:8", "const:4:8"]]
- 004cc870 ["CALL", null, ["callee:00c58bb0:8"]]
+ 004cc8b0 ["INT_ADD", "register:40f0:8", ["const:4cc8b0:8", "const:4:8"]]
+ 004cc8b0 ["CALL", null, ["callee:00c58bb0:8"]]
- 004cc870 bytes 9c301e94
+ 004cc8b0 bytes c0301e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c54361519c296685f6b60c9d89ba153"></a>

### [`004cd140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd140.md) → [`004cd180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd180.md) _ZN5Botan4HMAC5clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59180.md) · 呼出先 2件 [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c59250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59250.md) · 呼出先 2件 [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd140.md#insn-004cd15c) · [`004cd174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd140.md#insn-004cd174) · [`004cd184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd140.md#insn-004cd184)
- 新版 [`004cd19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd180.md#insn-004cd19c) · [`004cd1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd180.md#insn-004cd1b4) · [`004cd1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd180.md#insn-004cd1c4)

~~~diff
- 004cd15c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cd15c ["INT_ADD", "register:40f0:8", ["const:4cd15c:8", "const:4:8"]]
- 004cd15c ["CALLIND", null, ["register:0:8"]]
+ 004cd19c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd19c ["INT_ADD", "register:40f0:8", ["const:4cd19c:8", "const:4:8"]]
+ 004cd19c ["CALLIND", null, ["register:0:8"]]
- 004cd15c bytes 00013fd6
+ 004cd19c bytes 00013fd6
- 004cd174 ["INT_ADD", "register:40f0:8", ["const:4cd174:8", "const:4:8"]]
- 004cd174 ["CALL", null, ["callee:00c58160:8"]]
+ 004cd1b4 ["INT_ADD", "register:40f0:8", ["const:4cd1b4:8", "const:4:8"]]
+ 004cd1b4 ["CALL", null, ["callee:00c58160:8"]]
- 004cd174 bytes c72b1e94
+ 004cd1b4 bytes eb2b1e94
- 004cd184 ["INT_ADD", "register:40f0:8", ["const:4cd184:8", "const:4:8"]]
- 004cd184 ["CALL", null, ["callee:00540bb8:8"]]
+ 004cd1c4 ["INT_ADD", "register:40f0:8", ["const:4cd1c4:8", "const:4:8"]]
+ 004cd1c4 ["CALL", null, ["callee:00540bb8:8"]]
- 004cd184 bytes 7dce0194
+ 004cd1c4 bytes 7dce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7378f19bb24221fdf45504a617d0d4"></a>

### [`004cd2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd2dc.md) → [`004cd31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd31c.md) _ZNK5Botan4HMAC5cloneEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c591a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c59270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd2dc.md#insn-004cd2f0) · [`004cd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd2dc.md#insn-004cd308) · [`004cd314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd2dc.md#insn-004cd314)
- 新版 [`004cd330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd31c.md#insn-004cd330) · [`004cd348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd31c.md#insn-004cd348) · [`004cd354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd31c.md#insn-004cd354)

~~~diff
- 004cd2f0 ["INT_ADD", "register:40f0:8", ["const:4cd2f0:8", "const:4:8"]]
- 004cd2f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 004cd330 ["INT_ADD", "register:40f0:8", ["const:4cd330:8", "const:4:8"]]
+ 004cd330 ["CALL", null, ["callee:00c57f60:8"]]
- 004cd2f0 bytes e82a1e94
+ 004cd330 bytes 0c2b1e94
- 004cd308 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd308 ["INT_ADD", "register:40f0:8", ["const:4cd308:8", "const:4:8"]]
- 004cd308 ["CALLIND", null, ["register:0:8"]]
+ 004cd348 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cd348 ["INT_ADD", "register:40f0:8", ["const:4cd348:8", "const:4:8"]]
+ 004cd348 ["CALLIND", null, ["register:0:8"]]
- 004cd308 bytes 20013fd6
+ 004cd348 bytes 20013fd6
- 004cd314 ["INT_ADD", "register:40f0:8", ["const:4cd314:8", "const:4:8"]]
- 004cd314 ["CALL", null, ["callee:00c59270:8"]]
+ 004cd354 ["INT_ADD", "register:40f0:8", ["const:4cd354:8", "const:4:8"]]
+ 004cd354 ["CALL", null, ["callee:00c59270:8"]]
- 004cd314 bytes a32f1e94
+ 004cd354 bytes c72f1e94
~~~


<a id="compare-2534a771642b1797ba6e01400ea86a4c"></a>

### [`004cd4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd4fc.md) → [`004cd53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd53c.md) _ZN5Botan3KDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c591b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591b0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)
- 新版 呼出元 1件 [`00c59280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59280.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd4fc.md#insn-004cd544) · [`004cd550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd4fc.md#insn-004cd550) · [`004cd560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd4fc.md#insn-004cd560)
- 新版 [`004cd584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd53c.md#insn-004cd584) · [`004cd590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd53c.md#insn-004cd590) · [`004cd5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd53c.md#insn-004cd5a0)

~~~diff
- 004cd544 ["INT_ADD", "register:40f0:8", ["const:4cd544:8", "const:4:8"]]
- 004cd544 ["CALL", null, ["callee:0043bb60:8"]]
+ 004cd584 ["INT_ADD", "register:40f0:8", ["const:4cd584:8", "const:4:8"]]
+ 004cd584 ["CALL", null, ["callee:0043bb60:8"]]
- 004cd544 bytes 77b9fd97
+ 004cd584 bytes 77b9fd97
- 004cd550 ["INT_ADD", "register:40f0:8", ["const:4cd550:8", "const:4:8"]]
- 004cd550 ["CALL", null, ["callee:00c58e10:8"]]
+ 004cd590 ["INT_ADD", "register:40f0:8", ["const:4cd590:8", "const:4:8"]]
+ 004cd590 ["CALL", null, ["callee:00c58e10:8"]]
- 004cd550 bytes fc2d1e94
+ 004cd590 bytes 202e1e94
- 004cd560 ["INT_ADD", "register:40f0:8", ["const:4cd560:8", "const:4:8"]]
- 004cd560 ["CALL", null, ["callee:00c57f80:8"]]
+ 004cd5a0 ["INT_ADD", "register:40f0:8", ["const:4cd5a0:8", "const:4:8"]]
+ 004cd5a0 ["CALL", null, ["callee:00c57f80:8"]]
- 004cd560 bytes 542a1e94
+ 004cd5a0 bytes 782a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21c75948a43dbc723e8b220efc87c65a"></a>

### [`004cd788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md) → [`004cd7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd7c8.md) _ZN5Botan3KDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004cd8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004cd8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd8e8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md#insn-004cd7d4) · [`004cd7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md#insn-004cd7e4) · [`004cd820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md#insn-004cd820)
- 新版 [`004cd814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd7c8.md#insn-004cd814) · [`004cd824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd7c8.md#insn-004cd824) · [`004cd860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd7c8.md#insn-004cd860)

~~~diff
- 004cd7d4 ["INT_ADD", "register:40f0:8", ["const:4cd7d4:8", "const:4:8"]]
- 004cd7d4 ["CALL", null, ["callee:00473580:8"]]
+ 004cd814 ["INT_ADD", "register:40f0:8", ["const:4cd814:8", "const:4:8"]]
+ 004cd814 ["CALL", null, ["callee:00473580:8"]]
- 004cd7d4 bytes 5b97fe97
+ 004cd814 bytes 5b97fe97
- 004cd7e4 ["INT_ADD", "register:40f0:8", ["const:4cd7e4:8", "const:4:8"]]
- 004cd7e4 ["CALL", null, ["callee:004cd8e8:8"]]
+ 004cd824 ["INT_ADD", "register:40f0:8", ["const:4cd824:8", "const:4:8"]]
+ 004cd824 ["CALL", null, ["callee:004cd8e8:8"]]
- 004cd7e4 bytes 31000094
+ 004cd824 bytes 31000094
- 004cd820 ["INT_ADD", "register:40f0:8", ["const:4cd820:8", "const:4:8"]]
- 004cd820 ["CALL", null, ["callee:00c57f80:8"]]
+ 004cd860 ["INT_ADD", "register:40f0:8", ["const:4cd860:8", "const:4:8"]]
+ 004cd860 ["CALL", null, ["callee:00c57f80:8"]]
- 004cd820 bytes a4291e94
+ 004cd860 bytes c8291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360044b2721a7f14297b2000e6cf16cd"></a>

### [`004cd8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md) → [`004cd8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd8e8.md) FUN_004cd8e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004cd788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c591b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591b0.md)
- 新版 呼出元 1件 [`004cd7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd7c8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md#insn-004cd8f8) · [`004cd90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md#insn-004cd90c) · [`004cd924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md#insn-004cd924)
- 新版 [`004cd938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd8e8.md#insn-004cd938) · [`004cd94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd8e8.md#insn-004cd94c) · [`004cd964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd8e8.md#insn-004cd964)

~~~diff
- 004cd8f8 ["INT_ADD", "register:40f0:8", ["const:4cd8f8:8", "const:4:8"]]
- 004cd8f8 ["CALL", null, ["callee:00540dbc:8"]]
+ 004cd938 ["INT_ADD", "register:40f0:8", ["const:4cd938:8", "const:4:8"]]
+ 004cd938 ["CALL", null, ["callee:00540dbc:8"]]
- 004cd8f8 bytes 21cd0194
+ 004cd938 bytes 21cd0194
- 004cd90c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cd90c ["INT_ADD", "register:40f0:8", ["const:4cd90c:8", "const:4:8"]]
- 004cd90c ["CALLIND", null, ["register:0:8"]]
+ 004cd94c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd94c ["INT_ADD", "register:40f0:8", ["const:4cd94c:8", "const:4:8"]]
+ 004cd94c ["CALLIND", null, ["register:0:8"]]
- 004cd90c bytes 00013fd6
+ 004cd94c bytes 00013fd6
- 004cd924 ["INT_ADD", "register:40f0:8", ["const:4cd924:8", "const:4:8"]]
- 004cd924 ["CALL", null, ["callee:00c59280:8"]]
+ 004cd964 ["INT_ADD", "register:40f0:8", ["const:4cd964:8", "const:4:8"]]
+ 004cd964 ["CALL", null, ["callee:00c59280:8"]]
- 004cd924 bytes 232e1e94
+ 004cd964 bytes 472e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-201f9ae3462a52ed6288da84df183e3a"></a>

### [`004ce050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce050.md) → [`004ce090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce090.md) _ZNK5Botan16PK_Encryptor_EME18maximum_input_sizeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce050.md#insn-004ce064)
- 新版 [`004ce0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce090.md#insn-004ce0a4)

~~~diff
- 004ce064 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ce064 ["INT_ADD", "register:40f0:8", ["const:4ce064:8", "const:4:8"]]
- 004ce064 ["CALLIND", null, ["register:0:8"]]
+ 004ce0a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce0a4 ["INT_ADD", "register:40f0:8", ["const:4ce0a4:8", "const:4:8"]]
+ 004ce0a4 ["CALLIND", null, ["register:0:8"]]
- 004ce064 bytes 00013fd6
+ 004ce0a4 bytes 00013fd6
~~~


<a id="compare-fbd7a30629a01bcdeb88fbf5bcd2fbf8"></a>

### [`004ce074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce074.md) → [`004ce0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce0b4.md) _ZN5Botan7KeyPair27signature_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringIc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59220.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59230.md) [`00c59240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59240.md)
- 新版 呼出元 1件 [`00c592f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c592f0.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59300.md) [`00c59310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce074.md#insn-004ce0b8) · [`004ce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce074.md#insn-004ce0c8) · [`004ce0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce074.md#insn-004ce0e4)
- 新版 [`004ce0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce0b4.md#insn-004ce0f8) · [`004ce108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce0b4.md#insn-004ce108) · [`004ce124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce0b4.md#insn-004ce124)

~~~diff
- 004ce0b8 ["INT_ADD", "register:40f0:8", ["const:4ce0b8:8", "const:4:8"]]
- 004ce0b8 ["CALL", null, ["callee:00c59300:8"]]
+ 004ce0f8 ["INT_ADD", "register:40f0:8", ["const:4ce0f8:8", "const:4:8"]]
+ 004ce0f8 ["CALL", null, ["callee:00c59300:8"]]
- 004ce0b8 bytes 5e2c1e94
+ 004ce0f8 bytes 822c1e94
- 004ce0c8 ["INT_ADD", "register:40f0:8", ["const:4ce0c8:8", "const:4:8"]]
- 004ce0c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ce108 ["INT_ADD", "register:40f0:8", ["const:4ce108:8", "const:4:8"]]
+ 004ce108 ["CALL", null, ["callee:00c57f80:8"]]
- 004ce0c8 bytes 7a271e94
+ 004ce108 bytes 9e271e94
- 004ce0e4 ["INT_ADD", "register:40f0:8", ["const:4ce0e4:8", "const:4:8"]]
- 004ce0e4 ["CALL", null, ["callee:00c59310:8"]]
+ 004ce124 ["INT_ADD", "register:40f0:8", ["const:4ce124:8", "const:4:8"]]
+ 004ce124 ["CALL", null, ["callee:00c59310:8"]]
- 004ce0e4 bytes 572c1e94
+ 004ce124 bytes 7b2c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953be649fea844ea1493e861395d661e"></a>

### [`004ce2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce2cc.md) → [`004ce30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce30c.md) _ZN5Botan25MessageAuthenticationCode6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md)
- 新版 呼出元 1件 [`00c58f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f60.md) · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce2cc.md#insn-004ce318) · [`004ce324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce2cc.md#insn-004ce324) · [`004ce334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce2cc.md#insn-004ce334)
- 新版 [`004ce358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce30c.md#insn-004ce358) · [`004ce364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce30c.md#insn-004ce364) · [`004ce374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce30c.md#insn-004ce374)

~~~diff
- 004ce318 ["INT_ADD", "register:40f0:8", ["const:4ce318:8", "const:4:8"]]
- 004ce318 ["CALL", null, ["callee:0043bb60:8"]]
+ 004ce358 ["INT_ADD", "register:40f0:8", ["const:4ce358:8", "const:4:8"]]
+ 004ce358 ["CALL", null, ["callee:0043bb60:8"]]
- 004ce318 bytes 02b6fd97
+ 004ce358 bytes 02b6fd97
- 004ce324 ["INT_ADD", "register:40f0:8", ["const:4ce324:8", "const:4:8"]]
- 004ce324 ["CALL", null, ["callee:00c58e10:8"]]
+ 004ce364 ["INT_ADD", "register:40f0:8", ["const:4ce364:8", "const:4:8"]]
+ 004ce364 ["CALL", null, ["callee:00c58e10:8"]]
- 004ce324 bytes 872a1e94
+ 004ce364 bytes ab2a1e94
- 004ce334 ["INT_ADD", "register:40f0:8", ["const:4ce334:8", "const:4:8"]]
- 004ce334 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ce374 ["INT_ADD", "register:40f0:8", ["const:4ce374:8", "const:4:8"]]
+ 004ce374 ["CALL", null, ["callee:00c57f80:8"]]
- 004ce334 bytes df261e94
+ 004ce374 bytes 03271e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f02286de18e57dde642da37bdd8168"></a>

### [`004ce584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md) → [`004ce5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce5c4.md) _ZN5Botan25MessageAuthenticationCode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004ce6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004ce728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce728.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md#insn-004ce5f4) · [`004ce604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md#insn-004ce604) · [`004ce640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md#insn-004ce640)
- 新版 [`004ce634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce5c4.md#insn-004ce634) · [`004ce644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce5c4.md#insn-004ce644) · [`004ce680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce5c4.md#insn-004ce680)

~~~diff
- 004ce5f4 ["INT_ADD", "register:40f0:8", ["const:4ce5f4:8", "const:4:8"]]
- 004ce5f4 ["CALL", null, ["callee:00473580:8"]]
+ 004ce634 ["INT_ADD", "register:40f0:8", ["const:4ce634:8", "const:4:8"]]
+ 004ce634 ["CALL", null, ["callee:00473580:8"]]
- 004ce5f4 bytes d393fe97
+ 004ce634 bytes d393fe97
- 004ce604 ["INT_ADD", "register:40f0:8", ["const:4ce604:8", "const:4:8"]]
- 004ce604 ["CALL", null, ["callee:004ce728:8"]]
+ 004ce644 ["INT_ADD", "register:40f0:8", ["const:4ce644:8", "const:4:8"]]
+ 004ce644 ["CALL", null, ["callee:004ce728:8"]]
- 004ce604 bytes 39000094
+ 004ce644 bytes 39000094
- 004ce640 ["INT_ADD", "register:40f0:8", ["const:4ce640:8", "const:4:8"]]
- 004ce640 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ce680 ["INT_ADD", "register:40f0:8", ["const:4ce680:8", "const:4:8"]]
+ 004ce680 ["CALL", null, ["callee:00c57f80:8"]]
- 004ce640 bytes 1c261e94
+ 004ce680 bytes 40261e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c440b51518f29c4d05df908c08a5e87b"></a>

### [`004ce6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md) → [`004ce728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce728.md) FUN_004ce728

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ce584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md)
- 新版 呼出元 1件 [`004ce5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce5c4.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md#insn-004ce738) · [`004ce74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md#insn-004ce74c) · [`004ce768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md#insn-004ce768)
- 新版 [`004ce778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce728.md#insn-004ce778) · [`004ce78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce728.md#insn-004ce78c) · [`004ce7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce728.md#insn-004ce7a8)

~~~diff
- 004ce738 ["INT_ADD", "register:40f0:8", ["const:4ce738:8", "const:4:8"]]
- 004ce738 ["CALL", null, ["callee:00540dbc:8"]]
+ 004ce778 ["INT_ADD", "register:40f0:8", ["const:4ce778:8", "const:4:8"]]
+ 004ce778 ["CALL", null, ["callee:00540dbc:8"]]
- 004ce738 bytes 91c90194
+ 004ce778 bytes 91c90194
- 004ce74c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ce74c ["INT_ADD", "register:40f0:8", ["const:4ce74c:8", "const:4:8"]]
- 004ce74c ["CALLIND", null, ["register:0:8"]]
+ 004ce78c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce78c ["INT_ADD", "register:40f0:8", ["const:4ce78c:8", "const:4:8"]]
+ 004ce78c ["CALLIND", null, ["register:0:8"]]
- 004ce74c bytes 00013fd6
+ 004ce78c bytes 00013fd6
- 004ce768 ["INT_ADD", "register:40f0:8", ["const:4ce768:8", "const:4:8"]]
- 004ce768 ["CALL", null, ["callee:00c58f60:8"]]
+ 004ce7a8 ["INT_ADD", "register:40f0:8", ["const:4ce7a8:8", "const:4:8"]]
+ 004ce7a8 ["CALL", null, ["callee:00c58f60:8"]]
- 004ce768 bytes ca291e94
+ 004ce7a8 bytes ee291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd98de468591909dda5c512cdab05e13"></a>

### [`004cea78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004cea78.md) → [`004ceab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ceab8.md) _ZN5Botan3MD510compress_nEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004cea78.md#insn-004cf490)
- 新版 [`004cf4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ceab8.md#insn-004cf4d0)

~~~diff
- 004cf490 ["INT_ADD", "register:40f0:8", ["const:4cf490:8", "const:4:8"]]
- 004cf490 ["CALL", null, ["callee:00c580d0:8"]]
+ 004cf4d0 ["INT_ADD", "register:40f0:8", ["const:4cf4d0:8", "const:4:8"]]
+ 004cf4d0 ["CALL", null, ["callee:00c580d0:8"]]
- 004cf490 bytes dc221e94
+ 004cf4d0 bytes 00231e94
~~~


<a id="compare-3ef9455e45d0c0f6bf8db7f256cbd0ce"></a>

### [`004cf550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf550.md) → [`004cf590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf590.md) _ZN5Botan16MDx_HashFunction5clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf550.md#insn-004cf574)
- 新版 [`004cf5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf590.md#insn-004cf5b4)

~~~diff
- 004cf574 ["INT_ADD", "register:40f0:8", ["const:4cf574:8", "const:4:8"]]
- 004cf574 ["CALL", null, ["callee:00c58160:8"]]
+ 004cf5b4 ["INT_ADD", "register:40f0:8", ["const:4cf5b4:8", "const:4:8"]]
+ 004cf5b4 ["CALL", null, ["callee:00c58160:8"]]
- 004cf574 bytes c7221e94
+ 004cf5b4 bytes eb221e94
~~~


<a id="compare-b27b300b558fcb2faf06d641bb26a302"></a>

### [`004cf5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf5dc.md) → [`004cf61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf61c.md) _ZN5Botan16MDx_HashFunction8add_dataEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf5dc.md#insn-004cf62c) · [`004cf658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf5dc.md#insn-004cf658) · [`004cf6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf5dc.md#insn-004cf6ac)
- 新版 [`004cf66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf61c.md#insn-004cf66c) · [`004cf698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf61c.md#insn-004cf698) · [`004cf6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf61c.md#insn-004cf6ec)

~~~diff
- 004cf62c ["INT_ADD", "register:40f0:8", ["const:4cf62c:8", "const:4:8"]]
- 004cf62c ["CALL", null, ["callee:00c58010:8"]]
+ 004cf66c ["INT_ADD", "register:40f0:8", ["const:4cf66c:8", "const:4:8"]]
+ 004cf66c ["CALL", null, ["callee:00c58010:8"]]
- 004cf62c bytes 45221e94
+ 004cf66c bytes 69221e94
- 004cf658 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf658 ["INT_ADD", "register:40f0:8", ["const:4cf658:8", "const:4:8"]]
- 004cf658 ["CALLIND", null, ["register:0:8"]]
+ 004cf698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf698 ["INT_ADD", "register:40f0:8", ["const:4cf698:8", "const:4:8"]]
+ 004cf698 ["CALLIND", null, ["register:0:8"]]
- 004cf658 bytes 00013fd6
+ 004cf698 bytes 00013fd6
- 004cf6ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf6ac ["INT_ADD", "register:40f0:8", ["const:4cf6ac:8", "const:4:8"]]
- 004cf6ac ["CALLIND", null, ["register:0:8"]]
+ 004cf6ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf6ec ["INT_ADD", "register:40f0:8", ["const:4cf6ec:8", "const:4:8"]]
+ 004cf6ec ["CALLIND", null, ["register:0:8"]]
- 004cf6ac bytes 00013fd6
+ 004cf6ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a8f4576485e2c192854672e79d9ea24"></a>

### [`004cf708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf708.md) → [`004cf748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf748.md) _ZN5Botan16MDx_HashFunction12final_resultEPh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf708.md#insn-004cf794) · [`004cf7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf708.md#insn-004cf7a8) · [`004cf7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf708.md#insn-004cf7c4)
- 新版 [`004cf7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf748.md#insn-004cf7d4) · [`004cf7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf748.md#insn-004cf7e8) · [`004cf804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cf748.md#insn-004cf804)

~~~diff
- 004cf794 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf794 ["INT_ADD", "register:40f0:8", ["const:4cf794:8", "const:4:8"]]
- 004cf794 ["CALLIND", null, ["register:0:8"]]
+ 004cf7d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cf7d4 ["INT_ADD", "register:40f0:8", ["const:4cf7d4:8", "const:4:8"]]
+ 004cf7d4 ["CALLIND", null, ["register:0:8"]]
- 004cf794 bytes 20013fd6
+ 004cf7d4 bytes 20013fd6
- 004cf7a8 ["INT_ADD", "register:40f0:8", ["const:4cf7a8:8", "const:4:8"]]
- 004cf7a8 ["CALL", null, ["callee:00c58160:8"]]
+ 004cf7e8 ["INT_ADD", "register:40f0:8", ["const:4cf7e8:8", "const:4:8"]]
+ 004cf7e8 ["CALL", null, ["callee:00c58160:8"]]
- 004cf7a8 bytes 3a221e94
+ 004cf7e8 bytes 5e221e94
- 004cf7c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf7c4 ["INT_ADD", "register:40f0:8", ["const:4cf7c4:8", "const:4:8"]]
- 004cf7c4 ["CALLIND", null, ["register:0:8"]]
+ 004cf804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf804 ["INT_ADD", "register:40f0:8", ["const:4cf804:8", "const:4:8"]]
+ 004cf804 ["CALLIND", null, ["register:0:8"]]
- 004cf7c4 bytes 00013fd6
+ 004cf804 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991cda9b0ac7888b264ce99a07c1e981"></a>

### [`004cfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfdc8.md) → [`004cfe08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfe08.md) _ZNK5Botan13PKCS7_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00544cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544cdc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00544d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cfe34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfdc8.md#insn-004cfe34) · [`004cfe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfdc8.md#insn-004cfe60)
- 新版 [`004cfe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfe08.md#insn-004cfe74) · [`004cfea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfe08.md#insn-004cfea0)

~~~diff
- 004cfe34 ["INT_ADD", "register:40f0:8", ["const:4cfe34:8", "const:4:8"]]
- 004cfe34 ["CALL", null, ["callee:00544d1c:8"]]
+ 004cfe74 ["INT_ADD", "register:40f0:8", ["const:4cfe74:8", "const:4:8"]]
+ 004cfe74 ["CALL", null, ["callee:00544d1c:8"]]
- 004cfe34 bytes aad30194
+ 004cfe74 bytes aad30194
- 004cfe60 ["INT_ADD", "register:40f0:8", ["const:4cfe60:8", "const:4:8"]]
- 004cfe60 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004cfea0 ["INT_ADD", "register:40f0:8", ["const:4cfea0:8", "const:4:8"]]
+ 004cfea0 ["CALL", null, ["callee:00c57fb0:8"]]
- 004cfe60 bytes 20201e94
+ 004cfea0 bytes 44201e94
~~~


<a id="compare-40ee7c834f8356a7fdeabf63a8de9220"></a>

### [`004d028c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d028c.md) → [`004d02cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md) _ZNK5Botan17ANSI_X923_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00544cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544cdc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00544d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d02dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d028c.md#insn-004d02dc) · [`004d0328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d028c.md#insn-004d0328) · [`004d0354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d028c.md#insn-004d0354)
- 新版 [`004d031c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md#insn-004d031c) · [`004d0368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md#insn-004d0368) · [`004d0394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md#insn-004d0394)

~~~diff
- 004d02dc ["INT_ADD", "register:40f0:8", ["const:4d02dc:8", "const:4:8"]]
- 004d02dc ["CALL", null, ["callee:005411e4:8"]]
+ 004d031c ["INT_ADD", "register:40f0:8", ["const:4d031c:8", "const:4:8"]]
+ 004d031c ["CALL", null, ["callee:005411e4:8"]]
- 004d02dc bytes b2c30194
+ 004d031c bytes b2c30194
- 004d0328 ["INT_ADD", "register:40f0:8", ["const:4d0328:8", "const:4:8"]]
- 004d0328 ["CALL", null, ["callee:00544d1c:8"]]
+ 004d0368 ["INT_ADD", "register:40f0:8", ["const:4d0368:8", "const:4:8"]]
+ 004d0368 ["CALL", null, ["callee:00544d1c:8"]]
- 004d0328 bytes 6dd20194
+ 004d0368 bytes 6dd20194
- 004d0354 ["INT_ADD", "register:40f0:8", ["const:4d0354:8", "const:4:8"]]
- 004d0354 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004d0394 ["INT_ADD", "register:40f0:8", ["const:4d0394:8", "const:4:8"]]
+ 004d0394 ["CALL", null, ["callee:00c57fb0:8"]]
- 004d0354 bytes e31e1e94
+ 004d0394 bytes 071f1e94
~~~


<a id="compare-4de2d141346f4e2331837953a37f24c2"></a>

### [`004d0754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0754.md) → [`004d0794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0794.md) _ZNK5Botan19OneAndZeros_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d07a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0754.md#insn-004d07a4) · [`004d07f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0754.md#insn-004d07f8) · [`004d0824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0754.md#insn-004d0824)
- 新版 [`004d07e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0794.md#insn-004d07e4) · [`004d0838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0794.md#insn-004d0838) · [`004d0864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0794.md#insn-004d0864)

~~~diff
- 004d07a4 ["INT_ADD", "register:40f0:8", ["const:4d07a4:8", "const:4:8"]]
- 004d07a4 ["CALL", null, ["callee:005411e4:8"]]
+ 004d07e4 ["INT_ADD", "register:40f0:8", ["const:4d07e4:8", "const:4:8"]]
+ 004d07e4 ["CALL", null, ["callee:005411e4:8"]]
- 004d07a4 bytes 80c20194
+ 004d07e4 bytes 80c20194
- 004d07f8 ["INT_ADD", "register:40f0:8", ["const:4d07f8:8", "const:4:8"]]
- 004d07f8 ["CALL", null, ["callee:005411e4:8"]]
+ 004d0838 ["INT_ADD", "register:40f0:8", ["const:4d0838:8", "const:4:8"]]
+ 004d0838 ["CALL", null, ["callee:005411e4:8"]]
- 004d07f8 bytes 6bc20194
+ 004d0838 bytes 6bc20194
- 004d0824 ["INT_ADD", "register:40f0:8", ["const:4d0824:8", "const:4:8"]]
- 004d0824 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004d0864 ["INT_ADD", "register:40f0:8", ["const:4d0864:8", "const:4:8"]]
+ 004d0864 ["CALL", null, ["callee:00c57fb0:8"]]
- 004d0824 bytes af1d1e94
+ 004d0864 bytes d31d1e94
~~~


<a id="compare-efe4bee6ab021c679dcecfc1833e7453"></a>

### [`004d08cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d08cc.md) → [`004d090c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d090c.md) _ZNK5Botan11ESP_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d090c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d08cc.md#insn-004d090c) · [`004d095c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d08cc.md#insn-004d095c)
- 新版 [`004d094c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d090c.md#insn-004d094c) · [`004d099c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d090c.md#insn-004d099c)

~~~diff
- 004d090c ["INT_ADD", "register:40f0:8", ["const:4d090c:8", "const:4:8"]]
- 004d090c ["CALL", null, ["callee:005411e4:8"]]
+ 004d094c ["INT_ADD", "register:40f0:8", ["const:4d094c:8", "const:4:8"]]
+ 004d094c ["CALL", null, ["callee:005411e4:8"]]
- 004d090c bytes 26c20194
+ 004d094c bytes 26c20194
- 004d095c ["INT_ADD", "register:40f0:8", ["const:4d095c:8", "const:4:8"]]
- 004d095c ["CALL", null, ["callee:00c57fb0:8"]]
+ 004d099c ["INT_ADD", "register:40f0:8", ["const:4d099c:8", "const:4:8"]]
+ 004d099c ["CALL", null, ["callee:00c57fb0:8"]]
- 004d095c bytes 611d1e94
+ 004d099c bytes 851d1e94
~~~


<a id="compare-014d41be472df0580a2f9d9619af148b"></a>

### [`004d0d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0d70.md) → [`004d0db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0db0.md) _ZN5Botan12StreamCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e60.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)
- 新版 呼出元 1件 [`00c58f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f30.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d0db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0d70.md#insn-004d0db8) · [`004d0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0d70.md#insn-004d0dc4) · [`004d0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0d70.md#insn-004d0dd4)
- 新版 [`004d0df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0db0.md#insn-004d0df8) · [`004d0e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0db0.md#insn-004d0e04) · [`004d0e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0db0.md#insn-004d0e14)

~~~diff
- 004d0db8 ["INT_ADD", "register:40f0:8", ["const:4d0db8:8", "const:4:8"]]
- 004d0db8 ["CALL", null, ["callee:0043bb60:8"]]
+ 004d0df8 ["INT_ADD", "register:40f0:8", ["const:4d0df8:8", "const:4:8"]]
+ 004d0df8 ["CALL", null, ["callee:0043bb60:8"]]
- 004d0db8 bytes 5aabfd97
+ 004d0df8 bytes 5aabfd97
- 004d0dc4 ["INT_ADD", "register:40f0:8", ["const:4d0dc4:8", "const:4:8"]]
- 004d0dc4 ["CALL", null, ["callee:00c58e10:8"]]
+ 004d0e04 ["INT_ADD", "register:40f0:8", ["const:4d0e04:8", "const:4:8"]]
+ 004d0e04 ["CALL", null, ["callee:00c58e10:8"]]
- 004d0dc4 bytes df1f1e94
+ 004d0e04 bytes 03201e94
- 004d0dd4 ["INT_ADD", "register:40f0:8", ["const:4d0dd4:8", "const:4:8"]]
- 004d0dd4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004d0e14 ["INT_ADD", "register:40f0:8", ["const:4d0e14:8", "const:4:8"]]
+ 004d0e14 ["CALL", null, ["callee:00c57f80:8"]]
- 004d0dd4 bytes 371c1e94
+ 004d0e14 bytes 5b1c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8797393b3f050111e64739b4c177280"></a>

### [`004d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1c40.md) → [`004d1c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1c80.md) _ZN5Botan11Cipher_Mode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d1cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1c40.md#insn-004d1cb8) · [`004d1cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1c40.md#insn-004d1cc8) · [`004d1cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1c40.md#insn-004d1cd8)
- 新版 [`004d1cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1c80.md#insn-004d1cf8) · [`004d1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1c80.md#insn-004d1d08) · [`004d1d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1c80.md#insn-004d1d18)

~~~diff
- 004d1cb8 ["INT_ADD", "register:40f0:8", ["const:4d1cb8:8", "const:4:8"]]
- 004d1cb8 ["CALL", null, ["callee:00473580:8"]]
+ 004d1cf8 ["INT_ADD", "register:40f0:8", ["const:4d1cf8:8", "const:4:8"]]
+ 004d1cf8 ["CALL", null, ["callee:00473580:8"]]
- 004d1cb8 bytes 2286fe97
+ 004d1cf8 bytes 2286fe97
- 004d1cc8 ["INT_ADD", "register:40f0:8", ["const:4d1cc8:8", "const:4:8"]]
- 004d1cc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004d1d08 ["INT_ADD", "register:40f0:8", ["const:4d1d08:8", "const:4:8"]]
+ 004d1d08 ["CALL", null, ["callee:00c57f80:8"]]
- 004d1cc8 bytes 7a181e94
+ 004d1d08 bytes 9e181e94
- 004d1cd8 ["INT_ADD", "register:40f0:8", ["const:4d1cd8:8", "const:4:8"]]
- 004d1cd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004d1d18 ["INT_ADD", "register:40f0:8", ["const:4d1d18:8", "const:4:8"]]
+ 004d1d18 ["CALL", null, ["callee:00c57f80:8"]]
- 004d1cd8 bytes 76181e94
+ 004d1d18 bytes 9a181e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b9030748ea765e776b592a70ff3939a"></a>

### [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) → [`004d6ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md) FUN_004d6ea8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) [`004ba1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba1f4.md) [`004db6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db6a0.md) [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) · 呼出先 10件 [`004b90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b90e0.md) [`004d1f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1f90.md) [`004d239c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d239c.md) [`004d2b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2b90.md) [`004d3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d3/004d3764.md)
- 新版 呼出元 5件 [`004b7c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7c50.md) [`004ba234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba234.md) [`004db6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004db/004db6e0.md) [`004df71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004df71c.md) [`004e0468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e0/004e0468.md) · 呼出先 10件 [`004b9120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9120.md) [`004d1fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1fd0.md) [`004d23dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d23dc.md) [`004d2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d2bd0.md) [`004d37a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d3/004d37a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md#insn-004d6eb4) · [`004d70ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md#insn-004d70ac)
- 新版 [`004d6ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md#insn-004d6ef4) · [`004d70ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md#insn-004d70ec)

~~~diff
- 004d6eb4 ["INT_ADD", "register:40f0:8", ["const:4d6eb4:8", "const:4:8"]]
- 004d6eb4 ["CALL", null, ["callee:00c58160:8"]]
+ 004d6ef4 ["INT_ADD", "register:40f0:8", ["const:4d6ef4:8", "const:4:8"]]
+ 004d6ef4 ["CALL", null, ["callee:00c58160:8"]]
- 004d6eb4 bytes 77041e94
+ 004d6ef4 bytes 9b041e94
- 004d70ac ["INT_ADD", "register:40f0:8", ["const:4d70ac:8", "const:4:8"]]
- 004d70ac ["CALL", null, ["callee:004d72fc:8"]]
+ 004d70ec ["INT_ADD", "register:40f0:8", ["const:4d70ec:8", "const:4:8"]]
+ 004d70ec ["CALL", null, ["callee:004d72fc:8"]]
- 004d70ac bytes 84000094
+ 004d70ec bytes 84000094
~~~


<a id="compare-e63aabf4133d4d52ca18891b72da6c01"></a>

### [`004d7114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7114.md) → [`004d7154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7154.md) FUN_004d7154

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 4件 [`004d6ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md) [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) [`004d7704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7704.md) [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d7150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7114.md#insn-004d7150)
- 新版 [`004d7190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7154.md#insn-004d7190)

~~~diff
- 004d7150 ["INT_ADD", "register:40f0:8", ["const:4d7150:8", "const:4:8"]]
- 004d7150 ["CALL", null, ["callee:00c58160:8"]]
+ 004d7190 ["INT_ADD", "register:40f0:8", ["const:4d7190:8", "const:4:8"]]
+ 004d7190 ["CALL", null, ["callee:00c58160:8"]]
- 004d7150 bytes d0031e94
+ 004d7190 bytes f4031e94
~~~


<a id="compare-314cca44e707dafbf7fb651db1f2e060"></a>

### [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) → [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) FUN_004d73d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) · 呼出先 11件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d239c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d239c.md) [`004d2b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2b90.md)
- 新版 呼出元 2件 [`004d6ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md) [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) · 呼出先 11件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004d23dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d23dc.md) [`004d2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d2bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d73e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md#insn-004d73e8) · [`004d7400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md#insn-004d7400) · [`004d7418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md#insn-004d7418)
- 新版 [`004d7428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md#insn-004d7428) · [`004d7440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md#insn-004d7440) · [`004d7458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md#insn-004d7458)

~~~diff
- 004d73e8 ["INT_ADD", "register:40f0:8", ["const:4d73e8:8", "const:4:8"]]
- 004d73e8 ["CALL", null, ["callee:004b87f4:8"]]
+ 004d7428 ["INT_ADD", "register:40f0:8", ["const:4d7428:8", "const:4:8"]]
+ 004d7428 ["CALL", null, ["callee:004b87f4:8"]]
- 004d73e8 bytes f384ff97
+ 004d7428 bytes f384ff97
- 004d7400 ["INT_ADD", "register:40f0:8", ["const:4d7400:8", "const:4:8"]]
- 004d7400 ["CALL", null, ["callee:004b87f4:8"]]
+ 004d7440 ["INT_ADD", "register:40f0:8", ["const:4d7440:8", "const:4:8"]]
+ 004d7440 ["CALL", null, ["callee:004b87f4:8"]]
- 004d7400 bytes ed84ff97
+ 004d7440 bytes ed84ff97
- 004d7418 ["INT_ADD", "register:40f0:8", ["const:4d7418:8", "const:4:8"]]
- 004d7418 ["CALL", null, ["callee:00c58160:8"]]
+ 004d7458 ["INT_ADD", "register:40f0:8", ["const:4d7458:8", "const:4:8"]]
+ 004d7458 ["CALL", null, ["callee:00c58160:8"]]
- 004d7418 bytes 1e031e94
+ 004d7458 bytes 42031e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-358468bfbe18388e5b5778ba6b45c229"></a>

### [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) → [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) FUN_004d7948

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 11件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d2118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2118.md) [`004d2714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2714.md)
- 新版 呼出元 2件 [`004d7704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7704.md) [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) · 呼出先 11件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004d2158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d2158.md) [`004d2754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d2/004d2754.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d795c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md#insn-004d795c) · [`004d7974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md#insn-004d7974) · [`004d79e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md#insn-004d79e4)
- 新版 [`004d799c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md#insn-004d799c) · [`004d79b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md#insn-004d79b4) · [`004d7a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md#insn-004d7a24)

~~~diff
- 004d795c ["INT_ADD", "register:40f0:8", ["const:4d795c:8", "const:4:8"]]
- 004d795c ["CALL", null, ["callee:004b87f4:8"]]
+ 004d799c ["INT_ADD", "register:40f0:8", ["const:4d799c:8", "const:4:8"]]
+ 004d799c ["CALL", null, ["callee:004b87f4:8"]]
- 004d795c bytes 9683ff97
+ 004d799c bytes 9683ff97
- 004d7974 ["INT_ADD", "register:40f0:8", ["const:4d7974:8", "const:4:8"]]
- 004d7974 ["CALL", null, ["callee:00c58160:8"]]
+ 004d79b4 ["INT_ADD", "register:40f0:8", ["const:4d79b4:8", "const:4:8"]]
+ 004d79b4 ["CALL", null, ["callee:00c58160:8"]]
- 004d7974 bytes c7011e94
+ 004d79b4 bytes eb011e94
- 004d79e4 ["INT_ADD", "register:40f0:8", ["const:4d79e4:8", "const:4:8"]]
- 004d79e4 ["CALL", null, ["callee:004b898c:8"]]
+ 004d7a24 ["INT_ADD", "register:40f0:8", ["const:4d7a24:8", "const:4:8"]]
+ 004d7a24 ["CALL", null, ["callee:004b898c:8"]]
- 004d79e4 bytes da83ff97
+ 004d7a24 bytes da83ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4b0bd172e5986d936756bf97e52962"></a>

### [`004d7b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7b6c.md) → [`004d7bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7bac.md) FUN_004d7bac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 2件 [`004df71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004df71c.md) [`004e0468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e0/004e0468.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d7dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7b6c.md#insn-004d7dcc)
- 新版 [`004d7e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7bac.md#insn-004d7e0c)

~~~diff
- 004d7dcc ["INT_ADD", "register:40f0:8", ["const:4d7dcc:8", "const:4:8"]]
- 004d7dcc ["CALL", null, ["callee:00c58010:8"]]
+ 004d7e0c ["INT_ADD", "register:40f0:8", ["const:4d7e0c:8", "const:4:8"]]
+ 004d7e0c ["CALL", null, ["callee:00c58010:8"]]
- 004d7dcc bytes 5d001e94
+ 004d7e0c bytes 81001e94
~~~


<a id="compare-19437ba8bb80fb5621248b0a8f746789"></a>

### [`004d9418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9418.md) → [`004d9458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9458.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c592b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c59380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d946c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9418.md#insn-004d946c) · [`004d9488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9418.md#insn-004d9488) · [`004d94a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9418.md#insn-004d94a4)
- 新版 [`004d94ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9458.md#insn-004d94ac) · [`004d94c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9458.md#insn-004d94c8) · [`004d94e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9458.md#insn-004d94e4)

~~~diff
- 004d946c ["INT_ADD", "register:40f0:8", ["const:4d946c:8", "const:4:8"]]
- 004d946c ["CALL", null, ["callee:00c57f60:8"]]
+ 004d94ac ["INT_ADD", "register:40f0:8", ["const:4d94ac:8", "const:4:8"]]
+ 004d94ac ["CALL", null, ["callee:00c57f60:8"]]
- 004d946c bytes 89fa1d94
+ 004d94ac bytes adfa1d94
- 004d9488 ["INT_ADD", "register:40f0:8", ["const:4d9488:8", "const:4:8"]]
- 004d9488 ["CALL", null, ["callee:00c58160:8"]]
+ 004d94c8 ["INT_ADD", "register:40f0:8", ["const:4d94c8:8", "const:4:8"]]
+ 004d94c8 ["CALL", null, ["callee:00c58160:8"]]
- 004d9488 bytes 02fb1d94
+ 004d94c8 bytes 26fb1d94
- 004d94a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d94a4 ["INT_ADD", "register:40f0:8", ["const:4d94a4:8", "const:4:8"]]
- 004d94a4 ["CALLIND", null, ["register:0:8"]]
+ 004d94e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004d94e4 ["INT_ADD", "register:40f0:8", ["const:4d94e4:8", "const:4:8"]]
+ 004d94e4 ["CALLIND", null, ["register:0:8"]]
- 004d94a4 bytes 00013fd6
+ 004d94e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b77e062e8dbd1d59c14fafdc1f0b5616"></a>

### [`004dc688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dc/004dc688.md) → [`004dc6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dc/004dc6c8.md) _ZN5Botan29normalized_montgomery_inverseERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md) [`00c593a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ba0.md) [`00c59470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dc/004dc688.md#insn-004dc6c0) · [`004dc708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dc/004dc688.md#insn-004dc708)
- 新版 [`004dc700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dc/004dc6c8.md#insn-004dc700) · [`004dc748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dc/004dc6c8.md#insn-004dc748)

~~~diff
- 004dc6c0 ["INT_ADD", "register:40f0:8", ["const:4dc6c0:8", "const:4:8"]]
- 004dc6c0 ["CALL", null, ["callee:00c59470:8"]]
+ 004dc700 ["INT_ADD", "register:40f0:8", ["const:4dc700:8", "const:4:8"]]
+ 004dc700 ["CALL", null, ["callee:00c59470:8"]]
- 004dc6c0 bytes 38f31d94
+ 004dc700 bytes 5cf31d94
- 004dc708 ["INT_ADD", "register:40f0:8", ["const:4dc708:8", "const:4:8"]]
- 004dc708 ["CALL", null, ["callee:00c58ba0:8"]]
+ 004dc748 ["INT_ADD", "register:40f0:8", ["const:4dc748:8", "const:4:8"]]
+ 004dc748 ["CALL", null, ["callee:00c58ba0:8"]]
- 004dc708 bytes f2f01d94
+ 004dc748 bytes 16f11d94
~~~


<a id="compare-f92e1404c9951150c8fe2a00e9be4a42"></a>

### [`004dea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004dea1c.md) → [`004dea5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004dea5c.md) _ZN5Botan9Power_ModaSERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004dea1c.md#insn-004dea44) · [`004dea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004dea1c.md#insn-004dea60)
- 新版 [`004dea84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004dea5c.md#insn-004dea84) · [`004deaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004dea5c.md#insn-004deaa0)

~~~diff
- 004dea44 ["COPY", "register:0:8", ["register:4040:8"]]
- 004dea44 ["INT_ADD", "register:40f0:8", ["const:4dea44:8", "const:4:8"]]
- 004dea44 ["CALLIND", null, ["register:0:8"]]
+ 004dea84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004dea84 ["INT_ADD", "register:40f0:8", ["const:4dea84:8", "const:4:8"]]
+ 004dea84 ["CALLIND", null, ["register:0:8"]]
- 004dea44 bytes 00013fd6
+ 004dea84 bytes 00013fd6
- 004dea60 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dea60 ["INT_ADD", "register:40f0:8", ["const:4dea60:8", "const:4:8"]]
- 004dea60 ["CALLIND", null, ["register:0:8"]]
+ 004deaa0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004deaa0 ["INT_ADD", "register:40f0:8", ["const:4deaa0:8", "const:4:8"]]
+ 004deaa0 ["CALLIND", null, ["register:0:8"]]
- 004dea60 bytes 20013fd6
+ 004deaa0 bytes 20013fd6
~~~


<a id="compare-c6e0f4daf58179b5bb223bb5adf8a096"></a>

### [`004def04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004def04.md) → [`004def44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004def44.md) FUN_004def44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004def30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004def04.md#insn-004def30)
- 新版 [`004def70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004def44.md#insn-004def70)

~~~diff
- 004def30 ["INT_ADD", "register:40f0:8", ["const:4def30:8", "const:4:8"]]
- 004def30 ["CALL", null, ["callee:0054371c:8"]]
+ 004def70 ["INT_ADD", "register:40f0:8", ["const:4def70:8", "const:4:8"]]
+ 004def70 ["CALL", null, ["callee:0054371c:8"]]
- 004def30 bytes eb910194
+ 004def70 bytes eb910194
~~~


<a id="compare-18c19786cb64736b3dff322b7715ca5a"></a>

### [`004df620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df620.md) → [`004df660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004df660.md) FUN_004df660

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df620.md#insn-004df64c)
- 新版 [`004df68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004df660.md#insn-004df68c)

~~~diff
- 004df64c ["INT_ADD", "register:40f0:8", ["const:4df64c:8", "const:4:8"]]
- 004df64c ["CALL", null, ["callee:0054371c:8"]]
+ 004df68c ["INT_ADD", "register:40f0:8", ["const:4df68c:8", "const:4:8"]]
+ 004df68c ["CALL", null, ["callee:0054371c:8"]]
- 004df64c bytes 24900194
+ 004df68c bytes 24900194
~~~


<a id="compare-74bb6b8e4b7bfebaf28b8f16282b8dbd"></a>

### [`004e23f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e23f8.md) → [`004e2438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2438.md) _ZN5Botan13pbes2_encryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e242c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e23f8.md#insn-004e242c) · [`004e2450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e23f8.md#insn-004e2450)
- 新版 [`004e246c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2438.md#insn-004e246c) · [`004e2490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2438.md#insn-004e2490)

~~~diff
- 004e242c ["INT_ADD", "register:40f0:8", ["const:4e242c:8", "const:4:8"]]
- 004e242c ["CALL", null, ["callee:004e2494:8"]]
+ 004e246c ["INT_ADD", "register:40f0:8", ["const:4e246c:8", "const:4:8"]]
+ 004e246c ["CALL", null, ["callee:004e2494:8"]]
- 004e242c bytes 0a000094
+ 004e246c bytes 0a000094
- 004e2450 ["INT_ADD", "register:40f0:8", ["const:4e2450:8", "const:4:8"]]
- 004e2450 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004e2490 ["INT_ADD", "register:40f0:8", ["const:4e2490:8", "const:4:8"]]
+ 004e2490 ["CALL", null, ["callee:00c57fb0:8"]]
- 004e2450 bytes a4d61d94
+ 004e2490 bytes c8d61d94
~~~


<a id="compare-14e3e36c431b4c69274f316a7e8c0b37"></a>

### [`004e33f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e33f8.md) → [`004e3438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3438.md) _ZN5Botan18pbes2_encrypt_msecERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e3424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e33f8.md#insn-004e3424) · [`004e3454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e33f8.md#insn-004e3454)
- 新版 [`004e3464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3438.md#insn-004e3464) · [`004e3494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3438.md#insn-004e3494)

~~~diff
- 004e3424 ["INT_ADD", "register:40f0:8", ["const:4e3424:8", "const:4:8"]]
- 004e3424 ["CALL", null, ["callee:004e2494:8"]]
+ 004e3464 ["INT_ADD", "register:40f0:8", ["const:4e3464:8", "const:4:8"]]
+ 004e3464 ["CALL", null, ["callee:004e2494:8"]]
- 004e3424 bytes 0cfcff97
+ 004e3464 bytes 0cfcff97
- 004e3454 ["INT_ADD", "register:40f0:8", ["const:4e3454:8", "const:4:8"]]
- 004e3454 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004e3494 ["INT_ADD", "register:40f0:8", ["const:4e3494:8", "const:4:8"]]
+ 004e3494 ["CALL", null, ["callee:00c57fb0:8"]]
- 004e3454 bytes a3d21d94
+ 004e3494 bytes c7d21d94
~~~


<a id="compare-6e6a7c26b1662f5e61a2a67557a5af23"></a>

### [`004e3458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e3458.md) → [`004e3498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3498.md) FUN_004e3498

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e3474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e3458.md#insn-004e3474) · [`004e3484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e3458.md#insn-004e3484)
- 新版 [`004e34b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3498.md#insn-004e34b4) · [`004e34c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3498.md#insn-004e34c4)

~~~diff
- 004e3474 ["INT_ADD", "register:40f0:8", ["const:4e3474:8", "const:4:8"]]
- 004e3474 ["CALL", null, ["callee:00c57f80:8"]]
+ 004e34b4 ["INT_ADD", "register:40f0:8", ["const:4e34b4:8", "const:4:8"]]
+ 004e34b4 ["CALL", null, ["callee:00c57f80:8"]]
- 004e3474 bytes 8fd21d94
+ 004e34b4 bytes b3d21d94
- 004e3484 ["INT_ADD", "register:40f0:8", ["const:4e3484:8", "const:4:8"]]
- 004e3484 ["CALL", null, ["callee:00c57f80:8"]]
+ 004e34c4 ["INT_ADD", "register:40f0:8", ["const:4e34c4:8", "const:4:8"]]
+ 004e34c4 ["CALL", null, ["callee:00c57f80:8"]]
- 004e3484 bytes 8bd21d94
+ 004e34c4 bytes afd21d94
~~~


<a id="compare-768cafea69c031d13473b5737b279e1a"></a>

### [`004e4654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4654.md) → [`004e4694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4694.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c59430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59430.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c59500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e468c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4654.md#insn-004e468c) · [`004e46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4654.md#insn-004e46ac)
- 新版 [`004e46cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4694.md#insn-004e46cc) · [`004e46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4694.md#insn-004e46ec)

~~~diff
- 004e468c ["INT_ADD", "register:40f0:8", ["const:4e468c:8", "const:4:8"]]
- 004e468c ["CALL", null, ["callee:004b3548:8"]]
+ 004e46cc ["INT_ADD", "register:40f0:8", ["const:4e46cc:8", "const:4:8"]]
+ 004e46cc ["CALL", null, ["callee:004b3548:8"]]
- 004e468c bytes 9f3bff97
+ 004e46cc bytes 9f3bff97
- 004e46ac ["INT_ADD", "register:40f0:8", ["const:4e46ac:8", "const:4:8"]]
- 004e46ac ["CALL", null, ["callee:00c59500:8"]]
+ 004e46ec ["INT_ADD", "register:40f0:8", ["const:4e46ec:8", "const:4:8"]]
+ 004e46ec ["CALL", null, ["callee:00c59500:8"]]
- 004e46ac bytes 61d31d94
+ 004e46ec bytes 85d31d94
~~~


<a id="compare-4a8ab2f03fe5db6ebe3ecb28fee98a14"></a>

### [`004e4bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md) → [`004e4c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4c2c.md) _ZN5Botan5PBKDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004e4d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004e4d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4d90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md#insn-004e4c5c) · [`004e4c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md#insn-004e4c6c) · [`004e4ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md#insn-004e4ca8)
- 新版 [`004e4c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4c2c.md#insn-004e4c9c) · [`004e4cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4c2c.md#insn-004e4cac) · [`004e4ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4c2c.md#insn-004e4ce8)

~~~diff
- 004e4c5c ["INT_ADD", "register:40f0:8", ["const:4e4c5c:8", "const:4:8"]]
- 004e4c5c ["CALL", null, ["callee:00473580:8"]]
+ 004e4c9c ["INT_ADD", "register:40f0:8", ["const:4e4c9c:8", "const:4:8"]]
+ 004e4c9c ["CALL", null, ["callee:00473580:8"]]
- 004e4c5c bytes 393afe97
+ 004e4c9c bytes 393afe97
- 004e4c6c ["INT_ADD", "register:40f0:8", ["const:4e4c6c:8", "const:4:8"]]
- 004e4c6c ["CALL", null, ["callee:004e4d90:8"]]
+ 004e4cac ["INT_ADD", "register:40f0:8", ["const:4e4cac:8", "const:4:8"]]
+ 004e4cac ["CALL", null, ["callee:004e4d90:8"]]
- 004e4c6c bytes 39000094
+ 004e4cac bytes 39000094
- 004e4ca8 ["INT_ADD", "register:40f0:8", ["const:4e4ca8:8", "const:4:8"]]
- 004e4ca8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004e4ce8 ["INT_ADD", "register:40f0:8", ["const:4e4ce8:8", "const:4:8"]]
+ 004e4ce8 ["CALL", null, ["callee:00c57f80:8"]]
- 004e4ca8 bytes 82cc1d94
+ 004e4ce8 bytes a6cc1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810ea528d4b3205e938b4021dd173f37"></a>

### [`004e4d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md) → [`004e4d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4d90.md) FUN_004e4d90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e4bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59420.md)
- 新版 呼出元 1件 [`004e4c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4c2c.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c594f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md#insn-004e4da0) · [`004e4db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md#insn-004e4db4) · [`004e4dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md#insn-004e4dd0)
- 新版 [`004e4de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4d90.md#insn-004e4de0) · [`004e4df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4d90.md#insn-004e4df4) · [`004e4e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4d90.md#insn-004e4e10)

~~~diff
- 004e4da0 ["INT_ADD", "register:40f0:8", ["const:4e4da0:8", "const:4:8"]]
- 004e4da0 ["CALL", null, ["callee:00540dbc:8"]]
+ 004e4de0 ["INT_ADD", "register:40f0:8", ["const:4e4de0:8", "const:4:8"]]
+ 004e4de0 ["CALL", null, ["callee:00540dbc:8"]]
- 004e4da0 bytes f76f0194
+ 004e4de0 bytes f76f0194
- 004e4db4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e4db4 ["INT_ADD", "register:40f0:8", ["const:4e4db4:8", "const:4:8"]]
- 004e4db4 ["CALLIND", null, ["register:0:8"]]
+ 004e4df4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4df4 ["INT_ADD", "register:40f0:8", ["const:4e4df4:8", "const:4:8"]]
+ 004e4df4 ["CALLIND", null, ["register:0:8"]]
- 004e4db4 bytes 00013fd6
+ 004e4df4 bytes 00013fd6
- 004e4dd0 ["INT_ADD", "register:40f0:8", ["const:4e4dd0:8", "const:4:8"]]
- 004e4dd0 ["CALL", null, ["callee:00c594f0:8"]]
+ 004e4e10 ["INT_ADD", "register:40f0:8", ["const:4e4e10:8", "const:4:8"]]
+ 004e4e10 ["CALL", null, ["callee:00c594f0:8"]]
- 004e4dd0 bytes 94d11d94
+ 004e4e10 bytes b8d11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ec2c645743fa95f0cc75306afdc346"></a>

### [`004e4e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4e90.md) → [`004e4ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4ed0.md) _ZNK5Botan5PBKDF11pbkdf_timedEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmNS2_6chrono8durationIxNS2_5ratioIL

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4e90.md#insn-004e4eb0)
- 新版 [`004e4ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e4/004e4ed0.md#insn-004e4ef0)

~~~diff
- 004e4eb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e4eb0 ["INT_ADD", "register:40f0:8", ["const:4e4eb0:8", "const:4:8"]]
- 004e4eb0 ["CALLIND", null, ["register:0:8"]]
+ 004e4ef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4ef0 ["INT_ADD", "register:40f0:8", ["const:4e4ef0:8", "const:4:8"]]
+ 004e4ef0 ["CALLIND", null, ["register:0:8"]]
- 004e4eb0 bytes 00013fd6
+ 004e4ef0 bytes 00013fd6
~~~


<a id="compare-e782799b53f4e19fe83fe7c488a5cf75"></a>

### [`004e5068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5068.md) → [`004e50a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e5/004e50a8.md) _ZNK5Botan5PBKDF11pbkdf_timedEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmNS1_6chrono8durationIxNS1_5ratioILl1

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e50a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5068.md#insn-004e50a4) · [`004e50d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5068.md#insn-004e50d0)
- 新版 [`004e50e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e5/004e50a8.md#insn-004e50e4) · [`004e5110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e5/004e50a8.md#insn-004e5110)

~~~diff
- 004e50a4 ["INT_ADD", "register:40f0:8", ["const:4e50a4:8", "const:4:8"]]
- 004e50a4 ["CALL", null, ["callee:004b3548:8"]]
+ 004e50e4 ["INT_ADD", "register:40f0:8", ["const:4e50e4:8", "const:4:8"]]
+ 004e50e4 ["CALL", null, ["callee:004b3548:8"]]
- 004e50a4 bytes 1939ff97
+ 004e50e4 bytes 1939ff97
- 004e50d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e50d0 ["INT_ADD", "register:40f0:8", ["const:4e50d0:8", "const:4:8"]]
- 004e50d0 ["CALLIND", null, ["register:0:8"]]
+ 004e5110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e5110 ["INT_ADD", "register:40f0:8", ["const:4e5110:8", "const:4:8"]]
+ 004e5110 ["CALLIND", null, ["register:0:8"]]
- 004e50d0 bytes 00013fd6
+ 004e5110 bytes 00013fd6
~~~


<a id="compare-8a8a100dbdb96c92f1a620e5e6e922f0"></a>

### [`004e72b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e72b4.md) → [`004e72f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e72f4.md) _ZN5Botan13hash_for_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59540.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)
- 新版 呼出元 1件 [`00c59610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59610.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c60.md) [`00c58e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e72fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e72b4.md#insn-004e72fc) · [`004e7308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e72b4.md#insn-004e7308) · [`004e7318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e72b4.md#insn-004e7318)
- 新版 [`004e733c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e72f4.md#insn-004e733c) · [`004e7348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e72f4.md#insn-004e7348) · [`004e7358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e72f4.md#insn-004e7358)

~~~diff
- 004e72fc ["INT_ADD", "register:40f0:8", ["const:4e72fc:8", "const:4:8"]]
- 004e72fc ["CALL", null, ["callee:0043bb60:8"]]
+ 004e733c ["INT_ADD", "register:40f0:8", ["const:4e733c:8", "const:4:8"]]
+ 004e733c ["CALL", null, ["callee:0043bb60:8"]]
- 004e72fc bytes 0952fd97
+ 004e733c bytes 0952fd97
- 004e7308 ["INT_ADD", "register:40f0:8", ["const:4e7308:8", "const:4:8"]]
- 004e7308 ["CALL", null, ["callee:00c58e10:8"]]
+ 004e7348 ["INT_ADD", "register:40f0:8", ["const:4e7348:8", "const:4:8"]]
+ 004e7348 ["CALL", null, ["callee:00c58e10:8"]]
- 004e7308 bytes 8ec61d94
+ 004e7348 bytes b2c61d94
- 004e7318 ["INT_ADD", "register:40f0:8", ["const:4e7318:8", "const:4:8"]]
- 004e7318 ["CALL", null, ["callee:00c57f80:8"]]
+ 004e7358 ["INT_ADD", "register:40f0:8", ["const:4e7358:8", "const:4:8"]]
+ 004e7358 ["CALL", null, ["callee:00c57f80:8"]]
- 004e7318 bytes e6c21d94
+ 004e7358 bytes 0ac31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e373473b66fa3d80294f823c97f5ed6"></a>

### [`004e7494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md) → [`004e74d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e74d4.md) FUN_004e74d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054f430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005451d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md) [`00545474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0054f470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f470.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00545218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545218.md) [`005454b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005454b4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e74e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md#insn-004e74e4) · [`004e7514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md#insn-004e7514) · [`004e7530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md#insn-004e7530)
- 新版 [`004e7524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e74d4.md#insn-004e7524) · [`004e7554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e74d4.md#insn-004e7554) · [`004e7570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e74d4.md#insn-004e7570)

~~~diff
- 004e74e4 ["INT_ADD", "register:40f0:8", ["const:4e74e4:8", "const:4:8"]]
- 004e74e4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 004e7524 ["INT_ADD", "register:40f0:8", ["const:4e7524:8", "const:4:8"]]
+ 004e7524 ["CALL", null, ["callee:0043bbe4:8"]]
- 004e74e4 bytes b051fd97
+ 004e7524 bytes b051fd97
- 004e7514 ["INT_ADD", "register:40f0:8", ["const:4e7514:8", "const:4:8"]]
- 004e7514 ["CALL", null, ["callee:00545218:8"]]
+ 004e7554 ["INT_ADD", "register:40f0:8", ["const:4e7554:8", "const:4:8"]]
+ 004e7554 ["CALL", null, ["callee:00545218:8"]]
- 004e7514 bytes 31770194
+ 004e7554 bytes 31770194
- 004e7530 ["INT_ADD", "register:40f0:8", ["const:4e7530:8", "const:4:8"]]
- 004e7530 ["CALL", null, ["callee:005454b4:8"]]
+ 004e7570 ["INT_ADD", "register:40f0:8", ["const:4e7570:8", "const:4:8"]]
+ 004e7570 ["CALL", null, ["callee:005454b4:8"]]
- 004e7530 bytes d1770194
+ 004e7570 bytes d1770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaa988b5eaea8981c78edcad8637886c"></a>

### [`004e75b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e75b0.md) → [`004e75f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e75f0.md) FUN_004e75f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e75fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e75b0.md#insn-004e75fc) · [`004e760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e75b0.md#insn-004e760c)
- 新版 [`004e763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e75f0.md#insn-004e763c) · [`004e764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e7/004e75f0.md#insn-004e764c)

~~~diff
- 004e75fc ["INT_ADD", "register:40f0:8", ["const:4e75fc:8", "const:4:8"]]
- 004e75fc ["CALL", null, ["callee:00c57f80:8"]]
+ 004e763c ["INT_ADD", "register:40f0:8", ["const:4e763c:8", "const:4:8"]]
+ 004e763c ["CALL", null, ["callee:00c57f80:8"]]
- 004e75fc bytes 2dc21d94
+ 004e763c bytes 51c21d94
- 004e760c ["INT_ADD", "register:40f0:8", ["const:4e760c:8", "const:4:8"]]
- 004e760c ["CALL", null, ["callee:00c57f80:8"]]
+ 004e764c ["INT_ADD", "register:40f0:8", ["const:4e764c:8", "const:4:8"]]
+ 004e764c ["CALL", null, ["callee:00c57f80:8"]]
- 004e760c bytes 29c21d94
+ 004e764c bytes 4dc21d94
~~~


<a id="compare-832cfa090ef77afef1cdfe614b9f5acf"></a>

### [`004e8d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8d28.md) → [`004e8d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8d68.md) _ZN5Botan18create_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS_21RandomNumberGeneratorES8_S8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c587f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md) [`00c595b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c588c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588c0.md) [`00c59680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e8db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8d28.md#insn-004e8db8) · [`004e8dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8d28.md#insn-004e8dcc) · [`004e8de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8d28.md#insn-004e8de0)
- 新版 [`004e8df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8d68.md#insn-004e8df8) · [`004e8e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8d68.md#insn-004e8e0c) · [`004e8e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8d68.md#insn-004e8e20)

~~~diff
- 004e8db8 ["INT_ADD", "register:40f0:8", ["const:4e8db8:8", "const:4:8"]]
- 004e8db8 ["CALL", null, ["callee:00c588c0:8"]]
+ 004e8df8 ["INT_ADD", "register:40f0:8", ["const:4e8df8:8", "const:4:8"]]
+ 004e8df8 ["CALL", null, ["callee:00c588c0:8"]]
- 004e8db8 bytes 8ebe1d94
+ 004e8df8 bytes b2be1d94
- 004e8dcc ["INT_ADD", "register:40f0:8", ["const:4e8dcc:8", "const:4:8"]]
- 004e8dcc ["CALL", null, ["callee:00c57f60:8"]]
+ 004e8e0c ["INT_ADD", "register:40f0:8", ["const:4e8e0c:8", "const:4:8"]]
+ 004e8e0c ["CALL", null, ["callee:00c57f60:8"]]
- 004e8dcc bytes 31bc1d94
+ 004e8e0c bytes 55bc1d94
- 004e8de0 ["INT_ADD", "register:40f0:8", ["const:4e8de0:8", "const:4:8"]]
- 004e8de0 ["CALL", null, ["callee:00c59680:8"]]
+ 004e8e20 ["INT_ADD", "register:40f0:8", ["const:4e8e20:8", "const:4:8"]]
+ 004e8e20 ["CALL", null, ["callee:00c59680:8"]]
- 004e8de0 bytes f4c11d94
+ 004e8e20 bytes 18c21d94
~~~


<a id="compare-fb5c84810c4f85a36584786123a9313e"></a>

### [`004e9a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e9/004e9a28.md) → [`004e9a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e9/004e9a68.md) _ZN5Botan26probe_provider_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_6vectorIS6_NS4_IS6_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e9/004e9a28.md#insn-004e9acc) · [`004e9ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e9/004e9a28.md#insn-004e9ae0)
- 新版 [`004e9b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e9/004e9a68.md#insn-004e9b0c) · [`004e9b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e9/004e9a68.md#insn-004e9b20)

~~~diff
- 004e9acc ["INT_ADD", "register:40f0:8", ["const:4e9acc:8", "const:4:8"]]
- 004e9acc ["CALL", null, ["callee:0043bb60:8"]]
+ 004e9b0c ["INT_ADD", "register:40f0:8", ["const:4e9b0c:8", "const:4:8"]]
+ 004e9b0c ["CALL", null, ["callee:0043bb60:8"]]
- 004e9acc bytes 1548fd97
+ 004e9b0c bytes 1548fd97
- 004e9ae0 ["INT_ADD", "register:40f0:8", ["const:4e9ae0:8", "const:4:8"]]
- 004e9ae0 ["CALL", null, ["callee:00540dbc:8"]]
+ 004e9b20 ["INT_ADD", "register:40f0:8", ["const:4e9b20:8", "const:4:8"]]
+ 004e9b20 ["CALL", null, ["callee:00540dbc:8"]]
- 004e9ae0 bytes a75c0194
+ 004e9b20 bytes a75c0194
~~~


<a id="compare-4a1b2edaeec493f1698f8ee5b9fed284"></a>

### [`004ea010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea010.md) → [`004ea050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea050.md) _ZNK5Botan10Public_Key7get_oidEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ea044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea010.md#insn-004ea044) · [`004ea050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea010.md#insn-004ea050) · [`004ea060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea010.md#insn-004ea060)
- 新版 [`004ea084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea050.md#insn-004ea084) · [`004ea090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea050.md#insn-004ea090) · [`004ea0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea050.md#insn-004ea0a0)

~~~diff
- 004ea044 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea044 ["INT_ADD", "register:40f0:8", ["const:4ea044:8", "const:4:8"]]
- 004ea044 ["CALLIND", null, ["register:0:8"]]
+ 004ea084 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea084 ["INT_ADD", "register:40f0:8", ["const:4ea084:8", "const:4:8"]]
+ 004ea084 ["CALLIND", null, ["register:0:8"]]
- 004ea044 bytes 20013fd6
+ 004ea084 bytes 20013fd6
- 004ea050 ["INT_ADD", "register:40f0:8", ["const:4ea050:8", "const:4:8"]]
- 004ea050 ["CALL", null, ["callee:00c58750:8"]]
+ 004ea090 ["INT_ADD", "register:40f0:8", ["const:4ea090:8", "const:4:8"]]
+ 004ea090 ["CALL", null, ["callee:00c58750:8"]]
- 004ea050 bytes 8cb91d94
+ 004ea090 bytes b0b91d94
- 004ea060 ["INT_ADD", "register:40f0:8", ["const:4ea060:8", "const:4:8"]]
- 004ea060 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ea0a0 ["INT_ADD", "register:40f0:8", ["const:4ea0a0:8", "const:4:8"]]
+ 004ea0a0 ["CALL", null, ["callee:00c57f80:8"]]
- 004ea060 bytes 94b71d94
+ 004ea0a0 bytes b8b71d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b746a6e11169eb1e4deab785f6f751cb"></a>

### [`004ea4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea4f0.md) → [`004ea530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea530.md) _ZNK5Botan10Public_Key18fingerprint_publicERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c595c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595c0.md) [`00c595d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59690.md) [`00c596a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ea51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea4f0.md#insn-004ea51c) · [`004ea530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea4f0.md#insn-004ea530) · [`004ea540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea4f0.md#insn-004ea540)
- 新版 [`004ea55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea530.md#insn-004ea55c) · [`004ea570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea530.md#insn-004ea570) · [`004ea580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ea/004ea530.md#insn-004ea580)

~~~diff
- 004ea51c ["INT_ADD", "register:40f0:8", ["const:4ea51c:8", "const:4:8"]]
- 004ea51c ["CALL", null, ["callee:00c596a0:8"]]
+ 004ea55c ["INT_ADD", "register:40f0:8", ["const:4ea55c:8", "const:4:8"]]
+ 004ea55c ["CALL", null, ["callee:00c596a0:8"]]
- 004ea51c bytes 2dbc1d94
+ 004ea55c bytes 51bc1d94
- 004ea530 ["INT_ADD", "register:40f0:8", ["const:4ea530:8", "const:4:8"]]
- 004ea530 ["CALL", null, ["callee:00c59690:8"]]
+ 004ea570 ["INT_ADD", "register:40f0:8", ["const:4ea570:8", "const:4:8"]]
+ 004ea570 ["CALL", null, ["callee:00c59690:8"]]
- 004ea530 bytes 24bc1d94
+ 004ea570 bytes 48bc1d94
- 004ea540 ["INT_ADD", "register:40f0:8", ["const:4ea540:8", "const:4:8"]]
- 004ea540 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ea580 ["INT_ADD", "register:40f0:8", ["const:4ea580:8", "const:4:8"]]
+ 004ea580 ["CALL", null, ["callee:00c57f80:8"]]
- 004ea540 bytes 5cb61d94
+ 004ea580 bytes 80b61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b19a8aac8ed319bc826c5abe758e1c2f"></a>

### [`004ec258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec258.md) → [`004ec298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ec298.md) FUN_004ec298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005d37c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d37c8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec258.md#insn-004ec274)
- 新版 [`004ec2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ec298.md#insn-004ec2b4)

~~~diff
- 004ec274 ["INT_ADD", "register:40f0:8", ["const:4ec274:8", "const:4:8"]]
- 004ec274 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ec2b4 ["INT_ADD", "register:40f0:8", ["const:4ec2b4:8", "const:4:8"]]
+ 004ec2b4 ["CALL", null, ["callee:00c57f80:8"]]
- 004ec274 bytes 0faf1d94
+ 004ec2b4 bytes 33af1d94
~~~


<a id="compare-32c2b8425e03523cc4cc10c7ef5b9cda"></a>

### [`004ecbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md) → [`004ecc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecc24.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceENSt6__ndk18functionIFNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEvEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ecc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md#insn-004ecc28) · [`004ecc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md#insn-004ecc54) · [`004ecc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md#insn-004ecc6c)
- 新版 [`004ecc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecc24.md#insn-004ecc68) · [`004ecc94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecc24.md#insn-004ecc94) · [`004eccac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecc24.md#insn-004eccac)

~~~diff
- 004ecc28 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ecc28 ["INT_ADD", "register:40f0:8", ["const:4ecc28:8", "const:4:8"]]
- 004ecc28 ["CALLIND", null, ["register:0:8"]]
+ 004ecc68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecc68 ["INT_ADD", "register:40f0:8", ["const:4ecc68:8", "const:4:8"]]
+ 004ecc68 ["CALLIND", null, ["register:0:8"]]
- 004ecc28 bytes 00013fd6
+ 004ecc68 bytes 00013fd6
- 004ecc54 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ecc54 ["INT_ADD", "register:40f0:8", ["const:4ecc54:8", "const:4:8"]]
- 004ecc54 ["CALLIND", null, ["register:0:8"]]
+ 004ecc94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecc94 ["INT_ADD", "register:40f0:8", ["const:4ecc94:8", "const:4:8"]]
+ 004ecc94 ["CALLIND", null, ["register:0:8"]]
- 004ecc54 bytes 00013fd6
+ 004ecc94 bytes 00013fd6
- 004ecc6c ["INT_ADD", "register:40f0:8", ["const:4ecc6c:8", "const:4:8"]]
- 004ecc6c ["CALL", null, ["callee:004ecd50:8"]]
+ 004eccac ["INT_ADD", "register:40f0:8", ["const:4eccac:8", "const:4:8"]]
+ 004eccac ["CALL", null, ["callee:004ecd50:8"]]
- 004ecc6c bytes 29000094
+ 004eccac bytes 29000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8d402625578c5ee4b1c28ca2df1e53d"></a>

### [`004ee018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md) → [`004ee058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee058.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorENSt6__ndk18functionIFNS5_12basic_stringIcNS5_11char_traitsIcEENS5_9all

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md#insn-004ee054) · [`004ee074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md#insn-004ee074) · [`004ee0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md#insn-004ee0a4)
- 新版 [`004ee094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee058.md#insn-004ee094) · [`004ee0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee058.md#insn-004ee0b4) · [`004ee0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee058.md#insn-004ee0e4)

~~~diff
- 004ee054 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ee054 ["INT_ADD", "register:40f0:8", ["const:4ee054:8", "const:4:8"]]
- 004ee054 ["CALLIND", null, ["register:0:8"]]
+ 004ee094 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ee094 ["INT_ADD", "register:40f0:8", ["const:4ee094:8", "const:4:8"]]
+ 004ee094 ["CALLIND", null, ["register:0:8"]]
- 004ee054 bytes 20013fd6
+ 004ee094 bytes 20013fd6
- 004ee074 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee074 ["INT_ADD", "register:40f0:8", ["const:4ee074:8", "const:4:8"]]
- 004ee074 ["CALLIND", null, ["register:0:8"]]
+ 004ee0b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee0b4 ["INT_ADD", "register:40f0:8", ["const:4ee0b4:8", "const:4:8"]]
+ 004ee0b4 ["CALLIND", null, ["register:0:8"]]
- 004ee074 bytes 00013fd6
+ 004ee0b4 bytes 00013fd6
- 004ee0a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee0a4 ["INT_ADD", "register:40f0:8", ["const:4ee0a4:8", "const:4:8"]]
- 004ee0a4 ["CALLIND", null, ["register:0:8"]]
+ 004ee0e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee0e4 ["INT_ADD", "register:40f0:8", ["const:4ee0e4:8", "const:4:8"]]
+ 004ee0e4 ["CALLIND", null, ["register:0:8"]]
- 004ee0a4 bytes 00013fd6
+ 004ee0e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d9a861d4795850ccf66d0920cbabf7"></a>

### [`004ee204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee204.md) → [`004ee244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee244.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59630.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee204.md#insn-004ee228) · [`004ee250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee204.md#insn-004ee250)
- 新版 [`004ee268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee244.md#insn-004ee268) · [`004ee290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee244.md#insn-004ee290)

~~~diff
- 004ee228 ["INT_ADD", "register:40f0:8", ["const:4ee228:8", "const:4:8"]]
- 004ee228 ["CALL", null, ["callee:00c59700:8"]]
+ 004ee268 ["INT_ADD", "register:40f0:8", ["const:4ee268:8", "const:4:8"]]
+ 004ee268 ["CALL", null, ["callee:00c59700:8"]]
- 004ee228 bytes 02ad1d94
+ 004ee268 bytes 26ad1d94
- 004ee250 ["INT_ADD", "register:40f0:8", ["const:4ee250:8", "const:4:8"]]
- 004ee250 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004ee290 ["INT_ADD", "register:40f0:8", ["const:4ee290:8", "const:4:8"]]
+ 004ee290 ["CALL", null, ["callee:00c57fb0:8"]]
- 004ee250 bytes 24a71d94
+ 004ee290 bytes 48a71d94
~~~


<a id="compare-385db38575a5d2ef66b1a15dc27781f5"></a>

### [`004ee334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee334.md) → [`004ee374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee374.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorENS1_8functionIFS7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee334.md#insn-004ee360) · [`004ee37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee334.md#insn-004ee37c) · [`004ee3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee334.md#insn-004ee3ac)
- 新版 [`004ee3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee374.md#insn-004ee3a0) · [`004ee3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee374.md#insn-004ee3bc) · [`004ee3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee374.md#insn-004ee3ec)

~~~diff
- 004ee360 ["INT_ADD", "register:40f0:8", ["const:4ee360:8", "const:4:8"]]
- 004ee360 ["CALL", null, ["callee:00c59730:8"]]
+ 004ee3a0 ["INT_ADD", "register:40f0:8", ["const:4ee3a0:8", "const:4:8"]]
+ 004ee3a0 ["CALL", null, ["callee:00c59730:8"]]
- 004ee360 bytes c0ac1d94
+ 004ee3a0 bytes e4ac1d94
- 004ee37c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee37c ["INT_ADD", "register:40f0:8", ["const:4ee37c:8", "const:4:8"]]
- 004ee37c ["CALLIND", null, ["register:0:8"]]
+ 004ee3bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee3bc ["INT_ADD", "register:40f0:8", ["const:4ee3bc:8", "const:4:8"]]
+ 004ee3bc ["CALLIND", null, ["register:0:8"]]
- 004ee37c bytes 00013fd6
+ 004ee3bc bytes 00013fd6
- 004ee3ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee3ac ["INT_ADD", "register:40f0:8", ["const:4ee3ac:8", "const:4:8"]]
- 004ee3ac ["CALLIND", null, ["register:0:8"]]
+ 004ee3ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee3ec ["INT_ADD", "register:40f0:8", ["const:4ee3ec:8", "const:4:8"]]
+ 004ee3ec ["CALLIND", null, ["register:0:8"]]
- 004ee3ac bytes 00013fd6
+ 004ee3ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73253025aeb145748003c6e2ce26be3a"></a>

### [`004ee848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee848.md) → [`004ee888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee888.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee848.md#insn-004ee868) · [`004ee890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee848.md#insn-004ee890)
- 新版 [`004ee8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee888.md#insn-004ee8a8) · [`004ee8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee888.md#insn-004ee8d0)

~~~diff
- 004ee868 ["INT_ADD", "register:40f0:8", ["const:4ee868:8", "const:4:8"]]
- 004ee868 ["CALL", null, ["callee:00c59720:8"]]
+ 004ee8a8 ["INT_ADD", "register:40f0:8", ["const:4ee8a8:8", "const:4:8"]]
+ 004ee8a8 ["CALL", null, ["callee:00c59720:8"]]
- 004ee868 bytes 7aab1d94
+ 004ee8a8 bytes 9eab1d94
- 004ee890 ["INT_ADD", "register:40f0:8", ["const:4ee890:8", "const:4:8"]]
- 004ee890 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004ee8d0 ["INT_ADD", "register:40f0:8", ["const:4ee8d0:8", "const:4:8"]]
+ 004ee8d0 ["CALL", null, ["callee:00c57fb0:8"]]
- 004ee890 bytes 94a51d94
+ 004ee8d0 bytes b8a51d94
~~~


<a id="compare-1663bcc2b0e20faa6b3a2fe8d0721380"></a>

### [`004eef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eef3c.md) → [`004eef7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004eef7c.md) _ZN5Botan16PK_Encryptor_EMED0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c592e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c592e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eef4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eef3c.md#insn-004eef4c)
- 新版 [`004eef8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004eef7c.md#insn-004eef8c)

~~~diff
- 004eef4c ["INT_ADD", "register:40f0:8", ["const:4eef4c:8", "const:4:8"]]
- 004eef4c ["CALL", null, ["callee:00c592e0:8"]]
+ 004eef8c ["INT_ADD", "register:40f0:8", ["const:4eef8c:8", "const:4:8"]]
+ 004eef8c ["CALL", null, ["callee:00c592e0:8"]]
- 004eef4c bytes b1a81d94
+ 004eef8c bytes d5a81d94
~~~


<a id="compare-dd7bb181a24b967221dde737cb0c25c8"></a>

### [`004ef300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef300.md) → [`004ef340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ef/004ef340.md) _ZN5Botan16PK_Decryptor_EMED0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c592d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c592d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef300.md#insn-004ef310)
- 新版 [`004ef350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ef/004ef340.md#insn-004ef350)

~~~diff
- 004ef310 ["INT_ADD", "register:40f0:8", ["const:4ef310:8", "const:4:8"]]
- 004ef310 ["CALL", null, ["callee:00c592d0:8"]]
+ 004ef350 ["INT_ADD", "register:40f0:8", ["const:4ef350:8", "const:4:8"]]
+ 004ef350 ["CALL", null, ["callee:00c592d0:8"]]
- 004ef310 bytes bca71d94
+ 004ef350 bytes e0a71d94
~~~


<a id="compare-65cf8ae473a669e9d2d9e351be000887"></a>

### [`004efa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efa54.md) → [`004efa94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ef/004efa94.md) _ZN5Botan16PK_Key_AgreementaSEOS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004efa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efa54.md#insn-004efa8c)
- 新版 [`004efacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ef/004efa94.md#insn-004efacc)

~~~diff
- 004efa8c ["COPY", "register:0:8", ["register:4048:8"]]
- 004efa8c ["INT_ADD", "register:40f0:8", ["const:4efa8c:8", "const:4:8"]]
- 004efa8c ["CALLIND", null, ["register:0:8"]]
+ 004efacc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004efacc ["INT_ADD", "register:40f0:8", ["const:4efacc:8", "const:4:8"]]
+ 004efacc ["CALLIND", null, ["register:0:8"]]
- 004efa8c bytes 20013fd6
+ 004efacc bytes 20013fd6
~~~


<a id="compare-187c911d1be61a40e701cc5602c3e7b8"></a>

### [`004f06ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f06ec.md) → [`004f072c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f072c.md) _ZN5Botan11PK_Verifier14verify_messageEPKhmS2_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c596a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596a0.md) · 呼出先 1件 [`00c59260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59260.md)
- 新版 呼出元 1件 [`00c59770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59770.md) · 呼出先 1件 [`00c59330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f0714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f06ec.md#insn-004f0714)
- 新版 [`004f0754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f072c.md#insn-004f0754)

~~~diff
- 004f0714 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f0714 ["INT_ADD", "register:40f0:8", ["const:4f0714:8", "const:4:8"]]
- 004f0714 ["CALLIND", null, ["register:0:8"]]
+ 004f0754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f0754 ["INT_ADD", "register:40f0:8", ["const:4f0754:8", "const:4:8"]]
+ 004f0754 ["CALLIND", null, ["register:0:8"]]
- 004f0714 bytes 00013fd6
+ 004f0754 bytes 00013fd6
~~~


<a id="compare-00a130141e2d2684c79f40e0f513a63c"></a>

### [`004f0b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md) → [`004f0bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0bc0.md) FUN_004f0bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f0744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`004f0784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0784.md) · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f0bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md#insn-004f0bf8) · [`004f0c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md#insn-004f0c14) · [`004f0c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md#insn-004f0c24)
- 新版 [`004f0c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0bc0.md#insn-004f0c38) · [`004f0c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0bc0.md#insn-004f0c54) · [`004f0c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0bc0.md#insn-004f0c64)

~~~diff
- 004f0bf8 ["INT_ADD", "register:40f0:8", ["const:4f0bf8:8", "const:4:8"]]
- 004f0bf8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004f0c38 ["INT_ADD", "register:40f0:8", ["const:4f0c38:8", "const:4:8"]]
+ 004f0c38 ["CALL", null, ["callee:00c57f60:8"]]
- 004f0bf8 bytes a69c1d94
+ 004f0c38 bytes ca9c1d94
- 004f0c14 ["INT_ADD", "register:40f0:8", ["const:4f0c14:8", "const:4:8"]]
- 004f0c14 ["CALL", null, ["callee:00c58160:8"]]
+ 004f0c54 ["INT_ADD", "register:40f0:8", ["const:4f0c54:8", "const:4:8"]]
+ 004f0c54 ["CALL", null, ["callee:00c58160:8"]]
- 004f0c14 bytes 1f9d1d94
+ 004f0c54 bytes 439d1d94
- 004f0c24 ["INT_ADD", "register:40f0:8", ["const:4f0c24:8", "const:4:8"]]
- 004f0c24 ["CALL", null, ["callee:00c580d0:8"]]
+ 004f0c64 ["INT_ADD", "register:40f0:8", ["const:4f0c64:8", "const:4:8"]]
+ 004f0c64 ["CALL", null, ["callee:00c580d0:8"]]
- 004f0c24 bytes f79c1d94
+ 004f0c64 bytes 1b9d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b27cd9b140bd934794ff48588914b561"></a>

### [`004f1548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1548.md) → [`004f1588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1588.md) _ZN5Botan4X5098load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md) [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md) [`00c597a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1548.md#insn-004f1570) · [`004f1578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1548.md#insn-004f1578) · [`004f1584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1548.md#insn-004f1584)
- 新版 [`004f15b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1588.md#insn-004f15b0) · [`004f15b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1588.md#insn-004f15b8) · [`004f15c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1588.md#insn-004f15c4)

~~~diff
- 004f1570 ["INT_ADD", "register:40f0:8", ["const:4f1570:8", "const:4:8"]]
- 004f1570 ["CALL", null, ["callee:00c59730:8"]]
+ 004f15b0 ["INT_ADD", "register:40f0:8", ["const:4f15b0:8", "const:4:8"]]
+ 004f15b0 ["CALL", null, ["callee:00c59730:8"]]
- 004f1570 bytes 3ca01d94
+ 004f15b0 bytes 60a01d94
- 004f1578 ["INT_ADD", "register:40f0:8", ["const:4f1578:8", "const:4:8"]]
- 004f1578 ["CALL", null, ["callee:00c597a0:8"]]
+ 004f15b8 ["INT_ADD", "register:40f0:8", ["const:4f15b8:8", "const:4:8"]]
+ 004f15b8 ["CALL", null, ["callee:00c597a0:8"]]
- 004f1578 bytes 56a01d94
+ 004f15b8 bytes 7aa01d94
- 004f1584 ["INT_ADD", "register:40f0:8", ["const:4f1584:8", "const:4:8"]]
- 004f1584 ["CALL", null, ["callee:00c59740:8"]]
+ 004f15c4 ["INT_ADD", "register:40f0:8", ["const:4f15c4:8", "const:4:8"]]
+ 004f15c4 ["CALL", null, ["callee:00c59740:8"]]
- 004f1584 bytes 3ba01d94
+ 004f15c4 bytes 5fa01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d783403710da4555d2851ace5161fa3c"></a>

### [`004f179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f179c.md) → [`004f17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f17dc.md) _ZN5Botan21RandomNumberGenerator23randomize_with_ts_inputEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md) [`00c59710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59710.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md) [`00c597e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f17d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f179c.md#insn-004f17d0) · [`004f17d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f179c.md#insn-004f17d8) · [`004f17fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f179c.md#insn-004f17fc)
- 新版 [`004f1810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f17dc.md#insn-004f1810) · [`004f1818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f17dc.md#insn-004f1818) · [`004f183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f17dc.md#insn-004f183c)

~~~diff
- 004f17d0 ["INT_ADD", "register:40f0:8", ["const:4f17d0:8", "const:4:8"]]
- 004f17d0 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f1810 ["INT_ADD", "register:40f0:8", ["const:4f1810:8", "const:4:8"]]
+ 004f1810 ["CALL", null, ["callee:00c597d0:8"]]
- 004f17d0 bytes cc9f1d94
+ 004f1810 bytes f09f1d94
- 004f17d8 ["INT_ADD", "register:40f0:8", ["const:4f17d8:8", "const:4:8"]]
- 004f17d8 ["CALL", null, ["callee:00c58650:8"]]
+ 004f1818 ["INT_ADD", "register:40f0:8", ["const:4f1818:8", "const:4:8"]]
+ 004f1818 ["CALL", null, ["callee:00c58650:8"]]
- 004f17d8 bytes 6a9b1d94
+ 004f1818 bytes 8e9b1d94
- 004f17fc ["INT_ADD", "register:40f0:8", ["const:4f17fc:8", "const:4:8"]]
- 004f17fc ["CALL", null, ["callee:00c597e0:8"]]
+ 004f183c ["INT_ADD", "register:40f0:8", ["const:4f183c:8", "const:4:8"]]
+ 004f183c ["CALL", null, ["callee:00c597e0:8"]]
- 004f17fc bytes c59f1d94
+ 004f183c bytes e99f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f21ea79cdd2b68dc8d50e267ca2bd3"></a>

### [`004f184c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f184c.md) → [`004f188c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f188c.md) _ZN5Botan2OS23get_system_timestamp_nsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f184c.md#insn-004f1870) · [`004f1878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f184c.md#insn-004f1878) · [`004f18b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f184c.md#insn-004f18b8)
- 新版 [`004f18b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f188c.md#insn-004f18b0) · [`004f18b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f188c.md#insn-004f18b8) · [`004f18f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f188c.md#insn-004f18f8)

~~~diff
- 004f1870 ["INT_ADD", "register:40f0:8", ["const:4f1870:8", "const:4:8"]]
- 004f1870 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f18b0 ["INT_ADD", "register:40f0:8", ["const:4f18b0:8", "const:4:8"]]
+ 004f18b0 ["CALL", null, ["callee:00c597d0:8"]]
- 004f1870 bytes a49f1d94
+ 004f18b0 bytes c89f1d94
- 004f1878 ["INT_ADD", "register:40f0:8", ["const:4f1878:8", "const:4:8"]]
- 004f1878 ["CALL", null, ["callee:00c58650:8"]]
+ 004f18b8 ["INT_ADD", "register:40f0:8", ["const:4f18b8:8", "const:4:8"]]
+ 004f18b8 ["CALL", null, ["callee:00c58650:8"]]
- 004f1878 bytes 429b1d94
+ 004f18b8 bytes 669b1d94
- 004f18b8 ["INT_ADD", "register:40f0:8", ["const:4f18b8:8", "const:4:8"]]
- 004f18b8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004f18f8 ["INT_ADD", "register:40f0:8", ["const:4f18f8:8", "const:4:8"]]
+ 004f18f8 ["CALL", null, ["callee:00c57fb0:8"]]
- 004f18b8 bytes 8a991d94
+ 004f18f8 bytes ae991d94
~~~


<a id="compare-a27e6dd8926982093ddb1356e73e04bb"></a>

### [`004f18bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f18bc.md) → [`004f18fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f18fc.md) _ZN5Botan2OS25get_high_resolution_clockEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59710.md) · 呼出先 3件 [`00c57ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ec0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)
- 新版 呼出元 1件 [`00c597e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597e0.md) · 呼出先 3件 [`00c57f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f90.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f18e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f18bc.md#insn-004f18e0) · [`004f18f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f18bc.md#insn-004f18f0) · [`004f1900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f18bc.md#insn-004f1900)
- 新版 [`004f1920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f18fc.md#insn-004f1920) · [`004f1930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f18fc.md#insn-004f1930) · [`004f1940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f18fc.md#insn-004f1940)

~~~diff
- 004f18e0 ["INT_ADD", "register:40f0:8", ["const:4f18e0:8", "const:4:8"]]
- 004f18e0 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f1920 ["INT_ADD", "register:40f0:8", ["const:4f1920:8", "const:4:8"]]
+ 004f1920 ["CALL", null, ["callee:00c597d0:8"]]
- 004f18e0 bytes 889f1d94
+ 004f1920 bytes ac9f1d94
- 004f18f0 ["INT_ADD", "register:40f0:8", ["const:4f18f0:8", "const:4:8"]]
- 004f18f0 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f1930 ["INT_ADD", "register:40f0:8", ["const:4f1930:8", "const:4:8"]]
+ 004f1930 ["CALL", null, ["callee:00c597d0:8"]]
- 004f18f0 bytes 849f1d94
+ 004f1930 bytes a89f1d94
- 004f1900 ["INT_ADD", "register:40f0:8", ["const:4f1900:8", "const:4:8"]]
- 004f1900 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f1940 ["INT_ADD", "register:40f0:8", ["const:4f1940:8", "const:4:8"]]
+ 004f1940 ["CALL", null, ["callee:00c597d0:8"]]
- 004f1900 bytes 809f1d94
+ 004f1940 bytes a49f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9eba86ee8467dd9b62be55a019201d"></a>

### [`004f195c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f195c.md) → [`004f199c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f199c.md) _ZN5Botan21RandomNumberGenerator20randomize_with_inputEPhmPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f195c.md#insn-004f1988)
- 新版 [`004f19c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f199c.md#insn-004f19c8)

~~~diff
- 004f1988 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f1988 ["INT_ADD", "register:40f0:8", ["const:4f1988:8", "const:4:8"]]
- 004f1988 ["CALLIND", null, ["register:0:8"]]
+ 004f19c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f19c8 ["INT_ADD", "register:40f0:8", ["const:4f19c8:8", "const:4:8"]]
+ 004f19c8 ["CALLIND", null, ["register:0:8"]]
- 004f1988 bytes 00013fd6
+ 004f19c8 bytes 00013fd6
~~~


<a id="compare-2bfa5cef860b0c0c938f780899807491"></a>

### [`004f19b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f19b0.md) → [`004f19f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f19f0.md) _ZN5Botan21RandomNumberGenerator6reseedERNS_15Entropy_SourcesEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f19d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f19b0.md#insn-004f19d4) · [`004f1a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f19b0.md#insn-004f1a04) · [`004f1a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f19b0.md#insn-004f1a14)
- 新版 [`004f1a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f19f0.md#insn-004f1a14) · [`004f1a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f19f0.md#insn-004f1a44) · [`004f1a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f19f0.md#insn-004f1a54)

~~~diff
- 004f19d4 ["INT_ADD", "register:40f0:8", ["const:4f19d4:8", "const:4:8"]]
- 004f19d4 ["CALL", null, ["callee:00c58650:8"]]
+ 004f1a14 ["INT_ADD", "register:40f0:8", ["const:4f1a14:8", "const:4:8"]]
+ 004f1a14 ["CALL", null, ["callee:00c58650:8"]]
- 004f19d4 bytes eb9a1d94
+ 004f1a14 bytes 0f9b1d94
- 004f1a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f1a04 ["INT_ADD", "register:40f0:8", ["const:4f1a04:8", "const:4:8"]]
- 004f1a04 ["CALLIND", null, ["register:0:8"]]
+ 004f1a44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1a44 ["INT_ADD", "register:40f0:8", ["const:4f1a44:8", "const:4:8"]]
+ 004f1a44 ["CALLIND", null, ["register:0:8"]]
- 004f1a04 bytes 00013fd6
+ 004f1a44 bytes 00013fd6
- 004f1a14 ["INT_ADD", "register:40f0:8", ["const:4f1a14:8", "const:4:8"]]
- 004f1a14 ["CALL", null, ["callee:00c58650:8"]]
+ 004f1a54 ["INT_ADD", "register:40f0:8", ["const:4f1a54:8", "const:4:8"]]
+ 004f1a54 ["CALL", null, ["callee:00c58650:8"]]
- 004f1a14 bytes db9a1d94
+ 004f1a54 bytes ff9a1d94
~~~


<a id="compare-127391d396022f96dca32e328fdf036e"></a>

### [`004f1f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1f44.md) → [`004f1f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1f84.md) _ZNK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c597f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1f44.md#insn-004f1f7c) · [`004f1f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1f44.md#insn-004f1f8c) · [`004f1f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1f44.md#insn-004f1f9c)
- 新版 [`004f1fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1f84.md#insn-004f1fbc) · [`004f1fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1f84.md#insn-004f1fcc) · [`004f1fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1f84.md#insn-004f1fdc)

~~~diff
- 004f1f7c ["COPY", "register:0:8", ["register:4050:8"]]
- 004f1f7c ["INT_ADD", "register:40f0:8", ["const:4f1f7c:8", "const:4:8"]]
- 004f1f7c ["CALLIND", null, ["register:0:8"]]
+ 004f1fbc ["COPY", "register:0:8", ["register:4050:8"]]
+ 004f1fbc ["INT_ADD", "register:40f0:8", ["const:4f1fbc:8", "const:4:8"]]
+ 004f1fbc ["CALLIND", null, ["register:0:8"]]
- 004f1f7c bytes 40013fd6
+ 004f1fbc bytes 40013fd6
- 004f1f8c ["INT_ADD", "register:40f0:8", ["const:4f1f8c:8", "const:4:8"]]
- 004f1f8c ["CALL", null, ["callee:00c597f0:8"]]
+ 004f1fcc ["INT_ADD", "register:40f0:8", ["const:4f1fcc:8", "const:4:8"]]
+ 004f1fcc ["CALL", null, ["callee:00c597f0:8"]]
- 004f1f8c bytes e59d1d94
+ 004f1fcc bytes 099e1d94
- 004f1f9c ["INT_ADD", "register:40f0:8", ["const:4f1f9c:8", "const:4:8"]]
- 004f1f9c ["CALL", null, ["callee:00c57f80:8"]]
+ 004f1fdc ["INT_ADD", "register:40f0:8", ["const:4f1fdc:8", "const:4:8"]]
+ 004f1fdc ["CALL", null, ["callee:00c57f80:8"]]
- 004f1f9c bytes c5971d94
+ 004f1fdc bytes e9971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c747f7957639960ba7a4ec05dcc3f1da"></a>

### [`004f1ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ff4.md) → [`004f2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f2/004f2034.md) _ZTv0_n72_NK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c597f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f2038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ff4.md#insn-004f2038) · [`004f2048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ff4.md#insn-004f2048) · [`004f2058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ff4.md#insn-004f2058)
- 新版 [`004f2078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f2/004f2034.md#insn-004f2078) · [`004f2088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f2/004f2034.md#insn-004f2088) · [`004f2098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f2/004f2034.md#insn-004f2098)

~~~diff
- 004f2038 ["COPY", "register:0:8", ["register:4058:8"]]
- 004f2038 ["INT_ADD", "register:40f0:8", ["const:4f2038:8", "const:4:8"]]
- 004f2038 ["CALLIND", null, ["register:0:8"]]
+ 004f2078 ["COPY", "register:0:8", ["register:4058:8"]]
+ 004f2078 ["INT_ADD", "register:40f0:8", ["const:4f2078:8", "const:4:8"]]
+ 004f2078 ["CALLIND", null, ["register:0:8"]]
- 004f2038 bytes 60013fd6
+ 004f2078 bytes 60013fd6
- 004f2048 ["INT_ADD", "register:40f0:8", ["const:4f2048:8", "const:4:8"]]
- 004f2048 ["CALL", null, ["callee:00c597f0:8"]]
+ 004f2088 ["INT_ADD", "register:40f0:8", ["const:4f2088:8", "const:4:8"]]
+ 004f2088 ["CALL", null, ["callee:00c597f0:8"]]
- 004f2048 bytes b69d1d94
+ 004f2088 bytes da9d1d94
- 004f2058 ["INT_ADD", "register:40f0:8", ["const:4f2058:8", "const:4:8"]]
- 004f2058 ["CALL", null, ["callee:00c57f80:8"]]
+ 004f2098 ["INT_ADD", "register:40f0:8", ["const:4f2098:8", "const:4:8"]]
+ 004f2098 ["CALL", null, ["callee:00c57f80:8"]]
- 004f2058 bytes 96971d94
+ 004f2098 bytes ba971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce19b6db2c924c13ba5511447ffe2233"></a>

### [`004f5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5208.md) → [`004f5248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5248.md) _ZTv0_n104_NK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9a

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59760.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f521c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5208.md#insn-004f521c)
- 新版 [`004f525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5248.md#insn-004f525c)

~~~diff
- 004f521c ["INT_ADD", "register:40f0:8", ["const:4f521c:8", "const:4:8"]]
- 004f521c ["CALL", null, ["callee:00c59830:8"]]
+ 004f525c ["INT_ADD", "register:40f0:8", ["const:4f525c:8", "const:4:8"]]
+ 004f525c ["CALL", null, ["callee:00c59830:8"]]
- 004f521c bytes 51911d94
+ 004f525c bytes 75911d94
~~~


<a id="compare-cb26ceebcd55647f18a8ff8044b3a361"></a>

### [`004f5b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5b48.md) → [`004f5b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5b88.md) _ZN5Botan7SHA_16010compress_nEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f5ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5b48.md#insn-004f5ba8)
- 新版 [`004f5be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5b88.md#insn-004f5be8)

~~~diff
- 004f5ba8 ["INT_ADD", "register:40f0:8", ["const:4f5ba8:8", "const:4:8"]]
- 004f5ba8 ["CALL", null, ["callee:00540960:8"]]
+ 004f5be8 ["INT_ADD", "register:40f0:8", ["const:4f5be8:8", "const:4:8"]]
+ 004f5be8 ["CALL", null, ["callee:00540960:8"]]
- 004f5ba8 bytes 5e2b0194
+ 004f5be8 bytes 5e2b0194
~~~


<a id="compare-29f9d02f339df186b244e2e9f061a689"></a>

### [`004f8b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md) → [`004f8b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8b48.md) _ZN5Botan12StreamCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004f8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004f8cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8cac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md#insn-004f8b78) · [`004f8b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md#insn-004f8b88) · [`004f8bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md#insn-004f8bc4)
- 新版 [`004f8bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8b48.md#insn-004f8bb8) · [`004f8bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8b48.md#insn-004f8bc8) · [`004f8c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8b48.md#insn-004f8c04)

~~~diff
- 004f8b78 ["INT_ADD", "register:40f0:8", ["const:4f8b78:8", "const:4:8"]]
- 004f8b78 ["CALL", null, ["callee:00473580:8"]]
+ 004f8bb8 ["INT_ADD", "register:40f0:8", ["const:4f8bb8:8", "const:4:8"]]
+ 004f8bb8 ["CALL", null, ["callee:00473580:8"]]
- 004f8b78 bytes 72eafd97
+ 004f8bb8 bytes 72eafd97
- 004f8b88 ["INT_ADD", "register:40f0:8", ["const:4f8b88:8", "const:4:8"]]
- 004f8b88 ["CALL", null, ["callee:004f8cac:8"]]
+ 004f8bc8 ["INT_ADD", "register:40f0:8", ["const:4f8bc8:8", "const:4:8"]]
+ 004f8bc8 ["CALL", null, ["callee:004f8cac:8"]]
- 004f8b88 bytes 39000094
+ 004f8bc8 bytes 39000094
- 004f8bc4 ["INT_ADD", "register:40f0:8", ["const:4f8bc4:8", "const:4:8"]]
- 004f8bc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004f8c04 ["INT_ADD", "register:40f0:8", ["const:4f8c04:8", "const:4:8"]]
+ 004f8c04 ["CALL", null, ["callee:00c57f80:8"]]
- 004f8bc4 bytes bb7c1d94
+ 004f8c04 bytes df7c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ee9597ea9842e0d86d9aa584421649"></a>

### [`004f8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md) → [`004f8cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8cac.md) FUN_004f8cac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f8b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e60.md)
- 新版 呼出元 1件 [`004f8b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8b48.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md#insn-004f8cbc) · [`004f8cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md#insn-004f8cd0) · [`004f8ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md#insn-004f8ce8)
- 新版 [`004f8cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8cac.md#insn-004f8cfc) · [`004f8d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8cac.md#insn-004f8d10) · [`004f8d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8cac.md#insn-004f8d28)

~~~diff
- 004f8cbc ["INT_ADD", "register:40f0:8", ["const:4f8cbc:8", "const:4:8"]]
- 004f8cbc ["CALL", null, ["callee:00540dbc:8"]]
+ 004f8cfc ["INT_ADD", "register:40f0:8", ["const:4f8cfc:8", "const:4:8"]]
+ 004f8cfc ["CALL", null, ["callee:00540dbc:8"]]
- 004f8cbc bytes 30200194
+ 004f8cfc bytes 30200194
- 004f8cd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f8cd0 ["INT_ADD", "register:40f0:8", ["const:4f8cd0:8", "const:4:8"]]
- 004f8cd0 ["CALLIND", null, ["register:0:8"]]
+ 004f8d10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f8d10 ["INT_ADD", "register:40f0:8", ["const:4f8d10:8", "const:4:8"]]
+ 004f8d10 ["CALLIND", null, ["register:0:8"]]
- 004f8cd0 bytes 00013fd6
+ 004f8d10 bytes 00013fd6
- 004f8ce8 ["INT_ADD", "register:40f0:8", ["const:4f8ce8:8", "const:4:8"]]
- 004f8ce8 ["CALL", null, ["callee:00c58f30:8"]]
+ 004f8d28 ["INT_ADD", "register:40f0:8", ["const:4f8d28:8", "const:4:8"]]
+ 004f8d28 ["CALL", null, ["callee:00c58f30:8"]]
- 004f8ce8 bytes 5e801d94
+ 004f8d28 bytes 82801d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9955995dbf753ea0e9b76cd14be2b15"></a>

### [`004f8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md) → [`004f8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8fac.md) FUN_004f8fac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004f8da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md) [`00535f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md) · 呼出先 1件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md)
- 新版 呼出元 2件 [`004f8de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8de8.md) [`00535fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md) · 呼出先 1件 [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md#insn-004f8f80)
- 新版 [`004f8fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8fac.md#insn-004f8fc0)

~~~diff
- 004f8f80 ["INT_ADD", "register:40f0:8", ["const:4f8f80:8", "const:4:8"]]
- 004f8f80 ["CALL", null, ["callee:00c598a0:8"]]
+ 004f8fc0 ["INT_ADD", "register:40f0:8", ["const:4f8fc0:8", "const:4:8"]]
+ 004f8fc0 ["CALL", null, ["callee:00c598a0:8"]]
- 004f8f80 bytes 14821d94
+ 004f8fc0 bytes 38821d94
~~~


<a id="compare-c241854cc64e8347a308c872d226183e"></a>

### [`004f9984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9984.md) → [`004f99c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f99c4.md) _ZN5Botan10DataSource12discard_nextEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f99e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9984.md#insn-004f99e0) · [`004f9a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9984.md#insn-004f9a1c)
- 新版 [`004f9a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f99c4.md#insn-004f9a20) · [`004f9a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f99c4.md#insn-004f9a5c)

~~~diff
- 004f99e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f99e0 ["INT_ADD", "register:40f0:8", ["const:4f99e0:8", "const:4:8"]]
- 004f99e0 ["CALLIND", null, ["register:0:8"]]
+ 004f9a20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f9a20 ["INT_ADD", "register:40f0:8", ["const:4f9a20:8", "const:4:8"]]
+ 004f9a20 ["CALLIND", null, ["register:0:8"]]
- 004f99e0 bytes 00013fd6
+ 004f9a20 bytes 00013fd6
- 004f9a1c ["INT_ADD", "register:40f0:8", ["const:4f9a1c:8", "const:4:8"]]
- 004f9a1c ["CALL", null, ["callee:00c57fb0:8"]]
+ 004f9a5c ["INT_ADD", "register:40f0:8", ["const:4f9a5c:8", "const:4:8"]]
+ 004f9a5c ["CALL", null, ["callee:00c57fb0:8"]]
- 004f9a1c bytes 31791d94
+ 004f9a5c bytes 55791d94
~~~


<a id="compare-5a9661f7fcc1796cbb77c59bd95729a2"></a>

### [`004f9a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md) → [`004f9a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9a60.md) _ZN5Botan17DataSource_Memory4readEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md#insn-004f9a58)
- 新版 [`004f9a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9a60.md#insn-004f9a98)

~~~diff
- 004f9a58 ["INT_ADD", "register:40f0:8", ["const:4f9a58:8", "const:4:8"]]
- 004f9a58 ["CALL", null, ["callee:00c58010:8"]]
+ 004f9a98 ["INT_ADD", "register:40f0:8", ["const:4f9a98:8", "const:4:8"]]
+ 004f9a98 ["CALL", null, ["callee:00c58010:8"]]
- 004f9a58 bytes 3a791d94
+ 004f9a98 bytes 5e791d94
~~~


<a id="compare-bb059cdd3c80812a0e60f413b1a1979d"></a>

### [`004f9a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a94.md) → [`004f9ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ad4.md) _ZNK5Botan17DataSource_Memory4peekEPhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a94.md#insn-004f9ad4)
- 新版 [`004f9b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ad4.md#insn-004f9b14)

~~~diff
- 004f9ad4 ["INT_ADD", "register:40f0:8", ["const:4f9ad4:8", "const:4:8"]]
- 004f9ad4 ["CALL", null, ["callee:00c58010:8"]]
+ 004f9b14 ["INT_ADD", "register:40f0:8", ["const:4f9b14:8", "const:4:8"]]
+ 004f9b14 ["CALL", null, ["callee:00c58010:8"]]
- 004f9ad4 bytes 1b791d94
+ 004f9b14 bytes 3f791d94
~~~


<a id="compare-c8e7701cffaef2b0382a459a875ddb39"></a>

### [`004f9c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9c8c.md) → [`004f9ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ccc.md) _ZN5Botan17DataSource_Stream15check_availableEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c597e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597e0.md) [`00c597f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597f0.md) [`00c59800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59800.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c598b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598b0.md) [`00c598c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598c0.md) [`00c598d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9c8c.md#insn-004f9ca8) · [`004f9cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9c8c.md#insn-004f9cc0) · [`004f9cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9c8c.md#insn-004f9cc8)
- 新版 [`004f9ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ccc.md#insn-004f9ce8) · [`004f9d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ccc.md#insn-004f9d00) · [`004f9d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9ccc.md#insn-004f9d08)

~~~diff
- 004f9ca8 ["INT_ADD", "register:40f0:8", ["const:4f9ca8:8", "const:4:8"]]
- 004f9ca8 ["CALL", null, ["callee:00c598b0:8"]]
+ 004f9ce8 ["INT_ADD", "register:40f0:8", ["const:4f9ce8:8", "const:4:8"]]
+ 004f9ce8 ["CALL", null, ["callee:00c598b0:8"]]
- 004f9ca8 bytes ce7e1d94
+ 004f9ce8 bytes f27e1d94
- 004f9cc0 ["INT_ADD", "register:40f0:8", ["const:4f9cc0:8", "const:4:8"]]
- 004f9cc0 ["CALL", null, ["callee:00c598c0:8"]]
+ 004f9d00 ["INT_ADD", "register:40f0:8", ["const:4f9d00:8", "const:4:8"]]
+ 004f9d00 ["CALL", null, ["callee:00c598c0:8"]]
- 004f9cc0 bytes cc7e1d94
+ 004f9d00 bytes f07e1d94
- 004f9cc8 ["INT_ADD", "register:40f0:8", ["const:4f9cc8:8", "const:4:8"]]
- 004f9cc8 ["CALL", null, ["callee:00c598b0:8"]]
+ 004f9d08 ["INT_ADD", "register:40f0:8", ["const:4f9d08:8", "const:4:8"]]
+ 004f9d08 ["CALL", null, ["callee:00c598b0:8"]]
- 004f9cc8 bytes c67e1d94
+ 004f9d08 bytes ea7e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d3c7e4f70285591da586c53cdb29aa"></a>

### [`004fa384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa384.md) → [`004fa3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fa/004fa3c4.md) _ZN5Botan17DataSource_StreamD1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fa3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa384.md#insn-004fa3a8)
- 新版 [`004fa3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fa/004fa3c4.md#insn-004fa3e8)

~~~diff
- 004fa3a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fa3a8 ["INT_ADD", "register:40f0:8", ["const:4fa3a8:8", "const:4:8"]]
- 004fa3a8 ["CALLIND", null, ["register:0:8"]]
+ 004fa3e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fa3e8 ["INT_ADD", "register:40f0:8", ["const:4fa3e8:8", "const:4:8"]]
+ 004fa3e8 ["CALLIND", null, ["register:0:8"]]
- 004fa3a8 bytes 00013fd6
+ 004fa3e8 bytes 00013fd6
~~~


<a id="compare-3b9bf595a2a9bfbcbd55c5a0c3510ae9"></a>

### [`004fa3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3d0.md) → [`004fa410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fa/004fa410.md) _ZN5Botan17DataSource_StreamD0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fa3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3d0.md#insn-004fa3e0)
- 新版 [`004fa420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fa/004fa410.md#insn-004fa420)

~~~diff
- 004fa3e0 ["INT_ADD", "register:40f0:8", ["const:4fa3e0:8", "const:4:8"]]
- 004fa3e0 ["CALL", null, ["callee:00c59740:8"]]
+ 004fa420 ["INT_ADD", "register:40f0:8", ["const:4fa420:8", "const:4:8"]]
+ 004fa420 ["CALL", null, ["callee:00c59740:8"]]
- 004fa3e0 bytes a47c1d94
+ 004fa420 bytes c87c1d94
~~~


<a id="compare-7f223843a75de23f6aac9bd5d3122532"></a>

### [`004fc6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc6dc.md) → [`004fc71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fc71c.md) FUN_004fc71c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fc72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc6dc.md#insn-004fc72c) · [`004fc73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc6dc.md#insn-004fc73c)
- 新版 [`004fc76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fc71c.md#insn-004fc76c) · [`004fc77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fc71c.md#insn-004fc77c)

~~~diff
- 004fc72c ["INT_ADD", "register:40f0:8", ["const:4fc72c:8", "const:4:8"]]
- 004fc72c ["CALL", null, ["callee:00c57f80:8"]]
+ 004fc76c ["INT_ADD", "register:40f0:8", ["const:4fc76c:8", "const:4:8"]]
+ 004fc76c ["CALL", null, ["callee:00c57f80:8"]]
- 004fc72c bytes e16d1d94
+ 004fc76c bytes 056e1d94
- 004fc73c ["INT_ADD", "register:40f0:8", ["const:4fc73c:8", "const:4:8"]]
- 004fc73c ["CALL", null, ["callee:00c57f80:8"]]
+ 004fc77c ["INT_ADD", "register:40f0:8", ["const:4fc77c:8", "const:4:8"]]
+ 004fc77c ["CALL", null, ["callee:00c57f80:8"]]
- 004fc73c bytes dd6d1d94
+ 004fc77c bytes 016e1d94
~~~


<a id="compare-76bb7008fee0717c28712cacc9a00891"></a>

### [`004fd71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd71c.md) → [`004fd75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd75c.md) _ZN5Botan11erase_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd71c.md#insn-004fd764)
- 新版 [`004fd7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd75c.md#insn-004fd7a4)

~~~diff
- 004fd764 ["INT_ADD", "register:40f0:8", ["const:4fd764:8", "const:4:8"]]
- 004fd764 ["CALL", null, ["callee:00c586d0:8"]]
+ 004fd7a4 ["INT_ADD", "register:40f0:8", ["const:4fd7a4:8", "const:4:8"]]
+ 004fd7a4 ["CALL", null, ["callee:00c586d0:8"]]
- 004fd764 bytes a76b1d94
+ 004fd7a4 bytes cb6b1d94
~~~


<a id="compare-afe7f9b986823466b8d7d451fc621552"></a>

### [`004fd7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd7d4.md) → [`004fd814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd814.md) _ZN5Botan13replace_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd7d4.md#insn-004fd814)
- 新版 [`004fd854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd814.md#insn-004fd854)

~~~diff
- 004fd814 ["INT_ADD", "register:40f0:8", ["const:4fd814:8", "const:4:8"]]
- 004fd814 ["CALL", null, ["callee:0043bb60:8"]]
+ 004fd854 ["INT_ADD", "register:40f0:8", ["const:4fd854:8", "const:4:8"]]
+ 004fd854 ["CALL", null, ["callee:0043bb60:8"]]
- 004fd814 bytes c3f8fc97
+ 004fd854 bytes c3f8fc97
~~~


<a id="compare-75ae5c88c4c7bc2406e0febda079173d"></a>

### [`004fd8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd8b8.md) → [`004fd8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd8f8.md) _ZN5Botan12replace_charERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEcc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd8b8.md#insn-004fd8f8)
- 新版 [`004fd938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd8f8.md#insn-004fd938)

~~~diff
- 004fd8f8 ["INT_ADD", "register:40f0:8", ["const:4fd8f8:8", "const:4:8"]]
- 004fd8f8 ["CALL", null, ["callee:0043bb60:8"]]
+ 004fd938 ["INT_ADD", "register:40f0:8", ["const:4fd938:8", "const:4:8"]]
+ 004fd938 ["CALL", null, ["callee:0043bb60:8"]]
- 004fd8f8 bytes 8af8fc97
+ 004fd938 bytes 8af8fc97
~~~


<a id="compare-7860d464c2ecd5cf74a425975afdc2c2"></a>

### [`004fe2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe2a0.md) → [`004fe2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe2e0.md) _ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59940.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c59a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a10.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fe3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe2a0.md#insn-004fe3d8) · [`004fe3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe2a0.md#insn-004fe3f8) · [`004fe41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe2a0.md#insn-004fe41c)
- 新版 [`004fe418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe2e0.md#insn-004fe418) · [`004fe438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe2e0.md#insn-004fe438) · [`004fe45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe2e0.md#insn-004fe45c)

~~~diff
- 004fe3d8 ["INT_ADD", "register:40f0:8", ["const:4fe3d8:8", "const:4:8"]]
- 004fe3d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004fe418 ["INT_ADD", "register:40f0:8", ["const:4fe418:8", "const:4:8"]]
+ 004fe418 ["CALL", null, ["callee:00c57f60:8"]]
- 004fe3d8 bytes ae661d94
+ 004fe418 bytes d2661d94
- 004fe3f8 ["INT_ADD", "register:40f0:8", ["const:4fe3f8:8", "const:4:8"]]
- 004fe3f8 ["CALL", null, ["callee:00c58010:8"]]
+ 004fe438 ["INT_ADD", "register:40f0:8", ["const:4fe438:8", "const:4:8"]]
+ 004fe438 ["CALL", null, ["callee:00c58010:8"]]
- 004fe3f8 bytes d2661d94
+ 004fe438 bytes f6661d94
- 004fe41c ["INT_ADD", "register:40f0:8", ["const:4fe41c:8", "const:4:8"]]
- 004fe41c ["CALL", null, ["callee:0044295c:8"]]
+ 004fe45c ["INT_ADD", "register:40f0:8", ["const:4fe45c:8", "const:4:8"]]
+ 004fe45c ["CALL", null, ["callee:0044295c:8"]]
- 004fe41c bytes 4011fd97
+ 004fe45c bytes 4011fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-277dae0baa90113abd124be894a4cf57"></a>

### [`004ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md) → [`004ff080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff080.md) _ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59950.md) · 呼出先 3件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c59a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a20.md) · 呼出先 3件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00547bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bf0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md#insn-004ff098) · [`004ff12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md#insn-004ff12c)
- 新版 [`004ff0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff080.md#insn-004ff0d8) · [`004ff16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff080.md#insn-004ff16c)

~~~diff
- 004ff098 ["INT_ADD", "register:40f0:8", ["const:4ff098:8", "const:4:8"]]
- 004ff098 ["CALL", null, ["callee:00547bf0:8"]]
+ 004ff0d8 ["INT_ADD", "register:40f0:8", ["const:4ff0d8:8", "const:4:8"]]
+ 004ff0d8 ["CALL", null, ["callee:00547bf0:8"]]
- 004ff098 bytes c6220194
+ 004ff0d8 bytes c6220194
- 004ff12c ["INT_ADD", "register:40f0:8", ["const:4ff12c:8", "const:4:8"]]
- 004ff12c ["CALL", null, ["callee:00c58120:8"]]
+ 004ff16c ["INT_ADD", "register:40f0:8", ["const:4ff16c:8", "const:4:8"]]
+ 004ff16c ["CALL", null, ["callee:00c58120:8"]]
- 004ff12c bytes c9631d94
+ 004ff16c bytes ed631d94
~~~


<a id="compare-48a82f4cbfc092a1d89335847d354748"></a>

### [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) → [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) FUN_004ff1e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`004ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md) [`004ff428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md) [`005049c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c4.md) [`005049c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md) [`00504a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504a70.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 18件 [`004ff080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff080.md) [`004ff468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff468.md) [`00504a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a04.md) [`00504a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md) [`00504ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504ab0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md#insn-004ff1f0) · [`004ff21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md#insn-004ff21c) · [`004ff228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md#insn-004ff228)
- 新版 [`004ff230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md#insn-004ff230) · [`004ff25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md#insn-004ff25c) · [`004ff268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md#insn-004ff268)

~~~diff
- 004ff1f0 ["INT_ADD", "register:40f0:8", ["const:4ff1f0:8", "const:4:8"]]
- 004ff1f0 ["CALL", null, ["callee:0043bb60:8"]]
+ 004ff230 ["INT_ADD", "register:40f0:8", ["const:4ff230:8", "const:4:8"]]
+ 004ff230 ["CALL", null, ["callee:0043bb60:8"]]
- 004ff1f0 bytes 4cf2fc97
+ 004ff230 bytes 4cf2fc97
- 004ff21c ["INT_ADD", "register:40f0:8", ["const:4ff21c:8", "const:4:8"]]
- 004ff21c ["CALL", null, ["callee:0043bb60:8"]]
+ 004ff25c ["INT_ADD", "register:40f0:8", ["const:4ff25c:8", "const:4:8"]]
+ 004ff25c ["CALL", null, ["callee:0043bb60:8"]]
- 004ff21c bytes 41f2fc97
+ 004ff25c bytes 41f2fc97
- 004ff228 ["INT_ADD", "register:40f0:8", ["const:4ff228:8", "const:4:8"]]
- 004ff228 ["CALL", null, ["callee:00549114:8"]]
+ 004ff268 ["INT_ADD", "register:40f0:8", ["const:4ff268:8", "const:4:8"]]
+ 004ff268 ["CALL", null, ["callee:00549114:8"]]
- 004ff228 bytes ab270194
+ 004ff268 bytes ab270194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a21aec63edaccb9c449ee8f019f81a"></a>

### [`004ff2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md) → [`004ff2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff2f0.md) _ZN5Botan15AlternativeName13add_othernameERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59960.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md#insn-004ff2fc) · [`004ff30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md#insn-004ff30c) · [`004ff31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md#insn-004ff31c)
- 新版 [`004ff33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff2f0.md#insn-004ff33c) · [`004ff34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff2f0.md#insn-004ff34c) · [`004ff35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff2f0.md#insn-004ff35c)

~~~diff
- 004ff2fc ["INT_ADD", "register:40f0:8", ["const:4ff2fc:8", "const:4:8"]]
- 004ff2fc ["CALL", null, ["callee:00c59a30:8"]]
+ 004ff33c ["INT_ADD", "register:40f0:8", ["const:4ff33c:8", "const:4:8"]]
+ 004ff33c ["CALL", null, ["callee:00c59a30:8"]]
- 004ff2fc bytes 99691d94
+ 004ff33c bytes bd691d94
- 004ff30c ["INT_ADD", "register:40f0:8", ["const:4ff30c:8", "const:4:8"]]
- 004ff30c ["CALL", null, ["callee:004ff3bc:8"]]
+ 004ff34c ["INT_ADD", "register:40f0:8", ["const:4ff34c:8", "const:4:8"]]
+ 004ff34c ["CALL", null, ["callee:004ff3bc:8"]]
- 004ff30c bytes 1c000094
+ 004ff34c bytes 1c000094
- 004ff31c ["INT_ADD", "register:40f0:8", ["const:4ff31c:8", "const:4:8"]]
- 004ff31c ["CALL", null, ["callee:00c57f80:8"]]
+ 004ff35c ["INT_ADD", "register:40f0:8", ["const:4ff35c:8", "const:4:8"]]
+ 004ff35c ["CALL", null, ["callee:00c57f80:8"]]
- 004ff31c bytes e5621d94
+ 004ff35c bytes 09631d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526e36093793c384f336d55571d78f32"></a>

### [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) → [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) FUN_004ff3bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004ff2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md) [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) [`005140b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md) [`0052de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md) · 呼出先 4件 [`00547dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md) [`00547f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`004ff2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff2f0.md) [`004ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md) [`005140f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md) [`0052de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md) · 呼出先 4件 [`00547e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547e04.md) [`00547f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547f6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md#insn-004ff3a0) · [`004ff3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md#insn-004ff3ac) · [`004ff3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md#insn-004ff3bc)
- 新版 [`004ff3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md#insn-004ff3e0) · [`004ff3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md#insn-004ff3ec) · [`004ff3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md#insn-004ff3fc)

~~~diff
- 004ff3a0 ["INT_ADD", "register:40f0:8", ["const:4ff3a0:8", "const:4:8"]]
- 004ff3a0 ["CALL", null, ["callee:00547f6c:8"]]
+ 004ff3e0 ["INT_ADD", "register:40f0:8", ["const:4ff3e0:8", "const:4:8"]]
+ 004ff3e0 ["CALL", null, ["callee:00547f6c:8"]]
- 004ff3a0 bytes e3220194
+ 004ff3e0 bytes e3220194
- 004ff3ac ["INT_ADD", "register:40f0:8", ["const:4ff3ac:8", "const:4:8"]]
- 004ff3ac ["CALL", null, ["callee:00547e04:8"]]
+ 004ff3ec ["INT_ADD", "register:40f0:8", ["const:4ff3ec:8", "const:4:8"]]
+ 004ff3ec ["CALL", null, ["callee:00547e04:8"]]
- 004ff3ac bytes 86220194
+ 004ff3ec bytes 86220194
- 004ff3bc ["INT_ADD", "register:40f0:8", ["const:4ff3bc:8", "const:4:8"]]
- 004ff3bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004ff3fc ["INT_ADD", "register:40f0:8", ["const:4ff3fc:8", "const:4:8"]]
+ 004ff3fc ["CALL", null, ["callee:00c57f80:8"]]
- 004ff3bc bytes bd621d94
+ 004ff3fc bytes e1621d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99821cfccbbcd389e66b4bc4f13b36cd"></a>

### [`004ff428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md) → [`004ff468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff468.md) _ZNK5Botan15AlternativeName8contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md) · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md)
- 新版 呼出元 1件 [`00c59a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a40.md) · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md#insn-004ff4c4) · [`004ff50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md#insn-004ff50c) · [`004ff51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md#insn-004ff51c)
- 新版 [`004ff504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff468.md#insn-004ff504) · [`004ff54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff468.md#insn-004ff54c) · [`004ff55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff468.md#insn-004ff55c)

~~~diff
- 004ff4c4 ["INT_ADD", "register:40f0:8", ["const:4ff4c4:8", "const:4:8"]]
- 004ff4c4 ["CALL", null, ["callee:004ff1e0:8"]]
+ 004ff504 ["INT_ADD", "register:40f0:8", ["const:4ff504:8", "const:4:8"]]
+ 004ff504 ["CALL", null, ["callee:004ff1e0:8"]]
- 004ff4c4 bytes 37ffff97
+ 004ff504 bytes 37ffff97
- 004ff50c ["INT_ADD", "register:40f0:8", ["const:4ff50c:8", "const:4:8"]]
- 004ff50c ["CALL", null, ["callee:00c58980:8"]]
+ 004ff54c ["INT_ADD", "register:40f0:8", ["const:4ff54c:8", "const:4:8"]]
+ 004ff54c ["CALL", null, ["callee:00c58980:8"]]
- 004ff50c bytes e9641d94
+ 004ff54c bytes 0d651d94
- 004ff51c ["INT_ADD", "register:40f0:8", ["const:4ff51c:8", "const:4:8"]]
- 004ff51c ["CALL", null, ["callee:004ff1e0:8"]]
+ 004ff55c ["INT_ADD", "register:40f0:8", ["const:4ff55c:8", "const:4:8"]]
+ 004ff55c ["CALL", null, ["callee:004ff1e0:8"]]
- 004ff51c bytes 21ffff97
+ 004ff55c bytes 21ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ac5b3880c061f72f6443188e6070afb"></a>

### [`004ff5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5a8.md) → [`004ff5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff5e8.md) _ZNK5Botan15AlternativeName9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5a8.md#insn-004ff5b4)
- 新版 [`004ff5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff5e8.md#insn-004ff5f4)

~~~diff
- 004ff5b4 ["INT_ADD", "register:40f0:8", ["const:4ff5b4:8", "const:4:8"]]
- 004ff5b4 ["CALL", null, ["callee:005480d8:8"]]
+ 004ff5f4 ["INT_ADD", "register:40f0:8", ["const:4ff5f4:8", "const:4:8"]]
+ 004ff5f4 ["CALL", null, ["callee:005480d8:8"]]
- 004ff5b4 bytes b9220194
+ 004ff5f4 bytes b9220194
~~~


<a id="compare-946fa691f388bf6c4cb988e69c36fb9d"></a>

### [`004ff5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5c8.md) → [`004ff608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff608.md) _ZNK5Botan15AlternativeName19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5c8.md#insn-004ff638) · [`004ff6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5c8.md#insn-004ff6c0)
- 新版 [`004ff678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff608.md#insn-004ff678) · [`004ff700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff608.md#insn-004ff700)

~~~diff
- 004ff638 ["INT_ADD", "register:40f0:8", ["const:4ff638:8", "const:4:8"]]
- 004ff638 ["CALL", null, ["callee:00c58120:8"]]
+ 004ff678 ["INT_ADD", "register:40f0:8", ["const:4ff678:8", "const:4:8"]]
+ 004ff678 ["CALL", null, ["callee:00c58120:8"]]
- 004ff638 bytes 86621d94
+ 004ff678 bytes aa621d94
- 004ff6c0 ["INT_ADD", "register:40f0:8", ["const:4ff6c0:8", "const:4:8"]]
- 004ff6c0 ["CALL", null, ["callee:00c58120:8"]]
+ 004ff700 ["INT_ADD", "register:40f0:8", ["const:4ff700:8", "const:4:8"]]
+ 004ff700 ["CALL", null, ["callee:00c58120:8"]]
- 004ff6c0 bytes 64621d94
+ 004ff700 bytes 88621d94
~~~


<a id="compare-5068824d6ba02ac168dfa7ce9f0e785d"></a>

### [`004ff724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md) → [`004ff764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff764.md) _ZNK5Botan15AlternativeName13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59980.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)
- 新版 呼出元 1件 [`00c59a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a50.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md#insn-004ff744) · [`004ff79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md#insn-004ff79c) · [`004ff7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md#insn-004ff7b0)
- 新版 [`004ff784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff764.md#insn-004ff784) · [`004ff7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff764.md#insn-004ff7dc) · [`004ff7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff764.md#insn-004ff7f0)

~~~diff
- 004ff744 ["INT_ADD", "register:40f0:8", ["const:4ff744:8", "const:4:8"]]
- 004ff744 ["CALL", null, ["callee:005480d8:8"]]
+ 004ff784 ["INT_ADD", "register:40f0:8", ["const:4ff784:8", "const:4:8"]]
+ 004ff784 ["CALL", null, ["callee:005480d8:8"]]
- 004ff744 bytes 55220194
+ 004ff784 bytes 55220194
- 004ff79c ["INT_ADD", "register:40f0:8", ["const:4ff79c:8", "const:4:8"]]
- 004ff79c ["CALL", null, ["callee:00540dbc:8"]]
+ 004ff7dc ["INT_ADD", "register:40f0:8", ["const:4ff7dc:8", "const:4:8"]]
+ 004ff7dc ["CALL", null, ["callee:00540dbc:8"]]
- 004ff79c bytes 78050194
+ 004ff7dc bytes 78050194
- 004ff7b0 ["INT_ADD", "register:40f0:8", ["const:4ff7b0:8", "const:4:8"]]
- 004ff7b0 ["CALL", null, ["callee:0043bb60:8"]]
+ 004ff7f0 ["INT_ADD", "register:40f0:8", ["const:4ff7f0:8", "const:4:8"]]
+ 004ff7f0 ["CALL", null, ["callee:0043bb60:8"]]
- 004ff7b0 bytes dcf0fc97
+ 004ff7f0 bytes dcf0fc97
~~~


<a id="compare-0f16b98e9b7bb424a01cd6a6e6fb1621"></a>

### [`004ff838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md) → [`004ff878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md) _ZNK5Botan15AlternativeName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md#insn-004ff870) · [`004ff8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md#insn-004ff8a4) · [`004ff8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md#insn-004ff8b4)
- 新版 [`004ff8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md#insn-004ff8b0) · [`004ff8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md#insn-004ff8e4) · [`004ff8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md#insn-004ff8f4)

~~~diff
- 004ff870 ["INT_ADD", "register:40f0:8", ["const:4ff870:8", "const:4:8"]]
- 004ff870 ["CALL", null, ["callee:00c58780:8"]]
+ 004ff8b0 ["INT_ADD", "register:40f0:8", ["const:4ff8b0:8", "const:4:8"]]
+ 004ff8b0 ["CALL", null, ["callee:00c58780:8"]]
- 004ff870 bytes 90631d94
+ 004ff8b0 bytes b4631d94
- 004ff8a4 ["INT_ADD", "register:40f0:8", ["const:4ff8a4:8", "const:4:8"]]
- 004ff8a4 ["CALL", null, ["callee:004ffaec:8"]]
+ 004ff8e4 ["INT_ADD", "register:40f0:8", ["const:4ff8e4:8", "const:4:8"]]
+ 004ff8e4 ["CALL", null, ["callee:004ffaec:8"]]
- 004ff8a4 bytes 82000094
+ 004ff8e4 bytes 82000094
- 004ff8b4 ["INT_ADD", "register:40f0:8", ["const:4ff8b4:8", "const:4:8"]]
- 004ff8b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ff8f4 ["INT_ADD", "register:40f0:8", ["const:4ff8f4:8", "const:4:8"]]
+ 004ff8f4 ["CALL", null, ["callee:00c57f80:8"]]
- 004ff8b4 bytes 7f611d94
+ 004ff8f4 bytes a3611d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5aa73445686bb887c1e233676eb45c"></a>

### [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) → [`00500f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md) FUN_00500f4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 2件 [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00500f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md#insn-00500f28)
- 新版 [`00500f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md#insn-00500f68)

~~~diff
- 00500f28 ["INT_ADD", "register:40f0:8", ["const:500f28:8", "const:4:8"]]
- 00500f28 ["CALL", null, ["callee:00c57f80:8"]]
+ 00500f68 ["INT_ADD", "register:40f0:8", ["const:500f68:8", "const:4:8"]]
+ 00500f68 ["CALL", null, ["callee:00c57f80:8"]]
- 00500f28 bytes e25b1d94
+ 00500f68 bytes 065c1d94
~~~


<a id="compare-b02bc36808f7c564db6ab35bb4695fc6"></a>

### [`00501574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501574.md) → [`005015b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005015b4.md) _ZNK5Botan16X509_CertificateeqERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005015a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501574.md#insn-005015a0) · [`005015b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501574.md#insn-005015b0) · [`005015d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501574.md#insn-005015d0)
- 新版 [`005015e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005015b4.md#insn-005015e0) · [`005015f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005015b4.md#insn-005015f0) · [`00501610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005015b4.md#insn-00501610)

~~~diff
- 005015a0 ["INT_ADD", "register:40f0:8", ["const:5015a0:8", "const:4:8"]]
- 005015a0 ["CALL", null, ["callee:00c58120:8"]]
+ 005015e0 ["INT_ADD", "register:40f0:8", ["const:5015e0:8", "const:4:8"]]
+ 005015e0 ["CALL", null, ["callee:00c58120:8"]]
- 005015a0 bytes ac5a1d94
+ 005015e0 bytes d05a1d94
- 005015b0 ["INT_ADD", "register:40f0:8", ["const:5015b0:8", "const:4:8"]]
- 005015b0 ["CALL", null, ["callee:00c58770:8"]]
+ 005015f0 ["INT_ADD", "register:40f0:8", ["const:5015f0:8", "const:4:8"]]
+ 005015f0 ["CALL", null, ["callee:00c58770:8"]]
- 005015b0 bytes 3c5c1d94
+ 005015f0 bytes 605c1d94
- 005015d0 ["INT_ADD", "register:40f0:8", ["const:5015d0:8", "const:4:8"]]
- 005015d0 ["CALL", null, ["callee:00c58120:8"]]
+ 00501610 ["INT_ADD", "register:40f0:8", ["const:501610:8", "const:4:8"]]
+ 00501610 ["CALL", null, ["callee:00c58120:8"]]
- 005015d0 bytes a05a1d94
+ 00501610 bytes c45a1d94
~~~


<a id="compare-27d4d4dded81c604a2700e16ff7cc805"></a>

### [`005015f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md) → [`00501630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501630.md) FUN_00501630

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050160c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md#insn-0050160c) · [`0050162c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md#insn-0050162c)
- 新版 [`0050164c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501630.md#insn-0050164c) · [`0050166c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501630.md#insn-0050166c)

~~~diff
- 0050160c ["INT_ADD", "register:40f0:8", ["const:50160c:8", "const:4:8"]]
- 0050160c ["CALL", null, ["callee:00c53da0:8"]]
+ 0050164c ["INT_ADD", "register:40f0:8", ["const:50164c:8", "const:4:8"]]
+ 0050164c ["CALL", null, ["callee:00c53da0:8"]]
- 0050160c bytes bd491d94
+ 0050164c bytes d5491d94
- 0050162c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050162c ["INT_ADD", "register:40f0:8", ["const:50162c:8", "const:4:8"]]
- 0050162c ["CALLIND", null, ["register:0:8"]]
+ 0050166c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050166c ["INT_ADD", "register:40f0:8", ["const:50166c:8", "const:4:8"]]
+ 0050166c ["CALLIND", null, ["register:0:8"]]
- 0050162c bytes 00013fd6
+ 0050166c bytes 00013fd6
~~~


<a id="compare-2d766af6104bcd0561dd4394ac6d1f5a"></a>

### [`00501640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md) → [`00501680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501680.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateENSt6__ndk110shared_ptrIKNS_16X509_CertificateEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c599e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599e0.md) · 呼出先 4件 [`00548598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)
- 新版 呼出元 1件 [`00c59ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ab0.md) · 呼出先 4件 [`005485d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005485d8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005016ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md#insn-005016ac) · [`005016bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md#insn-005016bc) · [`005016dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md#insn-005016dc)
- 新版 [`005016ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501680.md#insn-005016ec) · [`005016fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501680.md#insn-005016fc) · [`0050171c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501680.md#insn-0050171c)

~~~diff
- 005016ac ["INT_ADD", "register:40f0:8", ["const:5016ac:8", "const:4:8"]]
- 005016ac ["CALL", null, ["callee:00c58120:8"]]
+ 005016ec ["INT_ADD", "register:40f0:8", ["const:5016ec:8", "const:4:8"]]
+ 005016ec ["CALL", null, ["callee:00c58120:8"]]
- 005016ac bytes 695a1d94
+ 005016ec bytes 8d5a1d94
- 005016bc ["INT_ADD", "register:40f0:8", ["const:5016bc:8", "const:4:8"]]
- 005016bc ["CALL", null, ["callee:00c58770:8"]]
+ 005016fc ["INT_ADD", "register:40f0:8", ["const:5016fc:8", "const:4:8"]]
+ 005016fc ["CALL", null, ["callee:00c58770:8"]]
- 005016bc bytes f95b1d94
+ 005016fc bytes 1d5c1d94
- 005016dc ["INT_ADD", "register:40f0:8", ["const:5016dc:8", "const:4:8"]]
- 005016dc ["CALL", null, ["callee:00c58120:8"]]
+ 0050171c ["INT_ADD", "register:40f0:8", ["const:50171c:8", "const:4:8"]]
+ 0050171c ["CALL", null, ["callee:00c58120:8"]]
- 005016dc bytes 5d5a1d94
+ 0050171c bytes 815a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

