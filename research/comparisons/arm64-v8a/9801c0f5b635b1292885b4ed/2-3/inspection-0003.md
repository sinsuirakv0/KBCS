# v16.0.1 → v16.0.2 · 要調査の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-c24e5c27ea12fd3e13cba0a0e0782ad5"></a>

### [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) → [`004701a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004701a4.md) FUN_004701a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470394.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047020c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-0047020c) · [`0047024c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-0047024c) · [`00470290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-00470290)
- 新版 `0047024c`（命令位置の公開資料なし） · `0047028c`（命令位置の公開資料なし） · `004702d0`（命令位置の公開資料なし）

~~~diff
- 0047020c ["INT_ADD", "register:40f0:8", ["const:47020c:8", "const:4:8"]]
- 0047020c ["CALL", null, ["callee:00c57f60:8"]]
+ 0047024c ["INT_ADD", "register:40f0:8", ["const:47024c:8", "const:4:8"]]
+ 0047024c ["CALL", null, ["callee:00c57f60:8"]]
- 0047020c bytes 219f1f94
+ 0047024c bytes 459f1f94
- 0047024c ["INT_ADD", "register:40f0:8", ["const:47024c:8", "const:4:8"]]
- 0047024c ["CALL", null, ["callee:00c58160:8"]]
+ 0047028c ["INT_ADD", "register:40f0:8", ["const:47028c:8", "const:4:8"]]
+ 0047028c ["CALL", null, ["callee:00c58160:8"]]
- 0047024c bytes 919f1f94
+ 0047028c bytes b59f1f94
- 00470290 ["INT_ADD", "register:40f0:8", ["const:470290:8", "const:4:8"]]
- 00470290 ["CALL", null, ["callee:00c58160:8"]]
+ 004702d0 ["INT_ADD", "register:40f0:8", ["const:4702d0:8", "const:4:8"]]
+ 004702d0 ["CALL", null, ["callee:00c58160:8"]]
- 00470290 bytes 809f1f94
+ 004702d0 bytes a49f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4211273d289b2726c37707e1c90bb5a"></a>

### [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) → [`004703a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004703a8.md) FUN_004703a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004704d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704d4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004703e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-004703e0) · [`00470404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-00470404) · [`00470430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-00470430)
- 新版 `00470420`（命令位置の公開資料なし） · `00470444`（命令位置の公開資料なし） · `00470470`（命令位置の公開資料なし）

~~~diff
- 004703e0 ["INT_ADD", "register:40f0:8", ["const:4703e0:8", "const:4:8"]]
- 004703e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00470420 ["INT_ADD", "register:40f0:8", ["const:470420:8", "const:4:8"]]
+ 00470420 ["CALL", null, ["callee:00c57f60:8"]]
- 004703e0 bytes ac9e1f94
+ 00470420 bytes d09e1f94
- 00470404 ["INT_ADD", "register:40f0:8", ["const:470404:8", "const:4:8"]]
- 00470404 ["CALL", null, ["callee:00c58160:8"]]
+ 00470444 ["INT_ADD", "register:40f0:8", ["const:470444:8", "const:4:8"]]
+ 00470444 ["CALL", null, ["callee:00c58160:8"]]
- 00470404 bytes 239f1f94
+ 00470444 bytes 479f1f94
- 00470430 ["INT_ADD", "register:40f0:8", ["const:470430:8", "const:4:8"]]
- 00470430 ["CALL", null, ["callee:00c58160:8"]]
+ 00470470 ["INT_ADD", "register:40f0:8", ["const:470470:8", "const:4:8"]]
+ 00470470 ["CALL", null, ["callee:00c58160:8"]]
- 00470430 bytes 189f1f94
+ 00470470 bytes 3c9f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58fb60930ad78fc96d69a97368efb500"></a>

### [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) → [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md) FUN_00470754

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`009e3ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3ea8.md) [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) [`009e3efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3efc.md) [`00a355e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a355e8.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-0047078c) · [`004707b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-004707b0) · [`004707dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-004707dc)
- 新版 `004707cc`（命令位置の公開資料なし） · `004707f0`（命令位置の公開資料なし） · `0047081c`（命令位置の公開資料なし）

~~~diff
- 0047078c ["INT_ADD", "register:40f0:8", ["const:47078c:8", "const:4:8"]]
- 0047078c ["CALL", null, ["callee:00c57f60:8"]]
+ 004707cc ["INT_ADD", "register:40f0:8", ["const:4707cc:8", "const:4:8"]]
+ 004707cc ["CALL", null, ["callee:00c57f60:8"]]
- 0047078c bytes c19d1f94
+ 004707cc bytes e59d1f94
- 004707b0 ["INT_ADD", "register:40f0:8", ["const:4707b0:8", "const:4:8"]]
- 004707b0 ["CALL", null, ["callee:00c58160:8"]]
+ 004707f0 ["INT_ADD", "register:40f0:8", ["const:4707f0:8", "const:4:8"]]
+ 004707f0 ["CALL", null, ["callee:00c58160:8"]]
- 004707b0 bytes 389e1f94
+ 004707f0 bytes 5c9e1f94
- 004707dc ["INT_ADD", "register:40f0:8", ["const:4707dc:8", "const:4:8"]]
- 004707dc ["CALL", null, ["callee:00c58160:8"]]
+ 0047081c ["INT_ADD", "register:40f0:8", ["const:47081c:8", "const:4:8"]]
+ 0047081c ["CALL", null, ["callee:00c58160:8"]]
- 004707dc bytes 2d9e1f94
+ 0047081c bytes 519e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea749c334d868bd4a0e0cc6b47811a3"></a>

### [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) → [`00470894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470894.md) FUN_00470894

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004709c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004708cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-004708cc) · [`004708f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-004708f0) · [`0047091c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-0047091c)
- 新版 `0047090c`（命令位置の公開資料なし） · `00470930`（命令位置の公開資料なし） · `0047095c`（命令位置の公開資料なし）

~~~diff
- 004708cc ["INT_ADD", "register:40f0:8", ["const:4708cc:8", "const:4:8"]]
- 004708cc ["CALL", null, ["callee:00c57f60:8"]]
+ 0047090c ["INT_ADD", "register:40f0:8", ["const:47090c:8", "const:4:8"]]
+ 0047090c ["CALL", null, ["callee:00c57f60:8"]]
- 004708cc bytes 719d1f94
+ 0047090c bytes 959d1f94
- 004708f0 ["INT_ADD", "register:40f0:8", ["const:4708f0:8", "const:4:8"]]
- 004708f0 ["CALL", null, ["callee:00c58160:8"]]
+ 00470930 ["INT_ADD", "register:40f0:8", ["const:470930:8", "const:4:8"]]
+ 00470930 ["CALL", null, ["callee:00c58160:8"]]
- 004708f0 bytes e89d1f94
+ 00470930 bytes 0c9e1f94
- 0047091c ["INT_ADD", "register:40f0:8", ["const:47091c:8", "const:4:8"]]
- 0047091c ["CALL", null, ["callee:00c58160:8"]]
+ 0047095c ["INT_ADD", "register:40f0:8", ["const:47095c:8", "const:4:8"]]
+ 0047095c ["CALL", null, ["callee:00c58160:8"]]
- 0047091c bytes dd9d1f94
+ 0047095c bytes 019e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb077da6d94d3c6a76b5958881bc65e"></a>

### [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) → [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) FUN_004709d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) [`006416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006416ec.md) [`006847fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006847fc.md) [`0068ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068ae30.md) [`0068c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md) · 呼出先 5件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 19件 [`0046f79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f79c.md) [`0064172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md) [`0068483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/0068483c.md) [`0068ae88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068ae88.md) [`0068c668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068c/0068c668.md) · 呼出先 5件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004709d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-004709d8) · [`00470a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-00470a20) · [`00470a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-00470a48)
- 新版 `00470a18`（命令位置の公開資料なし） · `00470a60`（命令位置の公開資料なし） · `00470a88`（命令位置の公開資料なし）

~~~diff
- 004709d8 ["INT_ADD", "register:40f0:8", ["const:4709d8:8", "const:4:8"]]
- 004709d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00470a18 ["INT_ADD", "register:40f0:8", ["const:470a18:8", "const:4:8"]]
+ 00470a18 ["CALL", null, ["callee:00c57f80:8"]]
- 004709d8 bytes 369d1f94
+ 00470a18 bytes 5a9d1f94
- 00470a20 ["INT_ADD", "register:40f0:8", ["const:470a20:8", "const:4:8"]]
- 00470a20 ["CALL", null, ["callee:00c57f60:8"]]
+ 00470a60 ["INT_ADD", "register:40f0:8", ["const:470a60:8", "const:4:8"]]
+ 00470a60 ["CALL", null, ["callee:00c57f60:8"]]
- 00470a20 bytes 1c9d1f94
+ 00470a60 bytes 409d1f94
- 00470a48 ["INT_ADD", "register:40f0:8", ["const:470a48:8", "const:4:8"]]
- 00470a48 ["CALL", null, ["callee:00c580d0:8"]]
+ 00470a88 ["INT_ADD", "register:40f0:8", ["const:470a88:8", "const:4:8"]]
+ 00470a88 ["CALL", null, ["callee:00c580d0:8"]]
- 00470a48 bytes 6e9d1f94
+ 00470a88 bytes 929d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c83da552623c1b8ea359ba45361bff"></a>

