# v15.7.2 → v15.7.3 · 要調査の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-7200b3f05cc2f3a6f8d650540dea3dcb"></a>

### [`00b96470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96470.md) → [`00b96538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96538.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd820.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b964a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96470.md#insn-00b964a8)
- 新版 [`00b96570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96538.md#insn-00b96570)

~~~diff
- 00b964a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b964a8 ["INT_ADD", "register:40f0:8", ["const:b964a8:8", "const:4:8"]]
- 00b964a8 ["CALLIND", null, ["register:0:8"]]
+ 00b96570 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b96570 ["INT_ADD", "register:40f0:8", ["const:b96570:8", "const:4:8"]]
+ 00b96570 ["CALLIND", null, ["register:0:8"]]
- 00b964a8 bytes 00013fd6
+ 00b96570 bytes 00013fd6
~~~


<a id="compare-cf4597325d424cefc3a7dffc769bce09"></a>

### [`00b96654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96654.md) → [`00b9671c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ab9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96654.md#insn-00b96688) · [`00b966ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96654.md#insn-00b966ac)
- 新版 [`00b96750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md#insn-00b96750) · [`00b96774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md#insn-00b96774)

~~~diff
- 00b96688 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b96688 ["INT_ADD", "register:40f0:8", ["const:b96688:8", "const:4:8"]]
- 00b96688 ["CALLIND", null, ["register:0:8"]]
+ 00b96750 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b96750 ["INT_ADD", "register:40f0:8", ["const:b96750:8", "const:4:8"]]
+ 00b96750 ["CALLIND", null, ["register:0:8"]]
- 00b96688 bytes 00013fd6
+ 00b96750 bytes 00013fd6
- 00b966ac ["INT_ADD", "register:40f0:8", ["const:b966ac:8", "const:4:8"]]
- 00b966ac ["CALL", null, ["callee:00b8ac64:8"]]
+ 00b96774 ["INT_ADD", "register:40f0:8", ["const:b96774:8", "const:4:8"]]
+ 00b96774 ["CALL", null, ["callee:00b8ac64:8"]]
- 00b966ac bytes 3cd1ff97
+ 00b96774 bytes 3cd1ff97
~~~


<a id="compare-413faf8c6cae7623c9f9e6fe7ee52cc0"></a>

### [`00b96860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96860.md) → [`00b96928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ab9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96860.md#insn-00b96894) · [`00b968b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96860.md#insn-00b968b8)
- 新版 [`00b9695c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md#insn-00b9695c) · [`00b96980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md#insn-00b96980)

~~~diff
- 00b96894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b96894 ["INT_ADD", "register:40f0:8", ["const:b96894:8", "const:4:8"]]
- 00b96894 ["CALLIND", null, ["register:0:8"]]
+ 00b9695c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9695c ["INT_ADD", "register:40f0:8", ["const:b9695c:8", "const:4:8"]]
+ 00b9695c ["CALLIND", null, ["register:0:8"]]
- 00b96894 bytes 00013fd6
+ 00b9695c bytes 00013fd6
- 00b968b8 ["INT_ADD", "register:40f0:8", ["const:b968b8:8", "const:4:8"]]
- 00b968b8 ["CALL", null, ["callee:00b8ac64:8"]]
+ 00b96980 ["INT_ADD", "register:40f0:8", ["const:b96980:8", "const:4:8"]]
+ 00b96980 ["CALL", null, ["callee:00b8ac64:8"]]
- 00b968b8 bytes b9d0ff97
+ 00b96980 bytes b9d0ff97
~~~


<a id="compare-b915fcca16bdc573c6917fb588b71ee6"></a>

### [`00b96a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96a30.md) → [`00b96af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96a30.md#insn-00b96a5c)
- 新版 [`00b96b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md#insn-00b96b24)

~~~diff
- 00b96a5c ["INT_ADD", "register:40f0:8", ["const:b96a5c:8", "const:4:8"]]
- 00b96a5c ["CALL", null, ["callee:00b979f8:8"]]
+ 00b96b24 ["INT_ADD", "register:40f0:8", ["const:b96b24:8", "const:4:8"]]
+ 00b96b24 ["CALL", null, ["callee:00b979f8:8"]]
- 00b96a5c bytes b5030094
+ 00b96b24 bytes b5030094
~~~


<a id="compare-1fd603ce651f18412f9978f5fa6814be"></a>

### [`00b97118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97118.md) → [`00b971e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97118.md#insn-00b97144)
- 新版 [`00b9720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md#insn-00b9720c)

~~~diff
- 00b97144 ["INT_ADD", "register:40f0:8", ["const:b97144:8", "const:4:8"]]
- 00b97144 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b9720c ["INT_ADD", "register:40f0:8", ["const:b9720c:8", "const:4:8"]]
+ 00b9720c ["CALL", null, ["callee:00b979f8:8"]]
- 00b97144 bytes fb010094
+ 00b9720c bytes fb010094
~~~


<a id="compare-05d3239ca9eef37af826c294aac21b3e"></a>

### [`00b9717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9717c.md) → [`00b97244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b971a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9717c.md#insn-00b971a8)
- 新版 [`00b97270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md#insn-00b97270)

~~~diff
- 00b971a8 ["INT_ADD", "register:40f0:8", ["const:b971a8:8", "const:4:8"]]
- 00b971a8 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b97270 ["INT_ADD", "register:40f0:8", ["const:b97270:8", "const:4:8"]]
+ 00b97270 ["CALL", null, ["callee:00b979f8:8"]]
- 00b971a8 bytes e2010094
+ 00b97270 bytes e2010094
~~~


<a id="compare-339fd3c09fd49e291d48b8157bed9766"></a>

### [`00b971dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b971dc.md) → [`00b972a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b972a4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b971dc.md#insn-00b97208)
- 新版 [`00b972d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b972a4.md#insn-00b972d0)

~~~diff
- 00b97208 ["INT_ADD", "register:40f0:8", ["const:b97208:8", "const:4:8"]]
- 00b97208 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b972d0 ["INT_ADD", "register:40f0:8", ["const:b972d0:8", "const:4:8"]]
+ 00b972d0 ["CALL", null, ["callee:00b979f8:8"]]
- 00b97208 bytes ca010094
+ 00b972d0 bytes ca010094
~~~


<a id="compare-823a22cfd4c2834bf1beba7482f67715"></a>

### [`00b97240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97240.md) → [`00b97308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97308.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9726c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97240.md#insn-00b9726c)
- 新版 [`00b97334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97308.md#insn-00b97334)

~~~diff
- 00b9726c ["INT_ADD", "register:40f0:8", ["const:b9726c:8", "const:4:8"]]
- 00b9726c ["CALL", null, ["callee:00b979f8:8"]]
+ 00b97334 ["INT_ADD", "register:40f0:8", ["const:b97334:8", "const:4:8"]]
+ 00b97334 ["CALL", null, ["callee:00b979f8:8"]]
- 00b9726c bytes b1010094
+ 00b97334 bytes b1010094
~~~


<a id="compare-c4340f062db69bb4e0c646f933e1fa53"></a>

### [`00b972a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b972a0.md) → [`00b97368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97368.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b972cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b972a0.md#insn-00b972cc)
- 新版 [`00b97394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97368.md#insn-00b97394)

~~~diff
- 00b972cc ["INT_ADD", "register:40f0:8", ["const:b972cc:8", "const:4:8"]]
- 00b972cc ["CALL", null, ["callee:00b979f8:8"]]
+ 00b97394 ["INT_ADD", "register:40f0:8", ["const:b97394:8", "const:4:8"]]
+ 00b97394 ["CALL", null, ["callee:00b979f8:8"]]
- 00b972cc bytes 99010094
+ 00b97394 bytes 99010094
~~~


<a id="compare-d40ea864e4617e2334c539bea5fd6e02"></a>

### [`00b97304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97304.md) → [`00b973cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b973cc.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97304.md#insn-00b97330)
- 新版 [`00b973f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b973cc.md#insn-00b973f8)

~~~diff
- 00b97330 ["INT_ADD", "register:40f0:8", ["const:b97330:8", "const:4:8"]]
- 00b97330 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b973f8 ["INT_ADD", "register:40f0:8", ["const:b973f8:8", "const:4:8"]]
+ 00b973f8 ["CALL", null, ["callee:00b979f8:8"]]
- 00b97330 bytes 80010094
+ 00b973f8 bytes 80010094
~~~


<a id="compare-e50ee551a8e2a78124a2f81a043ba889"></a>

### [`00b97364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97364.md) → [`00b9742c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1520.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be15d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b973c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97364.md#insn-00b973c8) · [`00b9741c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97364.md#insn-00b9741c) · [`00b9745c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97364.md#insn-00b9745c)
- 新版 [`00b97490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b97490) · [`00b974e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b974e4) · [`00b97524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b97524)

~~~diff
- 00b973c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b973c8 ["INT_ADD", "register:40f0:8", ["const:b973c8:8", "const:4:8"]]
- 00b973c8 ["CALLIND", null, ["register:0:8"]]
+ 00b97490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97490 ["INT_ADD", "register:40f0:8", ["const:b97490:8", "const:4:8"]]
+ 00b97490 ["CALLIND", null, ["register:0:8"]]
- 00b973c8 bytes 00013fd6
+ 00b97490 bytes 00013fd6
- 00b9741c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9741c ["INT_ADD", "register:40f0:8", ["const:b9741c:8", "const:4:8"]]
- 00b9741c ["CALLIND", null, ["register:0:8"]]
+ 00b974e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b974e4 ["INT_ADD", "register:40f0:8", ["const:b974e4:8", "const:4:8"]]
+ 00b974e4 ["CALLIND", null, ["register:0:8"]]
- 00b9741c bytes 00013fd6
+ 00b974e4 bytes 00013fd6
- 00b9745c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9745c ["INT_ADD", "register:40f0:8", ["const:b9745c:8", "const:4:8"]]
- 00b9745c ["CALLIND", null, ["register:0:8"]]
+ 00b97524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97524 ["INT_ADD", "register:40f0:8", ["const:b97524:8", "const:4:8"]]
+ 00b97524 ["CALLIND", null, ["register:0:8"]]
- 00b9745c bytes 00013fd6
+ 00b97524 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12487fedf2092cc340402da62672efdc"></a>

### [`00b9754c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9754c.md) → [`00b97614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ab9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9754c.md#insn-00b97580) · [`00b975e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9754c.md#insn-00b975e4)
- 新版 [`00b97648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md#insn-00b97648) · [`00b976ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md#insn-00b976ac)

~~~diff
- 00b97580 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97580 ["INT_ADD", "register:40f0:8", ["const:b97580:8", "const:4:8"]]
- 00b97580 ["CALLIND", null, ["register:0:8"]]
+ 00b97648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97648 ["INT_ADD", "register:40f0:8", ["const:b97648:8", "const:4:8"]]
+ 00b97648 ["CALLIND", null, ["register:0:8"]]
- 00b97580 bytes 00013fd6
+ 00b97648 bytes 00013fd6
- 00b975e4 ["INT_ADD", "register:40f0:8", ["const:b975e4:8", "const:4:8"]]
- 00b975e4 ["CALL", null, ["callee:00b8ac64:8"]]
+ 00b976ac ["INT_ADD", "register:40f0:8", ["const:b976ac:8", "const:4:8"]]
+ 00b976ac ["CALL", null, ["callee:00b8ac64:8"]]
- 00b975e4 bytes 6ecdff97
+ 00b976ac bytes 6ecdff97
~~~


<a id="compare-c4a626f79bacfbf5e82acd0a1dd699c9"></a>

### [`00b97634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97634.md) → [`00b976fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b976fc.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97634.md#insn-00b97660)
- 新版 [`00b97728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b976fc.md#insn-00b97728)

~~~diff
- 00b97660 ["INT_ADD", "register:40f0:8", ["const:b97660:8", "const:4:8"]]
- 00b97660 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b97728 ["INT_ADD", "register:40f0:8", ["const:b97728:8", "const:4:8"]]
+ 00b97728 ["CALL", null, ["callee:00b979f8:8"]]
- 00b97660 bytes b4000094
+ 00b97728 bytes b4000094
~~~


<a id="compare-0d523627df1e5d258077eb38c5439d6a"></a>

### [`00b97694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97694.md) → [`00b9775c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9775c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b976c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97694.md#insn-00b976c0)
- 新版 [`00b97788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9775c.md#insn-00b97788)

~~~diff
- 00b976c0 ["INT_ADD", "register:40f0:8", ["const:b976c0:8", "const:4:8"]]
- 00b976c0 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b97788 ["INT_ADD", "register:40f0:8", ["const:b97788:8", "const:4:8"]]
+ 00b97788 ["CALL", null, ["callee:00b979f8:8"]]
- 00b976c0 bytes 9c000094
+ 00b97788 bytes 9c000094
~~~


<a id="compare-3a1491157a13057b71a034c5ef8e43ac"></a>

### [`00b976f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b976f4.md) → [`00b977bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b977bc.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b976f4.md#insn-00b97720)
- 新版 [`00b977e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b977bc.md#insn-00b977e8)

~~~diff
- 00b97720 ["INT_ADD", "register:40f0:8", ["const:b97720:8", "const:4:8"]]
- 00b97720 ["CALL", null, ["callee:00b979f8:8"]]
+ 00b977e8 ["INT_ADD", "register:40f0:8", ["const:b977e8:8", "const:4:8"]]
+ 00b977e8 ["CALL", null, ["callee:00b979f8:8"]]
- 00b97720 bytes 84000094
+ 00b977e8 bytes 84000094
~~~


<a id="compare-25332d5387c5958ecf0da2c7a6e25482"></a>

### [`00b97744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97744.md) → [`00b9780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1530.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be15e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97744.md#insn-00b9779c) · [`00b977fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97744.md#insn-00b977fc) · [`00b97824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97744.md#insn-00b97824)
- 新版 [`00b97864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b97864) · [`00b978c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b978c4) · [`00b978ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b978ec)

~~~diff
- 00b9779c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9779c ["INT_ADD", "register:40f0:8", ["const:b9779c:8", "const:4:8"]]
- 00b9779c ["CALLIND", null, ["register:0:8"]]
+ 00b97864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97864 ["INT_ADD", "register:40f0:8", ["const:b97864:8", "const:4:8"]]
+ 00b97864 ["CALLIND", null, ["register:0:8"]]
- 00b9779c bytes 00013fd6
+ 00b97864 bytes 00013fd6
- 00b977fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b977fc ["INT_ADD", "register:40f0:8", ["const:b977fc:8", "const:4:8"]]
- 00b977fc ["CALLIND", null, ["register:0:8"]]
+ 00b978c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b978c4 ["INT_ADD", "register:40f0:8", ["const:b978c4:8", "const:4:8"]]
+ 00b978c4 ["CALLIND", null, ["register:0:8"]]
- 00b977fc bytes 00013fd6
+ 00b978c4 bytes 00013fd6
- 00b97824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97824 ["INT_ADD", "register:40f0:8", ["const:b97824:8", "const:4:8"]]
- 00b97824 ["CALLIND", null, ["register:0:8"]]
+ 00b978ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b978ec ["INT_ADD", "register:40f0:8", ["const:b978ec:8", "const:4:8"]]
+ 00b978ec ["CALLIND", null, ["register:0:8"]]
- 00b97824 bytes 00013fd6
+ 00b978ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3c0a0beb473eb758cf2de64f7e38287"></a>

### [`00b97930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md) → [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md) FUN_00b979f8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00b96914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96914.md) [`00b96a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96a30.md) [`00b96a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96a98.md) [`00b97118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97118.md) [`00b9717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b9717c.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00b969dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md) [`00b96af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md) [`00b96b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md) [`00b971e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md) [`00b97244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md#insn-00b97988) · [`00b979f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md#insn-00b979f4) · [`00b97a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b97/00b97930.md#insn-00b97a20)
- 新版 [`00b97a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97a50) · [`00b97abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97abc) · [`00b97ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97ae8)

~~~diff
- 00b97988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97988 ["INT_ADD", "register:40f0:8", ["const:b97988:8", "const:4:8"]]
- 00b97988 ["CALLIND", null, ["register:0:8"]]
+ 00b97a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97a50 ["INT_ADD", "register:40f0:8", ["const:b97a50:8", "const:4:8"]]
+ 00b97a50 ["CALLIND", null, ["register:0:8"]]
- 00b97988 bytes 00013fd6
+ 00b97a50 bytes 00013fd6
- 00b979f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b979f4 ["INT_ADD", "register:40f0:8", ["const:b979f4:8", "const:4:8"]]
- 00b979f4 ["CALLIND", null, ["register:0:8"]]
+ 00b97abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97abc ["INT_ADD", "register:40f0:8", ["const:b97abc:8", "const:4:8"]]
+ 00b97abc ["CALLIND", null, ["register:0:8"]]
- 00b979f4 bytes 00013fd6
+ 00b97abc bytes 00013fd6
- 00b97a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97a20 ["INT_ADD", "register:40f0:8", ["const:b97a20:8", "const:4:8"]]
- 00b97a20 ["CALLIND", null, ["register:0:8"]]
+ 00b97ae8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97ae8 ["INT_ADD", "register:40f0:8", ["const:b97ae8:8", "const:4:8"]]
+ 00b97ae8 ["CALLIND", null, ["register:0:8"]]
- 00b97a20 bytes 00013fd6
+ 00b97ae8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577d7b5d5f0466ce6c2d3ca60dc02d5d"></a>

### [`00b98174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98174.md) → [`00b9823c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9823c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1540.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b981a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98174.md#insn-00b981a0)
- 新版 [`00b98268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9823c.md#insn-00b98268)

~~~diff
- 00b981a0 ["INT_ADD", "register:40f0:8", ["const:b981a0:8", "const:4:8"]]
- 00b981a0 ["CALL", null, ["callee:00be15f0:8"]]
+ 00b98268 ["INT_ADD", "register:40f0:8", ["const:b98268:8", "const:4:8"]]
+ 00b98268 ["CALL", null, ["callee:00be15f0:8"]]
- 00b981a0 bytes e8240194
+ 00b98268 bytes e2240194
~~~


<a id="compare-4e9c06056dd4e751e24fcc35877e8f46"></a>

### [`00b981b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b981b4.md) → [`00b9827c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9827c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1540.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b981ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b981b4.md#insn-00b981ec)
- 新版 [`00b982b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9827c.md#insn-00b982b4)

~~~diff
- 00b981ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b981ec ["INT_ADD", "register:40f0:8", ["const:b981ec:8", "const:4:8"]]
- 00b981ec ["CALLIND", null, ["register:0:8"]]
+ 00b982b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b982b4 ["INT_ADD", "register:40f0:8", ["const:b982b4:8", "const:4:8"]]
+ 00b982b4 ["CALLIND", null, ["register:0:8"]]
- 00b981ec bytes 00013fd6
+ 00b982b4 bytes 00013fd6
~~~


<a id="compare-65f01b4df4e67b8cb36e96ec33a9063f"></a>

### [`00b9839c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b9839c.md) → [`00b98464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8e074.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b983d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b9839c.md#insn-00b983d0) · [`00b983f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b9839c.md#insn-00b983f4)
- 新版 [`00b98498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md#insn-00b98498) · [`00b984bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md#insn-00b984bc)

~~~diff
- 00b983d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b983d0 ["INT_ADD", "register:40f0:8", ["const:b983d0:8", "const:4:8"]]
- 00b983d0 ["CALLIND", null, ["register:0:8"]]
+ 00b98498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b98498 ["INT_ADD", "register:40f0:8", ["const:b98498:8", "const:4:8"]]
+ 00b98498 ["CALLIND", null, ["register:0:8"]]
- 00b983d0 bytes 00013fd6
+ 00b98498 bytes 00013fd6
- 00b983f4 ["INT_ADD", "register:40f0:8", ["const:b983f4:8", "const:4:8"]]
- 00b983f4 ["CALL", null, ["callee:00b8e13c:8"]]
+ 00b984bc ["INT_ADD", "register:40f0:8", ["const:b984bc:8", "const:4:8"]]
+ 00b984bc ["CALL", null, ["callee:00b8e13c:8"]]
- 00b983f4 bytes 20d7ff97
+ 00b984bc bytes 20d7ff97
~~~


<a id="compare-cfcb07abded7d1b45461e6e21c1354a3"></a>

### [`00b985a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b985a8.md) → [`00b98670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8e074.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b985dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b985a8.md#insn-00b985dc) · [`00b98600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b985a8.md#insn-00b98600)
- 新版 [`00b986a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md#insn-00b986a4) · [`00b986c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md#insn-00b986c8)

~~~diff
- 00b985dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b985dc ["INT_ADD", "register:40f0:8", ["const:b985dc:8", "const:4:8"]]
- 00b985dc ["CALLIND", null, ["register:0:8"]]
+ 00b986a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b986a4 ["INT_ADD", "register:40f0:8", ["const:b986a4:8", "const:4:8"]]
+ 00b986a4 ["CALLIND", null, ["register:0:8"]]
- 00b985dc bytes 00013fd6
+ 00b986a4 bytes 00013fd6
- 00b98600 ["INT_ADD", "register:40f0:8", ["const:b98600:8", "const:4:8"]]
- 00b98600 ["CALL", null, ["callee:00b8e13c:8"]]
+ 00b986c8 ["INT_ADD", "register:40f0:8", ["const:b986c8:8", "const:4:8"]]
+ 00b986c8 ["CALL", null, ["callee:00b8e13c:8"]]
- 00b98600 bytes 9dd6ff97
+ 00b986c8 bytes 9dd6ff97
~~~


<a id="compare-db967e08731e4538fd53697e2ac4e30e"></a>

### [`00b98778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98778.md) → [`00b98840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b987a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98778.md#insn-00b987a4)
- 新版 [`00b9886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md#insn-00b9886c)

~~~diff
- 00b987a4 ["INT_ADD", "register:40f0:8", ["const:b987a4:8", "const:4:8"]]
- 00b987a4 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b9886c ["INT_ADD", "register:40f0:8", ["const:b9886c:8", "const:4:8"]]
+ 00b9886c ["CALL", null, ["callee:00b9973c:8"]]
- 00b987a4 bytes b4030094
+ 00b9886c bytes b4030094
~~~


<a id="compare-8703e8e51105171683129561d4a219ea"></a>

### [`00b98e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98e50.md) → [`00b98f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98e50.md#insn-00b98e7c)
- 新版 [`00b98f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md#insn-00b98f44)

~~~diff
- 00b98e7c ["INT_ADD", "register:40f0:8", ["const:b98e7c:8", "const:4:8"]]
- 00b98e7c ["CALL", null, ["callee:00b9973c:8"]]
+ 00b98f44 ["INT_ADD", "register:40f0:8", ["const:b98f44:8", "const:4:8"]]
+ 00b98f44 ["CALL", null, ["callee:00b9973c:8"]]
- 00b98e7c bytes fe010094
+ 00b98f44 bytes fe010094
~~~


<a id="compare-9b572037221a279910bae2616cc1aab1"></a>

### [`00b98eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98eb4.md) → [`00b98f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98eb4.md#insn-00b98ee0)
- 新版 [`00b98fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md#insn-00b98fa8)

~~~diff
- 00b98ee0 ["INT_ADD", "register:40f0:8", ["const:b98ee0:8", "const:4:8"]]
- 00b98ee0 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b98fa8 ["INT_ADD", "register:40f0:8", ["const:b98fa8:8", "const:4:8"]]
+ 00b98fa8 ["CALL", null, ["callee:00b9973c:8"]]
- 00b98ee0 bytes e5010094
+ 00b98fa8 bytes e5010094
~~~


<a id="compare-cef54211a198f8bdfbab9d0a9924edcb"></a>

### [`00b98f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98f14.md) → [`00b98fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98fdc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98f14.md#insn-00b98f40)
- 新版 [`00b99008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98fdc.md#insn-00b99008)

~~~diff
- 00b98f40 ["INT_ADD", "register:40f0:8", ["const:b98f40:8", "const:4:8"]]
- 00b98f40 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b99008 ["INT_ADD", "register:40f0:8", ["const:b99008:8", "const:4:8"]]
+ 00b99008 ["CALL", null, ["callee:00b9973c:8"]]
- 00b98f40 bytes cd010094
+ 00b99008 bytes cd010094
~~~


<a id="compare-b36b526ea6811a3fe7c80c92ba4255ee"></a>

### [`00b98f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98f78.md) → [`00b99040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99040.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98f78.md#insn-00b98fa4)
- 新版 [`00b9906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99040.md#insn-00b9906c)

~~~diff
- 00b98fa4 ["INT_ADD", "register:40f0:8", ["const:b98fa4:8", "const:4:8"]]
- 00b98fa4 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b9906c ["INT_ADD", "register:40f0:8", ["const:b9906c:8", "const:4:8"]]
+ 00b9906c ["CALL", null, ["callee:00b9973c:8"]]
- 00b98fa4 bytes b4010094
+ 00b9906c bytes b4010094
~~~


<a id="compare-66c21e4ad94b8c97dc7c74a916d2840e"></a>

### [`00b98fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98fd8.md) → [`00b990a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b990a0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98fd8.md#insn-00b99004)
- 新版 [`00b990cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b990a0.md#insn-00b990cc)

~~~diff
- 00b99004 ["INT_ADD", "register:40f0:8", ["const:b99004:8", "const:4:8"]]
- 00b99004 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b990cc ["INT_ADD", "register:40f0:8", ["const:b990cc:8", "const:4:8"]]
+ 00b990cc ["CALL", null, ["callee:00b9973c:8"]]
- 00b99004 bytes 9c010094
+ 00b990cc bytes 9c010094
~~~


<a id="compare-308edab97a63a6c91d66d4a798fb9014"></a>

### [`00b9903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9903c.md) → [`00b99104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99104.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9903c.md#insn-00b99068)
- 新版 [`00b99130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99104.md#insn-00b99130)

~~~diff
- 00b99068 ["INT_ADD", "register:40f0:8", ["const:b99068:8", "const:4:8"]]
- 00b99068 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b99130 ["INT_ADD", "register:40f0:8", ["const:b99130:8", "const:4:8"]]
+ 00b99130 ["CALL", null, ["callee:00b9973c:8"]]
- 00b99068 bytes 83010094
+ 00b99130 bytes 83010094
~~~


<a id="compare-5a75d4688a64f03d03caeab393f228b2"></a>

### [`00b9909c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9909c.md) → [`00b99164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1550.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1600.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9909c.md#insn-00b99118) · [`00b99154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9909c.md#insn-00b99154) · [`00b99194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9909c.md#insn-00b99194)
- 新版 [`00b991e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b991e0) · [`00b9921c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b9921c) · [`00b9925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b9925c)

~~~diff
- 00b99118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99118 ["INT_ADD", "register:40f0:8", ["const:b99118:8", "const:4:8"]]
- 00b99118 ["CALLIND", null, ["register:0:8"]]
+ 00b991e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b991e0 ["INT_ADD", "register:40f0:8", ["const:b991e0:8", "const:4:8"]]
+ 00b991e0 ["CALLIND", null, ["register:0:8"]]
- 00b99118 bytes 00013fd6
+ 00b991e0 bytes 00013fd6
- 00b99154 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99154 ["INT_ADD", "register:40f0:8", ["const:b99154:8", "const:4:8"]]
- 00b99154 ["CALLIND", null, ["register:0:8"]]
+ 00b9921c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9921c ["INT_ADD", "register:40f0:8", ["const:b9921c:8", "const:4:8"]]
+ 00b9921c ["CALLIND", null, ["register:0:8"]]
- 00b99154 bytes 00013fd6
+ 00b9921c bytes 00013fd6
- 00b99194 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99194 ["INT_ADD", "register:40f0:8", ["const:b99194:8", "const:4:8"]]
- 00b99194 ["CALLIND", null, ["register:0:8"]]
+ 00b9925c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9925c ["INT_ADD", "register:40f0:8", ["const:b9925c:8", "const:4:8"]]
+ 00b9925c ["CALLIND", null, ["register:0:8"]]
- 00b99194 bytes 00013fd6
+ 00b9925c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc160c30b3d4903da477d5dddaed713f"></a>

### [`00b9928c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9928c.md) → [`00b99354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8e074.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b992c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9928c.md#insn-00b992c0) · [`00b99324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b9928c.md#insn-00b99324)
- 新版 [`00b99388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md#insn-00b99388) · [`00b993ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md#insn-00b993ec)

~~~diff
- 00b992c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b992c0 ["INT_ADD", "register:40f0:8", ["const:b992c0:8", "const:4:8"]]
- 00b992c0 ["CALLIND", null, ["register:0:8"]]
+ 00b99388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99388 ["INT_ADD", "register:40f0:8", ["const:b99388:8", "const:4:8"]]
+ 00b99388 ["CALLIND", null, ["register:0:8"]]
- 00b992c0 bytes 00013fd6
+ 00b99388 bytes 00013fd6
- 00b99324 ["INT_ADD", "register:40f0:8", ["const:b99324:8", "const:4:8"]]
- 00b99324 ["CALL", null, ["callee:00b8e13c:8"]]
+ 00b993ec ["INT_ADD", "register:40f0:8", ["const:b993ec:8", "const:4:8"]]
+ 00b993ec ["CALL", null, ["callee:00b8e13c:8"]]
- 00b99324 bytes 54d3ff97
+ 00b993ec bytes 54d3ff97
~~~


<a id="compare-d883b854c42975c26c6739b40dcad618"></a>

### [`00b99374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99374.md) → [`00b9943c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9943c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b993a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99374.md#insn-00b993a0)
- 新版 [`00b99468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9943c.md#insn-00b99468)

~~~diff
- 00b993a0 ["INT_ADD", "register:40f0:8", ["const:b993a0:8", "const:4:8"]]
- 00b993a0 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b99468 ["INT_ADD", "register:40f0:8", ["const:b99468:8", "const:4:8"]]
+ 00b99468 ["CALL", null, ["callee:00b9973c:8"]]
- 00b993a0 bytes b5000094
+ 00b99468 bytes b5000094
~~~


<a id="compare-c20e36baf1d685f1481a5f31ec8eac25"></a>

### [`00b993d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b993d4.md) → [`00b9949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9949c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b993d4.md#insn-00b99400)
- 新版 [`00b994c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9949c.md#insn-00b994c8)

~~~diff
- 00b99400 ["INT_ADD", "register:40f0:8", ["const:b99400:8", "const:4:8"]]
- 00b99400 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b994c8 ["INT_ADD", "register:40f0:8", ["const:b994c8:8", "const:4:8"]]
+ 00b994c8 ["CALL", null, ["callee:00b9973c:8"]]
- 00b99400 bytes 9d000094
+ 00b994c8 bytes 9d000094
~~~


<a id="compare-fbee8d3063eb1d41037f04d84fc8aa4d"></a>

### [`00b99434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99434.md) → [`00b994fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b994fc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99434.md#insn-00b99460)
- 新版 [`00b99528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b994fc.md#insn-00b99528)

~~~diff
- 00b99460 ["INT_ADD", "register:40f0:8", ["const:b99460:8", "const:4:8"]]
- 00b99460 ["CALL", null, ["callee:00b9973c:8"]]
+ 00b99528 ["INT_ADD", "register:40f0:8", ["const:b99528:8", "const:4:8"]]
+ 00b99528 ["CALL", null, ["callee:00b9973c:8"]]
- 00b99460 bytes 85000094
+ 00b99528 bytes 85000094
~~~


<a id="compare-40b047f072320f24ec47bab61e881ba8"></a>

### [`00b99484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99484.md) → [`00b9954c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1560.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1610.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b994f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99484.md#insn-00b994f0) · [`00b99528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99484.md#insn-00b99528) · [`00b99568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99484.md#insn-00b99568)
- 新版 [`00b995b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b995b8) · [`00b995f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b995f0) · [`00b99630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b99630)

~~~diff
- 00b994f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b994f0 ["INT_ADD", "register:40f0:8", ["const:b994f0:8", "const:4:8"]]
- 00b994f0 ["CALLIND", null, ["register:0:8"]]
+ 00b995b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b995b8 ["INT_ADD", "register:40f0:8", ["const:b995b8:8", "const:4:8"]]
+ 00b995b8 ["CALLIND", null, ["register:0:8"]]
- 00b994f0 bytes 00013fd6
+ 00b995b8 bytes 00013fd6
- 00b99528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99528 ["INT_ADD", "register:40f0:8", ["const:b99528:8", "const:4:8"]]
- 00b99528 ["CALLIND", null, ["register:0:8"]]
+ 00b995f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b995f0 ["INT_ADD", "register:40f0:8", ["const:b995f0:8", "const:4:8"]]
+ 00b995f0 ["CALLIND", null, ["register:0:8"]]
- 00b99528 bytes 00013fd6
+ 00b995f0 bytes 00013fd6
- 00b99568 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99568 ["INT_ADD", "register:40f0:8", ["const:b99568:8", "const:4:8"]]
- 00b99568 ["CALLIND", null, ["register:0:8"]]
+ 00b99630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99630 ["INT_ADD", "register:40f0:8", ["const:b99630:8", "const:4:8"]]
+ 00b99630 ["CALLIND", null, ["register:0:8"]]
- 00b99568 bytes 00013fd6
+ 00b99630 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94bda0a043c9ecc8b4c75431d84f3cad"></a>

### [`00b99674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md) → [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md) FUN_00b9973c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00b9865c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b9865c.md) [`00b98778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98778.md) [`00b987e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b987e0.md) [`00b98e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98e50.md) [`00b98eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b98/00b98eb4.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00b98724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md) [`00b98840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md) [`00b988a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md) [`00b98f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md) [`00b98f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b996e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md#insn-00b996e8) · [`00b99720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md#insn-00b99720) · [`00b99764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99674.md#insn-00b99764)
- 新版 [`00b997b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b997b0) · [`00b997e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b997e8) · [`00b9982c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b9982c)

~~~diff
- 00b996e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b996e8 ["INT_ADD", "register:40f0:8", ["const:b996e8:8", "const:4:8"]]
- 00b996e8 ["CALLIND", null, ["register:0:8"]]
+ 00b997b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b997b0 ["INT_ADD", "register:40f0:8", ["const:b997b0:8", "const:4:8"]]
+ 00b997b0 ["CALLIND", null, ["register:0:8"]]
- 00b996e8 bytes 00013fd6
+ 00b997b0 bytes 00013fd6
- 00b99720 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99720 ["INT_ADD", "register:40f0:8", ["const:b99720:8", "const:4:8"]]
- 00b99720 ["CALLIND", null, ["register:0:8"]]
+ 00b997e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b997e8 ["INT_ADD", "register:40f0:8", ["const:b997e8:8", "const:4:8"]]
+ 00b997e8 ["CALLIND", null, ["register:0:8"]]
- 00b99720 bytes 00013fd6
+ 00b997e8 bytes 00013fd6
- 00b99764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99764 ["INT_ADD", "register:40f0:8", ["const:b99764:8", "const:4:8"]]
- 00b99764 ["CALLIND", null, ["register:0:8"]]
+ 00b9982c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9982c ["INT_ADD", "register:40f0:8", ["const:b9982c:8", "const:4:8"]]
+ 00b9982c ["CALLIND", null, ["register:0:8"]]
- 00b99764 bytes 00013fd6
+ 00b9982c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d37bbc59f0a517c39ad0412fbc9402d7"></a>

### [`00b99c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99c70.md) → [`00b99d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPK2tmcc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1570.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99c70.md#insn-00b99cc4) · [`00b99ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99c70.md#insn-00b99ce4)
- 新版 [`00b99d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md#insn-00b99d8c) · [`00b99dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md#insn-00b99dac)

~~~diff
- 00b99cc4 ["INT_ADD", "register:40f0:8", ["const:b99cc4:8", "const:4:8"]]
- 00b99cc4 ["CALL", null, ["callee:00be1620:8"]]
+ 00b99d8c ["INT_ADD", "register:40f0:8", ["const:b99d8c:8", "const:4:8"]]
+ 00b99d8c ["CALL", null, ["callee:00be1620:8"]]
- 00b99cc4 bytes 2b1e0194
+ 00b99d8c bytes 251e0194
- 00b99ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99ce4 ["INT_ADD", "register:40f0:8", ["const:b99ce4:8", "const:4:8"]]
- 00b99ce4 ["CALLIND", null, ["register:0:8"]]
+ 00b99dac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99dac ["INT_ADD", "register:40f0:8", ["const:b99dac:8", "const:4:8"]]
+ 00b99dac ["CALLIND", null, ["register:0:8"]]
- 00b99ce4 bytes 00013fd6
+ 00b99dac bytes 00013fd6
~~~


<a id="compare-210629eadd79261b3633f8af769cf879"></a>

### [`00b99d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99d3c.md) → [`00b99e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e04.md) _ZNKSt6__ndk110__time_put8__do_putEPcRS1_PK2tmcc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1570.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b99/00b99d3c.md#insn-00b99d90)
- 新版 [`00b99e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e04.md#insn-00b99e58)

~~~diff
- 00b99d90 ["INT_ADD", "register:40f0:8", ["const:b99d90:8", "const:4:8"]]
- 00b99d90 ["CALL", null, ["callee:00be1620:8"]]
+ 00b99e58 ["INT_ADD", "register:40f0:8", ["const:b99e58:8", "const:4:8"]]
+ 00b99e58 ["CALL", null, ["callee:00be1620:8"]]
- 00b99d90 bytes f81d0194
+ 00b99e58 bytes f21d0194
~~~


<a id="compare-06c546dfb5a9688946f1715854236a09"></a>

### [`00b9a060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a060.md) → [`00b9a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPK2tmcc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a060.md#insn-00b9a0a0) · [`00b9a0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a060.md#insn-00b9a0f4)
- 新版 [`00b9a168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md#insn-00b9a168) · [`00b9a1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md#insn-00b9a1bc)

~~~diff
- 00b9a0a0 ["INT_ADD", "register:40f0:8", ["const:b9a0a0:8", "const:4:8"]]
- 00b9a0a0 ["CALL", null, ["callee:00be1630:8"]]
+ 00b9a168 ["INT_ADD", "register:40f0:8", ["const:b9a168:8", "const:4:8"]]
+ 00b9a168 ["CALL", null, ["callee:00be1630:8"]]
- 00b9a0a0 bytes 381d0194
+ 00b9a168 bytes 321d0194
- 00b9a0f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9a0f4 ["INT_ADD", "register:40f0:8", ["const:b9a0f4:8", "const:4:8"]]
- 00b9a0f4 ["CALLIND", null, ["register:0:8"]]
+ 00b9a1bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a1bc ["INT_ADD", "register:40f0:8", ["const:b9a1bc:8", "const:4:8"]]
+ 00b9a1bc ["CALLIND", null, ["register:0:8"]]
- 00b9a0f4 bytes 00013fd6
+ 00b9a1bc bytes 00013fd6
~~~


<a id="compare-0ee73282d6cd6435dbc39daaa079bf37"></a>

### [`00b9a11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a11c.md) → [`00b9a1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1580.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1570.md) [`00be1590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1590.md)
- 新版 呼出元 1件 [`00be1630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1630.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md) [`00be1640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a11c.md#insn-00b9a17c) · [`00b9a194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a11c.md#insn-00b9a194) · [`00b9a1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9a/00b9a11c.md#insn-00b9a1b0)
- 新版 [`00b9a244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a244) · [`00b9a25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a25c) · [`00b9a278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a278)

~~~diff
- 00b9a17c ["INT_ADD", "register:40f0:8", ["const:b9a17c:8", "const:4:8"]]
- 00b9a17c ["CALL", null, ["callee:00be1620:8"]]
+ 00b9a244 ["INT_ADD", "register:40f0:8", ["const:b9a244:8", "const:4:8"]]
+ 00b9a244 ["CALL", null, ["callee:00be1620:8"]]
- 00b9a17c bytes fd1c0194
+ 00b9a244 bytes f71c0194
- 00b9a194 ["INT_ADD", "register:40f0:8", ["const:b9a194:8", "const:4:8"]]
- 00b9a194 ["CALL", null, ["callee:00be1530:8"]]
+ 00b9a25c ["INT_ADD", "register:40f0:8", ["const:b9a25c:8", "const:4:8"]]
+ 00b9a25c ["CALL", null, ["callee:00be1530:8"]]
- 00b9a194 bytes bb1c0194
+ 00b9a25c bytes b51c0194
- 00b9a1b0 ["INT_ADD", "register:40f0:8", ["const:b9a1b0:8", "const:4:8"]]
- 00b9a1b0 ["CALL", null, ["callee:00be1640:8"]]
+ 00b9a278 ["INT_ADD", "register:40f0:8", ["const:b9a278:8", "const:4:8"]]
+ 00b9a278 ["CALL", null, ["callee:00be1640:8"]]
- 00b9a1b0 bytes f81c0194
+ 00b9a278 bytes f21c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94cc7e2fea2a05fafd55ec52e87c45b3"></a>

### [`00b9c048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9c/00b9c048.md) → [`00b9c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md) FUN_00b9c110

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9bd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9b/00b9bd88.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00b9be50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9c/00b9c048.md#insn-00b9c180) · [`00b9c1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9c/00b9c048.md#insn-00b9c1a0) · [`00b9c1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9c/00b9c048.md#insn-00b9c1fc)
- 新版 [`00b9c248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c248) · [`00b9c268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c268) · [`00b9c2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c2c4)

~~~diff
- 00b9c180 ["INT_ADD", "register:40f0:8", ["const:b9c180:8", "const:4:8"]]
- 00b9c180 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b9c248 ["INT_ADD", "register:40f0:8", ["const:b9c248:8", "const:4:8"]]
+ 00b9c248 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b9c180 bytes 70fb0094
+ 00b9c248 bytes 6afb0094
- 00b9c1a0 ["INT_ADD", "register:40f0:8", ["const:b9c1a0:8", "const:4:8"]]
- 00b9c1a0 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b9c268 ["INT_ADD", "register:40f0:8", ["const:b9c268:8", "const:4:8"]]
+ 00b9c268 ["CALL", null, ["callee:00bdb160:8"]]
- 00b9c1a0 bytes c4fb0094
+ 00b9c268 bytes befb0094
- 00b9c1fc ["INT_ADD", "register:40f0:8", ["const:b9c1fc:8", "const:4:8"]]
- 00b9c1fc ["CALL", null, ["callee:00bde1d0:8"]]
+ 00b9c2c4 ["INT_ADD", "register:40f0:8", ["const:b9c2c4:8", "const:4:8"]]
+ 00b9c2c4 ["CALL", null, ["callee:00bde1d0:8"]]
- 00b9c1fc bytes c9070194
+ 00b9c2c4 bytes c3070194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b20f205d5ded16deef182a829e7d19ad"></a>

### [`00b9e070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9e070.md) → [`00b9e138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md) FUN_00b9e138

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9dd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9d/00b9dd44.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00b9de0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9e160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9e070.md#insn-00b9e160) · [`00b9e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9e070.md#insn-00b9e1dc) · [`00b9e20c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9e070.md#insn-00b9e20c)
- 新版 [`00b9e228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e228) · [`00b9e2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e2a4) · [`00b9e2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e2d4)

~~~diff
- 00b9e160 ["INT_ADD", "register:40f0:8", ["const:b9e160:8", "const:4:8"]]
- 00b9e160 ["CALL", null, ["callee:00bdda00:8"]]
+ 00b9e228 ["INT_ADD", "register:40f0:8", ["const:b9e228:8", "const:4:8"]]
+ 00b9e228 ["CALL", null, ["callee:00bdda00:8"]]
- 00b9e160 bytes fcfd0094
+ 00b9e228 bytes f6fd0094
- 00b9e1dc ["INT_ADD", "register:40f0:8", ["const:b9e1dc:8", "const:4:8"]]
- 00b9e1dc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b9e2a4 ["INT_ADD", "register:40f0:8", ["const:b9e2a4:8", "const:4:8"]]
+ 00b9e2a4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b9e1dc bytes 59f30094
+ 00b9e2a4 bytes 53f30094
- 00b9e20c ["INT_ADD", "register:40f0:8", ["const:b9e20c:8", "const:4:8"]]
- 00b9e20c ["CALL", null, ["callee:00bdb160:8"]]
+ 00b9e2d4 ["INT_ADD", "register:40f0:8", ["const:b9e2d4:8", "const:4:8"]]
+ 00b9e2d4 ["CALL", null, ["callee:00bdb160:8"]]
- 00b9e20c bytes a9f30094
+ 00b9e2d4 bytes a3f30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e63f24033c49cc97fd79645c2902e1a8"></a>

### [`00b9ea64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ea64.md) → [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) FUN_00b9eb2c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00b926fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b926fc.md) [`00b92b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b92b8c.md) [`00b93e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93e30.md) [`00b942c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b94/00b942c0.md) [`00b9e5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9e5b8.md) · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1610.md)
- 新版 呼出元 6件 [`00b927c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md) [`00b92c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md) [`00b93ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md) [`00b94388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md) [`00b9e680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md) · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9eac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ea64.md#insn-00b9eac8) · [`00b9eae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ea64.md#insn-00b9eae8) · [`00b9eaf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ea64.md#insn-00b9eaf8)
- 新版 [`00b9eb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9eb90) · [`00b9ebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9ebb0) · [`00b9ebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9ebc0)

~~~diff
- 00b9eac8 ["INT_ADD", "register:40f0:8", ["const:b9eac8:8", "const:4:8"]]
- 00b9eac8 ["CALL", null, ["callee:00be1530:8"]]
+ 00b9eb90 ["INT_ADD", "register:40f0:8", ["const:b9eb90:8", "const:4:8"]]
+ 00b9eb90 ["CALL", null, ["callee:00be1530:8"]]
- 00b9eac8 bytes 6e0a0194
+ 00b9eb90 bytes 680a0194
- 00b9eae8 ["INT_ADD", "register:40f0:8", ["const:b9eae8:8", "const:4:8"]]
- 00b9eae8 ["CALL", null, ["callee:00be16c0:8"]]
+ 00b9ebb0 ["INT_ADD", "register:40f0:8", ["const:b9ebb0:8", "const:4:8"]]
+ 00b9ebb0 ["CALL", null, ["callee:00be16c0:8"]]
- 00b9eae8 bytes ca0a0194
+ 00b9ebb0 bytes c40a0194
- 00b9eaf8 ["INT_ADD", "register:40f0:8", ["const:b9eaf8:8", "const:4:8"]]
- 00b9eaf8 ["CALL", null, ["callee:00be1530:8"]]
+ 00b9ebc0 ["INT_ADD", "register:40f0:8", ["const:b9ebc0:8", "const:4:8"]]
+ 00b9ebc0 ["CALL", null, ["callee:00be1530:8"]]
- 00b9eaf8 bytes 620a0194
+ 00b9ebc0 bytes 5c0a0194
~~~


<a id="compare-6786147f06442ff5f6fefe634394a147"></a>

### [`00b9ed44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ed44.md) → [`00b9ee0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md) _ZNSt6__ndk111__money_putIcE8__formatEPcRS2_S3_jPKcS5_RKNS_5ctypeIcEEbRKNS_10money_base7patternEccRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1600.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00be16b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16b0.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9eee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ed44.md#insn-00b9eee0) · [`00b9ef3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ed44.md#insn-00b9ef3c) · [`00b9efa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9e/00b9ed44.md#insn-00b9efa0)
- 新版 [`00b9efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9efa8) · [`00b9f004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9f004) · [`00b9f068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9f068)

~~~diff
- 00b9eee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9eee0 ["INT_ADD", "register:40f0:8", ["const:b9eee0:8", "const:4:8"]]
- 00b9eee0 ["CALLIND", null, ["register:0:8"]]
+ 00b9efa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9efa8 ["INT_ADD", "register:40f0:8", ["const:b9efa8:8", "const:4:8"]]
+ 00b9efa8 ["CALLIND", null, ["register:0:8"]]
- 00b9eee0 bytes 00013fd6
+ 00b9efa8 bytes 00013fd6
- 00b9ef3c ["INT_ADD", "register:40f0:8", ["const:b9ef3c:8", "const:4:8"]]
- 00b9ef3c ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b9f004 ["INT_ADD", "register:40f0:8", ["const:b9f004:8", "const:4:8"]]
+ 00b9f004 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b9ef3c bytes 2df00094
+ 00b9f004 bytes 27f00094
- 00b9efa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9efa0 ["INT_ADD", "register:40f0:8", ["const:b9efa0:8", "const:4:8"]]
- 00b9efa0 ["CALLIND", null, ["register:0:8"]]
+ 00b9f068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9f068 ["INT_ADD", "register:40f0:8", ["const:b9f068:8", "const:4:8"]]
+ 00b9f068 ["CALLIND", null, ["register:0:8"]]
- 00b9efa0 bytes 00013fd6
+ 00b9f068 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98035c742e2986e6363382f6dbfbd0f4"></a>

### [`00b9fc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9f/00b9fc00.md) → [`00b9fcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md) _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1630.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00be16e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16e0.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9fd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9f/00b9fc00.md#insn-00b9fd0c) · [`00b9fd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9f/00b9fc00.md#insn-00b9fd94) · [`00b9fdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b9f/00b9fc00.md#insn-00b9fdec)
- 新版 [`00b9fdd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9fdd4) · [`00b9fe5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9fe5c) · [`00b9feb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9feb4)

~~~diff
- 00b9fd0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9fd0c ["INT_ADD", "register:40f0:8", ["const:b9fd0c:8", "const:4:8"]]
- 00b9fd0c ["CALLIND", null, ["register:0:8"]]
+ 00b9fdd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9fdd4 ["INT_ADD", "register:40f0:8", ["const:b9fdd4:8", "const:4:8"]]
+ 00b9fdd4 ["CALLIND", null, ["register:0:8"]]
- 00b9fd0c bytes 00013fd6
+ 00b9fdd4 bytes 00013fd6
- 00b9fd94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9fd94 ["INT_ADD", "register:40f0:8", ["const:b9fd94:8", "const:4:8"]]
- 00b9fd94 ["CALLIND", null, ["register:0:8"]]
+ 00b9fe5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9fe5c ["INT_ADD", "register:40f0:8", ["const:b9fe5c:8", "const:4:8"]]
+ 00b9fe5c ["CALLIND", null, ["register:0:8"]]
- 00b9fd94 bytes 00013fd6
+ 00b9fe5c bytes 00013fd6
- 00b9fdec ["INT_ADD", "register:40f0:8", ["const:b9fdec:8", "const:4:8"]]
- 00b9fdec ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b9feb4 ["INT_ADD", "register:40f0:8", ["const:b9feb4:8", "const:4:8"]]
+ 00b9feb4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b9fdec bytes 81ec0094
+ 00b9feb4 bytes 7bec0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ca6294534d54e67ea2c86a65ceb61ad"></a>

### [`00ba04b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba04b4.md) → [`00ba057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba057c.md) _ZNSt6__ndk114codecvt_bynameIcc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba04c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba04b4.md#insn-00ba04c8)
- 新版 [`00ba0590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba057c.md#insn-00ba0590)

~~~diff
- 00ba04c8 ["INT_ADD", "register:40f0:8", ["const:ba04c8:8", "const:4:8"]]
- 00ba04c8 ["CALL", null, ["callee:00be1700:8"]]
+ 00ba0590 ["INT_ADD", "register:40f0:8", ["const:ba0590:8", "const:4:8"]]
+ 00ba0590 ["CALL", null, ["callee:00be1700:8"]]
- 00ba04c8 bytes 62040194
+ 00ba0590 bytes 5c040194
~~~


<a id="compare-f2fd6d8346113b9a724c707b915fd9c0"></a>

### [`00ba04e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba04e8.md) → [`00ba05b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05b0.md) _ZNSt6__ndk114codecvt_bynameIwc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba04fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba04e8.md#insn-00ba04fc)
- 新版 [`00ba05c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05b0.md#insn-00ba05c4)

~~~diff
- 00ba04fc ["INT_ADD", "register:40f0:8", ["const:ba04fc:8", "const:4:8"]]
- 00ba04fc ["CALL", null, ["callee:00be1710:8"]]
+ 00ba05c4 ["INT_ADD", "register:40f0:8", ["const:ba05c4:8", "const:4:8"]]
+ 00ba05c4 ["CALL", null, ["callee:00be1710:8"]]
- 00ba04fc bytes 59040194
+ 00ba05c4 bytes 53040194
~~~


<a id="compare-fcdd30f53f43126f8b74dd944f2837f7"></a>

### [`00ba051c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba051c.md) → [`00ba05e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05e4.md) _ZNSt6__ndk114codecvt_bynameIDsc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1680.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba051c.md#insn-00ba0530)
- 新版 [`00ba05f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05e4.md#insn-00ba05f8)

~~~diff
- 00ba0530 ["INT_ADD", "register:40f0:8", ["const:ba0530:8", "const:4:8"]]
- 00ba0530 ["CALL", null, ["callee:00be1730:8"]]
+ 00ba05f8 ["INT_ADD", "register:40f0:8", ["const:ba05f8:8", "const:4:8"]]
+ 00ba05f8 ["CALL", null, ["callee:00be1730:8"]]
- 00ba0530 bytes 54040194
+ 00ba05f8 bytes 4e040194
~~~


<a id="compare-48d478cb75f3ea4494a4fe326382587d"></a>

### [`00ba0550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0550.md) → [`00ba0618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0618.md) _ZNSt6__ndk114codecvt_bynameIDic9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be16a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be16a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0550.md#insn-00ba0564)
- 新版 [`00ba062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0618.md#insn-00ba062c)

~~~diff
- 00ba0564 ["INT_ADD", "register:40f0:8", ["const:ba0564:8", "const:4:8"]]
- 00ba0564 ["CALL", null, ["callee:00be1750:8"]]
+ 00ba062c ["INT_ADD", "register:40f0:8", ["const:ba062c:8", "const:4:8"]]
+ 00ba062c ["CALL", null, ["callee:00be1750:8"]]
- 00ba0564 bytes 4f040194
+ 00ba062c bytes 49040194
~~~


<a id="compare-0653200ab6f7856038fcff21ed7f2782"></a>

### [`00ba0584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0584.md) → [`00ba064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba064c.md) _ZNSt6__ndk114codecvt_bynameIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be16c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be16c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0584.md#insn-00ba0598)
- 新版 [`00ba0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba064c.md#insn-00ba0660)

~~~diff
- 00ba0598 ["INT_ADD", "register:40f0:8", ["const:ba0598:8", "const:4:8"]]
- 00ba0598 ["CALL", null, ["callee:00be1770:8"]]
+ 00ba0660 ["INT_ADD", "register:40f0:8", ["const:ba0660:8", "const:4:8"]]
+ 00ba0660 ["CALL", null, ["callee:00be1770:8"]]
- 00ba0598 bytes 4a040194
+ 00ba0660 bytes 44040194
~~~


<a id="compare-e76f2c5b2f72bd5ab36cfe1e2fc473ce"></a>

### [`00ba05b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05b8.md) → [`00ba0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0680.md) _ZNSt6__ndk114codecvt_bynameIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be16e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be16e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba05cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05b8.md#insn-00ba05cc)
- 新版 [`00ba0694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0680.md#insn-00ba0694)

~~~diff
- 00ba05cc ["INT_ADD", "register:40f0:8", ["const:ba05cc:8", "const:4:8"]]
- 00ba05cc ["CALL", null, ["callee:00be1790:8"]]
+ 00ba0694 ["INT_ADD", "register:40f0:8", ["const:ba0694:8", "const:4:8"]]
+ 00ba0694 ["CALL", null, ["callee:00be1790:8"]]
- 00ba05cc bytes 45040194
+ 00ba0694 bytes 3f040194
~~~


<a id="compare-c6f03f3ae227dc14d80c46c422d9e8a4"></a>

### [`00ba05e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05e4.md) → [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) FUN_00ba06ac

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 2件 [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba06d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05e4.md#insn-00ba06d4)
- 新版 [`00ba079c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md#insn-00ba079c)

~~~diff
- 00ba06d4 ["INT_ADD", "register:40f0:8", ["const:ba06d4:8", "const:4:8"]]
- 00ba06d4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba079c ["INT_ADD", "register:40f0:8", ["const:ba079c:8", "const:4:8"]]
+ 00ba079c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba06d4 bytes 8bea0094
+ 00ba079c bytes 85ea0094
~~~


<a id="compare-076884743c2d82c44491d0df9c15a429"></a>

### [`00ba88a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88a4.md) → [`00ba896c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba896c.md) _ZNSt6__ndk16locale5facetD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba88b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88a4.md#insn-00ba88b8)
- 新版 [`00ba8980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba896c.md#insn-00ba8980)

~~~diff
- 00ba88b8 ["INT_ADD", "register:40f0:8", ["const:ba88b8:8", "const:4:8"]]
- 00ba88b8 ["CALL", null, ["callee:00be18d0:8"]]
+ 00ba8980 ["INT_ADD", "register:40f0:8", ["const:ba8980:8", "const:4:8"]]
+ 00ba8980 ["CALL", null, ["callee:00be18d0:8"]]
- 00ba88b8 bytes dae30094
+ 00ba8980 bytes d4e30094
~~~


<a id="compare-7353d65b1da628a17dced004b26af4db"></a>

### [`00ba9104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9104.md) → [`00ba91cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91cc.md) _ZNSt6__ndk114collate_bynameIwED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1870.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9104.md#insn-00ba9118)
- 新版 [`00ba91e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91cc.md#insn-00ba91e0)

~~~diff
- 00ba9118 ["INT_ADD", "register:40f0:8", ["const:ba9118:8", "const:4:8"]]
- 00ba9118 ["CALL", null, ["callee:00be1920:8"]]
+ 00ba91e0 ["INT_ADD", "register:40f0:8", ["const:ba91e0:8", "const:4:8"]]
+ 00ba91e0 ["CALL", null, ["callee:00be1920:8"]]
- 00ba9118 bytes d6e10094
+ 00ba91e0 bytes d0e10094
~~~


<a id="compare-c7792567ae6e419a2a4617c9b7795822"></a>

### [`00ba9d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d18.md) → [`00ba9de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9de0.md) _ZNSt6__ndk15ctypeIcED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be18d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d18.md#insn-00ba9d2c)
- 新版 [`00ba9df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9de0.md#insn-00ba9df4)

~~~diff
- 00ba9d2c ["INT_ADD", "register:40f0:8", ["const:ba9d2c:8", "const:4:8"]]
- 00ba9d2c ["CALL", null, ["callee:00be1980:8"]]
+ 00ba9df4 ["INT_ADD", "register:40f0:8", ["const:ba9df4:8", "const:4:8"]]
+ 00ba9df4 ["CALL", null, ["callee:00be1980:8"]]
- 00ba9d2c bytes e9de0094
+ 00ba9df4 bytes e3de0094
~~~


<a id="compare-45c6ccbbfc841d778b2b8466ad780823"></a>

### [`00baa3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa3d8.md) → [`00baa4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa4a0.md) _ZNSt6__ndk112ctype_bynameIcED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1900.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be19b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa3ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa3d8.md#insn-00baa3ec)
- 新版 [`00baa4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa4a0.md#insn-00baa4b4)

~~~diff
- 00baa3ec ["INT_ADD", "register:40f0:8", ["const:baa3ec:8", "const:4:8"]]
- 00baa3ec ["CALL", null, ["callee:00be19b0:8"]]
+ 00baa4b4 ["INT_ADD", "register:40f0:8", ["const:baa4b4:8", "const:4:8"]]
+ 00baa4b4 ["CALL", null, ["callee:00be19b0:8"]]
- 00baa3ec bytes 45dd0094
+ 00baa4b4 bytes 3fdd0094
~~~


<a id="compare-d0ad90fe0a25b0dbb5b008815686cc9c"></a>

### [`00baa930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa930.md) → [`00baa9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa9f8.md) _ZNSt6__ndk112ctype_bynameIwED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1940.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be19f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa930.md#insn-00baa944)
- 新版 [`00baaa0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa9f8.md#insn-00baaa0c)

~~~diff
- 00baa944 ["INT_ADD", "register:40f0:8", ["const:baa944:8", "const:4:8"]]
- 00baa944 ["CALL", null, ["callee:00be19f0:8"]]
+ 00baaa0c ["INT_ADD", "register:40f0:8", ["const:baaa0c:8", "const:4:8"]]
+ 00baaa0c ["CALL", null, ["callee:00be19f0:8"]]
- 00baa944 bytes ffdb0094
+ 00baaa0c bytes f9db0094
~~~


<a id="compare-4e214674e522eeec94146b24313978cf"></a>

### [`00baa95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa95c.md) → [`00baaa24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be18b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18b0.md) [`00be1950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1950.md) [`00be1960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1960.md) [`00be1970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1970.md) [`00be1980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1980.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa95c.md#insn-00baa994) · [`00baa9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa95c.md#insn-00baa9ac) · [`00baa9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa95c.md#insn-00baa9e0)
- 新版 [`00baaa5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaa5c) · [`00baaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaa74) · [`00baaaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaaa8)

~~~diff
- 00baa994 ["INT_ADD", "register:40f0:8", ["const:baa994:8", "const:4:8"]]
- 00baa994 ["CALL", null, ["callee:00be1a00:8"]]
+ 00baaa5c ["INT_ADD", "register:40f0:8", ["const:baaa5c:8", "const:4:8"]]
+ 00baaa5c ["CALL", null, ["callee:00be1a00:8"]]
- 00baa994 bytes efdb0094
+ 00baaa5c bytes e9db0094
- 00baa9ac ["INT_ADD", "register:40f0:8", ["const:baa9ac:8", "const:4:8"]]
- 00baa9ac ["CALL", null, ["callee:00be1a10:8"]]
+ 00baaa74 ["INT_ADD", "register:40f0:8", ["const:baaa74:8", "const:4:8"]]
+ 00baaa74 ["CALL", null, ["callee:00be1a10:8"]]
- 00baa9ac bytes eddb0094
+ 00baaa74 bytes e7db0094
- 00baa9e0 ["INT_ADD", "register:40f0:8", ["const:baa9e0:8", "const:4:8"]]
- 00baa9e0 ["CALL", null, ["callee:00be1a20:8"]]
+ 00baaaa8 ["INT_ADD", "register:40f0:8", ["const:baaaa8:8", "const:4:8"]]
+ 00baaaa8 ["CALL", null, ["callee:00be1a20:8"]]
- 00baa9e0 bytes e4db0094
+ 00baaaa8 bytes dedb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dcc2a1e0248d9c865c10e5c3bb4280e"></a>

### [`00baaab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaab0.md) → [`00baab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be18b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18b0.md) [`00be1950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1950.md) [`00be1960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1960.md) [`00be1970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1970.md) [`00be1980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1980.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baab1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaab0.md#insn-00baab1c) · [`00baab38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaab0.md#insn-00baab38) · [`00baab54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaab0.md#insn-00baab54)
- 新版 [`00baabe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baabe4) · [`00baac00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baac00) · [`00baac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baac1c)

~~~diff
- 00baab1c ["INT_ADD", "register:40f0:8", ["const:baab1c:8", "const:4:8"]]
- 00baab1c ["CALL", null, ["callee:00be1a00:8"]]
+ 00baabe4 ["INT_ADD", "register:40f0:8", ["const:baabe4:8", "const:4:8"]]
+ 00baabe4 ["CALL", null, ["callee:00be1a00:8"]]
- 00baab1c bytes 8ddb0094
+ 00baabe4 bytes 87db0094
- 00baab38 ["INT_ADD", "register:40f0:8", ["const:baab38:8", "const:4:8"]]
- 00baab38 ["CALL", null, ["callee:00be1a10:8"]]
+ 00baac00 ["INT_ADD", "register:40f0:8", ["const:baac00:8", "const:4:8"]]
+ 00baac00 ["CALL", null, ["callee:00be1a10:8"]]
- 00baab38 bytes 8adb0094
+ 00baac00 bytes 84db0094
- 00baab54 ["INT_ADD", "register:40f0:8", ["const:baab54:8", "const:4:8"]]
- 00baab54 ["CALL", null, ["callee:00be1a30:8"]]
+ 00baac1c ["INT_ADD", "register:40f0:8", ["const:baac1c:8", "const:4:8"]]
+ 00baac1c ["CALL", null, ["callee:00be1a30:8"]]
- 00baab54 bytes 8bdb0094
+ 00baac1c bytes 85db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-debbf0b67ddc1e499c18bbb24278708e"></a>

### [`00baac4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baac4c.md) → [`00baad14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md) _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be18b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18b0.md) [`00be1950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1950.md) [`00be1960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1960.md) [`00be1970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1970.md) [`00be1980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1980.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baac9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baac4c.md#insn-00baac9c) · [`00baacb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baac4c.md#insn-00baacb0) · [`00baacc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baac4c.md#insn-00baacc4)
- 新版 [`00baad64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad64) · [`00baad78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad78) · [`00baad8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad8c)

~~~diff
- 00baac9c ["INT_ADD", "register:40f0:8", ["const:baac9c:8", "const:4:8"]]
- 00baac9c ["CALL", null, ["callee:00be1a00:8"]]
+ 00baad64 ["INT_ADD", "register:40f0:8", ["const:baad64:8", "const:4:8"]]
+ 00baad64 ["CALL", null, ["callee:00be1a00:8"]]
- 00baac9c bytes 2ddb0094
+ 00baad64 bytes 27db0094
- 00baacb0 ["INT_ADD", "register:40f0:8", ["const:baacb0:8", "const:4:8"]]
- 00baacb0 ["CALL", null, ["callee:00be1a10:8"]]
+ 00baad78 ["INT_ADD", "register:40f0:8", ["const:baad78:8", "const:4:8"]]
+ 00baad78 ["CALL", null, ["callee:00be1a10:8"]]
- 00baacb0 bytes 2cdb0094
+ 00baad78 bytes 26db0094
- 00baacc4 ["INT_ADD", "register:40f0:8", ["const:baacc4:8", "const:4:8"]]
- 00baacc4 ["CALL", null, ["callee:00be1a30:8"]]
+ 00baad8c ["INT_ADD", "register:40f0:8", ["const:baad8c:8", "const:4:8"]]
+ 00baad8c ["CALL", null, ["callee:00be1a30:8"]]
- 00baacc4 bytes 2fdb0094
+ 00baad8c bytes 29db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de5e55ed9e8966b3561ded348b6b08d5"></a>

### [`00baad7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baad7c.md) → [`00baae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md) _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be18b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18b0.md) [`00be1950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1950.md) [`00be1960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1960.md) [`00be1970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1970.md) [`00be1980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1980.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baadb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baad7c.md#insn-00baadb8) · [`00baade0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baad7c.md#insn-00baade0) · [`00baadf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baad7c.md#insn-00baadf4)
- 新版 [`00baae80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baae80) · [`00baaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baaea8) · [`00baaebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baaebc)

~~~diff
- 00baadb8 ["INT_ADD", "register:40f0:8", ["const:baadb8:8", "const:4:8"]]
- 00baadb8 ["CALL", null, ["callee:00be1a00:8"]]
+ 00baae80 ["INT_ADD", "register:40f0:8", ["const:baae80:8", "const:4:8"]]
+ 00baae80 ["CALL", null, ["callee:00be1a00:8"]]
- 00baadb8 bytes e6da0094
+ 00baae80 bytes e0da0094
- 00baade0 ["INT_ADD", "register:40f0:8", ["const:baade0:8", "const:4:8"]]
- 00baade0 ["CALL", null, ["callee:00be1a10:8"]]
+ 00baaea8 ["INT_ADD", "register:40f0:8", ["const:baaea8:8", "const:4:8"]]
+ 00baaea8 ["CALL", null, ["callee:00be1a10:8"]]
- 00baade0 bytes e0da0094
+ 00baaea8 bytes dada0094
- 00baadf4 ["INT_ADD", "register:40f0:8", ["const:baadf4:8", "const:4:8"]]
- 00baadf4 ["CALL", null, ["callee:00be1a30:8"]]
+ 00baaebc ["INT_ADD", "register:40f0:8", ["const:baaebc:8", "const:4:8"]]
+ 00baaebc ["CALL", null, ["callee:00be1a30:8"]]
- 00baadf4 bytes e3da0094
+ 00baaebc bytes ddda0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26201fa1bb3c4f5702f66aa8b54a0875"></a>

### [`00baaec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaec0.md) → [`00baaf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md) _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be19e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be19e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baaef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaec0.md#insn-00baaef0)
- 新版 [`00baafb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md#insn-00baafb8)

~~~diff
- 00baaef0 ["INT_ADD", "register:40f0:8", ["const:baaef0:8", "const:4:8"]]
- 00baaef0 ["CALL", null, ["callee:00be1a90:8"]]
+ 00baafb8 ["INT_ADD", "register:40f0:8", ["const:baafb8:8", "const:4:8"]]
+ 00baafb8 ["CALL", null, ["callee:00be1a90:8"]]
- 00baaef0 bytes bcda0094
+ 00baafb8 bytes b6da0094
~~~


<a id="compare-130882ff06ae6505da536080a7d30274"></a>

### [`00baaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf30.md) → [`00baaff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaff8.md) _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be19f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be19f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf30.md#insn-00baaf60)
- 新版 [`00bab028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaff8.md#insn-00bab028)

~~~diff
- 00baaf60 ["INT_ADD", "register:40f0:8", ["const:baaf60:8", "const:4:8"]]
- 00baaf60 ["CALL", null, ["callee:00be1aa0:8"]]
+ 00bab028 ["INT_ADD", "register:40f0:8", ["const:bab028:8", "const:4:8"]]
+ 00bab028 ["CALL", null, ["callee:00be1aa0:8"]]
- 00baaf60 bytes a4da0094
+ 00bab028 bytes 9eda0094
~~~


<a id="compare-7162f67b6159e5e41f2d73eaa923dc7e"></a>

### [`00baaf8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf8c.md) → [`00bab054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baafa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf8c.md#insn-00baafa8) · [`00baafb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf8c.md#insn-00baafb8) · [`00baafc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf8c.md#insn-00baafc8)
- 新版 [`00bab070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab070) · [`00bab080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab080) · [`00bab090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab090)

~~~diff
- 00baafa8 ["INT_ADD", "register:40f0:8", ["const:baafa8:8", "const:4:8"]]
- 00baafa8 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab070 ["INT_ADD", "register:40f0:8", ["const:bab070:8", "const:4:8"]]
+ 00bab070 ["CALL", null, ["callee:00be1530:8"]]
- 00baafa8 bytes 36d90094
+ 00bab070 bytes 30d90094
- 00baafb8 ["INT_ADD", "register:40f0:8", ["const:baafb8:8", "const:4:8"]]
- 00baafb8 ["CALL", null, ["callee:00be1ab0:8"]]
+ 00bab080 ["INT_ADD", "register:40f0:8", ["const:bab080:8", "const:4:8"]]
+ 00bab080 ["CALL", null, ["callee:00be1ab0:8"]]
- 00baafb8 bytes 92da0094
+ 00bab080 bytes 8cda0094
- 00baafc8 ["INT_ADD", "register:40f0:8", ["const:baafc8:8", "const:4:8"]]
- 00baafc8 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab090 ["INT_ADD", "register:40f0:8", ["const:bab090:8", "const:4:8"]]
+ 00bab090 ["CALL", null, ["callee:00be1530:8"]]
- 00baafc8 bytes 2ed90094
+ 00bab090 bytes 28d90094
~~~


<a id="compare-12d085455fd75cd0011d39794b0a3678"></a>

### [`00baaffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaffc.md) → [`00bab0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaffc.md#insn-00bab04c) · [`00bab05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaffc.md#insn-00bab05c) · [`00bab06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaffc.md#insn-00bab06c)
- 新版 [`00bab114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab114) · [`00bab124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab124) · [`00bab134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab134)

~~~diff
- 00bab04c ["INT_ADD", "register:40f0:8", ["const:bab04c:8", "const:4:8"]]
- 00bab04c ["CALL", null, ["callee:00be1530:8"]]
+ 00bab114 ["INT_ADD", "register:40f0:8", ["const:bab114:8", "const:4:8"]]
+ 00bab114 ["CALL", null, ["callee:00be1530:8"]]
- 00bab04c bytes 0dd90094
+ 00bab114 bytes 07d90094
- 00bab05c ["INT_ADD", "register:40f0:8", ["const:bab05c:8", "const:4:8"]]
- 00bab05c ["CALL", null, ["callee:00be1ab0:8"]]
+ 00bab124 ["INT_ADD", "register:40f0:8", ["const:bab124:8", "const:4:8"]]
+ 00bab124 ["CALL", null, ["callee:00be1ab0:8"]]
- 00bab05c bytes 69da0094
+ 00bab124 bytes 63da0094
- 00bab06c ["INT_ADD", "register:40f0:8", ["const:bab06c:8", "const:4:8"]]
- 00bab06c ["CALL", null, ["callee:00be1530:8"]]
+ 00bab134 ["INT_ADD", "register:40f0:8", ["const:bab134:8", "const:4:8"]]
+ 00bab134 ["CALL", null, ["callee:00be1530:8"]]
- 00bab06c bytes 05d90094
+ 00bab134 bytes ffd80094
~~~


<a id="compare-fccb61e3205a04208f82f1c43b3185c2"></a>

### [`00bab0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab0b0.md) → [`00bab178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab0b0.md#insn-00bab0d0) · [`00bab0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab0b0.md#insn-00bab0e0) · [`00bab0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab0b0.md#insn-00bab0f0)
- 新版 [`00bab198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab198) · [`00bab1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab1a8) · [`00bab1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab1b8)

~~~diff
- 00bab0d0 ["INT_ADD", "register:40f0:8", ["const:bab0d0:8", "const:4:8"]]
- 00bab0d0 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab198 ["INT_ADD", "register:40f0:8", ["const:bab198:8", "const:4:8"]]
+ 00bab198 ["CALL", null, ["callee:00be1530:8"]]
- 00bab0d0 bytes ecd80094
+ 00bab198 bytes e6d80094
- 00bab0e0 ["INT_ADD", "register:40f0:8", ["const:bab0e0:8", "const:4:8"]]
- 00bab0e0 ["CALL", null, ["callee:00be1ac0:8"]]
+ 00bab1a8 ["INT_ADD", "register:40f0:8", ["const:bab1a8:8", "const:4:8"]]
+ 00bab1a8 ["CALL", null, ["callee:00be1ac0:8"]]
- 00bab0e0 bytes 4cda0094
+ 00bab1a8 bytes 46da0094
- 00bab0f0 ["INT_ADD", "register:40f0:8", ["const:bab0f0:8", "const:4:8"]]
- 00bab0f0 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab1b8 ["INT_ADD", "register:40f0:8", ["const:bab1b8:8", "const:4:8"]]
+ 00bab1b8 ["CALL", null, ["callee:00be1530:8"]]
- 00bab0f0 bytes e4d80094
+ 00bab1b8 bytes ded80094
~~~


<a id="compare-34f884f65b4a4baa008a49ab6953f436"></a>

### [`00bab128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab128.md) → [`00bab1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEPKwS3_cPc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab128.md#insn-00bab184) · [`00bab194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab128.md#insn-00bab194) · [`00bab1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab128.md#insn-00bab1a4)
- 新版 [`00bab24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab24c) · [`00bab25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab25c) · [`00bab26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab26c)

~~~diff
- 00bab184 ["INT_ADD", "register:40f0:8", ["const:bab184:8", "const:4:8"]]
- 00bab184 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab24c ["INT_ADD", "register:40f0:8", ["const:bab24c:8", "const:4:8"]]
+ 00bab24c ["CALL", null, ["callee:00be1530:8"]]
- 00bab184 bytes bfd80094
+ 00bab24c bytes b9d80094
- 00bab194 ["INT_ADD", "register:40f0:8", ["const:bab194:8", "const:4:8"]]
- 00bab194 ["CALL", null, ["callee:00be1ac0:8"]]
+ 00bab25c ["INT_ADD", "register:40f0:8", ["const:bab25c:8", "const:4:8"]]
+ 00bab25c ["CALL", null, ["callee:00be1ac0:8"]]
- 00bab194 bytes 1fda0094
+ 00bab25c bytes 19da0094
- 00bab1a4 ["INT_ADD", "register:40f0:8", ["const:bab1a4:8", "const:4:8"]]
- 00bab1a4 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab26c ["INT_ADD", "register:40f0:8", ["const:bab26c:8", "const:4:8"]]
+ 00bab26c ["CALL", null, ["callee:00be1530:8"]]
- 00bab1a4 bytes b7d80094
+ 00bab26c bytes b1d80094
~~~


<a id="compare-d4a37d5fa3dce7fbb940f80de15f9588"></a>

### [`00bab1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab1e8.md) → [`00bab2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab2b0.md) _ZNSt6__ndk17codecvtIcc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab1e8.md#insn-00bab1fc)
- 新版 [`00bab2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab2b0.md#insn-00bab2c4)

~~~diff
- 00bab1fc ["INT_ADD", "register:40f0:8", ["const:bab1fc:8", "const:4:8"]]
- 00bab1fc ["CALL", null, ["callee:00be1ad0:8"]]
+ 00bab2c4 ["INT_ADD", "register:40f0:8", ["const:bab2c4:8", "const:4:8"]]
+ 00bab2c4 ["CALL", null, ["callee:00be1ad0:8"]]
- 00bab1fc bytes 09da0094
+ 00bab2c4 bytes 03da0094
~~~


<a id="compare-92821216ba15eb33d2ee8392e1d93210"></a>

### [`00bab408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab408.md) → [`00bab4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4d0.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab408.md#insn-00bab41c)
- 新版 [`00bab4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4d0.md#insn-00bab4e4)

~~~diff
- 00bab41c ["INT_ADD", "register:40f0:8", ["const:bab41c:8", "const:4:8"]]
- 00bab41c ["CALL", null, ["callee:00be1ae0:8"]]
+ 00bab4e4 ["INT_ADD", "register:40f0:8", ["const:bab4e4:8", "const:4:8"]]
+ 00bab4e4 ["CALL", null, ["callee:00be1ae0:8"]]
- 00bab41c bytes 85d90094
+ 00bab4e4 bytes 7fd90094
~~~


<a id="compare-97e2a5bfcfd44d056c4d5e62ace605ab"></a>

### [`00bab434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab434.md) → [`00bab4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a40.md) [`00be1a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1af0.md) [`00be1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab434.md#insn-00bab4e8) · [`00bab508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab434.md#insn-00bab508) · [`00bab518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab434.md#insn-00bab518)
- 新版 [`00bab5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5b0) · [`00bab5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5d0) · [`00bab5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5e0)

~~~diff
- 00bab4e8 ["INT_ADD", "register:40f0:8", ["const:bab4e8:8", "const:4:8"]]
- 00bab4e8 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab5b0 ["INT_ADD", "register:40f0:8", ["const:bab5b0:8", "const:4:8"]]
+ 00bab5b0 ["CALL", null, ["callee:00be1530:8"]]
- 00bab4e8 bytes e6d70094
+ 00bab5b0 bytes e0d70094
- 00bab508 ["INT_ADD", "register:40f0:8", ["const:bab508:8", "const:4:8"]]
- 00bab508 ["CALL", null, ["callee:00be1af0:8"]]
+ 00bab5d0 ["INT_ADD", "register:40f0:8", ["const:bab5d0:8", "const:4:8"]]
+ 00bab5d0 ["CALL", null, ["callee:00be1af0:8"]]
- 00bab508 bytes 4ed90094
+ 00bab5d0 bytes 48d90094
- 00bab518 ["INT_ADD", "register:40f0:8", ["const:bab518:8", "const:4:8"]]
- 00bab518 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab5e0 ["INT_ADD", "register:40f0:8", ["const:bab5e0:8", "const:4:8"]]
+ 00bab5e0 ["CALL", null, ["callee:00be1530:8"]]
- 00bab518 bytes dad70094
+ 00bab5e0 bytes d4d70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1d134142df9c514db38fb3fa2692b8"></a>

### [`00bab6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab6f8.md) → [`00bab7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE5do_inERS1_PKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b10.md) [`00be1b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab6f8.md#insn-00bab798) · [`00bab7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab6f8.md#insn-00bab7b8) · [`00bab7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab6f8.md#insn-00bab7c8)
- 新版 [`00bab860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab860) · [`00bab880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab880) · [`00bab890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab890)

~~~diff
- 00bab798 ["INT_ADD", "register:40f0:8", ["const:bab798:8", "const:4:8"]]
- 00bab798 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab860 ["INT_ADD", "register:40f0:8", ["const:bab860:8", "const:4:8"]]
+ 00bab860 ["CALL", null, ["callee:00be1530:8"]]
- 00bab798 bytes 3ad70094
+ 00bab860 bytes 34d70094
- 00bab7b8 ["INT_ADD", "register:40f0:8", ["const:bab7b8:8", "const:4:8"]]
- 00bab7b8 ["CALL", null, ["callee:00be1b10:8"]]
+ 00bab880 ["INT_ADD", "register:40f0:8", ["const:bab880:8", "const:4:8"]]
+ 00bab880 ["CALL", null, ["callee:00be1b10:8"]]
- 00bab7b8 bytes aad80094
+ 00bab880 bytes a4d80094
- 00bab7c8 ["INT_ADD", "register:40f0:8", ["const:bab7c8:8", "const:4:8"]]
- 00bab7c8 ["CALL", null, ["callee:00be1530:8"]]
+ 00bab890 ["INT_ADD", "register:40f0:8", ["const:bab890:8", "const:4:8"]]
+ 00bab890 ["CALL", null, ["callee:00be1530:8"]]
- 00bab7c8 bytes 2ed70094
+ 00bab890 bytes 28d70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1b4067c2baddd6f0c37fa4ac009831"></a>

### [`00bab9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab9ac.md) → [`00baba74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab9ac.md#insn-00bab9d8) · [`00bab9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab9ac.md#insn-00bab9f0) · [`00baba00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab9ac.md#insn-00baba00)
- 新版 [`00babaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babaa0) · [`00babab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babab8) · [`00babac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babac8)

~~~diff
- 00bab9d8 ["INT_ADD", "register:40f0:8", ["const:bab9d8:8", "const:4:8"]]
- 00bab9d8 ["CALL", null, ["callee:00be1530:8"]]
+ 00babaa0 ["INT_ADD", "register:40f0:8", ["const:babaa0:8", "const:4:8"]]
+ 00babaa0 ["CALL", null, ["callee:00be1530:8"]]
- 00bab9d8 bytes aad60094
+ 00babaa0 bytes a4d60094
- 00bab9f0 ["INT_ADD", "register:40f0:8", ["const:bab9f0:8", "const:4:8"]]
- 00bab9f0 ["CALL", null, ["callee:00be1b00:8"]]
+ 00babab8 ["INT_ADD", "register:40f0:8", ["const:babab8:8", "const:4:8"]]
+ 00babab8 ["CALL", null, ["callee:00be1b00:8"]]
- 00bab9f0 bytes 18d80094
+ 00babab8 bytes 12d80094
- 00baba00 ["INT_ADD", "register:40f0:8", ["const:baba00:8", "const:4:8"]]
- 00baba00 ["CALL", null, ["callee:00be1530:8"]]
+ 00babac8 ["INT_ADD", "register:40f0:8", ["const:babac8:8", "const:4:8"]]
+ 00babac8 ["CALL", null, ["callee:00be1530:8"]]
- 00baba00 bytes a0d60094
+ 00babac8 bytes 9ad60094
~~~


<a id="compare-3dcb36380fe23df4afc62d3d41a52a74"></a>

### [`00baba8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00baba8c.md) → [`00babb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a80.md) [`00be1a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b30.md) [`00be1b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00baba8c.md#insn-00babaa8) · [`00babac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00baba8c.md#insn-00babac0) · [`00babad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00baba8c.md#insn-00babad0)
- 新版 [`00babb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb70) · [`00babb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb88) · [`00babb98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb98)

~~~diff
- 00babaa8 ["INT_ADD", "register:40f0:8", ["const:babaa8:8", "const:4:8"]]
- 00babaa8 ["CALL", null, ["callee:00be1530:8"]]
+ 00babb70 ["INT_ADD", "register:40f0:8", ["const:babb70:8", "const:4:8"]]
+ 00babb70 ["CALL", null, ["callee:00be1530:8"]]
- 00babaa8 bytes 76d60094
+ 00babb70 bytes 70d60094
- 00babac0 ["INT_ADD", "register:40f0:8", ["const:babac0:8", "const:4:8"]]
- 00babac0 ["CALL", null, ["callee:00be1b30:8"]]
+ 00babb88 ["INT_ADD", "register:40f0:8", ["const:babb88:8", "const:4:8"]]
+ 00babb88 ["CALL", null, ["callee:00be1b30:8"]]
- 00babac0 bytes f0d70094
+ 00babb88 bytes ead70094
- 00babad0 ["INT_ADD", "register:40f0:8", ["const:babad0:8", "const:4:8"]]
- 00babad0 ["CALL", null, ["callee:00be1530:8"]]
+ 00babb98 ["INT_ADD", "register:40f0:8", ["const:babb98:8", "const:4:8"]]
+ 00babb98 ["CALL", null, ["callee:00be1530:8"]]
- 00babad0 bytes 6cd60094
+ 00babb98 bytes 66d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d65808832668c775500c879f025ad2"></a>

### [`00babb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babb5c.md) → [`00babc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1aa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babb5c.md#insn-00babbb0) · [`00babbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babb5c.md#insn-00babbc8) · [`00babbd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babb5c.md#insn-00babbd8)
- 新版 [`00babc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babc78) · [`00babc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babc90) · [`00babca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babca0)

~~~diff
- 00babbb0 ["INT_ADD", "register:40f0:8", ["const:babbb0:8", "const:4:8"]]
- 00babbb0 ["CALL", null, ["callee:00be1530:8"]]
+ 00babc78 ["INT_ADD", "register:40f0:8", ["const:babc78:8", "const:4:8"]]
+ 00babc78 ["CALL", null, ["callee:00be1530:8"]]
- 00babbb0 bytes 34d60094
+ 00babc78 bytes 2ed60094
- 00babbc8 ["INT_ADD", "register:40f0:8", ["const:babbc8:8", "const:4:8"]]
- 00babbc8 ["CALL", null, ["callee:00be1b50:8"]]
+ 00babc90 ["INT_ADD", "register:40f0:8", ["const:babc90:8", "const:4:8"]]
+ 00babc90 ["CALL", null, ["callee:00be1b50:8"]]
- 00babbc8 bytes b6d70094
+ 00babc90 bytes b0d70094
- 00babbd8 ["INT_ADD", "register:40f0:8", ["const:babbd8:8", "const:4:8"]]
- 00babbd8 ["CALL", null, ["callee:00be1530:8"]]
+ 00babca0 ["INT_ADD", "register:40f0:8", ["const:babca0:8", "const:4:8"]]
+ 00babca0 ["CALL", null, ["callee:00be1530:8"]]
- 00babbd8 bytes 2ad60094
+ 00babca0 bytes 24d60094
~~~


<a id="compare-6226a4c168536e7424eedf989232ae91"></a>

### [`00babc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babc54.md) → [`00babd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md) [`00be1a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babc54.md#insn-00babc70) · [`00babc7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babc54.md#insn-00babc7c) · [`00babc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babc54.md#insn-00babc8c)
- 新版 [`00babd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd38) · [`00babd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd44) · [`00babd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd54)

~~~diff
- 00babc70 ["INT_ADD", "register:40f0:8", ["const:babc70:8", "const:4:8"]]
- 00babc70 ["CALL", null, ["callee:00be1530:8"]]
+ 00babd38 ["INT_ADD", "register:40f0:8", ["const:babd38:8", "const:4:8"]]
+ 00babd38 ["CALL", null, ["callee:00be1530:8"]]
- 00babc70 bytes 04d60094
+ 00babd38 bytes fed50094
- 00babc7c ["INT_ADD", "register:40f0:8", ["const:babc7c:8", "const:4:8"]]
- 00babc7c ["CALL", null, ["callee:00be1b40:8"]]
+ 00babd44 ["INT_ADD", "register:40f0:8", ["const:babd44:8", "const:4:8"]]
+ 00babd44 ["CALL", null, ["callee:00be1b40:8"]]
- 00babc7c bytes 85d70094
+ 00babd44 bytes 7fd70094
- 00babc8c ["INT_ADD", "register:40f0:8", ["const:babc8c:8", "const:4:8"]]
- 00babc8c ["CALL", null, ["callee:00be1530:8"]]
+ 00babd54 ["INT_ADD", "register:40f0:8", ["const:babd54:8", "const:4:8"]]
+ 00babd54 ["CALL", null, ["callee:00be1530:8"]]
- 00babc8c bytes fdd50094
+ 00babd54 bytes f7d50094
~~~


<a id="compare-95a3d3f250b2670c04760b44f131d99c"></a>

### [`00babccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babccc.md) → [`00babd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd94.md) _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babccc.md#insn-00babce0)
- 新版 [`00babda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd94.md#insn-00babda8)

~~~diff
- 00babce0 ["INT_ADD", "register:40f0:8", ["const:babce0:8", "const:4:8"]]
- 00babce0 ["CALL", null, ["callee:00be1b60:8"]]
+ 00babda8 ["INT_ADD", "register:40f0:8", ["const:babda8:8", "const:4:8"]]
+ 00babda8 ["CALL", null, ["callee:00be1b60:8"]]
- 00babce0 bytes 74d70094
+ 00babda8 bytes 6ed70094
~~~


<a id="compare-21de2192ff92e4c96cdcf9232165bff0"></a>

### [`00babcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babcf8.md) → [`00babdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babdc0.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babcf8.md#insn-00babd3c)
- 新版 [`00babe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babdc0.md#insn-00babe04)

~~~diff
- 00babd3c ["INT_ADD", "register:40f0:8", ["const:babd3c:8", "const:4:8"]]
- 00babd3c ["CALL", null, ["callee:00babe28:8"]]
+ 00babe04 ["INT_ADD", "register:40f0:8", ["const:babe04:8", "const:4:8"]]
+ 00babe04 ["CALL", null, ["callee:00babe28:8"]]
- 00babd3c bytes 09000094
+ 00babe04 bytes 09000094
~~~


<a id="compare-537c7dfe5949551b0991e49dba029db7"></a>

### [`00babfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babfbc.md) → [`00bac084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac084.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac024.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babfbc.md#insn-00bac000)
- 新版 [`00bac0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac084.md#insn-00bac0c8)

~~~diff
- 00bac000 ["INT_ADD", "register:40f0:8", ["const:bac000:8", "const:4:8"]]
- 00bac000 ["CALL", null, ["callee:00bac0ec:8"]]
+ 00bac0c8 ["INT_ADD", "register:40f0:8", ["const:bac0c8:8", "const:4:8"]]
+ 00bac0c8 ["CALL", null, ["callee:00bac0ec:8"]]
- 00bac000 bytes 09000094
+ 00bac0c8 bytes 09000094
~~~


<a id="compare-64dba76161e8b54e199f6df6d6be75dd"></a>

### [`00bac508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac508.md) → [`00bac5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5d0.md) _ZNSt6__ndk17codecvtIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac51c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac508.md#insn-00bac51c)
- 新版 [`00bac5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5d0.md#insn-00bac5e4)

~~~diff
- 00bac51c ["INT_ADD", "register:40f0:8", ["const:bac51c:8", "const:4:8"]]
- 00bac51c ["CALL", null, ["callee:00be1b70:8"]]
+ 00bac5e4 ["INT_ADD", "register:40f0:8", ["const:bac5e4:8", "const:4:8"]]
+ 00bac5e4 ["CALL", null, ["callee:00be1b70:8"]]
- 00bac51c bytes 69d50094
+ 00bac5e4 bytes 63d50094
~~~


<a id="compare-6fddb17f64b3a3755741cf82c61dc7c1"></a>

### [`00bac534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac534.md) → [`00bac5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5fc.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac534.md#insn-00bac578)
- 新版 [`00bac640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5fc.md#insn-00bac640)

~~~diff
- 00bac578 ["INT_ADD", "register:40f0:8", ["const:bac578:8", "const:4:8"]]
- 00bac578 ["CALL", null, ["callee:00babe28:8"]]
+ 00bac640 ["INT_ADD", "register:40f0:8", ["const:bac640:8", "const:4:8"]]
+ 00bac640 ["CALL", null, ["callee:00babe28:8"]]
- 00bac578 bytes fafdff97
+ 00bac640 bytes fafdff97
~~~


<a id="compare-30715a4047a6f10f9c505418e7316ac9"></a>

### [`00bac59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac59c.md) → [`00bac664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac664.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac024.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac59c.md#insn-00bac5e0)
- 新版 [`00bac6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac664.md#insn-00bac6a8)

~~~diff
- 00bac5e0 ["INT_ADD", "register:40f0:8", ["const:bac5e0:8", "const:4:8"]]
- 00bac5e0 ["CALL", null, ["callee:00bac0ec:8"]]
+ 00bac6a8 ["INT_ADD", "register:40f0:8", ["const:bac6a8:8", "const:4:8"]]
+ 00bac6a8 ["CALL", null, ["callee:00bac0ec:8"]]
- 00bac5e0 bytes 91feff97
+ 00bac6a8 bytes 91feff97
~~~


<a id="compare-b8aba37f8a56cdc768e4fd57d65592c0"></a>

### [`00bac654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac654.md) → [`00bac71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac71c.md) _ZNSt6__ndk17codecvtIDic9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ad0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac654.md#insn-00bac668)
- 新版 [`00bac730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac71c.md#insn-00bac730)

~~~diff
- 00bac668 ["INT_ADD", "register:40f0:8", ["const:bac668:8", "const:4:8"]]
- 00bac668 ["CALL", null, ["callee:00be1b80:8"]]
+ 00bac730 ["INT_ADD", "register:40f0:8", ["const:bac730:8", "const:4:8"]]
+ 00bac730 ["CALL", null, ["callee:00be1b80:8"]]
- 00bac668 bytes 1ad50094
+ 00bac730 bytes 14d50094
~~~


<a id="compare-41a056006b2380631a1bd9daa0bde938"></a>

### [`00bac930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac930.md) → [`00bac9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac9f8.md) _ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac930.md#insn-00bac974)
- 新版 [`00baca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac9f8.md#insn-00baca3c)

~~~diff
- 00bac974 ["INT_ADD", "register:40f0:8", ["const:bac974:8", "const:4:8"]]
- 00bac974 ["CALL", null, ["callee:00baca60:8"]]
+ 00baca3c ["INT_ADD", "register:40f0:8", ["const:baca3c:8", "const:4:8"]]
+ 00baca3c ["CALL", null, ["callee:00baca60:8"]]
- 00bac974 bytes 09000094
+ 00baca3c bytes 09000094
~~~


<a id="compare-818900bb902e2bbff9f2752e0e691025"></a>

### [`00bace10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bace10.md) → [`00baced8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baced8.md) _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bace24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bace10.md#insn-00bace24)
- 新版 [`00baceec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baced8.md#insn-00baceec)

~~~diff
- 00bace24 ["INT_ADD", "register:40f0:8", ["const:bace24:8", "const:4:8"]]
- 00bace24 ["CALL", null, ["callee:00be1b90:8"]]
+ 00baceec ["INT_ADD", "register:40f0:8", ["const:baceec:8", "const:4:8"]]
+ 00baceec ["CALL", null, ["callee:00be1b90:8"]]
- 00bace24 bytes 2fd30094
+ 00baceec bytes 29d30094
~~~


<a id="compare-d42366992ebd9dc819d4f9473f4fc473"></a>

### [`00bacf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacf64.md) → [`00bad02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad02c.md) _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bacfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacf64.md#insn-00bacfa8)
- 新版 [`00bad070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad02c.md#insn-00bad070)

~~~diff
- 00bacfa8 ["INT_ADD", "register:40f0:8", ["const:bacfa8:8", "const:4:8"]]
- 00bacfa8 ["CALL", null, ["callee:00baca60:8"]]
+ 00bad070 ["INT_ADD", "register:40f0:8", ["const:bad070:8", "const:4:8"]]
+ 00bad070 ["CALL", null, ["callee:00baca60:8"]]
- 00bacfa8 bytes 7cfeff97
+ 00bad070 bytes 7cfeff97
~~~


<a id="compare-6146c6787dfd6fa98225abe4565ec448"></a>

### [`00bad01c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad01c.md) → [`00bad0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad0e4.md) _ZNKSt6__ndk114__codecvt_utf8IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac7a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac870.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad01c.md#insn-00bad068)
- 新版 [`00bad130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad0e4.md#insn-00bad130)

~~~diff
- 00bad068 ["INT_ADD", "register:40f0:8", ["const:bad068:8", "const:4:8"]]
- 00bad068 ["CALL", null, ["callee:00bac870:8"]]
+ 00bad130 ["INT_ADD", "register:40f0:8", ["const:bad130:8", "const:4:8"]]
+ 00bad130 ["CALL", null, ["callee:00bac870:8"]]
- 00bad068 bytes d0fdff97
+ 00bad130 bytes d0fdff97
~~~


<a id="compare-52af278fd933808f4f48e80bdc0c9c0a"></a>

### [`00bad08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad08c.md) → [`00bad154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad154.md) _ZNKSt6__ndk114__codecvt_utf8IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad08c.md#insn-00bad0d8)
- 新版 [`00bad1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad154.md#insn-00bad1a0)

~~~diff
- 00bad0d8 ["INT_ADD", "register:40f0:8", ["const:bad0d8:8", "const:4:8"]]
- 00bad0d8 ["CALL", null, ["callee:00baca60:8"]]
+ 00bad1a0 ["INT_ADD", "register:40f0:8", ["const:bad1a0:8", "const:4:8"]]
+ 00bad1a0 ["CALL", null, ["callee:00baca60:8"]]
- 00bad0d8 bytes 30feff97
+ 00bad1a0 bytes 30feff97
~~~


<a id="compare-4b2062255cdc9587db99d85d913bf9ad"></a>

### [`00bad5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad5ac.md) → [`00bad674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad674.md) _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac7a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac870.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad5f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad5ac.md#insn-00bad5f8)
- 新版 [`00bad6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad674.md#insn-00bad6c0)

~~~diff
- 00bad5f8 ["INT_ADD", "register:40f0:8", ["const:bad5f8:8", "const:4:8"]]
- 00bad5f8 ["CALL", null, ["callee:00bac870:8"]]
+ 00bad6c0 ["INT_ADD", "register:40f0:8", ["const:bad6c0:8", "const:4:8"]]
+ 00bad6c0 ["CALL", null, ["callee:00bac870:8"]]
- 00bad5f8 bytes 6cfcff97
+ 00bad6c0 bytes 6cfcff97
~~~


<a id="compare-5bfd43d764b752ac3ee8694a130c050b"></a>

### [`00bad61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad61c.md) → [`00bad6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad6e4.md) _ZNKSt6__ndk114__codecvt_utf8IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad61c.md#insn-00bad668)
- 新版 [`00bad730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad6e4.md#insn-00bad730)

~~~diff
- 00bad668 ["INT_ADD", "register:40f0:8", ["const:bad668:8", "const:4:8"]]
- 00bad668 ["CALL", null, ["callee:00baca60:8"]]
+ 00bad730 ["INT_ADD", "register:40f0:8", ["const:bad730:8", "const:4:8"]]
+ 00bad730 ["CALL", null, ["callee:00baca60:8"]]
- 00bad668 bytes ccfcff97
+ 00bad730 bytes ccfcff97
~~~


<a id="compare-55061ed8dafd5a03e7e20f7d93692b17"></a>

### [`00bae5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae5c0.md) → [`00bae688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae688.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae6f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae5c0.md#insn-00bae60c)
- 新版 [`00bae6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae688.md#insn-00bae6d4)

~~~diff
- 00bae60c ["INT_ADD", "register:40f0:8", ["const:bae60c:8", "const:4:8"]]
- 00bae60c ["CALL", null, ["callee:00bae6f8:8"]]
+ 00bae6d4 ["INT_ADD", "register:40f0:8", ["const:bae6d4:8", "const:4:8"]]
+ 00bae6d4 ["CALL", null, ["callee:00bae6f8:8"]]
- 00bae60c bytes 09000094
+ 00bae6d4 bytes 09000094
~~~


<a id="compare-ef828e9e46ee2588e336c7021e640faa"></a>

### [`00bae858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae858.md) → [`00bae920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae920.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae8c8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae990.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae858.md#insn-00bae8a4)
- 新版 [`00bae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae920.md#insn-00bae96c)

~~~diff
- 00bae8a4 ["INT_ADD", "register:40f0:8", ["const:bae8a4:8", "const:4:8"]]
- 00bae8a4 ["CALL", null, ["callee:00bae990:8"]]
+ 00bae96c ["INT_ADD", "register:40f0:8", ["const:bae96c:8", "const:4:8"]]
+ 00bae96c ["CALL", null, ["callee:00bae990:8"]]
- 00bae8a4 bytes 09000094
+ 00bae96c bytes 09000094
~~~


<a id="compare-51ad2266b2326229580058ac55568558"></a>

### [`00baebb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baebb8.md) → [`00baec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baec04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baebb8.md#insn-00baec04)
- 新版 [`00baeccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md#insn-00baeccc)

~~~diff
- 00baec04 ["INT_ADD", "register:40f0:8", ["const:baec04:8", "const:4:8"]]
- 00baec04 ["CALL", null, ["callee:00babe28:8"]]
+ 00baeccc ["INT_ADD", "register:40f0:8", ["const:baeccc:8", "const:4:8"]]
+ 00baeccc ["CALL", null, ["callee:00babe28:8"]]
- 00baec04 bytes 57f4ff97
+ 00baeccc bytes 57f4ff97
~~~


<a id="compare-0ba0ca15cb4608bb043b298f20b0cbb0"></a>

### [`00baec28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baec28.md) → [`00baecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baecf0.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac024.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baec74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baec28.md#insn-00baec74)
- 新版 [`00baed3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baecf0.md#insn-00baed3c)

~~~diff
- 00baec74 ["INT_ADD", "register:40f0:8", ["const:baec74:8", "const:4:8"]]
- 00baec74 ["CALL", null, ["callee:00bac0ec:8"]]
+ 00baed3c ["INT_ADD", "register:40f0:8", ["const:baed3c:8", "const:4:8"]]
+ 00baed3c ["CALL", null, ["callee:00bac0ec:8"]]
- 00baec74 bytes ecf4ff97
+ 00baed3c bytes ecf4ff97
~~~


<a id="compare-d9b5193dc229d47e684e6753ea7810e5"></a>

### [`00baecfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baecfc.md) → [`00baedc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baedc4.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae6f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baed48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baecfc.md#insn-00baed48)
- 新版 [`00baee10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baedc4.md#insn-00baee10)

~~~diff
- 00baed48 ["INT_ADD", "register:40f0:8", ["const:baed48:8", "const:4:8"]]
- 00baed48 ["CALL", null, ["callee:00bae6f8:8"]]
+ 00baee10 ["INT_ADD", "register:40f0:8", ["const:baee10:8", "const:4:8"]]
+ 00baee10 ["CALL", null, ["callee:00bae6f8:8"]]
- 00baed48 bytes 3afeff97
+ 00baee10 bytes 3afeff97
~~~


<a id="compare-ccb61dcffe4ee830b1d280bd467a4d00"></a>

### [`00baed6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baed6c.md) → [`00baee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baee34.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae8c8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae990.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baedb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baed6c.md#insn-00baedb8)
- 新版 [`00baee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baee34.md#insn-00baee80)

~~~diff
- 00baedb8 ["INT_ADD", "register:40f0:8", ["const:baedb8:8", "const:4:8"]]
- 00baedb8 ["CALL", null, ["callee:00bae990:8"]]
+ 00baee80 ["INT_ADD", "register:40f0:8", ["const:baee80:8", "const:4:8"]]
+ 00baee80 ["CALL", null, ["callee:00bae990:8"]]
- 00baedb8 bytes c4feff97
+ 00baee80 bytes c4feff97
~~~


<a id="compare-5da1f0d30f5979be13ab390467a256fe"></a>

### [`00baee40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee40.md) → [`00baef08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef08.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1af0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baee54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee40.md#insn-00baee54)
- 新版 [`00baef1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef08.md#insn-00baef1c)

~~~diff
- 00baee54 ["INT_ADD", "register:40f0:8", ["const:baee54:8", "const:4:8"]]
- 00baee54 ["CALL", null, ["callee:00be1ba0:8"]]
+ 00baef1c ["INT_ADD", "register:40f0:8", ["const:baef1c:8", "const:4:8"]]
+ 00baef1c ["CALL", null, ["callee:00be1ba0:8"]]
- 00baee54 bytes 27cb0094
+ 00baef1c bytes 21cb0094
~~~


<a id="compare-fdeb511748d4d63802ecb6f0b2779551"></a>

### [`00baee6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee6c.md) → [`00baef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef34.md) _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baee80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee6c.md#insn-00baee80)
- 新版 [`00baef48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef34.md#insn-00baef48)

~~~diff
- 00baee80 ["INT_ADD", "register:40f0:8", ["const:baee80:8", "const:4:8"]]
- 00baee80 ["CALL", null, ["callee:00be1bb0:8"]]
+ 00baef48 ["INT_ADD", "register:40f0:8", ["const:baef48:8", "const:4:8"]]
+ 00baef48 ["CALL", null, ["callee:00be1bb0:8"]]
- 00baee80 bytes 20cb0094
+ 00baef48 bytes 1acb0094
~~~


<a id="compare-b2b0fd8c0c396f1085ea4bae703a7043"></a>

### [`00baee98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee98.md) → [`00baef60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef60.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baee98.md#insn-00baeeac)
- 新版 [`00baef74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef60.md#insn-00baef74)

~~~diff
- 00baeeac ["INT_ADD", "register:40f0:8", ["const:baeeac:8", "const:4:8"]]
- 00baeeac ["CALL", null, ["callee:00be1bc0:8"]]
+ 00baef74 ["INT_ADD", "register:40f0:8", ["const:baef74:8", "const:4:8"]]
+ 00baef74 ["CALL", null, ["callee:00be1bc0:8"]]
- 00baeeac bytes 19cb0094
+ 00baef74 bytes 13cb0094
~~~


<a id="compare-9452ae0277af4a1ff67469544de3dcaf"></a>

### [`00baeec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baeec4.md) → [`00baef8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef8c.md) _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baeec4.md#insn-00baeed8)
- 新版 [`00baefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef8c.md#insn-00baefa0)

~~~diff
- 00baeed8 ["INT_ADD", "register:40f0:8", ["const:baeed8:8", "const:4:8"]]
- 00baeed8 ["CALL", null, ["callee:00be1bd0:8"]]
+ 00baefa0 ["INT_ADD", "register:40f0:8", ["const:baefa0:8", "const:4:8"]]
+ 00baefa0 ["CALL", null, ["callee:00be1bd0:8"]]
- 00baeed8 bytes 12cb0094
+ 00baefa0 bytes 0ccb0094
~~~


<a id="compare-17adff04e2490aaec46bc5377404ecc8"></a>

### [`00baef9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baef9c.md) → [`00baf064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf064.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baefb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baef9c.md#insn-00baefb0)
- 新版 [`00baf078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf064.md#insn-00baf078)

~~~diff
- 00baefb0 ["INT_ADD", "register:40f0:8", ["const:baefb0:8", "const:4:8"]]
- 00baefb0 ["CALL", null, ["callee:00be1bf0:8"]]
+ 00baf078 ["INT_ADD", "register:40f0:8", ["const:baf078:8", "const:4:8"]]
+ 00baf078 ["CALL", null, ["callee:00be1bf0:8"]]
- 00baefb0 bytes e4ca0094
+ 00baf078 bytes deca0094
~~~


<a id="compare-922046a1b641b993b9e2dd4c69ddc436"></a>

### [`00baf018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf018.md) → [`00baf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf0e0.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf018.md#insn-00baf02c)
- 新版 [`00baf0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf0e0.md#insn-00baf0f4)

~~~diff
- 00baf02c ["INT_ADD", "register:40f0:8", ["const:baf02c:8", "const:4:8"]]
- 00baf02c ["CALL", null, ["callee:00be1c10:8"]]
+ 00baf0f4 ["INT_ADD", "register:40f0:8", ["const:baf0f4:8", "const:4:8"]]
+ 00baf0f4 ["CALL", null, ["callee:00be1c10:8"]]
- 00baf02c bytes cdca0094
+ 00baf0f4 bytes c7ca0094
~~~


