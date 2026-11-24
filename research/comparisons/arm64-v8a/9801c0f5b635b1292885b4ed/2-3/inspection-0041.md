# v16.0.1 → v16.0.2 · 要調査の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-c1df8998ae745d8db694b7c6e044d9a5"></a>

### [`00bf49c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf49c0.md) → [`00bf4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4a5c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf49c0.md#insn-00bf4a44)
- 新版 `00bf4ae0`（命令位置の公開資料なし）

~~~diff
- 00bf4a44 ["INT_ADD", "register:40f0:8", ["const:bf4a44:8", "const:4:8"]]
- 00bf4a44 ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf4ae0 ["INT_ADD", "register:40f0:8", ["const:bf4ae0:8", "const:4:8"]]
+ 00bf4ae0 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf4a44 bytes 97970194
+ 00bf4ae0 bytes a4970194
~~~


<a id="compare-6a1b55a67e6284cdc9c703e4a95df668"></a>

### [`00bf4b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md) → [`00bf4bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4bbc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md#insn-00bf4b6c)
- 新版 `00bf4c08`（命令位置の公開資料なし）

~~~diff
- 00bf4b6c ["INT_ADD", "register:40f0:8", ["const:bf4b6c:8", "const:4:8"]]
- 00bf4b6c ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf4c08 ["INT_ADD", "register:40f0:8", ["const:bf4c08:8", "const:4:8"]]
+ 00bf4c08 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf4b6c bytes 5bf7ff97
+ 00bf4c08 bytes 5bf7ff97
~~~


<a id="compare-fb765b3c8d9b4a145a787212fc617a7e"></a>

### [`00bf66c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md) → [`00bf6764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6764.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00bf8258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8258.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00bf82f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf82f4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf66f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf66f0) · [`00bf6734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf6734) · [`00bf6760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf6760)
- 新版 `00bf678c`（命令位置の公開資料なし） · `00bf67d0`（命令位置の公開資料なし） · `00bf67fc`（命令位置の公開資料なし）

~~~diff
- 00bf66f0 ["INT_ADD", "register:40f0:8", ["const:bf66f0:8", "const:4:8"]]
- 00bf66f0 ["CALL", null, ["callee:00bf82f4:8"]]
+ 00bf678c ["INT_ADD", "register:40f0:8", ["const:bf678c:8", "const:4:8"]]
+ 00bf678c ["CALL", null, ["callee:00bf82f4:8"]]
- 00bf66f0 bytes da060094
+ 00bf678c bytes da060094
- 00bf6734 ["INT_ADD", "register:40f0:8", ["const:bf6734:8", "const:4:8"]]
- 00bf6734 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf67d0 ["INT_ADD", "register:40f0:8", ["const:bf67d0:8", "const:4:8"]]
+ 00bf67d0 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf6734 bytes d7850194
+ 00bf67d0 bytes e4850194
- 00bf6760 ["INT_ADD", "register:40f0:8", ["const:bf6760:8", "const:4:8"]]
- 00bf6760 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf67fc ["INT_ADD", "register:40f0:8", ["const:bf67fc:8", "const:4:8"]]
+ 00bf67fc ["CALL", null, ["callee:00c580d0:8"]]
- 00bf6760 bytes 28860194
+ 00bf67fc bytes 35860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715c0c0bc5975058da34ddb260076f81"></a>

### [`00bf903c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf903c.md) → [`00bf90d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d8.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf903c.md#insn-00bf9050)
- 新版 `00bf90ec`（命令位置の公開資料なし）

~~~diff
- 00bf9050 ["INT_ADD", "register:40f0:8", ["const:bf9050:8", "const:4:8"]]
- 00bf9050 ["CALL", null, ["callee:00c5e250:8"]]
+ 00bf90ec ["INT_ADD", "register:40f0:8", ["const:bf90ec:8", "const:4:8"]]
+ 00bf90ec ["CALL", null, ["callee:00c5e250:8"]]
- 00bf9050 bytes 4c940194
+ 00bf90ec bytes 59940194
~~~


<a id="compare-5078c49435140930c2172a025c8b89bd"></a>

### [`00bf90f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf90f0.md) → [`00bf918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf918c.md) FUN_00bf918c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf90f0.md#insn-00bf9104)
- 新版 `00bf91a0`（命令位置の公開資料なし）

~~~diff
- 00bf9104 ["INT_ADD", "register:40f0:8", ["const:bf9104:8", "const:4:8"]]
- 00bf9104 ["CALL", null, ["callee:00c5dfc0:8"]]
+ 00bf91a0 ["INT_ADD", "register:40f0:8", ["const:bf91a0:8", "const:4:8"]]
+ 00bf91a0 ["CALL", null, ["callee:00c5dfc0:8"]]
- 00bf9104 bytes 7b930194
+ 00bf91a0 bytes 88930194
~~~


<a id="compare-2ecb8ac81303ef3edf7e09ccaff1e33b"></a>

### [`00bf911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf911c.md) → [`00bf91b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf91b8.md) FUN_00bf91b8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf911c.md#insn-00bf9130)
- 新版 `00bf91cc`（命令位置の公開資料なし）

~~~diff
- 00bf9130 ["INT_ADD", "register:40f0:8", ["const:bf9130:8", "const:4:8"]]
- 00bf9130 ["CALL", null, ["callee:00c5dfc0:8"]]
+ 00bf91cc ["INT_ADD", "register:40f0:8", ["const:bf91cc:8", "const:4:8"]]
+ 00bf91cc ["CALL", null, ["callee:00c5dfc0:8"]]
- 00bf9130 bytes 70930194
+ 00bf91cc bytes 7d930194
~~~


<a id="compare-d1d3aad7e52c2c714507a6561eb17991"></a>

### [`00bf9184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9184.md) → [`00bf9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9220.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf91a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9184.md#insn-00bf91a0)
- 新版 `00bf923c`（命令位置の公開資料なし）

~~~diff
- 00bf91a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf91a0 ["INT_ADD", "register:40f0:8", ["const:bf91a0:8", "const:4:8"]]
- 00bf91a0 ["CALLIND", null, ["register:0:8"]]
+ 00bf923c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf923c ["INT_ADD", "register:40f0:8", ["const:bf923c:8", "const:4:8"]]
+ 00bf923c ["CALLIND", null, ["register:0:8"]]
- 00bf91a0 bytes 00013fd6
+ 00bf923c bytes 00013fd6
~~~


<a id="compare-9e57fe3854631fa8501bbc4d508716c5"></a>

### [`00bf91e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf91e4.md) → [`00bf9280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9280.md) _ZNSt6__ndk118condition_variableD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) · 呼出先 1件 [`00c5d620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d620.md)
- 新版 呼出元 1件 [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) · 呼出先 1件 [`00c5d6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf91f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf91e4.md#insn-00bf91f0)
- 新版 `00bf928c`（命令位置の公開資料なし）

~~~diff
- 00bf91f0 ["INT_ADD", "register:40f0:8", ["const:bf91f0:8", "const:4:8"]]
- 00bf91f0 ["CALL", null, ["callee:00c5d6f0:8"]]
+ 00bf928c ["INT_ADD", "register:40f0:8", ["const:bf928c:8", "const:4:8"]]
+ 00bf928c ["CALL", null, ["callee:00c5d6f0:8"]]
- 00bf91f0 bytes 0c910194
+ 00bf928c bytes 19910194
~~~


<a id="compare-53089a9917ffcf5fbaac4fb76f1edc7f"></a>

### [`00bf9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9204.md) → [`00bf92a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92a0.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) · 呼出先 1件 [`00c5d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d630.md)
- 新版 呼出元 1件 [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) · 呼出先 1件 [`00c5d700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9204.md#insn-00bf9210)
- 新版 `00bf92ac`（命令位置の公開資料なし）

~~~diff
- 00bf9210 ["INT_ADD", "register:40f0:8", ["const:bf9210:8", "const:4:8"]]
- 00bf9210 ["CALL", null, ["callee:00c5d700:8"]]
+ 00bf92ac ["INT_ADD", "register:40f0:8", ["const:bf92ac:8", "const:4:8"]]
+ 00bf92ac ["CALL", null, ["callee:00c5d700:8"]]
- 00bf9210 bytes 08910194
+ 00bf92ac bytes 15910194
~~~


<a id="compare-eb17fc33f86bb97a5482c63463814d9e"></a>

### [`00bf9224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9224.md) → [`00bf92c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92c0.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) · 呼出先 1件 [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)
- 新版 呼出元 1件 [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) · 呼出先 1件 [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9224.md#insn-00bf9230)
- 新版 `00bf92cc`（命令位置の公開資料なし）

~~~diff
- 00bf9230 ["INT_ADD", "register:40f0:8", ["const:bf9230:8", "const:4:8"]]
- 00bf9230 ["CALL", null, ["callee:00c5e290:8"]]
+ 00bf92cc ["INT_ADD", "register:40f0:8", ["const:bf92cc:8", "const:4:8"]]
+ 00bf92cc ["CALL", null, ["callee:00c5e290:8"]]
- 00bf9230 bytes e4930194
+ 00bf92cc bytes f1930194
~~~


<a id="compare-2a9172562b51e8cacd8ac4a04ecd2ef6"></a>

### [`00bf9330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md) → [`00bf93cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf93cc.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5e1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5e2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf934c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf934c) · [`00bf9358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf9358) · [`00bf9364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf9364)
- 新版 `00bf93e8`（命令位置の公開資料なし） · `00bf93f4`（命令位置の公開資料なし） · `00bf9400`（命令位置の公開資料なし）

~~~diff
- 00bf934c ["INT_ADD", "register:40f0:8", ["const:bf934c:8", "const:4:8"]]
- 00bf934c ["CALL", null, ["callee:00c58200:8"]]
+ 00bf93e8 ["INT_ADD", "register:40f0:8", ["const:bf93e8:8", "const:4:8"]]
+ 00bf93e8 ["CALL", null, ["callee:00c58200:8"]]
- 00bf934c bytes 797b0194
+ 00bf93e8 bytes 867b0194
- 00bf9358 ["INT_ADD", "register:40f0:8", ["const:bf9358:8", "const:4:8"]]
- 00bf9358 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00bf93f4 ["INT_ADD", "register:40f0:8", ["const:bf93f4:8", "const:4:8"]]
+ 00bf93f4 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00bf9358 bytes a6930194
+ 00bf93f4 bytes b3930194
- 00bf9364 ["INT_ADD", "register:40f0:8", ["const:bf9364:8", "const:4:8"]]
- 00bf9364 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf9400 ["INT_ADD", "register:40f0:8", ["const:bf9400:8", "const:4:8"]]
+ 00bf9400 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf9364 bytes cb7a0194
+ 00bf9400 bytes d87a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed71c2bf9eee0990225b4642ce25360"></a>

### [`00bf9640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9640.md) → [`00bf96dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf96dc.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58440.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9640.md#insn-00bf9654)
- 新版 `00bf96f0`（命令位置の公開資料なし）

~~~diff
- 00bf9654 ["INT_ADD", "register:40f0:8", ["const:bf9654:8", "const:4:8"]]
- 00bf9654 ["CALL", null, ["callee:00c58440:8"]]
+ 00bf96f0 ["INT_ADD", "register:40f0:8", ["const:bf96f0:8", "const:4:8"]]
+ 00bf96f0 ["CALL", null, ["callee:00c58440:8"]]
- 00bf9654 bytes 477b0194
+ 00bf96f0 bytes 547b0194
~~~


<a id="compare-5342cd89a1fa2b884aadbd76c22246c0"></a>

### [`00bf967c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md) → [`00bf9718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9718.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md) · 呼出先 5件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c58620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58620.md) · 呼出先 5件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf9698) · [`00bf96b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf96b0) · [`00bf96cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf96cc)
- 新版 `00bf9734`（命令位置の公開資料なし） · `00bf974c`（命令位置の公開資料なし） · `00bf9768`（命令位置の公開資料なし）

~~~diff
- 00bf9698 ["INT_ADD", "register:40f0:8", ["const:bf9698:8", "const:4:8"]]
- 00bf9698 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf9734 ["INT_ADD", "register:40f0:8", ["const:bf9734:8", "const:4:8"]]
+ 00bf9734 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9698 bytes 927a0194
+ 00bf9734 bytes 9f7a0194
- 00bf96b0 ["INT_ADD", "register:40f0:8", ["const:bf96b0:8", "const:4:8"]]
- 00bf96b0 ["CALL", null, ["callee:00c583c0:8"]]
+ 00bf974c ["INT_ADD", "register:40f0:8", ["const:bf974c:8", "const:4:8"]]
+ 00bf974c ["CALL", null, ["callee:00c583c0:8"]]
- 00bf96b0 bytes 107b0194
+ 00bf974c bytes 1d7b0194
- 00bf96cc ["INT_ADD", "register:40f0:8", ["const:bf96cc:8", "const:4:8"]]
- 00bf96cc ["CALL", null, ["callee:00c58450:8"]]
+ 00bf9768 ["INT_ADD", "register:40f0:8", ["const:bf9768:8", "const:4:8"]]
+ 00bf9768 ["CALL", null, ["callee:00c58450:8"]]
- 00bf96cc bytes 2d7b0194
+ 00bf9768 bytes 3a7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58e3cfea5e610efec48189d890683a7"></a>

### [`00bf9708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md) → [`00bf97a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf97a4.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e220.md) · 呼出先 7件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`00c5e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2f0.md) · 呼出先 7件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf9724) · [`00bf973c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf973c) · [`00bf9750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf9750)
- 新版 `00bf97c0`（命令位置の公開資料なし） · `00bf97d8`（命令位置の公開資料なし） · `00bf97ec`（命令位置の公開資料なし）

~~~diff
- 00bf9724 ["INT_ADD", "register:40f0:8", ["const:bf9724:8", "const:4:8"]]
- 00bf9724 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf97c0 ["INT_ADD", "register:40f0:8", ["const:bf97c0:8", "const:4:8"]]
+ 00bf97c0 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9724 bytes 6f7a0194
+ 00bf97c0 bytes 7c7a0194
- 00bf973c ["INT_ADD", "register:40f0:8", ["const:bf973c:8", "const:4:8"]]
- 00bf973c ["CALL", null, ["callee:00c583c0:8"]]
+ 00bf97d8 ["INT_ADD", "register:40f0:8", ["const:bf97d8:8", "const:4:8"]]
+ 00bf97d8 ["CALL", null, ["callee:00c583c0:8"]]
- 00bf973c bytes ed7a0194
+ 00bf97d8 bytes fa7a0194
- 00bf9750 ["INT_ADD", "register:40f0:8", ["const:bf9750:8", "const:4:8"]]
- 00bf9750 ["CALL", null, ["callee:00c58200:8"]]
+ 00bf97ec ["INT_ADD", "register:40f0:8", ["const:bf97ec:8", "const:4:8"]]
+ 00bf97ec ["CALL", null, ["callee:00c58200:8"]]
- 00bf9750 bytes 787a0194
+ 00bf97ec bytes 857a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c3a182b4293c3913e1e94181faf8dbb"></a>