### [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) → [`00470f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f30.md) FUN_00470f30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) · 呼出先 3件 [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md)
- 新版 呼出元 1件 [`00470e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470e94.md) · 呼出先 3件 [`00471c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c70.md) [`00471cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471cfc.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00470f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f04) · [`00470f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f10) · [`00470f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f1c)
- 新版 `00470f44`（命令位置の公開資料なし） · `00470f50`（命令位置の公開資料なし） · `00470f5c`（命令位置の公開資料なし）

~~~diff
- 00470f04 ["INT_ADD", "register:40f0:8", ["const:470f04:8", "const:4:8"]]
- 00470f04 ["CALL", null, ["callee:00c57f30:8"]]
+ 00470f44 ["INT_ADD", "register:40f0:8", ["const:470f44:8", "const:4:8"]]
+ 00470f44 ["CALL", null, ["callee:00c57f30:8"]]
- 00470f04 bytes d79b1f94
+ 00470f44 bytes fb9b1f94
- 00470f10 ["INT_ADD", "register:40f0:8", ["const:470f10:8", "const:4:8"]]
- 00470f10 ["CALL", null, ["callee:00471c70:8"]]
+ 00470f50 ["INT_ADD", "register:40f0:8", ["const:470f50:8", "const:4:8"]]
+ 00470f50 ["CALL", null, ["callee:00471c70:8"]]
- 00470f10 bytes 48030094
+ 00470f50 bytes 48030094
- 00470f1c ["INT_ADD", "register:40f0:8", ["const:470f1c:8", "const:4:8"]]
- 00470f1c ["CALL", null, ["callee:00471c70:8"]]
+ 00470f5c ["INT_ADD", "register:40f0:8", ["const:470f5c:8", "const:4:8"]]
+ 00470f5c ["CALL", null, ["callee:00471c70:8"]]
- 00470f1c bytes 45030094
+ 00470f5c bytes 45030094
~~~


<a id="compare-881e2c34468962300ea7f74bb6160501"></a>

### [`004716d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md) → [`00471714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471714.md) FUN_00471714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004716f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md#insn-004716f0) · [`00471710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md#insn-00471710)
- 新版 `00471730`（命令位置の公開資料なし） · `00471750`（命令位置の公開資料なし）

~~~diff
- 004716f0 ["INT_ADD", "register:40f0:8", ["const:4716f0:8", "const:4:8"]]
- 004716f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00471730 ["INT_ADD", "register:40f0:8", ["const:471730:8", "const:4:8"]]
+ 00471730 ["CALL", null, ["callee:00c53da0:8"]]
- 004716f0 bytes 84891f94
+ 00471730 bytes 9c891f94
- 00471710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471710 ["INT_ADD", "register:40f0:8", ["const:471710:8", "const:4:8"]]
- 00471710 ["CALLIND", null, ["register:0:8"]]
+ 00471750 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00471750 ["INT_ADD", "register:40f0:8", ["const:471750:8", "const:4:8"]]
+ 00471750 ["CALLIND", null, ["register:0:8"]]
- 00471710 bytes 00013fd6
+ 00471750 bytes 00013fd6
~~~


<a id="compare-4a4b3354c606a98f7c387fd7cc51977c"></a>

### [`00471c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md) → [`00471c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c44.md) FUN_00471c44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009265b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00926/009265b0.md) · 呼出先 1件 [`0047256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md)
- 新版 呼出元 1件 [`00926604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00926/00926604.md) · 呼出先 1件 [`004725ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004725ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md#insn-00471c14)
- 新版 `00471c54`（命令位置の公開資料なし）

~~~diff
- 00471c14 ["INT_ADD", "register:40f0:8", ["const:471c14:8", "const:4:8"]]
- 00471c14 ["CALL", null, ["callee:004725ac:8"]]
+ 00471c54 ["INT_ADD", "register:40f0:8", ["const:471c54:8", "const:4:8"]]
+ 00471c54 ["CALL", null, ["callee:004725ac:8"]]
- 00471c14 bytes 56020094
+ 00471c54 bytes 56020094
~~~


<a id="compare-59cf0260d9382db3eb04b83605e4fc3a"></a>

### [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) → [`00471c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c70.md) FUN_00471c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) · 呼出先 4件 [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00470f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f30.md) [`00471c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c70.md) · 呼出先 4件 [`00471c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c4c) · [`00471c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c58) · [`00471c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c6c)
- 新版 `00471c8c`（命令位置の公開資料なし） · `00471c98`（命令位置の公開資料なし） · `00471cac`（命令位置の公開資料なし）

~~~diff
- 00471c4c ["INT_ADD", "register:40f0:8", ["const:471c4c:8", "const:4:8"]]
- 00471c4c ["CALL", null, ["local:b0:8"]]
+ 00471c8c ["INT_ADD", "register:40f0:8", ["const:471c8c:8", "const:4:8"]]
+ 00471c8c ["CALL", null, ["local:b0:8"]]
- 00471c4c bytes f9ffff97
+ 00471c8c bytes f9ffff97
- 00471c58 ["INT_ADD", "register:40f0:8", ["const:471c58:8", "const:4:8"]]
- 00471c58 ["CALL", null, ["local:b0:8"]]
+ 00471c98 ["INT_ADD", "register:40f0:8", ["const:471c98:8", "const:4:8"]]
+ 00471c98 ["CALL", null, ["local:b0:8"]]
- 00471c58 bytes f6ffff97
+ 00471c98 bytes f6ffff97
- 00471c6c ["INT_ADD", "register:40f0:8", ["const:471c6c:8", "const:4:8"]]
- 00471c6c ["CALL", null, ["callee:00c53da0:8"]]
+ 00471cac ["INT_ADD", "register:40f0:8", ["const:471cac:8", "const:4:8"]]
+ 00471cac ["CALL", null, ["callee:00c53da0:8"]]
- 00471c6c bytes 25881f94
+ 00471cac bytes 3d881f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd7e0cadf47055db11816a9ba7223d4"></a>

### [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) → [`00471cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471cfc.md) FUN_00471cfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) · 呼出先 2件 [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00470f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f30.md) [`00471cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471cfc.md) · 呼出先 2件 [`00471cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471cfc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471cd8) · [`00471ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471ce4) · [`00471cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471cf4)
- 新版 `00471d18`（命令位置の公開資料なし） · `00471d24`（命令位置の公開資料なし） · `00471d34`（命令位置の公開資料なし）

~~~diff
- 00471cd8 ["INT_ADD", "register:40f0:8", ["const:471cd8:8", "const:4:8"]]
- 00471cd8 ["CALL", null, ["local:b0:8"]]
+ 00471d18 ["INT_ADD", "register:40f0:8", ["const:471d18:8", "const:4:8"]]
+ 00471d18 ["CALL", null, ["local:b0:8"]]
- 00471cd8 bytes f9ffff97
+ 00471d18 bytes f9ffff97
- 00471ce4 ["INT_ADD", "register:40f0:8", ["const:471ce4:8", "const:4:8"]]
- 00471ce4 ["CALL", null, ["local:b0:8"]]
+ 00471d24 ["INT_ADD", "register:40f0:8", ["const:471d24:8", "const:4:8"]]
+ 00471d24 ["CALL", null, ["local:b0:8"]]
- 00471ce4 bytes f6ffff97
+ 00471d24 bytes f6ffff97
- 00471cf4 ["INT_ADD", "register:40f0:8", ["const:471cf4:8", "const:4:8"]]
- 00471cf4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00471d34 ["INT_ADD", "register:40f0:8", ["const:471d34:8", "const:4:8"]]
+ 00471d34 ["CALL", null, ["callee:00c57f80:8"]]
- 00471cf4 bytes 6f981f94
+ 00471d34 bytes 93981f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31c958badab2fb799b4992c0ecd3be22"></a>

### [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) → [`00471d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471d5c.md) FUN_00471d5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00471e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00471e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471e94.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471d50) · [`00471d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471d70) · [`00471dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471dac)
- 新版 `00471d90`（命令位置の公開資料なし） · `00471db0`（命令位置の公開資料なし） · `00471dec`（命令位置の公開資料なし）

~~~diff
- 00471d50 ["INT_ADD", "register:40f0:8", ["const:471d50:8", "const:4:8"]]
- 00471d50 ["CALL", null, ["callee:00471e94:8"]]
+ 00471d90 ["INT_ADD", "register:40f0:8", ["const:471d90:8", "const:4:8"]]
+ 00471d90 ["CALL", null, ["callee:00471e94:8"]]
- 00471d50 bytes 41000094
+ 00471d90 bytes 41000094
- 00471d70 ["INT_ADD", "register:40f0:8", ["const:471d70:8", "const:4:8"]]
- 00471d70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00471db0 ["INT_ADD", "register:40f0:8", ["const:471db0:8", "const:4:8"]]
+ 00471db0 ["CALL", null, ["callee:00c57f60:8"]]
- 00471d70 bytes 48981f94
+ 00471db0 bytes 6c981f94
- 00471dac ["INT_ADD", "register:40f0:8", ["const:471dac:8", "const:4:8"]]
- 00471dac ["CALL", null, ["callee:0043bb60:8"]]
+ 00471dec ["INT_ADD", "register:40f0:8", ["const:471dec:8", "const:4:8"]]
+ 00471dec ["CALL", null, ["callee:0043bb60:8"]]
- 00471dac bytes 5d27ff97
+ 00471dec bytes 5d27ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be32cf5d20ea4c2fce7d9a9cd49e19d"></a>

### [`00471e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md) → [`00471e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471e94.md) FUN_00471e94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00471d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471d5c.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md#insn-00471ed8) · [`00471f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md#insn-00471f04)
- 新版 `00471f18`（命令位置の公開資料なし） · `00471f44`（命令位置の公開資料なし）

~~~diff
- 00471ed8 ["INT_ADD", "register:40f0:8", ["const:471ed8:8", "const:4:8"]]
- 00471ed8 ["CALL", null, ["callee:00c58120:8"]]
+ 00471f18 ["INT_ADD", "register:40f0:8", ["const:471f18:8", "const:4:8"]]
+ 00471f18 ["CALL", null, ["callee:00c58120:8"]]
- 00471ed8 bytes 5e981f94
+ 00471f18 bytes 82981f94
- 00471f04 ["INT_ADD", "register:40f0:8", ["const:471f04:8", "const:4:8"]]
- 00471f04 ["CALL", null, ["callee:00c58120:8"]]
+ 00471f44 ["INT_ADD", "register:40f0:8", ["const:471f44:8", "const:4:8"]]
+ 00471f44 ["CALL", null, ["callee:00c58120:8"]]
- 00471f04 bytes 53981f94
+ 00471f44 bytes 77981f94
~~~


<a id="compare-c0052f6268e05a6707780ef2a902df8e"></a>

### [`00471f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md) → [`00471f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471f98.md) FUN_00471f98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md#insn-00471f84) · [`00471f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md#insn-00471f94)
- 新版 `00471fc4`（命令位置の公開資料なし） · `00471fd4`（命令位置の公開資料なし）

~~~diff
- 00471f84 ["INT_ADD", "register:40f0:8", ["const:471f84:8", "const:4:8"]]
- 00471f84 ["CALL", null, ["callee:00c57f80:8"]]
+ 00471fc4 ["INT_ADD", "register:40f0:8", ["const:471fc4:8", "const:4:8"]]
+ 00471fc4 ["CALL", null, ["callee:00c57f80:8"]]
- 00471f84 bytes cb971f94
+ 00471fc4 bytes ef971f94
- 00471f94 ["INT_ADD", "register:40f0:8", ["const:471f94:8", "const:4:8"]]
- 00471f94 ["CALL", null, ["callee:00c57f80:8"]]
+ 00471fd4 ["INT_ADD", "register:40f0:8", ["const:471fd4:8", "const:4:8"]]
+ 00471fd4 ["CALL", null, ["callee:00c57f80:8"]]
- 00471f94 bytes c7971f94
+ 00471fd4 bytes eb971f94
~~~


<a id="compare-adc158dc21eb9e4ca85c0437d0b53329"></a>

### [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) → [`00471ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471ff4.md) FUN_00471ff4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md#insn-00472020) · [`0047207c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md#insn-0047207c)
- 新版 `00472060`（命令位置の公開資料なし） · `004720bc`（命令位置の公開資料なし）

~~~diff
- 00472020 ["INT_ADD", "register:40f0:8", ["const:472020:8", "const:4:8"]]
- 00472020 ["CALL", null, ["callee:00c58120:8"]]
+ 00472060 ["INT_ADD", "register:40f0:8", ["const:472060:8", "const:4:8"]]
+ 00472060 ["CALL", null, ["callee:00c58120:8"]]
- 00472020 bytes 0c981f94
+ 00472060 bytes 30981f94
- 0047207c ["INT_ADD", "register:40f0:8", ["const:47207c:8", "const:4:8"]]
- 0047207c ["CALL", null, ["callee:00c58120:8"]]
+ 004720bc ["INT_ADD", "register:40f0:8", ["const:4720bc:8", "const:4:8"]]
+ 004720bc ["CALL", null, ["callee:00c58120:8"]]
- 0047207c bytes f5971f94
+ 004720bc bytes 19981f94
~~~


<a id="compare-ed3a56d1ed0756d58574a14aa1441d61"></a>

### [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) → [`004720f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004720f8.md) FUN_004720f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004721e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00472224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472224.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004720ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-004720ec) · [`0047210c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-0047210c) · [`00472148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-00472148)
- 新版 `0047212c`（命令位置の公開資料なし） · `0047214c`（命令位置の公開資料なし） · `00472188`（命令位置の公開資料なし）

~~~diff
- 004720ec ["INT_ADD", "register:40f0:8", ["const:4720ec:8", "const:4:8"]]
- 004720ec ["CALL", null, ["callee:00472224:8"]]
+ 0047212c ["INT_ADD", "register:40f0:8", ["const:47212c:8", "const:4:8"]]
+ 0047212c ["CALL", null, ["callee:00472224:8"]]
- 004720ec bytes 3e000094
+ 0047212c bytes 3e000094
- 0047210c ["INT_ADD", "register:40f0:8", ["const:47210c:8", "const:4:8"]]
- 0047210c ["CALL", null, ["callee:00c57f60:8"]]
+ 0047214c ["INT_ADD", "register:40f0:8", ["const:47214c:8", "const:4:8"]]
+ 0047214c ["CALL", null, ["callee:00c57f60:8"]]
- 0047210c bytes 61971f94
+ 0047214c bytes 85971f94
- 00472148 ["INT_ADD", "register:40f0:8", ["const:472148:8", "const:4:8"]]
- 00472148 ["CALL", null, ["callee:0043bb60:8"]]
+ 00472188 ["INT_ADD", "register:40f0:8", ["const:472188:8", "const:4:8"]]
+ 00472188 ["CALL", null, ["callee:0043bb60:8"]]
- 00472148 bytes 7626ff97
+ 00472188 bytes 7626ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a4f8056aff191e7ddbbd3d03016028"></a>

### [`004721e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md) → [`00472224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472224.md) FUN_00472224

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`004720f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004720f8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md#insn-00472268) · [`00472294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md#insn-00472294)
- 新版 `004722a8`（命令位置の公開資料なし） · `004722d4`（命令位置の公開資料なし）

~~~diff
- 00472268 ["INT_ADD", "register:40f0:8", ["const:472268:8", "const:4:8"]]
- 00472268 ["CALL", null, ["callee:00c58120:8"]]
+ 004722a8 ["INT_ADD", "register:40f0:8", ["const:4722a8:8", "const:4:8"]]
+ 004722a8 ["CALL", null, ["callee:00c58120:8"]]
- 00472268 bytes 7a971f94
+ 004722a8 bytes 9e971f94
- 00472294 ["INT_ADD", "register:40f0:8", ["const:472294:8", "const:4:8"]]
- 00472294 ["CALL", null, ["callee:00c58120:8"]]
+ 004722d4 ["INT_ADD", "register:40f0:8", ["const:4722d4:8", "const:4:8"]]
+ 004722d4 ["CALL", null, ["callee:00c58120:8"]]
- 00472294 bytes 6f971f94
+ 004722d4 bytes 93971f94
~~~


<a id="compare-1912aa0685131c197c1e7c0ee0257361"></a>

### [`004722e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md) → [`00472328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472328.md) FUN_00472328

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-00472318) · [`0047232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-0047232c) · [`00472334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-00472334)
- 新版 `00472358`（命令位置の公開資料なし） · `0047236c`（命令位置の公開資料なし） · `00472374`（命令位置の公開資料なし）

~~~diff
- 00472318 ["INT_ADD", "register:40f0:8", ["const:472318:8", "const:4:8"]]
- 00472318 ["CALL", null, ["callee:00c53da0:8"]]
+ 00472358 ["INT_ADD", "register:40f0:8", ["const:472358:8", "const:4:8"]]
+ 00472358 ["CALL", null, ["callee:00c53da0:8"]]
- 00472318 bytes 7a861f94
+ 00472358 bytes 92861f94
- 0047232c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047232c ["INT_ADD", "register:40f0:8", ["const:47232c:8", "const:4:8"]]
- 0047232c ["CALLIND", null, ["register:0:8"]]
+ 0047236c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047236c ["INT_ADD", "register:40f0:8", ["const:47236c:8", "const:4:8"]]
+ 0047236c ["CALLIND", null, ["register:0:8"]]
- 0047232c bytes 00013fd6
+ 0047236c bytes 00013fd6
- 00472334 ["INT_ADD", "register:40f0:8", ["const:472334:8", "const:4:8"]]
- 00472334 ["CALL", null, ["callee:00c57f50:8"]]
+ 00472374 ["INT_ADD", "register:40f0:8", ["const:472374:8", "const:4:8"]]
+ 00472374 ["CALL", null, ["callee:00c57f50:8"]]
- 00472334 bytes d3961f94
+ 00472374 bytes f7961f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83143e59cf9b1a01f7545c3b70f3a3a4"></a>

### [`00472364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md) → [`004723a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004723a4.md) FUN_004723a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00471764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471764.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004723d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md#insn-004723d0) · [`0047242c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md#insn-0047242c)
- 新版 `00472410`（命令位置の公開資料なし） · `0047246c`（命令位置の公開資料なし）

~~~diff
- 004723d0 ["INT_ADD", "register:40f0:8", ["const:4723d0:8", "const:4:8"]]
- 004723d0 ["CALL", null, ["callee:00c58120:8"]]
+ 00472410 ["INT_ADD", "register:40f0:8", ["const:472410:8", "const:4:8"]]
+ 00472410 ["CALL", null, ["callee:00c58120:8"]]
- 004723d0 bytes 20971f94
+ 00472410 bytes 44971f94
- 0047242c ["INT_ADD", "register:40f0:8", ["const:47242c:8", "const:4:8"]]
- 0047242c ["CALL", null, ["callee:00c58120:8"]]
+ 0047246c ["INT_ADD", "register:40f0:8", ["const:47246c:8", "const:4:8"]]
+ 0047246c ["CALL", null, ["callee:00c58120:8"]]
- 0047242c bytes 09971f94
+ 0047246c bytes 2d971f94
~~~


<a id="compare-69764b6e350e7e287f881a2849c18a0b"></a>

### [`00472468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md) → [`004724a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004724a8.md) FUN_004724a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00471764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471764.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004724d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md#insn-004724d4) · [`00472530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md#insn-00472530)
- 新版 `00472514`（命令位置の公開資料なし） · `00472570`（命令位置の公開資料なし）

~~~diff
- 004724d4 ["INT_ADD", "register:40f0:8", ["const:4724d4:8", "const:4:8"]]
- 004724d4 ["CALL", null, ["callee:00c58120:8"]]
+ 00472514 ["INT_ADD", "register:40f0:8", ["const:472514:8", "const:4:8"]]
+ 00472514 ["CALL", null, ["callee:00c58120:8"]]
- 004724d4 bytes df961f94
+ 00472514 bytes 03971f94
- 00472530 ["INT_ADD", "register:40f0:8", ["const:472530:8", "const:4:8"]]
- 00472530 ["CALL", null, ["callee:00c58120:8"]]
+ 00472570 ["INT_ADD", "register:40f0:8", ["const:472570:8", "const:4:8"]]
+ 00472570 ["CALL", null, ["callee:00c58120:8"]]
- 00472530 bytes c8961f94
+ 00472570 bytes ec961f94
~~~


<a id="compare-eef4f53ffdc07f2ec7e3a92876dc9c42"></a>

### [`0047256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md) → [`004725ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004725ac.md) FUN_004725ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00471c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00471c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471c44.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004725d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md#insn-004725d8) · [`00472634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md#insn-00472634)
- 新版 `00472618`（命令位置の公開資料なし） · `00472674`（命令位置の公開資料なし）

~~~diff
- 004725d8 ["INT_ADD", "register:40f0:8", ["const:4725d8:8", "const:4:8"]]
- 004725d8 ["CALL", null, ["callee:00c58120:8"]]
+ 00472618 ["INT_ADD", "register:40f0:8", ["const:472618:8", "const:4:8"]]
+ 00472618 ["CALL", null, ["callee:00c58120:8"]]
- 004725d8 bytes 9e961f94
+ 00472618 bytes c2961f94
- 00472634 ["INT_ADD", "register:40f0:8", ["const:472634:8", "const:4:8"]]
- 00472634 ["CALL", null, ["callee:00c58120:8"]]
+ 00472674 ["INT_ADD", "register:40f0:8", ["const:472674:8", "const:4:8"]]
+ 00472674 ["CALL", null, ["callee:00c58120:8"]]
- 00472634 bytes 87961f94
+ 00472674 bytes ab961f94
~~~


<a id="compare-e5e5463a72be83f4309670d8b1d95ca7"></a>

### [`00472a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md) → [`00472a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472a4c.md) FUN_00472a4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a5c) · [`00472a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a70) · [`00472a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a78)
- 新版 `00472a9c`（命令位置の公開資料なし） · `00472ab0`（命令位置の公開資料なし） · `00472ab8`（命令位置の公開資料なし）

~~~diff
- 00472a5c ["INT_ADD", "register:40f0:8", ["const:472a5c:8", "const:4:8"]]
- 00472a5c ["CALL", null, ["callee:00c53da0:8"]]
+ 00472a9c ["INT_ADD", "register:40f0:8", ["const:472a9c:8", "const:4:8"]]
+ 00472a9c ["CALL", null, ["callee:00c53da0:8"]]
- 00472a5c bytes a9841f94
+ 00472a9c bytes c1841f94
- 00472a70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472a70 ["INT_ADD", "register:40f0:8", ["const:472a70:8", "const:4:8"]]
- 00472a70 ["CALLIND", null, ["register:0:8"]]
+ 00472ab0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472ab0 ["INT_ADD", "register:40f0:8", ["const:472ab0:8", "const:4:8"]]
+ 00472ab0 ["CALLIND", null, ["register:0:8"]]
- 00472a70 bytes 00013fd6
+ 00472ab0 bytes 00013fd6
- 00472a78 ["INT_ADD", "register:40f0:8", ["const:472a78:8", "const:4:8"]]
- 00472a78 ["CALL", null, ["callee:00c57f50:8"]]
+ 00472ab8 ["INT_ADD", "register:40f0:8", ["const:472ab8:8", "const:4:8"]]
+ 00472ab8 ["CALL", null, ["callee:00c57f50:8"]]
- 00472a78 bytes 02951f94
+ 00472ab8 bytes 26951f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a971fc84a12236fcd6683fa54a931f8a"></a>

### [`00472af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md) → [`00472b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472b38.md) FUN_00472b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b40) · [`00472b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b54) · [`00472b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b5c)
- 新版 `00472b80`（命令位置の公開資料なし） · `00472b94`（命令位置の公開資料なし） · `00472b9c`（命令位置の公開資料なし）

~~~diff
- 00472b40 ["INT_ADD", "register:40f0:8", ["const:472b40:8", "const:4:8"]]
- 00472b40 ["CALL", null, ["callee:00c53da0:8"]]
+ 00472b80 ["INT_ADD", "register:40f0:8", ["const:472b80:8", "const:4:8"]]
+ 00472b80 ["CALL", null, ["callee:00c53da0:8"]]
- 00472b40 bytes 70841f94
+ 00472b80 bytes 88841f94
- 00472b54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472b54 ["INT_ADD", "register:40f0:8", ["const:472b54:8", "const:4:8"]]
- 00472b54 ["CALLIND", null, ["register:0:8"]]
+ 00472b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472b94 ["INT_ADD", "register:40f0:8", ["const:472b94:8", "const:4:8"]]
+ 00472b94 ["CALLIND", null, ["register:0:8"]]
- 00472b54 bytes 00013fd6
+ 00472b94 bytes 00013fd6
- 00472b5c ["INT_ADD", "register:40f0:8", ["const:472b5c:8", "const:4:8"]]
- 00472b5c ["CALL", null, ["callee:00c57f50:8"]]
+ 00472b9c ["INT_ADD", "register:40f0:8", ["const:472b9c:8", "const:4:8"]]
+ 00472b9c ["CALL", null, ["callee:00c57f50:8"]]
- 00472b5c bytes c9941f94
+ 00472b9c bytes ed941f94
~~~


<a id="compare-f1d847a15f80fed05eaa0b86d4ca7ae1"></a>

### [`00472bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md) → [`00472bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bfc.md) FUN_00472bfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 3件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md#insn-00472be0)
- 新版 `00472c20`（命令位置の公開資料なし）

~~~diff
- 00472be0 ["INT_ADD", "register:40f0:8", ["const:472be0:8", "const:4:8"]]
- 00472be0 ["CALL", null, ["callee:00c53d70:8"]]
+ 00472c20 ["INT_ADD", "register:40f0:8", ["const:472c20:8", "const:4:8"]]
+ 00472c20 ["CALL", null, ["callee:00c53d70:8"]]
- 00472be0 bytes 3c841f94
+ 00472c20 bytes 54841f94
~~~


<a id="compare-e4f4006d4db652123534dd86744caa4f"></a>

### [`00472bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md) → [`00472c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472c2c.md) FUN_00472c2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 4件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c40) · [`00472c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c4c) · [`00472c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c70)
- 新版 `00472c80`（命令位置の公開資料なし） · `00472c8c`（命令位置の公開資料なし） · `00472cb0`（命令位置の公開資料なし）

~~~diff
- 00472c40 ["INT_ADD", "register:40f0:8", ["const:472c40:8", "const:4:8"]]
- 00472c40 ["CALL", null, ["callee:00c58120:8"]]
+ 00472c80 ["INT_ADD", "register:40f0:8", ["const:472c80:8", "const:4:8"]]
+ 00472c80 ["CALL", null, ["callee:00c58120:8"]]
- 00472c40 bytes 04951f94
+ 00472c80 bytes 28951f94
- 00472c4c ["INT_ADD", "register:40f0:8", ["const:472c4c:8", "const:4:8"]]
- 00472c4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00472c8c ["INT_ADD", "register:40f0:8", ["const:472c8c:8", "const:4:8"]]
+ 00472c8c ["CALL", null, ["callee:00c57f80:8"]]
- 00472c4c bytes 99941f94
+ 00472c8c bytes bd941f94
- 00472c70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00472c70 ["INT_ADD", "register:40f0:8", ["const:472c70:8", "const:4:8"]]
- 00472c70 ["CALLIND", null, ["register:0:8"]]
+ 00472cb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00472cb0 ["INT_ADD", "register:40f0:8", ["const:472cb0:8", "const:4:8"]]
+ 00472cb0 ["CALLIND", null, ["register:0:8"]]
- 00472c70 bytes 20013fd6
+ 00472cb0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82097b03d999909494322216cdc06627"></a>

### [`00472f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md) → [`00472f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472f78.md) FUN_00472f78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md#insn-00472f54) · [`00472f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md#insn-00472f74)
- 新版 `00472f94`（命令位置の公開資料なし） · `00472fb4`（命令位置の公開資料なし）

~~~diff
- 00472f54 ["INT_ADD", "register:40f0:8", ["const:472f54:8", "const:4:8"]]
- 00472f54 ["CALL", null, ["callee:00c53da0:8"]]
+ 00472f94 ["INT_ADD", "register:40f0:8", ["const:472f94:8", "const:4:8"]]
+ 00472f94 ["CALL", null, ["callee:00c53da0:8"]]
- 00472f54 bytes 6b831f94
+ 00472f94 bytes 83831f94
- 00472f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472f74 ["INT_ADD", "register:40f0:8", ["const:472f74:8", "const:4:8"]]
- 00472f74 ["CALLIND", null, ["register:0:8"]]
+ 00472fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472fb4 ["INT_ADD", "register:40f0:8", ["const:472fb4:8", "const:4:8"]]
+ 00472fb4 ["CALLIND", null, ["register:0:8"]]
- 00472f74 bytes 00013fd6
+ 00472fb4 bytes 00013fd6
~~~


<a id="compare-444582dfa59270e30645485b13f764d4"></a>

### [`00472f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md) → [`00472fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472fc8.md) FUN_00472fc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md#insn-00472fa4) · [`00472fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md#insn-00472fc4)
- 新版 `00472fe4`（命令位置の公開資料なし） · `00473004`（命令位置の公開資料なし）

~~~diff
- 00472fa4 ["INT_ADD", "register:40f0:8", ["const:472fa4:8", "const:4:8"]]
- 00472fa4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00472fe4 ["INT_ADD", "register:40f0:8", ["const:472fe4:8", "const:4:8"]]
+ 00472fe4 ["CALL", null, ["callee:00c53da0:8"]]
- 00472fa4 bytes 57831f94
+ 00472fe4 bytes 6f831f94
- 00472fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472fc4 ["INT_ADD", "register:40f0:8", ["const:472fc4:8", "const:4:8"]]
- 00472fc4 ["CALLIND", null, ["register:0:8"]]
+ 00473004 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473004 ["INT_ADD", "register:40f0:8", ["const:473004:8", "const:4:8"]]
+ 00473004 ["CALLIND", null, ["register:0:8"]]
- 00472fc4 bytes 00013fd6
+ 00473004 bytes 00013fd6
~~~


<a id="compare-7cc2152ce153174969fba5194fd0ce04"></a>

### [`00472fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md) → [`00473018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473018.md) FUN_00473018

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md#insn-00472ff4) · [`00473014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md#insn-00473014)
- 新版 `00473034`（命令位置の公開資料なし） · `00473054`（命令位置の公開資料なし）

~~~diff
- 00472ff4 ["INT_ADD", "register:40f0:8", ["const:472ff4:8", "const:4:8"]]
- 00472ff4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00473034 ["INT_ADD", "register:40f0:8", ["const:473034:8", "const:4:8"]]
+ 00473034 ["CALL", null, ["callee:00c53da0:8"]]
- 00472ff4 bytes 43831f94
+ 00473034 bytes 5b831f94
- 00473014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00473014 ["INT_ADD", "register:40f0:8", ["const:473014:8", "const:4:8"]]
- 00473014 ["CALLIND", null, ["register:0:8"]]
+ 00473054 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473054 ["INT_ADD", "register:40f0:8", ["const:473054:8", "const:4:8"]]
+ 00473054 ["CALLIND", null, ["register:0:8"]]
- 00473014 bytes 00013fd6
+ 00473054 bytes 00013fd6
~~~


<a id="compare-cb30223990d73a601d7a9457f90b848d"></a>

### [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) → [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) FUN_00473580

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`00473394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md) [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`004bc114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md) [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00479624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 33件 [`004733d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004733d4.md) [`004814a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004814a0.md) [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) [`004bc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md) [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00479664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479664.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004735a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-004735a4) · [`00473604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-00473604) · [`00473650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-00473650)
- 新版 `004735e4`（命令位置の公開資料なし） · `00473644`（命令位置の公開資料なし） · `00473690`（命令位置の公開資料なし）

~~~diff
- 004735a4 ["INT_ADD", "register:40f0:8", ["const:4735a4:8", "const:4:8"]]
- 004735a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004735e4 ["INT_ADD", "register:40f0:8", ["const:4735e4:8", "const:4:8"]]
+ 004735e4 ["CALL", null, ["callee:00c57f60:8"]]
- 004735a4 bytes 3b921f94
+ 004735e4 bytes 5f921f94
- 00473604 ["INT_ADD", "register:40f0:8", ["const:473604:8", "const:4:8"]]
- 00473604 ["CALL", null, ["callee:0043bb60:8"]]
+ 00473644 ["INT_ADD", "register:40f0:8", ["const:473644:8", "const:4:8"]]
+ 00473644 ["CALL", null, ["callee:0043bb60:8"]]
- 00473604 bytes 4721ff97
+ 00473644 bytes 4721ff97
- 00473650 ["INT_ADD", "register:40f0:8", ["const:473650:8", "const:4:8"]]
- 00473650 ["CALL", null, ["callee:00440f9c:8"]]
+ 00473690 ["INT_ADD", "register:40f0:8", ["const:473690:8", "const:4:8"]]
+ 00473690 ["CALL", null, ["callee:00440f9c:8"]]
- 00473650 bytes 4336ff97
+ 00473690 bytes 4336ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd9c0e9cd04168f64fd3efa82120effe"></a>

### [`00473e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md) → [`00473eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473eac.md) FUN_00473eac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md#insn-00473e88) · [`00473ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md#insn-00473ea8)
- 新版 `00473ec8`（命令位置の公開資料なし） · `00473ee8`（命令位置の公開資料なし）

~~~diff
- 00473e88 ["INT_ADD", "register:40f0:8", ["const:473e88:8", "const:4:8"]]
- 00473e88 ["CALL", null, ["callee:00c53da0:8"]]
+ 00473ec8 ["INT_ADD", "register:40f0:8", ["const:473ec8:8", "const:4:8"]]
+ 00473ec8 ["CALL", null, ["callee:00c53da0:8"]]
- 00473e88 bytes 9e7f1f94
+ 00473ec8 bytes b67f1f94
- 00473ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00473ea8 ["INT_ADD", "register:40f0:8", ["const:473ea8:8", "const:4:8"]]
- 00473ea8 ["CALLIND", null, ["register:0:8"]]
+ 00473ee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473ee8 ["INT_ADD", "register:40f0:8", ["const:473ee8:8", "const:4:8"]]
+ 00473ee8 ["CALLIND", null, ["register:0:8"]]
- 00473ea8 bytes 00013fd6
+ 00473ee8 bytes 00013fd6
~~~


<a id="compare-eff9ba077de6710558b5e9e36b0e008c"></a>

### [`00473ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md) → [`00473efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473efc.md) FUN_00473efc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473ed8) · [`00473eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473eec) · [`00473f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473f0c)
- 新版 `00473f18`（命令位置の公開資料なし） · `00473f2c`（命令位置の公開資料なし） · `00473f4c`（命令位置の公開資料なし）

~~~diff
- 00473ed8 ["INT_ADD", "register:40f0:8", ["const:473ed8:8", "const:4:8"]]
- 00473ed8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00473f18 ["INT_ADD", "register:40f0:8", ["const:473f18:8", "const:4:8"]]
+ 00473f18 ["CALL", null, ["callee:00c57f80:8"]]
- 00473ed8 bytes f68f1f94
+ 00473f18 bytes 1a901f94
- 00473eec ["INT_ADD", "register:40f0:8", ["const:473eec:8", "const:4:8"]]
- 00473eec ["CALL", null, ["callee:00c53da0:8"]]
+ 00473f2c ["INT_ADD", "register:40f0:8", ["const:473f2c:8", "const:4:8"]]
+ 00473f2c ["CALL", null, ["callee:00c53da0:8"]]
- 00473eec bytes 857f1f94
+ 00473f2c bytes 9d7f1f94
- 00473f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00473f0c ["INT_ADD", "register:40f0:8", ["const:473f0c:8", "const:4:8"]]
- 00473f0c ["CALLIND", null, ["register:0:8"]]
+ 00473f4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f4c ["INT_ADD", "register:40f0:8", ["const:473f4c:8", "const:4:8"]]
+ 00473f4c ["CALLIND", null, ["register:0:8"]]
- 00473f0c bytes 00013fd6
+ 00473f4c bytes 00013fd6
~~~


<a id="compare-f65eded171a170f3d78fadc13ca47b27"></a>

### [`00473f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md) → [`00473f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473f60.md) FUN_00473f60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md#insn-00473f3c) · [`00473f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md#insn-00473f5c)
- 新版 `00473f7c`（命令位置の公開資料なし） · `00473f9c`（命令位置の公開資料なし）

~~~diff
- 00473f3c ["INT_ADD", "register:40f0:8", ["const:473f3c:8", "const:4:8"]]
- 00473f3c ["CALL", null, ["callee:00c53da0:8"]]
+ 00473f7c ["INT_ADD", "register:40f0:8", ["const:473f7c:8", "const:4:8"]]
+ 00473f7c ["CALL", null, ["callee:00c53da0:8"]]
- 00473f3c bytes 717f1f94
+ 00473f7c bytes 897f1f94
- 00473f5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00473f5c ["INT_ADD", "register:40f0:8", ["const:473f5c:8", "const:4:8"]]
- 00473f5c ["CALLIND", null, ["register:0:8"]]
+ 00473f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f9c ["INT_ADD", "register:40f0:8", ["const:473f9c:8", "const:4:8"]]
+ 00473f9c ["CALLIND", null, ["register:0:8"]]
- 00473f5c bytes 00013fd6
+ 00473f9c bytes 00013fd6
~~~


<a id="compare-26245da9af151ba5bb720a3d08034357"></a>

### [`00473f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md) → [`00473fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473fb0.md) FUN_00473fb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md#insn-00473f8c) · [`00473fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md#insn-00473fac)
- 新版 `00473fcc`（命令位置の公開資料なし） · `00473fec`（命令位置の公開資料なし）

~~~diff
- 00473f8c ["INT_ADD", "register:40f0:8", ["const:473f8c:8", "const:4:8"]]
- 00473f8c ["CALL", null, ["callee:00c53da0:8"]]
+ 00473fcc ["INT_ADD", "register:40f0:8", ["const:473fcc:8", "const:4:8"]]
+ 00473fcc ["CALL", null, ["callee:00c53da0:8"]]
- 00473f8c bytes 5d7f1f94
+ 00473fcc bytes 757f1f94
- 00473fac ["COPY", "register:0:8", ["register:4040:8"]]
- 00473fac ["INT_ADD", "register:40f0:8", ["const:473fac:8", "const:4:8"]]
- 00473fac ["CALLIND", null, ["register:0:8"]]
+ 00473fec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473fec ["INT_ADD", "register:40f0:8", ["const:473fec:8", "const:4:8"]]
+ 00473fec ["CALLIND", null, ["register:0:8"]]
- 00473fac bytes 00013fd6
+ 00473fec bytes 00013fd6
~~~


<a id="compare-5919f713d09a10ada91c6858f533a0f6"></a>

### [`00473fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md) → [`00474000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474000.md) FUN_00474000

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md#insn-00473fdc) · [`00473ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md#insn-00473ffc)
- 新版 `0047401c`（命令位置の公開資料なし） · `0047403c`（命令位置の公開資料なし）

~~~diff
- 00473fdc ["INT_ADD", "register:40f0:8", ["const:473fdc:8", "const:4:8"]]
- 00473fdc ["CALL", null, ["callee:00c53da0:8"]]
+ 0047401c ["INT_ADD", "register:40f0:8", ["const:47401c:8", "const:4:8"]]
+ 0047401c ["CALL", null, ["callee:00c53da0:8"]]
- 00473fdc bytes 497f1f94
+ 0047401c bytes 617f1f94
- 00473ffc ["COPY", "register:0:8", ["register:4040:8"]]
- 00473ffc ["INT_ADD", "register:40f0:8", ["const:473ffc:8", "const:4:8"]]
- 00473ffc ["CALLIND", null, ["register:0:8"]]
+ 0047403c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047403c ["INT_ADD", "register:40f0:8", ["const:47403c:8", "const:4:8"]]
+ 0047403c ["CALLIND", null, ["register:0:8"]]
- 00473ffc bytes 00013fd6
+ 0047403c bytes 00013fd6
~~~


<a id="compare-969ae6e9bb1b2be3d17b8b8eb1191d3a"></a>

### [`00474010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md) → [`00474050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474050.md) FUN_00474050

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 6件 [`0047a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a810.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 6件 [`0047a850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a850.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474048) · [`00474054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474054) · [`00474060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474060)
- 新版 `00474088`（命令位置の公開資料なし） · `00474094`（命令位置の公開資料なし） · `004740a0`（命令位置の公開資料なし）

~~~diff
- 00474048 ["INT_ADD", "register:40f0:8", ["const:474048:8", "const:4:8"]]
- 00474048 ["CALL", null, ["callee:00c581b0:8"]]
+ 00474088 ["INT_ADD", "register:40f0:8", ["const:474088:8", "const:4:8"]]
+ 00474088 ["CALL", null, ["callee:00c581b0:8"]]
- 00474048 bytes 26901f94
+ 00474088 bytes 4a901f94
- 00474054 ["INT_ADD", "register:40f0:8", ["const:474054:8", "const:4:8"]]
- 00474054 ["CALL", null, ["callee:0047a850:8"]]
+ 00474094 ["INT_ADD", "register:40f0:8", ["const:474094:8", "const:4:8"]]
+ 00474094 ["CALL", null, ["callee:0047a850:8"]]
- 00474054 bytes ef190094
+ 00474094 bytes ef190094
- 00474060 ["INT_ADD", "register:40f0:8", ["const:474060:8", "const:4:8"]]
- 00474060 ["CALL", null, ["callee:00c581c0:8"]]
+ 004740a0 ["INT_ADD", "register:40f0:8", ["const:4740a0:8", "const:4:8"]]
+ 004740a0 ["CALL", null, ["callee:00c581c0:8"]]
- 00474060 bytes 24901f94
+ 004740a0 bytes 48901f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f0ea1b9062daf64161ac6c26370b61"></a>

### [`00474148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md) → [`00474188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474188.md) FUN_00474188

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md#insn-00474164) · [`00474184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md#insn-00474184)
- 新版 `004741a4`（命令位置の公開資料なし） · `004741c4`（命令位置の公開資料なし）

~~~diff
- 00474164 ["INT_ADD", "register:40f0:8", ["const:474164:8", "const:4:8"]]
- 00474164 ["CALL", null, ["callee:00c53da0:8"]]
+ 004741a4 ["INT_ADD", "register:40f0:8", ["const:4741a4:8", "const:4:8"]]
+ 004741a4 ["CALL", null, ["callee:00c53da0:8"]]
- 00474164 bytes e77e1f94
+ 004741a4 bytes ff7e1f94
- 00474184 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474184 ["INT_ADD", "register:40f0:8", ["const:474184:8", "const:4:8"]]
- 00474184 ["CALLIND", null, ["register:0:8"]]
+ 004741c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004741c4 ["INT_ADD", "register:40f0:8", ["const:4741c4:8", "const:4:8"]]
+ 004741c4 ["CALLIND", null, ["register:0:8"]]
- 00474184 bytes 00013fd6
+ 004741c4 bytes 00013fd6
~~~


<a id="compare-427665bca2b5fb1ad83adf5a9edd134b"></a>

### [`00474af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md) → [`00474b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474b38.md) FUN_00474b38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474b6c.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md#insn-00474b0c) · [`00474b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md#insn-00474b14)
- 新版 `00474b4c`（命令位置の公開資料なし） · `00474b54`（命令位置の公開資料なし）

~~~diff
- 00474b0c ["INT_ADD", "register:40f0:8", ["const:474b0c:8", "const:4:8"]]
- 00474b0c ["CALL", null, ["callee:00c581a0:8"]]
+ 00474b4c ["INT_ADD", "register:40f0:8", ["const:474b4c:8", "const:4:8"]]
+ 00474b4c ["CALL", null, ["callee:00c581a0:8"]]
- 00474b0c bytes 718d1f94
+ 00474b4c bytes 958d1f94
- 00474b14 ["INT_ADD", "register:40f0:8", ["const:474b14:8", "const:4:8"]]
- 00474b14 ["CALL", null, ["callee:00c57f30:8"]]
+ 00474b54 ["INT_ADD", "register:40f0:8", ["const:474b54:8", "const:4:8"]]
+ 00474b54 ["CALL", null, ["callee:00c57f30:8"]]
- 00474b14 bytes d38c1f94
+ 00474b54 bytes f78c1f94
~~~


<a id="compare-74092ce8a7b808d42c07ea573b50f122"></a>

### [`00474b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md) → [`00474b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474b6c.md) FUN_00474b6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00474af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00474b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474b38.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474ba8) · [`00474bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474bbc) · [`00474bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474bc4)
- 新版 `00474be8`（命令位置の公開資料なし） · `00474bfc`（命令位置の公開資料なし） · `00474c04`（命令位置の公開資料なし）

~~~diff
- 00474ba8 ["INT_ADD", "register:40f0:8", ["const:474ba8:8", "const:4:8"]]
- 00474ba8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00474be8 ["INT_ADD", "register:40f0:8", ["const:474be8:8", "const:4:8"]]
+ 00474be8 ["CALL", null, ["callee:00c53da0:8"]]
- 00474ba8 bytes 567c1f94
+ 00474be8 bytes 6e7c1f94
- 00474bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00474bbc ["INT_ADD", "register:40f0:8", ["const:474bbc:8", "const:4:8"]]
- 00474bbc ["CALLIND", null, ["register:0:8"]]
+ 00474bfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474bfc ["INT_ADD", "register:40f0:8", ["const:474bfc:8", "const:4:8"]]
+ 00474bfc ["CALLIND", null, ["register:0:8"]]
- 00474bbc bytes 00013fd6
+ 00474bfc bytes 00013fd6
- 00474bc4 ["INT_ADD", "register:40f0:8", ["const:474bc4:8", "const:4:8"]]
- 00474bc4 ["CALL", null, ["callee:00c57f50:8"]]
+ 00474c04 ["INT_ADD", "register:40f0:8", ["const:474c04:8", "const:4:8"]]
+ 00474c04 ["CALL", null, ["callee:00c57f50:8"]]
- 00474bc4 bytes af8c1f94
+ 00474c04 bytes d38c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d044d81f10108a9181a9be72f189a871"></a>

### [`00474cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md) → [`00474d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474d3c.md) FUN_00474d3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474d70.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md#insn-00474d10) · [`00474d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md#insn-00474d18)
- 新版 `00474d50`（命令位置の公開資料なし） · `00474d58`（命令位置の公開資料なし）

~~~diff
- 00474d10 ["INT_ADD", "register:40f0:8", ["const:474d10:8", "const:4:8"]]
- 00474d10 ["CALL", null, ["callee:00c581a0:8"]]
+ 00474d50 ["INT_ADD", "register:40f0:8", ["const:474d50:8", "const:4:8"]]
+ 00474d50 ["CALL", null, ["callee:00c581a0:8"]]
- 00474d10 bytes f08c1f94
+ 00474d50 bytes 148d1f94
- 00474d18 ["INT_ADD", "register:40f0:8", ["const:474d18:8", "const:4:8"]]
- 00474d18 ["CALL", null, ["callee:00c57f30:8"]]
+ 00474d58 ["INT_ADD", "register:40f0:8", ["const:474d58:8", "const:4:8"]]
+ 00474d58 ["CALL", null, ["callee:00c57f30:8"]]
- 00474d18 bytes 528c1f94
+ 00474d58 bytes 768c1f94
~~~


<a id="compare-579ffd28113356c2001f4dd79ff405d3"></a>

### [`00474d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md) → [`00474d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474d70.md) FUN_00474d70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00474cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00474d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474d3c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474db4) · [`00474dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474dc8) · [`00474dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474dd0)
- 新版 `00474df4`（命令位置の公開資料なし） · `00474e08`（命令位置の公開資料なし） · `00474e10`（命令位置の公開資料なし）

~~~diff
- 00474db4 ["INT_ADD", "register:40f0:8", ["const:474db4:8", "const:4:8"]]
- 00474db4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00474df4 ["INT_ADD", "register:40f0:8", ["const:474df4:8", "const:4:8"]]
+ 00474df4 ["CALL", null, ["callee:00c53da0:8"]]
- 00474db4 bytes d37b1f94
+ 00474df4 bytes eb7b1f94
- 00474dc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474dc8 ["INT_ADD", "register:40f0:8", ["const:474dc8:8", "const:4:8"]]
- 00474dc8 ["CALLIND", null, ["register:0:8"]]
+ 00474e08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474e08 ["INT_ADD", "register:40f0:8", ["const:474e08:8", "const:4:8"]]
+ 00474e08 ["CALLIND", null, ["register:0:8"]]
- 00474dc8 bytes 00013fd6
+ 00474e08 bytes 00013fd6
- 00474dd0 ["INT_ADD", "register:40f0:8", ["const:474dd0:8", "const:4:8"]]
- 00474dd0 ["CALL", null, ["callee:00c57f50:8"]]
+ 00474e10 ["INT_ADD", "register:40f0:8", ["const:474e10:8", "const:4:8"]]
+ 00474e10 ["CALL", null, ["callee:00c57f50:8"]]
- 00474dd0 bytes 2c8c1f94
+ 00474e10 bytes 508c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f2f8d31bab996482aa9c5a461b56855"></a>

### [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) → [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) FUN_00474f08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00475388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md) [`00475510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md) [`0047569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00473068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473068.md) [`004758c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758c0.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004753c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004753c8.md) [`00475550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475550.md) [`004756dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004756dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474f60) · [`00474fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474fa4) · [`00474fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474fb4)
- 新版 `00474fa0`（命令位置の公開資料なし） · `00474fe4`（命令位置の公開資料なし） · `00474ff4`（命令位置の公開資料なし）

~~~diff
- 00474f60 ["INT_ADD", "register:40f0:8", ["const:474f60:8", "const:4:8"]]
- 00474f60 ["CALL", null, ["callee:00c58010:8"]]
+ 00474fa0 ["INT_ADD", "register:40f0:8", ["const:474fa0:8", "const:4:8"]]
+ 00474fa0 ["CALL", null, ["callee:00c58010:8"]]
- 00474f60 bytes f88b1f94
+ 00474fa0 bytes 1c8c1f94
- 00474fa4 ["INT_ADD", "register:40f0:8", ["const:474fa4:8", "const:4:8"]]
- 00474fa4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00474fe4 ["INT_ADD", "register:40f0:8", ["const:474fe4:8", "const:4:8"]]
+ 00474fe4 ["CALL", null, ["callee:00c57f60:8"]]
- 00474fa4 bytes bb8b1f94
+ 00474fe4 bytes df8b1f94
- 00474fb4 ["INT_ADD", "register:40f0:8", ["const:474fb4:8", "const:4:8"]]
- 00474fb4 ["CALL", null, ["callee:004753c8:8"]]
+ 00474ff4 ["INT_ADD", "register:40f0:8", ["const:474ff4:8", "const:4:8"]]
+ 00474ff4 ["CALL", null, ["callee:004753c8:8"]]
- 00474fb4 bytes f5000094
+ 00474ff4 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c221045dcfb63fe895e5dba9f624f10"></a>

### [`00475388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md) → [`004753c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004753c8.md) FUN_004753c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004753f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-004753f0) · [`00475428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-00475428) · [`004754d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-004754d8)
- 新版 `00475430`（命令位置の公開資料なし） · `00475468`（命令位置の公開資料なし） · `00475518`（命令位置の公開資料なし）

~~~diff
- 004753f0 ["INT_ADD", "register:40f0:8", ["const:4753f0:8", "const:4:8"]]
- 004753f0 ["CALL", null, ["callee:00c58010:8"]]
+ 00475430 ["INT_ADD", "register:40f0:8", ["const:475430:8", "const:4:8"]]
+ 00475430 ["CALL", null, ["callee:00c58010:8"]]
- 004753f0 bytes d48a1f94
+ 00475430 bytes f88a1f94
- 00475428 ["INT_ADD", "register:40f0:8", ["const:475428:8", "const:4:8"]]
- 00475428 ["CALL", null, ["callee:00c57f60:8"]]
+ 00475468 ["INT_ADD", "register:40f0:8", ["const:475468:8", "const:4:8"]]
+ 00475468 ["CALL", null, ["callee:00c57f60:8"]]
- 00475428 bytes 9a8a1f94
+ 00475468 bytes be8a1f94
- 004754d8 ["INT_ADD", "register:40f0:8", ["const:4754d8:8", "const:4:8"]]
- 004754d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00475518 ["INT_ADD", "register:40f0:8", ["const:475518:8", "const:4:8"]]
+ 00475518 ["CALL", null, ["callee:00c57f80:8"]]
- 004754d8 bytes 768a1f94
+ 00475518 bytes 9a8a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6751258812feb478b5bb68a650d6581"></a>

### [`00475510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md) → [`00475550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475550.md) FUN_00475550

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-00475580) · [`004755b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-004755b8) · [`00475668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-00475668)
- 新版 `004755c0`（命令位置の公開資料なし） · `004755f8`（命令位置の公開資料なし） · `004756a8`（命令位置の公開資料なし）

~~~diff
- 00475580 ["INT_ADD", "register:40f0:8", ["const:475580:8", "const:4:8"]]
- 00475580 ["CALL", null, ["callee:00c58010:8"]]
+ 004755c0 ["INT_ADD", "register:40f0:8", ["const:4755c0:8", "const:4:8"]]
+ 004755c0 ["CALL", null, ["callee:00c58010:8"]]
- 00475580 bytes 708a1f94
+ 004755c0 bytes 948a1f94
- 004755b8 ["INT_ADD", "register:40f0:8", ["const:4755b8:8", "const:4:8"]]
- 004755b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004755f8 ["INT_ADD", "register:40f0:8", ["const:4755f8:8", "const:4:8"]]
+ 004755f8 ["CALL", null, ["callee:00c57f60:8"]]
- 004755b8 bytes 368a1f94
+ 004755f8 bytes 5a8a1f94
- 00475668 ["INT_ADD", "register:40f0:8", ["const:475668:8", "const:4:8"]]
- 00475668 ["CALL", null, ["callee:00c57f80:8"]]
+ 004756a8 ["INT_ADD", "register:40f0:8", ["const:4756a8:8", "const:4:8"]]
+ 004756a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00475668 bytes 128a1f94
+ 004756a8 bytes 368a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d07fe125b08c626e63342deaa41bcd3"></a>

### [`0047569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md) → [`004756dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004756dc.md) FUN_004756dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047570c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-0047570c) · [`00475744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-00475744) · [`004757f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-004757f4)
- 新版 `0047574c`（命令位置の公開資料なし） · `00475784`（命令位置の公開資料なし） · `00475834`（命令位置の公開資料なし）

~~~diff
- 0047570c ["INT_ADD", "register:40f0:8", ["const:47570c:8", "const:4:8"]]
- 0047570c ["CALL", null, ["callee:00c58010:8"]]
+ 0047574c ["INT_ADD", "register:40f0:8", ["const:47574c:8", "const:4:8"]]
+ 0047574c ["CALL", null, ["callee:00c58010:8"]]
- 0047570c bytes 0d8a1f94
+ 0047574c bytes 318a1f94
- 00475744 ["INT_ADD", "register:40f0:8", ["const:475744:8", "const:4:8"]]
- 00475744 ["CALL", null, ["callee:00c57f60:8"]]
+ 00475784 ["INT_ADD", "register:40f0:8", ["const:475784:8", "const:4:8"]]
+ 00475784 ["CALL", null, ["callee:00c57f60:8"]]
- 00475744 bytes d3891f94
+ 00475784 bytes f7891f94
- 004757f4 ["INT_ADD", "register:40f0:8", ["const:4757f4:8", "const:4:8"]]
- 004757f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00475834 ["INT_ADD", "register:40f0:8", ["const:475834:8", "const:4:8"]]
+ 00475834 ["CALL", null, ["callee:00c57f80:8"]]
- 004757f4 bytes af891f94
+ 00475834 bytes d3891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92f0c46cab860908e31c85978aee9c2"></a>

### [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) → [`004758c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758c0.md) FUN_004758c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) [`00475b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) [`00475b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475b68.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004758c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758c0) · [`004758e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758e0) · [`004758f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758f4)
- 新版 `00475900`（命令位置の公開資料なし） · `00475920`（命令位置の公開資料なし） · `00475934`（命令位置の公開資料なし）

~~~diff
- 004758c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004758c0 ["INT_ADD", "register:40f0:8", ["const:4758c0:8", "const:4:8"]]
- 004758c0 ["CALLIND", null, ["register:0:8"]]
+ 00475900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00475900 ["INT_ADD", "register:40f0:8", ["const:475900:8", "const:4:8"]]
+ 00475900 ["CALLIND", null, ["register:0:8"]]
- 004758c0 bytes 00013fd6
+ 00475900 bytes 00013fd6
- 004758e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004758e0 ["INT_ADD", "register:40f0:8", ["const:4758e0:8", "const:4:8"]]
- 004758e0 ["CALLIND", null, ["register:0:8"]]
+ 00475920 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00475920 ["INT_ADD", "register:40f0:8", ["const:475920:8", "const:4:8"]]
+ 00475920 ["CALLIND", null, ["register:0:8"]]
- 004758e0 bytes 20013fd6
+ 00475920 bytes 20013fd6
- 004758f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004758f4 ["INT_ADD", "register:40f0:8", ["const:4758f4:8", "const:4:8"]]
- 004758f4 ["CALLIND", null, ["register:0:8"]]
+ 00475934 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00475934 ["INT_ADD", "register:40f0:8", ["const:475934:8", "const:4:8"]]
+ 00475934 ["CALLIND", null, ["register:0:8"]]
- 004758f4 bytes 20013fd6
+ 00475934 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40829fde45dd13f0f0f3775bf4ea256c"></a>

### [`00475b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md) → [`00475b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475b68.md) FUN_00475b68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) · 呼出先 8件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`004758c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758c0.md) · 呼出先 8件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b74) · [`00475b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b80) · [`00475b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b94)
- 新版 `00475bb4`（命令位置の公開資料なし） · `00475bc0`（命令位置の公開資料なし） · `00475bd4`（命令位置の公開資料なし）

~~~diff
- 00475b74 ["INT_ADD", "register:40f0:8", ["const:475b74:8", "const:4:8"]]
- 00475b74 ["CALL", null, ["callee:00c53d70:8"]]
+ 00475bb4 ["INT_ADD", "register:40f0:8", ["const:475bb4:8", "const:4:8"]]
+ 00475bb4 ["CALL", null, ["callee:00c53d70:8"]]
- 00475b74 bytes 57781f94
+ 00475bb4 bytes 6f781f94
- 00475b80 ["INT_ADD", "register:40f0:8", ["const:475b80:8", "const:4:8"]]
- 00475b80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00475bc0 ["INT_ADD", "register:40f0:8", ["const:475bc0:8", "const:4:8"]]
+ 00475bc0 ["CALL", null, ["callee:00c53da0:8"]]
- 00475b80 bytes 60781f94
+ 00475bc0 bytes 78781f94
- 00475b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00475b94 ["INT_ADD", "register:40f0:8", ["const:475b94:8", "const:4:8"]]
- 00475b94 ["CALLIND", null, ["register:0:8"]]
+ 00475bd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00475bd4 ["INT_ADD", "register:40f0:8", ["const:475bd4:8", "const:4:8"]]
+ 00475bd4 ["CALLIND", null, ["register:0:8"]]
- 00475b94 bytes 00013fd6
+ 00475bd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29246847035ba10ca21ba7ca41093b4f"></a>

### [`00476154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md) → [`00476194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476194.md) FUN_00476194

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047617c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md#insn-0047617c) · [`00476184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md#insn-00476184)
- 新版 `004761bc`（命令位置の公開資料なし） · `004761c4`（命令位置の公開資料なし）

~~~diff
- 0047617c ["INT_ADD", "register:40f0:8", ["const:47617c:8", "const:4:8"]]
- 0047617c ["CALL", null, ["callee:00c58220:8"]]
+ 004761bc ["INT_ADD", "register:40f0:8", ["const:4761bc:8", "const:4:8"]]
+ 004761bc ["CALL", null, ["callee:00c58220:8"]]
- 0047617c bytes f5871f94
+ 004761bc bytes 19881f94
- 00476184 ["INT_ADD", "register:40f0:8", ["const:476184:8", "const:4:8"]]
- 00476184 ["CALL", null, ["callee:00c57f80:8"]]
+ 004761c4 ["INT_ADD", "register:40f0:8", ["const:4761c4:8", "const:4:8"]]
+ 004761c4 ["CALL", null, ["callee:00c57f80:8"]]
- 00476184 bytes 4b871f94
+ 004761c4 bytes 6f871f94
~~~


<a id="compare-f0d2b70a810a4eb594908ed8cc1e95bf"></a>

### [`00476538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md) → [`00476578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476578.md) FUN_00476578

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md#insn-00476554) · [`00476574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md#insn-00476574)
- 新版 `00476594`（命令位置の公開資料なし） · `004765b4`（命令位置の公開資料なし）

~~~diff
- 00476554 ["INT_ADD", "register:40f0:8", ["const:476554:8", "const:4:8"]]
- 00476554 ["CALL", null, ["callee:00c53da0:8"]]
+ 00476594 ["INT_ADD", "register:40f0:8", ["const:476594:8", "const:4:8"]]
+ 00476594 ["CALL", null, ["callee:00c53da0:8"]]
- 00476554 bytes eb751f94
+ 00476594 bytes 03761f94
- 00476574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476574 ["INT_ADD", "register:40f0:8", ["const:476574:8", "const:4:8"]]
- 00476574 ["CALLIND", null, ["register:0:8"]]
+ 004765b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004765b4 ["INT_ADD", "register:40f0:8", ["const:4765b4:8", "const:4:8"]]
+ 004765b4 ["CALLIND", null, ["register:0:8"]]
- 00476574 bytes 00013fd6
+ 004765b4 bytes 00013fd6
~~~


<a id="compare-33d63eafebcc1b23d5e87cdea53e6f13"></a>

### [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md) → [`00478188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478188.md) FUN_00478188

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 8件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 2件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) · 呼出先 8件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-00478184) · [`00478190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-00478190) · [`004781a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-004781a4)
- 新版 `004781c4`（命令位置の公開資料なし） · `004781d0`（命令位置の公開資料なし） · `004781e4`（命令位置の公開資料なし）

