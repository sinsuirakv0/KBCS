# v16.0.1 → v16.0.2 · 要調査の変更候補 (21)

[一覧の目次](README.md)

<a id="compare-c381ea201373bb09a6093c6f54e52086"></a>

### [`006e03b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e03b4.md) → [`006e040c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e040c.md) FUN_006e040c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e03f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e03b4.md#insn-006e03f4) · [`006e0404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e03b4.md#insn-006e0404) · [`006e0414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e03b4.md#insn-006e0414)
- 新版 `006e044c`（命令位置の公開資料なし） · `006e045c`（命令位置の公開資料なし） · `006e046c`（命令位置の公開資料なし）

~~~diff
- 006e03f4 ["INT_ADD", "register:40f0:8", ["const:6e03f4:8", "const:4:8"]]
- 006e03f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e044c ["INT_ADD", "register:40f0:8", ["const:6e044c:8", "const:4:8"]]
+ 006e044c ["CALL", null, ["callee:00c57f80:8"]]
- 006e03f4 bytes afde1594
+ 006e044c bytes cdde1594
- 006e0404 ["INT_ADD", "register:40f0:8", ["const:6e0404:8", "const:4:8"]]
- 006e0404 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e045c ["INT_ADD", "register:40f0:8", ["const:6e045c:8", "const:4:8"]]
+ 006e045c ["CALL", null, ["callee:00c57f80:8"]]
- 006e0404 bytes abde1594
+ 006e045c bytes c9de1594
- 006e0414 ["INT_ADD", "register:40f0:8", ["const:6e0414:8", "const:4:8"]]
- 006e0414 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e046c ["INT_ADD", "register:40f0:8", ["const:6e046c:8", "const:4:8"]]
+ 006e046c ["CALL", null, ["callee:00c57f80:8"]]
- 006e0414 bytes a7de1594
+ 006e046c bytes c5de1594
~~~


<a id="compare-e4b200bc189a6339c5cc95d3ede1bd0e"></a>

### [`006e0430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0430.md) → [`006e0488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0488.md) FUN_006e0488

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e0470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0430.md#insn-006e0470) · [`006e0480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0430.md#insn-006e0480) · [`006e0490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0430.md#insn-006e0490)
- 新版 `006e04c8`（命令位置の公開資料なし） · `006e04d8`（命令位置の公開資料なし） · `006e04e8`（命令位置の公開資料なし）

~~~diff
- 006e0470 ["INT_ADD", "register:40f0:8", ["const:6e0470:8", "const:4:8"]]
- 006e0470 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e04c8 ["INT_ADD", "register:40f0:8", ["const:6e04c8:8", "const:4:8"]]
+ 006e04c8 ["CALL", null, ["callee:00c57f80:8"]]
- 006e0470 bytes 90de1594
+ 006e04c8 bytes aede1594
- 006e0480 ["INT_ADD", "register:40f0:8", ["const:6e0480:8", "const:4:8"]]
- 006e0480 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e04d8 ["INT_ADD", "register:40f0:8", ["const:6e04d8:8", "const:4:8"]]
+ 006e04d8 ["CALL", null, ["callee:00c57f80:8"]]
- 006e0480 bytes 8cde1594
+ 006e04d8 bytes aade1594
- 006e0490 ["INT_ADD", "register:40f0:8", ["const:6e0490:8", "const:4:8"]]
- 006e0490 ["CALL", null, ["callee:00c57f80:8"]]
+ 006e04e8 ["INT_ADD", "register:40f0:8", ["const:6e04e8:8", "const:4:8"]]
+ 006e04e8 ["CALL", null, ["callee:00c57f80:8"]]
- 006e0490 bytes 88de1594
+ 006e04e8 bytes a6de1594
~~~


<a id="compare-b56db97b8b56debe54c65c0b860ba1a0"></a>

### [`006e0588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0588.md) → [`006e05e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e05e0.md) FUN_006e05e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e05b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0588.md#insn-006e05b8) · [`006e05d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0588.md#insn-006e05d0) · [`006e05ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0588.md#insn-006e05ec)
- 新版 `006e0610`（命令位置の公開資料なし） · `006e0628`（命令位置の公開資料なし） · `006e0644`（命令位置の公開資料なし）

~~~diff
- 006e05b8 ["INT_ADD", "register:40f0:8", ["const:6e05b8:8", "const:4:8"]]
- 006e05b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 006e0610 ["INT_ADD", "register:40f0:8", ["const:6e0610:8", "const:4:8"]]
+ 006e0610 ["CALL", null, ["callee:00c57f60:8"]]
- 006e05b8 bytes 36de1594
+ 006e0610 bytes 54de1594
- 006e05d0 ["INT_ADD", "register:40f0:8", ["const:6e05d0:8", "const:4:8"]]
- 006e05d0 ["CALL", null, ["callee:00c580d0:8"]]
+ 006e0628 ["INT_ADD", "register:40f0:8", ["const:6e0628:8", "const:4:8"]]
+ 006e0628 ["CALL", null, ["callee:00c580d0:8"]]
- 006e05d0 bytes 8cde1594
+ 006e0628 bytes aade1594
- 006e05ec ["INT_ADD", "register:40f0:8", ["const:6e05ec:8", "const:4:8"]]
- 006e05ec ["CALL", null, ["callee:00470880:8"]]
+ 006e0644 ["INT_ADD", "register:40f0:8", ["const:6e0644:8", "const:4:8"]]
+ 006e0644 ["CALL", null, ["callee:00470880:8"]]
- 006e05ec bytes 9540f697
+ 006e0644 bytes 8f40f697
~~~


<a id="compare-1929514c3a296107022849a7b0f50fa7"></a>

### [`006e1c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1c80.md) → [`006e1cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1cd8.md) FUN_006e1cd8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e15e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e15e0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`006e1638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e1ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1c80.md#insn-006e1ccc) · [`006e1cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1c80.md#insn-006e1cf8) · [`006e1d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1c80.md#insn-006e1d24)
- 新版 `006e1d24`（命令位置の公開資料なし） · `006e1d50`（命令位置の公開資料なし） · `006e1d7c`（命令位置の公開資料なし）

~~~diff
- 006e1ccc ["INT_ADD", "register:40f0:8", ["const:6e1ccc:8", "const:4:8"]]
- 006e1ccc ["CALL", null, ["callee:0043bb60:8"]]
+ 006e1d24 ["INT_ADD", "register:40f0:8", ["const:6e1d24:8", "const:4:8"]]
+ 006e1d24 ["CALL", null, ["callee:0043bb60:8"]]
- 006e1ccc bytes 9567f597
+ 006e1d24 bytes 8f67f597
- 006e1cf8 ["INT_ADD", "register:40f0:8", ["const:6e1cf8:8", "const:4:8"]]
- 006e1cf8 ["CALL", null, ["callee:0043bb60:8"]]
+ 006e1d50 ["INT_ADD", "register:40f0:8", ["const:6e1d50:8", "const:4:8"]]
+ 006e1d50 ["CALL", null, ["callee:0043bb60:8"]]
- 006e1cf8 bytes 8a67f597
+ 006e1d50 bytes 8467f597
- 006e1d24 ["INT_ADD", "register:40f0:8", ["const:6e1d24:8", "const:4:8"]]
- 006e1d24 ["CALL", null, ["callee:0043bb60:8"]]
+ 006e1d7c ["INT_ADD", "register:40f0:8", ["const:6e1d7c:8", "const:4:8"]]
+ 006e1d7c ["CALL", null, ["callee:0043bb60:8"]]
- 006e1d24 bytes 7f67f597
+ 006e1d7c bytes 7967f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aa3ab58b75f0f087c3a9d98c31547bd"></a>

### [`006e41c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e41c8.md) → [`006e4220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4220.md) FUN_006e4220

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e41c8.md#insn-006e41dc) · [`006e41f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e41c8.md#insn-006e41f4) · [`006e420c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e41c8.md#insn-006e420c)
- 新版 `006e4234`（命令位置の公開資料なし） · `006e424c`（命令位置の公開資料なし） · `006e4264`（命令位置の公開資料なし）

~~~diff
- 006e41dc ["INT_ADD", "register:40f0:8", ["const:6e41dc:8", "const:4:8"]]
- 006e41dc ["CALL", null, ["callee:00851550:8"]]
+ 006e4234 ["INT_ADD", "register:40f0:8", ["const:6e4234:8", "const:4:8"]]
+ 006e4234 ["CALL", null, ["callee:00851550:8"]]
- 006e41dc bytes c7b40594
+ 006e4234 bytes c7b40594
- 006e41f4 ["INT_ADD", "register:40f0:8", ["const:6e41f4:8", "const:4:8"]]
- 006e41f4 ["CALL", null, ["callee:00851550:8"]]
+ 006e424c ["INT_ADD", "register:40f0:8", ["const:6e424c:8", "const:4:8"]]
+ 006e424c ["CALL", null, ["callee:00851550:8"]]
- 006e41f4 bytes c1b40594
+ 006e424c bytes c1b40594
- 006e420c ["INT_ADD", "register:40f0:8", ["const:6e420c:8", "const:4:8"]]
- 006e420c ["CALL", null, ["callee:00851550:8"]]
+ 006e4264 ["INT_ADD", "register:40f0:8", ["const:6e4264:8", "const:4:8"]]
+ 006e4264 ["CALL", null, ["callee:00851550:8"]]
- 006e420c bytes bbb40594
+ 006e4264 bytes bbb40594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2603c812f4031b4cc153f2353c799bbb"></a>

### [`006e4244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4244.md) → [`006e429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e429c.md) FUN_006e429c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e4260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4244.md#insn-006e4260) · [`006e4278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4244.md#insn-006e4278) · [`006e4290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4244.md#insn-006e4290)
- 新版 `006e42b8`（命令位置の公開資料なし） · `006e42d0`（命令位置の公開資料なし） · `006e42e8`（命令位置の公開資料なし）

~~~diff
- 006e4260 ["INT_ADD", "register:40f0:8", ["const:6e4260:8", "const:4:8"]]
- 006e4260 ["CALL", null, ["callee:00851550:8"]]
+ 006e42b8 ["INT_ADD", "register:40f0:8", ["const:6e42b8:8", "const:4:8"]]
+ 006e42b8 ["CALL", null, ["callee:00851550:8"]]
- 006e4260 bytes a6b40594
+ 006e42b8 bytes a6b40594
- 006e4278 ["INT_ADD", "register:40f0:8", ["const:6e4278:8", "const:4:8"]]
- 006e4278 ["CALL", null, ["callee:00851550:8"]]
+ 006e42d0 ["INT_ADD", "register:40f0:8", ["const:6e42d0:8", "const:4:8"]]
+ 006e42d0 ["CALL", null, ["callee:00851550:8"]]
- 006e4278 bytes a0b40594
+ 006e42d0 bytes a0b40594
- 006e4290 ["INT_ADD", "register:40f0:8", ["const:6e4290:8", "const:4:8"]]
- 006e4290 ["CALL", null, ["callee:00851550:8"]]
+ 006e42e8 ["INT_ADD", "register:40f0:8", ["const:6e42e8:8", "const:4:8"]]
+ 006e42e8 ["CALL", null, ["callee:00851550:8"]]
- 006e4290 bytes 9ab40594
+ 006e42e8 bytes 9ab40594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da319bd8b605edca6317b4e7e4e45f7"></a>

### [`006e8b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8b54.md) → [`006e8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md) FUN_006e8bac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 3件 [`006c41c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c41c0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 3件 [`006c4218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e8b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8b54.md#insn-006e8b68) · [`006e8b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8b54.md#insn-006e8b70) · [`006e8b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8b54.md#insn-006e8b78)
- 新版 `006e8bc0`（命令位置の公開資料なし） · `006e8bc8`（命令位置の公開資料なし） · `006e8bd0`（命令位置の公開資料なし）

~~~diff
- 006e8b68 ["INT_ADD", "register:40f0:8", ["const:6e8b68:8", "const:4:8"]]
- 006e8b68 ["CALL", null, ["callee:006c4218:8"]]
+ 006e8bc0 ["INT_ADD", "register:40f0:8", ["const:6e8bc0:8", "const:4:8"]]
+ 006e8bc0 ["CALL", null, ["callee:006c4218:8"]]
- 006e8b68 bytes 966dff97
+ 006e8bc0 bytes 966dff97
- 006e8b70 ["INT_ADD", "register:40f0:8", ["const:6e8b70:8", "const:4:8"]]
- 006e8b70 ["CALL", null, ["callee:006c4218:8"]]
+ 006e8bc8 ["INT_ADD", "register:40f0:8", ["const:6e8bc8:8", "const:4:8"]]
+ 006e8bc8 ["CALL", null, ["callee:006c4218:8"]]
- 006e8b70 bytes 946dff97
+ 006e8bc8 bytes 946dff97
- 006e8b78 ["INT_ADD", "register:40f0:8", ["const:6e8b78:8", "const:4:8"]]
- 006e8b78 ["CALL", null, ["callee:006c4218:8"]]
+ 006e8bd0 ["INT_ADD", "register:40f0:8", ["const:6e8bd0:8", "const:4:8"]]
+ 006e8bd0 ["CALL", null, ["callee:006c4218:8"]]
- 006e8b78 bytes 926dff97
+ 006e8bd0 bytes 926dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b5fa1073ea1ba1a3f5d681a82adba5"></a>

### [`006ec6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ec/006ec6cc.md) → [`006ec724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ec724.md) FUN_006ec724

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ec6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ec/006ec6cc.md#insn-006ec6f4) · [`006ec708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ec/006ec6cc.md#insn-006ec708) · [`006ec710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ec/006ec6cc.md#insn-006ec710)
- 新版 `006ec74c`（命令位置の公開資料なし） · `006ec760`（命令位置の公開資料なし） · `006ec768`（命令位置の公開資料なし）

~~~diff
- 006ec6f4 ["INT_ADD", "register:40f0:8", ["const:6ec6f4:8", "const:4:8"]]
- 006ec6f4 ["CALL", null, ["callee:00c53da0:8"]]
+ 006ec74c ["INT_ADD", "register:40f0:8", ["const:6ec74c:8", "const:4:8"]]
+ 006ec74c ["CALL", null, ["callee:00c53da0:8"]]
- 006ec6f4 bytes 839d1594
+ 006ec74c bytes 959d1594
- 006ec708 ["COPY", "register:0:8", ["register:4040:8"]]
- 006ec708 ["INT_ADD", "register:40f0:8", ["const:6ec708:8", "const:4:8"]]
- 006ec708 ["CALLIND", null, ["register:0:8"]]
+ 006ec760 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006ec760 ["INT_ADD", "register:40f0:8", ["const:6ec760:8", "const:4:8"]]
+ 006ec760 ["CALLIND", null, ["register:0:8"]]
- 006ec708 bytes 00013fd6
+ 006ec760 bytes 00013fd6
- 006ec710 ["INT_ADD", "register:40f0:8", ["const:6ec710:8", "const:4:8"]]
- 006ec710 ["CALL", null, ["callee:00c57f50:8"]]
+ 006ec768 ["INT_ADD", "register:40f0:8", ["const:6ec768:8", "const:4:8"]]
+ 006ec768 ["CALL", null, ["callee:00c57f50:8"]]
- 006ec710 bytes dcad1594
+ 006ec768 bytes faad1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b30d072b815b47ec664195e2b4fb043"></a>

### [`006f040c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f040c.md) → [`006f0464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0464.md) FUN_006f0464

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006ef744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ef/006ef744.md) [`006fda2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`006ef79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ef/006ef79c.md) [`006fda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`00ab4d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab4/00ab4d70.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f0430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f040c.md#insn-006f0430) · [`006f0478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f040c.md#insn-006f0478) · [`006f0498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f040c.md#insn-006f0498)
- 新版 `006f0488`（命令位置の公開資料なし） · `006f04d0`（命令位置の公開資料なし） · `006f04f0`（命令位置の公開資料なし）

~~~diff
- 006f0430 ["INT_ADD", "register:40f0:8", ["const:6f0430:8", "const:4:8"]]
- 006f0430 ["CALL", null, ["callee:00c580b0:8"]]
+ 006f0488 ["INT_ADD", "register:40f0:8", ["const:6f0488:8", "const:4:8"]]
+ 006f0488 ["CALL", null, ["callee:00c580b0:8"]]
- 006f0430 bytes ec9e1594
+ 006f0488 bytes 0a9f1594
- 006f0478 ["INT_ADD", "register:40f0:8", ["const:6f0478:8", "const:4:8"]]
- 006f0478 ["CALL", null, ["callee:00c57f60:8"]]
+ 006f04d0 ["INT_ADD", "register:40f0:8", ["const:6f04d0:8", "const:4:8"]]
+ 006f04d0 ["CALL", null, ["callee:00c57f60:8"]]
- 006f0478 bytes 869e1594
+ 006f04d0 bytes a49e1594
- 006f0498 ["INT_ADD", "register:40f0:8", ["const:6f0498:8", "const:4:8"]]
- 006f0498 ["CALL", null, ["callee:00c58010:8"]]
+ 006f04f0 ["INT_ADD", "register:40f0:8", ["const:6f04f0:8", "const:4:8"]]
+ 006f04f0 ["CALL", null, ["callee:00c58010:8"]]
- 006f0498 bytes aa9e1594
+ 006f04f0 bytes c89e1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaaa595b5ef818b896a635629e6f4a82"></a>

### [`006f15c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f15c0.md) → [`006f1618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f1618.md) FUN_006f1618

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 9件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f1628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f15c0.md#insn-006f1628) · [`006f1660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f15c0.md#insn-006f1660)
- 新版 `006f1680`（命令位置の公開資料なし） · `006f16b8`（命令位置の公開資料なし）

~~~diff
- 006f1628 ["INT_ADD", "register:40f0:8", ["const:6f1628:8", "const:4:8"]]
- 006f1628 ["CALL", null, ["callee:00c57f60:8"]]
+ 006f1680 ["INT_ADD", "register:40f0:8", ["const:6f1680:8", "const:4:8"]]
+ 006f1680 ["CALL", null, ["callee:00c57f60:8"]]
- 006f1628 bytes 1a9a1594
+ 006f1680 bytes 389a1594
- 006f1660 ["INT_ADD", "register:40f0:8", ["const:6f1660:8", "const:4:8"]]
- 006f1660 ["CALL", null, ["callee:0043bbe4:8"]]
+ 006f16b8 ["INT_ADD", "register:40f0:8", ["const:6f16b8:8", "const:4:8"]]
+ 006f16b8 ["CALL", null, ["callee:0043bbe4:8"]]
- 006f1660 bytes 5129f597
+ 006f16b8 bytes 4b29f597
~~~


<a id="compare-6f901a89747d98bd010bd3a3b8606520"></a>

### [`006f8654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8654.md) → [`006f86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f86ac.md) FUN_006f86ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md)
- 新版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f8690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8654.md#insn-006f8690) · [`006f86a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8654.md#insn-006f86a4)
- 新版 `006f86e8`（命令位置の公開資料なし） · `006f86fc`（命令位置の公開資料なし）

~~~diff
- 006f8690 ["INT_ADD", "register:40f0:8", ["const:6f8690:8", "const:4:8"]]
- 006f8690 ["CALL", null, ["callee:00540dbc:8"]]
+ 006f86e8 ["INT_ADD", "register:40f0:8", ["const:6f86e8:8", "const:4:8"]]
+ 006f86e8 ["CALL", null, ["callee:00540dbc:8"]]
- 006f8690 bytes bb21f997
+ 006f86e8 bytes b521f997
- 006f86a4 ["INT_ADD", "register:40f0:8", ["const:6f86a4:8", "const:4:8"]]
- 006f86a4 ["CALL", null, ["callee:0043bb60:8"]]
+ 006f86fc ["INT_ADD", "register:40f0:8", ["const:6f86fc:8", "const:4:8"]]
+ 006f86fc ["CALL", null, ["callee:0043bb60:8"]]
- 006f86a4 bytes 1f0df597
+ 006f86fc bytes 190df597
~~~


<a id="compare-dcc991995fad6fe5290b0f7713c62e75"></a>

### [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) → [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) FUN_006fb0cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`006e44e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`006fb910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md) [`006fbcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md) · 呼出先 4件 [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 10件 [`006e4538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) [`006fb968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md) [`006fbd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md) · 呼出先 4件 [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fb090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md#insn-006fb090) · [`006fb09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md#insn-006fb09c) · [`006fb0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md#insn-006fb0b0)
- 新版 `006fb0e8`（命令位置の公開資料なし） · `006fb0f4`（命令位置の公開資料なし） · `006fb108`（命令位置の公開資料なし）

~~~diff
- 006fb090 ["INT_ADD", "register:40f0:8", ["const:6fb090:8", "const:4:8"]]
- 006fb090 ["CALL", null, ["local:b0:8"]]
+ 006fb0e8 ["INT_ADD", "register:40f0:8", ["const:6fb0e8:8", "const:4:8"]]
+ 006fb0e8 ["CALL", null, ["local:b0:8"]]
- 006fb090 bytes f9ffff97
+ 006fb0e8 bytes f9ffff97
- 006fb09c ["INT_ADD", "register:40f0:8", ["const:6fb09c:8", "const:4:8"]]
- 006fb09c ["CALL", null, ["local:b0:8"]]
+ 006fb0f4 ["INT_ADD", "register:40f0:8", ["const:6fb0f4:8", "const:4:8"]]
+ 006fb0f4 ["CALL", null, ["local:b0:8"]]
- 006fb09c bytes f6ffff97
+ 006fb0f4 bytes f6ffff97
- 006fb0b0 ["INT_ADD", "register:40f0:8", ["const:6fb0b0:8", "const:4:8"]]
- 006fb0b0 ["CALL", null, ["callee:00c53da0:8"]]
+ 006fb108 ["INT_ADD", "register:40f0:8", ["const:6fb108:8", "const:4:8"]]
+ 006fb108 ["CALL", null, ["callee:00c53da0:8"]]
- 006fb0b0 bytes 14631594
+ 006fb108 bytes 26631594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-843b67fe6f9f37a58263380d50301797"></a>

### [`006ff1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md) → [`006ff254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff254.md) FUN_006ff254

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ff228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff228) · [`006ff22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff22c) · [`006ff234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff234)
- 新版 `006ff280`（命令位置の公開資料なし） · `006ff284`（命令位置の公開資料なし） · `006ff28c`（命令位置の公開資料なし）

