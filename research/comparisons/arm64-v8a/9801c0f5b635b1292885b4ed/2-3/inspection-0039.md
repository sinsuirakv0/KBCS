# v16.0.1 → v16.0.2 · 要調査の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-693fe11f724ff71ca970067e25e138c4"></a>

### [`00bb1234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1234.md) → [`00bb12d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb12d0.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5cc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc00.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ccd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccd0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1234.md#insn-00bb1264) · [`00bb1280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1234.md#insn-00bb1280) · [`00bb12bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1234.md#insn-00bb12bc)
- 新版 `00bb1300`（命令位置の公開資料なし） · `00bb131c`（命令位置の公開資料なし） · `00bb1358`（命令位置の公開資料なし）

~~~diff
- 00bb1264 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1264 ["INT_ADD", "register:40f0:8", ["const:bb1264:8", "const:4:8"]]
- 00bb1264 ["CALLIND", null, ["register:0:8"]]
+ 00bb1300 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1300 ["INT_ADD", "register:40f0:8", ["const:bb1300:8", "const:4:8"]]
+ 00bb1300 ["CALLIND", null, ["register:0:8"]]
- 00bb1264 bytes 20013fd6
+ 00bb1300 bytes 20013fd6
- 00bb1280 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1280 ["INT_ADD", "register:40f0:8", ["const:bb1280:8", "const:4:8"]]
- 00bb1280 ["CALLIND", null, ["register:0:8"]]
+ 00bb131c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb131c ["INT_ADD", "register:40f0:8", ["const:bb131c:8", "const:4:8"]]
+ 00bb131c ["CALLIND", null, ["register:0:8"]]
- 00bb1280 bytes 20013fd6
+ 00bb131c bytes 20013fd6
- 00bb12bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb12bc ["INT_ADD", "register:40f0:8", ["const:bb12bc:8", "const:4:8"]]
- 00bb12bc ["CALLIND", null, ["register:0:8"]]
+ 00bb1358 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb1358 ["INT_ADD", "register:40f0:8", ["const:bb1358:8", "const:4:8"]]
+ 00bb1358 ["CALLIND", null, ["register:0:8"]]
- 00bb12bc bytes 00013fd6
+ 00bb1358 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1e2f308ac3d0e3459ab6a4a085fe02c"></a>