~~~diff
- 00478184 ["INT_ADD", "register:40f0:8", ["const:478184:8", "const:4:8"]]
- 00478184 ["CALL", null, ["callee:00c581b0:8"]]
+ 004781c4 ["INT_ADD", "register:40f0:8", ["const:4781c4:8", "const:4:8"]]
+ 004781c4 ["CALL", null, ["callee:00c581b0:8"]]
- 00478184 bytes d77f1f94
+ 004781c4 bytes fb7f1f94
- 00478190 ["INT_ADD", "register:40f0:8", ["const:478190:8", "const:4:8"]]
- 00478190 ["CALL", null, ["callee:00c58570:8"]]
+ 004781d0 ["INT_ADD", "register:40f0:8", ["const:4781d0:8", "const:4:8"]]
+ 004781d0 ["CALL", null, ["callee:00c58570:8"]]
- 00478190 bytes c4801f94
+ 004781d0 bytes e8801f94
- 004781a4 ["INT_ADD", "register:40f0:8", ["const:4781a4:8", "const:4:8"]]
- 004781a4 ["CALL", null, ["callee:00c583c0:8"]]
+ 004781e4 ["INT_ADD", "register:40f0:8", ["const:4781e4:8", "const:4:8"]]
+ 004781e4 ["CALL", null, ["callee:00c583c0:8"]]
- 004781a4 bytes 53801f94
+ 004781e4 bytes 77801f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08bee6e129f2496a27935853acc7034e"></a>