### [`00bf979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md) → [`00bf9838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9838.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58360.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c58430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58430.md) · 呼出先 6件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf97c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97c0) · [`00bf97dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97dc) · [`00bf97ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97ec)
- 新版 `00bf985c`（命令位置の公開資料なし） · `00bf9878`（命令位置の公開資料なし） · `00bf9888`（命令位置の公開資料なし）

~~~diff
- 00bf97c0 ["INT_ADD", "register:40f0:8", ["const:bf97c0:8", "const:4:8"]]
- 00bf97c0 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf985c ["INT_ADD", "register:40f0:8", ["const:bf985c:8", "const:4:8"]]
+ 00bf985c ["CALL", null, ["callee:00c581b0:8"]]
- 00bf97c0 bytes 487a0194
+ 00bf985c bytes 557a0194
- 00bf97dc ["INT_ADD", "register:40f0:8", ["const:bf97dc:8", "const:4:8"]]
- 00bf97dc ["CALL", null, ["callee:00c583c0:8"]]
+ 00bf9878 ["INT_ADD", "register:40f0:8", ["const:bf9878:8", "const:4:8"]]
+ 00bf9878 ["CALL", null, ["callee:00c583c0:8"]]
- 00bf97dc bytes c57a0194
+ 00bf9878 bytes d27a0194
- 00bf97ec ["INT_ADD", "register:40f0:8", ["const:bf97ec:8", "const:4:8"]]
- 00bf97ec ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf9888 ["INT_ADD", "register:40f0:8", ["const:bf9888:8", "const:4:8"]]
+ 00bf9888 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf97ec bytes d1910194
+ 00bf9888 bytes de910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580b1fa2493b81d6ad6b68eebfaced80"></a>

### [`00bf9840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md) → [`00bf98dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf98dc.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e240.md) · 呼出先 8件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`00c5e310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e310.md) · 呼出先 8件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9864) · [`00bf9880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9880) · [`00bf9890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9890)
- 新版 `00bf9900`（命令位置の公開資料なし） · `00bf991c`（命令位置の公開資料なし） · `00bf992c`（命令位置の公開資料なし）

~~~diff
- 00bf9864 ["INT_ADD", "register:40f0:8", ["const:bf9864:8", "const:4:8"]]
- 00bf9864 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf9900 ["INT_ADD", "register:40f0:8", ["const:bf9900:8", "const:4:8"]]
+ 00bf9900 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9864 bytes 1f7a0194
+ 00bf9900 bytes 2c7a0194
- 00bf9880 ["INT_ADD", "register:40f0:8", ["const:bf9880:8", "const:4:8"]]
- 00bf9880 ["CALL", null, ["callee:00c583c0:8"]]
+ 00bf991c ["INT_ADD", "register:40f0:8", ["const:bf991c:8", "const:4:8"]]
+ 00bf991c ["CALL", null, ["callee:00c583c0:8"]]
- 00bf9880 bytes 9c7a0194
+ 00bf991c bytes a97a0194
- 00bf9890 ["INT_ADD", "register:40f0:8", ["const:bf9890:8", "const:4:8"]]
- 00bf9890 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf992c ["INT_ADD", "register:40f0:8", ["const:bf992c:8", "const:4:8"]]
+ 00bf992c ["CALL", null, ["callee:00c5e000:8"]]
- 00bf9890 bytes a8910194
+ 00bf992c bytes b5910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72a9f08d26e71e16b5f006996aa4ecbf"></a>

### [`00bf98e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md) → [`00bf9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9980.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e250.md) · 呼出先 3件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e320.md) · 呼出先 3件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md#insn-00bf98fc) · [`00bf9910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md#insn-00bf9910)
- 新版 `00bf9998`（命令位置の公開資料なし） · `00bf99ac`（命令位置の公開資料なし）

~~~diff
- 00bf98fc ["INT_ADD", "register:40f0:8", ["const:bf98fc:8", "const:4:8"]]
- 00bf98fc ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf9998 ["INT_ADD", "register:40f0:8", ["const:bf9998:8", "const:4:8"]]
+ 00bf9998 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf98fc bytes f9790194
+ 00bf9998 bytes 067a0194
- 00bf9910 ["INT_ADD", "register:40f0:8", ["const:bf9910:8", "const:4:8"]]
- 00bf9910 ["CALL", null, ["callee:00c58450:8"]]
+ 00bf99ac ["INT_ADD", "register:40f0:8", ["const:bf99ac:8", "const:4:8"]]
+ 00bf99ac ["CALL", null, ["callee:00c58450:8"]]
- 00bf9910 bytes 9c7a0194
+ 00bf99ac bytes a97a0194
~~~


<a id="compare-3b528f41b70bdfa32ca51717170e9647"></a>

### [`00bf9928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md) → [`00bf99c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf99c4.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e260.md) · 呼出先 7件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`00c5e330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e330.md) · 呼出先 7件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf9954) · [`00bf996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf996c) · [`00bf9988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf9988)
- 新版 `00bf99f0`（命令位置の公開資料なし） · `00bf9a08`（命令位置の公開資料なし） · `00bf9a24`（命令位置の公開資料なし）

~~~diff
- 00bf9954 ["INT_ADD", "register:40f0:8", ["const:bf9954:8", "const:4:8"]]
- 00bf9954 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf99f0 ["INT_ADD", "register:40f0:8", ["const:bf99f0:8", "const:4:8"]]
+ 00bf99f0 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9954 bytes e3790194
+ 00bf99f0 bytes f0790194
- 00bf996c ["INT_ADD", "register:40f0:8", ["const:bf996c:8", "const:4:8"]]
- 00bf996c ["CALL", null, ["callee:00c58550:8"]]
+ 00bf9a08 ["INT_ADD", "register:40f0:8", ["const:bf9a08:8", "const:4:8"]]
+ 00bf9a08 ["CALL", null, ["callee:00c58550:8"]]
- 00bf996c bytes c57a0194
+ 00bf9a08 bytes d27a0194
- 00bf9988 ["INT_ADD", "register:40f0:8", ["const:bf9988:8", "const:4:8"]]
- 00bf9988 ["CALL", null, ["callee:00c581c0:8"]]
+ 00bf9a24 ["INT_ADD", "register:40f0:8", ["const:bf9a24:8", "const:4:8"]]
+ 00bf9a24 ["CALL", null, ["callee:00c581c0:8"]]
- 00bf9988 bytes da790194
+ 00bf9a24 bytes e7790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-720e2ee3264c1b80dcb2218c37ef44ce"></a>

### [`00bf9aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md) → [`00bf9b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9b3c.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58530.md) · 呼出先 3件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`00c58600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58600.md) · 呼出先 3件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9acc) · [`00bf9ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9ae4) · [`00bf9afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9afc)
- 新版 `00bf9b68`（命令位置の公開資料なし） · `00bf9b80`（命令位置の公開資料なし） · `00bf9b98`（命令位置の公開資料なし）

~~~diff
- 00bf9acc ["INT_ADD", "register:40f0:8", ["const:bf9acc:8", "const:4:8"]]
- 00bf9acc ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf9b68 ["INT_ADD", "register:40f0:8", ["const:bf9b68:8", "const:4:8"]]
+ 00bf9b68 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9acc bytes 85790194
+ 00bf9b68 bytes 92790194
- 00bf9ae4 ["INT_ADD", "register:40f0:8", ["const:bf9ae4:8", "const:4:8"]]
- 00bf9ae4 ["CALL", null, ["callee:00c58550:8"]]
+ 00bf9b80 ["INT_ADD", "register:40f0:8", ["const:bf9b80:8", "const:4:8"]]
+ 00bf9b80 ["CALL", null, ["callee:00c58550:8"]]
- 00bf9ae4 bytes 677a0194
+ 00bf9b80 bytes 747a0194
- 00bf9afc ["INT_ADD", "register:40f0:8", ["const:bf9afc:8", "const:4:8"]]
- 00bf9afc ["CALL", null, ["callee:00c581c0:8"]]
+ 00bf9b98 ["INT_ADD", "register:40f0:8", ["const:bf9b98:8", "const:4:8"]]
+ 00bf9b98 ["CALL", null, ["callee:00c581c0:8"]]
- 00bf9afc bytes 7d790194
+ 00bf9b98 bytes 8a790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69d018f9c8051ab0bf436dc7680b2c2"></a>

### [`00bf9b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b44.md) → [`00bf9be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9be0.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b44.md#insn-00bf9b54)
- 新版 `00bf9bf0`（命令位置の公開資料なし）

~~~diff
- 00bf9b54 ["INT_ADD", "register:40f0:8", ["const:bf9b54:8", "const:4:8"]]
- 00bf9b54 ["CALL", null, ["callee:0045a714:8"]]
+ 00bf9bf0 ["INT_ADD", "register:40f0:8", ["const:bf9bf0:8", "const:4:8"]]
+ 00bf9bf0 ["CALL", null, ["callee:0045a714:8"]]
- 00bf9b54 bytes e082e197
+ 00bf9bf0 bytes c982e197
~~~


<a id="compare-ebc2ac804caba53fdf2742643dcb1d76"></a>

### [`00bf9b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md) → [`00bf9bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md) _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58520.md) · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c585f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585f0.md) · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9b74) · [`00bf9b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9b88) · [`00bf9bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9bac)
- 新版 `00bf9c10`（命令位置の公開資料なし） · `00bf9c24`（命令位置の公開資料なし） · `00bf9c48`（命令位置の公開資料なし）

~~~diff
- 00bf9b74 ["INT_ADD", "register:40f0:8", ["const:bf9b74:8", "const:4:8"]]
- 00bf9b74 ["CALL", null, ["callee:00c581b0:8"]]
+ 00bf9c10 ["INT_ADD", "register:40f0:8", ["const:bf9c10:8", "const:4:8"]]
+ 00bf9c10 ["CALL", null, ["callee:00c581b0:8"]]
- 00bf9b74 bytes 5b790194
+ 00bf9c10 bytes 68790194
- 00bf9b88 ["INT_ADD", "register:40f0:8", ["const:bf9b88:8", "const:4:8"]]
- 00bf9b88 ["CALL", null, ["callee:00c53d70:8"]]
+ 00bf9c24 ["INT_ADD", "register:40f0:8", ["const:bf9c24:8", "const:4:8"]]
+ 00bf9c24 ["CALL", null, ["callee:00c53d70:8"]]
- 00bf9b88 bytes 52680194
+ 00bf9c24 bytes 53680194
- 00bf9bac ["INT_ADD", "register:40f0:8", ["const:bf9bac:8", "const:4:8"]]
- 00bf9bac ["CALL", null, ["callee:0045a714:8"]]
+ 00bf9c48 ["INT_ADD", "register:40f0:8", ["const:bf9c48:8", "const:4:8"]]
+ 00bf9c48 ["CALL", null, ["callee:0045a714:8"]]
- 00bf9bac bytes ca82e197
+ 00bf9c48 bytes b382e197
~~~


<a id="compare-cc8b3d4fb7ae34bba46348cc196b490e"></a>

### [`00bf9bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9bc4.md) → [`00bf9c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9c60.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9bc4.md#insn-00bf9be4)
- 新版 `00bf9c80`（命令位置の公開資料なし）

~~~diff
- 00bf9be4 ["INT_ADD", "register:40f0:8", ["const:bf9be4:8", "const:4:8"]]
- 00bf9be4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf9c80 ["INT_ADD", "register:40f0:8", ["const:bf9c80:8", "const:4:8"]]
+ 00bf9c80 ["CALL", null, ["callee:00c53da0:8"]]
- 00bf9be4 bytes 47680194
+ 00bf9c80 bytes 48680194
~~~


<a id="compare-fa382769a7707b13b4d7b8d388da5e7c"></a>

### [`00bf9c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md) → [`00bf9cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9cb4.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5e330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md#insn-00bf9c34) · [`00bf9c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md#insn-00bf9c40)
- 新版 `00bf9cd0`（命令位置の公開資料なし） · `00bf9cdc`（命令位置の公開資料なし）

~~~diff
- 00bf9c34 ["INT_ADD", "register:40f0:8", ["const:bf9c34:8", "const:4:8"]]
- 00bf9c34 ["CALL", null, ["callee:00c5e330:8"]]
+ 00bf9cd0 ["INT_ADD", "register:40f0:8", ["const:bf9cd0:8", "const:4:8"]]
+ 00bf9cd0 ["CALL", null, ["callee:00c5e330:8"]]
- 00bf9c34 bytes 8b910194
+ 00bf9cd0 bytes 98910194
- 00bf9c40 ["INT_ADD", "register:40f0:8", ["const:bf9c40:8", "const:4:8"]]
- 00bf9c40 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf9cdc ["INT_ADD", "register:40f0:8", ["const:bf9cdc:8", "const:4:8"]]
+ 00bf9cdc ["CALL", null, ["callee:00c53da0:8"]]
- 00bf9c40 bytes 30680194
+ 00bf9cdc bytes 31680194
~~~


<a id="compare-f9565cc95fccc0d425810ca51da8aac0"></a>

### [`00bf9e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9e8c.md) → [`00bf9f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f28.md) _ZNSt6__ndk17promiseIvE10get_futureEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c58520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c585f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9e8c.md#insn-00bf9eb0)
- 新版 `00bf9f4c`（命令位置の公開資料なし）

~~~diff
- 00bf9eb0 ["INT_ADD", "register:40f0:8", ["const:bf9eb0:8", "const:4:8"]]
- 00bf9eb0 ["CALL", null, ["callee:0045a714:8"]]
+ 00bf9f4c ["INT_ADD", "register:40f0:8", ["const:bf9f4c:8", "const:4:8"]]
+ 00bf9f4c ["CALL", null, ["callee:0045a714:8"]]
- 00bf9eb0 bytes 0982e197
+ 00bf9f4c bytes f281e197
~~~


<a id="compare-42b497aa4d070260fa288ff826126cde"></a>

### [`00bf9eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9eb4.md) → [`00bf9f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f50.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c58620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9eb4.md#insn-00bf9ed4)
- 新版 `00bf9f70`（命令位置の公開資料なし）

