# v16.0.1 → v16.0.2 · 要調査の変更候補 (28)

[一覧の目次](README.md)

<a id="compare-6d98dc47a88032c2150d33b5615ae1a7"></a>

### [`0087bbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md) → [`0087bc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc1c.md) FUN_0087bc1c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md#insn-0087bc04) · [`0087bc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md#insn-0087bc30)
- 新版 `0087bc5c`（命令位置の公開資料なし） · `0087bc88`（命令位置の公開資料なし）

~~~diff
- 0087bc04 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bc04 ["INT_ADD", "register:40f0:8", ["const:87bc04:8", "const:4:8"]]
- 0087bc04 ["CALLIND", null, ["register:0:8"]]
+ 0087bc5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bc5c ["INT_ADD", "register:40f0:8", ["const:87bc5c:8", "const:4:8"]]
+ 0087bc5c ["CALLIND", null, ["register:0:8"]]
- 0087bc04 bytes 00013fd6
+ 0087bc5c bytes 00013fd6
- 0087bc30 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bc30 ["INT_ADD", "register:40f0:8", ["const:87bc30:8", "const:4:8"]]
- 0087bc30 ["CALLIND", null, ["register:0:8"]]
+ 0087bc88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bc88 ["INT_ADD", "register:40f0:8", ["const:87bc88:8", "const:4:8"]]
+ 0087bc88 ["CALLIND", null, ["register:0:8"]]
- 0087bc30 bytes 00013fd6
+ 0087bc88 bytes 00013fd6
~~~


<a id="compare-7b5b7ee28796fd6239b01a78f614c083"></a>

### [`0087bf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bf28.md) → [`0087bf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bf80.md) FUN_0087bf80

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bf28.md#insn-0087bf68)
- 新版 `0087bfc0`（命令位置の公開資料なし）

~~~diff
- 0087bf68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bf68 ["INT_ADD", "register:40f0:8", ["const:87bf68:8", "const:4:8"]]
- 0087bf68 ["CALLIND", null, ["register:0:8"]]
+ 0087bfc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bfc0 ["INT_ADD", "register:40f0:8", ["const:87bfc0:8", "const:4:8"]]
+ 0087bfc0 ["CALLIND", null, ["register:0:8"]]
- 0087bf68 bytes 00013fd6
+ 0087bfc0 bytes 00013fd6
~~~


<a id="compare-b4cce51d180086eccbb072c25e3c6057"></a>

### [`0087c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c178.md) → [`0087c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md) FUN_0087c1d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c178.md#insn-0087c1b4)
- 新版 `0087c20c`（命令位置の公開資料なし）

~~~diff
- 0087c1b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c1b4 ["INT_ADD", "register:40f0:8", ["const:87c1b4:8", "const:4:8"]]
- 0087c1b4 ["CALLIND", null, ["register:0:8"]]
+ 0087c20c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c20c ["INT_ADD", "register:40f0:8", ["const:87c20c:8", "const:4:8"]]
+ 0087c20c ["CALLIND", null, ["register:0:8"]]
- 0087c1b4 bytes 00013fd6
+ 0087c20c bytes 00013fd6
~~~


<a id="compare-939131df6e05d94ff572007feb94354f"></a>

### [`0087c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c1c8.md) → [`0087c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c220.md) FUN_0087c220

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c1c8.md#insn-0087c1e4)
- 新版 `0087c23c`（命令位置の公開資料なし）

~~~diff
- 0087c1e4 ["INT_ADD", "register:40f0:8", ["const:87c1e4:8", "const:4:8"]]
- 0087c1e4 ["CALL", null, ["callee:00459db4:8"]]
+ 0087c23c ["INT_ADD", "register:40f0:8", ["const:87c23c:8", "const:4:8"]]
+ 0087c23c ["CALL", null, ["callee:00459db4:8"]]
- 0087c1e4 bytes e476ef97
+ 0087c23c bytes de76ef97
~~~


<a id="compare-ba8f734b21f20d4c24f9aa447a8d295f"></a>

### [`0087c3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c3e4.md) → [`0087c43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c43c.md) FUN_0087c43c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c3e4.md#insn-0087c420)
- 新版 `0087c478`（命令位置の公開資料なし）

~~~diff
- 0087c420 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c420 ["INT_ADD", "register:40f0:8", ["const:87c420:8", "const:4:8"]]
- 0087c420 ["CALLIND", null, ["register:0:8"]]
+ 0087c478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c478 ["INT_ADD", "register:40f0:8", ["const:87c478:8", "const:4:8"]]
+ 0087c478 ["CALLIND", null, ["register:0:8"]]
- 0087c420 bytes 00013fd6
+ 0087c478 bytes 00013fd6
~~~


<a id="compare-ebc148ab15d18a5066c4cbe3beca343b"></a>

### [`0087c434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c434.md) → [`0087c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c48c.md) FUN_0087c48c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c434.md#insn-0087c464) · [`0087c47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c434.md#insn-0087c47c) · [`0087c490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c434.md#insn-0087c490)
- 新版 `0087c4bc`（命令位置の公開資料なし） · `0087c4d4`（命令位置の公開資料なし） · `0087c4e8`（命令位置の公開資料なし）

~~~diff
- 0087c464 ["INT_ADD", "register:40f0:8", ["const:87c464:8", "const:4:8"]]
- 0087c464 ["CALL", null, ["callee:00c5aad0:8"]]
+ 0087c4bc ["INT_ADD", "register:40f0:8", ["const:87c4bc:8", "const:4:8"]]
+ 0087c4bc ["CALL", null, ["callee:00c5aad0:8"]]
- 0087c464 bytes 67790f94
+ 0087c4bc bytes 85790f94
- 0087c47c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c47c ["INT_ADD", "register:40f0:8", ["const:87c47c:8", "const:4:8"]]
- 0087c47c ["CALLIND", null, ["register:0:8"]]
+ 0087c4d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c4d4 ["INT_ADD", "register:40f0:8", ["const:87c4d4:8", "const:4:8"]]
+ 0087c4d4 ["CALLIND", null, ["register:0:8"]]
- 0087c47c bytes 00013fd6
+ 0087c4d4 bytes 00013fd6
- 0087c490 ["INT_ADD", "register:40f0:8", ["const:87c490:8", "const:4:8"]]
- 0087c490 ["CALL", null, ["callee:00c5aae0:8"]]
+ 0087c4e8 ["INT_ADD", "register:40f0:8", ["const:87c4e8:8", "const:4:8"]]
+ 0087c4e8 ["CALL", null, ["callee:00c5aae0:8"]]
- 0087c490 bytes 60790f94
+ 0087c4e8 bytes 7e790f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1053213c0b1616120b3e34f6c95f51a8"></a>

### [`0087c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c7e0.md) → [`0087c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md) FUN_0087c838

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c7e0.md#insn-0087c81c)
- 新版 `0087c874`（命令位置の公開資料なし）

~~~diff
- 0087c81c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c81c ["INT_ADD", "register:40f0:8", ["const:87c81c:8", "const:4:8"]]
- 0087c81c ["CALLIND", null, ["register:0:8"]]
+ 0087c874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c874 ["INT_ADD", "register:40f0:8", ["const:87c874:8", "const:4:8"]]
+ 0087c874 ["CALLIND", null, ["register:0:8"]]
- 0087c81c bytes 00013fd6
+ 0087c874 bytes 00013fd6
~~~


<a id="compare-271187723196c92b5583d069fdaaeca3"></a>

### [`0087c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c830.md) → [`0087c888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c888.md) FUN_0087c888

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c830.md#insn-0087c84c)
- 新版 `0087c8a4`（命令位置の公開資料なし）

~~~diff
- 0087c84c ["INT_ADD", "register:40f0:8", ["const:87c84c:8", "const:4:8"]]
- 0087c84c ["CALL", null, ["callee:00459db4:8"]]
+ 0087c8a4 ["INT_ADD", "register:40f0:8", ["const:87c8a4:8", "const:4:8"]]
+ 0087c8a4 ["CALL", null, ["callee:00459db4:8"]]
- 0087c84c bytes 4a75ef97
+ 0087c8a4 bytes 4475ef97
~~~


<a id="compare-75701d5a37b57648c51cbbebc24a3bd8"></a>

### [`0087cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087cc2c.md) → [`0087cc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cc84.md) FUN_0087cc84

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087cc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087cc2c.md#insn-0087cc6c) · [`0087cc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087cc2c.md#insn-0087cc98)
- 新版 `0087ccc4`（命令位置の公開資料なし） · `0087ccf0`（命令位置の公開資料なし）

~~~diff
- 0087cc6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cc6c ["INT_ADD", "register:40f0:8", ["const:87cc6c:8", "const:4:8"]]
- 0087cc6c ["CALLIND", null, ["register:0:8"]]
+ 0087ccc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087ccc4 ["INT_ADD", "register:40f0:8", ["const:87ccc4:8", "const:4:8"]]
+ 0087ccc4 ["CALLIND", null, ["register:0:8"]]
- 0087cc6c bytes 00013fd6
+ 0087ccc4 bytes 00013fd6
- 0087cc98 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cc98 ["INT_ADD", "register:40f0:8", ["const:87cc98:8", "const:4:8"]]
- 0087cc98 ["CALLIND", null, ["register:0:8"]]
+ 0087ccf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087ccf0 ["INT_ADD", "register:40f0:8", ["const:87ccf0:8", "const:4:8"]]
+ 0087ccf0 ["CALLIND", null, ["register:0:8"]]
- 0087cc98 bytes 00013fd6
+ 0087ccf0 bytes 00013fd6
~~~


<a id="compare-3a7bed810406f3ed830272e6246960be"></a>

### [`0087d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d27c.md) → [`0087d2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2d4.md) FUN_0087d2d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d27c.md#insn-0087d28c)
- 新版 `0087d2e4`（命令位置の公開資料なし）

~~~diff
- 0087d28c ["INT_ADD", "register:40f0:8", ["const:87d28c:8", "const:4:8"]]
- 0087d28c ["CALL", null, ["callee:00c5ab90:8"]]
+ 0087d2e4 ["INT_ADD", "register:40f0:8", ["const:87d2e4:8", "const:4:8"]]
+ 0087d2e4 ["CALL", null, ["callee:00c5ab90:8"]]
- 0087d28c bytes 0d760f94
+ 0087d2e4 bytes 2b760f94
~~~


<a id="compare-e407745158a7396becf399c6a8551c98"></a>

### [`0087d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md) → [`0087d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md) FUN_0087d2f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`00575d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) [`00575d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575d54.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md#insn-0087d2f8) · [`0087d30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md#insn-0087d30c) · [`0087d328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md#insn-0087d328)
- 新版 `0087d350`（命令位置の公開資料なし） · `0087d364`（命令位置の公開資料なし） · `0087d380`（命令位置の公開資料なし）

~~~diff
- 0087d2f8 ["INT_ADD", "register:40f0:8", ["const:87d2f8:8", "const:4:8"]]
- 0087d2f8 ["CALL", null, ["callee:00493e08:8"]]
+ 0087d350 ["INT_ADD", "register:40f0:8", ["const:87d350:8", "const:4:8"]]
+ 0087d350 ["CALL", null, ["callee:00493e08:8"]]
- 0087d2f8 bytes b45af097
+ 0087d350 bytes ae5af097
- 0087d30c ["INT_ADD", "register:40f0:8", ["const:87d30c:8", "const:4:8"]]
- 0087d30c ["CALL", null, ["callee:00c57f80:8"]]
+ 0087d364 ["INT_ADD", "register:40f0:8", ["const:87d364:8", "const:4:8"]]
+ 0087d364 ["CALL", null, ["callee:00c57f80:8"]]
- 0087d30c bytes e96a0f94
+ 0087d364 bytes 076b0f94
- 0087d328 ["INT_ADD", "register:40f0:8", ["const:87d328:8", "const:4:8"]]
- 0087d328 ["CALL", null, ["callee:00575d54:8"]]
+ 0087d380 ["INT_ADD", "register:40f0:8", ["const:87d380:8", "const:4:8"]]
+ 0087d380 ["CALL", null, ["callee:00575d54:8"]]
- 0087d328 bytes 7be2f397
+ 0087d380 bytes 75e2f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82c1de75d1bc482bee15956f4f04644"></a>

### [`0087d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md) → [`0087d3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d3d8.md) FUN_0087d3d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00575ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575ca4.md) [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00575ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575ce4.md) [`0058ae08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md#insn-0087d3ac) · [`0087d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md#insn-0087d3f8) · [`0087d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md#insn-0087d418)
- 新版 `0087d404`（命令位置の公開資料なし） · `0087d450`（命令位置の公開資料なし） · `0087d470`（命令位置の公開資料なし）

~~~diff
- 0087d3ac ["INT_ADD", "register:40f0:8", ["const:87d3ac:8", "const:4:8"]]
- 0087d3ac ["CALL", null, ["callee:00c580b0:8"]]
+ 0087d404 ["INT_ADD", "register:40f0:8", ["const:87d404:8", "const:4:8"]]
+ 0087d404 ["CALL", null, ["callee:00c580b0:8"]]
- 0087d3ac bytes 0d6b0f94
+ 0087d404 bytes 2b6b0f94
- 0087d3f8 ["INT_ADD", "register:40f0:8", ["const:87d3f8:8", "const:4:8"]]
- 0087d3f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087d450 ["INT_ADD", "register:40f0:8", ["const:87d450:8", "const:4:8"]]
+ 0087d450 ["CALL", null, ["callee:00c57f60:8"]]
- 0087d3f8 bytes a66a0f94
+ 0087d450 bytes c46a0f94
- 0087d418 ["INT_ADD", "register:40f0:8", ["const:87d418:8", "const:4:8"]]
- 0087d418 ["CALL", null, ["callee:00c580d0:8"]]
+ 0087d470 ["INT_ADD", "register:40f0:8", ["const:87d470:8", "const:4:8"]]
+ 0087d470 ["CALL", null, ["callee:00c580d0:8"]]
- 0087d418 bytes fa6a0f94
+ 0087d470 bytes 186b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471250f3330bccb19c2be89abc41c860"></a>