### [`00478274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md) → [`004782b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/004782b4.md) FUN_004782b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md#insn-00478290) · [`004782b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md#insn-004782b0)
- 新版 `004782d0`（命令位置の公開資料なし） · `004782f0`（命令位置の公開資料なし）

~~~diff
- 00478290 ["INT_ADD", "register:40f0:8", ["const:478290:8", "const:4:8"]]
- 00478290 ["CALL", null, ["callee:00c53da0:8"]]
+ 004782d0 ["INT_ADD", "register:40f0:8", ["const:4782d0:8", "const:4:8"]]
+ 004782d0 ["CALL", null, ["callee:00c53da0:8"]]
- 00478290 bytes 9c6e1f94
+ 004782d0 bytes b46e1f94
- 004782b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004782b0 ["INT_ADD", "register:40f0:8", ["const:4782b0:8", "const:4:8"]]
- 004782b0 ["CALLIND", null, ["register:0:8"]]
+ 004782f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004782f0 ["INT_ADD", "register:40f0:8", ["const:4782f0:8", "const:4:8"]]
+ 004782f0 ["CALLIND", null, ["register:0:8"]]
- 004782b0 bytes 00013fd6
+ 004782f0 bytes 00013fd6
~~~


<a id="compare-73a0fb782cdd3fd4460ac554bff2970a"></a>

### [`004782c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md) → [`00478304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478304.md) FUN_00478304

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004782e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md#insn-004782e0) · [`00478300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md#insn-00478300)
- 新版 `00478320`（命令位置の公開資料なし） · `00478340`（命令位置の公開資料なし）

~~~diff
- 004782e0 ["INT_ADD", "register:40f0:8", ["const:4782e0:8", "const:4:8"]]
- 004782e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00478320 ["INT_ADD", "register:40f0:8", ["const:478320:8", "const:4:8"]]
+ 00478320 ["CALL", null, ["callee:00c53da0:8"]]
- 004782e0 bytes 886e1f94
+ 00478320 bytes a06e1f94
- 00478300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00478300 ["INT_ADD", "register:40f0:8", ["const:478300:8", "const:4:8"]]
- 00478300 ["CALLIND", null, ["register:0:8"]]
+ 00478340 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00478340 ["INT_ADD", "register:40f0:8", ["const:478340:8", "const:4:8"]]
+ 00478340 ["CALLIND", null, ["register:0:8"]]
- 00478300 bytes 00013fd6
+ 00478340 bytes 00013fd6
~~~


<a id="compare-6e88ca7d4af9298747e56e38a4c7de5b"></a>

