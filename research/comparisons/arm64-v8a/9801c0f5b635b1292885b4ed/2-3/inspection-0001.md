# v16.0.1 → v16.0.2 · 要調査の変更候補 (1)

[一覧の目次](README.md)

<a id="compare-16868266e25bcf590e246a09fa983d9e"></a>

### [`0043aed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043aed4.md) → [`0043af14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af14.md) FUN_0043af14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043bdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bdd4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0043be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md) [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043aed4.md#insn-0043aef0) · [`0043af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043aed4.md#insn-0043af10)
- 新版 `0043af30`（命令位置の公開資料なし） · `0043af50`（命令位置の公開資料なし）

~~~diff
- 0043aef0 ["INT_ADD", "register:40f0:8", ["const:43aef0:8", "const:4:8"]]
- 0043aef0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0043af30 ["INT_ADD", "register:40f0:8", ["const:43af30:8", "const:4:8"]]
+ 0043af30 ["CALL", null, ["callee:00c53da0:8"]]
- 0043aef0 bytes 84632094
+ 0043af30 bytes 9c632094
- 0043af10 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043af10 ["INT_ADD", "register:40f0:8", ["const:43af10:8", "const:4:8"]]
- 0043af10 ["CALLIND", null, ["register:0:8"]]
+ 0043af50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043af50 ["INT_ADD", "register:40f0:8", ["const:43af50:8", "const:4:8"]]
+ 0043af50 ["CALLIND", null, ["register:0:8"]]
- 0043af10 bytes 00013fd6
+ 0043af50 bytes 00013fd6
~~~


<a id="compare-04190f9f1954767a4aabb5a8cecf502f"></a>

### [`0043b1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b1fc.md) → [`0043b23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b23c.md) FUN_0043b23c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b0e8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0043b128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043b218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b1fc.md#insn-0043b218) · [`0043b238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b1fc.md#insn-0043b238)
- 新版 `0043b258`（命令位置の公開資料なし） · `0043b278`（命令位置の公開資料なし）

~~~diff
- 0043b218 ["INT_ADD", "register:40f0:8", ["const:43b218:8", "const:4:8"]]
- 0043b218 ["CALL", null, ["callee:00c53da0:8"]]
+ 0043b258 ["INT_ADD", "register:40f0:8", ["const:43b258:8", "const:4:8"]]
+ 0043b258 ["CALL", null, ["callee:00c53da0:8"]]
- 0043b218 bytes ba622094
+ 0043b258 bytes d2622094
- 0043b238 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043b238 ["INT_ADD", "register:40f0:8", ["const:43b238:8", "const:4:8"]]
- 0043b238 ["CALLIND", null, ["register:0:8"]]
+ 0043b278 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043b278 ["INT_ADD", "register:40f0:8", ["const:43b278:8", "const:4:8"]]
+ 0043b278 ["CALLIND", null, ["register:0:8"]]
- 0043b238 bytes 00013fd6
+ 0043b278 bytes 00013fd6
~~~


<a id="compare-da769019d1a9ebb416d6d2adb3667286"></a>

### [`0043b6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md) → [`0043b714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b714.md) Java_jp_co_ponos_battlecats_MyActivity_firebaseInAppMessagingCallback

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00b35d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00b35da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35da8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043b6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md#insn-0043b6f8) · [`0043b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md#insn-0043b700) · [`0043b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md#insn-0043b710)
- 新版 `0043b738`（命令位置の公開資料なし） · `0043b740`（命令位置の公開資料なし） · `0043b750`（命令位置の公開資料なし）

~~~diff
- 0043b6f8 ["INT_ADD", "register:40f0:8", ["const:43b6f8:8", "const:4:8"]]
- 0043b6f8 ["CALL", null, ["callee:00589994:8"]]
+ 0043b738 ["INT_ADD", "register:40f0:8", ["const:43b738:8", "const:4:8"]]
+ 0043b738 ["CALL", null, ["callee:00589994:8"]]
- 0043b6f8 bytes 97380594
+ 0043b738 bytes 97380594
- 0043b700 ["INT_ADD", "register:40f0:8", ["const:43b700:8", "const:4:8"]]
- 0043b700 ["CALL", null, ["callee:00b35da8:8"]]
+ 0043b740 ["INT_ADD", "register:40f0:8", ["const:43b740:8", "const:4:8"]]
+ 0043b740 ["CALL", null, ["callee:00b35da8:8"]]
- 0043b700 bytes 83e91b94
+ 0043b740 bytes 9ae91b94
- 0043b710 ["INT_ADD", "register:40f0:8", ["const:43b710:8", "const:4:8"]]
- 0043b710 ["CALL", null, ["callee:00c57f80:8"]]
+ 0043b750 ["INT_ADD", "register:40f0:8", ["const:43b750:8", "const:4:8"]]
+ 0043b750 ["CALL", null, ["callee:00c57f80:8"]]
- 0043b710 bytes e8712094
+ 0043b750 bytes 0c722094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b281ef79f9987f9d16f8b7aaf70612b"></a>

