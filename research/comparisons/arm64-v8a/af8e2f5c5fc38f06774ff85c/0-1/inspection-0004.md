# v15.7.2 → v15.7.3 · 要調査の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-f142531aac3cb20b5c0fb4fcb647e02a"></a>

### [`00b7d094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d094.md) → [`00b7d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d15c.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d094.md#insn-00b7d0c0) · [`00b7d0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d094.md#insn-00b7d0d4) · [`00b7d0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d094.md#insn-00b7d0e8)
- 新版 `00b7d188`（命令位置の公開資料なし） · `00b7d19c`（命令位置の公開資料なし） · `00b7d1b0`（命令位置の公開資料なし）

~~~diff
- 00b7d0c0 ["INT_ADD", "register:40f0:8", ["const:b7d0c0:8", "const:4:8"]]
- 00b7d0c0 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00b7d188 ["INT_ADD", "register:40f0:8", ["const:b7d188:8", "const:4:8"]]
+ 00b7d188 ["CALL", null, ["callee:00bd6e20:8"]]
- 00b7d0c0 bytes 28670194
+ 00b7d188 bytes 26670194
- 00b7d0d4 ["INT_ADD", "register:40f0:8", ["const:b7d0d4:8", "const:4:8"]]
- 00b7d0d4 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b7d19c ["INT_ADD", "register:40f0:8", ["const:b7d19c:8", "const:4:8"]]
+ 00b7d19c ["CALL", null, ["callee:00bd6e50:8"]]
- 00b7d0d4 bytes 2f670194
+ 00b7d19c bytes 2d670194
- 00b7d0e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7d0e8 ["INT_ADD", "register:40f0:8", ["const:b7d0e8:8", "const:4:8"]]
- 00b7d0e8 ["CALLIND", null, ["register:0:8"]]
+ 00b7d1b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7d1b0 ["INT_ADD", "register:40f0:8", ["const:b7d1b0:8", "const:4:8"]]
+ 00b7d1b0 ["CALLIND", null, ["register:0:8"]]
- 00b7d0e8 bytes 00013fd6
+ 00b7d1b0 bytes 00013fd6
~~~


<a id="compare-809a0e3ab589877763738d7241a1ae2c"></a>

### [`00b7d1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d1e0.md) → [`00b7d2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2a8.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1170.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d1e0.md#insn-00b7d1ec)
- 新版 `00b7d2b4`（命令位置の公開資料なし）

~~~diff
- 00b7d1ec ["INT_ADD", "register:40f0:8", ["const:b7d1ec:8", "const:4:8"]]
- 00b7d1ec ["CALL", null, ["callee:00be1220:8"]]
+ 00b7d2b4 ["INT_ADD", "register:40f0:8", ["const:b7d2b4:8", "const:4:8"]]
+ 00b7d2b4 ["CALL", null, ["callee:00be1220:8"]]
- 00b7d1ec bytes e18f0194
+ 00b7d2b4 bytes db8f0194
~~~


<a id="compare-2ddb39052b93a303ee9121862196c9d8"></a>

### [`00b7d208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d208.md) → [`00b7d2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2d0.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) · 呼出先 1件 [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d208.md#insn-00b7d214)
- 新版 `00b7d2dc`（命令位置の公開資料なし）

~~~diff
- 00b7d214 ["INT_ADD", "register:40f0:8", ["const:b7d214:8", "const:4:8"]]
- 00b7d214 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d2dc ["INT_ADD", "register:40f0:8", ["const:b7d2dc:8", "const:4:8"]]
+ 00b7d2dc ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d214 bytes 47850194
+ 00b7d2dc bytes 41850194
~~~


<a id="compare-d6afbc3e4740e528770a2c9adec3b318"></a>

### [`00b7d2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2cc.md) → [`00b7d394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d394.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd180.md) · 呼出先 1件 [`00bde710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bdd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md) · 呼出先 1件 [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2cc.md#insn-00b7d2d8)
- 新版 `00b7d3a0`（命令位置の公開資料なし）

~~~diff
- 00b7d2d8 ["INT_ADD", "register:40f0:8", ["const:b7d2d8:8", "const:4:8"]]
- 00b7d2d8 ["CALL", null, ["callee:00bde7c0:8"]]
+ 00b7d3a0 ["INT_ADD", "register:40f0:8", ["const:b7d3a0:8", "const:4:8"]]
+ 00b7d3a0 ["CALL", null, ["callee:00bde7c0:8"]]
- 00b7d2d8 bytes 0e850194
+ 00b7d3a0 bytes 08850194
~~~


<a id="compare-2841b99eba8f0ea2433e13599a6fdca1"></a>

### [`00b7d460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d460.md) → [`00b7d528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d528.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be1170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d460.md#insn-00b7d474) · [`00b7d4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d460.md#insn-00b7d4a0)
- 新版 `00b7d53c`（命令位置の公開資料なし） · `00b7d568`（命令位置の公開資料なし）

~~~diff
- 00b7d474 ["INT_ADD", "register:40f0:8", ["const:b7d474:8", "const:4:8"]]
- 00b7d474 ["CALL", null, ["callee:00be1220:8"]]
+ 00b7d53c ["INT_ADD", "register:40f0:8", ["const:b7d53c:8", "const:4:8"]]
+ 00b7d53c ["CALL", null, ["callee:00be1220:8"]]
- 00b7d474 bytes 3f8f0194
+ 00b7d53c bytes 398f0194
- 00b7d4a0 ["INT_ADD", "register:40f0:8", ["const:b7d4a0:8", "const:4:8"]]
- 00b7d4a0 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d568 ["INT_ADD", "register:40f0:8", ["const:b7d568:8", "const:4:8"]]
+ 00b7d568 ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d4a0 bytes a4840194
+ 00b7d568 bytes 9e840194
~~~


<a id="compare-3c6ea444e4f096ebf53f3e84e42b95d4"></a>

### [`00b7d664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d664.md) → [`00b7d72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d72c.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6d0.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be1170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d664.md#insn-00b7d67c) · [`00b7d688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d664.md#insn-00b7d688) · [`00b7d6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d664.md#insn-00b7d6c8)
- 新版 `00b7d744`（命令位置の公開資料なし） · `00b7d750`（命令位置の公開資料なし） · `00b7d790`（命令位置の公開資料なし）

~~~diff
- 00b7d67c ["INT_ADD", "register:40f0:8", ["const:b7d67c:8", "const:4:8"]]
- 00b7d67c ["CALL", null, ["callee:00bdb780:8"]]
+ 00b7d744 ["INT_ADD", "register:40f0:8", ["const:b7d744:8", "const:4:8"]]
+ 00b7d744 ["CALL", null, ["callee:00bdb780:8"]]
- 00b7d67c bytes 15780194
+ 00b7d744 bytes 0f780194
- 00b7d688 ["INT_ADD", "register:40f0:8", ["const:b7d688:8", "const:4:8"]]
- 00b7d688 ["CALL", null, ["callee:00be1220:8"]]
+ 00b7d750 ["INT_ADD", "register:40f0:8", ["const:b7d750:8", "const:4:8"]]
+ 00b7d750 ["CALL", null, ["callee:00be1220:8"]]
- 00b7d688 bytes ba8e0194
+ 00b7d750 bytes b48e0194
- 00b7d6c8 ["INT_ADD", "register:40f0:8", ["const:b7d6c8:8", "const:4:8"]]
- 00b7d6c8 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d790 ["INT_ADD", "register:40f0:8", ["const:b7d790:8", "const:4:8"]]
+ 00b7d790 ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d6c8 bytes 1a840194
+ 00b7d790 bytes 14840194
~~~


<a id="compare-c832b15ab14a3689094625295e06d025"></a>

### [`00b7d768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d768.md) → [`00b7d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d830.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb230.md) · 呼出先 1件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bdb2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2e0.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d768.md#insn-00b7d784)
- 新版 `00b7d84c`（命令位置の公開資料なし）

~~~diff
- 00b7d784 ["INT_ADD", "register:40f0:8", ["const:b7d784:8", "const:4:8"]]
- 00b7d784 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b7d84c ["INT_ADD", "register:40f0:8", ["const:b7d84c:8", "const:4:8"]]
+ 00b7d84c ["CALL", null, ["callee:00bdb180:8"]]
- 00b7d784 bytes 53760194
+ 00b7d84c bytes 4d760194
~~~


<a id="compare-832ce4adce4c0bcc74362b0d546c462f"></a>

### [`00b7d81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d81c.md) → [`00b7d8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d8e4.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1190.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d81c.md#insn-00b7d82c)
- 新版 `00b7d8f4`（命令位置の公開資料なし）

~~~diff
- 00b7d82c ["INT_ADD", "register:40f0:8", ["const:b7d82c:8", "const:4:8"]]
- 00b7d82c ["CALL", null, ["callee:00be1240:8"]]
+ 00b7d8f4 ["INT_ADD", "register:40f0:8", ["const:b7d8f4:8", "const:4:8"]]
+ 00b7d8f4 ["CALL", null, ["callee:00be1240:8"]]
- 00b7d82c bytes 598e0194
+ 00b7d8f4 bytes 538e0194
~~~


<a id="compare-20318cc17adad6856da1905f6c16ec7c"></a>