### [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) → [`00478c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478c54.md) FUN_00478c54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`00478b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b90.md) [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 2件 [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`00478bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478bd0.md) [`00478c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478c54.md) [`0048cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cef8.md) · 呼出先 2件 [`00478c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478c54.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md#insn-00478c34) · [`00478c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md#insn-00478c40)
- 新版 `00478c74`（命令位置の公開資料なし） · `00478c80`（命令位置の公開資料なし）

~~~diff
- 00478c34 ["INT_ADD", "register:40f0:8", ["const:478c34:8", "const:4:8"]]
- 00478c34 ["CALL", null, ["local:b0:8"]]
+ 00478c74 ["INT_ADD", "register:40f0:8", ["const:478c74:8", "const:4:8"]]
+ 00478c74 ["CALL", null, ["local:b0:8"]]
- 00478c34 bytes f8ffff97
+ 00478c74 bytes f8ffff97
- 00478c40 ["INT_ADD", "register:40f0:8", ["const:478c40:8", "const:4:8"]]
- 00478c40 ["CALL", null, ["local:b0:8"]]
+ 00478c80 ["INT_ADD", "register:40f0:8", ["const:478c80:8", "const:4:8"]]
+ 00478c80 ["CALL", null, ["local:b0:8"]]
- 00478c40 bytes f5ffff97
+ 00478c80 bytes f5ffff97
~~~


<a id="compare-24a0c01e0ef9a14b15e48b11b7866456"></a>

### [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) → [`00478d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478d04.md) FUN_00478d04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00479184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md) [`0047930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md) [`00479498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00475de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475de0.md) [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004791c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004791c4.md) [`0047934c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/0047934c.md) [`004794d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004794d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478d5c) · [`00478da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478da0) · [`00478db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478db0)
- 新版 `00478d9c`（命令位置の公開資料なし） · `00478de0`（命令位置の公開資料なし） · `00478df0`（命令位置の公開資料なし）

~~~diff
- 00478d5c ["INT_ADD", "register:40f0:8", ["const:478d5c:8", "const:4:8"]]
- 00478d5c ["CALL", null, ["callee:00c58010:8"]]
+ 00478d9c ["INT_ADD", "register:40f0:8", ["const:478d9c:8", "const:4:8"]]
+ 00478d9c ["CALL", null, ["callee:00c58010:8"]]
- 00478d5c bytes 797c1f94
+ 00478d9c bytes 9d7c1f94
- 00478da0 ["INT_ADD", "register:40f0:8", ["const:478da0:8", "const:4:8"]]
- 00478da0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00478de0 ["INT_ADD", "register:40f0:8", ["const:478de0:8", "const:4:8"]]
+ 00478de0 ["CALL", null, ["callee:00c57f60:8"]]
- 00478da0 bytes 3c7c1f94
+ 00478de0 bytes 607c1f94
- 00478db0 ["INT_ADD", "register:40f0:8", ["const:478db0:8", "const:4:8"]]
- 00478db0 ["CALL", null, ["callee:004791c4:8"]]
+ 00478df0 ["INT_ADD", "register:40f0:8", ["const:478df0:8", "const:4:8"]]
+ 00478df0 ["CALL", null, ["callee:004791c4:8"]]
- 00478db0 bytes f5000094
+ 00478df0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-031898edb7d698aeff4690b2aaa528ff"></a>

### [`00479184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md) → [`004791c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004791c4.md) FUN_004791c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00478d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478d04.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004791ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-004791ec) · [`00479224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-00479224) · [`004792d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-004792d4)
- 新版 `0047922c`（命令位置の公開資料なし） · `00479264`（命令位置の公開資料なし） · `00479314`（命令位置の公開資料なし）

~~~diff
- 004791ec ["INT_ADD", "register:40f0:8", ["const:4791ec:8", "const:4:8"]]
- 004791ec ["CALL", null, ["callee:00c58010:8"]]
+ 0047922c ["INT_ADD", "register:40f0:8", ["const:47922c:8", "const:4:8"]]
+ 0047922c ["CALL", null, ["callee:00c58010:8"]]
- 004791ec bytes 557b1f94
+ 0047922c bytes 797b1f94
- 00479224 ["INT_ADD", "register:40f0:8", ["const:479224:8", "const:4:8"]]
- 00479224 ["CALL", null, ["callee:00c57f60:8"]]
+ 00479264 ["INT_ADD", "register:40f0:8", ["const:479264:8", "const:4:8"]]
+ 00479264 ["CALL", null, ["callee:00c57f60:8"]]
- 00479224 bytes 1b7b1f94
+ 00479264 bytes 3f7b1f94
- 004792d4 ["INT_ADD", "register:40f0:8", ["const:4792d4:8", "const:4:8"]]
- 004792d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00479314 ["INT_ADD", "register:40f0:8", ["const:479314:8", "const:4:8"]]
+ 00479314 ["CALL", null, ["callee:00c57f80:8"]]
- 004792d4 bytes f77a1f94
+ 00479314 bytes 1b7b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56011e063117dfdee3c0a1862ccdf2a7"></a>

### [`0047930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md) → [`0047934c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/0047934c.md) FUN_0047934c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00478d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478d04.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-0047937c) · [`004793b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-004793b4) · [`00479464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-00479464)
- 新版 `004793bc`（命令位置の公開資料なし） · `004793f4`（命令位置の公開資料なし） · `004794a4`（命令位置の公開資料なし）

~~~diff
- 0047937c ["INT_ADD", "register:40f0:8", ["const:47937c:8", "const:4:8"]]
- 0047937c ["CALL", null, ["callee:00c58010:8"]]
+ 004793bc ["INT_ADD", "register:40f0:8", ["const:4793bc:8", "const:4:8"]]
+ 004793bc ["CALL", null, ["callee:00c58010:8"]]
- 0047937c bytes f17a1f94
+ 004793bc bytes 157b1f94
- 004793b4 ["INT_ADD", "register:40f0:8", ["const:4793b4:8", "const:4:8"]]
- 004793b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004793f4 ["INT_ADD", "register:40f0:8", ["const:4793f4:8", "const:4:8"]]
+ 004793f4 ["CALL", null, ["callee:00c57f60:8"]]
- 004793b4 bytes b77a1f94
+ 004793f4 bytes db7a1f94
- 00479464 ["INT_ADD", "register:40f0:8", ["const:479464:8", "const:4:8"]]
- 00479464 ["CALL", null, ["callee:00c57f80:8"]]
+ 004794a4 ["INT_ADD", "register:40f0:8", ["const:4794a4:8", "const:4:8"]]
+ 004794a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00479464 bytes 937a1f94
+ 004794a4 bytes b77a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7230e51c2cecd279fae646ae1048b597"></a>

### [`00479498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md) → [`004794d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004794d8.md) FUN_004794d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00478d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478d04.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-00479508) · [`00479540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-00479540) · [`004795f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-004795f0)
- 新版 `00479548`（命令位置の公開資料なし） · `00479580`（命令位置の公開資料なし） · `00479630`（命令位置の公開資料なし）

~~~diff
- 00479508 ["INT_ADD", "register:40f0:8", ["const:479508:8", "const:4:8"]]
- 00479508 ["CALL", null, ["callee:00c58010:8"]]
+ 00479548 ["INT_ADD", "register:40f0:8", ["const:479548:8", "const:4:8"]]
+ 00479548 ["CALL", null, ["callee:00c58010:8"]]
- 00479508 bytes 8e7a1f94
+ 00479548 bytes b27a1f94
- 00479540 ["INT_ADD", "register:40f0:8", ["const:479540:8", "const:4:8"]]
- 00479540 ["CALL", null, ["callee:00c57f60:8"]]
+ 00479580 ["INT_ADD", "register:40f0:8", ["const:479580:8", "const:4:8"]]
+ 00479580 ["CALL", null, ["callee:00c57f60:8"]]
- 00479540 bytes 547a1f94
+ 00479580 bytes 787a1f94
- 004795f0 ["INT_ADD", "register:40f0:8", ["const:4795f0:8", "const:4:8"]]
- 004795f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00479630 ["INT_ADD", "register:40f0:8", ["const:479630:8", "const:4:8"]]
+ 00479630 ["CALL", null, ["callee:00c57f80:8"]]
- 004795f0 bytes 307a1f94
+ 00479630 bytes 547a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03de75f2c210d2465fd76475abcd3e84"></a>

### [`00479624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md) → [`00479664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479664.md) FUN_00479664

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md#insn-0047968c)
- 新版 `004796cc`（命令位置の公開資料なし）

~~~diff
- 0047968c ["INT_ADD", "register:40f0:8", ["const:47968c:8", "const:4:8"]]
- 0047968c ["CALL", null, ["callee:00c57f80:8"]]
+ 004796cc ["INT_ADD", "register:40f0:8", ["const:4796cc:8", "const:4:8"]]
+ 004796cc ["CALL", null, ["callee:00c57f80:8"]]
- 0047968c bytes 097a1f94
+ 004796cc bytes 2d7a1f94
~~~


<a id="compare-87fee79fc704aff7eab638784c82e951"></a>

### [`004796b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004796b0.md) → [`004796f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004796f0.md) FUN_004796f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f018.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0053f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f058.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004796fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004796b0.md#insn-004796fc)
- 新版 `0047973c`（命令位置の公開資料なし）

~~~diff
- 004796fc ["INT_ADD", "register:40f0:8", ["const:4796fc:8", "const:4:8"]]
- 004796fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0047973c ["INT_ADD", "register:40f0:8", ["const:47973c:8", "const:4:8"]]
+ 0047973c ["CALL", null, ["callee:00c57f80:8"]]
- 004796fc bytes ed791f94
+ 0047973c bytes 117a1f94
~~~


<a id="compare-ebe94a685c6e2e753c694be0853e5a95"></a>

### [`00479a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md) → [`00479ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479ac4.md) FUN_00479ac4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479aa0) · [`00479ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479ab4) · [`00479ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479ad4)
- 新版 `00479ae0`（命令位置の公開資料なし） · `00479af4`（命令位置の公開資料なし） · `00479b14`（命令位置の公開資料なし）

~~~diff
- 00479aa0 ["INT_ADD", "register:40f0:8", ["const:479aa0:8", "const:4:8"]]
- 00479aa0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00479ae0 ["INT_ADD", "register:40f0:8", ["const:479ae0:8", "const:4:8"]]
+ 00479ae0 ["CALL", null, ["callee:00c57f80:8"]]
- 00479aa0 bytes 04791f94
+ 00479ae0 bytes 28791f94
- 00479ab4 ["INT_ADD", "register:40f0:8", ["const:479ab4:8", "const:4:8"]]
- 00479ab4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479af4 ["INT_ADD", "register:40f0:8", ["const:479af4:8", "const:4:8"]]
+ 00479af4 ["CALL", null, ["callee:00c53da0:8"]]
- 00479ab4 bytes 93681f94
+ 00479af4 bytes ab681f94
- 00479ad4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479ad4 ["INT_ADD", "register:40f0:8", ["const:479ad4:8", "const:4:8"]]
- 00479ad4 ["CALLIND", null, ["register:0:8"]]
+ 00479b14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479b14 ["INT_ADD", "register:40f0:8", ["const:479b14:8", "const:4:8"]]
+ 00479b14 ["CALLIND", null, ["register:0:8"]]
- 00479ad4 bytes 00013fd6
+ 00479b14 bytes 00013fd6
~~~


<a id="compare-c84b1f6744c097bc616083911485e14f"></a>

### [`00479ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md) → [`00479b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479b28.md) FUN_00479b28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b04) · [`00479b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b18) · [`00479b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b2c)
- 新版 `00479b44`（命令位置の公開資料なし） · `00479b58`（命令位置の公開資料なし） · `00479b6c`（命令位置の公開資料なし）

~~~diff
- 00479b04 ["INT_ADD", "register:40f0:8", ["const:479b04:8", "const:4:8"]]
- 00479b04 ["CALL", null, ["callee:00c57f80:8"]]
+ 00479b44 ["INT_ADD", "register:40f0:8", ["const:479b44:8", "const:4:8"]]
+ 00479b44 ["CALL", null, ["callee:00c57f80:8"]]
- 00479b04 bytes eb781f94
+ 00479b44 bytes 0f791f94
- 00479b18 ["INT_ADD", "register:40f0:8", ["const:479b18:8", "const:4:8"]]
- 00479b18 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479b58 ["INT_ADD", "register:40f0:8", ["const:479b58:8", "const:4:8"]]
+ 00479b58 ["CALL", null, ["callee:00c53da0:8"]]
- 00479b18 bytes 7a681f94
+ 00479b58 bytes 92681f94
- 00479b2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00479b2c ["INT_ADD", "register:40f0:8", ["const:479b2c:8", "const:4:8"]]
- 00479b2c ["CALLIND", null, ["register:0:8"]]
+ 00479b6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479b6c ["INT_ADD", "register:40f0:8", ["const:479b6c:8", "const:4:8"]]
+ 00479b6c ["CALLIND", null, ["register:0:8"]]
- 00479b2c bytes 00013fd6
+ 00479b6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4186939da48f654cd7e7770998c3c778"></a>

### [`00479d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md) → [`00479d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479d58.md) FUN_00479d58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md#insn-00479d34) · [`00479d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md#insn-00479d54)
- 新版 `00479d74`（命令位置の公開資料なし） · `00479d94`（命令位置の公開資料なし）

~~~diff
- 00479d34 ["INT_ADD", "register:40f0:8", ["const:479d34:8", "const:4:8"]]
- 00479d34 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479d74 ["INT_ADD", "register:40f0:8", ["const:479d74:8", "const:4:8"]]
+ 00479d74 ["CALL", null, ["callee:00c53da0:8"]]
- 00479d34 bytes f3671f94
+ 00479d74 bytes 0b681f94
- 00479d54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479d54 ["INT_ADD", "register:40f0:8", ["const:479d54:8", "const:4:8"]]
- 00479d54 ["CALLIND", null, ["register:0:8"]]
+ 00479d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479d94 ["INT_ADD", "register:40f0:8", ["const:479d94:8", "const:4:8"]]
+ 00479d94 ["CALLIND", null, ["register:0:8"]]
- 00479d54 bytes 00013fd6
+ 00479d94 bytes 00013fd6
~~~


<a id="compare-15f4b763bada62d68887e43375a86dd4"></a>

### [`00479f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md) → [`00479f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479f8c.md) FUN_00479f8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md#insn-00479f68) · [`00479f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md#insn-00479f88)
- 新版 `00479fa8`（命令位置の公開資料なし） · `00479fc8`（命令位置の公開資料なし）

~~~diff
- 00479f68 ["INT_ADD", "register:40f0:8", ["const:479f68:8", "const:4:8"]]
- 00479f68 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479fa8 ["INT_ADD", "register:40f0:8", ["const:479fa8:8", "const:4:8"]]
+ 00479fa8 ["CALL", null, ["callee:00c53da0:8"]]
- 00479f68 bytes 66671f94
+ 00479fa8 bytes 7e671f94
- 00479f88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479f88 ["INT_ADD", "register:40f0:8", ["const:479f88:8", "const:4:8"]]
- 00479f88 ["CALLIND", null, ["register:0:8"]]
+ 00479fc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479fc8 ["INT_ADD", "register:40f0:8", ["const:479fc8:8", "const:4:8"]]
+ 00479fc8 ["CALLIND", null, ["register:0:8"]]
- 00479f88 bytes 00013fd6
+ 00479fc8 bytes 00013fd6
~~~


<a id="compare-581ce468fe7fa3e532f4279025c22d8c"></a>

### [`00479f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md) → [`00479fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479fdc.md) FUN_00479fdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fbc) · [`00479fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fd0) · [`00479fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fd8)
- 新版 `00479ffc`（命令位置の公開資料なし） · `0047a010`（命令位置の公開資料なし） · `0047a018`（命令位置の公開資料なし）

~~~diff
- 00479fbc ["INT_ADD", "register:40f0:8", ["const:479fbc:8", "const:4:8"]]
- 00479fbc ["CALL", null, ["callee:00c53da0:8"]]
+ 00479ffc ["INT_ADD", "register:40f0:8", ["const:479ffc:8", "const:4:8"]]
+ 00479ffc ["CALL", null, ["callee:00c53da0:8"]]
- 00479fbc bytes 51671f94
+ 00479ffc bytes 69671f94
- 00479fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479fd0 ["INT_ADD", "register:40f0:8", ["const:479fd0:8", "const:4:8"]]
- 00479fd0 ["CALLIND", null, ["register:0:8"]]
+ 0047a010 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a010 ["INT_ADD", "register:40f0:8", ["const:47a010:8", "const:4:8"]]
+ 0047a010 ["CALLIND", null, ["register:0:8"]]
- 00479fd0 bytes 00013fd6
+ 0047a010 bytes 00013fd6
- 00479fd8 ["INT_ADD", "register:40f0:8", ["const:479fd8:8", "const:4:8"]]
- 00479fd8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047a018 ["INT_ADD", "register:40f0:8", ["const:47a018:8", "const:4:8"]]
+ 0047a018 ["CALL", null, ["callee:00c57f50:8"]]
- 00479fd8 bytes aa771f94
+ 0047a018 bytes ce771f94
~~~


<a id="compare-2baad408b92d986781c759b004c52f68"></a>

### [`0047a568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md) → [`0047a5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a5a8.md) FUN_0047a5a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md#insn-0047a584) · [`0047a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md#insn-0047a5a4)
- 新版 `0047a5c4`（命令位置の公開資料なし） · `0047a5e4`（命令位置の公開資料なし）

~~~diff
- 0047a584 ["INT_ADD", "register:40f0:8", ["const:47a584:8", "const:4:8"]]
- 0047a584 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a5c4 ["INT_ADD", "register:40f0:8", ["const:47a5c4:8", "const:4:8"]]
+ 0047a5c4 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a584 bytes df651f94
+ 0047a5c4 bytes f7651f94
- 0047a5a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a5a4 ["INT_ADD", "register:40f0:8", ["const:47a5a4:8", "const:4:8"]]
- 0047a5a4 ["CALLIND", null, ["register:0:8"]]
+ 0047a5e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a5e4 ["INT_ADD", "register:40f0:8", ["const:47a5e4:8", "const:4:8"]]
+ 0047a5e4 ["CALLIND", null, ["register:0:8"]]
- 0047a5a4 bytes 00013fd6
+ 0047a5e4 bytes 00013fd6
~~~


<a id="compare-62c74dc7f2208ae78a6e0590b6e97f2a"></a>

### [`0047a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md) → [`0047a5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a5f8.md) FUN_0047a5f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md#insn-0047a5d4) · [`0047a5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md#insn-0047a5f4)
- 新版 `0047a614`（命令位置の公開資料なし） · `0047a634`（命令位置の公開資料なし）

