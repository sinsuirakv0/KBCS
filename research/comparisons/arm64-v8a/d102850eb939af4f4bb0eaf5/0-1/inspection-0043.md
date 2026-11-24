# v16.0.1 → v16.0.2 · 要調査の変更候補 (43)

[一覧の目次](README.md)

<a id="compare-963aef5e3d47fbfb6d3e505b7a7aac38"></a>

### [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) → [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) FUN_00c10240

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`00c0ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed80.md) [`00c0efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efcc.md) [`00c0f218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f218.md) [`00c0f448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f448.md) [`00c0f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f678.md) · 呼出先 2件 [`00c5b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b150.md) [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md)
- 新版 呼出元 14件 [`00c0ee1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0e/00c0ee1c.md) [`00c0f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f068.md) [`00c0f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f2b4.md) [`00c0f4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f4e4.md) [`00c0f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f714.md) · 呼出先 2件 [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md) [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1020c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md#insn-00c1020c) · [`00c1022c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md#insn-00c1022c) · [`00c1023c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md#insn-00c1023c)
- 新版 [`00c102a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102a8) · [`00c102c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102c8) · [`00c102d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102d8)

~~~diff
- 00c1020c ["INT_ADD", "register:40f0:8", ["const:c1020c:8", "const:4:8"]]
- 00c1020c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c102a8 ["INT_ADD", "register:40f0:8", ["const:c102a8:8", "const:4:8"]]
+ 00c102a8 ["CALL", null, ["callee:00c5e640:8"]]
- 00c1020c bytes d9380194
+ 00c102a8 bytes e6380194
- 00c1022c ["INT_ADD", "register:40f0:8", ["const:c1022c:8", "const:4:8"]]
- 00c1022c ["CALL", null, ["callee:00c5b220:8"]]
+ 00c102c8 ["INT_ADD", "register:40f0:8", ["const:c102c8:8", "const:4:8"]]
+ 00c102c8 ["CALL", null, ["callee:00c5b220:8"]]
- 00c1022c bytes c92b0194
+ 00c102c8 bytes d62b0194
- 00c1023c ["INT_ADD", "register:40f0:8", ["const:c1023c:8", "const:4:8"]]
- 00c1023c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c102d8 ["INT_ADD", "register:40f0:8", ["const:c102d8:8", "const:4:8"]]
+ 00c102d8 ["CALL", null, ["callee:00c5e640:8"]]
- 00c1023c bytes cd380194
+ 00c102d8 bytes da380194
~~~


<a id="compare-f4f13b9b46c99ef314f7a89116200e4c"></a>

### [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) → [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) FUN_00c11980

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00c104b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c104b4.md) [`00c10700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10700.md) [`00c1094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c1094c.md) [`00c10b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10b7c.md) [`00c10dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10dac.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 9件 [`00c10550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10550.md) [`00c1079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1079c.md) [`00c109e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109e8.md) [`00c10c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c18.md) [`00c10e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c11950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md#insn-00c11950) · [`00c119b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md#insn-00c119b4) · [`00c11a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md#insn-00c11a3c)
- 新版 [`00c119ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md#insn-00c119ec) · [`00c11a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md#insn-00c11a50) · [`00c11ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md#insn-00c11ad8)

~~~diff
- 00c11950 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c11950 ["INT_ADD", "register:40f0:8", ["const:c11950:8", "const:4:8"]]
- 00c11950 ["CALLIND", null, ["register:0:8"]]
+ 00c119ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c119ec ["INT_ADD", "register:40f0:8", ["const:c119ec:8", "const:4:8"]]
+ 00c119ec ["CALLIND", null, ["register:0:8"]]
- 00c11950 bytes 00013fd6
+ 00c119ec bytes 00013fd6
- 00c119b4 ["INT_ADD", "register:40f0:8", ["const:c119b4:8", "const:4:8"]]
- 00c119b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c11a50 ["INT_ADD", "register:40f0:8", ["const:c11a50:8", "const:4:8"]]
+ 00c11a50 ["CALL", null, ["callee:00c57f60:8"]]
- 00c119b4 bytes 37190194
+ 00c11a50 bytes 44190194
- 00c11a3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c11a3c ["INT_ADD", "register:40f0:8", ["const:c11a3c:8", "const:4:8"]]
- 00c11a3c ["CALLIND", null, ["register:0:8"]]
+ 00c11ad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c11ad8 ["INT_ADD", "register:40f0:8", ["const:c11ad8:8", "const:4:8"]]
+ 00c11ad8 ["CALLIND", null, ["register:0:8"]]
- 00c11a3c bytes 00013fd6
+ 00c11ad8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f15498311177000c27b25b92bc5a125d"></a>

### [`00c133a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c133a8.md) → [`00c13444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13444.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a770.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c133d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c133a8.md#insn-00c133d8)
- 新版 [`00c13474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13444.md#insn-00c13474)

~~~diff
- 00c133d8 ["INT_ADD", "register:40f0:8", ["const:c133d8:8", "const:4:8"]]
- 00c133d8 ["CALL", null, ["callee:00c5a840:8"]]
+ 00c13474 ["INT_ADD", "register:40f0:8", ["const:c13474:8", "const:4:8"]]
+ 00c13474 ["CALL", null, ["callee:00c5a840:8"]]
- 00c133d8 bytes e61c0194
+ 00c13474 bytes f31c0194
~~~


<a id="compare-c38179cf1d6e09e9ae9286fd2241667f"></a>

### [`00c133ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c133ec.md) → [`00c13488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13488.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a770.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c13424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c133ec.md#insn-00c13424)
- 新版 [`00c134c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13488.md#insn-00c134c0)

~~~diff
- 00c13424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c13424 ["INT_ADD", "register:40f0:8", ["const:c13424:8", "const:4:8"]]
- 00c13424 ["CALLIND", null, ["register:0:8"]]
+ 00c134c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c134c0 ["INT_ADD", "register:40f0:8", ["const:c134c0:8", "const:4:8"]]
+ 00c134c0 ["CALLIND", null, ["register:0:8"]]
- 00c13424 bytes 00013fd6
+ 00c134c0 bytes 00013fd6
~~~


<a id="compare-e649ad3fa38ac9cff62ef9916b1a3367"></a>

### [`00c135d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c135d0.md) → [`00c1366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1366c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c13604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c135d0.md#insn-00c13604) · [`00c13628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c135d0.md#insn-00c13628)
- 新版 [`00c136a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1366c.md#insn-00c136a0) · [`00c136c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1366c.md#insn-00c136c4)

~~~diff
- 00c13604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c13604 ["INT_ADD", "register:40f0:8", ["const:c13604:8", "const:4:8"]]
- 00c13604 ["CALLIND", null, ["register:0:8"]]
+ 00c136a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c136a0 ["INT_ADD", "register:40f0:8", ["const:c136a0:8", "const:4:8"]]
+ 00c136a0 ["CALLIND", null, ["register:0:8"]]
- 00c13604 bytes 00013fd6
+ 00c136a0 bytes 00013fd6
- 00c13628 ["INT_ADD", "register:40f0:8", ["const:c13628:8", "const:4:8"]]
- 00c13628 ["CALL", null, ["callee:00c07bb4:8"]]
+ 00c136c4 ["INT_ADD", "register:40f0:8", ["const:c136c4:8", "const:4:8"]]
+ 00c136c4 ["CALL", null, ["callee:00c07bb4:8"]]
- 00c13628 bytes 3cd1ff97
+ 00c136c4 bytes 3cd1ff97
~~~


<a id="compare-49865c7851b9cc1ff72cb13e3610a4a5"></a>

### [`00c137dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c137dc.md) → [`00c13878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13878.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c13810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c137dc.md#insn-00c13810) · [`00c13834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c137dc.md#insn-00c13834)
- 新版 [`00c138ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13878.md#insn-00c138ac) · [`00c138d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13878.md#insn-00c138d0)

~~~diff
- 00c13810 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c13810 ["INT_ADD", "register:40f0:8", ["const:c13810:8", "const:4:8"]]
- 00c13810 ["CALLIND", null, ["register:0:8"]]
+ 00c138ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c138ac ["INT_ADD", "register:40f0:8", ["const:c138ac:8", "const:4:8"]]
+ 00c138ac ["CALLIND", null, ["register:0:8"]]
- 00c13810 bytes 00013fd6
+ 00c138ac bytes 00013fd6
- 00c13834 ["INT_ADD", "register:40f0:8", ["const:c13834:8", "const:4:8"]]
- 00c13834 ["CALL", null, ["callee:00c07bb4:8"]]
+ 00c138d0 ["INT_ADD", "register:40f0:8", ["const:c138d0:8", "const:4:8"]]
+ 00c138d0 ["CALL", null, ["callee:00c07bb4:8"]]
- 00c13834 bytes b9d0ff97
+ 00c138d0 bytes b9d0ff97
~~~


<a id="compare-2e222d32c48b83562d4bcc4e5123bcc3"></a>

### [`00c139ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c139ac.md) → [`00c13a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13a48.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c139d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c139ac.md#insn-00c139d8)
- 新版 [`00c13a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13a48.md#insn-00c13a74)

~~~diff
- 00c139d8 ["INT_ADD", "register:40f0:8", ["const:c139d8:8", "const:4:8"]]
- 00c139d8 ["CALL", null, ["callee:00c14948:8"]]
+ 00c13a74 ["INT_ADD", "register:40f0:8", ["const:c13a74:8", "const:4:8"]]
+ 00c13a74 ["CALL", null, ["callee:00c14948:8"]]
- 00c139d8 bytes b5030094
+ 00c13a74 bytes b5030094
~~~


<a id="compare-b512d681044c55ee0e3453f8e6728ff2"></a>

### [`00c14094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14094.md) → [`00c14130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14130.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c140c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14094.md#insn-00c140c0)
- 新版 [`00c1415c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14130.md#insn-00c1415c)

~~~diff
- 00c140c0 ["INT_ADD", "register:40f0:8", ["const:c140c0:8", "const:4:8"]]
- 00c140c0 ["CALL", null, ["callee:00c14948:8"]]
+ 00c1415c ["INT_ADD", "register:40f0:8", ["const:c1415c:8", "const:4:8"]]
+ 00c1415c ["CALL", null, ["callee:00c14948:8"]]
- 00c140c0 bytes fb010094
+ 00c1415c bytes fb010094
~~~


<a id="compare-ff6e192a152f23c9813e24930beaedd2"></a>

### [`00c140f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c140f8.md) → [`00c14194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14194.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c140f8.md#insn-00c14124)
- 新版 [`00c141c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14194.md#insn-00c141c0)

~~~diff
- 00c14124 ["INT_ADD", "register:40f0:8", ["const:c14124:8", "const:4:8"]]
- 00c14124 ["CALL", null, ["callee:00c14948:8"]]
+ 00c141c0 ["INT_ADD", "register:40f0:8", ["const:c141c0:8", "const:4:8"]]
+ 00c141c0 ["CALL", null, ["callee:00c14948:8"]]
- 00c14124 bytes e2010094
+ 00c141c0 bytes e2010094
~~~


<a id="compare-074292394b59147f7ae1d5b28aef06e2"></a>

### [`00c14158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14158.md) → [`00c141f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c141f4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14158.md#insn-00c14184)
- 新版 [`00c14220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c141f4.md#insn-00c14220)

~~~diff
- 00c14184 ["INT_ADD", "register:40f0:8", ["const:c14184:8", "const:4:8"]]
- 00c14184 ["CALL", null, ["callee:00c14948:8"]]
+ 00c14220 ["INT_ADD", "register:40f0:8", ["const:c14220:8", "const:4:8"]]
+ 00c14220 ["CALL", null, ["callee:00c14948:8"]]
- 00c14184 bytes ca010094
+ 00c14220 bytes ca010094
~~~


<a id="compare-3e113da88b016ae07c99c36efa32de5c"></a>

### [`00c141bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c141bc.md) → [`00c14258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14258.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c141e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c141bc.md#insn-00c141e8)
- 新版 [`00c14284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14258.md#insn-00c14284)

~~~diff
- 00c141e8 ["INT_ADD", "register:40f0:8", ["const:c141e8:8", "const:4:8"]]
- 00c141e8 ["CALL", null, ["callee:00c14948:8"]]
+ 00c14284 ["INT_ADD", "register:40f0:8", ["const:c14284:8", "const:4:8"]]
+ 00c14284 ["CALL", null, ["callee:00c14948:8"]]
- 00c141e8 bytes b1010094
+ 00c14284 bytes b1010094
~~~


<a id="compare-4395a257310755286e9331abce1b7b47"></a>

### [`00c1421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c1421c.md) → [`00c142b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c142b8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c1421c.md#insn-00c14248)
- 新版 [`00c142e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c142b8.md#insn-00c142e4)

~~~diff
- 00c14248 ["INT_ADD", "register:40f0:8", ["const:c14248:8", "const:4:8"]]
- 00c14248 ["CALL", null, ["callee:00c14948:8"]]
+ 00c142e4 ["INT_ADD", "register:40f0:8", ["const:c142e4:8", "const:4:8"]]
+ 00c142e4 ["CALL", null, ["callee:00c14948:8"]]
- 00c14248 bytes 99010094
+ 00c142e4 bytes 99010094
~~~


<a id="compare-07db35cbb7b1949c04d5803cd5cb203a"></a>

### [`00c14280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14280.md) → [`00c1431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1431c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c142ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14280.md#insn-00c142ac)
- 新版 [`00c14348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1431c.md#insn-00c14348)

~~~diff
- 00c142ac ["INT_ADD", "register:40f0:8", ["const:c142ac:8", "const:4:8"]]
- 00c142ac ["CALL", null, ["callee:00c14948:8"]]
+ 00c14348 ["INT_ADD", "register:40f0:8", ["const:c14348:8", "const:4:8"]]
+ 00c14348 ["CALL", null, ["callee:00c14948:8"]]
- 00c142ac bytes 80010094
+ 00c14348 bytes 80010094
~~~


<a id="compare-6177ad3a32ee831534f5c76501685bb1"></a>

### [`00c142e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c142e0.md) → [`00c1437c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1437c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e610.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c142e0.md#insn-00c14344) · [`00c14398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c142e0.md#insn-00c14398) · [`00c143d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c142e0.md#insn-00c143d8)
- 新版 [`00c143e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1437c.md#insn-00c143e0) · [`00c14434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1437c.md#insn-00c14434) · [`00c14474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1437c.md#insn-00c14474)

~~~diff
- 00c14344 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14344 ["INT_ADD", "register:40f0:8", ["const:c14344:8", "const:4:8"]]
- 00c14344 ["CALLIND", null, ["register:0:8"]]
+ 00c143e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c143e0 ["INT_ADD", "register:40f0:8", ["const:c143e0:8", "const:4:8"]]
+ 00c143e0 ["CALLIND", null, ["register:0:8"]]
- 00c14344 bytes 00013fd6
+ 00c143e0 bytes 00013fd6
- 00c14398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14398 ["INT_ADD", "register:40f0:8", ["const:c14398:8", "const:4:8"]]
- 00c14398 ["CALLIND", null, ["register:0:8"]]
+ 00c14434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14434 ["INT_ADD", "register:40f0:8", ["const:c14434:8", "const:4:8"]]
+ 00c14434 ["CALLIND", null, ["register:0:8"]]
- 00c14398 bytes 00013fd6
+ 00c14434 bytes 00013fd6
- 00c143d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c143d8 ["INT_ADD", "register:40f0:8", ["const:c143d8:8", "const:4:8"]]
- 00c143d8 ["CALLIND", null, ["register:0:8"]]
+ 00c14474 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14474 ["INT_ADD", "register:40f0:8", ["const:c14474:8", "const:4:8"]]
+ 00c14474 ["CALLIND", null, ["register:0:8"]]
- 00c143d8 bytes 00013fd6
+ 00c14474 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94e11a6199a24c543586231e9def08ee"></a>

### [`00c144c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c144c8.md) → [`00c14564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14564.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c144fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c144c8.md#insn-00c144fc) · [`00c14560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c144c8.md#insn-00c14560)
- 新版 [`00c14598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14564.md#insn-00c14598) · [`00c145fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14564.md#insn-00c145fc)

~~~diff
- 00c144fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c144fc ["INT_ADD", "register:40f0:8", ["const:c144fc:8", "const:4:8"]]
- 00c144fc ["CALLIND", null, ["register:0:8"]]
+ 00c14598 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14598 ["INT_ADD", "register:40f0:8", ["const:c14598:8", "const:4:8"]]
+ 00c14598 ["CALLIND", null, ["register:0:8"]]
- 00c144fc bytes 00013fd6
+ 00c14598 bytes 00013fd6
- 00c14560 ["INT_ADD", "register:40f0:8", ["const:c14560:8", "const:4:8"]]
- 00c14560 ["CALL", null, ["callee:00c07bb4:8"]]
+ 00c145fc ["INT_ADD", "register:40f0:8", ["const:c145fc:8", "const:4:8"]]
+ 00c145fc ["CALL", null, ["callee:00c07bb4:8"]]
- 00c14560 bytes 6ecdff97
+ 00c145fc bytes 6ecdff97
~~~


<a id="compare-5f7267a5e180d0b7d3ed853328854cd5"></a>

### [`00c145b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c145b0.md) → [`00c1464c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1464c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c145dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c145b0.md#insn-00c145dc)
- 新版 [`00c14678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1464c.md#insn-00c14678)

~~~diff
- 00c145dc ["INT_ADD", "register:40f0:8", ["const:c145dc:8", "const:4:8"]]
- 00c145dc ["CALL", null, ["callee:00c14948:8"]]
+ 00c14678 ["INT_ADD", "register:40f0:8", ["const:c14678:8", "const:4:8"]]
+ 00c14678 ["CALL", null, ["callee:00c14948:8"]]
- 00c145dc bytes b4000094
+ 00c14678 bytes b4000094
~~~


<a id="compare-7a50908b8eaadd959f2ffec6e0c2e981"></a>

### [`00c14610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14610.md) → [`00c146ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c146ac.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1463c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14610.md#insn-00c1463c)
- 新版 [`00c146d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c146ac.md#insn-00c146d8)

~~~diff
- 00c1463c ["INT_ADD", "register:40f0:8", ["const:c1463c:8", "const:4:8"]]
- 00c1463c ["CALL", null, ["callee:00c14948:8"]]
+ 00c146d8 ["INT_ADD", "register:40f0:8", ["const:c146d8:8", "const:4:8"]]
+ 00c146d8 ["CALL", null, ["callee:00c14948:8"]]
- 00c1463c bytes 9c000094
+ 00c146d8 bytes 9c000094
~~~


<a id="compare-2a193ef0aa4075f5a8929adcc5cbc53c"></a>

### [`00c14670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14670.md) → [`00c1470c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1470c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1469c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14670.md#insn-00c1469c)
- 新版 [`00c14738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1470c.md#insn-00c14738)

~~~diff
- 00c1469c ["INT_ADD", "register:40f0:8", ["const:c1469c:8", "const:4:8"]]
- 00c1469c ["CALL", null, ["callee:00c14948:8"]]
+ 00c14738 ["INT_ADD", "register:40f0:8", ["const:c14738:8", "const:4:8"]]
+ 00c14738 ["CALL", null, ["callee:00c14948:8"]]
- 00c1469c bytes 84000094
+ 00c14738 bytes 84000094
~~~


<a id="compare-f9c3695febf5d843a46d041d637b038d"></a>

### [`00c146c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c146c0.md) → [`00c1475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1475c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e620.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6f0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c146c0.md#insn-00c14718) · [`00c14778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c146c0.md#insn-00c14778) · [`00c147a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c146c0.md#insn-00c147a0)
- 新版 [`00c147b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1475c.md#insn-00c147b4) · [`00c14814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1475c.md#insn-00c14814) · [`00c1483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c1475c.md#insn-00c1483c)

~~~diff
- 00c14718 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14718 ["INT_ADD", "register:40f0:8", ["const:c14718:8", "const:4:8"]]
- 00c14718 ["CALLIND", null, ["register:0:8"]]
+ 00c147b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c147b4 ["INT_ADD", "register:40f0:8", ["const:c147b4:8", "const:4:8"]]
+ 00c147b4 ["CALLIND", null, ["register:0:8"]]
- 00c14718 bytes 00013fd6
+ 00c147b4 bytes 00013fd6
- 00c14778 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14778 ["INT_ADD", "register:40f0:8", ["const:c14778:8", "const:4:8"]]
- 00c14778 ["CALLIND", null, ["register:0:8"]]
+ 00c14814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14814 ["INT_ADD", "register:40f0:8", ["const:c14814:8", "const:4:8"]]
+ 00c14814 ["CALLIND", null, ["register:0:8"]]
- 00c14778 bytes 00013fd6
+ 00c14814 bytes 00013fd6
- 00c147a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c147a0 ["INT_ADD", "register:40f0:8", ["const:c147a0:8", "const:4:8"]]
- 00c147a0 ["CALLIND", null, ["register:0:8"]]
+ 00c1483c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1483c ["INT_ADD", "register:40f0:8", ["const:c1483c:8", "const:4:8"]]
+ 00c1483c ["CALLIND", null, ["register:0:8"]]
- 00c147a0 bytes 00013fd6
+ 00c1483c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85888f090f65d437974448331c069e41"></a>

### [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md) → [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md) FUN_00c14948

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00c13890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13890.md) [`00c139ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c139ac.md) [`00c13a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13a14.md) [`00c14094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14094.md) [`00c140f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c140f8.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00c1392c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1392c.md) [`00c13a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13a48.md) [`00c13ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13ab0.md) [`00c14130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14130.md) [`00c14194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14194.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c14904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md#insn-00c14904) · [`00c14970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md#insn-00c14970) · [`00c1499c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md#insn-00c1499c)
- 新版 [`00c149a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md#insn-00c149a0) · [`00c14a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md#insn-00c14a0c) · [`00c14a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md#insn-00c14a38)

~~~diff
- 00c14904 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14904 ["INT_ADD", "register:40f0:8", ["const:c14904:8", "const:4:8"]]
- 00c14904 ["CALLIND", null, ["register:0:8"]]
+ 00c149a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c149a0 ["INT_ADD", "register:40f0:8", ["const:c149a0:8", "const:4:8"]]
+ 00c149a0 ["CALLIND", null, ["register:0:8"]]
- 00c14904 bytes 00013fd6
+ 00c149a0 bytes 00013fd6
- 00c14970 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c14970 ["INT_ADD", "register:40f0:8", ["const:c14970:8", "const:4:8"]]
- 00c14970 ["CALLIND", null, ["register:0:8"]]
+ 00c14a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14a0c ["INT_ADD", "register:40f0:8", ["const:c14a0c:8", "const:4:8"]]
+ 00c14a0c ["CALLIND", null, ["register:0:8"]]
- 00c14970 bytes 00013fd6
+ 00c14a0c bytes 00013fd6
- 00c1499c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1499c ["INT_ADD", "register:40f0:8", ["const:c1499c:8", "const:4:8"]]
- 00c1499c ["CALLIND", null, ["register:0:8"]]
+ 00c14a38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14a38 ["INT_ADD", "register:40f0:8", ["const:c14a38:8", "const:4:8"]]
+ 00c14a38 ["CALLIND", null, ["register:0:8"]]
- 00c1499c bytes 00013fd6
+ 00c14a38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e81037e5ff645087b6de252386ec5c8"></a>

### [`00c15130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15130.md) → [`00c151cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c151cc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15130.md#insn-00c15168)
- 新版 [`00c15204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c151cc.md#insn-00c15204)

~~~diff
- 00c15168 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c15168 ["INT_ADD", "register:40f0:8", ["const:c15168:8", "const:4:8"]]
- 00c15168 ["CALLIND", null, ["register:0:8"]]
+ 00c15204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c15204 ["INT_ADD", "register:40f0:8", ["const:c15204:8", "const:4:8"]]
+ 00c15204 ["CALLIND", null, ["register:0:8"]]
- 00c15168 bytes 00013fd6
+ 00c15204 bytes 00013fd6
~~~


<a id="compare-9b77d9068da9f1cb6d8900eb8f292b69"></a>

### [`00c15318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15318.md) → [`00c153b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c153b4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1534c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15318.md#insn-00c1534c) · [`00c15370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15318.md#insn-00c15370)
- 新版 [`00c153e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c153b4.md#insn-00c153e8) · [`00c1540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c153b4.md#insn-00c1540c)

~~~diff
- 00c1534c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1534c ["INT_ADD", "register:40f0:8", ["const:c1534c:8", "const:4:8"]]
- 00c1534c ["CALLIND", null, ["register:0:8"]]
+ 00c153e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c153e8 ["INT_ADD", "register:40f0:8", ["const:c153e8:8", "const:4:8"]]
+ 00c153e8 ["CALLIND", null, ["register:0:8"]]
- 00c1534c bytes 00013fd6
+ 00c153e8 bytes 00013fd6
- 00c15370 ["INT_ADD", "register:40f0:8", ["const:c15370:8", "const:4:8"]]
- 00c15370 ["CALL", null, ["callee:00c0b08c:8"]]
+ 00c1540c ["INT_ADD", "register:40f0:8", ["const:c1540c:8", "const:4:8"]]
+ 00c1540c ["CALL", null, ["callee:00c0b08c:8"]]
- 00c15370 bytes 20d7ff97
+ 00c1540c bytes 20d7ff97
~~~


<a id="compare-710e2b115392fa255a28d5a92176b690"></a>

### [`00c15524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15524.md) → [`00c155c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c155c0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15524.md#insn-00c15558) · [`00c1557c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15524.md#insn-00c1557c)
- 新版 [`00c155f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c155c0.md#insn-00c155f4) · [`00c15618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c155c0.md#insn-00c15618)

~~~diff
- 00c15558 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c15558 ["INT_ADD", "register:40f0:8", ["const:c15558:8", "const:4:8"]]
- 00c15558 ["CALLIND", null, ["register:0:8"]]
+ 00c155f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c155f4 ["INT_ADD", "register:40f0:8", ["const:c155f4:8", "const:4:8"]]
+ 00c155f4 ["CALLIND", null, ["register:0:8"]]
- 00c15558 bytes 00013fd6
+ 00c155f4 bytes 00013fd6
- 00c1557c ["INT_ADD", "register:40f0:8", ["const:c1557c:8", "const:4:8"]]
- 00c1557c ["CALL", null, ["callee:00c0b08c:8"]]
+ 00c15618 ["INT_ADD", "register:40f0:8", ["const:c15618:8", "const:4:8"]]
+ 00c15618 ["CALL", null, ["callee:00c0b08c:8"]]
- 00c1557c bytes 9dd6ff97
+ 00c15618 bytes 9dd6ff97
~~~


<a id="compare-a21f2d4e3f9e7c1ff659f0c5435b2c77"></a>

### [`00c156f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c156f4.md) → [`00c15790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15790.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c156f4.md#insn-00c15720)
- 新版 [`00c157bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15790.md#insn-00c157bc)

~~~diff
- 00c15720 ["INT_ADD", "register:40f0:8", ["const:c15720:8", "const:4:8"]]
- 00c15720 ["CALL", null, ["callee:00c1668c:8"]]
+ 00c157bc ["INT_ADD", "register:40f0:8", ["const:c157bc:8", "const:4:8"]]
+ 00c157bc ["CALL", null, ["callee:00c1668c:8"]]
- 00c15720 bytes b4030094
+ 00c157bc bytes b4030094
~~~


<a id="compare-0024ec88c67b822e8fd0256b7a558cab"></a>

### [`00c15dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15dcc.md) → [`00c15e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15e68.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15dcc.md#insn-00c15df8)
- 新版 [`00c15e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15e68.md#insn-00c15e94)

~~~diff
- 00c15df8 ["INT_ADD", "register:40f0:8", ["const:c15df8:8", "const:4:8"]]
- 00c15df8 ["CALL", null, ["callee:00c1668c:8"]]
+ 00c15e94 ["INT_ADD", "register:40f0:8", ["const:c15e94:8", "const:4:8"]]
+ 00c15e94 ["CALL", null, ["callee:00c1668c:8"]]
- 00c15df8 bytes fe010094
+ 00c15e94 bytes fe010094
~~~


<a id="compare-610e023d302a597d94104ce69e3d2d01"></a>

### [`00c15e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15e30.md) → [`00c15ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15ecc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15e30.md#insn-00c15e5c)
- 新版 [`00c15ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15ecc.md#insn-00c15ef8)

~~~diff
- 00c15e5c ["INT_ADD", "register:40f0:8", ["const:c15e5c:8", "const:4:8"]]
- 00c15e5c ["CALL", null, ["callee:00c1668c:8"]]
+ 00c15ef8 ["INT_ADD", "register:40f0:8", ["const:c15ef8:8", "const:4:8"]]
+ 00c15ef8 ["CALL", null, ["callee:00c1668c:8"]]
- 00c15e5c bytes e5010094
+ 00c15ef8 bytes e5010094
~~~


<a id="compare-d4c0f8c31fb4d1f4cbbb5fb518143de1"></a>

### [`00c15e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15e90.md) → [`00c15f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15f2c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15e90.md#insn-00c15ebc)
- 新版 [`00c15f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15f2c.md#insn-00c15f58)

~~~diff
- 00c15ebc ["INT_ADD", "register:40f0:8", ["const:c15ebc:8", "const:4:8"]]
- 00c15ebc ["CALL", null, ["callee:00c1668c:8"]]
+ 00c15f58 ["INT_ADD", "register:40f0:8", ["const:c15f58:8", "const:4:8"]]
+ 00c15f58 ["CALL", null, ["callee:00c1668c:8"]]
- 00c15ebc bytes cd010094
+ 00c15f58 bytes cd010094
~~~


<a id="compare-b9bcf7fc7cf3cbea6ee91c99b842eb07"></a>

### [`00c15ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15ef4.md) → [`00c15f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15f90.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15ef4.md#insn-00c15f20)
- 新版 [`00c15fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15f90.md#insn-00c15fbc)

~~~diff
- 00c15f20 ["INT_ADD", "register:40f0:8", ["const:c15f20:8", "const:4:8"]]
- 00c15f20 ["CALL", null, ["callee:00c1668c:8"]]
+ 00c15fbc ["INT_ADD", "register:40f0:8", ["const:c15fbc:8", "const:4:8"]]
+ 00c15fbc ["CALL", null, ["callee:00c1668c:8"]]
- 00c15f20 bytes b4010094
+ 00c15fbc bytes b4010094
~~~


<a id="compare-3aef56fd2fd91fc6a5b3b7f7ec685cf2"></a>

### [`00c15f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15f54.md) → [`00c15ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15ff0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15f54.md#insn-00c15f80)
- 新版 [`00c1601c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15ff0.md#insn-00c1601c)

~~~diff
- 00c15f80 ["INT_ADD", "register:40f0:8", ["const:c15f80:8", "const:4:8"]]
- 00c15f80 ["CALL", null, ["callee:00c1668c:8"]]
+ 00c1601c ["INT_ADD", "register:40f0:8", ["const:c1601c:8", "const:4:8"]]
+ 00c1601c ["CALL", null, ["callee:00c1668c:8"]]
- 00c15f80 bytes 9c010094
+ 00c1601c bytes 9c010094
~~~


<a id="compare-dae0e5f1adb3144d94940c9b80ca9f0a"></a>

### [`00c15fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15fb8.md) → [`00c16054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16054.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c15fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15fb8.md#insn-00c15fe4)
- 新版 [`00c16080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16054.md#insn-00c16080)

~~~diff
- 00c15fe4 ["INT_ADD", "register:40f0:8", ["const:c15fe4:8", "const:4:8"]]
- 00c15fe4 ["CALL", null, ["callee:00c1668c:8"]]
+ 00c16080 ["INT_ADD", "register:40f0:8", ["const:c16080:8", "const:4:8"]]
+ 00c16080 ["CALL", null, ["callee:00c1668c:8"]]
- 00c15fe4 bytes 83010094
+ 00c16080 bytes 83010094
~~~


<a id="compare-f25d78fe6dc9c58ecb879842e5002db1"></a>

### [`00c16018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16018.md) → [`00c160b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c160b4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e640.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e710.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c16094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16018.md#insn-00c16094) · [`00c160d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16018.md#insn-00c160d0) · [`00c16110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16018.md#insn-00c16110)
- 新版 [`00c16130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c160b4.md#insn-00c16130) · [`00c1616c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c160b4.md#insn-00c1616c) · [`00c161ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c160b4.md#insn-00c161ac)

~~~diff
- 00c16094 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c16094 ["INT_ADD", "register:40f0:8", ["const:c16094:8", "const:4:8"]]
- 00c16094 ["CALLIND", null, ["register:0:8"]]
+ 00c16130 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16130 ["INT_ADD", "register:40f0:8", ["const:c16130:8", "const:4:8"]]
+ 00c16130 ["CALLIND", null, ["register:0:8"]]
- 00c16094 bytes 00013fd6
+ 00c16130 bytes 00013fd6
- 00c160d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c160d0 ["INT_ADD", "register:40f0:8", ["const:c160d0:8", "const:4:8"]]
- 00c160d0 ["CALLIND", null, ["register:0:8"]]
+ 00c1616c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1616c ["INT_ADD", "register:40f0:8", ["const:c1616c:8", "const:4:8"]]
+ 00c1616c ["CALLIND", null, ["register:0:8"]]
- 00c160d0 bytes 00013fd6
+ 00c1616c bytes 00013fd6
- 00c16110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c16110 ["INT_ADD", "register:40f0:8", ["const:c16110:8", "const:4:8"]]
- 00c16110 ["CALLIND", null, ["register:0:8"]]
+ 00c161ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c161ac ["INT_ADD", "register:40f0:8", ["const:c161ac:8", "const:4:8"]]
+ 00c161ac ["CALLIND", null, ["register:0:8"]]
- 00c16110 bytes 00013fd6
+ 00c161ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1350afe0eebdd90cfd27c2f60693cf72"></a>

### [`00c16208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16208.md) → [`00c162a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c162a4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1623c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16208.md#insn-00c1623c) · [`00c162a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16208.md#insn-00c162a0)
- 新版 [`00c162d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c162a4.md#insn-00c162d8) · [`00c1633c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c162a4.md#insn-00c1633c)

~~~diff
- 00c1623c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1623c ["INT_ADD", "register:40f0:8", ["const:c1623c:8", "const:4:8"]]
- 00c1623c ["CALLIND", null, ["register:0:8"]]
+ 00c162d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c162d8 ["INT_ADD", "register:40f0:8", ["const:c162d8:8", "const:4:8"]]
+ 00c162d8 ["CALLIND", null, ["register:0:8"]]
- 00c1623c bytes 00013fd6
+ 00c162d8 bytes 00013fd6
- 00c162a0 ["INT_ADD", "register:40f0:8", ["const:c162a0:8", "const:4:8"]]
- 00c162a0 ["CALL", null, ["callee:00c0b08c:8"]]
+ 00c1633c ["INT_ADD", "register:40f0:8", ["const:c1633c:8", "const:4:8"]]
+ 00c1633c ["CALL", null, ["callee:00c0b08c:8"]]
- 00c162a0 bytes 54d3ff97
+ 00c1633c bytes 54d3ff97
~~~


<a id="compare-0809efad8f6f103e3fd55a12fe4fdd61"></a>

### [`00c162f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c162f0.md) → [`00c1638c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1638c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1631c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c162f0.md#insn-00c1631c)
- 新版 [`00c163b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1638c.md#insn-00c163b8)

~~~diff
- 00c1631c ["INT_ADD", "register:40f0:8", ["const:c1631c:8", "const:4:8"]]
- 00c1631c ["CALL", null, ["callee:00c1668c:8"]]
+ 00c163b8 ["INT_ADD", "register:40f0:8", ["const:c163b8:8", "const:4:8"]]
+ 00c163b8 ["CALL", null, ["callee:00c1668c:8"]]
- 00c1631c bytes b5000094
+ 00c163b8 bytes b5000094
~~~


<a id="compare-4be90b4f8c3c178a810f19068c0da43a"></a>

### [`00c16350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16350.md) → [`00c163ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c163ec.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1637c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16350.md#insn-00c1637c)
- 新版 [`00c16418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c163ec.md#insn-00c16418)

~~~diff
- 00c1637c ["INT_ADD", "register:40f0:8", ["const:c1637c:8", "const:4:8"]]
- 00c1637c ["CALL", null, ["callee:00c1668c:8"]]
+ 00c16418 ["INT_ADD", "register:40f0:8", ["const:c16418:8", "const:4:8"]]
+ 00c16418 ["CALL", null, ["callee:00c1668c:8"]]
- 00c1637c bytes 9d000094
+ 00c16418 bytes 9d000094
~~~


<a id="compare-ea920da4610eefe29421abc83ff487c7"></a>

### [`00c163b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c163b0.md) → [`00c1644c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1644c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c163dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c163b0.md#insn-00c163dc)
- 新版 [`00c16478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1644c.md#insn-00c16478)

~~~diff
- 00c163dc ["INT_ADD", "register:40f0:8", ["const:c163dc:8", "const:4:8"]]
- 00c163dc ["CALL", null, ["callee:00c1668c:8"]]
+ 00c16478 ["INT_ADD", "register:40f0:8", ["const:c16478:8", "const:4:8"]]
+ 00c16478 ["CALL", null, ["callee:00c1668c:8"]]
- 00c163dc bytes 85000094
+ 00c16478 bytes 85000094
~~~


<a id="compare-3a70b443cd1ad17c0cd843746a08c993"></a>

### [`00c16400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16400.md) → [`00c1649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1649c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e650.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e720.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1646c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16400.md#insn-00c1646c) · [`00c164a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16400.md#insn-00c164a4) · [`00c164e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16400.md#insn-00c164e4)
- 新版 [`00c16508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1649c.md#insn-00c16508) · [`00c16540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1649c.md#insn-00c16540) · [`00c16580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1649c.md#insn-00c16580)

~~~diff
- 00c1646c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1646c ["INT_ADD", "register:40f0:8", ["const:c1646c:8", "const:4:8"]]
- 00c1646c ["CALLIND", null, ["register:0:8"]]
+ 00c16508 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16508 ["INT_ADD", "register:40f0:8", ["const:c16508:8", "const:4:8"]]
+ 00c16508 ["CALLIND", null, ["register:0:8"]]
- 00c1646c bytes 00013fd6
+ 00c16508 bytes 00013fd6
- 00c164a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c164a4 ["INT_ADD", "register:40f0:8", ["const:c164a4:8", "const:4:8"]]
- 00c164a4 ["CALLIND", null, ["register:0:8"]]
+ 00c16540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16540 ["INT_ADD", "register:40f0:8", ["const:c16540:8", "const:4:8"]]
+ 00c16540 ["CALLIND", null, ["register:0:8"]]
- 00c164a4 bytes 00013fd6
+ 00c16540 bytes 00013fd6
- 00c164e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c164e4 ["INT_ADD", "register:40f0:8", ["const:c164e4:8", "const:4:8"]]
- 00c164e4 ["CALLIND", null, ["register:0:8"]]
+ 00c16580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16580 ["INT_ADD", "register:40f0:8", ["const:c16580:8", "const:4:8"]]
+ 00c16580 ["CALLIND", null, ["register:0:8"]]
- 00c164e4 bytes 00013fd6
+ 00c16580 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5b22d0fa78e53ee9c407e7f17dcd9ed"></a>

### [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md) → [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md) FUN_00c1668c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00c155d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c155d8.md) [`00c156f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c156f4.md) [`00c1575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c1575c.md) [`00c15dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15dcc.md) [`00c15e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15e30.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00c15674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15674.md) [`00c15790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15790.md) [`00c157f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c157f8.md) [`00c15e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15e68.md) [`00c15ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15ecc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c16664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md#insn-00c16664) · [`00c1669c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md#insn-00c1669c) · [`00c166e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md#insn-00c166e0)
- 新版 [`00c16700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md#insn-00c16700) · [`00c16738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md#insn-00c16738) · [`00c1677c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md#insn-00c1677c)

~~~diff
- 00c16664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c16664 ["INT_ADD", "register:40f0:8", ["const:c16664:8", "const:4:8"]]
- 00c16664 ["CALLIND", null, ["register:0:8"]]
+ 00c16700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16700 ["INT_ADD", "register:40f0:8", ["const:c16700:8", "const:4:8"]]
+ 00c16700 ["CALLIND", null, ["register:0:8"]]
- 00c16664 bytes 00013fd6
+ 00c16700 bytes 00013fd6
- 00c1669c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1669c ["INT_ADD", "register:40f0:8", ["const:c1669c:8", "const:4:8"]]
- 00c1669c ["CALLIND", null, ["register:0:8"]]
+ 00c16738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16738 ["INT_ADD", "register:40f0:8", ["const:c16738:8", "const:4:8"]]
+ 00c16738 ["CALLIND", null, ["register:0:8"]]
- 00c1669c bytes 00013fd6
+ 00c16738 bytes 00013fd6
- 00c166e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c166e0 ["INT_ADD", "register:40f0:8", ["const:c166e0:8", "const:4:8"]]
- 00c166e0 ["CALLIND", null, ["register:0:8"]]
+ 00c1677c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1677c ["INT_ADD", "register:40f0:8", ["const:c1677c:8", "const:4:8"]]
+ 00c1677c ["CALLIND", null, ["register:0:8"]]
- 00c166e0 bytes 00013fd6
+ 00c1677c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc33eab8e935be5d15375309fce4f0d4"></a>

### [`00c16bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16bec.md) → [`00c16c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16c88.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPK2tmcc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c16c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16bec.md#insn-00c16c40) · [`00c16c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16bec.md#insn-00c16c60)
- 新版 [`00c16cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16c88.md#insn-00c16cdc) · [`00c16cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16c88.md#insn-00c16cfc)

~~~diff
- 00c16c40 ["INT_ADD", "register:40f0:8", ["const:c16c40:8", "const:4:8"]]
- 00c16c40 ["CALL", null, ["callee:00c5e730:8"]]
+ 00c16cdc ["INT_ADD", "register:40f0:8", ["const:c16cdc:8", "const:4:8"]]
+ 00c16cdc ["CALL", null, ["callee:00c5e730:8"]]
- 00c16c40 bytes 881e0194
+ 00c16cdc bytes 951e0194
- 00c16c60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c16c60 ["INT_ADD", "register:40f0:8", ["const:c16c60:8", "const:4:8"]]
- 00c16c60 ["CALLIND", null, ["register:0:8"]]
+ 00c16cfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c16cfc ["INT_ADD", "register:40f0:8", ["const:c16cfc:8", "const:4:8"]]
+ 00c16cfc ["CALLIND", null, ["register:0:8"]]
- 00c16c60 bytes 00013fd6
+ 00c16cfc bytes 00013fd6
~~~


<a id="compare-c69c0363ecb1243c81e8db20e3639e0d"></a>

### [`00c16cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16cb8.md) → [`00c16d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16d54.md) _ZNKSt6__ndk110__time_put8__do_putEPcRS1_PK2tmcc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c16d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16cb8.md#insn-00c16d0c)
- 新版 [`00c16da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16d54.md#insn-00c16da8)

~~~diff
- 00c16d0c ["INT_ADD", "register:40f0:8", ["const:c16d0c:8", "const:4:8"]]
- 00c16d0c ["CALL", null, ["callee:00c5e730:8"]]
+ 00c16da8 ["INT_ADD", "register:40f0:8", ["const:c16da8:8", "const:4:8"]]
+ 00c16da8 ["CALL", null, ["callee:00c5e730:8"]]
- 00c16d0c bytes 551e0194
+ 00c16da8 bytes 621e0194
~~~


<a id="compare-97eb3ae9f1023c63ca2b37d968678cff"></a>

### [`00c16fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md) → [`00c17078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17078.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPK2tmcc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e670.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md#insn-00c1701c) · [`00c17070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md#insn-00c17070)
- 新版 [`00c170b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17078.md#insn-00c170b8) · [`00c1710c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17078.md#insn-00c1710c)

~~~diff
- 00c1701c ["INT_ADD", "register:40f0:8", ["const:c1701c:8", "const:4:8"]]
- 00c1701c ["CALL", null, ["callee:00c5e740:8"]]
+ 00c170b8 ["INT_ADD", "register:40f0:8", ["const:c170b8:8", "const:4:8"]]
+ 00c170b8 ["CALL", null, ["callee:00c5e740:8"]]
- 00c1701c bytes 951d0194
+ 00c170b8 bytes a21d0194
- 00c17070 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c17070 ["INT_ADD", "register:40f0:8", ["const:c17070:8", "const:4:8"]]
- 00c17070 ["CALLIND", null, ["register:0:8"]]
+ 00c1710c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1710c ["INT_ADD", "register:40f0:8", ["const:c1710c:8", "const:4:8"]]
+ 00c1710c ["CALLIND", null, ["register:0:8"]]
- 00c17070 bytes 00013fd6
+ 00c1710c bytes 00013fd6
~~~


<a id="compare-b8bad68c65e2c5561625868de4248417"></a>

### [`00c18fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md) → [`00c19060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19060.md) FUN_00c19060

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c18d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18d04.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c18da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c18/00c18da0.md) · 呼出先 6件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c190fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c190fc) · [`00c1911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c1911c) · [`00c19178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c19178)
- 新版 [`00c19198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19060.md#insn-00c19198) · [`00c191b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19060.md#insn-00c191b8) · [`00c19214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19060.md#insn-00c19214)

~~~diff
- 00c190fc ["INT_ADD", "register:40f0:8", ["const:c190fc:8", "const:4:8"]]
- 00c190fc ["CALL", null, ["callee:00c57f60:8"]]
+ 00c19198 ["INT_ADD", "register:40f0:8", ["const:c19198:8", "const:4:8"]]
+ 00c19198 ["CALL", null, ["callee:00c57f60:8"]]
- 00c190fc bytes 65fb0094
+ 00c19198 bytes 72fb0094
- 00c1911c ["INT_ADD", "register:40f0:8", ["const:c1911c:8", "const:4:8"]]
- 00c1911c ["CALL", null, ["callee:00c580d0:8"]]
+ 00c191b8 ["INT_ADD", "register:40f0:8", ["const:c191b8:8", "const:4:8"]]
+ 00c191b8 ["CALL", null, ["callee:00c580d0:8"]]
- 00c1911c bytes b9fb0094
+ 00c191b8 bytes c6fb0094
- 00c19178 ["INT_ADD", "register:40f0:8", ["const:c19178:8", "const:4:8"]]
- 00c19178 ["CALL", null, ["callee:00c5b170:8"]]
+ 00c19214 ["INT_ADD", "register:40f0:8", ["const:c19214:8", "const:4:8"]]
+ 00c19214 ["CALL", null, ["callee:00c5b170:8"]]
- 00c19178 bytes ca070194
+ 00c19214 bytes d7070194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f273a5a0873f105646ae2686d5d662b9"></a>

### [`00c1afec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md) → [`00c1b088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b088.md) FUN_00c1b088

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c1acc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1acc0.md) · 呼出先 8件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c1ad5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1a/00c1ad5c.md) · 呼出先 8件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b0dc) · [`00c1b158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b158) · [`00c1b188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b188)
- 新版 [`00c1b178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b088.md#insn-00c1b178) · [`00c1b1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b088.md#insn-00c1b1f4) · [`00c1b224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b088.md#insn-00c1b224)

~~~diff
- 00c1b0dc ["INT_ADD", "register:40f0:8", ["const:c1b0dc:8", "const:4:8"]]
- 00c1b0dc ["CALL", null, ["callee:00c5a970:8"]]
+ 00c1b178 ["INT_ADD", "register:40f0:8", ["const:c1b178:8", "const:4:8"]]
+ 00c1b178 ["CALL", null, ["callee:00c5a970:8"]]
- 00c1b0dc bytes f1fd0094
+ 00c1b178 bytes fefd0094
- 00c1b158 ["INT_ADD", "register:40f0:8", ["const:c1b158:8", "const:4:8"]]
- 00c1b158 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c1b1f4 ["INT_ADD", "register:40f0:8", ["const:c1b1f4:8", "const:4:8"]]
+ 00c1b1f4 ["CALL", null, ["callee:00c57f60:8"]]
- 00c1b158 bytes 4ef30094
+ 00c1b1f4 bytes 5bf30094
- 00c1b188 ["INT_ADD", "register:40f0:8", ["const:c1b188:8", "const:4:8"]]
- 00c1b188 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c1b224 ["INT_ADD", "register:40f0:8", ["const:c1b224:8", "const:4:8"]]
+ 00c1b224 ["CALL", null, ["callee:00c580d0:8"]]
- 00c1b188 bytes 9ef30094
+ 00c1b224 bytes abf30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd9dedd74a424d6523ff1575b1ade9c"></a>

### [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) → [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) FUN_00c1ba7c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00c0f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f678.md) [`00c0fb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0fb08.md) [`00c10dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10dac.md) [`00c1123c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1123c.md) [`00c1b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b534.md) · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5e700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e700.md)
- 新版 呼出元 6件 [`00c0f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f714.md) [`00c0fba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fba4.md) [`00c10e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md) [`00c112d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112d8.md) [`00c1b5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b5d0.md) · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5e7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1ba44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba44) · [`00c1ba64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba64) · [`00c1ba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba74)
- 新版 [`00c1bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md#insn-00c1bae0) · [`00c1bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md#insn-00c1bb00) · [`00c1bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md#insn-00c1bb10)

~~~diff
- 00c1ba44 ["INT_ADD", "register:40f0:8", ["const:c1ba44:8", "const:4:8"]]
- 00c1ba44 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c1bae0 ["INT_ADD", "register:40f0:8", ["const:c1bae0:8", "const:4:8"]]
+ 00c1bae0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c1ba44 bytes cb0a0194
+ 00c1bae0 bytes d80a0194
- 00c1ba64 ["INT_ADD", "register:40f0:8", ["const:c1ba64:8", "const:4:8"]]
- 00c1ba64 ["CALL", null, ["callee:00c5e7d0:8"]]
+ 00c1bb00 ["INT_ADD", "register:40f0:8", ["const:c1bb00:8", "const:4:8"]]
+ 00c1bb00 ["CALL", null, ["callee:00c5e7d0:8"]]
- 00c1ba64 bytes 270b0194
+ 00c1bb00 bytes 340b0194
- 00c1ba74 ["INT_ADD", "register:40f0:8", ["const:c1ba74:8", "const:4:8"]]
- 00c1ba74 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c1bb10 ["INT_ADD", "register:40f0:8", ["const:c1bb10:8", "const:4:8"]]
+ 00c1bb10 ["CALL", null, ["callee:00c5e640:8"]]
- 00c1ba74 bytes bf0a0194
+ 00c1bb10 bytes cc0a0194
~~~


<a id="compare-398d7106c8d30b15b5684768c7071bdc"></a>

### [`00c1bcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md) → [`00c1bd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1bd5c.md) _ZNSt6__ndk111__money_putIcE8__formatEPcRS2_S3_jPKcS5_RKNS_5ctypeIcEEbRKNS_10money_base7patternEccRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e6f0.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e7c0.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1be5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1be5c) · [`00c1beb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1beb8) · [`00c1bf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1bf1c)
- 新版 [`00c1bef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1bd5c.md#insn-00c1bef8) · [`00c1bf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1bd5c.md#insn-00c1bf54) · [`00c1bfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1bd5c.md#insn-00c1bfb8)

~~~diff
- 00c1be5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1be5c ["INT_ADD", "register:40f0:8", ["const:c1be5c:8", "const:4:8"]]
- 00c1be5c ["CALLIND", null, ["register:0:8"]]
+ 00c1bef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1bef8 ["INT_ADD", "register:40f0:8", ["const:c1bef8:8", "const:4:8"]]
+ 00c1bef8 ["CALLIND", null, ["register:0:8"]]
- 00c1be5c bytes 00013fd6
+ 00c1bef8 bytes 00013fd6
- 00c1beb8 ["INT_ADD", "register:40f0:8", ["const:c1beb8:8", "const:4:8"]]
- 00c1beb8 ["CALL", null, ["callee:00c58010:8"]]
+ 00c1bf54 ["INT_ADD", "register:40f0:8", ["const:c1bf54:8", "const:4:8"]]
+ 00c1bf54 ["CALL", null, ["callee:00c58010:8"]]
- 00c1beb8 bytes 22f00094
+ 00c1bf54 bytes 2ff00094
- 00c1bf1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1bf1c ["INT_ADD", "register:40f0:8", ["const:c1bf1c:8", "const:4:8"]]
- 00c1bf1c ["CALLIND", null, ["register:0:8"]]
+ 00c1bfb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1bfb8 ["INT_ADD", "register:40f0:8", ["const:c1bfb8:8", "const:4:8"]]
+ 00c1bfb8 ["CALLIND", null, ["register:0:8"]]
- 00c1bf1c bytes 00013fd6
+ 00c1bfb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af33fd5affb05d36b26ba56dfbfa8cc1"></a>

### [`00c1cb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md) → [`00c1cc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1cc18.md) _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e720.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5e7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e7f0.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1cc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cc88) · [`00c1cd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cd10) · [`00c1cd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cd68)
- 新版 [`00c1cd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1cc18.md#insn-00c1cd24) · [`00c1cdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1cc18.md#insn-00c1cdac) · [`00c1ce04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1cc18.md#insn-00c1ce04)

~~~diff
- 00c1cc88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1cc88 ["INT_ADD", "register:40f0:8", ["const:c1cc88:8", "const:4:8"]]
- 00c1cc88 ["CALLIND", null, ["register:0:8"]]
+ 00c1cd24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1cd24 ["INT_ADD", "register:40f0:8", ["const:c1cd24:8", "const:4:8"]]
+ 00c1cd24 ["CALLIND", null, ["register:0:8"]]
- 00c1cc88 bytes 00013fd6
+ 00c1cd24 bytes 00013fd6
- 00c1cd10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1cd10 ["INT_ADD", "register:40f0:8", ["const:c1cd10:8", "const:4:8"]]
- 00c1cd10 ["CALLIND", null, ["register:0:8"]]
+ 00c1cdac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1cdac ["INT_ADD", "register:40f0:8", ["const:c1cdac:8", "const:4:8"]]
+ 00c1cdac ["CALLIND", null, ["register:0:8"]]
- 00c1cd10 bytes 00013fd6
+ 00c1cdac bytes 00013fd6
- 00c1cd68 ["INT_ADD", "register:40f0:8", ["const:c1cd68:8", "const:4:8"]]
- 00c1cd68 ["CALL", null, ["callee:00c58010:8"]]
+ 00c1ce04 ["INT_ADD", "register:40f0:8", ["const:c1ce04:8", "const:4:8"]]
+ 00c1ce04 ["CALL", null, ["callee:00c58010:8"]]
- 00c1cd68 bytes 76ec0094
+ 00c1ce04 bytes 83ec0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69885ed62849fa5b131a9be9d84e0be8"></a>

### [`00c1d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d430.md) → [`00c1d4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d4cc.md) _ZNSt6__ndk114codecvt_bynameIcc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d430.md#insn-00c1d444)
- 新版 [`00c1d4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d4cc.md#insn-00c1d4e0)

~~~diff
- 00c1d444 ["INT_ADD", "register:40f0:8", ["const:c1d444:8", "const:4:8"]]
- 00c1d444 ["CALL", null, ["callee:00c5e810:8"]]
+ 00c1d4e0 ["INT_ADD", "register:40f0:8", ["const:c1d4e0:8", "const:4:8"]]
+ 00c1d4e0 ["CALL", null, ["callee:00c5e810:8"]]
- 00c1d444 bytes bf040194
+ 00c1d4e0 bytes cc040194
~~~


<a id="compare-43ffcecf469242be9fefa8c6b3b9f14c"></a>

### [`00c1d464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d464.md) → [`00c1d500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d500.md) _ZNSt6__ndk114codecvt_bynameIwc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e750.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d464.md#insn-00c1d478)
- 新版 [`00c1d514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d500.md#insn-00c1d514)

~~~diff
- 00c1d478 ["INT_ADD", "register:40f0:8", ["const:c1d478:8", "const:4:8"]]
- 00c1d478 ["CALL", null, ["callee:00c5e820:8"]]
+ 00c1d514 ["INT_ADD", "register:40f0:8", ["const:c1d514:8", "const:4:8"]]
+ 00c1d514 ["CALL", null, ["callee:00c5e820:8"]]
- 00c1d478 bytes b6040194
+ 00c1d514 bytes c3040194
~~~


<a id="compare-a9674fe56d72a928eeb4e31f5497ed63"></a>

### [`00c1d498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d498.md) → [`00c1d534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d534.md) _ZNSt6__ndk114codecvt_bynameIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e770.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d498.md#insn-00c1d4ac)
- 新版 [`00c1d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d534.md#insn-00c1d548)

~~~diff
- 00c1d4ac ["INT_ADD", "register:40f0:8", ["const:c1d4ac:8", "const:4:8"]]
- 00c1d4ac ["CALL", null, ["callee:00c5e840:8"]]
+ 00c1d548 ["INT_ADD", "register:40f0:8", ["const:c1d548:8", "const:4:8"]]
+ 00c1d548 ["CALL", null, ["callee:00c5e840:8"]]
- 00c1d4ac bytes b1040194
+ 00c1d548 bytes be040194
~~~


<a id="compare-6c487cdf81f763961e9d9fa887d523bf"></a>

### [`00c1d4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d4cc.md) → [`00c1d568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d568.md) _ZNSt6__ndk114codecvt_bynameIDic9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d4cc.md#insn-00c1d4e0)
- 新版 [`00c1d57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d568.md#insn-00c1d57c)

~~~diff
- 00c1d4e0 ["INT_ADD", "register:40f0:8", ["const:c1d4e0:8", "const:4:8"]]
- 00c1d4e0 ["CALL", null, ["callee:00c5e860:8"]]
+ 00c1d57c ["INT_ADD", "register:40f0:8", ["const:c1d57c:8", "const:4:8"]]
+ 00c1d57c ["CALL", null, ["callee:00c5e860:8"]]
- 00c1d4e0 bytes ac040194
+ 00c1d57c bytes b9040194
~~~


<a id="compare-85e89f8a6fd9d725110b476d36d607df"></a>

### [`00c1d500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d500.md) → [`00c1d59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d59c.md) _ZNSt6__ndk114codecvt_bynameIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d500.md#insn-00c1d514)
- 新版 [`00c1d5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d59c.md#insn-00c1d5b0)

~~~diff
- 00c1d514 ["INT_ADD", "register:40f0:8", ["const:c1d514:8", "const:4:8"]]
- 00c1d514 ["CALL", null, ["callee:00c5e880:8"]]
+ 00c1d5b0 ["INT_ADD", "register:40f0:8", ["const:c1d5b0:8", "const:4:8"]]
+ 00c1d5b0 ["CALL", null, ["callee:00c5e880:8"]]
- 00c1d514 bytes a7040194
+ 00c1d5b0 bytes b4040194
~~~


<a id="compare-d7c0fd5d98e27c00aed71e78e581c62e"></a>

### [`00c1d534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d534.md) → [`00c1d5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5d0.md) _ZNSt6__ndk114codecvt_bynameIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d534.md#insn-00c1d548)
- 新版 [`00c1d5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5d0.md#insn-00c1d5e4)

~~~diff
- 00c1d548 ["INT_ADD", "register:40f0:8", ["const:c1d548:8", "const:4:8"]]
- 00c1d548 ["CALL", null, ["callee:00c5e8a0:8"]]
+ 00c1d5e4 ["INT_ADD", "register:40f0:8", ["const:c1d5e4:8", "const:4:8"]]
+ 00c1d5e4 ["CALL", null, ["callee:00c5e8a0:8"]]
- 00c1d548 bytes a2040194
+ 00c1d5e4 bytes af040194
~~~


<a id="compare-9ed053e42175e7f5c5c6c83187ddba87"></a>

### [`00c1d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) → [`00c1d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5fc.md) FUN_00c1d5fc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md#insn-00c1d650)
- 新版 [`00c1d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5fc.md#insn-00c1d6ec)

~~~diff
- 00c1d650 ["INT_ADD", "register:40f0:8", ["const:c1d650:8", "const:4:8"]]
- 00c1d650 ["CALL", null, ["callee:00c58120:8"]]
+ 00c1d6ec ["INT_ADD", "register:40f0:8", ["const:c1d6ec:8", "const:4:8"]]
+ 00c1d6ec ["CALL", null, ["callee:00c58120:8"]]
- 00c1d650 bytes 80ea0094
+ 00c1d6ec bytes 8dea0094
~~~


<a id="compare-9bd14081bf93762a5c0a2bae03faa5ca"></a>

### [`00c24c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24c7c.md) → [`00c24d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d18.md) FUN_00c24d18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c24ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24ba8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c24c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24c44.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c24c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24c7c.md#insn-00c24c90)
- 新版 [`00c24d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d18.md#insn-00c24d2c)

~~~diff
- 00c24c90 ["INT_ADD", "register:40f0:8", ["const:c24c90:8", "const:4:8"]]
- 00c24c90 ["CALL", null, ["callee:00c24c44:8"]]
+ 00c24d2c ["INT_ADD", "register:40f0:8", ["const:c24d2c:8", "const:4:8"]]
+ 00c24d2c ["CALL", null, ["callee:00c24c44:8"]]
- 00c24c90 bytes c6ffff97
+ 00c24d2c bytes c6ffff97
~~~


<a id="compare-25b0cdd02623092b722b1262b96cc5cd"></a>

### [`00c25034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md) → [`00c250d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c250d0.md) _ZNSt6__ndk16localeC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25054) · [`00c25064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25064) · [`00c25074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25074)
- 新版 [`00c250f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c250d0.md#insn-00c250f0) · [`00c25100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c250d0.md#insn-00c25100) · [`00c25110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c250d0.md#insn-00c25110)

~~~diff
- 00c25054 ["INT_ADD", "register:40f0:8", ["const:c25054:8", "const:4:8"]]
- 00c25054 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c250f0 ["INT_ADD", "register:40f0:8", ["const:c250f0:8", "const:4:8"]]
+ 00c250f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00c25054 bytes 8fcb0094
+ 00c250f0 bytes 9ccb0094
- 00c25064 ["INT_ADD", "register:40f0:8", ["const:c25064:8", "const:4:8"]]
- 00c25064 ["CALL", null, ["callee:00c1f528:8"]]
+ 00c25100 ["INT_ADD", "register:40f0:8", ["const:c25100:8", "const:4:8"]]
+ 00c25100 ["CALL", null, ["callee:00c1f528:8"]]
- 00c25064 bytes 0ae9ff97
+ 00c25100 bytes 0ae9ff97
- 00c25074 ["INT_ADD", "register:40f0:8", ["const:c25074:8", "const:4:8"]]
- 00c25074 ["CALL", null, ["callee:00c53d70:8"]]
+ 00c25110 ["INT_ADD", "register:40f0:8", ["const:c25110:8", "const:4:8"]]
+ 00c25110 ["CALL", null, ["callee:00c53d70:8"]]
- 00c25074 bytes 17bb0094
+ 00c25110 bytes 18bb0094
~~~


<a id="compare-8b51e4f697a5fb7e3653168d11942c4b"></a>

### [`00c251f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md) → [`00c2528c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2528c.md) _ZNSt6__ndk16localeC1ERKS0_RKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c25218) · [`00c2522c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c2522c) · [`00c2523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c2523c)
- 新版 [`00c252b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2528c.md#insn-00c252b4) · [`00c252c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2528c.md#insn-00c252c8) · [`00c252d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2528c.md#insn-00c252d8)

~~~diff
- 00c25218 ["INT_ADD", "register:40f0:8", ["const:c25218:8", "const:4:8"]]
- 00c25218 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c252b4 ["INT_ADD", "register:40f0:8", ["const:c252b4:8", "const:4:8"]]
+ 00c252b4 ["CALL", null, ["callee:00c57f60:8"]]
- 00c25218 bytes 1ecb0094
+ 00c252b4 bytes 2bcb0094
- 00c2522c ["INT_ADD", "register:40f0:8", ["const:c2522c:8", "const:4:8"]]
- 00c2522c ["CALL", null, ["callee:00c219c4:8"]]
+ 00c252c8 ["INT_ADD", "register:40f0:8", ["const:c252c8:8", "const:4:8"]]
+ 00c252c8 ["CALL", null, ["callee:00c219c4:8"]]
- 00c2522c bytes bff1ff97
+ 00c252c8 bytes bff1ff97
- 00c2523c ["INT_ADD", "register:40f0:8", ["const:c2523c:8", "const:4:8"]]
- 00c2523c ["CALL", null, ["callee:00c53d70:8"]]
+ 00c252d8 ["INT_ADD", "register:40f0:8", ["const:c252d8:8", "const:4:8"]]
+ 00c252d8 ["CALL", null, ["callee:00c53d70:8"]]
- 00c2523c bytes a5ba0094
+ 00c252d8 bytes a6ba0094
~~~


<a id="compare-8f26d7b3db60e916a3030f4dfdb3a299"></a>

### [`00c25268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md) → [`00c25304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25304.md) _ZNSt6__ndk16localeC1ERKS0_S2_i

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c25290) · [`00c252a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c252a4) · [`00c252b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c252b4)
- 新版 [`00c2532c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25304.md#insn-00c2532c) · [`00c25340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25304.md#insn-00c25340) · [`00c25350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25304.md#insn-00c25350)

~~~diff
- 00c25290 ["INT_ADD", "register:40f0:8", ["const:c25290:8", "const:4:8"]]
- 00c25290 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c2532c ["INT_ADD", "register:40f0:8", ["const:c2532c:8", "const:4:8"]]
+ 00c2532c ["CALL", null, ["callee:00c57f60:8"]]
- 00c25290 bytes 00cb0094
+ 00c2532c bytes 0dcb0094
- 00c252a4 ["INT_ADD", "register:40f0:8", ["const:c252a4:8", "const:4:8"]]
- 00c252a4 ["CALL", null, ["callee:00c22014:8"]]
+ 00c25340 ["INT_ADD", "register:40f0:8", ["const:c25340:8", "const:4:8"]]
+ 00c25340 ["CALL", null, ["callee:00c22014:8"]]
- 00c252a4 bytes 35f3ff97
+ 00c25340 bytes 35f3ff97
- 00c252b4 ["INT_ADD", "register:40f0:8", ["const:c252b4:8", "const:4:8"]]
- 00c252b4 ["CALL", null, ["callee:00c53d70:8"]]
+ 00c25350 ["INT_ADD", "register:40f0:8", ["const:c25350:8", "const:4:8"]]
+ 00c25350 ["CALL", null, ["callee:00c53d70:8"]]
- 00c252b4 bytes 87ba0094
+ 00c25350 bytes 88ba0094
~~~


<a id="compare-b121f9f046beb1c25a02807755334fa2"></a>

### [`00c25730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25730.md) → [`00c257cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c257cc.md) _ZNKSt6__ndk16localeeqERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c257dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25730.md#insn-00c257dc)
- 新版 [`00c25878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c257cc.md#insn-00c25878)

~~~diff
- 00c257dc ["INT_ADD", "register:40f0:8", ["const:c257dc:8", "const:4:8"]]
- 00c257dc ["CALL", null, ["callee:00c58120:8"]]
+ 00c25878 ["INT_ADD", "register:40f0:8", ["const:c25878:8", "const:4:8"]]
+ 00c25878 ["CALL", null, ["callee:00c58120:8"]]
- 00c257dc bytes 1dca0094
+ 00c25878 bytes 2aca0094
~~~


<a id="compare-0d0cefda1587cfdbf56cd28b23ef23af"></a>

### [`00c25820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25820.md) → [`00c258bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258bc.md) _ZNSt6__ndk16locale5facetD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e910.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25820.md#insn-00c25834)
- 新版 [`00c258d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258bc.md#insn-00c258d0)

~~~diff
- 00c25834 ["INT_ADD", "register:40f0:8", ["const:c25834:8", "const:4:8"]]
- 00c25834 ["CALL", null, ["callee:00c5e9e0:8"]]
+ 00c258d0 ["INT_ADD", "register:40f0:8", ["const:c258d0:8", "const:4:8"]]
+ 00c258d0 ["CALL", null, ["callee:00c5e9e0:8"]]
- 00c25834 bytes 37e40094
+ 00c258d0 bytes 44e40094
~~~


<a id="compare-f25ae1ddb409381f649644e89f0ae762"></a>

### [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) → [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) FUN_00c259d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`00c2585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c2585c.md) [`00c25ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ea0.md) [`00c27198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md) [`00c27710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md) [`00c282ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c282ac.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)
- 新版 呼出元 13件 [`00c258f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258f8.md) [`00c25f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25f3c.md) [`00c27234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md) [`00c277ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md) [`00c28348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28348.md) · 呼出先 2件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md#insn-00c25954) · [`00c25968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md#insn-00c25968)
- 新版 [`00c259f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md#insn-00c259f0) · [`00c25a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md#insn-00c25a04)

~~~diff
- 00c25954 ["INT_ADD", "register:40f0:8", ["const:c25954:8", "const:4:8"]]
- 00c25954 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c259f0 ["INT_ADD", "register:40f0:8", ["const:c259f0:8", "const:4:8"]]
+ 00c259f0 ["CALL", null, ["callee:00c580b0:8"]]
- 00c25954 bytes a3c90094
+ 00c259f0 bytes b0c90094
- 00c25968 ["INT_ADD", "register:40f0:8", ["const:c25968:8", "const:4:8"]]
- 00c25968 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c25a04 ["INT_ADD", "register:40f0:8", ["const:c25a04:8", "const:4:8"]]
+ 00c25a04 ["CALL", null, ["callee:00c590a0:8"]]
- 00c25968 bytes 9acd0094
+ 00c25a04 bytes a7cd0094
~~~


<a id="compare-5024ff0b94ae09f6e97a0b227f4621a0"></a>

### [`00c25aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25aa0.md) → [`00c25b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b3c.md) _ZNSt6__ndk114collate_bynameIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25aa0.md#insn-00c25ab4)
- 新版 [`00c25b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b3c.md#insn-00c25b50)

~~~diff
- 00c25ab4 ["INT_ADD", "register:40f0:8", ["const:c25ab4:8", "const:4:8"]]
- 00c25ab4 ["CALL", null, ["callee:00c5e9f0:8"]]
+ 00c25b50 ["INT_ADD", "register:40f0:8", ["const:c25b50:8", "const:4:8"]]
+ 00c25b50 ["CALL", null, ["callee:00c5e9f0:8"]]
- 00c25ab4 bytes 9be30094
+ 00c25b50 bytes a8e30094
~~~


<a id="compare-5629515475767a9e53ab65ec69d72ca3"></a>

### [`00c25acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md) → [`00c25b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b68.md) _ZNKSt6__ndk114collate_bynameIcE10do_compareEPKcS3_S3_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5e930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e930.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ea00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25b4c) · [`00c25b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25b74) · [`00c25bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25bb8)
- 新版 [`00c25be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b68.md#insn-00c25be8) · [`00c25c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b68.md#insn-00c25c10) · [`00c25c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25b68.md#insn-00c25c54)

~~~diff
- 00c25b4c ["INT_ADD", "register:40f0:8", ["const:c25b4c:8", "const:4:8"]]
- 00c25b4c ["CALL", null, ["callee:00c57f60:8"]]
+ 00c25be8 ["INT_ADD", "register:40f0:8", ["const:c25be8:8", "const:4:8"]]
+ 00c25be8 ["CALL", null, ["callee:00c57f60:8"]]
- 00c25b4c bytes d1c80094
+ 00c25be8 bytes dec80094
- 00c25b74 ["INT_ADD", "register:40f0:8", ["const:c25b74:8", "const:4:8"]]
- 00c25b74 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c25c10 ["INT_ADD", "register:40f0:8", ["const:c25c10:8", "const:4:8"]]
+ 00c25c10 ["CALL", null, ["callee:00c580d0:8"]]
- 00c25b74 bytes 23c90094
+ 00c25c10 bytes 30c90094
- 00c25bb8 ["INT_ADD", "register:40f0:8", ["const:c25bb8:8", "const:4:8"]]
- 00c25bb8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c25c54 ["INT_ADD", "register:40f0:8", ["const:c25c54:8", "const:4:8"]]
+ 00c25c54 ["CALL", null, ["callee:00c580d0:8"]]
- 00c25bb8 bytes 12c90094
+ 00c25c54 bytes 1fc90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7b37297b79a09430fe90d64c818554c"></a>

### [`00c25ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md) → [`00c25d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25d40.md) _ZNKSt6__ndk114collate_bynameIcE12do_transformEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d1c) · [`00c25d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d44) · [`00c25d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d70)
- 新版 [`00c25db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25d40.md#insn-00c25db8) · [`00c25de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25d40.md#insn-00c25de0) · [`00c25e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25d40.md#insn-00c25e0c)

~~~diff
- 00c25d1c ["INT_ADD", "register:40f0:8", ["const:c25d1c:8", "const:4:8"]]
- 00c25d1c ["CALL", null, ["callee:00c57f60:8"]]
+ 00c25db8 ["INT_ADD", "register:40f0:8", ["const:c25db8:8", "const:4:8"]]
+ 00c25db8 ["CALL", null, ["callee:00c57f60:8"]]
- 00c25d1c bytes 5dc80094
+ 00c25db8 bytes 6ac80094
- 00c25d44 ["INT_ADD", "register:40f0:8", ["const:c25d44:8", "const:4:8"]]
- 00c25d44 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c25de0 ["INT_ADD", "register:40f0:8", ["const:c25de0:8", "const:4:8"]]
+ 00c25de0 ["CALL", null, ["callee:00c580d0:8"]]
- 00c25d44 bytes afc80094
+ 00c25de0 bytes bcc80094
- 00c25d70 ["INT_ADD", "register:40f0:8", ["const:c25d70:8", "const:4:8"]]
- 00c25d70 ["CALL", null, ["callee:00c5ea10:8"]]
+ 00c25e0c ["INT_ADD", "register:40f0:8", ["const:c25e0c:8", "const:4:8"]]
+ 00c25e0c ["CALL", null, ["callee:00c5ea10:8"]]
- 00c25d70 bytes f4e20094
+ 00c25e0c bytes 01e30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12126fef2532d7b1119023e8d0ff9155"></a>

### [`00c26080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26080.md) → [`00c2611c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c2611c.md) _ZNSt6__ndk114collate_bynameIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ea20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26080.md#insn-00c26094)
- 新版 [`00c26130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c2611c.md#insn-00c26130)

~~~diff
- 00c26094 ["INT_ADD", "register:40f0:8", ["const:c26094:8", "const:4:8"]]
- 00c26094 ["CALL", null, ["callee:00c5ea20:8"]]
+ 00c26130 ["INT_ADD", "register:40f0:8", ["const:c26130:8", "const:4:8"]]
+ 00c26130 ["CALL", null, ["callee:00c5ea20:8"]]
- 00c26094 bytes 2fe20094
+ 00c26130 bytes 3ce20094
~~~


<a id="compare-baad33d7e99dc8633a46e6261c97ffb4"></a>

### [`00c260ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md) → [`00c26148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26148.md) _ZNKSt6__ndk114collate_bynameIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c26140) · [`00c26174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c26174) · [`00c261cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c261cc)
- 新版 [`00c261dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26148.md#insn-00c261dc) · [`00c26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26148.md#insn-00c26210) · [`00c26268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26148.md#insn-00c26268)

~~~diff
- 00c26140 ["INT_ADD", "register:40f0:8", ["const:c26140:8", "const:4:8"]]
- 00c26140 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c261dc ["INT_ADD", "register:40f0:8", ["const:c261dc:8", "const:4:8"]]
+ 00c261dc ["CALL", null, ["callee:00c57f60:8"]]
- 00c26140 bytes 54c70094
+ 00c261dc bytes 61c70094
- 00c26174 ["INT_ADD", "register:40f0:8", ["const:c26174:8", "const:4:8"]]
- 00c26174 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c26210 ["INT_ADD", "register:40f0:8", ["const:c26210:8", "const:4:8"]]
+ 00c26210 ["CALL", null, ["callee:00c580d0:8"]]
- 00c26174 bytes a3c70094
+ 00c26210 bytes b0c70094
- 00c261cc ["INT_ADD", "register:40f0:8", ["const:c261cc:8", "const:4:8"]]
- 00c261cc ["CALL", null, ["callee:00c580d0:8"]]
+ 00c26268 ["INT_ADD", "register:40f0:8", ["const:c26268:8", "const:4:8"]]
+ 00c26268 ["CALL", null, ["callee:00c580d0:8"]]
- 00c261cc bytes 8dc70094
+ 00c26268 bytes 9ac70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c609df1b72f3e60848e53dfefac8f70c"></a>

### [`00c262c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md) → [`00c26360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26360.md) _ZNKSt6__ndk114collate_bynameIwE12do_transformEPKwS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c26350) · [`00c26384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c26384) · [`00c263b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c263b4)
- 新版 [`00c263ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26360.md#insn-00c263ec) · [`00c26420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26360.md#insn-00c26420) · [`00c26450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26360.md#insn-00c26450)

~~~diff
- 00c26350 ["INT_ADD", "register:40f0:8", ["const:c26350:8", "const:4:8"]]
- 00c26350 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c263ec ["INT_ADD", "register:40f0:8", ["const:c263ec:8", "const:4:8"]]
+ 00c263ec ["CALL", null, ["callee:00c57f60:8"]]
- 00c26350 bytes d0c60094
+ 00c263ec bytes ddc60094
- 00c26384 ["INT_ADD", "register:40f0:8", ["const:c26384:8", "const:4:8"]]
- 00c26384 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c26420 ["INT_ADD", "register:40f0:8", ["const:c26420:8", "const:4:8"]]
+ 00c26420 ["CALL", null, ["callee:00c580d0:8"]]
- 00c26384 bytes 1fc70094
+ 00c26420 bytes 2cc70094
- 00c263b4 ["INT_ADD", "register:40f0:8", ["const:c263b4:8", "const:4:8"]]
- 00c263b4 ["CALL", null, ["callee:00c5ea40:8"]]
+ 00c26450 ["INT_ADD", "register:40f0:8", ["const:c26450:8", "const:4:8"]]
+ 00c26450 ["CALL", null, ["callee:00c5ea40:8"]]
- 00c263b4 bytes 6fe10094
+ 00c26450 bytes 7ce10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3e647a894619739b092e2ae1cb912f0"></a>

### [`00c264f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c264f8.md) → [`00c26594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26594.md) _ZNSt6__ndk15ctypeIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ea50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2650c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c264f8.md#insn-00c2650c)
- 新版 [`00c265a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26594.md#insn-00c265a8)

~~~diff
- 00c2650c ["INT_ADD", "register:40f0:8", ["const:c2650c:8", "const:4:8"]]
- 00c2650c ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c265a8 ["INT_ADD", "register:40f0:8", ["const:c265a8:8", "const:4:8"]]
+ 00c265a8 ["CALL", null, ["callee:00c5ea50:8"]]
- 00c2650c bytes 1de10094
+ 00c265a8 bytes 2ae10094
~~~


<a id="compare-0529d8e1cf62e1d00bb6be34c19fbdbf"></a>

### [`00c26c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c94.md) → [`00c26d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d30.md) _ZNSt6__ndk15ctypeIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ea80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c94.md#insn-00c26ca8)
- 新版 [`00c26d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d30.md#insn-00c26d44)

~~~diff
- 00c26ca8 ["INT_ADD", "register:40f0:8", ["const:c26ca8:8", "const:4:8"]]
- 00c26ca8 ["CALL", null, ["callee:00c5ea80:8"]]
+ 00c26d44 ["INT_ADD", "register:40f0:8", ["const:c26d44:8", "const:4:8"]]
+ 00c26d44 ["CALL", null, ["callee:00c5ea80:8"]]
- 00c26ca8 bytes 42df0094
+ 00c26d44 bytes 4fdf0094
~~~


<a id="compare-c3ff3c46ed04eaa86f87b16c0d99948a"></a>

### [`00c27354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27354.md) → [`00c273f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c273f0.md) _ZNSt6__ndk112ctype_bynameIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27354.md#insn-00c27368)
- 新版 [`00c27404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c273f0.md#insn-00c27404)

~~~diff
- 00c27368 ["INT_ADD", "register:40f0:8", ["const:c27368:8", "const:4:8"]]
- 00c27368 ["CALL", null, ["callee:00c5eab0:8"]]
+ 00c27404 ["INT_ADD", "register:40f0:8", ["const:c27404:8", "const:4:8"]]
+ 00c27404 ["CALL", null, ["callee:00c5eab0:8"]]
- 00c27368 bytes 9edd0094
+ 00c27404 bytes abdd0094
~~~


<a id="compare-a35d4532652a5aaa5f6ad66b827087ce"></a>

### [`00c278ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278ac.md) → [`00c27948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27948.md) _ZNSt6__ndk112ctype_bynameIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ea20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c278c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278ac.md#insn-00c278c0)
- 新版 [`00c2795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27948.md#insn-00c2795c)

~~~diff
- 00c278c0 ["INT_ADD", "register:40f0:8", ["const:c278c0:8", "const:4:8"]]
- 00c278c0 ["CALL", null, ["callee:00c5eaf0:8"]]
+ 00c2795c ["INT_ADD", "register:40f0:8", ["const:c2795c:8", "const:4:8"]]
+ 00c2795c ["CALL", null, ["callee:00c5eaf0:8"]]
- 00c278c0 bytes 58dc0094
+ 00c2795c bytes 65dc0094
~~~


<a id="compare-afb9db1566bc72072e321550869c0c0a"></a>

### [`00c278d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md) → [`00c27974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27974.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5ea60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea60.md) [`00c5eb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb00.md) [`00c5eb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb10.md) [`00c5eb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c27910) · [`00c27928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c27928) · [`00c2795c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c2795c)
- 新版 [`00c279ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27974.md#insn-00c279ac) · [`00c279c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27974.md#insn-00c279c4) · [`00c279f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27974.md#insn-00c279f8)

~~~diff
- 00c27910 ["INT_ADD", "register:40f0:8", ["const:c27910:8", "const:4:8"]]
- 00c27910 ["CALL", null, ["callee:00c5eb00:8"]]
+ 00c279ac ["INT_ADD", "register:40f0:8", ["const:c279ac:8", "const:4:8"]]
+ 00c279ac ["CALL", null, ["callee:00c5eb00:8"]]
- 00c27910 bytes 48dc0094
+ 00c279ac bytes 55dc0094
- 00c27928 ["INT_ADD", "register:40f0:8", ["const:c27928:8", "const:4:8"]]
- 00c27928 ["CALL", null, ["callee:00c5eb10:8"]]
+ 00c279c4 ["INT_ADD", "register:40f0:8", ["const:c279c4:8", "const:4:8"]]
+ 00c279c4 ["CALL", null, ["callee:00c5eb10:8"]]
- 00c27928 bytes 46dc0094
+ 00c279c4 bytes 53dc0094
- 00c2795c ["INT_ADD", "register:40f0:8", ["const:c2795c:8", "const:4:8"]]
- 00c2795c ["CALL", null, ["callee:00c5eb20:8"]]
+ 00c279f8 ["INT_ADD", "register:40f0:8", ["const:c279f8:8", "const:4:8"]]
+ 00c279f8 ["CALL", null, ["callee:00c5eb20:8"]]
- 00c2795c bytes 3ddc0094
+ 00c279f8 bytes 4adc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9729b2a0e1f798934ba056ff0177c924"></a>

### [`00c27bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md) → [`00c27c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27c64.md) _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5ea60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea60.md) [`00c5eb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb00.md) [`00c5eb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb10.md) [`00c5eb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c18) · [`00c27c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c2c) · [`00c27c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c40)
- 新版 [`00c27cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27c64.md#insn-00c27cb4) · [`00c27cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27c64.md#insn-00c27cc8) · [`00c27cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27c64.md#insn-00c27cdc)

~~~diff
- 00c27c18 ["INT_ADD", "register:40f0:8", ["const:c27c18:8", "const:4:8"]]
- 00c27c18 ["CALL", null, ["callee:00c5eb00:8"]]
+ 00c27cb4 ["INT_ADD", "register:40f0:8", ["const:c27cb4:8", "const:4:8"]]
+ 00c27cb4 ["CALL", null, ["callee:00c5eb00:8"]]
- 00c27c18 bytes 86db0094
+ 00c27cb4 bytes 93db0094
- 00c27c2c ["INT_ADD", "register:40f0:8", ["const:c27c2c:8", "const:4:8"]]
- 00c27c2c ["CALL", null, ["callee:00c5eb10:8"]]
+ 00c27cc8 ["INT_ADD", "register:40f0:8", ["const:c27cc8:8", "const:4:8"]]
+ 00c27cc8 ["CALL", null, ["callee:00c5eb10:8"]]
- 00c27c2c bytes 85db0094
+ 00c27cc8 bytes 92db0094
- 00c27c40 ["INT_ADD", "register:40f0:8", ["const:c27c40:8", "const:4:8"]]
- 00c27c40 ["CALL", null, ["callee:00c5eb30:8"]]
+ 00c27cdc ["INT_ADD", "register:40f0:8", ["const:c27cdc:8", "const:4:8"]]
+ 00c27cdc ["CALL", null, ["callee:00c5eb30:8"]]
- 00c27c40 bytes 88db0094
+ 00c27cdc bytes 95db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a9fe50d88ae47d1a77b1d39fd9f7e6b"></a>

### [`00c27cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md) → [`00c27d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27d94.md) _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5ea60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea60.md) [`00c5eb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb00.md) [`00c5eb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb10.md) [`00c5eb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d34) · [`00c27d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d5c) · [`00c27d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d70)
- 新版 [`00c27dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27d94.md#insn-00c27dd0) · [`00c27df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27d94.md#insn-00c27df8) · [`00c27e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27d94.md#insn-00c27e0c)

~~~diff
- 00c27d34 ["INT_ADD", "register:40f0:8", ["const:c27d34:8", "const:4:8"]]
- 00c27d34 ["CALL", null, ["callee:00c5eb00:8"]]
+ 00c27dd0 ["INT_ADD", "register:40f0:8", ["const:c27dd0:8", "const:4:8"]]
+ 00c27dd0 ["CALL", null, ["callee:00c5eb00:8"]]
- 00c27d34 bytes 3fdb0094
+ 00c27dd0 bytes 4cdb0094
- 00c27d5c ["INT_ADD", "register:40f0:8", ["const:c27d5c:8", "const:4:8"]]
- 00c27d5c ["CALL", null, ["callee:00c5eb10:8"]]
+ 00c27df8 ["INT_ADD", "register:40f0:8", ["const:c27df8:8", "const:4:8"]]
+ 00c27df8 ["CALL", null, ["callee:00c5eb10:8"]]
- 00c27d5c bytes 39db0094
+ 00c27df8 bytes 46db0094
- 00c27d70 ["INT_ADD", "register:40f0:8", ["const:c27d70:8", "const:4:8"]]
- 00c27d70 ["CALL", null, ["callee:00c5eb30:8"]]
+ 00c27e0c ["INT_ADD", "register:40f0:8", ["const:c27e0c:8", "const:4:8"]]
+ 00c27e0c ["CALL", null, ["callee:00c5eb30:8"]]
- 00c27d70 bytes 3cdb0094
+ 00c27e0c bytes 49db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-429c53699ef61b15cfd287ead6199729"></a>

### [`00c27e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27e3c.md) → [`00c27ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27ed8.md) _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27e3c.md#insn-00c27e6c)
- 新版 [`00c27f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27ed8.md#insn-00c27f08)

~~~diff
- 00c27e6c ["INT_ADD", "register:40f0:8", ["const:c27e6c:8", "const:4:8"]]
- 00c27e6c ["CALL", null, ["callee:00c5eb90:8"]]
+ 00c27f08 ["INT_ADD", "register:40f0:8", ["const:c27f08:8", "const:4:8"]]
+ 00c27f08 ["CALL", null, ["callee:00c5eb90:8"]]
- 00c27e6c bytes 15db0094
+ 00c27f08 bytes 22db0094
~~~


<a id="compare-e305421e16383f17c62d7a6fb6c8e462"></a>

### [`00c27eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27eac.md) → [`00c27f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27f48.md) _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ead0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ead0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27eac.md#insn-00c27edc)
- 新版 [`00c27f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27f48.md#insn-00c27f78)

~~~diff
- 00c27edc ["INT_ADD", "register:40f0:8", ["const:c27edc:8", "const:4:8"]]
- 00c27edc ["CALL", null, ["callee:00c5eba0:8"]]
+ 00c27f78 ["INT_ADD", "register:40f0:8", ["const:c27f78:8", "const:4:8"]]
+ 00c27f78 ["CALL", null, ["callee:00c5eba0:8"]]
- 00c27edc bytes fdda0094
+ 00c27f78 bytes 0adb0094
~~~


<a id="compare-834c1d43ff9a3c13ef4d6e309c353ba0"></a>

### [`00c27f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md) → [`00c27fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27fa4.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ebb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f24) · [`00c27f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f34) · [`00c27f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f44)
- 新版 [`00c27fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27fa4.md#insn-00c27fc0) · [`00c27fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27fa4.md#insn-00c27fd0) · [`00c27fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27fa4.md#insn-00c27fe0)

~~~diff
- 00c27f24 ["INT_ADD", "register:40f0:8", ["const:c27f24:8", "const:4:8"]]
- 00c27f24 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c27fc0 ["INT_ADD", "register:40f0:8", ["const:c27fc0:8", "const:4:8"]]
+ 00c27fc0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c27f24 bytes 93d90094
+ 00c27fc0 bytes a0d90094
- 00c27f34 ["INT_ADD", "register:40f0:8", ["const:c27f34:8", "const:4:8"]]
- 00c27f34 ["CALL", null, ["callee:00c5ebb0:8"]]
+ 00c27fd0 ["INT_ADD", "register:40f0:8", ["const:c27fd0:8", "const:4:8"]]
+ 00c27fd0 ["CALL", null, ["callee:00c5ebb0:8"]]
- 00c27f34 bytes ebda0094
+ 00c27fd0 bytes f8da0094
- 00c27f44 ["INT_ADD", "register:40f0:8", ["const:c27f44:8", "const:4:8"]]
- 00c27f44 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c27fe0 ["INT_ADD", "register:40f0:8", ["const:c27fe0:8", "const:4:8"]]
+ 00c27fe0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c27f44 bytes 8bd90094
+ 00c27fe0 bytes 98d90094
~~~


<a id="compare-a3af66146a5790ed023910edb3a2ab02"></a>

### [`00c27f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md) → [`00c28014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28014.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ebb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fc8) · [`00c27fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fd8) · [`00c27fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fe8)
- 新版 [`00c28064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28014.md#insn-00c28064) · [`00c28074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28014.md#insn-00c28074) · [`00c28084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28014.md#insn-00c28084)

~~~diff
- 00c27fc8 ["INT_ADD", "register:40f0:8", ["const:c27fc8:8", "const:4:8"]]
- 00c27fc8 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28064 ["INT_ADD", "register:40f0:8", ["const:c28064:8", "const:4:8"]]
+ 00c28064 ["CALL", null, ["callee:00c5e640:8"]]
- 00c27fc8 bytes 6ad90094
+ 00c28064 bytes 77d90094
- 00c27fd8 ["INT_ADD", "register:40f0:8", ["const:c27fd8:8", "const:4:8"]]
- 00c27fd8 ["CALL", null, ["callee:00c5ebb0:8"]]
+ 00c28074 ["INT_ADD", "register:40f0:8", ["const:c28074:8", "const:4:8"]]
+ 00c28074 ["CALL", null, ["callee:00c5ebb0:8"]]
- 00c27fd8 bytes c2da0094
+ 00c28074 bytes cfda0094
- 00c27fe8 ["INT_ADD", "register:40f0:8", ["const:c27fe8:8", "const:4:8"]]
- 00c27fe8 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28084 ["INT_ADD", "register:40f0:8", ["const:c28084:8", "const:4:8"]]
+ 00c28084 ["CALL", null, ["callee:00c5e640:8"]]
- 00c27fe8 bytes 62d90094
+ 00c28084 bytes 6fd90094
~~~


<a id="compare-80b5d40285a05c2acdfbf753569d34c4"></a>

### [`00c2802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md) → [`00c280c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c280c8.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eaf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ebc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2804c) · [`00c2805c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2805c) · [`00c2806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2806c)
- 新版 [`00c280e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c280c8.md#insn-00c280e8) · [`00c280f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c280c8.md#insn-00c280f8) · [`00c28108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c280c8.md#insn-00c28108)

~~~diff
- 00c2804c ["INT_ADD", "register:40f0:8", ["const:c2804c:8", "const:4:8"]]
- 00c2804c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c280e8 ["INT_ADD", "register:40f0:8", ["const:c280e8:8", "const:4:8"]]
+ 00c280e8 ["CALL", null, ["callee:00c5e640:8"]]
- 00c2804c bytes 49d90094
+ 00c280e8 bytes 56d90094
- 00c2805c ["INT_ADD", "register:40f0:8", ["const:c2805c:8", "const:4:8"]]
- 00c2805c ["CALL", null, ["callee:00c5ebc0:8"]]
+ 00c280f8 ["INT_ADD", "register:40f0:8", ["const:c280f8:8", "const:4:8"]]
+ 00c280f8 ["CALL", null, ["callee:00c5ebc0:8"]]
- 00c2805c bytes a5da0094
+ 00c280f8 bytes b2da0094
- 00c2806c ["INT_ADD", "register:40f0:8", ["const:c2806c:8", "const:4:8"]]
- 00c2806c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28108 ["INT_ADD", "register:40f0:8", ["const:c28108:8", "const:4:8"]]
+ 00c28108 ["CALL", null, ["callee:00c5e640:8"]]
- 00c2806c bytes 41d90094
+ 00c28108 bytes 4ed90094
~~~


<a id="compare-f6898006e3b82bb7ced2f24aec4c764c"></a>

### [`00c280a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md) → [`00c28140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28140.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEPKwS3_cPc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eaf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ebc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28100) · [`00c28110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28110) · [`00c28120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28120)
- 新版 [`00c2819c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28140.md#insn-00c2819c) · [`00c281ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28140.md#insn-00c281ac) · [`00c281bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28140.md#insn-00c281bc)

~~~diff
- 00c28100 ["INT_ADD", "register:40f0:8", ["const:c28100:8", "const:4:8"]]
- 00c28100 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c2819c ["INT_ADD", "register:40f0:8", ["const:c2819c:8", "const:4:8"]]
+ 00c2819c ["CALL", null, ["callee:00c5e640:8"]]
- 00c28100 bytes 1cd90094
+ 00c2819c bytes 29d90094
- 00c28110 ["INT_ADD", "register:40f0:8", ["const:c28110:8", "const:4:8"]]
- 00c28110 ["CALL", null, ["callee:00c5ebc0:8"]]
+ 00c281ac ["INT_ADD", "register:40f0:8", ["const:c281ac:8", "const:4:8"]]
+ 00c281ac ["CALL", null, ["callee:00c5ebc0:8"]]
- 00c28110 bytes 78da0094
+ 00c281ac bytes 85da0094
- 00c28120 ["INT_ADD", "register:40f0:8", ["const:c28120:8", "const:4:8"]]
- 00c28120 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c281bc ["INT_ADD", "register:40f0:8", ["const:c281bc:8", "const:4:8"]]
+ 00c281bc ["CALL", null, ["callee:00c5e640:8"]]
- 00c28120 bytes 14d90094
+ 00c281bc bytes 21d90094
~~~


<a id="compare-56be31847d2e14f96b28d6f6b0bf534f"></a>

### [`00c28164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28164.md) → [`00c28200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28200.md) _ZNSt6__ndk17codecvtIcc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ebd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28164.md#insn-00c28178)
- 新版 [`00c28214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28200.md#insn-00c28214)

~~~diff
- 00c28178 ["INT_ADD", "register:40f0:8", ["const:c28178:8", "const:4:8"]]
- 00c28178 ["CALL", null, ["callee:00c5ebd0:8"]]
+ 00c28214 ["INT_ADD", "register:40f0:8", ["const:c28214:8", "const:4:8"]]
+ 00c28214 ["CALL", null, ["callee:00c5ebd0:8"]]
- 00c28178 bytes 62da0094
+ 00c28214 bytes 6fda0094
~~~


<a id="compare-21b938872bb57d0194311e764c26a27c"></a>

### [`00c28384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28384.md) → [`00c28420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28420.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28384.md#insn-00c28398)
- 新版 [`00c28434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28420.md#insn-00c28434)

~~~diff
- 00c28398 ["INT_ADD", "register:40f0:8", ["const:c28398:8", "const:4:8"]]
- 00c28398 ["CALL", null, ["callee:00c5ebe0:8"]]
+ 00c28434 ["INT_ADD", "register:40f0:8", ["const:c28434:8", "const:4:8"]]
+ 00c28434 ["CALL", null, ["callee:00c5ebe0:8"]]
- 00c28398 bytes ded90094
+ 00c28434 bytes ebd90094
~~~


<a id="compare-1e30cad372663b8ce036a944e4bf714c"></a>

### [`00c283b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md) → [`00c2844c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2844c.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ebf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebf0.md) [`00c5ec00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28464) · [`00c28484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28484) · [`00c28494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28494)
- 新版 [`00c28500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2844c.md#insn-00c28500) · [`00c28520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2844c.md#insn-00c28520) · [`00c28530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2844c.md#insn-00c28530)

~~~diff
- 00c28464 ["INT_ADD", "register:40f0:8", ["const:c28464:8", "const:4:8"]]
- 00c28464 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28500 ["INT_ADD", "register:40f0:8", ["const:c28500:8", "const:4:8"]]
+ 00c28500 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28464 bytes 43d80094
+ 00c28500 bytes 50d80094
- 00c28484 ["INT_ADD", "register:40f0:8", ["const:c28484:8", "const:4:8"]]
- 00c28484 ["CALL", null, ["callee:00c5ebf0:8"]]
+ 00c28520 ["INT_ADD", "register:40f0:8", ["const:c28520:8", "const:4:8"]]
+ 00c28520 ["CALL", null, ["callee:00c5ebf0:8"]]
- 00c28484 bytes a7d90094
+ 00c28520 bytes b4d90094
- 00c28494 ["INT_ADD", "register:40f0:8", ["const:c28494:8", "const:4:8"]]
- 00c28494 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28530 ["INT_ADD", "register:40f0:8", ["const:c28530:8", "const:4:8"]]
+ 00c28530 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28494 bytes 37d80094
+ 00c28530 bytes 44d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0ccd7d0cc3d280881957effa50dc4f"></a>

### [`00c28674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md) → [`00c28710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28710.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE5do_inERS1_PKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb40.md) [`00c5eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec10.md) [`00c5ec20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28714) · [`00c28734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28734) · [`00c28744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28744)
- 新版 [`00c287b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28710.md#insn-00c287b0) · [`00c287d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28710.md#insn-00c287d0) · [`00c287e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28710.md#insn-00c287e0)

~~~diff
- 00c28714 ["INT_ADD", "register:40f0:8", ["const:c28714:8", "const:4:8"]]
- 00c28714 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c287b0 ["INT_ADD", "register:40f0:8", ["const:c287b0:8", "const:4:8"]]
+ 00c287b0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28714 bytes 97d70094
+ 00c287b0 bytes a4d70094
- 00c28734 ["INT_ADD", "register:40f0:8", ["const:c28734:8", "const:4:8"]]
- 00c28734 ["CALL", null, ["callee:00c5ec10:8"]]
+ 00c287d0 ["INT_ADD", "register:40f0:8", ["const:c287d0:8", "const:4:8"]]
+ 00c287d0 ["CALL", null, ["callee:00c5ec10:8"]]
- 00c28734 bytes 03d90094
+ 00c287d0 bytes 10d90094
- 00c28744 ["INT_ADD", "register:40f0:8", ["const:c28744:8", "const:4:8"]]
- 00c28744 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c287e0 ["INT_ADD", "register:40f0:8", ["const:c287e0:8", "const:4:8"]]
+ 00c287e0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28744 bytes 8bd70094
+ 00c287e0 bytes 98d70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40f1ceb69e3beef07739d43dbeb54f1e"></a>

### [`00c28928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md) → [`00c289c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c289c4.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ec00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c28954) · [`00c2896c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c2896c) · [`00c2897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c2897c)
- 新版 [`00c289f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c289c4.md#insn-00c289f0) · [`00c28a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c289c4.md#insn-00c28a08) · [`00c28a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c289c4.md#insn-00c28a18)

~~~diff
- 00c28954 ["INT_ADD", "register:40f0:8", ["const:c28954:8", "const:4:8"]]
- 00c28954 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c289f0 ["INT_ADD", "register:40f0:8", ["const:c289f0:8", "const:4:8"]]
+ 00c289f0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28954 bytes 07d70094
+ 00c289f0 bytes 14d70094
- 00c2896c ["INT_ADD", "register:40f0:8", ["const:c2896c:8", "const:4:8"]]
- 00c2896c ["CALL", null, ["callee:00c5ec00:8"]]
+ 00c28a08 ["INT_ADD", "register:40f0:8", ["const:c28a08:8", "const:4:8"]]
+ 00c28a08 ["CALL", null, ["callee:00c5ec00:8"]]
- 00c2896c bytes 71d80094
+ 00c28a08 bytes 7ed80094
- 00c2897c ["INT_ADD", "register:40f0:8", ["const:c2897c:8", "const:4:8"]]
- 00c2897c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28a18 ["INT_ADD", "register:40f0:8", ["const:c28a18:8", "const:4:8"]]
+ 00c28a18 ["CALL", null, ["callee:00c5e640:8"]]
- 00c2897c bytes fdd60094
+ 00c28a18 bytes 0ad70094
~~~


<a id="compare-7d666b814a13b0ca26e087e17368817f"></a>

### [`00c28a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md) → [`00c28aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28aa4.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb60.md) [`00c5eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ec30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec30.md) [`00c5ec40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a24) · [`00c28a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a3c) · [`00c28a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a4c)
- 新版 [`00c28ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28aa4.md#insn-00c28ac0) · [`00c28ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28aa4.md#insn-00c28ad8) · [`00c28ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28aa4.md#insn-00c28ae8)

~~~diff
- 00c28a24 ["INT_ADD", "register:40f0:8", ["const:c28a24:8", "const:4:8"]]
- 00c28a24 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28ac0 ["INT_ADD", "register:40f0:8", ["const:c28ac0:8", "const:4:8"]]
+ 00c28ac0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28a24 bytes d3d60094
+ 00c28ac0 bytes e0d60094
- 00c28a3c ["INT_ADD", "register:40f0:8", ["const:c28a3c:8", "const:4:8"]]
- 00c28a3c ["CALL", null, ["callee:00c5ec30:8"]]
+ 00c28ad8 ["INT_ADD", "register:40f0:8", ["const:c28ad8:8", "const:4:8"]]
+ 00c28ad8 ["CALL", null, ["callee:00c5ec30:8"]]
- 00c28a3c bytes 49d80094
+ 00c28ad8 bytes 56d80094
- 00c28a4c ["INT_ADD", "register:40f0:8", ["const:c28a4c:8", "const:4:8"]]
- 00c28a4c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28ae8 ["INT_ADD", "register:40f0:8", ["const:c28ae8:8", "const:4:8"]]
+ 00c28ae8 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28a4c bytes c9d60094
+ 00c28ae8 bytes d6d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32556afcc98071beb1d0470406b5d15c"></a>

### [`00c28ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md) → [`00c28b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28b74.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ec50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b2c) · [`00c28b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b44) · [`00c28b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b54)
- 新版 [`00c28bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28b74.md#insn-00c28bc8) · [`00c28be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28b74.md#insn-00c28be0) · [`00c28bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28b74.md#insn-00c28bf0)

~~~diff
- 00c28b2c ["INT_ADD", "register:40f0:8", ["const:c28b2c:8", "const:4:8"]]
- 00c28b2c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28bc8 ["INT_ADD", "register:40f0:8", ["const:c28bc8:8", "const:4:8"]]
+ 00c28bc8 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28b2c bytes 91d60094
+ 00c28bc8 bytes 9ed60094
- 00c28b44 ["INT_ADD", "register:40f0:8", ["const:c28b44:8", "const:4:8"]]
- 00c28b44 ["CALL", null, ["callee:00c5ec50:8"]]
+ 00c28be0 ["INT_ADD", "register:40f0:8", ["const:c28be0:8", "const:4:8"]]
+ 00c28be0 ["CALL", null, ["callee:00c5ec50:8"]]
- 00c28b44 bytes 0fd80094
+ 00c28be0 bytes 1cd80094
- 00c28b54 ["INT_ADD", "register:40f0:8", ["const:c28b54:8", "const:4:8"]]
- 00c28b54 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28bf0 ["INT_ADD", "register:40f0:8", ["const:c28bf0:8", "const:4:8"]]
+ 00c28bf0 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28b54 bytes 87d60094
+ 00c28bf0 bytes 94d60094
~~~


<a id="compare-edf69d656155db9eb055799de7ddcc18"></a>

### [`00c28bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md) → [`00c28c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28c6c.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5ec40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28bec) · [`00c28bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28bf8) · [`00c28c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28c08)
- 新版 [`00c28c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28c6c.md#insn-00c28c88) · [`00c28c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28c6c.md#insn-00c28c94) · [`00c28ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28c6c.md#insn-00c28ca4)

~~~diff
- 00c28bec ["INT_ADD", "register:40f0:8", ["const:c28bec:8", "const:4:8"]]
- 00c28bec ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28c88 ["INT_ADD", "register:40f0:8", ["const:c28c88:8", "const:4:8"]]
+ 00c28c88 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28bec bytes 61d60094
+ 00c28c88 bytes 6ed60094
- 00c28bf8 ["INT_ADD", "register:40f0:8", ["const:c28bf8:8", "const:4:8"]]
- 00c28bf8 ["CALL", null, ["callee:00c5ec40:8"]]
+ 00c28c94 ["INT_ADD", "register:40f0:8", ["const:c28c94:8", "const:4:8"]]
+ 00c28c94 ["CALL", null, ["callee:00c5ec40:8"]]
- 00c28bf8 bytes ded70094
+ 00c28c94 bytes ebd70094
- 00c28c08 ["INT_ADD", "register:40f0:8", ["const:c28c08:8", "const:4:8"]]
- 00c28c08 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c28ca4 ["INT_ADD", "register:40f0:8", ["const:c28ca4:8", "const:4:8"]]
+ 00c28ca4 ["CALL", null, ["callee:00c5e640:8"]]
- 00c28c08 bytes 5ad60094
+ 00c28ca4 bytes 67d60094
~~~


<a id="compare-8f2819709bc360df6d7935c50c112fe2"></a>

### [`00c28c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c48.md) → [`00c28ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28ce4.md) _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c48.md#insn-00c28c5c)
- 新版 [`00c28cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28ce4.md#insn-00c28cf8)

~~~diff
- 00c28c5c ["INT_ADD", "register:40f0:8", ["const:c28c5c:8", "const:4:8"]]
- 00c28c5c ["CALL", null, ["callee:00c5ec60:8"]]
+ 00c28cf8 ["INT_ADD", "register:40f0:8", ["const:c28cf8:8", "const:4:8"]]
+ 00c28cf8 ["CALL", null, ["callee:00c5ec60:8"]]
- 00c28c5c bytes cdd70094
+ 00c28cf8 bytes dad70094
~~~


<a id="compare-e236c6a77f47729f76ed78f33433af6e"></a>

### [`00c28c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c74.md) → [`00c28d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d10.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c74.md#insn-00c28cb8)
- 新版 [`00c28d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d10.md#insn-00c28d54)

~~~diff
- 00c28cb8 ["INT_ADD", "register:40f0:8", ["const:c28cb8:8", "const:4:8"]]
- 00c28cb8 ["CALL", null, ["callee:00c28d78:8"]]
+ 00c28d54 ["INT_ADD", "register:40f0:8", ["const:c28d54:8", "const:4:8"]]
+ 00c28d54 ["CALL", null, ["callee:00c28d78:8"]]
- 00c28cb8 bytes 09000094
+ 00c28d54 bytes 09000094
~~~


<a id="compare-3ee7b00ba7e769ce958887412a491419"></a>

### [`00c28f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28f38.md) → [`00c28fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28fd4.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2903c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28f38.md#insn-00c28f7c)
- 新版 [`00c29018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28fd4.md#insn-00c29018)

~~~diff
- 00c28f7c ["INT_ADD", "register:40f0:8", ["const:c28f7c:8", "const:4:8"]]
- 00c28f7c ["CALL", null, ["callee:00c2903c:8"]]
+ 00c29018 ["INT_ADD", "register:40f0:8", ["const:c29018:8", "const:4:8"]]
+ 00c29018 ["CALL", null, ["callee:00c2903c:8"]]
- 00c28f7c bytes 09000094
+ 00c29018 bytes 09000094
~~~


<a id="compare-71df6595cdd42e226eb18c023b6d1af3"></a>

### [`00c29484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29484.md) → [`00c29520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29520.md) _ZNSt6__ndk17codecvtIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29484.md#insn-00c29498)
- 新版 [`00c29534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29520.md#insn-00c29534)

~~~diff
- 00c29498 ["INT_ADD", "register:40f0:8", ["const:c29498:8", "const:4:8"]]
- 00c29498 ["CALL", null, ["callee:00c5ec70:8"]]
+ 00c29534 ["INT_ADD", "register:40f0:8", ["const:c29534:8", "const:4:8"]]
+ 00c29534 ["CALL", null, ["callee:00c5ec70:8"]]
- 00c29498 bytes c2d50094
+ 00c29534 bytes cfd50094
~~~


<a id="compare-ebafeac062c68485594ca51b99ad9ad2"></a>

### [`00c294b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c294b0.md) → [`00c2954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2954c.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c294f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c294b0.md#insn-00c294f4)
- 新版 [`00c29590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2954c.md#insn-00c29590)

~~~diff
- 00c294f4 ["INT_ADD", "register:40f0:8", ["const:c294f4:8", "const:4:8"]]
- 00c294f4 ["CALL", null, ["callee:00c28d78:8"]]
+ 00c29590 ["INT_ADD", "register:40f0:8", ["const:c29590:8", "const:4:8"]]
+ 00c29590 ["CALL", null, ["callee:00c28d78:8"]]
- 00c294f4 bytes fafdff97
+ 00c29590 bytes fafdff97
~~~


<a id="compare-d97359e30560721482cc4ba493bf816a"></a>

### [`00c29518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29518.md) → [`00c295b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c295b4.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2903c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29518.md#insn-00c2955c)
- 新版 [`00c295f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c295b4.md#insn-00c295f8)

~~~diff
- 00c2955c ["INT_ADD", "register:40f0:8", ["const:c2955c:8", "const:4:8"]]
- 00c2955c ["CALL", null, ["callee:00c2903c:8"]]
+ 00c295f8 ["INT_ADD", "register:40f0:8", ["const:c295f8:8", "const:4:8"]]
+ 00c295f8 ["CALL", null, ["callee:00c2903c:8"]]
- 00c2955c bytes 91feff97
+ 00c295f8 bytes 91feff97
~~~


<a id="compare-74782c0d693964cfd973423d0ae891d2"></a>

### [`00c295d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c295d0.md) → [`00c2966c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2966c.md) _ZNSt6__ndk17codecvtIDic9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ec80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c295e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c295d0.md#insn-00c295e4)
- 新版 [`00c29680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2966c.md#insn-00c29680)

~~~diff
- 00c295e4 ["INT_ADD", "register:40f0:8", ["const:c295e4:8", "const:4:8"]]
- 00c295e4 ["CALL", null, ["callee:00c5ec80:8"]]
+ 00c29680 ["INT_ADD", "register:40f0:8", ["const:c29680:8", "const:4:8"]]
+ 00c29680 ["CALL", null, ["callee:00c5ec80:8"]]
- 00c295e4 bytes 73d50094
+ 00c29680 bytes 80d50094
~~~


<a id="compare-95dea117d1c31e99af11c64e102bee41"></a>

### [`00c298ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c298ac.md) → [`00c29948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29948.md) _ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c299b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c299b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c298f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c298ac.md#insn-00c298f0)
- 新版 [`00c2998c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29948.md#insn-00c2998c)

~~~diff
- 00c298f0 ["INT_ADD", "register:40f0:8", ["const:c298f0:8", "const:4:8"]]
- 00c298f0 ["CALL", null, ["callee:00c299b0:8"]]
+ 00c2998c ["INT_ADD", "register:40f0:8", ["const:c2998c:8", "const:4:8"]]
+ 00c2998c ["CALL", null, ["callee:00c299b0:8"]]
- 00c298f0 bytes 09000094
+ 00c2998c bytes 09000094
~~~


<a id="compare-fe4fc724500024c8b1339817583b9950"></a>

### [`00c29d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29d8c.md) → [`00c29e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29e28.md) _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ec90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ec90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29d8c.md#insn-00c29da0)
- 新版 [`00c29e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29e28.md#insn-00c29e3c)

~~~diff
- 00c29da0 ["INT_ADD", "register:40f0:8", ["const:c29da0:8", "const:4:8"]]
- 00c29da0 ["CALL", null, ["callee:00c5ec90:8"]]
+ 00c29e3c ["INT_ADD", "register:40f0:8", ["const:c29e3c:8", "const:4:8"]]
+ 00c29e3c ["CALL", null, ["callee:00c5ec90:8"]]
- 00c29da0 bytes 88d30094
+ 00c29e3c bytes 95d30094
~~~


<a id="compare-f3798e257971e62c8a41684ec0d0a4d3"></a>

### [`00c29ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29ee0.md) → [`00c29f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29f7c.md) _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c299b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c299b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29ee0.md#insn-00c29f24)
- 新版 [`00c29fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c29f7c.md#insn-00c29fc0)

~~~diff
- 00c29f24 ["INT_ADD", "register:40f0:8", ["const:c29f24:8", "const:4:8"]]
- 00c29f24 ["CALL", null, ["callee:00c299b0:8"]]
+ 00c29fc0 ["INT_ADD", "register:40f0:8", ["const:c29fc0:8", "const:4:8"]]
+ 00c29fc0 ["CALL", null, ["callee:00c299b0:8"]]
- 00c29f24 bytes 7cfeff97
+ 00c29fc0 bytes 7cfeff97
~~~


<a id="compare-78c83803f87f540a094cd64c5dbf6553"></a>

### [`00c29f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29f98.md) → [`00c2a034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a034.md) _ZNKSt6__ndk114__codecvt_utf8IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29724.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c297c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c297c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29f98.md#insn-00c29fe4)
- 新版 [`00c2a080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a034.md#insn-00c2a080)

~~~diff
- 00c29fe4 ["INT_ADD", "register:40f0:8", ["const:c29fe4:8", "const:4:8"]]
- 00c29fe4 ["CALL", null, ["callee:00c297c0:8"]]
+ 00c2a080 ["INT_ADD", "register:40f0:8", ["const:c2a080:8", "const:4:8"]]
+ 00c2a080 ["CALL", null, ["callee:00c297c0:8"]]
- 00c29fe4 bytes d0fdff97
+ 00c2a080 bytes d0fdff97
~~~


<a id="compare-a1a85b2f47ccc35f066b8b12fbaab2cb"></a>

### [`00c2a008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a008.md) → [`00c2a0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a0a4.md) _ZNKSt6__ndk114__codecvt_utf8IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c299b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c299b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2a054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a008.md#insn-00c2a054)
- 新版 [`00c2a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a0a4.md#insn-00c2a0f0)

~~~diff
- 00c2a054 ["INT_ADD", "register:40f0:8", ["const:c2a054:8", "const:4:8"]]
- 00c2a054 ["CALL", null, ["callee:00c299b0:8"]]
+ 00c2a0f0 ["INT_ADD", "register:40f0:8", ["const:c2a0f0:8", "const:4:8"]]
+ 00c2a0f0 ["CALL", null, ["callee:00c299b0:8"]]
- 00c2a054 bytes 30feff97
+ 00c2a0f0 bytes 30feff97
~~~


<a id="compare-d7701f6e8020f4cadcc6b11225d26495"></a>

### [`00c2a528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a528.md) → [`00c2a5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a5c4.md) _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29724.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c297c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c297c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a528.md#insn-00c2a574)
- 新版 [`00c2a610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a5c4.md#insn-00c2a610)

~~~diff
- 00c2a574 ["INT_ADD", "register:40f0:8", ["const:c2a574:8", "const:4:8"]]
- 00c2a574 ["CALL", null, ["callee:00c297c0:8"]]
+ 00c2a610 ["INT_ADD", "register:40f0:8", ["const:c2a610:8", "const:4:8"]]
+ 00c2a610 ["CALL", null, ["callee:00c297c0:8"]]
- 00c2a574 bytes 6cfcff97
+ 00c2a610 bytes 6cfcff97
~~~


<a id="compare-a3e69a18dc1fd280b8222c8f16ee1d02"></a>

### [`00c2a598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a598.md) → [`00c2a634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a634.md) _ZNKSt6__ndk114__codecvt_utf8IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c299b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c299b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a598.md#insn-00c2a5e4)
- 新版 [`00c2a680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2a634.md#insn-00c2a680)

~~~diff
- 00c2a5e4 ["INT_ADD", "register:40f0:8", ["const:c2a5e4:8", "const:4:8"]]
- 00c2a5e4 ["CALL", null, ["callee:00c299b0:8"]]
+ 00c2a680 ["INT_ADD", "register:40f0:8", ["const:c2a680:8", "const:4:8"]]
+ 00c2a680 ["CALL", null, ["callee:00c299b0:8"]]
- 00c2a5e4 bytes ccfcff97
+ 00c2a680 bytes ccfcff97
~~~