~~~diff
- 006ff228 ["INT_ADD", "register:40f0:8", ["const:6ff228:8", "const:4:8"]]
- 006ff228 ["CALL", null, ["callee:004700f4:8"]]
+ 006ff280 ["INT_ADD", "register:40f0:8", ["const:6ff280:8", "const:4:8"]]
+ 006ff280 ["CALL", null, ["callee:004700f4:8"]]
- 006ff228 bytes a3c3f597
+ 006ff280 bytes 9dc3f597
- 006ff22c ["INT_ADD", "register:40f0:8", ["const:6ff22c:8", "const:4:8"]]
- 006ff22c ["CALL", null, ["callee:004678a0:8"]]
+ 006ff284 ["INT_ADD", "register:40f0:8", ["const:6ff284:8", "const:4:8"]]
+ 006ff284 ["CALL", null, ["callee:004678a0:8"]]
- 006ff22c bytes 8da1f597
+ 006ff284 bytes 87a1f597
- 006ff234 ["INT_ADD", "register:40f0:8", ["const:6ff234:8", "const:4:8"]]
- 006ff234 ["CALL", null, ["callee:00851550:8"]]
+ 006ff28c ["INT_ADD", "register:40f0:8", ["const:6ff28c:8", "const:4:8"]]
+ 006ff28c ["CALL", null, ["callee:00851550:8"]]
- 006ff234 bytes b1480594
+ 006ff28c bytes b1480594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b3398ff9a67b1cd6f5e0b3916a77fc9"></a>

### [`00700510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700510.md) → [`00700568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700568.md) FUN_00700568

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00700530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700510.md#insn-00700530)
- 新版 `00700588`（命令位置の公開資料なし）

~~~diff
- 00700530 ["INT_ADD", "register:40f0:8", ["const:700530:8", "const:4:8"]]
- 00700530 ["CALL", null, ["callee:00c57f80:8"]]
+ 00700588 ["INT_ADD", "register:40f0:8", ["const:700588:8", "const:4:8"]]
+ 00700588 ["CALL", null, ["callee:00c57f80:8"]]
- 00700530 bytes 605e1594
+ 00700588 bytes 7e5e1594
~~~


<a id="compare-4a27d2e5cf1ac18e43505107d5ded498"></a>