~~~diff
- 00bf9ed4 ["INT_ADD", "register:40f0:8", ["const:bf9ed4:8", "const:4:8"]]
- 00bf9ed4 ["CALL", null, ["callee:0045a714:8"]]
+ 00bf9f70 ["INT_ADD", "register:40f0:8", ["const:bf9f70:8", "const:4:8"]]
+ 00bf9f70 ["CALL", null, ["callee:0045a714:8"]]
- 00bf9ed4 bytes 0082e197
+ 00bf9f70 bytes e981e197
~~~


<a id="compare-68c9211abeca1cdea2501943d00121ae"></a>

### [`00bf9ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md) → [`00bf9f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f74.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58360.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58430.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9ef4) · [`00bf9f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9f00) · [`00bf9f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9f08)
- 新版 `00bf9f90`（命令位置の公開資料なし） · `00bf9f9c`（命令位置の公開資料なし） · `00bf9fa4`（命令位置の公開資料なし）

~~~diff
- 00bf9ef4 ["INT_ADD", "register:40f0:8", ["const:bf9ef4:8", "const:4:8"]]
- 00bf9ef4 ["CALL", null, ["callee:00c58580:8"]]
+ 00bf9f90 ["INT_ADD", "register:40f0:8", ["const:bf9f90:8", "const:4:8"]]
+ 00bf9f90 ["CALL", null, ["callee:00c58580:8"]]
- 00bf9ef4 bytes 6f790194
+ 00bf9f90 bytes 7c790194
- 00bf9f00 ["INT_ADD", "register:40f0:8", ["const:bf9f00:8", "const:4:8"]]
- 00bf9f00 ["CALL", null, ["callee:00c58430:8"]]
+ 00bf9f9c ["INT_ADD", "register:40f0:8", ["const:bf9f9c:8", "const:4:8"]]
+ 00bf9f9c ["CALL", null, ["callee:00c58430:8"]]
- 00bf9f00 bytes 18790194
+ 00bf9f9c bytes 25790194
- 00bf9f08 ["INT_ADD", "register:40f0:8", ["const:bf9f08:8", "const:4:8"]]
- 00bf9f08 ["CALL", null, ["callee:00c583c0:8"]]
+ 00bf9fa4 ["INT_ADD", "register:40f0:8", ["const:bf9fa4:8", "const:4:8"]]
+ 00bf9fa4 ["CALL", null, ["callee:00c583c0:8"]]
- 00bf9f08 bytes fa780194
+ 00bf9fa4 bytes 07790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c59902444f9ba0cf82d51bab8f9b5b7"></a>

### [`00bf9f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f38.md) → [`00bf9fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9fd4.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c5e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c5e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f38.md#insn-00bf9f58)
- 新版 `00bf9ff4`（命令位置の公開資料なし）

~~~diff
- 00bf9f58 ["INT_ADD", "register:40f0:8", ["const:bf9f58:8", "const:4:8"]]
- 00bf9f58 ["CALL", null, ["callee:0045a714:8"]]
+ 00bf9ff4 ["INT_ADD", "register:40f0:8", ["const:bf9ff4:8", "const:4:8"]]
+ 00bf9ff4 ["CALL", null, ["callee:0045a714:8"]]
- 00bf9f58 bytes df81e197
+ 00bf9ff4 bytes c881e197
~~~


<a id="compare-82676c1d30432982ea7b0aad206be8dc"></a>

### [`00bf9f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md) → [`00bf9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md) [`00c5e240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e240.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md) [`00c5e310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f78) · [`00bf9f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f84) · [`00bf9f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f8c)
- 新版 `00bfa014`（命令位置の公開資料なし） · `00bfa020`（命令位置の公開資料なし） · `00bfa028`（命令位置の公開資料なし）

~~~diff
- 00bf9f78 ["INT_ADD", "register:40f0:8", ["const:bf9f78:8", "const:4:8"]]
- 00bf9f78 ["CALL", null, ["callee:00c58580:8"]]
+ 00bfa014 ["INT_ADD", "register:40f0:8", ["const:bfa014:8", "const:4:8"]]
+ 00bfa014 ["CALL", null, ["callee:00c58580:8"]]
- 00bf9f78 bytes 4e790194
+ 00bfa014 bytes 5b790194
- 00bf9f84 ["INT_ADD", "register:40f0:8", ["const:bf9f84:8", "const:4:8"]]
- 00bf9f84 ["CALL", null, ["callee:00c5e310:8"]]
+ 00bfa020 ["INT_ADD", "register:40f0:8", ["const:bfa020:8", "const:4:8"]]
+ 00bfa020 ["CALL", null, ["callee:00c5e310:8"]]
- 00bf9f84 bytes af900194
+ 00bfa020 bytes bc900194
- 00bf9f8c ["INT_ADD", "register:40f0:8", ["const:bf9f8c:8", "const:4:8"]]
- 00bf9f8c ["CALL", null, ["callee:00c583c0:8"]]
+ 00bfa028 ["INT_ADD", "register:40f0:8", ["const:bfa028:8", "const:4:8"]]
+ 00bfa028 ["CALL", null, ["callee:00c583c0:8"]]
- 00bf9f8c bytes d9780194
+ 00bfa028 bytes e6780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-476512cc8ae28dbc012005cd71c6bd81"></a>

### [`00bf9fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9fbc.md) → [`00bfa058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa058.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9fbc.md#insn-00bf9fdc)
- 新版 `00bfa078`（命令位置の公開資料なし）

~~~diff
- 00bf9fdc ["INT_ADD", "register:40f0:8", ["const:bf9fdc:8", "const:4:8"]]
- 00bf9fdc ["CALL", null, ["callee:00c53da0:8"]]
+ 00bfa078 ["INT_ADD", "register:40f0:8", ["const:bfa078:8", "const:4:8"]]
+ 00bfa078 ["CALL", null, ["callee:00c53da0:8"]]
- 00bf9fdc bytes 49670194
+ 00bfa078 bytes 4a670194
~~~


<a id="compare-279147a0ae6f7584e859d1a380038e44"></a>

### [`00bfa010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md) → [`00bfa0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa0ac.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa03c) · [`00bfa050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa050) · [`00bfa064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa064)
- 新版 `00bfa0d8`（命令位置の公開資料なし） · `00bfa0ec`（命令位置の公開資料なし） · `00bfa100`（命令位置の公開資料なし）

~~~diff
- 00bfa03c ["INT_ADD", "register:40f0:8", ["const:bfa03c:8", "const:4:8"]]
- 00bfa03c ["CALL", null, ["callee:00c53d70:8"]]
+ 00bfa0d8 ["INT_ADD", "register:40f0:8", ["const:bfa0d8:8", "const:4:8"]]
+ 00bfa0d8 ["CALL", null, ["callee:00c53d70:8"]]
- 00bfa03c bytes 25670194
+ 00bfa0d8 bytes 26670194
- 00bfa050 ["INT_ADD", "register:40f0:8", ["const:bfa050:8", "const:4:8"]]
- 00bfa050 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bfa0ec ["INT_ADD", "register:40f0:8", ["const:bfa0ec:8", "const:4:8"]]
+ 00bfa0ec ["CALL", null, ["callee:00c53da0:8"]]
- 00bfa050 bytes 2c670194
+ 00bfa0ec bytes 2d670194
- 00bfa064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfa064 ["INT_ADD", "register:40f0:8", ["const:bfa064:8", "const:4:8"]]
- 00bfa064 ["CALLIND", null, ["register:0:8"]]
+ 00bfa100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfa100 ["INT_ADD", "register:40f0:8", ["const:bfa100:8", "const:4:8"]]
+ 00bfa100 ["CALLIND", null, ["register:0:8"]]
- 00bfa064 bytes 00013fd6
+ 00bfa100 bytes 00013fd6
~~~


<a id="compare-e6cfcd897e9e400468300c959affc979"></a>

### [`00bfa0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa0e4.md) → [`00bfa180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa180.md) FUN_00bfa180

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa0e4.md#insn-00bfa0f8)
- 新版 `00bfa194`（命令位置の公開資料なし）

~~~diff
- 00bfa0f8 ["INT_ADD", "register:40f0:8", ["const:bfa0f8:8", "const:4:8"]]
- 00bfa0f8 ["CALL", null, ["callee:00c5dfc0:8"]]
+ 00bfa194 ["INT_ADD", "register:40f0:8", ["const:bfa194:8", "const:4:8"]]
+ 00bfa194 ["CALL", null, ["callee:00c5dfc0:8"]]
- 00bfa0f8 bytes 7e8f0194
+ 00bfa194 bytes 8b8f0194
~~~


<a id="compare-971d012776bb25562fedb806da48076d"></a>