~~~diff
- 0047a5d4 ["INT_ADD", "register:40f0:8", ["const:47a5d4:8", "const:4:8"]]
- 0047a5d4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a614 ["INT_ADD", "register:40f0:8", ["const:47a614:8", "const:4:8"]]
+ 0047a614 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a5d4 bytes cb651f94
+ 0047a614 bytes e3651f94
- 0047a5f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a5f4 ["INT_ADD", "register:40f0:8", ["const:47a5f4:8", "const:4:8"]]
- 0047a5f4 ["CALLIND", null, ["register:0:8"]]
+ 0047a634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a634 ["INT_ADD", "register:40f0:8", ["const:47a634:8", "const:4:8"]]
+ 0047a634 ["CALLIND", null, ["register:0:8"]]
- 0047a5f4 bytes 00013fd6
+ 0047a634 bytes 00013fd6
~~~


<a id="compare-bf2dfab5fe90187ada2de6604b21cf87"></a>

### [`0047a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md) → [`0047a784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a784.md) FUN_0047a784

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0047a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1c0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md#insn-0047a760) · [`0047a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md#insn-0047a780)
- 新版 `0047a7a0`（命令位置の公開資料なし） · `0047a7c0`（命令位置の公開資料なし）

~~~diff
- 0047a760 ["INT_ADD", "register:40f0:8", ["const:47a760:8", "const:4:8"]]
- 0047a760 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a7a0 ["INT_ADD", "register:40f0:8", ["const:47a7a0:8", "const:4:8"]]
+ 0047a7a0 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a760 bytes 68651f94
+ 0047a7a0 bytes 80651f94
- 0047a780 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a780 ["INT_ADD", "register:40f0:8", ["const:47a780:8", "const:4:8"]]
- 0047a780 ["CALLIND", null, ["register:0:8"]]
+ 0047a7c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a7c0 ["INT_ADD", "register:40f0:8", ["const:47a7c0:8", "const:4:8"]]
+ 0047a7c0 ["CALLIND", null, ["register:0:8"]]
- 0047a780 bytes 00013fd6
+ 0047a7c0 bytes 00013fd6
~~~


<a id="compare-5946e3e202fc3ae6e013c415be652722"></a>

### [`0047a794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md) → [`0047a7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a7d4.md) FUN_0047a7d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0047a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1c0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7b4) · [`0047a7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7c8) · [`0047a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7d0)
- 新版 `0047a7f4`（命令位置の公開資料なし） · `0047a808`（命令位置の公開資料なし） · `0047a810`（命令位置の公開資料なし）

~~~diff
- 0047a7b4 ["INT_ADD", "register:40f0:8", ["const:47a7b4:8", "const:4:8"]]
- 0047a7b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a7f4 ["INT_ADD", "register:40f0:8", ["const:47a7f4:8", "const:4:8"]]
+ 0047a7f4 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a7b4 bytes 53651f94
+ 0047a7f4 bytes 6b651f94
- 0047a7c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a7c8 ["INT_ADD", "register:40f0:8", ["const:47a7c8:8", "const:4:8"]]
- 0047a7c8 ["CALLIND", null, ["register:0:8"]]
+ 0047a808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a808 ["INT_ADD", "register:40f0:8", ["const:47a808:8", "const:4:8"]]
+ 0047a808 ["CALLIND", null, ["register:0:8"]]
- 0047a7c8 bytes 00013fd6
+ 0047a808 bytes 00013fd6
- 0047a7d0 ["INT_ADD", "register:40f0:8", ["const:47a7d0:8", "const:4:8"]]
- 0047a7d0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047a810 ["INT_ADD", "register:40f0:8", ["const:47a810:8", "const:4:8"]]
+ 0047a810 ["CALL", null, ["callee:00c57f50:8"]]
- 0047a7d0 bytes ac751f94
+ 0047a810 bytes d0751f94
~~~


<a id="compare-2e373627c1e361f7ee6ec7688bacdaf4"></a>

### [`0047ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md) → [`0047ade4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ade4.md) FUN_0047ade4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fa8c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047adc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047adc4) · [`0047add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047add0) · [`0047ade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047ade4)
- 新版 `0047ae04`（命令位置の公開資料なし） · `0047ae10`（命令位置の公開資料なし） · `0047ae24`（命令位置の公開資料なし）

~~~diff
- 0047adc4 ["INT_ADD", "register:40f0:8", ["const:47adc4:8", "const:4:8"]]
- 0047adc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047ae04 ["INT_ADD", "register:40f0:8", ["const:47ae04:8", "const:4:8"]]
+ 0047ae04 ["CALL", null, ["callee:00c57f80:8"]]
- 0047adc4 bytes 3b741f94
+ 0047ae04 bytes 5f741f94
- 0047add0 ["INT_ADD", "register:40f0:8", ["const:47add0:8", "const:4:8"]]
- 0047add0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047ae10 ["INT_ADD", "register:40f0:8", ["const:47ae10:8", "const:4:8"]]
+ 0047ae10 ["CALL", null, ["callee:00c57f80:8"]]
- 0047add0 bytes 38741f94
+ 0047ae10 bytes 5c741f94
- 0047ade4 ["INT_ADD", "register:40f0:8", ["const:47ade4:8", "const:4:8"]]
- 0047ade4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047ae24 ["INT_ADD", "register:40f0:8", ["const:47ae24:8", "const:4:8"]]
+ 0047ae24 ["CALL", null, ["callee:00c53da0:8"]]
- 0047ade4 bytes c7631f94
+ 0047ae24 bytes df631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b068c7d192db8323443930cfc6040a6"></a>

### [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) → [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) FUN_0047b54c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`007c7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7978.md) [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 7件 [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) [`007c79d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c79d0.md) [`0080bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080bd30.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 7件 [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b5b8) · [`0047b5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b5ec) · [`0047b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b650)
- 新版 `0047b5f8`（命令位置の公開資料なし） · `0047b62c`（命令位置の公開資料なし） · `0047b690`（命令位置の公開資料なし）

~~~diff
- 0047b5b8 ["INT_ADD", "register:40f0:8", ["const:47b5b8:8", "const:4:8"]]
- 0047b5b8 ["CALL", null, ["callee:0047d5f4:8"]]
+ 0047b5f8 ["INT_ADD", "register:40f0:8", ["const:47b5f8:8", "const:4:8"]]
+ 0047b5f8 ["CALL", null, ["callee:0047d5f4:8"]]
- 0047b5b8 bytes ff070094
+ 0047b5f8 bytes ff070094
- 0047b5ec ["INT_ADD", "register:40f0:8", ["const:47b5ec:8", "const:4:8"]]
- 0047b5ec ["CALL", null, ["callee:00c58010:8"]]
+ 0047b62c ["INT_ADD", "register:40f0:8", ["const:47b62c:8", "const:4:8"]]
+ 0047b62c ["CALL", null, ["callee:00c58010:8"]]
- 0047b5ec bytes 55721f94
+ 0047b62c bytes 79721f94
- 0047b650 ["INT_ADD", "register:40f0:8", ["const:47b650:8", "const:4:8"]]
- 0047b650 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047b690 ["INT_ADD", "register:40f0:8", ["const:47b690:8", "const:4:8"]]
+ 0047b690 ["CALL", null, ["callee:00c57f80:8"]]
- 0047b650 bytes 18721f94
+ 0047b690 bytes 3c721f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea957683c8947223ff4dd61acb1cc31b"></a>

### [`0047b7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md) → [`0047b80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b80c.md) FUN_0047b80c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2c424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00b2c4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b804) · [`0047b818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b818) · [`0047b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b820)
- 新版 `0047b844`（命令位置の公開資料なし） · `0047b858`（命令位置の公開資料なし） · `0047b860`（命令位置の公開資料なし）

~~~diff
- 0047b804 ["INT_ADD", "register:40f0:8", ["const:47b804:8", "const:4:8"]]
- 0047b804 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047b844 ["INT_ADD", "register:40f0:8", ["const:47b844:8", "const:4:8"]]
+ 0047b844 ["CALL", null, ["callee:00c53da0:8"]]
- 0047b804 bytes 3f611f94
+ 0047b844 bytes 57611f94
- 0047b818 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047b818 ["INT_ADD", "register:40f0:8", ["const:47b818:8", "const:4:8"]]
- 0047b818 ["CALLIND", null, ["register:0:8"]]
+ 0047b858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047b858 ["INT_ADD", "register:40f0:8", ["const:47b858:8", "const:4:8"]]
+ 0047b858 ["CALLIND", null, ["register:0:8"]]
- 0047b818 bytes 00013fd6
+ 0047b858 bytes 00013fd6
- 0047b820 ["INT_ADD", "register:40f0:8", ["const:47b820:8", "const:4:8"]]
- 0047b820 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047b860 ["INT_ADD", "register:40f0:8", ["const:47b860:8", "const:4:8"]]
+ 0047b860 ["CALL", null, ["callee:00c57f50:8"]]
- 0047b820 bytes 98711f94
+ 0047b860 bytes bc711f94
~~~


<a id="compare-898512121786ea645c32fc41cbd3ae06"></a>

### [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) → [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) FUN_0047c9a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 27件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061308c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md) [`00631334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00631/00631334.md) [`00632d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00632/00632d54.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0047d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d8a0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047c9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9bc) · [`0047c9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9cc) · [`0047c9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9fc)
- 新版 `0047c9fc`（命令位置の公開資料なし） · `0047ca0c`（命令位置の公開資料なし） · `0047ca3c`（命令位置の公開資料なし）

~~~diff
- 0047c9bc ["INT_ADD", "register:40f0:8", ["const:47c9bc:8", "const:4:8"]]
- 0047c9bc ["CALL", null, ["callee:0043bb60:8"]]
+ 0047c9fc ["INT_ADD", "register:40f0:8", ["const:47c9fc:8", "const:4:8"]]
+ 0047c9fc ["CALL", null, ["callee:0043bb60:8"]]
- 0047c9bc bytes 59fcfe97
+ 0047c9fc bytes 59fcfe97
- 0047c9cc ["INT_ADD", "register:40f0:8", ["const:47c9cc:8", "const:4:8"]]
- 0047c9cc ["CALL", null, ["callee:0043bb60:8"]]
+ 0047ca0c ["INT_ADD", "register:40f0:8", ["const:47ca0c:8", "const:4:8"]]
+ 0047ca0c ["CALL", null, ["callee:0043bb60:8"]]
- 0047c9cc bytes 55fcfe97
+ 0047ca0c bytes 55fcfe97
- 0047c9fc ["INT_ADD", "register:40f0:8", ["const:47c9fc:8", "const:4:8"]]
- 0047c9fc ["CALL", null, ["callee:0047d8a0:8"]]
+ 0047ca3c ["INT_ADD", "register:40f0:8", ["const:47ca3c:8", "const:4:8"]]
+ 0047ca3c ["CALL", null, ["callee:0047d8a0:8"]]
- 0047c9fc bytes 99030094
+ 0047ca3c bytes 99030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-551221d8b4c9f2de2dde3539213adbc6"></a>

### [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) → [`0047cacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cacc.md) FUN_0047cacc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`005e6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6dfc.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0064e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e37c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 27件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) [`005e6e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e6/005e6e3c.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`0064e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbbc) · [`0047cbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbdc) · [`0047cbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbf0)
- 新版 `0047cbfc`（命令位置の公開資料なし） · `0047cc1c`（命令位置の公開資料なし） · `0047cc30`（命令位置の公開資料なし）

~~~diff
- 0047cbbc ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cbbc ["INT_ADD", "register:40f0:8", ["const:47cbbc:8", "const:4:8"]]
- 0047cbbc ["CALLIND", null, ["register:0:8"]]
+ 0047cbfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cbfc ["INT_ADD", "register:40f0:8", ["const:47cbfc:8", "const:4:8"]]
+ 0047cbfc ["CALLIND", null, ["register:0:8"]]
- 0047cbbc bytes 00013fd6
+ 0047cbfc bytes 00013fd6
- 0047cbdc ["INT_ADD", "register:40f0:8", ["const:47cbdc:8", "const:4:8"]]
- 0047cbdc ["CALL", null, ["callee:00c53da0:8"]]
+ 0047cc1c ["INT_ADD", "register:40f0:8", ["const:47cc1c:8", "const:4:8"]]
+ 0047cc1c ["CALL", null, ["callee:00c53da0:8"]]
- 0047cbdc bytes 495c1f94
+ 0047cc1c bytes 615c1f94
- 0047cbf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cbf0 ["INT_ADD", "register:40f0:8", ["const:47cbf0:8", "const:4:8"]]
- 0047cbf0 ["CALLIND", null, ["register:0:8"]]
+ 0047cc30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cc30 ["INT_ADD", "register:40f0:8", ["const:47cc30:8", "const:4:8"]]
+ 0047cc30 ["CALLIND", null, ["register:0:8"]]
- 0047cbf0 bytes 00013fd6
+ 0047cc30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fedc14b1c455c8694959e35dee952b26"></a>

### [`0047cd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md) → [`0047cd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cd68.md) FUN_0047cd68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd54) · [`0047cd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd68) · [`0047cd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd70)
- 新版 `0047cd94`（命令位置の公開資料なし） · `0047cda8`（命令位置の公開資料なし） · `0047cdb0`（命令位置の公開資料なし）

~~~diff
- 0047cd54 ["INT_ADD", "register:40f0:8", ["const:47cd54:8", "const:4:8"]]
- 0047cd54 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047cd94 ["INT_ADD", "register:40f0:8", ["const:47cd94:8", "const:4:8"]]
+ 0047cd94 ["CALL", null, ["callee:00c53da0:8"]]
- 0047cd54 bytes eb5b1f94
+ 0047cd94 bytes 035c1f94
- 0047cd68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cd68 ["INT_ADD", "register:40f0:8", ["const:47cd68:8", "const:4:8"]]
- 0047cd68 ["CALLIND", null, ["register:0:8"]]
+ 0047cda8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cda8 ["INT_ADD", "register:40f0:8", ["const:47cda8:8", "const:4:8"]]
+ 0047cda8 ["CALLIND", null, ["register:0:8"]]
- 0047cd68 bytes 00013fd6
+ 0047cda8 bytes 00013fd6
- 0047cd70 ["INT_ADD", "register:40f0:8", ["const:47cd70:8", "const:4:8"]]
- 0047cd70 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047cdb0 ["INT_ADD", "register:40f0:8", ["const:47cdb0:8", "const:4:8"]]
+ 0047cdb0 ["CALL", null, ["callee:00c57f50:8"]]
- 0047cd70 bytes 446c1f94
+ 0047cdb0 bytes 686c1f94
~~~


<a id="compare-350a176b4245771249b33d8e3ee8d903"></a>

### [`0047cd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md) → [`0047cdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cdc4.md) FUN_0047cdc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md#insn-0047cda0) · [`0047cdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md#insn-0047cdc0)
- 新版 `0047cde0`（命令位置の公開資料なし） · `0047ce00`（命令位置の公開資料なし）

~~~diff
- 0047cda0 ["INT_ADD", "register:40f0:8", ["const:47cda0:8", "const:4:8"]]
- 0047cda0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047cde0 ["INT_ADD", "register:40f0:8", ["const:47cde0:8", "const:4:8"]]
+ 0047cde0 ["CALL", null, ["callee:00c53da0:8"]]
- 0047cda0 bytes d85b1f94
+ 0047cde0 bytes f05b1f94
- 0047cdc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cdc0 ["INT_ADD", "register:40f0:8", ["const:47cdc0:8", "const:4:8"]]
- 0047cdc0 ["CALLIND", null, ["register:0:8"]]
+ 0047ce00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ce00 ["INT_ADD", "register:40f0:8", ["const:47ce00:8", "const:4:8"]]
+ 0047ce00 ["CALLIND", null, ["register:0:8"]]
- 0047cdc0 bytes 00013fd6
+ 0047ce00 bytes 00013fd6
~~~


<a id="compare-56adbdd767fcfd6d7124c9e3a0b191fd"></a>