### [`00bb1640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md) → [`00bb16dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md) FUN_00bb16dc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8e0dc.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca40.md)
- 新版 呼出元 1件 [`00b8e178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md#insn-00bb1684) · [`00bb169c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md#insn-00bb169c) · [`00bb16f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md#insn-00bb16f8)
- 新版 `00bb1720`（命令位置の公開資料なし） · `00bb1738`（命令位置の公開資料なし） · `00bb1794`（命令位置の公開資料なし）

~~~diff
- 00bb1684 ["INT_ADD", "register:40f0:8", ["const:bb1684:8", "const:4:8"]]
- 00bb1684 ["CALL", null, ["callee:00c5cb10:8"]]
+ 00bb1720 ["INT_ADD", "register:40f0:8", ["const:bb1720:8", "const:4:8"]]
+ 00bb1720 ["CALL", null, ["callee:00c5cb10:8"]]
- 00bb1684 bytes efac0294
+ 00bb1720 bytes fcac0294
- 00bb169c ["INT_ADD", "register:40f0:8", ["const:bb169c:8", "const:4:8"]]
- 00bb169c ["CALL", null, ["callee:00c5cb10:8"]]
+ 00bb1738 ["INT_ADD", "register:40f0:8", ["const:bb1738:8", "const:4:8"]]
+ 00bb1738 ["CALL", null, ["callee:00c5cb10:8"]]
- 00bb169c bytes e9ac0294
+ 00bb1738 bytes f6ac0294
- 00bb16f8 ["INT_ADD", "register:40f0:8", ["const:bb16f8:8", "const:4:8"]]
- 00bb16f8 ["CALL", null, ["callee:00c58120:8"]]
+ 00bb1794 ["INT_ADD", "register:40f0:8", ["const:bb1794:8", "const:4:8"]]
+ 00bb1794 ["CALL", null, ["callee:00c58120:8"]]
- 00bb16f8 bytes 569a0294
+ 00bb1794 bytes 639a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d5dab1a9dd1b91cb2e0d9acbe718432"></a>

### [`00bb24f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb24f4.md) → [`00bb2590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2590.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf70.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf70.md)
- 新版 呼出元 1件 [`00c5d040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d040.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb24f4.md#insn-00bb2510) · [`00bb251c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb24f4.md#insn-00bb251c) · [`00bb252c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb24f4.md#insn-00bb252c)
- 新版 `00bb25ac`（命令位置の公開資料なし） · `00bb25b8`（命令位置の公開資料なし） · `00bb25c8`（命令位置の公開資料なし）

~~~diff
- 00bb2510 ["INT_ADD", "register:40f0:8", ["const:bb2510:8", "const:4:8"]]
- 00bb2510 ["CALL", null, ["callee:00c5d040:8"]]
+ 00bb25ac ["INT_ADD", "register:40f0:8", ["const:bb25ac:8", "const:4:8"]]
+ 00bb25ac ["CALL", null, ["callee:00c5d040:8"]]
- 00bb2510 bytes 98aa0294
+ 00bb25ac bytes a5aa0294
- 00bb251c ["INT_ADD", "register:40f0:8", ["const:bb251c:8", "const:4:8"]]
- 00bb251c ["CALL", null, ["callee:00c5d040:8"]]
+ 00bb25b8 ["INT_ADD", "register:40f0:8", ["const:bb25b8:8", "const:4:8"]]
+ 00bb25b8 ["CALL", null, ["callee:00c5d040:8"]]
- 00bb251c bytes 95aa0294
+ 00bb25b8 bytes a2aa0294
- 00bb252c ["INT_ADD", "register:40f0:8", ["const:bb252c:8", "const:4:8"]]
- 00bb252c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb25c8 ["INT_ADD", "register:40f0:8", ["const:bb25c8:8", "const:4:8"]]
+ 00bb25c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb252c bytes 61960294
+ 00bb25c8 bytes 6e960294
~~~


<a id="compare-6289ab4b09b1468647d8849c547b2162"></a>

### [`00bb2658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2658.md) → [`00bb26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb26f4.md) _ZNSt6__ndk16__treeIPN11flatbuffers8FieldDefENS_4lessIS3_EENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfd0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfd0.md)
- 新版 呼出元 1件 [`00c5d0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0a0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2658.md#insn-00bb2674) · [`00bb2680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2658.md#insn-00bb2680)
- 新版 `00bb2710`（命令位置の公開資料なし） · `00bb271c`（命令位置の公開資料なし）

~~~diff
- 00bb2674 ["INT_ADD", "register:40f0:8", ["const:bb2674:8", "const:4:8"]]
- 00bb2674 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00bb2710 ["INT_ADD", "register:40f0:8", ["const:bb2710:8", "const:4:8"]]
+ 00bb2710 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00bb2674 bytes 57aa0294
+ 00bb2710 bytes 64aa0294
- 00bb2680 ["INT_ADD", "register:40f0:8", ["const:bb2680:8", "const:4:8"]]
- 00bb2680 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00bb271c ["INT_ADD", "register:40f0:8", ["const:bb271c:8", "const:4:8"]]
+ 00bb271c ["CALL", null, ["callee:00c5d0a0:8"]]
- 00bb2680 bytes 54aa0294
+ 00bb271c bytes 61aa0294
~~~


<a id="compare-5883266769318ab2580cb96282bd79ff"></a>

### [`00bb31b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb31b4.md) → [`00bb3250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3250.md) _ZN11flatbuffers18ConCatPathFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c740.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5c810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c810.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb31d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb31b4.md#insn-00bb31d4) · [`00bb3268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb31b4.md#insn-00bb3268) · [`00bb32b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb31b4.md#insn-00bb32b8)
- 新版 `00bb3270`（命令位置の公開資料なし） · `00bb3304`（命令位置の公開資料なし） · `00bb3354`（命令位置の公開資料なし）

~~~diff
- 00bb31d4 ["INT_ADD", "register:40f0:8", ["const:bb31d4:8", "const:4:8"]]
- 00bb31d4 ["CALL", null, ["callee:00c5b680:8"]]
+ 00bb3270 ["INT_ADD", "register:40f0:8", ["const:bb3270:8", "const:4:8"]]
+ 00bb3270 ["CALL", null, ["callee:00c5b680:8"]]
- 00bb31d4 bytes f7a00294
+ 00bb3270 bytes 04a10294
- 00bb3268 ["INT_ADD", "register:40f0:8", ["const:bb3268:8", "const:4:8"]]
- 00bb3268 ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00bb3304 ["INT_ADD", "register:40f0:8", ["const:bb3304:8", "const:4:8"]]
+ 00bb3304 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00bb3268 bytes 9e9d0294
+ 00bb3304 bytes ab9d0294
- 00bb32b8 ["INT_ADD", "register:40f0:8", ["const:bb32b8:8", "const:4:8"]]
- 00bb32b8 ["CALL", null, ["callee:00c58050:8"]]
+ 00bb3354 ["INT_ADD", "register:40f0:8", ["const:bb3354:8", "const:4:8"]]
+ 00bb3354 ["CALL", null, ["callee:00c58050:8"]]
- 00bb32b8 bytes 32930294
+ 00bb3354 bytes 3f930294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d22e2471e25f367385247cf2f444fc36"></a>

### [`00bb371c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md) → [`00bb37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb37b8.md) _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c720.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7f0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb3758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md#insn-00bb3758) · [`00bb3770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md#insn-00bb3770) · [`00bb3780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md#insn-00bb3780)
- 新版 `00bb37f4`（命令位置の公開資料なし） · `00bb380c`（命令位置の公開資料なし） · `00bb381c`（命令位置の公開資料なし）

~~~diff
- 00bb3758 ["INT_ADD", "register:40f0:8", ["const:bb3758:8", "const:4:8"]]
- 00bb3758 ["CALL", null, ["callee:00c5d300:8"]]
+ 00bb37f4 ["INT_ADD", "register:40f0:8", ["const:bb37f4:8", "const:4:8"]]
+ 00bb37f4 ["CALL", null, ["callee:00c5d300:8"]]
- 00bb3758 bytes b6a60294
+ 00bb37f4 bytes c3a60294
- 00bb3770 ["INT_ADD", "register:40f0:8", ["const:bb3770:8", "const:4:8"]]
- 00bb3770 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bb380c ["INT_ADD", "register:40f0:8", ["const:bb380c:8", "const:4:8"]]
+ 00bb380c ["CALL", null, ["callee:00c580b0:8"]]
- 00bb3770 bytes 1c920294
+ 00bb380c bytes 29920294
- 00bb3780 ["INT_ADD", "register:40f0:8", ["const:bb3780:8", "const:4:8"]]
- 00bb3780 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb381c ["INT_ADD", "register:40f0:8", ["const:bb381c:8", "const:4:8"]]
+ 00bb381c ["CALL", null, ["callee:00c5b180:8"]]
- 00bb3780 bytes 4c9e0294
+ 00bb381c bytes 599e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92770a0be7a78420bbafb6128c17e544"></a>

### [`00bb58ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb58ac.md) → [`00bb5948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5948.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb58bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb58ac.md#insn-00bb58bc)
- 新版 `00bb5958`（命令位置の公開資料なし）

~~~diff
- 00bb58bc ["INT_ADD", "register:40f0:8", ["const:bb58bc:8", "const:4:8"]]
- 00bb58bc ["CALL", null, ["callee:00c5d280:8"]]
+ 00bb5958 ["INT_ADD", "register:40f0:8", ["const:bb5958:8", "const:4:8"]]
+ 00bb5958 ["CALL", null, ["callee:00c5d280:8"]]
- 00bb58bc bytes 3d9e0294
+ 00bb5958 bytes 4a9e0294
~~~


<a id="compare-c379013ff7c29e6eb302c96de228eecf"></a>

### [`00bb60b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md) → [`00bb6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE8overflowEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb61a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md#insn-00bb61a8) · [`00bb61f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md#insn-00bb61f8) · [`00bb6238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md#insn-00bb6238)
- 新版 `00bb6244`（命令位置の公開資料なし） · `00bb6294`（命令位置の公開資料なし） · `00bb62d4`（命令位置の公開資料なし）

~~~diff
- 00bb61a8 ["INT_ADD", "register:40f0:8", ["const:bb61a8:8", "const:4:8"]]
- 00bb61a8 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00bb6244 ["INT_ADD", "register:40f0:8", ["const:bb6244:8", "const:4:8"]]
+ 00bb6244 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00bb61a8 bytes 1e900294
+ 00bb6244 bytes 2b900294
- 00bb61f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb61f8 ["INT_ADD", "register:40f0:8", ["const:bb61f8:8", "const:4:8"]]
- 00bb61f8 ["CALLIND", null, ["register:0:8"]]
+ 00bb6294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb6294 ["INT_ADD", "register:40f0:8", ["const:bb6294:8", "const:4:8"]]
+ 00bb6294 ["CALLIND", null, ["register:0:8"]]
- 00bb61f8 bytes 00013fd6
+ 00bb6294 bytes 00013fd6
- 00bb6238 ["INT_ADD", "register:40f0:8", ["const:bb6238:8", "const:4:8"]]
- 00bb6238 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00bb62d4 ["INT_ADD", "register:40f0:8", ["const:bb62d4:8", "const:4:8"]]
+ 00bb62d4 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00bb6238 bytes fa8f0294
+ 00bb62d4 bytes 07900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d73bd806cc1664e08b756f0cfc2031fd"></a>

### [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) → [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) FUN_00bb6388

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md) [`00bb5be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md) [`00bb5dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md) [`00bb60b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 4件 [`00bb5b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md) [`00bb5c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md) [`00bb5e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md) [`00bb6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6150.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb62f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md#insn-00bb62f4)
- 新版 `00bb6390`（命令位置の公開資料なし）

~~~diff
- 00bb62f4 ["INT_ADD", "register:40f0:8", ["const:bb62f4:8", "const:4:8"]]
- 00bb62f4 ["CALL", null, ["callee:00c5b210:8"]]
+ 00bb6390 ["INT_ADD", "register:40f0:8", ["const:bb6390:8", "const:4:8"]]
+ 00bb6390 ["CALL", null, ["callee:00c5b210:8"]]
- 00bb62f4 bytes 93930294
+ 00bb6390 bytes a0930294
~~~


<a id="compare-88f27322987e60c1588028489ab3f77c"></a>

### [`00bb6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6300.md) → [`00bb639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb639c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6300.md#insn-00bb6314)
- 新版 `00bb63b0`（命令位置の公開資料なし）

~~~diff
- 00bb6314 ["INT_ADD", "register:40f0:8", ["const:bb6314:8", "const:4:8"]]
- 00bb6314 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb63b0 ["INT_ADD", "register:40f0:8", ["const:bb63b0:8", "const:4:8"]]
+ 00bb63b0 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb6314 bytes 739b0294
+ 00bb63b0 bytes 809b0294
~~~


<a id="compare-834db8c04161e5eee294d3fab79368fe"></a>

### [`00bb633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb633c.md) → [`00bb63d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb63d8.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb633c.md#insn-00bb6358)
- 新版 `00bb63f4`（命令位置の公開資料なし）

~~~diff
- 00bb6358 ["INT_ADD", "register:40f0:8", ["const:bb6358:8", "const:4:8"]]
- 00bb6358 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb63f4 ["INT_ADD", "register:40f0:8", ["const:bb63f4:8", "const:4:8"]]
+ 00bb63f4 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb6358 bytes 629b0294
+ 00bb63f4 bytes 6f9b0294
~~~


<a id="compare-3841cf96fa8b5c83d72be71412007909"></a>

### [`00bb66a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66a4.md) → [`00bb6740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6740.md) FUN_00bb6740

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aad0.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)
- 新版 呼出元 1件 [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) · 呼出先 2件 [`00c5aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aba0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb66b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66a4.md#insn-00bb66b4)
- 新版 `00bb6750`（命令位置の公開資料なし）

~~~diff
- 00bb66b4 ["INT_ADD", "register:40f0:8", ["const:bb66b4:8", "const:4:8"]]
- 00bb66b4 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bb6750 ["INT_ADD", "register:40f0:8", ["const:bb6750:8", "const:4:8"]]
+ 00bb6750 ["CALL", null, ["callee:00c5ad30:8"]]
- 00bb66b4 bytes 6b910294
+ 00bb6750 bytes 78910294
~~~


<a id="compare-a08d57c442b6a77b0ee2a91754e0e4bd"></a>

### [`00bb6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6dfc.md) → [`00bb6e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md) _ZN8firebase9messaging20PollableListenerImplD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d460.md)
- 新版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6dfc.md#insn-00bb6e18) · [`00bb6e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6dfc.md#insn-00bb6e2c) · [`00bb6e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6dfc.md#insn-00bb6e60)
- 新版 `00bb6eb4`（命令位置の公開資料なし） · `00bb6ec8`（命令位置の公開資料なし） · `00bb6efc`（命令位置の公開資料なし）

~~~diff
- 00bb6e18 ["INT_ADD", "register:40f0:8", ["const:bb6e18:8", "const:4:8"]]
- 00bb6e18 ["CALL", null, ["callee:00c5d530:8"]]
+ 00bb6eb4 ["INT_ADD", "register:40f0:8", ["const:bb6eb4:8", "const:4:8"]]
+ 00bb6eb4 ["CALL", null, ["callee:00c5d530:8"]]
- 00bb6e18 bytes 92990294
+ 00bb6eb4 bytes 9f990294
- 00bb6e2c ["INT_ADD", "register:40f0:8", ["const:bb6e2c:8", "const:4:8"]]
- 00bb6e2c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb6ec8 ["INT_ADD", "register:40f0:8", ["const:bb6ec8:8", "const:4:8"]]
+ 00bb6ec8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb6e2c bytes 21840294
+ 00bb6ec8 bytes 2e840294
- 00bb6e60 ["INT_ADD", "register:40f0:8", ["const:bb6e60:8", "const:4:8"]]
- 00bb6e60 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb6efc ["INT_ADD", "register:40f0:8", ["const:bb6efc:8", "const:4:8"]]
+ 00bb6efc ["CALL", null, ["callee:00c57f80:8"]]
- 00bb6e60 bytes 14840294
+ 00bb6efc bytes 21840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c69a3eba6126b810b1944b2247089ce"></a>

### [`00bb6f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md) → [`00bb6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6fb0.md) _ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d370.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3e0.md) [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md)
- 新版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d440.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4b0.md) [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md#insn-00bb6f3c) · [`00bb6f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md#insn-00bb6f44) · [`00bb6f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md#insn-00bb6f70)
- 新版 `00bb6fd8`（命令位置の公開資料なし） · `00bb6fe0`（命令位置の公開資料なし） · `00bb700c`（命令位置の公開資料なし）

~~~diff
- 00bb6f3c ["INT_ADD", "register:40f0:8", ["const:bb6f3c:8", "const:4:8"]]
- 00bb6f3c ["CALL", null, ["callee:00c5d4b0:8"]]
+ 00bb6fd8 ["INT_ADD", "register:40f0:8", ["const:bb6fd8:8", "const:4:8"]]
+ 00bb6fd8 ["CALL", null, ["callee:00c5d4b0:8"]]
- 00bb6f3c bytes 29990294
+ 00bb6fd8 bytes 36990294
- 00bb6f44 ["INT_ADD", "register:40f0:8", ["const:bb6f44:8", "const:4:8"]]
- 00bb6f44 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6fe0 ["INT_ADD", "register:40f0:8", ["const:bb6fe0:8", "const:4:8"]]
+ 00bb6fe0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb6f44 bytes af8e0294
+ 00bb6fe0 bytes bc8e0294
- 00bb6f70 ["INT_ADD", "register:40f0:8", ["const:bb6f70:8", "const:4:8"]]
- 00bb6f70 ["CALL", null, ["callee:00c5d580:8"]]
+ 00bb700c ["INT_ADD", "register:40f0:8", ["const:bb700c:8", "const:4:8"]]
+ 00bb700c ["CALL", null, ["callee:00c5d580:8"]]
- 00bb6f70 bytes 50990294
+ 00bb700c bytes 5d990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dbd1ca28110be2e47be3507cb618186"></a>

### [`00bb7028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7028.md) → [`00bb70c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb70c4.md) _ZN8firebase9messaging20PollableListenerImpl15OnTokenReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d310.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3e0.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7028.md#insn-00bb7040) · [`00bb704c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7028.md#insn-00bb704c) · [`00bb705c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7028.md#insn-00bb705c)
- 新版 `00bb70dc`（命令位置の公開資料なし） · `00bb70e8`（命令位置の公開資料なし） · `00bb70f8`（命令位置の公開資料なし）

~~~diff
- 00bb7040 ["INT_ADD", "register:40f0:8", ["const:bb7040:8", "const:4:8"]]
- 00bb7040 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb70dc ["INT_ADD", "register:40f0:8", ["const:bb70dc:8", "const:4:8"]]
+ 00bb70dc ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb7040 bytes 708e0294
+ 00bb70dc bytes 7d8e0294
- 00bb704c ["INT_ADD", "register:40f0:8", ["const:bb704c:8", "const:4:8"]]
- 00bb704c ["CALL", null, ["callee:00c580b0:8"]]
+ 00bb70e8 ["INT_ADD", "register:40f0:8", ["const:bb70e8:8", "const:4:8"]]
+ 00bb70e8 ["CALL", null, ["callee:00c580b0:8"]]
- 00bb704c bytes e5830294
+ 00bb70e8 bytes f2830294
- 00bb705c ["INT_ADD", "register:40f0:8", ["const:bb705c:8", "const:4:8"]]
- 00bb705c ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb70f8 ["INT_ADD", "register:40f0:8", ["const:bb70f8:8", "const:4:8"]]
+ 00bb70f8 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb705c bytes 15900294
+ 00bb70f8 bytes 22900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-676b7dbbae449905969e06184522934e"></a>

### [`00bb709c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb709c.md) → [`00bb7138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7138.md) _ZN8firebase9messaging20PollableListenerImpl22OnRegistrationReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d350.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d420.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb70b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb709c.md#insn-00bb70b4) · [`00bb70c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb709c.md#insn-00bb70c0) · [`00bb70d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb709c.md#insn-00bb70d0)
- 新版 `00bb7150`（命令位置の公開資料なし） · `00bb715c`（命令位置の公開資料なし） · `00bb716c`（命令位置の公開資料なし）

~~~diff
- 00bb70b4 ["INT_ADD", "register:40f0:8", ["const:bb70b4:8", "const:4:8"]]
- 00bb70b4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb7150 ["INT_ADD", "register:40f0:8", ["const:bb7150:8", "const:4:8"]]
+ 00bb7150 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb70b4 bytes 538e0294
+ 00bb7150 bytes 608e0294
- 00bb70c0 ["INT_ADD", "register:40f0:8", ["const:bb70c0:8", "const:4:8"]]
- 00bb70c0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bb715c ["INT_ADD", "register:40f0:8", ["const:bb715c:8", "const:4:8"]]
+ 00bb715c ["CALL", null, ["callee:00c580b0:8"]]
- 00bb70c0 bytes c8830294
+ 00bb715c bytes d5830294
- 00bb70d0 ["INT_ADD", "register:40f0:8", ["const:bb70d0:8", "const:4:8"]]
- 00bb70d0 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb716c ["INT_ADD", "register:40f0:8", ["const:bb716c:8", "const:4:8"]]
+ 00bb716c ["CALL", null, ["callee:00c5b180:8"]]
- 00bb70d0 bytes f88f0294
+ 00bb716c bytes 05900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057bfd59ff6db8ffa6c077c2b2ac1336"></a>

### [`00bb7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7110.md) → [`00bb71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb71ac.md) _ZN8firebase9messaging20PollableListenerImpl24OnUnregistrationReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d360.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d430.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7110.md#insn-00bb7128) · [`00bb7134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7110.md#insn-00bb7134) · [`00bb7144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7110.md#insn-00bb7144)
- 新版 `00bb71c4`（命令位置の公開資料なし） · `00bb71d0`（命令位置の公開資料なし） · `00bb71e0`（命令位置の公開資料なし）

~~~diff
- 00bb7128 ["INT_ADD", "register:40f0:8", ["const:bb7128:8", "const:4:8"]]
- 00bb7128 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb71c4 ["INT_ADD", "register:40f0:8", ["const:bb71c4:8", "const:4:8"]]
+ 00bb71c4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb7128 bytes 368e0294
+ 00bb71c4 bytes 438e0294
- 00bb7134 ["INT_ADD", "register:40f0:8", ["const:bb7134:8", "const:4:8"]]
- 00bb7134 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bb71d0 ["INT_ADD", "register:40f0:8", ["const:bb71d0:8", "const:4:8"]]
+ 00bb71d0 ["CALL", null, ["callee:00c580b0:8"]]
- 00bb7134 bytes ab830294
+ 00bb71d0 bytes b8830294
- 00bb7144 ["INT_ADD", "register:40f0:8", ["const:bb7144:8", "const:4:8"]]
- 00bb7144 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb71e0 ["INT_ADD", "register:40f0:8", ["const:bb71e0:8", "const:4:8"]]
+ 00bb71e0 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7144 bytes db8f0294
+ 00bb71e0 bytes e88f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b39d56d256afc954c83984655ba967"></a>

### [`00bb7274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7274.md) → [`00bb7310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7310.md) _ZN8firebase9messaging16PollableListener21PollRegistrationTokenEPb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7274.md#insn-00bb7298)
- 新版 `00bb7334`（命令位置の公開資料なし）

~~~diff
- 00bb7298 ["INT_ADD", "register:40f0:8", ["const:bb7298:8", "const:4:8"]]
- 00bb7298 ["CALL", null, ["callee:00c5d410:8"]]
+ 00bb7334 ["INT_ADD", "register:40f0:8", ["const:bb7334:8", "const:4:8"]]
+ 00bb7334 ["CALL", null, ["callee:00c5d410:8"]]
- 00bb7298 bytes 2a980294
+ 00bb7334 bytes 37980294
~~~


<a id="compare-20a141715f55e69060ac451584565bf1"></a>

### [`00bb72cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb72cc.md) → [`00bb7368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7368.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d340.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d410.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb72e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb72cc.md#insn-00bb72e4) · [`00bb731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb72cc.md#insn-00bb731c) · [`00bb7354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb72cc.md#insn-00bb7354)
- 新版 `00bb7380`（命令位置の公開資料なし） · `00bb73b8`（命令位置の公開資料なし） · `00bb73f0`（命令位置の公開資料なし）

~~~diff
- 00bb72e4 ["INT_ADD", "register:40f0:8", ["const:bb72e4:8", "const:4:8"]]
- 00bb72e4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb7380 ["INT_ADD", "register:40f0:8", ["const:bb7380:8", "const:4:8"]]
+ 00bb7380 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb72e4 bytes c78d0294
+ 00bb7380 bytes d48d0294
- 00bb731c ["INT_ADD", "register:40f0:8", ["const:bb731c:8", "const:4:8"]]
- 00bb731c ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb73b8 ["INT_ADD", "register:40f0:8", ["const:bb73b8:8", "const:4:8"]]
+ 00bb73b8 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb731c bytes 658f0294
+ 00bb73b8 bytes 728f0294
- 00bb7354 ["INT_ADD", "register:40f0:8", ["const:bb7354:8", "const:4:8"]]
- 00bb7354 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bb73f0 ["INT_ADD", "register:40f0:8", ["const:bb73f0:8", "const:4:8"]]
+ 00bb73f0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bb7354 bytes af8d0294
+ 00bb73f0 bytes bc8d0294
~~~


<a id="compare-1096e1be319ad2c5526aed44d753ed92"></a>

### [`00bb7388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7388.md) → [`00bb7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7424.md) _ZN8firebase9messaging16PollableListener16PollRegistrationEPb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb73ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7388.md#insn-00bb73ac)
- 新版 `00bb7448`（命令位置の公開資料なし）

~~~diff
- 00bb73ac ["INT_ADD", "register:40f0:8", ["const:bb73ac:8", "const:4:8"]]
- 00bb73ac ["CALL", null, ["callee:00c5d3f0:8"]]
+ 00bb7448 ["INT_ADD", "register:40f0:8", ["const:bb7448:8", "const:4:8"]]
+ 00bb7448 ["CALL", null, ["callee:00c5d3f0:8"]]
- 00bb73ac bytes dd970294
+ 00bb7448 bytes ea970294
~~~


<a id="compare-c9cedafb1ef61e5bb3e35313bd9e516a"></a>

### [`00bb73e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb73e0.md) → [`00bb747c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb747c.md) _ZN8firebase9messaging20PollableListenerImpl16PollRegistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d320.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3f0.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb73f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb73e0.md#insn-00bb73f8) · [`00bb7430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb73e0.md#insn-00bb7430) · [`00bb7468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb73e0.md#insn-00bb7468)
- 新版 `00bb7494`（命令位置の公開資料なし） · `00bb74cc`（命令位置の公開資料なし） · `00bb7504`（命令位置の公開資料なし）

~~~diff
- 00bb73f8 ["INT_ADD", "register:40f0:8", ["const:bb73f8:8", "const:4:8"]]
- 00bb73f8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb7494 ["INT_ADD", "register:40f0:8", ["const:bb7494:8", "const:4:8"]]
+ 00bb7494 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb73f8 bytes 828d0294
+ 00bb7494 bytes 8f8d0294
- 00bb7430 ["INT_ADD", "register:40f0:8", ["const:bb7430:8", "const:4:8"]]
- 00bb7430 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb74cc ["INT_ADD", "register:40f0:8", ["const:bb74cc:8", "const:4:8"]]
+ 00bb74cc ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7430 bytes 208f0294
+ 00bb74cc bytes 2d8f0294
- 00bb7468 ["INT_ADD", "register:40f0:8", ["const:bb7468:8", "const:4:8"]]
- 00bb7468 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bb7504 ["INT_ADD", "register:40f0:8", ["const:bb7504:8", "const:4:8"]]
+ 00bb7504 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bb7468 bytes 6a8d0294
+ 00bb7504 bytes 778d0294
~~~


<a id="compare-83f2d453e317e7b284edb383224bba78"></a>

### [`00bb749c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb749c.md) → [`00bb7538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7538.md) _ZN8firebase9messaging16PollableListener18PollUnregistrationEPb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d330.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb749c.md#insn-00bb74c0)
- 新版 `00bb755c`（命令位置の公開資料なし）

~~~diff
- 00bb74c0 ["INT_ADD", "register:40f0:8", ["const:bb74c0:8", "const:4:8"]]
- 00bb74c0 ["CALL", null, ["callee:00c5d400:8"]]
+ 00bb755c ["INT_ADD", "register:40f0:8", ["const:bb755c:8", "const:4:8"]]
+ 00bb755c ["CALL", null, ["callee:00c5d400:8"]]
- 00bb74c0 bytes 9c970294
+ 00bb755c bytes a9970294
~~~


<a id="compare-ce8e5fd14a1ab5a9e3d4767c9940d449"></a>

### [`00bb74f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb74f4.md) → [`00bb7590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7590.md) _ZN8firebase9messaging20PollableListenerImpl18PollUnregistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d330.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d400.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb74f4.md#insn-00bb750c) · [`00bb7544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb74f4.md#insn-00bb7544) · [`00bb757c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb74f4.md#insn-00bb757c)
- 新版 `00bb75a8`（命令位置の公開資料なし） · `00bb75e0`（命令位置の公開資料なし） · `00bb7618`（命令位置の公開資料なし）

~~~diff
- 00bb750c ["INT_ADD", "register:40f0:8", ["const:bb750c:8", "const:4:8"]]
- 00bb750c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb75a8 ["INT_ADD", "register:40f0:8", ["const:bb75a8:8", "const:4:8"]]
+ 00bb75a8 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb750c bytes 3d8d0294
+ 00bb75a8 bytes 4a8d0294
- 00bb7544 ["INT_ADD", "register:40f0:8", ["const:bb7544:8", "const:4:8"]]
- 00bb7544 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb75e0 ["INT_ADD", "register:40f0:8", ["const:bb75e0:8", "const:4:8"]]
+ 00bb75e0 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7544 bytes db8e0294
+ 00bb75e0 bytes e88e0294
- 00bb757c ["INT_ADD", "register:40f0:8", ["const:bb757c:8", "const:4:8"]]
- 00bb757c ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bb7618 ["INT_ADD", "register:40f0:8", ["const:bb7618:8", "const:4:8"]]
+ 00bb7618 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bb757c bytes 258d0294
+ 00bb7618 bytes 328d0294
~~~


<a id="compare-bfa4e15bc1e9ab9455f05cc727fd94f0"></a>

### [`00bb7678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7678.md) → [`00bb7714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7714.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d460.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md)
- 新版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d530.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb76f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7678.md#insn-00bb76f8) · [`00bb773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7678.md#insn-00bb773c)
- 新版 `00bb7794`（命令位置の公開資料なし） · `00bb77d8`（命令位置の公開資料なし）

~~~diff
- 00bb76f8 ["INT_ADD", "register:40f0:8", ["const:bb76f8:8", "const:4:8"]]
- 00bb76f8 ["CALL", null, ["callee:00c5d4c0:8"]]
+ 00bb7794 ["INT_ADD", "register:40f0:8", ["const:bb7794:8", "const:4:8"]]
+ 00bb7794 ["CALL", null, ["callee:00c5d4c0:8"]]
- 00bb76f8 bytes 3e970294
+ 00bb7794 bytes 4b970294
- 00bb773c ["INT_ADD", "register:40f0:8", ["const:bb773c:8", "const:4:8"]]
- 00bb773c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb77d8 ["INT_ADD", "register:40f0:8", ["const:bb77d8:8", "const:4:8"]]
+ 00bb77d8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb773c bytes dd810294
+ 00bb77d8 bytes ea810294
~~~


<a id="compare-f6127520356cf4312a94545174b13dbf"></a>

### [`00bb7790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7790.md) → [`00bb782c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb782c.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md) · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2d0.md)
- 新版 呼出元 1件 [`00c5d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4c0.md) · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb77ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7790.md#insn-00bb77ac) · [`00bb77b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7790.md#insn-00bb77b4) · [`00bb77fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7790.md#insn-00bb77fc)
- 新版 `00bb7848`（命令位置の公開資料なし） · `00bb7850`（命令位置の公開資料なし） · `00bb7898`（命令位置の公開資料なし）

~~~diff
- 00bb77ac ["INT_ADD", "register:40f0:8", ["const:bb77ac:8", "const:4:8"]]
- 00bb77ac ["CALL", null, ["callee:00c5d3a0:8"]]
+ 00bb7848 ["INT_ADD", "register:40f0:8", ["const:bb7848:8", "const:4:8"]]
+ 00bb7848 ["CALL", null, ["callee:00c5d3a0:8"]]
- 00bb77ac bytes c9960294
+ 00bb7848 bytes d6960294
- 00bb77b4 ["INT_ADD", "register:40f0:8", ["const:bb77b4:8", "const:4:8"]]
- 00bb77b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb7850 ["INT_ADD", "register:40f0:8", ["const:bb7850:8", "const:4:8"]]
+ 00bb7850 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb77b4 bytes bf810294
+ 00bb7850 bytes cc810294
- 00bb77fc ["INT_ADD", "register:40f0:8", ["const:bb77fc:8", "const:4:8"]]
- 00bb77fc ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb7898 ["INT_ADD", "register:40f0:8", ["const:bb7898:8", "const:4:8"]]
+ 00bb7898 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb77fc bytes ad810294
+ 00bb7898 bytes ba810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8e0bbfdcd9d58fa46443c310663402b"></a>

### [`00bb78d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb78d4.md) → [`00bb7970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7970.md) _ZN8firebase9messaging12NotificationD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3a0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb78fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb78d4.md#insn-00bb78fc) · [`00bb7904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb78d4.md#insn-00bb7904) · [`00bb7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb78d4.md#insn-00bb7940)
- 新版 `00bb7998`（命令位置の公開資料なし） · `00bb79a0`（命令位置の公開資料なし） · `00bb79dc`（命令位置の公開資料なし）

~~~diff
- 00bb78fc ["INT_ADD", "register:40f0:8", ["const:bb78fc:8", "const:4:8"]]
- 00bb78fc ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb7998 ["INT_ADD", "register:40f0:8", ["const:bb7998:8", "const:4:8"]]
+ 00bb7998 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb78fc bytes 6d810294
+ 00bb7998 bytes 7a810294
- 00bb7904 ["INT_ADD", "register:40f0:8", ["const:bb7904:8", "const:4:8"]]
- 00bb7904 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb79a0 ["INT_ADD", "register:40f0:8", ["const:bb79a0:8", "const:4:8"]]
+ 00bb79a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb7904 bytes 6b810294
+ 00bb79a0 bytes 78810294
- 00bb7940 ["INT_ADD", "register:40f0:8", ["const:bb7940:8", "const:4:8"]]
- 00bb7940 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb79dc ["INT_ADD", "register:40f0:8", ["const:bb79dc:8", "const:4:8"]]
+ 00bb79dc ["CALL", null, ["callee:00c57f80:8"]]
- 00bb7940 bytes 5c810294
+ 00bb79dc bytes 69810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb16f31a23deb7ab9139d43415d1912"></a>

### [`00bb7aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7aac.md) → [`00bb7b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7b48.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3e0.md) · 呼出先 1件 [`00c5d400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d400.md)
- 新版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4b0.md) · 呼出先 1件 [`00c5d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7aac.md#insn-00bb7b1c)
- 新版 `00bb7bb8`（命令位置の公開資料なし）

~~~diff
- 00bb7b1c ["INT_ADD", "register:40f0:8", ["const:bb7b1c:8", "const:4:8"]]
- 00bb7b1c ["CALL", null, ["callee:00c5d4d0:8"]]
+ 00bb7bb8 ["INT_ADD", "register:40f0:8", ["const:bb7bb8:8", "const:4:8"]]
+ 00bb7bb8 ["CALL", null, ["callee:00c5d4d0:8"]]
- 00bb7b1c bytes 39960294
+ 00bb7bb8 bytes 46960294
~~~


<a id="compare-7c4256d9a2e5d367b1dd128541624d30"></a>

### [`00bb7c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md) → [`00bb7cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7cec.md) _ZN8firebase9messaging7MessageaSERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d400.md) · 呼出先 7件 [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2c0.md)
- 新版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4d0.md) · 呼出先 7件 [`0053b7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b7bc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md#insn-00bb7c8c) · [`00bb7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md#insn-00bb7cb0) · [`00bb7cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md#insn-00bb7cd4)
- 新版 `00bb7d28`（命令位置の公開資料なし） · `00bb7d4c`（命令位置の公開資料なし） · `00bb7d70`（命令位置の公開資料なし）

~~~diff
- 00bb7c8c ["INT_ADD", "register:40f0:8", ["const:bb7c8c:8", "const:4:8"]]
- 00bb7c8c ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb7d28 ["INT_ADD", "register:40f0:8", ["const:bb7d28:8", "const:4:8"]]
+ 00bb7d28 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7c8c bytes 098d0294
+ 00bb7d28 bytes 168d0294
- 00bb7cb0 ["INT_ADD", "register:40f0:8", ["const:bb7cb0:8", "const:4:8"]]
- 00bb7cb0 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb7d4c ["INT_ADD", "register:40f0:8", ["const:bb7d4c:8", "const:4:8"]]
+ 00bb7d4c ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7cb0 bytes 008d0294
+ 00bb7d4c bytes 0d8d0294
- 00bb7cd4 ["INT_ADD", "register:40f0:8", ["const:bb7cd4:8", "const:4:8"]]
- 00bb7cd4 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bb7d70 ["INT_ADD", "register:40f0:8", ["const:bb7d70:8", "const:4:8"]]
+ 00bb7d70 ["CALL", null, ["callee:00c5b180:8"]]
- 00bb7cd4 bytes f78c0294
+ 00bb7d70 bytes 048d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d577a627494e0e493c8eb1684265c0c0"></a>

### [`00bb7e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7e80.md) → [`00bb7f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7f1c.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2c0.md) · 呼出先 1件 [`00c5d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2e0.md)
- 新版 呼出元 1件 [`00c5d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d390.md) · 呼出先 1件 [`00c5d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7e80.md#insn-00bb7ec0)
- 新版 `00bb7f5c`（命令位置の公開資料なし）

~~~diff
- 00bb7ec0 ["INT_ADD", "register:40f0:8", ["const:bb7ec0:8", "const:4:8"]]
- 00bb7ec0 ["CALL", null, ["callee:00c5d3b0:8"]]
+ 00bb7f5c ["INT_ADD", "register:40f0:8", ["const:bb7f5c:8", "const:4:8"]]
+ 00bb7f5c ["CALL", null, ["callee:00c5d3b0:8"]]
- 00bb7ec0 bytes 08950294
+ 00bb7f5c bytes 15950294
~~~


<a id="compare-f93f4e4371e5a2f0e04b74f3f6f27e45"></a>

### [`00bb8070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8070.md) → [`00bb810c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb810c.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4c0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d590.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb80b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8070.md#insn-00bb80b4) · [`00bb8110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8070.md#insn-00bb8110) · [`00bb8138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8070.md#insn-00bb8138)
- 新版 `00bb8150`（命令位置の公開資料なし） · `00bb81ac`（命令位置の公開資料なし） · `00bb81d4`（命令位置の公開資料なし）

~~~diff
- 00bb80b4 ["INT_ADD", "register:40f0:8", ["const:bb80b4:8", "const:4:8"]]
- 00bb80b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb8150 ["INT_ADD", "register:40f0:8", ["const:bb8150:8", "const:4:8"]]
+ 00bb8150 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb80b4 bytes 7f7f0294
+ 00bb8150 bytes 8c7f0294
- 00bb8110 ["INT_ADD", "register:40f0:8", ["const:bb8110:8", "const:4:8"]]
- 00bb8110 ["CALL", null, ["callee:00c58010:8"]]
+ 00bb81ac ["INT_ADD", "register:40f0:8", ["const:bb81ac:8", "const:4:8"]]
+ 00bb81ac ["CALL", null, ["callee:00c58010:8"]]
- 00bb8110 bytes 8c7f0294
+ 00bb81ac bytes 997f0294
- 00bb8138 ["INT_ADD", "register:40f0:8", ["const:bb8138:8", "const:4:8"]]
- 00bb8138 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bb81d4 ["INT_ADD", "register:40f0:8", ["const:bb81d4:8", "const:4:8"]]
+ 00bb81d4 ["CALL", null, ["callee:00c580d0:8"]]
- 00bb8138 bytes b27f0294
+ 00bb81d4 bytes bf7f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd018b72b4f9f2293b77e3f16a44c0cb"></a>

### [`00bb9638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9638.md) → [`00bb96d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb96d4.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb9658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9638.md#insn-00bb9658)
- 新版 `00bb96f4`（命令位置の公開資料なし）

~~~diff
- 00bb9658 ["INT_ADD", "register:40f0:8", ["const:bb9658:8", "const:4:8"]]
- 00bb9658 ["CALL", null, ["callee:00c5d650:8"]]
+ 00bb96f4 ["INT_ADD", "register:40f0:8", ["const:bb96f4:8", "const:4:8"]]
+ 00bb96f4 ["CALL", null, ["callee:00c5d650:8"]]
- 00bb9658 bytes ca8f0294
+ 00bb96f4 bytes d78f0294
~~~


<a id="compare-a2db984f30b44c552a11e1c0d309d508"></a>

### [`00bc10a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md) → [`00bc1140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1140.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d560.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5d630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d630.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc1140) · [`00bc122c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc122c) · [`00bc1268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc1268)
- 新版 `00bc11dc`（命令位置の公開資料なし） · `00bc12c8`（命令位置の公開資料なし） · `00bc1304`（命令位置の公開資料なし）

~~~diff
- 00bc1140 ["INT_ADD", "register:40f0:8", ["const:bc1140:8", "const:4:8"]]
- 00bc1140 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bc11dc ["INT_ADD", "register:40f0:8", ["const:bc11dc:8", "const:4:8"]]
+ 00bc11dc ["CALL", null, ["callee:00c57f60:8"]]
- 00bc1140 bytes 545b0294
+ 00bc11dc bytes 615b0294
- 00bc122c ["INT_ADD", "register:40f0:8", ["const:bc122c:8", "const:4:8"]]
- 00bc122c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc12c8 ["INT_ADD", "register:40f0:8", ["const:bc12c8:8", "const:4:8"]]
+ 00bc12c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bc122c bytes 215b0294
+ 00bc12c8 bytes 2e5b0294
- 00bc1268 ["INT_ADD", "register:40f0:8", ["const:bc1268:8", "const:4:8"]]
- 00bc1268 ["CALL", null, ["callee:00c5ade0:8"]]
+ 00bc1304 ["INT_ADD", "register:40f0:8", ["const:bc1304:8", "const:4:8"]]
+ 00bc1304 ["CALL", null, ["callee:00c5ade0:8"]]
- 00bc1268 bytes aa660294
+ 00bc1304 bytes b7660294
~~~


<a id="compare-59f31be3d0f4df77c10d45034ee601c4"></a>

### [`00bc17e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc17e8.md) → [`00bc1884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1884.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc17f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc17e8.md#insn-00bc17f0)
- 新版 `00bc188c`（命令位置の公開資料なし）

~~~diff
- 00bc17f0 ["INT_ADD", "register:40f0:8", ["const:bc17f0:8", "const:4:8"]]
- 00bc17f0 ["CALL", null, ["callee:00c5d780:8"]]
+ 00bc188c ["INT_ADD", "register:40f0:8", ["const:bc188c:8", "const:4:8"]]
+ 00bc188c ["CALL", null, ["callee:00c5d780:8"]]
- 00bc17f0 bytes b06f0294
+ 00bc188c bytes bd6f0294
~~~


<a id="compare-4e445027f298e33d816248c2bf2d0ebb"></a>

### [`00bc1830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1830.md) → [`00bc18cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc18cc.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d750.md) [`00c5d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d820.md) [`00c5d8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1830.md#insn-00bc1848)
- 新版 `00bc18e4`（命令位置の公開資料なし）

~~~diff
- 00bc1848 ["INT_ADD", "register:40f0:8", ["const:bc1848:8", "const:4:8"]]
- 00bc1848 ["CALL", null, ["callee:00c5d820:8"]]
+ 00bc18e4 ["INT_ADD", "register:40f0:8", ["const:bc18e4:8", "const:4:8"]]
+ 00bc18e4 ["CALL", null, ["callee:00c5d820:8"]]
- 00bc1848 bytes c26f0294
+ 00bc18e4 bytes cf6f0294
~~~


<a id="compare-3d64191084007d1bb1a98db9c9ab00e4"></a>

### [`00bc1958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md) → [`00bc19f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc19f4.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc199c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc199c) · [`00bc19c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc19c4) · [`00bc19d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc19d8)
- 新版 `00bc1a38`（命令位置の公開資料なし） · `00bc1a60`（命令位置の公開資料なし） · `00bc1a74`（命令位置の公開資料なし）

~~~diff
- 00bc199c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc199c ["INT_ADD", "register:40f0:8", ["const:bc199c:8", "const:4:8"]]
- 00bc199c ["CALLIND", null, ["register:0:8"]]
+ 00bc1a38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1a38 ["INT_ADD", "register:40f0:8", ["const:bc1a38:8", "const:4:8"]]
+ 00bc1a38 ["CALLIND", null, ["register:0:8"]]
- 00bc199c bytes 00013fd6
+ 00bc1a38 bytes 00013fd6
- 00bc19c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc19c4 ["INT_ADD", "register:40f0:8", ["const:bc19c4:8", "const:4:8"]]
- 00bc19c4 ["CALLIND", null, ["register:0:8"]]
+ 00bc1a60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1a60 ["INT_ADD", "register:40f0:8", ["const:bc1a60:8", "const:4:8"]]
+ 00bc1a60 ["CALLIND", null, ["register:0:8"]]
- 00bc19c4 bytes 00013fd6
+ 00bc1a60 bytes 00013fd6
- 00bc19d8 ["INT_ADD", "register:40f0:8", ["const:bc19d8:8", "const:4:8"]]
- 00bc19d8 ["CALL", null, ["callee:00c5d860:8"]]
+ 00bc1a74 ["INT_ADD", "register:40f0:8", ["const:bc1a74:8", "const:4:8"]]
+ 00bc1a74 ["CALL", null, ["callee:00c5d860:8"]]
- 00bc19d8 bytes 6e6f0294
+ 00bc1a74 bytes 7b6f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1a2592a37afd933d74544a54bae9a0"></a>

### [`00bc1a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md) → [`00bc1b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b34.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8b0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8b0.md)
- 新版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d980.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md#insn-00bc1ab4) · [`00bc1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md#insn-00bc1ac0)
- 新版 `00bc1b50`（命令位置の公開資料なし） · `00bc1b5c`（命令位置の公開資料なし）

~~~diff
- 00bc1ab4 ["INT_ADD", "register:40f0:8", ["const:bc1ab4:8", "const:4:8"]]
- 00bc1ab4 ["CALL", null, ["callee:00c5d980:8"]]
+ 00bc1b50 ["INT_ADD", "register:40f0:8", ["const:bc1b50:8", "const:4:8"]]
+ 00bc1b50 ["CALL", null, ["callee:00c5d980:8"]]
- 00bc1ab4 bytes 7f6f0294
+ 00bc1b50 bytes 8c6f0294
- 00bc1ac0 ["INT_ADD", "register:40f0:8", ["const:bc1ac0:8", "const:4:8"]]
- 00bc1ac0 ["CALL", null, ["callee:00c5d980:8"]]
+ 00bc1b5c ["INT_ADD", "register:40f0:8", ["const:bc1b5c:8", "const:4:8"]]
+ 00bc1b5c ["CALL", null, ["callee:00c5d980:8"]]
- 00bc1ac0 bytes 7c6f0294
+ 00bc1b5c bytes 896f0294
~~~


<a id="compare-80c3ec523fe66605560228a0e83e1fa2"></a>

### [`00bc48d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md) → [`00bc4974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4974.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d930.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da00.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc48f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc48f8) · [`00bc4910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc4910) · [`00bc4918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc4918)
- 新版 `00bc4994`（命令位置の公開資料なし） · `00bc49ac`（命令位置の公開資料なし） · `00bc49b4`（命令位置の公開資料なし）

~~~diff
- 00bc48f8 ["INT_ADD", "register:40f0:8", ["const:bc48f8:8", "const:4:8"]]
- 00bc48f8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc4994 ["INT_ADD", "register:40f0:8", ["const:bc4994:8", "const:4:8"]]
+ 00bc4994 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc48f8 bytes 42580294
+ 00bc4994 bytes 4f580294
- 00bc4910 ["INT_ADD", "register:40f0:8", ["const:bc4910:8", "const:4:8"]]
- 00bc4910 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc49ac ["INT_ADD", "register:40f0:8", ["const:bc49ac:8", "const:4:8"]]
+ 00bc49ac ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc4910 bytes 40580294
+ 00bc49ac bytes 4d580294
- 00bc4918 ["INT_ADD", "register:40f0:8", ["const:bc4918:8", "const:4:8"]]
- 00bc4918 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc49b4 ["INT_ADD", "register:40f0:8", ["const:bc49b4:8", "const:4:8"]]
+ 00bc49b4 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc4918 bytes 3e580294
+ 00bc49b4 bytes 4b580294
~~~


<a id="compare-1680f1009e5a0572dee6d71f8e049041"></a>

### [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) → [`00bc51bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bc5a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md) [`00bc5d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2e0.md)
- 新版 呼出元 2件 [`00bc5a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md) [`00bc5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5b3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md#insn-00bc5160) · [`00bc5180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md#insn-00bc5180) · [`00bc519c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md#insn-00bc519c)
- 新版 `00bc51fc`（命令位置の公開資料なし） · `00bc521c`（命令位置の公開資料なし） · `00bc5238`（命令位置の公開資料なし）

~~~diff
- 00bc5160 ["INT_ADD", "register:40f0:8", ["const:bc5160:8", "const:4:8"]]
- 00bc5160 ["CALL", null, ["callee:00c5b3b0:8"]]
+ 00bc51fc ["INT_ADD", "register:40f0:8", ["const:bc51fc:8", "const:4:8"]]
+ 00bc51fc ["CALL", null, ["callee:00c5b3b0:8"]]
- 00bc5160 bytes 60580294
+ 00bc51fc bytes 6d580294
- 00bc5180 ["INT_ADD", "register:40f0:8", ["const:bc5180:8", "const:4:8"]]
- 00bc5180 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bc521c ["INT_ADD", "register:40f0:8", ["const:bc521c:8", "const:4:8"]]
+ 00bc521c ["CALL", null, ["callee:00c5aed0:8"]]
- 00bc5180 bytes 20570294
+ 00bc521c bytes 2d570294
- 00bc519c ["INT_ADD", "register:40f0:8", ["const:bc519c:8", "const:4:8"]]
- 00bc519c ["CALL", null, ["callee:00c5d9b0:8"]]
+ 00bc5238 ["INT_ADD", "register:40f0:8", ["const:bc5238:8", "const:4:8"]]
+ 00bc5238 ["CALL", null, ["callee:00c5d9b0:8"]]
- 00bc519c bytes d1610294
+ 00bc5238 bytes de610294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4cd4dbe85a6020f44bbd2d14716bdb7"></a>

### [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) → [`00bc52ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bc72e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md) [`00bc773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md) [`00c5d8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8c0.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 3件 [`00bc7384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md) [`00bc77d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc77d8.md) [`00c5d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc528c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc528c) · [`00bc52a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc52a8) · [`00bc52b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc52b0)
- 新版 `00bc5328`（命令位置の公開資料なし） · `00bc5344`（命令位置の公開資料なし） · `00bc534c`（命令位置の公開資料なし）

~~~diff
- 00bc528c ["INT_ADD", "register:40f0:8", ["const:bc528c:8", "const:4:8"]]
- 00bc528c ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bc5328 ["INT_ADD", "register:40f0:8", ["const:bc5328:8", "const:4:8"]]
+ 00bc5328 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bc528c bytes dd560294
+ 00bc5328 bytes ea560294
- 00bc52a8 ["INT_ADD", "register:40f0:8", ["const:bc52a8:8", "const:4:8"]]
- 00bc52a8 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bc5344 ["INT_ADD", "register:40f0:8", ["const:bc5344:8", "const:4:8"]]
+ 00bc5344 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bc52a8 bytes be560294
+ 00bc5344 bytes cb560294
- 00bc52b0 ["INT_ADD", "register:40f0:8", ["const:bc52b0:8", "const:4:8"]]
- 00bc52b0 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00bc534c ["INT_ADD", "register:40f0:8", ["const:bc534c:8", "const:4:8"]]
+ 00bc534c ["CALL", null, ["callee:00c5ab60:8"]]
- 00bc52b0 bytes f8550294
+ 00bc534c bytes 05560294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f0467b0c466aeb2b40f7f1d786784d"></a>

### [`00bc55b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md) → [`00bc564c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc564c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d980.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5da50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da50.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc5600) · [`00bc562c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc562c) · [`00bc5658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc5658)
- 新版 `00bc569c`（命令位置の公開資料なし） · `00bc56c8`（命令位置の公開資料なし） · `00bc56f4`（命令位置の公開資料なし）

~~~diff
- 00bc5600 ["INT_ADD", "register:40f0:8", ["const:bc5600:8", "const:4:8"]]
- 00bc5600 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bc569c ["INT_ADD", "register:40f0:8", ["const:bc569c:8", "const:4:8"]]
+ 00bc569c ["CALL", null, ["callee:00c57f60:8"]]
- 00bc5600 bytes 244a0294
+ 00bc569c bytes 314a0294
- 00bc562c ["INT_ADD", "register:40f0:8", ["const:bc562c:8", "const:4:8"]]
- 00bc562c ["CALL", null, ["callee:00c5b680:8"]]
+ 00bc56c8 ["INT_ADD", "register:40f0:8", ["const:bc56c8:8", "const:4:8"]]
+ 00bc56c8 ["CALL", null, ["callee:00c5b680:8"]]
- 00bc562c bytes e1570294
+ 00bc56c8 bytes ee570294
- 00bc5658 ["INT_ADD", "register:40f0:8", ["const:bc5658:8", "const:4:8"]]
- 00bc5658 ["CALL", null, ["callee:00c5ade0:8"]]
+ 00bc56f4 ["INT_ADD", "register:40f0:8", ["const:bc56f4:8", "const:4:8"]]
+ 00bc56f4 ["CALL", null, ["callee:00c5ade0:8"]]
- 00bc5658 bytes ae550294
+ 00bc56f4 bytes bb550294
~~~


<a id="compare-09825731c8d94399981649f85bbcb4a2"></a>

### [`00bc5970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md) → [`00bc5a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a0c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7c0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d890.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc5990) · [`00bc599c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc599c) · [`00bc59a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc59a8)
- 新版 `00bc5a2c`（命令位置の公開資料なし） · `00bc5a38`（命令位置の公開資料なし） · `00bc5a44`（命令位置の公開資料なし）

~~~diff
- 00bc5990 ["INT_ADD", "register:40f0:8", ["const:bc5990:8", "const:4:8"]]
- 00bc5990 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc5a2c ["INT_ADD", "register:40f0:8", ["const:bc5a2c:8", "const:4:8"]]
+ 00bc5a2c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc5990 bytes 1c540294
+ 00bc5a2c bytes 29540294
- 00bc599c ["INT_ADD", "register:40f0:8", ["const:bc599c:8", "const:4:8"]]
- 00bc599c ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc5a38 ["INT_ADD", "register:40f0:8", ["const:bc5a38:8", "const:4:8"]]
+ 00bc5a38 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc599c bytes 1d540294
+ 00bc5a38 bytes 2a540294
- 00bc59a8 ["INT_ADD", "register:40f0:8", ["const:bc59a8:8", "const:4:8"]]
- 00bc59a8 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc5a44 ["INT_ADD", "register:40f0:8", ["const:bc5a44:8", "const:4:8"]]
+ 00bc5a44 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc59a8 bytes b2540294
+ 00bc5a44 bytes bf540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f63b71a235096d8051f6456be9842e"></a>

### [`00bc5c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md) → [`00bc5d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5d38.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d770.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d840.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cbc) · [`00bc5cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cc8) · [`00bc5cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cd4)
- 新版 `00bc5d58`（命令位置の公開資料なし） · `00bc5d64`（命令位置の公開資料なし） · `00bc5d70`（命令位置の公開資料なし）

~~~diff
- 00bc5cbc ["INT_ADD", "register:40f0:8", ["const:bc5cbc:8", "const:4:8"]]
- 00bc5cbc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc5d58 ["INT_ADD", "register:40f0:8", ["const:bc5d58:8", "const:4:8"]]
+ 00bc5d58 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc5cbc bytes 51530294
+ 00bc5d58 bytes 5e530294
- 00bc5cc8 ["INT_ADD", "register:40f0:8", ["const:bc5cc8:8", "const:4:8"]]
- 00bc5cc8 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc5d64 ["INT_ADD", "register:40f0:8", ["const:bc5d64:8", "const:4:8"]]
+ 00bc5d64 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc5cc8 bytes 52530294
+ 00bc5d64 bytes 5f530294
- 00bc5cd4 ["INT_ADD", "register:40f0:8", ["const:bc5cd4:8", "const:4:8"]]
- 00bc5cd4 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc5d70 ["INT_ADD", "register:40f0:8", ["const:bc5d70:8", "const:4:8"]]
+ 00bc5d70 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc5cd4 bytes e7530294
+ 00bc5d70 bytes f4530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf335ff3d139b7a16bd57417b2d1c07"></a>

### [`00bc5fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md) → [`00bc6064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6064.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26FetchAndActivateLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7a0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d870.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc5fe8) · [`00bc5ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc5ff4) · [`00bc6000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc6000)
- 新版 `00bc6084`（命令位置の公開資料なし） · `00bc6090`（命令位置の公開資料なし） · `00bc609c`（命令位置の公開資料なし）

~~~diff
- 00bc5fe8 ["INT_ADD", "register:40f0:8", ["const:bc5fe8:8", "const:4:8"]]
- 00bc5fe8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc6084 ["INT_ADD", "register:40f0:8", ["const:bc6084:8", "const:4:8"]]
+ 00bc6084 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc5fe8 bytes 86520294
+ 00bc6084 bytes 93520294
- 00bc5ff4 ["INT_ADD", "register:40f0:8", ["const:bc5ff4:8", "const:4:8"]]
- 00bc5ff4 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc6090 ["INT_ADD", "register:40f0:8", ["const:bc6090:8", "const:4:8"]]
+ 00bc6090 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc5ff4 bytes 87520294
+ 00bc6090 bytes 94520294
- 00bc6000 ["INT_ADD", "register:40f0:8", ["const:bc6000:8", "const:4:8"]]
- 00bc6000 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc609c ["INT_ADD", "register:40f0:8", ["const:bc609c:8", "const:4:8"]]
+ 00bc609c ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc6000 bytes 1c530294
+ 00bc609c bytes 29530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45a2206357ea7165f1127d4163b011d"></a>

### [`00bc62f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md) → [`00bc638c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc638c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d700.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7d0.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc6310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc6310) · [`00bc631c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc631c) · [`00bc6328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc6328)
- 新版 `00bc63ac`（命令位置の公開資料なし） · `00bc63b8`（命令位置の公開資料なし） · `00bc63c4`（命令位置の公開資料なし）

~~~diff
- 00bc6310 ["INT_ADD", "register:40f0:8", ["const:bc6310:8", "const:4:8"]]
- 00bc6310 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc63ac ["INT_ADD", "register:40f0:8", ["const:bc63ac:8", "const:4:8"]]
+ 00bc63ac ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc6310 bytes bc510294
+ 00bc63ac bytes c9510294
- 00bc631c ["INT_ADD", "register:40f0:8", ["const:bc631c:8", "const:4:8"]]
- 00bc631c ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc63b8 ["INT_ADD", "register:40f0:8", ["const:bc63b8:8", "const:4:8"]]
+ 00bc63b8 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc631c bytes bd510294
+ 00bc63b8 bytes ca510294
- 00bc6328 ["INT_ADD", "register:40f0:8", ["const:bc6328:8", "const:4:8"]]
- 00bc6328 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc63c4 ["INT_ADD", "register:40f0:8", ["const:bc63c4:8", "const:4:8"]]
+ 00bc63c4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc6328 bytes 52520294
+ 00bc63c4 bytes 5f520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6755950fef3d5f0fb0b86df2b760e0c"></a>

### [`00bc7258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md) → [`00bc72f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc72f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d780.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d850.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7278) · [`00bc7284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7284) · [`00bc7290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7290)
- 新版 `00bc7314`（命令位置の公開資料なし） · `00bc7320`（命令位置の公開資料なし） · `00bc732c`（命令位置の公開資料なし）

~~~diff
- 00bc7278 ["INT_ADD", "register:40f0:8", ["const:bc7278:8", "const:4:8"]]
- 00bc7278 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc7314 ["INT_ADD", "register:40f0:8", ["const:bc7314:8", "const:4:8"]]
+ 00bc7314 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc7278 bytes e24d0294
+ 00bc7314 bytes ef4d0294
- 00bc7284 ["INT_ADD", "register:40f0:8", ["const:bc7284:8", "const:4:8"]]
- 00bc7284 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc7320 ["INT_ADD", "register:40f0:8", ["const:bc7320:8", "const:4:8"]]
+ 00bc7320 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc7284 bytes e34d0294
+ 00bc7320 bytes f04d0294
- 00bc7290 ["INT_ADD", "register:40f0:8", ["const:bc7290:8", "const:4:8"]]
- 00bc7290 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc732c ["INT_ADD", "register:40f0:8", ["const:bc732c:8", "const:4:8"]]
+ 00bc732c ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc7290 bytes 784e0294
+ 00bc732c bytes 854e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cb9f742c0e5496ef57712909cfe1c49"></a>

### [`00bc76ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md) → [`00bc7748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7748.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7d0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8a0.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc76cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76cc) · [`00bc76d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76d8) · [`00bc76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76e4)
- 新版 `00bc7768`（命令位置の公開資料なし） · `00bc7774`（命令位置の公開資料なし） · `00bc7780`（命令位置の公開資料なし）

~~~diff
- 00bc76cc ["INT_ADD", "register:40f0:8", ["const:bc76cc:8", "const:4:8"]]
- 00bc76cc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc7768 ["INT_ADD", "register:40f0:8", ["const:bc7768:8", "const:4:8"]]
+ 00bc7768 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc76cc bytes cd4c0294
+ 00bc7768 bytes da4c0294
- 00bc76d8 ["INT_ADD", "register:40f0:8", ["const:bc76d8:8", "const:4:8"]]
- 00bc76d8 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc7774 ["INT_ADD", "register:40f0:8", ["const:bc7774:8", "const:4:8"]]
+ 00bc7774 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc76d8 bytes ce4c0294
+ 00bc7774 bytes db4c0294
- 00bc76e4 ["INT_ADD", "register:40f0:8", ["const:bc76e4:8", "const:4:8"]]
- 00bc76e4 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc7780 ["INT_ADD", "register:40f0:8", ["const:bc7780:8", "const:4:8"]]
+ 00bc7780 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc76e4 bytes 634d0294
+ 00bc7780 bytes 704d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e2e58435da53fbd2a38364305ea8063"></a>

### [`00bc7df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md) → [`00bc7e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7e90.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26SetCustomSignalsLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7b0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d880.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e14) · [`00bc7e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e20) · [`00bc7e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e2c)
- 新版 `00bc7eb0`（命令位置の公開資料なし） · `00bc7ebc`（命令位置の公開資料なし） · `00bc7ec8`（命令位置の公開資料なし）

~~~diff
- 00bc7e14 ["INT_ADD", "register:40f0:8", ["const:bc7e14:8", "const:4:8"]]
- 00bc7e14 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc7eb0 ["INT_ADD", "register:40f0:8", ["const:bc7eb0:8", "const:4:8"]]
+ 00bc7eb0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc7e14 bytes fb4a0294
+ 00bc7eb0 bytes 084b0294
- 00bc7e20 ["INT_ADD", "register:40f0:8", ["const:bc7e20:8", "const:4:8"]]
- 00bc7e20 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc7ebc ["INT_ADD", "register:40f0:8", ["const:bc7ebc:8", "const:4:8"]]
+ 00bc7ebc ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc7e20 bytes fc4a0294
+ 00bc7ebc bytes 094b0294
- 00bc7e2c ["INT_ADD", "register:40f0:8", ["const:bc7e2c:8", "const:4:8"]]
- 00bc7e2c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc7ec8 ["INT_ADD", "register:40f0:8", ["const:bc7ec8:8", "const:4:8"]]
+ 00bc7ec8 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc7e2c bytes 914b0294
+ 00bc7ec8 bytes 9e4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe64385785ce43dbffd1aaf574c4a6d"></a>

### [`00bc89b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89b4.md) → [`00bc8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a50.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d940.md) · 呼出先 1件 [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5da10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da10.md) · 呼出先 1件 [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc89c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89b4.md#insn-00bc89c0)
- 新版 `00bc8a5c`（命令位置の公開資料なし）

~~~diff
- 00bc89c0 ["INT_ADD", "register:40f0:8", ["const:bc89c0:8", "const:4:8"]]
- 00bc89c0 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc8a5c ["INT_ADD", "register:40f0:8", ["const:bc8a5c:8", "const:4:8"]]
+ 00bc8a5c ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc89c0 bytes 14480294
+ 00bc8a5c bytes 21480294
~~~


<a id="compare-f20d9dc66a2c11ae50521619670e5ca8"></a>

### [`00bc9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md) → [`00bc96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc96a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96a4) · [`00bc96e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96e0) · [`00bc96f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96f8)
- 新版 `00bc9740`（命令位置の公開資料なし） · `00bc977c`（命令位置の公開資料なし） · `00bc9794`（命令位置の公開資料なし）

~~~diff
- 00bc96a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc96a4 ["INT_ADD", "register:40f0:8", ["const:bc96a4:8", "const:4:8"]]
- 00bc96a4 ["CALLIND", null, ["register:0:8"]]
+ 00bc9740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc9740 ["INT_ADD", "register:40f0:8", ["const:bc9740:8", "const:4:8"]]
+ 00bc9740 ["CALLIND", null, ["register:0:8"]]
- 00bc96a4 bytes 00013fd6
+ 00bc9740 bytes 00013fd6
- 00bc96e0 ["INT_ADD", "register:40f0:8", ["const:bc96e0:8", "const:4:8"]]
- 00bc96e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc977c ["INT_ADD", "register:40f0:8", ["const:bc977c:8", "const:4:8"]]
+ 00bc977c ["CALL", null, ["callee:00c57f80:8"]]
- 00bc96e0 bytes f4390294
+ 00bc977c bytes 013a0294
- 00bc96f8 ["INT_ADD", "register:40f0:8", ["const:bc96f8:8", "const:4:8"]]
- 00bc96f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc9794 ["INT_ADD", "register:40f0:8", ["const:bc9794:8", "const:4:8"]]
+ 00bc9794 ["CALL", null, ["callee:00c57f80:8"]]
- 00bc96f8 bytes ee390294
+ 00bc9794 bytes fb390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7232231d4cf227692e84d9cf5e5bdf96"></a>

### [`00bc9788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md) → [`00bc9824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9824.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d960.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d950.md)
- 新版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da30.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc97bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc97bc) · [`00bc97d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc97d8) · [`00bc9800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc9800)
- 新版 `00bc9858`（命令位置の公開資料なし） · `00bc9874`（命令位置の公開資料なし） · `00bc989c`（命令位置の公開資料なし）

~~~diff
- 00bc97bc ["INT_ADD", "register:40f0:8", ["const:bc97bc:8", "const:4:8"]]
- 00bc97bc ["CALL", null, ["callee:00c5da20:8"]]
+ 00bc9858 ["INT_ADD", "register:40f0:8", ["const:bc9858:8", "const:4:8"]]
+ 00bc9858 ["CALL", null, ["callee:00c5da20:8"]]
- 00bc97bc bytes 65500294
+ 00bc9858 bytes 72500294
- 00bc97d8 ["INT_ADD", "register:40f0:8", ["const:bc97d8:8", "const:4:8"]]
- 00bc97d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bc9874 ["INT_ADD", "register:40f0:8", ["const:bc9874:8", "const:4:8"]]
+ 00bc9874 ["CALL", null, ["callee:00c57f60:8"]]
- 00bc97d8 bytes ae390294
+ 00bc9874 bytes bb390294
- 00bc9800 ["INT_ADD", "register:40f0:8", ["const:bc9800:8", "const:4:8"]]
- 00bc9800 ["CALL", null, ["callee:00c5a910:8"]]
+ 00bc989c ["INT_ADD", "register:40f0:8", ["const:bc989c:8", "const:4:8"]]
+ 00bc989c ["CALL", null, ["callee:00c5a910:8"]]
- 00bc9800 bytes 10440294
+ 00bc989c bytes 1d440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3738a33f3a0ec0c78d0c982d97f33288"></a>

### [`00bc9878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md) → [`00bc9914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9914.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d950.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da20.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md#insn-00bc9914) · [`00bc9954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md#insn-00bc9954)
- 新版 `00bc99b0`（命令位置の公開資料なし） · `00bc99f0`（命令位置の公開資料なし）

~~~diff
- 00bc9914 ["INT_ADD", "register:40f0:8", ["const:bc9914:8", "const:4:8"]]
- 00bc9914 ["CALL", null, ["callee:00c58120:8"]]
+ 00bc99b0 ["INT_ADD", "register:40f0:8", ["const:bc99b0:8", "const:4:8"]]
+ 00bc99b0 ["CALL", null, ["callee:00c58120:8"]]
- 00bc9914 bytes cf390294
+ 00bc99b0 bytes dc390294
- 00bc9954 ["INT_ADD", "register:40f0:8", ["const:bc9954:8", "const:4:8"]]
- 00bc9954 ["CALL", null, ["callee:00c58120:8"]]
+ 00bc99f0 ["INT_ADD", "register:40f0:8", ["const:bc99f0:8", "const:4:8"]]
+ 00bc99f0 ["CALL", null, ["callee:00c58120:8"]]
- 00bc9954 bytes bf390294
+ 00bc99f0 bytes cc390294
~~~


<a id="compare-6872edbcd13a2f22e6251a7f8e5c04de"></a>

### [`00bc9998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md) → [`00bc9a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a34.md) FUN_00bc9a34

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc91f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d690.md)
- 新版 呼出元 1件 [`00bc9290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc99ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md#insn-00bc99ac)
- 新版 `00bc9a48`（命令位置の公開資料なし）

~~~diff
- 00bc99ac ["INT_ADD", "register:40f0:8", ["const:bc99ac:8", "const:4:8"]]
- 00bc99ac ["CALL", null, ["callee:00c5d760:8"]]
+ 00bc9a48 ["INT_ADD", "register:40f0:8", ["const:bc9a48:8", "const:4:8"]]
+ 00bc9a48 ["CALL", null, ["callee:00c5d760:8"]]
- 00bc99ac bytes 394f0294
+ 00bc9a48 bytes 464f0294
~~~


<a id="compare-f240b8fdf1299f3c4e63cd054d409940"></a>

### [`00bca324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca324.md) → [`00bca3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca3c0.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d670.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca324.md#insn-00bca344)
- 新版 `00bca3e0`（命令位置の公開資料なし）

~~~diff
- 00bca344 ["INT_ADD", "register:40f0:8", ["const:bca344:8", "const:4:8"]]
- 00bca344 ["CALL", null, ["callee:00c5d740:8"]]
+ 00bca3e0 ["INT_ADD", "register:40f0:8", ["const:bca3e0:8", "const:4:8"]]
+ 00bca3e0 ["CALL", null, ["callee:00c5d740:8"]]
- 00bca344 bytes cb4c0294
+ 00bca3e0 bytes d84c0294
~~~


<a id="compare-f696616d6dc4e9a2dd4493da2f4991d1"></a>

### [`00bca368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md) → [`00bca404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca404.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d680.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d750.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md#insn-00bca39c) · [`00bca3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md#insn-00bca3c0)
- 新版 `00bca438`（命令位置の公開資料なし） · `00bca45c`（命令位置の公開資料なし）

~~~diff
- 00bca39c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca39c ["INT_ADD", "register:40f0:8", ["const:bca39c:8", "const:4:8"]]
- 00bca39c ["CALLIND", null, ["register:0:8"]]
+ 00bca438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca438 ["INT_ADD", "register:40f0:8", ["const:bca438:8", "const:4:8"]]
+ 00bca438 ["CALLIND", null, ["register:0:8"]]
- 00bca39c bytes 00013fd6
+ 00bca438 bytes 00013fd6
- 00bca3c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca3c0 ["INT_ADD", "register:40f0:8", ["const:bca3c0:8", "const:4:8"]]
- 00bca3c0 ["CALLIND", null, ["register:0:8"]]
+ 00bca45c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca45c ["INT_ADD", "register:40f0:8", ["const:bca45c:8", "const:4:8"]]
+ 00bca45c ["CALLIND", null, ["register:0:8"]]
- 00bca3c0 bytes 00013fd6
+ 00bca45c bytes 00013fd6
~~~


<a id="compare-532bf794d83f2d4bde801e4331b89c27"></a>

### [`00bca3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md) → [`00bca470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca470.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d690.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)
- 新版 呼出元 1件 [`00c5d760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d760.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md#insn-00bca404) · [`00bca448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md#insn-00bca448)
- 新版 `00bca4a0`（命令位置の公開資料なし） · `00bca4e4`（命令位置の公開資料なし）

~~~diff
- 00bca404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca404 ["INT_ADD", "register:40f0:8", ["const:bca404:8", "const:4:8"]]
- 00bca404 ["CALLIND", null, ["register:0:8"]]
+ 00bca4a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca4a0 ["INT_ADD", "register:40f0:8", ["const:bca4a0:8", "const:4:8"]]
+ 00bca4a0 ["CALLIND", null, ["register:0:8"]]
- 00bca404 bytes 00013fd6
+ 00bca4a0 bytes 00013fd6
- 00bca448 ["INT_ADD", "register:40f0:8", ["const:bca448:8", "const:4:8"]]
- 00bca448 ["CALL", null, ["callee:00b611c8:8"]]
+ 00bca4e4 ["INT_ADD", "register:40f0:8", ["const:bca4e4:8", "const:4:8"]]
+ 00bca4e4 ["CALL", null, ["callee:00b611c8:8"]]
- 00bca448 bytes 395bfe97
+ 00bca4e4 bytes 395bfe97
~~~


<a id="compare-9ebbac5c584d0997e191ebb22d83d3b1"></a>

### [`00bca460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md) → [`00bca4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca4fc.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d670.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)
- 新版 呼出元 1件 [`00c5d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d740.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md#insn-00bca49c)
- 新版 `00bca538`（命令位置の公開資料なし）

~~~diff
- 00bca49c ["INT_ADD", "register:40f0:8", ["const:bca49c:8", "const:4:8"]]
- 00bca49c ["CALL", null, ["callee:00b611c8:8"]]
+ 00bca538 ["INT_ADD", "register:40f0:8", ["const:bca538:8", "const:4:8"]]
+ 00bca538 ["CALL", null, ["callee:00b611c8:8"]]
- 00bca49c bytes 245bfe97
+ 00bca538 bytes 245bfe97
~~~


<a id="compare-763d4751e644fc42933d51dac731a0f4"></a>

### [`00bcac98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md) → [`00bcad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcad34.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dab0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9a0.md)
- 新版 呼出元 1件 [`00c5db80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db80.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab20.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5da70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcaca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcaca8) · [`00bcacc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcacc4) · [`00bcacd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcacd4)
- 新版 `00bcad44`（命令位置の公開資料なし） · `00bcad60`（命令位置の公開資料なし） · `00bcad70`（命令位置の公開資料なし）

~~~diff
- 00bcaca8 ["INT_ADD", "register:40f0:8", ["const:bcaca8:8", "const:4:8"]]
- 00bcaca8 ["CALL", null, ["callee:00c5da70:8"]]
+ 00bcad44 ["INT_ADD", "register:40f0:8", ["const:bcad44:8", "const:4:8"]]
+ 00bcad44 ["CALL", null, ["callee:00c5da70:8"]]
- 00bcaca8 bytes 3e4b0294
+ 00bcad44 bytes 4b4b0294
- 00bcacc4 ["INT_ADD", "register:40f0:8", ["const:bcacc4:8", "const:4:8"]]
- 00bcacc4 ["CALL", null, ["callee:00c5db40:8"]]
+ 00bcad60 ["INT_ADD", "register:40f0:8", ["const:bcad60:8", "const:4:8"]]
+ 00bcad60 ["CALL", null, ["callee:00c5db40:8"]]
- 00bcacc4 bytes 6b4b0294
+ 00bcad60 bytes 784b0294
- 00bcacd4 ["INT_ADD", "register:40f0:8", ["const:bcacd4:8", "const:4:8"]]
- 00bcacd4 ["CALL", null, ["callee:00c5db30:8"]]
+ 00bcad70 ["INT_ADD", "register:40f0:8", ["const:bcad70:8", "const:4:8"]]
+ 00bcad70 ["CALL", null, ["callee:00c5db30:8"]]
- 00bcacd4 bytes 634b0294
+ 00bcad70 bytes 704b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7819ca8cc67b9cb24f51a92a578992b5"></a>

### [`00bcade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcade4.md) → [`00bcae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae80.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5db00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcadec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcade4.md#insn-00bcadec)
- 新版 `00bcae88`（命令位置の公開資料なし）

~~~diff
- 00bcadec ["INT_ADD", "register:40f0:8", ["const:bcadec:8", "const:4:8"]]
- 00bcadec ["CALL", null, ["callee:00c5db00:8"]]
+ 00bcae88 ["INT_ADD", "register:40f0:8", ["const:bcae88:8", "const:4:8"]]
+ 00bcae88 ["CALL", null, ["callee:00c5db00:8"]]
- 00bcadec bytes 114b0294
+ 00bcae88 bytes 1e4b0294
~~~


<a id="compare-4be199d0f2f762360f04595bfab61eac"></a>

### [`00bcb9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md) → [`00bcba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba40.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9c4) · [`00bcb9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9d0) · [`00bcb9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9dc)
- 新版 `00bcba60`（命令位置の公開資料なし） · `00bcba6c`（命令位置の公開資料なし） · `00bcba78`（命令位置の公開資料なし）

~~~diff
- 00bcb9c4 ["INT_ADD", "register:40f0:8", ["const:bcb9c4:8", "const:4:8"]]
- 00bcb9c4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcba60 ["INT_ADD", "register:40f0:8", ["const:bcba60:8", "const:4:8"]]
+ 00bcba60 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcb9c4 bytes 0f3c0294
+ 00bcba60 bytes 1c3c0294
- 00bcb9d0 ["INT_ADD", "register:40f0:8", ["const:bcb9d0:8", "const:4:8"]]
- 00bcb9d0 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bcba6c ["INT_ADD", "register:40f0:8", ["const:bcba6c:8", "const:4:8"]]
+ 00bcba6c ["CALL", null, ["callee:00c5aae0:8"]]
- 00bcb9d0 bytes 103c0294
+ 00bcba6c bytes 1d3c0294
- 00bcb9dc ["INT_ADD", "register:40f0:8", ["const:bcb9dc:8", "const:4:8"]]
- 00bcb9dc ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bcba78 ["INT_ADD", "register:40f0:8", ["const:bcba78:8", "const:4:8"]]
+ 00bcba78 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcb9dc bytes a53c0294
+ 00bcba78 bytes b23c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24cb05b4cab7210ddfe8b9b816125e3c"></a>

### [`00bcba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md) → [`00bcbad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbad0.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcba54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md#insn-00bcba54) · [`00bcba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md#insn-00bcba60) · [`00bcba6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md#insn-00bcba6c)
- 新版 `00bcbaf0`（命令位置の公開資料なし） · `00bcbafc`（命令位置の公開資料なし） · `00bcbb08`（命令位置の公開資料なし）

~~~diff
- 00bcba54 ["INT_ADD", "register:40f0:8", ["const:bcba54:8", "const:4:8"]]
- 00bcba54 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcbaf0 ["INT_ADD", "register:40f0:8", ["const:bcbaf0:8", "const:4:8"]]
+ 00bcbaf0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcba54 bytes eb3b0294
+ 00bcbaf0 bytes f83b0294
- 00bcba60 ["INT_ADD", "register:40f0:8", ["const:bcba60:8", "const:4:8"]]
- 00bcba60 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bcbafc ["INT_ADD", "register:40f0:8", ["const:bcbafc:8", "const:4:8"]]
+ 00bcbafc ["CALL", null, ["callee:00c5aae0:8"]]
- 00bcba60 bytes ec3b0294
+ 00bcbafc bytes f93b0294
- 00bcba6c ["INT_ADD", "register:40f0:8", ["const:bcba6c:8", "const:4:8"]]
- 00bcba6c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bcbb08 ["INT_ADD", "register:40f0:8", ["const:bcbb08:8", "const:4:8"]]
+ 00bcbb08 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcba6c bytes 813c0294
+ 00bcbb08 bytes 8e3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83483be0567ce3610d08a40ad00a210d"></a>

### [`00bcbac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md) → [`00bcbb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbb60.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md#insn-00bcbae4) · [`00bcbaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md#insn-00bcbaf0) · [`00bcbafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md#insn-00bcbafc)
- 新版 `00bcbb80`（命令位置の公開資料なし） · `00bcbb8c`（命令位置の公開資料なし） · `00bcbb98`（命令位置の公開資料なし）

~~~diff
- 00bcbae4 ["INT_ADD", "register:40f0:8", ["const:bcbae4:8", "const:4:8"]]
- 00bcbae4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcbb80 ["INT_ADD", "register:40f0:8", ["const:bcbb80:8", "const:4:8"]]
+ 00bcbb80 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcbae4 bytes c73b0294
+ 00bcbb80 bytes d43b0294
- 00bcbaf0 ["INT_ADD", "register:40f0:8", ["const:bcbaf0:8", "const:4:8"]]
- 00bcbaf0 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bcbb8c ["INT_ADD", "register:40f0:8", ["const:bcbb8c:8", "const:4:8"]]
+ 00bcbb8c ["CALL", null, ["callee:00c5aae0:8"]]
- 00bcbaf0 bytes c83b0294
+ 00bcbb8c bytes d53b0294
- 00bcbafc ["INT_ADD", "register:40f0:8", ["const:bcbafc:8", "const:4:8"]]
- 00bcbafc ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bcbb98 ["INT_ADD", "register:40f0:8", ["const:bcbb98:8", "const:4:8"]]
+ 00bcbb98 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcbafc bytes 5d3c0294
+ 00bcbb98 bytes 6a3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-228ab95a92c5d964d1cd308ee24f6ab7"></a>

### [`00bcbc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md) → [`00bcbd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbd10.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

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
    "new": null,
    "old": {
      "definition_site": "00bcbc90",
      "incomplete_value": true,
      "site": "00bcbc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcbc9c",
      "incomplete_value": true,
      "site": "00bcbca0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md#insn-00bcbc94) · [`00bcbca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md#insn-00bcbca0) · [`00bcbcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md#insn-00bcbcac)
- 新版 `00bcbd30`（命令位置の公開資料なし） · `00bcbd3c`（命令位置の公開資料なし） · `00bcbd48`（命令位置の公開資料なし）

~~~diff
- 00bcbc94 ["INT_ADD", "register:40f0:8", ["const:bcbc94:8", "const:4:8"]]
- 00bcbc94 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcbd30 ["INT_ADD", "register:40f0:8", ["const:bcbd30:8", "const:4:8"]]
+ 00bcbd30 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcbc94 bytes 5b3b0294
+ 00bcbd30 bytes 683b0294
- 00bcbca0 ["INT_ADD", "register:40f0:8", ["const:bcbca0:8", "const:4:8"]]
- 00bcbca0 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bcbd3c ["INT_ADD", "register:40f0:8", ["const:bcbd3c:8", "const:4:8"]]
+ 00bcbd3c ["CALL", null, ["callee:00c5aae0:8"]]
- 00bcbca0 bytes 5c3b0294
+ 00bcbd3c bytes 693b0294
- 00bcbcac ["INT_ADD", "register:40f0:8", ["const:bcbcac:8", "const:4:8"]]
- 00bcbcac ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bcbd48 ["INT_ADD", "register:40f0:8", ["const:bcbd48:8", "const:4:8"]]
+ 00bcbd48 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcbcac bytes f13b0294
+ 00bcbd48 bytes fe3b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c52473b6a69a22026258f74bc1d2214f"></a>

### [`00bcbde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md) → [`00bcbe80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe80.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md)
- 新版 呼出元 1件 [`00c5db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md#insn-00bcbe00) · [`00bcbe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md#insn-00bcbe0c)
- 新版 `00bcbe9c`（命令位置の公開資料なし） · `00bcbea8`（命令位置の公開資料なし）

~~~diff
- 00bcbe00 ["INT_ADD", "register:40f0:8", ["const:bcbe00:8", "const:4:8"]]
- 00bcbe00 ["CALL", null, ["callee:00c5db90:8"]]
+ 00bcbe9c ["INT_ADD", "register:40f0:8", ["const:bcbe9c:8", "const:4:8"]]
+ 00bcbe9c ["CALL", null, ["callee:00c5db90:8"]]
- 00bcbe00 bytes 30470294
+ 00bcbe9c bytes 3d470294
- 00bcbe0c ["INT_ADD", "register:40f0:8", ["const:bcbe0c:8", "const:4:8"]]
- 00bcbe0c ["CALL", null, ["callee:00c5db90:8"]]
+ 00bcbea8 ["INT_ADD", "register:40f0:8", ["const:bcbea8:8", "const:4:8"]]
+ 00bcbea8 ["CALL", null, ["callee:00c5db90:8"]]
- 00bcbe0c bytes 2d470294
+ 00bcbea8 bytes 3a470294
~~~


<a id="compare-71e4a5568fb0743686d2413a939fc93d"></a>

### [`00bcc2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md) → [`00bcc340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc340.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5aa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md#insn-00bcc2b4) · [`00bcc2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md#insn-00bcc2c0)
- 新版 `00bcc350`（命令位置の公開資料なし） · `00bcc35c`（命令位置の公開資料なし）

~~~diff
- 00bcc2b4 ["INT_ADD", "register:40f0:8", ["const:bcc2b4:8", "const:4:8"]]
- 00bcc2b4 ["CALL", null, ["callee:00c5ab30:8"]]
+ 00bcc350 ["INT_ADD", "register:40f0:8", ["const:bcc350:8", "const:4:8"]]
+ 00bcc350 ["CALL", null, ["callee:00c5ab30:8"]]
- 00bcc2b4 bytes eb390294
+ 00bcc350 bytes f8390294
- 00bcc2c0 ["INT_ADD", "register:40f0:8", ["const:bcc2c0:8", "const:4:8"]]
- 00bcc2c0 ["CALL", null, ["callee:00c5ab30:8"]]
+ 00bcc35c ["INT_ADD", "register:40f0:8", ["const:bcc35c:8", "const:4:8"]]
+ 00bcc35c ["CALL", null, ["callee:00c5ab30:8"]]
- 00bcc2c0 bytes e8390294
+ 00bcc35c bytes f5390294
~~~


<a id="compare-6af7584010a039ce81bd61cf48350c66"></a>

### [`00bcc2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md) → [`00bcc374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc374.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5aa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md#insn-00bcc2e8) · [`00bcc2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md#insn-00bcc2f4)
- 新版 `00bcc384`（命令位置の公開資料なし） · `00bcc390`（命令位置の公開資料なし）

~~~diff
- 00bcc2e8 ["INT_ADD", "register:40f0:8", ["const:bcc2e8:8", "const:4:8"]]
- 00bcc2e8 ["CALL", null, ["callee:00c5ab30:8"]]
+ 00bcc384 ["INT_ADD", "register:40f0:8", ["const:bcc384:8", "const:4:8"]]
+ 00bcc384 ["CALL", null, ["callee:00c5ab30:8"]]
- 00bcc2e8 bytes de390294
+ 00bcc384 bytes eb390294
- 00bcc2f4 ["INT_ADD", "register:40f0:8", ["const:bcc2f4:8", "const:4:8"]]
- 00bcc2f4 ["CALL", null, ["callee:00c5ab30:8"]]
+ 00bcc390 ["INT_ADD", "register:40f0:8", ["const:bcc390:8", "const:4:8"]]
+ 00bcc390 ["CALL", null, ["callee:00c5ab30:8"]]
- 00bcc2f4 bytes db390294
+ 00bcc390 bytes e8390294
~~~


<a id="compare-2791c9db66f7407730be801529da9c21"></a>

### [`00bce3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md) → [`00bce474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce474.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcd0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbc0.md)
- 新版 呼出元 1件 [`00c5dda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dda0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md#insn-00bce40c) · [`00bce420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md#insn-00bce420) · [`00bce44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md#insn-00bce44c)
- 新版 `00bce4a8`（命令位置の公開資料なし） · `00bce4bc`（命令位置の公開資料なし） · `00bce4e8`（命令位置の公開資料なし）

~~~diff
- 00bce40c ["INT_ADD", "register:40f0:8", ["const:bce40c:8", "const:4:8"]]
- 00bce40c ["CALL", null, ["callee:00c5dde0:8"]]
+ 00bce4a8 ["INT_ADD", "register:40f0:8", ["const:bce4a8:8", "const:4:8"]]
+ 00bce4a8 ["CALL", null, ["callee:00c5dde0:8"]]
- 00bce40c bytes 413e0294
+ 00bce4a8 bytes 4e3e0294
- 00bce420 ["INT_ADD", "register:40f0:8", ["const:bce420:8", "const:4:8"]]
- 00bce420 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bce4bc ["INT_ADD", "register:40f0:8", ["const:bce4bc:8", "const:4:8"]]
+ 00bce4bc ["CALL", null, ["callee:00c5aed0:8"]]
- 00bce420 bytes 78320294
+ 00bce4bc bytes 85320294
- 00bce44c ["INT_ADD", "register:40f0:8", ["const:bce44c:8", "const:4:8"]]
- 00bce44c ["CALL", null, ["callee:00c5dc90:8"]]
+ 00bce4e8 ["INT_ADD", "register:40f0:8", ["const:bce4e8:8", "const:4:8"]]
+ 00bce4e8 ["CALL", null, ["callee:00c5dc90:8"]]
- 00bce44c bytes dd3d0294
+ 00bce4e8 bytes ea3d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d8330e46f7c0a8bdd2115234b71dbc"></a>

### [`00bce78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md) → [`00bce828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce828.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcf0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbe0.md)
- 新版 呼出元 1件 [`00c5ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddc0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce7c0) · [`00bce7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce7d4) · [`00bce800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce800)
- 新版 `00bce85c`（命令位置の公開資料なし） · `00bce870`（命令位置の公開資料なし） · `00bce89c`（命令位置の公開資料なし）

~~~diff
- 00bce7c0 ["INT_ADD", "register:40f0:8", ["const:bce7c0:8", "const:4:8"]]
- 00bce7c0 ["CALL", null, ["callee:00c5dde0:8"]]
+ 00bce85c ["INT_ADD", "register:40f0:8", ["const:bce85c:8", "const:4:8"]]
+ 00bce85c ["CALL", null, ["callee:00c5dde0:8"]]
- 00bce7c0 bytes 543d0294
+ 00bce85c bytes 613d0294
- 00bce7d4 ["INT_ADD", "register:40f0:8", ["const:bce7d4:8", "const:4:8"]]
- 00bce7d4 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bce870 ["INT_ADD", "register:40f0:8", ["const:bce870:8", "const:4:8"]]
+ 00bce870 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bce7d4 bytes 8b310294
+ 00bce870 bytes 98310294
- 00bce800 ["INT_ADD", "register:40f0:8", ["const:bce800:8", "const:4:8"]]
- 00bce800 ["CALL", null, ["callee:00c5dcb0:8"]]
+ 00bce89c ["INT_ADD", "register:40f0:8", ["const:bce89c:8", "const:4:8"]]
+ 00bce89c ["CALL", null, ["callee:00c5dcb0:8"]]
- 00bce800 bytes f83c0294
+ 00bce89c bytes 053d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6930183fadbc320903ec3d8a925f11c0"></a>

### [`00bcf8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) → [`00bcf93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf93c.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md#insn-00bcf8f0) · [`00bcf90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md#insn-00bcf90c)
- 新版 `00bcf98c`（命令位置の公開資料なし） · `00bcf9a8`（命令位置の公開資料なし）

~~~diff
- 00bcf8f0 ["INT_ADD", "register:40f0:8", ["const:bcf8f0:8", "const:4:8"]]
- 00bcf8f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bcf98c ["INT_ADD", "register:40f0:8", ["const:bcf98c:8", "const:4:8"]]
+ 00bcf98c ["CALL", null, ["callee:00c57f80:8"]]
- 00bcf8f0 bytes 70210294
+ 00bcf98c bytes 7d210294
- 00bcf90c ["INT_ADD", "register:40f0:8", ["const:bcf90c:8", "const:4:8"]]
- 00bcf90c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bcf9a8 ["INT_ADD", "register:40f0:8", ["const:bcf9a8:8", "const:4:8"]]
+ 00bcf9a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bcf90c bytes 69210294
+ 00bcf9a8 bytes 76210294
~~~


<a id="compare-adbd381b7691697c3e6871e6e5066cc0"></a>

### [`00bcfa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) → [`00bcfac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md) _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dba0.md)
- 新版 呼出元 1件 [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfa64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfa64) · [`00bcfa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfa7c) · [`00bcfaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfaa4)
- 新版 `00bcfb00`（命令位置の公開資料なし） · `00bcfb18`（命令位置の公開資料なし） · `00bcfb40`（命令位置の公開資料なし）

~~~diff
- 00bcfa64 ["INT_ADD", "register:40f0:8", ["const:bcfa64:8", "const:4:8"]]
- 00bcfa64 ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00bcfb00 ["INT_ADD", "register:40f0:8", ["const:bcfb00:8", "const:4:8"]]
+ 00bcfb00 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00bcfa64 bytes af380294
+ 00bcfb00 bytes bc380294
- 00bcfa7c ["INT_ADD", "register:40f0:8", ["const:bcfa7c:8", "const:4:8"]]
- 00bcfa7c ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcfb18 ["INT_ADD", "register:40f0:8", ["const:bcfb18:8", "const:4:8"]]
+ 00bcfb18 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcfa7c bytes e12c0294
+ 00bcfb18 bytes ee2c0294
- 00bcfaa4 ["INT_ADD", "register:40f0:8", ["const:bcfaa4:8", "const:4:8"]]
- 00bcfaa4 ["CALL", null, ["callee:00c5dc70:8"]]
+ 00bcfb40 ["INT_ADD", "register:40f0:8", ["const:bcfb40:8", "const:4:8"]]
+ 00bcfb40 ["CALL", null, ["callee:00c5dc70:8"]]
- 00bcfaa4 bytes 3f380294
+ 00bcfb40 bytes 4c380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f96190a80622e1bef80bc1597d4fb8"></a>

### [`00bcfc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md) → [`00bcfcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfcd4.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd40.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5de10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de10.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc58) · [`00bcfc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc6c) · [`00bcfc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc80)
- 新版 `00bcfcf4`（命令位置の公開資料なし） · `00bcfd08`（命令位置の公開資料なし） · `00bcfd1c`（命令位置の公開資料なし）

~~~diff
- 00bcfc58 ["INT_ADD", "register:40f0:8", ["const:bcfc58:8", "const:4:8"]]
- 00bcfc58 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bcfcf4 ["INT_ADD", "register:40f0:8", ["const:bcfcf4:8", "const:4:8"]]
+ 00bcfcf4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcfc58 bytes 062c0294
+ 00bcfcf4 bytes 132c0294
- 00bcfc6c ["INT_ADD", "register:40f0:8", ["const:bcfc6c:8", "const:4:8"]]
- 00bcfc6c ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcfd08 ["INT_ADD", "register:40f0:8", ["const:bcfd08:8", "const:4:8"]]
+ 00bcfd08 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcfc6c bytes 652c0294
+ 00bcfd08 bytes 722c0294
- 00bcfc80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfc80 ["INT_ADD", "register:40f0:8", ["const:bcfc80:8", "const:4:8"]]
- 00bcfc80 ["CALLIND", null, ["register:0:8"]]
+ 00bcfd1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfd1c ["INT_ADD", "register:40f0:8", ["const:bcfd1c:8", "const:4:8"]]
+ 00bcfd1c ["CALLIND", null, ["register:0:8"]]
- 00bcfc80 bytes 00013fd6
+ 00bcfd1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67be0d56395de774b626285b05aa89aa"></a>

### [`00bcfcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) → [`00bcfd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bce28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce28c.md) [`00bdbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9f0.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)
- 新版 呼出元 2件 [`00bce328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce328.md) [`00bdbc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aac0.md) [`00c5ab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab20.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfcf0) · [`00bcfcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfcf8) · [`00bcfd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfd00)
- 新版 `00bcfd8c`（命令位置の公開資料なし） · `00bcfd94`（命令位置の公開資料なし） · `00bcfd9c`（命令位置の公開資料なし）

~~~diff
- 00bcfcf0 ["INT_ADD", "register:40f0:8", ["const:bcfcf0:8", "const:4:8"]]
- 00bcfcf0 ["CALL", null, ["callee:00c5ab20:8"]]
+ 00bcfd8c ["INT_ADD", "register:40f0:8", ["const:bcfd8c:8", "const:4:8"]]
+ 00bcfd8c ["CALL", null, ["callee:00c5ab20:8"]]
- 00bcfcf0 bytes 582b0294
+ 00bcfd8c bytes 652b0294
- 00bcfcf8 ["INT_ADD", "register:40f0:8", ["const:bcfcf8:8", "const:4:8"]]
- 00bcfcf8 ["CALL", null, ["callee:00c5aac0:8"]]
+ 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
+ 00bcfd94 ["CALL", null, ["callee:00c5aac0:8"]]
- 00bcfcf8 bytes 3e2b0294
+ 00bcfd94 bytes 4b2b0294
- 00bcfd00 ["INT_ADD", "register:40f0:8", ["const:bcfd00:8", "const:4:8"]]
- 00bcfd00 ["CALL", null, ["callee:00c5aac0:8"]]
+ 00bcfd9c ["INT_ADD", "register:40f0:8", ["const:bcfd9c:8", "const:4:8"]]
+ 00bcfd9c ["CALL", null, ["callee:00c5aac0:8"]]
- 00bcfd00 bytes 3c2b0294
+ 00bcfd9c bytes 492b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe500d6beb4df98f3d78c525ea1a8cd"></a>

### [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) → [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) [`00bce890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) [`00bceb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) [`00bcec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) [`00bcef18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db90.md)
- 新版 呼出元 8件 [`00bce164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce164.md) [`00bce92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce92c.md) [`00bceb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md) [`00bced28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md) [`00bcefb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfd7c) · [`00bcfd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfd94) · [`00bcfdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfdbc)
- 新版 `00bcfe18`（命令位置の公開資料なし） · `00bcfe30`（命令位置の公開資料なし） · `00bcfe58`（命令位置の公開資料なし）

~~~diff
- 00bcfd7c ["INT_ADD", "register:40f0:8", ["const:bcfd7c:8", "const:4:8"]]
- 00bcfd7c ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00bcfe18 ["INT_ADD", "register:40f0:8", ["const:bcfe18:8", "const:4:8"]]
+ 00bcfe18 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00bcfd7c bytes e9370294
+ 00bcfe18 bytes f6370294
- 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
- 00bcfd94 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcfe30 ["INT_ADD", "register:40f0:8", ["const:bcfe30:8", "const:4:8"]]
+ 00bcfe30 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcfd94 bytes 1b2c0294
+ 00bcfe30 bytes 282c0294
- 00bcfdbc ["INT_ADD", "register:40f0:8", ["const:bcfdbc:8", "const:4:8"]]
- 00bcfdbc ["CALL", null, ["callee:00c5dc60:8"]]
+ 00bcfe58 ["INT_ADD", "register:40f0:8", ["const:bcfe58:8", "const:4:8"]]
+ 00bcfe58 ["CALL", null, ["callee:00c5dc60:8"]]
- 00bcfdbc bytes 75370294
+ 00bcfe58 bytes 82370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e67a18f22d16604409551347395044ae"></a>

### [`00bd47b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd47b0.md) → [`00bd484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd484c.md) _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd50.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd47e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd47b0.md#insn-00bd47e0) · [`00bd47fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd47b0.md#insn-00bd47fc) · [`00bd4814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd47b0.md#insn-00bd4814)
- 新版 `00bd487c`（命令位置の公開資料なし） · `00bd4898`（命令位置の公開資料なし） · `00bd48b0`（命令位置の公開資料なし）

~~~diff
- 00bd47e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd47e0 ["INT_ADD", "register:40f0:8", ["const:bd47e0:8", "const:4:8"]]
- 00bd47e0 ["CALLIND", null, ["register:0:8"]]
+ 00bd487c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd487c ["INT_ADD", "register:40f0:8", ["const:bd487c:8", "const:4:8"]]
+ 00bd487c ["CALLIND", null, ["register:0:8"]]
- 00bd47e0 bytes 00013fd6
+ 00bd487c bytes 00013fd6
- 00bd47fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd47fc ["INT_ADD", "register:40f0:8", ["const:bd47fc:8", "const:4:8"]]
- 00bd47fc ["CALLIND", null, ["register:0:8"]]
+ 00bd4898 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4898 ["INT_ADD", "register:40f0:8", ["const:bd4898:8", "const:4:8"]]
+ 00bd4898 ["CALLIND", null, ["register:0:8"]]
- 00bd47fc bytes 00013fd6
+ 00bd4898 bytes 00013fd6
- 00bd4814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4814 ["INT_ADD", "register:40f0:8", ["const:bd4814:8", "const:4:8"]]
- 00bd4814 ["CALLIND", null, ["register:0:8"]]
+ 00bd48b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd48b0 ["INT_ADD", "register:40f0:8", ["const:bd48b0:8", "const:4:8"]]
+ 00bd48b0 ["CALLIND", null, ["register:0:8"]]
- 00bd4814 bytes 00013fd6
+ 00bd48b0 bytes 00013fd6
~~~


<a id="compare-b688343574f36c831ba9720c94566875"></a>

### [`00bd4d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md) → [`00bd4e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4e04.md) _ZN8firebase4auth18AdditionalUserInfoaSEOS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd70.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)
- 新版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de40.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4da8) · [`00bd4df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4df8) · [`00bd4e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4e28)
- 新版 `00bd4e44`（命令位置の公開資料なし） · `00bd4e94`（命令位置の公開資料なし） · `00bd4ec4`（命令位置の公開資料なし）

~~~diff
- 00bd4da8 ["INT_ADD", "register:40f0:8", ["const:bd4da8:8", "const:4:8"]]
- 00bd4da8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bd4e44 ["INT_ADD", "register:40f0:8", ["const:bd4e44:8", "const:4:8"]]
+ 00bd4e44 ["CALL", null, ["callee:00c57f80:8"]]
- 00bd4da8 bytes 420c0294
+ 00bd4e44 bytes 4f0c0294
- 00bd4df8 ["INT_ADD", "register:40f0:8", ["const:bd4df8:8", "const:4:8"]]
- 00bd4df8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bd4e94 ["INT_ADD", "register:40f0:8", ["const:bd4e94:8", "const:4:8"]]
+ 00bd4e94 ["CALL", null, ["callee:00c57f80:8"]]
- 00bd4df8 bytes 2e0c0294
+ 00bd4e94 bytes 3b0c0294
- 00bd4e28 ["INT_ADD", "register:40f0:8", ["const:bd4e28:8", "const:4:8"]]
- 00bd4e28 ["CALL", null, ["callee:00c5bef0:8"]]
+ 00bd4ec4 ["INT_ADD", "register:40f0:8", ["const:bd4ec4:8", "const:4:8"]]
+ 00bd4ec4 ["CALL", null, ["callee:00c5bef0:8"]]
- 00bd4e28 bytes fe1b0294
+ 00bd4ec4 bytes 0b1c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-682fc1955d7a1b764da4de513588e261"></a>

### [`00bd9270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9270.md) → [`00bd930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd930c.md) _ZN8firebase4auth10CredentialC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd9294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9270.md#insn-00bd9294)
- 新版 `00bd9330`（命令位置の公開資料なし）

~~~diff
- 00bd9294 ["INT_ADD", "register:40f0:8", ["const:bd9294:8", "const:4:8"]]
- 00bd9294 ["CALL", null, ["callee:00c5de30:8"]]
+ 00bd9330 ["INT_ADD", "register:40f0:8", ["const:bd9330:8", "const:4:8"]]
+ 00bd9330 ["CALL", null, ["callee:00c5de30:8"]]
- 00bd9294 bytes b3120294
+ 00bd9330 bytes c0120294
~~~


<a id="compare-012894c61001aa38facfd96186182171"></a>

### [`00bd9714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md) → [`00bd97b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd97b0.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de30.md) · 呼出先 2件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)
- 新版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df00.md) · 呼出先 2件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd9728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md#insn-00bd9728) · [`00bd9754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md#insn-00bd9754)
- 新版 `00bd97c4`（命令位置の公開資料なし） · `00bd97f0`（命令位置の公開資料なし）

~~~diff
- 00bd9728 ["INT_ADD", "register:40f0:8", ["const:bd9728:8", "const:4:8"]]
- 00bd9728 ["CALL", null, ["callee:00c5de30:8"]]
+ 00bd97c4 ["INT_ADD", "register:40f0:8", ["const:bd97c4:8", "const:4:8"]]
+ 00bd97c4 ["CALL", null, ["callee:00c5de30:8"]]
- 00bd9728 bytes 8e110294
+ 00bd97c4 bytes 9b110294
- 00bd9754 ["INT_ADD", "register:40f0:8", ["const:bd9754:8", "const:4:8"]]
- 00bd9754 ["CALL", null, ["callee:00c5b180:8"]]
+ 00bd97f0 ["INT_ADD", "register:40f0:8", ["const:bd97f0:8", "const:4:8"]]
+ 00bd97f0 ["CALL", null, ["callee:00c5b180:8"]]
- 00bd9754 bytes 57060294
+ 00bd97f0 bytes 64060294
~~~


<a id="compare-99498844e5dd8f1716c2952141f07ad2"></a>

### [`00bda534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md) → [`00bda5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda5d0.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda558) · [`00bda568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda568) · [`00bda574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda574)
- 新版 `00bda5f4`（命令位置の公開資料なし） · `00bda604`（命令位置の公開資料なし） · `00bda610`（命令位置の公開資料なし）

~~~diff
- 00bda558 ["INT_ADD", "register:40f0:8", ["const:bda558:8", "const:4:8"]]
- 00bda558 ["CALL", null, ["callee:00c5dc20:8"]]
+ 00bda5f4 ["INT_ADD", "register:40f0:8", ["const:bda5f4:8", "const:4:8"]]
+ 00bda5f4 ["CALL", null, ["callee:00c5dc20:8"]]
- 00bda558 bytes 7e0d0294
+ 00bda5f4 bytes 8b0d0294
- 00bda568 ["INT_ADD", "register:40f0:8", ["const:bda568:8", "const:4:8"]]
- 00bda568 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bda604 ["INT_ADD", "register:40f0:8", ["const:bda604:8", "const:4:8"]]
+ 00bda604 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bda568 bytes 26010294
+ 00bda604 bytes 33010294
- 00bda574 ["INT_ADD", "register:40f0:8", ["const:bda574:8", "const:4:8"]]
- 00bda574 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bda610 ["INT_ADD", "register:40f0:8", ["const:bda610:8", "const:4:8"]]
+ 00bda610 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bda574 bytes 27010294
+ 00bda610 bytes 34010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d10626594bdc2d55ac1853ea8db9058b"></a>

### [`00bda678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda678.md) → [`00bda714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda714.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda678.md#insn-00bda68c)
- 新版 `00bda728`（命令位置の公開資料なし）

~~~diff
- 00bda68c ["INT_ADD", "register:40f0:8", ["const:bda68c:8", "const:4:8"]]
- 00bda68c ["CALL", null, ["callee:00c57f60:8"]]
+ 00bda728 ["INT_ADD", "register:40f0:8", ["const:bda728:8", "const:4:8"]]
+ 00bda728 ["CALL", null, ["callee:00c57f60:8"]]
- 00bda68c bytes 01f60194
+ 00bda728 bytes 0ef60194
~~~


<a id="compare-69258b05a5d3918e5277c5a92473c853"></a>

### [`00bda710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda710.md) → [`00bda7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7ac.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda710.md#insn-00bda728)
- 新版 `00bda7c4`（命令位置の公開資料なし）

~~~diff
- 00bda728 ["INT_ADD", "register:40f0:8", ["const:bda728:8", "const:4:8"]]
- 00bda728 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bda7c4 ["INT_ADD", "register:40f0:8", ["const:bda7c4:8", "const:4:8"]]
+ 00bda7c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00bda728 bytes daf50194
+ 00bda7c4 bytes e7f50194
~~~


<a id="compare-9e028feb0cef754c24a90c050df454a8"></a>

### [`00bda7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda7ec.md) → [`00bda888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda888.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda7ec.md#insn-00bda808)
- 新版 `00bda8a4`（命令位置の公開資料なし）

~~~diff
- 00bda808 ["INT_ADD", "register:40f0:8", ["const:bda808:8", "const:4:8"]]
- 00bda808 ["CALL", null, ["callee:00c5df10:8"]]
+ 00bda8a4 ["INT_ADD", "register:40f0:8", ["const:bda8a4:8", "const:4:8"]]
+ 00bda8a4 ["CALL", null, ["callee:00c5df10:8"]]
- 00bda808 bytes 8e0d0294
+ 00bda8a4 bytes 9b0d0294
~~~


<a id="compare-8e6986569232663b61a2d97cbfb28fde"></a>

### [`00bdb2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md) → [`00bdb37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb37c.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb308) · [`00bdb31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb31c) · [`00bdb32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb32c)
- 新版 `00bdb3a4`（命令位置の公開資料なし） · `00bdb3b8`（命令位置の公開資料なし） · `00bdb3c8`（命令位置の公開資料なし）

~~~diff
- 00bdb308 ["INT_ADD", "register:40f0:8", ["const:bdb308:8", "const:4:8"]]
- 00bdb308 ["CALL", null, ["callee:00c5aff0:8"]]
+ 00bdb3a4 ["INT_ADD", "register:40f0:8", ["const:bdb3a4:8", "const:4:8"]]
+ 00bdb3a4 ["CALL", null, ["callee:00c5aff0:8"]]
- 00bdb308 bytes 06ff0194
+ 00bdb3a4 bytes 13ff0194
- 00bdb31c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb31c ["INT_ADD", "register:40f0:8", ["const:bdb31c:8", "const:4:8"]]
- 00bdb31c ["CALLIND", null, ["register:0:8"]]
+ 00bdb3b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdb3b8 ["INT_ADD", "register:40f0:8", ["const:bdb3b8:8", "const:4:8"]]
+ 00bdb3b8 ["CALLIND", null, ["register:0:8"]]
- 00bdb31c bytes 00013fd6
+ 00bdb3b8 bytes 00013fd6
- 00bdb32c ["INT_ADD", "register:40f0:8", ["const:bdb32c:8", "const:4:8"]]
- 00bdb32c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bdb3c8 ["INT_ADD", "register:40f0:8", ["const:bdb3c8:8", "const:4:8"]]
+ 00bdb3c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bdb32c bytes e1f20194
+ 00bdb3c8 bytes eef20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c6a3c4f35072a194bdf782fcf6806b"></a>

### [`00bdb4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md) → [`00bdb58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb58c.md) _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb518) · [`00bdb52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb52c) · [`00bdb53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb53c)
- 新版 `00bdb5b4`（命令位置の公開資料なし） · `00bdb5c8`（命令位置の公開資料なし） · `00bdb5d8`（命令位置の公開資料なし）

~~~diff
- 00bdb518 ["INT_ADD", "register:40f0:8", ["const:bdb518:8", "const:4:8"]]
- 00bdb518 ["CALL", null, ["callee:00c5b460:8"]]
+ 00bdb5b4 ["INT_ADD", "register:40f0:8", ["const:bdb5b4:8", "const:4:8"]]
+ 00bdb5b4 ["CALL", null, ["callee:00c5b460:8"]]
- 00bdb518 bytes 9eff0194
+ 00bdb5b4 bytes abff0194
- 00bdb52c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb52c ["INT_ADD", "register:40f0:8", ["const:bdb52c:8", "const:4:8"]]
- 00bdb52c ["CALLIND", null, ["register:0:8"]]
+ 00bdb5c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdb5c8 ["INT_ADD", "register:40f0:8", ["const:bdb5c8:8", "const:4:8"]]
+ 00bdb5c8 ["CALLIND", null, ["register:0:8"]]
- 00bdb52c bytes 00013fd6
+ 00bdb5c8 bytes 00013fd6
- 00bdb53c ["INT_ADD", "register:40f0:8", ["const:bdb53c:8", "const:4:8"]]
- 00bdb53c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bdb5d8 ["INT_ADD", "register:40f0:8", ["const:bdb5d8:8", "const:4:8"]]
+ 00bdb5d8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bdb53c bytes 5df20194
+ 00bdb5d8 bytes 6af20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d62b002057a7858165a7fde37ec7d7d2"></a>

### [`00bdc428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md) → [`00bdc4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4c4.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bda410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5de00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de00.md)
- 新版 呼出元 1件 [`00bda4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ded0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ded0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md#insn-00bdc43c)
- 新版 `00bdc4d8`（命令位置の公開資料なし）

~~~diff
- 00bdc43c ["INT_ADD", "register:40f0:8", ["const:bdc43c:8", "const:4:8"]]
- 00bdc43c ["CALL", null, ["callee:00c5ded0:8"]]
+ 00bdc4d8 ["INT_ADD", "register:40f0:8", ["const:bdc4d8:8", "const:4:8"]]
+ 00bdc4d8 ["CALL", null, ["callee:00c5ded0:8"]]
- 00bdc43c bytes 71060294
+ 00bdc4d8 bytes 7e060294
~~~


<a id="compare-de58215272d2d729b9dccc8a674610c2"></a>

### [`00bdc55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc55c.md) → [`00bdc5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md) _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de50.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df20.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc55c.md#insn-00bdc57c) · [`00bdc590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc55c.md#insn-00bdc590) · [`00bdc5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc55c.md#insn-00bdc5a4)
- 新版 `00bdc618`（命令位置の公開資料なし） · `00bdc62c`（命令位置の公開資料なし） · `00bdc640`（命令位置の公開資料なし）

~~~diff
- 00bdc57c ["INT_ADD", "register:40f0:8", ["const:bdc57c:8", "const:4:8"]]
- 00bdc57c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bdc618 ["INT_ADD", "register:40f0:8", ["const:bdc618:8", "const:4:8"]]
+ 00bdc618 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bdc57c bytes bdf90194
+ 00bdc618 bytes caf90194
- 00bdc590 ["INT_ADD", "register:40f0:8", ["const:bdc590:8", "const:4:8"]]
- 00bdc590 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bdc62c ["INT_ADD", "register:40f0:8", ["const:bdc62c:8", "const:4:8"]]
+ 00bdc62c ["CALL", null, ["callee:00c5aed0:8"]]
- 00bdc590 bytes 1cfa0194
+ 00bdc62c bytes 29fa0194
- 00bdc5a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdc5a4 ["INT_ADD", "register:40f0:8", ["const:bdc5a4:8", "const:4:8"]]
- 00bdc5a4 ["CALLIND", null, ["register:0:8"]]
+ 00bdc640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdc640 ["INT_ADD", "register:40f0:8", ["const:bdc640:8", "const:4:8"]]
+ 00bdc640 ["CALLIND", null, ["register:0:8"]]
- 00bdc5a4 bytes 00013fd6
+ 00bdc640 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2018647fee0c740b82146093e16420f"></a>

### [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) → [`00bdcc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) [`00bdbe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbe78.md) [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd20.md)
- 新版 呼出元 3件 [`00bdb930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb930.md) [`00bdbf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbf14.md) [`00bdc1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdcbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md#insn-00bdcbb4) · [`00bdcbd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md#insn-00bdcbd4) · [`00bdcbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md#insn-00bdcbfc)
- 新版 `00bdcc50`（命令位置の公開資料なし） · `00bdcc70`（命令位置の公開資料なし） · `00bdcc98`（命令位置の公開資料なし）

~~~diff
- 00bdcbb4 ["INT_ADD", "register:40f0:8", ["const:bdcbb4:8", "const:4:8"]]
- 00bdcbb4 ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00bdcc50 ["INT_ADD", "register:40f0:8", ["const:bdcc50:8", "const:4:8"]]
+ 00bdcc50 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00bdcbb4 bytes 5b040294
+ 00bdcc50 bytes 68040294
- 00bdcbd4 ["INT_ADD", "register:40f0:8", ["const:bdcbd4:8", "const:4:8"]]
- 00bdcbd4 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bdcc70 ["INT_ADD", "register:40f0:8", ["const:bdcc70:8", "const:4:8"]]
+ 00bdcc70 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bdcbd4 bytes 8bf80194
+ 00bdcc70 bytes 98f80194
- 00bdcbfc ["INT_ADD", "register:40f0:8", ["const:bdcbfc:8", "const:4:8"]]
- 00bdcbfc ["CALL", null, ["callee:00c5de90:8"]]
+ 00bdcc98 ["INT_ADD", "register:40f0:8", ["const:bdcc98:8", "const:4:8"]]
+ 00bdcc98 ["CALL", null, ["callee:00c5de90:8"]]
- 00bdcbfc bytes 71040294
+ 00bdcc98 bytes 7e040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251c7161dd9a12177686e99b84e08e88"></a>

### [`00bdcdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcdc0.md) → [`00bdce5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdce5c.md) _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdcde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcdc0.md#insn-00bdcde4)
- 新版 `00bdce80`（命令位置の公開資料なし）

~~~diff
- 00bdcde4 ["INT_ADD", "register:40f0:8", ["const:bdcde4:8", "const:4:8"]]
- 00bdcde4 ["CALL", null, ["callee:00c5df00:8"]]
+ 00bdce80 ["INT_ADD", "register:40f0:8", ["const:bdce80:8", "const:4:8"]]
+ 00bdce80 ["CALL", null, ["callee:00c5df00:8"]]
- 00bdcde4 bytes 13040294
+ 00bdce80 bytes 20040294
~~~


<a id="compare-cbb7be7320a499040be7787f4605255d"></a>

### [`00bdea78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md) → [`00bdeb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdeb14.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26Refere

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5deb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5deb0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd10.md)
- 新版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df80.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dde0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdeaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeaac) · [`00bdeac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeac0) · [`00bdeaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeaec)
- 新版 `00bdeb48`（命令位置の公開資料なし） · `00bdeb5c`（命令位置の公開資料なし） · `00bdeb88`（命令位置の公開資料なし）

~~~diff
- 00bdeaac ["INT_ADD", "register:40f0:8", ["const:bdeaac:8", "const:4:8"]]
- 00bdeaac ["CALL", null, ["callee:00c5dde0:8"]]
+ 00bdeb48 ["INT_ADD", "register:40f0:8", ["const:bdeb48:8", "const:4:8"]]
+ 00bdeb48 ["CALL", null, ["callee:00c5dde0:8"]]
- 00bdeaac bytes 99fc0194
+ 00bdeb48 bytes a6fc0194
- 00bdeac0 ["INT_ADD", "register:40f0:8", ["const:bdeac0:8", "const:4:8"]]
- 00bdeac0 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bdeb5c ["INT_ADD", "register:40f0:8", ["const:bdeb5c:8", "const:4:8"]]
+ 00bdeb5c ["CALL", null, ["callee:00c5aed0:8"]]
- 00bdeac0 bytes d0f00194
+ 00bdeb5c bytes ddf00194
- 00bdeaec ["INT_ADD", "register:40f0:8", ["const:bdeaec:8", "const:4:8"]]
- 00bdeaec ["CALL", null, ["callee:00c5df60:8"]]
+ 00bdeb88 ["INT_ADD", "register:40f0:8", ["const:bdeb88:8", "const:4:8"]]
+ 00bdeb88 ["CALL", null, ["callee:00c5df60:8"]]
- 00bdeaec bytes e9fc0194
+ 00bdeb88 bytes f6fc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-102daf2c86206eae7cd48f8b9b61ef11"></a>

### [`00be13b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md) → [`00be1450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1450.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd20.md)
- 新版 呼出元 1件 [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be13ec) · [`00be1404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be1404) · [`00be142c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be142c)
- 新版 `00be1488`（命令位置の公開資料なし） · `00be14a0`（命令位置の公開資料なし） · `00be14c8`（命令位置の公開資料なし）

~~~diff
- 00be13ec ["INT_ADD", "register:40f0:8", ["const:be13ec:8", "const:4:8"]]
- 00be13ec ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00be1488 ["INT_ADD", "register:40f0:8", ["const:be1488:8", "const:4:8"]]
+ 00be1488 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00be13ec bytes 4df20194
+ 00be1488 bytes 5af20194
- 00be1404 ["INT_ADD", "register:40f0:8", ["const:be1404:8", "const:4:8"]]
- 00be1404 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00be14a0 ["INT_ADD", "register:40f0:8", ["const:be14a0:8", "const:4:8"]]
+ 00be14a0 ["CALL", null, ["callee:00c5aed0:8"]]
- 00be1404 bytes 7fe60194
+ 00be14a0 bytes 8ce60194
- 00be142c ["INT_ADD", "register:40f0:8", ["const:be142c:8", "const:4:8"]]
- 00be142c ["CALL", null, ["callee:00c5df50:8"]]
+ 00be14c8 ["INT_ADD", "register:40f0:8", ["const:be14c8:8", "const:4:8"]]
+ 00be14c8 ["CALL", null, ["callee:00c5df50:8"]]
- 00be142c bytes 95f20194
+ 00be14c8 bytes a2f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cede4403cca8515da51a66191c27658"></a>

### [`00be1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md) → [`00be17c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be17c4.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dec0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5dea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dea0.md)
- 新版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df90.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be17c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17c4) · [`00be17dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17dc) · [`00be17fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17fc)
- 新版 `00be1860`（命令位置の公開資料なし） · `00be1878`（命令位置の公開資料なし） · `00be1898`（命令位置の公開資料なし）

~~~diff
- 00be17c4 ["INT_ADD", "register:40f0:8", ["const:be17c4:8", "const:4:8"]]
- 00be17c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00be1860 ["INT_ADD", "register:40f0:8", ["const:be1860:8", "const:4:8"]]
+ 00be1860 ["CALL", null, ["callee:00c57f60:8"]]
- 00be17c4 bytes b3d90194
+ 00be1860 bytes c0d90194
- 00be17dc ["INT_ADD", "register:40f0:8", ["const:be17dc:8", "const:4:8"]]
- 00be17dc ["CALL", null, ["callee:00c5df70:8"]]
+ 00be1878 ["INT_ADD", "register:40f0:8", ["const:be1878:8", "const:4:8"]]
+ 00be1878 ["CALL", null, ["callee:00c5df70:8"]]
- 00be17dc bytes b1f10194
+ 00be1878 bytes bef10194
- 00be17fc ["INT_ADD", "register:40f0:8", ["const:be17fc:8", "const:4:8"]]
- 00be17fc ["CALL", null, ["callee:00c5df70:8"]]
+ 00be1898 ["INT_ADD", "register:40f0:8", ["const:be1898:8", "const:4:8"]]
+ 00be1898 ["CALL", null, ["callee:00c5df70:8"]]
- 00be17fc bytes a9f10194
+ 00be1898 bytes b6f10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafd29b42fb4b0acc1bb54dc286f75cc"></a>

### [`00be18d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md) → [`00be1974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1974.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be18f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be18f8) · [`00be1904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be1904) · [`00be1910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be1910)
- 新版 `00be1994`（命令位置の公開資料なし） · `00be19a0`（命令位置の公開資料なし） · `00be19ac`（命令位置の公開資料なし）

~~~diff
- 00be18f8 ["INT_ADD", "register:40f0:8", ["const:be18f8:8", "const:4:8"]]
- 00be18f8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1994 ["INT_ADD", "register:40f0:8", ["const:be1994:8", "const:4:8"]]
+ 00be1994 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be18f8 bytes 42e40194
+ 00be1994 bytes 4fe40194
- 00be1904 ["INT_ADD", "register:40f0:8", ["const:be1904:8", "const:4:8"]]
- 00be1904 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be19a0 ["INT_ADD", "register:40f0:8", ["const:be19a0:8", "const:4:8"]]
+ 00be19a0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1904 bytes 43e40194
+ 00be19a0 bytes 50e40194
- 00be1910 ["INT_ADD", "register:40f0:8", ["const:be1910:8", "const:4:8"]]
- 00be1910 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be19ac ["INT_ADD", "register:40f0:8", ["const:be19ac:8", "const:4:8"]]
+ 00be19ac ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1910 bytes d8e40194
+ 00be19ac bytes e5e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-176c77b8f034e0c50bd809d66fa4d89f"></a>

### [`00be1968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md) → [`00be1a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a04.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be1988) · [`00be1994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be1994) · [`00be19a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be19a0)
- 新版 `00be1a24`（命令位置の公開資料なし） · `00be1a30`（命令位置の公開資料なし） · `00be1a3c`（命令位置の公開資料なし）

~~~diff
- 00be1988 ["INT_ADD", "register:40f0:8", ["const:be1988:8", "const:4:8"]]
- 00be1988 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1a24 ["INT_ADD", "register:40f0:8", ["const:be1a24:8", "const:4:8"]]
+ 00be1a24 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1988 bytes 1ee40194
+ 00be1a24 bytes 2be40194
- 00be1994 ["INT_ADD", "register:40f0:8", ["const:be1994:8", "const:4:8"]]
- 00be1994 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1a30 ["INT_ADD", "register:40f0:8", ["const:be1a30:8", "const:4:8"]]
+ 00be1a30 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1994 bytes 1fe40194
+ 00be1a30 bytes 2ce40194
- 00be19a0 ["INT_ADD", "register:40f0:8", ["const:be19a0:8", "const:4:8"]]
- 00be19a0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1a3c ["INT_ADD", "register:40f0:8", ["const:be1a3c:8", "const:4:8"]]
+ 00be1a3c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be19a0 bytes b4e40194
+ 00be1a3c bytes c1e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5585d912bb19f11a24cec916dc98e44b"></a>

### [`00be19f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md) → [`00be1a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a94.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a18) · [`00be1a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a24) · [`00be1a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a30)
- 新版 `00be1ab4`（命令位置の公開資料なし） · `00be1ac0`（命令位置の公開資料なし） · `00be1acc`（命令位置の公開資料なし）

~~~diff
- 00be1a18 ["INT_ADD", "register:40f0:8", ["const:be1a18:8", "const:4:8"]]
- 00be1a18 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1ab4 ["INT_ADD", "register:40f0:8", ["const:be1ab4:8", "const:4:8"]]
+ 00be1ab4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1a18 bytes fae30194
+ 00be1ab4 bytes 07e40194
- 00be1a24 ["INT_ADD", "register:40f0:8", ["const:be1a24:8", "const:4:8"]]
- 00be1a24 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1ac0 ["INT_ADD", "register:40f0:8", ["const:be1ac0:8", "const:4:8"]]
+ 00be1ac0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1a24 bytes fbe30194
+ 00be1ac0 bytes 08e40194
- 00be1a30 ["INT_ADD", "register:40f0:8", ["const:be1a30:8", "const:4:8"]]
- 00be1a30 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1acc ["INT_ADD", "register:40f0:8", ["const:be1acc:8", "const:4:8"]]
+ 00be1acc ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1a30 bytes 90e40194
+ 00be1acc bytes 9de40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e39eb45c6e5ae7169d895c23cffd710"></a>

### [`00be1a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md) → [`00be1b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1b24.md) _ZNK8firebase4auth4User24ReauthenticateLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1aa8) · [`00be1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1ab4) · [`00be1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1ac0)
- 新版 `00be1b44`（命令位置の公開資料なし） · `00be1b50`（命令位置の公開資料なし） · `00be1b5c`（命令位置の公開資料なし）

~~~diff
- 00be1aa8 ["INT_ADD", "register:40f0:8", ["const:be1aa8:8", "const:4:8"]]
- 00be1aa8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1b44 ["INT_ADD", "register:40f0:8", ["const:be1b44:8", "const:4:8"]]
+ 00be1b44 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1aa8 bytes d6e30194
+ 00be1b44 bytes e3e30194
- 00be1ab4 ["INT_ADD", "register:40f0:8", ["const:be1ab4:8", "const:4:8"]]
- 00be1ab4 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1b50 ["INT_ADD", "register:40f0:8", ["const:be1b50:8", "const:4:8"]]
+ 00be1b50 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1ab4 bytes d7e30194
+ 00be1b50 bytes e4e30194
- 00be1ac0 ["INT_ADD", "register:40f0:8", ["const:be1ac0:8", "const:4:8"]]
- 00be1ac0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1b5c ["INT_ADD", "register:40f0:8", ["const:be1b5c:8", "const:4:8"]]
+ 00be1b5c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1ac0 bytes 6ce40194
+ 00be1b5c bytes 79e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a60591e88a8f1bc175b8a6f9024de9aa"></a>

### [`00be1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md) → [`00be1bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1bb4.md) _ZNK8firebase4auth4User39ReauthenticateAndRetrieveDataLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b38) · [`00be1b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b44) · [`00be1b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b50)
- 新版 `00be1bd4`（命令位置の公開資料なし） · `00be1be0`（命令位置の公開資料なし） · `00be1bec`（命令位置の公開資料なし）

~~~diff
- 00be1b38 ["INT_ADD", "register:40f0:8", ["const:be1b38:8", "const:4:8"]]
- 00be1b38 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1bd4 ["INT_ADD", "register:40f0:8", ["const:be1bd4:8", "const:4:8"]]
+ 00be1bd4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1b38 bytes b2e30194
+ 00be1bd4 bytes bfe30194
- 00be1b44 ["INT_ADD", "register:40f0:8", ["const:be1b44:8", "const:4:8"]]
- 00be1b44 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1be0 ["INT_ADD", "register:40f0:8", ["const:be1be0:8", "const:4:8"]]
+ 00be1be0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1b44 bytes b3e30194
+ 00be1be0 bytes c0e30194
- 00be1b50 ["INT_ADD", "register:40f0:8", ["const:be1b50:8", "const:4:8"]]
- 00be1b50 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1bec ["INT_ADD", "register:40f0:8", ["const:be1bec:8", "const:4:8"]]
+ 00be1bec ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1b50 bytes 48e40194
+ 00be1bec bytes 55e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c3c0f198f8549170ed0daf3594eee39"></a>

### [`00be1ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md) → [`00be1c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1c44.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1bc8) · [`00be1bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1bd4) · [`00be1be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1be0)
- 新版 `00be1c64`（命令位置の公開資料なし） · `00be1c70`（命令位置の公開資料なし） · `00be1c7c`（命令位置の公開資料なし）

~~~diff
- 00be1bc8 ["INT_ADD", "register:40f0:8", ["const:be1bc8:8", "const:4:8"]]
- 00be1bc8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1c64 ["INT_ADD", "register:40f0:8", ["const:be1c64:8", "const:4:8"]]
+ 00be1c64 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1bc8 bytes 8ee30194
+ 00be1c64 bytes 9be30194
- 00be1bd4 ["INT_ADD", "register:40f0:8", ["const:be1bd4:8", "const:4:8"]]
- 00be1bd4 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1c70 ["INT_ADD", "register:40f0:8", ["const:be1c70:8", "const:4:8"]]
+ 00be1c70 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1bd4 bytes 8fe30194
+ 00be1c70 bytes 9ce30194
- 00be1be0 ["INT_ADD", "register:40f0:8", ["const:be1be0:8", "const:4:8"]]
- 00be1be0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1c7c ["INT_ADD", "register:40f0:8", ["const:be1c7c:8", "const:4:8"]]
+ 00be1c7c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1be0 bytes 24e40194
+ 00be1c7c bytes 31e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22f9b390c32681ec35f73929db2a8395"></a>

### [`00be1c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md) → [`00be1cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1cd4.md) _ZNK8firebase4auth4User50SendEmailVerificationBeforeUpdatingEmailLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c58) · [`00be1c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c64) · [`00be1c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c70)
- 新版 `00be1cf4`（命令位置の公開資料なし） · `00be1d00`（命令位置の公開資料なし） · `00be1d0c`（命令位置の公開資料なし）

~~~diff
- 00be1c58 ["INT_ADD", "register:40f0:8", ["const:be1c58:8", "const:4:8"]]
- 00be1c58 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1cf4 ["INT_ADD", "register:40f0:8", ["const:be1cf4:8", "const:4:8"]]
+ 00be1cf4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1c58 bytes 6ae30194
+ 00be1cf4 bytes 77e30194
- 00be1c64 ["INT_ADD", "register:40f0:8", ["const:be1c64:8", "const:4:8"]]
- 00be1c64 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1d00 ["INT_ADD", "register:40f0:8", ["const:be1d00:8", "const:4:8"]]
+ 00be1d00 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1c64 bytes 6be30194
+ 00be1d00 bytes 78e30194
- 00be1c70 ["INT_ADD", "register:40f0:8", ["const:be1c70:8", "const:4:8"]]
- 00be1c70 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1d0c ["INT_ADD", "register:40f0:8", ["const:be1d0c:8", "const:4:8"]]
+ 00be1d0c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1c70 bytes 00e40194
+ 00be1d0c bytes 0de40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b851da1b1aef304a181edb15c24c14"></a>

### [`00be1cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md) → [`00be1d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1d64.md) _ZNK8firebase4auth4User16UnlinkLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1ce8) · [`00be1cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1cf4) · [`00be1d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1d00)
- 新版 `00be1d84`（命令位置の公開資料なし） · `00be1d90`（命令位置の公開資料なし） · `00be1d9c`（命令位置の公開資料なし）

~~~diff
- 00be1ce8 ["INT_ADD", "register:40f0:8", ["const:be1ce8:8", "const:4:8"]]
- 00be1ce8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1d84 ["INT_ADD", "register:40f0:8", ["const:be1d84:8", "const:4:8"]]
+ 00be1d84 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1ce8 bytes 46e30194
+ 00be1d84 bytes 53e30194
- 00be1cf4 ["INT_ADD", "register:40f0:8", ["const:be1cf4:8", "const:4:8"]]
- 00be1cf4 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1d90 ["INT_ADD", "register:40f0:8", ["const:be1d90:8", "const:4:8"]]
+ 00be1d90 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1cf4 bytes 47e30194
+ 00be1d90 bytes 54e30194
- 00be1d00 ["INT_ADD", "register:40f0:8", ["const:be1d00:8", "const:4:8"]]
- 00be1d00 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1d9c ["INT_ADD", "register:40f0:8", ["const:be1d9c:8", "const:4:8"]]
+ 00be1d9c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1d00 bytes dce30194
+ 00be1d9c bytes e9e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5377c9a6fb1ee08d996d790cec5e3e5d"></a>

### [`00be1d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md) → [`00be1df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1df4.md) _ZNK8firebase4auth4User27UpdateUserProfileLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d78) · [`00be1d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d84) · [`00be1d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d90)
- 新版 `00be1e14`（命令位置の公開資料なし） · `00be1e20`（命令位置の公開資料なし） · `00be1e2c`（命令位置の公開資料なし）

~~~diff
- 00be1d78 ["INT_ADD", "register:40f0:8", ["const:be1d78:8", "const:4:8"]]
- 00be1d78 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1e14 ["INT_ADD", "register:40f0:8", ["const:be1e14:8", "const:4:8"]]
+ 00be1e14 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1d78 bytes 22e30194
+ 00be1e14 bytes 2fe30194
- 00be1d84 ["INT_ADD", "register:40f0:8", ["const:be1d84:8", "const:4:8"]]
- 00be1d84 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1e20 ["INT_ADD", "register:40f0:8", ["const:be1e20:8", "const:4:8"]]
+ 00be1e20 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1d84 bytes 23e30194
+ 00be1e20 bytes 30e30194
- 00be1d90 ["INT_ADD", "register:40f0:8", ["const:be1d90:8", "const:4:8"]]
- 00be1d90 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1e2c ["INT_ADD", "register:40f0:8", ["const:be1e2c:8", "const:4:8"]]
+ 00be1e2c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1d90 bytes b8e30194
+ 00be1e2c bytes c5e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580f7a804705319a4f33ba29216a640d"></a>

### [`00be1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md) → [`00be1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1e84.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e08) · [`00be1e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e14) · [`00be1e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e20)
- 新版 `00be1ea4`（命令位置の公開資料なし） · `00be1eb0`（命令位置の公開資料なし） · `00be1ebc`（命令位置の公開資料なし）

~~~diff
- 00be1e08 ["INT_ADD", "register:40f0:8", ["const:be1e08:8", "const:4:8"]]
- 00be1e08 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1ea4 ["INT_ADD", "register:40f0:8", ["const:be1ea4:8", "const:4:8"]]
+ 00be1ea4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1e08 bytes fee20194
+ 00be1ea4 bytes 0be30194
- 00be1e14 ["INT_ADD", "register:40f0:8", ["const:be1e14:8", "const:4:8"]]
- 00be1e14 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1eb0 ["INT_ADD", "register:40f0:8", ["const:be1eb0:8", "const:4:8"]]
+ 00be1eb0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1e14 bytes ffe20194
+ 00be1eb0 bytes 0ce30194
- 00be1e20 ["INT_ADD", "register:40f0:8", ["const:be1e20:8", "const:4:8"]]
- 00be1e20 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1ebc ["INT_ADD", "register:40f0:8", ["const:be1ebc:8", "const:4:8"]]
+ 00be1ebc ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1e20 bytes 94e30194
+ 00be1ebc bytes a1e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1376e4e997d3c9c12be21f87839d6c64"></a>

### [`00be1e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md) → [`00be1f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1f14.md) _ZNK8firebase4auth4User16DeleteLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1e98) · [`00be1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1ea4) · [`00be1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1eb0)
- 新版 `00be1f34`（命令位置の公開資料なし） · `00be1f40`（命令位置の公開資料なし） · `00be1f4c`（命令位置の公開資料なし）

~~~diff
- 00be1e98 ["INT_ADD", "register:40f0:8", ["const:be1e98:8", "const:4:8"]]
- 00be1e98 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1f34 ["INT_ADD", "register:40f0:8", ["const:be1f34:8", "const:4:8"]]
+ 00be1f34 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1e98 bytes dae20194
+ 00be1f34 bytes e7e20194
- 00be1ea4 ["INT_ADD", "register:40f0:8", ["const:be1ea4:8", "const:4:8"]]
- 00be1ea4 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1f40 ["INT_ADD", "register:40f0:8", ["const:be1f40:8", "const:4:8"]]
+ 00be1f40 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1ea4 bytes dbe20194
+ 00be1f40 bytes e8e20194
- 00be1eb0 ["INT_ADD", "register:40f0:8", ["const:be1eb0:8", "const:4:8"]]
- 00be1eb0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1f4c ["INT_ADD", "register:40f0:8", ["const:be1f4c:8", "const:4:8"]]
+ 00be1f4c ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1eb0 bytes 70e30194
+ 00be1f4c bytes 7de30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