### [`00bfa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md) → [`00bfa1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0043ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae78.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`0048baf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md) [`0058f6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md)
- 新版 呼出元 6件 [`0043aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`0048bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048bb30.md) [`0058f6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md) · 呼出先 1件 [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md#insn-00bfa11c)
- 新版 `00bfa1b8`（命令位置の公開資料なし）

~~~diff
- 00bfa11c ["INT_ADD", "register:40f0:8", ["const:bfa11c:8", "const:4:8"]]
- 00bfa11c ["CALL", null, ["callee:00c5b760:8"]]
+ 00bfa1b8 ["INT_ADD", "register:40f0:8", ["const:bfa1b8:8", "const:4:8"]]
+ 00bfa1b8 ["CALL", null, ["callee:00c5b760:8"]]
- 00bfa11c bytes 5d850194
+ 00bfa1b8 bytes 6a850194
~~~


<a id="compare-99e59b98b506917e217f4d6246f0c248"></a>

### [`00bfa15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa15c.md) → [`00bfa1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1f8.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa15c.md#insn-00bfa168)
- 新版 `00bfa204`（命令位置の公開資料なし）

~~~diff
- 00bfa168 ["INT_ADD", "register:40f0:8", ["const:bfa168:8", "const:4:8"]]
- 00bfa168 ["CALL", null, ["callee:00c5e340:8"]]
+ 00bfa204 ["INT_ADD", "register:40f0:8", ["const:bfa204:8", "const:4:8"]]
+ 00bfa204 ["CALL", null, ["callee:00c5e340:8"]]
- 00bfa168 bytes 42900194
+ 00bfa204 bytes 4f900194
~~~


<a id="compare-5765a5ec5e95538113fc99c523d723f5"></a>

### [`00bfa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa184.md) → [`00bfa220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa220.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa184.md#insn-00bfa190)
- 新版 `00bfa22c`（命令位置の公開資料なし）

~~~diff
- 00bfa190 ["INT_ADD", "register:40f0:8", ["const:bfa190:8", "const:4:8"]]
- 00bfa190 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa22c ["INT_ADD", "register:40f0:8", ["const:bfa22c:8", "const:4:8"]]
+ 00bfa22c ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa190 bytes 48850194
+ 00bfa22c bytes 55850194
~~~


<a id="compare-df6b6f28b9a25465a2e2df89e2e1ed0e"></a>

### [`00bfa248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa248.md) → [`00bfa2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa2e4.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0d0.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5a1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1a0.md) · 呼出先 1件 [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa248.md#insn-00bfa254)
- 新版 `00bfa2f0`（命令位置の公開資料なし）

~~~diff
- 00bfa254 ["INT_ADD", "register:40f0:8", ["const:bfa254:8", "const:4:8"]]
- 00bfa254 ["CALL", null, ["callee:00c5b760:8"]]
+ 00bfa2f0 ["INT_ADD", "register:40f0:8", ["const:bfa2f0:8", "const:4:8"]]
+ 00bfa2f0 ["CALL", null, ["callee:00c5b760:8"]]
- 00bfa254 bytes 0f850194
+ 00bfa2f0 bytes 1c850194
~~~


<a id="compare-fb1fa66fca427873d53c7b6b3e4f2e13"></a>

### [`00bfa294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa294.md) → [`00bfa330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa330.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md) · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md) · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa294.md#insn-00bfa2a0)
- 新版 `00bfa33c`（命令位置の公開資料なし）

~~~diff
- 00bfa2a0 ["INT_ADD", "register:40f0:8", ["const:bfa2a0:8", "const:4:8"]]
- 00bfa2a0 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa33c ["INT_ADD", "register:40f0:8", ["const:bfa33c:8", "const:4:8"]]
+ 00bfa33c ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa2a0 bytes 04850194
+ 00bfa33c bytes 11850194
~~~


<a id="compare-655cc1e771a0e68218b0a2fdc6c6dabb"></a>

### [`00bfa2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2b4.md) → [`00bfa350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa350.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2b4.md#insn-00bfa2c0)
- 新版 `00bfa35c`（命令位置の公開資料なし）

~~~diff
- 00bfa2c0 ["INT_ADD", "register:40f0:8", ["const:bfa2c0:8", "const:4:8"]]
- 00bfa2c0 ["CALL", null, ["callee:00c5e340:8"]]
+ 00bfa35c ["INT_ADD", "register:40f0:8", ["const:bfa35c:8", "const:4:8"]]
+ 00bfa35c ["CALL", null, ["callee:00c5e340:8"]]
- 00bfa2c0 bytes ec8f0194
+ 00bfa35c bytes f98f0194
~~~


<a id="compare-9e0af1983df2d00984fad1b4f06122e6"></a>

### [`00bfa3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md) → [`00bfa478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa478.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md#insn-00bfa3f0) · [`00bfa41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md#insn-00bfa41c)
- 新版 `00bfa48c`（命令位置の公開資料なし） · `00bfa4b8`（命令位置の公開資料なし）

~~~diff
- 00bfa3f0 ["INT_ADD", "register:40f0:8", ["const:bfa3f0:8", "const:4:8"]]
- 00bfa3f0 ["CALL", null, ["callee:00c5e340:8"]]
+ 00bfa48c ["INT_ADD", "register:40f0:8", ["const:bfa48c:8", "const:4:8"]]
+ 00bfa48c ["CALL", null, ["callee:00c5e340:8"]]
- 00bfa3f0 bytes a08f0194
+ 00bfa48c bytes ad8f0194
- 00bfa41c ["INT_ADD", "register:40f0:8", ["const:bfa41c:8", "const:4:8"]]
- 00bfa41c ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa4b8 ["INT_ADD", "register:40f0:8", ["const:bfa4b8:8", "const:4:8"]]
+ 00bfa4b8 ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa41c bytes a5840194
+ 00bfa4b8 bytes b2840194
~~~


<a id="compare-c4e87b7c0d471134ad4428fe8580177a"></a>

### [`00bfa5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md) → [`00bfa67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa67c.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa5f8) · [`00bfa604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa604) · [`00bfa644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa644)
- 新版 `00bfa694`（命令位置の公開資料なし） · `00bfa6a0`（命令位置の公開資料なし） · `00bfa6e0`（命令位置の公開資料なし）

~~~diff
- 00bfa5f8 ["INT_ADD", "register:40f0:8", ["const:bfa5f8:8", "const:4:8"]]
- 00bfa5f8 ["CALL", null, ["callee:00c586f0:8"]]
+ 00bfa694 ["INT_ADD", "register:40f0:8", ["const:bfa694:8", "const:4:8"]]
+ 00bfa694 ["CALL", null, ["callee:00c586f0:8"]]
- 00bfa5f8 bytes 0a780194
+ 00bfa694 bytes 17780194
- 00bfa604 ["INT_ADD", "register:40f0:8", ["const:bfa604:8", "const:4:8"]]
- 00bfa604 ["CALL", null, ["callee:00c5e340:8"]]
+ 00bfa6a0 ["INT_ADD", "register:40f0:8", ["const:bfa6a0:8", "const:4:8"]]
+ 00bfa6a0 ["CALL", null, ["callee:00c5e340:8"]]
- 00bfa604 bytes 1b8f0194
+ 00bfa6a0 bytes 288f0194
- 00bfa644 ["INT_ADD", "register:40f0:8", ["const:bfa644:8", "const:4:8"]]
- 00bfa644 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa6e0 ["INT_ADD", "register:40f0:8", ["const:bfa6e0:8", "const:4:8"]]
+ 00bfa6e0 ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa644 bytes 1b840194
+ 00bfa6e0 bytes 28840194
~~~


<a id="compare-d62bfdb7680f34b204e7b1b079096977"></a>

### [`00bfa6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa6e4.md) → [`00bfa780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa780.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58180.md) · 呼出先 1件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c58250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58250.md) · 呼出先 1件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa6e4.md#insn-00bfa700)
- 新版 `00bfa79c`（命令位置の公開資料なし）

~~~diff
- 00bfa700 ["INT_ADD", "register:40f0:8", ["const:bfa700:8", "const:4:8"]]
- 00bfa700 ["CALL", null, ["callee:00c580f0:8"]]
+ 00bfa79c ["INT_ADD", "register:40f0:8", ["const:bfa79c:8", "const:4:8"]]
+ 00bfa79c ["CALL", null, ["callee:00c580f0:8"]]
- 00bfa700 bytes 48760194
+ 00bfa79c bytes 55760194
~~~


<a id="compare-1a1562e522172e3fb705f4a7be975544"></a>

### [`00bfa798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa798.md) → [`00bfa834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa834.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa798.md#insn-00bfa7a8)
- 新版 `00bfa844`（命令位置の公開資料なし）

~~~diff
- 00bfa7a8 ["INT_ADD", "register:40f0:8", ["const:bfa7a8:8", "const:4:8"]]
- 00bfa7a8 ["CALL", null, ["callee:00c5e360:8"]]
+ 00bfa844 ["INT_ADD", "register:40f0:8", ["const:bfa844:8", "const:4:8"]]
+ 00bfa844 ["CALL", null, ["callee:00c5e360:8"]]
- 00bfa7a8 bytes ba8e0194
+ 00bfa844 bytes c78e0194
~~~


<a id="compare-9899330386c01a683abecf572704b8bc"></a>

### [`00bfa7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md) → [`00bfa860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa860.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58490.md) · 呼出先 2件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2a0.md)
- 新版 呼出元 1件 [`00c58560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58560.md) · 呼出先 2件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md#insn-00bfa818) · [`00bfa824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md#insn-00bfa824)
- 新版 `00bfa8b4`（命令位置の公開資料なし） · `00bfa8c0`（命令位置の公開資料なし）

~~~diff
- 00bfa818 ["INT_ADD", "register:40f0:8", ["const:bfa818:8", "const:4:8"]]
- 00bfa818 ["CALL", null, ["callee:00c5e370:8"]]
+ 00bfa8b4 ["INT_ADD", "register:40f0:8", ["const:bfa8b4:8", "const:4:8"]]
+ 00bfa8b4 ["CALL", null, ["callee:00c5e370:8"]]
- 00bfa818 bytes a28e0194
+ 00bfa8b4 bytes af8e0194
- 00bfa824 ["INT_ADD", "register:40f0:8", ["const:bfa824:8", "const:4:8"]]
- 00bfa824 ["CALL", null, ["callee:00c58190:8"]]
+ 00bfa8c0 ["INT_ADD", "register:40f0:8", ["const:bfa8c0:8", "const:4:8"]]
+ 00bfa8c0 ["CALL", null, ["callee:00c58190:8"]]
- 00bfa824 bytes 27760194
+ 00bfa8c0 bytes 34760194
~~~


<a id="compare-e708b96c8cd2d57ad54927d4af4f1b9f"></a>

### [`00bfa8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md) → [`00bfa998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md) FUN_00bfa998

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfabf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md) · 呼出先 5件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) [`00c5e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e250.md)
- 新版 呼出元 1件 [`00bfac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md) · 呼出先 5件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) [`00c5e320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa924) · [`00bfa92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa92c) · [`00bfa954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa954)
- 新版 `00bfa9c0`（命令位置の公開資料なし） · `00bfa9c8`（命令位置の公開資料なし） · `00bfa9f0`（命令位置の公開資料なし）

~~~diff
- 00bfa924 ["INT_ADD", "register:40f0:8", ["const:bfa924:8", "const:4:8"]]
- 00bfa924 ["CALL", null, ["callee:00c58450:8"]]
+ 00bfa9c0 ["INT_ADD", "register:40f0:8", ["const:bfa9c0:8", "const:4:8"]]
+ 00bfa9c0 ["CALL", null, ["callee:00c58450:8"]]
- 00bfa924 bytes 97760194
+ 00bfa9c0 bytes a4760194
- 00bfa92c ["INT_ADD", "register:40f0:8", ["const:bfa92c:8", "const:4:8"]]
- 00bfa92c ["CALL", null, ["callee:00c581c0:8"]]
+ 00bfa9c8 ["INT_ADD", "register:40f0:8", ["const:bfa9c8:8", "const:4:8"]]
+ 00bfa9c8 ["CALL", null, ["callee:00c581c0:8"]]
- 00bfa92c bytes f1750194
+ 00bfa9c8 bytes fe750194
- 00bfa954 ["INT_ADD", "register:40f0:8", ["const:bfa954:8", "const:4:8"]]
- 00bfa954 ["CALL", null, ["callee:00c5e320:8"]]
+ 00bfa9f0 ["INT_ADD", "register:40f0:8", ["const:bfa9f0:8", "const:4:8"]]
+ 00bfa9f0 ["CALL", null, ["callee:00c5e320:8"]]
- 00bfa954 bytes 3f8e0194
+ 00bfa9f0 bytes 4c8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-831eb5e6e80ed6bfe908f53c1271c3bf"></a>

### [`00bfa9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md) → [`00bfaa64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md) FUN_00bfaa64

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfac34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac34.md) · 呼出先 4件 [`00bfac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00bfacd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfacd0.md) · 呼出先 4件 [`00bface8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfaa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa44) · [`00bfaa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa88) · [`00bfaa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa9c)
- 新版 `00bfaae0`（命令位置の公開資料なし） · `00bfab24`（命令位置の公開資料なし） · `00bfab38`（命令位置の公開資料なし）

~~~diff
- 00bfaa44 ["INT_ADD", "register:40f0:8", ["const:bfaa44:8", "const:4:8"]]
- 00bfaa44 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bfaae0 ["INT_ADD", "register:40f0:8", ["const:bfaae0:8", "const:4:8"]]
+ 00bfaae0 ["CALL", null, ["callee:00c57f60:8"]]
- 00bfaa44 bytes 13750194
+ 00bfaae0 bytes 20750194
- 00bfaa88 ["INT_ADD", "register:40f0:8", ["const:bfaa88:8", "const:4:8"]]
- 00bfaa88 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bfab24 ["INT_ADD", "register:40f0:8", ["const:bfab24:8", "const:4:8"]]
+ 00bfab24 ["CALL", null, ["callee:00c580d0:8"]]
- 00bfaa88 bytes 5e750194
+ 00bfab24 bytes 6b750194
- 00bfaa9c ["INT_ADD", "register:40f0:8", ["const:bfaa9c:8", "const:4:8"]]
- 00bfaa9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bfab38 ["INT_ADD", "register:40f0:8", ["const:bfab38:8", "const:4:8"]]
+ 00bfab38 ["CALL", null, ["callee:00c57f80:8"]]
- 00bfaa9c bytes 05750194
+ 00bfab38 bytes 12750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26522fa960208ee8d4f2c74c2738d3d0"></a>

### [`00bfaac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md) → [`00bfab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md) FUN_00bfab60

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfac40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac40.md) · 呼出先 5件 [`00bfac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00bfacdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfacdc.md) · 呼出先 5件 [`00bfad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab38) · [`00bfab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab6c) · [`00bfab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab80)
- 新版 `00bfabd4`（命令位置の公開資料なし） · `00bfac08`（命令位置の公開資料なし） · `00bfac1c`（命令位置の公開資料なし）

~~~diff
- 00bfab38 ["INT_ADD", "register:40f0:8", ["const:bfab38:8", "const:4:8"]]
- 00bfab38 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bfabd4 ["INT_ADD", "register:40f0:8", ["const:bfabd4:8", "const:4:8"]]
+ 00bfabd4 ["CALL", null, ["callee:00c57f60:8"]]
- 00bfab38 bytes d6740194
+ 00bfabd4 bytes e3740194
- 00bfab6c ["INT_ADD", "register:40f0:8", ["const:bfab6c:8", "const:4:8"]]
- 00bfab6c ["CALL", null, ["callee:00c580d0:8"]]
+ 00bfac08 ["INT_ADD", "register:40f0:8", ["const:bfac08:8", "const:4:8"]]
+ 00bfac08 ["CALL", null, ["callee:00c580d0:8"]]
- 00bfab6c bytes 25750194
+ 00bfac08 bytes 32750194
- 00bfab80 ["INT_ADD", "register:40f0:8", ["const:bfab80:8", "const:4:8"]]
- 00bfab80 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bfac1c ["INT_ADD", "register:40f0:8", ["const:bfac1c:8", "const:4:8"]]
+ 00bfac1c ["CALL", null, ["callee:00c57f80:8"]]
- 00bfab80 bytes cc740194
+ 00bfac1c bytes d9740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25e7e555e6be83cf896ef208a5435dda"></a>

### [`00bfabb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabb4.md) → [`00bfac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac50.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabb4.md#insn-00bfabcc)
- 新版 `00bfac68`（命令位置の公開資料なし）

~~~diff
- 00bfabcc ["INT_ADD", "register:40f0:8", ["const:bfabcc:8", "const:4:8"]]
- 00bfabcc ["CALL", null, ["callee:00c57f60:8"]]
+ 00bfac68 ["INT_ADD", "register:40f0:8", ["const:bfac68:8", "const:4:8"]]
+ 00bfac68 ["CALL", null, ["callee:00c57f60:8"]]
- 00bfabcc bytes b1740194
+ 00bfac68 bytes be740194
~~~


<a id="compare-2bbb432faa287affe7cc9baa43ed28ed"></a>

### [`00bfabf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md) → [`00bfac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md) _ZNSt6__ndk115__thread_structD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md) · 呼出先 2件 [`00bfa8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md) · 呼出先 2件 [`00bfa998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md#insn-00bfac0c)
- 新版 `00bfaca8`（命令位置の公開資料なし）

~~~diff
- 00bfac0c ["INT_ADD", "register:40f0:8", ["const:bfac0c:8", "const:4:8"]]
- 00bfac0c ["CALL", null, ["callee:00bfa998:8"]]
+ 00bfaca8 ["INT_ADD", "register:40f0:8", ["const:bfaca8:8", "const:4:8"]]
+ 00bfaca8 ["CALL", null, ["callee:00bfa998:8"]]
- 00bfac0c bytes 3cffff97
+ 00bfaca8 bytes 3cffff97
~~~


<a id="compare-4d3e5eb3e8839b77c8553f759854bd82"></a>

### [`00bfac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md) → [`00bfad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) FUN_00bfad18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 1件 [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfac98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md#insn-00bfac98)
- 新版 `00bfad34`（命令位置の公開資料なし）

~~~diff
- 00bfac98 ["INT_ADD", "register:40f0:8", ["const:bfac98:8", "const:4:8"]]
- 00bfac98 ["CALL", null, ["callee:00c58220:8"]]
+ 00bfad34 ["INT_ADD", "register:40f0:8", ["const:bfad34:8", "const:4:8"]]
+ 00bfad34 ["CALL", null, ["callee:00c58220:8"]]
- 00bfac98 bytes 2e750194
+ 00bfad34 bytes 3b750194
~~~


<a id="compare-20003a1c7729fa1dcfeba1f37098c86c"></a>

### [`00bfad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md) → [`00bfadf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfadf4.md) _ZNSt6__ndk113random_deviceD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md) [`00c583d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583d0.md) · 呼出先 1件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md)
- 新版 呼出元 2件 [`005607cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005607cc.md) [`00c584a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c584a0.md) · 呼出先 1件 [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md#insn-00bfad68)
- 新版 `00bfae04`（命令位置の公開資料なし）

~~~diff
- 00bfad68 ["INT_ADD", "register:40f0:8", ["const:bfad68:8", "const:4:8"]]
- 00bfad68 ["CALL", null, ["callee:00c598a0:8"]]
+ 00bfae04 ["INT_ADD", "register:40f0:8", ["const:bfae04:8", "const:4:8"]]
+ 00bfae04 ["CALL", null, ["callee:00c598a0:8"]]
- 00bfad68 bytes 9a7a0194
+ 00bfae04 bytes a77a0194
~~~


<a id="compare-83609ba1a4cb0a8541a353c931587655"></a>

### [`00bfae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae10.md) → [`00bfaeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaeac.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae10.md#insn-00bfae30)
- 新版 `00bfaecc`（命令位置の公開資料なし）

~~~diff
- 00bfae30 ["INT_ADD", "register:40f0:8", ["const:bfae30:8", "const:4:8"]]
- 00bfae30 ["CALL", null, ["callee:00c5e380:8"]]
+ 00bfaecc ["INT_ADD", "register:40f0:8", ["const:bfaecc:8", "const:4:8"]]
+ 00bfaecc ["CALL", null, ["callee:00c5e380:8"]]
- 00bfae30 bytes 208d0194
+ 00bfaecc bytes 2d8d0194
~~~


<a id="compare-cf2a38c8a036f5c34b8ff654429e33f7"></a>

### [`00bfafc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafc4.md) → [`00bfb060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb060.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfafd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafc4.md#insn-00bfafd8)
- 新版 `00bfb074`（命令位置の公開資料なし）

~~~diff
- 00bfafd8 ["INT_ADD", "register:40f0:8", ["const:bfafd8:8", "const:4:8"]]
- 00bfafd8 ["CALL", null, ["callee:00c5e390:8"]]
+ 00bfb074 ["INT_ADD", "register:40f0:8", ["const:bfb074:8", "const:4:8"]]
+ 00bfb074 ["CALL", null, ["callee:00c5e390:8"]]
- 00bfafd8 bytes ba8c0194
+ 00bfb074 bytes c78c0194
~~~


<a id="compare-ece620a77bb6261c61a6350e09c557ff"></a>

### [`00bfaff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaff0.md) → [`00bfb08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb08c.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaff0.md#insn-00bfb030)
- 新版 `00bfb0cc`（命令位置の公開資料なし）

~~~diff
- 00bfb030 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb030 ["INT_ADD", "register:40f0:8", ["const:bfb030:8", "const:4:8"]]
- 00bfb030 ["CALLIND", null, ["register:0:8"]]
+ 00bfb0cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb0cc ["INT_ADD", "register:40f0:8", ["const:bfb0cc:8", "const:4:8"]]
+ 00bfb0cc ["CALLIND", null, ["register:0:8"]]
- 00bfb030 bytes 00013fd6
+ 00bfb0cc bytes 00013fd6
~~~


<a id="compare-fee9f8b67e2781d63ff2bc23200d1d24"></a>

### [`00bfb054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md) → [`00bfb0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb0f0.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb07c) · [`00bfb088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb088) · [`00bfb0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb0ac)
- 新版 `00bfb118`（命令位置の公開資料なし） · `00bfb124`（命令位置の公開資料なし） · `00bfb148`（命令位置の公開資料なし）

~~~diff
- 00bfb07c ["INT_ADD", "register:40f0:8", ["const:bfb07c:8", "const:4:8"]]
- 00bfb07c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfb118 ["INT_ADD", "register:40f0:8", ["const:bfb118:8", "const:4:8"]]
+ 00bfb118 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfb07c bytes d57d0194
+ 00bfb118 bytes e27d0194
- 00bfb088 ["INT_ADD", "register:40f0:8", ["const:bfb088:8", "const:4:8"]]
- 00bfb088 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfb124 ["INT_ADD", "register:40f0:8", ["const:bfb124:8", "const:4:8"]]
+ 00bfb124 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfb088 bytes 968c0194
+ 00bfb124 bytes a38c0194
- 00bfb0ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb0ac ["INT_ADD", "register:40f0:8", ["const:bfb0ac:8", "const:4:8"]]
- 00bfb0ac ["CALLIND", null, ["register:0:8"]]
+ 00bfb148 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb148 ["INT_ADD", "register:40f0:8", ["const:bfb148:8", "const:4:8"]]
+ 00bfb148 ["CALLIND", null, ["register:0:8"]]
- 00bfb0ac bytes 00013fd6
+ 00bfb148 bytes 00013fd6
~~~


<a id="compare-4fc24ff325efeb7dd5510ec92cc69a7e"></a>

### [`00bfb4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb4d8.md) → [`00bfb574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb574.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb4d8.md#insn-00bfb4ec)
- 新版 `00bfb588`（命令位置の公開資料なし）

~~~diff
- 00bfb4ec ["INT_ADD", "register:40f0:8", ["const:bfb4ec:8", "const:4:8"]]
- 00bfb4ec ["CALL", null, ["callee:00c5e3c0:8"]]
+ 00bfb588 ["INT_ADD", "register:40f0:8", ["const:bfb588:8", "const:4:8"]]
+ 00bfb588 ["CALL", null, ["callee:00c5e3c0:8"]]
- 00bfb4ec bytes 818b0194
+ 00bfb588 bytes 8e8b0194
~~~


<a id="compare-8d3205166a170fb1df84c6a63216f034"></a>

### [`00bfb630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md) → [`00bfb6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb6cc.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 1件 [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb664) · [`00bfb674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb674) · [`00bfb6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb6a0)
- 新版 `00bfb700`（命令位置の公開資料なし） · `00bfb710`（命令位置の公開資料なし） · `00bfb73c`（命令位置の公開資料なし）

~~~diff
- 00bfb664 ["INT_ADD", "register:40f0:8", ["const:bfb664:8", "const:4:8"]]
- 00bfb664 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00bfb700 ["INT_ADD", "register:40f0:8", ["const:bfb700:8", "const:4:8"]]
+ 00bfb700 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00bfb664 bytes 6f7a0194
+ 00bfb700 bytes 7c7a0194
- 00bfb674 ["INT_ADD", "register:40f0:8", ["const:bfb674:8", "const:4:8"]]
- 00bfb674 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00bfb710 ["INT_ADD", "register:40f0:8", ["const:bfb710:8", "const:4:8"]]
+ 00bfb710 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00bfb674 bytes 6b7a0194
+ 00bfb710 bytes 787a0194
- 00bfb6a0 ["INT_ADD", "register:40f0:8", ["const:bfb6a0:8", "const:4:8"]]
- 00bfb6a0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00bfb73c ["INT_ADD", "register:40f0:8", ["const:bfb73c:8", "const:4:8"]]
+ 00bfb73c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00bfb6a0 bytes 607a0194
+ 00bfb73c bytes 6d7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694d8ddf4e082be8a5fc397d7a7686c5"></a>

### [`00bfb8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb8f0.md) → [`00bfb98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb98c.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb8f0.md#insn-00bfb92c)
- 新版 `00bfb9c8`（命令位置の公開資料なし）

~~~diff
- 00bfb92c ["INT_ADD", "register:40f0:8", ["const:bfb92c:8", "const:4:8"]]
- 00bfb92c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfb9c8 ["INT_ADD", "register:40f0:8", ["const:bfb9c8:8", "const:4:8"]]
+ 00bfb9c8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfb92c bytes a97b0194
+ 00bfb9c8 bytes b67b0194
~~~


<a id="compare-06f1d21e6d06bd2211fc8435a494624e"></a>

### [`00bfb98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md) → [`00bfba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md) · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba00) · [`00bfba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba0c) · [`00bfba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba18)
- 新版 `00bfba9c`（命令位置の公開資料なし） · `00bfbaa8`（命令位置の公開資料なし） · `00bfbab4`（命令位置の公開資料なし）

~~~diff
- 00bfba00 ["INT_ADD", "register:40f0:8", ["const:bfba00:8", "const:4:8"]]
- 00bfba00 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfba9c ["INT_ADD", "register:40f0:8", ["const:bfba9c:8", "const:4:8"]]
+ 00bfba9c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfba00 bytes 747b0194
+ 00bfba9c bytes 817b0194
- 00bfba0c ["INT_ADD", "register:40f0:8", ["const:bfba0c:8", "const:4:8"]]
- 00bfba0c ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfbaa8 ["INT_ADD", "register:40f0:8", ["const:bfbaa8:8", "const:4:8"]]
+ 00bfbaa8 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfba0c bytes 358a0194
+ 00bfbaa8 bytes 428a0194
- 00bfba18 ["INT_ADD", "register:40f0:8", ["const:bfba18:8", "const:4:8"]]
- 00bfba18 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfbab4 ["INT_ADD", "register:40f0:8", ["const:bfbab4:8", "const:4:8"]]
+ 00bfbab4 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfba18 bytes 328a0194
+ 00bfbab4 bytes 3f8a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88132b8f589595a3de6bbd3b71748b2a"></a>

### [`00bfbaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbaa8.md) → [`00bfbb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb44.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c582c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582c0.md) · 呼出先 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md)
- 新版 呼出元 1件 [`00c58390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58390.md) · 呼出先 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbaa8.md#insn-00bfbad0)
- 新版 `00bfbb6c`（命令位置の公開資料なし）

~~~diff
- 00bfbad0 ["INT_ADD", "register:40f0:8", ["const:bfbad0:8", "const:4:8"]]
- 00bfbad0 ["CALL", null, ["callee:00c585d0:8"]]
+ 00bfbb6c ["INT_ADD", "register:40f0:8", ["const:bfbb6c:8", "const:4:8"]]
+ 00bfbb6c ["CALL", null, ["callee:00c585d0:8"]]
- 00bfbad0 bytes 8c720194
+ 00bfbb6c bytes 99720194
~~~


<a id="compare-686367bb3a1373a06790f21bf03b1a05"></a>

### [`00bfbad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbad4.md) → [`00bfbb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb70.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e330.md) · 呼出先 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md)
- 新版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e400.md) · 呼出先 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbad4.md#insn-00bfbafc)
- 新版 `00bfbb98`（命令位置の公開資料なし）

~~~diff
- 00bfbafc ["INT_ADD", "register:40f0:8", ["const:bfbafc:8", "const:4:8"]]
- 00bfbafc ["CALL", null, ["callee:00c585d0:8"]]
+ 00bfbb98 ["INT_ADD", "register:40f0:8", ["const:bfbb98:8", "const:4:8"]]
+ 00bfbb98 ["CALL", null, ["callee:00c585d0:8"]]
- 00bfbafc bytes 81720194
+ 00bfbb98 bytes 8e720194
~~~


<a id="compare-5e2ea7d553b29713f1c914b5ba715a71"></a>

### [`00bfbb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb1c.md) → [`00bfbbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbb8.md) FUN_00bfbbb8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb1c.md#insn-00bfbb30)
- 新版 `00bfbbcc`（命令位置の公開資料なし）

~~~diff
- 00bfbb30 ["INT_ADD", "register:40f0:8", ["const:bfbb30:8", "const:4:8"]]
- 00bfbb30 ["CALL", null, ["callee:00c5dfc0:8"]]
+ 00bfbbcc ["INT_ADD", "register:40f0:8", ["const:bfbbcc:8", "const:4:8"]]
+ 00bfbbcc ["CALL", null, ["callee:00c5dfc0:8"]]
- 00bfbb30 bytes f0880194
+ 00bfbbcc bytes fd880194
~~~


<a id="compare-cea63bcd13e52694f761ee4ca26a612b"></a>

### [`00bfbb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md) → [`00bfbbec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbec.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md#insn-00bfbb64)
- 新版 `00bfbc00`（命令位置の公開資料なし）

~~~diff
- 00bfbb64 ["INT_ADD", "register:40f0:8", ["const:bfbb64:8", "const:4:8"]]
- 00bfbb64 ["CALL", null, ["callee:00c5e410:8"]]
+ 00bfbc00 ["INT_ADD", "register:40f0:8", ["const:bfbc00:8", "const:4:8"]]
+ 00bfbc00 ["CALL", null, ["callee:00c5e410:8"]]
- 00bfbb64 bytes f7890194
+ 00bfbc00 bytes 048a0194
~~~


<a id="compare-9ce5ba7bcc2dfcfda4eb330c09352acd"></a>

### [`00bfbb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md) → [`00bfbc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbba4) · [`00bfbbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbbb0) · [`00bfbbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbbcc)
- 新版 `00bfbc40`（命令位置の公開資料なし） · `00bfbc4c`（命令位置の公開資料なし） · `00bfbc68`（命令位置の公開資料なし）

~~~diff
- 00bfbba4 ["INT_ADD", "register:40f0:8", ["const:bfbba4:8", "const:4:8"]]
- 00bfbba4 ["CALL", null, ["callee:00c5e3a0:8"]]
+ 00bfbc40 ["INT_ADD", "register:40f0:8", ["const:bfbc40:8", "const:4:8"]]
+ 00bfbc40 ["CALL", null, ["callee:00c5e3a0:8"]]
- 00bfbba4 bytes cb890194
+ 00bfbc40 bytes d8890194
- 00bfbbb0 ["INT_ADD", "register:40f0:8", ["const:bfbbb0:8", "const:4:8"]]
- 00bfbbb0 ["CALL", null, ["callee:00c5e3e0:8"]]
+ 00bfbc4c ["INT_ADD", "register:40f0:8", ["const:bfbc4c:8", "const:4:8"]]
+ 00bfbc4c ["CALL", null, ["callee:00c5e3e0:8"]]
- 00bfbbb0 bytes d8890194
+ 00bfbc4c bytes e5890194
- 00bfbbcc ["INT_ADD", "register:40f0:8", ["const:bfbbcc:8", "const:4:8"]]
- 00bfbbcc ["CALL", null, ["callee:00c5e3a0:8"]]
+ 00bfbc68 ["INT_ADD", "register:40f0:8", ["const:bfbc68:8", "const:4:8"]]
+ 00bfbc68 ["CALL", null, ["callee:00c5e3a0:8"]]
- 00bfbbcc bytes c1890194
+ 00bfbc68 bytes ce890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3275953293310c67470ae1fd231d859"></a>

### [`00bfbc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc10.md) → [`00bfbcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcac.md) FUN_00bfbcac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e350.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc10.md#insn-00bfbc24)
- 新版 `00bfbcc0`（命令位置の公開資料なし）

~~~diff
- 00bfbc24 ["INT_ADD", "register:40f0:8", ["const:bfbc24:8", "const:4:8"]]
- 00bfbc24 ["CALL", null, ["callee:00c5e420:8"]]
+ 00bfbcc0 ["INT_ADD", "register:40f0:8", ["const:bfbcc0:8", "const:4:8"]]
+ 00bfbcc0 ["CALL", null, ["callee:00c5e420:8"]]
- 00bfbc24 bytes cb890194
+ 00bfbcc0 bytes d8890194
~~~


<a id="compare-8d4b0483e4e8c0a5b8a7c94931f7e46d"></a>

### [`00bfbc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md) → [`00bfbcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcd8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md#insn-00bfbc64) · [`00bfbc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md#insn-00bfbc70)
- 新版 `00bfbd00`（命令位置の公開資料なし） · `00bfbd0c`（命令位置の公開資料なし）

~~~diff
- 00bfbc64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfbc64 ["INT_ADD", "register:40f0:8", ["const:bfbc64:8", "const:4:8"]]
- 00bfbc64 ["CALLIND", null, ["register:0:8"]]
+ 00bfbd00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfbd00 ["INT_ADD", "register:40f0:8", ["const:bfbd00:8", "const:4:8"]]
+ 00bfbd00 ["CALLIND", null, ["register:0:8"]]
- 00bfbc64 bytes 20013fd6
+ 00bfbd00 bytes 20013fd6
- 00bfbc70 ["INT_ADD", "register:40f0:8", ["const:bfbc70:8", "const:4:8"]]
- 00bfbc70 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfbd0c ["INT_ADD", "register:40f0:8", ["const:bfbd0c:8", "const:4:8"]]
+ 00bfbd0c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfbc70 bytes d87a0194
+ 00bfbd0c bytes e57a0194
~~~


<a id="compare-47be016882b36d68a0ecee7aed54f7cb"></a>

### [`00bfbd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md) → [`00bfbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbda0.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md#insn-00bfbd44)
- 新版 `00bfbde0`（命令位置の公開資料なし）

~~~diff
- 00bfbd44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfbd44 ["INT_ADD", "register:40f0:8", ["const:bfbd44:8", "const:4:8"]]
- 00bfbd44 ["CALLIND", null, ["register:0:8"]]
+ 00bfbde0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfbde0 ["INT_ADD", "register:40f0:8", ["const:bfbde0:8", "const:4:8"]]
+ 00bfbde0 ["CALLIND", null, ["register:0:8"]]
- 00bfbd44 bytes 00013fd6
+ 00bfbde0 bytes 00013fd6
~~~


<a id="compare-62f7a11f46a8035445f45ad2ad18436f"></a>

### [`00bfbf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf38.md) → [`00bfbfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbfd4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf38.md#insn-00bfbf58)
- 新版 `00bfbff4`（命令位置の公開資料なし）

~~~diff
- 00bfbf58 ["INT_ADD", "register:40f0:8", ["const:bfbf58:8", "const:4:8"]]
- 00bfbf58 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfbff4 ["INT_ADD", "register:40f0:8", ["const:bfbff4:8", "const:4:8"]]
+ 00bfbff4 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfbf58 bytes e2880194
+ 00bfbff4 bytes ef880194
~~~


<a id="compare-731cd2d75cab247853de2669fc9792a9"></a>

### [`00bfbf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md) → [`00bfc024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc024.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfac) · [`00bfbfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfb8) · [`00bfbfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfc4)
- 新版 `00bfc048`（命令位置の公開資料なし） · `00bfc054`（命令位置の公開資料なし） · `00bfc060`（命令位置の公開資料なし）

~~~diff
- 00bfbfac ["INT_ADD", "register:40f0:8", ["const:bfbfac:8", "const:4:8"]]
- 00bfbfac ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfc048 ["INT_ADD", "register:40f0:8", ["const:bfc048:8", "const:4:8"]]
+ 00bfc048 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfbfac bytes 097a0194
+ 00bfc048 bytes 167a0194
- 00bfbfb8 ["INT_ADD", "register:40f0:8", ["const:bfbfb8:8", "const:4:8"]]
- 00bfbfb8 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfc054 ["INT_ADD", "register:40f0:8", ["const:bfc054:8", "const:4:8"]]
+ 00bfc054 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfbfb8 bytes ca880194
+ 00bfc054 bytes d7880194
- 00bfbfc4 ["INT_ADD", "register:40f0:8", ["const:bfbfc4:8", "const:4:8"]]
- 00bfbfc4 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bfc060 ["INT_ADD", "register:40f0:8", ["const:bfc060:8", "const:4:8"]]
+ 00bfc060 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bfbfc4 bytes c7880194
+ 00bfc060 bytes d4880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777d2ecf22606f622fada354ab957c1e"></a>

### [`00bfc08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc08c.md) → [`00bfc128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc128.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc08c.md#insn-00bfc0c8)
- 新版 `00bfc164`（命令位置の公開資料なし）

~~~diff
- 00bfc0c8 ["INT_ADD", "register:40f0:8", ["const:bfc0c8:8", "const:4:8"]]
- 00bfc0c8 ["CALL", null, ["callee:00c582b0:8"]]
+ 00bfc164 ["INT_ADD", "register:40f0:8", ["const:bfc164:8", "const:4:8"]]
+ 00bfc164 ["CALL", null, ["callee:00c582b0:8"]]
- 00bfc0c8 bytes 46700194
+ 00bfc164 bytes 53700194
~~~


<a id="compare-88944e7c51191b097ccff5919461b2cc"></a>

### [`00bfc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc15c.md) → [`00bfc1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc1f8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc15c.md#insn-00bfc194)
- 新版 `00bfc230`（命令位置の公開資料なし）

~~~diff
- 00bfc194 ["INT_ADD", "register:40f0:8", ["const:bfc194:8", "const:4:8"]]
- 00bfc194 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00bfc230 ["INT_ADD", "register:40f0:8", ["const:bfc230:8", "const:4:8"]]
+ 00bfc230 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00bfc194 bytes 63880194
+ 00bfc230 bytes 70880194
~~~


<a id="compare-932dfeb59e96b139e3ac5e76bfb93c8f"></a>

### [`00bfc3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3ac.md) → [`00bfc448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc448.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3ac.md#insn-00bfc3cc)
- 新版 `00bfc468`（命令位置の公開資料なし）

~~~diff
- 00bfc3cc ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfc3cc ["INT_ADD", "register:40f0:8", ["const:bfc3cc:8", "const:4:8"]]
- 00bfc3cc ["CALLIND", null, ["register:0:8"]]
+ 00bfc468 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfc468 ["INT_ADD", "register:40f0:8", ["const:bfc468:8", "const:4:8"]]
+ 00bfc468 ["CALLIND", null, ["register:0:8"]]
- 00bfc3cc bytes 20003fd6
+ 00bfc468 bytes 20003fd6
~~~


<a id="compare-a4ce3661414e171218426ad72e9bbee0"></a>

### [`00bfc3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3e4.md) → [`00bfc480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc480.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3e4.md#insn-00bfc404)
- 新版 `00bfc4a0`（命令位置の公開資料なし）

~~~diff
- 00bfc404 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfc404 ["INT_ADD", "register:40f0:8", ["const:bfc404:8", "const:4:8"]]
- 00bfc404 ["CALLIND", null, ["register:0:8"]]
+ 00bfc4a0 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfc4a0 ["INT_ADD", "register:40f0:8", ["const:bfc4a0:8", "const:4:8"]]
+ 00bfc4a0 ["CALLIND", null, ["register:0:8"]]
- 00bfc404 bytes 20003fd6
+ 00bfc4a0 bytes 20003fd6
~~~


<a id="compare-e148214d933422b9d7ba30cccc93df64"></a>

### [`00bfc41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md) → [`00bfc4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc44c) · [`00bfc4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc4b0) · [`00bfc4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc4e8)
- 新版 `00bfc4e8`（命令位置の公開資料なし） · `00bfc54c`（命令位置の公開資料なし） · `00bfc584`（命令位置の公開資料なし）

~~~diff
- 00bfc44c ["INT_ADD", "register:40f0:8", ["const:bfc44c:8", "const:4:8"]]
- 00bfc44c ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfc4e8 ["INT_ADD", "register:40f0:8", ["const:bfc4e8:8", "const:4:8"]]
+ 00bfc4e8 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfc44c bytes 61760194
+ 00bfc4e8 bytes 6e760194
- 00bfc4b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc4b0 ["INT_ADD", "register:40f0:8", ["const:bfc4b0:8", "const:4:8"]]
- 00bfc4b0 ["CALLIND", null, ["register:0:8"]]
+ 00bfc54c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc54c ["INT_ADD", "register:40f0:8", ["const:bfc54c:8", "const:4:8"]]
+ 00bfc54c ["CALLIND", null, ["register:0:8"]]
- 00bfc4b0 bytes 00013fd6
+ 00bfc54c bytes 00013fd6
- 00bfc4e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc4e8 ["INT_ADD", "register:40f0:8", ["const:bfc4e8:8", "const:4:8"]]
- 00bfc4e8 ["CALLIND", null, ["register:0:8"]]
+ 00bfc584 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc584 ["INT_ADD", "register:40f0:8", ["const:bfc584:8", "const:4:8"]]
+ 00bfc584 ["CALLIND", null, ["register:0:8"]]
- 00bfc4e8 bytes 00013fd6
+ 00bfc584 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e6453b95fc8391ad9d3fe0d6a9c3ee"></a>

### [`00bfd62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md) → [`00bfd6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e360.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c5e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e430.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd654) · [`00bfd69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd69c) · [`00bfd6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd6cc)
- 新版 `00bfd6f0`（命令位置の公開資料なし） · `00bfd738`（命令位置の公開資料なし） · `00bfd768`（命令位置の公開資料なし）

~~~diff
- 00bfd654 ["INT_ADD", "register:40f0:8", ["const:bfd654:8", "const:4:8"]]
- 00bfd654 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfd6f0 ["INT_ADD", "register:40f0:8", ["const:bfd6f0:8", "const:4:8"]]
+ 00bfd6f0 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfd654 bytes df710194
+ 00bfd6f0 bytes ec710194
- 00bfd69c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd69c ["INT_ADD", "register:40f0:8", ["const:bfd69c:8", "const:4:8"]]
- 00bfd69c ["CALLIND", null, ["register:0:8"]]
+ 00bfd738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd738 ["INT_ADD", "register:40f0:8", ["const:bfd738:8", "const:4:8"]]
+ 00bfd738 ["CALLIND", null, ["register:0:8"]]
- 00bfd69c bytes 00013fd6
+ 00bfd738 bytes 00013fd6
- 00bfd6cc ["INT_ADD", "register:40f0:8", ["const:bfd6cc:8", "const:4:8"]]
- 00bfd6cc ["CALL", null, ["callee:00c58370:8"]]
+ 00bfd768 ["INT_ADD", "register:40f0:8", ["const:bfd768:8", "const:4:8"]]
+ 00bfd768 ["CALL", null, ["callee:00c58370:8"]]
- 00bfd6cc bytes f56a0194
+ 00bfd768 bytes 026b0194
~~~


<a id="compare-1a1aaf2a6ddbfe418890215a228526fc"></a>

### [`00bfd744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd744.md) → [`00bfd7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd7e0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd744.md#insn-00bfd75c)
- 新版 `00bfd7f8`（命令位置の公開資料なし）

~~~diff
- 00bfd75c ["INT_ADD", "register:40f0:8", ["const:bfd75c:8", "const:4:8"]]
- 00bfd75c ["CALL", null, ["callee:00c5e430:8"]]
+ 00bfd7f8 ["INT_ADD", "register:40f0:8", ["const:bfd7f8:8", "const:4:8"]]
+ 00bfd7f8 ["CALL", null, ["callee:00c5e430:8"]]
- 00bfd75c bytes 01830194
+ 00bfd7f8 bytes 0e830194
~~~


<a id="compare-e0f9148f18a6ecf1fd87bc43126b9ab7"></a>

### [`00bfd824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md) → [`00bfd8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd8c0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e370.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c5e440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e440.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd860) · [`00bfd8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd8dc) · [`00bfd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd91c)
- 新版 `00bfd8fc`（命令位置の公開資料なし） · `00bfd978`（命令位置の公開資料なし） · `00bfd9b8`（命令位置の公開資料なし）

~~~diff
- 00bfd860 ["INT_ADD", "register:40f0:8", ["const:bfd860:8", "const:4:8"]]
- 00bfd860 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfd8fc ["INT_ADD", "register:40f0:8", ["const:bfd8fc:8", "const:4:8"]]
+ 00bfd8fc ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfd860 bytes 5c710194
+ 00bfd8fc bytes 69710194
- 00bfd8dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd8dc ["INT_ADD", "register:40f0:8", ["const:bfd8dc:8", "const:4:8"]]
- 00bfd8dc ["CALLIND", null, ["register:0:8"]]
+ 00bfd978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd978 ["INT_ADD", "register:40f0:8", ["const:bfd978:8", "const:4:8"]]
+ 00bfd978 ["CALLIND", null, ["register:0:8"]]
- 00bfd8dc bytes 00013fd6
+ 00bfd978 bytes 00013fd6
- 00bfd91c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd91c ["INT_ADD", "register:40f0:8", ["const:bfd91c:8", "const:4:8"]]
- 00bfd91c ["CALLIND", null, ["register:0:8"]]
+ 00bfd9b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd9b8 ["INT_ADD", "register:40f0:8", ["const:bfd9b8:8", "const:4:8"]]
+ 00bfd9b8 ["CALLIND", null, ["register:0:8"]]
- 00bfd91c bytes 00013fd6
+ 00bfd9b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e0564eeecf6497eaa9b6dc6367a5345"></a>

### [`00bfda8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md) → [`00bfdb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e380.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c5e450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e450.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdac0) · [`00bfdb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdb24) · [`00bfdb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdb68)
- 新版 `00bfdb5c`（命令位置の公開資料なし） · `00bfdbc0`（命令位置の公開資料なし） · `00bfdc04`（命令位置の公開資料なし）

~~~diff
- 00bfdac0 ["INT_ADD", "register:40f0:8", ["const:bfdac0:8", "const:4:8"]]
- 00bfdac0 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfdb5c ["INT_ADD", "register:40f0:8", ["const:bfdb5c:8", "const:4:8"]]
+ 00bfdb5c ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfdac0 bytes c4700194
+ 00bfdb5c bytes d1700194
- 00bfdb24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdb24 ["INT_ADD", "register:40f0:8", ["const:bfdb24:8", "const:4:8"]]
- 00bfdb24 ["CALLIND", null, ["register:0:8"]]
+ 00bfdbc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdbc0 ["INT_ADD", "register:40f0:8", ["const:bfdbc0:8", "const:4:8"]]
+ 00bfdbc0 ["CALLIND", null, ["register:0:8"]]
- 00bfdb24 bytes 00013fd6
+ 00bfdbc0 bytes 00013fd6
- 00bfdb68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdb68 ["INT_ADD", "register:40f0:8", ["const:bfdb68:8", "const:4:8"]]
- 00bfdb68 ["CALLIND", null, ["register:0:8"]]
+ 00bfdc04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdc04 ["INT_ADD", "register:40f0:8", ["const:bfdc04:8", "const:4:8"]]
+ 00bfdc04 ["CALLIND", null, ["register:0:8"]]
- 00bfdb68 bytes 00013fd6
+ 00bfdc04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0162eee0da6513944a43de132579704e"></a>

### [`00bfdca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md) → [`00bfdd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e390.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c5e460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e460.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdce0) · [`00bfdd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdd24) · [`00bfdd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdd7c)
- 新版 `00bfdd7c`（命令位置の公開資料なし） · `00bfddc0`（命令位置の公開資料なし） · `00bfde18`（命令位置の公開資料なし）

~~~diff
- 00bfdce0 ["INT_ADD", "register:40f0:8", ["const:bfdce0:8", "const:4:8"]]
- 00bfdce0 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfdd7c ["INT_ADD", "register:40f0:8", ["const:bfdd7c:8", "const:4:8"]]
+ 00bfdd7c ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfdce0 bytes 3c700194
+ 00bfdd7c bytes 49700194
- 00bfdd24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdd24 ["INT_ADD", "register:40f0:8", ["const:bfdd24:8", "const:4:8"]]
- 00bfdd24 ["CALLIND", null, ["register:0:8"]]
+ 00bfddc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfddc0 ["INT_ADD", "register:40f0:8", ["const:bfddc0:8", "const:4:8"]]
+ 00bfddc0 ["CALLIND", null, ["register:0:8"]]
- 00bfdd24 bytes 00013fd6
+ 00bfddc0 bytes 00013fd6
- 00bfdd7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdd7c ["INT_ADD", "register:40f0:8", ["const:bfdd7c:8", "const:4:8"]]
- 00bfdd7c ["CALLIND", null, ["register:0:8"]]
+ 00bfde18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfde18 ["INT_ADD", "register:40f0:8", ["const:bfde18:8", "const:4:8"]]
+ 00bfde18 ["CALLIND", null, ["register:0:8"]]
- 00bfdd7c bytes 00013fd6
+ 00bfde18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cdebc5a98e4816ee9be1490adc2238d"></a>

### [`00bfdee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md) → [`00bfdf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdf18) · [`00bfdf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdf70) · [`00bfdfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdfec)
- 新版 `00bfdfb4`（命令位置の公開資料なし） · `00bfe00c`（命令位置の公開資料なし） · `00bfe088`（命令位置の公開資料なし）

~~~diff
- 00bfdf18 ["INT_ADD", "register:40f0:8", ["const:bfdf18:8", "const:4:8"]]
- 00bfdf18 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfdfb4 ["INT_ADD", "register:40f0:8", ["const:bfdfb4:8", "const:4:8"]]
+ 00bfdfb4 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfdf18 bytes ae6f0194
+ 00bfdfb4 bytes bb6f0194
- 00bfdf70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdf70 ["INT_ADD", "register:40f0:8", ["const:bfdf70:8", "const:4:8"]]
- 00bfdf70 ["CALLIND", null, ["register:0:8"]]
+ 00bfe00c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe00c ["INT_ADD", "register:40f0:8", ["const:bfe00c:8", "const:4:8"]]
+ 00bfe00c ["CALLIND", null, ["register:0:8"]]
- 00bfdf70 bytes 00013fd6
+ 00bfe00c bytes 00013fd6
- 00bfdfec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdfec ["INT_ADD", "register:40f0:8", ["const:bfdfec:8", "const:4:8"]]
- 00bfdfec ["CALLIND", null, ["register:0:8"]]
+ 00bfe088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe088 ["INT_ADD", "register:40f0:8", ["const:bfe088:8", "const:4:8"]]
+ 00bfe088 ["CALLIND", null, ["register:0:8"]]
- 00bfdfec bytes 00013fd6
+ 00bfe088 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf15130f168d59870de97bac9a6f5b0d"></a>

### [`00bfe0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md) → [`00bfe13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe13c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe0c8) · [`00bfe108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe108) · [`00bfe130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe130)
- 新版 `00bfe164`（命令位置の公開資料なし） · `00bfe1a4`（命令位置の公開資料なし） · `00bfe1cc`（命令位置の公開資料なし）

~~~diff
- 00bfe0c8 ["INT_ADD", "register:40f0:8", ["const:bfe0c8:8", "const:4:8"]]
- 00bfe0c8 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe164 ["INT_ADD", "register:40f0:8", ["const:bfe164:8", "const:4:8"]]
+ 00bfe164 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe0c8 bytes 426f0194
+ 00bfe164 bytes 4f6f0194
- 00bfe108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe108 ["INT_ADD", "register:40f0:8", ["const:bfe108:8", "const:4:8"]]
- 00bfe108 ["CALLIND", null, ["register:0:8"]]
+ 00bfe1a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe1a4 ["INT_ADD", "register:40f0:8", ["const:bfe1a4:8", "const:4:8"]]
+ 00bfe1a4 ["CALLIND", null, ["register:0:8"]]
- 00bfe108 bytes 00013fd6
+ 00bfe1a4 bytes 00013fd6
- 00bfe130 ["INT_ADD", "register:40f0:8", ["const:bfe130:8", "const:4:8"]]
- 00bfe130 ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe1cc ["INT_ADD", "register:40f0:8", ["const:bfe1cc:8", "const:4:8"]]
+ 00bfe1cc ["CALL", null, ["callee:00c58370:8"]]
- 00bfe130 bytes 5c680194
+ 00bfe1cc bytes 69680194
~~~


<a id="compare-f42b3697397c9e2ef2565a9c6bfab1cf"></a>

### [`00bfe1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md) → [`00bfe23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe23c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590d0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591a0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe1d0) · [`00bfe1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe1fc) · [`00bfe22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe22c)
- 新版 `00bfe26c`（命令位置の公開資料なし） · `00bfe298`（命令位置の公開資料なし） · `00bfe2c8`（命令位置の公開資料なし）

~~~diff
- 00bfe1d0 ["INT_ADD", "register:40f0:8", ["const:bfe1d0:8", "const:4:8"]]
- 00bfe1d0 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe26c ["INT_ADD", "register:40f0:8", ["const:bfe26c:8", "const:4:8"]]
+ 00bfe26c ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe1d0 bytes 006f0194
+ 00bfe26c bytes 0d6f0194
- 00bfe1fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe1fc ["INT_ADD", "register:40f0:8", ["const:bfe1fc:8", "const:4:8"]]
- 00bfe1fc ["CALLIND", null, ["register:0:8"]]
+ 00bfe298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe298 ["INT_ADD", "register:40f0:8", ["const:bfe298:8", "const:4:8"]]
+ 00bfe298 ["CALLIND", null, ["register:0:8"]]
- 00bfe1fc bytes 00013fd6
+ 00bfe298 bytes 00013fd6
- 00bfe22c ["INT_ADD", "register:40f0:8", ["const:bfe22c:8", "const:4:8"]]
- 00bfe22c ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe2c8 ["INT_ADD", "register:40f0:8", ["const:bfe2c8:8", "const:4:8"]]
+ 00bfe2c8 ["CALL", null, ["callee:00c58370:8"]]
- 00bfe22c bytes 1d680194
+ 00bfe2c8 bytes 2a680194
~~~


<a id="compare-ad3cd21667a2ca41efdc7de75dad3cbf"></a>

### [`00bfe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md) → [`00bfe334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe334.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe2c8) · [`00bfe308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe308) · [`00bfe354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe354)
- 新版 `00bfe364`（命令位置の公開資料なし） · `00bfe3a4`（命令位置の公開資料なし） · `00bfe3f0`（命令位置の公開資料なし）

~~~diff
- 00bfe2c8 ["INT_ADD", "register:40f0:8", ["const:bfe2c8:8", "const:4:8"]]
- 00bfe2c8 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe364 ["INT_ADD", "register:40f0:8", ["const:bfe364:8", "const:4:8"]]
+ 00bfe364 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe2c8 bytes c26e0194
+ 00bfe364 bytes cf6e0194
- 00bfe308 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe308 ["INT_ADD", "register:40f0:8", ["const:bfe308:8", "const:4:8"]]
- 00bfe308 ["CALLIND", null, ["register:0:8"]]
+ 00bfe3a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe3a4 ["INT_ADD", "register:40f0:8", ["const:bfe3a4:8", "const:4:8"]]
+ 00bfe3a4 ["CALLIND", null, ["register:0:8"]]
- 00bfe308 bytes 00013fd6
+ 00bfe3a4 bytes 00013fd6
- 00bfe354 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfe354 ["INT_ADD", "register:40f0:8", ["const:bfe354:8", "const:4:8"]]
- 00bfe354 ["CALLIND", null, ["register:0:8"]]
+ 00bfe3f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfe3f0 ["INT_ADD", "register:40f0:8", ["const:bfe3f0:8", "const:4:8"]]
+ 00bfe3f0 ["CALLIND", null, ["register:0:8"]]
- 00bfe354 bytes 20013fd6
+ 00bfe3f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6397b0ad6b8eaa03e049083a71916eee"></a>

### [`00bfe3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md) → [`00bfe484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe484.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe428) · [`00bfe438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe438) · [`00bfe48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe48c)
- 新版 `00bfe4c4`（命令位置の公開資料なし） · `00bfe4d4`（命令位置の公開資料なし） · `00bfe528`（命令位置の公開資料なし）

~~~diff
- 00bfe428 ["INT_ADD", "register:40f0:8", ["const:bfe428:8", "const:4:8"]]
- 00bfe428 ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe4c4 ["INT_ADD", "register:40f0:8", ["const:bfe4c4:8", "const:4:8"]]
+ 00bfe4c4 ["CALL", null, ["callee:00c58370:8"]]
- 00bfe428 bytes 9e670194
+ 00bfe4c4 bytes ab670194
- 00bfe438 ["INT_ADD", "register:40f0:8", ["const:bfe438:8", "const:4:8"]]
- 00bfe438 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe4d4 ["INT_ADD", "register:40f0:8", ["const:bfe4d4:8", "const:4:8"]]
+ 00bfe4d4 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe438 bytes 666e0194
+ 00bfe4d4 bytes 736e0194
- 00bfe48c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe48c ["INT_ADD", "register:40f0:8", ["const:bfe48c:8", "const:4:8"]]
- 00bfe48c ["CALLIND", null, ["register:0:8"]]
+ 00bfe528 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe528 ["INT_ADD", "register:40f0:8", ["const:bfe528:8", "const:4:8"]]
+ 00bfe528 ["CALLIND", null, ["register:0:8"]]
- 00bfe48c bytes 00013fd6
+ 00bfe528 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1143811ff5fcf09a6596129d1feeccc8"></a>

### [`00bfe51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md) → [`00bfe5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe558) · [`00bfe568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe568) · [`00bfe5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe5b4)
- 新版 `00bfe5f4`（命令位置の公開資料なし） · `00bfe604`（命令位置の公開資料なし） · `00bfe650`（命令位置の公開資料なし）

~~~diff
- 00bfe558 ["INT_ADD", "register:40f0:8", ["const:bfe558:8", "const:4:8"]]
- 00bfe558 ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe5f4 ["INT_ADD", "register:40f0:8", ["const:bfe5f4:8", "const:4:8"]]
+ 00bfe5f4 ["CALL", null, ["callee:00c58370:8"]]
- 00bfe558 bytes 52670194
+ 00bfe5f4 bytes 5f670194
- 00bfe568 ["INT_ADD", "register:40f0:8", ["const:bfe568:8", "const:4:8"]]
- 00bfe568 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe604 ["INT_ADD", "register:40f0:8", ["const:bfe604:8", "const:4:8"]]
+ 00bfe604 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe568 bytes 1a6e0194
+ 00bfe604 bytes 276e0194
- 00bfe5b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe5b4 ["INT_ADD", "register:40f0:8", ["const:bfe5b4:8", "const:4:8"]]
- 00bfe5b4 ["CALLIND", null, ["register:0:8"]]
+ 00bfe650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe650 ["INT_ADD", "register:40f0:8", ["const:bfe650:8", "const:4:8"]]
+ 00bfe650 ["CALLIND", null, ["register:0:8"]]
- 00bfe5b4 bytes 00013fd6
+ 00bfe650 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4efe70e3a69bcd37dd989cb3607f27"></a>

### [`00bfe644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md) → [`00bfe6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe6e0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe668) · [`00bfe690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe690) · [`00bfe6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe6b4)
- 新版 `00bfe704`（命令位置の公開資料なし） · `00bfe72c`（命令位置の公開資料なし） · `00bfe750`（命令位置の公開資料なし）

~~~diff
- 00bfe668 ["INT_ADD", "register:40f0:8", ["const:bfe668:8", "const:4:8"]]
- 00bfe668 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe704 ["INT_ADD", "register:40f0:8", ["const:bfe704:8", "const:4:8"]]
+ 00bfe704 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe668 bytes da6d0194
+ 00bfe704 bytes e76d0194
- 00bfe690 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe690 ["INT_ADD", "register:40f0:8", ["const:bfe690:8", "const:4:8"]]
- 00bfe690 ["CALLIND", null, ["register:0:8"]]
+ 00bfe72c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe72c ["INT_ADD", "register:40f0:8", ["const:bfe72c:8", "const:4:8"]]
+ 00bfe72c ["CALLIND", null, ["register:0:8"]]
- 00bfe690 bytes 00013fd6
+ 00bfe72c bytes 00013fd6
- 00bfe6b4 ["INT_ADD", "register:40f0:8", ["const:bfe6b4:8", "const:4:8"]]
- 00bfe6b4 ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe750 ["INT_ADD", "register:40f0:8", ["const:bfe750:8", "const:4:8"]]
+ 00bfe750 ["CALL", null, ["callee:00c58370:8"]]
- 00bfe6b4 bytes fb660194
+ 00bfe750 bytes 08670194
~~~


<a id="compare-2b92c9c24cd8225d3d9606e8404b1d9b"></a>

### [`00bfe734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md) → [`00bfe7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe7d0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59800.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00c598d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598d0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe770) · [`00bfe780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe780) · [`00bfe7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe7b0)
- 新版 `00bfe80c`（命令位置の公開資料なし） · `00bfe81c`（命令位置の公開資料なし） · `00bfe84c`（命令位置の公開資料なし）

~~~diff
- 00bfe770 ["INT_ADD", "register:40f0:8", ["const:bfe770:8", "const:4:8"]]
- 00bfe770 ["CALL", null, ["callee:00c58370:8"]]
+ 00bfe80c ["INT_ADD", "register:40f0:8", ["const:bfe80c:8", "const:4:8"]]
+ 00bfe80c ["CALL", null, ["callee:00c58370:8"]]
- 00bfe770 bytes cc660194
+ 00bfe80c bytes d9660194
- 00bfe780 ["INT_ADD", "register:40f0:8", ["const:bfe780:8", "const:4:8"]]
- 00bfe780 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfe81c ["INT_ADD", "register:40f0:8", ["const:bfe81c:8", "const:4:8"]]
+ 00bfe81c ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfe780 bytes 946d0194
+ 00bfe81c bytes a16d0194
- 00bfe7b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe7b0 ["INT_ADD", "register:40f0:8", ["const:bfe7b0:8", "const:4:8"]]
- 00bfe7b0 ["CALLIND", null, ["register:0:8"]]
+ 00bfe84c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe84c ["INT_ADD", "register:40f0:8", ["const:bfe84c:8", "const:4:8"]]
+ 00bfe84c ["CALLIND", null, ["register:0:8"]]
- 00bfe7b0 bytes 00013fd6
+ 00bfe84c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3d118e32ff64794f469abee3e804fce"></a>

### [`00bfe844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe844.md) → [`00bfe8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe8e0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe844.md#insn-00bfe87c)
- 新版 `00bfe918`（命令位置の公開資料なし）

~~~diff
- 00bfe87c ["INT_ADD", "register:40f0:8", ["const:bfe87c:8", "const:4:8"]]
- 00bfe87c ["CALL", null, ["callee:00c582b0:8"]]
+ 00bfe918 ["INT_ADD", "register:40f0:8", ["const:bfe918:8", "const:4:8"]]
+ 00bfe918 ["CALL", null, ["callee:00c582b0:8"]]
- 00bfe87c bytes 59660194
+ 00bfe918 bytes 66660194
~~~


<a id="compare-f5a3f60cfd1c6df2b5fd151844b46626"></a>

### [`00bfe910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md) → [`00bfe9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe9ac.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md#insn-00bfe940)
- 新版 `00bfe9dc`（命令位置の公開資料なし）

~~~diff
- 00bfe940 ["INT_ADD", "register:40f0:8", ["const:bfe940:8", "const:4:8"]]
- 00bfe940 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00bfe9dc ["INT_ADD", "register:40f0:8", ["const:bfe9dc:8", "const:4:8"]]
+ 00bfe9dc ["CALL", null, ["callee:00c5e3f0:8"]]
- 00bfe940 bytes 787e0194
+ 00bfe9dc bytes 857e0194
~~~


<a id="compare-3216d65199a7af8c6362ccbb9ef47fe5"></a>

### [`00bfe974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe974.md) → [`00bfea10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea10.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) · 呼出先 1件 [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)
- 新版 呼出元 1件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) · 呼出先 1件 [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe974.md#insn-00bfe9b8)
- 新版 `00bfea54`（命令位置の公開資料なし）

~~~diff
- 00bfe9b8 ["INT_ADD", "register:40f0:8", ["const:bfe9b8:8", "const:4:8"]]
- 00bfe9b8 ["CALL", null, ["callee:00c58fc0:8"]]
+ 00bfea54 ["INT_ADD", "register:40f0:8", ["const:bfea54:8", "const:4:8"]]
+ 00bfea54 ["CALL", null, ["callee:00c58fc0:8"]]
- 00bfe9b8 bytes 4e690194
+ 00bfea54 bytes 5b690194
~~~


<a id="compare-764030ab98377d80a961f9da059c0ee1"></a>

### [`00bfe9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md) → [`00bfea74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea74.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md)
- 新版 呼出元 1件 [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfea14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea14) · [`00bfea38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea38) · [`00bfea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea5c)
- 新版 `00bfeab0`（命令位置の公開資料なし） · `00bfead4`（命令位置の公開資料なし） · `00bfeaf8`（命令位置の公開資料なし）

~~~diff
- 00bfea14 ["INT_ADD", "register:40f0:8", ["const:bfea14:8", "const:4:8"]]
- 00bfea14 ["CALL", null, ["callee:00c5d1c0:8"]]
+ 00bfeab0 ["INT_ADD", "register:40f0:8", ["const:bfeab0:8", "const:4:8"]]
+ 00bfeab0 ["CALL", null, ["callee:00c5d1c0:8"]]
- 00bfea14 bytes b7790194
+ 00bfeab0 bytes c4790194
- 00bfea38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfea38 ["INT_ADD", "register:40f0:8", ["const:bfea38:8", "const:4:8"]]
- 00bfea38 ["CALLIND", null, ["register:0:8"]]
+ 00bfead4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfead4 ["INT_ADD", "register:40f0:8", ["const:bfead4:8", "const:4:8"]]
+ 00bfead4 ["CALLIND", null, ["register:0:8"]]
- 00bfea38 bytes 00013fd6
+ 00bfead4 bytes 00013fd6
- 00bfea5c ["INT_ADD", "register:40f0:8", ["const:bfea5c:8", "const:4:8"]]
- 00bfea5c ["CALL", null, ["callee:00c58370:8"]]
+ 00bfeaf8 ["INT_ADD", "register:40f0:8", ["const:bfeaf8:8", "const:4:8"]]
+ 00bfeaf8 ["CALL", null, ["callee:00c58370:8"]]
- 00bfea5c bytes 11660194
+ 00bfeaf8 bytes 1e660194
~~~


<a id="compare-5ebfb06603d0682e7b19804581ec55ff"></a>

### [`00bfea8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfea8c.md) → [`00bfeb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb28.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfeaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfea8c.md#insn-00bfeaac)
- 新版 `00bfeb48`（命令位置の公開資料なし）

~~~diff
- 00bfeaac ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfeaac ["INT_ADD", "register:40f0:8", ["const:bfeaac:8", "const:4:8"]]
- 00bfeaac ["CALLIND", null, ["register:0:8"]]
+ 00bfeb48 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfeb48 ["INT_ADD", "register:40f0:8", ["const:bfeb48:8", "const:4:8"]]
+ 00bfeb48 ["CALLIND", null, ["register:0:8"]]
- 00bfeaac bytes 20003fd6
+ 00bfeb48 bytes 20003fd6
~~~


<a id="compare-8c879348f058476266940f40e1fcc8f3"></a>

### [`00bfeac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfeac4.md) → [`00bfeb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb60.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfeae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfeac4.md#insn-00bfeae4)
- 新版 `00bfeb80`（命令位置の公開資料なし）

~~~diff
- 00bfeae4 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfeae4 ["INT_ADD", "register:40f0:8", ["const:bfeae4:8", "const:4:8"]]
- 00bfeae4 ["CALLIND", null, ["register:0:8"]]
+ 00bfeb80 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfeb80 ["INT_ADD", "register:40f0:8", ["const:bfeb80:8", "const:4:8"]]
+ 00bfeb80 ["CALLIND", null, ["register:0:8"]]
- 00bfeae4 bytes 20003fd6
+ 00bfeb80 bytes 20003fd6
~~~


<a id="compare-19b437e4bd4e8dafc929f370ea88b64d"></a>

### [`00bff464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md) → [`00bff500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff500.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff488) · [`00bff4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff4d0) · [`00bff4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff4f0)
- 新版 `00bff524`（命令位置の公開資料なし） · `00bff56c`（命令位置の公開資料なし） · `00bff58c`（命令位置の公開資料なし）

~~~diff
- 00bff488 ["INT_ADD", "register:40f0:8", ["const:bff488:8", "const:4:8"]]
- 00bff488 ["CALL", null, ["callee:00c58330:8"]]
+ 00bff524 ["INT_ADD", "register:40f0:8", ["const:bff524:8", "const:4:8"]]
+ 00bff524 ["CALL", null, ["callee:00c58330:8"]]
- 00bff488 bytes 76630194
+ 00bff524 bytes 83630194
- 00bff4d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff4d0 ["INT_ADD", "register:40f0:8", ["const:bff4d0:8", "const:4:8"]]
- 00bff4d0 ["CALLIND", null, ["register:0:8"]]
+ 00bff56c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff56c ["INT_ADD", "register:40f0:8", ["const:bff56c:8", "const:4:8"]]
+ 00bff56c ["CALLIND", null, ["register:0:8"]]
- 00bff4d0 bytes 00013fd6
+ 00bff56c bytes 00013fd6
- 00bff4f0 ["INT_ADD", "register:40f0:8", ["const:bff4f0:8", "const:4:8"]]
- 00bff4f0 ["CALL", null, ["callee:00c58370:8"]]
+ 00bff58c ["INT_ADD", "register:40f0:8", ["const:bff58c:8", "const:4:8"]]
+ 00bff58c ["CALL", null, ["callee:00c58370:8"]]
- 00bff4f0 bytes 6c630194
+ 00bff58c bytes 79630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6887a621684216cff1df078d35d7f9e8"></a>

### [`00bff55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff55c.md) → [`00bff5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff5f8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff55c.md#insn-00bff5ac)
- 新版 `00bff648`（命令位置の公開資料なし）

~~~diff
- 00bff5ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff5ac ["INT_ADD", "register:40f0:8", ["const:bff5ac:8", "const:4:8"]]
- 00bff5ac ["CALLIND", null, ["register:0:8"]]
+ 00bff648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff648 ["INT_ADD", "register:40f0:8", ["const:bff648:8", "const:4:8"]]
+ 00bff648 ["CALLIND", null, ["register:0:8"]]
- 00bff5ac bytes 00013fd6
+ 00bff648 bytes 00013fd6
~~~


<a id="compare-b1e981bddc9f7a7c0805e610f6c9cde9"></a>

### [`00bff5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md) → [`00bff658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff5e8) · [`00bff620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff620) · [`00bff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff640)
- 新版 `00bff684`（命令位置の公開資料なし） · `00bff6bc`（命令位置の公開資料なし） · `00bff6dc`（命令位置の公開資料なし）

~~~diff
- 00bff5e8 ["INT_ADD", "register:40f0:8", ["const:bff5e8:8", "const:4:8"]]
- 00bff5e8 ["CALL", null, ["callee:00c58330:8"]]
+ 00bff684 ["INT_ADD", "register:40f0:8", ["const:bff684:8", "const:4:8"]]
+ 00bff684 ["CALL", null, ["callee:00c58330:8"]]
- 00bff5e8 bytes 1e630194
+ 00bff684 bytes 2b630194
- 00bff620 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff620 ["INT_ADD", "register:40f0:8", ["const:bff620:8", "const:4:8"]]
- 00bff620 ["CALLIND", null, ["register:0:8"]]
+ 00bff6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff6bc ["INT_ADD", "register:40f0:8", ["const:bff6bc:8", "const:4:8"]]
+ 00bff6bc ["CALLIND", null, ["register:0:8"]]
- 00bff620 bytes 00013fd6
+ 00bff6bc bytes 00013fd6
- 00bff640 ["INT_ADD", "register:40f0:8", ["const:bff640:8", "const:4:8"]]
- 00bff640 ["CALL", null, ["callee:00c58370:8"]]
+ 00bff6dc ["INT_ADD", "register:40f0:8", ["const:bff6dc:8", "const:4:8"]]
+ 00bff6dc ["CALL", null, ["callee:00c58370:8"]]
- 00bff640 bytes 18630194
+ 00bff6dc bytes 25630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c021626898b03a092c027f497c5a5ff"></a>

### [`00bff680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md) → [`00bff71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff71c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff6ac) · [`00bff6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff6e4) · [`00bff704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff704)
- 新版 `00bff748`（命令位置の公開資料なし） · `00bff780`（命令位置の公開資料なし） · `00bff7a0`（命令位置の公開資料なし）

~~~diff
- 00bff6ac ["INT_ADD", "register:40f0:8", ["const:bff6ac:8", "const:4:8"]]
- 00bff6ac ["CALL", null, ["callee:00c58330:8"]]
+ 00bff748 ["INT_ADD", "register:40f0:8", ["const:bff748:8", "const:4:8"]]
+ 00bff748 ["CALL", null, ["callee:00c58330:8"]]
- 00bff6ac bytes ed620194
+ 00bff748 bytes fa620194
- 00bff6e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff6e4 ["INT_ADD", "register:40f0:8", ["const:bff6e4:8", "const:4:8"]]
- 00bff6e4 ["CALLIND", null, ["register:0:8"]]
+ 00bff780 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff780 ["INT_ADD", "register:40f0:8", ["const:bff780:8", "const:4:8"]]
+ 00bff780 ["CALLIND", null, ["register:0:8"]]
- 00bff6e4 bytes 00013fd6
+ 00bff780 bytes 00013fd6
- 00bff704 ["INT_ADD", "register:40f0:8", ["const:bff704:8", "const:4:8"]]
- 00bff704 ["CALL", null, ["callee:00c58370:8"]]
+ 00bff7a0 ["INT_ADD", "register:40f0:8", ["const:bff7a0:8", "const:4:8"]]
+ 00bff7a0 ["CALL", null, ["callee:00c58370:8"]]
- 00bff704 bytes e7620194
+ 00bff7a0 bytes f4620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31ae82a7ec11e7d757c88448a760934"></a>

### [`00bff744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff744.md) → [`00bff7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff7e0.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff744.md#insn-00bff78c)
- 新版 `00bff828`（命令位置の公開資料なし）

~~~diff
- 00bff78c ["INT_ADD", "register:40f0:8", ["const:bff78c:8", "const:4:8"]]
- 00bff78c ["CALL", null, ["callee:00c582b0:8"]]
+ 00bff828 ["INT_ADD", "register:40f0:8", ["const:bff828:8", "const:4:8"]]
+ 00bff828 ["CALL", null, ["callee:00c582b0:8"]]
- 00bff78c bytes 95620194
+ 00bff828 bytes a2620194
~~~


<a id="compare-b7568001de0d390438c4324f1da8b6c6"></a>

### [`00bff8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8a4.md) → [`00bff940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff940.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8a4.md#insn-00bff8bc)
- 新版 `00bff958`（命令位置の公開資料なし）

~~~diff
- 00bff8bc ["INT_ADD", "register:40f0:8", ["const:bff8bc:8", "const:4:8"]]
- 00bff8bc ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bff958 ["INT_ADD", "register:40f0:8", ["const:bff958:8", "const:4:8"]]
+ 00bff958 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bff8bc bytes 09760194
+ 00bff958 bytes 16760194
~~~


<a id="compare-146c86b9a221854513b45ab4e54a231a"></a>

### [`00bff8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8d4.md) → [`00bff970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff970.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8d4.md#insn-00bff8ec)
- 新版 `00bff988`（命令位置の公開資料なし）

~~~diff
- 00bff8ec ["INT_ADD", "register:40f0:8", ["const:bff8ec:8", "const:4:8"]]
- 00bff8ec ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bff988 ["INT_ADD", "register:40f0:8", ["const:bff988:8", "const:4:8"]]
+ 00bff988 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bff8ec bytes fd750194
+ 00bff988 bytes 0a760194
~~~


<a id="compare-8df7b6b519e0246f80fe3dc4998a77ab"></a>

### [`00bff904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff904.md) → [`00bff9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9a0.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff904.md#insn-00bff924)
- 新版 `00bff9c0`（命令位置の公開資料なし）

~~~diff
- 00bff924 ["INT_ADD", "register:40f0:8", ["const:bff924:8", "const:4:8"]]
- 00bff924 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bff9c0 ["INT_ADD", "register:40f0:8", ["const:bff9c0:8", "const:4:8"]]
+ 00bff9c0 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bff924 bytes ef750194
+ 00bff9c0 bytes fc750194
~~~


<a id="compare-24c9b099c643002437751b2bfb67d403"></a>

### [`00bff93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff93c.md) → [`00bff9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9d8.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff93c.md#insn-00bff974)
- 新版 `00bffa10`（命令位置の公開資料なし）

~~~diff
- 00bff974 ["INT_ADD", "register:40f0:8", ["const:bff974:8", "const:4:8"]]
- 00bff974 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00bffa10 ["INT_ADD", "register:40f0:8", ["const:bffa10:8", "const:4:8"]]
+ 00bffa10 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00bff974 bytes 6b7a0194
+ 00bffa10 bytes 787a0194
~~~