### [`0047cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) → [`0047ce1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce1c.md) FUN_0047ce1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005f1ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f1ad4.md) [`005f210c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f210c.md) [`005f2340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2340.md) [`005f2798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2798.md) [`005f8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8820.md) · 呼出先 2件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`005e0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d68.md)
- 新版 呼出元 9件 [`005f1b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f1/005f1b14.md) [`005f214c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f214c.md) [`005f2380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f2380.md) [`005f27d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f27d8.md) [`005f8860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f8/005f8860.md) · 呼出先 2件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) [`005e0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0da8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md#insn-0047cdf0)
- 新版 `0047ce30`（命令位置の公開資料なし）

~~~diff
- 0047cdf0 ["INT_ADD", "register:40f0:8", ["const:47cdf0:8", "const:4:8"]]
- 0047cdf0 ["CALL", null, ["callee:005e0da8:8"]]
+ 0047ce30 ["INT_ADD", "register:40f0:8", ["const:47ce30:8", "const:4:8"]]
+ 0047ce30 ["CALL", null, ["callee:005e0da8:8"]]
- 0047cdf0 bytes de8f0594
+ 0047ce30 bytes de8f0594
~~~


<a id="compare-1b9186557d420998de62e0b11c113540"></a>

### [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) → [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) FUN_0047ce68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) [`0085460c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/0085460c.md) [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 6件 [`0061675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md) [`006ff370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md) [`007fd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd3d4.md) [`00854664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854664.md) [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ce58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ce58) · [`0047ceb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ceb0) · [`0047ced0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ced0)
- 新版 `0047ce98`（命令位置の公開資料なし） · `0047cef0`（命令位置の公開資料なし） · `0047cf10`（命令位置の公開資料なし）

~~~diff
- 0047ce58 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047ce58 ["INT_ADD", "register:40f0:8", ["const:47ce58:8", "const:4:8"]]
- 0047ce58 ["CALLIND", null, ["register:0:8"]]
+ 0047ce98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ce98 ["INT_ADD", "register:40f0:8", ["const:47ce98:8", "const:4:8"]]
+ 0047ce98 ["CALLIND", null, ["register:0:8"]]
- 0047ce58 bytes 00013fd6
+ 0047ce98 bytes 00013fd6
- 0047ceb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047ceb0 ["INT_ADD", "register:40f0:8", ["const:47ceb0:8", "const:4:8"]]
- 0047ceb0 ["CALLIND", null, ["register:0:8"]]
+ 0047cef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cef0 ["INT_ADD", "register:40f0:8", ["const:47cef0:8", "const:4:8"]]
+ 0047cef0 ["CALLIND", null, ["register:0:8"]]
- 0047ceb0 bytes 00013fd6
+ 0047cef0 bytes 00013fd6
- 0047ced0 ["INT_ADD", "register:40f0:8", ["const:47ced0:8", "const:4:8"]]
- 0047ced0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047cf10 ["INT_ADD", "register:40f0:8", ["const:47cf10:8", "const:4:8"]]
+ 0047cf10 ["CALL", null, ["callee:00c53da0:8"]]
- 0047ced0 bytes 8c5b1f94
+ 0047cf10 bytes a45b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a9547a49e7645158fe49489f722479c"></a>

### [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) → [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) FUN_0047cf48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) · 呼出先 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md)
- 新版 呼出元 7件 [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) [`00616990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md) [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`007fd648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd648.md) [`00853cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) · 呼出先 1件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md#insn-0047cf70)
- 新版 `0047cfb0`（命令位置の公開資料なし）

~~~diff
- 0047cf70 ["INT_ADD", "register:40f0:8", ["const:47cf70:8", "const:4:8"]]
- 0047cf70 ["CALL", null, ["callee:0047c088:8"]]
+ 0047cfb0 ["INT_ADD", "register:40f0:8", ["const:47cfb0:8", "const:4:8"]]
+ 0047cfb0 ["CALL", null, ["callee:0047c088:8"]]
- 0047cf70 bytes 36fcff97
+ 0047cfb0 bytes 36fcff97
~~~


<a id="compare-c0f475aa5e0e8fa40b2fe7ad16478fce"></a>

### [`0047cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md) → [`0047cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cff8.md) FUN_0047cff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0088043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`00880494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d02c) · [`0047d04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d04c) · [`0047d060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d060)
- 新版 `0047d06c`（命令位置の公開資料なし） · `0047d08c`（命令位置の公開資料なし） · `0047d0a0`（命令位置の公開資料なし）

~~~diff
- 0047d02c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d02c ["INT_ADD", "register:40f0:8", ["const:47d02c:8", "const:4:8"]]
- 0047d02c ["CALLIND", null, ["register:0:8"]]
+ 0047d06c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d06c ["INT_ADD", "register:40f0:8", ["const:47d06c:8", "const:4:8"]]
+ 0047d06c ["CALLIND", null, ["register:0:8"]]
- 0047d02c bytes 00013fd6
+ 0047d06c bytes 00013fd6
- 0047d04c ["INT_ADD", "register:40f0:8", ["const:47d04c:8", "const:4:8"]]
- 0047d04c ["CALL", null, ["callee:00c53da0:8"]]
+ 0047d08c ["INT_ADD", "register:40f0:8", ["const:47d08c:8", "const:4:8"]]
+ 0047d08c ["CALL", null, ["callee:00c53da0:8"]]
- 0047d04c bytes 2d5b1f94
+ 0047d08c bytes 455b1f94
- 0047d060 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d060 ["INT_ADD", "register:40f0:8", ["const:47d060:8", "const:4:8"]]
- 0047d060 ["CALLIND", null, ["register:0:8"]]
+ 0047d0a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d0a0 ["INT_ADD", "register:40f0:8", ["const:47d0a0:8", "const:4:8"]]
+ 0047d0a0 ["CALLIND", null, ["register:0:8"]]
- 0047d060 bytes 00013fd6
+ 0047d0a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1afa403111aabe43fbb1807ff9736f7"></a>

### [`0047d11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d11c.md) → [`0047d15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d15c.md) FUN_0047d15c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00933684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933684.md) [`00933f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933f58.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`009336d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00933/009336d8.md) [`00933fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00933/00933fac.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d11c.md#insn-0047d1a0)
- 新版 `0047d1e0`（命令位置の公開資料なし）

~~~diff
- 0047d1a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d1a0 ["INT_ADD", "register:40f0:8", ["const:47d1a0:8", "const:4:8"]]
- 0047d1a0 ["CALLIND", null, ["register:0:8"]]
+ 0047d1e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d1e0 ["INT_ADD", "register:40f0:8", ["const:47d1e0:8", "const:4:8"]]
+ 0047d1e0 ["CALLIND", null, ["register:0:8"]]
- 0047d1a0 bytes 00013fd6
+ 0047d1e0 bytes 00013fd6
~~~


<a id="compare-2b68ca8dab46386701ea717d379d4ad1"></a>

### [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md) → [`0047d2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d2bc.md) FUN_0047d2bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0047d404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0047d444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d444.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d2f4) · [`0047d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d318) · [`0047d344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d344)
- 新版 `0047d334`（命令位置の公開資料なし） · `0047d358`（命令位置の公開資料なし） · `0047d384`（命令位置の公開資料なし）

~~~diff
- 0047d2f4 ["INT_ADD", "register:40f0:8", ["const:47d2f4:8", "const:4:8"]]
- 0047d2f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047d334 ["INT_ADD", "register:40f0:8", ["const:47d334:8", "const:4:8"]]
+ 0047d334 ["CALL", null, ["callee:00c57f60:8"]]
- 0047d2f4 bytes e76a1f94
+ 0047d334 bytes 0b6b1f94
- 0047d318 ["INT_ADD", "register:40f0:8", ["const:47d318:8", "const:4:8"]]
- 0047d318 ["CALL", null, ["callee:00c58160:8"]]
+ 0047d358 ["INT_ADD", "register:40f0:8", ["const:47d358:8", "const:4:8"]]
+ 0047d358 ["CALL", null, ["callee:00c58160:8"]]
- 0047d318 bytes 5e6b1f94
+ 0047d358 bytes 826b1f94
- 0047d344 ["INT_ADD", "register:40f0:8", ["const:47d344:8", "const:4:8"]]
- 0047d344 ["CALL", null, ["callee:00c58160:8"]]
+ 0047d384 ["INT_ADD", "register:40f0:8", ["const:47d384:8", "const:4:8"]]
+ 0047d384 ["CALL", null, ["callee:00c58160:8"]]
- 0047d344 bytes 536b1f94
+ 0047d384 bytes 776b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b36116a396a0b59f9d12a4a4fa4e81"></a>

### [`0047d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md) → [`0047d458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d458.md) FUN_0047d458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0047d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0047d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d490) · [`0047d4b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d4b4) · [`0047d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d4e0)
- 新版 `0047d4d0`（命令位置の公開資料なし） · `0047d4f4`（命令位置の公開資料なし） · `0047d520`（命令位置の公開資料なし）

~~~diff
- 0047d490 ["INT_ADD", "register:40f0:8", ["const:47d490:8", "const:4:8"]]
- 0047d490 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047d4d0 ["INT_ADD", "register:40f0:8", ["const:47d4d0:8", "const:4:8"]]
+ 0047d4d0 ["CALL", null, ["callee:00c57f60:8"]]
- 0047d490 bytes 806a1f94
+ 0047d4d0 bytes a46a1f94
- 0047d4b4 ["INT_ADD", "register:40f0:8", ["const:47d4b4:8", "const:4:8"]]
- 0047d4b4 ["CALL", null, ["callee:00c58160:8"]]
+ 0047d4f4 ["INT_ADD", "register:40f0:8", ["const:47d4f4:8", "const:4:8"]]
+ 0047d4f4 ["CALL", null, ["callee:00c58160:8"]]
- 0047d4b4 bytes f76a1f94
+ 0047d4f4 bytes 1b6b1f94
- 0047d4e0 ["INT_ADD", "register:40f0:8", ["const:47d4e0:8", "const:4:8"]]
- 0047d4e0 ["CALL", null, ["callee:00c58160:8"]]
+ 0047d520 ["INT_ADD", "register:40f0:8", ["const:47d520:8", "const:4:8"]]
+ 0047d520 ["CALL", null, ["callee:00c58160:8"]]
- 0047d4e0 bytes ec6a1f94
+ 0047d520 bytes 106b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6508f139f866e662626af8264ed21c4"></a>

### [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) → [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) FUN_0047d5f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`0049eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md) [`0080f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080f128.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`0049ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md) [`0080f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080f180.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md#insn-0047d5e4) · [`0047d6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md#insn-0047d6b4)
- 新版 `0047d624`（命令位置の公開資料なし） · `0047d6f4`（命令位置の公開資料なし）

~~~diff
- 0047d5e4 ["INT_ADD", "register:40f0:8", ["const:47d5e4:8", "const:4:8"]]
- 0047d5e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047d624 ["INT_ADD", "register:40f0:8", ["const:47d624:8", "const:4:8"]]
+ 0047d624 ["CALL", null, ["callee:00c57f60:8"]]
- 0047d5e4 bytes 2b6a1f94
+ 0047d624 bytes 4f6a1f94
- 0047d6b4 ["INT_ADD", "register:40f0:8", ["const:47d6b4:8", "const:4:8"]]
- 0047d6b4 ["CALL", null, ["callee:0047d6f8:8"]]
+ 0047d6f4 ["INT_ADD", "register:40f0:8", ["const:47d6f4:8", "const:4:8"]]
+ 0047d6f4 ["CALL", null, ["callee:0047d6f8:8"]]
- 0047d6b4 bytes 01000094
+ 0047d6f4 bytes 01000094
~~~


<a id="compare-0b6ac2953a86b0890df5d3f62cf1b16e"></a>

### [`0047d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md) → [`0047d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d764.md) FUN_0047d764

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0047be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047be20.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d77c) · [`0047d798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d798) · [`0047d7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d7ac)
- 新版 `0047d7bc`（命令位置の公開資料なし） · `0047d7d8`（命令位置の公開資料なし） · `0047d7ec`（命令位置の公開資料なし）

~~~diff
- 0047d77c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d77c ["INT_ADD", "register:40f0:8", ["const:47d77c:8", "const:4:8"]]
- 0047d77c ["CALLIND", null, ["register:0:8"]]
+ 0047d7bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d7bc ["INT_ADD", "register:40f0:8", ["const:47d7bc:8", "const:4:8"]]
+ 0047d7bc ["CALLIND", null, ["register:0:8"]]
- 0047d77c bytes 00013fd6
+ 0047d7bc bytes 00013fd6
- 0047d798 ["INT_ADD", "register:40f0:8", ["const:47d798:8", "const:4:8"]]
- 0047d798 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047d7d8 ["INT_ADD", "register:40f0:8", ["const:47d7d8:8", "const:4:8"]]
+ 0047d7d8 ["CALL", null, ["callee:00c53da0:8"]]
- 0047d798 bytes 5a591f94
+ 0047d7d8 bytes 72591f94
- 0047d7ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d7ac ["INT_ADD", "register:40f0:8", ["const:47d7ac:8", "const:4:8"]]
- 0047d7ac ["CALLIND", null, ["register:0:8"]]
+ 0047d7ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d7ec ["INT_ADD", "register:40f0:8", ["const:47d7ec:8", "const:4:8"]]
+ 0047d7ec ["CALLIND", null, ["register:0:8"]]
- 0047d7ac bytes 00013fd6
+ 0047d7ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eabaf12c0a057a3ee24754c289dcf1ce"></a>

### [`0047ece4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md) → [`0047ed24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ed24.md) FUN_0047ed24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f714.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed10) · [`0047ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed28) · [`0047ed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed30)
- 新版 `0047ed50`（命令位置の公開資料なし） · `0047ed68`（命令位置の公開資料なし） · `0047ed70`（命令位置の公開資料なし）

~~~diff
- 0047ed10 ["INT_ADD", "register:40f0:8", ["const:47ed10:8", "const:4:8"]]
- 0047ed10 ["CALL", null, ["callee:0047f714:8"]]
+ 0047ed50 ["INT_ADD", "register:40f0:8", ["const:47ed50:8", "const:4:8"]]
+ 0047ed50 ["CALL", null, ["callee:0047f714:8"]]
- 0047ed10 bytes 71020094
+ 0047ed50 bytes 71020094
- 0047ed28 ["INT_ADD", "register:40f0:8", ["const:47ed28:8", "const:4:8"]]
- 0047ed28 ["CALL", null, ["callee:00c585b0:8"]]
+ 0047ed68 ["INT_ADD", "register:40f0:8", ["const:47ed68:8", "const:4:8"]]
+ 0047ed68 ["CALL", null, ["callee:00c585b0:8"]]
- 0047ed28 bytes ee651f94
+ 0047ed68 bytes 12661f94
- 0047ed30 ["INT_ADD", "register:40f0:8", ["const:47ed30:8", "const:4:8"]]
- 0047ed30 ["CALL", null, ["callee:00c585b0:8"]]
+ 0047ed70 ["INT_ADD", "register:40f0:8", ["const:47ed70:8", "const:4:8"]]
+ 0047ed70 ["CALL", null, ["callee:00c585b0:8"]]
- 0047ed30 bytes ec651f94
+ 0047ed70 bytes 10661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05622101dc6c65e94a366ae27c255857"></a>

### [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) → [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) FUN_0047edf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 213件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) [`005cc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc1b4.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 4件 [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 207件 [`0047e24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e24c.md) [`005ba350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md) [`005c429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md) [`005cc1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md) [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) · 呼出先 4件 [`0047ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ee40.md) [`0047eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047eef0.md) [`00497cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047edd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047edd4) · [`0047eddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047eddc) · [`0047ede8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047ede8)
- 新版 `0047ee14`（命令位置の公開資料なし） · `0047ee1c`（命令位置の公開資料なし） · `0047ee28`（命令位置の公開資料なし）

~~~diff
- 0047edd4 ["INT_ADD", "register:40f0:8", ["const:47edd4:8", "const:4:8"]]
- 0047edd4 ["CALL", null, ["callee:00497cbc:8"]]
+ 0047ee14 ["INT_ADD", "register:40f0:8", ["const:47ee14:8", "const:4:8"]]
+ 0047ee14 ["CALL", null, ["callee:00497cbc:8"]]
- 0047edd4 bytes aa630094
+ 0047ee14 bytes aa630094
- 0047eddc ["INT_ADD", "register:40f0:8", ["const:47eddc:8", "const:4:8"]]
- 0047eddc ["CALL", null, ["callee:00c57f80:8"]]
+ 0047ee1c ["INT_ADD", "register:40f0:8", ["const:47ee1c:8", "const:4:8"]]
+ 0047ee1c ["CALL", null, ["callee:00c57f80:8"]]
- 0047eddc bytes 35641f94
+ 0047ee1c bytes 59641f94
- 0047ede8 ["INT_ADD", "register:40f0:8", ["const:47ede8:8", "const:4:8"]]
- 0047ede8 ["CALL", null, ["callee:0047ee40:8"]]
+ 0047ee28 ["INT_ADD", "register:40f0:8", ["const:47ee28:8", "const:4:8"]]
+ 0047ee28 ["CALL", null, ["callee:0047ee40:8"]]
- 0047ede8 bytes 06000094
+ 0047ee28 bytes 06000094
~~~


<a id="compare-53af851852c740f4a6daaf50776312b5"></a>

### [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) → [`0047ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ee40.md) FUN_0047ee40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) · 呼出先 3件 [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0047ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ee40.md) · 呼出先 3件 [`0047ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ee40.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ee1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee1c) · [`0047ee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee28) · [`0047ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee34)
- 新版 `0047ee5c`（命令位置の公開資料なし） · `0047ee68`（命令位置の公開資料なし） · `0047ee74`（命令位置の公開資料なし）

~~~diff
- 0047ee1c ["INT_ADD", "register:40f0:8", ["const:47ee1c:8", "const:4:8"]]
- 0047ee1c ["CALL", null, ["local:b0:8"]]
+ 0047ee5c ["INT_ADD", "register:40f0:8", ["const:47ee5c:8", "const:4:8"]]
+ 0047ee5c ["CALL", null, ["local:b0:8"]]
- 0047ee1c bytes f9ffff97
+ 0047ee5c bytes f9ffff97
- 0047ee28 ["INT_ADD", "register:40f0:8", ["const:47ee28:8", "const:4:8"]]
- 0047ee28 ["CALL", null, ["local:b0:8"]]
+ 0047ee68 ["INT_ADD", "register:40f0:8", ["const:47ee68:8", "const:4:8"]]
+ 0047ee68 ["CALL", null, ["local:b0:8"]]
- 0047ee28 bytes f6ffff97
+ 0047ee68 bytes f6ffff97
- 0047ee34 ["INT_ADD", "register:40f0:8", ["const:47ee34:8", "const:4:8"]]
- 0047ee34 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047ee74 ["INT_ADD", "register:40f0:8", ["const:47ee74:8", "const:4:8"]]
+ 0047ee74 ["CALL", null, ["callee:00c57f50:8"]]
- 0047ee34 bytes 13641f94
+ 0047ee74 bytes 37641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159a2ba0a000b6327656be0e6e92e052"></a>

### [`0047ee6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee6c.md) → [`0047eeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047eeac.md) FUN_0047eeac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ee88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee6c.md#insn-0047ee88)
- 新版 `0047eec8`（命令位置の公開資料なし）

~~~diff
- 0047ee88 ["INT_ADD", "register:40f0:8", ["const:47ee88:8", "const:4:8"]]
- 0047ee88 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047eec8 ["INT_ADD", "register:40f0:8", ["const:47eec8:8", "const:4:8"]]
+ 0047eec8 ["CALL", null, ["callee:00c57f80:8"]]
- 0047ee88 bytes 0a641f94
+ 0047eec8 bytes 2e641f94
~~~


<a id="compare-460e1a21676cce53e330257a5a60e7a6"></a>

### [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) → [`0047eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047eef0.md) FUN_0047eef0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) · 呼出先 3件 [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0047eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047eef0.md) · 呼出先 3件 [`0047eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047eef0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eecc) · [`0047eed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eed8) · [`0047eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eee4)
- 新版 `0047ef0c`（命令位置の公開資料なし） · `0047ef18`（命令位置の公開資料なし） · `0047ef24`（命令位置の公開資料なし）

~~~diff
- 0047eecc ["INT_ADD", "register:40f0:8", ["const:47eecc:8", "const:4:8"]]
- 0047eecc ["CALL", null, ["local:b0:8"]]
+ 0047ef0c ["INT_ADD", "register:40f0:8", ["const:47ef0c:8", "const:4:8"]]
+ 0047ef0c ["CALL", null, ["local:b0:8"]]
- 0047eecc bytes f9ffff97
+ 0047ef0c bytes f9ffff97
- 0047eed8 ["INT_ADD", "register:40f0:8", ["const:47eed8:8", "const:4:8"]]
- 0047eed8 ["CALL", null, ["local:b0:8"]]
+ 0047ef18 ["INT_ADD", "register:40f0:8", ["const:47ef18:8", "const:4:8"]]
+ 0047ef18 ["CALL", null, ["local:b0:8"]]
- 0047eed8 bytes f6ffff97
+ 0047ef18 bytes f6ffff97
- 0047eee4 ["INT_ADD", "register:40f0:8", ["const:47eee4:8", "const:4:8"]]
- 0047eee4 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047ef24 ["INT_ADD", "register:40f0:8", ["const:47ef24:8", "const:4:8"]]
+ 0047ef24 ["CALL", null, ["callee:00c57f50:8"]]
- 0047eee4 bytes e7631f94
+ 0047ef24 bytes 0b641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-544a913aa137390fbd0496959a63b14f"></a>

### [`0047ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md) → [`0047ef4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ef4c.md) FUN_0047ef4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ef78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md#insn-0047ef78) · [`0047efd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md#insn-0047efd4)
- 新版 `0047efb8`（命令位置の公開資料なし） · `0047f014`（命令位置の公開資料なし）