### [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) → [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) FUN_0043b838

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 257件 [`0043bdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bdd4.md) [`0044372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/0044372c.md) [`00443abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443abc.md) [`0044add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044add0.md) [`0044f4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md) · 呼出先 5件 [`0043b928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b928.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 257件 [`0043be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md) [`0044376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044376c.md) [`00443afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443afc.md) [`0044ae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ae10.md) [`0044f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f528.md) · 呼出先 5件 [`0043b968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b968.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md#insn-0043b830) · [`0043b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md#insn-0043b850) · [`0043b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md#insn-0043b890)
- 新版 `0043b870`（命令位置の公開資料なし） · `0043b890`（命令位置の公開資料なし） · `0043b8d0`（命令位置の公開資料なし）

~~~diff
- 0043b830 ["INT_ADD", "register:40f0:8", ["const:43b830:8", "const:4:8"]]
- 0043b830 ["CALL", null, ["callee:0043b968:8"]]
+ 0043b870 ["INT_ADD", "register:40f0:8", ["const:43b870:8", "const:4:8"]]
+ 0043b870 ["CALL", null, ["callee:0043b968:8"]]
- 0043b830 bytes 3e000094
+ 0043b870 bytes 3e000094
- 0043b850 ["INT_ADD", "register:40f0:8", ["const:43b850:8", "const:4:8"]]
- 0043b850 ["CALL", null, ["callee:00c57f60:8"]]
+ 0043b890 ["INT_ADD", "register:40f0:8", ["const:43b890:8", "const:4:8"]]
+ 0043b890 ["CALL", null, ["callee:00c57f60:8"]]
- 0043b850 bytes 90712094
+ 0043b890 bytes b4712094
- 0043b890 ["INT_ADD", "register:40f0:8", ["const:43b890:8", "const:4:8"]]
- 0043b890 ["CALL", null, ["callee:0043bb60:8"]]
+ 0043b8d0 ["INT_ADD", "register:40f0:8", ["const:43b8d0:8", "const:4:8"]]
+ 0043b8d0 ["CALL", null, ["callee:0043bb60:8"]]
- 0043b890 bytes a4000094
+ 0043b8d0 bytes a4000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65aa66d8e8c94f1ffa1a92a18ab45eda"></a>

### [`0043bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bad0.md) → [`0043bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb10.md) FUN_0043bb10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bad0.md#insn-0043bb08)
- 新版 `0043bb48`（命令位置の公開資料なし）

~~~diff
- 0043bb08 ["INT_ADD", "register:40f0:8", ["const:43bb08:8", "const:4:8"]]
- 0043bb08 ["CALL", null, ["callee:00c57f80:8"]]
+ 0043bb48 ["INT_ADD", "register:40f0:8", ["const:43bb48:8", "const:4:8"]]
+ 0043bb48 ["CALL", null, ["callee:00c57f80:8"]]
- 0043bb08 bytes ea702094
+ 0043bb48 bytes 0e712094
~~~


<a id="compare-23ca0046d9086d64a64f67973a7c13b6"></a>

### [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) → [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) FUN_0043bb60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 762件 [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00441190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 761件 [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`004411d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004411d0.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043bb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md#insn-0043bb74) · [`0043bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md#insn-0043bba0)
- 新版 `0043bbb4`（命令位置の公開資料なし） · `0043bbe0`（命令位置の公開資料なし）

~~~diff
- 0043bb74 ["INT_ADD", "register:40f0:8", ["const:43bb74:8", "const:4:8"]]
- 0043bb74 ["CALL", null, ["callee:00c57f60:8"]]
+ 0043bbb4 ["INT_ADD", "register:40f0:8", ["const:43bbb4:8", "const:4:8"]]
+ 0043bbb4 ["CALL", null, ["callee:00c57f60:8"]]
- 0043bb74 bytes c7702094
+ 0043bbb4 bytes eb702094
- 0043bba0 ["INT_ADD", "register:40f0:8", ["const:43bba0:8", "const:4:8"]]
- 0043bba0 ["CALL", null, ["callee:0043b7a4:8"]]
+ 0043bbe0 ["INT_ADD", "register:40f0:8", ["const:43bbe0:8", "const:4:8"]]
+ 0043bbe0 ["CALL", null, ["callee:0043b7a4:8"]]
- 0043bba0 bytes f1feff97
+ 0043bbe0 bytes f1feff97
~~~


<a id="compare-4b109f974092d33e2f41b1c6832a7f01"></a>

### [`0043bd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md) → [`0043bd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bd78.md) FUN_0043bd78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043bd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md) · 呼出先 2件 [`0043bd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043bd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bd78.md) · 呼出先 2件 [`0043bd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bd78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md#insn-0043bd54) · [`0043bd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md#insn-0043bd60) · [`0043bd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bd38.md#insn-0043bd70)
- 新版 `0043bd94`（命令位置の公開資料なし） · `0043bda0`（命令位置の公開資料なし） · `0043bdb0`（命令位置の公開資料なし）

~~~diff
- 0043bd54 ["INT_ADD", "register:40f0:8", ["const:43bd54:8", "const:4:8"]]
- 0043bd54 ["CALL", null, ["local:b0:8"]]
+ 0043bd94 ["INT_ADD", "register:40f0:8", ["const:43bd94:8", "const:4:8"]]
+ 0043bd94 ["CALL", null, ["local:b0:8"]]
- 0043bd54 bytes f9ffff97
+ 0043bd94 bytes f9ffff97
- 0043bd60 ["INT_ADD", "register:40f0:8", ["const:43bd60:8", "const:4:8"]]
- 0043bd60 ["CALL", null, ["local:b0:8"]]
+ 0043bda0 ["INT_ADD", "register:40f0:8", ["const:43bda0:8", "const:4:8"]]
+ 0043bda0 ["CALL", null, ["local:b0:8"]]
- 0043bd60 bytes f6ffff97
+ 0043bda0 bytes f6ffff97
- 0043bd70 ["INT_ADD", "register:40f0:8", ["const:43bd70:8", "const:4:8"]]
- 0043bd70 ["CALL", null, ["callee:00c57f80:8"]]
+ 0043bdb0 ["INT_ADD", "register:40f0:8", ["const:43bdb0:8", "const:4:8"]]
+ 0043bdb0 ["CALL", null, ["callee:00c57f80:8"]]
- 0043bd70 bytes 50702094
+ 0043bdb0 bytes 74702094
~~~


<a id="compare-d6f72a885b1fc1eba95a97d44e1f07bf"></a>

### [`0043d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md) → [`0043d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d5f4.md) FUN_0043d5f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`004430c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/004430c0.md) [`00443398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443398.md) · 呼出先 6件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`00443100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443100.md) [`004433d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433d8.md) · 呼出先 6件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043d618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md#insn-0043d618) · [`0043d628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md#insn-0043d628) · [`0043d64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md#insn-0043d64c)
- 新版 `0043d658`（命令位置の公開資料なし） · `0043d668`（命令位置の公開資料なし） · `0043d68c`（命令位置の公開資料なし）

~~~diff
- 0043d618 ["INT_ADD", "register:40f0:8", ["const:43d618:8", "const:4:8"]]
- 0043d618 ["CALL", null, ["callee:00597efc:8"]]
+ 0043d658 ["INT_ADD", "register:40f0:8", ["const:43d658:8", "const:4:8"]]
+ 0043d658 ["CALL", null, ["callee:00597efc:8"]]
- 0043d618 bytes 296a0594
+ 0043d658 bytes 296a0594
- 0043d628 ["INT_ADD", "register:40f0:8", ["const:43d628:8", "const:4:8"]]
- 0043d628 ["CALL", null, ["callee:00c57f80:8"]]
+ 0043d668 ["INT_ADD", "register:40f0:8", ["const:43d668:8", "const:4:8"]]
+ 0043d668 ["CALL", null, ["callee:00c57f80:8"]]
- 0043d628 bytes 226a2094
+ 0043d668 bytes 466a2094
- 0043d64c ["INT_ADD", "register:40f0:8", ["const:43d64c:8", "const:4:8"]]
- 0043d64c ["CALL", null, ["callee:0048cec4:8"]]
+ 0043d68c ["INT_ADD", "register:40f0:8", ["const:43d68c:8", "const:4:8"]]
+ 0043d68c ["CALL", null, ["callee:0048cec4:8"]]
- 0043d64c bytes 0e3e0194
+ 0043d68c bytes 0e3e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76d091d7e3030525ae8e3f1b818143b9"></a>

### [`0043db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md) → [`0043db94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043db94.md) FUN_0043db94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043db70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md#insn-0043db70) · [`0043db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md#insn-0043db90)
- 新版 `0043dbb0`（命令位置の公開資料なし） · `0043dbd0`（命令位置の公開資料なし）

~~~diff
- 0043db70 ["INT_ADD", "register:40f0:8", ["const:43db70:8", "const:4:8"]]
- 0043db70 ["CALL", null, ["callee:00c53da0:8"]]
+ 0043dbb0 ["INT_ADD", "register:40f0:8", ["const:43dbb0:8", "const:4:8"]]
+ 0043dbb0 ["CALL", null, ["callee:00c53da0:8"]]
- 0043db70 bytes 64582094
+ 0043dbb0 bytes 7c582094
- 0043db90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043db90 ["INT_ADD", "register:40f0:8", ["const:43db90:8", "const:4:8"]]
- 0043db90 ["CALLIND", null, ["register:0:8"]]
+ 0043dbd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043dbd0 ["INT_ADD", "register:40f0:8", ["const:43dbd0:8", "const:4:8"]]
+ 0043dbd0 ["CALLIND", null, ["register:0:8"]]
- 0043db90 bytes 00013fd6
+ 0043dbd0 bytes 00013fd6
~~~


<a id="compare-b2fc444e2ee7f0466dca47bc4c00b7b7"></a>

### [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) → [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) FUN_0043de18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 345件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 345件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043ddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md#insn-0043ddf4) · [`0043de38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md#insn-0043de38) · [`0043de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md#insn-0043de58)
- 新版 `0043de34`（命令位置の公開資料なし） · `0043de78`（命令位置の公開資料なし） · `0043de98`（命令位置の公開資料なし）

~~~diff
- 0043ddf4 ["INT_ADD", "register:40f0:8", ["const:43ddf4:8", "const:4:8"]]
- 0043ddf4 ["CALL", null, ["callee:00c580b0:8"]]
+ 0043de34 ["INT_ADD", "register:40f0:8", ["const:43de34:8", "const:4:8"]]
+ 0043de34 ["CALL", null, ["callee:00c580b0:8"]]
- 0043ddf4 bytes 7b682094
+ 0043de34 bytes 9f682094
- 0043de38 ["INT_ADD", "register:40f0:8", ["const:43de38:8", "const:4:8"]]
- 0043de38 ["CALL", null, ["callee:00c57f60:8"]]
+ 0043de78 ["INT_ADD", "register:40f0:8", ["const:43de78:8", "const:4:8"]]
+ 0043de78 ["CALL", null, ["callee:00c57f60:8"]]
- 0043de38 bytes 16682094
+ 0043de78 bytes 3a682094
- 0043de58 ["INT_ADD", "register:40f0:8", ["const:43de58:8", "const:4:8"]]
- 0043de58 ["CALL", null, ["callee:00c58010:8"]]
+ 0043de98 ["INT_ADD", "register:40f0:8", ["const:43de98:8", "const:4:8"]]
+ 0043de98 ["CALL", null, ["callee:00c58010:8"]]
- 0043de58 bytes 3a682094
+ 0043de98 bytes 5e682094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-188a374f5260cecbadac4e0c298b4dd6"></a>

### [`0043df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043df60.md) → [`0043dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dfa0.md) FUN_0043dfa0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043df7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043df60.md#insn-0043df7c) · [`0043df9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043df60.md#insn-0043df9c)
- 新版 `0043dfbc`（命令位置の公開資料なし） · `0043dfdc`（命令位置の公開資料なし）

~~~diff
- 0043df7c ["INT_ADD", "register:40f0:8", ["const:43df7c:8", "const:4:8"]]
- 0043df7c ["CALL", null, ["callee:00c53da0:8"]]
+ 0043dfbc ["INT_ADD", "register:40f0:8", ["const:43dfbc:8", "const:4:8"]]
+ 0043dfbc ["CALL", null, ["callee:00c53da0:8"]]
- 0043df7c bytes 61572094
+ 0043dfbc bytes 79572094
- 0043df9c ["COPY", "register:0:8", ["register:4040:8"]]
- 0043df9c ["INT_ADD", "register:40f0:8", ["const:43df9c:8", "const:4:8"]]
- 0043df9c ["CALLIND", null, ["register:0:8"]]
+ 0043dfdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043dfdc ["INT_ADD", "register:40f0:8", ["const:43dfdc:8", "const:4:8"]]
+ 0043dfdc ["CALLIND", null, ["register:0:8"]]
- 0043df9c bytes 00013fd6
+ 0043dfdc bytes 00013fd6
~~~


<a id="compare-3209d902eec17aed8184cb0544d0c9c9"></a>

### [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) → [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) FUN_0043e868

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 24件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`005d8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f84.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00441190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 24件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`005d8fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8fc4.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`00618240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md) [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004411d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004411d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md#insn-0043e87c) · [`0043e890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md#insn-0043e890) · [`0043e8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md#insn-0043e8bc)
- 新版 `0043e8bc`（命令位置の公開資料なし） · `0043e8d0`（命令位置の公開資料なし） · `0043e8fc`（命令位置の公開資料なし）

~~~diff
- 0043e87c ["INT_ADD", "register:40f0:8", ["const:43e87c:8", "const:4:8"]]
- 0043e87c ["CALL", null, ["callee:0043bb60:8"]]
+ 0043e8bc ["INT_ADD", "register:40f0:8", ["const:43e8bc:8", "const:4:8"]]
+ 0043e8bc ["CALL", null, ["callee:0043bb60:8"]]
- 0043e87c bytes a9f4ff97
+ 0043e8bc bytes a9f4ff97
- 0043e890 ["INT_ADD", "register:40f0:8", ["const:43e890:8", "const:4:8"]]
- 0043e890 ["CALL", null, ["callee:0043bb60:8"]]
+ 0043e8d0 ["INT_ADD", "register:40f0:8", ["const:43e8d0:8", "const:4:8"]]
+ 0043e8d0 ["CALL", null, ["callee:0043bb60:8"]]
- 0043e890 bytes a4f4ff97
+ 0043e8d0 bytes a4f4ff97
- 0043e8bc ["INT_ADD", "register:40f0:8", ["const:43e8bc:8", "const:4:8"]]
- 0043e8bc ["CALL", null, ["callee:004411d0:8"]]
+ 0043e8fc ["INT_ADD", "register:40f0:8", ["const:43e8fc:8", "const:4:8"]]
+ 0043e8fc ["CALL", null, ["callee:004411d0:8"]]
- 0043e8bc bytes 350a0094
+ 0043e8fc bytes 350a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95fb14489705b6863e049f2884749011"></a>

### [`0043e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e9dc.md) → [`0043ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ea1c.md) FUN_0043ea1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`00443480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443480.md) · 呼出先 4件 [`00442ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442ddc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`004434c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md) · 呼出先 4件 [`00442e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442e1c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043ea08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e9dc.md#insn-0043ea08) · [`0043ea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e9dc.md#insn-0043ea1c) · [`0043ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e9dc.md#insn-0043ea30)
- 新版 `0043ea48`（命令位置の公開資料なし） · `0043ea5c`（命令位置の公開資料なし） · `0043ea70`（命令位置の公開資料なし）

~~~diff
- 0043ea08 ["INT_ADD", "register:40f0:8", ["const:43ea08:8", "const:4:8"]]
- 0043ea08 ["CALL", null, ["callee:00442e1c:8"]]
+ 0043ea48 ["INT_ADD", "register:40f0:8", ["const:43ea48:8", "const:4:8"]]
+ 0043ea48 ["CALL", null, ["callee:00442e1c:8"]]
- 0043ea08 bytes f5100094
+ 0043ea48 bytes f5100094
- 0043ea1c ["INT_ADD", "register:40f0:8", ["const:43ea1c:8", "const:4:8"]]
- 0043ea1c ["CALL", null, ["callee:00c53da0:8"]]
+ 0043ea5c ["INT_ADD", "register:40f0:8", ["const:43ea5c:8", "const:4:8"]]
+ 0043ea5c ["CALL", null, ["callee:00c53da0:8"]]
- 0043ea1c bytes b9542094
+ 0043ea5c bytes d1542094
- 0043ea30 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043ea30 ["INT_ADD", "register:40f0:8", ["const:43ea30:8", "const:4:8"]]
- 0043ea30 ["CALLIND", null, ["register:0:8"]]
+ 0043ea70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043ea70 ["INT_ADD", "register:40f0:8", ["const:43ea70:8", "const:4:8"]]
+ 0043ea70 ["CALLIND", null, ["register:0:8"]]
- 0043ea30 bytes 00013fd6
+ 0043ea70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79eeec8ab79f07003dd2333ca7f540b8"></a>

### [`0043eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043eb70.md) → [`0043ebb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ebb0.md) FUN_0043ebb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043eb70.md#insn-0043eb8c) · [`0043ebac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043eb70.md#insn-0043ebac)
- 新版 `0043ebcc`（命令位置の公開資料なし） · `0043ebec`（命令位置の公開資料なし）

~~~diff
- 0043eb8c ["INT_ADD", "register:40f0:8", ["const:43eb8c:8", "const:4:8"]]
- 0043eb8c ["CALL", null, ["callee:00c53da0:8"]]
+ 0043ebcc ["INT_ADD", "register:40f0:8", ["const:43ebcc:8", "const:4:8"]]
+ 0043ebcc ["CALL", null, ["callee:00c53da0:8"]]
- 0043eb8c bytes 5d542094
+ 0043ebcc bytes 75542094
- 0043ebac ["COPY", "register:0:8", ["register:4040:8"]]
- 0043ebac ["INT_ADD", "register:40f0:8", ["const:43ebac:8", "const:4:8"]]
- 0043ebac ["CALLIND", null, ["register:0:8"]]
+ 0043ebec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043ebec ["INT_ADD", "register:40f0:8", ["const:43ebec:8", "const:4:8"]]
+ 0043ebec ["CALLIND", null, ["register:0:8"]]
- 0043ebac bytes 00013fd6
+ 0043ebec bytes 00013fd6
~~~


<a id="compare-b8ffdb2985b14de7879003cda4c34615"></a>

### [`0043ebc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ebc0.md) → [`0043ec00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ec00.md) FUN_0043ec00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043ebdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ebc0.md#insn-0043ebdc) · [`0043ebfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ebc0.md#insn-0043ebfc)
- 新版 `0043ec1c`（命令位置の公開資料なし） · `0043ec3c`（命令位置の公開資料なし）

~~~diff
- 0043ebdc ["INT_ADD", "register:40f0:8", ["const:43ebdc:8", "const:4:8"]]
- 0043ebdc ["CALL", null, ["callee:00c53da0:8"]]
+ 0043ec1c ["INT_ADD", "register:40f0:8", ["const:43ec1c:8", "const:4:8"]]
+ 0043ec1c ["CALL", null, ["callee:00c53da0:8"]]
- 0043ebdc bytes 49542094
+ 0043ec1c bytes 61542094
- 0043ebfc ["COPY", "register:0:8", ["register:4040:8"]]
- 0043ebfc ["INT_ADD", "register:40f0:8", ["const:43ebfc:8", "const:4:8"]]
- 0043ebfc ["CALLIND", null, ["register:0:8"]]
+ 0043ec3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043ec3c ["INT_ADD", "register:40f0:8", ["const:43ec3c:8", "const:4:8"]]
+ 0043ec3c ["CALLIND", null, ["register:0:8"]]
- 0043ebfc bytes 00013fd6
+ 0043ec3c bytes 00013fd6
~~~


<a id="compare-bdd71fa73a05816a1aa3c72089e4d8c7"></a>

### [`0043ec10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec10.md) → [`0043ec50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ec50.md) FUN_0043ec50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043ec2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec10.md#insn-0043ec2c) · [`0043ec4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec10.md#insn-0043ec4c)
- 新版 `0043ec6c`（命令位置の公開資料なし） · `0043ec8c`（命令位置の公開資料なし）

~~~diff
- 0043ec2c ["INT_ADD", "register:40f0:8", ["const:43ec2c:8", "const:4:8"]]
- 0043ec2c ["CALL", null, ["callee:00c53da0:8"]]
+ 0043ec6c ["INT_ADD", "register:40f0:8", ["const:43ec6c:8", "const:4:8"]]
+ 0043ec6c ["CALL", null, ["callee:00c53da0:8"]]
- 0043ec2c bytes 35542094
+ 0043ec6c bytes 4d542094
- 0043ec4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0043ec4c ["INT_ADD", "register:40f0:8", ["const:43ec4c:8", "const:4:8"]]
- 0043ec4c ["CALLIND", null, ["register:0:8"]]
+ 0043ec8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043ec8c ["INT_ADD", "register:40f0:8", ["const:43ec8c:8", "const:4:8"]]
+ 0043ec8c ["CALLIND", null, ["register:0:8"]]
- 0043ec4c bytes 00013fd6
+ 0043ec8c bytes 00013fd6
~~~


<a id="compare-14db7efca0ac191f5ff2baeaaa304f01"></a>

### [`0043f3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f3d4.md) → [`0043f414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f414.md) FUN_0043f414

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f3d4.md#insn-0043f3f0) · [`0043f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f3d4.md#insn-0043f410)
- 新版 `0043f430`（命令位置の公開資料なし） · `0043f450`（命令位置の公開資料なし）

~~~diff
- 0043f3f0 ["INT_ADD", "register:40f0:8", ["const:43f3f0:8", "const:4:8"]]
- 0043f3f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0043f430 ["INT_ADD", "register:40f0:8", ["const:43f430:8", "const:4:8"]]
+ 0043f430 ["CALL", null, ["callee:00c53da0:8"]]
- 0043f3f0 bytes 44522094
+ 0043f430 bytes 5c522094
- 0043f410 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043f410 ["INT_ADD", "register:40f0:8", ["const:43f410:8", "const:4:8"]]
- 0043f410 ["CALLIND", null, ["register:0:8"]]
+ 0043f450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043f450 ["INT_ADD", "register:40f0:8", ["const:43f450:8", "const:4:8"]]
+ 0043f450 ["CALLIND", null, ["register:0:8"]]
- 0043f410 bytes 00013fd6
+ 0043f450 bytes 00013fd6
~~~


<a id="compare-687a7f0d17d02576b603606006e055de"></a>

### [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md) → [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md) FUN_0043f7cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`0088043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md) [`00882334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882334.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 5件 [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 6件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00880494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md) [`0088238c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088238c.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`00a95838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a95/00a95838.md) · 呼出先 5件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0043f7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md#insn-0043f7bc) · [`0043f7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md#insn-0043f7cc) · [`0043f800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md#insn-0043f800)
- 新版 `0043f7fc`（命令位置の公開資料なし） · `0043f80c`（命令位置の公開資料なし） · `0043f840`（命令位置の公開資料なし）

~~~diff
- 0043f7bc ["INT_ADD", "register:40f0:8", ["const:43f7bc:8", "const:4:8"]]
- 0043f7bc ["CALL", null, ["callee:00597efc:8"]]
+ 0043f7fc ["INT_ADD", "register:40f0:8", ["const:43f7fc:8", "const:4:8"]]
+ 0043f7fc ["CALL", null, ["callee:00597efc:8"]]
- 0043f7bc bytes c0610594
+ 0043f7fc bytes c0610594
- 0043f7cc ["INT_ADD", "register:40f0:8", ["const:43f7cc:8", "const:4:8"]]
- 0043f7cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0043f80c ["INT_ADD", "register:40f0:8", ["const:43f80c:8", "const:4:8"]]
+ 0043f80c ["CALL", null, ["callee:00c57f80:8"]]
- 0043f7cc bytes b9612094
+ 0043f80c bytes dd612094
- 0043f800 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043f800 ["INT_ADD", "register:40f0:8", ["const:43f800:8", "const:4:8"]]
- 0043f800 ["CALLIND", null, ["register:0:8"]]
+ 0043f840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0043f840 ["INT_ADD", "register:40f0:8", ["const:43f840:8", "const:4:8"]]
+ 0043f840 ["CALLIND", null, ["register:0:8"]]
- 0043f800 bytes 00013fd6
+ 0043f840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60d8b3355e86475312768188e24183d9"></a>

### [`00440a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440a9c.md) → [`00440adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440adc.md) FUN_00440adc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00440ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440a9c.md#insn-00440ac0) · [`00440ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440a9c.md#insn-00440ad0) · [`00440ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440a9c.md#insn-00440ae0)
- 新版 `00440b00`（命令位置の公開資料なし） · `00440b10`（命令位置の公開資料なし） · `00440b20`（命令位置の公開資料なし）

~~~diff
- 00440ac0 ["INT_ADD", "register:40f0:8", ["const:440ac0:8", "const:4:8"]]
- 00440ac0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00440b00 ["INT_ADD", "register:40f0:8", ["const:440b00:8", "const:4:8"]]
+ 00440b00 ["CALL", null, ["callee:00c57f80:8"]]
- 00440ac0 bytes fc5c2094
+ 00440b00 bytes 205d2094
- 00440ad0 ["INT_ADD", "register:40f0:8", ["const:440ad0:8", "const:4:8"]]
- 00440ad0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00440b10 ["INT_ADD", "register:40f0:8", ["const:440b10:8", "const:4:8"]]
+ 00440b10 ["CALL", null, ["callee:00c57f80:8"]]
- 00440ad0 bytes f85c2094
+ 00440b10 bytes 1c5d2094
- 00440ae0 ["INT_ADD", "register:40f0:8", ["const:440ae0:8", "const:4:8"]]
- 00440ae0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00440b20 ["INT_ADD", "register:40f0:8", ["const:440b20:8", "const:4:8"]]
+ 00440b20 ["CALL", null, ["callee:00c57f80:8"]]
- 00440ae0 bytes f45c2094
+ 00440b20 bytes 185d2094
~~~


<a id="compare-76d21251c962ef3c230e214e7d04720c"></a>

### [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) → [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) FUN_00440b40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 19件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00440b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md#insn-00440b4c)
- 新版 `00440b8c`（命令位置の公開資料なし）

~~~diff
- 00440b4c ["INT_ADD", "register:40f0:8", ["const:440b4c:8", "const:4:8"]]
- 00440b4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00440b8c ["INT_ADD", "register:40f0:8", ["const:440b8c:8", "const:4:8"]]
+ 00440b8c ["CALL", null, ["callee:00c57f80:8"]]
- 00440b4c bytes d95c2094
+ 00440b8c bytes fd5c2094
~~~


<a id="compare-3ec4ded604dbf1396814bc899545b7e6"></a>

### [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) → [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) FUN_00440c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 22件 [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) [`00519e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519e00.md) [`0051c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58010.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 22件 [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) [`00519e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519e40.md) [`0051c0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00440c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md#insn-00440c44) · [`00440c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md#insn-00440c48)
- 新版 `00440c84`（命令位置の公開資料なし） · `00440c88`（命令位置の公開資料なし）

~~~diff
- 00440c44 ["INT_ADD", "register:40f0:8", ["const:440c44:8", "const:4:8"]]
- 00440c44 ["CALL", null, ["callee:00c580e0:8"]]
+ 00440c84 ["INT_ADD", "register:40f0:8", ["const:440c84:8", "const:4:8"]]
+ 00440c84 ["CALL", null, ["callee:00c580e0:8"]]
- 00440c44 bytes f35c2094
+ 00440c84 bytes 175d2094
- 00440c48 ["INT_ADD", "register:40f0:8", ["const:440c48:8", "const:4:8"]]
- 00440c48 ["CALL", null, ["callee:00c580f0:8"]]
+ 00440c88 ["INT_ADD", "register:40f0:8", ["const:440c88:8", "const:4:8"]]
+ 00440c88 ["CALL", null, ["callee:00c580f0:8"]]
- 00440c48 bytes f65c2094
+ 00440c88 bytes 1a5d2094
~~~


<a id="compare-d00f47abb44954454f78caa786f09857"></a>

### [`00440c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c4c.md) → [`00440c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c8c.md) FUN_00440c8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00440cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c4c.md#insn-00440cf4) · [`00440db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c4c.md#insn-00440db0) · [`00440e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c4c.md#insn-00440e08)
- 新版 `00440d34`（命令位置の公開資料なし） · `00440df0`（命令位置の公開資料なし） · `00440e48`（命令位置の公開資料なし）

~~~diff
- 00440cf4 ["INT_ADD", "register:40f0:8", ["const:440cf4:8", "const:4:8"]]
- 00440cf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00440d34 ["INT_ADD", "register:40f0:8", ["const:440d34:8", "const:4:8"]]
+ 00440d34 ["CALL", null, ["callee:00c57f60:8"]]
- 00440cf4 bytes 675c2094
+ 00440d34 bytes 8b5c2094
- 00440db0 ["INT_ADD", "register:40f0:8", ["const:440db0:8", "const:4:8"]]
- 00440db0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00440df0 ["INT_ADD", "register:40f0:8", ["const:440df0:8", "const:4:8"]]
+ 00440df0 ["CALL", null, ["callee:00c57f60:8"]]
- 00440db0 bytes 385c2094
+ 00440df0 bytes 5c5c2094
- 00440e08 ["INT_ADD", "register:40f0:8", ["const:440e08:8", "const:4:8"]]
- 00440e08 ["CALL", null, ["callee:00c580d0:8"]]
+ 00440e48 ["INT_ADD", "register:40f0:8", ["const:440e48:8", "const:4:8"]]
+ 00440e48 ["CALL", null, ["callee:00c580d0:8"]]
- 00440e08 bytes 7e5c2094
+ 00440e48 bytes a25c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11a6cfc6313bbe2922a61468609938ce"></a>

### [`00440ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ef4.md) → [`00440f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f34.md) FUN_00440f34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00440f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ef4.md#insn-00440f44)
- 新版 `00440f84`（命令位置の公開資料なし）

~~~diff
- 00440f44 ["INT_ADD", "register:40f0:8", ["const:440f44:8", "const:4:8"]]
- 00440f44 ["CALL", null, ["callee:00c57f80:8"]]
+ 00440f84 ["INT_ADD", "register:40f0:8", ["const:440f84:8", "const:4:8"]]
+ 00440f84 ["CALL", null, ["callee:00c57f80:8"]]
- 00440f44 bytes db5b2094
+ 00440f84 bytes ff5b2094
~~~


<a id="compare-a5a09be2deb5a99bd7822160cb3313fa"></a>

### [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) → [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) FUN_00440fb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 116件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 116件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md#insn-0044100c) · [`00441040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md#insn-00441040) · [`00441060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md#insn-00441060)
- 新版 `0044104c`（命令位置の公開資料なし） · `00441080`（命令位置の公開資料なし） · `004410a0`（命令位置の公開資料なし）

~~~diff
- 0044100c ["INT_ADD", "register:40f0:8", ["const:44100c:8", "const:4:8"]]
- 0044100c ["CALL", null, ["callee:00c57f60:8"]]
+ 0044104c ["INT_ADD", "register:40f0:8", ["const:44104c:8", "const:4:8"]]
+ 0044104c ["CALL", null, ["callee:00c57f60:8"]]
- 0044100c bytes a15b2094
+ 0044104c bytes c55b2094
- 00441040 ["INT_ADD", "register:40f0:8", ["const:441040:8", "const:4:8"]]
- 00441040 ["CALL", null, ["callee:00c58010:8"]]
+ 00441080 ["INT_ADD", "register:40f0:8", ["const:441080:8", "const:4:8"]]
+ 00441080 ["CALL", null, ["callee:00c58010:8"]]
- 00441040 bytes c05b2094
+ 00441080 bytes e45b2094
- 00441060 ["INT_ADD", "register:40f0:8", ["const:441060:8", "const:4:8"]]
- 00441060 ["CALL", null, ["callee:00c58010:8"]]
+ 004410a0 ["INT_ADD", "register:40f0:8", ["const:4410a0:8", "const:4:8"]]
+ 004410a0 ["CALL", null, ["callee:00c58010:8"]]
- 00441060 bytes b85b2094
+ 004410a0 bytes dc5b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77504aa298971298bf87ed1ec5909231"></a>

### [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) → [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) FUN_004410cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 119件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) [`0045a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 119件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) [`0045a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md) [`0045a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004410f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md#insn-004410f8) · [`00441154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md#insn-00441154)
- 新版 `00441138`（命令位置の公開資料なし） · `00441194`（命令位置の公開資料なし）

~~~diff
- 004410f8 ["INT_ADD", "register:40f0:8", ["const:4410f8:8", "const:4:8"]]
- 004410f8 ["CALL", null, ["callee:00c58120:8"]]
+ 00441138 ["INT_ADD", "register:40f0:8", ["const:441138:8", "const:4:8"]]
+ 00441138 ["CALL", null, ["callee:00c58120:8"]]
- 004410f8 bytes d65b2094
+ 00441138 bytes fa5b2094
- 00441154 ["INT_ADD", "register:40f0:8", ["const:441154:8", "const:4:8"]]
- 00441154 ["CALL", null, ["callee:00c58120:8"]]
+ 00441194 ["INT_ADD", "register:40f0:8", ["const:441194:8", "const:4:8"]]
+ 00441194 ["CALL", null, ["callee:00c58120:8"]]
- 00441154 bytes bf5b2094
+ 00441194 bytes e35b2094
~~~


<a id="compare-aa6aaf55cdf87f4d15712977a0b7989e"></a>

### [`00441190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md) → [`004411d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004411d0.md) FUN_004411d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004411e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md#insn-004411e4) · [`004411f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md#insn-004411f8) · [`00441228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441190.md#insn-00441228)
- 新版 `00441224`（命令位置の公開資料なし） · `00441238`（命令位置の公開資料なし） · `00441268`（命令位置の公開資料なし）

~~~diff
- 004411e4 ["INT_ADD", "register:40f0:8", ["const:4411e4:8", "const:4:8"]]
- 004411e4 ["CALL", null, ["callee:0043bb60:8"]]
+ 00441224 ["INT_ADD", "register:40f0:8", ["const:441224:8", "const:4:8"]]
+ 00441224 ["CALL", null, ["callee:0043bb60:8"]]
- 004411e4 bytes 4feaff97
+ 00441224 bytes 4feaff97
- 004411f8 ["INT_ADD", "register:40f0:8", ["const:4411f8:8", "const:4:8"]]
- 004411f8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00441238 ["INT_ADD", "register:40f0:8", ["const:441238:8", "const:4:8"]]
+ 00441238 ["CALL", null, ["callee:0043bb60:8"]]
- 004411f8 bytes 4aeaff97
+ 00441238 bytes 4aeaff97
- 00441228 ["INT_ADD", "register:40f0:8", ["const:441228:8", "const:4:8"]]
- 00441228 ["CALL", null, ["callee:004412f8:8"]]
+ 00441268 ["INT_ADD", "register:40f0:8", ["const:441268:8", "const:4:8"]]
+ 00441268 ["CALL", null, ["callee:004412f8:8"]]
- 00441228 bytes 24000094
+ 00441268 bytes 24000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2110a10ae0ac5e2b4d0da14c075c29ec"></a>

### [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md) → [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md) FUN_00441d2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 95件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 3件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 95件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 3件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00441d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md#insn-00441d24) · [`00441d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md#insn-00441d90) · [`00441da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md#insn-00441da4)
- 新版 `00441d64`（命令位置の公開資料なし） · `00441dd0`（命令位置の公開資料なし） · `00441de4`（命令位置の公開資料なし）

~~~diff
- 00441d24 ["INT_ADD", "register:40f0:8", ["const:441d24:8", "const:4:8"]]
- 00441d24 ["CALL", null, ["callee:00c580b0:8"]]
+ 00441d64 ["INT_ADD", "register:40f0:8", ["const:441d64:8", "const:4:8"]]
+ 00441d64 ["CALL", null, ["callee:00c580b0:8"]]
- 00441d24 bytes af582094
+ 00441d64 bytes d3582094
- 00441d90 ["INT_ADD", "register:40f0:8", ["const:441d90:8", "const:4:8"]]
- 00441d90 ["CALL", null, ["callee:00c580a0:8"]]
+ 00441dd0 ["INT_ADD", "register:40f0:8", ["const:441dd0:8", "const:4:8"]]
+ 00441dd0 ["CALL", null, ["callee:00c580a0:8"]]
- 00441d90 bytes 90582094
+ 00441dd0 bytes b4582094
- 00441da4 ["INT_ADD", "register:40f0:8", ["const:441da4:8", "const:4:8"]]
- 00441da4 ["CALL", null, ["callee:00c58120:8"]]
+ 00441de4 ["INT_ADD", "register:40f0:8", ["const:441de4:8", "const:4:8"]]
+ 00441de4 ["CALL", null, ["callee:00c58120:8"]]
- 00441da4 bytes ab582094
+ 00441de4 bytes cf582094
~~~


<a id="compare-6af277a1e54c4c3a415c442fd75542fc"></a>

### [`00441dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md) → [`00441e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441e00.md) FUN_00441e00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 96件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 96件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00441e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md#insn-00441e48) · [`00441e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md#insn-00441e68) · [`00441e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md#insn-00441e88)
- 新版 `00441e88`（命令位置の公開資料なし） · `00441ea8`（命令位置の公開資料なし） · `00441ec8`（命令位置の公開資料なし）

~~~diff
- 00441e48 ["INT_ADD", "register:40f0:8", ["const:441e48:8", "const:4:8"]]
- 00441e48 ["CALL", null, ["callee:00c57f60:8"]]
+ 00441e88 ["INT_ADD", "register:40f0:8", ["const:441e88:8", "const:4:8"]]
+ 00441e88 ["CALL", null, ["callee:00c57f60:8"]]
- 00441e48 bytes 12582094
+ 00441e88 bytes 36582094
- 00441e68 ["INT_ADD", "register:40f0:8", ["const:441e68:8", "const:4:8"]]
- 00441e68 ["CALL", null, ["callee:00c58010:8"]]
+ 00441ea8 ["INT_ADD", "register:40f0:8", ["const:441ea8:8", "const:4:8"]]
+ 00441ea8 ["CALL", null, ["callee:00c58010:8"]]
- 00441e68 bytes 36582094
+ 00441ea8 bytes 5a582094
- 00441e88 ["INT_ADD", "register:40f0:8", ["const:441e88:8", "const:4:8"]]
- 00441e88 ["CALL", null, ["callee:0044295c:8"]]
+ 00441ec8 ["INT_ADD", "register:40f0:8", ["const:441ec8:8", "const:4:8"]]
+ 00441ec8 ["CALL", null, ["callee:0044295c:8"]]
- 00441e88 bytes a5020094
+ 00441ec8 bytes a5020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b95cb4fe5013dad4a0023c6ffa87243f"></a>

### [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) → [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) FUN_00441ed4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 108件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 108件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00441eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md#insn-00441eac) · [`00441ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md#insn-00441ee8) · [`00441f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md#insn-00441f0c)
- 新版 `00441eec`（命令位置の公開資料なし） · `00441f28`（命令位置の公開資料なし） · `00441f4c`（命令位置の公開資料なし）

~~~diff
- 00441eac ["INT_ADD", "register:40f0:8", ["const:441eac:8", "const:4:8"]]
- 00441eac ["CALL", null, ["callee:00c580b0:8"]]
+ 00441eec ["INT_ADD", "register:40f0:8", ["const:441eec:8", "const:4:8"]]
+ 00441eec ["CALL", null, ["callee:00c580b0:8"]]
- 00441eac bytes 4d582094
+ 00441eec bytes 71582094
- 00441ee8 ["INT_ADD", "register:40f0:8", ["const:441ee8:8", "const:4:8"]]
- 00441ee8 ["CALL", null, ["callee:00c58120:8"]]
+ 00441f28 ["INT_ADD", "register:40f0:8", ["const:441f28:8", "const:4:8"]]
+ 00441f28 ["CALL", null, ["callee:00c58120:8"]]
- 00441ee8 bytes 5a582094
+ 00441f28 bytes 7e582094
- 00441f0c ["INT_ADD", "register:40f0:8", ["const:441f0c:8", "const:4:8"]]
- 00441f0c ["CALL", null, ["callee:0044295c:8"]]
+ 00441f4c ["INT_ADD", "register:40f0:8", ["const:441f4c:8", "const:4:8"]]
+ 00441f4c ["CALL", null, ["callee:0044295c:8"]]
- 00441f0c bytes 84020094
+ 00441f4c bytes 84020094
~~~


<a id="compare-c894e9b03b4733c0deaa165ab79db892"></a>

### [`004427f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004427f4.md) → [`00442834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442834.md) FUN_00442834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 95件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 2件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 95件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 2件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044282c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004427f4.md#insn-0044282c) · [`00442850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004427f4.md#insn-00442850)
- 新版 `0044286c`（命令位置の公開資料なし） · `00442890`（命令位置の公開資料なし）

~~~diff
- 0044282c ["INT_ADD", "register:40f0:8", ["const:44282c:8", "const:4:8"]]
- 0044282c ["CALL", null, ["callee:00c580b0:8"]]
+ 0044286c ["INT_ADD", "register:40f0:8", ["const:44286c:8", "const:4:8"]]
+ 0044286c ["CALL", null, ["callee:00c580b0:8"]]
- 0044282c bytes ed552094
+ 0044286c bytes 11562094
- 00442850 ["INT_ADD", "register:40f0:8", ["const:442850:8", "const:4:8"]]
- 00442850 ["CALL", null, ["callee:00c580a0:8"]]
+ 00442890 ["INT_ADD", "register:40f0:8", ["const:442890:8", "const:4:8"]]
+ 00442890 ["CALL", null, ["callee:00c580a0:8"]]
- 00442850 bytes e0552094
+ 00442890 bytes 04562094
~~~


<a id="compare-024d7d12813611304dd8822a820ec16c"></a>

### [`00442884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442884.md) → [`004428c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/004428c4.md) FUN_004428c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 95件 [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00446dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446dc0.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 95件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004428dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442884.md#insn-004428dc) · [`004428fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442884.md#insn-004428fc) · [`00442918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442884.md#insn-00442918)
- 新版 `0044291c`（命令位置の公開資料なし） · `0044293c`（命令位置の公開資料なし） · `00442958`（命令位置の公開資料なし）

~~~diff
- 004428dc ["INT_ADD", "register:40f0:8", ["const:4428dc:8", "const:4:8"]]
- 004428dc ["CALL", null, ["callee:00c57f60:8"]]
+ 0044291c ["INT_ADD", "register:40f0:8", ["const:44291c:8", "const:4:8"]]
+ 0044291c ["CALL", null, ["callee:00c57f60:8"]]
- 004428dc bytes 6d552094
+ 0044291c bytes 91552094
- 004428fc ["INT_ADD", "register:40f0:8", ["const:4428fc:8", "const:4:8"]]
- 004428fc ["CALL", null, ["callee:00c58160:8"]]
+ 0044293c ["INT_ADD", "register:40f0:8", ["const:44293c:8", "const:4:8"]]
+ 0044293c ["CALL", null, ["callee:00c58160:8"]]
- 004428fc bytes e5552094
+ 0044293c bytes 09562094
- 00442918 ["INT_ADD", "register:40f0:8", ["const:442918:8", "const:4:8"]]
- 00442918 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00442958 ["INT_ADD", "register:40f0:8", ["const:442958:8", "const:4:8"]]
+ 00442958 ["CALL", null, ["callee:0043b7a4:8"]]
- 00442918 bytes 93e3ff97
+ 00442958 bytes 93e3ff97
~~~


<a id="compare-b2e604999ae928a48b0fcf9c6f57e332"></a>

### [`004429b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004429b0.md) → [`004429f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/004429f0.md) FUN_004429f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0044a2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044a2b8.md) [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`00486458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 12件 [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0044a2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md) [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`00486498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486498.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00442a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004429b0.md#insn-00442a1c) · [`00442a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004429b0.md#insn-00442a30) · [`00442a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004429b0.md#insn-00442a58)
- 新版 `00442a5c`（命令位置の公開資料なし） · `00442a70`（命令位置の公開資料なし） · `00442a98`（命令位置の公開資料なし）

~~~diff
- 00442a1c ["INT_ADD", "register:40f0:8", ["const:442a1c:8", "const:4:8"]]
- 00442a1c ["CALL", null, ["callee:0043bb60:8"]]
+ 00442a5c ["INT_ADD", "register:40f0:8", ["const:442a5c:8", "const:4:8"]]
+ 00442a5c ["CALL", null, ["callee:0043bb60:8"]]
- 00442a1c bytes 41e4ff97
+ 00442a5c bytes 41e4ff97
- 00442a30 ["INT_ADD", "register:40f0:8", ["const:442a30:8", "const:4:8"]]
- 00442a30 ["CALL", null, ["callee:00442b78:8"]]
+ 00442a70 ["INT_ADD", "register:40f0:8", ["const:442a70:8", "const:4:8"]]
+ 00442a70 ["CALL", null, ["callee:00442b78:8"]]
- 00442a30 bytes 42000094
+ 00442a70 bytes 42000094
- 00442a58 ["INT_ADD", "register:40f0:8", ["const:442a58:8", "const:4:8"]]
- 00442a58 ["CALL", null, ["callee:0043bb60:8"]]
+ 00442a98 ["INT_ADD", "register:40f0:8", ["const:442a98:8", "const:4:8"]]
+ 00442a98 ["CALL", null, ["callee:0043bb60:8"]]
- 00442a58 bytes 32e4ff97
+ 00442a98 bytes 32e4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304ea1c2f03e0ae2b394c3be23d302a8"></a>

### [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) → [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) FUN_00442b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 29件 [`004429b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/004429b0.md) [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`0074f6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074f/0074f6dc.md) · 呼出先 3件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md)
- 新版 呼出元 29件 [`004429f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/004429f0.md) [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`0047a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1c0.md) [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`0074f734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074f734.md) · 呼出先 3件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00442bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md#insn-00442bc8) · [`00442bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md#insn-00442bdc) · [`00442c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md#insn-00442c70)
- 新版 `00442c08`（命令位置の公開資料なし） · `00442c1c`（命令位置の公開資料なし） · `00442cb0`（命令位置の公開資料なし）

~~~diff
- 00442bc8 ["INT_ADD", "register:40f0:8", ["const:442bc8:8", "const:4:8"]]
- 00442bc8 ["CALL", null, ["callee:00c580a0:8"]]
+ 00442c08 ["INT_ADD", "register:40f0:8", ["const:442c08:8", "const:4:8"]]
+ 00442c08 ["CALL", null, ["callee:00c580a0:8"]]
- 00442bc8 bytes 02552094
+ 00442c08 bytes 26552094
- 00442bdc ["INT_ADD", "register:40f0:8", ["const:442bdc:8", "const:4:8"]]
- 00442bdc ["CALL", null, ["callee:00c58120:8"]]
+ 00442c1c ["INT_ADD", "register:40f0:8", ["const:442c1c:8", "const:4:8"]]
+ 00442c1c ["CALL", null, ["callee:00c58120:8"]]
- 00442bdc bytes 1d552094
+ 00442c1c bytes 41552094
- 00442c70 ["INT_ADD", "register:40f0:8", ["const:442c70:8", "const:4:8"]]
- 00442c70 ["CALL", null, ["callee:00c58140:8"]]
+ 00442cb0 ["INT_ADD", "register:40f0:8", ["const:442cb0:8", "const:4:8"]]
+ 00442cb0 ["CALL", null, ["callee:00c58140:8"]]
- 00442c70 bytes 00552094
+ 00442cb0 bytes 24552094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97f3f84d63204b735d9a6ef04fcc783f"></a>

### [`00442ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442ddc.md) → [`00442e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442e1c.md) FUN_00442e1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0043e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e9dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0043ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ea1c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00442e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442ddc.md#insn-00442e18) · [`00442e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442ddc.md#insn-00442e3c) · [`00442e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442ddc.md#insn-00442e4c)
- 新版 `00442e58`（命令位置の公開資料なし） · `00442e7c`（命令位置の公開資料なし） · `00442e8c`（命令位置の公開資料なし）

~~~diff
- 00442e18 ["INT_ADD", "register:40f0:8", ["const:442e18:8", "const:4:8"]]
- 00442e18 ["CALL", null, ["callee:00c57f80:8"]]
+ 00442e58 ["INT_ADD", "register:40f0:8", ["const:442e58:8", "const:4:8"]]
+ 00442e58 ["CALL", null, ["callee:00c57f80:8"]]
- 00442e18 bytes 26542094
+ 00442e58 bytes 4a542094
- 00442e3c ["INT_ADD", "register:40f0:8", ["const:442e3c:8", "const:4:8"]]
- 00442e3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00442e7c ["INT_ADD", "register:40f0:8", ["const:442e7c:8", "const:4:8"]]
+ 00442e7c ["CALL", null, ["callee:00c57f80:8"]]
- 00442e3c bytes 1d542094
+ 00442e7c bytes 41542094
- 00442e4c ["INT_ADD", "register:40f0:8", ["const:442e4c:8", "const:4:8"]]
- 00442e4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00442e8c ["INT_ADD", "register:40f0:8", ["const:442e8c:8", "const:4:8"]]
+ 00442e8c ["CALL", null, ["callee:00c57f80:8"]]
- 00442e4c bytes 19542094
+ 00442e8c bytes 3d542094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ace278c75219e58fbc0070155c4987b"></a>

### [`00442f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442f78.md) → [`00442fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442fb8.md) FUN_00442fb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00442fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442f78.md#insn-00442fac) · [`00442fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442f78.md#insn-00442fc4) · [`00442fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442f78.md#insn-00442fd8)
- 新版 `00442fec`（命令位置の公開資料なし） · `00443004`（命令位置の公開資料なし） · `00443018`（命令位置の公開資料なし）

~~~diff
- 00442fac ["INT_ADD", "register:40f0:8", ["const:442fac:8", "const:4:8"]]
- 00442fac ["CALL", null, ["callee:00c53d70:8"]]
+ 00442fec ["INT_ADD", "register:40f0:8", ["const:442fec:8", "const:4:8"]]
+ 00442fec ["CALL", null, ["callee:00c53d70:8"]]
- 00442fac bytes 49432094
+ 00442fec bytes 61432094
- 00442fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00442fc4 ["INT_ADD", "register:40f0:8", ["const:442fc4:8", "const:4:8"]]
- 00442fc4 ["CALLIND", null, ["register:0:8"]]
+ 00443004 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00443004 ["INT_ADD", "register:40f0:8", ["const:443004:8", "const:4:8"]]
+ 00443004 ["CALLIND", null, ["register:0:8"]]
- 00442fc4 bytes 00013fd6
+ 00443004 bytes 00013fd6
- 00442fd8 ["INT_ADD", "register:40f0:8", ["const:442fd8:8", "const:4:8"]]
- 00442fd8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00443018 ["INT_ADD", "register:40f0:8", ["const:443018:8", "const:4:8"]]
+ 00443018 ["CALL", null, ["callee:00c53da0:8"]]
- 00442fd8 bytes 4a432094
+ 00443018 bytes 62432094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b5d7dabaf12f0743f9a396ada6721c"></a>

### [`004430c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/004430c0.md) → [`00443100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443100.md) FUN_00443100

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d5f4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004430ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/004430c0.md#insn-004430ec) · [`00443100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/004430c0.md#insn-00443100) · [`00443108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/004430c0.md#insn-00443108)
- 新版 `0044312c`（命令位置の公開資料なし） · `00443140`（命令位置の公開資料なし） · `00443148`（命令位置の公開資料なし）

~~~diff
- 004430ec ["INT_ADD", "register:40f0:8", ["const:4430ec:8", "const:4:8"]]
- 004430ec ["CALL", null, ["callee:00c53da0:8"]]
+ 0044312c ["INT_ADD", "register:40f0:8", ["const:44312c:8", "const:4:8"]]
+ 0044312c ["CALL", null, ["callee:00c53da0:8"]]
- 004430ec bytes 05432094
+ 0044312c bytes 1d432094
- 00443100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00443100 ["INT_ADD", "register:40f0:8", ["const:443100:8", "const:4:8"]]
- 00443100 ["CALLIND", null, ["register:0:8"]]
+ 00443140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00443140 ["INT_ADD", "register:40f0:8", ["const:443140:8", "const:4:8"]]
+ 00443140 ["CALLIND", null, ["register:0:8"]]
- 00443100 bytes 00013fd6
+ 00443140 bytes 00013fd6
- 00443108 ["INT_ADD", "register:40f0:8", ["const:443108:8", "const:4:8"]]
- 00443108 ["CALL", null, ["callee:00c57f50:8"]]
+ 00443148 ["INT_ADD", "register:40f0:8", ["const:443148:8", "const:4:8"]]
+ 00443148 ["CALL", null, ["callee:00c57f50:8"]]
- 00443108 bytes 5e532094
+ 00443148 bytes 82532094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-759cead20135eae87ee6084aff2ce31a"></a>

### [`0044324c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/0044324c.md) → [`0044328c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044328c.md) FUN_0044328c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00443280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/0044324c.md#insn-00443280) · [`00443298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/0044324c.md#insn-00443298) · [`004432ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/0044324c.md#insn-004432ac)
- 新版 `004432c0`（命令位置の公開資料なし） · `004432d8`（命令位置の公開資料なし） · `004432ec`（命令位置の公開資料なし）

~~~diff
- 00443280 ["INT_ADD", "register:40f0:8", ["const:443280:8", "const:4:8"]]
- 00443280 ["CALL", null, ["callee:00c53d70:8"]]
+ 004432c0 ["INT_ADD", "register:40f0:8", ["const:4432c0:8", "const:4:8"]]
+ 004432c0 ["CALL", null, ["callee:00c53d70:8"]]
- 00443280 bytes 94422094
+ 004432c0 bytes ac422094
- 00443298 ["COPY", "register:0:8", ["register:4040:8"]]
- 00443298 ["INT_ADD", "register:40f0:8", ["const:443298:8", "const:4:8"]]
- 00443298 ["CALLIND", null, ["register:0:8"]]
+ 004432d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004432d8 ["INT_ADD", "register:40f0:8", ["const:4432d8:8", "const:4:8"]]
+ 004432d8 ["CALLIND", null, ["register:0:8"]]
- 00443298 bytes 00013fd6
+ 004432d8 bytes 00013fd6
- 004432ac ["INT_ADD", "register:40f0:8", ["const:4432ac:8", "const:4:8"]]
- 004432ac ["CALL", null, ["callee:00c53da0:8"]]
+ 004432ec ["INT_ADD", "register:40f0:8", ["const:4432ec:8", "const:4:8"]]
+ 004432ec ["CALL", null, ["callee:00c53da0:8"]]
- 004432ac bytes 95422094
+ 004432ec bytes ad422094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7227615774736ad15e8494fbf0bd2ed6"></a>

### [`00443398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443398.md) → [`004433d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433d8.md) FUN_004433d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d5f4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004433c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443398.md#insn-004433c4) · [`004433d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443398.md#insn-004433d8) · [`004433e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443398.md#insn-004433e0)
- 新版 `00443404`（命令位置の公開資料なし） · `00443418`（命令位置の公開資料なし） · `00443420`（命令位置の公開資料なし）

~~~diff
- 004433c4 ["INT_ADD", "register:40f0:8", ["const:4433c4:8", "const:4:8"]]
- 004433c4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00443404 ["INT_ADD", "register:40f0:8", ["const:443404:8", "const:4:8"]]
+ 00443404 ["CALL", null, ["callee:00c53da0:8"]]
- 004433c4 bytes 4f422094
+ 00443404 bytes 67422094
- 004433d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004433d8 ["INT_ADD", "register:40f0:8", ["const:4433d8:8", "const:4:8"]]
- 004433d8 ["CALLIND", null, ["register:0:8"]]
+ 00443418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00443418 ["INT_ADD", "register:40f0:8", ["const:443418:8", "const:4:8"]]
+ 00443418 ["CALLIND", null, ["register:0:8"]]
- 004433d8 bytes 00013fd6
+ 00443418 bytes 00013fd6
- 004433e0 ["INT_ADD", "register:40f0:8", ["const:4433e0:8", "const:4:8"]]
- 004433e0 ["CALL", null, ["callee:00c57f50:8"]]
+ 00443420 ["INT_ADD", "register:40f0:8", ["const:443420:8", "const:4:8"]]
+ 00443420 ["CALL", null, ["callee:00c57f50:8"]]
- 004433e0 bytes a8522094
+ 00443420 bytes cc522094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-659b059338bdbbf2da7f267bf2988dea"></a>

### [`00444614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444614.md) → [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) FUN_00444654

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00443e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00443/00443e4c.md) [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444154.md) [`00444464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444464.md) [`004460ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004460ec.md) · 呼出先 3件 [`0044ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ac68.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 7件 [`00443e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443e8c.md) [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00444194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md) [`004444a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md) [`0044612c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md) · 呼出先 3件 [`0044aca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aca8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00444630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444614.md#insn-00444630) · [`00444644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444614.md#insn-00444644) · [`00444664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444614.md#insn-00444664)
- 新版 `00444670`（命令位置の公開資料なし） · `00444684`（命令位置の公開資料なし） · `004446a4`（命令位置の公開資料なし）

~~~diff
- 00444630 ["INT_ADD", "register:40f0:8", ["const:444630:8", "const:4:8"]]
- 00444630 ["CALL", null, ["callee:0044aca8:8"]]
+ 00444670 ["INT_ADD", "register:40f0:8", ["const:444670:8", "const:4:8"]]
+ 00444670 ["CALL", null, ["callee:0044aca8:8"]]
- 00444630 bytes 8e190094
+ 00444670 bytes 8e190094
- 00444644 ["INT_ADD", "register:40f0:8", ["const:444644:8", "const:4:8"]]
- 00444644 ["CALL", null, ["callee:00c53da0:8"]]
+ 00444684 ["INT_ADD", "register:40f0:8", ["const:444684:8", "const:4:8"]]
+ 00444684 ["CALL", null, ["callee:00c53da0:8"]]
- 00444644 bytes af3d2094
+ 00444684 bytes c73d2094
- 00444664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00444664 ["INT_ADD", "register:40f0:8", ["const:444664:8", "const:4:8"]]
- 00444664 ["CALLIND", null, ["register:0:8"]]
+ 004446a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004446a4 ["INT_ADD", "register:40f0:8", ["const:4446a4:8", "const:4:8"]]
+ 004446a4 ["CALLIND", null, ["register:0:8"]]
- 00444664 bytes 00013fd6
+ 004446a4 bytes 00013fd6
~~~


<a id="compare-89eb07cd9f4240e3036042f5d8315afc"></a>

### [`00446530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446530.md) → [`00446570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446570.md) FUN_00446570

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446530.md#insn-0044654c) · [`0044656c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446530.md#insn-0044656c)
- 新版 `0044658c`（命令位置の公開資料なし） · `004465ac`（命令位置の公開資料なし）

~~~diff
- 0044654c ["INT_ADD", "register:40f0:8", ["const:44654c:8", "const:4:8"]]
- 0044654c ["CALL", null, ["callee:00c53da0:8"]]
+ 0044658c ["INT_ADD", "register:40f0:8", ["const:44658c:8", "const:4:8"]]
+ 0044658c ["CALL", null, ["callee:00c53da0:8"]]
- 0044654c bytes ed352094
+ 0044658c bytes 05362094
- 0044656c ["COPY", "register:0:8", ["register:4040:8"]]
- 0044656c ["INT_ADD", "register:40f0:8", ["const:44656c:8", "const:4:8"]]
- 0044656c ["CALLIND", null, ["register:0:8"]]
+ 004465ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004465ac ["INT_ADD", "register:40f0:8", ["const:4465ac:8", "const:4:8"]]
+ 004465ac ["CALLIND", null, ["register:0:8"]]
- 0044656c bytes 00013fd6
+ 004465ac bytes 00013fd6
~~~


<a id="compare-da2f9a50aee329cc158eba1828ca163c"></a>

### [`00446580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446580.md) → [`004465c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/004465c0.md) FUN_004465c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044659c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446580.md#insn-0044659c) · [`004465bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446580.md#insn-004465bc)
- 新版 `004465dc`（命令位置の公開資料なし） · `004465fc`（命令位置の公開資料なし）

~~~diff
- 0044659c ["INT_ADD", "register:40f0:8", ["const:44659c:8", "const:4:8"]]
- 0044659c ["CALL", null, ["callee:00c53da0:8"]]
+ 004465dc ["INT_ADD", "register:40f0:8", ["const:4465dc:8", "const:4:8"]]
+ 004465dc ["CALL", null, ["callee:00c53da0:8"]]
- 0044659c bytes d9352094
+ 004465dc bytes f1352094
- 004465bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004465bc ["INT_ADD", "register:40f0:8", ["const:4465bc:8", "const:4:8"]]
- 004465bc ["CALLIND", null, ["register:0:8"]]
+ 004465fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004465fc ["INT_ADD", "register:40f0:8", ["const:4465fc:8", "const:4:8"]]
+ 004465fc ["CALLIND", null, ["register:0:8"]]
- 004465bc bytes 00013fd6
+ 004465fc bytes 00013fd6
~~~


<a id="compare-b3b59e386572f07c1f7f552bf9741ea8"></a>

### [`004465d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004465d0.md) → [`00446610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446610.md) FUN_00446610

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004465ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004465d0.md#insn-004465ec)
- 新版 `0044662c`（命令位置の公開資料なし）

~~~diff
- 004465ec ["INT_ADD", "register:40f0:8", ["const:4465ec:8", "const:4:8"]]
- 004465ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0044662c ["INT_ADD", "register:40f0:8", ["const:44662c:8", "const:4:8"]]
+ 0044662c ["CALL", null, ["callee:00c57f80:8"]]
- 004465ec bytes 31462094
+ 0044662c bytes 55462094
~~~


<a id="compare-2ada69315eb58dfbeaf1e038574ddbb6"></a>

### [`00446a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446a48.md) → [`00446a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446a88.md) FUN_00446a88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00877a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00877a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md) · 呼出先 2件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00446a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446a48.md#insn-00446a58)
- 新版 `00446a98`（命令位置の公開資料なし）

~~~diff
- 00446a58 ["INT_ADD", "register:40f0:8", ["const:446a58:8", "const:4:8"]]
- 00446a58 ["CALL", null, ["callee:00c581b0:8"]]
+ 00446a98 ["INT_ADD", "register:40f0:8", ["const:446a98:8", "const:4:8"]]
+ 00446a98 ["CALL", null, ["callee:00c581b0:8"]]
- 00446a58 bytes a2452094
+ 00446a98 bytes c6452094
~~~


<a id="compare-c5e5c4f01f907aee3f8d747b1d87e8a4"></a>

### [`00446c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446c2c.md) → [`00446c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446c6c.md) FUN_00446c6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00446b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446b28.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 1件 [`00446b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b68.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00446c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446c2c.md#insn-00446c54) · [`00446c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446c2c.md#insn-00446c64) · [`00446c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446c2c.md#insn-00446c6c)
- 新版 `00446c94`（命令位置の公開資料なし） · `00446ca4`（命令位置の公開資料なし） · `00446cac`（命令位置の公開資料なし）

~~~diff
- 00446c54 ["INT_ADD", "register:40f0:8", ["const:446c54:8", "const:4:8"]]
- 00446c54 ["CALL", null, ["callee:00c58200:8"]]
+ 00446c94 ["INT_ADD", "register:40f0:8", ["const:446c94:8", "const:4:8"]]
+ 00446c94 ["CALL", null, ["callee:00c58200:8"]]
- 00446c54 bytes 37452094
+ 00446c94 bytes 5b452094
- 00446c64 ["INT_ADD", "register:40f0:8", ["const:446c64:8", "const:4:8"]]
- 00446c64 ["CALL", null, ["callee:00c58210:8"]]
+ 00446ca4 ["INT_ADD", "register:40f0:8", ["const:446ca4:8", "const:4:8"]]
+ 00446ca4 ["CALL", null, ["callee:00c58210:8"]]
- 00446c64 bytes 37452094
+ 00446ca4 bytes 5b452094
- 00446c6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00446c6c ["INT_ADD", "register:40f0:8", ["const:446c6c:8", "const:4:8"]]
- 00446c6c ["CALLIND", null, ["register:0:8"]]
+ 00446cac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00446cac ["INT_ADD", "register:40f0:8", ["const:446cac:8", "const:4:8"]]
+ 00446cac ["CALLIND", null, ["register:0:8"]]
- 00446c6c bytes 00013fd6
+ 00446cac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a74929d4cde2d14bcaba65bfdf8b118f"></a>

### [`00446ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446ce4.md) → [`00446d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446d24.md) FUN_00446d24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00446d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446ce4.md#insn-00446d0c) · [`00446d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446ce4.md#insn-00446d14)
- 新版 `00446d4c`（命令位置の公開資料なし） · `00446d54`（命令位置の公開資料なし）

~~~diff
- 00446d0c ["INT_ADD", "register:40f0:8", ["const:446d0c:8", "const:4:8"]]
- 00446d0c ["CALL", null, ["callee:00c58220:8"]]
+ 00446d4c ["INT_ADD", "register:40f0:8", ["const:446d4c:8", "const:4:8"]]
+ 00446d4c ["CALL", null, ["callee:00c58220:8"]]
- 00446d0c bytes 11452094
+ 00446d4c bytes 35452094
- 00446d14 ["INT_ADD", "register:40f0:8", ["const:446d14:8", "const:4:8"]]
- 00446d14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00446d54 ["INT_ADD", "register:40f0:8", ["const:446d54:8", "const:4:8"]]
+ 00446d54 ["CALL", null, ["callee:00c57f80:8"]]
- 00446d14 bytes 67442094
+ 00446d54 bytes 8b442094
~~~


<a id="compare-4ac0c0c851da6d7757b7cabbc3848c1a"></a>

### [`00446d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d34.md) → [`00446d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446d74.md) FUN_00446d74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00446d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d34.md#insn-00446d50)
- 新版 `00446d90`（命令位置の公開資料なし）

~~~diff
- 00446d50 ["INT_ADD", "register:40f0:8", ["const:446d50:8", "const:4:8"]]
- 00446d50 ["CALL", null, ["callee:00c58220:8"]]
+ 00446d90 ["INT_ADD", "register:40f0:8", ["const:446d90:8", "const:4:8"]]
+ 00446d90 ["CALL", null, ["callee:00c58220:8"]]
- 00446d50 bytes 00452094
+ 00446d90 bytes 24452094
~~~


<a id="compare-7e8dba41e9ae264cc6e38492620e0ffb"></a>

### [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md) → [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) FUN_00446db0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00444680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444680.md) [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md) [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) · 呼出先 2件 [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) [`00b07a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md) · 呼出先 2件 [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00446d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md#insn-00446d8c) · [`00446d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md#insn-00446d98) · [`00446da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md#insn-00446da8)
- 新版 `00446dcc`（命令位置の公開資料なし） · `00446dd8`（命令位置の公開資料なし） · `00446de8`（命令位置の公開資料なし）

~~~diff
- 00446d8c ["INT_ADD", "register:40f0:8", ["const:446d8c:8", "const:4:8"]]
- 00446d8c ["CALL", null, ["local:b0:8"]]
+ 00446dcc ["INT_ADD", "register:40f0:8", ["const:446dcc:8", "const:4:8"]]
+ 00446dcc ["CALL", null, ["local:b0:8"]]
- 00446d8c bytes f9ffff97
+ 00446dcc bytes f9ffff97
- 00446d98 ["INT_ADD", "register:40f0:8", ["const:446d98:8", "const:4:8"]]
- 00446d98 ["CALL", null, ["local:b0:8"]]
+ 00446dd8 ["INT_ADD", "register:40f0:8", ["const:446dd8:8", "const:4:8"]]
+ 00446dd8 ["CALL", null, ["local:b0:8"]]
- 00446d98 bytes f6ffff97
+ 00446dd8 bytes f6ffff97
- 00446da8 ["INT_ADD", "register:40f0:8", ["const:446da8:8", "const:4:8"]]
- 00446da8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00446de8 ["INT_ADD", "register:40f0:8", ["const:446de8:8", "const:4:8"]]
+ 00446de8 ["CALL", null, ["callee:00c57f80:8"]]
- 00446da8 bytes 42442094
+ 00446de8 bytes 66442094
~~~


<a id="compare-d9da1e83f3c1882f0f5902280062ca15"></a>

### [`0044982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/0044982c.md) → [`0044986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/0044986c.md) FUN_0044986c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0048d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d91c.md) [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md) · 呼出先 3件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0048d95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d95c.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) · 呼出先 3件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00449868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/0044982c.md#insn-00449868) · [`00449880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/0044982c.md#insn-00449880) · [`004498a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/0044982c.md#insn-004498a4)
- 新版 `004498a8`（命令位置の公開資料なし） · `004498c0`（命令位置の公開資料なし） · `004498e4`（命令位置の公開資料なし）

~~~diff
- 00449868 ["INT_ADD", "register:40f0:8", ["const:449868:8", "const:4:8"]]
- 00449868 ["CALL", null, ["callee:00c57f60:8"]]
+ 004498a8 ["INT_ADD", "register:40f0:8", ["const:4498a8:8", "const:4:8"]]
+ 004498a8 ["CALL", null, ["callee:00c57f60:8"]]
- 00449868 bytes 8a392094
+ 004498a8 bytes ae392094
- 00449880 ["INT_ADD", "register:40f0:8", ["const:449880:8", "const:4:8"]]
- 00449880 ["CALL", null, ["callee:00c580d0:8"]]
+ 004498c0 ["INT_ADD", "register:40f0:8", ["const:4498c0:8", "const:4:8"]]
+ 004498c0 ["CALL", null, ["callee:00c580d0:8"]]
- 00449880 bytes e0392094
+ 004498c0 bytes 043a2094
- 004498a4 ["INT_ADD", "register:40f0:8", ["const:4498a4:8", "const:4:8"]]
- 004498a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004498e4 ["INT_ADD", "register:40f0:8", ["const:4498e4:8", "const:4:8"]]
+ 004498e4 ["CALL", null, ["callee:00c57f60:8"]]
- 004498a4 bytes 7b392094
+ 004498e4 bytes 9f392094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edcfbdd4e9eaff0af7bdd9cf3ad28655"></a>

### [`0044ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ac68.md) → [`0044aca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aca8.md) FUN_0044aca8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00444614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444614.md) [`00446614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446614.md) · 呼出先 7件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 2件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00446654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446654.md) · 呼出先 7件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ac68.md#insn-0044ac80) · [`0044ac88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ac68.md#insn-0044ac88) · [`0044ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ac68.md#insn-0044ac90)
- 新版 `0044acc0`（命令位置の公開資料なし） · `0044acc8`（命令位置の公開資料なし） · `0044acd0`（命令位置の公開資料なし）

~~~diff
- 0044ac80 ["INT_ADD", "register:40f0:8", ["const:44ac80:8", "const:4:8"]]
- 0044ac80 ["CALL", null, ["callee:00c581b0:8"]]
+ 0044acc0 ["INT_ADD", "register:40f0:8", ["const:44acc0:8", "const:4:8"]]
+ 0044acc0 ["CALL", null, ["callee:00c581b0:8"]]
- 0044ac80 bytes 18352094
+ 0044acc0 bytes 3c352094
- 0044ac88 ["INT_ADD", "register:40f0:8", ["const:44ac88:8", "const:4:8"]]
- 0044ac88 ["CALL", null, ["callee:00c581c0:8"]]
+ 0044acc8 ["INT_ADD", "register:40f0:8", ["const:44acc8:8", "const:4:8"]]
+ 0044acc8 ["CALL", null, ["callee:00c581c0:8"]]
- 0044ac88 bytes 1a352094
+ 0044acc8 bytes 3e352094
- 0044ac90 ["INT_ADD", "register:40f0:8", ["const:44ac90:8", "const:4:8"]]
- 0044ac90 ["CALL", null, ["callee:00c58240:8"]]
+ 0044acd0 ["INT_ADD", "register:40f0:8", ["const:44acd0:8", "const:4:8"]]
+ 0044acd0 ["CALL", null, ["callee:00c58240:8"]]
- 0044ac90 bytes 38352094
+ 0044acd0 bytes 5c352094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64dd2d93a475f3361fbb639bacf2d88e"></a>

### [`0044accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044accc.md) → [`0044ad0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ad0c.md) FUN_0044ad0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`005944b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`005944f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005944f0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044accc.md#insn-0044ad50) · [`0044ad7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044accc.md#insn-0044ad7c)
- 新版 `0044ad90`（命令位置の公開資料なし） · `0044adbc`（命令位置の公開資料なし）

~~~diff
- 0044ad50 ["INT_ADD", "register:40f0:8", ["const:44ad50:8", "const:4:8"]]
- 0044ad50 ["CALL", null, ["callee:00c58120:8"]]
+ 0044ad90 ["INT_ADD", "register:40f0:8", ["const:44ad90:8", "const:4:8"]]
+ 0044ad90 ["CALL", null, ["callee:00c58120:8"]]
- 0044ad50 bytes c0342094
+ 0044ad90 bytes e4342094
- 0044ad7c ["INT_ADD", "register:40f0:8", ["const:44ad7c:8", "const:4:8"]]
- 0044ad7c ["CALL", null, ["callee:00c58120:8"]]
+ 0044adbc ["INT_ADD", "register:40f0:8", ["const:44adbc:8", "const:4:8"]]
+ 0044adbc ["CALL", null, ["callee:00c58120:8"]]
- 0044ad7c bytes b5342094
+ 0044adbc bytes d9342094
~~~


<a id="compare-2ac7350cdf9061850cfdb174639ebc22"></a>

### [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) → [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) FUN_0044fcfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`004b4ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md) [`004b5c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md) [`004cc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc3a0.md) [`004e5c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5c14.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 17件 [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) [`004b4af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4af8.md) [`004b5cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5cc8.md) [`004cc3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc3e0.md) [`004e5c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e5/004e5c54.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044fce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md#insn-0044fce4)
- 新版 `0044fd24`（命令位置の公開資料なし）

~~~diff
- 0044fce4 ["INT_ADD", "register:40f0:8", ["const:44fce4:8", "const:4:8"]]
- 0044fce4 ["CALL", null, ["callee:00c58050:8"]]
+ 0044fd24 ["INT_ADD", "register:40f0:8", ["const:44fd24:8", "const:4:8"]]
+ 0044fd24 ["CALL", null, ["callee:00c58050:8"]]
- 0044fce4 bytes a7202094
+ 0044fd24 bytes cb202094
~~~


<a id="compare-28f3c00efda9f3769c02b35beb3cf96e"></a>

### [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) → [`0044ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044ff9c.md) FUN_0044ff9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) · 呼出先 9件 [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0055eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md) [`00560454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560454.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md)
- 新版 呼出元 2件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) · 呼出先 9件 [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`0055eb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md) [`00560494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560494.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ff90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md#insn-0044ff90) · [`0044ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md#insn-0044ffa0) · [`0044ffb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md#insn-0044ffb0)
- 新版 `0044ffd0`（命令位置の公開資料なし） · `0044ffe0`（命令位置の公開資料なし） · `0044fff0`（命令位置の公開資料なし）

~~~diff
- 0044ff90 ["INT_ADD", "register:40f0:8", ["const:44ff90:8", "const:4:8"]]
- 0044ff90 ["CALL", null, ["callee:00560494:8"]]
+ 0044ffd0 ["INT_ADD", "register:40f0:8", ["const:44ffd0:8", "const:4:8"]]
+ 0044ffd0 ["CALL", null, ["callee:00560494:8"]]
- 0044ff90 bytes 31410494
+ 0044ffd0 bytes 31410494
- 0044ffa0 ["INT_ADD", "register:40f0:8", ["const:44ffa0:8", "const:4:8"]]
- 0044ffa0 ["CALL", null, ["callee:00560498:8"]]
+ 0044ffe0 ["INT_ADD", "register:40f0:8", ["const:44ffe0:8", "const:4:8"]]
+ 0044ffe0 ["CALL", null, ["callee:00560498:8"]]
- 0044ffa0 bytes 2e410494
+ 0044ffe0 bytes 2e410494
- 0044ffb0 ["INT_ADD", "register:40f0:8", ["const:44ffb0:8", "const:4:8"]]
- 0044ffb0 ["CALL", null, ["callee:00440fb0:8"]]
+ 0044fff0 ["INT_ADD", "register:40f0:8", ["const:44fff0:8", "const:4:8"]]
+ 0044fff0 ["CALL", null, ["callee:00440fb0:8"]]
- 0044ffb0 bytes f0c3ff97
+ 0044fff0 bytes f0c3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-026f8f94a585fb5d1d1615a2045c7ae2"></a>

### [`00450700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450700.md) → [`00450740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450740.md) FUN_00450740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450700.md#insn-0045071c) · [`0045073c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450700.md#insn-0045073c)
- 新版 `0045075c`（命令位置の公開資料なし） · `0045077c`（命令位置の公開資料なし）

~~~diff
- 0045071c ["INT_ADD", "register:40f0:8", ["const:45071c:8", "const:4:8"]]
- 0045071c ["CALL", null, ["callee:00c53da0:8"]]
+ 0045075c ["INT_ADD", "register:40f0:8", ["const:45075c:8", "const:4:8"]]
+ 0045075c ["CALL", null, ["callee:00c53da0:8"]]
- 0045071c bytes 790d2094
+ 0045075c bytes 910d2094
- 0045073c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045073c ["INT_ADD", "register:40f0:8", ["const:45073c:8", "const:4:8"]]
- 0045073c ["CALLIND", null, ["register:0:8"]]
+ 0045077c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045077c ["INT_ADD", "register:40f0:8", ["const:45077c:8", "const:4:8"]]
+ 0045077c ["CALLIND", null, ["register:0:8"]]
- 0045073c bytes 00013fd6
+ 0045077c bytes 00013fd6
~~~


<a id="compare-735ee13a16419abb0af811867432676f"></a>

### [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md) → [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md) FUN_00451e0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045aa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa8c.md) [`0045aa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md) [`0045ab3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab3c.md) [`0045ab44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab44.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`0045aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aacc.md) [`0045aadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md) [`0045ab7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab7c.md) [`0045ab84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab84.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md#insn-00451e08) · [`00451e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md#insn-00451e38) · [`00451e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md#insn-00451e48)
- 新版 `00451e48`（命令位置の公開資料なし） · `00451e78`（命令位置の公開資料なし） · `00451e88`（命令位置の公開資料なし）

~~~diff
- 00451e08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451e08 ["INT_ADD", "register:40f0:8", ["const:451e08:8", "const:4:8"]]
- 00451e08 ["CALLIND", null, ["register:0:8"]]
+ 00451e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00451e48 ["INT_ADD", "register:40f0:8", ["const:451e48:8", "const:4:8"]]
+ 00451e48 ["CALLIND", null, ["register:0:8"]]
- 00451e08 bytes 00013fd6
+ 00451e48 bytes 00013fd6
- 00451e38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451e38 ["INT_ADD", "register:40f0:8", ["const:451e38:8", "const:4:8"]]
- 00451e38 ["CALLIND", null, ["register:0:8"]]
+ 00451e78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00451e78 ["INT_ADD", "register:40f0:8", ["const:451e78:8", "const:4:8"]]
+ 00451e78 ["CALLIND", null, ["register:0:8"]]
- 00451e38 bytes 00013fd6
+ 00451e78 bytes 00013fd6
- 00451e48 ["INT_ADD", "register:40f0:8", ["const:451e48:8", "const:4:8"]]
- 00451e48 ["CALL", null, ["callee:00c57f80:8"]]
+ 00451e88 ["INT_ADD", "register:40f0:8", ["const:451e88:8", "const:4:8"]]
+ 00451e88 ["CALL", null, ["callee:00c57f80:8"]]
- 00451e48 bytes 1a182094
+ 00451e88 bytes 3e182094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf89357052eca8b6d6ac66d1729fac9"></a>

### [`00452bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452bc4.md) → [`00452c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c04.md) FUN_00452c04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00452c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452bc4.md#insn-00452c04)
- 新版 `00452c44`（命令位置の公開資料なし）

~~~diff
- 00452c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00452c04 ["INT_ADD", "register:40f0:8", ["const:452c04:8", "const:4:8"]]
- 00452c04 ["CALLIND", null, ["register:0:8"]]
+ 00452c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00452c44 ["INT_ADD", "register:40f0:8", ["const:452c44:8", "const:4:8"]]
+ 00452c44 ["CALLIND", null, ["register:0:8"]]
- 00452c04 bytes 00013fd6
+ 00452c44 bytes 00013fd6
~~~


<a id="compare-25f69aa5b7368eea5dc67b4af0d1a2a2"></a>

### [`004531d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004531d8.md) → [`00453218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453218.md) FUN_00453218

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00453218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004531d8.md#insn-00453218)
- 新版 `00453258`（命令位置の公開資料なし）

~~~diff
- 00453218 ["COPY", "register:0:8", ["register:4040:8"]]
- 00453218 ["INT_ADD", "register:40f0:8", ["const:453218:8", "const:4:8"]]
- 00453218 ["CALLIND", null, ["register:0:8"]]
+ 00453258 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00453258 ["INT_ADD", "register:40f0:8", ["const:453258:8", "const:4:8"]]
+ 00453258 ["CALLIND", null, ["register:0:8"]]
- 00453218 bytes 00013fd6
+ 00453258 bytes 00013fd6
~~~


<a id="compare-cfeb1936f4d1fbbecaae9cd2b515b654"></a>

### [`00453268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453268.md) → [`004532a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532a8.md) FUN_004532a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00453284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453268.md#insn-00453284) · [`004532a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453268.md#insn-004532a4)
- 新版 `004532c4`（命令位置の公開資料なし） · `004532e4`（命令位置の公開資料なし）

~~~diff
- 00453284 ["INT_ADD", "register:40f0:8", ["const:453284:8", "const:4:8"]]
- 00453284 ["CALL", null, ["callee:00c53da0:8"]]
+ 004532c4 ["INT_ADD", "register:40f0:8", ["const:4532c4:8", "const:4:8"]]
+ 004532c4 ["CALL", null, ["callee:00c53da0:8"]]
- 00453284 bytes 9f022094
+ 004532c4 bytes b7022094
- 004532a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004532a4 ["INT_ADD", "register:40f0:8", ["const:4532a4:8", "const:4:8"]]
- 004532a4 ["CALLIND", null, ["register:0:8"]]
+ 004532e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004532e4 ["INT_ADD", "register:40f0:8", ["const:4532e4:8", "const:4:8"]]
+ 004532e4 ["CALLIND", null, ["register:0:8"]]
- 004532a4 bytes 00013fd6
+ 004532e4 bytes 00013fd6
~~~


<a id="compare-c4458aea02712b91863dd4b8e7959518"></a>

### [`00453c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453c60.md) → [`00453ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453ca0.md) FUN_00453ca0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00453c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453c60.md#insn-00453c7c) · [`00453c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453c60.md#insn-00453c9c)
- 新版 `00453cbc`（命令位置の公開資料なし） · `00453cdc`（命令位置の公開資料なし）

~~~diff
- 00453c7c ["INT_ADD", "register:40f0:8", ["const:453c7c:8", "const:4:8"]]
- 00453c7c ["CALL", null, ["callee:00c53da0:8"]]
+ 00453cbc ["INT_ADD", "register:40f0:8", ["const:453cbc:8", "const:4:8"]]
+ 00453cbc ["CALL", null, ["callee:00c53da0:8"]]
- 00453c7c bytes 21002094
+ 00453cbc bytes 39002094
- 00453c9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00453c9c ["INT_ADD", "register:40f0:8", ["const:453c9c:8", "const:4:8"]]
- 00453c9c ["CALLIND", null, ["register:0:8"]]
+ 00453cdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00453cdc ["INT_ADD", "register:40f0:8", ["const:453cdc:8", "const:4:8"]]
+ 00453cdc ["CALLIND", null, ["register:0:8"]]
- 00453c9c bytes 00013fd6
+ 00453cdc bytes 00013fd6
~~~


<a id="compare-5c11395ceee8e6736d40b5b62b32b02a"></a>

### [`004543bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/004543bc.md) → [`004543fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/004543fc.md) FUN_004543fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/004543bc.md#insn-004543d8) · [`004543f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/004543bc.md#insn-004543f8)
- 新版 `00454418`（命令位置の公開資料なし） · `00454438`（命令位置の公開資料なし）

~~~diff
- 004543d8 ["INT_ADD", "register:40f0:8", ["const:4543d8:8", "const:4:8"]]
- 004543d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00454418 ["INT_ADD", "register:40f0:8", ["const:454418:8", "const:4:8"]]
+ 00454418 ["CALL", null, ["callee:00c53da0:8"]]
- 004543d8 bytes 4afe1f94
+ 00454418 bytes 62fe1f94
- 004543f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004543f8 ["INT_ADD", "register:40f0:8", ["const:4543f8:8", "const:4:8"]]
- 004543f8 ["CALLIND", null, ["register:0:8"]]
+ 00454438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00454438 ["INT_ADD", "register:40f0:8", ["const:454438:8", "const:4:8"]]
+ 00454438 ["CALLIND", null, ["register:0:8"]]
- 004543f8 bytes 00013fd6
+ 00454438 bytes 00013fd6
~~~


<a id="compare-ef3222cde13eaff4efa67e5eebaed88e"></a>

### [`004581cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004581cc.md) → [`0045820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045820c.md) FUN_0045820c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00458204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004581cc.md#insn-00458204) · [`00458214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004581cc.md#insn-00458214)
- 新版 `00458244`（命令位置の公開資料なし） · `00458254`（命令位置の公開資料なし）

~~~diff
- 00458204 ["INT_ADD", "register:40f0:8", ["const:458204:8", "const:4:8"]]
- 00458204 ["CALL", null, ["callee:00c57f80:8"]]
+ 00458244 ["INT_ADD", "register:40f0:8", ["const:458244:8", "const:4:8"]]
+ 00458244 ["CALL", null, ["callee:00c57f80:8"]]
- 00458204 bytes 2bff1f94
+ 00458244 bytes 4fff1f94
- 00458214 ["INT_ADD", "register:40f0:8", ["const:458214:8", "const:4:8"]]
- 00458214 ["CALL", null, ["callee:00c57f80:8"]]
+ 00458254 ["INT_ADD", "register:40f0:8", ["const:458254:8", "const:4:8"]]
+ 00458254 ["CALL", null, ["callee:00c57f80:8"]]
- 00458214 bytes 27ff1f94
+ 00458254 bytes 4bff1f94
~~~


<a id="compare-69eb56f82dd99491ba80a20725ab5458"></a>

### [`00458d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md) → [`00458d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458d68.md) FUN_00458d68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) · 呼出先 2件 [`00458e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) · 呼出先 2件 [`00458ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458ed0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00458da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md#insn-00458da4) · [`00458e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md#insn-00458e00) · [`00458e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md#insn-00458e3c)
- 新版 `00458de4`（命令位置の公開資料なし） · `00458e40`（命令位置の公開資料なし） · `00458e7c`（命令位置の公開資料なし）

~~~diff
- 00458da4 ["INT_ADD", "register:40f0:8", ["const:458da4:8", "const:4:8"]]
- 00458da4 ["CALL", null, ["callee:00c58120:8"]]
+ 00458de4 ["INT_ADD", "register:40f0:8", ["const:458de4:8", "const:4:8"]]
+ 00458de4 ["CALL", null, ["callee:00c58120:8"]]
- 00458da4 bytes abfc1f94
+ 00458de4 bytes cffc1f94
- 00458e00 ["INT_ADD", "register:40f0:8", ["const:458e00:8", "const:4:8"]]
- 00458e00 ["CALL", null, ["callee:00c58120:8"]]
+ 00458e40 ["INT_ADD", "register:40f0:8", ["const:458e40:8", "const:4:8"]]
+ 00458e40 ["CALL", null, ["callee:00c58120:8"]]
- 00458e00 bytes 94fc1f94
+ 00458e40 bytes b8fc1f94
- 00458e3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00458e3c ["INT_ADD", "register:40f0:8", ["const:458e3c:8", "const:4:8"]]
- 00458e3c ["CALLIND", null, ["register:0:8"]]
+ 00458e7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00458e7c ["INT_ADD", "register:40f0:8", ["const:458e7c:8", "const:4:8"]]
+ 00458e7c ["CALLIND", null, ["register:0:8"]]
- 00458e3c bytes 00013fd6
+ 00458e7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7208a0635ae59f048dda69fbed3365f0"></a>

### [`00458e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md) → [`00458ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458ed0.md) FUN_00458ed0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00458d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00458d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458d68.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00458ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md#insn-00458ed0) · [`00458ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md#insn-00458ef0) · [`00458f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md#insn-00458f24)
- 新版 `00458f10`（命令位置の公開資料なし） · `00458f30`（命令位置の公開資料なし） · `00458f64`（命令位置の公開資料なし）

~~~diff
- 00458ed0 ["INT_ADD", "register:40f0:8", ["const:458ed0:8", "const:4:8"]]
- 00458ed0 ["CALL", null, ["callee:0045900c:8"]]
+ 00458f10 ["INT_ADD", "register:40f0:8", ["const:458f10:8", "const:4:8"]]
+ 00458f10 ["CALL", null, ["callee:0045900c:8"]]
- 00458ed0 bytes 3f000094
+ 00458f10 bytes 3f000094
- 00458ef0 ["INT_ADD", "register:40f0:8", ["const:458ef0:8", "const:4:8"]]
- 00458ef0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00458f30 ["INT_ADD", "register:40f0:8", ["const:458f30:8", "const:4:8"]]
+ 00458f30 ["CALL", null, ["callee:00c57f60:8"]]
- 00458ef0 bytes e8fb1f94
+ 00458f30 bytes 0cfc1f94
- 00458f24 ["INT_ADD", "register:40f0:8", ["const:458f24:8", "const:4:8"]]
- 00458f24 ["CALL", null, ["callee:0043bb60:8"]]
+ 00458f64 ["INT_ADD", "register:40f0:8", ["const:458f64:8", "const:4:8"]]
+ 00458f64 ["CALL", null, ["callee:0043bb60:8"]]
- 00458f24 bytes ff8aff97
+ 00458f64 bytes ff8aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858eaceece8a2a2267dbedd9bf59e29a"></a>

### [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) → [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) FUN_0045900c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00458e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458e90.md) [`00459994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md) [`00459c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md) [`00597230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md) [`0059736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md) · 呼出先 2件 [`004592cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004592cc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 5件 [`00458ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458ed0.md) [`004599d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004599d4.md) [`00459c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459c78.md) [`00597270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597270.md) [`005973ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005973ac.md) · 呼出先 2件 [`0045930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045930c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md#insn-00459054) · [`004590a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md#insn-004590a8) · [`00459144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md#insn-00459144)
- 新版 `00459094`（命令位置の公開資料なし） · `004590e8`（命令位置の公開資料なし） · `00459184`（命令位置の公開資料なし）

~~~diff
- 00459054 ["INT_ADD", "register:40f0:8", ["const:459054:8", "const:4:8"]]
- 00459054 ["CALL", null, ["callee:00c58120:8"]]
+ 00459094 ["INT_ADD", "register:40f0:8", ["const:459094:8", "const:4:8"]]
+ 00459094 ["CALL", null, ["callee:00c58120:8"]]
- 00459054 bytes fffb1f94
+ 00459094 bytes 23fc1f94
- 004590a8 ["INT_ADD", "register:40f0:8", ["const:4590a8:8", "const:4:8"]]
- 004590a8 ["CALL", null, ["callee:00c58120:8"]]
+ 004590e8 ["INT_ADD", "register:40f0:8", ["const:4590e8:8", "const:4:8"]]
+ 004590e8 ["CALL", null, ["callee:00c58120:8"]]
- 004590a8 bytes eafb1f94
+ 004590e8 bytes 0efc1f94
- 00459144 ["INT_ADD", "register:40f0:8", ["const:459144:8", "const:4:8"]]
- 00459144 ["CALL", null, ["callee:00c58120:8"]]
+ 00459184 ["INT_ADD", "register:40f0:8", ["const:459184:8", "const:4:8"]]
+ 00459184 ["CALL", null, ["callee:00c58120:8"]]
- 00459144 bytes c3fb1f94
+ 00459184 bytes e7fb1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-410fb6f2c95f3851f3826d9c2ca7c30b"></a>

### [`00459268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459268.md) → [`004592a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004592a8.md) FUN_004592a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459268.md#insn-0045929c) · [`004592ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459268.md#insn-004592ac)
- 新版 `004592dc`（命令位置の公開資料なし） · `004592ec`（命令位置の公開資料なし）

~~~diff
- 0045929c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045929c ["INT_ADD", "register:40f0:8", ["const:45929c:8", "const:4:8"]]
- 0045929c ["CALLIND", null, ["register:0:8"]]
+ 004592dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004592dc ["INT_ADD", "register:40f0:8", ["const:4592dc:8", "const:4:8"]]
+ 004592dc ["CALLIND", null, ["register:0:8"]]
- 0045929c bytes 00013fd6
+ 004592dc bytes 00013fd6
- 004592ac ["INT_ADD", "register:40f0:8", ["const:4592ac:8", "const:4:8"]]
- 004592ac ["CALL", null, ["callee:00c57f80:8"]]
+ 004592ec ["INT_ADD", "register:40f0:8", ["const:4592ec:8", "const:4:8"]]
+ 004592ec ["CALL", null, ["callee:00c57f80:8"]]
- 004592ac bytes 01fb1f94
+ 004592ec bytes 25fb1f94
~~~


<a id="compare-86523e19dcd9ba399cf414cc13484607"></a>

### [`004592cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004592cc.md) → [`0045930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045930c.md) FUN_0045930c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004592cc.md#insn-00459350) · [`0045937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004592cc.md#insn-0045937c)
- 新版 `00459390`（命令位置の公開資料なし） · `004593bc`（命令位置の公開資料なし）

~~~diff
- 00459350 ["INT_ADD", "register:40f0:8", ["const:459350:8", "const:4:8"]]
- 00459350 ["CALL", null, ["callee:00c58120:8"]]
+ 00459390 ["INT_ADD", "register:40f0:8", ["const:459390:8", "const:4:8"]]
+ 00459390 ["CALL", null, ["callee:00c58120:8"]]
- 00459350 bytes 40fb1f94
+ 00459390 bytes 64fb1f94
- 0045937c ["INT_ADD", "register:40f0:8", ["const:45937c:8", "const:4:8"]]
- 0045937c ["CALL", null, ["callee:00c58120:8"]]
+ 004593bc ["INT_ADD", "register:40f0:8", ["const:4593bc:8", "const:4:8"]]
+ 004593bc ["CALL", null, ["callee:00c58120:8"]]
- 0045937c bytes 35fb1f94
+ 004593bc bytes 59fb1f94
~~~


<a id="compare-226c89b858c042a6915a8d6b08d8454d"></a>

### [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) → [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) FUN_004596a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c0ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed80.md) [`00c0efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efcc.md) [`00c0f218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f218.md) [`00c0f448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f448.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 10件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c0ee1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0e/00c0ee1c.md) [`00c0f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f068.md) [`00c0f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f2b4.md) [`00c0f4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f4e4.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004596d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md#insn-004596d8) · [`00459724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md#insn-00459724) · [`00459744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md#insn-00459744)
- 新版 `00459718`（命令位置の公開資料なし） · `00459764`（命令位置の公開資料なし） · `00459784`（命令位置の公開資料なし）

~~~diff
- 004596d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004596d8 ["INT_ADD", "register:40f0:8", ["const:4596d8:8", "const:4:8"]]
- 004596d8 ["CALLIND", null, ["register:0:8"]]
+ 00459718 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459718 ["INT_ADD", "register:40f0:8", ["const:459718:8", "const:4:8"]]
+ 00459718 ["CALLIND", null, ["register:0:8"]]
- 004596d8 bytes 00013fd6
+ 00459718 bytes 00013fd6
- 00459724 ["INT_ADD", "register:40f0:8", ["const:459724:8", "const:4:8"]]
- 00459724 ["CALL", null, ["callee:00c57f60:8"]]
+ 00459764 ["INT_ADD", "register:40f0:8", ["const:459764:8", "const:4:8"]]
+ 00459764 ["CALL", null, ["callee:00c57f60:8"]]
- 00459724 bytes dbf91f94
+ 00459764 bytes fff91f94
- 00459744 ["INT_ADD", "register:40f0:8", ["const:459744:8", "const:4:8"]]
- 00459744 ["CALL", null, ["callee:00c58160:8"]]
+ 00459784 ["INT_ADD", "register:40f0:8", ["const:459784:8", "const:4:8"]]
+ 00459784 ["CALL", null, ["callee:00c58160:8"]]
- 00459744 bytes 53fa1f94
+ 00459784 bytes 77fa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2ebc89644de19f787b612bfc4712df"></a>

### [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) → [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) FUN_0045986c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) [`00497038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497038.md) [`00497114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497114.md) · 呼出先 2件 [`00459994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 15件 [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) [`00497078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497078.md) [`00497154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497154.md) · 呼出先 2件 [`004599d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004599d4.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004598a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md#insn-004598a8) · [`00459904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md#insn-00459904) · [`00459940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md#insn-00459940)
- 新版 `004598e8`（命令位置の公開資料なし） · `00459944`（命令位置の公開資料なし） · `00459980`（命令位置の公開資料なし）

~~~diff
- 004598a8 ["INT_ADD", "register:40f0:8", ["const:4598a8:8", "const:4:8"]]
- 004598a8 ["CALL", null, ["callee:00c58120:8"]]
+ 004598e8 ["INT_ADD", "register:40f0:8", ["const:4598e8:8", "const:4:8"]]
+ 004598e8 ["CALL", null, ["callee:00c58120:8"]]
- 004598a8 bytes eaf91f94
+ 004598e8 bytes 0efa1f94
- 00459904 ["INT_ADD", "register:40f0:8", ["const:459904:8", "const:4:8"]]
- 00459904 ["CALL", null, ["callee:00c58120:8"]]
+ 00459944 ["INT_ADD", "register:40f0:8", ["const:459944:8", "const:4:8"]]
+ 00459944 ["CALL", null, ["callee:00c58120:8"]]
- 00459904 bytes d3f91f94
+ 00459944 bytes f7f91f94
- 00459940 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459940 ["INT_ADD", "register:40f0:8", ["const:459940:8", "const:4:8"]]
- 00459940 ["CALLIND", null, ["register:0:8"]]
+ 00459980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459980 ["INT_ADD", "register:40f0:8", ["const:459980:8", "const:4:8"]]
+ 00459980 ["CALLIND", null, ["register:0:8"]]
- 00459940 bytes 00013fd6
+ 00459980 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3922bb238c215092bb7c2153ab52d3dd"></a>

### [`00459994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md) → [`004599d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004599d4.md) FUN_004599d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004599d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md#insn-004599d4) · [`004599f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md#insn-004599f4) · [`00459a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459994.md#insn-00459a28)
- 新版 `00459a14`（命令位置の公開資料なし） · `00459a34`（命令位置の公開資料なし） · `00459a68`（命令位置の公開資料なし）

~~~diff
- 004599d4 ["INT_ADD", "register:40f0:8", ["const:4599d4:8", "const:4:8"]]
- 004599d4 ["CALL", null, ["callee:0045900c:8"]]
+ 00459a14 ["INT_ADD", "register:40f0:8", ["const:459a14:8", "const:4:8"]]
+ 00459a14 ["CALL", null, ["callee:0045900c:8"]]
- 004599d4 bytes 7efdff97
+ 00459a14 bytes 7efdff97
- 004599f4 ["INT_ADD", "register:40f0:8", ["const:4599f4:8", "const:4:8"]]
- 004599f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00459a34 ["INT_ADD", "register:40f0:8", ["const:459a34:8", "const:4:8"]]
+ 00459a34 ["CALL", null, ["callee:00c57f60:8"]]
- 004599f4 bytes 27f91f94
+ 00459a34 bytes 4bf91f94
- 00459a28 ["INT_ADD", "register:40f0:8", ["const:459a28:8", "const:4:8"]]
- 00459a28 ["CALL", null, ["callee:0043bb60:8"]]
+ 00459a68 ["INT_ADD", "register:40f0:8", ["const:459a68:8", "const:4:8"]]
+ 00459a68 ["CALL", null, ["callee:0043bb60:8"]]
- 00459a28 bytes 3e88ff97
+ 00459a68 bytes 3e88ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a66a7a03757f8bea795c537be2fb05"></a>

### [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) → [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) FUN_00459b10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) [`00458230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`0059bae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bae4.md) · 呼出先 2件 [`00459c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 10件 [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) [`00458270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`0059bb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bb24.md) · 呼出先 2件 [`00459c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459c78.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md#insn-00459b4c) · [`00459ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md#insn-00459ba8) · [`00459be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md#insn-00459be4)
- 新版 `00459b8c`（命令位置の公開資料なし） · `00459be8`（命令位置の公開資料なし） · `00459c24`（命令位置の公開資料なし）

~~~diff
- 00459b4c ["INT_ADD", "register:40f0:8", ["const:459b4c:8", "const:4:8"]]
- 00459b4c ["CALL", null, ["callee:00c58120:8"]]
+ 00459b8c ["INT_ADD", "register:40f0:8", ["const:459b8c:8", "const:4:8"]]
+ 00459b8c ["CALL", null, ["callee:00c58120:8"]]
- 00459b4c bytes 41f91f94
+ 00459b8c bytes 65f91f94
- 00459ba8 ["INT_ADD", "register:40f0:8", ["const:459ba8:8", "const:4:8"]]
- 00459ba8 ["CALL", null, ["callee:00c58120:8"]]
+ 00459be8 ["INT_ADD", "register:40f0:8", ["const:459be8:8", "const:4:8"]]
+ 00459be8 ["CALL", null, ["callee:00c58120:8"]]
- 00459ba8 bytes 2af91f94
+ 00459be8 bytes 4ef91f94
- 00459be4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459be4 ["INT_ADD", "register:40f0:8", ["const:459be4:8", "const:4:8"]]
- 00459be4 ["CALLIND", null, ["register:0:8"]]
+ 00459c24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459c24 ["INT_ADD", "register:40f0:8", ["const:459c24:8", "const:4:8"]]
+ 00459c24 ["CALLIND", null, ["register:0:8"]]
- 00459be4 bytes 00013fd6
+ 00459c24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9beac4ef4031f2b2d21cd223bdd093e"></a>

### [`00459c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md) → [`00459c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459c78.md) FUN_00459c78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md#insn-00459c78) · [`00459c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md#insn-00459c98) · [`00459ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459c38.md#insn-00459ccc)
- 新版 `00459cb8`（命令位置の公開資料なし） · `00459cd8`（命令位置の公開資料なし） · `00459d0c`（命令位置の公開資料なし）

~~~diff
- 00459c78 ["INT_ADD", "register:40f0:8", ["const:459c78:8", "const:4:8"]]
- 00459c78 ["CALL", null, ["callee:0045900c:8"]]
+ 00459cb8 ["INT_ADD", "register:40f0:8", ["const:459cb8:8", "const:4:8"]]
+ 00459cb8 ["CALL", null, ["callee:0045900c:8"]]
- 00459c78 bytes d5fcff97
+ 00459cb8 bytes d5fcff97
- 00459c98 ["INT_ADD", "register:40f0:8", ["const:459c98:8", "const:4:8"]]
- 00459c98 ["CALL", null, ["callee:00c57f60:8"]]
+ 00459cd8 ["INT_ADD", "register:40f0:8", ["const:459cd8:8", "const:4:8"]]
+ 00459cd8 ["CALL", null, ["callee:00c57f60:8"]]
- 00459c98 bytes 7ef81f94
+ 00459cd8 bytes a2f81f94
- 00459ccc ["INT_ADD", "register:40f0:8", ["const:459ccc:8", "const:4:8"]]
- 00459ccc ["CALL", null, ["callee:0043bb60:8"]]
+ 00459d0c ["INT_ADD", "register:40f0:8", ["const:459d0c:8", "const:4:8"]]
+ 00459d0c ["CALL", null, ["callee:0043bb60:8"]]
- 00459ccc bytes 9587ff97
+ 00459d0c bytes 9587ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4220a10edc23efa6e951c097a5ffaeed"></a>

### [`00459da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459da8.md) → [`00459de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459de8.md) FUN_00459de8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459da8.md#insn-00459db8)
- 新版 `00459df8`（命令位置の公開資料なし）

~~~diff
- 00459db8 ["INT_ADD", "register:40f0:8", ["const:459db8:8", "const:4:8"]]
- 00459db8 ["CALL", null, ["callee:00c583b0:8"]]
+ 00459df8 ["INT_ADD", "register:40f0:8", ["const:459df8:8", "const:4:8"]]
+ 00459df8 ["CALL", null, ["callee:00c583b0:8"]]
- 00459db8 bytes 4af91f94
+ 00459df8 bytes 6ef91f94
~~~


<a id="compare-243907602a496f3a2274a135451da43c"></a>

### [`00459fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459fa0.md) → [`00459fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459fe0.md) FUN_00459fe0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459fa0.md#insn-00459fdc)
- 新版 `0045a01c`（命令位置の公開資料なし）

~~~diff
- 00459fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00459fdc ["INT_ADD", "register:40f0:8", ["const:459fdc:8", "const:4:8"]]
- 00459fdc ["CALLIND", null, ["register:0:8"]]
+ 0045a01c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a01c ["INT_ADD", "register:40f0:8", ["const:45a01c:8", "const:4:8"]]
+ 0045a01c ["CALLIND", null, ["register:0:8"]]
- 00459fdc bytes 00013fd6
+ 0045a01c bytes 00013fd6
~~~


<a id="compare-201ebe838cf057c58f3a6b7e39ddf068"></a>

### [`0045ab44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab44.md) → [`0045ab84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab84.md) FUN_0045ab84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) · 呼出先 2件 [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) · 呼出先 2件 [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045ab58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab44.md#insn-0045ab58)
- 新版 `0045ab98`（命令位置の公開資料なし）

~~~diff
- 0045ab58 ["INT_ADD", "register:40f0:8", ["const:45ab58:8", "const:4:8"]]
- 0045ab58 ["CALL", null, ["callee:00451e0c:8"]]
+ 0045ab98 ["INT_ADD", "register:40f0:8", ["const:45ab98:8", "const:4:8"]]
+ 0045ab98 ["CALL", null, ["callee:00451e0c:8"]]
- 0045ab58 bytes 9ddcff97
+ 0045ab98 bytes 9ddcff97
~~~


<a id="compare-1a5336f8962982980551feef14a2e424"></a>

### [`0045b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md) → [`0045b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b330.md) FUN_0045b330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0045aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md) [`0045ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab20.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 2件 [`0045ab0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md) [`0045ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab60.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045b32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md#insn-0045b32c) · [`0045b358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md#insn-0045b358) · [`0045b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md#insn-0045b384)
- 新版 `0045b36c`（命令位置の公開資料なし） · `0045b398`（命令位置の公開資料なし） · `0045b3c4`（命令位置の公開資料なし）

~~~diff
- 0045b32c ["INT_ADD", "register:40f0:8", ["const:45b32c:8", "const:4:8"]]
- 0045b32c ["CALL", null, ["callee:0043bb60:8"]]
+ 0045b36c ["INT_ADD", "register:40f0:8", ["const:45b36c:8", "const:4:8"]]
+ 0045b36c ["CALL", null, ["callee:0043bb60:8"]]
- 0045b32c bytes fd81ff97
+ 0045b36c bytes fd81ff97
- 0045b358 ["INT_ADD", "register:40f0:8", ["const:45b358:8", "const:4:8"]]
- 0045b358 ["CALL", null, ["callee:0043bb60:8"]]
+ 0045b398 ["INT_ADD", "register:40f0:8", ["const:45b398:8", "const:4:8"]]
+ 0045b398 ["CALL", null, ["callee:0043bb60:8"]]
- 0045b358 bytes f281ff97
+ 0045b398 bytes f281ff97
- 0045b384 ["INT_ADD", "register:40f0:8", ["const:45b384:8", "const:4:8"]]
- 0045b384 ["CALL", null, ["callee:0043bb60:8"]]
+ 0045b3c4 ["INT_ADD", "register:40f0:8", ["const:45b3c4:8", "const:4:8"]]
+ 0045b3c4 ["CALL", null, ["callee:0043bb60:8"]]
- 0045b384 bytes e781ff97
+ 0045b3c4 bytes e781ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d12d1b8c941380dad0393ceb95b2430a"></a>

### [`0045b530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b530.md) → [`0045b570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b570.md) FUN_0045b570

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b530.md#insn-0045b56c) · [`0045b59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b530.md#insn-0045b59c) · [`0045b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b530.md#insn-0045b5b0)
- 新版 `0045b5ac`（命令位置の公開資料なし） · `0045b5dc`（命令位置の公開資料なし） · `0045b5f0`（命令位置の公開資料なし）

~~~diff
- 0045b56c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b56c ["INT_ADD", "register:40f0:8", ["const:45b56c:8", "const:4:8"]]
- 0045b56c ["CALLIND", null, ["register:0:8"]]
+ 0045b5ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b5ac ["INT_ADD", "register:40f0:8", ["const:45b5ac:8", "const:4:8"]]
+ 0045b5ac ["CALLIND", null, ["register:0:8"]]
- 0045b56c bytes 00013fd6
+ 0045b5ac bytes 00013fd6
- 0045b59c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b59c ["INT_ADD", "register:40f0:8", ["const:45b59c:8", "const:4:8"]]
- 0045b59c ["CALLIND", null, ["register:0:8"]]
+ 0045b5dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b5dc ["INT_ADD", "register:40f0:8", ["const:45b5dc:8", "const:4:8"]]
+ 0045b5dc ["CALLIND", null, ["register:0:8"]]
- 0045b59c bytes 00013fd6
+ 0045b5dc bytes 00013fd6
- 0045b5b0 ["INT_ADD", "register:40f0:8", ["const:45b5b0:8", "const:4:8"]]
- 0045b5b0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0045b5f0 ["INT_ADD", "register:40f0:8", ["const:45b5f0:8", "const:4:8"]]
+ 0045b5f0 ["CALL", null, ["callee:00c53da0:8"]]
- 0045b5b0 bytes d4e11f94
+ 0045b5f0 bytes ece11f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c8aca28ea112deb7f797b3b9273e98e"></a>

### [`0045b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b610.md) → [`0045b650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b650.md) FUN_0045b650

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045b62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b610.md#insn-0045b62c) · [`0045b64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b610.md#insn-0045b64c)
- 新版 `0045b66c`（命令位置の公開資料なし） · `0045b68c`（命令位置の公開資料なし）

~~~diff
- 0045b62c ["INT_ADD", "register:40f0:8", ["const:45b62c:8", "const:4:8"]]
- 0045b62c ["CALL", null, ["callee:00c53da0:8"]]
+ 0045b66c ["INT_ADD", "register:40f0:8", ["const:45b66c:8", "const:4:8"]]
+ 0045b66c ["CALL", null, ["callee:00c53da0:8"]]
- 0045b62c bytes b5e11f94
+ 0045b66c bytes cde11f94
- 0045b64c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b64c ["INT_ADD", "register:40f0:8", ["const:45b64c:8", "const:4:8"]]
- 0045b64c ["CALLIND", null, ["register:0:8"]]
+ 0045b68c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b68c ["INT_ADD", "register:40f0:8", ["const:45b68c:8", "const:4:8"]]
+ 0045b68c ["CALLIND", null, ["register:0:8"]]
- 0045b64c bytes 00013fd6
+ 0045b68c bytes 00013fd6
~~~


<a id="compare-4bec6c39e9e31c4400d4b45e690df552"></a>

### [`0045b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8ac.md) → [`0045b8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8ec.md) FUN_0045b8ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) · 呼出先 2件 [`0045bcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bcac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) · 呼出先 2件 [`0045bcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bcec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045b8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8ac.md#insn-0045b8c0)
- 新版 `0045b900`（命令位置の公開資料なし）

~~~diff
- 0045b8c0 ["INT_ADD", "register:40f0:8", ["const:45b8c0:8", "const:4:8"]]
- 0045b8c0 ["CALL", null, ["callee:0045bcec:8"]]
+ 0045b900 ["INT_ADD", "register:40f0:8", ["const:45b900:8", "const:4:8"]]
+ 0045b900 ["CALL", null, ["callee:0045bcec:8"]]
- 0045b8c0 bytes fb000094
+ 0045b900 bytes fb000094
~~~


<a id="compare-ec04f1e06cdecda4e6909d085bd62464"></a>

### [`0045bafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md) → [`0045bb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bb3c.md) FUN_0045bb3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0045b834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md) [`0045b888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b888.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 2件 [`0045b874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md) [`0045b8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8c8.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045bb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md#insn-0045bb38) · [`0045bb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md#insn-0045bb64) · [`0045bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md#insn-0045bb80)
- 新版 `0045bb78`（命令位置の公開資料なし） · `0045bba4`（命令位置の公開資料なし） · `0045bbc0`（命令位置の公開資料なし）

~~~diff
- 0045bb38 ["INT_ADD", "register:40f0:8", ["const:45bb38:8", "const:4:8"]]
- 0045bb38 ["CALL", null, ["callee:0043bb60:8"]]
+ 0045bb78 ["INT_ADD", "register:40f0:8", ["const:45bb78:8", "const:4:8"]]
+ 0045bb78 ["CALL", null, ["callee:0043bb60:8"]]
- 0045bb38 bytes fa7fff97
+ 0045bb78 bytes fa7fff97
- 0045bb64 ["INT_ADD", "register:40f0:8", ["const:45bb64:8", "const:4:8"]]
- 0045bb64 ["CALL", null, ["callee:0043bb60:8"]]
+ 0045bba4 ["INT_ADD", "register:40f0:8", ["const:45bba4:8", "const:4:8"]]
+ 0045bba4 ["CALL", null, ["callee:0043bb60:8"]]
- 0045bb64 bytes ef7fff97
+ 0045bba4 bytes ef7fff97
- 0045bb80 ["INT_ADD", "register:40f0:8", ["const:45bb80:8", "const:4:8"]]
- 0045bb80 ["CALL", null, ["callee:00c53d70:8"]]
+ 0045bbc0 ["INT_ADD", "register:40f0:8", ["const:45bbc0:8", "const:4:8"]]
+ 0045bbc0 ["CALL", null, ["callee:00c53d70:8"]]
- 0045bb80 bytes 54e01f94
+ 0045bbc0 bytes 6ce01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4fd22db606385d1c9c0cf021d4a784d"></a>

### [`0045bcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bcac.md) → [`0045bcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bcec.md) FUN_0045bcec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0045b8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8a4.md) [`0045b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8ac.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0045b8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8e4.md) [`0045b8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8ec.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045bce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bcac.md#insn-0045bce8) · [`0045bd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bcac.md#insn-0045bd18) · [`0045bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bcac.md#insn-0045bd2c)
- 新版 `0045bd28`（命令位置の公開資料なし） · `0045bd58`（命令位置の公開資料なし） · `0045bd6c`（命令位置の公開資料なし）

~~~diff
- 0045bce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bce8 ["INT_ADD", "register:40f0:8", ["const:45bce8:8", "const:4:8"]]
- 0045bce8 ["CALLIND", null, ["register:0:8"]]
+ 0045bd28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bd28 ["INT_ADD", "register:40f0:8", ["const:45bd28:8", "const:4:8"]]
+ 0045bd28 ["CALLIND", null, ["register:0:8"]]
- 0045bce8 bytes 00013fd6
+ 0045bd28 bytes 00013fd6
- 0045bd18 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bd18 ["INT_ADD", "register:40f0:8", ["const:45bd18:8", "const:4:8"]]
- 0045bd18 ["CALLIND", null, ["register:0:8"]]
+ 0045bd58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bd58 ["INT_ADD", "register:40f0:8", ["const:45bd58:8", "const:4:8"]]
+ 0045bd58 ["CALLIND", null, ["register:0:8"]]
- 0045bd18 bytes 00013fd6
+ 0045bd58 bytes 00013fd6
- 0045bd2c ["INT_ADD", "register:40f0:8", ["const:45bd2c:8", "const:4:8"]]
- 0045bd2c ["CALL", null, ["callee:00c53da0:8"]]
+ 0045bd6c ["INT_ADD", "register:40f0:8", ["const:45bd6c:8", "const:4:8"]]
+ 0045bd6c ["CALL", null, ["callee:00c53da0:8"]]
- 0045bd2c bytes f5df1f94
+ 0045bd6c bytes 0de01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16617a09dc2bd7e348d930e3fbe598bf"></a>

### [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md) → [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md) FUN_0045be6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0045bddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bddc.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md) · 呼出先 2件 [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0045be1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be1c.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md) · 呼出先 2件 [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045be48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md#insn-0045be48) · [`0045be54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md#insn-0045be54) · [`0045be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md#insn-0045be6c)
- 新版 `0045be88`（命令位置の公開資料なし） · `0045be94`（命令位置の公開資料なし） · `0045beac`（命令位置の公開資料なし）

~~~diff
- 0045be48 ["INT_ADD", "register:40f0:8", ["const:45be48:8", "const:4:8"]]
- 0045be48 ["CALL", null, ["local:b0:8"]]
+ 0045be88 ["INT_ADD", "register:40f0:8", ["const:45be88:8", "const:4:8"]]
+ 0045be88 ["CALL", null, ["local:b0:8"]]
- 0045be48 bytes f9ffff97
+ 0045be88 bytes f9ffff97
- 0045be54 ["INT_ADD", "register:40f0:8", ["const:45be54:8", "const:4:8"]]
- 0045be54 ["CALL", null, ["local:b0:8"]]
+ 0045be94 ["INT_ADD", "register:40f0:8", ["const:45be94:8", "const:4:8"]]
+ 0045be94 ["CALL", null, ["local:b0:8"]]
- 0045be54 bytes f6ffff97
+ 0045be94 bytes f6ffff97
- 0045be6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045be6c ["INT_ADD", "register:40f0:8", ["const:45be6c:8", "const:4:8"]]
- 0045be6c ["CALLIND", null, ["register:0:8"]]
+ 0045beac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045beac ["INT_ADD", "register:40f0:8", ["const:45beac:8", "const:4:8"]]
+ 0045beac ["CALLIND", null, ["register:0:8"]]
- 0045be6c bytes 00013fd6
+ 0045beac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ea8904519cec496130412b47303083"></a>

### [`0045c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c068.md) → [`0045c0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0a8.md) FUN_0045c0a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c068.md#insn-0045c0a4)
- 新版 `0045c0e4`（命令位置の公開資料なし）

~~~diff
- 0045c0a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c0a4 ["INT_ADD", "register:40f0:8", ["const:45c0a4:8", "const:4:8"]]
- 0045c0a4 ["CALLIND", null, ["register:0:8"]]
+ 0045c0e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c0e4 ["INT_ADD", "register:40f0:8", ["const:45c0e4:8", "const:4:8"]]
+ 0045c0e4 ["CALLIND", null, ["register:0:8"]]
- 0045c0a4 bytes 00013fd6
+ 0045c0e4 bytes 00013fd6
~~~


<a id="compare-19a44cf029e8fa3de0d78242cf18b860"></a>

### [`0045c8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c8b8.md) → [`0045c8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c8f8.md) FUN_0045c8f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c8b8.md#insn-0045c8f4)
- 新版 `0045c934`（命令位置の公開資料なし）

~~~diff
- 0045c8f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c8f4 ["INT_ADD", "register:40f0:8", ["const:45c8f4:8", "const:4:8"]]
- 0045c8f4 ["CALLIND", null, ["register:0:8"]]
+ 0045c934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c934 ["INT_ADD", "register:40f0:8", ["const:45c934:8", "const:4:8"]]
+ 0045c934 ["CALLIND", null, ["register:0:8"]]
- 0045c8f4 bytes 00013fd6
+ 0045c934 bytes 00013fd6
~~~


<a id="compare-af763253fb35b9a73a16c2330bd8e6e9"></a>

### [`0045c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md) → [`0045c948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c948.md) FUN_0045c948

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md#insn-0045c940) · [`0045c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md#insn-0045c954) · [`0045c958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md#insn-0045c958)
- 新版 `0045c980`（命令位置の公開資料なし） · `0045c994`（命令位置の公開資料なし） · `0045c998`（命令位置の公開資料なし）

~~~diff
- 0045c940 ["INT_ADD", "register:40f0:8", ["const:45c940:8", "const:4:8"]]
- 0045c940 ["CALL", null, ["callee:00851550:8"]]
+ 0045c980 ["INT_ADD", "register:40f0:8", ["const:45c980:8", "const:4:8"]]
+ 0045c980 ["CALL", null, ["callee:00851550:8"]]
- 0045c940 bytes eed20f94
+ 0045c980 bytes f4d20f94
- 0045c954 ["INT_ADD", "register:40f0:8", ["const:45c954:8", "const:4:8"]]
- 0045c954 ["CALL", null, ["callee:00851550:8"]]
+ 0045c994 ["INT_ADD", "register:40f0:8", ["const:45c994:8", "const:4:8"]]
+ 0045c994 ["CALL", null, ["callee:00851550:8"]]
- 0045c954 bytes e9d20f94
+ 0045c994 bytes efd20f94
- 0045c958 ["INT_ADD", "register:40f0:8", ["const:45c958:8", "const:4:8"]]
- 0045c958 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 0045c998 ["INT_ADD", "register:40f0:8", ["const:45c998:8", "const:4:8"]]
+ 0045c998 ["CALL", null, ["callee:00a1a6f8:8"]]
- 0045c958 bytes 53f71694
+ 0045c998 bytes 58f71694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-805ce19526a90d5a465afca65a2ab20c"></a>

### [`0045ca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md) → [`0045cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cad8.md) FUN_0045cad8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0045cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0045cdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045cb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md#insn-0045cb3c) · [`0045cb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md#insn-0045cb74) · [`0045cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md#insn-0045cba0)
- 新版 `0045cb7c`（命令位置の公開資料なし） · `0045cbb4`（命令位置の公開資料なし） · `0045cbe0`（命令位置の公開資料なし）

~~~diff
- 0045cb3c ["INT_ADD", "register:40f0:8", ["const:45cb3c:8", "const:4:8"]]
- 0045cb3c ["CALL", null, ["callee:00c57f60:8"]]
+ 0045cb7c ["INT_ADD", "register:40f0:8", ["const:45cb7c:8", "const:4:8"]]
+ 0045cb7c ["CALL", null, ["callee:00c57f60:8"]]
- 0045cb3c bytes d5ec1f94
+ 0045cb7c bytes f9ec1f94
- 0045cb74 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045cb74 ["INT_ADD", "register:40f0:8", ["const:45cb74:8", "const:4:8"]]
- 0045cb74 ["CALLIND", null, ["register:0:8"]]
+ 0045cbb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cbb4 ["INT_ADD", "register:40f0:8", ["const:45cbb4:8", "const:4:8"]]
+ 0045cbb4 ["CALLIND", null, ["register:0:8"]]
- 0045cb74 bytes 00013fd6
+ 0045cbb4 bytes 00013fd6
- 0045cba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045cba0 ["INT_ADD", "register:40f0:8", ["const:45cba0:8", "const:4:8"]]
- 0045cba0 ["CALLIND", null, ["register:0:8"]]
+ 0045cbe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cbe0 ["INT_ADD", "register:40f0:8", ["const:45cbe0:8", "const:4:8"]]
+ 0045cbe0 ["CALLIND", null, ["register:0:8"]]
- 0045cba0 bytes 00013fd6
+ 0045cbe0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a49b6e5f17ba8b952a860ed876f4e1b"></a>

### [`0045cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cf74.md) → [`0045cfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cfb4.md) FUN_0045cfb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045cfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cf74.md#insn-0045cfb0)
- 新版 `0045cff0`（命令位置の公開資料なし）

~~~diff
- 0045cfb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045cfb0 ["INT_ADD", "register:40f0:8", ["const:45cfb0:8", "const:4:8"]]
- 0045cfb0 ["CALLIND", null, ["register:0:8"]]
+ 0045cff0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cff0 ["INT_ADD", "register:40f0:8", ["const:45cff0:8", "const:4:8"]]
+ 0045cff0 ["CALLIND", null, ["register:0:8"]]
- 0045cfb0 bytes 00013fd6
+ 0045cff0 bytes 00013fd6
~~~


<a id="compare-16835ceb6d65eacfa342f54de7fd04d1"></a>

### [`0045d964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d964.md) → [`0045d9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9a4.md) FUN_0045d9a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d964.md#insn-0045d9a0)
- 新版 `0045d9e0`（命令位置の公開資料なし）

~~~diff
- 0045d9a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d9a0 ["INT_ADD", "register:40f0:8", ["const:45d9a0:8", "const:4:8"]]
- 0045d9a0 ["CALLIND", null, ["register:0:8"]]
+ 0045d9e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d9e0 ["INT_ADD", "register:40f0:8", ["const:45d9e0:8", "const:4:8"]]
+ 0045d9e0 ["CALLIND", null, ["register:0:8"]]
- 0045d9a0 bytes 00013fd6
+ 0045d9e0 bytes 00013fd6
~~~


<a id="compare-3ef44c2dddb4919ca1e9adb272c3dded"></a>

### [`0045db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md) → [`0045dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dbb8.md) FUN_0045dbb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0045de6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0045deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045dc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md#insn-0045dc1c) · [`0045dc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md#insn-0045dc54) · [`0045dc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md#insn-0045dc80)
- 新版 `0045dc5c`（命令位置の公開資料なし） · `0045dc94`（命令位置の公開資料なし） · `0045dcc0`（命令位置の公開資料なし）

~~~diff
- 0045dc1c ["INT_ADD", "register:40f0:8", ["const:45dc1c:8", "const:4:8"]]
- 0045dc1c ["CALL", null, ["callee:00c57f60:8"]]
+ 0045dc5c ["INT_ADD", "register:40f0:8", ["const:45dc5c:8", "const:4:8"]]
+ 0045dc5c ["CALL", null, ["callee:00c57f60:8"]]
- 0045dc1c bytes 9de81f94
+ 0045dc5c bytes c1e81f94
- 0045dc54 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045dc54 ["INT_ADD", "register:40f0:8", ["const:45dc54:8", "const:4:8"]]
- 0045dc54 ["CALLIND", null, ["register:0:8"]]
+ 0045dc94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045dc94 ["INT_ADD", "register:40f0:8", ["const:45dc94:8", "const:4:8"]]
+ 0045dc94 ["CALLIND", null, ["register:0:8"]]
- 0045dc54 bytes 00013fd6
+ 0045dc94 bytes 00013fd6
- 0045dc80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045dc80 ["INT_ADD", "register:40f0:8", ["const:45dc80:8", "const:4:8"]]
- 0045dc80 ["CALLIND", null, ["register:0:8"]]
+ 0045dcc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045dcc0 ["INT_ADD", "register:40f0:8", ["const:45dcc0:8", "const:4:8"]]
+ 0045dcc0 ["CALLIND", null, ["register:0:8"]]
- 0045dc80 bytes 00013fd6
+ 0045dcc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-504dec6f19d4925f5329ee0503c229b7"></a>

### [`0045f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md) → [`0045f07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f07c.md) FUN_0045f07c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045fadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`0045fb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fb1c.md) · 呼出先 6件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045f068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md#insn-0045f068) · [`0045f080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md#insn-0045f080) · [`0045f0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md#insn-0045f0c8)
- 新版 `0045f0a8`（命令位置の公開資料なし） · `0045f0c0`（命令位置の公開資料なし） · `0045f108`（命令位置の公開資料なし）

~~~diff
- 0045f068 ["INT_ADD", "register:40f0:8", ["const:45f068:8", "const:4:8"]]
- 0045f068 ["CALL", null, ["callee:00c581b0:8"]]
+ 0045f0a8 ["INT_ADD", "register:40f0:8", ["const:45f0a8:8", "const:4:8"]]
+ 0045f0a8 ["CALL", null, ["callee:00c581b0:8"]]
- 0045f068 bytes 1ee41f94
+ 0045f0a8 bytes 42e41f94
- 0045f080 ["INT_ADD", "register:40f0:8", ["const:45f080:8", "const:4:8"]]
- 0045f080 ["CALL", null, ["callee:00c583c0:8"]]
+ 0045f0c0 ["INT_ADD", "register:40f0:8", ["const:45f0c0:8", "const:4:8"]]
+ 0045f0c0 ["CALL", null, ["callee:00c583c0:8"]]
- 0045f080 bytes 9ce41f94
+ 0045f0c0 bytes c0e41f94
- 0045f0c8 ["INT_ADD", "register:40f0:8", ["const:45f0c8:8", "const:4:8"]]
- 0045f0c8 ["CALL", null, ["callee:00c58450:8"]]
+ 0045f108 ["INT_ADD", "register:40f0:8", ["const:45f108:8", "const:4:8"]]
+ 0045f108 ["CALL", null, ["callee:00c58450:8"]]
- 0045f0c8 bytes aee41f94
+ 0045f108 bytes d2e41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d995cb74e433da377b461e8a96132f8"></a>

### [`0045f318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f318.md) → [`0045f358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f358.md) FUN_0045f358

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045f354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f318.md#insn-0045f354)
- 新版 `0045f394`（命令位置の公開資料なし）

~~~diff
- 0045f354 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f354 ["INT_ADD", "register:40f0:8", ["const:45f354:8", "const:4:8"]]
- 0045f354 ["CALLIND", null, ["register:0:8"]]
+ 0045f394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f394 ["INT_ADD", "register:40f0:8", ["const:45f394:8", "const:4:8"]]
+ 0045f394 ["CALLIND", null, ["register:0:8"]]
- 0045f354 bytes 00013fd6
+ 0045f394 bytes 00013fd6
~~~


<a id="compare-8cab65f9ea21e8e13b5f6bf94dc19178"></a>

### [`0045f800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f800.md) → [`0045f840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f840.md) FUN_0045f840

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045f83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f800.md#insn-0045f83c)
- 新版 `0045f87c`（命令位置の公開資料なし）

~~~diff
- 0045f83c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f83c ["INT_ADD", "register:40f0:8", ["const:45f83c:8", "const:4:8"]]
- 0045f83c ["CALLIND", null, ["register:0:8"]]
+ 0045f87c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f87c ["INT_ADD", "register:40f0:8", ["const:45f87c:8", "const:4:8"]]
+ 0045f87c ["CALLIND", null, ["register:0:8"]]
- 0045f83c bytes 00013fd6
+ 0045f87c bytes 00013fd6
~~~


<a id="compare-a4657c78c58d464cb6d12e7528b6175f"></a>

### [`0045f850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f850.md) → [`0045f890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f890.md) FUN_0045f890

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045f89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f850.md#insn-0045f89c) · [`0045f8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f850.md#insn-0045f8d0) · [`0045f8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f850.md#insn-0045f8d4)
- 新版 `0045f8dc`（命令位置の公開資料なし） · `0045f910`（命令位置の公開資料なし） · `0045f914`（命令位置の公開資料なし）

~~~diff
- 0045f89c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f89c ["INT_ADD", "register:40f0:8", ["const:45f89c:8", "const:4:8"]]
- 0045f89c ["CALLIND", null, ["register:0:8"]]
+ 0045f8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f8dc ["INT_ADD", "register:40f0:8", ["const:45f8dc:8", "const:4:8"]]
+ 0045f8dc ["CALLIND", null, ["register:0:8"]]
- 0045f89c bytes 00013fd6
+ 0045f8dc bytes 00013fd6
- 0045f8d0 ["INT_ADD", "register:40f0:8", ["const:45f8d0:8", "const:4:8"]]
- 0045f8d0 ["CALL", null, ["callee:00459db4:8"]]
+ 0045f910 ["INT_ADD", "register:40f0:8", ["const:45f910:8", "const:4:8"]]
+ 0045f910 ["CALL", null, ["callee:00459db4:8"]]
- 0045f8d0 bytes 29e9ff97
+ 0045f910 bytes 29e9ff97
- 0045f8d4 ["INT_ADD", "register:40f0:8", ["const:45f8d4:8", "const:4:8"]]
- 0045f8d4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0045f914 ["INT_ADD", "register:40f0:8", ["const:45f914:8", "const:4:8"]]
+ 0045f914 ["CALL", null, ["callee:00c57fb0:8"]]
- 0045f8d4 bytes 83e11f94
+ 0045f914 bytes a7e11f94
~~~


<a id="compare-87d9e189776e8bdf7da8157bf8ba9f1e"></a>

### [`0045fa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa3c.md) → [`0045fa7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa7c.md) FUN_0045fa7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa3c.md#insn-0045fa58) · [`0045fa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa3c.md#insn-0045fa78)
- 新版 `0045fa98`（命令位置の公開資料なし） · `0045fab8`（命令位置の公開資料なし）

~~~diff
- 0045fa58 ["INT_ADD", "register:40f0:8", ["const:45fa58:8", "const:4:8"]]
- 0045fa58 ["CALL", null, ["callee:00c53da0:8"]]
+ 0045fa98 ["INT_ADD", "register:40f0:8", ["const:45fa98:8", "const:4:8"]]
+ 0045fa98 ["CALL", null, ["callee:00c53da0:8"]]
- 0045fa58 bytes aad01f94
+ 0045fa98 bytes c2d01f94
- 0045fa78 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fa78 ["INT_ADD", "register:40f0:8", ["const:45fa78:8", "const:4:8"]]
- 0045fa78 ["CALLIND", null, ["register:0:8"]]
+ 0045fab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fab8 ["INT_ADD", "register:40f0:8", ["const:45fab8:8", "const:4:8"]]
+ 0045fab8 ["CALLIND", null, ["register:0:8"]]
- 0045fa78 bytes 00013fd6
+ 0045fab8 bytes 00013fd6
~~~


<a id="compare-7d49612a13227aac2269796092b46a24"></a>

### [`0045fa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md) → [`0045facc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045facc.md) FUN_0045facc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045faac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md#insn-0045faac) · [`0045fac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md#insn-0045fac0) · [`0045fac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md#insn-0045fac8)
- 新版 `0045faec`（命令位置の公開資料なし） · `0045fb00`（命令位置の公開資料なし） · `0045fb08`（命令位置の公開資料なし）

~~~diff
- 0045faac ["INT_ADD", "register:40f0:8", ["const:45faac:8", "const:4:8"]]
- 0045faac ["CALL", null, ["callee:00c53da0:8"]]
+ 0045faec ["INT_ADD", "register:40f0:8", ["const:45faec:8", "const:4:8"]]
+ 0045faec ["CALL", null, ["callee:00c53da0:8"]]
- 0045faac bytes 95d01f94
+ 0045faec bytes add01f94
- 0045fac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fac0 ["INT_ADD", "register:40f0:8", ["const:45fac0:8", "const:4:8"]]
- 0045fac0 ["CALLIND", null, ["register:0:8"]]
+ 0045fb00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fb00 ["INT_ADD", "register:40f0:8", ["const:45fb00:8", "const:4:8"]]
+ 0045fb00 ["CALLIND", null, ["register:0:8"]]
- 0045fac0 bytes 00013fd6
+ 0045fb00 bytes 00013fd6
- 0045fac8 ["INT_ADD", "register:40f0:8", ["const:45fac8:8", "const:4:8"]]
- 0045fac8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0045fb08 ["INT_ADD", "register:40f0:8", ["const:45fb08:8", "const:4:8"]]
+ 0045fb08 ["CALL", null, ["callee:00c57f50:8"]]
- 0045fac8 bytes eee01f94
+ 0045fb08 bytes 12e11f94
~~~


<a id="compare-6f7e48fe9b9aa6fbc240c7c5660bad3c"></a>

### [`0045fadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md) → [`0045fb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fb1c.md) FUN_0045fb1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`0045f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`0045f07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f07c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045fb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md#insn-0045fb34) · [`0045fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md#insn-0045fb6c) · [`0045fb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md#insn-0045fb70)
- 新版 `0045fb74`（命令位置の公開資料なし） · `0045fbac`（命令位置の公開資料なし） · `0045fbb0`（命令位置の公開資料なし）

~~~diff
- 0045fb34 ["INT_ADD", "register:40f0:8", ["const:45fb34:8", "const:4:8"]]
- 0045fb34 ["CALL", null, ["callee:0045f07c:8"]]
+ 0045fb74 ["INT_ADD", "register:40f0:8", ["const:45fb74:8", "const:4:8"]]
+ 0045fb74 ["CALL", null, ["callee:0045f07c:8"]]
- 0045fb34 bytes 42fdff97
+ 0045fb74 bytes 42fdff97
- 0045fb6c ["INT_ADD", "register:40f0:8", ["const:45fb6c:8", "const:4:8"]]
- 0045fb6c ["CALL", null, ["callee:0045a714:8"]]
+ 0045fbac ["INT_ADD", "register:40f0:8", ["const:45fbac:8", "const:4:8"]]
+ 0045fbac ["CALL", null, ["callee:0045a714:8"]]
- 0045fb6c bytes daeaff97
+ 0045fbac bytes daeaff97
- 0045fb70 ["INT_ADD", "register:40f0:8", ["const:45fb70:8", "const:4:8"]]
- 0045fb70 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0045fbb0 ["INT_ADD", "register:40f0:8", ["const:45fbb0:8", "const:4:8"]]
+ 0045fbb0 ["CALL", null, ["callee:00c57fb0:8"]]
- 0045fb70 bytes dce01f94
+ 0045fbb0 bytes 00e11f94
~~~


<a id="compare-6e9b9e25a5ad71932d9087369e7b5114"></a>

### [`0045fd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fd70.md) → [`0045fdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fdb0.md) FUN_0045fdb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fd70.md#insn-0045fdac)
- 新版 `0045fdec`（命令位置の公開資料なし）

~~~diff
- 0045fdac ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fdac ["INT_ADD", "register:40f0:8", ["const:45fdac:8", "const:4:8"]]
- 0045fdac ["CALLIND", null, ["register:0:8"]]
+ 0045fdec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fdec ["INT_ADD", "register:40f0:8", ["const:45fdec:8", "const:4:8"]]
+ 0045fdec ["CALLIND", null, ["register:0:8"]]
- 0045fdac bytes 00013fd6
+ 0045fdec bytes 00013fd6
~~~


<a id="compare-b41dce80d3f379e0fbb5ed4ce0739f7e"></a>

### [`0045fdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fdc0.md) → [`0045fe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe00.md) FUN_0045fe00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045fddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fdc0.md#insn-0045fddc)
- 新版 `0045fe1c`（命令位置の公開資料なし）

~~~diff
- 0045fddc ["INT_ADD", "register:40f0:8", ["const:45fddc:8", "const:4:8"]]
- 0045fddc ["CALL", null, ["callee:00459db4:8"]]
+ 0045fe1c ["INT_ADD", "register:40f0:8", ["const:45fe1c:8", "const:4:8"]]
+ 0045fe1c ["CALL", null, ["callee:00459db4:8"]]
- 0045fddc bytes e6e7ff97
+ 0045fe1c bytes e6e7ff97
~~~


<a id="compare-e6b86ac2b81c893794bca77516002335"></a>

### [`0045ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ffdc.md) → [`0046001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046001c.md) FUN_0046001c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00460018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ffdc.md#insn-00460018)
- 新版 `00460058`（命令位置の公開資料なし）

~~~diff
- 00460018 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460018 ["INT_ADD", "register:40f0:8", ["const:460018:8", "const:4:8"]]
- 00460018 ["CALLIND", null, ["register:0:8"]]
+ 00460058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460058 ["INT_ADD", "register:40f0:8", ["const:460058:8", "const:4:8"]]
+ 00460058 ["CALLIND", null, ["register:0:8"]]
- 00460018 bytes 00013fd6
+ 00460058 bytes 00013fd6
~~~


<a id="compare-121abcd1f3c97fb7324bb5e511968930"></a>

### [`0046002c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046002c.md) → [`0046006c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046006c.md) FUN_0046006c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00460064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046002c.md#insn-00460064) · [`00460098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046002c.md#insn-00460098) · [`0046009c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046002c.md#insn-0046009c)
- 新版 `004600a4`（命令位置の公開資料なし） · `004600d8`（命令位置の公開資料なし） · `004600dc`（命令位置の公開資料なし）

~~~diff
- 00460064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460064 ["INT_ADD", "register:40f0:8", ["const:460064:8", "const:4:8"]]
- 00460064 ["CALLIND", null, ["register:0:8"]]
+ 004600a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004600a4 ["INT_ADD", "register:40f0:8", ["const:4600a4:8", "const:4:8"]]
+ 004600a4 ["CALLIND", null, ["register:0:8"]]
- 00460064 bytes 00013fd6
+ 004600a4 bytes 00013fd6
- 00460098 ["INT_ADD", "register:40f0:8", ["const:460098:8", "const:4:8"]]
- 00460098 ["CALL", null, ["callee:00459db4:8"]]
+ 004600d8 ["INT_ADD", "register:40f0:8", ["const:4600d8:8", "const:4:8"]]
+ 004600d8 ["CALL", null, ["callee:00459db4:8"]]
- 00460098 bytes 37e7ff97
+ 004600d8 bytes 37e7ff97
- 0046009c ["INT_ADD", "register:40f0:8", ["const:46009c:8", "const:4:8"]]
- 0046009c ["CALL", null, ["callee:00c57fb0:8"]]
+ 004600dc ["INT_ADD", "register:40f0:8", ["const:4600dc:8", "const:4:8"]]
+ 004600dc ["CALL", null, ["callee:00c57fb0:8"]]
- 0046009c bytes 91df1f94
+ 004600dc bytes b5df1f94
~~~


<a id="compare-95132b715471262ce9dbc8aad83222e4"></a>

### [`00460740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460740.md) → [`00460780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460780.md) FUN_00460780

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00454884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046077c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460740.md#insn-0046077c)
- 新版 `004607bc`（命令位置の公開資料なし）

~~~diff
- 0046077c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046077c ["INT_ADD", "register:40f0:8", ["const:46077c:8", "const:4:8"]]
- 0046077c ["CALLIND", null, ["register:0:8"]]
+ 004607bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004607bc ["INT_ADD", "register:40f0:8", ["const:4607bc:8", "const:4:8"]]
+ 004607bc ["CALLIND", null, ["register:0:8"]]
- 0046077c bytes 00013fd6
+ 004607bc bytes 00013fd6
~~~


<a id="compare-10c0eb8743521282b7563bed4e1395cd"></a>

### [`00461318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461318.md) → [`00461358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461358.md) FUN_00461358

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461318.md#insn-00461358)
- 新版 `00461398`（命令位置の公開資料なし）

~~~diff
- 00461358 ["INT_ADD", "register:40f0:8", ["const:461358:8", "const:4:8"]]
- 00461358 ["CALL", null, ["callee:00461ac0:8"]]
+ 00461398 ["INT_ADD", "register:40f0:8", ["const:461398:8", "const:4:8"]]
+ 00461398 ["CALL", null, ["callee:00461ac0:8"]]
- 00461358 bytes ca010094
+ 00461398 bytes ca010094
~~~