### [`00707d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md) → [`00707dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707dc8.md) FUN_00707dc8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 2件 [`00afc50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc50c.md) [`00afc568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc568.md)
- 新版 呼出元 3件 [`005f2da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f2da8.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 2件 [`00afc5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc5a8.md) [`00afc604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc604.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md#insn-00707d98) · [`00707db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md#insn-00707db0) · [`00707dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md#insn-00707dc8)
- 新版 `00707df0`（命令位置の公開資料なし） · `00707e08`（命令位置の公開資料なし） · `00707e20`（命令位置の公開資料なし）

~~~diff
- 00707d98 ["INT_ADD", "register:40f0:8", ["const:707d98:8", "const:4:8"]]
- 00707d98 ["CALL", null, ["callee:00afc5a8:8"]]
+ 00707df0 ["INT_ADD", "register:40f0:8", ["const:707df0:8", "const:4:8"]]
+ 00707df0 ["CALL", null, ["callee:00afc5a8:8"]]
- 00707d98 bytes ddd10f94
+ 00707df0 bytes eed10f94
- 00707db0 ["INT_ADD", "register:40f0:8", ["const:707db0:8", "const:4:8"]]
- 00707db0 ["CALL", null, ["callee:00afc5a8:8"]]
+ 00707e08 ["INT_ADD", "register:40f0:8", ["const:707e08:8", "const:4:8"]]
+ 00707e08 ["CALL", null, ["callee:00afc5a8:8"]]
- 00707db0 bytes d7d10f94
+ 00707e08 bytes e8d10f94
- 00707dc8 ["INT_ADD", "register:40f0:8", ["const:707dc8:8", "const:4:8"]]
- 00707dc8 ["CALL", null, ["callee:00afc5a8:8"]]
+ 00707e20 ["INT_ADD", "register:40f0:8", ["const:707e20:8", "const:4:8"]]
+ 00707e20 ["CALL", null, ["callee:00afc5a8:8"]]
- 00707dc8 bytes d1d10f94
+ 00707e20 bytes e2d10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36c9054460f09e48af89e9581f07fac7"></a>

### [`00707eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707eb0.md) → [`00707f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f08.md) FUN_00707f08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707eb0.md#insn-00707ec8)
- 新版 `00707f20`（命令位置の公開資料なし）

~~~diff
- 00707ec8 ["INT_ADD", "register:40f0:8", ["const:707ec8:8", "const:4:8"]]
- 00707ec8 ["CALL", null, ["callee:00676aa0:8"]]
+ 00707f20 ["INT_ADD", "register:40f0:8", ["const:707f20:8", "const:4:8"]]
+ 00707f20 ["CALL", null, ["callee:00676aa0:8"]]
- 00707ec8 bytes e6bafd97
+ 00707f20 bytes e0bafd97
~~~


<a id="compare-4e459f8f490dfcb475e992e4a28551e5"></a>

### [`0070e148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e148.md) → [`0070e1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1a0.md) FUN_0070e1a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e148.md#insn-0070e16c)
- 新版 `0070e1c4`（命令位置の公開資料なし）

~~~diff
- 0070e16c ["INT_ADD", "register:40f0:8", ["const:70e16c:8", "const:4:8"]]
- 0070e16c ["CALL", null, ["callee:0046f01c:8"]]
+ 0070e1c4 ["INT_ADD", "register:40f0:8", ["const:70e1c4:8", "const:4:8"]]
+ 0070e1c4 ["CALL", null, ["callee:0046f01c:8"]]
- 0070e16c bytes 9c83f597
+ 0070e1c4 bytes 9683f597
~~~


<a id="compare-7440d69bde7d1f92689687d41b035ab2"></a>

### [`00714124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md) → [`0071417c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/0071417c.md) FUN_0071417c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005fe25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe25c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005fe29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe29c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007141a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md#insn-007141a4) · [`007141e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md#insn-007141e0) · [`007141f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md#insn-007141f4)
- 新版 `007141fc`（命令位置の公開資料なし） · `00714238`（命令位置の公開資料なし） · `0071424c`（命令位置の公開資料なし）

~~~diff
- 007141a4 ["INT_ADD", "register:40f0:8", ["const:7141a4:8", "const:4:8"]]
- 007141a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007141fc ["INT_ADD", "register:40f0:8", ["const:7141fc:8", "const:4:8"]]
+ 007141fc ["CALL", null, ["callee:00c57f60:8"]]
- 007141a4 bytes 3b0f1594
+ 007141fc bytes 590f1594
- 007141e0 ["INT_ADD", "register:40f0:8", ["const:7141e0:8", "const:4:8"]]
- 007141e0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00714238 ["INT_ADD", "register:40f0:8", ["const:714238:8", "const:4:8"]]
+ 00714238 ["CALL", null, ["callee:00c580d0:8"]]
- 007141e0 bytes 880f1594
+ 00714238 bytes a60f1594
- 007141f4 ["INT_ADD", "register:40f0:8", ["const:7141f4:8", "const:4:8"]]
- 007141f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0071424c ["INT_ADD", "register:40f0:8", ["const:71424c:8", "const:4:8"]]
+ 0071424c ["CALL", null, ["callee:00c57f80:8"]]
- 007141f4 bytes 2f0f1594
+ 0071424c bytes 4d0f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ad94efb8dea38bda82eb1c1e75e730"></a>

### [`0071421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071421c.md) → [`00714274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714274.md) FUN_00714274

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe2d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071423c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071421c.md#insn-0071423c)
- 新版 `00714294`（命令位置の公開資料なし）

~~~diff
- 0071423c ["INT_ADD", "register:40f0:8", ["const:71423c:8", "const:4:8"]]
- 0071423c ["CALL", null, ["callee:005fe2d8:8"]]
+ 00714294 ["INT_ADD", "register:40f0:8", ["const:714294:8", "const:4:8"]]
+ 00714294 ["CALL", null, ["callee:005fe2d8:8"]]
- 0071423c bytes 17a8fb97
+ 00714294 bytes 11a8fb97
~~~


<a id="compare-e935f88223a669946376e62fd9175c47"></a>

### [`0071e2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e2f4.md) → [`0071e34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e34c.md) FUN_0071e34c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 3件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md)
- 新版 呼出元 1件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) · 呼出先 3件 [`00b3befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3befc.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e2f4.md#insn-0071e334) · [`0071e33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e2f4.md#insn-0071e33c) · [`0071e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e2f4.md#insn-0071e370)
- 新版 `0071e38c`（命令位置の公開資料なし） · `0071e394`（命令位置の公開資料なし） · `0071e3c8`（命令位置の公開資料なし）

~~~diff
- 0071e334 ["INT_ADD", "register:40f0:8", ["const:71e334:8", "const:4:8"]]
- 0071e334 ["CALL", null, ["callee:00b3bf74:8"]]
+ 0071e38c ["INT_ADD", "register:40f0:8", ["const:71e38c:8", "const:4:8"]]
+ 0071e38c ["CALL", null, ["callee:00b3bf74:8"]]
- 0071e334 bytes e9761094
+ 0071e38c bytes fa761094
- 0071e33c ["INT_ADD", "register:40f0:8", ["const:71e33c:8", "const:4:8"]]
- 0071e33c ["CALL", null, ["callee:00b3bf30:8"]]
+ 0071e394 ["INT_ADD", "register:40f0:8", ["const:71e394:8", "const:4:8"]]
+ 0071e394 ["CALL", null, ["callee:00b3bf30:8"]]
- 0071e33c bytes d6761094
+ 0071e394 bytes e7761094
- 0071e370 ["INT_ADD", "register:40f0:8", ["const:71e370:8", "const:4:8"]]
- 0071e370 ["CALL", null, ["callee:00b3bf74:8"]]
+ 0071e3c8 ["INT_ADD", "register:40f0:8", ["const:71e3c8:8", "const:4:8"]]
+ 0071e3c8 ["CALL", null, ["callee:00b3bf74:8"]]
- 0071e370 bytes da761094
+ 0071e3c8 bytes eb761094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74f984bc116e08341d94253ac1e93a8"></a>

### [`0071e7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e7cc.md) → [`0071e824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e824.md) FUN_0071e824

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 3件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md)
- 新版 呼出元 1件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) · 呼出先 3件 [`00b3befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3befc.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e7cc.md#insn-0071e7f4) · [`0071e7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e7cc.md#insn-0071e7fc)
- 新版 `0071e84c`（命令位置の公開資料なし） · `0071e854`（命令位置の公開資料なし）

~~~diff
- 0071e7f4 ["INT_ADD", "register:40f0:8", ["const:71e7f4:8", "const:4:8"]]
- 0071e7f4 ["CALL", null, ["callee:00b3bf74:8"]]
+ 0071e84c ["INT_ADD", "register:40f0:8", ["const:71e84c:8", "const:4:8"]]
+ 0071e84c ["CALL", null, ["callee:00b3bf74:8"]]
- 0071e7f4 bytes b9751094
+ 0071e84c bytes ca751094
- 0071e7fc ["INT_ADD", "register:40f0:8", ["const:71e7fc:8", "const:4:8"]]
- 0071e7fc ["CALL", null, ["callee:00b3bf30:8"]]
+ 0071e854 ["INT_ADD", "register:40f0:8", ["const:71e854:8", "const:4:8"]]
+ 0071e854 ["CALL", null, ["callee:00b3bf30:8"]]
- 0071e7fc bytes a6751094
+ 0071e854 bytes b7751094
~~~


<a id="compare-07307ac354d91a704e5d5bdb71c68978"></a>

### [`0071ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ed00.md) → [`0071ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md) FUN_0071ed58

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 43件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`0060d624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060d/0060d624.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 43件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`0060d664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060d/0060d664.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ed18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ed00.md#insn-0071ed18) · [`0071ed24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ed00.md#insn-0071ed24)
- 新版 `0071ed70`（命令位置の公開資料なし） · `0071ed7c`（命令位置の公開資料なし）

~~~diff
- 0071ed18 ["INT_ADD", "register:40f0:8", ["const:71ed18:8", "const:4:8"]]
- 0071ed18 ["CALL", null, ["callee:00851550:8"]]
+ 0071ed70 ["INT_ADD", "register:40f0:8", ["const:71ed70:8", "const:4:8"]]
+ 0071ed70 ["CALL", null, ["callee:00851550:8"]]
- 0071ed18 bytes f8c90494
+ 0071ed70 bytes f8c90494
- 0071ed24 ["INT_ADD", "register:40f0:8", ["const:71ed24:8", "const:4:8"]]
- 0071ed24 ["CALL", null, ["callee:00851550:8"]]
+ 0071ed7c ["INT_ADD", "register:40f0:8", ["const:71ed7c:8", "const:4:8"]]
+ 0071ed7c ["CALL", null, ["callee:00851550:8"]]
- 0071ed24 bytes f5c90494
+ 0071ed7c bytes f5c90494
~~~


<a id="compare-56f7e9a0c29a908f03db4526008b6fa6"></a>

### [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) → [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md) FUN_007263e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 4件 [`007247f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00724/007247f0.md) [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md) · 呼出先 3件 [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00724848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/00724848.md) [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c2c.md) · 呼出先 3件 [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md) [`00726438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726438.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "007263b4",
      "incomplete_value": true,
      "site": "007263bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`007263bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md#insn-007263bc) · [`007263b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md#insn-007263b0) · [`007263c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md#insn-007263c8)
- 新版 `00726414`（命令位置の公開資料なし） · `00726408`（命令位置の公開資料なし） · `00726420`（命令位置の公開資料なし）

~~~diff
- 007263bc ["INT_ADD", "register:40f0:8", ["const:7263bc:8", "const:4:8"]]
- 007263bc ["CALL", null, ["local:b0:8"]]
+ 00726414 ["INT_ADD", "register:40f0:8", ["const:726414:8", "const:4:8"]]
+ 00726414 ["CALL", null, ["local:b0:8"]]
- 007263bc bytes f5ffff97
+ 00726414 bytes f5ffff97
- 007263b0 ["INT_ADD", "register:40f0:8", ["const:7263b0:8", "const:4:8"]]
- 007263b0 ["CALL", null, ["local:b0:8"]]
+ 00726408 ["INT_ADD", "register:40f0:8", ["const:726408:8", "const:4:8"]]
+ 00726408 ["CALL", null, ["local:b0:8"]]
- 007263b0 bytes f8ffff97
+ 00726408 bytes f8ffff97
- 007263c8 ["INT_ADD", "register:40f0:8", ["const:7263c8:8", "const:4:8"]]
- 007263c8 ["CALL", null, ["callee:00726438:8"]]
+ 00726420 ["INT_ADD", "register:40f0:8", ["const:726420:8", "const:4:8"]]
+ 00726420 ["CALL", null, ["callee:00726438:8"]]
- 007263c8 bytes 06000094
+ 00726420 bytes 06000094
~~~


<a id="compare-95979e17bd46b18a1e558a23bf7829d5"></a>

### [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) → [`00726438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726438.md) FUN_00726438

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 2件 [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) · 呼出先 2件 [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md) [`00726438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726438.md) · 呼出先 2件 [`00726438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726438.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0072645c",
      "incomplete_value": true,
      "site": "00726460",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00726458",
      "incomplete_value": true,
      "site": "00726460",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00726408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md#insn-00726408) · [`007263fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md#insn-007263fc) · [`00726418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md#insn-00726418)
- 新版 `00726460`（命令位置の公開資料なし） · `00726454`（命令位置の公開資料なし） · `00726470`（命令位置の公開資料なし）

~~~diff
- 00726408 ["INT_ADD", "register:40f0:8", ["const:726408:8", "const:4:8"]]
- 00726408 ["CALL", null, ["local:b0:8"]]
+ 00726460 ["INT_ADD", "register:40f0:8", ["const:726460:8", "const:4:8"]]
+ 00726460 ["CALL", null, ["local:b0:8"]]
- 00726408 bytes f6ffff97
+ 00726460 bytes f6ffff97
- 007263fc ["INT_ADD", "register:40f0:8", ["const:7263fc:8", "const:4:8"]]
- 007263fc ["CALL", null, ["local:b0:8"]]
+ 00726454 ["INT_ADD", "register:40f0:8", ["const:726454:8", "const:4:8"]]
+ 00726454 ["CALL", null, ["local:b0:8"]]
- 007263fc bytes f9ffff97
+ 00726454 bytes f9ffff97
- 00726418 ["INT_ADD", "register:40f0:8", ["const:726418:8", "const:4:8"]]
- 00726418 ["CALL", null, ["callee:00c57f80:8"]]
+ 00726470 ["INT_ADD", "register:40f0:8", ["const:726470:8", "const:4:8"]]
+ 00726470 ["CALL", null, ["callee:00c57f80:8"]]
- 00726418 bytes a6c61494
+ 00726470 bytes c4c61494
~~~


<a id="compare-1a847fb0810986ff9fa91b7df210da88"></a>

### [`00726f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f48.md) → [`00726fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726fa0.md) FUN_00726fa0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00930414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930414.md) [`00934d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d58.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`005509c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c4.md)
- 新版 呼出元 4件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`00930468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/00930468.md) [`00934dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/00934dac.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 1件 [`00550a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f48.md#insn-00726f58)
- 新版 `00726fb0`（命令位置の公開資料なし）

~~~diff
- 00726f58 ["INT_ADD", "register:40f0:8", ["const:726f58:8", "const:4:8"]]
- 00726f58 ["CALL", null, ["callee:00550a04:8"]]
+ 00726fb0 ["INT_ADD", "register:40f0:8", ["const:726fb0:8", "const:4:8"]]
+ 00726fb0 ["CALL", null, ["callee:00550a04:8"]]
- 00726f58 bytes 9ba6f897
+ 00726fb0 bytes 95a6f897
~~~


<a id="compare-7d009b275e17d860306660fda8754235"></a>

### [`00726f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f70.md) → [`00726fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726fc8.md) FUN_00726fc8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0093047c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/0093047c.md) · 呼出先 1件 [`005509c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c8.md)
- 新版 呼出元 4件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`009304d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/009304d0.md) · 呼出先 1件 [`00550a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f70.md#insn-00726f80)
- 新版 `00726fd8`（命令位置の公開資料なし）

~~~diff
- 00726f80 ["INT_ADD", "register:40f0:8", ["const:726f80:8", "const:4:8"]]
- 00726f80 ["CALL", null, ["callee:00550a08:8"]]
+ 00726fd8 ["INT_ADD", "register:40f0:8", ["const:726fd8:8", "const:4:8"]]
+ 00726fd8 ["CALL", null, ["callee:00550a08:8"]]
- 00726f80 bytes 92a6f897
+ 00726fd8 bytes 8ca6f897
~~~


<a id="compare-06ae2fa9bbe1e3430f938f32a737b2a1"></a>

### [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) → [`00727604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727604.md) FUN_00727604

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007267c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00726818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726818.md) [`00727604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727604.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`00727604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727604.md) [`00727654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727654.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007275cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md#insn-007275cc) · [`007275d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md#insn-007275d8) · [`007275e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md#insn-007275e4)
- 新版 `00727624`（命令位置の公開資料なし） · `00727630`（命令位置の公開資料なし） · `0072763c`（命令位置の公開資料なし）

~~~diff
- 007275cc ["INT_ADD", "register:40f0:8", ["const:7275cc:8", "const:4:8"]]
- 007275cc ["CALL", null, ["local:b0:8"]]
+ 00727624 ["INT_ADD", "register:40f0:8", ["const:727624:8", "const:4:8"]]
+ 00727624 ["CALL", null, ["local:b0:8"]]
- 007275cc bytes f8ffff97
+ 00727624 bytes f8ffff97
- 007275d8 ["INT_ADD", "register:40f0:8", ["const:7275d8:8", "const:4:8"]]
- 007275d8 ["CALL", null, ["local:b0:8"]]
+ 00727630 ["INT_ADD", "register:40f0:8", ["const:727630:8", "const:4:8"]]
+ 00727630 ["CALL", null, ["local:b0:8"]]
- 007275d8 bytes f5ffff97
+ 00727630 bytes f5ffff97
- 007275e4 ["INT_ADD", "register:40f0:8", ["const:7275e4:8", "const:4:8"]]
- 007275e4 ["CALL", null, ["callee:00727654:8"]]
+ 0072763c ["INT_ADD", "register:40f0:8", ["const:72763c:8", "const:4:8"]]
+ 0072763c ["CALL", null, ["callee:00727654:8"]]
- 007275e4 bytes 06000094
+ 0072763c bytes 06000094
~~~


<a id="compare-af58826423f1d8f5b36def24a01acbb9"></a>

### [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) → [`00727654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727654.md) FUN_00727654

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) · 呼出先 2件 [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00727604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727604.md) [`00727654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727654.md) · 呼出先 2件 [`00727654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727654.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072761c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md#insn-0072761c) · [`00727628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md#insn-00727628)
- 新版 `00727674`（命令位置の公開資料なし） · `00727680`（命令位置の公開資料なし）

~~~diff
- 0072761c ["INT_ADD", "register:40f0:8", ["const:72761c:8", "const:4:8"]]
- 0072761c ["CALL", null, ["local:b0:8"]]
+ 00727674 ["INT_ADD", "register:40f0:8", ["const:727674:8", "const:4:8"]]
+ 00727674 ["CALL", null, ["local:b0:8"]]
- 0072761c bytes f8ffff97
+ 00727674 bytes f8ffff97
- 00727628 ["INT_ADD", "register:40f0:8", ["const:727628:8", "const:4:8"]]
- 00727628 ["CALL", null, ["local:b0:8"]]
+ 00727680 ["INT_ADD", "register:40f0:8", ["const:727680:8", "const:4:8"]]
+ 00727680 ["CALL", null, ["local:b0:8"]]
- 00727628 bytes f5ffff97
+ 00727680 bytes f5ffff97
~~~


<a id="compare-f3e9373059ec5acd6d11be77383d919b"></a>

### [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) → [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) FUN_00727a28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`0063d914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d914.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`006b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8a64.md) [`006e4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4d6c.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b2f7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f7f0.md) [`00b2f880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md)
- 新版 呼出元 37件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`0063d954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`006b8abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8abc.md) [`006e4dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4dc4.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b2f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f88c.md) [`00b2f91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f91c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md#insn-00727a2c) · [`00727a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md#insn-00727a80) · [`00727a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md#insn-00727a88)
- 新版 `00727a84`（命令位置の公開資料なし） · `00727ad8`（命令位置の公開資料なし） · `00727ae0`（命令位置の公開資料なし）

~~~diff
- 00727a2c ["INT_ADD", "register:40f0:8", ["const:727a2c:8", "const:4:8"]]
- 00727a2c ["CALL", null, ["callee:00851550:8"]]
+ 00727a84 ["INT_ADD", "register:40f0:8", ["const:727a84:8", "const:4:8"]]
+ 00727a84 ["CALL", null, ["callee:00851550:8"]]
- 00727a2c bytes b3a60494
+ 00727a84 bytes b3a60494
- 00727a80 ["INT_ADD", "register:40f0:8", ["const:727a80:8", "const:4:8"]]
- 00727a80 ["CALL", null, ["callee:00851550:8"]]
+ 00727ad8 ["INT_ADD", "register:40f0:8", ["const:727ad8:8", "const:4:8"]]
+ 00727ad8 ["CALL", null, ["callee:00851550:8"]]
- 00727a80 bytes 9ea60494
+ 00727ad8 bytes 9ea60494
- 00727a88 ["INT_ADD", "register:40f0:8", ["const:727a88:8", "const:4:8"]]
- 00727a88 ["CALL", null, ["callee:00b2f91c:8"]]
+ 00727ae0 ["INT_ADD", "register:40f0:8", ["const:727ae0:8", "const:4:8"]]
+ 00727ae0 ["CALL", null, ["callee:00b2f91c:8"]]
- 00727a88 bytes 7e1f1094
+ 00727ae0 bytes 8f1f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7451ff1033f7662df018c63be3bed32a"></a>

### [`00727ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727ca0.md) → [`00727cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727cf8.md) FUN_00727cf8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00665110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665110.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 1件 [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md)
- 新版 呼出元 3件 [`00665150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665150.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) · 呼出先 1件 [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727ca0.md#insn-00727ca8)
- 新版 `00727d00`（命令位置の公開資料なし）

~~~diff
- 00727ca8 ["INT_ADD", "register:40f0:8", ["const:727ca8:8", "const:4:8"]]
- 00727ca8 ["CALL", null, ["callee:00727a28:8"]]
+ 00727d00 ["INT_ADD", "register:40f0:8", ["const:727d00:8", "const:4:8"]]
+ 00727d00 ["CALL", null, ["callee:00727a28:8"]]
- 00727ca8 bytes 4affff97
+ 00727d00 bytes 4affff97
~~~


<a id="compare-94cb3e8b115cdec25db6cbf86a7eb802"></a>

### [`00727cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727cbc.md) → [`00727d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727d14.md) FUN_00727d14

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727cbc.md#insn-00727cc4)
- 新版 `00727d1c`（命令位置の公開資料なし）

~~~diff
- 00727cc4 ["INT_ADD", "register:40f0:8", ["const:727cc4:8", "const:4:8"]]
- 00727cc4 ["CALL", null, ["callee:00851550:8"]]
+ 00727d1c ["INT_ADD", "register:40f0:8", ["const:727d1c:8", "const:4:8"]]
+ 00727d1c ["CALL", null, ["callee:00851550:8"]]
- 00727cc4 bytes 0da60494
+ 00727d1c bytes 0da60494
~~~


<a id="compare-265ff0c9638ae2e21bea63dde7df297b"></a>

### [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md) → [`00727d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727d74.md) FUN_00727d74

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 28件 [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) [`00739e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739e44.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 28件 [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/007394fc.md) [`00739e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/00739e9c.md) [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md#insn-00727d48) · [`00727da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md#insn-00727da4) · [`00727df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md#insn-00727df4)
- 新版 `00727da0`（命令位置の公開資料なし） · `00727dfc`（命令位置の公開資料なし） · `00727e4c`（命令位置の公開資料なし）

~~~diff
- 00727d48 ["INT_ADD", "register:40f0:8", ["const:727d48:8", "const:4:8"]]
- 00727d48 ["CALL", null, ["callee:00851550:8"]]
+ 00727da0 ["INT_ADD", "register:40f0:8", ["const:727da0:8", "const:4:8"]]
+ 00727da0 ["CALL", null, ["callee:00851550:8"]]
- 00727d48 bytes eca50494
+ 00727da0 bytes eca50494
- 00727da4 ["INT_ADD", "register:40f0:8", ["const:727da4:8", "const:4:8"]]
- 00727da4 ["CALL", null, ["callee:00851550:8"]]
+ 00727dfc ["INT_ADD", "register:40f0:8", ["const:727dfc:8", "const:4:8"]]
+ 00727dfc ["CALL", null, ["callee:00851550:8"]]
- 00727da4 bytes d5a50494
+ 00727dfc bytes d5a50494
- 00727df4 ["INT_ADD", "register:40f0:8", ["const:727df4:8", "const:4:8"]]
- 00727df4 ["CALL", null, ["callee:00851550:8"]]
+ 00727e4c ["INT_ADD", "register:40f0:8", ["const:727e4c:8", "const:4:8"]]
+ 00727e4c ["CALL", null, ["callee:00851550:8"]]
- 00727df4 bytes c1a50494
+ 00727e4c bytes c1a50494
~~~


<a id="compare-c56e1cfb12951bb76e13825582c97194"></a>

### [`00728ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ed0.md) → [`00728f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728f28.md) FUN_00728f28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00728e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728e48.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`00728ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728ea0.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00728f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ed0.md#insn-00728f00) · [`00728f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ed0.md#insn-00728f1c) · [`00728f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ed0.md#insn-00728f38)
- 新版 `00728f58`（命令位置の公開資料なし） · `00728f74`（命令位置の公開資料なし） · `00728f90`（命令位置の公開資料なし）

~~~diff
- 00728f00 ["INT_ADD", "register:40f0:8", ["const:728f00:8", "const:4:8"]]
- 00728f00 ["CALL", null, ["callee:00851550:8"]]
+ 00728f58 ["INT_ADD", "register:40f0:8", ["const:728f58:8", "const:4:8"]]
+ 00728f58 ["CALL", null, ["callee:00851550:8"]]
- 00728f00 bytes 7ea10494
+ 00728f58 bytes 7ea10494
- 00728f1c ["INT_ADD", "register:40f0:8", ["const:728f1c:8", "const:4:8"]]
- 00728f1c ["CALL", null, ["callee:00851550:8"]]
+ 00728f74 ["INT_ADD", "register:40f0:8", ["const:728f74:8", "const:4:8"]]
+ 00728f74 ["CALL", null, ["callee:00851550:8"]]
- 00728f1c bytes 77a10494
+ 00728f74 bytes 77a10494
- 00728f38 ["INT_ADD", "register:40f0:8", ["const:728f38:8", "const:4:8"]]
- 00728f38 ["CALL", null, ["callee:00851550:8"]]
+ 00728f90 ["INT_ADD", "register:40f0:8", ["const:728f90:8", "const:4:8"]]
+ 00728f90 ["CALL", null, ["callee:00851550:8"]]
- 00728f38 bytes 70a10494
+ 00728f90 bytes 70a10494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93a5ac3c738ea9b2a2fdf6d722024bb8"></a>

### [`0072ad20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md) → [`0072ad78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072a/0072ad78.md) FUN_0072ad78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007640f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/007640f0.md) · 呼出先 4件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00729e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729e78.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00764148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764148.md) · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00729ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/00729ed0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md#insn-0072ad40) · [`0072ad5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md#insn-0072ad5c) · [`0072ad80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md#insn-0072ad80)
- 新版 `0072ad98`（命令位置の公開資料なし） · `0072adb4`（命令位置の公開資料なし） · `0072add8`（命令位置の公開資料なし）

~~~diff
- 0072ad40 ["INT_ADD", "register:40f0:8", ["const:72ad40:8", "const:4:8"]]
- 0072ad40 ["CALL", null, ["callee:00729ed0:8"]]
+ 0072ad98 ["INT_ADD", "register:40f0:8", ["const:72ad98:8", "const:4:8"]]
+ 0072ad98 ["CALL", null, ["callee:00729ed0:8"]]
- 0072ad40 bytes 4efcff97
+ 0072ad98 bytes 4efcff97
- 0072ad5c ["INT_ADD", "register:40f0:8", ["const:72ad5c:8", "const:4:8"]]
- 0072ad5c ["CALL", null, ["callee:0046d7f0:8"]]
+ 0072adb4 ["INT_ADD", "register:40f0:8", ["const:72adb4:8", "const:4:8"]]
+ 0072adb4 ["CALL", null, ["callee:0046d7f0:8"]]
- 0072ad5c bytes 950af597
+ 0072adb4 bytes 8f0af597
- 0072ad80 ["INT_ADD", "register:40f0:8", ["const:72ad80:8", "const:4:8"]]
- 0072ad80 ["CALL", null, ["callee:00c57f80:8"]]
+ 0072add8 ["INT_ADD", "register:40f0:8", ["const:72add8:8", "const:4:8"]]
+ 0072add8 ["CALL", null, ["callee:00c57f80:8"]]
- 0072ad80 bytes 4cb41494
+ 0072add8 bytes 6ab41494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23b29da627984340cbcfcd90af3d730"></a>

### [`0072bcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md) → [`0072bd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072b/0072bd10.md) FUN_0072bd10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) · 呼出先 4件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0072b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b2a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`006247e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247e8.md) · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0072b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072b/0072b2fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md#insn-0072bcd8) · [`0072bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md#insn-0072bcf4) · [`0072bd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md#insn-0072bd18)
- 新版 `0072bd30`（命令位置の公開資料なし） · `0072bd4c`（命令位置の公開資料なし） · `0072bd70`（命令位置の公開資料なし）

~~~diff
- 0072bcd8 ["INT_ADD", "register:40f0:8", ["const:72bcd8:8", "const:4:8"]]
- 0072bcd8 ["CALL", null, ["callee:0072b2fc:8"]]
+ 0072bd30 ["INT_ADD", "register:40f0:8", ["const:72bd30:8", "const:4:8"]]
+ 0072bd30 ["CALL", null, ["callee:0072b2fc:8"]]
- 0072bcd8 bytes 73fdff97
+ 0072bd30 bytes 73fdff97
- 0072bcf4 ["INT_ADD", "register:40f0:8", ["const:72bcf4:8", "const:4:8"]]
- 0072bcf4 ["CALL", null, ["callee:0046d7f0:8"]]
+ 0072bd4c ["INT_ADD", "register:40f0:8", ["const:72bd4c:8", "const:4:8"]]
+ 0072bd4c ["CALL", null, ["callee:0046d7f0:8"]]
- 0072bcf4 bytes af06f597
+ 0072bd4c bytes a906f597
- 0072bd18 ["INT_ADD", "register:40f0:8", ["const:72bd18:8", "const:4:8"]]
- 0072bd18 ["CALL", null, ["callee:00c57f80:8"]]
+ 0072bd70 ["INT_ADD", "register:40f0:8", ["const:72bd70:8", "const:4:8"]]
+ 0072bd70 ["CALL", null, ["callee:00c57f80:8"]]
- 0072bd18 bytes 66b01494
+ 0072bd70 bytes 84b01494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986d2dc27302c256421292e334a8dd43"></a>

### [`0072c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md) → [`0072c334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c334.md) FUN_0072c334

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0074fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074f/0074fbe0.md) [`00750d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00750/00750d48.md) [`0077b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b30c.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`009a1600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a1600.md) · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md)
- 新版 呼出元 5件 [`0074fc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074fc38.md) [`00751008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00751/00751008.md) [`0077b364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`009a1654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a1/009a1654.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a34c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md#insn-0072c2f0) · [`0072c314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md#insn-0072c314) · [`0072c358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md#insn-0072c358)
- 新版 `0072c348`（命令位置の公開資料なし） · `0072c36c`（命令位置の公開資料なし） · `0072c3b0`（命令位置の公開資料なし）

~~~diff
- 0072c2f0 ["INT_ADD", "register:40f0:8", ["const:72c2f0:8", "const:4:8"]]
- 0072c2f0 ["CALL", null, ["callee:004678a0:8"]]
+ 0072c348 ["INT_ADD", "register:40f0:8", ["const:72c348:8", "const:4:8"]]
+ 0072c348 ["CALL", null, ["callee:004678a0:8"]]
- 0072c2f0 bytes 5cedf497
+ 0072c348 bytes 56edf497
- 0072c314 ["INT_ADD", "register:40f0:8", ["const:72c314:8", "const:4:8"]]
- 0072c314 ["CALL", null, ["callee:0046a34c:8"]]
+ 0072c36c ["INT_ADD", "register:40f0:8", ["const:72c36c:8", "const:4:8"]]
+ 0072c36c ["CALL", null, ["callee:0046a34c:8"]]
- 0072c314 bytes fef7f497
+ 0072c36c bytes f8f7f497
- 0072c358 ["INT_ADD", "register:40f0:8", ["const:72c358:8", "const:4:8"]]
- 0072c358 ["CALL", null, ["callee:00469c44:8"]]
+ 0072c3b0 ["INT_ADD", "register:40f0:8", ["const:72c3b0:8", "const:4:8"]]
+ 0072c3b0 ["CALL", null, ["callee:00469c44:8"]]
- 0072c358 bytes 2bf6f497
+ 0072c3b0 bytes 25f6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53a500a693fe8f00962a392923d913b"></a>

### [`0072c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md) → [`0072c3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c3d8.md) FUN_0072c3d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00729974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729974.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007299cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/007299cc.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0061af38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md#insn-0072c3dc) · [`0072c3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md#insn-0072c3ec) · [`0072c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md#insn-0072c420)
- 新版 `0072c434`（命令位置の公開資料なし） · `0072c444`（命令位置の公開資料なし） · `0072c478`（命令位置の公開資料なし）

~~~diff
- 0072c3dc ["INT_ADD", "register:40f0:8", ["const:72c3dc:8", "const:4:8"]]
- 0072c3dc ["CALL", null, ["callee:0043bb60:8"]]
+ 0072c434 ["INT_ADD", "register:40f0:8", ["const:72c434:8", "const:4:8"]]
+ 0072c434 ["CALL", null, ["callee:0043bb60:8"]]
- 0072c3dc bytes d13df497
+ 0072c434 bytes cb3df497
- 0072c3ec ["INT_ADD", "register:40f0:8", ["const:72c3ec:8", "const:4:8"]]
- 0072c3ec ["CALL", null, ["callee:0043bb60:8"]]
+ 0072c444 ["INT_ADD", "register:40f0:8", ["const:72c444:8", "const:4:8"]]
+ 0072c444 ["CALL", null, ["callee:0043bb60:8"]]
- 0072c3ec bytes cd3df497
+ 0072c444 bytes c73df497
- 0072c420 ["INT_ADD", "register:40f0:8", ["const:72c420:8", "const:4:8"]]
- 0072c420 ["CALL", null, ["callee:0061af38:8"]]
+ 0072c478 ["INT_ADD", "register:40f0:8", ["const:72c478:8", "const:4:8"]]
+ 0072c478 ["CALL", null, ["callee:0061af38:8"]]
- 0072c420 bytes b6bafb97
+ 0072c478 bytes b0bafb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0765e3a163278ec71a5fb7fb2b2e82fd"></a>

### [`0072c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md) → [`0072c8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c8a4.md) FUN_0072c8a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00805bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md) [`00805d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 4件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00800684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800684.md) [`00805c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805c4c.md) [`00805d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805d8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md#insn-0072c86c) · [`0072c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md#insn-0072c878) · [`0072c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md#insn-0072c888)
- 新版 `0072c8c4`（命令位置の公開資料なし） · `0072c8d0`（命令位置の公開資料なし） · `0072c8e0`（命令位置の公開資料なし）

~~~diff
- 0072c86c ["INT_ADD", "register:40f0:8", ["const:72c86c:8", "const:4:8"]]
- 0072c86c ["CALL", null, ["callee:0048cec4:8"]]
+ 0072c8c4 ["INT_ADD", "register:40f0:8", ["const:72c8c4:8", "const:4:8"]]
+ 0072c8c4 ["CALL", null, ["callee:0048cec4:8"]]
- 0072c86c bytes 8681f597
+ 0072c8c4 bytes 8081f597
- 0072c878 ["INT_ADD", "register:40f0:8", ["const:72c878:8", "const:4:8"]]
- 0072c878 ["CALL", null, ["callee:00800684:8"]]
+ 0072c8d0 ["INT_ADD", "register:40f0:8", ["const:72c8d0:8", "const:4:8"]]
+ 0072c8d0 ["CALL", null, ["callee:00800684:8"]]
- 0072c878 bytes 6d4f0394
+ 0072c8d0 bytes 6d4f0394
- 0072c888 ["INT_ADD", "register:40f0:8", ["const:72c888:8", "const:4:8"]]
- 0072c888 ["CALL", null, ["callee:00805d8c:8"]]
+ 0072c8e0 ["INT_ADD", "register:40f0:8", ["const:72c8e0:8", "const:4:8"]]
+ 0072c8e0 ["CALL", null, ["callee:00805d8c:8"]]
- 0072c888 bytes 2b650394
+ 0072c8e0 bytes 2b650394
~~~


<a id="compare-af356d172fd350dd8c9d6bc8ca6b0f42"></a>

### [`0072c8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c8ac.md) → [`0072c904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c904.md) FUN_0072c904

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`00731b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b50.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c8ac.md#insn-0072c8c4) · [`0072c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c8ac.md#insn-0072c910)
- 新版 `0072c91c`（命令位置の公開資料なし） · `0072c968`（命令位置の公開資料なし）

~~~diff
- 0072c8c4 ["INT_ADD", "register:40f0:8", ["const:72c8c4:8", "const:4:8"]]
- 0072c8c4 ["CALL", null, ["callee:00851550:8"]]
+ 0072c91c ["INT_ADD", "register:40f0:8", ["const:72c91c:8", "const:4:8"]]
+ 0072c91c ["CALL", null, ["callee:00851550:8"]]
- 0072c8c4 bytes 0d930494
+ 0072c91c bytes 0d930494
- 0072c910 ["INT_ADD", "register:40f0:8", ["const:72c910:8", "const:4:8"]]
- 0072c910 ["CALL", null, ["callee:00731b50:8"]]
+ 0072c968 ["INT_ADD", "register:40f0:8", ["const:72c968:8", "const:4:8"]]
+ 0072c968 ["CALL", null, ["callee:00731b50:8"]]
- 0072c910 bytes 7a140094
+ 0072c968 bytes 7a140094
~~~


<a id="compare-352f461056e7bb514c5ee1b22096f2c2"></a>

### [`0072c914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c914.md) → [`0072c96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c96c.md) FUN_0072c96c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md)
- 新版 呼出元 2件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 1件 [`00731b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c914.md#insn-0072c938)
- 新版 `0072c990`（命令位置の公開資料なし）

~~~diff
- 0072c938 ["INT_ADD", "register:40f0:8", ["const:72c938:8", "const:4:8"]]
- 0072c938 ["CALL", null, ["callee:00731b50:8"]]
+ 0072c990 ["INT_ADD", "register:40f0:8", ["const:72c990:8", "const:4:8"]]
+ 0072c990 ["CALL", null, ["callee:00731b50:8"]]
- 0072c938 bytes 70140094
+ 0072c990 bytes 70140094
~~~


<a id="compare-3c4b65a754858d6a6acdc1083aa11b8f"></a>

### [`0072c93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md) → [`0072c994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c994.md) FUN_0072c994

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00805d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00805d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805d8c.md) · 呼出先 3件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md#insn-0072c954) · [`0072c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md#insn-0072c968) · [`0072c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md#insn-0072c9b0)
- 新版 `0072c9ac`（命令位置の公開資料なし） · `0072c9c0`（命令位置の公開資料なし） · `0072ca08`（命令位置の公開資料なし）

~~~diff
- 0072c954 ["INT_ADD", "register:40f0:8", ["const:72c954:8", "const:4:8"]]
- 0072c954 ["CALL", null, ["callee:00851550:8"]]
+ 0072c9ac ["INT_ADD", "register:40f0:8", ["const:72c9ac:8", "const:4:8"]]
+ 0072c9ac ["CALL", null, ["callee:00851550:8"]]
- 0072c954 bytes e9920494
+ 0072c9ac bytes e9920494
- 0072c968 ["INT_ADD", "register:40f0:8", ["const:72c968:8", "const:4:8"]]
- 0072c968 ["CALL", null, ["callee:00800244:8"]]
+ 0072c9c0 ["INT_ADD", "register:40f0:8", ["const:72c9c0:8", "const:4:8"]]
+ 0072c9c0 ["CALL", null, ["callee:00800244:8"]]
- 0072c968 bytes 214e0394
+ 0072c9c0 bytes 214e0394
- 0072c9b0 ["INT_ADD", "register:40f0:8", ["const:72c9b0:8", "const:4:8"]]
- 0072c9b0 ["CALL", null, ["callee:0049f430:8"]]
+ 0072ca08 ["INT_ADD", "register:40f0:8", ["const:72ca08:8", "const:4:8"]]
+ 0072ca08 ["CALL", null, ["callee:0049f430:8"]]
- 0072c9b0 bytes 90caf597
+ 0072ca08 bytes 8acaf597
~~~


<a id="compare-ea967e043a559e2419cf7fefce707f6f"></a>

### [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) → [`0072efc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072efc4.md) FUN_0072efc4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`00480d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d30.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ef90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md#insn-0072ef90) · [`0072ef9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md#insn-0072ef9c) · [`0072efa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md#insn-0072efa8)
- 新版 `0072efe8`（命令位置の公開資料なし） · `0072eff4`（命令位置の公開資料なし） · `0072f000`（命令位置の公開資料なし）

~~~diff
- 0072ef90 ["INT_ADD", "register:40f0:8", ["const:72ef90:8", "const:4:8"]]
- 0072ef90 ["CALL", null, ["callee:00480e68:8"]]
+ 0072efe8 ["INT_ADD", "register:40f0:8", ["const:72efe8:8", "const:4:8"]]
+ 0072efe8 ["CALL", null, ["callee:00480e68:8"]]
- 0072ef90 bytes a647f597
+ 0072efe8 bytes a047f597
- 0072ef9c ["INT_ADD", "register:40f0:8", ["const:72ef9c:8", "const:4:8"]]
- 0072ef9c ["CALL", null, ["callee:00480e68:8"]]
+ 0072eff4 ["INT_ADD", "register:40f0:8", ["const:72eff4:8", "const:4:8"]]
+ 0072eff4 ["CALL", null, ["callee:00480e68:8"]]
- 0072ef9c bytes a347f597
+ 0072eff4 bytes 9d47f597
- 0072efa8 ["INT_ADD", "register:40f0:8", ["const:72efa8:8", "const:4:8"]]
- 0072efa8 ["CALL", null, ["callee:00480d30:8"]]
+ 0072f000 ["INT_ADD", "register:40f0:8", ["const:72f000:8", "const:4:8"]]
+ 0072f000 ["CALL", null, ["callee:00480d30:8"]]
- 0072efa8 bytes 5247f597
+ 0072f000 bytes 4c47f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811e320a2673c12d5c1dd2970ab5502b"></a>

### [`00730cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cfc.md) → [`00730d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00730/00730d54.md) FUN_00730d54

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`00731ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ae4.md)
- 新版 呼出元 3件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`0085d54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 1件 [`00731b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00730d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cfc.md#insn-00730d20)
- 新版 `00730d78`（命令位置の公開資料なし）

~~~diff
- 00730d20 ["INT_ADD", "register:40f0:8", ["const:730d20:8", "const:4:8"]]
- 00730d20 ["CALL", null, ["callee:00731b3c:8"]]
+ 00730d78 ["INT_ADD", "register:40f0:8", ["const:730d78:8", "const:4:8"]]
+ 00730d78 ["CALL", null, ["callee:00731b3c:8"]]
- 00730d20 bytes 71030094
+ 00730d78 bytes 71030094
~~~


<a id="compare-0050eb517b109b9d2b84c66125f708b0"></a>

### [`00731328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md) → [`00731380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731380.md) FUN_00731380

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00731ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ae4.md) [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 4件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00731b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b3c.md) [`00731b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b50.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md#insn-00731344) · [`0073138c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md#insn-0073138c) · [`00731400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md#insn-00731400)
- 新版 `0073139c`（命令位置の公開資料なし） · `007313e4`（命令位置の公開資料なし） · `00731458`（命令位置の公開資料なし）

~~~diff
- 00731344 ["INT_ADD", "register:40f0:8", ["const:731344:8", "const:4:8"]]
- 00731344 ["CALL", null, ["callee:0048cec4:8"]]
+ 0073139c ["INT_ADD", "register:40f0:8", ["const:73139c:8", "const:4:8"]]
+ 0073139c ["CALL", null, ["callee:0048cec4:8"]]
- 00731344 bytes d06ef597
+ 0073139c bytes ca6ef597
- 0073138c ["INT_ADD", "register:40f0:8", ["const:73138c:8", "const:4:8"]]
- 0073138c ["CALL", null, ["callee:00851550:8"]]
+ 007313e4 ["INT_ADD", "register:40f0:8", ["const:7313e4:8", "const:4:8"]]
+ 007313e4 ["CALL", null, ["callee:00851550:8"]]
- 0073138c bytes 5b800494
+ 007313e4 bytes 5b800494
- 00731400 ["INT_ADD", "register:40f0:8", ["const:731400:8", "const:4:8"]]
- 00731400 ["CALL", null, ["callee:00731b50:8"]]
+ 00731458 ["INT_ADD", "register:40f0:8", ["const:731458:8", "const:4:8"]]
+ 00731458 ["CALL", null, ["callee:00731b50:8"]]
- 00731400 bytes be010094
+ 00731458 bytes be010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b3a4891ebdbe90586d160991f59ad0"></a>

### [`00731670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731670.md) → [`007316c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/007316c8.md) FUN_007316c8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md)
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 3件 [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00800684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800684.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073168c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731670.md#insn-0073168c) · [`00731698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731670.md#insn-00731698) · [`007316ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731670.md#insn-007316ac)
- 新版 `007316e4`（命令位置の公開資料なし） · `007316f0`（命令位置の公開資料なし） · `00731704`（命令位置の公開資料なし）

~~~diff
- 0073168c ["INT_ADD", "register:40f0:8", ["const:73168c:8", "const:4:8"]]
- 0073168c ["CALL", null, ["callee:008003d0:8"]]
+ 007316e4 ["INT_ADD", "register:40f0:8", ["const:7316e4:8", "const:4:8"]]
+ 007316e4 ["CALL", null, ["callee:008003d0:8"]]
- 0073168c bytes 3b3b0394
+ 007316e4 bytes 3b3b0394
- 00731698 ["INT_ADD", "register:40f0:8", ["const:731698:8", "const:4:8"]]
- 00731698 ["CALL", null, ["callee:00800684:8"]]
+ 007316f0 ["INT_ADD", "register:40f0:8", ["const:7316f0:8", "const:4:8"]]
+ 007316f0 ["CALL", null, ["callee:00800684:8"]]
- 00731698 bytes e53b0394
+ 007316f0 bytes e53b0394
- 007316ac ["INT_ADD", "register:40f0:8", ["const:7316ac:8", "const:4:8"]]
- 007316ac ["CALL", null, ["callee:00800244:8"]]
+ 00731704 ["INT_ADD", "register:40f0:8", ["const:731704:8", "const:4:8"]]
+ 00731704 ["CALL", null, ["callee:00800244:8"]]
- 007316ac bytes d03a0394
+ 00731704 bytes d03a0394
~~~


<a id="compare-823f09fb62e1a6fc09e7da75be75e9fc"></a>

### [`00731734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731734.md) → [`0073178c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/0073178c.md) FUN_0073178c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731734.md#insn-00731798) · [`007317d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731734.md#insn-007317d8)
- 新版 `007317f0`（命令位置の公開資料なし） · `00731830`（命令位置の公開資料なし）

~~~diff
- 00731798 ["INT_ADD", "register:40f0:8", ["const:731798:8", "const:4:8"]]
- 00731798 ["CALL", null, ["callee:00c57f60:8"]]
+ 007317f0 ["INT_ADD", "register:40f0:8", ["const:7317f0:8", "const:4:8"]]
+ 007317f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00731798 bytes be991494
+ 007317f0 bytes dc991494
- 007317d8 ["INT_ADD", "register:40f0:8", ["const:7317d8:8", "const:4:8"]]
- 007317d8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00731830 ["INT_ADD", "register:40f0:8", ["const:731830:8", "const:4:8"]]
+ 00731830 ["CALL", null, ["callee:0043bbe4:8"]]
- 007317d8 bytes f328f497
+ 00731830 bytes ed28f497
~~~


<a id="compare-49dd411d12761c472bb68481aa1eaf49"></a>

### [`0073180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md) → [`00731864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731864.md) FUN_00731864

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 8件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00730bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730bbc.md) [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md)
- 新版 呼出元 1件 [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) · 呼出先 8件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`00730c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00730/00730c14.md) [`00731b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md#insn-00731880) · [`00731908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md#insn-00731908) · [`00731914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md#insn-00731914)
- 新版 `007318d8`（命令位置の公開資料なし） · `00731960`（命令位置の公開資料なし） · `0073196c`（命令位置の公開資料なし）

~~~diff
- 00731880 ["INT_ADD", "register:40f0:8", ["const:731880:8", "const:4:8"]]
- 00731880 ["CALL", null, ["callee:0046d7f0:8"]]
+ 007318d8 ["INT_ADD", "register:40f0:8", ["const:7318d8:8", "const:4:8"]]
+ 007318d8 ["CALL", null, ["callee:0046d7f0:8"]]
- 00731880 bytes cceff497
+ 007318d8 bytes c6eff497
- 00731908 ["INT_ADD", "register:40f0:8", ["const:731908:8", "const:4:8"]]
- 00731908 ["CALL", null, ["callee:0048cec4:8"]]
+ 00731960 ["INT_ADD", "register:40f0:8", ["const:731960:8", "const:4:8"]]
+ 00731960 ["CALL", null, ["callee:0048cec4:8"]]
- 00731908 bytes 5f6df597
+ 00731960 bytes 596df597
- 00731914 ["INT_ADD", "register:40f0:8", ["const:731914:8", "const:4:8"]]
- 00731914 ["CALL", null, ["callee:00800684:8"]]
+ 0073196c ["INT_ADD", "register:40f0:8", ["const:73196c:8", "const:4:8"]]
+ 0073196c ["CALL", null, ["callee:00800684:8"]]
- 00731914 bytes 463b0394
+ 0073196c bytes 463b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e58bb864ca0ce6ce403e7d4e58afe4"></a>

### [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) → [`00731a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a00.md) FUN_00731a00

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0072ca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`00848d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848d44.md) · 呼出先 3件 [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0072ca68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072ca68.md) [`00731a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a00.md) [`00848d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d9c.md) · 呼出先 3件 [`00731a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a00.md) [`00731a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007319c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md#insn-007319c8) · [`007319d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md#insn-007319d4) · [`007319e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md#insn-007319e0)
- 新版 `00731a20`（命令位置の公開資料なし） · `00731a2c`（命令位置の公開資料なし） · `00731a38`（命令位置の公開資料なし）

~~~diff
- 007319c8 ["INT_ADD", "register:40f0:8", ["const:7319c8:8", "const:4:8"]]
- 007319c8 ["CALL", null, ["local:b0:8"]]
+ 00731a20 ["INT_ADD", "register:40f0:8", ["const:731a20:8", "const:4:8"]]
+ 00731a20 ["CALL", null, ["local:b0:8"]]
- 007319c8 bytes f8ffff97
+ 00731a20 bytes f8ffff97
- 007319d4 ["INT_ADD", "register:40f0:8", ["const:7319d4:8", "const:4:8"]]
- 007319d4 ["CALL", null, ["local:b0:8"]]
+ 00731a2c ["INT_ADD", "register:40f0:8", ["const:731a2c:8", "const:4:8"]]
+ 00731a2c ["CALL", null, ["local:b0:8"]]
- 007319d4 bytes f5ffff97
+ 00731a2c bytes f5ffff97
- 007319e0 ["INT_ADD", "register:40f0:8", ["const:7319e0:8", "const:4:8"]]
- 007319e0 ["CALL", null, ["callee:00731a50:8"]]
+ 00731a38 ["INT_ADD", "register:40f0:8", ["const:731a38:8", "const:4:8"]]
+ 00731a38 ["CALL", null, ["callee:00731a50:8"]]
- 007319e0 bytes 06000094
+ 00731a38 bytes 06000094
~~~


<a id="compare-41500fa920cbe811a9b5709d001e4f85"></a>

### [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) → [`00731a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a50.md) FUN_00731a50

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) · 呼出先 2件 [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00731a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a00.md) [`00731a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a50.md) · 呼出先 2件 [`00731a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731a50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md#insn-00731a14) · [`00731a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md#insn-00731a20) · [`00731a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md#insn-00731a3c)
- 新版 `00731a6c`（命令位置の公開資料なし） · `00731a78`（命令位置の公開資料なし） · `00731a94`（命令位置の公開資料なし）

~~~diff
- 00731a14 ["INT_ADD", "register:40f0:8", ["const:731a14:8", "const:4:8"]]
- 00731a14 ["CALL", null, ["local:b0:8"]]
+ 00731a6c ["INT_ADD", "register:40f0:8", ["const:731a6c:8", "const:4:8"]]
+ 00731a6c ["CALL", null, ["local:b0:8"]]
- 00731a14 bytes f9ffff97
+ 00731a6c bytes f9ffff97
- 00731a20 ["INT_ADD", "register:40f0:8", ["const:731a20:8", "const:4:8"]]
- 00731a20 ["CALL", null, ["local:b0:8"]]
+ 00731a78 ["INT_ADD", "register:40f0:8", ["const:731a78:8", "const:4:8"]]
+ 00731a78 ["CALL", null, ["local:b0:8"]]
- 00731a20 bytes f6ffff97
+ 00731a78 bytes f6ffff97
- 00731a3c ["INT_ADD", "register:40f0:8", ["const:731a3c:8", "const:4:8"]]
- 00731a3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00731a94 ["INT_ADD", "register:40f0:8", ["const:731a94:8", "const:4:8"]]
+ 00731a94 ["CALL", null, ["callee:00c57f80:8"]]
- 00731a3c bytes 1d991494
+ 00731a94 bytes 3b991494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e703bc5bb605cb7b0302bd46258be079"></a>

### [`00732834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732834.md) → [`0073288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/0073288c.md) FUN_0073288c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a871b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a871b0.md)
- 新版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a87220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007328fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732834.md#insn-007328fc) · [`00732904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732834.md#insn-00732904)
- 新版 `00732954`（命令位置の公開資料なし） · `0073295c`（命令位置の公開資料なし）

~~~diff
- 007328fc ["INT_ADD", "register:40f0:8", ["const:7328fc:8", "const:4:8"]]
- 007328fc ["CALL", null, ["callee:00851550:8"]]
+ 00732954 ["INT_ADD", "register:40f0:8", ["const:732954:8", "const:4:8"]]
+ 00732954 ["CALL", null, ["callee:00851550:8"]]
- 007328fc bytes ff7a0494
+ 00732954 bytes ff7a0494
- 00732904 ["INT_ADD", "register:40f0:8", ["const:732904:8", "const:4:8"]]
- 00732904 ["CALL", null, ["callee:00a87220:8"]]
+ 0073295c ["INT_ADD", "register:40f0:8", ["const:73295c:8", "const:4:8"]]
+ 0073295c ["CALL", null, ["callee:00a87220:8"]]
- 00732904 bytes 2b520d94
+ 0073295c bytes 31520d94
~~~


<a id="compare-094873cbef5fd0dd3137e9cb203e5a3c"></a>

### [`00733e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md) → [`00733ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00733/00733ebc.md) FUN_00733ebc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00733af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733af8.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00737b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737b64.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00733b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00733/00733b50.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00737bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00737/00737bbc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00733e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md#insn-00733e78) · [`00733e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md#insn-00733e88) · [`00733ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md#insn-00733ee0)
- 新版 `00733ed0`（命令位置の公開資料なし） · `00733ee0`（命令位置の公開資料なし） · `00733f38`（命令位置の公開資料なし）

~~~diff
- 00733e78 ["INT_ADD", "register:40f0:8", ["const:733e78:8", "const:4:8"]]
- 00733e78 ["CALL", null, ["callee:00737bbc:8"]]
+ 00733ed0 ["INT_ADD", "register:40f0:8", ["const:733ed0:8", "const:4:8"]]
+ 00733ed0 ["CALL", null, ["callee:00737bbc:8"]]
- 00733e78 bytes 3b0f0094
+ 00733ed0 bytes 3b0f0094
- 00733e88 ["INT_ADD", "register:40f0:8", ["const:733e88:8", "const:4:8"]]
- 00733e88 ["CALL", null, ["callee:00851550:8"]]
+ 00733ee0 ["INT_ADD", "register:40f0:8", ["const:733ee0:8", "const:4:8"]]
+ 00733ee0 ["CALL", null, ["callee:00851550:8"]]
- 00733e88 bytes 9c750494
+ 00733ee0 bytes 9c750494
- 00733ee0 ["INT_ADD", "register:40f0:8", ["const:733ee0:8", "const:4:8"]]
- 00733ee0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00733f38 ["INT_ADD", "register:40f0:8", ["const:733f38:8", "const:4:8"]]
+ 00733f38 ["CALL", null, ["callee:00c57f60:8"]]
- 00733ee0 bytes ec8f1494
+ 00733f38 bytes 0a901494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e88bd970d8fc603ba475c04c1795170"></a>

### [`0073417c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md) → [`007341d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007341d4.md) FUN_007341d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00734070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0073a354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a354.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007340c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007340c8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0073a3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a3ac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007341d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md#insn-007341d0) · [`007341e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md#insn-007341e0) · [`00734210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md#insn-00734210)
- 新版 `00734228`（命令位置の公開資料なし） · `00734238`（命令位置の公開資料なし） · `00734268`（命令位置の公開資料なし）

~~~diff
- 007341d0 ["INT_ADD", "register:40f0:8", ["const:7341d0:8", "const:4:8"]]
- 007341d0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00734228 ["INT_ADD", "register:40f0:8", ["const:734228:8", "const:4:8"]]
+ 00734228 ["CALL", null, ["callee:0043bb60:8"]]
- 007341d0 bytes 541ef497
+ 00734228 bytes 4e1ef497
- 007341e0 ["INT_ADD", "register:40f0:8", ["const:7341e0:8", "const:4:8"]]
- 007341e0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00734238 ["INT_ADD", "register:40f0:8", ["const:734238:8", "const:4:8"]]
+ 00734238 ["CALL", null, ["callee:0043bb60:8"]]
- 007341e0 bytes 501ef497
+ 00734238 bytes 4a1ef497
- 00734210 ["INT_ADD", "register:40f0:8", ["const:734210:8", "const:4:8"]]
- 00734210 ["CALL", null, ["callee:0073a3ac:8"]]
+ 00734268 ["INT_ADD", "register:40f0:8", ["const:734268:8", "const:4:8"]]
+ 00734268 ["CALL", null, ["callee:0073a3ac:8"]]
- 00734210 bytes 51180094
+ 00734268 bytes 51180094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ef8230f34a7b74c8e22ff6ac738ba4f"></a>

### [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) → [`007342f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007342f8.md) FUN_007342f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 6件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 6件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00734420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/00734420.md) [`0073aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007342c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md#insn-007342c0) · [`007342dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md#insn-007342dc) · [`007342f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md#insn-007342f0)
- 新版 `00734318`（命令位置の公開資料なし） · `00734334`（命令位置の公開資料なし） · `00734348`（命令位置の公開資料なし）

~~~diff
- 007342c0 ["INT_ADD", "register:40f0:8", ["const:7342c0:8", "const:4:8"]]
- 007342c0 ["CALL", null, ["callee:0073aea0:8"]]
+ 00734318 ["INT_ADD", "register:40f0:8", ["const:734318:8", "const:4:8"]]
+ 00734318 ["CALL", null, ["callee:0073aea0:8"]]
- 007342c0 bytes e21a0094
+ 00734318 bytes e21a0094
- 007342dc ["INT_ADD", "register:40f0:8", ["const:7342dc:8", "const:4:8"]]
- 007342dc ["CALL", null, ["callee:00676aa0:8"]]
+ 00734334 ["INT_ADD", "register:40f0:8", ["const:734334:8", "const:4:8"]]
+ 00734334 ["CALL", null, ["callee:00676aa0:8"]]
- 007342dc bytes e109fd97
+ 00734334 bytes db09fd97
- 007342f0 ["INT_ADD", "register:40f0:8", ["const:7342f0:8", "const:4:8"]]
- 007342f0 ["CALL", null, ["callee:00734420:8"]]
+ 00734348 ["INT_ADD", "register:40f0:8", ["const:734348:8", "const:4:8"]]
+ 00734348 ["CALL", null, ["callee:00734420:8"]]
- 007342f0 bytes 36000094
+ 00734348 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbb96b3a17ee0ddeee9ef959387229f9"></a>

### [`007356b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md) → [`00735708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00735/00735708.md) FUN_00735708

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00736704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736704.md) [`00736c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) · 呼出先 5件 [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md) [`00a37064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37064.md) [`00a3787c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a3787c.md) [`00a38bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bbc.md) [`00a38bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bd8.md)
- 新版 呼出元 3件 [`00734420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/00734420.md) [`0073675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00736/0073675c.md) [`00736c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00736/00736c74.md) · 呼出先 5件 [`00a35bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a35bec.md) [`00a370b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a370b8.md) [`00a378d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a378d0.md) [`00a38c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38c10.md) [`00a38c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38c2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007356cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md#insn-007356cc) · [`007356d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md#insn-007356d0) · [`007356e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md#insn-007356e8)
- 新版 `00735724`（命令位置の公開資料なし） · `00735728`（命令位置の公開資料なし） · `00735740`（命令位置の公開資料なし）

~~~diff
- 007356cc ["INT_ADD", "register:40f0:8", ["const:7356cc:8", "const:4:8"]]
- 007356cc ["CALL", null, ["callee:00a35bec:8"]]
+ 00735724 ["INT_ADD", "register:40f0:8", ["const:735724:8", "const:4:8"]]
+ 00735724 ["CALL", null, ["callee:00a35bec:8"]]
- 007356cc bytes 33010c94
+ 00735724 bytes 32010c94
- 007356d0 ["INT_ADD", "register:40f0:8", ["const:7356d0:8", "const:4:8"]]
- 007356d0 ["CALL", null, ["callee:00a38c10:8"]]
+ 00735728 ["INT_ADD", "register:40f0:8", ["const:735728:8", "const:4:8"]]
+ 00735728 ["CALL", null, ["callee:00a38c10:8"]]
- 007356d0 bytes 3b0d0c94
+ 00735728 bytes 3a0d0c94
- 007356e8 ["INT_ADD", "register:40f0:8", ["const:7356e8:8", "const:4:8"]]
- 007356e8 ["CALL", null, ["callee:00a35bec:8"]]
+ 00735740 ["INT_ADD", "register:40f0:8", ["const:735740:8", "const:4:8"]]
+ 00735740 ["CALL", null, ["callee:00a35bec:8"]]
- 007356e8 bytes 2c010c94
+ 00735740 bytes 2b010c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5cd504cd338067b54b1936581e8249"></a>

### [`00738308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738308.md) → [`00738360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738360.md) FUN_00738360

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)
- 新版 呼出元 1件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 1件 [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738308.md#insn-00738320) · [`0073832c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738308.md#insn-0073832c)
- 新版 `00738378`（命令位置の公開資料なし） · `00738384`（命令位置の公開資料なし）

~~~diff
- 00738320 ["INT_ADD", "register:40f0:8", ["const:738320:8", "const:4:8"]]
- 00738320 ["CALL", null, ["callee:00480e68:8"]]
+ 00738378 ["INT_ADD", "register:40f0:8", ["const:738378:8", "const:4:8"]]
+ 00738378 ["CALL", null, ["callee:00480e68:8"]]
- 00738320 bytes c222f597
+ 00738378 bytes bc22f597
- 0073832c ["INT_ADD", "register:40f0:8", ["const:73832c:8", "const:4:8"]]
- 0073832c ["CALL", null, ["callee:00480e68:8"]]
+ 00738384 ["INT_ADD", "register:40f0:8", ["const:738384:8", "const:4:8"]]
+ 00738384 ["CALL", null, ["callee:00480e68:8"]]
- 0073832c bytes bf22f597
+ 00738384 bytes b922f597
~~~


<a id="compare-9bcd60c0d169b796e2d8dedab92ccc36"></a>

### [`00738344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738344.md) → [`0073839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/0073839c.md) FUN_0073839c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)
- 新版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 1件 [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738344.md#insn-00738358) · [`00738360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738344.md#insn-00738360)
- 新版 `007383b0`（命令位置の公開資料なし） · `007383b8`（命令位置の公開資料なし）

~~~diff
- 00738358 ["INT_ADD", "register:40f0:8", ["const:738358:8", "const:4:8"]]
- 00738358 ["CALL", null, ["callee:00480430:8"]]
+ 007383b0 ["INT_ADD", "register:40f0:8", ["const:7383b0:8", "const:4:8"]]
+ 007383b0 ["CALL", null, ["callee:00480430:8"]]
- 00738358 bytes 2620f597
+ 007383b0 bytes 2020f597
- 00738360 ["INT_ADD", "register:40f0:8", ["const:738360:8", "const:4:8"]]
- 00738360 ["CALL", null, ["callee:00480430:8"]]
+ 007383b8 ["INT_ADD", "register:40f0:8", ["const:7383b8:8", "const:4:8"]]
+ 007383b8 ["CALL", null, ["callee:00480430:8"]]
- 00738360 bytes 2420f597
+ 007383b8 bytes 1e20f597
~~~


<a id="compare-79f0109269d22b2939381b15d9b2b72a"></a>

### [`0073855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/0073855c.md) → [`007385b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/007385b4.md) FUN_007385b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 2件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/0073855c.md#insn-0073857c)
- 新版 `007385d4`（命令位置の公開資料なし）

~~~diff
- 0073857c ["INT_ADD", "register:40f0:8", ["const:73857c:8", "const:4:8"]]
- 0073857c ["CALL", null, ["callee:00480d88:8"]]
+ 007385d4 ["INT_ADD", "register:40f0:8", ["const:7385d4:8", "const:4:8"]]
+ 007385d4 ["CALL", null, ["callee:00480d88:8"]]
- 0073857c bytes f321f597
+ 007385d4 bytes ed21f597
~~~


<a id="compare-0aecc5b98a24e97bfec4ed65eadaccc8"></a>

### [`00738ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738ff8.md) → [`00739050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/00739050.md) FUN_00739050

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00739010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738ff8.md#insn-00739010)
- 新版 `00739068`（命令位置の公開資料なし）

~~~diff
- 00739010 ["INT_ADD", "register:40f0:8", ["const:739010:8", "const:4:8"]]
- 00739010 ["CALL", null, ["callee:005c17dc:8"]]
+ 00739068 ["INT_ADD", "register:40f0:8", ["const:739068:8", "const:4:8"]]
+ 00739068 ["CALL", null, ["callee:005c17dc:8"]]
- 00739010 bytes e321fa97
+ 00739068 bytes dd21fa97
~~~


<a id="compare-34fdd6f54f3d92daa5fb5c7ab7037919"></a>

### [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) → [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) FUN_0073a35c

採用 · 移動量 `+0x58` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) [`00738b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738b88.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) · 呼出先 2件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 10件 [`00737ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00737/00737ee4.md) [`00738be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738be0.md) [`007394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/007394fc.md) [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`0073aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aea0.md) · 呼出先 2件 [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md#insn-0073a320) · [`0073a32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md#insn-0073a32c) · [`0073a33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md#insn-0073a33c)
- 新版 `0073a378`（命令位置の公開資料なし） · `0073a384`（命令位置の公開資料なし） · `0073a394`（命令位置の公開資料なし）

~~~diff
- 0073a320 ["INT_ADD", "register:40f0:8", ["const:73a320:8", "const:4:8"]]
- 0073a320 ["CALL", null, ["local:b0:8"]]
+ 0073a378 ["INT_ADD", "register:40f0:8", ["const:73a378:8", "const:4:8"]]
+ 0073a378 ["CALL", null, ["local:b0:8"]]
- 0073a320 bytes f9ffff97
+ 0073a378 bytes f9ffff97
- 0073a32c ["INT_ADD", "register:40f0:8", ["const:73a32c:8", "const:4:8"]]
- 0073a32c ["CALL", null, ["local:b0:8"]]
+ 0073a384 ["INT_ADD", "register:40f0:8", ["const:73a384:8", "const:4:8"]]
+ 0073a384 ["CALL", null, ["local:b0:8"]]
- 0073a32c bytes f6ffff97
+ 0073a384 bytes f6ffff97
- 0073a33c ["INT_ADD", "register:40f0:8", ["const:73a33c:8", "const:4:8"]]
- 0073a33c ["CALL", null, ["callee:00c57f80:8"]]
+ 0073a394 ["INT_ADD", "register:40f0:8", ["const:73a394:8", "const:4:8"]]
+ 0073a394 ["CALL", null, ["callee:00c57f80:8"]]
- 0073a33c bytes dd761494
+ 0073a394 bytes fb761494
~~~


<a id="compare-463dad551a9d0451973c106a0631822f"></a>

### [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) → [`0073aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aea0.md) FUN_0073aea0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) [`007380e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007380e4.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 3件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`007342f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007342f8.md) [`0073813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/0073813c.md) [`0073aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aea0.md) [`00848180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848180.md) · 呼出先 3件 [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`0073aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aea0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ae68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md#insn-0073ae68) · [`0073ae74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md#insn-0073ae74) · [`0073ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md#insn-0073ae80)
- 新版 `0073aec0`（命令位置の公開資料なし） · `0073aecc`（命令位置の公開資料なし） · `0073aed8`（命令位置の公開資料なし）

~~~diff
- 0073ae68 ["INT_ADD", "register:40f0:8", ["const:73ae68:8", "const:4:8"]]
- 0073ae68 ["CALL", null, ["local:b0:8"]]
+ 0073aec0 ["INT_ADD", "register:40f0:8", ["const:73aec0:8", "const:4:8"]]
+ 0073aec0 ["CALL", null, ["local:b0:8"]]
- 0073ae68 bytes f8ffff97
+ 0073aec0 bytes f8ffff97
- 0073ae74 ["INT_ADD", "register:40f0:8", ["const:73ae74:8", "const:4:8"]]
- 0073ae74 ["CALL", null, ["local:b0:8"]]
+ 0073aecc ["INT_ADD", "register:40f0:8", ["const:73aecc:8", "const:4:8"]]
+ 0073aecc ["CALL", null, ["local:b0:8"]]
- 0073ae74 bytes f5ffff97
+ 0073aecc bytes f5ffff97
- 0073ae80 ["INT_ADD", "register:40f0:8", ["const:73ae80:8", "const:4:8"]]
- 0073ae80 ["CALL", null, ["callee:0073a35c:8"]]
+ 0073aed8 ["INT_ADD", "register:40f0:8", ["const:73aed8:8", "const:4:8"]]
+ 0073aed8 ["CALL", null, ["callee:0073a35c:8"]]
- 0073ae80 bytes 21fdff97
+ 0073aed8 bytes 21fdff97
~~~


<a id="compare-359477059619d19181763a3eacb79459"></a>

### [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) → [`0073aef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aef0.md) FUN_0073aef0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 2件 [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`007342f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00734/007342f8.md) [`00738804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738804.md) [`0073aef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aef0.md) [`00848180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848180.md) · 呼出先 2件 [`0073aef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073aef0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073aeb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md#insn-0073aeb8) · [`0073aec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md#insn-0073aec4)
- 新版 `0073af10`（命令位置の公開資料なし） · `0073af1c`（命令位置の公開資料なし）

~~~diff
- 0073aeb8 ["INT_ADD", "register:40f0:8", ["const:73aeb8:8", "const:4:8"]]
- 0073aeb8 ["CALL", null, ["local:b0:8"]]
+ 0073af10 ["INT_ADD", "register:40f0:8", ["const:73af10:8", "const:4:8"]]
+ 0073af10 ["CALL", null, ["local:b0:8"]]
- 0073aeb8 bytes f8ffff97
+ 0073af10 bytes f8ffff97
- 0073aec4 ["INT_ADD", "register:40f0:8", ["const:73aec4:8", "const:4:8"]]
- 0073aec4 ["CALL", null, ["local:b0:8"]]
+ 0073af1c ["INT_ADD", "register:40f0:8", ["const:73af1c:8", "const:4:8"]]
+ 0073af1c ["CALL", null, ["local:b0:8"]]
- 0073aec4 bytes f5ffff97
+ 0073af1c bytes f5ffff97
~~~


<a id="compare-b4a588e9bead14467e62c1c64d48ea2f"></a>

### [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) → [`0073af34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073af34.md) FUN_0073af34

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007350f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007350f4.md) [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 2件 [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0073514c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00735/0073514c.md) [`0073af34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073af34.md) [`00848180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848180.md) · 呼出先 2件 [`0073af34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073af34.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md#insn-0073aefc) · [`0073af08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md#insn-0073af08)
- 新版 `0073af54`（命令位置の公開資料なし） · `0073af60`（命令位置の公開資料なし）

~~~diff
- 0073aefc ["INT_ADD", "register:40f0:8", ["const:73aefc:8", "const:4:8"]]
- 0073aefc ["CALL", null, ["local:b0:8"]]
+ 0073af54 ["INT_ADD", "register:40f0:8", ["const:73af54:8", "const:4:8"]]
+ 0073af54 ["CALL", null, ["local:b0:8"]]
- 0073aefc bytes f8ffff97
+ 0073af54 bytes f8ffff97
- 0073af08 ["INT_ADD", "register:40f0:8", ["const:73af08:8", "const:4:8"]]
- 0073af08 ["CALL", null, ["local:b0:8"]]
+ 0073af60 ["INT_ADD", "register:40f0:8", ["const:73af60:8", "const:4:8"]]
+ 0073af60 ["CALL", null, ["local:b0:8"]]
- 0073af08 bytes f5ffff97
+ 0073af60 bytes f5ffff97
~~~


<a id="compare-fd68fa7ca045470cd0d6aea2fd6a1250"></a>

### [`0073af5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md) → [`0073afb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073afb4.md) FUN_0073afb4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00736704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736704.md) [`00736c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0073675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00736/0073675c.md) [`00736c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00736/00736c74.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md#insn-0073b00c) · [`0073b018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md#insn-0073b018) · [`0073b020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md#insn-0073b020)
- 新版 `0073b064`（命令位置の公開資料なし） · `0073b070`（命令位置の公開資料なし） · `0073b078`（命令位置の公開資料なし）

~~~diff
- 0073b00c ["INT_ADD", "register:40f0:8", ["const:73b00c:8", "const:4:8"]]
- 0073b00c ["CALL", null, ["callee:00494650:8"]]
+ 0073b064 ["INT_ADD", "register:40f0:8", ["const:73b064:8", "const:4:8"]]
+ 0073b064 ["CALL", null, ["callee:00494650:8"]]
- 0073b00c bytes 8165f597
+ 0073b064 bytes 7b65f597
- 0073b018 ["INT_ADD", "register:40f0:8", ["const:73b018:8", "const:4:8"]]
- 0073b018 ["CALL", null, ["callee:0073a35c:8"]]
+ 0073b070 ["INT_ADD", "register:40f0:8", ["const:73b070:8", "const:4:8"]]
+ 0073b070 ["CALL", null, ["callee:0073a35c:8"]]
- 0073b018 bytes bbfcff97
+ 0073b070 bytes bbfcff97
- 0073b020 ["INT_ADD", "register:40f0:8", ["const:73b020:8", "const:4:8"]]
- 0073b020 ["CALL", null, ["callee:00c57f80:8"]]
+ 0073b078 ["INT_ADD", "register:40f0:8", ["const:73b078:8", "const:4:8"]]
+ 0073b078 ["CALL", null, ["callee:00c57f80:8"]]
- 0073b020 bytes a4731494
+ 0073b078 bytes c2731494
~~~


<a id="compare-1d83008ba193aa40febb0602431fe12c"></a>

### [`0073b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md) → [`0073b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b08c.md) FUN_0073b08c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00738d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738d60.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0073b268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md) [`0073b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b428.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00738db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738db8.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0073b2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b2c0.md) [`0073b480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b480.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md#insn-0073b0ec) · [`0073b19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md#insn-0073b19c) · [`0073b1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md#insn-0073b1c0)
- 新版 `0073b144`（命令位置の公開資料なし） · `0073b1f4`（命令位置の公開資料なし） · `0073b218`（命令位置の公開資料なし）

~~~diff
- 0073b0ec ["INT_ADD", "register:40f0:8", ["const:73b0ec:8", "const:4:8"]]
- 0073b0ec ["CALL", null, ["callee:00c57f60:8"]]
+ 0073b144 ["INT_ADD", "register:40f0:8", ["const:73b144:8", "const:4:8"]]
+ 0073b144 ["CALL", null, ["callee:00c57f60:8"]]
- 0073b0ec bytes 69731494
+ 0073b144 bytes 87731494
- 0073b19c ["INT_ADD", "register:40f0:8", ["const:73b19c:8", "const:4:8"]]
- 0073b19c ["CALL", null, ["callee:0073b2c0:8"]]
+ 0073b1f4 ["INT_ADD", "register:40f0:8", ["const:73b1f4:8", "const:4:8"]]
+ 0073b1f4 ["CALL", null, ["callee:0073b2c0:8"]]
- 0073b19c bytes 33000094
+ 0073b1f4 bytes 33000094
- 0073b1c0 ["INT_ADD", "register:40f0:8", ["const:73b1c0:8", "const:4:8"]]
- 0073b1c0 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b218 ["INT_ADD", "register:40f0:8", ["const:73b218:8", "const:4:8"]]
+ 0073b218 ["CALL", null, ["callee:005c17dc:8"]]
- 0073b1c0 bytes 7719fa97
+ 0073b218 bytes 7119fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8644a8d39ea357ce21c3c5b063e88ec"></a>

### [`0073b268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md) → [`0073b2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b2c0.md) FUN_0073b2c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md) · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 1件 [`0073b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b08c.md) · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md#insn-0073b348) · [`0073b354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md#insn-0073b354)
- 新版 `0073b3a0`（命令位置の公開資料なし） · `0073b3ac`（命令位置の公開資料なし）

~~~diff
- 0073b348 ["INT_ADD", "register:40f0:8", ["const:73b348:8", "const:4:8"]]
- 0073b348 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b3a0 ["INT_ADD", "register:40f0:8", ["const:73b3a0:8", "const:4:8"]]
+ 0073b3a0 ["CALL", null, ["callee:005c17dc:8"]]
- 0073b348 bytes 1519fa97
+ 0073b3a0 bytes 0f19fa97
- 0073b354 ["INT_ADD", "register:40f0:8", ["const:73b354:8", "const:4:8"]]
- 0073b354 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b3ac ["INT_ADD", "register:40f0:8", ["const:73b3ac:8", "const:4:8"]]
+ 0073b3ac ["CALL", null, ["callee:005c17dc:8"]]
- 0073b354 bytes 1219fa97
+ 0073b3ac bytes 0c19fa97
~~~


<a id="compare-8592fb307c53e9cb267eafa908a13190"></a>

### [`0073b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b3b4.md) → [`0073b40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b40c.md) FUN_0073b40c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b3b4.md#insn-0073b3e4) · [`0073b3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b3b4.md#insn-0073b3f0)
- 新版 `0073b43c`（命令位置の公開資料なし） · `0073b448`（命令位置の公開資料なし）

~~~diff
- 0073b3e4 ["INT_ADD", "register:40f0:8", ["const:73b3e4:8", "const:4:8"]]
- 0073b3e4 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b43c ["INT_ADD", "register:40f0:8", ["const:73b43c:8", "const:4:8"]]
+ 0073b43c ["CALL", null, ["callee:005c17dc:8"]]
- 0073b3e4 bytes ee18fa97
+ 0073b43c bytes e818fa97
- 0073b3f0 ["INT_ADD", "register:40f0:8", ["const:73b3f0:8", "const:4:8"]]
- 0073b3f0 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b448 ["INT_ADD", "register:40f0:8", ["const:73b448:8", "const:4:8"]]
+ 0073b448 ["CALL", null, ["callee:005c17dc:8"]]
- 0073b3f0 bytes eb18fa97
+ 0073b448 bytes e518fa97
~~~


<a id="compare-002a8a6bc2c49fb067b1057b59257822"></a>

### [`0073b43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b43c.md) → [`0073b494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b494.md) FUN_0073b494

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b43c.md#insn-0073b474) · [`0073b480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b43c.md#insn-0073b480)
- 新版 `0073b4cc`（命令位置の公開資料なし） · `0073b4d8`（命令位置の公開資料なし）

~~~diff
- 0073b474 ["INT_ADD", "register:40f0:8", ["const:73b474:8", "const:4:8"]]
- 0073b474 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b4cc ["INT_ADD", "register:40f0:8", ["const:73b4cc:8", "const:4:8"]]
+ 0073b4cc ["CALL", null, ["callee:005c17dc:8"]]
- 0073b474 bytes ca18fa97
+ 0073b4cc bytes c418fa97
- 0073b480 ["INT_ADD", "register:40f0:8", ["const:73b480:8", "const:4:8"]]
- 0073b480 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b4d8 ["INT_ADD", "register:40f0:8", ["const:73b4d8:8", "const:4:8"]]
+ 0073b4d8 ["CALL", null, ["callee:005c17dc:8"]]
- 0073b480 bytes c718fa97
+ 0073b4d8 bytes c118fa97
~~~


<a id="compare-1628659ed0ed8d9d5fcbd4b767bcc1c4"></a>

### [`0073b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b4a0.md) → [`0073b4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b4f8.md) FUN_0073b4f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007391f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007391f0.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00739248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/00739248.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b4a0.md#insn-0073b4f4) · [`0073b500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b4a0.md#insn-0073b500)
- 新版 `0073b54c`（命令位置の公開資料なし） · `0073b558`（命令位置の公開資料なし）

~~~diff
- 0073b4f4 ["INT_ADD", "register:40f0:8", ["const:73b4f4:8", "const:4:8"]]
- 0073b4f4 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b54c ["INT_ADD", "register:40f0:8", ["const:73b54c:8", "const:4:8"]]
+ 0073b54c ["CALL", null, ["callee:005c17dc:8"]]
- 0073b4f4 bytes aa18fa97
+ 0073b54c bytes a418fa97
- 0073b500 ["INT_ADD", "register:40f0:8", ["const:73b500:8", "const:4:8"]]
- 0073b500 ["CALL", null, ["callee:005c17dc:8"]]
+ 0073b558 ["INT_ADD", "register:40f0:8", ["const:73b558:8", "const:4:8"]]
+ 0073b558 ["CALL", null, ["callee:005c17dc:8"]]
- 0073b500 bytes a718fa97
+ 0073b558 bytes a118fa97
~~~


<a id="compare-c6d79b050fad90a000076193b1624740"></a>

### [`0073b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b534.md) → [`0073b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073b58c.md) FUN_0073b58c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007391f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007391f0.md) · 呼出先 2件 [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00739248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00739/00739248.md) · 呼出先 2件 [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b534.md#insn-0073b5b4) · [`0073b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b534.md#insn-0073b5d4) · [`0073b668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b534.md#insn-0073b668)
- 新版 `0073b60c`（命令位置の公開資料なし） · `0073b62c`（命令位置の公開資料なし） · `0073b6c0`（命令位置の公開資料なし）

~~~diff
- 0073b5b4 ["INT_ADD", "register:40f0:8", ["const:73b5b4:8", "const:4:8"]]
- 0073b5b4 ["CALL", null, ["callee:00691858:8"]]
+ 0073b60c ["INT_ADD", "register:40f0:8", ["const:73b60c:8", "const:4:8"]]
+ 0073b60c ["CALL", null, ["callee:00691858:8"]]
- 0073b5b4 bytes 9358fd97
+ 0073b60c bytes 9358fd97
- 0073b5d4 ["INT_ADD", "register:40f0:8", ["const:73b5d4:8", "const:4:8"]]
- 0073b5d4 ["CALL", null, ["callee:00691858:8"]]
+ 0073b62c ["INT_ADD", "register:40f0:8", ["const:73b62c:8", "const:4:8"]]
+ 0073b62c ["CALL", null, ["callee:00691858:8"]]
- 0073b5d4 bytes 8b58fd97
+ 0073b62c bytes 8b58fd97
- 0073b668 ["INT_ADD", "register:40f0:8", ["const:73b668:8", "const:4:8"]]
- 0073b668 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0073b6c0 ["INT_ADD", "register:40f0:8", ["const:73b6c0:8", "const:4:8"]]
+ 0073b6c0 ["CALL", null, ["callee:00c57fb0:8"]]
- 0073b668 bytes 1e721494
+ 0073b6c0 bytes 3c721494
~~~


<a id="compare-001c192aa69cb3db7ff21c049b1471ab"></a>

### [`0073c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c878.md) → [`0073c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c8d0.md) FUN_0073c8d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073c898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c878.md#insn-0073c898) · [`0073c8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c878.md#insn-0073c8ac) · [`0073c8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c878.md#insn-0073c8b4)
- 新版 `0073c8f0`（命令位置の公開資料なし） · `0073c904`（命令位置の公開資料なし） · `0073c90c`（命令位置の公開資料なし）

~~~diff
- 0073c898 ["INT_ADD", "register:40f0:8", ["const:73c898:8", "const:4:8"]]
- 0073c898 ["CALL", null, ["callee:00c53da0:8"]]
+ 0073c8f0 ["INT_ADD", "register:40f0:8", ["const:73c8f0:8", "const:4:8"]]
+ 0073c8f0 ["CALL", null, ["callee:00c53da0:8"]]
- 0073c898 bytes 1a5d1494
+ 0073c8f0 bytes 2c5d1494
- 0073c8ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0073c8ac ["INT_ADD", "register:40f0:8", ["const:73c8ac:8", "const:4:8"]]
- 0073c8ac ["CALLIND", null, ["register:0:8"]]
+ 0073c904 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0073c904 ["INT_ADD", "register:40f0:8", ["const:73c904:8", "const:4:8"]]
+ 0073c904 ["CALLIND", null, ["register:0:8"]]
- 0073c8ac bytes 00013fd6
+ 0073c904 bytes 00013fd6
- 0073c8b4 ["INT_ADD", "register:40f0:8", ["const:73c8b4:8", "const:4:8"]]
- 0073c8b4 ["CALL", null, ["callee:00c57f50:8"]]
+ 0073c90c ["INT_ADD", "register:40f0:8", ["const:73c90c:8", "const:4:8"]]
+ 0073c90c ["CALL", null, ["callee:00c57f50:8"]]
- 0073c8b4 bytes 736d1494
+ 0073c90c bytes 916d1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a5b343a2030ddeb6639b4e90218cebd"></a>

### [`0073ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ed6c.md) → [`0073edc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073edc4.md) FUN_0073edc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0073d7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073d/0073d7fc.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ed6c.md#insn-0073ed90) · [`0073edd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ed6c.md#insn-0073edd8) · [`0073edf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ed6c.md#insn-0073edf8)
- 新版 `0073ede8`（命令位置の公開資料なし） · `0073ee30`（命令位置の公開資料なし） · `0073ee50`（命令位置の公開資料なし）

~~~diff
- 0073ed90 ["INT_ADD", "register:40f0:8", ["const:73ed90:8", "const:4:8"]]
- 0073ed90 ["CALL", null, ["callee:00c580b0:8"]]
+ 0073ede8 ["INT_ADD", "register:40f0:8", ["const:73ede8:8", "const:4:8"]]
+ 0073ede8 ["CALL", null, ["callee:00c580b0:8"]]
- 0073ed90 bytes 94641494
+ 0073ede8 bytes b2641494
- 0073edd8 ["INT_ADD", "register:40f0:8", ["const:73edd8:8", "const:4:8"]]
- 0073edd8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0073ee30 ["INT_ADD", "register:40f0:8", ["const:73ee30:8", "const:4:8"]]
+ 0073ee30 ["CALL", null, ["callee:00c57f60:8"]]
- 0073edd8 bytes 2e641494
+ 0073ee30 bytes 4c641494
- 0073edf8 ["INT_ADD", "register:40f0:8", ["const:73edf8:8", "const:4:8"]]
- 0073edf8 ["CALL", null, ["callee:00c58010:8"]]
+ 0073ee50 ["INT_ADD", "register:40f0:8", ["const:73ee50:8", "const:4:8"]]
+ 0073ee50 ["CALL", null, ["callee:00c58010:8"]]
- 0073edf8 bytes 52641494
+ 0073ee50 bytes 70641494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-182955c838179954378322f6b39989c9"></a>

### [`00741000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741000.md) → [`00741058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741058.md) FUN_00741058

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00740e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00740/00740e68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00740ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00740/00740ec0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00741010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741000.md#insn-00741010)
- 新版 `00741068`（命令位置の公開資料なし）

~~~diff
- 00741010 ["INT_ADD", "register:40f0:8", ["const:741010:8", "const:4:8"]]
- 00741010 ["CALL", null, ["callee:00740ec0:8"]]
+ 00741068 ["INT_ADD", "register:40f0:8", ["const:741068:8", "const:4:8"]]
+ 00741068 ["CALL", null, ["callee:00740ec0:8"]]
- 00741010 bytes 96ffff97
+ 00741068 bytes 96ffff97
~~~


<a id="compare-0e212070b94c56f44b355c6b6fda497b"></a>

### [`00741190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741190.md) → [`007411e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007411e8.md) FUN_007411e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007411c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741190.md#insn-007411c8)
- 新版 `00741220`（命令位置の公開資料なし）

~~~diff
- 007411c8 ["INT_ADD", "register:40f0:8", ["const:7411c8:8", "const:4:8"]]
- 007411c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00741220 ["INT_ADD", "register:40f0:8", ["const:741220:8", "const:4:8"]]
+ 00741220 ["CALL", null, ["callee:00c57f80:8"]]
- 007411c8 bytes 3a5b1494
+ 00741220 bytes 585b1494
~~~


<a id="compare-0979f4cb77235dcba6509adbdc7e03cd"></a>

### [`00743d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md) → [`00743de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md) FUN_00743de8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`007fa148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 14件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`007fa1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa1a0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md#insn-00743df4) · [`00743e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md#insn-00743e2c)
- 新版 `00743e4c`（命令位置の公開資料なし） · `00743e84`（命令位置の公開資料なし）

~~~diff
- 00743df4 ["INT_ADD", "register:40f0:8", ["const:743df4:8", "const:4:8"]]
- 00743df4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00743e4c ["INT_ADD", "register:40f0:8", ["const:743e4c:8", "const:4:8"]]
+ 00743e4c ["CALL", null, ["callee:00c57f60:8"]]
- 00743df4 bytes 27501494
+ 00743e4c bytes 45501494
- 00743e2c ["INT_ADD", "register:40f0:8", ["const:743e2c:8", "const:4:8"]]
- 00743e2c ["CALL", null, ["callee:0043bbe4:8"]]
+ 00743e84 ["INT_ADD", "register:40f0:8", ["const:743e84:8", "const:4:8"]]
+ 00743e84 ["CALL", null, ["callee:0043bbe4:8"]]
- 00743e2c bytes 5edff397
+ 00743e84 bytes 58dff397
~~~


<a id="compare-4bba62d424bcd5d44e78e14039136aca"></a>

### [`00743e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743e5c.md) → [`00743eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743eb4.md) FUN_00743eb4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) [`007fbe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) [`007fbe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbe60.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743e5c.md#insn-00743ec4) · [`00743efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743e5c.md#insn-00743efc)
- 新版 `00743f1c`（命令位置の公開資料なし） · `00743f54`（命令位置の公開資料なし）

~~~diff
- 00743ec4 ["INT_ADD", "register:40f0:8", ["const:743ec4:8", "const:4:8"]]
- 00743ec4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00743f1c ["INT_ADD", "register:40f0:8", ["const:743f1c:8", "const:4:8"]]
+ 00743f1c ["CALL", null, ["callee:00c57f60:8"]]
- 00743ec4 bytes f34f1494
+ 00743f1c bytes 11501494
- 00743efc ["INT_ADD", "register:40f0:8", ["const:743efc:8", "const:4:8"]]
- 00743efc ["CALL", null, ["callee:0043bbe4:8"]]
+ 00743f54 ["INT_ADD", "register:40f0:8", ["const:743f54:8", "const:4:8"]]
+ 00743f54 ["CALL", null, ["callee:0043bbe4:8"]]
- 00743efc bytes 2adff397
+ 00743f54 bytes 24dff397
~~~


<a id="compare-694d60cc95e2b2fb5f4c56bfb3286b1a"></a>

### [`00745434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md) → [`0074548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md) FUN_0074548c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00745458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md#insn-00745458) · [`00745464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md#insn-00745464) · [`00745470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md#insn-00745470)
- 新版 `007454b0`（命令位置の公開資料なし） · `007454bc`（命令位置の公開資料なし） · `007454c8`（命令位置の公開資料なし）

~~~diff
- 00745458 ["INT_ADD", "register:40f0:8", ["const:745458:8", "const:4:8"]]
- 00745458 ["CALL", null, ["callee:00480c28:8"]]
+ 007454b0 ["INT_ADD", "register:40f0:8", ["const:7454b0:8", "const:4:8"]]
+ 007454b0 ["CALL", null, ["callee:00480c28:8"]]
- 00745458 bytes e4edf497
+ 007454b0 bytes deedf497
- 00745464 ["INT_ADD", "register:40f0:8", ["const:745464:8", "const:4:8"]]
- 00745464 ["CALL", null, ["callee:00480bd0:8"]]
+ 007454bc ["INT_ADD", "register:40f0:8", ["const:7454bc:8", "const:4:8"]]
+ 007454bc ["CALL", null, ["callee:00480bd0:8"]]
- 00745464 bytes cbedf497
+ 007454bc bytes c5edf497
- 00745470 ["INT_ADD", "register:40f0:8", ["const:745470:8", "const:4:8"]]
- 00745470 ["CALL", null, ["callee:00480b78:8"]]
+ 007454c8 ["INT_ADD", "register:40f0:8", ["const:7454c8:8", "const:4:8"]]
+ 007454c8 ["CALL", null, ["callee:00480b78:8"]]
- 00745470 bytes b2edf497
+ 007454c8 bytes acedf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8acc0f8b3ed700e4db4cbb25e95ca88f"></a>

### [`00745930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md) → [`00745988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md) FUN_00745988

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007457cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/007457cc.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00a33c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md)
- 新版 呼出元 2件 [`00745824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745824.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 2件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00a33c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00745944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md#insn-00745944) · [`00745950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md#insn-00745950) · [`0074595c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md#insn-0074595c)
- 新版 `0074599c`（命令位置の公開資料なし） · `007459a8`（命令位置の公開資料なし） · `007459b4`（命令位置の公開資料なし）

~~~diff
- 00745944 ["INT_ADD", "register:40f0:8", ["const:745944:8", "const:4:8"]]
- 00745944 ["CALL", null, ["callee:0048cec4:8"]]
+ 0074599c ["INT_ADD", "register:40f0:8", ["const:74599c:8", "const:4:8"]]
+ 0074599c ["CALL", null, ["callee:0048cec4:8"]]
- 00745944 bytes 501df597
+ 0074599c bytes 4a1df597
- 00745950 ["INT_ADD", "register:40f0:8", ["const:745950:8", "const:4:8"]]
- 00745950 ["CALL", null, ["callee:00a33c70:8"]]
+ 007459a8 ["INT_ADD", "register:40f0:8", ["const:7459a8:8", "const:4:8"]]
+ 007459a8 ["CALL", null, ["callee:00a33c70:8"]]
- 00745950 bytes b3b80b94
+ 007459a8 bytes b2b80b94
- 0074595c ["INT_ADD", "register:40f0:8", ["const:74595c:8", "const:4:8"]]
- 0074595c ["CALL", null, ["callee:0048cec4:8"]]
+ 007459b4 ["INT_ADD", "register:40f0:8", ["const:7459b4:8", "const:4:8"]]
+ 007459b4 ["CALL", null, ["callee:0048cec4:8"]]
- 0074595c bytes 4a1df597
+ 007459b4 bytes 441df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cd5e65cc0ba4ef1e2886ca1fad6f607"></a>

### [`007468ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007468ec.md) → [`00746944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746944.md) FUN_00746944

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 4件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00746948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007468ec.md#insn-00746948) · [`00746968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007468ec.md#insn-00746968) · [`007469c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007468ec.md#insn-007469c0)
- 新版 `007469a0`（命令位置の公開資料なし） · `007469c0`（命令位置の公開資料なし） · `00746a18`（命令位置の公開資料なし）

~~~diff
- 00746948 ["INT_ADD", "register:40f0:8", ["const:746948:8", "const:4:8"]]
- 00746948 ["CALL", null, ["callee:0043bbe4:8"]]
+ 007469a0 ["INT_ADD", "register:40f0:8", ["const:7469a0:8", "const:4:8"]]
+ 007469a0 ["CALL", null, ["callee:0043bbe4:8"]]
- 00746948 bytes 97d4f397
+ 007469a0 bytes 91d4f397
- 00746968 ["INT_ADD", "register:40f0:8", ["const:746968:8", "const:4:8"]]
- 00746968 ["CALL", null, ["callee:00851550:8"]]
+ 007469c0 ["INT_ADD", "register:40f0:8", ["const:7469c0:8", "const:4:8"]]
+ 007469c0 ["CALL", null, ["callee:00851550:8"]]
- 00746968 bytes e42a0494
+ 007469c0 bytes e42a0494
- 007469c0 ["INT_ADD", "register:40f0:8", ["const:7469c0:8", "const:4:8"]]
- 007469c0 ["CALL", null, ["callee:00851550:8"]]
+ 00746a18 ["INT_ADD", "register:40f0:8", ["const:746a18:8", "const:4:8"]]
+ 00746a18 ["CALL", null, ["callee:00851550:8"]]
- 007469c0 bytes ce2a0494
+ 00746a18 bytes ce2a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c00f97b9663e875884a91201c096e71c"></a>

### [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) → [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) FUN_007472b4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 6件 [`00748f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f48.md) [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 6件 [`00748fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md) [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007472e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md#insn-007472e0) · [`00747304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md#insn-00747304) · [`0074734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md#insn-0074734c)
- 新版 `00747338`（命令位置の公開資料なし） · `0074735c`（命令位置の公開資料なし） · `007473a4`（命令位置の公開資料なし）

~~~diff
- 007472e0 ["INT_ADD", "register:40f0:8", ["const:7472e0:8", "const:4:8"]]
- 007472e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00747338 ["INT_ADD", "register:40f0:8", ["const:747338:8", "const:4:8"]]
+ 00747338 ["CALL", null, ["callee:00c57f60:8"]]
- 007472e0 bytes ec421494
+ 00747338 bytes 0a431494
- 00747304 ["INT_ADD", "register:40f0:8", ["const:747304:8", "const:4:8"]]
- 00747304 ["CALL", null, ["callee:0074a72c:8"]]
+ 0074735c ["INT_ADD", "register:40f0:8", ["const:74735c:8", "const:4:8"]]
+ 0074735c ["CALL", null, ["callee:0074a72c:8"]]
- 00747304 bytes f40c0094
+ 0074735c bytes f40c0094
- 0074734c ["INT_ADD", "register:40f0:8", ["const:74734c:8", "const:4:8"]]
- 0074734c ["CALL", null, ["callee:00748fa0:8"]]
+ 007473a4 ["INT_ADD", "register:40f0:8", ["const:7473a4:8", "const:4:8"]]
+ 007473a4 ["CALL", null, ["callee:00748fa0:8"]]
- 0074734c bytes ff060094
+ 007473a4 bytes ff060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0885fd2d0851225ef9af514a0e9be3"></a>

### [`007473e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473e0.md) → [`00747438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747438.md) FUN_00747438

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 17件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`007427b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/007427b0.md) [`007457cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/007457cc.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00a33c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md)
- 新版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 17件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00742808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742808.md) [`00745824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745824.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00a33c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473e0.md#insn-00747410) · [`00747418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473e0.md#insn-00747418) · [`0074741c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473e0.md#insn-0074741c)
- 新版 `00747468`（命令位置の公開資料なし） · `00747470`（命令位置の公開資料なし） · `00747474`（命令位置の公開資料なし）

~~~diff
- 00747410 ["INT_ADD", "register:40f0:8", ["const:747410:8", "const:4:8"]]
- 00747410 ["CALL", null, ["callee:0048cec4:8"]]
+ 00747468 ["INT_ADD", "register:40f0:8", ["const:747468:8", "const:4:8"]]
+ 00747468 ["CALL", null, ["callee:0048cec4:8"]]
- 00747410 bytes 9d16f597
+ 00747468 bytes 9716f597
- 00747418 ["INT_ADD", "register:40f0:8", ["const:747418:8", "const:4:8"]]
- 00747418 ["CALL", null, ["callee:00a35bec:8"]]
+ 00747470 ["INT_ADD", "register:40f0:8", ["const:747470:8", "const:4:8"]]
+ 00747470 ["CALL", null, ["callee:00a35bec:8"]]
- 00747418 bytes e0b90b94
+ 00747470 bytes dfb90b94
- 0074741c ["INT_ADD", "register:40f0:8", ["const:74741c:8", "const:4:8"]]
- 0074741c ["CALL", null, ["callee:00a38c10:8"]]
+ 00747474 ["INT_ADD", "register:40f0:8", ["const:747474:8", "const:4:8"]]
+ 00747474 ["CALL", null, ["callee:00a38c10:8"]]
- 0074741c bytes e8c50b94
+ 00747474 bytes e7c50b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0e8c4c4e0046cec96ec2f9639fb1632"></a>

### [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) → [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) FUN_0074785c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00742bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/00742bb8.md) [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md) · 呼出先 2件 [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00742c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742c10.md) [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008493c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008493c8.md) · 呼出先 2件 [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md#insn-00747820) · [`0074782c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md#insn-0074782c) · [`0074783c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md#insn-0074783c)
- 新版 `00747878`（命令位置の公開資料なし） · `00747884`（命令位置の公開資料なし） · `00747894`（命令位置の公開資料なし）

~~~diff
- 00747820 ["INT_ADD", "register:40f0:8", ["const:747820:8", "const:4:8"]]
- 00747820 ["CALL", null, ["local:b0:8"]]
+ 00747878 ["INT_ADD", "register:40f0:8", ["const:747878:8", "const:4:8"]]
+ 00747878 ["CALL", null, ["local:b0:8"]]
- 00747820 bytes f9ffff97
+ 00747878 bytes f9ffff97
- 0074782c ["INT_ADD", "register:40f0:8", ["const:74782c:8", "const:4:8"]]
- 0074782c ["CALL", null, ["local:b0:8"]]
+ 00747884 ["INT_ADD", "register:40f0:8", ["const:747884:8", "const:4:8"]]
+ 00747884 ["CALL", null, ["local:b0:8"]]
- 0074782c bytes f6ffff97
+ 00747884 bytes f6ffff97
- 0074783c ["INT_ADD", "register:40f0:8", ["const:74783c:8", "const:4:8"]]
- 0074783c ["CALL", null, ["callee:00c57f80:8"]]
+ 00747894 ["INT_ADD", "register:40f0:8", ["const:747894:8", "const:4:8"]]
+ 00747894 ["CALL", null, ["callee:00c57f80:8"]]
- 0074783c bytes 9d411494
+ 00747894 bytes bb411494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b08ce58c2b9c04b45659395b9d977c3"></a>

### [`00747a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747a60.md) → [`00747ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747ab8.md) FUN_00747ab8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745a24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00745a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745a7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747a60.md#insn-00747a9c)
- 新版 `00747af4`（命令位置の公開資料なし）

~~~diff
- 00747a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00747a9c ["INT_ADD", "register:40f0:8", ["const:747a9c:8", "const:4:8"]]
- 00747a9c ["CALLIND", null, ["register:0:8"]]
+ 00747af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00747af4 ["INT_ADD", "register:40f0:8", ["const:747af4:8", "const:4:8"]]
+ 00747af4 ["CALLIND", null, ["register:0:8"]]
- 00747a9c bytes 00013fd6
+ 00747af4 bytes 00013fd6
~~~


<a id="compare-62c0236222b5402cbb05211cd0a2b4f5"></a>

### [`007481bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007481bc.md) → [`00748214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748214.md) FUN_00748214

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745fb4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0074600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074600c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007481f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007481bc.md#insn-007481f8)
- 新版 `00748250`（命令位置の公開資料なし）

~~~diff
- 007481f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007481f8 ["INT_ADD", "register:40f0:8", ["const:7481f8:8", "const:4:8"]]
- 007481f8 ["CALLIND", null, ["register:0:8"]]
+ 00748250 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748250 ["INT_ADD", "register:40f0:8", ["const:748250:8", "const:4:8"]]
+ 00748250 ["CALLIND", null, ["register:0:8"]]
- 007481f8 bytes 00013fd6
+ 00748250 bytes 00013fd6
~~~


<a id="compare-45be5267e5f9e1c5523472f047f8f31c"></a>

### [`0074820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md) → [`00748264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md) FUN_00748264

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`0071d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`0071d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d18c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007482d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md#insn-007482d8) · [`007482e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md#insn-007482e8) · [`007482fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md#insn-007482fc)
- 新版 `00748330`（命令位置の公開資料なし） · `00748340`（命令位置の公開資料なし） · `00748354`（命令位置の公開資料なし）

~~~diff
- 007482d8 ["INT_ADD", "register:40f0:8", ["const:7482d8:8", "const:4:8"]]
- 007482d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00748330 ["INT_ADD", "register:40f0:8", ["const:748330:8", "const:4:8"]]
+ 00748330 ["CALL", null, ["callee:00c57f60:8"]]
- 007482d8 bytes ee3e1494
+ 00748330 bytes 0c3f1494
- 007482e8 ["INT_ADD", "register:40f0:8", ["const:7482e8:8", "const:4:8"]]
- 007482e8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00748340 ["INT_ADD", "register:40f0:8", ["const:748340:8", "const:4:8"]]
+ 00748340 ["CALL", null, ["callee:00c580d0:8"]]
- 007482e8 bytes 463f1494
+ 00748340 bytes 643f1494
- 007482fc ["INT_ADD", "register:40f0:8", ["const:7482fc:8", "const:4:8"]]
- 007482fc ["CALL", null, ["callee:0071d18c:8"]]
+ 00748354 ["INT_ADD", "register:40f0:8", ["const:748354:8", "const:4:8"]]
+ 00748354 ["CALL", null, ["callee:0071d18c:8"]]
- 007482fc bytes 8e53ff97
+ 00748354 bytes 8e53ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-139d5de0e53a00382ea1d4af11fa8399"></a>

### [`00748678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748678.md) → [`007486d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007486d0.md) FUN_007486d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745fb4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0074600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074600c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007486b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748678.md#insn-007486b4)
- 新版 `0074870c`（命令位置の公開資料なし）

~~~diff
- 007486b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 007486b4 ["INT_ADD", "register:40f0:8", ["const:7486b4:8", "const:4:8"]]
- 007486b4 ["CALLIND", null, ["register:0:8"]]
+ 0074870c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074870c ["INT_ADD", "register:40f0:8", ["const:74870c:8", "const:4:8"]]
+ 0074870c ["CALLIND", null, ["register:0:8"]]
- 007486b4 bytes 00013fd6
+ 0074870c bytes 00013fd6
~~~


<a id="compare-2e9bf350669cf96dad87b8a02d55c4f6"></a>

### [`007486c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007486c8.md) → [`00748720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748720.md) FUN_00748720

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007486c8.md#insn-00748708) · [`0074873c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007486c8.md#insn-0074873c) · [`00748740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007486c8.md#insn-00748740)
- 新版 `00748760`（命令位置の公開資料なし） · `00748794`（命令位置の公開資料なし） · `00748798`（命令位置の公開資料なし）

~~~diff
- 00748708 ["COPY", "register:0:8", ["register:4040:8"]]
- 00748708 ["INT_ADD", "register:40f0:8", ["const:748708:8", "const:4:8"]]
- 00748708 ["CALLIND", null, ["register:0:8"]]
+ 00748760 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748760 ["INT_ADD", "register:40f0:8", ["const:748760:8", "const:4:8"]]
+ 00748760 ["CALLIND", null, ["register:0:8"]]
- 00748708 bytes 00013fd6
+ 00748760 bytes 00013fd6
- 0074873c ["INT_ADD", "register:40f0:8", ["const:74873c:8", "const:4:8"]]
- 0074873c ["CALL", null, ["callee:00459db4:8"]]
+ 00748794 ["INT_ADD", "register:40f0:8", ["const:748794:8", "const:4:8"]]
+ 00748794 ["CALL", null, ["callee:00459db4:8"]]
- 0074873c bytes 8e45f497
+ 00748794 bytes 8845f497
- 00748740 ["INT_ADD", "register:40f0:8", ["const:748740:8", "const:4:8"]]
- 00748740 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00748798 ["INT_ADD", "register:40f0:8", ["const:748798:8", "const:4:8"]]
+ 00748798 ["CALL", null, ["callee:00c57fb0:8"]]
- 00748740 bytes e83d1494
+ 00748798 bytes 063e1494
~~~


<a id="compare-2f55a47961777a38df9890c3bfa7ee57"></a>

### [`0074889c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074889c.md) → [`007488f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488f4.md) FUN_007488f4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`0071d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`0071d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d18c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074889c.md#insn-00748914) · [`00748928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074889c.md#insn-00748928) · [`00748998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074889c.md#insn-00748998)
- 新版 `0074896c`（命令位置の公開資料なし） · `00748980`（命令位置の公開資料なし） · `007489f0`（命令位置の公開資料なし）

~~~diff
- 00748914 ["INT_ADD", "register:40f0:8", ["const:748914:8", "const:4:8"]]
- 00748914 ["CALL", null, ["callee:00c57f60:8"]]
+ 0074896c ["INT_ADD", "register:40f0:8", ["const:74896c:8", "const:4:8"]]
+ 0074896c ["CALL", null, ["callee:00c57f60:8"]]
- 00748914 bytes 5f3d1494
+ 0074896c bytes 7d3d1494
- 00748928 ["INT_ADD", "register:40f0:8", ["const:748928:8", "const:4:8"]]
- 00748928 ["CALL", null, ["callee:00c580d0:8"]]
+ 00748980 ["INT_ADD", "register:40f0:8", ["const:748980:8", "const:4:8"]]
+ 00748980 ["CALL", null, ["callee:00c580d0:8"]]
- 00748928 bytes b63d1494
+ 00748980 bytes d43d1494
- 00748998 ["INT_ADD", "register:40f0:8", ["const:748998:8", "const:4:8"]]
- 00748998 ["CALL", null, ["callee:0071d18c:8"]]
+ 007489f0 ["INT_ADD", "register:40f0:8", ["const:7489f0:8", "const:4:8"]]
+ 007489f0 ["CALL", null, ["callee:0071d18c:8"]]
- 00748998 bytes e751ff97
+ 007489f0 bytes e751ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fff5d57683ec5481fcb09de5d766711"></a>

### [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) → [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) FUN_00748b88

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) [`00748d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md) [`00748f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f5c.md) [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) [`00748d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md) [`00748fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fb4.md) [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md#insn-00748b50) · [`00748b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md#insn-00748b8c) · [`00748b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md#insn-00748b9c)
- 新版 `00748ba8`（命令位置の公開資料なし） · `00748be4`（命令位置の公開資料なし） · `00748bf4`（命令位置の公開資料なし）

~~~diff
- 00748b50 ["INT_ADD", "register:40f0:8", ["const:748b50:8", "const:4:8"]]
- 00748b50 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748ba8 ["INT_ADD", "register:40f0:8", ["const:748ba8:8", "const:4:8"]]
+ 00748ba8 ["CALL", null, ["callee:00c57f80:8"]]
- 00748b50 bytes d83c1494
+ 00748ba8 bytes f63c1494
- 00748b8c ["INT_ADD", "register:40f0:8", ["const:748b8c:8", "const:4:8"]]
- 00748b8c ["CALL", null, ["callee:00c57f80:8"]]
+ 00748be4 ["INT_ADD", "register:40f0:8", ["const:748be4:8", "const:4:8"]]
+ 00748be4 ["CALL", null, ["callee:00c57f80:8"]]
- 00748b8c bytes c93c1494
+ 00748be4 bytes e73c1494
- 00748b9c ["INT_ADD", "register:40f0:8", ["const:748b9c:8", "const:4:8"]]
- 00748b9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00748bf4 ["INT_ADD", "register:40f0:8", ["const:748bf4:8", "const:4:8"]]
+ 00748bf4 ["CALL", null, ["callee:00c57f80:8"]]
- 00748b9c bytes c53c1494
+ 00748bf4 bytes e33c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dce39a732122b725895e1993ba6dbec7"></a>

### [`00748bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748bdc.md) → [`00748c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748c34.md) FUN_00748c34

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748bdc.md#insn-00748bfc) · [`00748c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748bdc.md#insn-00748c38) · [`00748c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748bdc.md#insn-00748c48)
- 新版 `00748c54`（命令位置の公開資料なし） · `00748c90`（命令位置の公開資料なし） · `00748ca0`（命令位置の公開資料なし）

~~~diff
- 00748bfc ["INT_ADD", "register:40f0:8", ["const:748bfc:8", "const:4:8"]]
- 00748bfc ["CALL", null, ["callee:00c57f80:8"]]
+ 00748c54 ["INT_ADD", "register:40f0:8", ["const:748c54:8", "const:4:8"]]
+ 00748c54 ["CALL", null, ["callee:00c57f80:8"]]
- 00748bfc bytes ad3c1494
+ 00748c54 bytes cb3c1494
- 00748c38 ["INT_ADD", "register:40f0:8", ["const:748c38:8", "const:4:8"]]
- 00748c38 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748c90 ["INT_ADD", "register:40f0:8", ["const:748c90:8", "const:4:8"]]
+ 00748c90 ["CALL", null, ["callee:00c57f80:8"]]
- 00748c38 bytes 9e3c1494
+ 00748c90 bytes bc3c1494
- 00748c48 ["INT_ADD", "register:40f0:8", ["const:748c48:8", "const:4:8"]]
- 00748c48 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748ca0 ["INT_ADD", "register:40f0:8", ["const:748ca0:8", "const:4:8"]]
+ 00748ca0 ["CALL", null, ["callee:00c57f80:8"]]
- 00748c48 bytes 9a3c1494
+ 00748ca0 bytes b83c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11e0afcbab3ba29d459ef032db74c263"></a>

### [`00748c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748c88.md) → [`00748ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748ce0.md) FUN_00748ce0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748c88.md#insn-00748cd4) · [`00748ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748c88.md#insn-00748ce4) · [`00748cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748c88.md#insn-00748cf4)
- 新版 `00748d2c`（命令位置の公開資料なし） · `00748d3c`（命令位置の公開資料なし） · `00748d4c`（命令位置の公開資料なし）

~~~diff
- 00748cd4 ["INT_ADD", "register:40f0:8", ["const:748cd4:8", "const:4:8"]]
- 00748cd4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748d2c ["INT_ADD", "register:40f0:8", ["const:748d2c:8", "const:4:8"]]
+ 00748d2c ["CALL", null, ["callee:00c57f80:8"]]
- 00748cd4 bytes 773c1494
+ 00748d2c bytes 953c1494
- 00748ce4 ["INT_ADD", "register:40f0:8", ["const:748ce4:8", "const:4:8"]]
- 00748ce4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748d3c ["INT_ADD", "register:40f0:8", ["const:748d3c:8", "const:4:8"]]
+ 00748d3c ["CALL", null, ["callee:00c57f80:8"]]
- 00748ce4 bytes 733c1494
+ 00748d3c bytes 913c1494
- 00748cf4 ["INT_ADD", "register:40f0:8", ["const:748cf4:8", "const:4:8"]]
- 00748cf4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748d4c ["INT_ADD", "register:40f0:8", ["const:748d4c:8", "const:4:8"]]
+ 00748d4c ["CALL", null, ["callee:00c57f80:8"]]
- 00748cf4 bytes 6f3c1494
+ 00748d4c bytes 8d3c1494
~~~


<a id="compare-42f1d4a8cd8b04fb2e58ce6c29e4cd14"></a>

### [`00748d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md) → [`00748d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md) FUN_00748d7c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00748f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00749a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749a2c.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00748fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md#insn-00748dc4) · [`00748efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md#insn-00748efc) · [`00748f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md#insn-00748f20)
- 新版 `00748e1c`（命令位置の公開資料なし） · `00748f54`（命令位置の公開資料なし） · `00748f78`（命令位置の公開資料なし）

~~~diff
- 00748dc4 ["INT_ADD", "register:40f0:8", ["const:748dc4:8", "const:4:8"]]
- 00748dc4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00748e1c ["INT_ADD", "register:40f0:8", ["const:748e1c:8", "const:4:8"]]
+ 00748e1c ["CALL", null, ["callee:00c57f60:8"]]
- 00748dc4 bytes 333c1494
+ 00748e1c bytes 513c1494
- 00748efc ["INT_ADD", "register:40f0:8", ["const:748efc:8", "const:4:8"]]
- 00748efc ["CALL", null, ["callee:00748b88:8"]]
+ 00748f54 ["INT_ADD", "register:40f0:8", ["const:748f54:8", "const:4:8"]]
+ 00748f54 ["CALL", null, ["callee:00748b88:8"]]
- 00748efc bytes 0dffff97
+ 00748f54 bytes 0dffff97
- 00748f20 ["INT_ADD", "register:40f0:8", ["const:748f20:8", "const:4:8"]]
- 00748f20 ["CALL", null, ["callee:00c57f80:8"]]
+ 00748f78 ["INT_ADD", "register:40f0:8", ["const:748f78:8", "const:4:8"]]
+ 00748f78 ["CALL", null, ["callee:00c57f80:8"]]
- 00748f20 bytes e43b1494
+ 00748f78 bytes 023c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b970118dcde159d42abda74d08be322"></a>

### [`00748f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f5c.md) → [`00748fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fb4.md) FUN_00748fb4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f5c.md#insn-00748f9c)
- 新版 `00748ff4`（命令位置の公開資料なし）

~~~diff
- 00748f9c ["INT_ADD", "register:40f0:8", ["const:748f9c:8", "const:4:8"]]
- 00748f9c ["CALL", null, ["callee:00748b88:8"]]
+ 00748ff4 ["INT_ADD", "register:40f0:8", ["const:748ff4:8", "const:4:8"]]
+ 00748ff4 ["CALL", null, ["callee:00748b88:8"]]
- 00748f9c bytes e5feff97
+ 00748ff4 bytes e5feff97
~~~


<a id="compare-684f33da83640eb6abc8993f3684afe1"></a>

### [`0074a318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a318.md) → [`0074a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a370.md) FUN_0074a370

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a318.md#insn-0074a34c) · [`0074a368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a318.md#insn-0074a368) · [`0074a378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a318.md#insn-0074a378)
- 新版 `0074a3a4`（命令位置の公開資料なし） · `0074a3c0`（命令位置の公開資料なし） · `0074a3d0`（命令位置の公開資料なし）

~~~diff
- 0074a34c ["INT_ADD", "register:40f0:8", ["const:74a34c:8", "const:4:8"]]
- 0074a34c ["CALL", null, ["callee:00c57f80:8"]]
+ 0074a3a4 ["INT_ADD", "register:40f0:8", ["const:74a3a4:8", "const:4:8"]]
+ 0074a3a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0074a34c bytes d9361494
+ 0074a3a4 bytes f7361494
- 0074a368 ["INT_ADD", "register:40f0:8", ["const:74a368:8", "const:4:8"]]
- 0074a368 ["CALL", null, ["callee:00c57f80:8"]]
+ 0074a3c0 ["INT_ADD", "register:40f0:8", ["const:74a3c0:8", "const:4:8"]]
+ 0074a3c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0074a368 bytes d2361494
+ 0074a3c0 bytes f0361494
- 0074a378 ["INT_ADD", "register:40f0:8", ["const:74a378:8", "const:4:8"]]
- 0074a378 ["CALL", null, ["callee:00c57f80:8"]]
+ 0074a3d0 ["INT_ADD", "register:40f0:8", ["const:74a3d0:8", "const:4:8"]]
+ 0074a3d0 ["CALL", null, ["callee:00c57f80:8"]]
- 0074a378 bytes ce361494
+ 0074a3d0 bytes ec361494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6958c5cbddfa863244ddfa8e8940f5e5"></a>

### [`0074a57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a57c.md) → [`0074a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a5d4.md) FUN_0074a5d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a57c.md#insn-0074a5b8)
- 新版 `0074a610`（命令位置の公開資料なし）

~~~diff
- 0074a5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a5b8 ["INT_ADD", "register:40f0:8", ["const:74a5b8:8", "const:4:8"]]
- 0074a5b8 ["CALLIND", null, ["register:0:8"]]
+ 0074a610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a610 ["INT_ADD", "register:40f0:8", ["const:74a610:8", "const:4:8"]]
+ 0074a610 ["CALLIND", null, ["register:0:8"]]
- 0074a5b8 bytes 00013fd6
+ 0074a610 bytes 00013fd6
~~~


<a id="compare-18cb2ccd11bbdda1cdd328c2008eda8b"></a>

### [`0074a5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a5cc.md) → [`0074a624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a624.md) FUN_0074a624

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a5cc.md#insn-0074a604) · [`0074a628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a5cc.md#insn-0074a628)
- 新版 `0074a65c`（命令位置の公開資料なし） · `0074a680`（命令位置の公開資料なし）

~~~diff
- 0074a604 ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a604 ["INT_ADD", "register:40f0:8", ["const:74a604:8", "const:4:8"]]
- 0074a604 ["CALLIND", null, ["register:0:8"]]
+ 0074a65c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a65c ["INT_ADD", "register:40f0:8", ["const:74a65c:8", "const:4:8"]]
+ 0074a65c ["CALLIND", null, ["register:0:8"]]
- 0074a604 bytes 00013fd6
+ 0074a65c bytes 00013fd6
- 0074a628 ["INT_ADD", "register:40f0:8", ["const:74a628:8", "const:4:8"]]
- 0074a628 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0074a680 ["INT_ADD", "register:40f0:8", ["const:74a680:8", "const:4:8"]]
+ 0074a680 ["CALL", null, ["callee:00c57fb0:8"]]
- 0074a628 bytes 2e361494
+ 0074a680 bytes 4c361494
~~~


<a id="compare-f2d5098299939c63118b81049db3b045"></a>

### [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) → [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) FUN_0074a6ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) · 呼出先 2件 [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) · 呼出先 2件 [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md#insn-0074a6a8)
- 新版 `0074a700`（命令位置の公開資料なし）

~~~diff
- 0074a6a8 ["INT_ADD", "register:40f0:8", ["const:74a6a8:8", "const:4:8"]]
- 0074a6a8 ["CALL", null, ["callee:00748b88:8"]]
+ 0074a700 ["INT_ADD", "register:40f0:8", ["const:74a700:8", "const:4:8"]]
+ 0074a700 ["CALL", null, ["callee:00748b88:8"]]
- 0074a6a8 bytes 22f9ff97
+ 0074a700 bytes 22f9ff97
~~~


<a id="compare-3283cca049b874d26a85cc4fecb46ce8"></a>

### [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) → [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) FUN_0074a72c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0074a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md#insn-0074a754) · [`0074a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md#insn-0074a76c) · [`0074a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md#insn-0074a7d0)
- 新版 `0074a7ac`（命令位置の公開資料なし） · `0074a7c4`（命令位置の公開資料なし） · `0074a828`（命令位置の公開資料なし）

~~~diff
- 0074a754 ["INT_ADD", "register:40f0:8", ["const:74a754:8", "const:4:8"]]
- 0074a754 ["CALL", null, ["callee:0074a82c:8"]]
+ 0074a7ac ["INT_ADD", "register:40f0:8", ["const:74a7ac:8", "const:4:8"]]
+ 0074a7ac ["CALL", null, ["callee:0074a82c:8"]]
- 0074a754 bytes 20000094
+ 0074a7ac bytes 20000094
- 0074a76c ["INT_ADD", "register:40f0:8", ["const:74a76c:8", "const:4:8"]]
- 0074a76c ["CALL", null, ["callee:0043bb60:8"]]
+ 0074a7c4 ["INT_ADD", "register:40f0:8", ["const:74a7c4:8", "const:4:8"]]
+ 0074a7c4 ["CALL", null, ["callee:0043bb60:8"]]
- 0074a76c bytes edc4f397
+ 0074a7c4 bytes e7c4f397
- 0074a7d0 ["INT_ADD", "register:40f0:8", ["const:74a7d0:8", "const:4:8"]]
- 0074a7d0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0074a828 ["INT_ADD", "register:40f0:8", ["const:74a828:8", "const:4:8"]]
+ 0074a828 ["CALL", null, ["callee:00c57fb0:8"]]
- 0074a7d0 bytes c4351494
+ 0074a828 bytes e2351494
~~~


<a id="compare-02ae8a4103d50d88f329ea5a4e3f41f8"></a>

### [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md) → [`0074a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md) FUN_0074a82c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) [`008a3c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3c98.md) [`009aae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aae00.md) [`009ac2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac2b8.md) [`009afea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009afea8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) [`008a3cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3cf0.md) [`009aae54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aae54.md) [`009ac30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac30c.md) [`009afefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md#insn-0074a828) · [`0074a854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md#insn-0074a854) · [`0074a86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md#insn-0074a86c)
- 新版 `0074a880`（命令位置の公開資料なし） · `0074a8ac`（命令位置の公開資料なし） · `0074a8c4`（命令位置の公開資料なし）

~~~diff
- 0074a828 ["INT_ADD", "register:40f0:8", ["const:74a828:8", "const:4:8"]]
- 0074a828 ["CALL", null, ["callee:0043bb60:8"]]
+ 0074a880 ["INT_ADD", "register:40f0:8", ["const:74a880:8", "const:4:8"]]
+ 0074a880 ["CALL", null, ["callee:0043bb60:8"]]
- 0074a828 bytes bec4f397
+ 0074a880 bytes b8c4f397
- 0074a854 ["INT_ADD", "register:40f0:8", ["const:74a854:8", "const:4:8"]]
- 0074a854 ["CALL", null, ["callee:00c57f60:8"]]
+ 0074a8ac ["INT_ADD", "register:40f0:8", ["const:74a8ac:8", "const:4:8"]]
+ 0074a8ac ["CALL", null, ["callee:00c57f60:8"]]
- 0074a854 bytes 8f351494
+ 0074a8ac bytes ad351494
- 0074a86c ["INT_ADD", "register:40f0:8", ["const:74a86c:8", "const:4:8"]]
- 0074a86c ["CALL", null, ["callee:00c580d0:8"]]
+ 0074a8c4 ["INT_ADD", "register:40f0:8", ["const:74a8c4:8", "const:4:8"]]
+ 0074a8c4 ["CALL", null, ["callee:00c580d0:8"]]
- 0074a86c bytes e5351494
+ 0074a8c4 bytes 03361494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd27e0f617d3281724859d3d1808738d"></a>

### [`0074dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074d/0074dfb0.md) → [`0074e008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e008.md) FUN_0074e008

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0091ab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091ab78.md) · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0091abcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091abcc.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074dffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074d/0074dfb0.md#insn-0074dffc) · [`0074e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074d/0074dfb0.md#insn-0074e004) · [`0074e008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074d/0074dfb0.md#insn-0074e008)
- 新版 `0074e054`（命令位置の公開資料なし） · `0074e05c`（命令位置の公開資料なし） · `0074e060`（命令位置の公開資料なし）

~~~diff
- 0074dffc ["INT_ADD", "register:40f0:8", ["const:74dffc:8", "const:4:8"]]
- 0074dffc ["CALL", null, ["callee:004678a0:8"]]
+ 0074e054 ["INT_ADD", "register:40f0:8", ["const:74e054:8", "const:4:8"]]
+ 0074e054 ["CALL", null, ["callee:004678a0:8"]]
- 0074dffc bytes 1966f497
+ 0074e054 bytes 1366f497
- 0074e004 ["INT_ADD", "register:40f0:8", ["const:74e004:8", "const:4:8"]]
- 0074e004 ["CALL", null, ["callee:00851550:8"]]
+ 0074e05c ["INT_ADD", "register:40f0:8", ["const:74e05c:8", "const:4:8"]]
+ 0074e05c ["CALL", null, ["callee:00851550:8"]]
- 0074e004 bytes 3d0d0494
+ 0074e05c bytes 3d0d0494
- 0074e008 ["INT_ADD", "register:40f0:8", ["const:74e008:8", "const:4:8"]]
- 0074e008 ["CALL", null, ["callee:0046ca04:8"]]
+ 0074e060 ["INT_ADD", "register:40f0:8", ["const:74e060:8", "const:4:8"]]
+ 0074e060 ["CALL", null, ["callee:0046ca04:8"]]
- 0074e008 bytes 6f7af497
+ 0074e060 bytes 697af497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef07619f9ce79f98e8bfe6be700b7241"></a>

### [`00755b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00755/00755b60.md) → [`00755bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bb8.md) FUN_00755bb8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00755a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00755/00755a68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00755ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00755b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00755/00755b60.md#insn-00755b70)
- 新版 `00755bc8`（命令位置の公開資料なし）

~~~diff
- 00755b70 ["INT_ADD", "register:40f0:8", ["const:755b70:8", "const:4:8"]]
- 00755b70 ["CALL", null, ["callee:00755ac0:8"]]
+ 00755bc8 ["INT_ADD", "register:40f0:8", ["const:755bc8:8", "const:4:8"]]
+ 00755bc8 ["CALL", null, ["callee:00755ac0:8"]]
- 00755b70 bytes beffff97
+ 00755bc8 bytes beffff97
~~~