~~~diff
- 0047ef78 ["INT_ADD", "register:40f0:8", ["const:47ef78:8", "const:4:8"]]
- 0047ef78 ["CALL", null, ["callee:00c58120:8"]]
+ 0047efb8 ["INT_ADD", "register:40f0:8", ["const:47efb8:8", "const:4:8"]]
+ 0047efb8 ["CALL", null, ["callee:00c58120:8"]]
- 0047ef78 bytes 36641f94
+ 0047efb8 bytes 5a641f94
- 0047efd4 ["INT_ADD", "register:40f0:8", ["const:47efd4:8", "const:4:8"]]
- 0047efd4 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f014 ["INT_ADD", "register:40f0:8", ["const:47f014:8", "const:4:8"]]
+ 0047f014 ["CALL", null, ["callee:00c58120:8"]]
- 0047efd4 bytes 1f641f94
+ 0047f014 bytes 43641f94
~~~


<a id="compare-756f8ae7ed30137dcc30662c04463447"></a>

### [`0047f05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md) → [`0047f09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f09c.md) FUN_0047f09c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047f050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f050.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0047f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f090.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f07c) · [`0047f090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f090) · [`0047f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f098)
- 新版 `0047f0bc`（命令位置の公開資料なし） · `0047f0d0`（命令位置の公開資料なし） · `0047f0d8`（命令位置の公開資料なし）

~~~diff
- 0047f07c ["INT_ADD", "register:40f0:8", ["const:47f07c:8", "const:4:8"]]
- 0047f07c ["CALL", null, ["callee:00c53da0:8"]]
+ 0047f0bc ["INT_ADD", "register:40f0:8", ["const:47f0bc:8", "const:4:8"]]
+ 0047f0bc ["CALL", null, ["callee:00c53da0:8"]]
- 0047f07c bytes 21531f94
+ 0047f0bc bytes 39531f94
- 0047f090 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047f090 ["INT_ADD", "register:40f0:8", ["const:47f090:8", "const:4:8"]]
- 0047f090 ["CALLIND", null, ["register:0:8"]]
+ 0047f0d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047f0d0 ["INT_ADD", "register:40f0:8", ["const:47f0d0:8", "const:4:8"]]
+ 0047f0d0 ["CALLIND", null, ["register:0:8"]]
- 0047f090 bytes 00013fd6
+ 0047f0d0 bytes 00013fd6
- 0047f098 ["INT_ADD", "register:40f0:8", ["const:47f098:8", "const:4:8"]]
- 0047f098 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047f0d8 ["INT_ADD", "register:40f0:8", ["const:47f0d8:8", "const:4:8"]]
+ 0047f0d8 ["CALL", null, ["callee:00c57f50:8"]]
- 0047f098 bytes 7a631f94
+ 0047f0d8 bytes 9e631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3406714eb1d601752468faf78d99d7"></a>

### [`0047f14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md) → [`0047f18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f18c.md) FUN_0047f18c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md#insn-0047f1d0) · [`0047f1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md#insn-0047f1fc)
- 新版 `0047f210`（命令位置の公開資料なし） · `0047f23c`（命令位置の公開資料なし）

~~~diff
- 0047f1d0 ["INT_ADD", "register:40f0:8", ["const:47f1d0:8", "const:4:8"]]
- 0047f1d0 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f210 ["INT_ADD", "register:40f0:8", ["const:47f210:8", "const:4:8"]]
+ 0047f210 ["CALL", null, ["callee:00c58120:8"]]
- 0047f1d0 bytes a0631f94
+ 0047f210 bytes c4631f94
- 0047f1fc ["INT_ADD", "register:40f0:8", ["const:47f1fc:8", "const:4:8"]]
- 0047f1fc ["CALL", null, ["callee:00c58120:8"]]
+ 0047f23c ["INT_ADD", "register:40f0:8", ["const:47f23c:8", "const:4:8"]]
+ 0047f23c ["CALL", null, ["callee:00c58120:8"]]
- 0047f1fc bytes 95631f94
+ 0047f23c bytes b9631f94
~~~


<a id="compare-39ea157bba02af3174d8b04d04fdae10"></a>

### [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) → [`0047f290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f290.md) FUN_0047f290

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) · 呼出先 3件 [`0047f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 3件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047f49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f49c.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) · 呼出先 3件 [`0047f39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f39c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f2c4) · [`0047f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f2f4) · [`0047f324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f324)
- 新版 `0047f304`（命令位置の公開資料なし） · `0047f334`（命令位置の公開資料なし） · `0047f364`（命令位置の公開資料なし）

~~~diff
- 0047f2c4 ["INT_ADD", "register:40f0:8", ["const:47f2c4:8", "const:4:8"]]
- 0047f2c4 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f304 ["INT_ADD", "register:40f0:8", ["const:47f304:8", "const:4:8"]]
+ 0047f304 ["CALL", null, ["callee:00c58120:8"]]
- 0047f2c4 bytes 63631f94
+ 0047f304 bytes 87631f94
- 0047f2f4 ["INT_ADD", "register:40f0:8", ["const:47f2f4:8", "const:4:8"]]
- 0047f2f4 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f334 ["INT_ADD", "register:40f0:8", ["const:47f334:8", "const:4:8"]]
+ 0047f334 ["CALL", null, ["callee:00c58120:8"]]
- 0047f2f4 bytes 57631f94
+ 0047f334 bytes 7b631f94
- 0047f324 ["INT_ADD", "register:40f0:8", ["const:47f324:8", "const:4:8"]]
- 0047f324 ["CALL", null, ["callee:0047f39c:8"]]
+ 0047f364 ["INT_ADD", "register:40f0:8", ["const:47f364:8", "const:4:8"]]
+ 0047f364 ["CALL", null, ["callee:0047f39c:8"]]
- 0047f324 bytes 0e000094
+ 0047f364 bytes 0e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba36b17996d84ed6b8c16b012f540a0"></a>

### [`0047f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md) → [`0047f39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f39c.md) FUN_0047f39c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0047f290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f290.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md#insn-0047f3c8) · [`0047f3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md#insn-0047f3f8)
- 新版 `0047f408`（命令位置の公開資料なし） · `0047f438`（命令位置の公開資料なし）

~~~diff
- 0047f3c8 ["INT_ADD", "register:40f0:8", ["const:47f3c8:8", "const:4:8"]]
- 0047f3c8 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f408 ["INT_ADD", "register:40f0:8", ["const:47f408:8", "const:4:8"]]
+ 0047f408 ["CALL", null, ["callee:00c58120:8"]]
- 0047f3c8 bytes 22631f94
+ 0047f408 bytes 46631f94
- 0047f3f8 ["INT_ADD", "register:40f0:8", ["const:47f3f8:8", "const:4:8"]]
- 0047f3f8 ["CALL", null, ["callee:00c58120:8"]]
+ 0047f438 ["INT_ADD", "register:40f0:8", ["const:47f438:8", "const:4:8"]]
+ 0047f438 ["CALL", null, ["callee:00c58120:8"]]
- 0047f3f8 bytes 16631f94
+ 0047f438 bytes 3a631f94
~~~


<a id="compare-03b7fb58b0bc05af4ef0fb798bce131a"></a>

### [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) → [`0047f49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f49c.md) FUN_0047f49c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) [`0047f58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047f290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f290.md) [`0047f5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f5cc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f4c4) · [`0047f4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f4d8) · [`0047f508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f508)
- 新版 `0047f504`（命令位置の公開資料なし） · `0047f518`（命令位置の公開資料なし） · `0047f548`（命令位置の公開資料なし）

~~~diff
- 0047f4c4 ["INT_ADD", "register:40f0:8", ["const:47f4c4:8", "const:4:8"]]
- 0047f4c4 ["CALL", null, ["callee:0047f290:8"]]
+ 0047f504 ["INT_ADD", "register:40f0:8", ["const:47f504:8", "const:4:8"]]
+ 0047f504 ["CALL", null, ["callee:0047f290:8"]]
- 0047f4c4 bytes 63ffff97
+ 0047f504 bytes 63ffff97
- 0047f4d8 ["INT_ADD", "register:40f0:8", ["const:47f4d8:8", "const:4:8"]]
- 0047f4d8 ["CALL", null, ["callee:0047f290:8"]]
+ 0047f518 ["INT_ADD", "register:40f0:8", ["const:47f518:8", "const:4:8"]]
+ 0047f518 ["CALL", null, ["callee:0047f290:8"]]
- 0047f4d8 bytes 5effff97
+ 0047f518 bytes 5effff97
- 0047f508 ["INT_ADD", "register:40f0:8", ["const:47f508:8", "const:4:8"]]
- 0047f508 ["CALL", null, ["callee:0047f5cc:8"]]
+ 0047f548 ["INT_ADD", "register:40f0:8", ["const:47f548:8", "const:4:8"]]
+ 0047f548 ["CALL", null, ["callee:0047f5cc:8"]]
- 0047f508 bytes 21000094
+ 0047f548 bytes 21000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc91df41b4530cc1d6ffb4e345a56dc"></a>

### [`0047f58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md) → [`0047f5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f5cc.md) FUN_0047f5cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0047f49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f49c.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f5ac) · [`0047f5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f5e4) · [`0047f610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f610)
- 新版 `0047f5ec`（命令位置の公開資料なし） · `0047f624`（命令位置の公開資料なし） · `0047f650`（命令位置の公開資料なし）

~~~diff
- 0047f5ac ["INT_ADD", "register:40f0:8", ["const:47f5ac:8", "const:4:8"]]
- 0047f5ac ["CALL", null, ["callee:00c57f60:8"]]
+ 0047f5ec ["INT_ADD", "register:40f0:8", ["const:47f5ec:8", "const:4:8"]]
+ 0047f5ec ["CALL", null, ["callee:00c57f60:8"]]
- 0047f5ac bytes 39621f94
+ 0047f5ec bytes 5d621f94
- 0047f5e4 ["INT_ADD", "register:40f0:8", ["const:47f5e4:8", "const:4:8"]]
- 0047f5e4 ["CALL", null, ["callee:0043bb60:8"]]
+ 0047f624 ["INT_ADD", "register:40f0:8", ["const:47f624:8", "const:4:8"]]
+ 0047f624 ["CALL", null, ["callee:0043bb60:8"]]
- 0047f5e4 bytes 4ff1fe97
+ 0047f624 bytes 4ff1fe97
- 0047f610 ["INT_ADD", "register:40f0:8", ["const:47f610:8", "const:4:8"]]
- 0047f610 ["CALL", null, ["callee:0043bb60:8"]]
+ 0047f650 ["INT_ADD", "register:40f0:8", ["const:47f650:8", "const:4:8"]]
+ 0047f650 ["CALL", null, ["callee:0043bb60:8"]]
- 0047f610 bytes 44f1fe97
+ 0047f650 bytes 44f1fe97
~~~


<a id="compare-3b3f4186b2cdccea4c51945bbbbb35db"></a>

### [`0047f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md) → [`0047f6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f6ac.md) FUN_0047f6ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f694) · [`0047f6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f6a4) · [`0047f6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f6b4)
- 新版 `0047f6d4`（命令位置の公開資料なし） · `0047f6e4`（命令位置の公開資料なし） · `0047f6f4`（命令位置の公開資料なし）

~~~diff
- 0047f694 ["INT_ADD", "register:40f0:8", ["const:47f694:8", "const:4:8"]]
- 0047f694 ["CALL", null, ["callee:00c57f50:8"]]
+ 0047f6d4 ["INT_ADD", "register:40f0:8", ["const:47f6d4:8", "const:4:8"]]
+ 0047f6d4 ["CALL", null, ["callee:00c57f50:8"]]
- 0047f694 bytes fb611f94
+ 0047f6d4 bytes 1f621f94
- 0047f6a4 ["INT_ADD", "register:40f0:8", ["const:47f6a4:8", "const:4:8"]]
- 0047f6a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047f6e4 ["INT_ADD", "register:40f0:8", ["const:47f6e4:8", "const:4:8"]]
+ 0047f6e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0047f6a4 bytes 03621f94
+ 0047f6e4 bytes 27621f94
- 0047f6b4 ["INT_ADD", "register:40f0:8", ["const:47f6b4:8", "const:4:8"]]
- 0047f6b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047f6f4 ["INT_ADD", "register:40f0:8", ["const:47f6f4:8", "const:4:8"]]
+ 0047f6f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0047f6b4 bytes ff611f94
+ 0047f6f4 bytes 23621f94
~~~


<a id="compare-142016b70f59863f78bdbd5cb050ce7b"></a>

### [`0047f97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md) → [`0047f9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f9bc.md) FUN_0047f9bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) · 呼出先 2件 [`00c58530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58530.md) [`00c58540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58540.md)
- 新版 呼出元 1件 [`0047f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f714.md) · 呼出先 2件 [`00c58600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58600.md) [`00c58610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md#insn-0047f98c)
- 新版 `0047f9cc`（命令位置の公開資料なし）

~~~diff
- 0047f98c ["INT_ADD", "register:40f0:8", ["const:47f98c:8", "const:4:8"]]
- 0047f98c ["CALL", null, ["callee:00c58600:8"]]
+ 0047f9cc ["INT_ADD", "register:40f0:8", ["const:47f9cc:8", "const:4:8"]]
+ 0047f9cc ["CALL", null, ["callee:00c58600:8"]]
- 0047f98c bytes e9621f94
+ 0047f9cc bytes 0d631f94
~~~


<a id="compare-d5d4db2b7e7f0feed0390ae136d0a942"></a>

### [`0047fc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md) → [`0047fcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fcac.md) FUN_0047fcac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 1件 [`0047f85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f85c.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047fc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fc94) · [`0047fca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fca4) · [`0047fcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fcc0)
- 新版 `0047fcd4`（命令位置の公開資料なし） · `0047fce4`（命令位置の公開資料なし） · `0047fd00`（命令位置の公開資料なし）

~~~diff
- 0047fc94 ["INT_ADD", "register:40f0:8", ["const:47fc94:8", "const:4:8"]]
- 0047fc94 ["CALL", null, ["callee:00c58200:8"]]
+ 0047fcd4 ["INT_ADD", "register:40f0:8", ["const:47fcd4:8", "const:4:8"]]
+ 0047fcd4 ["CALL", null, ["callee:00c58200:8"]]
- 0047fc94 bytes 27611f94
+ 0047fcd4 bytes 4b611f94
- 0047fca4 ["INT_ADD", "register:40f0:8", ["const:47fca4:8", "const:4:8"]]
- 0047fca4 ["CALL", null, ["callee:00c58210:8"]]
+ 0047fce4 ["INT_ADD", "register:40f0:8", ["const:47fce4:8", "const:4:8"]]
+ 0047fce4 ["CALL", null, ["callee:00c58210:8"]]
- 0047fca4 bytes 27611f94
+ 0047fce4 bytes 4b611f94
- 0047fcc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047fcc0 ["INT_ADD", "register:40f0:8", ["const:47fcc0:8", "const:4:8"]]
- 0047fcc0 ["CALLIND", null, ["register:0:8"]]
+ 0047fd00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047fd00 ["INT_ADD", "register:40f0:8", ["const:47fd00:8", "const:4:8"]]
+ 0047fd00 ["CALLIND", null, ["register:0:8"]]
- 0047fcc0 bytes 00013fd6
+ 0047fd00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc1c8e48ce52b80be4d67aa51513026"></a>

### [`0047fd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md) → [`0047fd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fd78.md) FUN_0047fd78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047fd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md#insn-0047fd60) · [`0047fd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md#insn-0047fd68)
- 新版 `0047fda0`（命令位置の公開資料なし） · `0047fda8`（命令位置の公開資料なし）

~~~diff
- 0047fd60 ["INT_ADD", "register:40f0:8", ["const:47fd60:8", "const:4:8"]]
- 0047fd60 ["CALL", null, ["callee:00c58220:8"]]
+ 0047fda0 ["INT_ADD", "register:40f0:8", ["const:47fda0:8", "const:4:8"]]
+ 0047fda0 ["CALL", null, ["callee:00c58220:8"]]
- 0047fd60 bytes fc601f94
+ 0047fda0 bytes 20611f94
- 0047fd68 ["INT_ADD", "register:40f0:8", ["const:47fd68:8", "const:4:8"]]
- 0047fd68 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047fda8 ["INT_ADD", "register:40f0:8", ["const:47fda8:8", "const:4:8"]]
+ 0047fda8 ["CALL", null, ["callee:00c57f80:8"]]
- 0047fd68 bytes 52601f94
+ 0047fda8 bytes 76601f94
~~~


<a id="compare-4cb4d7f11491682232cd128f33fc27d7"></a>

### [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) → [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) FUN_00480158

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 23件 [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) [`0066b364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b364.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 23件 [`005c0bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0bd8.md) [`0066b3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b3a4.md) [`006db0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md) [`0072ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072ed80.md) [`0073299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/0073299c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md#insn-00480144) · [`00480174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md#insn-00480174)
- 新版 `00480184`（命令位置の公開資料なし） · `004801b4`（命令位置の公開資料なし）

~~~diff
- 00480144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480144 ["INT_ADD", "register:40f0:8", ["const:480144:8", "const:4:8"]]
- 00480144 ["CALLIND", null, ["register:0:8"]]
+ 00480184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480184 ["INT_ADD", "register:40f0:8", ["const:480184:8", "const:4:8"]]
+ 00480184 ["CALLIND", null, ["register:0:8"]]
- 00480144 bytes 00013fd6
+ 00480184 bytes 00013fd6
- 00480174 ["INT_ADD", "register:40f0:8", ["const:480174:8", "const:4:8"]]
- 00480174 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004801b4 ["INT_ADD", "register:40f0:8", ["const:4801b4:8", "const:4:8"]]
+ 004801b4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480174 bytes 5b5f1f94
+ 004801b4 bytes 7f5f1f94
~~~


<a id="compare-cb9910a9eacce3e8cd4b1732d4c06473"></a>

### [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) → [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) FUN_004801b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) [`00675b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b94.md) [`006a48fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a48fc.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 26件 [`005c0bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0bd8.md) [`00675bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675bd4.md) [`006a4954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4954.md) [`006db0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md) [`00738804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738804.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004801a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md#insn-004801a4) · [`004801d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md#insn-004801d4)
- 新版 `004801e4`（命令位置の公開資料なし） · `00480214`（命令位置の公開資料なし）

~~~diff
- 004801a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004801a4 ["INT_ADD", "register:40f0:8", ["const:4801a4:8", "const:4:8"]]
- 004801a4 ["CALLIND", null, ["register:0:8"]]
+ 004801e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004801e4 ["INT_ADD", "register:40f0:8", ["const:4801e4:8", "const:4:8"]]
+ 004801e4 ["CALLIND", null, ["register:0:8"]]
- 004801a4 bytes 00013fd6
+ 004801e4 bytes 00013fd6
- 004801d4 ["INT_ADD", "register:40f0:8", ["const:4801d4:8", "const:4:8"]]
- 004801d4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480214 ["INT_ADD", "register:40f0:8", ["const:480214:8", "const:4:8"]]
+ 00480214 ["CALL", null, ["callee:00c57fb0:8"]]
- 004801d4 bytes 435f1f94
+ 00480214 bytes 675f1f94
~~~