### [`0087d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md) → [`0087d948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d948.md) FUN_0087d948

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58230.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaf0.md) [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md)
- 新版 呼出元 1件 [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58300.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abc0.md) [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md#insn-0087d928) · [`0087d934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md#insn-0087d934) · [`0087d944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md#insn-0087d944)
- 新版 `0087d980`（命令位置の公開資料なし） · `0087d98c`（命令位置の公開資料なし） · `0087d99c`（命令位置の公開資料なし）

~~~diff
- 0087d928 ["INT_ADD", "register:40f0:8", ["const:87d928:8", "const:4:8"]]
- 0087d928 ["CALL", null, ["callee:00c5abc0:8"]]
+ 0087d980 ["INT_ADD", "register:40f0:8", ["const:87d980:8", "const:4:8"]]
+ 0087d980 ["CALL", null, ["callee:00c5abc0:8"]]
- 0087d928 bytes 72740f94
+ 0087d980 bytes 90740f94
- 0087d934 ["INT_ADD", "register:40f0:8", ["const:87d934:8", "const:4:8"]]
- 0087d934 ["CALL", null, ["callee:00c5abd0:8"]]
+ 0087d98c ["INT_ADD", "register:40f0:8", ["const:87d98c:8", "const:4:8"]]
+ 0087d98c ["CALL", null, ["callee:00c5abd0:8"]]
- 0087d934 bytes 73740f94
+ 0087d98c bytes 91740f94
- 0087d944 ["INT_ADD", "register:40f0:8", ["const:87d944:8", "const:4:8"]]
- 0087d944 ["CALL", null, ["callee:00c5a900:8"]]
+ 0087d99c ["INT_ADD", "register:40f0:8", ["const:87d99c:8", "const:4:8"]]
+ 0087d99c ["CALL", null, ["callee:00c5a900:8"]]
- 0087d944 bytes bb730f94
+ 0087d99c bytes d9730f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c2f7664af36f7962387c417068126f"></a>

### [`0087d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md) → [`0087da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md) FUN_0087da1c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087da04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md#insn-0087da04) · [`0087da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md#insn-0087da10) · [`0087da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md#insn-0087da48)
- 新版 `0087da5c`（命令位置の公開資料なし） · `0087da68`（命令位置の公開資料なし） · `0087daa0`（命令位置の公開資料なし）

~~~diff
- 0087da04 ["INT_ADD", "register:40f0:8", ["const:87da04:8", "const:4:8"]]
- 0087da04 ["CALL", null, ["callee:00c5abe0:8"]]
+ 0087da5c ["INT_ADD", "register:40f0:8", ["const:87da5c:8", "const:4:8"]]
+ 0087da5c ["CALL", null, ["callee:00c5abe0:8"]]
- 0087da04 bytes 43740f94
+ 0087da5c bytes 61740f94
- 0087da10 ["INT_ADD", "register:40f0:8", ["const:87da10:8", "const:4:8"]]
- 0087da10 ["CALL", null, ["callee:00c5abf0:8"]]
+ 0087da68 ["INT_ADD", "register:40f0:8", ["const:87da68:8", "const:4:8"]]
+ 0087da68 ["CALL", null, ["callee:00c5abf0:8"]]
- 0087da10 bytes 44740f94
+ 0087da68 bytes 62740f94
- 0087da48 ["INT_ADD", "register:40f0:8", ["const:87da48:8", "const:4:8"]]
- 0087da48 ["CALL", null, ["callee:00c58500:8"]]
+ 0087daa0 ["INT_ADD", "register:40f0:8", ["const:87daa0:8", "const:4:8"]]
+ 0087daa0 ["CALL", null, ["callee:00c58500:8"]]
- 0087da48 bytes 7a6a0f94
+ 0087daa0 bytes 986a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c6e6b17d40adb82d146115a6b21ee41"></a>

### [`0087e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md) → [`0087e62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e62c.md) FUN_0087e62c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 7件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 7件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md) [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087e634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md#insn-0087e634) · [`0087e63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md#insn-0087e63c) · [`0087e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md#insn-0087e640)
- 新版 `0087e68c`（命令位置の公開資料なし） · `0087e694`（命令位置の公開資料なし） · `0087e698`（命令位置の公開資料なし）

~~~diff
- 0087e634 ["INT_ADD", "register:40f0:8", ["const:87e634:8", "const:4:8"]]
- 0087e634 ["CALL", null, ["callee:00588eac:8"]]
+ 0087e68c ["INT_ADD", "register:40f0:8", ["const:87e68c:8", "const:4:8"]]
+ 0087e68c ["CALL", null, ["callee:00588eac:8"]]
- 0087e634 bytes 0e2af497
+ 0087e68c bytes 082af497
- 0087e63c ["INT_ADD", "register:40f0:8", ["const:87e63c:8", "const:4:8"]]
- 0087e63c ["CALL", null, ["callee:0058919c:8"]]
+ 0087e694 ["INT_ADD", "register:40f0:8", ["const:87e694:8", "const:4:8"]]
+ 0087e694 ["CALL", null, ["callee:0058919c:8"]]
- 0087e63c bytes c82af497
+ 0087e694 bytes c22af497
- 0087e640 ["INT_ADD", "register:40f0:8", ["const:87e640:8", "const:4:8"]]
- 0087e640 ["CALL", null, ["callee:00589890:8"]]
+ 0087e698 ["INT_ADD", "register:40f0:8", ["const:87e698:8", "const:4:8"]]
+ 0087e698 ["CALL", null, ["callee:00589890:8"]]
- 0087e640 bytes 842cf497
+ 0087e698 bytes 7e2cf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e812d59a9f7da701b12348b38daa77"></a>

### [`0087e6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6dc.md) → [`0087e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e734.md) FUN_0087e734

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 1件 [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 1件 [`0087ec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ec14.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6dc.md#insn-0087e6f4)
- 新版 `0087e74c`（命令位置の公開資料なし）

~~~diff
- 0087e6f4 ["INT_ADD", "register:40f0:8", ["const:87e6f4:8", "const:4:8"]]
- 0087e6f4 ["CALL", null, ["callee:0087ec14:8"]]
+ 0087e74c ["INT_ADD", "register:40f0:8", ["const:87e74c:8", "const:4:8"]]
+ 0087e74c ["CALL", null, ["callee:0087ec14:8"]]
- 0087e6f4 bytes 32010094
+ 0087e74c bytes 32010094
~~~


<a id="compare-d9e8989cd38b85cd4df3b94c8c7c4538"></a>

### [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) → [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) FUN_0087eb18

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00763d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763d58.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0087d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md) [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md)
- 新版 呼出元 8件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00763db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763db0.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`0087d948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d948.md) [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md#insn-0087eae0) · [`0087eaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md#insn-0087eaf4)
- 新版 `0087eb38`（命令位置の公開資料なし） · `0087eb4c`（命令位置の公開資料なし）

~~~diff
- 0087eae0 ["INT_ADD", "register:40f0:8", ["const:87eae0:8", "const:4:8"]]
- 0087eae0 ["CALL", null, ["callee:0087eca0:8"]]
+ 0087eb38 ["INT_ADD", "register:40f0:8", ["const:87eb38:8", "const:4:8"]]
+ 0087eb38 ["CALL", null, ["callee:0087eca0:8"]]
- 0087eae0 bytes 5a000094
+ 0087eb38 bytes 5a000094
- 0087eaf4 ["INT_ADD", "register:40f0:8", ["const:87eaf4:8", "const:4:8"]]
- 0087eaf4 ["CALL", null, ["callee:0087d948:8"]]
+ 0087eb4c ["INT_ADD", "register:40f0:8", ["const:87eb4c:8", "const:4:8"]]
+ 0087eb4c ["CALL", null, ["callee:0087d948:8"]]
- 0087eaf4 bytes 7ffbff97
+ 0087eb4c bytes 7ffbff97
~~~


<a id="compare-65858f4dbfe0a82f31195c1bf9acc341"></a>

### [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) → [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) FUN_0087eb78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009cc648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md) · 呼出先 2件 [`0087d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md) [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md)
- 新版 呼出元 1件 [`009cc69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc69c.md) · 呼出先 2件 [`0087da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087da1c.md) [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md#insn-0087eb38)
- 新版 `0087eb90`（命令位置の公開資料なし）

~~~diff
- 0087eb38 ["INT_ADD", "register:40f0:8", ["const:87eb38:8", "const:4:8"]]
- 0087eb38 ["CALL", null, ["callee:0087eca0:8"]]
+ 0087eb90 ["INT_ADD", "register:40f0:8", ["const:87eb90:8", "const:4:8"]]
+ 0087eb90 ["CALL", null, ["callee:0087eca0:8"]]
- 0087eb38 bytes 44000094
+ 0087eb90 bytes 44000094
~~~


<a id="compare-1cd0ba73a09a653d76f9afdc8d16cd79"></a>

### [`0087eb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb6c.md) → [`0087ebc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ebc4.md) FUN_0087ebc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb6c.md#insn-0087eb88) · [`0087eba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb6c.md#insn-0087eba8)
- 新版 `0087ebe0`（命令位置の公開資料なし） · `0087ec00`（命令位置の公開資料なし）

~~~diff
- 0087eb88 ["INT_ADD", "register:40f0:8", ["const:87eb88:8", "const:4:8"]]
- 0087eb88 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087ebe0 ["INT_ADD", "register:40f0:8", ["const:87ebe0:8", "const:4:8"]]
+ 0087ebe0 ["CALL", null, ["callee:00c53da0:8"]]
- 0087eb88 bytes 5e540f94
+ 0087ebe0 bytes 70540f94
- 0087eba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087eba8 ["INT_ADD", "register:40f0:8", ["const:87eba8:8", "const:4:8"]]
- 0087eba8 ["CALLIND", null, ["register:0:8"]]
+ 0087ec00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087ec00 ["INT_ADD", "register:40f0:8", ["const:87ec00:8", "const:4:8"]]
+ 0087ec00 ["CALLIND", null, ["register:0:8"]]
- 0087eba8 bytes 00013fd6
+ 0087ec00 bytes 00013fd6
~~~


<a id="compare-0958d85b37eb331cd91947c1912900b0"></a>

### [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) → [`0087ec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ec14.md) FUN_0087ec14

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0087e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6d0.md) [`0087e6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6dc.md) [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) · 呼出先 4件 [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0087e728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e728.md) [`0087e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e734.md) [`0087ec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ec14.md) · 呼出先 4件 [`0087ec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ec14.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ebd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md#insn-0087ebd8) · [`0087ebe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md#insn-0087ebe4) · [`0087ebf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md#insn-0087ebf8)
- 新版 `0087ec30`（命令位置の公開資料なし） · `0087ec3c`（命令位置の公開資料なし） · `0087ec50`（命令位置の公開資料なし）

~~~diff
- 0087ebd8 ["INT_ADD", "register:40f0:8", ["const:87ebd8:8", "const:4:8"]]
- 0087ebd8 ["CALL", null, ["local:b0:8"]]
+ 0087ec30 ["INT_ADD", "register:40f0:8", ["const:87ec30:8", "const:4:8"]]
+ 0087ec30 ["CALL", null, ["local:b0:8"]]
- 0087ebd8 bytes f9ffff97
+ 0087ec30 bytes f9ffff97
- 0087ebe4 ["INT_ADD", "register:40f0:8", ["const:87ebe4:8", "const:4:8"]]
- 0087ebe4 ["CALL", null, ["local:b0:8"]]
+ 0087ec3c ["INT_ADD", "register:40f0:8", ["const:87ec3c:8", "const:4:8"]]
+ 0087ec3c ["CALL", null, ["local:b0:8"]]
- 0087ebe4 bytes f6ffff97
+ 0087ec3c bytes f6ffff97
- 0087ebf8 ["INT_ADD", "register:40f0:8", ["const:87ebf8:8", "const:4:8"]]
- 0087ebf8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087ec50 ["INT_ADD", "register:40f0:8", ["const:87ec50:8", "const:4:8"]]
+ 0087ec50 ["CALL", null, ["callee:00c53da0:8"]]
- 0087ebf8 bytes 42540f94
+ 0087ec50 bytes 54540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0ba0ba18f2a718c65a35a54aab8333"></a>

### [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md) → [`0087eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eca0.md) FUN_0087eca0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) [`0087eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb78.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ecb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md#insn-0087ecb4) · [`0087ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md#insn-0087ed10)
- 新版 `0087ed0c`（命令位置の公開資料なし） · `0087ed68`（命令位置の公開資料なし）

~~~diff
- 0087ecb4 ["INT_ADD", "register:40f0:8", ["const:87ecb4:8", "const:4:8"]]
- 0087ecb4 ["CALL", null, ["callee:00c58120:8"]]
+ 0087ed0c ["INT_ADD", "register:40f0:8", ["const:87ed0c:8", "const:4:8"]]
+ 0087ed0c ["CALL", null, ["callee:00c58120:8"]]
- 0087ecb4 bytes e7640f94
+ 0087ed0c bytes 05650f94
- 0087ed10 ["INT_ADD", "register:40f0:8", ["const:87ed10:8", "const:4:8"]]
- 0087ed10 ["CALL", null, ["callee:00c58120:8"]]
+ 0087ed68 ["INT_ADD", "register:40f0:8", ["const:87ed68:8", "const:4:8"]]
+ 0087ed68 ["CALL", null, ["callee:00c58120:8"]]
- 0087ed10 bytes d0640f94
+ 0087ed68 bytes ee640f94
~~~


<a id="compare-d6dbb1729eb99a0524974047354f0f69"></a>

### [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) → [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) FUN_0087eda4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0087ee78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0087eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md#insn-0087ed80) · [`0087eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md#insn-0087eda0) · [`0087eddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md#insn-0087eddc)
- 新版 `0087edd8`（命令位置の公開資料なし） · `0087edf8`（命令位置の公開資料なし） · `0087ee34`（命令位置の公開資料なし）

~~~diff
- 0087ed80 ["INT_ADD", "register:40f0:8", ["const:87ed80:8", "const:4:8"]]
- 0087ed80 ["CALL", null, ["callee:0087eed0:8"]]
+ 0087edd8 ["INT_ADD", "register:40f0:8", ["const:87edd8:8", "const:4:8"]]
+ 0087edd8 ["CALL", null, ["callee:0087eed0:8"]]
- 0087ed80 bytes 3e000094
+ 0087edd8 bytes 3e000094
- 0087eda0 ["INT_ADD", "register:40f0:8", ["const:87eda0:8", "const:4:8"]]
- 0087eda0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087edf8 ["INT_ADD", "register:40f0:8", ["const:87edf8:8", "const:4:8"]]
+ 0087edf8 ["CALL", null, ["callee:00c57f60:8"]]
- 0087eda0 bytes 3c640f94
+ 0087edf8 bytes 5a640f94
- 0087eddc ["INT_ADD", "register:40f0:8", ["const:87eddc:8", "const:4:8"]]
- 0087eddc ["CALL", null, ["callee:0043bb60:8"]]
+ 0087ee34 ["INT_ADD", "register:40f0:8", ["const:87ee34:8", "const:4:8"]]
+ 0087ee34 ["CALL", null, ["callee:0043bb60:8"]]
- 0087eddc bytes 51f3ee97
+ 0087ee34 bytes 4bf3ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074668bbfaeb58ae3f0048ebe996d313"></a>

### [`0087ee78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md) → [`0087eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eed0.md) FUN_0087eed0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md#insn-0087eefc) · [`0087ef28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md#insn-0087ef28)
- 新版 `0087ef54`（命令位置の公開資料なし） · `0087ef80`（命令位置の公開資料なし）

~~~diff
- 0087eefc ["INT_ADD", "register:40f0:8", ["const:87eefc:8", "const:4:8"]]
- 0087eefc ["CALL", null, ["callee:00c58120:8"]]
+ 0087ef54 ["INT_ADD", "register:40f0:8", ["const:87ef54:8", "const:4:8"]]
+ 0087ef54 ["CALL", null, ["callee:00c58120:8"]]
- 0087eefc bytes 55640f94
+ 0087ef54 bytes 73640f94
- 0087ef28 ["INT_ADD", "register:40f0:8", ["const:87ef28:8", "const:4:8"]]
- 0087ef28 ["CALL", null, ["callee:00c58120:8"]]
+ 0087ef80 ["INT_ADD", "register:40f0:8", ["const:87ef80:8", "const:4:8"]]
+ 0087ef80 ["CALL", null, ["callee:00c58120:8"]]
- 0087ef28 bytes 4a640f94
+ 0087ef80 bytes 68640f94
~~~


<a id="compare-c2b1b938624dd4086b55bc2702d2aaa5"></a>

### [`0087ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ef7c.md) → [`0087efd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087efd4.md) FUN_0087efd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ef7c.md#insn-0087efac) · [`0087efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ef7c.md#insn-0087efc0) · [`0087efc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ef7c.md#insn-0087efc8)
- 新版 `0087f004`（命令位置の公開資料なし） · `0087f018`（命令位置の公開資料なし） · `0087f020`（命令位置の公開資料なし）

~~~diff
- 0087efac ["INT_ADD", "register:40f0:8", ["const:87efac:8", "const:4:8"]]
- 0087efac ["CALL", null, ["callee:00c53da0:8"]]
+ 0087f004 ["INT_ADD", "register:40f0:8", ["const:87f004:8", "const:4:8"]]
+ 0087f004 ["CALL", null, ["callee:00c53da0:8"]]
- 0087efac bytes 55530f94
+ 0087f004 bytes 67530f94
- 0087efc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087efc0 ["INT_ADD", "register:40f0:8", ["const:87efc0:8", "const:4:8"]]
- 0087efc0 ["CALLIND", null, ["register:0:8"]]
+ 0087f018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087f018 ["INT_ADD", "register:40f0:8", ["const:87f018:8", "const:4:8"]]
+ 0087f018 ["CALLIND", null, ["register:0:8"]]
- 0087efc0 bytes 00013fd6
+ 0087f018 bytes 00013fd6
- 0087efc8 ["INT_ADD", "register:40f0:8", ["const:87efc8:8", "const:4:8"]]
- 0087efc8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0087f020 ["INT_ADD", "register:40f0:8", ["const:87f020:8", "const:4:8"]]
+ 0087f020 ["CALL", null, ["callee:00c57f50:8"]]
- 0087efc8 bytes ae630f94
+ 0087f020 bytes cc630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd96a5c7e67c4deff9776e114b34bb10"></a>

### [`0087f038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md) → [`0087f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md) FUN_0087f090

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)
- 新版 呼出元 1件 [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087f054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md#insn-0087f054) · [`0087f06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md#insn-0087f06c) · [`0087f074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md#insn-0087f074)
- 新版 `0087f0ac`（命令位置の公開資料なし） · `0087f0c4`（命令位置の公開資料なし） · `0087f0cc`（命令位置の公開資料なし）

~~~diff
- 0087f054 ["INT_ADD", "register:40f0:8", ["const:87f054:8", "const:4:8"]]
- 0087f054 ["CALL", null, ["callee:00c57f80:8"]]
+ 0087f0ac ["INT_ADD", "register:40f0:8", ["const:87f0ac:8", "const:4:8"]]
+ 0087f0ac ["CALL", null, ["callee:00c57f80:8"]]
- 0087f054 bytes 97630f94
+ 0087f0ac bytes b5630f94
- 0087f06c ["INT_ADD", "register:40f0:8", ["const:87f06c:8", "const:4:8"]]
- 0087f06c ["CALL", null, ["callee:00c5a900:8"]]
+ 0087f0c4 ["INT_ADD", "register:40f0:8", ["const:87f0c4:8", "const:4:8"]]
+ 0087f0c4 ["CALL", null, ["callee:00c5a900:8"]]
- 0087f06c bytes f16d0f94
+ 0087f0c4 bytes 0f6e0f94
- 0087f074 ["INT_ADD", "register:40f0:8", ["const:87f074:8", "const:4:8"]]
- 0087f074 ["CALL", null, ["callee:00c57f80:8"]]
+ 0087f0cc ["INT_ADD", "register:40f0:8", ["const:87f0cc:8", "const:4:8"]]
+ 0087f0cc ["CALL", null, ["callee:00c57f80:8"]]
- 0087f074 bytes 8f630f94
+ 0087f0cc bytes ad630f94
~~~


<a id="compare-accdef8967ba5463160c131b78c4fcdd"></a>

### [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) → [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) FUN_0087f0fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00bc89d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md) · 呼出先 3件 [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)
- 新版 呼出元 2件 [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) [`00bc8a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md) · 呼出先 3件 [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087f0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md#insn-0087f0c0) · [`0087f0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md#insn-0087f0cc) · [`0087f0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md#insn-0087f0d8)
- 新版 `0087f118`（命令位置の公開資料なし） · `0087f124`（命令位置の公開資料なし） · `0087f130`（命令位置の公開資料なし）

~~~diff
- 0087f0c0 ["INT_ADD", "register:40f0:8", ["const:87f0c0:8", "const:4:8"]]
- 0087f0c0 ["CALL", null, ["local:b0:8"]]
+ 0087f118 ["INT_ADD", "register:40f0:8", ["const:87f118:8", "const:4:8"]]
+ 0087f118 ["CALL", null, ["local:b0:8"]]
- 0087f0c0 bytes f9ffff97
+ 0087f118 bytes f9ffff97
- 0087f0cc ["INT_ADD", "register:40f0:8", ["const:87f0cc:8", "const:4:8"]]
- 0087f0cc ["CALL", null, ["local:b0:8"]]
+ 0087f124 ["INT_ADD", "register:40f0:8", ["const:87f124:8", "const:4:8"]]
+ 0087f124 ["CALL", null, ["local:b0:8"]]
- 0087f0cc bytes f6ffff97
+ 0087f124 bytes f6ffff97
- 0087f0d8 ["INT_ADD", "register:40f0:8", ["const:87f0d8:8", "const:4:8"]]
- 0087f0d8 ["CALL", null, ["callee:00c5a900:8"]]
+ 0087f130 ["INT_ADD", "register:40f0:8", ["const:87f130:8", "const:4:8"]]
+ 0087f130 ["CALL", null, ["callee:00c5a900:8"]]
- 0087f0d8 bytes d66d0f94
+ 0087f130 bytes f46d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b2b57171c98aed4bbef2559393dc696"></a>

### [`00880bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880bec.md) → [`00880c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880c44.md) FUN_00880c44

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00880c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880bec.md#insn-00880c28) · [`00880c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880bec.md#insn-00880c3c) · [`00880c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880bec.md#insn-00880c5c)
- 新版 `00880c80`（命令位置の公開資料なし） · `00880c94`（命令位置の公開資料なし） · `00880cb4`（命令位置の公開資料なし）

~~~diff
- 00880c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880c28 ["INT_ADD", "register:40f0:8", ["const:880c28:8", "const:4:8"]]
- 00880c28 ["CALLIND", null, ["register:0:8"]]
+ 00880c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880c80 ["INT_ADD", "register:40f0:8", ["const:880c80:8", "const:4:8"]]
+ 00880c80 ["CALLIND", null, ["register:0:8"]]
- 00880c28 bytes 00013fd6
+ 00880c80 bytes 00013fd6
- 00880c3c ["INT_ADD", "register:40f0:8", ["const:880c3c:8", "const:4:8"]]
- 00880c3c ["CALL", null, ["callee:00c53da0:8"]]
+ 00880c94 ["INT_ADD", "register:40f0:8", ["const:880c94:8", "const:4:8"]]
+ 00880c94 ["CALL", null, ["callee:00c53da0:8"]]
- 00880c3c bytes 314c0f94
+ 00880c94 bytes 434c0f94
- 00880c5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00880c5c ["INT_ADD", "register:40f0:8", ["const:880c5c:8", "const:4:8"]]
- 00880c5c ["CALLIND", null, ["register:0:8"]]
+ 00880cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880cb4 ["INT_ADD", "register:40f0:8", ["const:880cb4:8", "const:4:8"]]
+ 00880cb4 ["CALLIND", null, ["register:0:8"]]
- 00880c5c bytes 00013fd6
+ 00880cb4 bytes 00013fd6
~~~


<a id="compare-38057674f11d6088e8533e6a34634ebf"></a>

### [`00880c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880c70.md) → [`00880cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880cc8.md) FUN_00880cc8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00880cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880c70.md#insn-00880cac) · [`00880cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880c70.md#insn-00880cc0) · [`00880ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880c70.md#insn-00880ce0)
- 新版 `00880d04`（命令位置の公開資料なし） · `00880d18`（命令位置の公開資料なし） · `00880d38`（命令位置の公開資料なし）

~~~diff
- 00880cac ["COPY", "register:0:8", ["register:4040:8"]]
- 00880cac ["INT_ADD", "register:40f0:8", ["const:880cac:8", "const:4:8"]]
- 00880cac ["CALLIND", null, ["register:0:8"]]
+ 00880d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880d04 ["INT_ADD", "register:40f0:8", ["const:880d04:8", "const:4:8"]]
+ 00880d04 ["CALLIND", null, ["register:0:8"]]
- 00880cac bytes 00013fd6
+ 00880d04 bytes 00013fd6
- 00880cc0 ["INT_ADD", "register:40f0:8", ["const:880cc0:8", "const:4:8"]]
- 00880cc0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00880d18 ["INT_ADD", "register:40f0:8", ["const:880d18:8", "const:4:8"]]
+ 00880d18 ["CALL", null, ["callee:00c53da0:8"]]
- 00880cc0 bytes 104c0f94
+ 00880d18 bytes 224c0f94
- 00880ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880ce0 ["INT_ADD", "register:40f0:8", ["const:880ce0:8", "const:4:8"]]
- 00880ce0 ["CALLIND", null, ["register:0:8"]]
+ 00880d38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880d38 ["INT_ADD", "register:40f0:8", ["const:880d38:8", "const:4:8"]]
+ 00880d38 ["CALLIND", null, ["register:0:8"]]
- 00880ce0 bytes 00013fd6
+ 00880d38 bytes 00013fd6
~~~


<a id="compare-3f47aa529ee04489da6d8269494709e5"></a>

### [`00881014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881014.md) → [`0088106c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/0088106c.md) FUN_0088106c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881014.md#insn-00881034) · [`00881048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881014.md#insn-00881048) · [`00881050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881014.md#insn-00881050)
- 新版 `0088108c`（命令位置の公開資料なし） · `008810a0`（命令位置の公開資料なし） · `008810a8`（命令位置の公開資料なし）

~~~diff
- 00881034 ["INT_ADD", "register:40f0:8", ["const:881034:8", "const:4:8"]]
- 00881034 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088108c ["INT_ADD", "register:40f0:8", ["const:88108c:8", "const:4:8"]]
+ 0088108c ["CALL", null, ["callee:00c53da0:8"]]
- 00881034 bytes 334b0f94
+ 0088108c bytes 454b0f94
- 00881048 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881048 ["INT_ADD", "register:40f0:8", ["const:881048:8", "const:4:8"]]
- 00881048 ["CALLIND", null, ["register:0:8"]]
+ 008810a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008810a0 ["INT_ADD", "register:40f0:8", ["const:8810a0:8", "const:4:8"]]
+ 008810a0 ["CALLIND", null, ["register:0:8"]]
- 00881048 bytes 00013fd6
+ 008810a0 bytes 00013fd6
- 00881050 ["INT_ADD", "register:40f0:8", ["const:881050:8", "const:4:8"]]
- 00881050 ["CALL", null, ["callee:00c57f50:8"]]
+ 008810a8 ["INT_ADD", "register:40f0:8", ["const:8810a8:8", "const:4:8"]]
+ 008810a8 ["CALL", null, ["callee:00c57f50:8"]]
- 00881050 bytes 8c5b0f94
+ 008810a8 bytes aa5b0f94
~~~


<a id="compare-5f69313fd21b2e2e9499e6e6cdfdee03"></a>

### [`0088134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/0088134c.md) → [`008813a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008813a4.md) FUN_008813a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/0088134c.md#insn-00881388)
- 新版 `008813e0`（命令位置の公開資料なし）

~~~diff
- 00881388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881388 ["INT_ADD", "register:40f0:8", ["const:881388:8", "const:4:8"]]
- 00881388 ["CALLIND", null, ["register:0:8"]]
+ 008813e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008813e0 ["INT_ADD", "register:40f0:8", ["const:8813e0:8", "const:4:8"]]
+ 008813e0 ["CALLIND", null, ["register:0:8"]]
- 00881388 bytes 00013fd6
+ 008813e0 bytes 00013fd6
~~~


<a id="compare-24773972065087142527d2e0a021ff3b"></a>

### [`00881c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c2c.md) → [`00881c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881c84.md) FUN_00881c84

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c2c.md#insn-00881c48) · [`00881c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c2c.md#insn-00881c68)
- 新版 `00881ca0`（命令位置の公開資料なし） · `00881cc0`（命令位置の公開資料なし）

~~~diff
- 00881c48 ["INT_ADD", "register:40f0:8", ["const:881c48:8", "const:4:8"]]
- 00881c48 ["CALL", null, ["callee:00c53da0:8"]]
+ 00881ca0 ["INT_ADD", "register:40f0:8", ["const:881ca0:8", "const:4:8"]]
+ 00881ca0 ["CALL", null, ["callee:00c53da0:8"]]
- 00881c48 bytes 2e480f94
+ 00881ca0 bytes 40480f94
- 00881c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881c68 ["INT_ADD", "register:40f0:8", ["const:881c68:8", "const:4:8"]]
- 00881c68 ["CALLIND", null, ["register:0:8"]]
+ 00881cc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00881cc0 ["INT_ADD", "register:40f0:8", ["const:881cc0:8", "const:4:8"]]
+ 00881cc0 ["CALLIND", null, ["register:0:8"]]
- 00881c68 bytes 00013fd6
+ 00881cc0 bytes 00013fd6
~~~


<a id="compare-cb53aff9489caa5a661c6567e7cc8435"></a>

### [`00882614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882614.md) → [`0088266c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088266c.md) FUN_0088266c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008801e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882614.md#insn-00882650)
- 新版 `008826a8`（命令位置の公開資料なし）

~~~diff
- 00882650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00882650 ["INT_ADD", "register:40f0:8", ["const:882650:8", "const:4:8"]]
- 00882650 ["CALLIND", null, ["register:0:8"]]
+ 008826a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008826a8 ["INT_ADD", "register:40f0:8", ["const:8826a8:8", "const:4:8"]]
+ 008826a8 ["CALLIND", null, ["register:0:8"]]
- 00882650 bytes 00013fd6
+ 008826a8 bytes 00013fd6
~~~


<a id="compare-3bf71bec0ee43b03b435f8b5bc66061b"></a>

### [`00882d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d40.md) → [`00882d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882d98.md) FUN_00882d98

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d40.md#insn-00882d60)
- 新版 `00882db8`（命令位置の公開資料なし）

~~~diff
- 00882d60 ["INT_ADD", "register:40f0:8", ["const:882d60:8", "const:4:8"]]
- 00882d60 ["CALL", null, ["callee:00c57f80:8"]]
+ 00882db8 ["INT_ADD", "register:40f0:8", ["const:882db8:8", "const:4:8"]]
+ 00882db8 ["CALL", null, ["callee:00c57f80:8"]]
- 00882d60 bytes 54540f94
+ 00882db8 bytes 72540f94
~~~


<a id="compare-0a071c83529c383cad3a5c2d2f05f075"></a>

### [`008839d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008839d0.md) → [`00883a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883a28.md) FUN_00883a28

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00883a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008839d0.md#insn-00883a0c) · [`00883a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008839d0.md#insn-00883a20) · [`00883a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008839d0.md#insn-00883a40)
- 新版 `00883a64`（命令位置の公開資料なし） · `00883a78`（命令位置の公開資料なし） · `00883a98`（命令位置の公開資料なし）

~~~diff
- 00883a0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a0c ["INT_ADD", "register:40f0:8", ["const:883a0c:8", "const:4:8"]]
- 00883a0c ["CALLIND", null, ["register:0:8"]]
+ 00883a64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a64 ["INT_ADD", "register:40f0:8", ["const:883a64:8", "const:4:8"]]
+ 00883a64 ["CALLIND", null, ["register:0:8"]]
- 00883a0c bytes 00013fd6
+ 00883a64 bytes 00013fd6
- 00883a20 ["INT_ADD", "register:40f0:8", ["const:883a20:8", "const:4:8"]]
- 00883a20 ["CALL", null, ["callee:00c53da0:8"]]
+ 00883a78 ["INT_ADD", "register:40f0:8", ["const:883a78:8", "const:4:8"]]
+ 00883a78 ["CALL", null, ["callee:00c53da0:8"]]
- 00883a20 bytes b8400f94
+ 00883a78 bytes ca400f94
- 00883a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a40 ["INT_ADD", "register:40f0:8", ["const:883a40:8", "const:4:8"]]
- 00883a40 ["CALLIND", null, ["register:0:8"]]
+ 00883a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a98 ["INT_ADD", "register:40f0:8", ["const:883a98:8", "const:4:8"]]
+ 00883a98 ["CALLIND", null, ["register:0:8"]]
- 00883a40 bytes 00013fd6
+ 00883a98 bytes 00013fd6
~~~


<a id="compare-5142bfbe2b1902f37863e6e1d2b84b75"></a>

### [`00883a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883a54.md) → [`00883aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883aac.md) FUN_00883aac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00883a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883a54.md#insn-00883a90) · [`00883aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883a54.md#insn-00883aa4) · [`00883ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883a54.md#insn-00883ab8)
- 新版 `00883ae8`（命令位置の公開資料なし） · `00883afc`（命令位置の公開資料なし） · `00883b10`（命令位置の公開資料なし）

~~~diff
- 00883a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a90 ["INT_ADD", "register:40f0:8", ["const:883a90:8", "const:4:8"]]
- 00883a90 ["CALLIND", null, ["register:0:8"]]
+ 00883ae8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883ae8 ["INT_ADD", "register:40f0:8", ["const:883ae8:8", "const:4:8"]]
+ 00883ae8 ["CALLIND", null, ["register:0:8"]]
- 00883a90 bytes 00013fd6
+ 00883ae8 bytes 00013fd6
- 00883aa4 ["INT_ADD", "register:40f0:8", ["const:883aa4:8", "const:4:8"]]
- 00883aa4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00883afc ["INT_ADD", "register:40f0:8", ["const:883afc:8", "const:4:8"]]
+ 00883afc ["CALL", null, ["callee:00c53da0:8"]]
- 00883aa4 bytes 97400f94
+ 00883afc bytes a9400f94
- 00883ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883ab8 ["INT_ADD", "register:40f0:8", ["const:883ab8:8", "const:4:8"]]
- 00883ab8 ["CALLIND", null, ["register:0:8"]]
+ 00883b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883b10 ["INT_ADD", "register:40f0:8", ["const:883b10:8", "const:4:8"]]
+ 00883b10 ["CALLIND", null, ["register:0:8"]]
- 00883ab8 bytes 00013fd6
+ 00883b10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de95c2e0c960141be80116a93f2c4158"></a>

### [`00883fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883fa4.md) → [`00883ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883ffc.md) FUN_00883ffc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00883fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883fa4.md#insn-00883fe0) · [`00883ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883fa4.md#insn-00883ff4) · [`00884014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883fa4.md#insn-00884014)
- 新版 `00884038`（命令位置の公開資料なし） · `0088404c`（命令位置の公開資料なし） · `0088406c`（命令位置の公開資料なし）

~~~diff
- 00883fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883fe0 ["INT_ADD", "register:40f0:8", ["const:883fe0:8", "const:4:8"]]
- 00883fe0 ["CALLIND", null, ["register:0:8"]]
+ 00884038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884038 ["INT_ADD", "register:40f0:8", ["const:884038:8", "const:4:8"]]
+ 00884038 ["CALLIND", null, ["register:0:8"]]
- 00883fe0 bytes 00013fd6
+ 00884038 bytes 00013fd6
- 00883ff4 ["INT_ADD", "register:40f0:8", ["const:883ff4:8", "const:4:8"]]
- 00883ff4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088404c ["INT_ADD", "register:40f0:8", ["const:88404c:8", "const:4:8"]]
+ 0088404c ["CALL", null, ["callee:00c53da0:8"]]
- 00883ff4 bytes 433f0f94
+ 0088404c bytes 553f0f94
- 00884014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884014 ["INT_ADD", "register:40f0:8", ["const:884014:8", "const:4:8"]]
- 00884014 ["CALLIND", null, ["register:0:8"]]
+ 0088406c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088406c ["INT_ADD", "register:40f0:8", ["const:88406c:8", "const:4:8"]]
+ 0088406c ["CALLIND", null, ["register:0:8"]]
- 00884014 bytes 00013fd6
+ 0088406c bytes 00013fd6
~~~


<a id="compare-4264e64c4a0462c261394809141766b4"></a>

### [`00884028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884028.md) → [`00884080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884080.md) FUN_00884080

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884028.md#insn-00884064) · [`00884078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884028.md#insn-00884078) · [`00884098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884028.md#insn-00884098)
- 新版 `008840bc`（命令位置の公開資料なし） · `008840d0`（命令位置の公開資料なし） · `008840f0`（命令位置の公開資料なし）

~~~diff
- 00884064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884064 ["INT_ADD", "register:40f0:8", ["const:884064:8", "const:4:8"]]
- 00884064 ["CALLIND", null, ["register:0:8"]]
+ 008840bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008840bc ["INT_ADD", "register:40f0:8", ["const:8840bc:8", "const:4:8"]]
+ 008840bc ["CALLIND", null, ["register:0:8"]]
- 00884064 bytes 00013fd6
+ 008840bc bytes 00013fd6
- 00884078 ["INT_ADD", "register:40f0:8", ["const:884078:8", "const:4:8"]]
- 00884078 ["CALL", null, ["callee:00c53da0:8"]]
+ 008840d0 ["INT_ADD", "register:40f0:8", ["const:8840d0:8", "const:4:8"]]
+ 008840d0 ["CALL", null, ["callee:00c53da0:8"]]
- 00884078 bytes 223f0f94
+ 008840d0 bytes 343f0f94
- 00884098 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884098 ["INT_ADD", "register:40f0:8", ["const:884098:8", "const:4:8"]]
- 00884098 ["CALLIND", null, ["register:0:8"]]
+ 008840f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008840f0 ["INT_ADD", "register:40f0:8", ["const:8840f0:8", "const:4:8"]]
+ 008840f0 ["CALLIND", null, ["register:0:8"]]
- 00884098 bytes 00013fd6
+ 008840f0 bytes 00013fd6
~~~


<a id="compare-b60d1813a6aeba4c62a50e66e4da773e"></a>

### [`00884318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884318.md) → [`00884370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884370.md) FUN_00884370

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884318.md#insn-00884354) · [`00884368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884318.md#insn-00884368) · [`00884388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884318.md#insn-00884388)
- 新版 `008843ac`（命令位置の公開資料なし） · `008843c0`（命令位置の公開資料なし） · `008843e0`（命令位置の公開資料なし）

~~~diff
- 00884354 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884354 ["INT_ADD", "register:40f0:8", ["const:884354:8", "const:4:8"]]
- 00884354 ["CALLIND", null, ["register:0:8"]]
+ 008843ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008843ac ["INT_ADD", "register:40f0:8", ["const:8843ac:8", "const:4:8"]]
+ 008843ac ["CALLIND", null, ["register:0:8"]]
- 00884354 bytes 00013fd6
+ 008843ac bytes 00013fd6
- 00884368 ["INT_ADD", "register:40f0:8", ["const:884368:8", "const:4:8"]]
- 00884368 ["CALL", null, ["callee:00c53da0:8"]]
+ 008843c0 ["INT_ADD", "register:40f0:8", ["const:8843c0:8", "const:4:8"]]
+ 008843c0 ["CALL", null, ["callee:00c53da0:8"]]
- 00884368 bytes 663e0f94
+ 008843c0 bytes 783e0f94
- 00884388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884388 ["INT_ADD", "register:40f0:8", ["const:884388:8", "const:4:8"]]
- 00884388 ["CALLIND", null, ["register:0:8"]]
+ 008843e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008843e0 ["INT_ADD", "register:40f0:8", ["const:8843e0:8", "const:4:8"]]
+ 008843e0 ["CALLIND", null, ["register:0:8"]]
- 00884388 bytes 00013fd6
+ 008843e0 bytes 00013fd6
~~~


<a id="compare-01fc0135beb48c5ef24ba4b64a17d8c8"></a>

### [`0088439c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088439c.md) → [`008843f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008843f4.md) FUN_008843f4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008843d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088439c.md#insn-008843d8) · [`008843ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088439c.md#insn-008843ec) · [`00884400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088439c.md#insn-00884400)
- 新版 `00884430`（命令位置の公開資料なし） · `00884444`（命令位置の公開資料なし） · `00884458`（命令位置の公開資料なし）

~~~diff
- 008843d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008843d8 ["INT_ADD", "register:40f0:8", ["const:8843d8:8", "const:4:8"]]
- 008843d8 ["CALLIND", null, ["register:0:8"]]
+ 00884430 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884430 ["INT_ADD", "register:40f0:8", ["const:884430:8", "const:4:8"]]
+ 00884430 ["CALLIND", null, ["register:0:8"]]
- 008843d8 bytes 00013fd6
+ 00884430 bytes 00013fd6
- 008843ec ["INT_ADD", "register:40f0:8", ["const:8843ec:8", "const:4:8"]]
- 008843ec ["CALL", null, ["callee:00c53da0:8"]]
+ 00884444 ["INT_ADD", "register:40f0:8", ["const:884444:8", "const:4:8"]]
+ 00884444 ["CALL", null, ["callee:00c53da0:8"]]
- 008843ec bytes 453e0f94
+ 00884444 bytes 573e0f94
- 00884400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884400 ["INT_ADD", "register:40f0:8", ["const:884400:8", "const:4:8"]]
- 00884400 ["CALLIND", null, ["register:0:8"]]
+ 00884458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884458 ["INT_ADD", "register:40f0:8", ["const:884458:8", "const:4:8"]]
+ 00884458 ["CALLIND", null, ["register:0:8"]]
- 00884400 bytes 00013fd6
+ 00884458 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a37c316bd2a5822bc02eaea7f42fcbee"></a>

### [`008846c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008846c4.md) → [`0088471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088471c.md) FUN_0088471c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008846c4.md#insn-00884700) · [`00884714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008846c4.md#insn-00884714) · [`00884734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008846c4.md#insn-00884734)
- 新版 `00884758`（命令位置の公開資料なし） · `0088476c`（命令位置の公開資料なし） · `0088478c`（命令位置の公開資料なし）

~~~diff
- 00884700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884700 ["INT_ADD", "register:40f0:8", ["const:884700:8", "const:4:8"]]
- 00884700 ["CALLIND", null, ["register:0:8"]]
+ 00884758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884758 ["INT_ADD", "register:40f0:8", ["const:884758:8", "const:4:8"]]
+ 00884758 ["CALLIND", null, ["register:0:8"]]
- 00884700 bytes 00013fd6
+ 00884758 bytes 00013fd6
- 00884714 ["INT_ADD", "register:40f0:8", ["const:884714:8", "const:4:8"]]
- 00884714 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088476c ["INT_ADD", "register:40f0:8", ["const:88476c:8", "const:4:8"]]
+ 0088476c ["CALL", null, ["callee:00c53da0:8"]]
- 00884714 bytes 7b3d0f94
+ 0088476c bytes 8d3d0f94
- 00884734 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884734 ["INT_ADD", "register:40f0:8", ["const:884734:8", "const:4:8"]]
- 00884734 ["CALLIND", null, ["register:0:8"]]
+ 0088478c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088478c ["INT_ADD", "register:40f0:8", ["const:88478c:8", "const:4:8"]]
+ 0088478c ["CALLIND", null, ["register:0:8"]]
- 00884734 bytes 00013fd6
+ 0088478c bytes 00013fd6
~~~


<a id="compare-1f3b08bc112fe1f726ac9477581dfc39"></a>

### [`00884748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884748.md) → [`008847a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008847a0.md) FUN_008847a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884748.md#insn-00884784) · [`00884798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884748.md#insn-00884798) · [`008847ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884748.md#insn-008847ac)
- 新版 `008847dc`（命令位置の公開資料なし） · `008847f0`（命令位置の公開資料なし） · `00884804`（命令位置の公開資料なし）

~~~diff
- 00884784 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884784 ["INT_ADD", "register:40f0:8", ["const:884784:8", "const:4:8"]]
- 00884784 ["CALLIND", null, ["register:0:8"]]
+ 008847dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008847dc ["INT_ADD", "register:40f0:8", ["const:8847dc:8", "const:4:8"]]
+ 008847dc ["CALLIND", null, ["register:0:8"]]
- 00884784 bytes 00013fd6
+ 008847dc bytes 00013fd6
- 00884798 ["INT_ADD", "register:40f0:8", ["const:884798:8", "const:4:8"]]
- 00884798 ["CALL", null, ["callee:00c53da0:8"]]
+ 008847f0 ["INT_ADD", "register:40f0:8", ["const:8847f0:8", "const:4:8"]]
+ 008847f0 ["CALL", null, ["callee:00c53da0:8"]]
- 00884798 bytes 5a3d0f94
+ 008847f0 bytes 6c3d0f94
- 008847ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008847ac ["INT_ADD", "register:40f0:8", ["const:8847ac:8", "const:4:8"]]
- 008847ac ["CALLIND", null, ["register:0:8"]]
+ 00884804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884804 ["INT_ADD", "register:40f0:8", ["const:884804:8", "const:4:8"]]
+ 00884804 ["CALLIND", null, ["register:0:8"]]
- 008847ac bytes 00013fd6
+ 00884804 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cddff3af3e9fb5d41bd17213c09160c"></a>

### [`00884a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884a70.md) → [`00884ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884ac8.md) FUN_00884ac8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884a70.md#insn-00884aac) · [`00884ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884a70.md#insn-00884ac0) · [`00884ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884a70.md#insn-00884ae0)
- 新版 `00884b04`（命令位置の公開資料なし） · `00884b18`（命令位置の公開資料なし） · `00884b38`（命令位置の公開資料なし）

~~~diff
- 00884aac ["COPY", "register:0:8", ["register:4040:8"]]
- 00884aac ["INT_ADD", "register:40f0:8", ["const:884aac:8", "const:4:8"]]
- 00884aac ["CALLIND", null, ["register:0:8"]]
+ 00884b04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884b04 ["INT_ADD", "register:40f0:8", ["const:884b04:8", "const:4:8"]]
+ 00884b04 ["CALLIND", null, ["register:0:8"]]
- 00884aac bytes 00013fd6
+ 00884b04 bytes 00013fd6
- 00884ac0 ["INT_ADD", "register:40f0:8", ["const:884ac0:8", "const:4:8"]]
- 00884ac0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00884b18 ["INT_ADD", "register:40f0:8", ["const:884b18:8", "const:4:8"]]
+ 00884b18 ["CALL", null, ["callee:00c53da0:8"]]
- 00884ac0 bytes 903c0f94
+ 00884b18 bytes a23c0f94
- 00884ae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884ae0 ["INT_ADD", "register:40f0:8", ["const:884ae0:8", "const:4:8"]]
- 00884ae0 ["CALLIND", null, ["register:0:8"]]
+ 00884b38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884b38 ["INT_ADD", "register:40f0:8", ["const:884b38:8", "const:4:8"]]
+ 00884b38 ["CALLIND", null, ["register:0:8"]]
- 00884ae0 bytes 00013fd6
+ 00884b38 bytes 00013fd6
~~~


<a id="compare-a2ebfce64a3339c3cb0bcae9344ad8d1"></a>

### [`00884af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884af4.md) → [`00884b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884b4c.md) FUN_00884b4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884af4.md#insn-00884b30) · [`00884b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884af4.md#insn-00884b44) · [`00884b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884af4.md#insn-00884b58)
- 新版 `00884b88`（命令位置の公開資料なし） · `00884b9c`（命令位置の公開資料なし） · `00884bb0`（命令位置の公開資料なし）

~~~diff
- 00884b30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884b30 ["INT_ADD", "register:40f0:8", ["const:884b30:8", "const:4:8"]]
- 00884b30 ["CALLIND", null, ["register:0:8"]]
+ 00884b88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884b88 ["INT_ADD", "register:40f0:8", ["const:884b88:8", "const:4:8"]]
+ 00884b88 ["CALLIND", null, ["register:0:8"]]
- 00884b30 bytes 00013fd6
+ 00884b88 bytes 00013fd6
- 00884b44 ["INT_ADD", "register:40f0:8", ["const:884b44:8", "const:4:8"]]
- 00884b44 ["CALL", null, ["callee:00c53da0:8"]]
+ 00884b9c ["INT_ADD", "register:40f0:8", ["const:884b9c:8", "const:4:8"]]
+ 00884b9c ["CALL", null, ["callee:00c53da0:8"]]
- 00884b44 bytes 6f3c0f94
+ 00884b9c bytes 813c0f94
- 00884b58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884b58 ["INT_ADD", "register:40f0:8", ["const:884b58:8", "const:4:8"]]
- 00884b58 ["CALLIND", null, ["register:0:8"]]
+ 00884bb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884bb0 ["INT_ADD", "register:40f0:8", ["const:884bb0:8", "const:4:8"]]
+ 00884bb0 ["CALLIND", null, ["register:0:8"]]
- 00884b58 bytes 00013fd6
+ 00884bb0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f85773206cae49da6302e41122e423"></a>

### [`00884f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884f74.md) → [`00884fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884fcc.md) FUN_00884fcc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884f74.md#insn-00884fb0) · [`00884fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884f74.md#insn-00884fc4) · [`00884fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884f74.md#insn-00884fe4)
- 新版 `00885008`（命令位置の公開資料なし） · `0088501c`（命令位置の公開資料なし） · `0088503c`（命令位置の公開資料なし）

~~~diff
- 00884fb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884fb0 ["INT_ADD", "register:40f0:8", ["const:884fb0:8", "const:4:8"]]
- 00884fb0 ["CALLIND", null, ["register:0:8"]]
+ 00885008 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885008 ["INT_ADD", "register:40f0:8", ["const:885008:8", "const:4:8"]]
+ 00885008 ["CALLIND", null, ["register:0:8"]]
- 00884fb0 bytes 00013fd6
+ 00885008 bytes 00013fd6
- 00884fc4 ["INT_ADD", "register:40f0:8", ["const:884fc4:8", "const:4:8"]]
- 00884fc4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088501c ["INT_ADD", "register:40f0:8", ["const:88501c:8", "const:4:8"]]
+ 0088501c ["CALL", null, ["callee:00c53da0:8"]]
- 00884fc4 bytes 4f3b0f94
+ 0088501c bytes 613b0f94
- 00884fe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884fe4 ["INT_ADD", "register:40f0:8", ["const:884fe4:8", "const:4:8"]]
- 00884fe4 ["CALLIND", null, ["register:0:8"]]
+ 0088503c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088503c ["INT_ADD", "register:40f0:8", ["const:88503c:8", "const:4:8"]]
+ 0088503c ["CALLIND", null, ["register:0:8"]]
- 00884fe4 bytes 00013fd6
+ 0088503c bytes 00013fd6
~~~


<a id="compare-8fc1736bc59e16146146fab96720759d"></a>

### [`00885264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885264.md) → [`008852bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008852bc.md) FUN_008852bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008852a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885264.md#insn-008852a0) · [`008852b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885264.md#insn-008852b4) · [`008852d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885264.md#insn-008852d4)
- 新版 `008852f8`（命令位置の公開資料なし） · `0088530c`（命令位置の公開資料なし） · `0088532c`（命令位置の公開資料なし）

~~~diff
- 008852a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008852a0 ["INT_ADD", "register:40f0:8", ["const:8852a0:8", "const:4:8"]]
- 008852a0 ["CALLIND", null, ["register:0:8"]]
+ 008852f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008852f8 ["INT_ADD", "register:40f0:8", ["const:8852f8:8", "const:4:8"]]
+ 008852f8 ["CALLIND", null, ["register:0:8"]]
- 008852a0 bytes 00013fd6
+ 008852f8 bytes 00013fd6
- 008852b4 ["INT_ADD", "register:40f0:8", ["const:8852b4:8", "const:4:8"]]
- 008852b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088530c ["INT_ADD", "register:40f0:8", ["const:88530c:8", "const:4:8"]]
+ 0088530c ["CALL", null, ["callee:00c53da0:8"]]
- 008852b4 bytes 933a0f94
+ 0088530c bytes a53a0f94
- 008852d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008852d4 ["INT_ADD", "register:40f0:8", ["const:8852d4:8", "const:4:8"]]
- 008852d4 ["CALLIND", null, ["register:0:8"]]
+ 0088532c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088532c ["INT_ADD", "register:40f0:8", ["const:88532c:8", "const:4:8"]]
+ 0088532c ["CALLIND", null, ["register:0:8"]]
- 008852d4 bytes 00013fd6
+ 0088532c bytes 00013fd6
~~~


<a id="compare-b0fd491ed7578e260862ee97c97bd317"></a>

### [`008852e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008852e8.md) → [`00885340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885340.md) FUN_00885340

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00884b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00884bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884bcc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008852e8.md#insn-00885324) · [`00885338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008852e8.md#insn-00885338) · [`0088534c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008852e8.md#insn-0088534c)
- 新版 `0088537c`（命令位置の公開資料なし） · `00885390`（命令位置の公開資料なし） · `008853a4`（命令位置の公開資料なし）

~~~diff
- 00885324 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885324 ["INT_ADD", "register:40f0:8", ["const:885324:8", "const:4:8"]]
- 00885324 ["CALLIND", null, ["register:0:8"]]
+ 0088537c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088537c ["INT_ADD", "register:40f0:8", ["const:88537c:8", "const:4:8"]]
+ 0088537c ["CALLIND", null, ["register:0:8"]]
- 00885324 bytes 00013fd6
+ 0088537c bytes 00013fd6
- 00885338 ["INT_ADD", "register:40f0:8", ["const:885338:8", "const:4:8"]]
- 00885338 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885390 ["INT_ADD", "register:40f0:8", ["const:885390:8", "const:4:8"]]
+ 00885390 ["CALL", null, ["callee:00c53da0:8"]]
- 00885338 bytes 723a0f94
+ 00885390 bytes 843a0f94
- 0088534c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088534c ["INT_ADD", "register:40f0:8", ["const:88534c:8", "const:4:8"]]
- 0088534c ["CALLIND", null, ["register:0:8"]]
+ 008853a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008853a4 ["INT_ADD", "register:40f0:8", ["const:8853a4:8", "const:4:8"]]
+ 008853a4 ["CALLIND", null, ["register:0:8"]]
- 0088534c bytes 00013fd6
+ 008853a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfb78050443aff9a7af25bc30729cffb"></a>

### [`0088560c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088560c.md) → [`00885664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885664.md) FUN_00885664

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088560c.md#insn-00885634) · [`00885648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088560c.md#insn-00885648) · [`00885650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088560c.md#insn-00885650)
- 新版 `0088568c`（命令位置の公開資料なし） · `008856a0`（命令位置の公開資料なし） · `008856a8`（命令位置の公開資料なし）

~~~diff
- 00885634 ["INT_ADD", "register:40f0:8", ["const:885634:8", "const:4:8"]]
- 00885634 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088568c ["INT_ADD", "register:40f0:8", ["const:88568c:8", "const:4:8"]]
+ 0088568c ["CALL", null, ["callee:00c53da0:8"]]
- 00885634 bytes b3390f94
+ 0088568c bytes c5390f94
- 00885648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885648 ["INT_ADD", "register:40f0:8", ["const:885648:8", "const:4:8"]]
- 00885648 ["CALLIND", null, ["register:0:8"]]
+ 008856a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008856a0 ["INT_ADD", "register:40f0:8", ["const:8856a0:8", "const:4:8"]]
+ 008856a0 ["CALLIND", null, ["register:0:8"]]
- 00885648 bytes 00013fd6
+ 008856a0 bytes 00013fd6
- 00885650 ["INT_ADD", "register:40f0:8", ["const:885650:8", "const:4:8"]]
- 00885650 ["CALL", null, ["callee:00c57f50:8"]]
+ 008856a8 ["INT_ADD", "register:40f0:8", ["const:8856a8:8", "const:4:8"]]
+ 008856a8 ["CALL", null, ["callee:00c57f50:8"]]
- 00885650 bytes 0c4a0f94
+ 008856a8 bytes 2a4a0f94
~~~


<a id="compare-8a09451a8eecae4dee36c0780ef9b6e3"></a>

### [`0088569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088569c.md) → [`008856f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008856f4.md) FUN_008856f4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008856c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088569c.md#insn-008856c4) · [`008856d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088569c.md#insn-008856d8) · [`008856e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088569c.md#insn-008856e0)
- 新版 `0088571c`（命令位置の公開資料なし） · `00885730`（命令位置の公開資料なし） · `00885738`（命令位置の公開資料なし）

~~~diff
- 008856c4 ["INT_ADD", "register:40f0:8", ["const:8856c4:8", "const:4:8"]]
- 008856c4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088571c ["INT_ADD", "register:40f0:8", ["const:88571c:8", "const:4:8"]]
+ 0088571c ["CALL", null, ["callee:00c53da0:8"]]
- 008856c4 bytes 8f390f94
+ 0088571c bytes a1390f94
- 008856d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008856d8 ["INT_ADD", "register:40f0:8", ["const:8856d8:8", "const:4:8"]]
- 008856d8 ["CALLIND", null, ["register:0:8"]]
+ 00885730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885730 ["INT_ADD", "register:40f0:8", ["const:885730:8", "const:4:8"]]
+ 00885730 ["CALLIND", null, ["register:0:8"]]
- 008856d8 bytes 00013fd6
+ 00885730 bytes 00013fd6
- 008856e0 ["INT_ADD", "register:40f0:8", ["const:8856e0:8", "const:4:8"]]
- 008856e0 ["CALL", null, ["callee:00c57f50:8"]]
+ 00885738 ["INT_ADD", "register:40f0:8", ["const:885738:8", "const:4:8"]]
+ 00885738 ["CALL", null, ["callee:00c57f50:8"]]
- 008856e0 bytes e8490f94
+ 00885738 bytes 064a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d8a23d1840860e3b3814966b9ec5670"></a>

### [`00885a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885a90.md) → [`00885ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ae8.md) FUN_00885ae8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885a90.md#insn-00885acc) · [`00885ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885a90.md#insn-00885ae0) · [`00885b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885a90.md#insn-00885b00)
- 新版 `00885b24`（命令位置の公開資料なし） · `00885b38`（命令位置の公開資料なし） · `00885b58`（命令位置の公開資料なし）

~~~diff
- 00885acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00885acc ["INT_ADD", "register:40f0:8", ["const:885acc:8", "const:4:8"]]
- 00885acc ["CALLIND", null, ["register:0:8"]]
+ 00885b24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b24 ["INT_ADD", "register:40f0:8", ["const:885b24:8", "const:4:8"]]
+ 00885b24 ["CALLIND", null, ["register:0:8"]]
- 00885acc bytes 00013fd6
+ 00885b24 bytes 00013fd6
- 00885ae0 ["INT_ADD", "register:40f0:8", ["const:885ae0:8", "const:4:8"]]
- 00885ae0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885b38 ["INT_ADD", "register:40f0:8", ["const:885b38:8", "const:4:8"]]
+ 00885b38 ["CALL", null, ["callee:00c53da0:8"]]
- 00885ae0 bytes 88380f94
+ 00885b38 bytes 9a380f94
- 00885b00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885b00 ["INT_ADD", "register:40f0:8", ["const:885b00:8", "const:4:8"]]
- 00885b00 ["CALLIND", null, ["register:0:8"]]
+ 00885b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b58 ["INT_ADD", "register:40f0:8", ["const:885b58:8", "const:4:8"]]
+ 00885b58 ["CALLIND", null, ["register:0:8"]]
- 00885b00 bytes 00013fd6
+ 00885b58 bytes 00013fd6
~~~


<a id="compare-a2a5f8686a05ba9ad2086847fa8a3c8f"></a>

### [`00885d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885d80.md) → [`00885dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885dd8.md) FUN_00885dd8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885d80.md#insn-00885dbc) · [`00885dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885d80.md#insn-00885dd0) · [`00885df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885d80.md#insn-00885df0)
- 新版 `00885e14`（命令位置の公開資料なし） · `00885e28`（命令位置の公開資料なし） · `00885e48`（命令位置の公開資料なし）

~~~diff
- 00885dbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00885dbc ["INT_ADD", "register:40f0:8", ["const:885dbc:8", "const:4:8"]]
- 00885dbc ["CALLIND", null, ["register:0:8"]]
+ 00885e14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885e14 ["INT_ADD", "register:40f0:8", ["const:885e14:8", "const:4:8"]]
+ 00885e14 ["CALLIND", null, ["register:0:8"]]
- 00885dbc bytes 00013fd6
+ 00885e14 bytes 00013fd6
- 00885dd0 ["INT_ADD", "register:40f0:8", ["const:885dd0:8", "const:4:8"]]
- 00885dd0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885e28 ["INT_ADD", "register:40f0:8", ["const:885e28:8", "const:4:8"]]
+ 00885e28 ["CALL", null, ["callee:00c53da0:8"]]
- 00885dd0 bytes cc370f94
+ 00885e28 bytes de370f94
- 00885df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885df0 ["INT_ADD", "register:40f0:8", ["const:885df0:8", "const:4:8"]]
- 00885df0 ["CALLIND", null, ["register:0:8"]]
+ 00885e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885e48 ["INT_ADD", "register:40f0:8", ["const:885e48:8", "const:4:8"]]
+ 00885e48 ["CALLIND", null, ["register:0:8"]]
- 00885df0 bytes 00013fd6
+ 00885e48 bytes 00013fd6
~~~


<a id="compare-c02a0da4e9e8ac8ea5e0e77b576ef27d"></a>

### [`00885e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885e04.md) → [`00885e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885e5c.md) FUN_00885e5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0088577c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885e04.md#insn-00885e40) · [`00885e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885e04.md#insn-00885e54) · [`00885e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885e04.md#insn-00885e68)
- 新版 `00885e98`（命令位置の公開資料なし） · `00885eac`（命令位置の公開資料なし） · `00885ec0`（命令位置の公開資料なし）

~~~diff
- 00885e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e40 ["INT_ADD", "register:40f0:8", ["const:885e40:8", "const:4:8"]]
- 00885e40 ["CALLIND", null, ["register:0:8"]]
+ 00885e98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885e98 ["INT_ADD", "register:40f0:8", ["const:885e98:8", "const:4:8"]]
+ 00885e98 ["CALLIND", null, ["register:0:8"]]
- 00885e40 bytes 00013fd6
+ 00885e98 bytes 00013fd6
- 00885e54 ["INT_ADD", "register:40f0:8", ["const:885e54:8", "const:4:8"]]
- 00885e54 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885eac ["INT_ADD", "register:40f0:8", ["const:885eac:8", "const:4:8"]]
+ 00885eac ["CALL", null, ["callee:00c53da0:8"]]
- 00885e54 bytes ab370f94
+ 00885eac bytes bd370f94
- 00885e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e68 ["INT_ADD", "register:40f0:8", ["const:885e68:8", "const:4:8"]]
- 00885e68 ["CALLIND", null, ["register:0:8"]]
+ 00885ec0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885ec0 ["INT_ADD", "register:40f0:8", ["const:885ec0:8", "const:4:8"]]
+ 00885ec0 ["CALLIND", null, ["register:0:8"]]
- 00885e68 bytes 00013fd6
+ 00885ec0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d24de551408011fabc54583e5298611"></a>

### [`0088613c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/0088613c.md) → [`00886194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886194.md) FUN_00886194

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/0088613c.md#insn-00886178)
- 新版 `008861d0`（命令位置の公開資料なし）

~~~diff
- 00886178 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886178 ["INT_ADD", "register:40f0:8", ["const:886178:8", "const:4:8"]]
- 00886178 ["CALLIND", null, ["register:0:8"]]
+ 008861d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008861d0 ["INT_ADD", "register:40f0:8", ["const:8861d0:8", "const:4:8"]]
+ 008861d0 ["CALLIND", null, ["register:0:8"]]
- 00886178 bytes 00013fd6
+ 008861d0 bytes 00013fd6
~~~


<a id="compare-b0f179731f4ff204eb5d0d1776541e5b"></a>

### [`008861a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md) → [`008861f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md) FUN_008861f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008861dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md#insn-008861dc) · [`008861ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md#insn-008861ec)
- 新版 `00886234`（命令位置の公開資料なし） · `00886244`（命令位置の公開資料なし）

~~~diff
- 008861dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008861dc ["INT_ADD", "register:40f0:8", ["const:8861dc:8", "const:4:8"]]
- 008861dc ["CALLIND", null, ["register:0:8"]]
+ 00886234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886234 ["INT_ADD", "register:40f0:8", ["const:886234:8", "const:4:8"]]
+ 00886234 ["CALLIND", null, ["register:0:8"]]
- 008861dc bytes 00013fd6
+ 00886234 bytes 00013fd6
- 008861ec ["INT_ADD", "register:40f0:8", ["const:8861ec:8", "const:4:8"]]
- 008861ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00886244 ["INT_ADD", "register:40f0:8", ["const:886244:8", "const:4:8"]]
+ 00886244 ["CALL", null, ["callee:00c57f80:8"]]
- 008861ec bytes 31470f94
+ 00886244 bytes 4f470f94
~~~


<a id="compare-0e522f3ead59d0342566ae6fdb682e31"></a>

### [`008866a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866a8.md) → [`00886700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886700.md) FUN_00886700

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00886258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008866e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866a8.md#insn-008866e4)
- 新版 `0088673c`（命令位置の公開資料なし）

~~~diff
- 008866e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008866e4 ["INT_ADD", "register:40f0:8", ["const:8866e4:8", "const:4:8"]]
- 008866e4 ["CALLIND", null, ["register:0:8"]]
+ 0088673c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088673c ["INT_ADD", "register:40f0:8", ["const:88673c:8", "const:4:8"]]
+ 0088673c ["CALLIND", null, ["register:0:8"]]
- 008866e4 bytes 00013fd6
+ 0088673c bytes 00013fd6
~~~


<a id="compare-3885e0e342874c492ac0a121d19c0d7e"></a>

### [`008866f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866f8.md) → [`00886750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886750.md) FUN_00886750

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866f8.md#insn-00886798) · [`008867c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866f8.md#insn-008867c0) · [`008867d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866f8.md#insn-008867d8)
- 新版 `008867f0`（命令位置の公開資料なし） · `00886818`（命令位置の公開資料なし） · `00886830`（命令位置の公開資料なし）

~~~diff
- 00886798 ["INT_ADD", "register:40f0:8", ["const:886798:8", "const:4:8"]]
- 00886798 ["CALL", null, ["callee:0043bb60:8"]]
+ 008867f0 ["INT_ADD", "register:40f0:8", ["const:8867f0:8", "const:4:8"]]
+ 008867f0 ["CALL", null, ["callee:0043bb60:8"]]
- 00886798 bytes e2d4ee97
+ 008867f0 bytes dcd4ee97
- 008867c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008867c0 ["INT_ADD", "register:40f0:8", ["const:8867c0:8", "const:4:8"]]
- 008867c0 ["CALLIND", null, ["register:0:8"]]
+ 00886818 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886818 ["INT_ADD", "register:40f0:8", ["const:886818:8", "const:4:8"]]
+ 00886818 ["CALLIND", null, ["register:0:8"]]
- 008867c0 bytes 00013fd6
+ 00886818 bytes 00013fd6
- 008867d8 ["INT_ADD", "register:40f0:8", ["const:8867d8:8", "const:4:8"]]
- 008867d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00886830 ["INT_ADD", "register:40f0:8", ["const:886830:8", "const:4:8"]]
+ 00886830 ["CALL", null, ["callee:00c57f80:8"]]
- 008867d8 bytes b6450f94
+ 00886830 bytes d4450f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a50a008fd7255d61e272ea3a5fe43e0"></a>

### [`00886a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a04.md) → [`00886a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a5c.md) FUN_00886a5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a04.md#insn-00886a20) · [`00886a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a04.md#insn-00886a40)
- 新版 `00886a78`（命令位置の公開資料なし） · `00886a98`（命令位置の公開資料なし）

~~~diff
- 00886a20 ["INT_ADD", "register:40f0:8", ["const:886a20:8", "const:4:8"]]
- 00886a20 ["CALL", null, ["callee:00c53da0:8"]]
+ 00886a78 ["INT_ADD", "register:40f0:8", ["const:886a78:8", "const:4:8"]]
+ 00886a78 ["CALL", null, ["callee:00c53da0:8"]]
- 00886a20 bytes b8340f94
+ 00886a78 bytes ca340f94
- 00886a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886a40 ["INT_ADD", "register:40f0:8", ["const:886a40:8", "const:4:8"]]
- 00886a40 ["CALLIND", null, ["register:0:8"]]
+ 00886a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886a98 ["INT_ADD", "register:40f0:8", ["const:886a98:8", "const:4:8"]]
+ 00886a98 ["CALLIND", null, ["register:0:8"]]
- 00886a40 bytes 00013fd6
+ 00886a98 bytes 00013fd6
~~~


<a id="compare-55856188cbd19dca273674e92247782c"></a>

### [`00886a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a54.md) → [`00886aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886aac.md) FUN_00886aac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a54.md#insn-00886a74) · [`00886a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a54.md#insn-00886a88) · [`00886a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a54.md#insn-00886a90)
- 新版 `00886acc`（命令位置の公開資料なし） · `00886ae0`（命令位置の公開資料なし） · `00886ae8`（命令位置の公開資料なし）

~~~diff
- 00886a74 ["INT_ADD", "register:40f0:8", ["const:886a74:8", "const:4:8"]]
- 00886a74 ["CALL", null, ["callee:00c53da0:8"]]
+ 00886acc ["INT_ADD", "register:40f0:8", ["const:886acc:8", "const:4:8"]]
+ 00886acc ["CALL", null, ["callee:00c53da0:8"]]
- 00886a74 bytes a3340f94
+ 00886acc bytes b5340f94
- 00886a88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886a88 ["INT_ADD", "register:40f0:8", ["const:886a88:8", "const:4:8"]]
- 00886a88 ["CALLIND", null, ["register:0:8"]]
+ 00886ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886ae0 ["INT_ADD", "register:40f0:8", ["const:886ae0:8", "const:4:8"]]
+ 00886ae0 ["CALLIND", null, ["register:0:8"]]
- 00886a88 bytes 00013fd6
+ 00886ae0 bytes 00013fd6
- 00886a90 ["INT_ADD", "register:40f0:8", ["const:886a90:8", "const:4:8"]]
- 00886a90 ["CALL", null, ["callee:00c57f50:8"]]
+ 00886ae8 ["INT_ADD", "register:40f0:8", ["const:886ae8:8", "const:4:8"]]
+ 00886ae8 ["CALL", null, ["callee:00c57f50:8"]]
- 00886a90 bytes fc440f94
+ 00886ae8 bytes 1a450f94
~~~


<a id="compare-b9f08ab9af544525c1727b8dc118b833"></a>

### [`00886f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f10.md) → [`00886f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md) FUN_00886f68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00886afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f10.md#insn-00886f30)
- 新版 `00886f88`（命令位置の公開資料なし）

~~~diff
- 00886f30 ["INT_ADD", "register:40f0:8", ["const:886f30:8", "const:4:8"]]
- 00886f30 ["CALL", null, ["callee:00c57f80:8"]]
+ 00886f88 ["INT_ADD", "register:40f0:8", ["const:886f88:8", "const:4:8"]]
+ 00886f88 ["CALL", null, ["callee:00c57f80:8"]]
- 00886f30 bytes e0430f94
+ 00886f88 bytes fe430f94
~~~


<a id="compare-c0fbc15b1005008a21a4b16cb02cb813"></a>

### [`00887724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md) → [`0088777c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/0088777c.md) FUN_0088777c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848750.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 4件 [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008487a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008487a8.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 4件 [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088774c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md#insn-0088774c) · [`00887760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md#insn-00887760) · [`0088777c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md#insn-0088777c)
- 新版 `008877a4`（命令位置の公開資料なし） · `008877b8`（命令位置の公開資料なし） · `008877d4`（命令位置の公開資料なし）

~~~diff
- 0088774c ["INT_ADD", "register:40f0:8", ["const:88774c:8", "const:4:8"]]
- 0088774c ["CALL", null, ["callee:00c57f80:8"]]
+ 008877a4 ["INT_ADD", "register:40f0:8", ["const:8877a4:8", "const:4:8"]]
+ 008877a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0088774c bytes d9410f94
+ 008877a4 bytes f7410f94
- 00887760 ["INT_ADD", "register:40f0:8", ["const:887760:8", "const:4:8"]]
- 00887760 ["CALL", null, ["callee:006a2bd0:8"]]
+ 008877b8 ["INT_ADD", "register:40f0:8", ["const:8877b8:8", "const:4:8"]]
+ 008877b8 ["CALL", null, ["callee:006a2bd0:8"]]
- 00887760 bytes 066df897
+ 008877b8 bytes 066df897
- 0088777c ["INT_ADD", "register:40f0:8", ["const:88777c:8", "const:4:8"]]
- 0088777c ["CALL", null, ["callee:00c57f80:8"]]
+ 008877d4 ["INT_ADD", "register:40f0:8", ["const:8877d4:8", "const:4:8"]]
+ 008877d4 ["CALL", null, ["callee:00c57f80:8"]]
- 0088777c bytes cd410f94
+ 008877d4 bytes eb410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b0ad17840a183ab0cc51aba7108b0b"></a>

### [`0088802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md) → [`00888084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md) FUN_00888084

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md#insn-00888048) · [`00888068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md#insn-00888068)
- 新版 `008880a0`（命令位置の公開資料なし） · `008880c0`（命令位置の公開資料なし）

~~~diff
- 00888048 ["INT_ADD", "register:40f0:8", ["const:888048:8", "const:4:8"]]
- 00888048 ["CALL", null, ["callee:00c53da0:8"]]
+ 008880a0 ["INT_ADD", "register:40f0:8", ["const:8880a0:8", "const:4:8"]]
+ 008880a0 ["CALL", null, ["callee:00c53da0:8"]]
- 00888048 bytes 2e2f0f94
+ 008880a0 bytes 402f0f94
- 00888068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888068 ["INT_ADD", "register:40f0:8", ["const:888068:8", "const:4:8"]]
- 00888068 ["CALLIND", null, ["register:0:8"]]
+ 008880c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008880c0 ["INT_ADD", "register:40f0:8", ["const:8880c0:8", "const:4:8"]]
+ 008880c0 ["CALLIND", null, ["register:0:8"]]
- 00888068 bytes 00013fd6
+ 008880c0 bytes 00013fd6
~~~


<a id="compare-e4b40b78f0d33b0d64836e6ec7ce874c"></a>

### [`0088807c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088807c.md) → [`008880d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008880d4.md) FUN_008880d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088807c.md#insn-00888098) · [`008880b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088807c.md#insn-008880b8)
- 新版 `008880f0`（命令位置の公開資料なし） · `00888110`（命令位置の公開資料なし）

~~~diff
- 00888098 ["INT_ADD", "register:40f0:8", ["const:888098:8", "const:4:8"]]
- 00888098 ["CALL", null, ["callee:00c53da0:8"]]
+ 008880f0 ["INT_ADD", "register:40f0:8", ["const:8880f0:8", "const:4:8"]]
+ 008880f0 ["CALL", null, ["callee:00c53da0:8"]]
- 00888098 bytes 1a2f0f94
+ 008880f0 bytes 2c2f0f94
- 008880b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008880b8 ["INT_ADD", "register:40f0:8", ["const:8880b8:8", "const:4:8"]]
- 008880b8 ["CALLIND", null, ["register:0:8"]]
+ 00888110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888110 ["INT_ADD", "register:40f0:8", ["const:888110:8", "const:4:8"]]
+ 00888110 ["CALLIND", null, ["register:0:8"]]
- 008880b8 bytes 00013fd6
+ 00888110 bytes 00013fd6
~~~


<a id="compare-da3e19d487d54da879db6238c2050e02"></a>

### [`008880cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008880cc.md) → [`00888124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888124.md) FUN_00888124

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008880e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008880cc.md#insn-008880e8) · [`00888108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008880cc.md#insn-00888108)
- 新版 `00888140`（命令位置の公開資料なし） · `00888160`（命令位置の公開資料なし）

~~~diff
- 008880e8 ["INT_ADD", "register:40f0:8", ["const:8880e8:8", "const:4:8"]]
- 008880e8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00888140 ["INT_ADD", "register:40f0:8", ["const:888140:8", "const:4:8"]]
+ 00888140 ["CALL", null, ["callee:00c53da0:8"]]
- 008880e8 bytes 062f0f94
+ 00888140 bytes 182f0f94
- 00888108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888108 ["INT_ADD", "register:40f0:8", ["const:888108:8", "const:4:8"]]
- 00888108 ["CALLIND", null, ["register:0:8"]]
+ 00888160 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888160 ["INT_ADD", "register:40f0:8", ["const:888160:8", "const:4:8"]]
+ 00888160 ["CALLIND", null, ["register:0:8"]]
- 00888108 bytes 00013fd6
+ 00888160 bytes 00013fd6
~~~


<a id="compare-c6e84214c03ec41024871fd84f5fdcf6"></a>

### [`0088811c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088811c.md) → [`00888174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888174.md) FUN_00888174

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088811c.md#insn-00888138) · [`00888158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088811c.md#insn-00888158)
- 新版 `00888190`（命令位置の公開資料なし） · `008881b0`（命令位置の公開資料なし）

~~~diff
- 00888138 ["INT_ADD", "register:40f0:8", ["const:888138:8", "const:4:8"]]
- 00888138 ["CALL", null, ["callee:00c53da0:8"]]
+ 00888190 ["INT_ADD", "register:40f0:8", ["const:888190:8", "const:4:8"]]
+ 00888190 ["CALL", null, ["callee:00c53da0:8"]]
- 00888138 bytes f22e0f94
+ 00888190 bytes 042f0f94
- 00888158 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888158 ["INT_ADD", "register:40f0:8", ["const:888158:8", "const:4:8"]]
- 00888158 ["CALLIND", null, ["register:0:8"]]
+ 008881b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008881b0 ["INT_ADD", "register:40f0:8", ["const:8881b0:8", "const:4:8"]]
+ 008881b0 ["CALLIND", null, ["register:0:8"]]
- 00888158 bytes 00013fd6
+ 008881b0 bytes 00013fd6
~~~


<a id="compare-82f59f9326adb6013026fb22124b76ae"></a>

### [`0088816c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088816c.md) → [`008881c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008881c4.md) FUN_008881c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088816c.md#insn-00888188) · [`008881a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088816c.md#insn-008881a8)
- 新版 `008881e0`（命令位置の公開資料なし） · `00888200`（命令位置の公開資料なし）

~~~diff
- 00888188 ["INT_ADD", "register:40f0:8", ["const:888188:8", "const:4:8"]]
- 00888188 ["CALL", null, ["callee:00c53da0:8"]]
+ 008881e0 ["INT_ADD", "register:40f0:8", ["const:8881e0:8", "const:4:8"]]
+ 008881e0 ["CALL", null, ["callee:00c53da0:8"]]
- 00888188 bytes de2e0f94
+ 008881e0 bytes f02e0f94
- 008881a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008881a8 ["INT_ADD", "register:40f0:8", ["const:8881a8:8", "const:4:8"]]
- 008881a8 ["CALLIND", null, ["register:0:8"]]
+ 00888200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888200 ["INT_ADD", "register:40f0:8", ["const:888200:8", "const:4:8"]]
+ 00888200 ["CALLIND", null, ["register:0:8"]]
- 008881a8 bytes 00013fd6
+ 00888200 bytes 00013fd6
~~~


<a id="compare-150a3295f21d1cee6fa9a688942687fe"></a>

### [`008881bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008881bc.md) → [`00888214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888214.md) FUN_00888214

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008881d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008881bc.md#insn-008881d8) · [`008881f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008881bc.md#insn-008881f8)
- 新版 `00888230`（命令位置の公開資料なし） · `00888250`（命令位置の公開資料なし）

~~~diff
- 008881d8 ["INT_ADD", "register:40f0:8", ["const:8881d8:8", "const:4:8"]]
- 008881d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00888230 ["INT_ADD", "register:40f0:8", ["const:888230:8", "const:4:8"]]
+ 00888230 ["CALL", null, ["callee:00c53da0:8"]]
- 008881d8 bytes ca2e0f94
+ 00888230 bytes dc2e0f94
- 008881f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008881f8 ["INT_ADD", "register:40f0:8", ["const:8881f8:8", "const:4:8"]]
- 008881f8 ["CALLIND", null, ["register:0:8"]]
+ 00888250 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888250 ["INT_ADD", "register:40f0:8", ["const:888250:8", "const:4:8"]]
+ 00888250 ["CALLIND", null, ["register:0:8"]]
- 008881f8 bytes 00013fd6
+ 00888250 bytes 00013fd6
~~~


<a id="compare-c637ed1b10d9738887870fea5e514d05"></a>

### [`0088820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088820c.md) → [`00888264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888264.md) FUN_00888264

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088820c.md#insn-00888228) · [`00888248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088820c.md#insn-00888248)
- 新版 `00888280`（命令位置の公開資料なし） · `008882a0`（命令位置の公開資料なし）

~~~diff
- 00888228 ["INT_ADD", "register:40f0:8", ["const:888228:8", "const:4:8"]]
- 00888228 ["CALL", null, ["callee:00c53da0:8"]]
+ 00888280 ["INT_ADD", "register:40f0:8", ["const:888280:8", "const:4:8"]]
+ 00888280 ["CALL", null, ["callee:00c53da0:8"]]
- 00888228 bytes b62e0f94
+ 00888280 bytes c82e0f94
- 00888248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888248 ["INT_ADD", "register:40f0:8", ["const:888248:8", "const:4:8"]]
- 00888248 ["CALLIND", null, ["register:0:8"]]
+ 008882a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008882a0 ["INT_ADD", "register:40f0:8", ["const:8882a0:8", "const:4:8"]]
+ 008882a0 ["CALLIND", null, ["register:0:8"]]
- 00888248 bytes 00013fd6
+ 008882a0 bytes 00013fd6
~~~


<a id="compare-8f01d6b35dfc0ae37b2af055c28c1219"></a>

### [`0088825c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088825c.md) → [`008882b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008882b4.md) FUN_008882b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088825c.md#insn-00888278) · [`00888298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088825c.md#insn-00888298)
- 新版 `008882d0`（命令位置の公開資料なし） · `008882f0`（命令位置の公開資料なし）

~~~diff
- 00888278 ["INT_ADD", "register:40f0:8", ["const:888278:8", "const:4:8"]]
- 00888278 ["CALL", null, ["callee:00c53da0:8"]]
+ 008882d0 ["INT_ADD", "register:40f0:8", ["const:8882d0:8", "const:4:8"]]
+ 008882d0 ["CALL", null, ["callee:00c53da0:8"]]
- 00888278 bytes a22e0f94
+ 008882d0 bytes b42e0f94
- 00888298 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888298 ["INT_ADD", "register:40f0:8", ["const:888298:8", "const:4:8"]]
- 00888298 ["CALLIND", null, ["register:0:8"]]
+ 008882f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008882f0 ["INT_ADD", "register:40f0:8", ["const:8882f0:8", "const:4:8"]]
+ 008882f0 ["CALLIND", null, ["register:0:8"]]
- 00888298 bytes 00013fd6
+ 008882f0 bytes 00013fd6
~~~


<a id="compare-c3f43311ea666835f0235c3ebdec42a5"></a>

### [`008882ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008882ac.md) → [`00888304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888304.md) FUN_00888304

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) [`006264c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264c4.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00b37a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37a18.md)
- 新版 呼出元 10件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`00616990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md) [`00626504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/00626504.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00b37ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37ab4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008883b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008882ac.md#insn-008883b8) · [`008883c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008882ac.md#insn-008883c0)
- 新版 `00888410`（命令位置の公開資料なし） · `00888418`（命令位置の公開資料なし）

~~~diff
- 008883b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008883b8 ["INT_ADD", "register:40f0:8", ["const:8883b8:8", "const:4:8"]]
- 008883b8 ["CALLIND", null, ["register:0:8"]]
+ 00888410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888410 ["INT_ADD", "register:40f0:8", ["const:888410:8", "const:4:8"]]
+ 00888410 ["CALLIND", null, ["register:0:8"]]
- 008883b8 bytes 00013fd6
+ 00888410 bytes 00013fd6
- 008883c0 ["INT_ADD", "register:40f0:8", ["const:8883c0:8", "const:4:8"]]
- 008883c0 ["CALL", null, ["callee:00b37ab4:8"]]
+ 00888418 ["INT_ADD", "register:40f0:8", ["const:888418:8", "const:4:8"]]
+ 00888418 ["CALL", null, ["callee:00b37ab4:8"]]
- 008883c0 bytes 96bd0a94
+ 00888418 bytes a7bd0a94
~~~


<a id="compare-d382ad5b5ad9cbc3c9277df565691604"></a>

### [`008887c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008887c0.md) → [`00888818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888818.md) FUN_00888818

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008887c0.md#insn-00888848) · [`00888850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008887c0.md#insn-00888850)
- 新版 `008888a0`（命令位置の公開資料なし） · `008888a8`（命令位置の公開資料なし）

~~~diff
- 00888848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888848 ["INT_ADD", "register:40f0:8", ["const:888848:8", "const:4:8"]]
- 00888848 ["CALLIND", null, ["register:0:8"]]
+ 008888a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008888a0 ["INT_ADD", "register:40f0:8", ["const:8888a0:8", "const:4:8"]]
+ 008888a0 ["CALLIND", null, ["register:0:8"]]
- 00888848 bytes 00013fd6
+ 008888a0 bytes 00013fd6
- 00888850 ["INT_ADD", "register:40f0:8", ["const:888850:8", "const:4:8"]]
- 00888850 ["CALL", null, ["callee:00c57fb0:8"]]
+ 008888a8 ["INT_ADD", "register:40f0:8", ["const:8888a8:8", "const:4:8"]]
+ 008888a8 ["CALL", null, ["callee:00c57fb0:8"]]
- 00888850 bytes a43d0f94
+ 008888a8 bytes c23d0f94
~~~


<a id="compare-cf7ceee0c85fc517e269ae218258b550"></a>

### [`00888e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md) → [`00888ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888ed4.md) FUN_00888ed4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md#insn-00888ee8) · [`00888ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md#insn-00888ef8) · [`00888f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md#insn-00888f18)
- 新版 `00888f40`（命令位置の公開資料なし） · `00888f50`（命令位置の公開資料なし） · `00888f70`（命令位置の公開資料なし）

~~~diff
- 00888ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888ee8 ["INT_ADD", "register:40f0:8", ["const:888ee8:8", "const:4:8"]]
- 00888ee8 ["CALLIND", null, ["register:0:8"]]
+ 00888f40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888f40 ["INT_ADD", "register:40f0:8", ["const:888f40:8", "const:4:8"]]
+ 00888f40 ["CALLIND", null, ["register:0:8"]]
- 00888ee8 bytes 00013fd6
+ 00888f40 bytes 00013fd6
- 00888ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888ef8 ["INT_ADD", "register:40f0:8", ["const:888ef8:8", "const:4:8"]]
- 00888ef8 ["CALLIND", null, ["register:0:8"]]
+ 00888f50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888f50 ["INT_ADD", "register:40f0:8", ["const:888f50:8", "const:4:8"]]
+ 00888f50 ["CALLIND", null, ["register:0:8"]]
- 00888ef8 bytes 00013fd6
+ 00888f50 bytes 00013fd6
- 00888f18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888f18 ["INT_ADD", "register:40f0:8", ["const:888f18:8", "const:4:8"]]
- 00888f18 ["CALLIND", null, ["register:0:8"]]
+ 00888f70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888f70 ["INT_ADD", "register:40f0:8", ["const:888f70:8", "const:4:8"]]
+ 00888f70 ["CALLIND", null, ["register:0:8"]]
- 00888f18 bytes 00013fd6
+ 00888f70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a808c05933acde4214df15047846ab5"></a>

### [`00889070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889070.md) → [`008890c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008890c8.md) FUN_008890c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008890dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889070.md#insn-008890dc) · [`008890ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889070.md#insn-008890ec) · [`0088910c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889070.md#insn-0088910c)
- 新版 `00889134`（命令位置の公開資料なし） · `00889144`（命令位置の公開資料なし） · `00889164`（命令位置の公開資料なし）

~~~diff
- 008890dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008890dc ["INT_ADD", "register:40f0:8", ["const:8890dc:8", "const:4:8"]]
- 008890dc ["CALLIND", null, ["register:0:8"]]
+ 00889134 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889134 ["INT_ADD", "register:40f0:8", ["const:889134:8", "const:4:8"]]
+ 00889134 ["CALLIND", null, ["register:0:8"]]
- 008890dc bytes 00013fd6
+ 00889134 bytes 00013fd6
- 008890ec ["COPY", "register:0:8", ["register:4040:8"]]
- 008890ec ["INT_ADD", "register:40f0:8", ["const:8890ec:8", "const:4:8"]]
- 008890ec ["CALLIND", null, ["register:0:8"]]
+ 00889144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889144 ["INT_ADD", "register:40f0:8", ["const:889144:8", "const:4:8"]]
+ 00889144 ["CALLIND", null, ["register:0:8"]]
- 008890ec bytes 00013fd6
+ 00889144 bytes 00013fd6
- 0088910c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088910c ["INT_ADD", "register:40f0:8", ["const:88910c:8", "const:4:8"]]
- 0088910c ["CALLIND", null, ["register:0:8"]]
+ 00889164 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889164 ["INT_ADD", "register:40f0:8", ["const:889164:8", "const:4:8"]]
+ 00889164 ["CALLIND", null, ["register:0:8"]]
- 0088910c bytes 00013fd6
+ 00889164 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c96ecf8a5ba54e3a40697bfff943fba"></a>

### [`0088956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088956c.md) → [`008895c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008895c4.md) FUN_008895c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008895d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088956c.md#insn-008895d8) · [`008895e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088956c.md#insn-008895e8) · [`00889608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088956c.md#insn-00889608)
- 新版 `00889630`（命令位置の公開資料なし） · `00889640`（命令位置の公開資料なし） · `00889660`（命令位置の公開資料なし）

~~~diff
- 008895d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008895d8 ["INT_ADD", "register:40f0:8", ["const:8895d8:8", "const:4:8"]]
- 008895d8 ["CALLIND", null, ["register:0:8"]]
+ 00889630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889630 ["INT_ADD", "register:40f0:8", ["const:889630:8", "const:4:8"]]
+ 00889630 ["CALLIND", null, ["register:0:8"]]
- 008895d8 bytes 00013fd6
+ 00889630 bytes 00013fd6
- 008895e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008895e8 ["INT_ADD", "register:40f0:8", ["const:8895e8:8", "const:4:8"]]
- 008895e8 ["CALLIND", null, ["register:0:8"]]
+ 00889640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889640 ["INT_ADD", "register:40f0:8", ["const:889640:8", "const:4:8"]]
+ 00889640 ["CALLIND", null, ["register:0:8"]]
- 008895e8 bytes 00013fd6
+ 00889640 bytes 00013fd6
- 00889608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889608 ["INT_ADD", "register:40f0:8", ["const:889608:8", "const:4:8"]]
- 00889608 ["CALLIND", null, ["register:0:8"]]
+ 00889660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889660 ["INT_ADD", "register:40f0:8", ["const:889660:8", "const:4:8"]]
+ 00889660 ["CALLIND", null, ["register:0:8"]]
- 00889608 bytes 00013fd6
+ 00889660 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc251e326478e064f9773bf7b7a7dae9"></a>

### [`0088a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md) → [`0088a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3e0.md) FUN_0088a3e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md#insn-0088a3b8) · [`0088a3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md#insn-0088a3e4) · [`0088a414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md#insn-0088a414)
- 新版 `0088a410`（命令位置の公開資料なし） · `0088a43c`（命令位置の公開資料なし） · `0088a46c`（命令位置の公開資料なし）

~~~diff
- 0088a3b8 ["INT_ADD", "register:40f0:8", ["const:88a3b8:8", "const:4:8"]]
- 0088a3b8 ["CALL", null, ["callee:00b37c24:8"]]
+ 0088a410 ["INT_ADD", "register:40f0:8", ["const:88a410:8", "const:4:8"]]
+ 0088a410 ["CALL", null, ["callee:00b37c24:8"]]
- 0088a3b8 bytes f4b50a94
+ 0088a410 bytes 05b60a94
- 0088a3e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a3e4 ["INT_ADD", "register:40f0:8", ["const:88a3e4:8", "const:4:8"]]
- 0088a3e4 ["CALLIND", null, ["register:0:8"]]
+ 0088a43c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a43c ["INT_ADD", "register:40f0:8", ["const:88a43c:8", "const:4:8"]]
+ 0088a43c ["CALLIND", null, ["register:0:8"]]
- 0088a3e4 bytes 00013fd6
+ 0088a43c bytes 00013fd6
- 0088a414 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a414 ["INT_ADD", "register:40f0:8", ["const:88a414:8", "const:4:8"]]
- 0088a414 ["CALLIND", null, ["register:0:8"]]
+ 0088a46c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a46c ["INT_ADD", "register:40f0:8", ["const:88a46c:8", "const:4:8"]]
+ 0088a46c ["CALLIND", null, ["register:0:8"]]
- 0088a414 bytes 00013fd6
+ 0088a46c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c16bc1825e3dc7258291f46dbc119e4"></a>

### [`0088a4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a4e0.md) → [`0088a538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a538.md) FUN_0088a538

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 5件 [`0088a630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a630.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 5件 [`0088a688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a688.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a4e0.md#insn-0088a5d4) · [`0088a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a4e0.md#insn-0088a5fc) · [`0088a610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a4e0.md#insn-0088a610)
- 新版 `0088a62c`（命令位置の公開資料なし） · `0088a654`（命令位置の公開資料なし） · `0088a668`（命令位置の公開資料なし）

~~~diff
- 0088a5d4 ["INT_ADD", "register:40f0:8", ["const:88a5d4:8", "const:4:8"]]
- 0088a5d4 ["CALL", null, ["callee:0088a688:8"]]
+ 0088a62c ["INT_ADD", "register:40f0:8", ["const:88a62c:8", "const:4:8"]]
+ 0088a62c ["CALL", null, ["callee:0088a688:8"]]
- 0088a5d4 bytes 17000094
+ 0088a62c bytes 17000094
- 0088a5fc ["INT_ADD", "register:40f0:8", ["const:88a5fc:8", "const:4:8"]]
- 0088a5fc ["CALL", null, ["callee:00c53da0:8"]]
+ 0088a654 ["INT_ADD", "register:40f0:8", ["const:88a654:8", "const:4:8"]]
+ 0088a654 ["CALL", null, ["callee:00c53da0:8"]]
- 0088a5fc bytes c1250f94
+ 0088a654 bytes d3250f94
- 0088a610 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a610 ["INT_ADD", "register:40f0:8", ["const:88a610:8", "const:4:8"]]
- 0088a610 ["CALLIND", null, ["register:0:8"]]
+ 0088a668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a668 ["INT_ADD", "register:40f0:8", ["const:88a668:8", "const:4:8"]]
+ 0088a668 ["CALLIND", null, ["register:0:8"]]
- 0088a610 bytes 00013fd6
+ 0088a668 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d19c1de7ef314d3921e78d39ff71c16a"></a>

### [`0088a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a764.md) → [`0088a7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a7bc.md) FUN_0088a7bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a764.md#insn-0088a794) · [`0088a7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a764.md#insn-0088a7a8) · [`0088a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a764.md#insn-0088a7b0)
- 新版 `0088a7ec`（命令位置の公開資料なし） · `0088a800`（命令位置の公開資料なし） · `0088a808`（命令位置の公開資料なし）

~~~diff
- 0088a794 ["INT_ADD", "register:40f0:8", ["const:88a794:8", "const:4:8"]]
- 0088a794 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088a7ec ["INT_ADD", "register:40f0:8", ["const:88a7ec:8", "const:4:8"]]
+ 0088a7ec ["CALL", null, ["callee:00c53da0:8"]]
- 0088a794 bytes 5b250f94
+ 0088a7ec bytes 6d250f94
- 0088a7a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a7a8 ["INT_ADD", "register:40f0:8", ["const:88a7a8:8", "const:4:8"]]
- 0088a7a8 ["CALLIND", null, ["register:0:8"]]
+ 0088a800 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a800 ["INT_ADD", "register:40f0:8", ["const:88a800:8", "const:4:8"]]
+ 0088a800 ["CALLIND", null, ["register:0:8"]]
- 0088a7a8 bytes 00013fd6
+ 0088a800 bytes 00013fd6
- 0088a7b0 ["INT_ADD", "register:40f0:8", ["const:88a7b0:8", "const:4:8"]]
- 0088a7b0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0088a808 ["INT_ADD", "register:40f0:8", ["const:88a808:8", "const:4:8"]]
+ 0088a808 ["CALL", null, ["callee:00c57f50:8"]]
- 0088a7b0 bytes b4350f94
+ 0088a808 bytes d2350f94
~~~


<a id="compare-acd875bdd072313838550db79423962c"></a>

### [`0088a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md) → [`0088a948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md) FUN_0088a948

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 4件 [`0088ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 4件 [`0088ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md#insn-0088a9d4) · [`0088aa74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md#insn-0088aa74) · [`0088aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md#insn-0088aa90)
- 新版 `0088aa2c`（命令位置の公開資料なし） · `0088aacc`（命令位置の公開資料なし） · `0088aae8`（命令位置の公開資料なし）

~~~diff
- 0088a9d4 ["INT_ADD", "register:40f0:8", ["const:88a9d4:8", "const:4:8"]]
- 0088a9d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088aa2c ["INT_ADD", "register:40f0:8", ["const:88aa2c:8", "const:4:8"]]
+ 0088aa2c ["CALL", null, ["callee:00c57f60:8"]]
- 0088a9d4 bytes 2f350f94
+ 0088aa2c bytes 4d350f94
- 0088aa74 ["INT_ADD", "register:40f0:8", ["const:88aa74:8", "const:4:8"]]
- 0088aa74 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 0088aacc ["INT_ADD", "register:40f0:8", ["const:88aacc:8", "const:4:8"]]
+ 0088aacc ["CALL", null, ["callee:00c5a8f0:8"]]
- 0088aa74 bytes 6b3f0f94
+ 0088aacc bytes 893f0f94
- 0088aa90 ["INT_ADD", "register:40f0:8", ["const:88aa90:8", "const:4:8"]]
- 0088aa90 ["CALL", null, ["callee:0088ac64:8"]]
+ 0088aae8 ["INT_ADD", "register:40f0:8", ["const:88aae8:8", "const:4:8"]]
+ 0088aae8 ["CALL", null, ["callee:0088ac64:8"]]
- 0088aa90 bytes 5f000094
+ 0088aae8 bytes 5f000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1530d88caa2cdb25487d70ae6bb9d5"></a>

### [`0088ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md) → [`0088ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md) FUN_0088ac64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0088a948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md#insn-0088ac30) · [`0088ac44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md#insn-0088ac44) · [`0088aca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md#insn-0088aca4)
- 新版 `0088ac88`（命令位置の公開資料なし） · `0088ac9c`（命令位置の公開資料なし） · `0088acfc`（命令位置の公開資料なし）

~~~diff
- 0088ac30 ["INT_ADD", "register:40f0:8", ["const:88ac30:8", "const:4:8"]]
- 0088ac30 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088ac88 ["INT_ADD", "register:40f0:8", ["const:88ac88:8", "const:4:8"]]
+ 0088ac88 ["CALL", null, ["callee:00c57f60:8"]]
- 0088ac30 bytes 98340f94
+ 0088ac88 bytes b6340f94
- 0088ac44 ["INT_ADD", "register:40f0:8", ["const:88ac44:8", "const:4:8"]]
- 0088ac44 ["CALL", null, ["callee:00c57f80:8"]]
+ 0088ac9c ["INT_ADD", "register:40f0:8", ["const:88ac9c:8", "const:4:8"]]
+ 0088ac9c ["CALL", null, ["callee:00c57f80:8"]]
- 0088ac44 bytes 9b340f94
+ 0088ac9c bytes b9340f94
- 0088aca4 ["INT_ADD", "register:40f0:8", ["const:88aca4:8", "const:4:8"]]
- 0088aca4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0088acfc ["INT_ADD", "register:40f0:8", ["const:88acfc:8", "const:4:8"]]
+ 0088acfc ["CALL", null, ["callee:00c57f80:8"]]
- 0088aca4 bytes 83340f94
+ 0088acfc bytes a1340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2dfb520904888e2bb83a1b1b3b291e"></a>

### [`0088b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b940.md) → [`0088b998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b998.md) FUN_0088b998

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088b994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b940.md#insn-0088b994) · [`0088b9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b940.md#insn-0088b9c8) · [`0088b9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b940.md#insn-0088b9cc)
- 新版 `0088b9ec`（命令位置の公開資料なし） · `0088ba20`（命令位置の公開資料なし） · `0088ba24`（命令位置の公開資料なし）

~~~diff
- 0088b994 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088b994 ["INT_ADD", "register:40f0:8", ["const:88b994:8", "const:4:8"]]
- 0088b994 ["CALLIND", null, ["register:0:8"]]
+ 0088b9ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088b9ec ["INT_ADD", "register:40f0:8", ["const:88b9ec:8", "const:4:8"]]
+ 0088b9ec ["CALLIND", null, ["register:0:8"]]
- 0088b994 bytes 00013fd6
+ 0088b9ec bytes 00013fd6
- 0088b9c8 ["INT_ADD", "register:40f0:8", ["const:88b9c8:8", "const:4:8"]]
- 0088b9c8 ["CALL", null, ["callee:00459db4:8"]]
+ 0088ba20 ["INT_ADD", "register:40f0:8", ["const:88ba20:8", "const:4:8"]]
+ 0088ba20 ["CALL", null, ["callee:00459db4:8"]]
- 0088b9c8 bytes eb38ef97
+ 0088ba20 bytes e538ef97
- 0088b9cc ["INT_ADD", "register:40f0:8", ["const:88b9cc:8", "const:4:8"]]
- 0088b9cc ["CALL", null, ["callee:00c57fb0:8"]]
+ 0088ba24 ["INT_ADD", "register:40f0:8", ["const:88ba24:8", "const:4:8"]]
+ 0088ba24 ["CALL", null, ["callee:00c57fb0:8"]]
- 0088b9cc bytes 45310f94
+ 0088ba24 bytes 63310f94
~~~


<a id="compare-3bc299bbc73a56a414c1478552edc005"></a>

### [`0088ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba50.md) → [`0088baa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa8.md) FUN_0088baa8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba50.md#insn-0088ba90) · [`0088bac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba50.md#insn-0088bac4) · [`0088bac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba50.md#insn-0088bac8)
- 新版 `0088bae8`（命令位置の公開資料なし） · `0088bb1c`（命令位置の公開資料なし） · `0088bb20`（命令位置の公開資料なし）

~~~diff
- 0088ba90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088ba90 ["INT_ADD", "register:40f0:8", ["const:88ba90:8", "const:4:8"]]
- 0088ba90 ["CALLIND", null, ["register:0:8"]]
+ 0088bae8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088bae8 ["INT_ADD", "register:40f0:8", ["const:88bae8:8", "const:4:8"]]
+ 0088bae8 ["CALLIND", null, ["register:0:8"]]
- 0088ba90 bytes 00013fd6
+ 0088bae8 bytes 00013fd6
- 0088bac4 ["INT_ADD", "register:40f0:8", ["const:88bac4:8", "const:4:8"]]
- 0088bac4 ["CALL", null, ["callee:00459db4:8"]]
+ 0088bb1c ["INT_ADD", "register:40f0:8", ["const:88bb1c:8", "const:4:8"]]
+ 0088bb1c ["CALL", null, ["callee:00459db4:8"]]
- 0088bac4 bytes ac38ef97
+ 0088bb1c bytes a638ef97
- 0088bac8 ["INT_ADD", "register:40f0:8", ["const:88bac8:8", "const:4:8"]]
- 0088bac8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0088bb20 ["INT_ADD", "register:40f0:8", ["const:88bb20:8", "const:4:8"]]
+ 0088bb20 ["CALL", null, ["callee:00c57fb0:8"]]
- 0088bac8 bytes 06310f94
+ 0088bb20 bytes 24310f94
~~~


<a id="compare-f69f0d4895376daea78d9272f3725889"></a>

### [`0088bb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb48.md) → [`0088bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bba0.md) FUN_0088bba0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088bb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb48.md#insn-0088bb6c)
- 新版 `0088bbc4`（命令位置の公開資料なし）

~~~diff
- 0088bb6c ["INT_ADD", "register:40f0:8", ["const:88bb6c:8", "const:4:8"]]
- 0088bb6c ["CALL", null, ["callee:00459db4:8"]]
+ 0088bbc4 ["INT_ADD", "register:40f0:8", ["const:88bbc4:8", "const:4:8"]]
+ 0088bbc4 ["CALL", null, ["callee:00459db4:8"]]
- 0088bb6c bytes 8238ef97
+ 0088bbc4 bytes 7c38ef97
~~~


<a id="compare-1acc550d86cd6dc16003b016287b4876"></a>

### [`0088bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md) → [`0088bc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bc44.md) FUN_0088bc44

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00b37a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37a18.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00b37ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37ab4.md) [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088bc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md#insn-0088bc14) · [`0088bc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md#insn-0088bc30) · [`0088bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md#insn-0088bc5c)
- 新版 `0088bc6c`（命令位置の公開資料なし） · `0088bc88`（命令位置の公開資料なし） · `0088bcb4`（命令位置の公開資料なし）

~~~diff
- 0088bc14 ["INT_ADD", "register:40f0:8", ["const:88bc14:8", "const:4:8"]]
- 0088bc14 ["CALL", null, ["callee:00b37ab4:8"]]
+ 0088bc6c ["INT_ADD", "register:40f0:8", ["const:88bc6c:8", "const:4:8"]]
+ 0088bc6c ["CALL", null, ["callee:00b37ab4:8"]]
- 0088bc14 bytes 81af0a94
+ 0088bc6c bytes 92af0a94
- 0088bc30 ["INT_ADD", "register:40f0:8", ["const:88bc30:8", "const:4:8"]]
- 0088bc30 ["CALL", null, ["callee:00b37c24:8"]]
+ 0088bc88 ["INT_ADD", "register:40f0:8", ["const:88bc88:8", "const:4:8"]]
+ 0088bc88 ["CALL", null, ["callee:00b37c24:8"]]
- 0088bc30 bytes d6af0a94
+ 0088bc88 bytes e7af0a94
- 0088bc5c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088bc5c ["INT_ADD", "register:40f0:8", ["const:88bc5c:8", "const:4:8"]]
- 0088bc5c ["CALLIND", null, ["register:0:8"]]
+ 0088bcb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088bcb4 ["INT_ADD", "register:40f0:8", ["const:88bcb4:8", "const:4:8"]]
+ 0088bcb4 ["CALLIND", null, ["register:0:8"]]
- 0088bc5c bytes 00013fd6
+ 0088bcb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c5ca5159409ea5cf75e72e07b266c1"></a>

### [`0088eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088e/0088eec0.md) → [`0088ef18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088e/0088ef18.md) FUN_0088ef18

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088ef70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088e/0088eec0.md#insn-0088ef70) · [`0088efc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088e/0088eec0.md#insn-0088efc4) · [`0088efd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088e/0088eec0.md#insn-0088efd8)
- 新版 `0088efc8`（命令位置の公開資料なし） · `0088f01c`（命令位置の公開資料なし） · `0088f030`（命令位置の公開資料なし）

~~~diff
- 0088ef70 ["INT_ADD", "register:40f0:8", ["const:88ef70:8", "const:4:8"]]
- 0088ef70 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088efc8 ["INT_ADD", "register:40f0:8", ["const:88efc8:8", "const:4:8"]]
+ 0088efc8 ["CALL", null, ["callee:00c57f60:8"]]
- 0088ef70 bytes c8230f94
+ 0088efc8 bytes e6230f94
- 0088efc4 ["INT_ADD", "register:40f0:8", ["const:88efc4:8", "const:4:8"]]
- 0088efc4 ["CALL", null, ["callee:00c580d0:8"]]
+ 0088f01c ["INT_ADD", "register:40f0:8", ["const:88f01c:8", "const:4:8"]]
+ 0088f01c ["CALL", null, ["callee:00c580d0:8"]]
- 0088efc4 bytes 0f240f94
+ 0088f01c bytes 2d240f94
- 0088efd8 ["INT_ADD", "register:40f0:8", ["const:88efd8:8", "const:4:8"]]
- 0088efd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0088f030 ["INT_ADD", "register:40f0:8", ["const:88f030:8", "const:4:8"]]
+ 0088f030 ["CALL", null, ["callee:00c57f80:8"]]
- 0088efd8 bytes b6230f94
+ 0088f030 bytes d4230f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230bd0c66609a1c6beb23d7063f09f74"></a>

### [`0088f000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f000.md) → [`0088f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f058.md) FUN_0088f058

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f000.md#insn-0088f044)
- 新版 `0088f09c`（命令位置の公開資料なし）

~~~diff
- 0088f044 ["INT_ADD", "register:40f0:8", ["const:88f044:8", "const:4:8"]]
- 0088f044 ["CALL", null, ["callee:00c58120:8"]]
+ 0088f09c ["INT_ADD", "register:40f0:8", ["const:88f09c:8", "const:4:8"]]
+ 0088f09c ["CALL", null, ["callee:00c58120:8"]]
- 0088f044 bytes 03240f94
+ 0088f09c bytes 21240f94
~~~


<a id="compare-65e859d97b48756833f8738bdf19bc90"></a>

### [`0088f0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f0c0.md) → [`0088f118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f118.md) FUN_0088f118

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f0c0.md#insn-0088f0f4) · [`0088f108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f0c0.md#insn-0088f108) · [`0088f158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f0c0.md#insn-0088f158)
- 新版 `0088f14c`（命令位置の公開資料なし） · `0088f160`（命令位置の公開資料なし） · `0088f1b0`（命令位置の公開資料なし）

~~~diff
- 0088f0f4 ["INT_ADD", "register:40f0:8", ["const:88f0f4:8", "const:4:8"]]
- 0088f0f4 ["CALL", null, ["callee:006394fc:8"]]
+ 0088f14c ["INT_ADD", "register:40f0:8", ["const:88f14c:8", "const:4:8"]]
+ 0088f14c ["CALL", null, ["callee:006394fc:8"]]
- 0088f0f4 bytes f2a8f697
+ 0088f14c bytes eca8f697
- 0088f108 ["INT_ADD", "register:40f0:8", ["const:88f108:8", "const:4:8"]]
- 0088f108 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088f160 ["INT_ADD", "register:40f0:8", ["const:88f160:8", "const:4:8"]]
+ 0088f160 ["CALL", null, ["callee:00c57f60:8"]]
- 0088f108 bytes 62230f94
+ 0088f160 bytes 80230f94
- 0088f158 ["INT_ADD", "register:40f0:8", ["const:88f158:8", "const:4:8"]]
- 0088f158 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0088f1b0 ["INT_ADD", "register:40f0:8", ["const:88f1b0:8", "const:4:8"]]
+ 0088f1b0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0088f158 bytes 93b2ee97
+ 0088f1b0 bytes 8db2ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5d443d01747be078a2f175d3605f78"></a>

### [`0088f198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f198.md) → [`0088f1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f1f0.md) FUN_0088f1f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f198.md#insn-0088f210) · [`0088f238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f198.md#insn-0088f238)
- 新版 `0088f268`（命令位置の公開資料なし） · `0088f290`（命令位置の公開資料なし）

~~~diff
- 0088f210 ["INT_ADD", "register:40f0:8", ["const:88f210:8", "const:4:8"]]
- 0088f210 ["CALL", null, ["callee:00c58120:8"]]
+ 0088f268 ["INT_ADD", "register:40f0:8", ["const:88f268:8", "const:4:8"]]
+ 0088f268 ["CALL", null, ["callee:00c58120:8"]]
- 0088f210 bytes 90230f94
+ 0088f268 bytes ae230f94
- 0088f238 ["INT_ADD", "register:40f0:8", ["const:88f238:8", "const:4:8"]]
- 0088f238 ["CALL", null, ["callee:00c58120:8"]]
+ 0088f290 ["INT_ADD", "register:40f0:8", ["const:88f290:8", "const:4:8"]]
+ 0088f290 ["CALL", null, ["callee:00c58120:8"]]
- 0088f238 bytes 86230f94
+ 0088f290 bytes a4230f94
~~~


<a id="compare-106d4c46dfda1f7008078afb56fbd35a"></a>

### [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) → [`0088f34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md) FUN_0088f34c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 2件 [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 2件 [`0046d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d6ec.md) [`00564320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md#insn-0088f304) · [`0088f31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md#insn-0088f31c)
- 新版 `0088f35c`（命令位置の公開資料なし） · `0088f374`（命令位置の公開資料なし）

~~~diff
- 0088f304 ["INT_ADD", "register:40f0:8", ["const:88f304:8", "const:4:8"]]
- 0088f304 ["CALL", null, ["callee:0046d6ec:8"]]
+ 0088f35c ["INT_ADD", "register:40f0:8", ["const:88f35c:8", "const:4:8"]]
+ 0088f35c ["CALL", null, ["callee:0046d6ec:8"]]
- 0088f304 bytes ea78ef97
+ 0088f35c bytes e478ef97
- 0088f31c ["INT_ADD", "register:40f0:8", ["const:88f31c:8", "const:4:8"]]
- 0088f31c ["CALL", null, ["callee:00564320:8"]]
+ 0088f374 ["INT_ADD", "register:40f0:8", ["const:88f374:8", "const:4:8"]]
+ 0088f374 ["CALL", null, ["callee:00564320:8"]]
- 0088f31c bytes f153f397
+ 0088f374 bytes eb53f397
~~~


<a id="compare-f5c250524528c8991f6beb8227c9b348"></a>

### [`0088f338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f338.md) → [`0088f390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f390.md) FUN_0088f390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 1件 [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`00aa3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa3e94.md) · 呼出先 1件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f338.md#insn-0088f35c)
- 新版 `0088f3b4`（命令位置の公開資料なし）

~~~diff
- 0088f35c ["INT_ADD", "register:40f0:8", ["const:88f35c:8", "const:4:8"]]
- 0088f35c ["CALL", null, ["callee:00c5a9c0:8"]]
+ 0088f3b4 ["INT_ADD", "register:40f0:8", ["const:88f3b4:8", "const:4:8"]]
+ 0088f3b4 ["CALL", null, ["callee:00c5a9c0:8"]]
- 0088f35c bytes 652d0f94
+ 0088f3b4 bytes 832d0f94
~~~


<a id="compare-0d227dad1df02a51bd8553913330acb2"></a>

### [`0088f380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f380.md) → [`0088f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f3d8.md) FUN_0088f3d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f380.md#insn-0088f3c4) · [`0088f3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f380.md#insn-0088f3d4) · [`0088f3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f380.md#insn-0088f3e0)
- 新版 `0088f41c`（命令位置の公開資料なし） · `0088f42c`（命令位置の公開資料なし） · `0088f438`（命令位置の公開資料なし）

~~~diff
- 0088f3c4 ["INT_ADD", "register:40f0:8", ["const:88f3c4:8", "const:4:8"]]
- 0088f3c4 ["CALL", null, ["callee:00c5a900:8"]]
+ 0088f41c ["INT_ADD", "register:40f0:8", ["const:88f41c:8", "const:4:8"]]
+ 0088f41c ["CALL", null, ["callee:00c5a900:8"]]
- 0088f3c4 bytes 1b2d0f94
+ 0088f41c bytes 392d0f94
- 0088f3d4 ["INT_ADD", "register:40f0:8", ["const:88f3d4:8", "const:4:8"]]
- 0088f3d4 ["CALL", null, ["callee:00c5a910:8"]]
+ 0088f42c ["INT_ADD", "register:40f0:8", ["const:88f42c:8", "const:4:8"]]
+ 0088f42c ["CALL", null, ["callee:00c5a910:8"]]
- 0088f3d4 bytes 1b2d0f94
+ 0088f42c bytes 392d0f94
- 0088f3e0 ["INT_ADD", "register:40f0:8", ["const:88f3e0:8", "const:4:8"]]
- 0088f3e0 ["CALL", null, ["callee:00c5a900:8"]]
+ 0088f438 ["INT_ADD", "register:40f0:8", ["const:88f438:8", "const:4:8"]]
+ 0088f438 ["CALL", null, ["callee:00c5a900:8"]]
- 0088f3e0 bytes 142d0f94
+ 0088f438 bytes 322d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee02cace88c9a2e101bcad03de25de21"></a>

### [`0088f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md) → [`0088f4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4f4.md) FUN_0088f4f4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00769260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769260.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) [`009bd45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd45c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`007692b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0088c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md) [`009bd4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bd/009bd4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md#insn-0088f4e0) · [`0088f4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md#insn-0088f4f0) · [`0088f4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md#insn-0088f4f4)
- 新版 `0088f538`（命令位置の公開資料なし） · `0088f548`（命令位置の公開資料なし） · `0088f54c`（命令位置の公開資料なし）

~~~diff
- 0088f4e0 ["INT_ADD", "register:40f0:8", ["const:88f4e0:8", "const:4:8"]]
- 0088f4e0 ["CALL", null, ["callee:009bd4b0:8"]]
+ 0088f538 ["INT_ADD", "register:40f0:8", ["const:88f538:8", "const:4:8"]]
+ 0088f538 ["CALL", null, ["callee:009bd4b0:8"]]
- 0088f4e0 bytes dfb70494
+ 0088f538 bytes deb70494
- 0088f4f0 ["INT_ADD", "register:40f0:8", ["const:88f4f0:8", "const:4:8"]]
- 0088f4f0 ["CALL", null, ["callee:00851550:8"]]
+ 0088f548 ["INT_ADD", "register:40f0:8", ["const:88f548:8", "const:4:8"]]
+ 0088f548 ["CALL", null, ["callee:00851550:8"]]
- 0088f4f0 bytes 0208ff97
+ 0088f548 bytes 0208ff97
- 0088f4f4 ["INT_ADD", "register:40f0:8", ["const:88f4f4:8", "const:4:8"]]
- 0088f4f4 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 0088f54c ["INT_ADD", "register:40f0:8", ["const:88f54c:8", "const:4:8"]]
+ 0088f54c ["CALL", null, ["callee:00a1a6f8:8"]]
- 0088f4f4 bytes 6c2c0694
+ 0088f54c bytes 6b2c0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42404b2c2fc07db03d7b0542f559e348"></a>

### [`0088fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fad8.md) → [`0088fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb30.md) FUN_0088fb30

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088faf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fad8.md#insn-0088faf4) · [`0088fb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fad8.md#insn-0088fb14)
- 新版 `0088fb4c`（命令位置の公開資料なし） · `0088fb6c`（命令位置の公開資料なし）

~~~diff
- 0088faf4 ["INT_ADD", "register:40f0:8", ["const:88faf4:8", "const:4:8"]]
- 0088faf4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088fb4c ["INT_ADD", "register:40f0:8", ["const:88fb4c:8", "const:4:8"]]
+ 0088fb4c ["CALL", null, ["callee:00c53da0:8"]]
- 0088faf4 bytes 83100f94
+ 0088fb4c bytes 95100f94
- 0088fb14 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fb14 ["INT_ADD", "register:40f0:8", ["const:88fb14:8", "const:4:8"]]
- 0088fb14 ["CALLIND", null, ["register:0:8"]]
+ 0088fb6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fb6c ["INT_ADD", "register:40f0:8", ["const:88fb6c:8", "const:4:8"]]
+ 0088fb6c ["CALLIND", null, ["register:0:8"]]
- 0088fb14 bytes 00013fd6
+ 0088fb6c bytes 00013fd6
~~~


<a id="compare-3fc54638eaae1020d94595ce0f3c523f"></a>

### [`0088fc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md) → [`0088fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fcbc.md) FUN_0088fcbc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0088f738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md#insn-0088fc80) · [`0088fca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md#insn-0088fca0)
- 新版 `0088fcd8`（命令位置の公開資料なし） · `0088fcf8`（命令位置の公開資料なし）

~~~diff
- 0088fc80 ["INT_ADD", "register:40f0:8", ["const:88fc80:8", "const:4:8"]]
- 0088fc80 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088fcd8 ["INT_ADD", "register:40f0:8", ["const:88fcd8:8", "const:4:8"]]
+ 0088fcd8 ["CALL", null, ["callee:00c53da0:8"]]
- 0088fc80 bytes 20100f94
+ 0088fcd8 bytes 32100f94
- 0088fca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fca0 ["INT_ADD", "register:40f0:8", ["const:88fca0:8", "const:4:8"]]
- 0088fca0 ["CALLIND", null, ["register:0:8"]]
+ 0088fcf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fcf8 ["INT_ADD", "register:40f0:8", ["const:88fcf8:8", "const:4:8"]]
+ 0088fcf8 ["CALLIND", null, ["register:0:8"]]
- 0088fca0 bytes 00013fd6
+ 0088fcf8 bytes 00013fd6
~~~


<a id="compare-8c2d495efe3d94e99c1de1215544f9b1"></a>

### [`0088fcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fcb4.md) → [`0088fd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd0c.md) FUN_0088fd0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0088f738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fcb4.md#insn-0088fcd4) · [`0088fce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fcb4.md#insn-0088fce8) · [`0088fcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fcb4.md#insn-0088fcf0)
- 新版 `0088fd2c`（命令位置の公開資料なし） · `0088fd40`（命令位置の公開資料なし） · `0088fd48`（命令位置の公開資料なし）

~~~diff
- 0088fcd4 ["INT_ADD", "register:40f0:8", ["const:88fcd4:8", "const:4:8"]]
- 0088fcd4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088fd2c ["INT_ADD", "register:40f0:8", ["const:88fd2c:8", "const:4:8"]]
+ 0088fd2c ["CALL", null, ["callee:00c53da0:8"]]
- 0088fcd4 bytes 0b100f94
+ 0088fd2c bytes 1d100f94
- 0088fce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fce8 ["INT_ADD", "register:40f0:8", ["const:88fce8:8", "const:4:8"]]
- 0088fce8 ["CALLIND", null, ["register:0:8"]]
+ 0088fd40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fd40 ["INT_ADD", "register:40f0:8", ["const:88fd40:8", "const:4:8"]]
+ 0088fd40 ["CALLIND", null, ["register:0:8"]]
- 0088fce8 bytes 00013fd6
+ 0088fd40 bytes 00013fd6
- 0088fcf0 ["INT_ADD", "register:40f0:8", ["const:88fcf0:8", "const:4:8"]]
- 0088fcf0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0088fd48 ["INT_ADD", "register:40f0:8", ["const:88fd48:8", "const:4:8"]]
+ 0088fd48 ["CALL", null, ["callee:00c57f50:8"]]
- 0088fcf0 bytes 64200f94
+ 0088fd48 bytes 82200f94
~~~


<a id="compare-ee9325ad68809d378ca7691535930125"></a>

### [`00890028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890028.md) → [`00890080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890080.md) FUN_00890080

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890028.md#insn-00890044) · [`00890064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890028.md#insn-00890064)
- 新版 `0089009c`（命令位置の公開資料なし） · `008900bc`（命令位置の公開資料なし）

~~~diff
- 00890044 ["INT_ADD", "register:40f0:8", ["const:890044:8", "const:4:8"]]
- 00890044 ["CALL", null, ["callee:00c53da0:8"]]
+ 0089009c ["INT_ADD", "register:40f0:8", ["const:89009c:8", "const:4:8"]]
+ 0089009c ["CALL", null, ["callee:00c53da0:8"]]
- 00890044 bytes 2f0f0f94
+ 0089009c bytes 410f0f94
- 00890064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890064 ["INT_ADD", "register:40f0:8", ["const:890064:8", "const:4:8"]]
- 00890064 ["CALLIND", null, ["register:0:8"]]
+ 008900bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008900bc ["INT_ADD", "register:40f0:8", ["const:8900bc:8", "const:4:8"]]
+ 008900bc ["CALLIND", null, ["register:0:8"]]
- 00890064 bytes 00013fd6
+ 008900bc bytes 00013fd6
~~~


<a id="compare-fa66152be8cdca2d9f5941bd45726fe2"></a>

### [`008901b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md) → [`0089020c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089020c.md) FUN_0089020c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0088fdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008901d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md#insn-008901d0) · [`008901f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md#insn-008901f0)
- 新版 `00890228`（命令位置の公開資料なし） · `00890248`（命令位置の公開資料なし）

~~~diff
- 008901d0 ["INT_ADD", "register:40f0:8", ["const:8901d0:8", "const:4:8"]]
- 008901d0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00890228 ["INT_ADD", "register:40f0:8", ["const:890228:8", "const:4:8"]]
+ 00890228 ["CALL", null, ["callee:00c53da0:8"]]
- 008901d0 bytes cc0e0f94
+ 00890228 bytes de0e0f94
- 008901f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008901f0 ["INT_ADD", "register:40f0:8", ["const:8901f0:8", "const:4:8"]]
- 008901f0 ["CALLIND", null, ["register:0:8"]]
+ 00890248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890248 ["INT_ADD", "register:40f0:8", ["const:890248:8", "const:4:8"]]
+ 00890248 ["CALLIND", null, ["register:0:8"]]
- 008901f0 bytes 00013fd6
+ 00890248 bytes 00013fd6
~~~


<a id="compare-409c1548d5719c4012ba7d5745888c20"></a>

### [`00890204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md) → [`0089025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089025c.md) FUN_0089025c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0088fdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md#insn-00890224) · [`00890238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md#insn-00890238) · [`00890240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md#insn-00890240)
- 新版 `0089027c`（命令位置の公開資料なし） · `00890290`（命令位置の公開資料なし） · `00890298`（命令位置の公開資料なし）

~~~diff
- 00890224 ["INT_ADD", "register:40f0:8", ["const:890224:8", "const:4:8"]]
- 00890224 ["CALL", null, ["callee:00c53da0:8"]]
+ 0089027c ["INT_ADD", "register:40f0:8", ["const:89027c:8", "const:4:8"]]
+ 0089027c ["CALL", null, ["callee:00c53da0:8"]]
- 00890224 bytes b70e0f94
+ 0089027c bytes c90e0f94
- 00890238 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890238 ["INT_ADD", "register:40f0:8", ["const:890238:8", "const:4:8"]]
- 00890238 ["CALLIND", null, ["register:0:8"]]
+ 00890290 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890290 ["INT_ADD", "register:40f0:8", ["const:890290:8", "const:4:8"]]
+ 00890290 ["CALLIND", null, ["register:0:8"]]
- 00890238 bytes 00013fd6
+ 00890290 bytes 00013fd6
- 00890240 ["INT_ADD", "register:40f0:8", ["const:890240:8", "const:4:8"]]
- 00890240 ["CALL", null, ["callee:00c57f50:8"]]
+ 00890298 ["INT_ADD", "register:40f0:8", ["const:890298:8", "const:4:8"]]
+ 00890298 ["CALL", null, ["callee:00c57f50:8"]]
- 00890240 bytes 101f0f94
+ 00890298 bytes 2e1f0f94
~~~


<a id="compare-c05ac47fe2148f9e1ca587101ec87bf0"></a>

### [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) → [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) FUN_00890668

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) [`00891dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891dc8.md) · 呼出先 3件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 2件 [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) [`00891e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md) · 呼出先 3件 [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md#insn-00890648) · [`0089066c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md#insn-0089066c) · [`00890690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md#insn-00890690)
- 新版 `008906a0`（命令位置の公開資料なし） · `008906c4`（命令位置の公開資料なし） · `008906e8`（命令位置の公開資料なし）

~~~diff
- 00890648 ["INT_ADD", "register:40f0:8", ["const:890648:8", "const:4:8"]]
- 00890648 ["CALL", null, ["callee:00c58500:8"]]
+ 008906a0 ["INT_ADD", "register:40f0:8", ["const:8906a0:8", "const:4:8"]]
+ 008906a0 ["CALL", null, ["callee:00c58500:8"]]
- 00890648 bytes 7a1f0f94
+ 008906a0 bytes 981f0f94
- 0089066c ["COPY", "register:0:8", ["register:4040:8"]]
- 0089066c ["INT_ADD", "register:40f0:8", ["const:89066c:8", "const:4:8"]]
- 0089066c ["CALLIND", null, ["register:0:8"]]
+ 008906c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008906c4 ["INT_ADD", "register:40f0:8", ["const:8906c4:8", "const:4:8"]]
+ 008906c4 ["CALLIND", null, ["register:0:8"]]
- 0089066c bytes 00013fd6
+ 008906c4 bytes 00013fd6
- 00890690 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890690 ["INT_ADD", "register:40f0:8", ["const:890690:8", "const:4:8"]]
- 00890690 ["CALLIND", null, ["register:0:8"]]
+ 008906e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008906e8 ["INT_ADD", "register:40f0:8", ["const:8906e8:8", "const:4:8"]]
+ 008906e8 ["CALLIND", null, ["register:0:8"]]
- 00890690 bytes 00013fd6
+ 008906e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-305be5926bab30505fba0f2c0c272b15"></a>

### [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) → [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) FUN_00890c28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md#insn-00890bfc) · [`00890c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md#insn-00890c28) · [`00890c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md#insn-00890c40)
- 新版 `00890c54`（命令位置の公開資料なし） · `00890c80`（命令位置の公開資料なし） · `00890c98`（命令位置の公開資料なし）

~~~diff
- 00890bfc ["INT_ADD", "register:40f0:8", ["const:890bfc:8", "const:4:8"]]
- 00890bfc ["CALL", null, ["callee:00c57f60:8"]]
+ 00890c54 ["INT_ADD", "register:40f0:8", ["const:890c54:8", "const:4:8"]]
+ 00890c54 ["CALL", null, ["callee:00c57f60:8"]]
- 00890bfc bytes a51c0f94
+ 00890c54 bytes c31c0f94
- 00890c28 ["INT_ADD", "register:40f0:8", ["const:890c28:8", "const:4:8"]]
- 00890c28 ["CALL", null, ["callee:0043bb60:8"]]
+ 00890c80 ["INT_ADD", "register:40f0:8", ["const:890c80:8", "const:4:8"]]
+ 00890c80 ["CALL", null, ["callee:0043bb60:8"]]
- 00890c28 bytes beabee97
+ 00890c80 bytes b8abee97
- 00890c40 ["INT_ADD", "register:40f0:8", ["const:890c40:8", "const:4:8"]]
- 00890c40 ["CALL", null, ["callee:00890668:8"]]
+ 00890c98 ["INT_ADD", "register:40f0:8", ["const:890c98:8", "const:4:8"]]
+ 00890c98 ["CALL", null, ["callee:00890668:8"]]
- 00890c40 bytes 74feff97
+ 00890c98 bytes 74feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac67079e7b2db4ba268df5a0b76b4294"></a>

### [`00890d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d18.md) → [`00890d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890d70.md) FUN_00890d70

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d18.md#insn-00890d68) · [`00890d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d18.md#insn-00890d78)
- 新版 `00890dc0`（命令位置の公開資料なし） · `00890dd0`（命令位置の公開資料なし）

~~~diff
- 00890d68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890d68 ["INT_ADD", "register:40f0:8", ["const:890d68:8", "const:4:8"]]
- 00890d68 ["CALLIND", null, ["register:0:8"]]
+ 00890dc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890dc0 ["INT_ADD", "register:40f0:8", ["const:890dc0:8", "const:4:8"]]
+ 00890dc0 ["CALLIND", null, ["register:0:8"]]
- 00890d68 bytes 00013fd6
+ 00890dc0 bytes 00013fd6
- 00890d78 ["INT_ADD", "register:40f0:8", ["const:890d78:8", "const:4:8"]]
- 00890d78 ["CALL", null, ["callee:00c57f80:8"]]
+ 00890dd0 ["INT_ADD", "register:40f0:8", ["const:890dd0:8", "const:4:8"]]
+ 00890dd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00890d78 bytes 4e1c0f94
+ 00890dd0 bytes 6c1c0f94
~~~


<a id="compare-ab5971a60147a680a91ba23094c33951"></a>

### [`00890d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md) → [`00890de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md) FUN_00890de4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890e2c) · [`00890e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890e3c) · [`00890e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890e4c)
- 新版 `00890e84`（命令位置の公開資料なし） · `00890e94`（命令位置の公開資料なし） · `00890ea4`（命令位置の公開資料なし）

~~~diff
- 00890e2c ["INT_ADD", "register:40f0:8", ["const:890e2c:8", "const:4:8"]]
- 00890e2c ["CALL", null, ["callee:00c57f80:8"]]
+ 00890e84 ["INT_ADD", "register:40f0:8", ["const:890e84:8", "const:4:8"]]
+ 00890e84 ["CALL", null, ["callee:00c57f80:8"]]
- 00890e2c bytes 211c0f94
+ 00890e84 bytes 3f1c0f94
- 00890e3c ["INT_ADD", "register:40f0:8", ["const:890e3c:8", "const:4:8"]]
- 00890e3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00890e94 ["INT_ADD", "register:40f0:8", ["const:890e94:8", "const:4:8"]]
+ 00890e94 ["CALL", null, ["callee:00c57f80:8"]]
- 00890e3c bytes 1d1c0f94
+ 00890e94 bytes 3b1c0f94
- 00890e4c ["INT_ADD", "register:40f0:8", ["const:890e4c:8", "const:4:8"]]
- 00890e4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00890ea4 ["INT_ADD", "register:40f0:8", ["const:890ea4:8", "const:4:8"]]
+ 00890ea4 ["CALL", null, ["callee:00c57f80:8"]]
- 00890e4c bytes 191c0f94
+ 00890ea4 bytes 371c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-676b31399312881eb6dbad2e815525d4"></a>

### [`00890f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890f28.md) → [`00890f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890f80.md) FUN_00890f80

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890f28.md#insn-00890f5c) · [`00890fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890f28.md#insn-00890fa0) · [`00890fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890f28.md#insn-00890fb0)
- 新版 `00890fb4`（命令位置の公開資料なし） · `00890ff8`（命令位置の公開資料なし） · `00891008`（命令位置の公開資料なし）

~~~diff
- 00890f5c ["INT_ADD", "register:40f0:8", ["const:890f5c:8", "const:4:8"]]
- 00890f5c ["CALL", null, ["callee:00c57f80:8"]]
+ 00890fb4 ["INT_ADD", "register:40f0:8", ["const:890fb4:8", "const:4:8"]]
+ 00890fb4 ["CALL", null, ["callee:00c57f80:8"]]
- 00890f5c bytes d51b0f94
+ 00890fb4 bytes f31b0f94
- 00890fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890fa0 ["INT_ADD", "register:40f0:8", ["const:890fa0:8", "const:4:8"]]
- 00890fa0 ["CALLIND", null, ["register:0:8"]]
+ 00890ff8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890ff8 ["INT_ADD", "register:40f0:8", ["const:890ff8:8", "const:4:8"]]
+ 00890ff8 ["CALLIND", null, ["register:0:8"]]
- 00890fa0 bytes 00013fd6
+ 00890ff8 bytes 00013fd6
- 00890fb0 ["INT_ADD", "register:40f0:8", ["const:890fb0:8", "const:4:8"]]
- 00890fb0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00891008 ["INT_ADD", "register:40f0:8", ["const:891008:8", "const:4:8"]]
+ 00891008 ["CALL", null, ["callee:00c57f80:8"]]
- 00890fb0 bytes c01b0f94
+ 00891008 bytes de1b0f94
~~~


