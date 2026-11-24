# v16.0.1 → v16.0.2 · 要調査の変更候補 (14)

[一覧の目次](README.md)

<a id="compare-fbbbcf4e36abc4e9310479e98d508a15"></a>

### [`00584cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md) → [`00584d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584d18.md) FUN_00584d18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d04) · [`00584d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d24) · [`00584d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d38)
- 新版 [`00584d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584d18.md#insn-00584d44) · [`00584d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584d18.md#insn-00584d64) · [`00584d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584d18.md#insn-00584d78)

~~~diff
- 00584d04 ["INT_ADD", "register:40f0:8", ["const:584d04:8", "const:4:8"]]
- 00584d04 ["CALL", null, ["callee:00597648:8"]]
+ 00584d44 ["INT_ADD", "register:40f0:8", ["const:584d44:8", "const:4:8"]]
+ 00584d44 ["CALL", null, ["callee:00597648:8"]]
- 00584d04 bytes 414a0094
+ 00584d44 bytes 414a0094
- 00584d24 ["INT_ADD", "register:40f0:8", ["const:584d24:8", "const:4:8"]]
- 00584d24 ["CALL", null, ["callee:00c53da0:8"]]
+ 00584d64 ["INT_ADD", "register:40f0:8", ["const:584d64:8", "const:4:8"]]
+ 00584d64 ["CALL", null, ["callee:00c53da0:8"]]
- 00584d24 bytes f73b1b94
+ 00584d64 bytes 0f3c1b94
- 00584d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584d38 ["INT_ADD", "register:40f0:8", ["const:584d38:8", "const:4:8"]]
- 00584d38 ["CALLIND", null, ["register:0:8"]]
+ 00584d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584d78 ["INT_ADD", "register:40f0:8", ["const:584d78:8", "const:4:8"]]
+ 00584d78 ["CALLIND", null, ["register:0:8"]]
- 00584d38 bytes 00013fd6
+ 00584d78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d342e2e5b34efb604192f588843490"></a>

### [`00584d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md) → [`00584ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ddc.md) FUN_00584ddc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584de0) · [`00584df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584df8) · [`00584e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584e08)
- 新版 [`00584e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ddc.md#insn-00584e20) · [`00584e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ddc.md#insn-00584e38) · [`00584e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ddc.md#insn-00584e48)

~~~diff
- 00584de0 ["INT_ADD", "register:40f0:8", ["const:584de0:8", "const:4:8"]]
- 00584de0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00584e20 ["INT_ADD", "register:40f0:8", ["const:584e20:8", "const:4:8"]]
+ 00584e20 ["CALL", null, ["callee:00c57f60:8"]]
- 00584de0 bytes 2c4c1b94
+ 00584e20 bytes 504c1b94
- 00584df8 ["INT_ADD", "register:40f0:8", ["const:584df8:8", "const:4:8"]]
- 00584df8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00584e38 ["INT_ADD", "register:40f0:8", ["const:584e38:8", "const:4:8"]]
+ 00584e38 ["CALL", null, ["callee:00c580d0:8"]]
- 00584df8 bytes 824c1b94
+ 00584e38 bytes a64c1b94
- 00584e08 ["INT_ADD", "register:40f0:8", ["const:584e08:8", "const:4:8"]]
- 00584e08 ["CALL", null, ["callee:0058adac:8"]]
+ 00584e48 ["INT_ADD", "register:40f0:8", ["const:584e48:8", "const:4:8"]]
+ 00584e48 ["CALL", null, ["callee:0058adac:8"]]
- 00584e08 bytes d9170094
+ 00584e48 bytes d9170094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcf5dd3809dca2415be8bad6bde9b455"></a>

### [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) → [`00584f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584f40.md) FUN_00584f40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00547bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bf0.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00564320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f34) · [`00584f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f50) · [`00584f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f84)
- 新版 [`00584f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584f40.md#insn-00584f74) · [`00584f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584f40.md#insn-00584f90) · [`00584fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584f40.md#insn-00584fc4)

~~~diff
- 00584f34 ["INT_ADD", "register:40f0:8", ["const:584f34:8", "const:4:8"]]
- 00584f34 ["CALL", null, ["callee:00547bf0:8"]]
+ 00584f74 ["INT_ADD", "register:40f0:8", ["const:584f74:8", "const:4:8"]]
+ 00584f74 ["CALL", null, ["callee:00547bf0:8"]]
- 00584f34 bytes 1f0bff97
+ 00584f74 bytes 1f0bff97
- 00584f50 ["INT_ADD", "register:40f0:8", ["const:584f50:8", "const:4:8"]]
- 00584f50 ["CALL", null, ["callee:00564320:8"]]
+ 00584f90 ["INT_ADD", "register:40f0:8", ["const:584f90:8", "const:4:8"]]
+ 00584f90 ["CALL", null, ["callee:00564320:8"]]
- 00584f50 bytes e47cff97
+ 00584f90 bytes e47cff97
- 00584f84 ["INT_ADD", "register:40f0:8", ["const:584f84:8", "const:4:8"]]
- 00584f84 ["CALL", null, ["callee:0043bb60:8"]]
+ 00584fc4 ["INT_ADD", "register:40f0:8", ["const:584fc4:8", "const:4:8"]]
+ 00584fc4 ["CALL", null, ["callee:0043bb60:8"]]
- 00584f84 bytes e7dafa97
+ 00584fc4 bytes e7dafa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754f6c049dc17ee326686eb807ce50ad"></a>

### [`00585214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md) → [`00585254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585254.md) FUN_00585254

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005850a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/005850a0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md#insn-00585254) · [`005852a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md#insn-005852a0) · [`005852b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md#insn-005852b4)
- 新版 [`00585294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585254.md#insn-00585294) · [`005852e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585254.md#insn-005852e0) · [`005852f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585254.md#insn-005852f4)

~~~diff
- 00585254 ["INT_ADD", "register:40f0:8", ["const:585254:8", "const:4:8"]]
- 00585254 ["CALL", null, ["callee:00c57f60:8"]]
+ 00585294 ["INT_ADD", "register:40f0:8", ["const:585294:8", "const:4:8"]]
+ 00585294 ["CALL", null, ["callee:00c57f60:8"]]
- 00585254 bytes 0f4b1b94
+ 00585294 bytes 334b1b94
- 005852a0 ["INT_ADD", "register:40f0:8", ["const:5852a0:8", "const:4:8"]]
- 005852a0 ["CALL", null, ["callee:00c53da0:8"]]
+ 005852e0 ["INT_ADD", "register:40f0:8", ["const:5852e0:8", "const:4:8"]]
+ 005852e0 ["CALL", null, ["callee:00c53da0:8"]]
- 005852a0 bytes 983a1b94
+ 005852e0 bytes b03a1b94
- 005852b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005852b4 ["INT_ADD", "register:40f0:8", ["const:5852b4:8", "const:4:8"]]
- 005852b4 ["CALLIND", null, ["register:0:8"]]
+ 005852f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005852f4 ["INT_ADD", "register:40f0:8", ["const:5852f4:8", "const:4:8"]]
+ 005852f4 ["CALLIND", null, ["register:0:8"]]
- 005852b4 bytes 00013fd6
+ 005852f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d17cb33c4a99806a23bc2a35cfa99ed"></a>

### [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) → [`00585364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md) FUN_00585364

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) · 呼出先 3件 [`00587da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) · 呼出先 3件 [`00587de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058535c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md#insn-0058535c) · [`00585370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md#insn-00585370) · [`005853c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md#insn-005853c8)
- 新版 [`0058539c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md#insn-0058539c) · [`005853b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md#insn-005853b0) · [`00585408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md#insn-00585408)

~~~diff
- 0058535c ["INT_ADD", "register:40f0:8", ["const:58535c:8", "const:4:8"]]
- 0058535c ["CALL", null, ["callee:00c57f60:8"]]
+ 0058539c ["INT_ADD", "register:40f0:8", ["const:58539c:8", "const:4:8"]]
+ 0058539c ["CALL", null, ["callee:00c57f60:8"]]
- 0058535c bytes cd4a1b94
+ 0058539c bytes f14a1b94
- 00585370 ["INT_ADD", "register:40f0:8", ["const:585370:8", "const:4:8"]]
- 00585370 ["CALL", null, ["callee:00587de8:8"]]
+ 005853b0 ["INT_ADD", "register:40f0:8", ["const:5853b0:8", "const:4:8"]]
+ 005853b0 ["CALL", null, ["callee:00587de8:8"]]
- 00585370 bytes 8e0a0094
+ 005853b0 bytes 8e0a0094
- 005853c8 ["INT_ADD", "register:40f0:8", ["const:5853c8:8", "const:4:8"]]
- 005853c8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00585408 ["INT_ADD", "register:40f0:8", ["const:585408:8", "const:4:8"]]
+ 00585408 ["CALL", null, ["callee:00c57fb0:8"]]
- 005853c8 bytes c64a1b94
+ 00585408 bytes ea4a1b94
~~~


<a id="compare-45e30dea66a9997beedf7e01b0b9a795"></a>

### [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) → [`00585d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md) FUN_00585d90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) · 呼出先 3件 [`0058820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`00585f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md) · 呼出先 3件 [`0058824c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058824c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md#insn-00585dcc) · [`00585e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md#insn-00585e28) · [`00585e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md#insn-00585e58)
- 新版 [`00585e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md#insn-00585e0c) · [`00585e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md#insn-00585e68) · [`00585e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md#insn-00585e98)

~~~diff
- 00585dcc ["INT_ADD", "register:40f0:8", ["const:585dcc:8", "const:4:8"]]
- 00585dcc ["CALL", null, ["callee:00c58120:8"]]
+ 00585e0c ["INT_ADD", "register:40f0:8", ["const:585e0c:8", "const:4:8"]]
+ 00585e0c ["CALL", null, ["callee:00c58120:8"]]
- 00585dcc bytes a1481b94
+ 00585e0c bytes c5481b94
- 00585e28 ["INT_ADD", "register:40f0:8", ["const:585e28:8", "const:4:8"]]
- 00585e28 ["CALL", null, ["callee:00c58120:8"]]
+ 00585e68 ["INT_ADD", "register:40f0:8", ["const:585e68:8", "const:4:8"]]
+ 00585e68 ["CALL", null, ["callee:00c58120:8"]]
- 00585e28 bytes 8a481b94
+ 00585e68 bytes ae481b94
- 00585e58 ["INT_ADD", "register:40f0:8", ["const:585e58:8", "const:4:8"]]
- 00585e58 ["CALL", null, ["callee:00c57f80:8"]]
+ 00585e98 ["INT_ADD", "register:40f0:8", ["const:585e98:8", "const:4:8"]]
+ 00585e98 ["CALL", null, ["callee:00c57f80:8"]]
- 00585e58 bytes 16481b94
+ 00585e98 bytes 3a481b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ebccd683df683411c8a25bcf401d19"></a>

### [`00585ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585ec0.md) → [`00585f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f00.md) FUN_00585f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585ec0.md#insn-00585edc) · [`00585efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585ec0.md#insn-00585efc)
- 新版 [`00585f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f00.md#insn-00585f1c) · [`00585f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f00.md#insn-00585f3c)

~~~diff
- 00585edc ["INT_ADD", "register:40f0:8", ["const:585edc:8", "const:4:8"]]
- 00585edc ["CALL", null, ["callee:00c53da0:8"]]
+ 00585f1c ["INT_ADD", "register:40f0:8", ["const:585f1c:8", "const:4:8"]]
+ 00585f1c ["CALL", null, ["callee:00c53da0:8"]]
- 00585edc bytes 89371b94
+ 00585f1c bytes a1371b94
- 00585efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00585efc ["INT_ADD", "register:40f0:8", ["const:585efc:8", "const:4:8"]]
- 00585efc ["CALLIND", null, ["register:0:8"]]
+ 00585f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00585f3c ["INT_ADD", "register:40f0:8", ["const:585f3c:8", "const:4:8"]]
+ 00585f3c ["CALLIND", null, ["register:0:8"]]
- 00585efc bytes 00013fd6
+ 00585f3c bytes 00013fd6
~~~


<a id="compare-d9ce99cf20a7f6f0669f4012a8faece4"></a>

### [`005866dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005866dc.md) → [`0058671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058671c.md) FUN_0058671c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005865dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058661c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005866ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005866dc.md#insn-005866ec)
- 新版 [`0058672c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058671c.md#insn-0058672c)

~~~diff
- 005866ec ["INT_ADD", "register:40f0:8", ["const:5866ec:8", "const:4:8"]]
- 005866ec ["CALL", null, ["callee:0058661c:8"]]
+ 0058672c ["INT_ADD", "register:40f0:8", ["const:58672c:8", "const:4:8"]]
+ 0058672c ["CALL", null, ["callee:0058661c:8"]]
- 005866ec bytes bcffff97
+ 0058672c bytes bcffff97
~~~


<a id="compare-b9e0a8cce2dece743bddc4c10d77b8f6"></a>

### [`00586810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md) → [`00586850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md) FUN_00586850

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md#insn-00586848) · [`00586870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md#insn-00586870) · [`00586890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md#insn-00586890)
- 新版 [`00586888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md#insn-00586888) · [`005868b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md#insn-005868b0) · [`005868d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md#insn-005868d0)

~~~diff
- 00586848 ["COPY", "register:0:8", ["register:4048:8"]]
- 00586848 ["INT_ADD", "register:40f0:8", ["const:586848:8", "const:4:8"]]
- 00586848 ["CALLIND", null, ["register:0:8"]]
+ 00586888 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00586888 ["INT_ADD", "register:40f0:8", ["const:586888:8", "const:4:8"]]
+ 00586888 ["CALLIND", null, ["register:0:8"]]
- 00586848 bytes 20013fd6
+ 00586888 bytes 20013fd6
- 00586870 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586870 ["INT_ADD", "register:40f0:8", ["const:586870:8", "const:4:8"]]
- 00586870 ["CALLIND", null, ["register:0:8"]]
+ 005868b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005868b0 ["INT_ADD", "register:40f0:8", ["const:5868b0:8", "const:4:8"]]
+ 005868b0 ["CALLIND", null, ["register:0:8"]]
- 00586870 bytes 00013fd6
+ 005868b0 bytes 00013fd6
- 00586890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586890 ["INT_ADD", "register:40f0:8", ["const:586890:8", "const:4:8"]]
- 00586890 ["CALLIND", null, ["register:0:8"]]
+ 005868d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005868d0 ["INT_ADD", "register:40f0:8", ["const:5868d0:8", "const:4:8"]]
+ 005868d0 ["CALLIND", null, ["register:0:8"]]
- 00586890 bytes 00013fd6
+ 005868d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-193e11c7fc8e3a8c183f95ac3482f11b"></a>

### [`00586974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md) → [`005869b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md) FUN_005869b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005869a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md#insn-005869a8) · [`005869d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md#insn-005869d0) · [`005869f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md#insn-005869f4)
- 新版 [`005869e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md#insn-005869e8) · [`00586a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md#insn-00586a10) · [`00586a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md#insn-00586a34)

~~~diff
- 005869a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005869a8 ["INT_ADD", "register:40f0:8", ["const:5869a8:8", "const:4:8"]]
- 005869a8 ["CALLIND", null, ["register:0:8"]]
+ 005869e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005869e8 ["INT_ADD", "register:40f0:8", ["const:5869e8:8", "const:4:8"]]
+ 005869e8 ["CALLIND", null, ["register:0:8"]]
- 005869a8 bytes 20013fd6
+ 005869e8 bytes 20013fd6
- 005869d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005869d0 ["INT_ADD", "register:40f0:8", ["const:5869d0:8", "const:4:8"]]
- 005869d0 ["CALLIND", null, ["register:0:8"]]
+ 00586a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586a10 ["INT_ADD", "register:40f0:8", ["const:586a10:8", "const:4:8"]]
+ 00586a10 ["CALLIND", null, ["register:0:8"]]
- 005869d0 bytes 00013fd6
+ 00586a10 bytes 00013fd6
- 005869f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005869f4 ["INT_ADD", "register:40f0:8", ["const:5869f4:8", "const:4:8"]]
- 005869f4 ["CALLIND", null, ["register:0:8"]]
+ 00586a34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586a34 ["INT_ADD", "register:40f0:8", ["const:586a34:8", "const:4:8"]]
+ 00586a34 ["CALLIND", null, ["register:0:8"]]
- 005869f4 bytes 00013fd6
+ 00586a34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e6e910537193c2ecd5f679bba00805"></a>

### [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) → [`00586b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md) FUN_00586b1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0058337c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058337c.md) [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) · 呼出先 2件 [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005833bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833bc.md) [`00586b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md) · 呼出先 2件 [`00586b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md#insn-00586af8) · [`00586b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md#insn-00586b04) · [`00586b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md#insn-00586b38)
- 新版 [`00586b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md#insn-00586b38) · [`00586b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md#insn-00586b44) · [`00586b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b1c.md#insn-00586b78)

~~~diff
- 00586af8 ["INT_ADD", "register:40f0:8", ["const:586af8:8", "const:4:8"]]
- 00586af8 ["CALL", null, ["local:b0:8"]]
+ 00586b38 ["INT_ADD", "register:40f0:8", ["const:586b38:8", "const:4:8"]]
+ 00586b38 ["CALL", null, ["local:b0:8"]]
- 00586af8 bytes f9ffff97
+ 00586b38 bytes f9ffff97
- 00586b04 ["INT_ADD", "register:40f0:8", ["const:586b04:8", "const:4:8"]]
- 00586b04 ["CALL", null, ["local:b0:8"]]
+ 00586b44 ["INT_ADD", "register:40f0:8", ["const:586b44:8", "const:4:8"]]
+ 00586b44 ["CALL", null, ["local:b0:8"]]
- 00586b04 bytes f6ffff97
+ 00586b44 bytes f6ffff97
- 00586b38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586b38 ["INT_ADD", "register:40f0:8", ["const:586b38:8", "const:4:8"]]
- 00586b38 ["CALLIND", null, ["register:0:8"]]
+ 00586b78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586b78 ["INT_ADD", "register:40f0:8", ["const:586b78:8", "const:4:8"]]
+ 00586b78 ["CALLIND", null, ["register:0:8"]]
- 00586b38 bytes 00013fd6
+ 00586b78 bytes 00013fd6
~~~


<a id="compare-8782127f1f9d6f93c9a8f80390fe117c"></a>

### [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) → [`00586b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md) FUN_00586b8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00583384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583384.md) [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) · 呼出先 2件 [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005833c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833c4.md) [`00586b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md) · 呼出先 2件 [`00586b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md#insn-00586b68) · [`00586b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md#insn-00586b74) · [`00586ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md#insn-00586ba8)
- 新版 [`00586ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md#insn-00586ba8) · [`00586bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md#insn-00586bb4) · [`00586be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586b8c.md#insn-00586be8)

~~~diff
- 00586b68 ["INT_ADD", "register:40f0:8", ["const:586b68:8", "const:4:8"]]
- 00586b68 ["CALL", null, ["local:b0:8"]]
+ 00586ba8 ["INT_ADD", "register:40f0:8", ["const:586ba8:8", "const:4:8"]]
+ 00586ba8 ["CALL", null, ["local:b0:8"]]
- 00586b68 bytes f9ffff97
+ 00586ba8 bytes f9ffff97
- 00586b74 ["INT_ADD", "register:40f0:8", ["const:586b74:8", "const:4:8"]]
- 00586b74 ["CALL", null, ["local:b0:8"]]
+ 00586bb4 ["INT_ADD", "register:40f0:8", ["const:586bb4:8", "const:4:8"]]
+ 00586bb4 ["CALL", null, ["local:b0:8"]]
- 00586b74 bytes f6ffff97
+ 00586bb4 bytes f6ffff97
- 00586ba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586ba8 ["INT_ADD", "register:40f0:8", ["const:586ba8:8", "const:4:8"]]
- 00586ba8 ["CALLIND", null, ["register:0:8"]]
+ 00586be8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586be8 ["INT_ADD", "register:40f0:8", ["const:586be8:8", "const:4:8"]]
+ 00586be8 ["CALLIND", null, ["register:0:8"]]
- 00586ba8 bytes 00013fd6
+ 00586be8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81532402f6b29c433954a04313521483"></a>

### [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) → [`00586c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md) FUN_00586c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00586d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md) [`00586fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00588394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00586d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586d78.md) [`00586ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586ff0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md#insn-00586c78) · [`00586ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md#insn-00586ca0) · [`00586ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md#insn-00586ccc)
- 新版 [`00586cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md#insn-00586cb8) · [`00586ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md#insn-00586ce0) · [`00586d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md#insn-00586d0c)

~~~diff
- 00586c78 ["INT_ADD", "register:40f0:8", ["const:586c78:8", "const:4:8"]]
- 00586c78 ["CALL", null, ["callee:00586d78:8"]]
+ 00586cb8 ["INT_ADD", "register:40f0:8", ["const:586cb8:8", "const:4:8"]]
+ 00586cb8 ["CALL", null, ["callee:00586d78:8"]]
- 00586c78 bytes 30000094
+ 00586cb8 bytes 30000094
- 00586ca0 ["INT_ADD", "register:40f0:8", ["const:586ca0:8", "const:4:8"]]
- 00586ca0 ["CALL", null, ["callee:00586ff0:8"]]
+ 00586ce0 ["INT_ADD", "register:40f0:8", ["const:586ce0:8", "const:4:8"]]
+ 00586ce0 ["CALL", null, ["callee:00586ff0:8"]]
- 00586ca0 bytes c4000094
+ 00586ce0 bytes c4000094
- 00586ccc ["INT_ADD", "register:40f0:8", ["const:586ccc:8", "const:4:8"]]
- 00586ccc ["CALL", null, ["callee:0043bbe4:8"]]
+ 00586d0c ["INT_ADD", "register:40f0:8", ["const:586d0c:8", "const:4:8"]]
+ 00586d0c ["CALL", null, ["callee:0043bbe4:8"]]
- 00586ccc bytes b6d3fa97
+ 00586d0c bytes b6d3fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cae55a71b22ce8fafe461c1a975c93c"></a>

### [`00586d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md) → [`00586d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586d78.md) FUN_00586d78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) · 呼出先 1件 [`00c5a2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2e0.md)
- 新版 呼出元 1件 [`00586c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md) · 呼出先 1件 [`00c5a3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md#insn-00586d9c) · [`00586dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md#insn-00586dd4) · [`00586e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md#insn-00586e44)
- 新版 [`00586ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586d78.md#insn-00586ddc) · [`00586e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586d78.md#insn-00586e14) · [`00586e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586d78.md#insn-00586e84)

~~~diff
- 00586d9c ["INT_ADD", "register:40f0:8", ["const:586d9c:8", "const:4:8"]]
- 00586d9c ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00586ddc ["INT_ADD", "register:40f0:8", ["const:586ddc:8", "const:4:8"]]
+ 00586ddc ["CALL", null, ["callee:00c5a3b0:8"]]
- 00586d9c bytes 514d1b94
+ 00586ddc bytes 754d1b94
- 00586dd4 ["INT_ADD", "register:40f0:8", ["const:586dd4:8", "const:4:8"]]
- 00586dd4 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00586e14 ["INT_ADD", "register:40f0:8", ["const:586e14:8", "const:4:8"]]
+ 00586e14 ["CALL", null, ["callee:00c5a3b0:8"]]
- 00586dd4 bytes 434d1b94
+ 00586e14 bytes 674d1b94
- 00586e44 ["INT_ADD", "register:40f0:8", ["const:586e44:8", "const:4:8"]]
- 00586e44 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00586e84 ["INT_ADD", "register:40f0:8", ["const:586e84:8", "const:4:8"]]
+ 00586e84 ["CALL", null, ["callee:00c5a3b0:8"]]
- 00586e44 bytes 274d1b94
+ 00586e84 bytes 4b4d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eeadddff2c6838b0d14c4fd191b57c0"></a>

### [`00586fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md) → [`00586ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586ff0.md) FUN_00586ff0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00586c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md#insn-00586fd0) · [`00587004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md#insn-00587004) · [`00587030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md#insn-00587030)
- 新版 [`00587010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586ff0.md#insn-00587010) · [`00587044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586ff0.md#insn-00587044) · [`00587070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586ff0.md#insn-00587070)

~~~diff
- 00586fd0 ["INT_ADD", "register:40f0:8", ["const:586fd0:8", "const:4:8"]]
- 00586fd0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00587010 ["INT_ADD", "register:40f0:8", ["const:587010:8", "const:4:8"]]
+ 00587010 ["CALL", null, ["callee:00c57f60:8"]]
- 00586fd0 bytes b0431b94
+ 00587010 bytes d4431b94
- 00587004 ["INT_ADD", "register:40f0:8", ["const:587004:8", "const:4:8"]]
- 00587004 ["CALL", null, ["callee:0043bb60:8"]]
+ 00587044 ["INT_ADD", "register:40f0:8", ["const:587044:8", "const:4:8"]]
+ 00587044 ["CALL", null, ["callee:0043bb60:8"]]
- 00587004 bytes c7d2fa97
+ 00587044 bytes c7d2fa97
- 00587030 ["INT_ADD", "register:40f0:8", ["const:587030:8", "const:4:8"]]
- 00587030 ["CALL", null, ["callee:0043bb60:8"]]
+ 00587070 ["INT_ADD", "register:40f0:8", ["const:587070:8", "const:4:8"]]
+ 00587070 ["CALL", null, ["callee:0043bb60:8"]]
- 00587030 bytes bcd2fa97
+ 00587070 bytes bcd2fa97
~~~


<a id="compare-f67ad6213a25161ed5255e1a9ff12350"></a>

### [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) → [`005870b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md) FUN_005870b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) · 呼出先 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005870b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md) [`00587f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md) · 呼出先 2件 [`005870b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md#insn-00587094) · [`005870a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md#insn-005870a0) · [`005870b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md#insn-005870b0)
- 新版 [`005870d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md#insn-005870d4) · [`005870e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md#insn-005870e0) · [`005870f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md#insn-005870f0)

~~~diff
- 00587094 ["INT_ADD", "register:40f0:8", ["const:587094:8", "const:4:8"]]
- 00587094 ["CALL", null, ["local:b0:8"]]
+ 005870d4 ["INT_ADD", "register:40f0:8", ["const:5870d4:8", "const:4:8"]]
+ 005870d4 ["CALL", null, ["local:b0:8"]]
- 00587094 bytes f9ffff97
+ 005870d4 bytes f9ffff97
- 005870a0 ["INT_ADD", "register:40f0:8", ["const:5870a0:8", "const:4:8"]]
- 005870a0 ["CALL", null, ["local:b0:8"]]
+ 005870e0 ["INT_ADD", "register:40f0:8", ["const:5870e0:8", "const:4:8"]]
+ 005870e0 ["CALL", null, ["local:b0:8"]]
- 005870a0 bytes f6ffff97
+ 005870e0 bytes f6ffff97
- 005870b0 ["INT_ADD", "register:40f0:8", ["const:5870b0:8", "const:4:8"]]
- 005870b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005870f0 ["INT_ADD", "register:40f0:8", ["const:5870f0:8", "const:4:8"]]
+ 005870f0 ["CALL", null, ["callee:00c57f80:8"]]
- 005870b0 bytes 80431b94
+ 005870f0 bytes a4431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cadd2c509b426db21c22530f9ceb47d"></a>

### [`00587128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md) → [`00587168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md) FUN_00587168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md#insn-00587194) · [`005871f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md#insn-005871f0) · [`0058721c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md#insn-0058721c)
- 新版 [`005871d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md#insn-005871d4) · [`00587230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md#insn-00587230) · [`0058725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md#insn-0058725c)

~~~diff
- 00587194 ["INT_ADD", "register:40f0:8", ["const:587194:8", "const:4:8"]]
- 00587194 ["CALL", null, ["callee:00c57f60:8"]]
+ 005871d4 ["INT_ADD", "register:40f0:8", ["const:5871d4:8", "const:4:8"]]
+ 005871d4 ["CALL", null, ["callee:00c57f60:8"]]
- 00587194 bytes 3f431b94
+ 005871d4 bytes 63431b94
- 005871f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005871f0 ["INT_ADD", "register:40f0:8", ["const:5871f0:8", "const:4:8"]]
- 005871f0 ["CALLIND", null, ["register:0:8"]]
+ 00587230 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00587230 ["INT_ADD", "register:40f0:8", ["const:587230:8", "const:4:8"]]
+ 00587230 ["CALLIND", null, ["register:0:8"]]
- 005871f0 bytes 20013fd6
+ 00587230 bytes 20013fd6
- 0058721c ["INT_ADD", "register:40f0:8", ["const:58721c:8", "const:4:8"]]
- 0058721c ["CALL", null, ["callee:0043bbe4:8"]]
+ 0058725c ["INT_ADD", "register:40f0:8", ["const:58725c:8", "const:4:8"]]
+ 0058725c ["CALL", null, ["callee:0043bbe4:8"]]
- 0058721c bytes 62d2fa97
+ 0058725c bytes 62d2fa97
~~~


<a id="compare-e9abb533c1545a5eb1ea9c5ce4f5015a"></a>

### [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md) → [`0058728c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md) FUN_0058728c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00587334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00587374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587374.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005872bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md#insn-005872bc) · [`005872d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md#insn-005872d4) · [`00587300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md#insn-00587300)
- 新版 [`005872fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md#insn-005872fc) · [`00587314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md#insn-00587314) · [`00587340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md#insn-00587340)

~~~diff
- 005872bc ["INT_ADD", "register:40f0:8", ["const:5872bc:8", "const:4:8"]]
- 005872bc ["CALL", null, ["callee:00c57f60:8"]]
+ 005872fc ["INT_ADD", "register:40f0:8", ["const:5872fc:8", "const:4:8"]]
+ 005872fc ["CALL", null, ["callee:00c57f60:8"]]
- 005872bc bytes f5421b94
+ 005872fc bytes 19431b94
- 005872d4 ["INT_ADD", "register:40f0:8", ["const:5872d4:8", "const:4:8"]]
- 005872d4 ["CALL", null, ["callee:00587374:8"]]
+ 00587314 ["INT_ADD", "register:40f0:8", ["const:587314:8", "const:4:8"]]
+ 00587314 ["CALL", null, ["callee:00587374:8"]]
- 005872d4 bytes 18000094
+ 00587314 bytes 18000094
- 00587300 ["INT_ADD", "register:40f0:8", ["const:587300:8", "const:4:8"]]
- 00587300 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00587340 ["INT_ADD", "register:40f0:8", ["const:587340:8", "const:4:8"]]
+ 00587340 ["CALL", null, ["callee:0043bbe4:8"]]
- 00587300 bytes 29d2fa97
+ 00587340 bytes 29d2fa97
~~~


<a id="compare-5eea01b99d802fbd9e6874e62d5b1c29"></a>

### [`00587334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md) → [`00587374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587374.md) FUN_00587374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058728c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md#insn-00587384) · [`005873c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md#insn-005873c8) · [`0058740c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md#insn-0058740c)
- 新版 [`005873c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587374.md#insn-005873c4) · [`00587408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587374.md#insn-00587408) · [`0058744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587374.md#insn-0058744c)

~~~diff
- 00587384 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587384 ["INT_ADD", "register:40f0:8", ["const:587384:8", "const:4:8"]]
- 00587384 ["CALLIND", null, ["register:0:8"]]
+ 005873c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005873c4 ["INT_ADD", "register:40f0:8", ["const:5873c4:8", "const:4:8"]]
+ 005873c4 ["CALLIND", null, ["register:0:8"]]
- 00587384 bytes 00013fd6
+ 005873c4 bytes 00013fd6
- 005873c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005873c8 ["INT_ADD", "register:40f0:8", ["const:5873c8:8", "const:4:8"]]
- 005873c8 ["CALLIND", null, ["register:0:8"]]
+ 00587408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587408 ["INT_ADD", "register:40f0:8", ["const:587408:8", "const:4:8"]]
+ 00587408 ["CALLIND", null, ["register:0:8"]]
- 005873c8 bytes 00013fd6
+ 00587408 bytes 00013fd6
- 0058740c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058740c ["INT_ADD", "register:40f0:8", ["const:58740c:8", "const:4:8"]]
- 0058740c ["CALLIND", null, ["register:0:8"]]
+ 0058744c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058744c ["INT_ADD", "register:40f0:8", ["const:58744c:8", "const:4:8"]]
+ 0058744c ["CALLIND", null, ["register:0:8"]]
- 0058740c bytes 00013fd6
+ 0058744c bytes 00013fd6
~~~


<a id="compare-007593d01fbe5e690cd6c3765f89a086"></a>

### [`005874c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md) → [`00587508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md) FUN_00587508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005874f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md#insn-005874f0) · [`00587504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md#insn-00587504) · [`0058750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md#insn-0058750c)
- 新版 [`00587530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md#insn-00587530) · [`00587544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md#insn-00587544) · [`0058754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md#insn-0058754c)

~~~diff
- 005874f0 ["INT_ADD", "register:40f0:8", ["const:5874f0:8", "const:4:8"]]
- 005874f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00587530 ["INT_ADD", "register:40f0:8", ["const:587530:8", "const:4:8"]]
+ 00587530 ["CALL", null, ["callee:00c53da0:8"]]
- 005874f0 bytes 04321b94
+ 00587530 bytes 1c321b94
- 00587504 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587504 ["INT_ADD", "register:40f0:8", ["const:587504:8", "const:4:8"]]
- 00587504 ["CALLIND", null, ["register:0:8"]]
+ 00587544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587544 ["INT_ADD", "register:40f0:8", ["const:587544:8", "const:4:8"]]
+ 00587544 ["CALLIND", null, ["register:0:8"]]
- 00587504 bytes 00013fd6
+ 00587544 bytes 00013fd6
- 0058750c ["INT_ADD", "register:40f0:8", ["const:58750c:8", "const:4:8"]]
- 0058750c ["CALL", null, ["callee:00c57f50:8"]]
+ 0058754c ["INT_ADD", "register:40f0:8", ["const:58754c:8", "const:4:8"]]
+ 0058754c ["CALL", null, ["callee:00c57f50:8"]]
- 0058750c bytes 5d421b94
+ 0058754c bytes 81421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd4bd2c60705d21f88c7555f6b48c454"></a>

### [`00587558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587558.md) → [`00587598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587598.md) FUN_00587598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587558.md#insn-00587578) · [`00587590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587558.md#insn-00587590) · [`005875b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587558.md#insn-005875b0)
- 新版 [`005875b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587598.md#insn-005875b8) · [`005875d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587598.md#insn-005875d0) · [`005875f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587598.md#insn-005875f0)

~~~diff
- 00587578 ["INT_ADD", "register:40f0:8", ["const:587578:8", "const:4:8"]]
- 00587578 ["CALL", null, ["callee:00c53da0:8"]]
+ 005875b8 ["INT_ADD", "register:40f0:8", ["const:5875b8:8", "const:4:8"]]
+ 005875b8 ["CALL", null, ["callee:00c53da0:8"]]
- 00587578 bytes e2311b94
+ 005875b8 bytes fa311b94
- 00587590 ["INT_ADD", "register:40f0:8", ["const:587590:8", "const:4:8"]]
- 00587590 ["CALL", null, ["callee:00c53da0:8"]]
+ 005875d0 ["INT_ADD", "register:40f0:8", ["const:5875d0:8", "const:4:8"]]
+ 005875d0 ["CALL", null, ["callee:00c53da0:8"]]
- 00587590 bytes dc311b94
+ 005875d0 bytes f4311b94
- 005875b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005875b0 ["INT_ADD", "register:40f0:8", ["const:5875b0:8", "const:4:8"]]
- 005875b0 ["CALLIND", null, ["register:0:8"]]
+ 005875f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005875f0 ["INT_ADD", "register:40f0:8", ["const:5875f0:8", "const:4:8"]]
+ 005875f0 ["CALLIND", null, ["register:0:8"]]
- 005875b0 bytes 00013fd6
+ 005875f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f970af522202b2f8318c54c6d681483"></a>

### [`0058784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md) → [`0058788c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058788c.md) FUN_0058788c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md#insn-00587868) · [`00587888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md#insn-00587888)
- 新版 [`005878a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058788c.md#insn-005878a8) · [`005878c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058788c.md#insn-005878c8)

~~~diff
- 00587868 ["INT_ADD", "register:40f0:8", ["const:587868:8", "const:4:8"]]
- 00587868 ["CALL", null, ["callee:00c53da0:8"]]
+ 005878a8 ["INT_ADD", "register:40f0:8", ["const:5878a8:8", "const:4:8"]]
+ 005878a8 ["CALL", null, ["callee:00c53da0:8"]]
- 00587868 bytes 26311b94
+ 005878a8 bytes 3e311b94
- 00587888 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587888 ["INT_ADD", "register:40f0:8", ["const:587888:8", "const:4:8"]]
- 00587888 ["CALLIND", null, ["register:0:8"]]
+ 005878c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005878c8 ["INT_ADD", "register:40f0:8", ["const:5878c8:8", "const:4:8"]]
+ 005878c8 ["CALLIND", null, ["register:0:8"]]
- 00587888 bytes 00013fd6
+ 005878c8 bytes 00013fd6
~~~


<a id="compare-c112fb8b4fdd1e6f30aa0e21f46e4df5"></a>

### [`0058789c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058789c.md) → [`005878dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005878dc.md) FUN_005878dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005878bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058789c.md#insn-005878bc) · [`005878d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058789c.md#insn-005878d0) · [`005878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058789c.md#insn-005878d8)
- 新版 [`005878fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005878dc.md#insn-005878fc) · [`00587910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005878dc.md#insn-00587910) · [`00587918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005878dc.md#insn-00587918)

~~~diff
- 005878bc ["INT_ADD", "register:40f0:8", ["const:5878bc:8", "const:4:8"]]
- 005878bc ["CALL", null, ["callee:00c53da0:8"]]
+ 005878fc ["INT_ADD", "register:40f0:8", ["const:5878fc:8", "const:4:8"]]
+ 005878fc ["CALL", null, ["callee:00c53da0:8"]]
- 005878bc bytes 11311b94
+ 005878fc bytes 29311b94
- 005878d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005878d0 ["INT_ADD", "register:40f0:8", ["const:5878d0:8", "const:4:8"]]
- 005878d0 ["CALLIND", null, ["register:0:8"]]
+ 00587910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587910 ["INT_ADD", "register:40f0:8", ["const:587910:8", "const:4:8"]]
+ 00587910 ["CALLIND", null, ["register:0:8"]]
- 005878d0 bytes 00013fd6
+ 00587910 bytes 00013fd6
- 005878d8 ["INT_ADD", "register:40f0:8", ["const:5878d8:8", "const:4:8"]]
- 005878d8 ["CALL", null, ["callee:00c57f50:8"]]
+ 00587918 ["INT_ADD", "register:40f0:8", ["const:587918:8", "const:4:8"]]
+ 00587918 ["CALL", null, ["callee:00c57f50:8"]]
- 005878d8 bytes 6a411b94
+ 00587918 bytes 8e411b94
~~~


<a id="compare-419a9cbb4a94c9468ab9dd0ca76cc47d"></a>

### [`005878ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md) → [`0058792c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058792c.md) FUN_0058792c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00587a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00587a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587a88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md#insn-0058792c) · [`00587944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md#insn-00587944) · [`00587958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md#insn-00587958)
- 新版 [`0058796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058792c.md#insn-0058796c) · [`00587984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058792c.md#insn-00587984) · [`00587998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058792c.md#insn-00587998)

~~~diff
- 0058792c ["INT_ADD", "register:40f0:8", ["const:58792c:8", "const:4:8"]]
- 0058792c ["CALL", null, ["callee:00c53d70:8"]]
+ 0058796c ["INT_ADD", "register:40f0:8", ["const:58796c:8", "const:4:8"]]
+ 0058796c ["CALL", null, ["callee:00c53d70:8"]]
- 0058792c bytes e9301b94
+ 0058796c bytes 01311b94
- 00587944 ["INT_ADD", "register:40f0:8", ["const:587944:8", "const:4:8"]]
- 00587944 ["CALL", null, ["callee:00c53d70:8"]]
+ 00587984 ["INT_ADD", "register:40f0:8", ["const:587984:8", "const:4:8"]]
+ 00587984 ["CALL", null, ["callee:00c53d70:8"]]
- 00587944 bytes e3301b94
+ 00587984 bytes fb301b94
- 00587958 ["INT_ADD", "register:40f0:8", ["const:587958:8", "const:4:8"]]
- 00587958 ["CALL", null, ["callee:00587a88:8"]]
+ 00587998 ["INT_ADD", "register:40f0:8", ["const:587998:8", "const:4:8"]]
+ 00587998 ["CALL", null, ["callee:00587a88:8"]]
- 00587958 bytes 3c000094
+ 00587998 bytes 3c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2c0651f51d01f96d1f4ab2cae0c35db"></a>

### [`00587a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md) → [`00587a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587a88.md) FUN_00587a88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005878ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`0058792c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058792c.md) · 呼出先 6件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md#insn-00587a74) · [`00587a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md#insn-00587a8c) · [`00587ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md#insn-00587ac8)
- 新版 [`00587ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587a88.md#insn-00587ab4) · [`00587acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587a88.md#insn-00587acc) · [`00587b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587a88.md#insn-00587b08)

~~~diff
- 00587a74 ["INT_ADD", "register:40f0:8", ["const:587a74:8", "const:4:8"]]
- 00587a74 ["CALL", null, ["callee:00c581b0:8"]]
+ 00587ab4 ["INT_ADD", "register:40f0:8", ["const:587ab4:8", "const:4:8"]]
+ 00587ab4 ["CALL", null, ["callee:00c581b0:8"]]
- 00587a74 bytes 9b411b94
+ 00587ab4 bytes bf411b94
- 00587a8c ["INT_ADD", "register:40f0:8", ["const:587a8c:8", "const:4:8"]]
- 00587a8c ["CALL", null, ["callee:00c583c0:8"]]
+ 00587acc ["INT_ADD", "register:40f0:8", ["const:587acc:8", "const:4:8"]]
+ 00587acc ["CALL", null, ["callee:00c583c0:8"]]
- 00587a8c bytes 19421b94
+ 00587acc bytes 3d421b94
- 00587ac8 ["INT_ADD", "register:40f0:8", ["const:587ac8:8", "const:4:8"]]
- 00587ac8 ["CALL", null, ["callee:00c58450:8"]]
+ 00587b08 ["INT_ADD", "register:40f0:8", ["const:587b08:8", "const:4:8"]]
+ 00587b08 ["CALL", null, ["callee:00c58450:8"]]
- 00587ac8 bytes 2e421b94
+ 00587b08 bytes 52421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-104a59d5bf1256205953d6219d1abb48"></a>

### [`00587b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587b38.md) → [`00587b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587b78.md) FUN_00587b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 8件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 8件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587b38.md#insn-00587b74) · [`00587b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587b38.md#insn-00587b80) · [`00587b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587b38.md#insn-00587b94)
- 新版 [`00587bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587b78.md#insn-00587bb4) · [`00587bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587b78.md#insn-00587bc0) · [`00587bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587b78.md#insn-00587bd4)

~~~diff
- 00587b74 ["INT_ADD", "register:40f0:8", ["const:587b74:8", "const:4:8"]]
- 00587b74 ["CALL", null, ["callee:00c581b0:8"]]
+ 00587bb4 ["INT_ADD", "register:40f0:8", ["const:587bb4:8", "const:4:8"]]
+ 00587bb4 ["CALL", null, ["callee:00c581b0:8"]]
- 00587b74 bytes 5b411b94
+ 00587bb4 bytes 7f411b94
- 00587b80 ["INT_ADD", "register:40f0:8", ["const:587b80:8", "const:4:8"]]
- 00587b80 ["CALL", null, ["callee:00c58570:8"]]
+ 00587bc0 ["INT_ADD", "register:40f0:8", ["const:587bc0:8", "const:4:8"]]
+ 00587bc0 ["CALL", null, ["callee:00c58570:8"]]
- 00587b80 bytes 48421b94
+ 00587bc0 bytes 6c421b94
- 00587b94 ["INT_ADD", "register:40f0:8", ["const:587b94:8", "const:4:8"]]
- 00587b94 ["CALL", null, ["callee:00c583c0:8"]]
+ 00587bd4 ["INT_ADD", "register:40f0:8", ["const:587bd4:8", "const:4:8"]]
+ 00587bd4 ["CALL", null, ["callee:00c583c0:8"]]
- 00587b94 bytes d7411b94
+ 00587bd4 bytes fb411b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821a940b82478281b8beac8f43d05911"></a>

### [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) → [`00587c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md) FUN_00587c94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00587d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005850a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/005850a0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00587dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md#insn-00587cc0) · [`00587d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md#insn-00587d30) · [`00587d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md#insn-00587d44)
- 新版 [`00587d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md#insn-00587d00) · [`00587d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md#insn-00587d70) · [`00587d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md#insn-00587d84)

~~~diff
- 00587cc0 ["INT_ADD", "register:40f0:8", ["const:587cc0:8", "const:4:8"]]
- 00587cc0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00587d00 ["INT_ADD", "register:40f0:8", ["const:587d00:8", "const:4:8"]]
+ 00587d00 ["CALL", null, ["callee:00c57f60:8"]]
- 00587cc0 bytes 74401b94
+ 00587d00 bytes 98401b94
- 00587d30 ["INT_ADD", "register:40f0:8", ["const:587d30:8", "const:4:8"]]
- 00587d30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00587d70 ["INT_ADD", "register:40f0:8", ["const:587d70:8", "const:4:8"]]
+ 00587d70 ["CALL", null, ["callee:00c53da0:8"]]
- 00587d30 bytes f42f1b94
+ 00587d70 bytes 0c301b94
- 00587d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587d44 ["INT_ADD", "register:40f0:8", ["const:587d44:8", "const:4:8"]]
- 00587d44 ["CALLIND", null, ["register:0:8"]]
+ 00587d84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587d84 ["INT_ADD", "register:40f0:8", ["const:587d84:8", "const:4:8"]]
+ 00587d84 ["CALLIND", null, ["register:0:8"]]
- 00587d44 bytes 00013fd6
+ 00587d84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7737324f90d1f2754768de8b3de61bf9"></a>

### [`005880f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md) → [`00588134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md) FUN_00588134

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md#insn-0058815c) · [`0058818c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md#insn-0058818c) · [`005881c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md#insn-005881c0)
- 新版 [`0058819c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md#insn-0058819c) · [`005881cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md#insn-005881cc) · [`00588200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md#insn-00588200)

~~~diff
- 0058815c ["INT_ADD", "register:40f0:8", ["const:58815c:8", "const:4:8"]]
- 0058815c ["CALL", null, ["callee:00494650:8"]]
+ 0058819c ["INT_ADD", "register:40f0:8", ["const:58819c:8", "const:4:8"]]
+ 0058819c ["CALL", null, ["callee:00494650:8"]]
- 0058815c bytes 2d31fc97
+ 0058819c bytes 2d31fc97
- 0058818c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058818c ["INT_ADD", "register:40f0:8", ["const:58818c:8", "const:4:8"]]
- 0058818c ["CALLIND", null, ["register:0:8"]]
+ 005881cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005881cc ["INT_ADD", "register:40f0:8", ["const:5881cc:8", "const:4:8"]]
+ 005881cc ["CALLIND", null, ["register:0:8"]]
- 0058818c bytes 00013fd6
+ 005881cc bytes 00013fd6
- 005881c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005881c0 ["INT_ADD", "register:40f0:8", ["const:5881c0:8", "const:4:8"]]
- 005881c0 ["CALLIND", null, ["register:0:8"]]
+ 00588200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588200 ["INT_ADD", "register:40f0:8", ["const:588200:8", "const:4:8"]]
+ 00588200 ["CALLIND", null, ["register:0:8"]]
- 005881c0 bytes 00013fd6
+ 00588200 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00402df220df15c8647b5038baa99632"></a>

### [`0058820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md) → [`0058824c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058824c.md) FUN_0058824c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00585d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054f1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f1d4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md#insn-0058824c) · [`0058826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md#insn-0058826c) · [`005882a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md#insn-005882a0)
- 新版 [`0058828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058824c.md#insn-0058828c) · [`005882ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058824c.md#insn-005882ac) · [`005882e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058824c.md#insn-005882e0)

~~~diff
- 0058824c ["INT_ADD", "register:40f0:8", ["const:58824c:8", "const:4:8"]]
- 0058824c ["CALL", null, ["callee:0054f1d4:8"]]
+ 0058828c ["INT_ADD", "register:40f0:8", ["const:58828c:8", "const:4:8"]]
+ 0058828c ["CALL", null, ["callee:0054f1d4:8"]]
- 0058824c bytes d21bff97
+ 0058828c bytes d21bff97
- 0058826c ["INT_ADD", "register:40f0:8", ["const:58826c:8", "const:4:8"]]
- 0058826c ["CALL", null, ["callee:00c57f60:8"]]
+ 005882ac ["INT_ADD", "register:40f0:8", ["const:5882ac:8", "const:4:8"]]
+ 005882ac ["CALL", null, ["callee:00c57f60:8"]]
- 0058826c bytes 093f1b94
+ 005882ac bytes 2d3f1b94
- 005882a0 ["INT_ADD", "register:40f0:8", ["const:5882a0:8", "const:4:8"]]
- 005882a0 ["CALL", null, ["callee:0043bb60:8"]]
+ 005882e0 ["INT_ADD", "register:40f0:8", ["const:5882e0:8", "const:4:8"]]
+ 005882e0 ["CALL", null, ["callee:0043bb60:8"]]
- 005882a0 bytes 20cefa97
+ 005882e0 bytes 20cefa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95be5c3c4100af91d56db4a590347855"></a>

### [`005885a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885a8.md) → [`005885e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885e8.md) FUN_005885e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005885c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885a8.md#insn-005885c4) · [`005885e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885a8.md#insn-005885e4)
- 新版 [`00588604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885e8.md#insn-00588604) · [`00588624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885e8.md#insn-00588624)

~~~diff
- 005885c4 ["INT_ADD", "register:40f0:8", ["const:5885c4:8", "const:4:8"]]
- 005885c4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00588604 ["INT_ADD", "register:40f0:8", ["const:588604:8", "const:4:8"]]
+ 00588604 ["CALL", null, ["callee:00c53da0:8"]]
- 005885c4 bytes cf2d1b94
+ 00588604 bytes e72d1b94
- 005885e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005885e4 ["INT_ADD", "register:40f0:8", ["const:5885e4:8", "const:4:8"]]
- 005885e4 ["CALLIND", null, ["register:0:8"]]
+ 00588624 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588624 ["INT_ADD", "register:40f0:8", ["const:588624:8", "const:4:8"]]
+ 00588624 ["CALLIND", null, ["register:0:8"]]
- 005885e4 bytes 00013fd6
+ 00588624 bytes 00013fd6
~~~


<a id="compare-8f93bc322316d5a0e7c71225c4047016"></a>

### [`005888f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005888f4.md) → [`00588934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588934.md) FUN_00588934

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005888f4.md#insn-0058890c)
- 新版 [`0058894c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588934.md#insn-0058894c)

~~~diff
- 0058890c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058890c ["INT_ADD", "register:40f0:8", ["const:58890c:8", "const:4:8"]]
- 0058890c ["CALLIND", null, ["register:0:8"]]
+ 0058894c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058894c ["INT_ADD", "register:40f0:8", ["const:58894c:8", "const:4:8"]]
+ 0058894c ["CALLIND", null, ["register:0:8"]]
- 0058890c bytes 00013fd6
+ 0058894c bytes 00013fd6
~~~


<a id="compare-15c8de92e78adfefcf3c5d54f1d7dbe4"></a>

### [`00588948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588948.md) → [`00588988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588988.md) FUN_00588988

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588948.md#insn-00588974) · [`005889a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588948.md#insn-005889a4)
- 新版 [`005889b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588988.md#insn-005889b4) · [`005889e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588988.md#insn-005889e4)

~~~diff
- 00588974 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588974 ["INT_ADD", "register:40f0:8", ["const:588974:8", "const:4:8"]]
- 00588974 ["CALLIND", null, ["register:0:8"]]
+ 005889b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005889b4 ["INT_ADD", "register:40f0:8", ["const:5889b4:8", "const:4:8"]]
+ 005889b4 ["CALLIND", null, ["register:0:8"]]
- 00588974 bytes 00013fd6
+ 005889b4 bytes 00013fd6
- 005889a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005889a4 ["INT_ADD", "register:40f0:8", ["const:5889a4:8", "const:4:8"]]
- 005889a4 ["CALLIND", null, ["register:0:8"]]
+ 005889e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005889e4 ["INT_ADD", "register:40f0:8", ["const:5889e4:8", "const:4:8"]]
+ 005889e4 ["CALLIND", null, ["register:0:8"]]
- 005889a4 bytes 00013fd6
+ 005889e4 bytes 00013fd6
~~~


<a id="compare-6d41698fdf5254ff808b2d4ab110493d"></a>

### [`005889f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005889f8.md) → [`00588a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588a38.md) FUN_00588a38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005889f8.md#insn-00588a10)
- 新版 [`00588a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588a38.md#insn-00588a50)

~~~diff
- 00588a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588a10 ["INT_ADD", "register:40f0:8", ["const:588a10:8", "const:4:8"]]
- 00588a10 ["CALLIND", null, ["register:0:8"]]
+ 00588a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588a50 ["INT_ADD", "register:40f0:8", ["const:588a50:8", "const:4:8"]]
+ 00588a50 ["CALLIND", null, ["register:0:8"]]
- 00588a10 bytes 00013fd6
+ 00588a50 bytes 00013fd6
~~~


<a id="compare-b926c63e4ebe61a28a62286ea4250309"></a>

### [`00588a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588a48.md) → [`00588a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588a88.md) FUN_00588a88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588a48.md#insn-00588a74) · [`00588aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588a48.md#insn-00588aa4)
- 新版 [`00588ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588a88.md#insn-00588ab4) · [`00588ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588a88.md#insn-00588ae4)

~~~diff
- 00588a74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588a74 ["INT_ADD", "register:40f0:8", ["const:588a74:8", "const:4:8"]]
- 00588a74 ["CALLIND", null, ["register:0:8"]]
+ 00588ab4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588ab4 ["INT_ADD", "register:40f0:8", ["const:588ab4:8", "const:4:8"]]
+ 00588ab4 ["CALLIND", null, ["register:0:8"]]
- 00588a74 bytes 00013fd6
+ 00588ab4 bytes 00013fd6
- 00588aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588aa4 ["INT_ADD", "register:40f0:8", ["const:588aa4:8", "const:4:8"]]
- 00588aa4 ["CALLIND", null, ["register:0:8"]]
+ 00588ae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588ae4 ["INT_ADD", "register:40f0:8", ["const:588ae4:8", "const:4:8"]]
+ 00588ae4 ["CALLIND", null, ["register:0:8"]]
- 00588aa4 bytes 00013fd6
+ 00588ae4 bytes 00013fd6
~~~


<a id="compare-23e8f256dd2310a0fe67881ae2f43c98"></a>

### [`00588af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md) → [`00588b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md) FUN_00588b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597600.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00597640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597640.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00588c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md#insn-00588b20) · [`00588b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md#insn-00588b34) · [`00588b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md#insn-00588b58)
- 新版 [`00588b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md#insn-00588b60) · [`00588b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md#insn-00588b74) · [`00588b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md#insn-00588b98)

~~~diff
- 00588b20 ["INT_ADD", "register:40f0:8", ["const:588b20:8", "const:4:8"]]
- 00588b20 ["CALL", null, ["callee:00550be4:8"]]
+ 00588b60 ["INT_ADD", "register:40f0:8", ["const:588b60:8", "const:4:8"]]
+ 00588b60 ["CALL", null, ["callee:00550be4:8"]]
- 00588b20 bytes 2120ff97
+ 00588b60 bytes 2120ff97
- 00588b34 ["INT_ADD", "register:40f0:8", ["const:588b34:8", "const:4:8"]]
- 00588b34 ["CALL", null, ["callee:00588c00:8"]]
+ 00588b74 ["INT_ADD", "register:40f0:8", ["const:588b74:8", "const:4:8"]]
+ 00588b74 ["CALL", null, ["callee:00588c00:8"]]
- 00588b34 bytes 23000094
+ 00588b74 bytes 23000094
- 00588b58 ["INT_ADD", "register:40f0:8", ["const:588b58:8", "const:4:8"]]
- 00588b58 ["CALL", null, ["callee:00c53da0:8"]]
+ 00588b98 ["INT_ADD", "register:40f0:8", ["const:588b98:8", "const:4:8"]]
+ 00588b98 ["CALL", null, ["callee:00c53da0:8"]]
- 00588b58 bytes 6a2c1b94
+ 00588b98 bytes 822c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e952bc68fe791a9d5fe719cce7ac944"></a>

### [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md) → [`00588d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md) FUN_00588d2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) [`0058b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md) [`0058b1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1b0.md) [`00595028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 4件 [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) [`0058b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b170.md) [`0058b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b1f0.md) [`00595068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595068.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md#insn-00588d80) · [`00588dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md#insn-00588dac) · [`00588dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md#insn-00588dc0)
- 新版 [`00588dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md#insn-00588dc0) · [`00588dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md#insn-00588dec) · [`00588e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md#insn-00588e00)

~~~diff
- 00588d80 ["INT_ADD", "register:40f0:8", ["const:588d80:8", "const:4:8"]]
- 00588d80 ["CALL", null, ["callee:00c57f60:8"]]
+ 00588dc0 ["INT_ADD", "register:40f0:8", ["const:588dc0:8", "const:4:8"]]
+ 00588dc0 ["CALL", null, ["callee:00c57f60:8"]]
- 00588d80 bytes 443c1b94
+ 00588dc0 bytes 683c1b94
- 00588dac ["INT_ADD", "register:40f0:8", ["const:588dac:8", "const:4:8"]]
- 00588dac ["CALL", null, ["callee:00c580d0:8"]]
+ 00588dec ["INT_ADD", "register:40f0:8", ["const:588dec:8", "const:4:8"]]
+ 00588dec ["CALL", null, ["callee:00c580d0:8"]]
- 00588dac bytes 953c1b94
+ 00588dec bytes b93c1b94
- 00588dc0 ["INT_ADD", "register:40f0:8", ["const:588dc0:8", "const:4:8"]]
- 00588dc0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00588e00 ["INT_ADD", "register:40f0:8", ["const:588e00:8", "const:4:8"]]
+ 00588e00 ["CALL", null, ["callee:00c57f80:8"]]
- 00588dc0 bytes 3c3c1b94
+ 00588e00 bytes 603c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c62b7bbc8e388fb5b5d053fbfbee81"></a>

### [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) → [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) FUN_00589734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md) [`00b41334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md) [`00b41960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41960.md) [`00b41a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41a64.md) [`00b41f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 33件 [`005891d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md) [`00b413d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md) [`00b419fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b419fc.md) [`00b41b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41b00.md) [`00b41fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md#insn-00589768) · [`0058978c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md#insn-0058978c)
- 新版 [`005897a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md#insn-005897a8) · [`005897cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md#insn-005897cc)

~~~diff
- 00589768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589768 ["INT_ADD", "register:40f0:8", ["const:589768:8", "const:4:8"]]
- 00589768 ["CALLIND", null, ["register:0:8"]]
+ 005897a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005897a8 ["INT_ADD", "register:40f0:8", ["const:5897a8:8", "const:4:8"]]
+ 005897a8 ["CALLIND", null, ["register:0:8"]]
- 00589768 bytes 00013fd6
+ 005897a8 bytes 00013fd6
- 0058978c ["INT_ADD", "register:40f0:8", ["const:58978c:8", "const:4:8"]]
- 0058978c ["CALL", null, ["callee:00c57fb0:8"]]
+ 005897cc ["INT_ADD", "register:40f0:8", ["const:5897cc:8", "const:4:8"]]
+ 005897cc ["CALL", null, ["callee:00c57fb0:8"]]
- 0058978c bytes d5391b94
+ 005897cc bytes f9391b94
~~~


<a id="compare-03f54e15133fb6abec75ce340b017953"></a>

### [`00589860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589860.md) → [`005898a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898a0.md) FUN_005898a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)
- 新版 呼出元 1件 [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589860.md#insn-00589878)
- 新版 [`005898b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898a0.md#insn-005898b8)

~~~diff
- 00589878 ["INT_ADD", "register:40f0:8", ["const:589878:8", "const:4:8"]]
- 00589878 ["CALL", null, ["callee:00588f0c:8"]]
+ 005898b8 ["INT_ADD", "register:40f0:8", ["const:5898b8:8", "const:4:8"]]
+ 005898b8 ["CALL", null, ["callee:00588f0c:8"]]
- 00589878 bytes 95fdff97
+ 005898b8 bytes 95fdff97
~~~


<a id="compare-cd87740407d6df036d1b028a5aa12f6e"></a>

### [`0058988c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058988c.md) → [`005898cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898cc.md) FUN_005898cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005898a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058988c.md#insn-005898a8)
- 新版 [`005898e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898cc.md#insn-005898e8)

~~~diff
- 005898a8 ["INT_ADD", "register:40f0:8", ["const:5898a8:8", "const:4:8"]]
- 005898a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005898e8 ["INT_ADD", "register:40f0:8", ["const:5898e8:8", "const:4:8"]]
+ 005898e8 ["CALL", null, ["callee:00c57f80:8"]]
- 005898a8 bytes 82391b94
+ 005898e8 bytes a6391b94
~~~


<a id="compare-52fd675b76a96171cbb30fcb0f0caff0"></a>

### [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) → [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) FUN_00589994

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`0043b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b428.md) [`0043b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5bc.md) [`0043b6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md) [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 33件 [`0043b468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b468.md) [`0043b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b5fc.md) [`0043b714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b714.md) [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00573ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ba0.md) · 呼出先 6件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md#insn-00589998) · [`005899b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md#insn-005899b4) · [`005899bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md#insn-005899bc)
- 新版 [`005899d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md#insn-005899d8) · [`005899f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md#insn-005899f4) · [`005899fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md#insn-005899fc)

~~~diff
- 00589998 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589998 ["INT_ADD", "register:40f0:8", ["const:589998:8", "const:4:8"]]
- 00589998 ["CALLIND", null, ["register:0:8"]]
+ 005899d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005899d8 ["INT_ADD", "register:40f0:8", ["const:5899d8:8", "const:4:8"]]
+ 005899d8 ["CALLIND", null, ["register:0:8"]]
- 00589998 bytes 00013fd6
+ 005899d8 bytes 00013fd6
- 005899b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005899b4 ["INT_ADD", "register:40f0:8", ["const:5899b4:8", "const:4:8"]]
- 005899b4 ["CALLIND", null, ["register:0:8"]]
+ 005899f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005899f4 ["INT_ADD", "register:40f0:8", ["const:5899f4:8", "const:4:8"]]
+ 005899f4 ["CALLIND", null, ["register:0:8"]]
- 005899b4 bytes 00013fd6
+ 005899f4 bytes 00013fd6
- 005899bc ["INT_ADD", "register:40f0:8", ["const:5899bc:8", "const:4:8"]]
- 005899bc ["CALL", null, ["callee:00c580b0:8"]]
+ 005899fc ["INT_ADD", "register:40f0:8", ["const:5899fc:8", "const:4:8"]]
+ 005899fc ["CALL", null, ["callee:00c580b0:8"]]
- 005899bc bytes 89391b94
+ 005899fc bytes ad391b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0677f558fb74b504609d945caa9bf28"></a>

### [`0058a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a6a4.md) → [`0058a6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a6e4.md) FUN_0058a6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a6a4.md#insn-0058a6dc) · [`0058a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a6a4.md#insn-0058a6fc)
- 新版 [`0058a71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a6e4.md#insn-0058a71c) · [`0058a73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a6e4.md#insn-0058a73c)

~~~diff
- 0058a6dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a6dc ["INT_ADD", "register:40f0:8", ["const:58a6dc:8", "const:4:8"]]
- 0058a6dc ["CALLIND", null, ["register:0:8"]]
+ 0058a71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a71c ["INT_ADD", "register:40f0:8", ["const:58a71c:8", "const:4:8"]]
+ 0058a71c ["CALLIND", null, ["register:0:8"]]
- 0058a6dc bytes 00013fd6
+ 0058a71c bytes 00013fd6
- 0058a6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a6fc ["INT_ADD", "register:40f0:8", ["const:58a6fc:8", "const:4:8"]]
- 0058a6fc ["CALLIND", null, ["register:0:8"]]
+ 0058a73c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a73c ["INT_ADD", "register:40f0:8", ["const:58a73c:8", "const:4:8"]]
+ 0058a73c ["CALLIND", null, ["register:0:8"]]
- 0058a6fc bytes 00013fd6
+ 0058a73c bytes 00013fd6
~~~


<a id="compare-de9d59af54d2df4e1017aa567036b261"></a>

### [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) → [`0058a760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md) FUN_0058a760

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 1件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md)
- 新版 呼出元 3件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) · 呼出先 1件 [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md#insn-0058a748) · [`0058a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md#insn-0058a75c) · [`0058a774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md#insn-0058a774)
- 新版 [`0058a788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md#insn-0058a788) · [`0058a79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md#insn-0058a79c) · [`0058a7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md#insn-0058a7b4)

~~~diff
- 0058a748 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058a748 ["INT_ADD", "register:40f0:8", ["const:58a748:8", "const:4:8"]]
- 0058a748 ["CALLIND", null, ["register:0:8"]]
+ 0058a788 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058a788 ["INT_ADD", "register:40f0:8", ["const:58a788:8", "const:4:8"]]
+ 0058a788 ["CALLIND", null, ["register:0:8"]]
- 0058a748 bytes 20013fd6
+ 0058a788 bytes 20013fd6
- 0058a75c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a75c ["INT_ADD", "register:40f0:8", ["const:58a75c:8", "const:4:8"]]
- 0058a75c ["CALLIND", null, ["register:0:8"]]
+ 0058a79c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a79c ["INT_ADD", "register:40f0:8", ["const:58a79c:8", "const:4:8"]]
+ 0058a79c ["CALLIND", null, ["register:0:8"]]
- 0058a75c bytes 00013fd6
+ 0058a79c bytes 00013fd6
- 0058a774 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a774 ["INT_ADD", "register:40f0:8", ["const:58a774:8", "const:4:8"]]
- 0058a774 ["CALLIND", null, ["register:0:8"]]
+ 0058a7b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a7b4 ["INT_ADD", "register:40f0:8", ["const:58a7b4:8", "const:4:8"]]
+ 0058a7b4 ["CALLIND", null, ["register:0:8"]]
- 0058a774 bytes 00013fd6
+ 0058a7b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a78844392b1b7b700dd175b8b32137"></a>

### [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) → [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) FUN_0058a98c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) [`0058a824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md) [`0058a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md) · 呼出先 2件 [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 8件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`00589834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md) [`0058a2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md) [`0058a864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md) [`0058a8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md) · 呼出先 2件 [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md#insn-0058a968) · [`0058a974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md#insn-0058a974) · [`0058a984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md#insn-0058a984)
- 新版 [`0058a9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md#insn-0058a9a8) · [`0058a9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md#insn-0058a9b4) · [`0058a9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md#insn-0058a9c4)

~~~diff
- 0058a968 ["INT_ADD", "register:40f0:8", ["const:58a968:8", "const:4:8"]]
- 0058a968 ["CALL", null, ["local:b0:8"]]
+ 0058a9a8 ["INT_ADD", "register:40f0:8", ["const:58a9a8:8", "const:4:8"]]
+ 0058a9a8 ["CALL", null, ["local:b0:8"]]
- 0058a968 bytes f9ffff97
+ 0058a9a8 bytes f9ffff97
- 0058a974 ["INT_ADD", "register:40f0:8", ["const:58a974:8", "const:4:8"]]
- 0058a974 ["CALL", null, ["local:b0:8"]]
+ 0058a9b4 ["INT_ADD", "register:40f0:8", ["const:58a9b4:8", "const:4:8"]]
+ 0058a9b4 ["CALL", null, ["local:b0:8"]]
- 0058a974 bytes f6ffff97
+ 0058a9b4 bytes f6ffff97
- 0058a984 ["INT_ADD", "register:40f0:8", ["const:58a984:8", "const:4:8"]]
- 0058a984 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058a9c4 ["INT_ADD", "register:40f0:8", ["const:58a9c4:8", "const:4:8"]]
+ 0058a9c4 ["CALL", null, ["callee:00c57f80:8"]]
- 0058a984 bytes 4b351b94
+ 0058a9c4 bytes 6f351b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f97ffa2c4df9c642ae98d7060939dc"></a>

### [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) → [`0058a9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md) FUN_0058a9ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`0058ab14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md#insn-0058aa10) · [`0058aa40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md#insn-0058aa40) · [`0058aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md#insn-0058aaa4)
- 新版 [`0058aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md#insn-0058aa50) · [`0058aa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md#insn-0058aa80) · [`0058aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md#insn-0058aae4)

~~~diff
- 0058aa10 ["INT_ADD", "register:40f0:8", ["const:58aa10:8", "const:4:8"]]
- 0058aa10 ["CALL", null, ["callee:00c58120:8"]]
+ 0058aa50 ["INT_ADD", "register:40f0:8", ["const:58aa50:8", "const:4:8"]]
+ 0058aa50 ["CALL", null, ["callee:00c58120:8"]]
- 0058aa10 bytes 90351b94
+ 0058aa50 bytes b4351b94
- 0058aa40 ["INT_ADD", "register:40f0:8", ["const:58aa40:8", "const:4:8"]]
- 0058aa40 ["CALL", null, ["callee:00c58120:8"]]
+ 0058aa80 ["INT_ADD", "register:40f0:8", ["const:58aa80:8", "const:4:8"]]
+ 0058aa80 ["CALL", null, ["callee:00c58120:8"]]
- 0058aa40 bytes 84351b94
+ 0058aa80 bytes a8351b94
- 0058aaa4 ["INT_ADD", "register:40f0:8", ["const:58aaa4:8", "const:4:8"]]
- 0058aaa4 ["CALL", null, ["callee:00c58120:8"]]
+ 0058aae4 ["INT_ADD", "register:40f0:8", ["const:58aae4:8", "const:4:8"]]
+ 0058aae4 ["CALL", null, ["callee:00c58120:8"]]
- 0058aaa4 bytes 6b351b94
+ 0058aae4 bytes 8f351b94
~~~


<a id="compare-55a98f67c2ee75e9d66c1508558c1670"></a>

### [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) → [`0058ab14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md) FUN_0058ab14

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0058a9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ab1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md#insn-0058ab1c) · [`0058ab2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md#insn-0058ab2c) · [`0058ab4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md#insn-0058ab4c)
- 新版 [`0058ab5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md#insn-0058ab5c) · [`0058ab6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md#insn-0058ab6c) · [`0058ab8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md#insn-0058ab8c)

~~~diff
- 0058ab1c ["INT_ADD", "register:40f0:8", ["const:58ab1c:8", "const:4:8"]]
- 0058ab1c ["CALL", null, ["callee:0058a9ec:8"]]
+ 0058ab5c ["INT_ADD", "register:40f0:8", ["const:58ab5c:8", "const:4:8"]]
+ 0058ab5c ["CALL", null, ["callee:0058a9ec:8"]]
- 0058ab1c bytes a4ffff97
+ 0058ab5c bytes a4ffff97
- 0058ab2c ["INT_ADD", "register:40f0:8", ["const:58ab2c:8", "const:4:8"]]
- 0058ab2c ["CALL", null, ["callee:0058a9ec:8"]]
+ 0058ab6c ["INT_ADD", "register:40f0:8", ["const:58ab6c:8", "const:4:8"]]
+ 0058ab6c ["CALL", null, ["callee:0058a9ec:8"]]
- 0058ab2c bytes a0ffff97
+ 0058ab6c bytes a0ffff97
- 0058ab4c ["INT_ADD", "register:40f0:8", ["const:58ab4c:8", "const:4:8"]]
- 0058ab4c ["CALL", null, ["callee:00c57f60:8"]]
+ 0058ab8c ["INT_ADD", "register:40f0:8", ["const:58ab8c:8", "const:4:8"]]
+ 0058ab8c ["CALL", null, ["callee:00c57f60:8"]]
- 0058ab4c bytes d1341b94
+ 0058ab8c bytes f5341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d721557c4732a9a270c21d1521fb1fb"></a>

### [`0058acd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058acd0.md) → [`0058ad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ad10.md) FUN_0058ad10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ad2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058acd0.md#insn-0058ad2c) · [`0058ad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058acd0.md#insn-0058ad4c) · [`0058ad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058acd0.md#insn-0058ad68)
- 新版 [`0058ad6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ad10.md#insn-0058ad6c) · [`0058ad8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ad10.md#insn-0058ad8c) · [`0058ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ad10.md#insn-0058ada8)

~~~diff
- 0058ad2c ["INT_ADD", "register:40f0:8", ["const:58ad2c:8", "const:4:8"]]
- 0058ad2c ["CALL", null, ["callee:00c57f60:8"]]
+ 0058ad6c ["INT_ADD", "register:40f0:8", ["const:58ad6c:8", "const:4:8"]]
+ 0058ad6c ["CALL", null, ["callee:00c57f60:8"]]
- 0058ad2c bytes 59341b94
+ 0058ad6c bytes 7d341b94
- 0058ad4c ["INT_ADD", "register:40f0:8", ["const:58ad4c:8", "const:4:8"]]
- 0058ad4c ["CALL", null, ["callee:00c58010:8"]]
+ 0058ad8c ["INT_ADD", "register:40f0:8", ["const:58ad8c:8", "const:4:8"]]
+ 0058ad8c ["CALL", null, ["callee:00c58010:8"]]
- 0058ad4c bytes 7d341b94
+ 0058ad8c bytes a1341b94
- 0058ad68 ["INT_ADD", "register:40f0:8", ["const:58ad68:8", "const:4:8"]]
- 0058ad68 ["CALL", null, ["callee:0043b7a4:8"]]
+ 0058ada8 ["INT_ADD", "register:40f0:8", ["const:58ada8:8", "const:4:8"]]
+ 0058ada8 ["CALL", null, ["callee:0043b7a4:8"]]
- 0058ad68 bytes 7fc2fa97
+ 0058ada8 bytes 7fc2fa97
~~~


<a id="compare-776754fbf5261a7e5791bc04fd9a79a2"></a>

### [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) → [`0058adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md) FUN_0058adac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00584d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md) · 呼出先 2件 [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00584ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584ddc.md) · 呼出先 2件 [`0058b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ad98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md#insn-0058ad98) · [`0058adc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md#insn-0058adc4)
- 新版 [`0058add8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md#insn-0058add8) · [`0058ae04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md#insn-0058ae04)

~~~diff
- 0058ad98 ["INT_ADD", "register:40f0:8", ["const:58ad98:8", "const:4:8"]]
- 0058ad98 ["CALL", null, ["callee:0058b654:8"]]
+ 0058add8 ["INT_ADD", "register:40f0:8", ["const:58add8:8", "const:4:8"]]
+ 0058add8 ["CALL", null, ["callee:0058b654:8"]]
- 0058ad98 bytes 1f020094
+ 0058add8 bytes 1f020094
- 0058adc4 ["INT_ADD", "register:40f0:8", ["const:58adc4:8", "const:4:8"]]
- 0058adc4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0058ae04 ["INT_ADD", "register:40f0:8", ["const:58ae04:8", "const:4:8"]]
+ 0058ae04 ["CALL", null, ["callee:00c57fb0:8"]]
- 0058adc4 bytes 47341b94
+ 0058ae04 bytes 6b341b94
~~~


<a id="compare-00df8ed875caf6b76892f519cf5af8c2"></a>

### [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) → [`0058ae08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md) FUN_0058ae08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`0087d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`0087d3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md#insn-0058ae18) · [`0058aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md#insn-0058aeac) · [`0058aec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md#insn-0058aec4)
- 新版 [`0058ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md#insn-0058ae58) · [`0058aeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md#insn-0058aeec) · [`0058af04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md#insn-0058af04)

~~~diff
- 0058ae18 ["INT_ADD", "register:40f0:8", ["const:58ae18:8", "const:4:8"]]
- 0058ae18 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058ae58 ["INT_ADD", "register:40f0:8", ["const:58ae58:8", "const:4:8"]]
+ 0058ae58 ["CALL", null, ["callee:00c57f60:8"]]
- 0058ae18 bytes 1e341b94
+ 0058ae58 bytes 42341b94
- 0058aeac ["INT_ADD", "register:40f0:8", ["const:58aeac:8", "const:4:8"]]
- 0058aeac ["CALL", null, ["callee:0058b654:8"]]
+ 0058aeec ["INT_ADD", "register:40f0:8", ["const:58aeec:8", "const:4:8"]]
+ 0058aeec ["CALL", null, ["callee:0058b654:8"]]
- 0058aeac bytes da010094
+ 0058aeec bytes da010094
- 0058aec4 ["INT_ADD", "register:40f0:8", ["const:58aec4:8", "const:4:8"]]
- 0058aec4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058af04 ["INT_ADD", "register:40f0:8", ["const:58af04:8", "const:4:8"]]
+ 0058af04 ["CALL", null, ["callee:00c57f80:8"]]
- 0058aec4 bytes fb331b94
+ 0058af04 bytes 1f341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-552e1eaad279cb583b9a4df6e4a02196"></a>

### [`0058af3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md) → [`0058af7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md) FUN_0058af7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058af80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md#insn-0058af80) · [`0058af98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md#insn-0058af98) · [`0058afac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md#insn-0058afac)
- 新版 [`0058afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md#insn-0058afc0) · [`0058afd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md#insn-0058afd8) · [`0058afec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md#insn-0058afec)

~~~diff
- 0058af80 ["INT_ADD", "register:40f0:8", ["const:58af80:8", "const:4:8"]]
- 0058af80 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058afc0 ["INT_ADD", "register:40f0:8", ["const:58afc0:8", "const:4:8"]]
+ 0058afc0 ["CALL", null, ["callee:00c57f60:8"]]
- 0058af80 bytes c4331b94
+ 0058afc0 bytes e8331b94
- 0058af98 ["INT_ADD", "register:40f0:8", ["const:58af98:8", "const:4:8"]]
- 0058af98 ["CALL", null, ["callee:00c580d0:8"]]
+ 0058afd8 ["INT_ADD", "register:40f0:8", ["const:58afd8:8", "const:4:8"]]
+ 0058afd8 ["CALL", null, ["callee:00c580d0:8"]]
- 0058af98 bytes 1a341b94
+ 0058afd8 bytes 3e341b94
- 0058afac ["INT_ADD", "register:40f0:8", ["const:58afac:8", "const:4:8"]]
- 0058afac ["CALL", null, ["callee:0058b654:8"]]
+ 0058afec ["INT_ADD", "register:40f0:8", ["const:58afec:8", "const:4:8"]]
+ 0058afec ["CALL", null, ["callee:0058b654:8"]]
- 0058afac bytes 9a010094
+ 0058afec bytes 9a010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c40a50cf103601eb99d955e3f1a61f2"></a>

### [`0058b054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b054.md) → [`0058b094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b094.md) FUN_0058b094

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b054.md#insn-0058b0b0) · [`0058b0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b054.md#insn-0058b0d0) · [`0058b0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b054.md#insn-0058b0ec)
- 新版 [`0058b0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b094.md#insn-0058b0f0) · [`0058b110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b094.md#insn-0058b110) · [`0058b12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b094.md#insn-0058b12c)

~~~diff
- 0058b0b0 ["INT_ADD", "register:40f0:8", ["const:58b0b0:8", "const:4:8"]]
- 0058b0b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058b0f0 ["INT_ADD", "register:40f0:8", ["const:58b0f0:8", "const:4:8"]]
+ 0058b0f0 ["CALL", null, ["callee:00c57f60:8"]]
- 0058b0b0 bytes 78331b94
+ 0058b0f0 bytes 9c331b94
- 0058b0d0 ["INT_ADD", "register:40f0:8", ["const:58b0d0:8", "const:4:8"]]
- 0058b0d0 ["CALL", null, ["callee:00c58010:8"]]
+ 0058b110 ["INT_ADD", "register:40f0:8", ["const:58b110:8", "const:4:8"]]
+ 0058b110 ["CALL", null, ["callee:00c58010:8"]]
- 0058b0d0 bytes 9c331b94
+ 0058b110 bytes c0331b94
- 0058b0ec ["INT_ADD", "register:40f0:8", ["const:58b0ec:8", "const:4:8"]]
- 0058b0ec ["CALL", null, ["callee:0043b7a4:8"]]
+ 0058b12c ["INT_ADD", "register:40f0:8", ["const:58b12c:8", "const:4:8"]]
+ 0058b12c ["CALL", null, ["callee:0043b7a4:8"]]
- 0058b0ec bytes 9ec1fa97
+ 0058b12c bytes 9ec1fa97
~~~


<a id="compare-091a095692e5dc9e4f1b3f0d62b65f5f"></a>

### [`0058b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md) → [`0058b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b170.md) FUN_0058b170

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md#insn-0058b15c) · [`0058b174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md#insn-0058b174) · [`0058b18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md#insn-0058b18c)
- 新版 [`0058b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b170.md#insn-0058b19c) · [`0058b1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b170.md#insn-0058b1b4) · [`0058b1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b170.md#insn-0058b1cc)

~~~diff
- 0058b15c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b15c ["INT_ADD", "register:40f0:8", ["const:58b15c:8", "const:4:8"]]
- 0058b15c ["CALLIND", null, ["register:0:8"]]
+ 0058b19c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b19c ["INT_ADD", "register:40f0:8", ["const:58b19c:8", "const:4:8"]]
+ 0058b19c ["CALLIND", null, ["register:0:8"]]
- 0058b15c bytes 20013fd6
+ 0058b19c bytes 20013fd6
- 0058b174 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b174 ["INT_ADD", "register:40f0:8", ["const:58b174:8", "const:4:8"]]
- 0058b174 ["CALLIND", null, ["register:0:8"]]
+ 0058b1b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b1b4 ["INT_ADD", "register:40f0:8", ["const:58b1b4:8", "const:4:8"]]
+ 0058b1b4 ["CALLIND", null, ["register:0:8"]]
- 0058b174 bytes 20013fd6
+ 0058b1b4 bytes 20013fd6
- 0058b18c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b18c ["INT_ADD", "register:40f0:8", ["const:58b18c:8", "const:4:8"]]
- 0058b18c ["CALLIND", null, ["register:0:8"]]
+ 0058b1cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b1cc ["INT_ADD", "register:40f0:8", ["const:58b1cc:8", "const:4:8"]]
+ 0058b1cc ["CALLIND", null, ["register:0:8"]]
- 0058b18c bytes 20013fd6
+ 0058b1cc bytes 20013fd6
~~~


<a id="compare-461fa6308747f0096754e5f3941ea1a1"></a>

### [`0058b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md) → [`0058b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md) FUN_0058b210

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) · 呼出先 3件 [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) · 呼出先 3件 [`0058b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md#insn-0058b204) · [`0058b21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md#insn-0058b21c) · [`0058b270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md#insn-0058b270)
- 新版 [`0058b244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md#insn-0058b244) · [`0058b25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md#insn-0058b25c) · [`0058b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md#insn-0058b2b0)

~~~diff
- 0058b204 ["INT_ADD", "register:40f0:8", ["const:58b204:8", "const:4:8"]]
- 0058b204 ["CALL", null, ["callee:0058b834:8"]]
+ 0058b244 ["INT_ADD", "register:40f0:8", ["const:58b244:8", "const:4:8"]]
+ 0058b244 ["CALL", null, ["callee:0058b834:8"]]
- 0058b204 bytes 7c010094
+ 0058b244 bytes 7c010094
- 0058b21c ["INT_ADD", "register:40f0:8", ["const:58b21c:8", "const:4:8"]]
- 0058b21c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058b25c ["INT_ADD", "register:40f0:8", ["const:58b25c:8", "const:4:8"]]
+ 0058b25c ["CALL", null, ["callee:00c57f80:8"]]
- 0058b21c bytes 25331b94
+ 0058b25c bytes 49331b94
- 0058b270 ["INT_ADD", "register:40f0:8", ["const:58b270:8", "const:4:8"]]
- 0058b270 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0058b2b0 ["INT_ADD", "register:40f0:8", ["const:58b2b0:8", "const:4:8"]]
+ 0058b2b0 ["CALL", null, ["callee:00c57fb0:8"]]
- 0058b270 bytes 1c331b94
+ 0058b2b0 bytes 40331b94
~~~


<a id="compare-098ba9fb5c479a992ed16959001a6940"></a>

### [`0058b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md) → [`0058b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md) FUN_0058b2b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00597614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597614.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00597654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597654.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md#insn-0058b2c4) · [`0058b358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md#insn-0058b358) · [`0058b370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md#insn-0058b370)
- 新版 [`0058b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md#insn-0058b304) · [`0058b398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md#insn-0058b398) · [`0058b3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md#insn-0058b3b0)

~~~diff
- 0058b2c4 ["INT_ADD", "register:40f0:8", ["const:58b2c4:8", "const:4:8"]]
- 0058b2c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058b304 ["INT_ADD", "register:40f0:8", ["const:58b304:8", "const:4:8"]]
+ 0058b304 ["CALL", null, ["callee:00c57f60:8"]]
- 0058b2c4 bytes f3321b94
+ 0058b304 bytes 17331b94
- 0058b358 ["INT_ADD", "register:40f0:8", ["const:58b358:8", "const:4:8"]]
- 0058b358 ["CALL", null, ["callee:0058b834:8"]]
+ 0058b398 ["INT_ADD", "register:40f0:8", ["const:58b398:8", "const:4:8"]]
+ 0058b398 ["CALL", null, ["callee:0058b834:8"]]
- 0058b358 bytes 27010094
+ 0058b398 bytes 27010094
- 0058b370 ["INT_ADD", "register:40f0:8", ["const:58b370:8", "const:4:8"]]
- 0058b370 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058b3b0 ["INT_ADD", "register:40f0:8", ["const:58b3b0:8", "const:4:8"]]
+ 0058b3b0 ["CALL", null, ["callee:00c57f80:8"]]
- 0058b370 bytes d0321b94
+ 0058b3b0 bytes f4321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b80483007c1b965024fb3d965380ada9"></a>

### [`0058b3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md) → [`0058b428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md) FUN_0058b428

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00597658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597658.md) · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md#insn-0058b424) · [`0058b43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md#insn-0058b43c) · [`0058b454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md#insn-0058b454)
- 新版 [`0058b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md#insn-0058b464) · [`0058b47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md#insn-0058b47c) · [`0058b494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md#insn-0058b494)

~~~diff
- 0058b424 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058b424 ["INT_ADD", "register:40f0:8", ["const:58b424:8", "const:4:8"]]
- 0058b424 ["CALLIND", null, ["register:0:8"]]
+ 0058b464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058b464 ["INT_ADD", "register:40f0:8", ["const:58b464:8", "const:4:8"]]
+ 0058b464 ["CALLIND", null, ["register:0:8"]]
- 0058b424 bytes 00013fd6
+ 0058b464 bytes 00013fd6
- 0058b43c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b43c ["INT_ADD", "register:40f0:8", ["const:58b43c:8", "const:4:8"]]
- 0058b43c ["CALLIND", null, ["register:0:8"]]
+ 0058b47c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b47c ["INT_ADD", "register:40f0:8", ["const:58b47c:8", "const:4:8"]]
+ 0058b47c ["CALLIND", null, ["register:0:8"]]
- 0058b43c bytes 20013fd6
+ 0058b47c bytes 20013fd6
- 0058b454 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b454 ["INT_ADD", "register:40f0:8", ["const:58b454:8", "const:4:8"]]
- 0058b454 ["CALLIND", null, ["register:0:8"]]
+ 0058b494 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b494 ["INT_ADD", "register:40f0:8", ["const:58b494:8", "const:4:8"]]
+ 0058b494 ["CALLIND", null, ["register:0:8"]]
- 0058b454 bytes 20013fd6
+ 0058b494 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3c0c7846c802074640b624ab4b7107"></a>

### [`0058b6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b6ec.md) → [`0058b72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b72c.md) FUN_0058b72c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b0f8.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0058b138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b138.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b6ec.md#insn-0058b780) · [`0058b7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b6ec.md#insn-0058b7a8) · [`0058b7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b6ec.md#insn-0058b7bc)
- 新版 [`0058b7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b72c.md#insn-0058b7c0) · [`0058b7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b72c.md#insn-0058b7e8) · [`0058b7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b72c.md#insn-0058b7fc)

~~~diff
- 0058b780 ["INT_ADD", "register:40f0:8", ["const:58b780:8", "const:4:8"]]
- 0058b780 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058b7c0 ["INT_ADD", "register:40f0:8", ["const:58b7c0:8", "const:4:8"]]
+ 0058b7c0 ["CALL", null, ["callee:00c57f60:8"]]
- 0058b780 bytes c4311b94
+ 0058b7c0 bytes e8311b94
- 0058b7a8 ["INT_ADD", "register:40f0:8", ["const:58b7a8:8", "const:4:8"]]
- 0058b7a8 ["CALL", null, ["callee:00c580d0:8"]]
+ 0058b7e8 ["INT_ADD", "register:40f0:8", ["const:58b7e8:8", "const:4:8"]]
+ 0058b7e8 ["CALL", null, ["callee:00c580d0:8"]]
- 0058b7a8 bytes 16321b94
+ 0058b7e8 bytes 3a321b94
- 0058b7bc ["INT_ADD", "register:40f0:8", ["const:58b7bc:8", "const:4:8"]]
- 0058b7bc ["CALL", null, ["callee:00c57f80:8"]]
+ 0058b7fc ["INT_ADD", "register:40f0:8", ["const:58b7fc:8", "const:4:8"]]
+ 0058b7fc ["CALL", null, ["callee:00c57f80:8"]]
- 0058b7bc bytes bd311b94
+ 0058b7fc bytes e1311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d03bb221efe1fbb68bebeb39e82def"></a>

### [`0058eb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eb44.md) → [`0058eb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eb84.md) FUN_0058eb84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058eb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eb44.md#insn-0058eb6c) · [`0058eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eb44.md#insn-0058eb74) · [`0058ebc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eb44.md#insn-0058ebc0)
- 新版 [`0058ebac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eb84.md#insn-0058ebac) · [`0058ebb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eb84.md#insn-0058ebb4) · [`0058ec00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eb84.md#insn-0058ec00)

~~~diff
- 0058eb6c ["INT_ADD", "register:40f0:8", ["const:58eb6c:8", "const:4:8"]]
- 0058eb6c ["CALL", null, ["callee:00589880:8"]]
+ 0058ebac ["INT_ADD", "register:40f0:8", ["const:58ebac:8", "const:4:8"]]
+ 0058ebac ["CALL", null, ["callee:00589880:8"]]
- 0058eb6c bytes 35ebff97
+ 0058ebac bytes 35ebff97
- 0058eb74 ["INT_ADD", "register:40f0:8", ["const:58eb74:8", "const:4:8"]]
- 0058eb74 ["CALL", null, ["callee:00588eac:8"]]
+ 0058ebb4 ["INT_ADD", "register:40f0:8", ["const:58ebb4:8", "const:4:8"]]
+ 0058ebb4 ["CALL", null, ["callee:00588eac:8"]]
- 0058eb74 bytes bee8ff97
+ 0058ebb4 bytes bee8ff97
- 0058ebc0 ["INT_ADD", "register:40f0:8", ["const:58ebc0:8", "const:4:8"]]
- 0058ebc0 ["CALL", null, ["callee:00589360:8"]]
+ 0058ec00 ["INT_ADD", "register:40f0:8", ["const:58ec00:8", "const:4:8"]]
+ 0058ec00 ["CALL", null, ["callee:00589360:8"]]
- 0058ebc0 bytes d8e9ff97
+ 0058ec00 bytes d8e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6d1fafec951093d37a4a30afb260e2"></a>

### [`0058ed34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ed34.md) → [`0058ed74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed74.md) FUN_0058ed74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec0.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f00.md) · 呼出先 8件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ed54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ed34.md#insn-0058ed54) · [`0058ed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ed34.md#insn-0058ed5c) · [`0058eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ed34.md#insn-0058eda0)
- 新版 [`0058ed94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed74.md#insn-0058ed94) · [`0058ed9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed74.md#insn-0058ed9c) · [`0058ede0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed74.md#insn-0058ede0)

~~~diff
- 0058ed54 ["INT_ADD", "register:40f0:8", ["const:58ed54:8", "const:4:8"]]
- 0058ed54 ["CALL", null, ["callee:00588eac:8"]]
+ 0058ed94 ["INT_ADD", "register:40f0:8", ["const:58ed94:8", "const:4:8"]]
+ 0058ed94 ["CALL", null, ["callee:00588eac:8"]]
- 0058ed54 bytes 46e8ff97
+ 0058ed94 bytes 46e8ff97
- 0058ed5c ["INT_ADD", "register:40f0:8", ["const:58ed5c:8", "const:4:8"]]
- 0058ed5c ["CALL", null, ["callee:0058919c:8"]]
+ 0058ed9c ["INT_ADD", "register:40f0:8", ["const:58ed9c:8", "const:4:8"]]
+ 0058ed9c ["CALL", null, ["callee:0058919c:8"]]
- 0058ed5c bytes 00e9ff97
+ 0058ed9c bytes 00e9ff97
- 0058eda0 ["INT_ADD", "register:40f0:8", ["const:58eda0:8", "const:4:8"]]
- 0058eda0 ["CALL", null, ["callee:00589360:8"]]
+ 0058ede0 ["INT_ADD", "register:40f0:8", ["const:58ede0:8", "const:4:8"]]
+ 0058ede0 ["CALL", null, ["callee:00589360:8"]]
- 0058eda0 bytes 60e9ff97
+ 0058ede0 bytes 60e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a155c8bd2c4688b6a7c1a771b3ef3a55"></a>

### [`0058f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f310.md) → [`0058f350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f350.md) FUN_0058f350

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0058c5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f310.md#insn-0058f37c) · [`0058f3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f310.md#insn-0058f3d8) · [`0058f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f310.md#insn-0058f404)
- 新版 [`0058f3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f350.md#insn-0058f3bc) · [`0058f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f350.md#insn-0058f418) · [`0058f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f350.md#insn-0058f444)

~~~diff
- 0058f37c ["INT_ADD", "register:40f0:8", ["const:58f37c:8", "const:4:8"]]
- 0058f37c ["CALL", null, ["callee:00c57f60:8"]]
+ 0058f3bc ["INT_ADD", "register:40f0:8", ["const:58f3bc:8", "const:4:8"]]
+ 0058f3bc ["CALL", null, ["callee:00c57f60:8"]]
- 0058f37c bytes c5221b94
+ 0058f3bc bytes e9221b94
- 0058f3d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058f3d8 ["INT_ADD", "register:40f0:8", ["const:58f3d8:8", "const:4:8"]]
- 0058f3d8 ["CALLIND", null, ["register:0:8"]]
+ 0058f418 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058f418 ["INT_ADD", "register:40f0:8", ["const:58f418:8", "const:4:8"]]
+ 0058f418 ["CALLIND", null, ["register:0:8"]]
- 0058f3d8 bytes 20013fd6
+ 0058f418 bytes 20013fd6
- 0058f404 ["INT_ADD", "register:40f0:8", ["const:58f404:8", "const:4:8"]]
- 0058f404 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0058f444 ["INT_ADD", "register:40f0:8", ["const:58f444:8", "const:4:8"]]
+ 0058f444 ["CALL", null, ["callee:0043bbe4:8"]]
- 0058f404 bytes e8b1fa97
+ 0058f444 bytes e8b1fa97
~~~


<a id="compare-038a7f61e1045ba84bc8966d95f90c64"></a>

### [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) → [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) FUN_0058f474

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0058ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md) [`0058cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md) [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md) [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md) [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 7件 [`0058ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md) [`0058cf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md) [`005ad3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad3f8.md) [`00888480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md) [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md#insn-0058f4a0) · [`0058f4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md#insn-0058f4b0) · [`0058f4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md#insn-0058f4d0)
- 新版 [`0058f4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md#insn-0058f4e0) · [`0058f4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md#insn-0058f4f0) · [`0058f510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md#insn-0058f510)

~~~diff
- 0058f4a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f4a0 ["INT_ADD", "register:40f0:8", ["const:58f4a0:8", "const:4:8"]]
- 0058f4a0 ["CALLIND", null, ["register:0:8"]]
+ 0058f4e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f4e0 ["INT_ADD", "register:40f0:8", ["const:58f4e0:8", "const:4:8"]]
+ 0058f4e0 ["CALLIND", null, ["register:0:8"]]
- 0058f4a0 bytes 00013fd6
+ 0058f4e0 bytes 00013fd6
- 0058f4b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f4b0 ["INT_ADD", "register:40f0:8", ["const:58f4b0:8", "const:4:8"]]
- 0058f4b0 ["CALLIND", null, ["register:0:8"]]
+ 0058f4f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f4f0 ["INT_ADD", "register:40f0:8", ["const:58f4f0:8", "const:4:8"]]
+ 0058f4f0 ["CALLIND", null, ["register:0:8"]]
- 0058f4b0 bytes 00013fd6
+ 0058f4f0 bytes 00013fd6
- 0058f4d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f4d0 ["INT_ADD", "register:40f0:8", ["const:58f4d0:8", "const:4:8"]]
- 0058f4d0 ["CALLIND", null, ["register:0:8"]]
+ 0058f510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f510 ["INT_ADD", "register:40f0:8", ["const:58f510:8", "const:4:8"]]
+ 0058f510 ["CALLIND", null, ["register:0:8"]]
- 0058f4d0 bytes 00013fd6
+ 0058f510 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd529e7add3571145cd5e2adebbe8390"></a>

### [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) → [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) FUN_0058f5dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0058db8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md) [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) [`00b542e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b542e8.md) [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) [`00bc5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5358.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 9件 [`0058dbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md) [`00b52a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md) [`00b54384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54384.md) [`00bc50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md) [`00bc53f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc53f4.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md#insn-0058f610) · [`0058f634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md#insn-0058f634)
- 新版 [`0058f650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md#insn-0058f650) · [`0058f674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md#insn-0058f674)

~~~diff
- 0058f610 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f610 ["INT_ADD", "register:40f0:8", ["const:58f610:8", "const:4:8"]]
- 0058f610 ["CALLIND", null, ["register:0:8"]]
+ 0058f650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f650 ["INT_ADD", "register:40f0:8", ["const:58f650:8", "const:4:8"]]
+ 0058f650 ["CALLIND", null, ["register:0:8"]]
- 0058f610 bytes 00013fd6
+ 0058f650 bytes 00013fd6
- 0058f634 ["INT_ADD", "register:40f0:8", ["const:58f634:8", "const:4:8"]]
- 0058f634 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0058f674 ["INT_ADD", "register:40f0:8", ["const:58f674:8", "const:4:8"]]
+ 0058f674 ["CALL", null, ["callee:00c57fb0:8"]]
- 0058f634 bytes 2b221b94
+ 0058f674 bytes 4f221b94
~~~


<a id="compare-e810e32481f23bedbe2adb139fc69d60"></a>

### [`0058f728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f728.md) → [`0058f768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f768.md) FUN_0058f768

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00590d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590d58.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f728.md#insn-0058f744) · [`0058f764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f728.md#insn-0058f764)
- 新版 [`0058f784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f768.md#insn-0058f784) · [`0058f7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f768.md#insn-0058f7a4)

~~~diff
- 0058f744 ["INT_ADD", "register:40f0:8", ["const:58f744:8", "const:4:8"]]
- 0058f744 ["CALL", null, ["callee:00c53da0:8"]]
+ 0058f784 ["INT_ADD", "register:40f0:8", ["const:58f784:8", "const:4:8"]]
+ 0058f784 ["CALL", null, ["callee:00c53da0:8"]]
- 0058f744 bytes 6f111b94
+ 0058f784 bytes 87111b94
- 0058f764 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f764 ["INT_ADD", "register:40f0:8", ["const:58f764:8", "const:4:8"]]
- 0058f764 ["CALLIND", null, ["register:0:8"]]
+ 0058f7a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f7a4 ["INT_ADD", "register:40f0:8", ["const:58f7a4:8", "const:4:8"]]
+ 0058f7a4 ["CALLIND", null, ["register:0:8"]]
- 0058f764 bytes 00013fd6
+ 0058f7a4 bytes 00013fd6
~~~


<a id="compare-482d41c3f421e15c317ca364fa0387e2"></a>

### [`005902e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005902e8.md) → [`00590328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590328.md) FUN_00590328

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058f778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f778.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0058f7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7b8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005902e8.md#insn-00590318) · [`00590364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005902e8.md#insn-00590364)
- 新版 [`00590358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590328.md#insn-00590358) · [`005903a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590328.md#insn-005903a4)

~~~diff
- 00590318 ["INT_ADD", "register:40f0:8", ["const:590318:8", "const:4:8"]]
- 00590318 ["CALL", null, ["callee:00c57f80:8"]]
+ 00590358 ["INT_ADD", "register:40f0:8", ["const:590358:8", "const:4:8"]]
+ 00590358 ["CALL", null, ["callee:00c57f80:8"]]
- 00590318 bytes e61e1b94
+ 00590358 bytes 0a1f1b94
- 00590364 ["INT_ADD", "register:40f0:8", ["const:590364:8", "const:4:8"]]
- 00590364 ["CALL", null, ["callee:00c57f80:8"]]
+ 005903a4 ["INT_ADD", "register:40f0:8", ["const:5903a4:8", "const:4:8"]]
+ 005903a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00590364 bytes d31e1b94
+ 005903a4 bytes f71e1b94
~~~


<a id="compare-d36b5b11dcc37ea87646dfcda2895cde"></a>

### [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) → [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md) FUN_005903f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00590878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md) [`00590a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md) [`00590b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005908b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005908b8.md) [`00590a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590a40.md) [`00590bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590bcc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md#insn-00590450) · [`00590494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md#insn-00590494) · [`005904a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md#insn-005904a4)
- 新版 [`00590490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md#insn-00590490) · [`005904d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md#insn-005904d4) · [`005904e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md#insn-005904e4)

~~~diff
- 00590450 ["INT_ADD", "register:40f0:8", ["const:590450:8", "const:4:8"]]
- 00590450 ["CALL", null, ["callee:00c58010:8"]]
+ 00590490 ["INT_ADD", "register:40f0:8", ["const:590490:8", "const:4:8"]]
+ 00590490 ["CALL", null, ["callee:00c58010:8"]]
- 00590450 bytes bc1e1b94
+ 00590490 bytes e01e1b94
- 00590494 ["INT_ADD", "register:40f0:8", ["const:590494:8", "const:4:8"]]
- 00590494 ["CALL", null, ["callee:00c57f60:8"]]
+ 005904d4 ["INT_ADD", "register:40f0:8", ["const:5904d4:8", "const:4:8"]]
+ 005904d4 ["CALL", null, ["callee:00c57f60:8"]]
- 00590494 bytes 7f1e1b94
+ 005904d4 bytes a31e1b94
- 005904a4 ["INT_ADD", "register:40f0:8", ["const:5904a4:8", "const:4:8"]]
- 005904a4 ["CALL", null, ["callee:005908b8:8"]]
+ 005904e4 ["INT_ADD", "register:40f0:8", ["const:5904e4:8", "const:4:8"]]
+ 005904e4 ["CALL", null, ["callee:005908b8:8"]]
- 005904a4 bytes f5000094
+ 005904e4 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82bf9e62461c8e5f49c12289a16e4a82"></a>

### [`00590878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md) → [`005908b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005908b8.md) FUN_005908b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005908e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md#insn-005908e0) · [`00590918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md#insn-00590918) · [`005909c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md#insn-005909c8)
- 新版 [`00590920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005908b8.md#insn-00590920) · [`00590958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005908b8.md#insn-00590958) · [`00590a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005908b8.md#insn-00590a08)

~~~diff
- 005908e0 ["INT_ADD", "register:40f0:8", ["const:5908e0:8", "const:4:8"]]
- 005908e0 ["CALL", null, ["callee:00c58010:8"]]
+ 00590920 ["INT_ADD", "register:40f0:8", ["const:590920:8", "const:4:8"]]
+ 00590920 ["CALL", null, ["callee:00c58010:8"]]
- 005908e0 bytes 981d1b94
+ 00590920 bytes bc1d1b94
- 00590918 ["INT_ADD", "register:40f0:8", ["const:590918:8", "const:4:8"]]
- 00590918 ["CALL", null, ["callee:00c57f60:8"]]
+ 00590958 ["INT_ADD", "register:40f0:8", ["const:590958:8", "const:4:8"]]
+ 00590958 ["CALL", null, ["callee:00c57f60:8"]]
- 00590918 bytes 5e1d1b94
+ 00590958 bytes 821d1b94
- 005909c8 ["INT_ADD", "register:40f0:8", ["const:5909c8:8", "const:4:8"]]
- 005909c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00590a08 ["INT_ADD", "register:40f0:8", ["const:590a08:8", "const:4:8"]]
+ 00590a08 ["CALL", null, ["callee:00c57f80:8"]]
- 005909c8 bytes 3a1d1b94
+ 00590a08 bytes 5e1d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6453a68ea4fc71a1c8293e4792d2da16"></a>

### [`00590a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md) → [`00590a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590a40.md) FUN_00590a40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md#insn-00590a70) · [`00590aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md#insn-00590aa8) · [`00590b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md#insn-00590b58)
- 新版 [`00590ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590a40.md#insn-00590ab0) · [`00590ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590a40.md#insn-00590ae8) · [`00590b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590a40.md#insn-00590b98)

~~~diff
- 00590a70 ["INT_ADD", "register:40f0:8", ["const:590a70:8", "const:4:8"]]
- 00590a70 ["CALL", null, ["callee:00c58010:8"]]
+ 00590ab0 ["INT_ADD", "register:40f0:8", ["const:590ab0:8", "const:4:8"]]
+ 00590ab0 ["CALL", null, ["callee:00c58010:8"]]
- 00590a70 bytes 341d1b94
+ 00590ab0 bytes 581d1b94
- 00590aa8 ["INT_ADD", "register:40f0:8", ["const:590aa8:8", "const:4:8"]]
- 00590aa8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00590ae8 ["INT_ADD", "register:40f0:8", ["const:590ae8:8", "const:4:8"]]
+ 00590ae8 ["CALL", null, ["callee:00c57f60:8"]]
- 00590aa8 bytes fa1c1b94
+ 00590ae8 bytes 1e1d1b94
- 00590b58 ["INT_ADD", "register:40f0:8", ["const:590b58:8", "const:4:8"]]
- 00590b58 ["CALL", null, ["callee:00c57f80:8"]]
+ 00590b98 ["INT_ADD", "register:40f0:8", ["const:590b98:8", "const:4:8"]]
+ 00590b98 ["CALL", null, ["callee:00c57f80:8"]]
- 00590b58 bytes d61c1b94
+ 00590b98 bytes fa1c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ce5d9c32ee256c91d07d4a7a987e40d"></a>

### [`00590b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md) → [`00590bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590bcc.md) FUN_00590bcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md#insn-00590bfc) · [`00590c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md#insn-00590c34) · [`00590ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md#insn-00590ce4)
- 新版 [`00590c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590bcc.md#insn-00590c3c) · [`00590c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590bcc.md#insn-00590c74) · [`00590d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590bcc.md#insn-00590d24)

~~~diff
- 00590bfc ["INT_ADD", "register:40f0:8", ["const:590bfc:8", "const:4:8"]]
- 00590bfc ["CALL", null, ["callee:00c58010:8"]]
+ 00590c3c ["INT_ADD", "register:40f0:8", ["const:590c3c:8", "const:4:8"]]
+ 00590c3c ["CALL", null, ["callee:00c58010:8"]]
- 00590bfc bytes d11c1b94
+ 00590c3c bytes f51c1b94
- 00590c34 ["INT_ADD", "register:40f0:8", ["const:590c34:8", "const:4:8"]]
- 00590c34 ["CALL", null, ["callee:00c57f60:8"]]
+ 00590c74 ["INT_ADD", "register:40f0:8", ["const:590c74:8", "const:4:8"]]
+ 00590c74 ["CALL", null, ["callee:00c57f60:8"]]
- 00590c34 bytes 971c1b94
+ 00590c74 bytes bb1c1b94
- 00590ce4 ["INT_ADD", "register:40f0:8", ["const:590ce4:8", "const:4:8"]]
- 00590ce4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00590d24 ["INT_ADD", "register:40f0:8", ["const:590d24:8", "const:4:8"]]
+ 00590d24 ["CALL", null, ["callee:00c57f80:8"]]
- 00590ce4 bytes 731c1b94
+ 00590d24 bytes 971c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d50b8436f47addb5c5f32bdbc0c431fe"></a>

### [`0059120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059120c.md) → [`0059124c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059124c.md) FUN_0059124c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059120c.md#insn-00591228) · [`00591248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059120c.md#insn-00591248)
- 新版 [`00591268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059124c.md#insn-00591268) · [`00591288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059124c.md#insn-00591288)

~~~diff
- 00591228 ["INT_ADD", "register:40f0:8", ["const:591228:8", "const:4:8"]]
- 00591228 ["CALL", null, ["callee:00c53da0:8"]]
+ 00591268 ["INT_ADD", "register:40f0:8", ["const:591268:8", "const:4:8"]]
+ 00591268 ["CALL", null, ["callee:00c53da0:8"]]
- 00591228 bytes b60a1b94
+ 00591268 bytes ce0a1b94
- 00591248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00591248 ["INT_ADD", "register:40f0:8", ["const:591248:8", "const:4:8"]]
- 00591248 ["CALLIND", null, ["register:0:8"]]
+ 00591288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00591288 ["INT_ADD", "register:40f0:8", ["const:591288:8", "const:4:8"]]
+ 00591288 ["CALLIND", null, ["register:0:8"]]
- 00591248 bytes 00013fd6
+ 00591288 bytes 00013fd6
~~~


<a id="compare-fe545482a95ac165d5050f3db993062e"></a>

### [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) → [`0059129c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md) FUN_0059129c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) · 呼出先 2件 [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) · 呼出先 2件 [`00593ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md#insn-00591288) · [`005912b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md#insn-005912b4)
- 新版 [`005912c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md#insn-005912c8) · [`005912f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md#insn-005912f4)

~~~diff
- 00591288 ["INT_ADD", "register:40f0:8", ["const:591288:8", "const:4:8"]]
- 00591288 ["CALL", null, ["callee:00593ce4:8"]]
+ 005912c8 ["INT_ADD", "register:40f0:8", ["const:5912c8:8", "const:4:8"]]
+ 005912c8 ["CALL", null, ["callee:00593ce4:8"]]
- 00591288 bytes 870a0094
+ 005912c8 bytes 870a0094
- 005912b4 ["INT_ADD", "register:40f0:8", ["const:5912b4:8", "const:4:8"]]
- 005912b4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005912f4 ["INT_ADD", "register:40f0:8", ["const:5912f4:8", "const:4:8"]]
+ 005912f4 ["CALL", null, ["callee:00c57fb0:8"]]
- 005912b4 bytes 0b1b1b94
+ 005912f4 bytes 2f1b1b94
~~~


<a id="compare-d27b4483f71afe759661b2f4e1190ae5"></a>

### [`005916cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md) → [`0059170c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059170c.md) FUN_0059170c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00592b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005916f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md#insn-005916f4) · [`00591720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md#insn-00591720)
- 新版 [`00591734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059170c.md#insn-00591734) · [`00591760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059170c.md#insn-00591760)

~~~diff
- 005916f4 ["INT_ADD", "register:40f0:8", ["const:5916f4:8", "const:4:8"]]
- 005916f4 ["CALL", null, ["callee:00592bac:8"]]
+ 00591734 ["INT_ADD", "register:40f0:8", ["const:591734:8", "const:4:8"]]
+ 00591734 ["CALL", null, ["callee:00592bac:8"]]
- 005916f4 bytes 1e050094
+ 00591734 bytes 1e050094
- 00591720 ["INT_ADD", "register:40f0:8", ["const:591720:8", "const:4:8"]]
- 00591720 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00591760 ["INT_ADD", "register:40f0:8", ["const:591760:8", "const:4:8"]]
+ 00591760 ["CALL", null, ["callee:00c57fb0:8"]]
- 00591720 bytes f0191b94
+ 00591760 bytes 141a1b94
~~~


<a id="compare-de41df1d80153b26f9e8d50bd8e720e0"></a>

### [`005917d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005917d0.md) → [`00591810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591810.md) FUN_00591810

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a410.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a480.md) [`00c5a4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005917e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005917d0.md#insn-005917e4)
- 新版 [`00591824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591810.md#insn-00591824)

~~~diff
- 005917e4 ["INT_ADD", "register:40f0:8", ["const:5917e4:8", "const:4:8"]]
- 005917e4 ["CALL", null, ["callee:00c5a480:8"]]
+ 00591824 ["INT_ADD", "register:40f0:8", ["const:591824:8", "const:4:8"]]
+ 00591824 ["CALL", null, ["callee:00c5a480:8"]]
- 005917e4 bytes f3221b94
+ 00591824 bytes 17231b94
~~~


<a id="compare-a9749b5b649bb50dd3071df0c36f817d"></a>

### [`0059180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059180c.md) → [`0059184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059184c.md) FUN_0059184c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a420.md) [`00c5a450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a450.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a480.md) [`00c5a4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a4f0.md) [`00c5a520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059180c.md#insn-00591824)
- 新版 [`00591864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059184c.md#insn-00591864)

~~~diff
- 00591824 ["INT_ADD", "register:40f0:8", ["const:591824:8", "const:4:8"]]
- 00591824 ["CALL", null, ["callee:00c5a480:8"]]
+ 00591864 ["INT_ADD", "register:40f0:8", ["const:591864:8", "const:4:8"]]
+ 00591864 ["CALL", null, ["callee:00c5a480:8"]]
- 00591824 bytes e3221b94
+ 00591864 bytes 07231b94
~~~


<a id="compare-8a4ef4a06bda5bc58c81d9f980459f46"></a>

### [`00591920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591920.md) → [`00591960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591960.md) FUN_00591960

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a480.md) [`00c5a530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591920.md#insn-00591958) · [`00591964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591920.md#insn-00591964) · [`00591980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591920.md#insn-00591980)
- 新版 [`00591998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591960.md#insn-00591998) · [`005919a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591960.md#insn-005919a4) · [`005919c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591960.md#insn-005919c0)

~~~diff
- 00591958 ["INT_ADD", "register:40f0:8", ["const:591958:8", "const:4:8"]]
- 00591958 ["CALL", null, ["callee:00c5a480:8"]]
+ 00591998 ["INT_ADD", "register:40f0:8", ["const:591998:8", "const:4:8"]]
+ 00591998 ["CALL", null, ["callee:00c5a480:8"]]
- 00591958 bytes 96221b94
+ 00591998 bytes ba221b94
- 00591964 ["INT_ADD", "register:40f0:8", ["const:591964:8", "const:4:8"]]
- 00591964 ["CALL", null, ["callee:00c57fa0:8"]]
+ 005919a4 ["INT_ADD", "register:40f0:8", ["const:5919a4:8", "const:4:8"]]
+ 005919a4 ["CALL", null, ["callee:00c57fa0:8"]]
- 00591964 bytes 5b191b94
+ 005919a4 bytes 7f191b94
- 00591980 ["INT_ADD", "register:40f0:8", ["const:591980:8", "const:4:8"]]
- 00591980 ["CALL", null, ["callee:00c5a530:8"]]
+ 005919c0 ["INT_ADD", "register:40f0:8", ["const:5919c0:8", "const:4:8"]]
+ 005919c0 ["CALL", null, ["callee:00c5a530:8"]]
- 00591980 bytes b8221b94
+ 005919c0 bytes dc221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9317b8299b8249b27ef22ccb5ee3d657"></a>

### [`00591abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591abc.md) → [`00591afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591afc.md) FUN_00591afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a480.md) [`00c5a490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a490.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a480.md) [`00c5a550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a550.md) [`00c5a560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a560.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591abc.md#insn-00591ad4) · [`00591ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591abc.md#insn-00591ae4)
- 新版 [`00591b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591afc.md#insn-00591b14) · [`00591b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591afc.md#insn-00591b24)

~~~diff
- 00591ad4 ["INT_ADD", "register:40f0:8", ["const:591ad4:8", "const:4:8"]]
- 00591ad4 ["CALL", null, ["callee:00c5a480:8"]]
+ 00591b14 ["INT_ADD", "register:40f0:8", ["const:591b14:8", "const:4:8"]]
+ 00591b14 ["CALL", null, ["callee:00c5a480:8"]]
- 00591ad4 bytes 37221b94
+ 00591b14 bytes 5b221b94
- 00591ae4 ["INT_ADD", "register:40f0:8", ["const:591ae4:8", "const:4:8"]]
- 00591ae4 ["CALL", null, ["callee:00c5a550:8"]]
+ 00591b24 ["INT_ADD", "register:40f0:8", ["const:591b24:8", "const:4:8"]]
+ 00591b24 ["CALL", null, ["callee:00c5a550:8"]]
- 00591ae4 bytes 67221b94
+ 00591b24 bytes 8b221b94
~~~


<a id="compare-bf1884049b075a6b03e88085672a4db6"></a>

### [`00591b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b1c.md) → [`00591b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b5c.md) FUN_00591b5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4b0.md) [`00c5a4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a580.md) [`00c5a590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b1c.md#insn-00591b24)
- 新版 [`00591b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b5c.md#insn-00591b64)

~~~diff
- 00591b24 ["INT_ADD", "register:40f0:8", ["const:591b24:8", "const:4:8"]]
- 00591b24 ["CALL", null, ["callee:00c5a580:8"]]
+ 00591b64 ["INT_ADD", "register:40f0:8", ["const:591b64:8", "const:4:8"]]
+ 00591b64 ["CALL", null, ["callee:00c5a580:8"]]
- 00591b24 bytes 63221b94
+ 00591b64 bytes 87221b94
~~~


<a id="compare-53bab617f4a9ddecb9ec46fe4a46bf9b"></a>

### [`00591b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md) → [`00591b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md) FUN_00591b74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md) [`00c5a4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4e0.md) [`00c5a4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5a0.md) [`00c5a5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5b0.md) [`00c5a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md#insn-00591b5c) · [`00591b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md#insn-00591b60) · [`00591b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md#insn-00591b7c)
- 新版 [`00591b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md#insn-00591b9c) · [`00591ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md#insn-00591ba0) · [`00591bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md#insn-00591bbc)

~~~diff
- 00591b5c ["INT_ADD", "register:40f0:8", ["const:591b5c:8", "const:4:8"]]
- 00591b5c ["CALL", null, ["callee:00c5a440:8"]]
+ 00591b9c ["INT_ADD", "register:40f0:8", ["const:591b9c:8", "const:4:8"]]
+ 00591b9c ["CALL", null, ["callee:00c5a440:8"]]
- 00591b5c bytes 05221b94
+ 00591b9c bytes 29221b94
- 00591b60 ["INT_ADD", "register:40f0:8", ["const:591b60:8", "const:4:8"]]
- 00591b60 ["CALL", null, ["callee:0058fc04:8"]]
+ 00591ba0 ["INT_ADD", "register:40f0:8", ["const:591ba0:8", "const:4:8"]]
+ 00591ba0 ["CALL", null, ["callee:0058fc04:8"]]
- 00591b60 bytes 19f8ff97
+ 00591ba0 bytes 19f8ff97
- 00591b7c ["INT_ADD", "register:40f0:8", ["const:591b7c:8", "const:4:8"]]
- 00591b7c ["CALL", null, ["callee:00c5a5a0:8"]]
+ 00591bbc ["INT_ADD", "register:40f0:8", ["const:591bbc:8", "const:4:8"]]
+ 00591bbc ["CALL", null, ["callee:00c5a5a0:8"]]
- 00591b7c bytes 55221b94
+ 00591bbc bytes 79221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a58de5e482c0a2c28e3cfcd910d5cf2"></a>

### [`00592148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md) → [`00592188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md) FUN_00592188

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005920c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md) · 呼出先 9件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00592100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md) · 呼出先 9件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md#insn-00592190) · [`0059219c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md#insn-0059219c) · [`005921ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md#insn-005921ac)
- 新版 [`005921d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md#insn-005921d0) · [`005921dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md#insn-005921dc) · [`005921ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md#insn-005921ec)

~~~diff
- 00592190 ["INT_ADD", "register:40f0:8", ["const:592190:8", "const:4:8"]]
- 00592190 ["CALL", null, ["callee:00c57fa0:8"]]
+ 005921d0 ["INT_ADD", "register:40f0:8", ["const:5921d0:8", "const:4:8"]]
+ 005921d0 ["CALL", null, ["callee:00c57fa0:8"]]
- 00592190 bytes 50171b94
+ 005921d0 bytes 74171b94
- 0059219c ["INT_ADD", "register:40f0:8", ["const:59219c:8", "const:4:8"]]
- 0059219c ["CALL", null, ["callee:00c5a5f0:8"]]
+ 005921dc ["INT_ADD", "register:40f0:8", ["const:5921dc:8", "const:4:8"]]
+ 005921dc ["CALL", null, ["callee:00c5a5f0:8"]]
- 0059219c bytes e1201b94
+ 005921dc bytes 05211b94
- 005921ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005921ac ["INT_ADD", "register:40f0:8", ["const:5921ac:8", "const:4:8"]]
- 005921ac ["CALLIND", null, ["register:0:8"]]
+ 005921ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005921ec ["INT_ADD", "register:40f0:8", ["const:5921ec:8", "const:4:8"]]
+ 005921ec ["CALLIND", null, ["register:0:8"]]
- 005921ac bytes 00013fd6
+ 005921ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b8717cde1d1e483ff3f89370fd7f5b9"></a>

### [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md) → [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md) FUN_005925b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) [`00591788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md) [`00591840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md) [`00591888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md) [`005918d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005918d8.md) · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)
- 新版 呼出元 7件 [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) [`005917c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md) [`00591880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md) [`005918c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md) [`00591918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591918.md) · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005925a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md#insn-005925a4)
- 新版 [`005925e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md#insn-005925e4)

~~~diff
- 005925a4 ["INT_ADD", "register:40f0:8", ["const:5925a4:8", "const:4:8"]]
- 005925a4 ["CALL", null, ["local:b0:8"]]
+ 005925e4 ["INT_ADD", "register:40f0:8", ["const:5925e4:8", "const:4:8"]]
+ 005925e4 ["CALL", null, ["local:b0:8"]]
- 005925a4 bytes f5ffff97
+ 005925e4 bytes f5ffff97
~~~


<a id="compare-f96d1a603fc18e9cea02cff927570ab0"></a>

### [`005926a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926a8.md) → [`005926e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005926e8.md) FUN_005926e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005926b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926a8.md#insn-005926b8)
- 新版 [`005926f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005926e8.md#insn-005926f8)

~~~diff
- 005926b8 ["INT_ADD", "register:40f0:8", ["const:5926b8:8", "const:4:8"]]
- 005926b8 ["CALL", null, ["callee:005552c8:8"]]
+ 005926f8 ["INT_ADD", "register:40f0:8", ["const:5926f8:8", "const:4:8"]]
+ 005926f8 ["CALL", null, ["callee:005552c8:8"]]
- 005926b8 bytes f40aff97
+ 005926f8 bytes f40aff97
~~~


<a id="compare-bafb39edc85f8229fdcc83ae45058377"></a>

### [`005926d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926d0.md) → [`00592710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592710.md) FUN_00592710

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926d0.md#insn-00592714) · [`00592720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926d0.md#insn-00592720) · [`00592748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926d0.md#insn-00592748)
- 新版 [`00592754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592710.md#insn-00592754) · [`00592760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592710.md#insn-00592760) · [`00592788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592710.md#insn-00592788)

~~~diff
- 00592714 ["INT_ADD", "register:40f0:8", ["const:592714:8", "const:4:8"]]
- 00592714 ["CALL", null, ["callee:00c57fa0:8"]]
+ 00592754 ["INT_ADD", "register:40f0:8", ["const:592754:8", "const:4:8"]]
+ 00592754 ["CALL", null, ["callee:00c57fa0:8"]]
- 00592714 bytes ef151b94
+ 00592754 bytes 13161b94
- 00592720 ["INT_ADD", "register:40f0:8", ["const:592720:8", "const:4:8"]]
- 00592720 ["CALL", null, ["callee:00c5a440:8"]]
+ 00592760 ["INT_ADD", "register:40f0:8", ["const:592760:8", "const:4:8"]]
+ 00592760 ["CALL", null, ["callee:00c5a440:8"]]
- 00592720 bytes 141f1b94
+ 00592760 bytes 381f1b94
- 00592748 ["INT_ADD", "register:40f0:8", ["const:592748:8", "const:4:8"]]
- 00592748 ["CALL", null, ["callee:00c5a460:8"]]
+ 00592788 ["INT_ADD", "register:40f0:8", ["const:592788:8", "const:4:8"]]
+ 00592788 ["CALL", null, ["callee:00c5a460:8"]]
- 00592748 bytes 121f1b94
+ 00592788 bytes 361f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49c00272c21c8105b1c668905a0fc1b0"></a>

### [`00592784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592784.md) → [`005927c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005927c4.md) FUN_005927c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a380.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005927b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592784.md#insn-005927b4) · [`005927c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592784.md#insn-005927c0) · [`005927d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592784.md#insn-005927d0)
- 新版 [`005927f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005927c4.md#insn-005927f4) · [`00592800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005927c4.md#insn-00592800) · [`00592810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005927c4.md#insn-00592810)

~~~diff
- 005927b4 ["INT_ADD", "register:40f0:8", ["const:5927b4:8", "const:4:8"]]
- 005927b4 ["CALL", null, ["callee:00c57fa0:8"]]
+ 005927f4 ["INT_ADD", "register:40f0:8", ["const:5927f4:8", "const:4:8"]]
+ 005927f4 ["CALL", null, ["callee:00c57fa0:8"]]
- 005927b4 bytes c7151b94
+ 005927f4 bytes eb151b94
- 005927c0 ["INT_ADD", "register:40f0:8", ["const:5927c0:8", "const:4:8"]]
- 005927c0 ["CALL", null, ["callee:00c5a440:8"]]
+ 00592800 ["INT_ADD", "register:40f0:8", ["const:592800:8", "const:4:8"]]
+ 00592800 ["CALL", null, ["callee:00c5a440:8"]]
- 005927c0 bytes ec1e1b94
+ 00592800 bytes 101f1b94
- 005927d0 ["INT_ADD", "register:40f0:8", ["const:5927d0:8", "const:4:8"]]
- 005927d0 ["CALL", null, ["callee:00c5a450:8"]]
+ 00592810 ["INT_ADD", "register:40f0:8", ["const:592810:8", "const:4:8"]]
+ 00592810 ["CALL", null, ["callee:00c5a450:8"]]
- 005927d0 bytes ec1e1b94
+ 00592810 bytes 101f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-622297b2369435759b885c63a3998be2"></a>

### [`00592930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592930.md) → [`00592970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592970.md) FUN_00592970

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592930.md#insn-00592940)
- 新版 [`00592980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592970.md#insn-00592980)

~~~diff
- 00592940 ["INT_ADD", "register:40f0:8", ["const:592940:8", "const:4:8"]]
- 00592940 ["CALL", null, ["callee:005552c8:8"]]
+ 00592980 ["INT_ADD", "register:40f0:8", ["const:592980:8", "const:4:8"]]
+ 00592980 ["CALL", null, ["callee:005552c8:8"]]
- 00592940 bytes 520aff97
+ 00592980 bytes 520aff97
~~~


<a id="compare-c4125f7594fc5a7cc4526d30cb259f45"></a>

### [`00592a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a5c.md) → [`00592a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a9c.md) FUN_00592a9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a500.md) [`00c5a580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a580.md) [`00c5a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a590.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5d0.md) [`00c5a650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a650.md) [`00c5a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a5c.md#insn-00592a88) · [`00592aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a5c.md#insn-00592aa0) · [`00592ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a5c.md#insn-00592ab4)
- 新版 [`00592ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a9c.md#insn-00592ac8) · [`00592ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a9c.md#insn-00592ae0) · [`00592af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a9c.md#insn-00592af4)

~~~diff
- 00592a88 ["INT_ADD", "register:40f0:8", ["const:592a88:8", "const:4:8"]]
- 00592a88 ["CALL", null, ["callee:00c5a5d0:8"]]
+ 00592ac8 ["INT_ADD", "register:40f0:8", ["const:592ac8:8", "const:4:8"]]
+ 00592ac8 ["CALL", null, ["callee:00c5a5d0:8"]]
- 00592a88 bytes 9e1e1b94
+ 00592ac8 bytes c21e1b94
- 00592aa0 ["INT_ADD", "register:40f0:8", ["const:592aa0:8", "const:4:8"]]
- 00592aa0 ["CALL", null, ["callee:00c5a650:8"]]
+ 00592ae0 ["INT_ADD", "register:40f0:8", ["const:592ae0:8", "const:4:8"]]
+ 00592ae0 ["CALL", null, ["callee:00c5a650:8"]]
- 00592aa0 bytes b81e1b94
+ 00592ae0 bytes dc1e1b94
- 00592ab4 ["INT_ADD", "register:40f0:8", ["const:592ab4:8", "const:4:8"]]
- 00592ab4 ["CALL", null, ["callee:00c5a660:8"]]
+ 00592af4 ["INT_ADD", "register:40f0:8", ["const:592af4:8", "const:4:8"]]
+ 00592af4 ["CALL", null, ["callee:00c5a660:8"]]
- 00592ab4 bytes b71e1b94
+ 00592af4 bytes db1e1b94
~~~


<a id="compare-f67dc948f0175995c634bab80ba6c48e"></a>

### [`00592ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592ad0.md) → [`00592b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b10.md) FUN_00592b10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a500.md) [`00c5a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a5a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5d0.md) [`00c5a670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592ad0.md#insn-00592af8) · [`00592b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592ad0.md#insn-00592b08) · [`00592b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592ad0.md#insn-00592b14)
- 新版 [`00592b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b10.md#insn-00592b38) · [`00592b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b10.md#insn-00592b48) · [`00592b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b10.md#insn-00592b54)

~~~diff
- 00592af8 ["INT_ADD", "register:40f0:8", ["const:592af8:8", "const:4:8"]]
- 00592af8 ["CALL", null, ["callee:00c5a5d0:8"]]
+ 00592b38 ["INT_ADD", "register:40f0:8", ["const:592b38:8", "const:4:8"]]
+ 00592b38 ["CALL", null, ["callee:00c5a5d0:8"]]
- 00592af8 bytes 821e1b94
+ 00592b38 bytes a61e1b94
- 00592b08 ["INT_ADD", "register:40f0:8", ["const:592b08:8", "const:4:8"]]
- 00592b08 ["CALL", null, ["callee:00c5a670:8"]]
+ 00592b48 ["INT_ADD", "register:40f0:8", ["const:592b48:8", "const:4:8"]]
+ 00592b48 ["CALL", null, ["callee:00c5a670:8"]]
- 00592b08 bytes a61e1b94
+ 00592b48 bytes ca1e1b94
- 00592b14 ["INT_ADD", "register:40f0:8", ["const:592b14:8", "const:4:8"]]
- 00592b14 ["CALL", null, ["callee:00c5a5d0:8"]]
+ 00592b54 ["INT_ADD", "register:40f0:8", ["const:592b54:8", "const:4:8"]]
+ 00592b54 ["CALL", null, ["callee:00c5a5d0:8"]]
- 00592b14 bytes 7b1e1b94
+ 00592b54 bytes 9f1e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b121909096af775fa7644719e7c014ff"></a>

### [`00592b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b40.md) → [`00592b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b80.md) FUN_00592b80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b40.md#insn-00592b50)
- 新版 [`00592b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592b80.md#insn-00592b90)

~~~diff
- 00592b50 ["INT_ADD", "register:40f0:8", ["const:592b50:8", "const:4:8"]]
- 00592b50 ["CALL", null, ["callee:005552c8:8"]]
+ 00592b90 ["INT_ADD", "register:40f0:8", ["const:592b90:8", "const:4:8"]]
+ 00592b90 ["CALL", null, ["callee:005552c8:8"]]
- 00592b50 bytes ce09ff97
+ 00592b90 bytes ce09ff97
~~~


<a id="compare-74218943ff1bdc56e6296444e6e2000e"></a>

### [`00592c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c64.md) → [`00592ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ca4.md) FUN_00592ca4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c64.md#insn-00592c80) · [`00592ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c64.md#insn-00592ca0)
- 新版 [`00592cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ca4.md#insn-00592cc0) · [`00592ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ca4.md#insn-00592ce0)

~~~diff
- 00592c80 ["INT_ADD", "register:40f0:8", ["const:592c80:8", "const:4:8"]]
- 00592c80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592cc0 ["INT_ADD", "register:40f0:8", ["const:592cc0:8", "const:4:8"]]
+ 00592cc0 ["CALL", null, ["callee:00c53da0:8"]]
- 00592c80 bytes 20041b94
+ 00592cc0 bytes 38041b94
- 00592ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00592ca0 ["INT_ADD", "register:40f0:8", ["const:592ca0:8", "const:4:8"]]
- 00592ca0 ["CALLIND", null, ["register:0:8"]]
+ 00592ce0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00592ce0 ["INT_ADD", "register:40f0:8", ["const:592ce0:8", "const:4:8"]]
+ 00592ce0 ["CALLIND", null, ["register:0:8"]]
- 00592ca0 bytes 00013fd6
+ 00592ce0 bytes 00013fd6
~~~


<a id="compare-e426fb7b9cc1bb9875a343825e5f4f44"></a>

### [`00593aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593aa8.md) → [`00593ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ae8.md) FUN_00593ae8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md) [`00c5a720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593aa8.md#insn-00593b0c)
- 新版 [`00593b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ae8.md#insn-00593b4c)

~~~diff
- 00593b0c ["INT_ADD", "register:40f0:8", ["const:593b0c:8", "const:4:8"]]
- 00593b0c ["CALL", null, ["callee:00c5a540:8"]]
+ 00593b4c ["INT_ADD", "register:40f0:8", ["const:593b4c:8", "const:4:8"]]
+ 00593b4c ["CALL", null, ["callee:00c5a540:8"]]
- 00593b0c bytes 591a1b94
+ 00593b4c bytes 7d1a1b94
~~~


<a id="compare-1b6f262fac61c60bd0e57a95f03a087e"></a>

### [`00593b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593b28.md) → [`00593b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593b68.md) FUN_00593b68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md) [`00c5a730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593b28.md#insn-00593b90)
- 新版 [`00593bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593b68.md#insn-00593bd0)

~~~diff
- 00593b90 ["INT_ADD", "register:40f0:8", ["const:593b90:8", "const:4:8"]]
- 00593b90 ["CALL", null, ["callee:00c5a540:8"]]
+ 00593bd0 ["INT_ADD", "register:40f0:8", ["const:593bd0:8", "const:4:8"]]
+ 00593bd0 ["CALL", null, ["callee:00c5a540:8"]]
- 00593b90 bytes 381a1b94
+ 00593bd0 bytes 5c1a1b94
~~~


<a id="compare-2eede0351f4069c7090ec599294af1a0"></a>

### [`00593bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593bb0.md) → [`00593bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593bf0.md) FUN_00593bf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a670.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md) [`00c5a740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593bb0.md#insn-00593c0c)
- 新版 [`00593c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593bf0.md#insn-00593c4c)

~~~diff
- 00593c0c ["INT_ADD", "register:40f0:8", ["const:593c0c:8", "const:4:8"]]
- 00593c0c ["CALL", null, ["callee:00c5a540:8"]]
+ 00593c4c ["INT_ADD", "register:40f0:8", ["const:593c4c:8", "const:4:8"]]
+ 00593c4c ["CALL", null, ["callee:00c5a540:8"]]
- 00593c0c bytes 191a1b94
+ 00593c4c bytes 3d1a1b94
~~~


<a id="compare-60d62c9fb1d2b7579890b31e050fc26a"></a>

### [`00593c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593c28.md) → [`00593c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593c68.md) FUN_00593c68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a680.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md) [`00c5a750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593c28.md#insn-00593c84)
- 新版 [`00593cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593c68.md#insn-00593cc4)

~~~diff
- 00593c84 ["INT_ADD", "register:40f0:8", ["const:593c84:8", "const:4:8"]]
- 00593c84 ["CALL", null, ["callee:00c5a540:8"]]
+ 00593cc4 ["INT_ADD", "register:40f0:8", ["const:593cc4:8", "const:4:8"]]
+ 00593cc4 ["CALL", null, ["callee:00c5a540:8"]]
- 00593c84 bytes fb191b94
+ 00593cc4 bytes 1f1a1b94
~~~


<a id="compare-344b5045f5d4fe594260e8cea5900668"></a>

### [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) → [`00594380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md) FUN_00594380

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`005948e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md) · 呼出先 2件 [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00594380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md) [`00594920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md) · 呼出先 2件 [`00594380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md#insn-00594360) · [`0059436c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md#insn-0059436c)
- 新版 [`005943a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md#insn-005943a0) · [`005943ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md#insn-005943ac)

~~~diff
- 00594360 ["INT_ADD", "register:40f0:8", ["const:594360:8", "const:4:8"]]
- 00594360 ["CALL", null, ["local:b0:8"]]
+ 005943a0 ["INT_ADD", "register:40f0:8", ["const:5943a0:8", "const:4:8"]]
+ 005943a0 ["CALL", null, ["local:b0:8"]]
- 00594360 bytes f8ffff97
+ 005943a0 bytes f8ffff97
- 0059436c ["INT_ADD", "register:40f0:8", ["const:59436c:8", "const:4:8"]]
- 0059436c ["CALL", null, ["local:b0:8"]]
+ 005943ac ["INT_ADD", "register:40f0:8", ["const:5943ac:8", "const:4:8"]]
+ 005943ac ["CALL", null, ["local:b0:8"]]
- 0059436c bytes f5ffff97
+ 005943ac bytes f5ffff97
~~~


<a id="compare-c652ce3148bfdbab28a1b68a1e68d32d"></a>

### [`00594384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md) → [`005943c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005943c4.md) FUN_005943c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005944b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) [`00b07a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005944f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md#insn-005943bc) · [`005943dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md#insn-005943dc) · [`00594410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md#insn-00594410)
- 新版 [`005943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005943c4.md#insn-005943fc) · [`0059441c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005943c4.md#insn-0059441c) · [`00594450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005943c4.md#insn-00594450)

~~~diff
- 005943bc ["INT_ADD", "register:40f0:8", ["const:5943bc:8", "const:4:8"]]
- 005943bc ["CALL", null, ["callee:005944f0:8"]]
+ 005943fc ["INT_ADD", "register:40f0:8", ["const:5943fc:8", "const:4:8"]]
+ 005943fc ["CALL", null, ["callee:005944f0:8"]]
- 005943bc bytes 3d000094
+ 005943fc bytes 3d000094
- 005943dc ["INT_ADD", "register:40f0:8", ["const:5943dc:8", "const:4:8"]]
- 005943dc ["CALL", null, ["callee:00c57f60:8"]]
+ 0059441c ["INT_ADD", "register:40f0:8", ["const:59441c:8", "const:4:8"]]
+ 0059441c ["CALL", null, ["callee:00c57f60:8"]]
- 005943dc bytes ad0e1b94
+ 0059441c bytes d10e1b94
- 00594410 ["INT_ADD", "register:40f0:8", ["const:594410:8", "const:4:8"]]
- 00594410 ["CALL", null, ["callee:0043bb60:8"]]
+ 00594450 ["INT_ADD", "register:40f0:8", ["const:594450:8", "const:4:8"]]
+ 00594450 ["CALL", null, ["callee:0043bb60:8"]]
- 00594410 bytes c49dfa97
+ 00594450 bytes c49dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa594212bd91c1d24cd13d9a24931de0"></a>

### [`005944b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md) → [`005944f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md) FUN_005944f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md) · 呼出先 2件 [`0044accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044accc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`005943c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005943c4.md) · 呼出先 2件 [`0044ad0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ad0c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md#insn-00594538) · [`0059458c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md#insn-0059458c) · [`00594628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md#insn-00594628)
- 新版 [`00594578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md#insn-00594578) · [`005945cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md#insn-005945cc) · [`00594668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md#insn-00594668)

~~~diff
- 00594538 ["INT_ADD", "register:40f0:8", ["const:594538:8", "const:4:8"]]
- 00594538 ["CALL", null, ["callee:00c58120:8"]]
+ 00594578 ["INT_ADD", "register:40f0:8", ["const:594578:8", "const:4:8"]]
+ 00594578 ["CALL", null, ["callee:00c58120:8"]]
- 00594538 bytes c60e1b94
+ 00594578 bytes ea0e1b94
- 0059458c ["INT_ADD", "register:40f0:8", ["const:59458c:8", "const:4:8"]]
- 0059458c ["CALL", null, ["callee:00c58120:8"]]
+ 005945cc ["INT_ADD", "register:40f0:8", ["const:5945cc:8", "const:4:8"]]
+ 005945cc ["CALL", null, ["callee:00c58120:8"]]
- 0059458c bytes b10e1b94
+ 005945cc bytes d50e1b94
- 00594628 ["INT_ADD", "register:40f0:8", ["const:594628:8", "const:4:8"]]
- 00594628 ["CALL", null, ["callee:00c58120:8"]]
+ 00594668 ["INT_ADD", "register:40f0:8", ["const:594668:8", "const:4:8"]]
+ 00594668 ["CALL", null, ["callee:00c58120:8"]]
- 00594628 bytes 8a0e1b94
+ 00594668 bytes ae0e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a622aeac890c448376f7ce88ab2ecc5d"></a>

### [`0059474c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059474c.md) → [`0059478c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/0059478c.md) FUN_0059478c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059474c.md#insn-00594784)
- 新版 [`005947c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/0059478c.md#insn-005947c4)

~~~diff
- 00594784 ["INT_ADD", "register:40f0:8", ["const:594784:8", "const:4:8"]]
- 00594784 ["CALL", null, ["callee:00c57f80:8"]]
+ 005947c4 ["INT_ADD", "register:40f0:8", ["const:5947c4:8", "const:4:8"]]
+ 005947c4 ["CALL", null, ["callee:00c57f80:8"]]
- 00594784 bytes cb0d1b94
+ 005947c4 bytes ef0d1b94
~~~


<a id="compare-b35912780951cc319fe4727161481954"></a>

### [`0059479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059479c.md) → [`005947dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005947dc.md) FUN_005947dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059479c.md#insn-00594808) · [`00594864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059479c.md#insn-00594864)
- 新版 [`00594848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005947dc.md#insn-00594848) · [`005948a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005947dc.md#insn-005948a4)

~~~diff
- 00594808 ["INT_ADD", "register:40f0:8", ["const:594808:8", "const:4:8"]]
- 00594808 ["CALL", null, ["callee:00c58120:8"]]
+ 00594848 ["INT_ADD", "register:40f0:8", ["const:594848:8", "const:4:8"]]
+ 00594848 ["CALL", null, ["callee:00c58120:8"]]
- 00594808 bytes 120e1b94
+ 00594848 bytes 360e1b94
- 00594864 ["INT_ADD", "register:40f0:8", ["const:594864:8", "const:4:8"]]
- 00594864 ["CALL", null, ["callee:00c58120:8"]]
+ 005948a4 ["INT_ADD", "register:40f0:8", ["const:5948a4:8", "const:4:8"]]
+ 005948a4 ["CALL", null, ["callee:00c58120:8"]]
- 00594864 bytes fb0d1b94
+ 005948a4 bytes 1f0e1b94
~~~


<a id="compare-73aba503e11fff9b48f03a5b545ba843"></a>

### [`00595028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md) → [`00595068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595068.md) FUN_00595068

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md#insn-0059505c) · [`00595090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md#insn-00595090)
- 新版 [`0059509c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595068.md#insn-0059509c) · [`005950d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595068.md#insn-005950d0)

~~~diff
- 0059505c ["COPY", "register:0:8", ["register:4048:8"]]
- 0059505c ["INT_ADD", "register:40f0:8", ["const:59505c:8", "const:4:8"]]
- 0059505c ["CALLIND", null, ["register:0:8"]]
+ 0059509c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059509c ["INT_ADD", "register:40f0:8", ["const:59509c:8", "const:4:8"]]
+ 0059509c ["CALLIND", null, ["register:0:8"]]
- 0059505c bytes 20013fd6
+ 0059509c bytes 20013fd6
- 00595090 ["INT_ADD", "register:40f0:8", ["const:595090:8", "const:4:8"]]
- 00595090 ["CALL", null, ["callee:00588d2c:8"]]
+ 005950d0 ["INT_ADD", "register:40f0:8", ["const:5950d0:8", "const:4:8"]]
+ 005950d0 ["CALL", null, ["callee:00588d2c:8"]]
- 00595090 bytes 17cfff97
+ 005950d0 bytes 17cfff97
~~~


<a id="compare-0e95398f8a461db90d06d91bd2feaa3b"></a>

### [`00595190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595190.md) → [`005951d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005951d0.md) FUN_005951d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) · 呼出先 2件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md)
- 新版 呼出元 1件 [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) · 呼出先 2件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005951a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595190.md#insn-005951a8)
- 新版 [`005951e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005951d0.md#insn-005951e8)

~~~diff
- 005951a8 ["INT_ADD", "register:40f0:8", ["const:5951a8:8", "const:4:8"]]
- 005951a8 ["CALL", null, ["callee:0055f504:8"]]
+ 005951e8 ["INT_ADD", "register:40f0:8", ["const:5951e8:8", "const:4:8"]]
+ 005951e8 ["CALL", null, ["callee:0055f504:8"]]
- 005951a8 bytes c728ff97
+ 005951e8 bytes c728ff97
~~~


<a id="compare-5e0a9ad2e8731832d31e8c0f1aeb48eb"></a>

### [`005951d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005951d0.md) → [`00595210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595210.md) FUN_00595210

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) · 呼出先 2件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md)
- 新版 呼出元 1件 [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) · 呼出先 2件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005951e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005951d0.md#insn-005951e8)
- 新版 [`00595228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595210.md#insn-00595228)

~~~diff
- 005951e8 ["INT_ADD", "register:40f0:8", ["const:5951e8:8", "const:4:8"]]
- 005951e8 ["CALL", null, ["callee:0055f504:8"]]
+ 00595228 ["INT_ADD", "register:40f0:8", ["const:595228:8", "const:4:8"]]
+ 00595228 ["CALL", null, ["callee:0055f504:8"]]
- 005951e8 bytes b728ff97
+ 00595228 bytes b728ff97
~~~


<a id="compare-cfb4cd22e165e5d248647287e883dbc1"></a>

### [`005961d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md) → [`00596214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596214.md) FUN_00596214

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 2件 [`00597230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 2件 [`00597270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597270.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00596250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md#insn-00596250) · [`005962ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md#insn-005962ac) · [`005962e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md#insn-005962e8)
- 新版 [`00596290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596214.md#insn-00596290) · [`005962ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596214.md#insn-005962ec) · [`00596328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596214.md#insn-00596328)

~~~diff
- 00596250 ["INT_ADD", "register:40f0:8", ["const:596250:8", "const:4:8"]]
- 00596250 ["CALL", null, ["callee:00c58120:8"]]
+ 00596290 ["INT_ADD", "register:40f0:8", ["const:596290:8", "const:4:8"]]
+ 00596290 ["CALL", null, ["callee:00c58120:8"]]
- 00596250 bytes 80071b94
+ 00596290 bytes a4071b94
- 005962ac ["INT_ADD", "register:40f0:8", ["const:5962ac:8", "const:4:8"]]
- 005962ac ["CALL", null, ["callee:00c58120:8"]]
+ 005962ec ["INT_ADD", "register:40f0:8", ["const:5962ec:8", "const:4:8"]]
+ 005962ec ["CALL", null, ["callee:00c58120:8"]]
- 005962ac bytes 69071b94
+ 005962ec bytes 8d071b94
- 005962e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005962e8 ["INT_ADD", "register:40f0:8", ["const:5962e8:8", "const:4:8"]]
- 005962e8 ["CALLIND", null, ["register:0:8"]]
+ 00596328 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00596328 ["INT_ADD", "register:40f0:8", ["const:596328:8", "const:4:8"]]
+ 00596328 ["CALLIND", null, ["register:0:8"]]
- 005962e8 bytes 00013fd6
+ 00596328 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a87dca945a4ce3184d99b616ad6f06f"></a>

### [`0059633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md) → [`0059637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/0059637c.md) FUN_0059637c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 2件 [`0059736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 2件 [`005973ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005973ac.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005963b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md#insn-005963b8) · [`00596414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md#insn-00596414) · [`00596450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md#insn-00596450)
- 新版 [`005963f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/0059637c.md#insn-005963f8) · [`00596454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/0059637c.md#insn-00596454) · [`00596490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/0059637c.md#insn-00596490)

~~~diff
- 005963b8 ["INT_ADD", "register:40f0:8", ["const:5963b8:8", "const:4:8"]]
- 005963b8 ["CALL", null, ["callee:00c58120:8"]]
+ 005963f8 ["INT_ADD", "register:40f0:8", ["const:5963f8:8", "const:4:8"]]
+ 005963f8 ["CALL", null, ["callee:00c58120:8"]]
- 005963b8 bytes 26071b94
+ 005963f8 bytes 4a071b94
- 00596414 ["INT_ADD", "register:40f0:8", ["const:596414:8", "const:4:8"]]
- 00596414 ["CALL", null, ["callee:00c58120:8"]]
+ 00596454 ["INT_ADD", "register:40f0:8", ["const:596454:8", "const:4:8"]]
+ 00596454 ["CALL", null, ["callee:00c58120:8"]]
- 00596414 bytes 0f071b94
+ 00596454 bytes 33071b94
- 00596450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00596450 ["INT_ADD", "register:40f0:8", ["const:596450:8", "const:4:8"]]
- 00596450 ["CALLIND", null, ["register:0:8"]]
+ 00596490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00596490 ["INT_ADD", "register:40f0:8", ["const:596490:8", "const:4:8"]]
+ 00596490 ["CALLIND", null, ["register:0:8"]]
- 00596450 bytes 00013fd6
+ 00596490 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348e1af3cbe55b4c2c21be35d06a4c71"></a>

### [`00596e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md) → [`00596e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md) FUN_00596e5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0059705c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00596e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md#insn-00596e44) · [`00596e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md#insn-00596e5c) · [`00596e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md#insn-00596e68)
- 新版 [`00596e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md#insn-00596e84) · [`00596e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md#insn-00596e9c) · [`00596ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md#insn-00596ea8)

~~~diff
- 00596e44 ["INT_ADD", "register:40f0:8", ["const:596e44:8", "const:4:8"]]
- 00596e44 ["CALL", null, ["callee:00550be4:8"]]
+ 00596e84 ["INT_ADD", "register:40f0:8", ["const:596e84:8", "const:4:8"]]
+ 00596e84 ["CALL", null, ["callee:00550be4:8"]]
- 00596e44 bytes 58e7fe97
+ 00596e84 bytes 58e7fe97
- 00596e5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00596e5c ["INT_ADD", "register:40f0:8", ["const:596e5c:8", "const:4:8"]]
- 00596e5c ["CALLIND", null, ["register:0:8"]]
+ 00596e9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00596e9c ["INT_ADD", "register:40f0:8", ["const:596e9c:8", "const:4:8"]]
+ 00596e9c ["CALLIND", null, ["register:0:8"]]
- 00596e5c bytes 20013fd6
+ 00596e9c bytes 20013fd6
- 00596e68 ["INT_ADD", "register:40f0:8", ["const:596e68:8", "const:4:8"]]
- 00596e68 ["CALL", null, ["callee:00596d50:8"]]
+ 00596ea8 ["INT_ADD", "register:40f0:8", ["const:596ea8:8", "const:4:8"]]
+ 00596ea8 ["CALL", null, ["callee:00596d50:8"]]
- 00596e68 bytes aaffff97
+ 00596ea8 bytes aaffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