### [`00b7d848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d848.md) → [`00b7d910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d910.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb540.md) · 呼出先 2件 [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be11a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11a0.md)
- 新版 呼出元 1件 [`00bdb5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5f0.md) · 呼出先 2件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d848.md#insn-00b7d89c) · [`00b7d8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d848.md#insn-00b7d8a8)
- 新版 `00b7d964`（命令位置の公開資料なし） · `00b7d970`（命令位置の公開資料なし）

~~~diff
- 00b7d89c ["INT_ADD", "register:40f0:8", ["const:b7d89c:8", "const:4:8"]]
- 00b7d89c ["CALL", null, ["callee:00be1250:8"]]
+ 00b7d964 ["INT_ADD", "register:40f0:8", ["const:b7d964:8", "const:4:8"]]
+ 00b7d964 ["CALL", null, ["callee:00be1250:8"]]
- 00b7d89c bytes 418e0194
+ 00b7d964 bytes 3b8e0194
- 00b7d8a8 ["INT_ADD", "register:40f0:8", ["const:b7d8a8:8", "const:4:8"]]
- 00b7d8a8 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b7d970 ["INT_ADD", "register:40f0:8", ["const:b7d970:8", "const:4:8"]]
+ 00b7d970 ["CALL", null, ["callee:00bdb220:8"]]
- 00b7d8a8 bytes 32760194
+ 00b7d970 bytes 2c760194
~~~


<a id="compare-083341a30c7fb4b0600e41951e65d472"></a>

### [`00b7db48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7db48.md) → [`00b7dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md) FUN_00b7dc10

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7dcc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcc4.md) · 呼出先 5件 [`00b7dce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dce8.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00b7dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd8c.md) · 呼出先 5件 [`00b7ddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dbbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7db48.md#insn-00b7dbbc) · [`00b7dbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7db48.md#insn-00b7dbf0) · [`00b7dc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7db48.md#insn-00b7dc04)
- 新版 `00b7dc84`（命令位置の公開資料なし） · `00b7dcb8`（命令位置の公開資料なし） · `00b7dccc`（命令位置の公開資料なし）

~~~diff
- 00b7dbbc ["INT_ADD", "register:40f0:8", ["const:b7dbbc:8", "const:4:8"]]
- 00b7dbbc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7dc84 ["INT_ADD", "register:40f0:8", ["const:b7dc84:8", "const:4:8"]]
+ 00b7dc84 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7dbbc bytes e1740194
+ 00b7dc84 bytes db740194
- 00b7dbf0 ["INT_ADD", "register:40f0:8", ["const:b7dbf0:8", "const:4:8"]]
- 00b7dbf0 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b7dcb8 ["INT_ADD", "register:40f0:8", ["const:b7dcb8:8", "const:4:8"]]
+ 00b7dcb8 ["CALL", null, ["callee:00bdb160:8"]]
- 00b7dbf0 bytes 30750194
+ 00b7dcb8 bytes 2a750194
- 00b7dc04 ["INT_ADD", "register:40f0:8", ["const:b7dc04:8", "const:4:8"]]
- 00b7dc04 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b7dccc ["INT_ADD", "register:40f0:8", ["const:b7dccc:8", "const:4:8"]]
+ 00b7dccc ["CALL", null, ["callee:00bdb010:8"]]
- 00b7dc04 bytes d7740194
+ 00b7dccc bytes d1740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affc6f5ebf659faea232e1d1268c140c"></a>

### [`00b7dd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd00.md) → [`00b7ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddc8.md) FUN_00b7ddc8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7d94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd00.md#insn-00b7dd1c)
- 新版 `00b7dde4`（命令位置の公開資料なし）

~~~diff
- 00b7dd1c ["INT_ADD", "register:40f0:8", ["const:b7dd1c:8", "const:4:8"]]
- 00b7dd1c ["CALL", null, ["callee:00bdb2b0:8"]]
+ 00b7dde4 ["INT_ADD", "register:40f0:8", ["const:b7dde4:8", "const:4:8"]]
+ 00b7dde4 ["CALL", null, ["callee:00bdb2b0:8"]]
- 00b7dd1c bytes 39750194
+ 00b7dde4 bytes 33750194
~~~


<a id="compare-6aadf55b8fc9a4b4e61480b0323de9ad"></a>

### [`00b7dddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dddc.md) → [`00b7dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md) _ZNSt6__ndk113random_deviceD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053d8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d8b4.md) [`00bdb480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb480.md) · 呼出先 1件 [`00bdc880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc880.md)
- 新版 呼出元 2件 [`0053d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md) [`00bdb530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb530.md) · 呼出先 1件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ddec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dddc.md#insn-00b7ddec)
- 新版 `00b7deb4`（命令位置の公開資料なし）

~~~diff
- 00b7ddec ["INT_ADD", "register:40f0:8", ["const:b7ddec:8", "const:4:8"]]
- 00b7ddec ["CALL", null, ["callee:00bdc930:8"]]
+ 00b7deb4 ["INT_ADD", "register:40f0:8", ["const:b7deb4:8", "const:4:8"]]
+ 00b7deb4 ["CALL", null, ["callee:00bdc930:8"]]
- 00b7ddec bytes a57a0194
+ 00b7deb4 bytes 9f7a0194
~~~


<a id="compare-5b3c32cf3d4710c8e398c48ab9a695c5"></a>

### [`00b7e55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e55c.md) → [`00b7e624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e624.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be11f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be12a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e55c.md#insn-00b7e570)
- 新版 `00b7e638`（命令位置の公開資料なし）

~~~diff
- 00b7e570 ["INT_ADD", "register:40f0:8", ["const:b7e570:8", "const:4:8"]]
- 00b7e570 ["CALL", null, ["callee:00be12a0:8"]]
+ 00b7e638 ["INT_ADD", "register:40f0:8", ["const:b7e638:8", "const:4:8"]]
+ 00b7e638 ["CALL", null, ["callee:00be12a0:8"]]
- 00b7e570 bytes 208b0194
+ 00b7e638 bytes 1a8b0194
~~~


<a id="compare-2d43034bb3d2cdcd95a7d16212232f41"></a>

### [`00b7e6b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e6b4.md) → [`00b7e77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e77c.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1210.md) · 呼出先 5件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00be0e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e80.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 1件 [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md) · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e6b4.md#insn-00b7e6e8) · [`00b7e6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e6b4.md#insn-00b7e6f8) · [`00b7e724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e6b4.md#insn-00b7e724)
- 新版 `00b7e7b0`（命令位置の公開資料なし） · `00b7e7c0`（命令位置の公開資料なし） · `00b7e7ec`（命令位置の公開資料なし）

~~~diff
- 00b7e6e8 ["INT_ADD", "register:40f0:8", ["const:b7e6e8:8", "const:4:8"]]
- 00b7e6e8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00b7e7b0 ["INT_ADD", "register:40f0:8", ["const:b7e7b0:8", "const:4:8"]]
+ 00b7e7b0 ["CALL", null, ["callee:00bdd180:8"]]
- 00b7e6e8 bytes 7a7a0194
+ 00b7e7b0 bytes 747a0194
- 00b7e6f8 ["INT_ADD", "register:40f0:8", ["const:b7e6f8:8", "const:4:8"]]
- 00b7e6f8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00b7e7c0 ["INT_ADD", "register:40f0:8", ["const:b7e7c0:8", "const:4:8"]]
+ 00b7e7c0 ["CALL", null, ["callee:00bdd180:8"]]
- 00b7e6f8 bytes 767a0194
+ 00b7e7c0 bytes 707a0194
- 00b7e724 ["INT_ADD", "register:40f0:8", ["const:b7e724:8", "const:4:8"]]
- 00b7e724 ["CALL", null, ["callee:00bdd180:8"]]
+ 00b7e7ec ["INT_ADD", "register:40f0:8", ["const:b7e7ec:8", "const:4:8"]]
+ 00b7e7ec ["CALL", null, ["callee:00bdd180:8"]]
- 00b7e724 bytes 6b7a0194
+ 00b7e7ec bytes 657a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-327d7153a5ee9dbe142906fb83e152fe"></a>

### [`00b7e974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e974.md) → [`00b7ea3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ea3c.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e974.md#insn-00b7e9b0)
- 新版 `00b7ea78`（命令位置の公開資料なし）

~~~diff
- 00b7e9b0 ["INT_ADD", "register:40f0:8", ["const:b7e9b0:8", "const:4:8"]]
- 00b7e9b0 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b7ea78 ["INT_ADD", "register:40f0:8", ["const:b7ea78:8", "const:4:8"]]
+ 00b7ea78 ["CALL", null, ["callee:00bdd930:8"]]
- 00b7e9b0 bytes b47b0194
+ 00b7ea78 bytes ae7b0194
~~~


<a id="compare-cfaf8890dc3234b7492c3ebb1d6487b7"></a>

### [`00b7ea10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ea10.md) → [`00b7ead8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ead8.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md) · 呼出先 3件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ea84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ea10.md#insn-00b7ea84) · [`00b7ea90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ea10.md#insn-00b7ea90) · [`00b7ea9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ea10.md#insn-00b7ea9c)
- 新版 `00b7eb4c`（命令位置の公開資料なし） · `00b7eb58`（命令位置の公開資料なし） · `00b7eb64`（命令位置の公開資料なし）

~~~diff
- 00b7ea84 ["INT_ADD", "register:40f0:8", ["const:b7ea84:8", "const:4:8"]]
- 00b7ea84 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b7eb4c ["INT_ADD", "register:40f0:8", ["const:b7eb4c:8", "const:4:8"]]
+ 00b7eb4c ["CALL", null, ["callee:00bdd930:8"]]
- 00b7ea84 bytes 7f7b0194
+ 00b7eb4c bytes 797b0194
- 00b7ea90 ["INT_ADD", "register:40f0:8", ["const:b7ea90:8", "const:4:8"]]
- 00b7ea90 ["CALL", null, ["callee:00be1290:8"]]
+ 00b7eb58 ["INT_ADD", "register:40f0:8", ["const:b7eb58:8", "const:4:8"]]
+ 00b7eb58 ["CALL", null, ["callee:00be1290:8"]]
- 00b7ea90 bytes d4890194
+ 00b7eb58 bytes ce890194
- 00b7ea9c ["INT_ADD", "register:40f0:8", ["const:b7ea9c:8", "const:4:8"]]
- 00b7ea9c ["CALL", null, ["callee:00be1290:8"]]
+ 00b7eb64 ["INT_ADD", "register:40f0:8", ["const:b7eb64:8", "const:4:8"]]
+ 00b7eb64 ["CALL", null, ["callee:00be1290:8"]]
- 00b7ea9c bytes d1890194
+ 00b7eb64 bytes cb890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-428407535e19da1e1af5896979219d66"></a>

### [`00b7eb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb2c.md) → [`00b7ebf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ebf4.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb370.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 1件 [`00bdb420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb420.md) · 呼出先 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb2c.md#insn-00b7eb54)
- 新版 `00b7ec1c`（命令位置の公開資料なし）

~~~diff
- 00b7eb54 ["INT_ADD", "register:40f0:8", ["const:b7eb54:8", "const:4:8"]]
- 00b7eb54 ["CALL", null, ["callee:00bdb660:8"]]
+ 00b7ec1c ["INT_ADD", "register:40f0:8", ["const:b7ec1c:8", "const:4:8"]]
+ 00b7ec1c ["CALL", null, ["callee:00bdb660:8"]]
- 00b7eb54 bytes 97720194
+ 00b7ec1c bytes 91720194
~~~


<a id="compare-80502ff9af79794739c406684b121f81"></a>

### [`00b7eb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb58.md) → [`00b7ec20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec20.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1230.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 1件 [`00be12e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12e0.md) · 呼出先 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb58.md#insn-00b7eb80)
- 新版 `00b7ec48`（命令位置の公開資料なし）

~~~diff
- 00b7eb80 ["INT_ADD", "register:40f0:8", ["const:b7eb80:8", "const:4:8"]]
- 00b7eb80 ["CALL", null, ["callee:00bdb660:8"]]
+ 00b7ec48 ["INT_ADD", "register:40f0:8", ["const:b7ec48:8", "const:4:8"]]
+ 00b7ec48 ["CALL", null, ["callee:00bdb660:8"]]
- 00b7eb80 bytes 8c720194
+ 00b7ec48 bytes 86720194
~~~


<a id="compare-7e19395cda486035ddcf55167d085243"></a>

### [`00b7eba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eba0.md) → [`00b7ec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec68.md) FUN_00b7ec68

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ebb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eba0.md#insn-00b7ebb4)
- 新版 `00b7ec7c`（命令位置の公開資料なし）

~~~diff
- 00b7ebb4 ["INT_ADD", "register:40f0:8", ["const:b7ebb4:8", "const:4:8"]]
- 00b7ebb4 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b7ec7c ["INT_ADD", "register:40f0:8", ["const:b7ec7c:8", "const:4:8"]]
+ 00b7ec7c ["CALL", null, ["callee:00be0ea0:8"]]
- 00b7ebb4 bytes 8f880194
+ 00b7ec7c bytes 89880194
~~~


<a id="compare-8a85e81c03e50f3dc0f978325c4d9537"></a>

### [`00b7ebd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ebd4.md) → [`00b7ec9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec9c.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1240.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be12f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ebe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ebd4.md#insn-00b7ebe8)
- 新版 `00b7ecb0`（命令位置の公開資料なし）

~~~diff
- 00b7ebe8 ["INT_ADD", "register:40f0:8", ["const:b7ebe8:8", "const:4:8"]]
- 00b7ebe8 ["CALL", null, ["callee:00be12f0:8"]]
+ 00b7ecb0 ["INT_ADD", "register:40f0:8", ["const:b7ecb0:8", "const:4:8"]]
+ 00b7ecb0 ["CALL", null, ["callee:00be12f0:8"]]
- 00b7ebe8 bytes 96890194
+ 00b7ecb0 bytes 90890194
~~~


<a id="compare-a2897213b83eeb79c53fc72787b17a37"></a>

### [`00b7ec00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec00.md) → [`00b7ecc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ecc8.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be11d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11d0.md) [`00be1210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec00.md#insn-00b7ec28) · [`00b7ec34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec00.md#insn-00b7ec34) · [`00b7ec50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec00.md#insn-00b7ec50)
- 新版 `00b7ecf0`（命令位置の公開資料なし） · `00b7ecfc`（命令位置の公開資料なし） · `00b7ed18`（命令位置の公開資料なし）

~~~diff
- 00b7ec28 ["INT_ADD", "register:40f0:8", ["const:b7ec28:8", "const:4:8"]]
- 00b7ec28 ["CALL", null, ["callee:00be1280:8"]]
+ 00b7ecf0 ["INT_ADD", "register:40f0:8", ["const:b7ecf0:8", "const:4:8"]]
+ 00b7ecf0 ["CALL", null, ["callee:00be1280:8"]]
- 00b7ec28 bytes 6a890194
+ 00b7ecf0 bytes 64890194
- 00b7ec34 ["INT_ADD", "register:40f0:8", ["const:b7ec34:8", "const:4:8"]]
- 00b7ec34 ["CALL", null, ["callee:00be12c0:8"]]
+ 00b7ecfc ["INT_ADD", "register:40f0:8", ["const:b7ecfc:8", "const:4:8"]]
+ 00b7ecfc ["CALL", null, ["callee:00be12c0:8"]]
- 00b7ec34 bytes 77890194
+ 00b7ecfc bytes 71890194
- 00b7ec50 ["INT_ADD", "register:40f0:8", ["const:b7ec50:8", "const:4:8"]]
- 00b7ec50 ["CALL", null, ["callee:00be1280:8"]]
+ 00b7ed18 ["INT_ADD", "register:40f0:8", ["const:b7ed18:8", "const:4:8"]]
+ 00b7ed18 ["CALL", null, ["callee:00be1280:8"]]
- 00b7ec50 bytes 60890194
+ 00b7ed18 bytes 5a890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd109e6bc89e550cd2f55ba3117fe85c"></a>

### [`00b7ec94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec94.md) → [`00b7ed5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed5c.md) FUN_00b7ed5c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ec94.md#insn-00b7eca8)
- 新版 `00b7ed70`（命令位置の公開資料なし）

~~~diff
- 00b7eca8 ["INT_ADD", "register:40f0:8", ["const:b7eca8:8", "const:4:8"]]
- 00b7eca8 ["CALL", null, ["callee:00be1300:8"]]
+ 00b7ed70 ["INT_ADD", "register:40f0:8", ["const:b7ed70:8", "const:4:8"]]
+ 00b7ed70 ["CALL", null, ["callee:00be1300:8"]]
- 00b7eca8 bytes 6a890194
+ 00b7ed70 bytes 64890194
~~~


<a id="compare-1655a145f6f0dc88a3a369638e0bb52c"></a>

### [`00b7ecc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ecc0.md) → [`00b7ed88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ece8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ecc0.md#insn-00b7ece8) · [`00b7ecf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ecc0.md#insn-00b7ecf4)
- 新版 `00b7edb0`（命令位置の公開資料なし） · `00b7edbc`（命令位置の公開資料なし）

~~~diff
- 00b7ece8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7ece8 ["INT_ADD", "register:40f0:8", ["const:b7ece8:8", "const:4:8"]]
- 00b7ece8 ["CALLIND", null, ["register:0:8"]]
+ 00b7edb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b7edb0 ["INT_ADD", "register:40f0:8", ["const:b7edb0:8", "const:4:8"]]
+ 00b7edb0 ["CALLIND", null, ["register:0:8"]]
- 00b7ece8 bytes 20013fd6
+ 00b7edb0 bytes 20013fd6
- 00b7ecf4 ["INT_ADD", "register:40f0:8", ["const:b7ecf4:8", "const:4:8"]]
- 00b7ecf4 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b7edbc ["INT_ADD", "register:40f0:8", ["const:b7edbc:8", "const:4:8"]]
+ 00b7edbc ["CALL", null, ["callee:00bdd930:8"]]
- 00b7ecf4 bytes e37a0194
+ 00b7edbc bytes dd7a0194
~~~


<a id="compare-c848db2fa949d3e2f1a65c1b9a32f954"></a>

### [`00b7ed88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ed88.md) → [`00b7ee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ee50.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7edc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ed88.md#insn-00b7edc8)
- 新版 `00b7ee90`（命令位置の公開資料なし）

~~~diff
- 00b7edc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7edc8 ["INT_ADD", "register:40f0:8", ["const:b7edc8:8", "const:4:8"]]
- 00b7edc8 ["CALLIND", null, ["register:0:8"]]
+ 00b7ee90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7ee90 ["INT_ADD", "register:40f0:8", ["const:b7ee90:8", "const:4:8"]]
+ 00b7ee90 ["CALLIND", null, ["register:0:8"]]
- 00b7edc8 bytes 00013fd6
+ 00b7ee90 bytes 00013fd6
~~~


<a id="compare-92f8558bc13c64cb8c217d46b8a310a1"></a>

### [`00b7efbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7efbc.md) → [`00b7f084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f084.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7efdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7efbc.md#insn-00b7efdc)
- 新版 `00b7f0a4`（命令位置の公開資料なし）

~~~diff
- 00b7efdc ["INT_ADD", "register:40f0:8", ["const:b7efdc:8", "const:4:8"]]
- 00b7efdc ["CALL", null, ["callee:00be1290:8"]]
+ 00b7f0a4 ["INT_ADD", "register:40f0:8", ["const:b7f0a4:8", "const:4:8"]]
+ 00b7f0a4 ["CALL", null, ["callee:00be1290:8"]]
- 00b7efdc bytes 81880194
+ 00b7f0a4 bytes 7b880194
~~~


<a id="compare-d237342f0082be563588579a77995b94"></a>

### [`00b7f00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f00c.md) → [`00b7f0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f0d4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f00c.md#insn-00b7f030) · [`00b7f03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f00c.md#insn-00b7f03c) · [`00b7f048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f00c.md#insn-00b7f048)
- 新版 `00b7f0f8`（命令位置の公開資料なし） · `00b7f104`（命令位置の公開資料なし） · `00b7f110`（命令位置の公開資料なし）

~~~diff
- 00b7f030 ["INT_ADD", "register:40f0:8", ["const:b7f030:8", "const:4:8"]]
- 00b7f030 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b7f0f8 ["INT_ADD", "register:40f0:8", ["const:b7f0f8:8", "const:4:8"]]
+ 00b7f0f8 ["CALL", null, ["callee:00bdd930:8"]]
- 00b7f030 bytes 147a0194
+ 00b7f0f8 bytes 0e7a0194
- 00b7f03c ["INT_ADD", "register:40f0:8", ["const:b7f03c:8", "const:4:8"]]
- 00b7f03c ["CALL", null, ["callee:00be1290:8"]]
+ 00b7f104 ["INT_ADD", "register:40f0:8", ["const:b7f104:8", "const:4:8"]]
+ 00b7f104 ["CALL", null, ["callee:00be1290:8"]]
- 00b7f03c bytes 69880194
+ 00b7f104 bytes 63880194
- 00b7f048 ["INT_ADD", "register:40f0:8", ["const:b7f048:8", "const:4:8"]]
- 00b7f048 ["CALL", null, ["callee:00be1290:8"]]
+ 00b7f110 ["INT_ADD", "register:40f0:8", ["const:b7f110:8", "const:4:8"]]
+ 00b7f110 ["CALL", null, ["callee:00be1290:8"]]
- 00b7f048 bytes 66880194
+ 00b7f110 bytes 60880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-094ef699da74ba443607f8d104aad0c0"></a>

### [`00b7f110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f110.md) → [`00b7f1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f1d8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f110.md#insn-00b7f14c)
- 新版 `00b7f214`（命令位置の公開資料なし）

~~~diff
- 00b7f14c ["INT_ADD", "register:40f0:8", ["const:b7f14c:8", "const:4:8"]]
- 00b7f14c ["CALL", null, ["callee:00bdb340:8"]]
+ 00b7f214 ["INT_ADD", "register:40f0:8", ["const:b7f214:8", "const:4:8"]]
+ 00b7f214 ["CALL", null, ["callee:00bdb340:8"]]
- 00b7f14c bytes 51700194
+ 00b7f214 bytes 4b700194
~~~


<a id="compare-00d75f9917bf9f32d3f200fca356592e"></a>

### [`00b7f1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f1e0.md) → [`00b7f2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f2a8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f1e0.md#insn-00b7f218)
- 新版 `00b7f2e0`（命令位置の公開資料なし）

~~~diff
- 00b7f218 ["INT_ADD", "register:40f0:8", ["const:b7f218:8", "const:4:8"]]
- 00b7f218 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b7f2e0 ["INT_ADD", "register:40f0:8", ["const:b7f2e0:8", "const:4:8"]]
+ 00b7f2e0 ["CALL", null, ["callee:00be12d0:8"]]
- 00b7f218 bytes 02880194
+ 00b7f2e0 bytes fc870194
~~~


<a id="compare-5beaa1ef660e97abb4f28025b10daeb7"></a>

### [`00b7f430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f430.md) → [`00b7f4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f4f8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f430.md#insn-00b7f450)
- 新版 `00b7f518`（命令位置の公開資料なし）

~~~diff
- 00b7f450 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f450 ["INT_ADD", "register:40f0:8", ["const:b7f450:8", "const:4:8"]]
- 00b7f450 ["CALLIND", null, ["register:0:8"]]
+ 00b7f518 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b7f518 ["INT_ADD", "register:40f0:8", ["const:b7f518:8", "const:4:8"]]
+ 00b7f518 ["CALLIND", null, ["register:0:8"]]
- 00b7f450 bytes 20003fd6
+ 00b7f518 bytes 20003fd6
~~~


<a id="compare-ec3fa39f284cadd90ffb4b77434eef5a"></a>

### [`00b7f468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f468.md) → [`00b7f530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f530.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f468.md#insn-00b7f488)
- 新版 `00b7f550`（命令位置の公開資料なし）

~~~diff
- 00b7f488 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f488 ["INT_ADD", "register:40f0:8", ["const:b7f488:8", "const:4:8"]]
- 00b7f488 ["CALLIND", null, ["register:0:8"]]
+ 00b7f550 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b7f550 ["INT_ADD", "register:40f0:8", ["const:b7f550:8", "const:4:8"]]
+ 00b7f550 ["CALLIND", null, ["register:0:8"]]
- 00b7f488 bytes 20003fd6
+ 00b7f550 bytes 20003fd6
~~~


<a id="compare-b14f03c60fea1edc2f54b777b47d6578"></a>

### [`00b7f4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f4a0.md) → [`00b7f568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f568.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f4a0.md#insn-00b7f4d0) · [`00b7f534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f4a0.md#insn-00b7f534) · [`00b7f56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f4a0.md#insn-00b7f56c)
- 新版 `00b7f598`（命令位置の公開資料なし） · `00b7f5fc`（命令位置の公開資料なし） · `00b7f634`（命令位置の公開資料なし）

~~~diff
- 00b7f4d0 ["INT_ADD", "register:40f0:8", ["const:b7f4d0:8", "const:4:8"]]
- 00b7f4d0 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7f598 ["INT_ADD", "register:40f0:8", ["const:b7f598:8", "const:4:8"]]
+ 00b7f598 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7f4d0 bytes 6c760194
+ 00b7f598 bytes 66760194
- 00b7f534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f534 ["INT_ADD", "register:40f0:8", ["const:b7f534:8", "const:4:8"]]
- 00b7f534 ["CALLIND", null, ["register:0:8"]]
+ 00b7f5fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7f5fc ["INT_ADD", "register:40f0:8", ["const:b7f5fc:8", "const:4:8"]]
+ 00b7f5fc ["CALLIND", null, ["register:0:8"]]
- 00b7f534 bytes 00013fd6
+ 00b7f5fc bytes 00013fd6
- 00b7f56c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f56c ["INT_ADD", "register:40f0:8", ["const:b7f56c:8", "const:4:8"]]
- 00b7f56c ["CALLIND", null, ["register:0:8"]]
+ 00b7f634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7f634 ["INT_ADD", "register:40f0:8", ["const:b7f634:8", "const:4:8"]]
+ 00b7f634 ["CALLIND", null, ["register:0:8"]]
- 00b7f56c bytes 00013fd6
+ 00b7f634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18d2406af692ffd511135bb2817c19d6"></a>

### [`00b807c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b807c8.md) → [`00b80890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80890.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1260.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b807e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b807c8.md#insn-00b807e0)
- 新版 `00b808a8`（命令位置の公開資料なし）

~~~diff
- 00b807e0 ["INT_ADD", "register:40f0:8", ["const:b807e0:8", "const:4:8"]]
- 00b807e0 ["CALL", null, ["callee:00be1310:8"]]
+ 00b808a8 ["INT_ADD", "register:40f0:8", ["const:b808a8:8", "const:4:8"]]
+ 00b808a8 ["CALL", null, ["callee:00be1310:8"]]
- 00b807e0 bytes a0820194
+ 00b808a8 bytes 9a820194
~~~


<a id="compare-3fae535fde45dac063d4e40e71858f25"></a>

### [`00b808a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b808a8.md) → [`00b80970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80970.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1270.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00be1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1320.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b808e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b808a8.md#insn-00b808e4) · [`00b80960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b808a8.md#insn-00b80960) · [`00b809a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b808a8.md#insn-00b809a0)
- 新版 `00b809ac`（命令位置の公開資料なし） · `00b80a28`（命令位置の公開資料なし） · `00b80a68`（命令位置の公開資料なし）

~~~diff
- 00b808e4 ["INT_ADD", "register:40f0:8", ["const:b808e4:8", "const:4:8"]]
- 00b808e4 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b809ac ["INT_ADD", "register:40f0:8", ["const:b809ac:8", "const:4:8"]]
+ 00b809ac ["CALL", null, ["callee:00bdcf30:8"]]
- 00b808e4 bytes 67710194
+ 00b809ac bytes 61710194
- 00b80960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80960 ["INT_ADD", "register:40f0:8", ["const:b80960:8", "const:4:8"]]
- 00b80960 ["CALLIND", null, ["register:0:8"]]
+ 00b80a28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80a28 ["INT_ADD", "register:40f0:8", ["const:b80a28:8", "const:4:8"]]
+ 00b80a28 ["CALLIND", null, ["register:0:8"]]
- 00b80960 bytes 00013fd6
+ 00b80a28 bytes 00013fd6
- 00b809a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b809a0 ["INT_ADD", "register:40f0:8", ["const:b809a0:8", "const:4:8"]]
- 00b809a0 ["CALLIND", null, ["register:0:8"]]
+ 00b80a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80a68 ["INT_ADD", "register:40f0:8", ["const:b80a68:8", "const:4:8"]]
+ 00b80a68 ["CALLIND", null, ["register:0:8"]]
- 00b809a0 bytes 00013fd6
+ 00b80a68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469167ea64f6cc07b9935c9958dd3a10"></a>

### [`00b80b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80b10.md) → [`00b80bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80bd8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1280.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00be1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1330.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80b10.md#insn-00b80b44) · [`00b80ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80b10.md#insn-00b80ba8) · [`00b80bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80b10.md#insn-00b80bec)
- 新版 `00b80c0c`（命令位置の公開資料なし） · `00b80c70`（命令位置の公開資料なし） · `00b80cb4`（命令位置の公開資料なし）

~~~diff
- 00b80b44 ["INT_ADD", "register:40f0:8", ["const:b80b44:8", "const:4:8"]]
- 00b80b44 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b80c0c ["INT_ADD", "register:40f0:8", ["const:b80c0c:8", "const:4:8"]]
+ 00b80c0c ["CALL", null, ["callee:00bdcf30:8"]]
- 00b80b44 bytes cf700194
+ 00b80c0c bytes c9700194
- 00b80ba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80ba8 ["INT_ADD", "register:40f0:8", ["const:b80ba8:8", "const:4:8"]]
- 00b80ba8 ["CALLIND", null, ["register:0:8"]]
+ 00b80c70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80c70 ["INT_ADD", "register:40f0:8", ["const:b80c70:8", "const:4:8"]]
+ 00b80c70 ["CALLIND", null, ["register:0:8"]]
- 00b80ba8 bytes 00013fd6
+ 00b80c70 bytes 00013fd6
- 00b80bec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80bec ["INT_ADD", "register:40f0:8", ["const:b80bec:8", "const:4:8"]]
- 00b80bec ["CALLIND", null, ["register:0:8"]]
+ 00b80cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80cb4 ["INT_ADD", "register:40f0:8", ["const:b80cb4:8", "const:4:8"]]
+ 00b80cb4 ["CALLIND", null, ["register:0:8"]]
- 00b80bec bytes 00013fd6
+ 00b80cb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04964e28e0593d98a887bed6a3479c2e"></a>

### [`00b80d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80d24.md) → [`00b80dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80dec.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1290.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00be1340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1340.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80d24.md#insn-00b80d64) · [`00b80da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80d24.md#insn-00b80da8) · [`00b80e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80d24.md#insn-00b80e00)
- 新版 `00b80e2c`（命令位置の公開資料なし） · `00b80e70`（命令位置の公開資料なし） · `00b80ec8`（命令位置の公開資料なし）

~~~diff
- 00b80d64 ["INT_ADD", "register:40f0:8", ["const:b80d64:8", "const:4:8"]]
- 00b80d64 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b80e2c ["INT_ADD", "register:40f0:8", ["const:b80e2c:8", "const:4:8"]]
+ 00b80e2c ["CALL", null, ["callee:00bdcf30:8"]]
- 00b80d64 bytes 47700194
+ 00b80e2c bytes 41700194
- 00b80da8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80da8 ["INT_ADD", "register:40f0:8", ["const:b80da8:8", "const:4:8"]]
- 00b80da8 ["CALLIND", null, ["register:0:8"]]
+ 00b80e70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80e70 ["INT_ADD", "register:40f0:8", ["const:b80e70:8", "const:4:8"]]
+ 00b80e70 ["CALLIND", null, ["register:0:8"]]
- 00b80da8 bytes 00013fd6
+ 00b80e70 bytes 00013fd6
- 00b80e00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80e00 ["INT_ADD", "register:40f0:8", ["const:b80e00:8", "const:4:8"]]
- 00b80e00 ["CALLIND", null, ["register:0:8"]]
+ 00b80ec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80ec8 ["INT_ADD", "register:40f0:8", ["const:b80ec8:8", "const:4:8"]]
+ 00b80ec8 ["CALLIND", null, ["register:0:8"]]
- 00b80e00 bytes 00013fd6
+ 00b80ec8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97122b03e6771506d4f4e72c21f27e79"></a>

### [`00b80f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80f68.md) → [`00b81030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81030.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80f68.md#insn-00b80f9c) · [`00b80ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80f68.md#insn-00b80ff4) · [`00b81070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80f68.md#insn-00b81070)
- 新版 `00b81064`（命令位置の公開資料なし） · `00b810bc`（命令位置の公開資料なし） · `00b81138`（命令位置の公開資料なし）

~~~diff
- 00b80f9c ["INT_ADD", "register:40f0:8", ["const:b80f9c:8", "const:4:8"]]
- 00b80f9c ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b81064 ["INT_ADD", "register:40f0:8", ["const:b81064:8", "const:4:8"]]
+ 00b81064 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b80f9c bytes b96f0194
+ 00b81064 bytes b36f0194
- 00b80ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80ff4 ["INT_ADD", "register:40f0:8", ["const:b80ff4:8", "const:4:8"]]
- 00b80ff4 ["CALLIND", null, ["register:0:8"]]
+ 00b810bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b810bc ["INT_ADD", "register:40f0:8", ["const:b810bc:8", "const:4:8"]]
+ 00b810bc ["CALLIND", null, ["register:0:8"]]
- 00b80ff4 bytes 00013fd6
+ 00b810bc bytes 00013fd6
- 00b81070 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81070 ["INT_ADD", "register:40f0:8", ["const:b81070:8", "const:4:8"]]
- 00b81070 ["CALLIND", null, ["register:0:8"]]
+ 00b81138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81138 ["INT_ADD", "register:40f0:8", ["const:b81138:8", "const:4:8"]]
+ 00b81138 ["CALLIND", null, ["register:0:8"]]
- 00b81070 bytes 00013fd6
+ 00b81138 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e7d029683f96185a32ea269565e2153"></a>

### [`00b81b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b10.md) → [`00b81bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81bd8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b10.md#insn-00b81b30)
- 新版 `00b81bf8`（命令位置の公開資料なし）

~~~diff
- 00b81b30 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81b30 ["INT_ADD", "register:40f0:8", ["const:b81b30:8", "const:4:8"]]
- 00b81b30 ["CALLIND", null, ["register:0:8"]]
+ 00b81bf8 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b81bf8 ["INT_ADD", "register:40f0:8", ["const:b81bf8:8", "const:4:8"]]
+ 00b81bf8 ["CALLIND", null, ["register:0:8"]]
- 00b81b30 bytes 20003fd6
+ 00b81bf8 bytes 20003fd6
~~~


<a id="compare-483e91210833e9ef811917286831e9ef"></a>

### [`00b81b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b48.md) → [`00b81c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c10.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b48.md#insn-00b81b68)
- 新版 `00b81c30`（命令位置の公開資料なし）

~~~diff
- 00b81b68 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81b68 ["INT_ADD", "register:40f0:8", ["const:b81b68:8", "const:4:8"]]
- 00b81b68 ["CALLIND", null, ["register:0:8"]]
+ 00b81c30 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b81c30 ["INT_ADD", "register:40f0:8", ["const:b81c30:8", "const:4:8"]]
+ 00b81c30 ["CALLIND", null, ["register:0:8"]]
- 00b81b68 bytes 20003fd6
+ 00b81c30 bytes 20003fd6
~~~


<a id="compare-95ff422dd6519244d09f66ea3cbf91cc"></a>

### [`00b82704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82704.md) → [`00b827cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b827cc.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdb360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb360.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82704.md#insn-00b82730) · [`00b82768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82704.md#insn-00b82768) · [`00b82788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82704.md#insn-00b82788)
- 新版 `00b827f8`（命令位置の公開資料なし） · `00b82830`（命令位置の公開資料なし） · `00b82850`（命令位置の公開資料なし）

~~~diff
- 00b82730 ["INT_ADD", "register:40f0:8", ["const:b82730:8", "const:4:8"]]
- 00b82730 ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b827f8 ["INT_ADD", "register:40f0:8", ["const:b827f8:8", "const:4:8"]]
+ 00b827f8 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b82730 bytes f8620194
+ 00b827f8 bytes f2620194
- 00b82768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82768 ["INT_ADD", "register:40f0:8", ["const:b82768:8", "const:4:8"]]
- 00b82768 ["CALLIND", null, ["register:0:8"]]
+ 00b82830 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b82830 ["INT_ADD", "register:40f0:8", ["const:b82830:8", "const:4:8"]]
+ 00b82830 ["CALLIND", null, ["register:0:8"]]
- 00b82768 bytes 00013fd6
+ 00b82830 bytes 00013fd6
- 00b82788 ["INT_ADD", "register:40f0:8", ["const:b82788:8", "const:4:8"]]
- 00b82788 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b82850 ["INT_ADD", "register:40f0:8", ["const:b82850:8", "const:4:8"]]
+ 00b82850 ["CALL", null, ["callee:00bdb400:8"]]
- 00b82788 bytes f2620194
+ 00b82850 bytes ec620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48873d3ed9db26c9827046b07dfd0a9b"></a>

### [`00b827c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b827c8.md) → [`00b82890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82890.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b827c8.md#insn-00b82810)
- 新版 `00b828d8`（命令位置の公開資料なし）

~~~diff
- 00b82810 ["INT_ADD", "register:40f0:8", ["const:b82810:8", "const:4:8"]]
- 00b82810 ["CALL", null, ["callee:00bdb340:8"]]
+ 00b828d8 ["INT_ADD", "register:40f0:8", ["const:b828d8:8", "const:4:8"]]
+ 00b828d8 ["CALL", null, ["callee:00bdb340:8"]]
- 00b82810 bytes a0620194
+ 00b828d8 bytes 9a620194
~~~


<a id="compare-3a606542b35ccee874d59177ba12d4b3"></a>

### [`00b82958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82958.md) → [`00b82a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a20.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82958.md#insn-00b82970)
- 新版 `00b82a38`（命令位置の公開資料なし）

~~~diff
- 00b82970 ["INT_ADD", "register:40f0:8", ["const:b82970:8", "const:4:8"]]
- 00b82970 ["CALL", null, ["callee:00be0190:8"]]
+ 00b82a38 ["INT_ADD", "register:40f0:8", ["const:b82a38:8", "const:4:8"]]
+ 00b82a38 ["CALL", null, ["callee:00be0190:8"]]
- 00b82970 bytes dc750194
+ 00b82a38 bytes d6750194
~~~


<a id="compare-ce3c6cf2517c5d0222b95b51cb661adf"></a>

### [`00b82a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82a34.md) → [`00b82afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82afc.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be12b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82a34.md#insn-00b82a48)
- 新版 `00b82b10`（命令位置の公開資料なし）

~~~diff
- 00b82a48 ["INT_ADD", "register:40f0:8", ["const:b82a48:8", "const:4:8"]]
- 00b82a48 ["CALL", null, ["callee:00be1360:8"]]
+ 00b82b10 ["INT_ADD", "register:40f0:8", ["const:b82b10:8", "const:4:8"]]
+ 00b82b10 ["CALL", null, ["callee:00be1360:8"]]
- 00b82a48 bytes 1a7a0194
+ 00b82b10 bytes 147a0194
~~~


<a id="compare-7635dd544059fb9369c8e22e5e08a945"></a>

### [`00b82b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82b20.md) → [`00b82be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82be8.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82b20.md#insn-00b82b48) · [`00b82b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82b20.md#insn-00b82b54)
- 新版 `00b82c10`（命令位置の公開資料なし） · `00b82c1c`（命令位置の公開資料なし）

~~~diff
- 00b82b48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b82b48 ["INT_ADD", "register:40f0:8", ["const:b82b48:8", "const:4:8"]]
- 00b82b48 ["CALLIND", null, ["register:0:8"]]
+ 00b82c10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b82c10 ["INT_ADD", "register:40f0:8", ["const:b82c10:8", "const:4:8"]]
+ 00b82c10 ["CALLIND", null, ["register:0:8"]]
- 00b82b48 bytes 20013fd6
+ 00b82c10 bytes 20013fd6
- 00b82b54 ["INT_ADD", "register:40f0:8", ["const:b82b54:8", "const:4:8"]]
- 00b82b54 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b82c1c ["INT_ADD", "register:40f0:8", ["const:b82c1c:8", "const:4:8"]]
+ 00b82c1c ["CALL", null, ["callee:00bdd930:8"]]
- 00b82b54 bytes 4b6b0194
+ 00b82c1c bytes 456b0194
~~~


<a id="compare-fa832b892be77ebea9abdc6e775fad88"></a>

### [`00b82bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82bec.md) → [`00b82cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82cb4.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82bec.md#insn-00b82c38)
- 新版 `00b82d00`（命令位置の公開資料なし）

~~~diff
- 00b82c38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82c38 ["INT_ADD", "register:40f0:8", ["const:b82c38:8", "const:4:8"]]
- 00b82c38 ["CALLIND", null, ["register:0:8"]]
+ 00b82d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b82d00 ["INT_ADD", "register:40f0:8", ["const:b82d00:8", "const:4:8"]]
+ 00b82d00 ["CALLIND", null, ["register:0:8"]]
- 00b82c38 bytes 00013fd6
+ 00b82d00 bytes 00013fd6
~~~


<a id="compare-b60e7813905c8bdae9a68a898447c2c7"></a>

### [`00b82e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e28.md) → [`00b82ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82ef0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e28.md#insn-00b82e48)
- 新版 `00b82f10`（命令位置の公開資料なし）

~~~diff
- 00b82e48 ["INT_ADD", "register:40f0:8", ["const:b82e48:8", "const:4:8"]]
- 00b82e48 ["CALL", null, ["callee:00be1290:8"]]
+ 00b82f10 ["INT_ADD", "register:40f0:8", ["const:b82f10:8", "const:4:8"]]
+ 00b82f10 ["CALL", null, ["callee:00be1290:8"]]
- 00b82e48 bytes e6780194
+ 00b82f10 bytes e0780194
~~~


<a id="compare-aa947628c876e5061c0c3fb12561c2ed"></a>

### [`00b82fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82fc4.md) → [`00b8308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8308c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82fc4.md#insn-00b83048) · [`00b83060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82fc4.md#insn-00b83060)
- 新版 `00b83110`（命令位置の公開資料なし） · `00b83128`（命令位置の公開資料なし）

~~~diff
- 00b83048 ["INT_ADD", "register:40f0:8", ["const:b83048:8", "const:4:8"]]
- 00b83048 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b83110 ["INT_ADD", "register:40f0:8", ["const:b83110:8", "const:4:8"]]
+ 00b83110 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b83048 bytes ea5f0194
+ 00b83110 bytes e45f0194
- 00b83060 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83060 ["INT_ADD", "register:40f0:8", ["const:b83060:8", "const:4:8"]]
- 00b83060 ["CALLIND", null, ["register:0:8"]]
+ 00b83128 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83128 ["INT_ADD", "register:40f0:8", ["const:b83128:8", "const:4:8"]]
+ 00b83128 ["CALLIND", null, ["register:0:8"]]
- 00b83060 bytes 00013fd6
+ 00b83128 bytes 00013fd6
~~~


<a id="compare-865a28d4ca092d754aa9b0f0ca32283b"></a>

### [`00b830a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b830a4.md) → [`00b8316c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8316c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b830c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b830a4.md#insn-00b830c0)
- 新版 `00b83188`（命令位置の公開資料なし）

~~~diff
- 00b830c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b830c0 ["INT_ADD", "register:40f0:8", ["const:b830c0:8", "const:4:8"]]
- 00b830c0 ["CALLIND", null, ["register:0:8"]]
+ 00b83188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83188 ["INT_ADD", "register:40f0:8", ["const:b83188:8", "const:4:8"]]
+ 00b83188 ["CALLIND", null, ["register:0:8"]]
- 00b830c0 bytes 00013fd6
+ 00b83188 bytes 00013fd6
~~~


<a id="compare-17550a0070cfe801237a900ab40d571b"></a>

### [`00b830f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b830f4.md) → [`00b831bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b831bc.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b830f4.md#insn-00b83170) · [`00b8318c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b830f4.md#insn-00b8318c)
- 新版 `00b83238`（命令位置の公開資料なし） · `00b83254`（命令位置の公開資料なし）

~~~diff
- 00b83170 ["INT_ADD", "register:40f0:8", ["const:b83170:8", "const:4:8"]]
- 00b83170 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b83238 ["INT_ADD", "register:40f0:8", ["const:b83238:8", "const:4:8"]]
+ 00b83238 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b83170 bytes a05f0194
+ 00b83238 bytes 9a5f0194
- 00b8318c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8318c ["INT_ADD", "register:40f0:8", ["const:b8318c:8", "const:4:8"]]
- 00b8318c ["CALLIND", null, ["register:0:8"]]
+ 00b83254 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83254 ["INT_ADD", "register:40f0:8", ["const:b83254:8", "const:4:8"]]
+ 00b83254 ["CALLIND", null, ["register:0:8"]]
- 00b8318c bytes 00013fd6
+ 00b83254 bytes 00013fd6
~~~


<a id="compare-6897e06d3098807caaa5e123ba9e5221"></a>

### [`00b831d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b831d8.md) → [`00b832a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832a0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b831d8.md#insn-00b83214)
- 新版 `00b832dc`（命令位置の公開資料なし）

~~~diff
- 00b83214 ["INT_ADD", "register:40f0:8", ["const:b83214:8", "const:4:8"]]
- 00b83214 ["CALL", null, ["callee:00bdb340:8"]]
+ 00b832dc ["INT_ADD", "register:40f0:8", ["const:b832dc:8", "const:4:8"]]
+ 00b832dc ["CALL", null, ["callee:00bdb340:8"]]
- 00b83214 bytes 1f600194
+ 00b832dc bytes 19600194
~~~


<a id="compare-2d90afb9a30e3e374274f1cb19936bfc"></a>

### [`00b832cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b832cc.md) → [`00b83394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83394.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b832e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b832cc.md#insn-00b832e4)
- 新版 `00b833ac`（命令位置の公開資料なし）

~~~diff
- 00b832e4 ["INT_ADD", "register:40f0:8", ["const:b832e4:8", "const:4:8"]]
- 00b832e4 ["CALL", null, ["callee:00be0190:8"]]
+ 00b833ac ["INT_ADD", "register:40f0:8", ["const:b833ac:8", "const:4:8"]]
+ 00b833ac ["CALL", null, ["callee:00be0190:8"]]
- 00b832e4 bytes 7f730194
+ 00b833ac bytes 79730194
~~~


<a id="compare-e2fb59976e2a5a5fada5fb9cecd96dd6"></a>

### [`00b832fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b832fc.md) → [`00b833c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833c4.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8331c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b832fc.md#insn-00b8331c)
- 新版 `00b833e4`（命令位置の公開資料なし）

~~~diff
- 00b8331c ["INT_ADD", "register:40f0:8", ["const:b8331c:8", "const:4:8"]]
- 00b8331c ["CALL", null, ["callee:00be0190:8"]]
+ 00b833e4 ["INT_ADD", "register:40f0:8", ["const:b833e4:8", "const:4:8"]]
+ 00b833e4 ["CALL", null, ["callee:00be0190:8"]]
- 00b8331c bytes 71730194
+ 00b833e4 bytes 6b730194
~~~


<a id="compare-065df9062dabc5324f76e9674861c337"></a>

### [`00b83334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83334.md) → [`00b833fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833fc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8336c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83334.md#insn-00b8336c)
- 新版 `00b83434`（命令位置の公開資料なし）

~~~diff
- 00b8336c ["INT_ADD", "register:40f0:8", ["const:b8336c:8", "const:4:8"]]
- 00b8336c ["CALL", null, ["callee:00be12d0:8"]]
+ 00b83434 ["INT_ADD", "register:40f0:8", ["const:b83434:8", "const:4:8"]]
+ 00b83434 ["CALL", null, ["callee:00be12d0:8"]]
- 00b8336c bytes ad770194
+ 00b83434 bytes a7770194
~~~


<a id="compare-c0e700e548cd6746f38f2d9cbdfb7424"></a>

### [`00b83590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83590.md) → [`00b83658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83658.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be12f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12f0.md) · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 1件 [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b835c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83590.md#insn-00b835c4) · [`00b835e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83590.md#insn-00b835e8) · [`00b83608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83590.md#insn-00b83608)
- 新版 `00b8368c`（命令位置の公開資料なし） · `00b836b0`（命令位置の公開資料なし） · `00b836d0`（命令位置の公開資料なし）

~~~diff
- 00b835c4 ["INT_ADD", "register:40f0:8", ["const:b835c4:8", "const:4:8"]]
- 00b835c4 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b8368c ["INT_ADD", "register:40f0:8", ["const:b8368c:8", "const:4:8"]]
+ 00b8368c ["CALL", null, ["callee:00be13b0:8"]]
- 00b835c4 bytes 4f770194
+ 00b8368c bytes 49770194
- 00b835e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b835e8 ["INT_ADD", "register:40f0:8", ["const:b835e8:8", "const:4:8"]]
- 00b835e8 ["CALLIND", null, ["register:0:8"]]
+ 00b836b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b836b0 ["INT_ADD", "register:40f0:8", ["const:b836b0:8", "const:4:8"]]
+ 00b836b0 ["CALLIND", null, ["register:0:8"]]
- 00b835e8 bytes 00013fd6
+ 00b836b0 bytes 00013fd6
- 00b83608 ["INT_ADD", "register:40f0:8", ["const:b83608:8", "const:4:8"]]
- 00b83608 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b836d0 ["INT_ADD", "register:40f0:8", ["const:b836d0:8", "const:4:8"]]
+ 00b836d0 ["CALL", null, ["callee:00bdb400:8"]]
- 00b83608 bytes 525f0194
+ 00b836d0 bytes 4c5f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc16950ab100f861bd2a544e72df23f5"></a>

### [`00b83680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83680.md) → [`00b83748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83748.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b836a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83680.md#insn-00b836a0)
- 新版 `00b83768`（命令位置の公開資料なし）

~~~diff
- 00b836a0 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b836a0 ["INT_ADD", "register:40f0:8", ["const:b836a0:8", "const:4:8"]]
- 00b836a0 ["CALLIND", null, ["register:0:8"]]
+ 00b83768 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b83768 ["INT_ADD", "register:40f0:8", ["const:b83768:8", "const:4:8"]]
+ 00b83768 ["CALLIND", null, ["register:0:8"]]
- 00b836a0 bytes 20003fd6
+ 00b83768 bytes 20003fd6
~~~


<a id="compare-056565ddf34808dbf895485c9ce3fd0e"></a>

### [`00b836b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836b8.md) → [`00b83780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83780.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b836d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836b8.md#insn-00b836d8)
- 新版 `00b837a0`（命令位置の公開資料なし）

~~~diff
- 00b836d8 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b836d8 ["INT_ADD", "register:40f0:8", ["const:b836d8:8", "const:4:8"]]
- 00b836d8 ["CALLIND", null, ["register:0:8"]]
+ 00b837a0 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b837a0 ["INT_ADD", "register:40f0:8", ["const:b837a0:8", "const:4:8"]]
+ 00b837a0 ["CALLIND", null, ["register:0:8"]]
- 00b836d8 bytes 20003fd6
+ 00b837a0 bytes 20003fd6
~~~


<a id="compare-0eddd6d9c2a6a26bd482397adc363d27"></a>

### [`00b836f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836f0.md) → [`00b837b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b837b8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836f0.md#insn-00b83720) · [`00b83784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836f0.md#insn-00b83784) · [`00b837b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b836f0.md#insn-00b837b8)
- 新版 `00b837e8`（命令位置の公開資料なし） · `00b8384c`（命令位置の公開資料なし） · `00b83880`（命令位置の公開資料なし）

~~~diff
- 00b83720 ["INT_ADD", "register:40f0:8", ["const:b83720:8", "const:4:8"]]
- 00b83720 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b837e8 ["INT_ADD", "register:40f0:8", ["const:b837e8:8", "const:4:8"]]
+ 00b837e8 ["CALL", null, ["callee:00be13d0:8"]]
- 00b83720 bytes 00770194
+ 00b837e8 bytes fa760194
- 00b83784 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83784 ["INT_ADD", "register:40f0:8", ["const:b83784:8", "const:4:8"]]
- 00b83784 ["CALLIND", null, ["register:0:8"]]
+ 00b8384c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8384c ["INT_ADD", "register:40f0:8", ["const:b8384c:8", "const:4:8"]]
+ 00b8384c ["CALLIND", null, ["register:0:8"]]
- 00b83784 bytes 00013fd6
+ 00b8384c bytes 00013fd6
- 00b837b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b837b8 ["INT_ADD", "register:40f0:8", ["const:b837b8:8", "const:4:8"]]
- 00b837b8 ["CALLIND", null, ["register:0:8"]]
+ 00b83880 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83880 ["INT_ADD", "register:40f0:8", ["const:b83880:8", "const:4:8"]]
+ 00b83880 ["CALLIND", null, ["register:0:8"]]
- 00b837b8 bytes 00013fd6
+ 00b83880 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef043f4c4eed2c7d4a387dd5301c1142"></a>

### [`00b84a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a14.md) → [`00b84adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84adc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1330.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a14.md#insn-00b84a2c)
- 新版 `00b84af4`（命令位置の公開資料なし）

~~~diff
- 00b84a2c ["INT_ADD", "register:40f0:8", ["const:b84a2c:8", "const:4:8"]]
- 00b84a2c ["CALL", null, ["callee:00be13e0:8"]]
+ 00b84af4 ["INT_ADD", "register:40f0:8", ["const:b84af4:8", "const:4:8"]]
+ 00b84af4 ["CALL", null, ["callee:00be13e0:8"]]
- 00b84a2c bytes 41720194
+ 00b84af4 bytes 3b720194
~~~


<a id="compare-3e40ca4aacad75a495bb6c99822e311e"></a>

### [`00b84d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84d58.md) → [`00b84e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84e20.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1350.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00be1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1400.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84d58.md#insn-00b84d8c) · [`00b84dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84d58.md#insn-00b84dec) · [`00b84e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84d58.md#insn-00b84e28)
- 新版 `00b84e54`（命令位置の公開資料なし） · `00b84eb4`（命令位置の公開資料なし） · `00b84ef0`（命令位置の公開資料なし）

~~~diff
- 00b84d8c ["INT_ADD", "register:40f0:8", ["const:b84d8c:8", "const:4:8"]]
- 00b84d8c ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84e54 ["INT_ADD", "register:40f0:8", ["const:b84e54:8", "const:4:8"]]
+ 00b84e54 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84d8c bytes 65710194
+ 00b84e54 bytes 5f710194
- 00b84dec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84dec ["INT_ADD", "register:40f0:8", ["const:b84dec:8", "const:4:8"]]
- 00b84dec ["CALLIND", null, ["register:0:8"]]
+ 00b84eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84eb4 ["INT_ADD", "register:40f0:8", ["const:b84eb4:8", "const:4:8"]]
+ 00b84eb4 ["CALLIND", null, ["register:0:8"]]
- 00b84dec bytes 00013fd6
+ 00b84eb4 bytes 00013fd6
- 00b84e28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84e28 ["INT_ADD", "register:40f0:8", ["const:b84e28:8", "const:4:8"]]
- 00b84e28 ["CALLIND", null, ["register:0:8"]]
+ 00b84ef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84ef0 ["INT_ADD", "register:40f0:8", ["const:b84ef0:8", "const:4:8"]]
+ 00b84ef0 ["CALLIND", null, ["register:0:8"]]
- 00b84e28 bytes 00013fd6
+ 00b84ef0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc0ebabecb0bbef0ddf60b607e4bcf4"></a>

### [`00b85548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85548.md) → [`00b85610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85610.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85548.md#insn-00b85578) · [`00b855bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85548.md#insn-00b855bc) · [`00b85608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85548.md#insn-00b85608)
- 新版 `00b85640`（命令位置の公開資料なし） · `00b85684`（命令位置の公開資料なし） · `00b856d0`（命令位置の公開資料なし）

~~~diff
- 00b85578 ["INT_ADD", "register:40f0:8", ["const:b85578:8", "const:4:8"]]
- 00b85578 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85640 ["INT_ADD", "register:40f0:8", ["const:b85640:8", "const:4:8"]]
+ 00b85640 ["CALL", null, ["callee:00be13d0:8"]]
- 00b85578 bytes 6a6f0194
+ 00b85640 bytes 646f0194
- 00b855bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b855bc ["INT_ADD", "register:40f0:8", ["const:b855bc:8", "const:4:8"]]
- 00b855bc ["CALLIND", null, ["register:0:8"]]
+ 00b85684 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85684 ["INT_ADD", "register:40f0:8", ["const:b85684:8", "const:4:8"]]
+ 00b85684 ["CALLIND", null, ["register:0:8"]]
- 00b855bc bytes 00013fd6
+ 00b85684 bytes 00013fd6
- 00b85608 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85608 ["INT_ADD", "register:40f0:8", ["const:b85608:8", "const:4:8"]]
- 00b85608 ["CALLIND", null, ["register:0:8"]]
+ 00b856d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b856d0 ["INT_ADD", "register:40f0:8", ["const:b856d0:8", "const:4:8"]]
+ 00b856d0 ["CALLIND", null, ["register:0:8"]]
- 00b85608 bytes 20013fd6
+ 00b856d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ade3132eaff6a27aabe677e4ba04167"></a>

### [`00b8569c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8569c.md) → [`00b85764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85764.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b856dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8569c.md#insn-00b856dc) · [`00b856ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8569c.md#insn-00b856ec) · [`00b85748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8569c.md#insn-00b85748)
- 新版 `00b857a4`（命令位置の公開資料なし） · `00b857b4`（命令位置の公開資料なし） · `00b85810`（命令位置の公開資料なし）

~~~diff
- 00b856dc ["INT_ADD", "register:40f0:8", ["const:b856dc:8", "const:4:8"]]
- 00b856dc ["CALL", null, ["callee:00bdb400:8"]]
+ 00b857a4 ["INT_ADD", "register:40f0:8", ["const:b857a4:8", "const:4:8"]]
+ 00b857a4 ["CALL", null, ["callee:00bdb400:8"]]
- 00b856dc bytes 1d570194
+ 00b857a4 bytes 17570194
- 00b856ec ["INT_ADD", "register:40f0:8", ["const:b856ec:8", "const:4:8"]]
- 00b856ec ["CALL", null, ["callee:00be13d0:8"]]
+ 00b857b4 ["INT_ADD", "register:40f0:8", ["const:b857b4:8", "const:4:8"]]
+ 00b857b4 ["CALL", null, ["callee:00be13d0:8"]]
- 00b856ec bytes 0d6f0194
+ 00b857b4 bytes 076f0194
- 00b85748 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85748 ["INT_ADD", "register:40f0:8", ["const:b85748:8", "const:4:8"]]
- 00b85748 ["CALLIND", null, ["register:0:8"]]
+ 00b85810 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85810 ["INT_ADD", "register:40f0:8", ["const:b85810:8", "const:4:8"]]
+ 00b85810 ["CALLIND", null, ["register:0:8"]]
- 00b85748 bytes 00013fd6
+ 00b85810 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823d2f586a63966b461f489f9c2f689c"></a>

### [`00b857dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b857dc.md) → [`00b858a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b858a4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b857dc.md#insn-00b85818) · [`00b85828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b857dc.md#insn-00b85828) · [`00b8587c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b857dc.md#insn-00b8587c)
- 新版 `00b858e0`（命令位置の公開資料なし） · `00b858f0`（命令位置の公開資料なし） · `00b85944`（命令位置の公開資料なし）

~~~diff
- 00b85818 ["INT_ADD", "register:40f0:8", ["const:b85818:8", "const:4:8"]]
- 00b85818 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b858e0 ["INT_ADD", "register:40f0:8", ["const:b858e0:8", "const:4:8"]]
+ 00b858e0 ["CALL", null, ["callee:00bdb400:8"]]
- 00b85818 bytes ce560194
+ 00b858e0 bytes c8560194
- 00b85828 ["INT_ADD", "register:40f0:8", ["const:b85828:8", "const:4:8"]]
- 00b85828 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b858f0 ["INT_ADD", "register:40f0:8", ["const:b858f0:8", "const:4:8"]]
+ 00b858f0 ["CALL", null, ["callee:00be13d0:8"]]
- 00b85828 bytes be6e0194
+ 00b858f0 bytes b86e0194
- 00b8587c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8587c ["INT_ADD", "register:40f0:8", ["const:b8587c:8", "const:4:8"]]
- 00b8587c ["CALLIND", null, ["register:0:8"]]
+ 00b85944 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85944 ["INT_ADD", "register:40f0:8", ["const:b85944:8", "const:4:8"]]
+ 00b85944 ["CALLIND", null, ["register:0:8"]]
- 00b8587c bytes 00013fd6
+ 00b85944 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79718e01b785a4092d73766aa10ba616"></a>

### [`00b85e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e3c.md) → [`00b85f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f04.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e3c.md#insn-00b85e5c)
- 新版 `00b85f24`（命令位置の公開資料なし）

~~~diff
- 00b85e5c ["INT_ADD", "register:40f0:8", ["const:b85e5c:8", "const:4:8"]]
- 00b85e5c ["CALL", null, ["callee:00be0190:8"]]
+ 00b85f24 ["INT_ADD", "register:40f0:8", ["const:b85f24:8", "const:4:8"]]
+ 00b85f24 ["CALL", null, ["callee:00be0190:8"]]
- 00b85e5c bytes a1680194
+ 00b85f24 bytes 9b680194
~~~


<a id="compare-c1dae345b5eb3cf65aef1cf91776c95e"></a>

### [`00b85f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85f3c.md) → [`00b86004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86004.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be00f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00f0.md)
- 新版 呼出元 1件 [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85f3c.md#insn-00b85f78) · [`00b85f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85f3c.md#insn-00b85f9c) · [`00b85fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85f3c.md#insn-00b85fc0)
- 新版 `00b86040`（命令位置の公開資料なし） · `00b86064`（命令位置の公開資料なし） · `00b86088`（命令位置の公開資料なし）

~~~diff
- 00b85f78 ["INT_ADD", "register:40f0:8", ["const:b85f78:8", "const:4:8"]]
- 00b85f78 ["CALL", null, ["callee:00be01a0:8"]]
+ 00b86040 ["INT_ADD", "register:40f0:8", ["const:b86040:8", "const:4:8"]]
+ 00b86040 ["CALL", null, ["callee:00be01a0:8"]]
- 00b85f78 bytes 5e680194
+ 00b86040 bytes 58680194
- 00b85f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85f9c ["INT_ADD", "register:40f0:8", ["const:b85f9c:8", "const:4:8"]]
- 00b85f9c ["CALLIND", null, ["register:0:8"]]
+ 00b86064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b86064 ["INT_ADD", "register:40f0:8", ["const:b86064:8", "const:4:8"]]
+ 00b86064 ["CALLIND", null, ["register:0:8"]]
- 00b85f9c bytes 00013fd6
+ 00b86064 bytes 00013fd6
- 00b85fc0 ["INT_ADD", "register:40f0:8", ["const:b85fc0:8", "const:4:8"]]
- 00b85fc0 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b86088 ["INT_ADD", "register:40f0:8", ["const:b86088:8", "const:4:8"]]
+ 00b86088 ["CALL", null, ["callee:00bdb400:8"]]
- 00b85fc0 bytes e4540194
+ 00b86088 bytes de540194
~~~


<a id="compare-6fc8b80e509193b846a5383b017470e0"></a>

### [`00b85ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ff0.md) → [`00b860b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860b8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ff0.md#insn-00b86010)
- 新版 `00b860d8`（命令位置の公開資料なし）

~~~diff
- 00b86010 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b86010 ["INT_ADD", "register:40f0:8", ["const:b86010:8", "const:4:8"]]
- 00b86010 ["CALLIND", null, ["register:0:8"]]
+ 00b860d8 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b860d8 ["INT_ADD", "register:40f0:8", ["const:b860d8:8", "const:4:8"]]
+ 00b860d8 ["CALLIND", null, ["register:0:8"]]
- 00b86010 bytes 20003fd6
+ 00b860d8 bytes 20003fd6
~~~


<a id="compare-a6e459b0b8e5938a7a8569c4e6a293c4"></a>

### [`00b86028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86028.md) → [`00b860f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860f0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86028.md#insn-00b86048)
- 新版 `00b86110`（命令位置の公開資料なし）

~~~diff
- 00b86048 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b86048 ["INT_ADD", "register:40f0:8", ["const:b86048:8", "const:4:8"]]
- 00b86048 ["CALLIND", null, ["register:0:8"]]
+ 00b86110 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b86110 ["INT_ADD", "register:40f0:8", ["const:b86110:8", "const:4:8"]]
+ 00b86110 ["CALLIND", null, ["register:0:8"]]
- 00b86048 bytes 20003fd6
+ 00b86110 bytes 20003fd6
~~~


<a id="compare-cb88fb93938b47698dc38b3e6a9c85c2"></a>

### [`00b87510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87510.md) → [`00b875d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b875d8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87510.md#insn-00b87538) · [`00b8758c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87510.md#insn-00b8758c) · [`00b875b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87510.md#insn-00b875b8)
- 新版 `00b87600`（命令位置の公開資料なし） · `00b87654`（命令位置の公開資料なし） · `00b87680`（命令位置の公開資料なし）

~~~diff
- 00b87538 ["INT_ADD", "register:40f0:8", ["const:b87538:8", "const:4:8"]]
- 00b87538 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b87600 ["INT_ADD", "register:40f0:8", ["const:b87600:8", "const:4:8"]]
+ 00b87600 ["CALL", null, ["callee:00be13b0:8"]]
- 00b87538 bytes 72670194
+ 00b87600 bytes 6c670194
- 00b8758c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8758c ["INT_ADD", "register:40f0:8", ["const:b8758c:8", "const:4:8"]]
- 00b8758c ["CALLIND", null, ["register:0:8"]]
+ 00b87654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87654 ["INT_ADD", "register:40f0:8", ["const:b87654:8", "const:4:8"]]
+ 00b87654 ["CALLIND", null, ["register:0:8"]]
- 00b8758c bytes 00013fd6
+ 00b87654 bytes 00013fd6
- 00b875b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b875b8 ["INT_ADD", "register:40f0:8", ["const:b875b8:8", "const:4:8"]]
- 00b875b8 ["CALLIND", null, ["register:0:8"]]
+ 00b87680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87680 ["INT_ADD", "register:40f0:8", ["const:b87680:8", "const:4:8"]]
+ 00b87680 ["CALLIND", null, ["register:0:8"]]
- 00b875b8 bytes 00013fd6
+ 00b87680 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b1228c28cc2e03d366428a8e6f1955a"></a>

### [`00b876dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b876dc.md) → [`00b877a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b877a4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE3putEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b876dc.md#insn-00b87700) · [`00b8774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b876dc.md#insn-00b8774c) · [`00b87770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b876dc.md#insn-00b87770)
- 新版 `00b877c8`（命令位置の公開資料なし） · `00b87814`（命令位置の公開資料なし） · `00b87838`（命令位置の公開資料なし）

~~~diff
- 00b87700 ["INT_ADD", "register:40f0:8", ["const:b87700:8", "const:4:8"]]
- 00b87700 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b877c8 ["INT_ADD", "register:40f0:8", ["const:b877c8:8", "const:4:8"]]
+ 00b877c8 ["CALL", null, ["callee:00be13b0:8"]]
- 00b87700 bytes 00670194
+ 00b877c8 bytes fa660194
- 00b8774c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8774c ["INT_ADD", "register:40f0:8", ["const:b8774c:8", "const:4:8"]]
- 00b8774c ["CALLIND", null, ["register:0:8"]]
+ 00b87814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87814 ["INT_ADD", "register:40f0:8", ["const:b87814:8", "const:4:8"]]
+ 00b87814 ["CALLIND", null, ["register:0:8"]]
- 00b8774c bytes 00013fd6
+ 00b87814 bytes 00013fd6
- 00b87770 ["INT_ADD", "register:40f0:8", ["const:b87770:8", "const:4:8"]]
- 00b87770 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b87838 ["INT_ADD", "register:40f0:8", ["const:b87838:8", "const:4:8"]]
+ 00b87838 ["CALL", null, ["callee:00bdb400:8"]]
- 00b87770 bytes f84e0194
+ 00b87838 bytes f24e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c49a9f2473335371fe2b8f247b8284b1"></a>

### [`00b877dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b877dc.md) → [`00b878a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b878a4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5writeEPKwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b877dc.md#insn-00b87808) · [`00b87838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b877dc.md#insn-00b87838) · [`00b87858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b877dc.md#insn-00b87858)
- 新版 `00b878d0`（命令位置の公開資料なし） · `00b87900`（命令位置の公開資料なし） · `00b87920`（命令位置の公開資料なし）

~~~diff
- 00b87808 ["INT_ADD", "register:40f0:8", ["const:b87808:8", "const:4:8"]]
- 00b87808 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b878d0 ["INT_ADD", "register:40f0:8", ["const:b878d0:8", "const:4:8"]]
+ 00b878d0 ["CALL", null, ["callee:00be13b0:8"]]
- 00b87808 bytes be660194
+ 00b878d0 bytes b8660194
- 00b87838 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87838 ["INT_ADD", "register:40f0:8", ["const:b87838:8", "const:4:8"]]
- 00b87838 ["CALLIND", null, ["register:0:8"]]
+ 00b87900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87900 ["INT_ADD", "register:40f0:8", ["const:b87900:8", "const:4:8"]]
+ 00b87900 ["CALLIND", null, ["register:0:8"]]
- 00b87838 bytes 00013fd6
+ 00b87900 bytes 00013fd6
- 00b87858 ["INT_ADD", "register:40f0:8", ["const:b87858:8", "const:4:8"]]
- 00b87858 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b87920 ["INT_ADD", "register:40f0:8", ["const:b87920:8", "const:4:8"]]
+ 00b87920 ["CALL", null, ["callee:00bdb400:8"]]
- 00b87858 bytes be4e0194
+ 00b87920 bytes b84e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c022116a458e0cbe64d266c7f1be4c"></a>

### [`00b878c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b878c8.md) → [`00b87990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87990.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5tellpEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b878c8.md#insn-00b87918)
- 新版 `00b879e0`（命令位置の公開資料なし）

~~~diff
- 00b87918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87918 ["INT_ADD", "register:40f0:8", ["const:b87918:8", "const:4:8"]]
- 00b87918 ["CALLIND", null, ["register:0:8"]]
+ 00b879e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b879e0 ["INT_ADD", "register:40f0:8", ["const:b879e0:8", "const:4:8"]]
+ 00b879e0 ["CALLIND", null, ["register:0:8"]]
- 00b87918 bytes 00013fd6
+ 00b879e0 bytes 00013fd6
~~~


<a id="compare-dbde883e82921cb30785a9ed587008bf"></a>

### [`00b87928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87928.md) → [`00b879f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b879f0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87928.md#insn-00b87954) · [`00b8798c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87928.md#insn-00b8798c) · [`00b879ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87928.md#insn-00b879ac)
- 新版 `00b87a1c`（命令位置の公開資料なし） · `00b87a54`（命令位置の公開資料なし） · `00b87a74`（命令位置の公開資料なし）

~~~diff
- 00b87954 ["INT_ADD", "register:40f0:8", ["const:b87954:8", "const:4:8"]]
- 00b87954 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b87a1c ["INT_ADD", "register:40f0:8", ["const:b87a1c:8", "const:4:8"]]
+ 00b87a1c ["CALL", null, ["callee:00be13b0:8"]]
- 00b87954 bytes 6b660194
+ 00b87a1c bytes 65660194
- 00b8798c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8798c ["INT_ADD", "register:40f0:8", ["const:b8798c:8", "const:4:8"]]
- 00b8798c ["CALLIND", null, ["register:0:8"]]
+ 00b87a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87a54 ["INT_ADD", "register:40f0:8", ["const:b87a54:8", "const:4:8"]]
+ 00b87a54 ["CALLIND", null, ["register:0:8"]]
- 00b8798c bytes 00013fd6
+ 00b87a54 bytes 00013fd6
- 00b879ac ["INT_ADD", "register:40f0:8", ["const:b879ac:8", "const:4:8"]]
- 00b879ac ["CALL", null, ["callee:00bdb400:8"]]
+ 00b87a74 ["INT_ADD", "register:40f0:8", ["const:b87a74:8", "const:4:8"]]
+ 00b87a74 ["CALL", null, ["callee:00bdb400:8"]]
- 00b879ac bytes 694e0194
+ 00b87a74 bytes 634e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11b90b8c0984518a3147e0b8b09624c1"></a>

### [`00b879ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b879ec.md) → [`00b87ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ab4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) [`00be1310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b879ec.md#insn-00b87a18) · [`00b87a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b879ec.md#insn-00b87a50) · [`00b87a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b879ec.md#insn-00b87a70)
- 新版 `00b87ae0`（命令位置の公開資料なし） · `00b87b18`（命令位置の公開資料なし） · `00b87b38`（命令位置の公開資料なし）

~~~diff
- 00b87a18 ["INT_ADD", "register:40f0:8", ["const:b87a18:8", "const:4:8"]]
- 00b87a18 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b87ae0 ["INT_ADD", "register:40f0:8", ["const:b87ae0:8", "const:4:8"]]
+ 00b87ae0 ["CALL", null, ["callee:00be13b0:8"]]
- 00b87a18 bytes 3a660194
+ 00b87ae0 bytes 34660194
- 00b87a50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87a50 ["INT_ADD", "register:40f0:8", ["const:b87a50:8", "const:4:8"]]
- 00b87a50 ["CALLIND", null, ["register:0:8"]]
+ 00b87b18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87b18 ["INT_ADD", "register:40f0:8", ["const:b87b18:8", "const:4:8"]]
+ 00b87b18 ["CALLIND", null, ["register:0:8"]]
- 00b87a50 bytes 00013fd6
+ 00b87b18 bytes 00013fd6
- 00b87a70 ["INT_ADD", "register:40f0:8", ["const:b87a70:8", "const:4:8"]]
- 00b87a70 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b87b38 ["INT_ADD", "register:40f0:8", ["const:b87b38:8", "const:4:8"]]
+ 00b87b38 ["CALL", null, ["callee:00bdb400:8"]]
- 00b87a70 bytes 384e0194
+ 00b87b38 bytes 324e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13dd50c98890e97be44c4a4e434fdba4"></a>

### [`00b87b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87b5c.md) → [`00b87c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md) FUN_00b87c24

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b87ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87ab0.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 1件 [`00b87b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87b5c.md#insn-00b87c14) · [`00b87cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87b5c.md#insn-00b87cb8) · [`00b87ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87b5c.md#insn-00b87ccc)
- 新版 `00b87cdc`（命令位置の公開資料なし） · `00b87d80`（命令位置の公開資料なし） · `00b87d94`（命令位置の公開資料なし）

~~~diff
- 00b87c14 ["INT_ADD", "register:40f0:8", ["const:b87c14:8", "const:4:8"]]
- 00b87c14 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b87cdc ["INT_ADD", "register:40f0:8", ["const:b87cdc:8", "const:4:8"]]
+ 00b87cdc ["CALL", null, ["callee:00bdb010:8"]]
- 00b87c14 bytes d34c0194
+ 00b87cdc bytes cd4c0194
- 00b87cb8 ["INT_ADD", "register:40f0:8", ["const:b87cb8:8", "const:4:8"]]
- 00b87cb8 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b87d80 ["INT_ADD", "register:40f0:8", ["const:b87d80:8", "const:4:8"]]
+ 00b87d80 ["CALL", null, ["callee:00bdd930:8"]]
- 00b87cb8 bytes f2560194
+ 00b87d80 bytes ec560194
- 00b87ccc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87ccc ["INT_ADD", "register:40f0:8", ["const:b87ccc:8", "const:4:8"]]
- 00b87ccc ["CALLIND", null, ["register:0:8"]]
+ 00b87d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87d94 ["INT_ADD", "register:40f0:8", ["const:b87d94:8", "const:4:8"]]
+ 00b87d94 ["CALLIND", null, ["register:0:8"]]
- 00b87ccc bytes 00013fd6
+ 00b87d94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8251961de89903e66db1dcafa0c214c"></a>

### [`00b87d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87d30.md) → [`00b87df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87df8.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1370.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 1件 [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87d30.md#insn-00b87de8) · [`00b87eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87d30.md#insn-00b87eb0) · [`00b87ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87d30.md#insn-00b87ec4)
- 新版 `00b87eb0`（命令位置の公開資料なし） · `00b87f78`（命令位置の公開資料なし） · `00b87f8c`（命令位置の公開資料なし）

~~~diff
- 00b87de8 ["INT_ADD", "register:40f0:8", ["const:b87de8:8", "const:4:8"]]
- 00b87de8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b87eb0 ["INT_ADD", "register:40f0:8", ["const:b87eb0:8", "const:4:8"]]
+ 00b87eb0 ["CALL", null, ["callee:00bdb010:8"]]
- 00b87de8 bytes 5e4c0194
+ 00b87eb0 bytes 584c0194
- 00b87eb0 ["INT_ADD", "register:40f0:8", ["const:b87eb0:8", "const:4:8"]]
- 00b87eb0 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b87f78 ["INT_ADD", "register:40f0:8", ["const:b87f78:8", "const:4:8"]]
+ 00b87f78 ["CALL", null, ["callee:00bdd930:8"]]
- 00b87eb0 bytes 74560194
+ 00b87f78 bytes 6e560194
- 00b87ec4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87ec4 ["INT_ADD", "register:40f0:8", ["const:b87ec4:8", "const:4:8"]]
- 00b87ec4 ["CALLIND", null, ["register:0:8"]]
+ 00b87f8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87f8c ["INT_ADD", "register:40f0:8", ["const:b87f8c:8", "const:4:8"]]
+ 00b87f8c ["CALLIND", null, ["register:0:8"]]
- 00b87ec4 bytes 00013fd6
+ 00b87f8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f19cee4196a26f9c3970ab5e3cd7222"></a>

### [`00b87f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87f2c.md) → [`00b87ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ff4.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4swapERS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87f2c.md#insn-00b88160) · [`00b8816c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87f2c.md#insn-00b8816c) · [`00b88180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b87/00b87f2c.md#insn-00b88180)
- 新版 `00b88228`（命令位置の公開資料なし） · `00b88234`（命令位置の公開資料なし） · `00b88248`（命令位置の公開資料なし）

~~~diff
- 00b88160 ["INT_ADD", "register:40f0:8", ["const:b88160:8", "const:4:8"]]
- 00b88160 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b88228 ["INT_ADD", "register:40f0:8", ["const:b88228:8", "const:4:8"]]
+ 00b88228 ["CALL", null, ["callee:00bdd930:8"]]
- 00b88160 bytes c8550194
+ 00b88228 bytes c2550194
- 00b8816c ["INT_ADD", "register:40f0:8", ["const:b8816c:8", "const:4:8"]]
- 00b8816c ["CALL", null, ["callee:00bdd930:8"]]
+ 00b88234 ["INT_ADD", "register:40f0:8", ["const:b88234:8", "const:4:8"]]
+ 00b88234 ["CALL", null, ["callee:00bdd930:8"]]
- 00b8816c bytes c5550194
+ 00b88234 bytes bf550194
- 00b88180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88180 ["INT_ADD", "register:40f0:8", ["const:b88180:8", "const:4:8"]]
- 00b88180 ["CALLIND", null, ["register:0:8"]]
+ 00b88248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b88248 ["INT_ADD", "register:40f0:8", ["const:b88248:8", "const:4:8"]]
+ 00b88248 ["CALLIND", null, ["register:0:8"]]
- 00b88180 bytes 00013fd6
+ 00b88248 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8aa63cab4f457af1119c5cd353a80fc"></a>

### [`00b88204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88204.md) → [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00525380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525380.md) [`00b7522c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7522c.md) [`00b752e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b752e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00b752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md) [`00b753a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88204.md#insn-00b88260) · [`00b88278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88204.md#insn-00b88278)
- 新版 `00b88328`（命令位置の公開資料なし） · `00b88340`（命令位置の公開資料なし）

~~~diff
- 00b88260 ["INT_ADD", "register:40f0:8", ["const:b88260:8", "const:4:8"]]
- 00b88260 ["CALL", null, ["callee:00b753a8:8"]]
+ 00b88328 ["INT_ADD", "register:40f0:8", ["const:b88328:8", "const:4:8"]]
+ 00b88328 ["CALL", null, ["callee:00b753a8:8"]]
- 00b88260 bytes 20b4ff97
+ 00b88328 bytes 20b4ff97
- 00b88278 ["INT_ADD", "register:40f0:8", ["const:b88278:8", "const:4:8"]]
- 00b88278 ["CALL", null, ["callee:00b752f4:8"]]
+ 00b88340 ["INT_ADD", "register:40f0:8", ["const:b88340:8", "const:4:8"]]
+ 00b88340 ["CALL", null, ["callee:00b752f4:8"]]
- 00b88278 bytes edb3ff97
+ 00b88340 bytes edb3ff97
~~~


<a id="compare-edf6568485de33d16cb700a304e56341"></a>

### [`00b88438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88438.md) → [`00b88500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88e50.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdd0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0b0.md) [`00bdd110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd110.md) [`00bdd140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd140.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88438.md#insn-00b88490) · [`00b884a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88438.md#insn-00b884a0) · [`00b884bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88438.md#insn-00b884bc)
- 新版 `00b88558`（命令位置の公開資料なし） · `00b88568`（命令位置の公開資料なし） · `00b88584`（命令位置の公開資料なし）

~~~diff
- 00b88490 ["INT_ADD", "register:40f0:8", ["const:b88490:8", "const:4:8"]]
- 00b88490 ["CALL", null, ["callee:00b88f18:8"]]
+ 00b88558 ["INT_ADD", "register:40f0:8", ["const:b88558:8", "const:4:8"]]
+ 00b88558 ["CALL", null, ["callee:00b88f18:8"]]
- 00b88490 bytes 70020094
+ 00b88558 bytes 70020094
- 00b884a0 ["INT_ADD", "register:40f0:8", ["const:b884a0:8", "const:4:8"]]
- 00b884a0 ["CALL", null, ["callee:00bdd1f0:8"]]
+ 00b88568 ["INT_ADD", "register:40f0:8", ["const:b88568:8", "const:4:8"]]
+ 00b88568 ["CALL", null, ["callee:00bdd1f0:8"]]
- 00b884a0 bytes 28530194
+ 00b88568 bytes 22530194
- 00b884bc ["INT_ADD", "register:40f0:8", ["const:b884bc:8", "const:4:8"]]
- 00b884bc ["CALL", null, ["callee:00bdd1c0:8"]]
+ 00b88584 ["INT_ADD", "register:40f0:8", ["const:b88584:8", "const:4:8"]]
+ 00b88584 ["CALL", null, ["callee:00bdd1c0:8"]]
- 00b884bc bytes 15530194
+ 00b88584 bytes 0f530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b68bf3c0f0a886bc660683722e29f187"></a>

### [`00b88a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88a9c.md) → [`00b88b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88b64.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE5closeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88a9c.md#insn-00b88ac4) · [`00b88ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88a9c.md#insn-00b88ad0) · [`00b88af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88a9c.md#insn-00b88af8)
- 新版 `00b88b8c`（命令位置の公開資料なし） · `00b88b98`（命令位置の公開資料なし） · `00b88bc0`（命令位置の公開資料なし）

~~~diff
- 00b88ac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88ac4 ["INT_ADD", "register:40f0:8", ["const:b88ac4:8", "const:4:8"]]
- 00b88ac4 ["CALLIND", null, ["register:0:8"]]
+ 00b88b8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b88b8c ["INT_ADD", "register:40f0:8", ["const:b88b8c:8", "const:4:8"]]
+ 00b88b8c ["CALLIND", null, ["register:0:8"]]
- 00b88ac4 bytes 00013fd6
+ 00b88b8c bytes 00013fd6
- 00b88ad0 ["INT_ADD", "register:40f0:8", ["const:b88ad0:8", "const:4:8"]]
- 00b88ad0 ["CALL", null, ["callee:00bdd160:8"]]
+ 00b88b98 ["INT_ADD", "register:40f0:8", ["const:b88b98:8", "const:4:8"]]
+ 00b88b98 ["CALL", null, ["callee:00bdd160:8"]]
- 00b88ad0 bytes 78510194
+ 00b88b98 bytes 72510194
- 00b88af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88af8 ["INT_ADD", "register:40f0:8", ["const:b88af8:8", "const:4:8"]]
- 00b88af8 ["CALLIND", null, ["register:0:8"]]
+ 00b88bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b88bc0 ["INT_ADD", "register:40f0:8", ["const:b88bc0:8", "const:4:8"]]
+ 00b88bc0 ["CALLIND", null, ["register:0:8"]]
- 00b88af8 bytes 00013fd6
+ 00b88bc0 bytes 00013fd6
~~~


<a id="compare-4bf7abb60807b154b4bb1efaad09b04a"></a>

### [`00b89894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89894.md) → [`00b8995c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b8995c.md) FUN_00b8995c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b898a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89894.md#insn-00b898a8)
- 新版 `00b89970`（命令位置の公開資料なし）

~~~diff
- 00b898a8 ["INT_ADD", "register:40f0:8", ["const:b898a8:8", "const:4:8"]]
- 00b898a8 ["CALL", null, ["callee:00bdb100:8"]]
+ 00b89970 ["INT_ADD", "register:40f0:8", ["const:b89970:8", "const:4:8"]]
+ 00b89970 ["CALL", null, ["callee:00bdb100:8"]]
- 00b898a8 bytes ea450194
+ 00b89970 bytes e4450194
~~~


<a id="compare-b6ff5e89b0384e1510378afe7aa61ced"></a>

### [`00b89c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89c28.md) → [`00b89cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89cf0.md) FUN_00b89cf0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89c28.md#insn-00b89c3c)
- 新版 `00b89d04`（命令位置の公開資料なし）

~~~diff
- 00b89c3c ["INT_ADD", "register:40f0:8", ["const:b89c3c:8", "const:4:8"]]
- 00b89c3c ["CALL", null, ["callee:00bdb100:8"]]
+ 00b89d04 ["INT_ADD", "register:40f0:8", ["const:b89d04:8", "const:4:8"]]
+ 00b89d04 ["CALL", null, ["callee:00bdb100:8"]]
- 00b89c3c bytes 05450194
+ 00b89d04 bytes ff440194
~~~


<a id="compare-8e44b650638a4871cb9a39bfbef5492e"></a>

### [`00b89cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89cb0.md) → [`00b89d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d78.md) FUN_00b89d78

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89cb0.md#insn-00b89ce8) · [`00b89d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89cb0.md#insn-00b89d08) · [`00b89d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89cb0.md#insn-00b89d30)
- 新版 `00b89db0`（命令位置の公開資料なし） · `00b89dd0`（命令位置の公開資料なし） · `00b89df8`（命令位置の公開資料なし）

~~~diff
- 00b89ce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89ce8 ["INT_ADD", "register:40f0:8", ["const:b89ce8:8", "const:4:8"]]
- 00b89ce8 ["CALLIND", null, ["register:0:8"]]
+ 00b89db0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89db0 ["INT_ADD", "register:40f0:8", ["const:b89db0:8", "const:4:8"]]
+ 00b89db0 ["CALLIND", null, ["register:0:8"]]
- 00b89ce8 bytes 00013fd6
+ 00b89db0 bytes 00013fd6
- 00b89d08 ["INT_ADD", "register:40f0:8", ["const:b89d08:8", "const:4:8"]]
- 00b89d08 ["CALL", null, ["callee:00bdd380:8"]]
+ 00b89dd0 ["INT_ADD", "register:40f0:8", ["const:b89dd0:8", "const:4:8"]]
+ 00b89dd0 ["CALL", null, ["callee:00bdd380:8"]]
- 00b89d08 bytes 724d0194
+ 00b89dd0 bytes 6c4d0194
- 00b89d30 ["INT_ADD", "register:40f0:8", ["const:b89d30:8", "const:4:8"]]
- 00b89d30 ["CALL", null, ["callee:00bdd310:8"]]
+ 00b89df8 ["INT_ADD", "register:40f0:8", ["const:b89df8:8", "const:4:8"]]
+ 00b89df8 ["CALL", null, ["callee:00bdd310:8"]]
- 00b89d30 bytes 4c4d0194
+ 00b89df8 bytes 464d0194
~~~


<a id="compare-31076a82dbbf8a1bed308d594f53d656"></a>

### [`00b89d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89d54.md) → [`00b89e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89e1c.md) FUN_00b89e1c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89d54.md#insn-00b89dbc)
- 新版 `00b89e84`（命令位置の公開資料なし）

~~~diff
- 00b89dbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89dbc ["INT_ADD", "register:40f0:8", ["const:b89dbc:8", "const:4:8"]]
- 00b89dbc ["CALLIND", null, ["register:0:8"]]
+ 00b89e84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89e84 ["INT_ADD", "register:40f0:8", ["const:b89e84:8", "const:4:8"]]
+ 00b89e84 ["CALLIND", null, ["register:0:8"]]
- 00b89dbc bytes 00013fd6
+ 00b89e84 bytes 00013fd6
~~~


<a id="compare-ef26d1eea1b656dcafea869d01635cc7"></a>

### [`00b89df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89df8.md) → [`00b89ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ec0.md) FUN_00b89ec0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89df8.md#insn-00b89e44) · [`00b89e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89df8.md#insn-00b89e90) · [`00b89ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89df8.md#insn-00b89ecc)
- 新版 `00b89f0c`（命令位置の公開資料なし） · `00b89f58`（命令位置の公開資料なし） · `00b89f94`（命令位置の公開資料なし）

~~~diff
- 00b89e44 ["INT_ADD", "register:40f0:8", ["const:b89e44:8", "const:4:8"]]
- 00b89e44 ["CALL", null, ["callee:00bdd380:8"]]
+ 00b89f0c ["INT_ADD", "register:40f0:8", ["const:b89f0c:8", "const:4:8"]]
+ 00b89f0c ["CALL", null, ["callee:00bdd380:8"]]
- 00b89e44 bytes 234d0194
+ 00b89f0c bytes 1d4d0194
- 00b89e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89e90 ["INT_ADD", "register:40f0:8", ["const:b89e90:8", "const:4:8"]]
- 00b89e90 ["CALLIND", null, ["register:0:8"]]
+ 00b89f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89f58 ["INT_ADD", "register:40f0:8", ["const:b89f58:8", "const:4:8"]]
+ 00b89f58 ["CALLIND", null, ["register:0:8"]]
- 00b89e90 bytes 00013fd6
+ 00b89f58 bytes 00013fd6
- 00b89ecc ["INT_ADD", "register:40f0:8", ["const:b89ecc:8", "const:4:8"]]
- 00b89ecc ["CALL", null, ["callee:00bdd380:8"]]
+ 00b89f94 ["INT_ADD", "register:40f0:8", ["const:b89f94:8", "const:4:8"]]
+ 00b89f94 ["CALL", null, ["callee:00bdd380:8"]]
- 00b89ecc bytes 014d0194
+ 00b89f94 bytes fb4c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6b79ec03768864e2ecae28183fc10a2"></a>

### [`00b89f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89f28.md) → [`00b89ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ff0.md) FUN_00b89ff0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be12c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89f28.md#insn-00b89f3c)
- 新版 `00b8a004`（命令位置の公開資料なし）

~~~diff
- 00b89f3c ["INT_ADD", "register:40f0:8", ["const:b89f3c:8", "const:4:8"]]
- 00b89f3c ["CALL", null, ["callee:00be1370:8"]]
+ 00b8a004 ["INT_ADD", "register:40f0:8", ["const:b8a004:8", "const:4:8"]]
+ 00b8a004 ["CALL", null, ["callee:00be1370:8"]]
- 00b89f3c bytes e15c0194
+ 00b8a004 bytes db5c0194
~~~


<a id="compare-ae15d3caf8092ab22b0a6ff4980e7395"></a>

### [`00b8a2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a2b4.md) → [`00b8a37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a37c.md) FUN_00b8a37c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be12c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a2b4.md#insn-00b8a2c8)
- 新版 `00b8a390`（命令位置の公開資料なし）

~~~diff
- 00b8a2c8 ["INT_ADD", "register:40f0:8", ["const:b8a2c8:8", "const:4:8"]]
- 00b8a2c8 ["CALL", null, ["callee:00be1370:8"]]
+ 00b8a390 ["INT_ADD", "register:40f0:8", ["const:b8a390:8", "const:4:8"]]
+ 00b8a390 ["CALL", null, ["callee:00be1370:8"]]
- 00b8a2c8 bytes fe5b0194
+ 00b8a390 bytes f85b0194
~~~


<a id="compare-f6b1c06e321fbc8ffcdcdd22defff0d4"></a>

### [`00b8a33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a33c.md) → [`00b8a404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a404.md) FUN_00b8a404

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a33c.md#insn-00b8a374) · [`00b8a394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a33c.md#insn-00b8a394) · [`00b8a3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a33c.md#insn-00b8a3bc)
- 新版 `00b8a43c`（命令位置の公開資料なし） · `00b8a45c`（命令位置の公開資料なし） · `00b8a484`（命令位置の公開資料なし）

~~~diff
- 00b8a374 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a374 ["INT_ADD", "register:40f0:8", ["const:b8a374:8", "const:4:8"]]
- 00b8a374 ["CALLIND", null, ["register:0:8"]]
+ 00b8a43c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a43c ["INT_ADD", "register:40f0:8", ["const:b8a43c:8", "const:4:8"]]
+ 00b8a43c ["CALLIND", null, ["register:0:8"]]
- 00b8a374 bytes 00013fd6
+ 00b8a43c bytes 00013fd6
- 00b8a394 ["INT_ADD", "register:40f0:8", ["const:b8a394:8", "const:4:8"]]
- 00b8a394 ["CALL", null, ["callee:00bdd380:8"]]
+ 00b8a45c ["INT_ADD", "register:40f0:8", ["const:b8a45c:8", "const:4:8"]]
+ 00b8a45c ["CALL", null, ["callee:00bdd380:8"]]
- 00b8a394 bytes cf4b0194
+ 00b8a45c bytes c94b0194
- 00b8a3bc ["INT_ADD", "register:40f0:8", ["const:b8a3bc:8", "const:4:8"]]
- 00b8a3bc ["CALL", null, ["callee:00bdd310:8"]]
+ 00b8a484 ["INT_ADD", "register:40f0:8", ["const:b8a484:8", "const:4:8"]]
+ 00b8a484 ["CALL", null, ["callee:00bdd310:8"]]
- 00b8a3bc bytes a94b0194
+ 00b8a484 bytes a34b0194
~~~


<a id="compare-070d610beb10e665e4b62364f5a6c666"></a>

### [`00b8a3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a3e0.md) → [`00b8a4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a4a8.md) FUN_00b8a4a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a3e0.md#insn-00b8a448)
- 新版 `00b8a510`（命令位置の公開資料なし）

~~~diff
- 00b8a448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a448 ["INT_ADD", "register:40f0:8", ["const:b8a448:8", "const:4:8"]]
- 00b8a448 ["CALLIND", null, ["register:0:8"]]
+ 00b8a510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a510 ["INT_ADD", "register:40f0:8", ["const:b8a510:8", "const:4:8"]]
+ 00b8a510 ["CALLIND", null, ["register:0:8"]]
- 00b8a448 bytes 00013fd6
+ 00b8a510 bytes 00013fd6
~~~


<a id="compare-ff9de1e913758ecd5f752d5368ac7ba7"></a>

### [`00b8a484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a484.md) → [`00b8a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a54c.md) FUN_00b8a54c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md) [`00be13e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md) [`00be1490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a484.md#insn-00b8a4c4) · [`00b8a510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a484.md#insn-00b8a510) · [`00b8a54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a484.md#insn-00b8a54c)
- 新版 `00b8a58c`（命令位置の公開資料なし） · `00b8a5d8`（命令位置の公開資料なし） · `00b8a614`（命令位置の公開資料なし）

~~~diff
- 00b8a4c4 ["INT_ADD", "register:40f0:8", ["const:b8a4c4:8", "const:4:8"]]
- 00b8a4c4 ["CALL", null, ["callee:00be1490:8"]]
+ 00b8a58c ["INT_ADD", "register:40f0:8", ["const:b8a58c:8", "const:4:8"]]
+ 00b8a58c ["CALL", null, ["callee:00be1490:8"]]
- 00b8a4c4 bytes c75b0194
+ 00b8a58c bytes c15b0194
- 00b8a510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a510 ["INT_ADD", "register:40f0:8", ["const:b8a510:8", "const:4:8"]]
- 00b8a510 ["CALLIND", null, ["register:0:8"]]
+ 00b8a5d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a5d8 ["INT_ADD", "register:40f0:8", ["const:b8a5d8:8", "const:4:8"]]
+ 00b8a5d8 ["CALLIND", null, ["register:0:8"]]
- 00b8a510 bytes 00013fd6
+ 00b8a5d8 bytes 00013fd6
- 00b8a54c ["INT_ADD", "register:40f0:8", ["const:b8a54c:8", "const:4:8"]]
- 00b8a54c ["CALL", null, ["callee:00bdd380:8"]]
+ 00b8a614 ["INT_ADD", "register:40f0:8", ["const:b8a614:8", "const:4:8"]]
+ 00b8a614 ["CALL", null, ["callee:00bdd380:8"]]
- 00b8a54c bytes 614b0194
+ 00b8a614 bytes 5b4b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7974b321d20295822cda2af5705f4fdf"></a>

### [`00b8a5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a5f4.md) → [`00b8a6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a6bc.md) _ZNSt6__ndk17collateIcED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a5f4.md#insn-00b8a608)
- 新版 `00b8a6d0`（命令位置の公開資料なし）

~~~diff
- 00b8a608 ["INT_ADD", "register:40f0:8", ["const:b8a608:8", "const:4:8"]]
- 00b8a608 ["CALL", null, ["callee:00be14b0:8"]]
+ 00b8a6d0 ["INT_ADD", "register:40f0:8", ["const:b8a6d0:8", "const:4:8"]]
+ 00b8a6d0 ["CALL", null, ["callee:00be14b0:8"]]
- 00b8a608 bytes 7e5b0194
+ 00b8a6d0 bytes 785b0194
~~~


<a id="compare-02b8a00be4bdee9f611ad745cc7c9f2d"></a>

### [`00b8a684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a684.md) → [`00b8a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a74c.md) _ZNKSt6__ndk17collateIcE12do_transformEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a684.md#insn-00b8a6ec) · [`00b8a714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a684.md#insn-00b8a714) · [`00b8a73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a684.md#insn-00b8a73c)
- 新版 `00b8a7b4`（命令位置の公開資料なし） · `00b8a7dc`（命令位置の公開資料なし） · `00b8a804`（命令位置の公開資料なし）

~~~diff
- 00b8a6ec ["INT_ADD", "register:40f0:8", ["const:b8a6ec:8", "const:4:8"]]
- 00b8a6ec ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b8a7b4 ["INT_ADD", "register:40f0:8", ["const:b8a7b4:8", "const:4:8"]]
+ 00b8a7b4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b8a6ec bytes 15420194
+ 00b8a7b4 bytes 0f420194
- 00b8a714 ["INT_ADD", "register:40f0:8", ["const:b8a714:8", "const:4:8"]]
- 00b8a714 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b8a7dc ["INT_ADD", "register:40f0:8", ["const:b8a7dc:8", "const:4:8"]]
+ 00b8a7dc ["CALL", null, ["callee:00bdb160:8"]]
- 00b8a714 bytes 67420194
+ 00b8a7dc bytes 61420194
- 00b8a73c ["INT_ADD", "register:40f0:8", ["const:b8a73c:8", "const:4:8"]]
- 00b8a73c ["CALL", null, ["callee:00418c24:8"]]
+ 00b8a804 ["INT_ADD", "register:40f0:8", ["const:b8a804:8", "const:4:8"]]
+ 00b8a804 ["CALL", null, ["callee:00418c24:8"]]
- 00b8a73c bytes 3a39e297
+ 00b8a804 bytes 0839e297
~~~


<a id="compare-8bfca4ddf82b63c09b8e585f4cb8dfc4"></a>

### [`00b8a780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a780.md) → [`00b8a848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a848.md) _ZNSt6__ndk17collateIwED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be14c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a780.md#insn-00b8a794)
- 新版 `00b8a85c`（命令位置の公開資料なし）

~~~diff
- 00b8a794 ["INT_ADD", "register:40f0:8", ["const:b8a794:8", "const:4:8"]]
- 00b8a794 ["CALL", null, ["callee:00be14c0:8"]]
+ 00b8a85c ["INT_ADD", "register:40f0:8", ["const:b8a85c:8", "const:4:8"]]
+ 00b8a85c ["CALL", null, ["callee:00be14c0:8"]]
- 00b8a794 bytes 1f5b0194
+ 00b8a85c bytes 195b0194
~~~


<a id="compare-9d82bf5da5ad5fee163e62ba1e24007d"></a>

### [`00b8b010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b010.md) → [`00b8b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md) FUN_00b8b0d8

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8b008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b008.md) · 呼出先 6件 [`00bb91f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb91f0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1420.md) [`00be1430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1430.md)
- 新版 呼出元 1件 [`00b8b0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d0.md) · 呼出先 6件 [`00bb92b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b010.md#insn-00b8b098) · [`00b8b0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b010.md#insn-00b8b0b4) · [`00b8b138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b010.md#insn-00b8b138)
- 新版 `00b8b160`（命令位置の公開資料なし） · `00b8b17c`（命令位置の公開資料なし） · `00b8b200`（命令位置の公開資料なし）

~~~diff
- 00b8b098 ["INT_ADD", "register:40f0:8", ["const:b8b098:8", "const:4:8"]]
- 00b8b098 ["CALL", null, ["callee:00be14d0:8"]]
+ 00b8b160 ["INT_ADD", "register:40f0:8", ["const:b8b160:8", "const:4:8"]]
+ 00b8b160 ["CALL", null, ["callee:00be14d0:8"]]
- 00b8b098 bytes e2580194
+ 00b8b160 bytes dc580194
- 00b8b0b4 ["INT_ADD", "register:40f0:8", ["const:b8b0b4:8", "const:4:8"]]
- 00b8b0b4 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8b17c ["INT_ADD", "register:40f0:8", ["const:b8b17c:8", "const:4:8"]]
+ 00b8b17c ["CALL", null, ["callee:00bdef70:8"]]
- 00b8b0b4 bytes 834f0194
+ 00b8b17c bytes 7d4f0194
- 00b8b138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8b138 ["INT_ADD", "register:40f0:8", ["const:b8b138:8", "const:4:8"]]
- 00b8b138 ["CALLIND", null, ["register:0:8"]]
+ 00b8b200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8b200 ["INT_ADD", "register:40f0:8", ["const:b8b200:8", "const:4:8"]]
+ 00b8b200 ["CALLIND", null, ["register:0:8"]]
- 00b8b138 bytes 00013fd6
+ 00b8b200 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94b9d35bf0e814fa93860f4bbca4e269"></a>

### [`00b8b888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b888.md) → [`00b8b950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md) FUN_00b8b950

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8b880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b880.md) · 呼出先 6件 [`00bb9440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9440.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1420.md) [`00be1430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1430.md)
- 新版 呼出元 1件 [`00b8b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b948.md) · 呼出先 6件 [`00bb9508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b888.md#insn-00b8b910) · [`00b8b92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b888.md#insn-00b8b92c) · [`00b8b9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b888.md#insn-00b8b9b0)
- 新版 `00b8b9d8`（命令位置の公開資料なし） · `00b8b9f4`（命令位置の公開資料なし） · `00b8ba78`（命令位置の公開資料なし）

~~~diff
- 00b8b910 ["INT_ADD", "register:40f0:8", ["const:b8b910:8", "const:4:8"]]
- 00b8b910 ["CALL", null, ["callee:00be14d0:8"]]
+ 00b8b9d8 ["INT_ADD", "register:40f0:8", ["const:b8b9d8:8", "const:4:8"]]
+ 00b8b9d8 ["CALL", null, ["callee:00be14d0:8"]]
- 00b8b910 bytes c4560194
+ 00b8b9d8 bytes be560194
- 00b8b92c ["INT_ADD", "register:40f0:8", ["const:b8b92c:8", "const:4:8"]]
- 00b8b92c ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8b9f4 ["INT_ADD", "register:40f0:8", ["const:b8b9f4:8", "const:4:8"]]
+ 00b8b9f4 ["CALL", null, ["callee:00bdef70:8"]]
- 00b8b92c bytes 654d0194
+ 00b8b9f4 bytes 5f4d0194
- 00b8b9b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8b9b0 ["INT_ADD", "register:40f0:8", ["const:b8b9b0:8", "const:4:8"]]
- 00b8b9b0 ["CALLIND", null, ["register:0:8"]]
+ 00b8ba78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8ba78 ["INT_ADD", "register:40f0:8", ["const:b8ba78:8", "const:4:8"]]
+ 00b8ba78 ["CALLIND", null, ["register:0:8"]]
- 00b8b9b0 bytes 00013fd6
+ 00b8ba78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02eec75ae87af231d1a435a76a8a605"></a>

### [`00b8bcc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcc4.md) → [`00b8bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md) FUN_00b8bd8c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8bcbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcbc.md) · 呼出先 6件 [`00bb9598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1420.md) [`00be1430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1430.md)
- 新版 呼出元 1件 [`00b8bd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd84.md) · 呼出先 6件 [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8bd4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcc4.md#insn-00b8bd4c) · [`00b8bd68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcc4.md#insn-00b8bd68) · [`00b8bdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcc4.md#insn-00b8bdec)
- 新版 `00b8be14`（命令位置の公開資料なし） · `00b8be30`（命令位置の公開資料なし） · `00b8beb4`（命令位置の公開資料なし）

~~~diff
- 00b8bd4c ["INT_ADD", "register:40f0:8", ["const:b8bd4c:8", "const:4:8"]]
- 00b8bd4c ["CALL", null, ["callee:00be14d0:8"]]
+ 00b8be14 ["INT_ADD", "register:40f0:8", ["const:b8be14:8", "const:4:8"]]
+ 00b8be14 ["CALL", null, ["callee:00be14d0:8"]]
- 00b8bd4c bytes b5550194
+ 00b8be14 bytes af550194
- 00b8bd68 ["INT_ADD", "register:40f0:8", ["const:b8bd68:8", "const:4:8"]]
- 00b8bd68 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8be30 ["INT_ADD", "register:40f0:8", ["const:b8be30:8", "const:4:8"]]
+ 00b8be30 ["CALL", null, ["callee:00bdef70:8"]]
- 00b8bd68 bytes 564c0194
+ 00b8be30 bytes 504c0194
- 00b8bdec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8bdec ["INT_ADD", "register:40f0:8", ["const:b8bdec:8", "const:4:8"]]
- 00b8bdec ["CALLIND", null, ["register:0:8"]]
+ 00b8beb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8beb4 ["INT_ADD", "register:40f0:8", ["const:b8beb4:8", "const:4:8"]]
+ 00b8beb4 ["CALLIND", null, ["register:0:8"]]
- 00b8bdec bytes 00013fd6
+ 00b8beb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0094a59c51050d54bbe3daab5bc187be"></a>

### [`00b8c978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c978.md) → [`00b8ca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md) FUN_00b8ca40

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8c970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c970.md) · 呼出先 6件 [`00bb997c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb997c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1440.md) [`00be1450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1450.md)
- 新版 呼出元 1件 [`00b8ca38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca38.md) · 呼出先 6件 [`00bb9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8c9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c978.md#insn-00b8c9c4) · [`00b8c9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c978.md#insn-00b8c9e0) · [`00b8ca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c978.md#insn-00b8ca70)
- 新版 `00b8ca8c`（命令位置の公開資料なし） · `00b8caa8`（命令位置の公開資料なし） · `00b8cb38`（命令位置の公開資料なし）

~~~diff
- 00b8c9c4 ["INT_ADD", "register:40f0:8", ["const:b8c9c4:8", "const:4:8"]]
- 00b8c9c4 ["CALL", null, ["callee:00be1500:8"]]
+ 00b8ca8c ["INT_ADD", "register:40f0:8", ["const:b8ca8c:8", "const:4:8"]]
+ 00b8ca8c ["CALL", null, ["callee:00be1500:8"]]
- 00b8c9c4 bytes a3520194
+ 00b8ca8c bytes 9d520194
- 00b8c9e0 ["INT_ADD", "register:40f0:8", ["const:b8c9e0:8", "const:4:8"]]
- 00b8c9e0 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8caa8 ["INT_ADD", "register:40f0:8", ["const:b8caa8:8", "const:4:8"]]
+ 00b8caa8 ["CALL", null, ["callee:00bdef70:8"]]
- 00b8c9e0 bytes 38490194
+ 00b8caa8 bytes 32490194
- 00b8ca70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8ca70 ["INT_ADD", "register:40f0:8", ["const:b8ca70:8", "const:4:8"]]
- 00b8ca70 ["CALLIND", null, ["register:0:8"]]
+ 00b8cb38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8cb38 ["INT_ADD", "register:40f0:8", ["const:b8cb38:8", "const:4:8"]]
+ 00b8cb38 ["CALLIND", null, ["register:0:8"]]
- 00b8ca70 bytes 00013fd6
+ 00b8cb38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e142972439e3c64cd784153ce2779ae"></a>

### [`00b8d1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a8.md) → [`00b8d270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md) FUN_00b8d270

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8d1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a0.md) · 呼出先 6件 [`00bb9bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9bac.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1440.md) [`00be1450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1450.md)
- 新版 呼出元 1件 [`00b8d268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d268.md) · 呼出先 6件 [`00bb9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8d1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a8.md#insn-00b8d1f4) · [`00b8d210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a8.md#insn-00b8d210) · [`00b8d2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a8.md#insn-00b8d2a0)
- 新版 `00b8d2bc`（命令位置の公開資料なし） · `00b8d2d8`（命令位置の公開資料なし） · `00b8d368`（命令位置の公開資料なし）

~~~diff
- 00b8d1f4 ["INT_ADD", "register:40f0:8", ["const:b8d1f4:8", "const:4:8"]]
- 00b8d1f4 ["CALL", null, ["callee:00be1500:8"]]
+ 00b8d2bc ["INT_ADD", "register:40f0:8", ["const:b8d2bc:8", "const:4:8"]]
+ 00b8d2bc ["CALL", null, ["callee:00be1500:8"]]
- 00b8d1f4 bytes 97500194
+ 00b8d2bc bytes 91500194
- 00b8d210 ["INT_ADD", "register:40f0:8", ["const:b8d210:8", "const:4:8"]]
- 00b8d210 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8d2d8 ["INT_ADD", "register:40f0:8", ["const:b8d2d8:8", "const:4:8"]]
+ 00b8d2d8 ["CALL", null, ["callee:00bdef70:8"]]
- 00b8d210 bytes 2c470194
+ 00b8d2d8 bytes 26470194
- 00b8d2a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8d2a0 ["INT_ADD", "register:40f0:8", ["const:b8d2a0:8", "const:4:8"]]
- 00b8d2a0 ["CALLIND", null, ["register:0:8"]]
+ 00b8d368 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8d368 ["INT_ADD", "register:40f0:8", ["const:b8d368:8", "const:4:8"]]
+ 00b8d368 ["CALLIND", null, ["register:0:8"]]
- 00b8d2a0 bytes 00013fd6
+ 00b8d368 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e140238142937304af92c772471e554"></a>

### [`00b8f180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f180.md) → [`00b8f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md) FUN_00b8f248

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8f178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f178.md) · 呼出先 6件 [`00bb9598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1440.md) [`00be14a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be14a0.md)
- 新版 呼出元 1件 [`00b8f240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f240.md) · 呼出先 6件 [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8f208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f180.md#insn-00b8f208) · [`00b8f224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f180.md#insn-00b8f224) · [`00b8f294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f180.md#insn-00b8f294)
- 新版 `00b8f2d0`（命令位置の公開資料なし） · `00b8f2ec`（命令位置の公開資料なし） · `00b8f35c`（命令位置の公開資料なし）

~~~diff
- 00b8f208 ["INT_ADD", "register:40f0:8", ["const:b8f208:8", "const:4:8"]]
- 00b8f208 ["CALL", null, ["callee:00be1550:8"]]
+ 00b8f2d0 ["INT_ADD", "register:40f0:8", ["const:b8f2d0:8", "const:4:8"]]
+ 00b8f2d0 ["CALL", null, ["callee:00be1550:8"]]
- 00b8f208 bytes a6480194
+ 00b8f2d0 bytes a0480194
- 00b8f224 ["INT_ADD", "register:40f0:8", ["const:b8f224:8", "const:4:8"]]
- 00b8f224 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b8f2ec ["INT_ADD", "register:40f0:8", ["const:b8f2ec:8", "const:4:8"]]
+ 00b8f2ec ["CALL", null, ["callee:00bdef70:8"]]
- 00b8f224 bytes 273f0194
+ 00b8f2ec bytes 213f0194
- 00b8f294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8f294 ["INT_ADD", "register:40f0:8", ["const:b8f294:8", "const:4:8"]]
- 00b8f294 ["CALLIND", null, ["register:0:8"]]
+ 00b8f35c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8f35c ["INT_ADD", "register:40f0:8", ["const:b8f35c:8", "const:4:8"]]
+ 00b8f35c ["CALLIND", null, ["register:0:8"]]
- 00b8f294 bytes 00013fd6
+ 00b8f35c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30c2717487909ccf556461b444c1e2d"></a>

### [`00b9021c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b9021c.md) → [`00b902e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md) FUN_00b902e4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b90214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90214.md) · 呼出先 6件 [`00bb9a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1440.md) [`00be14c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be14c0.md)
- 新版 呼出元 1件 [`00b902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902dc.md) · 呼出先 6件 [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b90268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b9021c.md#insn-00b90268) · [`00b90284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b9021c.md#insn-00b90284) · [`00b90304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b9021c.md#insn-00b90304)
- 新版 `00b90330`（命令位置の公開資料なし） · `00b9034c`（命令位置の公開資料なし） · `00b903cc`（命令位置の公開資料なし）

~~~diff
- 00b90268 ["INT_ADD", "register:40f0:8", ["const:b90268:8", "const:4:8"]]
- 00b90268 ["CALL", null, ["callee:00be1570:8"]]
+ 00b90330 ["INT_ADD", "register:40f0:8", ["const:b90330:8", "const:4:8"]]
+ 00b90330 ["CALL", null, ["callee:00be1570:8"]]
- 00b90268 bytes 96440194
+ 00b90330 bytes 90440194
- 00b90284 ["INT_ADD", "register:40f0:8", ["const:b90284:8", "const:4:8"]]
- 00b90284 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b9034c ["INT_ADD", "register:40f0:8", ["const:b9034c:8", "const:4:8"]]
+ 00b9034c ["CALL", null, ["callee:00bdef70:8"]]
- 00b90284 bytes 0f3b0194
+ 00b9034c bytes 093b0194
- 00b90304 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b90304 ["INT_ADD", "register:40f0:8", ["const:b90304:8", "const:4:8"]]
- 00b90304 ["CALLIND", null, ["register:0:8"]]
+ 00b903cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b903cc ["INT_ADD", "register:40f0:8", ["const:b903cc:8", "const:4:8"]]
+ 00b903cc ["CALLIND", null, ["register:0:8"]]
- 00b90304 bytes 00013fd6
+ 00b903cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01fe00c2d6c56866ee9739ccd52adee"></a>

### [`00b93228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93228.md) → [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) FUN_00b932f0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`00b91e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b91e04.md) [`00b92050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b92050.md) [`00b9229c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b9229c.md) [`00b924cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b924cc.md) [`00b926fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b92/00b926fc.md) · 呼出先 2件 [`00bde1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1d0.md) [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md)
- 新版 呼出元 14件 [`00b91ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md) [`00b92118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md) [`00b92364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md) [`00b92594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md) [`00b927c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md) · 呼出先 2件 [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93228.md#insn-00b93290) · [`00b932b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93228.md#insn-00b932b0) · [`00b932c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93228.md#insn-00b932c0)
- 新版 `00b93358`（命令位置の公開資料なし） · `00b93378`（命令位置の公開資料なし） · `00b93388`（命令位置の公開資料なし）

~~~diff
- 00b93290 ["INT_ADD", "register:40f0:8", ["const:b93290:8", "const:4:8"]]
- 00b93290 ["CALL", null, ["callee:00be1530:8"]]
+ 00b93358 ["INT_ADD", "register:40f0:8", ["const:b93358:8", "const:4:8"]]
+ 00b93358 ["CALL", null, ["callee:00be1530:8"]]
- 00b93290 bytes 7c380194
+ 00b93358 bytes 76380194
- 00b932b0 ["INT_ADD", "register:40f0:8", ["const:b932b0:8", "const:4:8"]]
- 00b932b0 ["CALL", null, ["callee:00bde280:8"]]
+ 00b93378 ["INT_ADD", "register:40f0:8", ["const:b93378:8", "const:4:8"]]
+ 00b93378 ["CALL", null, ["callee:00bde280:8"]]
- 00b932b0 bytes c82b0194
+ 00b93378 bytes c22b0194
- 00b932c0 ["INT_ADD", "register:40f0:8", ["const:b932c0:8", "const:4:8"]]
- 00b932c0 ["CALL", null, ["callee:00be1530:8"]]
+ 00b93388 ["INT_ADD", "register:40f0:8", ["const:b93388:8", "const:4:8"]]
+ 00b93388 ["CALL", null, ["callee:00be1530:8"]]
- 00b932c0 bytes 70380194
+ 00b93388 bytes 6a380194
~~~


<a id="compare-8780ed687e5c2ea661d08afa38009c76"></a>

### [`00b94968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b94/00b94968.md) → [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) FUN_00b94a30

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00b93538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93538.md) [`00b93784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93784.md) [`00b939d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b939d0.md) [`00b93c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93c00.md) [`00b93e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b93/00b93e30.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 9件 [`00b93600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md) [`00b9384c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md) [`00b93a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md) [`00b93cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md) [`00b93ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b949d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b94/00b94968.md#insn-00b949d4) · [`00b94a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b94/00b94968.md#insn-00b94a38) · [`00b94ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b94/00b94968.md#insn-00b94ac0)
- 新版 `00b94a9c`（命令位置の公開資料なし） · `00b94b00`（命令位置の公開資料なし） · `00b94b88`（命令位置の公開資料なし）

~~~diff
- 00b949d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b949d4 ["INT_ADD", "register:40f0:8", ["const:b949d4:8", "const:4:8"]]
- 00b949d4 ["CALLIND", null, ["register:0:8"]]
+ 00b94a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b94a9c ["INT_ADD", "register:40f0:8", ["const:b94a9c:8", "const:4:8"]]
+ 00b94a9c ["CALLIND", null, ["register:0:8"]]
- 00b949d4 bytes 00013fd6
+ 00b94a9c bytes 00013fd6
- 00b94a38 ["INT_ADD", "register:40f0:8", ["const:b94a38:8", "const:4:8"]]
- 00b94a38 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b94b00 ["INT_ADD", "register:40f0:8", ["const:b94b00:8", "const:4:8"]]
+ 00b94b00 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b94a38 bytes 42190194
+ 00b94b00 bytes 3c190194
- 00b94ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b94ac0 ["INT_ADD", "register:40f0:8", ["const:b94ac0:8", "const:4:8"]]
- 00b94ac0 ["CALLIND", null, ["register:0:8"]]
+ 00b94b88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b94b88 ["INT_ADD", "register:40f0:8", ["const:b94b88:8", "const:4:8"]]
+ 00b94b88 ["CALLIND", null, ["register:0:8"]]
- 00b94ac0 bytes 00013fd6
+ 00b94b88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4270a21978795eb5f5380ddf831f3d4"></a>

### [`00b9642c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b9642c.md) → [`00b964f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b964f4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd820.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9645c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b9642c.md#insn-00b9645c)
- 新版 `00b96524`（命令位置の公開資料なし）

~~~diff
- 00b9645c ["INT_ADD", "register:40f0:8", ["const:b9645c:8", "const:4:8"]]
- 00b9645c ["CALL", null, ["callee:00bdd8d0:8"]]
+ 00b96524 ["INT_ADD", "register:40f0:8", ["const:b96524:8", "const:4:8"]]
+ 00b96524 ["CALL", null, ["callee:00bdd8d0:8"]]
- 00b9645c bytes f11c0194
+ 00b96524 bytes eb1c0194
~~~


