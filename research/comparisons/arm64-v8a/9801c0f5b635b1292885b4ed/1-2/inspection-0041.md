# v16.0.0 → v16.0.1 · 要調査の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-ba2ef230421d536f253296d8429b98d1"></a>

### [`00bfa2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2bc.md) → [`00bfa6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa6e4.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md) · 呼出先 1件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`00c58180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58180.md) · 呼出先 1件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2bc.md#insn-00bfa2d8)
- 新版 [`00bfa700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa6e4.md#insn-00bfa700)

~~~diff
- 00bfa2d8 ["INT_ADD", "register:40f0:8", ["const:bfa2d8:8", "const:4:8"]]
- 00bfa2d8 ["CALL", null, ["callee:00c58020:8"]]
+ 00bfa700 ["INT_ADD", "register:40f0:8", ["const:bfa700:8", "const:4:8"]]
+ 00bfa700 ["CALL", null, ["callee:00c58020:8"]]
- 00bfa2d8 bytes 52760194
+ 00bfa700 bytes 48760194
~~~


<a id="compare-36df670fe4767647a9862cc072692ec2"></a>

### [`00bfa370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa370.md) → [`00bfa798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa798.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa370.md#insn-00bfa380)
- 新版 [`00bfa7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa798.md#insn-00bfa7a8)

~~~diff
- 00bfa380 ["INT_ADD", "register:40f0:8", ["const:bfa380:8", "const:4:8"]]
- 00bfa380 ["CALL", null, ["callee:00c5e290:8"]]
+ 00bfa7a8 ["INT_ADD", "register:40f0:8", ["const:bfa7a8:8", "const:4:8"]]
+ 00bfa7a8 ["CALL", null, ["callee:00c5e290:8"]]
- 00bfa380 bytes c48e0194
+ 00bfa7a8 bytes ba8e0194
~~~


<a id="compare-4e21b4b162cbb24a01a2909edf9b4f35"></a>

### [`00bfa39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa39c.md) → [`00bfa7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58090.md) · 呼出先 2件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dea0.md)
- 新版 呼出元 1件 [`00c58490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58490.md) · 呼出先 2件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa39c.md#insn-00bfa3f0) · [`00bfa3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa39c.md#insn-00bfa3fc)
- 新版 [`00bfa818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md#insn-00bfa818) · [`00bfa824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa7c4.md#insn-00bfa824)

~~~diff
- 00bfa3f0 ["INT_ADD", "register:40f0:8", ["const:bfa3f0:8", "const:4:8"]]
- 00bfa3f0 ["CALL", null, ["callee:00c5e2a0:8"]]
+ 00bfa818 ["INT_ADD", "register:40f0:8", ["const:bfa818:8", "const:4:8"]]
+ 00bfa818 ["CALL", null, ["callee:00c5e2a0:8"]]
- 00bfa3f0 bytes ac8e0194
+ 00bfa818 bytes a28e0194
- 00bfa3fc ["INT_ADD", "register:40f0:8", ["const:bfa3fc:8", "const:4:8"]]
- 00bfa3fc ["CALL", null, ["callee:00c580c0:8"]]
+ 00bfa824 ["INT_ADD", "register:40f0:8", ["const:bfa824:8", "const:4:8"]]
+ 00bfa824 ["CALL", null, ["callee:00c580c0:8"]]
- 00bfa3fc bytes 31760194
+ 00bfa824 bytes 27760194
~~~


<a id="compare-03aed0459e0820e6f6bca5c0a4c9c78c"></a>

### [`00bfa4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md) → [`00bfa8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md) FUN_00bfa8fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) · 呼出先 5件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c5de50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de50.md)
- 新版 呼出元 1件 [`00bfabf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md) · 呼出先 5件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) [`00c5e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md#insn-00bfa4fc) · [`00bfa504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md#insn-00bfa504) · [`00bfa52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md#insn-00bfa52c)
- 新版 [`00bfa924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa924) · [`00bfa92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa92c) · [`00bfa954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md#insn-00bfa954)

~~~diff
- 00bfa4fc ["INT_ADD", "register:40f0:8", ["const:bfa4fc:8", "const:4:8"]]
- 00bfa4fc ["CALL", null, ["callee:00c58380:8"]]
+ 00bfa924 ["INT_ADD", "register:40f0:8", ["const:bfa924:8", "const:4:8"]]
+ 00bfa924 ["CALL", null, ["callee:00c58380:8"]]
- 00bfa4fc bytes a1760194
+ 00bfa924 bytes 97760194
- 00bfa504 ["INT_ADD", "register:40f0:8", ["const:bfa504:8", "const:4:8"]]
- 00bfa504 ["CALL", null, ["callee:00c580f0:8"]]
+ 00bfa92c ["INT_ADD", "register:40f0:8", ["const:bfa92c:8", "const:4:8"]]
+ 00bfa92c ["CALL", null, ["callee:00c580f0:8"]]
- 00bfa504 bytes fb750194
+ 00bfa92c bytes f1750194
- 00bfa52c ["INT_ADD", "register:40f0:8", ["const:bfa52c:8", "const:4:8"]]
- 00bfa52c ["CALL", null, ["callee:00c5e250:8"]]
+ 00bfa954 ["INT_ADD", "register:40f0:8", ["const:bfa954:8", "const:4:8"]]
+ 00bfa954 ["CALL", null, ["callee:00c5e250:8"]]
- 00bfa52c bytes 498e0194
+ 00bfa954 bytes 3f8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563194bcc798f96d97c511b7116e74c8"></a>

### [`00bfa5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md) → [`00bfa9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md) FUN_00bfa9c8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfa80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa80c.md) · 呼出先 4件 [`00bfa824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00bfac34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac34.md) · 呼出先 4件 [`00bfac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md#insn-00bfa61c) · [`00bfa660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md#insn-00bfa660) · [`00bfa674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md#insn-00bfa674)
- 新版 [`00bfaa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa44) · [`00bfaa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa88) · [`00bfaa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md#insn-00bfaa9c)

~~~diff
- 00bfa61c ["INT_ADD", "register:40f0:8", ["const:bfa61c:8", "const:4:8"]]
- 00bfa61c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bfaa44 ["INT_ADD", "register:40f0:8", ["const:bfaa44:8", "const:4:8"]]
+ 00bfaa44 ["CALL", null, ["callee:00c57e90:8"]]
- 00bfa61c bytes 1d750194
+ 00bfaa44 bytes 13750194
- 00bfa660 ["INT_ADD", "register:40f0:8", ["const:bfa660:8", "const:4:8"]]
- 00bfa660 ["CALL", null, ["callee:00c58000:8"]]
+ 00bfaa88 ["INT_ADD", "register:40f0:8", ["const:bfaa88:8", "const:4:8"]]
+ 00bfaa88 ["CALL", null, ["callee:00c58000:8"]]
- 00bfa660 bytes 68750194
+ 00bfaa88 bytes 5e750194
- 00bfa674 ["INT_ADD", "register:40f0:8", ["const:bfa674:8", "const:4:8"]]
- 00bfa674 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bfaa9c ["INT_ADD", "register:40f0:8", ["const:bfaa9c:8", "const:4:8"]]
+ 00bfaa9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bfa674 bytes 0f750194
+ 00bfaa9c bytes 05750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f9db51c5a24ef443e7cfb7a8dadd92d"></a>

### [`00bfa69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) → [`00bfaac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md) FUN_00bfaac4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfa818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa818.md) · 呼出先 5件 [`00bfa83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00bfac40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac40.md) · 呼出先 5件 [`00bfac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md#insn-00bfa710) · [`00bfa744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md#insn-00bfa744) · [`00bfa758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md#insn-00bfa758)
- 新版 [`00bfab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab38) · [`00bfab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab6c) · [`00bfab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md#insn-00bfab80)

~~~diff
- 00bfa710 ["INT_ADD", "register:40f0:8", ["const:bfa710:8", "const:4:8"]]
- 00bfa710 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bfab38 ["INT_ADD", "register:40f0:8", ["const:bfab38:8", "const:4:8"]]
+ 00bfab38 ["CALL", null, ["callee:00c57e90:8"]]
- 00bfa710 bytes e0740194
+ 00bfab38 bytes d6740194
- 00bfa744 ["INT_ADD", "register:40f0:8", ["const:bfa744:8", "const:4:8"]]
- 00bfa744 ["CALL", null, ["callee:00c58000:8"]]
+ 00bfab6c ["INT_ADD", "register:40f0:8", ["const:bfab6c:8", "const:4:8"]]
+ 00bfab6c ["CALL", null, ["callee:00c58000:8"]]
- 00bfa744 bytes 2f750194
+ 00bfab6c bytes 25750194
- 00bfa758 ["INT_ADD", "register:40f0:8", ["const:bfa758:8", "const:4:8"]]
- 00bfa758 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bfab80 ["INT_ADD", "register:40f0:8", ["const:bfab80:8", "const:4:8"]]
+ 00bfab80 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bfa758 bytes d6740194
+ 00bfab80 bytes cc740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd034768b97e456933eab7fa79fa0d58"></a>

### [`00bfa78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa78c.md) → [`00bfabb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabb4.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa78c.md#insn-00bfa7a4)
- 新版 [`00bfabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabb4.md#insn-00bfabcc)

~~~diff
- 00bfa7a4 ["INT_ADD", "register:40f0:8", ["const:bfa7a4:8", "const:4:8"]]
- 00bfa7a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bfabcc ["INT_ADD", "register:40f0:8", ["const:bfabcc:8", "const:4:8"]]
+ 00bfabcc ["CALL", null, ["callee:00c57e90:8"]]
- 00bfa7a4 bytes bb740194
+ 00bfabcc bytes b1740194
~~~


<a id="compare-a5610e2a13cc9f2dbeb3f3b2b2a10ebb"></a>

### [`00bfa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) → [`00bfabf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md) _ZNSt6__ndk115__thread_structD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md) · 呼出先 2件 [`00bfa4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md) · 呼出先 2件 [`00bfa8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md#insn-00bfa7e4)
- 新版 [`00bfac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfabf0.md#insn-00bfac0c)

~~~diff
- 00bfa7e4 ["INT_ADD", "register:40f0:8", ["const:bfa7e4:8", "const:4:8"]]
- 00bfa7e4 ["CALL", null, ["callee:00bfa8fc:8"]]
+ 00bfac0c ["INT_ADD", "register:40f0:8", ["const:bfac0c:8", "const:4:8"]]
+ 00bfac0c ["CALL", null, ["callee:00bfa8fc:8"]]
- 00bfa7e4 bytes 3cffff97
+ 00bfac0c bytes 3cffff97
~~~


<a id="compare-34f227b980e42878892784c9e6e3e88d"></a>

### [`00bfa854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md) → [`00bfac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md) FUN_00bfac7c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 1件 [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md#insn-00bfa870)
- 新版 [`00bfac98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md#insn-00bfac98)

~~~diff
- 00bfa870 ["INT_ADD", "register:40f0:8", ["const:bfa870:8", "const:4:8"]]
- 00bfa870 ["CALL", null, ["callee:00c58150:8"]]
+ 00bfac98 ["INT_ADD", "register:40f0:8", ["const:bfac98:8", "const:4:8"]]
+ 00bfac98 ["CALL", null, ["callee:00c58150:8"]]
- 00bfa870 bytes 38750194
+ 00bfac98 bytes 2e750194
~~~


<a id="compare-5c382600370839cf7f50bd5342968168"></a>

### [`00bfa930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa930.md) → [`00bfad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md) _ZNSt6__ndk113random_deviceD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md) [`00c57fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fd0.md) · 呼出先 1件 [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)
- 新版 呼出元 2件 [`0056078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md) [`00c583d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583d0.md) · 呼出先 1件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa930.md#insn-00bfa940)
- 新版 [`00bfad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md#insn-00bfad68)

~~~diff
- 00bfa940 ["INT_ADD", "register:40f0:8", ["const:bfa940:8", "const:4:8"]]
- 00bfa940 ["CALL", null, ["callee:00c597d0:8"]]
+ 00bfad68 ["INT_ADD", "register:40f0:8", ["const:bfad68:8", "const:4:8"]]
+ 00bfad68 ["CALL", null, ["callee:00c597d0:8"]]
- 00bfa940 bytes a47a0194
+ 00bfad68 bytes 9a7a0194
~~~


<a id="compare-624a702f4f2019dc5596b509e03f794a"></a>

### [`00bfa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa9e8.md) → [`00bfae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae10.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5deb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5deb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfaa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa9e8.md#insn-00bfaa08)
- 新版 [`00bfae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae10.md#insn-00bfae30)

~~~diff
- 00bfaa08 ["INT_ADD", "register:40f0:8", ["const:bfaa08:8", "const:4:8"]]
- 00bfaa08 ["CALL", null, ["callee:00c5e2b0:8"]]
+ 00bfae30 ["INT_ADD", "register:40f0:8", ["const:bfae30:8", "const:4:8"]]
+ 00bfae30 ["CALL", null, ["callee:00c5e2b0:8"]]
- 00bfaa08 bytes 2a8d0194
+ 00bfae30 bytes 208d0194
~~~


<a id="compare-2cf1ea63282e78eed9f59259431767ed"></a>

### [`00bfab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab9c.md) → [`00bfafc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafc4.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dec0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfabb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab9c.md#insn-00bfabb0)
- 新版 [`00bfafd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafc4.md#insn-00bfafd8)

~~~diff
- 00bfabb0 ["INT_ADD", "register:40f0:8", ["const:bfabb0:8", "const:4:8"]]
- 00bfabb0 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00bfafd8 ["INT_ADD", "register:40f0:8", ["const:bfafd8:8", "const:4:8"]]
+ 00bfafd8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00bfabb0 bytes c48c0194
+ 00bfafd8 bytes ba8c0194
~~~


<a id="compare-0e2ed90b512dbc4f1295225d3078ceb9"></a>

### [`00bfabc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfabc8.md) → [`00bfaff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaff0.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfac08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfabc8.md#insn-00bfac08)
- 新版 [`00bfb030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaff0.md#insn-00bfb030)

~~~diff
- 00bfac08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfac08 ["INT_ADD", "register:40f0:8", ["const:bfac08:8", "const:4:8"]]
- 00bfac08 ["CALLIND", null, ["register:0:8"]]
+ 00bfb030 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb030 ["INT_ADD", "register:40f0:8", ["const:bfb030:8", "const:4:8"]]
+ 00bfb030 ["CALLIND", null, ["register:0:8"]]
- 00bfac08 bytes 00013fd6
+ 00bfb030 bytes 00013fd6
~~~


<a id="compare-eeb946eadbee1fd43aa28901bc0659b0"></a>

### [`00bfac2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfac2c.md) → [`00bfb054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfac54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfac2c.md#insn-00bfac54) · [`00bfac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfac2c.md#insn-00bfac60) · [`00bfac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfac2c.md#insn-00bfac84)
- 新版 [`00bfb07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb07c) · [`00bfb088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb088) · [`00bfb0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md#insn-00bfb0ac)

~~~diff
- 00bfac54 ["INT_ADD", "register:40f0:8", ["const:bfac54:8", "const:4:8"]]
- 00bfac54 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfb07c ["INT_ADD", "register:40f0:8", ["const:bfb07c:8", "const:4:8"]]
+ 00bfb07c ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfac54 bytes df7d0194
+ 00bfb07c bytes d57d0194
- 00bfac60 ["INT_ADD", "register:40f0:8", ["const:bfac60:8", "const:4:8"]]
- 00bfac60 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfb088 ["INT_ADD", "register:40f0:8", ["const:bfb088:8", "const:4:8"]]
+ 00bfb088 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfac60 bytes a08c0194
+ 00bfb088 bytes 968c0194
- 00bfac84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfac84 ["INT_ADD", "register:40f0:8", ["const:bfac84:8", "const:4:8"]]
- 00bfac84 ["CALLIND", null, ["register:0:8"]]
+ 00bfb0ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb0ac ["INT_ADD", "register:40f0:8", ["const:bfb0ac:8", "const:4:8"]]
+ 00bfb0ac ["CALLIND", null, ["register:0:8"]]
- 00bfac84 bytes 00013fd6
+ 00bfb0ac bytes 00013fd6
~~~


<a id="compare-5372bb6fe0ea61c7be3786b62129b826"></a>

### [`00bfb0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0b0.md) → [`00bfb4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb4d8.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5def0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0b0.md#insn-00bfb0c4)
- 新版 [`00bfb4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb4d8.md#insn-00bfb4ec)

~~~diff
- 00bfb0c4 ["INT_ADD", "register:40f0:8", ["const:bfb0c4:8", "const:4:8"]]
- 00bfb0c4 ["CALL", null, ["callee:00c5e2f0:8"]]
+ 00bfb4ec ["INT_ADD", "register:40f0:8", ["const:bfb4ec:8", "const:4:8"]]
+ 00bfb4ec ["CALL", null, ["callee:00c5e2f0:8"]]
- 00bfb0c4 bytes 8b8b0194
+ 00bfb4ec bytes 818b0194
~~~


<a id="compare-4ce2d57b1b6758f6e1362682a1d8848c"></a>

### [`00bfb208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb208.md) → [`00bfb630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md) · 呼出先 5件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 1件 [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb208.md#insn-00bfb23c) · [`00bfb24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb208.md#insn-00bfb24c) · [`00bfb278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb208.md#insn-00bfb278)
- 新版 [`00bfb664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb664) · [`00bfb674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb674) · [`00bfb6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md#insn-00bfb6a0)

~~~diff
- 00bfb23c ["INT_ADD", "register:40f0:8", ["const:bfb23c:8", "const:4:8"]]
- 00bfb23c ["CALL", null, ["callee:00c5a020:8"]]
+ 00bfb664 ["INT_ADD", "register:40f0:8", ["const:bfb664:8", "const:4:8"]]
+ 00bfb664 ["CALL", null, ["callee:00c5a020:8"]]
- 00bfb23c bytes 797a0194
+ 00bfb664 bytes 6f7a0194
- 00bfb24c ["INT_ADD", "register:40f0:8", ["const:bfb24c:8", "const:4:8"]]
- 00bfb24c ["CALL", null, ["callee:00c5a020:8"]]
+ 00bfb674 ["INT_ADD", "register:40f0:8", ["const:bfb674:8", "const:4:8"]]
+ 00bfb674 ["CALL", null, ["callee:00c5a020:8"]]
- 00bfb24c bytes 757a0194
+ 00bfb674 bytes 6b7a0194
- 00bfb278 ["INT_ADD", "register:40f0:8", ["const:bfb278:8", "const:4:8"]]
- 00bfb278 ["CALL", null, ["callee:00c5a020:8"]]
+ 00bfb6a0 ["INT_ADD", "register:40f0:8", ["const:bfb6a0:8", "const:4:8"]]
+ 00bfb6a0 ["CALL", null, ["callee:00c5a020:8"]]
- 00bfb278 bytes 6a7a0194
+ 00bfb6a0 bytes 607a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-929ac05c30593247141d2844166da5fc"></a>

### [`00bfb4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb4c8.md) → [`00bfb8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb8f0.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb4c8.md#insn-00bfb504)
- 新版 [`00bfb92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb8f0.md#insn-00bfb92c)

~~~diff
- 00bfb504 ["INT_ADD", "register:40f0:8", ["const:bfb504:8", "const:4:8"]]
- 00bfb504 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfb92c ["INT_ADD", "register:40f0:8", ["const:bfb92c:8", "const:4:8"]]
+ 00bfb92c ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfb504 bytes b37b0194
+ 00bfb92c bytes a97b0194
~~~


<a id="compare-3a75c6c05d34f32573834f49771caa54"></a>

### [`00bfb564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md) → [`00bfb98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md) · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5d8) · [`00bfb5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5e4) · [`00bfb5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5f0)
- 新版 [`00bfba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba00) · [`00bfba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba0c) · [`00bfba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb98c.md#insn-00bfba18)

~~~diff
- 00bfb5d8 ["INT_ADD", "register:40f0:8", ["const:bfb5d8:8", "const:4:8"]]
- 00bfb5d8 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfba00 ["INT_ADD", "register:40f0:8", ["const:bfba00:8", "const:4:8"]]
+ 00bfba00 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfb5d8 bytes 7e7b0194
+ 00bfba00 bytes 747b0194
- 00bfb5e4 ["INT_ADD", "register:40f0:8", ["const:bfb5e4:8", "const:4:8"]]
- 00bfb5e4 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfba0c ["INT_ADD", "register:40f0:8", ["const:bfba0c:8", "const:4:8"]]
+ 00bfba0c ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfb5e4 bytes 3f8a0194
+ 00bfba0c bytes 358a0194
- 00bfb5f0 ["INT_ADD", "register:40f0:8", ["const:bfb5f0:8", "const:4:8"]]
- 00bfb5f0 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfba18 ["INT_ADD", "register:40f0:8", ["const:bfba18:8", "const:4:8"]]
+ 00bfba18 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfb5f0 bytes 3c8a0194
+ 00bfba18 bytes 328a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c62b2ab8d297bd0ab97f7243d6235d93"></a>

### [`00bfb680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb680.md) → [`00bfbaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbaa8.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ec0.md) · 呼出先 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md)
- 新版 呼出元 1件 [`00c582c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582c0.md) · 呼出先 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb680.md#insn-00bfb6a8)
- 新版 [`00bfbad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbaa8.md#insn-00bfbad0)

~~~diff
- 00bfb6a8 ["INT_ADD", "register:40f0:8", ["const:bfb6a8:8", "const:4:8"]]
- 00bfb6a8 ["CALL", null, ["callee:00c58500:8"]]
+ 00bfbad0 ["INT_ADD", "register:40f0:8", ["const:bfbad0:8", "const:4:8"]]
+ 00bfbad0 ["CALL", null, ["callee:00c58500:8"]]
- 00bfb6a8 bytes 96720194
+ 00bfbad0 bytes 8c720194
~~~


<a id="compare-3e768ae9c5bbccbaa17d1988cd22ca76"></a>

### [`00bfb6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6ac.md) → [`00bfbad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbad4.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df30.md) · 呼出先 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md)
- 新版 呼出元 1件 [`00c5e330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e330.md) · 呼出先 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6ac.md#insn-00bfb6d4)
- 新版 [`00bfbafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbad4.md#insn-00bfbafc)

~~~diff
- 00bfb6d4 ["INT_ADD", "register:40f0:8", ["const:bfb6d4:8", "const:4:8"]]
- 00bfb6d4 ["CALL", null, ["callee:00c58500:8"]]
+ 00bfbafc ["INT_ADD", "register:40f0:8", ["const:bfbafc:8", "const:4:8"]]
+ 00bfbafc ["CALL", null, ["callee:00c58500:8"]]
- 00bfb6d4 bytes 8b720194
+ 00bfbafc bytes 81720194
~~~


<a id="compare-4ada2d074ccfd113ff0cb55898681b85"></a>

### [`00bfb6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6f4.md) → [`00bfbb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb1c.md) FUN_00bfbb1c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6f4.md#insn-00bfb708)
- 新版 [`00bfbb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb1c.md#insn-00bfbb30)

~~~diff
- 00bfb708 ["INT_ADD", "register:40f0:8", ["const:bfb708:8", "const:4:8"]]
- 00bfb708 ["CALL", null, ["callee:00c5def0:8"]]
+ 00bfbb30 ["INT_ADD", "register:40f0:8", ["const:bfbb30:8", "const:4:8"]]
+ 00bfbb30 ["CALL", null, ["callee:00c5def0:8"]]
- 00bfb708 bytes fa880194
+ 00bfbb30 bytes f0880194
~~~


<a id="compare-03e7ad6a3e80955c532bf2ea74659fe2"></a>

### [`00bfb728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb728.md) → [`00bfbb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5df40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb728.md#insn-00bfb73c)
- 新版 [`00bfbb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md#insn-00bfbb64)

~~~diff
- 00bfb73c ["INT_ADD", "register:40f0:8", ["const:bfb73c:8", "const:4:8"]]
- 00bfb73c ["CALL", null, ["callee:00c5e340:8"]]
+ 00bfbb64 ["INT_ADD", "register:40f0:8", ["const:bfbb64:8", "const:4:8"]]
+ 00bfbb64 ["CALL", null, ["callee:00c5e340:8"]]
- 00bfb73c bytes 018a0194
+ 00bfbb64 bytes f7890194
~~~


<a id="compare-213349b644ce41e0accc3efc6e37f73a"></a>

### [`00bfb754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md) → [`00bfbb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md#insn-00bfb77c) · [`00bfb788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md#insn-00bfb788) · [`00bfb7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md#insn-00bfb7a4)
- 新版 [`00bfbba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbba4) · [`00bfbbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbbb0) · [`00bfbbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb7c.md#insn-00bfbbcc)

~~~diff
- 00bfb77c ["INT_ADD", "register:40f0:8", ["const:bfb77c:8", "const:4:8"]]
- 00bfb77c ["CALL", null, ["callee:00c5e2d0:8"]]
+ 00bfbba4 ["INT_ADD", "register:40f0:8", ["const:bfbba4:8", "const:4:8"]]
+ 00bfbba4 ["CALL", null, ["callee:00c5e2d0:8"]]
- 00bfb77c bytes d5890194
+ 00bfbba4 bytes cb890194
- 00bfb788 ["INT_ADD", "register:40f0:8", ["const:bfb788:8", "const:4:8"]]
- 00bfb788 ["CALL", null, ["callee:00c5e310:8"]]
+ 00bfbbb0 ["INT_ADD", "register:40f0:8", ["const:bfbbb0:8", "const:4:8"]]
+ 00bfbbb0 ["CALL", null, ["callee:00c5e310:8"]]
- 00bfb788 bytes e2890194
+ 00bfbbb0 bytes d8890194
- 00bfb7a4 ["INT_ADD", "register:40f0:8", ["const:bfb7a4:8", "const:4:8"]]
- 00bfb7a4 ["CALL", null, ["callee:00c5e2d0:8"]]
+ 00bfbbcc ["INT_ADD", "register:40f0:8", ["const:bfbbcc:8", "const:4:8"]]
+ 00bfbbcc ["CALL", null, ["callee:00c5e2d0:8"]]
- 00bfb7a4 bytes cb890194
+ 00bfbbcc bytes c1890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b99a67ce994bee38a979ae04b3bd2f8f"></a>

### [`00bfb7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb7e8.md) → [`00bfbc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc10.md) FUN_00bfbc10

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5df50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb7e8.md#insn-00bfb7fc)
- 新版 [`00bfbc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc10.md#insn-00bfbc24)

~~~diff
- 00bfb7fc ["INT_ADD", "register:40f0:8", ["const:bfb7fc:8", "const:4:8"]]
- 00bfb7fc ["CALL", null, ["callee:00c5e350:8"]]
+ 00bfbc24 ["INT_ADD", "register:40f0:8", ["const:bfbc24:8", "const:4:8"]]
+ 00bfbc24 ["CALL", null, ["callee:00c5e350:8"]]
- 00bfb7fc bytes d5890194
+ 00bfbc24 bytes cb890194
~~~


<a id="compare-e84033d27d22bd43ff6db03769174b45"></a>

### [`00bfb814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb814.md) → [`00bfbc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb814.md#insn-00bfb83c) · [`00bfb848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb814.md#insn-00bfb848)
- 新版 [`00bfbc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md#insn-00bfbc64) · [`00bfbc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md#insn-00bfbc70)

~~~diff
- 00bfb83c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfb83c ["INT_ADD", "register:40f0:8", ["const:bfb83c:8", "const:4:8"]]
- 00bfb83c ["CALLIND", null, ["register:0:8"]]
+ 00bfbc64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfbc64 ["INT_ADD", "register:40f0:8", ["const:bfbc64:8", "const:4:8"]]
+ 00bfbc64 ["CALLIND", null, ["register:0:8"]]
- 00bfb83c bytes 20013fd6
+ 00bfbc64 bytes 20013fd6
- 00bfb848 ["INT_ADD", "register:40f0:8", ["const:bfb848:8", "const:4:8"]]
- 00bfb848 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfbc70 ["INT_ADD", "register:40f0:8", ["const:bfbc70:8", "const:4:8"]]
+ 00bfbc70 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfb848 bytes e27a0194
+ 00bfbc70 bytes d87a0194
~~~


<a id="compare-ee21bf2955504fd85de9da4306f1ea19"></a>

### [`00bfb8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb8dc.md) → [`00bfbd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb8dc.md#insn-00bfb91c)
- 新版 [`00bfbd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md#insn-00bfbd44)

~~~diff
- 00bfb91c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb91c ["INT_ADD", "register:40f0:8", ["const:bfb91c:8", "const:4:8"]]
- 00bfb91c ["CALLIND", null, ["register:0:8"]]
+ 00bfbd44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfbd44 ["INT_ADD", "register:40f0:8", ["const:bfbd44:8", "const:4:8"]]
+ 00bfbd44 ["CALLIND", null, ["register:0:8"]]
- 00bfb91c bytes 00013fd6
+ 00bfbd44 bytes 00013fd6
~~~


<a id="compare-327ea901bc55cb54bc739f5cff0b79ba"></a>

### [`00bfbb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb10.md) → [`00bfbf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf38.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb10.md#insn-00bfbb30)
- 新版 [`00bfbf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf38.md#insn-00bfbf58)

~~~diff
- 00bfbb30 ["INT_ADD", "register:40f0:8", ["const:bfbb30:8", "const:4:8"]]
- 00bfbb30 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfbf58 ["INT_ADD", "register:40f0:8", ["const:bfbf58:8", "const:4:8"]]
+ 00bfbf58 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfbb30 bytes ec880194
+ 00bfbf58 bytes e2880194
~~~


<a id="compare-adcd2439a644bd92992f8e7d144e7968"></a>

### [`00bfbb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md) → [`00bfbf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbb84) · [`00bfbb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbb90) · [`00bfbb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbb9c)
- 新版 [`00bfbfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfac) · [`00bfbfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfb8) · [`00bfbfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf88.md#insn-00bfbfc4)

~~~diff
- 00bfbb84 ["INT_ADD", "register:40f0:8", ["const:bfbb84:8", "const:4:8"]]
- 00bfbb84 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfbfac ["INT_ADD", "register:40f0:8", ["const:bfbfac:8", "const:4:8"]]
+ 00bfbfac ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfbb84 bytes 137a0194
+ 00bfbfac bytes 097a0194
- 00bfbb90 ["INT_ADD", "register:40f0:8", ["const:bfbb90:8", "const:4:8"]]
- 00bfbb90 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfbfb8 ["INT_ADD", "register:40f0:8", ["const:bfbfb8:8", "const:4:8"]]
+ 00bfbfb8 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfbb90 bytes d4880194
+ 00bfbfb8 bytes ca880194
- 00bfbb9c ["INT_ADD", "register:40f0:8", ["const:bfbb9c:8", "const:4:8"]]
- 00bfbb9c ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bfbfc4 ["INT_ADD", "register:40f0:8", ["const:bfbfc4:8", "const:4:8"]]
+ 00bfbfc4 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bfbb9c bytes d1880194
+ 00bfbfc4 bytes c7880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd9b2522a7f58473dbfb6f2c54078b23"></a>

### [`00bfbc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbc64.md) → [`00bfc08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc08c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbc64.md#insn-00bfbca0)
- 新版 [`00bfc0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc08c.md#insn-00bfc0c8)

~~~diff
- 00bfbca0 ["INT_ADD", "register:40f0:8", ["const:bfbca0:8", "const:4:8"]]
- 00bfbca0 ["CALL", null, ["callee:00c581e0:8"]]
+ 00bfc0c8 ["INT_ADD", "register:40f0:8", ["const:bfc0c8:8", "const:4:8"]]
+ 00bfc0c8 ["CALL", null, ["callee:00c581e0:8"]]
- 00bfbca0 bytes 50700194
+ 00bfc0c8 bytes 46700194
~~~


<a id="compare-54dfe03eb85a69a74b8acf6d8ca1b2d6"></a>

### [`00bfbd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbd34.md) → [`00bfc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc15c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbd34.md#insn-00bfbd6c)
- 新版 [`00bfc194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc15c.md#insn-00bfc194)

~~~diff
- 00bfbd6c ["INT_ADD", "register:40f0:8", ["const:bfbd6c:8", "const:4:8"]]
- 00bfbd6c ["CALL", null, ["callee:00c5e320:8"]]
+ 00bfc194 ["INT_ADD", "register:40f0:8", ["const:bfc194:8", "const:4:8"]]
+ 00bfc194 ["CALL", null, ["callee:00c5e320:8"]]
- 00bfbd6c bytes 6d880194
+ 00bfc194 bytes 63880194
~~~


<a id="compare-f000207bd4fe6dc6b489021484145e18"></a>

### [`00bfbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbf84.md) → [`00bfc3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3ac.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbf84.md#insn-00bfbfa4)
- 新版 [`00bfc3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3ac.md#insn-00bfc3cc)

~~~diff
- 00bfbfa4 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfbfa4 ["INT_ADD", "register:40f0:8", ["const:bfbfa4:8", "const:4:8"]]
- 00bfbfa4 ["CALLIND", null, ["register:0:8"]]
+ 00bfc3cc ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfc3cc ["INT_ADD", "register:40f0:8", ["const:bfc3cc:8", "const:4:8"]]
+ 00bfc3cc ["CALLIND", null, ["register:0:8"]]
- 00bfbfa4 bytes 20003fd6
+ 00bfc3cc bytes 20003fd6
~~~


<a id="compare-7803045d22c013490bf527a6747604f0"></a>

### [`00bfbfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbfbc.md) → [`00bfc3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3e4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbfbc.md#insn-00bfbfdc)
- 新版 [`00bfc404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc3e4.md#insn-00bfc404)

~~~diff
- 00bfbfdc ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfbfdc ["INT_ADD", "register:40f0:8", ["const:bfbfdc:8", "const:4:8"]]
- 00bfbfdc ["CALLIND", null, ["register:0:8"]]
+ 00bfc404 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfc404 ["INT_ADD", "register:40f0:8", ["const:bfc404:8", "const:4:8"]]
+ 00bfc404 ["CALLIND", null, ["register:0:8"]]
- 00bfbfdc bytes 20003fd6
+ 00bfc404 bytes 20003fd6
~~~


<a id="compare-9cec2485bf4918c70c2bdd45ade6f918"></a>

### [`00bfbff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md) → [`00bfc41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc024) · [`00bfc088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc088) · [`00bfc0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc0c0)
- 新版 [`00bfc44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc44c) · [`00bfc4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc4b0) · [`00bfc4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md#insn-00bfc4e8)

~~~diff
- 00bfc024 ["INT_ADD", "register:40f0:8", ["const:bfc024:8", "const:4:8"]]
- 00bfc024 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfc44c ["INT_ADD", "register:40f0:8", ["const:bfc44c:8", "const:4:8"]]
+ 00bfc44c ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc024 bytes 6b760194
+ 00bfc44c bytes 61760194
- 00bfc088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc088 ["INT_ADD", "register:40f0:8", ["const:bfc088:8", "const:4:8"]]
- 00bfc088 ["CALLIND", null, ["register:0:8"]]
+ 00bfc4b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc4b0 ["INT_ADD", "register:40f0:8", ["const:bfc4b0:8", "const:4:8"]]
+ 00bfc4b0 ["CALLIND", null, ["register:0:8"]]
- 00bfc088 bytes 00013fd6
+ 00bfc4b0 bytes 00013fd6
- 00bfc0c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc0c0 ["INT_ADD", "register:40f0:8", ["const:bfc0c0:8", "const:4:8"]]
- 00bfc0c0 ["CALLIND", null, ["register:0:8"]]
+ 00bfc4e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc4e8 ["INT_ADD", "register:40f0:8", ["const:bfc4e8:8", "const:4:8"]]
+ 00bfc4e8 ["CALLIND", null, ["register:0:8"]]
- 00bfc0c0 bytes 00013fd6
+ 00bfc4e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc61e3365c3a6960274dcb8423fba7b"></a>

### [`00bfd204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md) → [`00bfd62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df60.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c5e360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e360.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd22c) · [`00bfd274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd274) · [`00bfd2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd2a4)
- 新版 [`00bfd654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd654) · [`00bfd69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd69c) · [`00bfd6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd62c.md#insn-00bfd6cc)

~~~diff
- 00bfd22c ["INT_ADD", "register:40f0:8", ["const:bfd22c:8", "const:4:8"]]
- 00bfd22c ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd654 ["INT_ADD", "register:40f0:8", ["const:bfd654:8", "const:4:8"]]
+ 00bfd654 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfd22c bytes e9710194
+ 00bfd654 bytes df710194
- 00bfd274 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd274 ["INT_ADD", "register:40f0:8", ["const:bfd274:8", "const:4:8"]]
- 00bfd274 ["CALLIND", null, ["register:0:8"]]
+ 00bfd69c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd69c ["INT_ADD", "register:40f0:8", ["const:bfd69c:8", "const:4:8"]]
+ 00bfd69c ["CALLIND", null, ["register:0:8"]]
- 00bfd274 bytes 00013fd6
+ 00bfd69c bytes 00013fd6
- 00bfd2a4 ["INT_ADD", "register:40f0:8", ["const:bfd2a4:8", "const:4:8"]]
- 00bfd2a4 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfd6cc ["INT_ADD", "register:40f0:8", ["const:bfd6cc:8", "const:4:8"]]
+ 00bfd6cc ["CALL", null, ["callee:00c582a0:8"]]
- 00bfd2a4 bytes ff6a0194
+ 00bfd6cc bytes f56a0194
~~~


<a id="compare-9d455267793e00c6378324f9163a0de6"></a>

### [`00bfd31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd31c.md) → [`00bfd744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd744.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd31c.md#insn-00bfd334)
- 新版 [`00bfd75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd744.md#insn-00bfd75c)

~~~diff
- 00bfd334 ["INT_ADD", "register:40f0:8", ["const:bfd334:8", "const:4:8"]]
- 00bfd334 ["CALL", null, ["callee:00c5e360:8"]]
+ 00bfd75c ["INT_ADD", "register:40f0:8", ["const:bfd75c:8", "const:4:8"]]
+ 00bfd75c ["CALL", null, ["callee:00c5e360:8"]]
- 00bfd334 bytes 0b830194
+ 00bfd75c bytes 01830194
~~~


<a id="compare-42b6a1d443cc482fe59aff22afdc6a59"></a>

### [`00bfd3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md) → [`00bfd824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df70.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c5e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e370.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd438) · [`00bfd4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd4b4) · [`00bfd4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd4f4)
- 新版 [`00bfd860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd860) · [`00bfd8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd8dc) · [`00bfd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md#insn-00bfd91c)

~~~diff
- 00bfd438 ["INT_ADD", "register:40f0:8", ["const:bfd438:8", "const:4:8"]]
- 00bfd438 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd860 ["INT_ADD", "register:40f0:8", ["const:bfd860:8", "const:4:8"]]
+ 00bfd860 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfd438 bytes 66710194
+ 00bfd860 bytes 5c710194
- 00bfd4b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd4b4 ["INT_ADD", "register:40f0:8", ["const:bfd4b4:8", "const:4:8"]]
- 00bfd4b4 ["CALLIND", null, ["register:0:8"]]
+ 00bfd8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd8dc ["INT_ADD", "register:40f0:8", ["const:bfd8dc:8", "const:4:8"]]
+ 00bfd8dc ["CALLIND", null, ["register:0:8"]]
- 00bfd4b4 bytes 00013fd6
+ 00bfd8dc bytes 00013fd6
- 00bfd4f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd4f4 ["INT_ADD", "register:40f0:8", ["const:bfd4f4:8", "const:4:8"]]
- 00bfd4f4 ["CALLIND", null, ["register:0:8"]]
+ 00bfd91c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd91c ["INT_ADD", "register:40f0:8", ["const:bfd91c:8", "const:4:8"]]
+ 00bfd91c ["CALLIND", null, ["register:0:8"]]
- 00bfd4f4 bytes 00013fd6
+ 00bfd91c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae917165a8156680828cabd24f722e2"></a>

### [`00bfd664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md) → [`00bfda8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df80.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c5e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e380.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd698) · [`00bfd6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd6fc) · [`00bfd740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd740)
- 新版 [`00bfdac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdac0) · [`00bfdb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdb24) · [`00bfdb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfda8c.md#insn-00bfdb68)

~~~diff
- 00bfd698 ["INT_ADD", "register:40f0:8", ["const:bfd698:8", "const:4:8"]]
- 00bfd698 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfdac0 ["INT_ADD", "register:40f0:8", ["const:bfdac0:8", "const:4:8"]]
+ 00bfdac0 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfd698 bytes ce700194
+ 00bfdac0 bytes c4700194
- 00bfd6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd6fc ["INT_ADD", "register:40f0:8", ["const:bfd6fc:8", "const:4:8"]]
- 00bfd6fc ["CALLIND", null, ["register:0:8"]]
+ 00bfdb24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdb24 ["INT_ADD", "register:40f0:8", ["const:bfdb24:8", "const:4:8"]]
+ 00bfdb24 ["CALLIND", null, ["register:0:8"]]
- 00bfd6fc bytes 00013fd6
+ 00bfdb24 bytes 00013fd6
- 00bfd740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd740 ["INT_ADD", "register:40f0:8", ["const:bfd740:8", "const:4:8"]]
- 00bfd740 ["CALLIND", null, ["register:0:8"]]
+ 00bfdb68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdb68 ["INT_ADD", "register:40f0:8", ["const:bfdb68:8", "const:4:8"]]
+ 00bfdb68 ["CALLIND", null, ["register:0:8"]]
- 00bfd740 bytes 00013fd6
+ 00bfdb68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cddab659c7c13d86dbee737f7e5b936"></a>

### [`00bfd878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md) → [`00bfdca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df90.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c5e390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e390.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd8b8) · [`00bfd8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd8fc) · [`00bfd954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd954)
- 新版 [`00bfdce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdce0) · [`00bfdd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdd24) · [`00bfdd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md#insn-00bfdd7c)

~~~diff
- 00bfd8b8 ["INT_ADD", "register:40f0:8", ["const:bfd8b8:8", "const:4:8"]]
- 00bfd8b8 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfdce0 ["INT_ADD", "register:40f0:8", ["const:bfdce0:8", "const:4:8"]]
+ 00bfdce0 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfd8b8 bytes 46700194
+ 00bfdce0 bytes 3c700194
- 00bfd8fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd8fc ["INT_ADD", "register:40f0:8", ["const:bfd8fc:8", "const:4:8"]]
- 00bfd8fc ["CALLIND", null, ["register:0:8"]]
+ 00bfdd24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdd24 ["INT_ADD", "register:40f0:8", ["const:bfdd24:8", "const:4:8"]]
+ 00bfdd24 ["CALLIND", null, ["register:0:8"]]
- 00bfd8fc bytes 00013fd6
+ 00bfdd24 bytes 00013fd6
- 00bfd954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd954 ["INT_ADD", "register:40f0:8", ["const:bfd954:8", "const:4:8"]]
- 00bfd954 ["CALLIND", null, ["register:0:8"]]
+ 00bfdd7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdd7c ["INT_ADD", "register:40f0:8", ["const:bfdd7c:8", "const:4:8"]]
+ 00bfdd7c ["CALLIND", null, ["register:0:8"]]
- 00bfd954 bytes 00013fd6
+ 00bfdd7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f6fe04cd72333891f7f148aec12d98"></a>

### [`00bfdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md) → [`00bfdee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdaf0) · [`00bfdb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdb48) · [`00bfdbc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdbc4)
- 新版 [`00bfdf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdf18) · [`00bfdf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdf70) · [`00bfdfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md#insn-00bfdfec)

~~~diff
- 00bfdaf0 ["INT_ADD", "register:40f0:8", ["const:bfdaf0:8", "const:4:8"]]
- 00bfdaf0 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfdf18 ["INT_ADD", "register:40f0:8", ["const:bfdf18:8", "const:4:8"]]
+ 00bfdf18 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfdaf0 bytes b86f0194
+ 00bfdf18 bytes ae6f0194
- 00bfdb48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdb48 ["INT_ADD", "register:40f0:8", ["const:bfdb48:8", "const:4:8"]]
- 00bfdb48 ["CALLIND", null, ["register:0:8"]]
+ 00bfdf70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdf70 ["INT_ADD", "register:40f0:8", ["const:bfdf70:8", "const:4:8"]]
+ 00bfdf70 ["CALLIND", null, ["register:0:8"]]
- 00bfdb48 bytes 00013fd6
+ 00bfdf70 bytes 00013fd6
- 00bfdbc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdbc4 ["INT_ADD", "register:40f0:8", ["const:bfdbc4:8", "const:4:8"]]
- 00bfdbc4 ["CALLIND", null, ["register:0:8"]]
+ 00bfdfec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdfec ["INT_ADD", "register:40f0:8", ["const:bfdfec:8", "const:4:8"]]
+ 00bfdfec ["CALLIND", null, ["register:0:8"]]
- 00bfdbc4 bytes 00013fd6
+ 00bfdfec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfceba4b14f874de171e011af7ec7e36"></a>

### [`00bfdc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdc78.md) → [`00bfe0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdc78.md#insn-00bfdca0) · [`00bfdce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdc78.md#insn-00bfdce0) · [`00bfdd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdc78.md#insn-00bfdd08)
- 新版 [`00bfe0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe0c8) · [`00bfe108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe108) · [`00bfe130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe0a0.md#insn-00bfe130)

~~~diff
- 00bfdca0 ["INT_ADD", "register:40f0:8", ["const:bfdca0:8", "const:4:8"]]
- 00bfdca0 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe0c8 ["INT_ADD", "register:40f0:8", ["const:bfe0c8:8", "const:4:8"]]
+ 00bfe0c8 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfdca0 bytes 4c6f0194
+ 00bfe0c8 bytes 426f0194
- 00bfdce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdce0 ["INT_ADD", "register:40f0:8", ["const:bfdce0:8", "const:4:8"]]
- 00bfdce0 ["CALLIND", null, ["register:0:8"]]
+ 00bfe108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe108 ["INT_ADD", "register:40f0:8", ["const:bfe108:8", "const:4:8"]]
+ 00bfe108 ["CALLIND", null, ["register:0:8"]]
- 00bfdce0 bytes 00013fd6
+ 00bfe108 bytes 00013fd6
- 00bfdd08 ["INT_ADD", "register:40f0:8", ["const:bfdd08:8", "const:4:8"]]
- 00bfdd08 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe130 ["INT_ADD", "register:40f0:8", ["const:bfe130:8", "const:4:8"]]
+ 00bfe130 ["CALL", null, ["callee:00c582a0:8"]]
- 00bfdd08 bytes 66680194
+ 00bfe130 bytes 5c680194
~~~


<a id="compare-b424e2867f181ce154c0fc6d33780172"></a>

### [`00bfdd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md) → [`00bfe1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cd0.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590d0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md#insn-00bfdda8) · [`00bfddd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md#insn-00bfddd4) · [`00bfde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md#insn-00bfde04)
- 新版 [`00bfe1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe1d0) · [`00bfe1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe1fc) · [`00bfe22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe1a0.md#insn-00bfe22c)

~~~diff
- 00bfdda8 ["INT_ADD", "register:40f0:8", ["const:bfdda8:8", "const:4:8"]]
- 00bfdda8 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe1d0 ["INT_ADD", "register:40f0:8", ["const:bfe1d0:8", "const:4:8"]]
+ 00bfe1d0 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfdda8 bytes 0a6f0194
+ 00bfe1d0 bytes 006f0194
- 00bfddd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfddd4 ["INT_ADD", "register:40f0:8", ["const:bfddd4:8", "const:4:8"]]
- 00bfddd4 ["CALLIND", null, ["register:0:8"]]
+ 00bfe1fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe1fc ["INT_ADD", "register:40f0:8", ["const:bfe1fc:8", "const:4:8"]]
+ 00bfe1fc ["CALLIND", null, ["register:0:8"]]
- 00bfddd4 bytes 00013fd6
+ 00bfe1fc bytes 00013fd6
- 00bfde04 ["INT_ADD", "register:40f0:8", ["const:bfde04:8", "const:4:8"]]
- 00bfde04 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe22c ["INT_ADD", "register:40f0:8", ["const:bfe22c:8", "const:4:8"]]
+ 00bfe22c ["CALL", null, ["callee:00c582a0:8"]]
- 00bfde04 bytes 27680194
+ 00bfe22c bytes 1d680194
~~~


<a id="compare-2f876837a902afdc6f38b035f7fad821"></a>

### [`00bfde70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfde70.md) → [`00bfe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfde70.md#insn-00bfdea0) · [`00bfdee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfde70.md#insn-00bfdee0) · [`00bfdf2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfde70.md#insn-00bfdf2c)
- 新版 [`00bfe2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe2c8) · [`00bfe308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe308) · [`00bfe354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe298.md#insn-00bfe354)

~~~diff
- 00bfdea0 ["INT_ADD", "register:40f0:8", ["const:bfdea0:8", "const:4:8"]]
- 00bfdea0 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe2c8 ["INT_ADD", "register:40f0:8", ["const:bfe2c8:8", "const:4:8"]]
+ 00bfe2c8 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfdea0 bytes cc6e0194
+ 00bfe2c8 bytes c26e0194
- 00bfdee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdee0 ["INT_ADD", "register:40f0:8", ["const:bfdee0:8", "const:4:8"]]
- 00bfdee0 ["CALLIND", null, ["register:0:8"]]
+ 00bfe308 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe308 ["INT_ADD", "register:40f0:8", ["const:bfe308:8", "const:4:8"]]
+ 00bfe308 ["CALLIND", null, ["register:0:8"]]
- 00bfdee0 bytes 00013fd6
+ 00bfe308 bytes 00013fd6
- 00bfdf2c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfdf2c ["INT_ADD", "register:40f0:8", ["const:bfdf2c:8", "const:4:8"]]
- 00bfdf2c ["CALLIND", null, ["register:0:8"]]
+ 00bfe354 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfe354 ["INT_ADD", "register:40f0:8", ["const:bfe354:8", "const:4:8"]]
+ 00bfe354 ["CALLIND", null, ["register:0:8"]]
- 00bfdf2c bytes 20013fd6
+ 00bfe354 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74b43d3902adb1f3eb4c4b1605a9f0b"></a>

### [`00bfdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md) → [`00bfe3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md#insn-00bfe000) · [`00bfe010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md#insn-00bfe010) · [`00bfe064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md#insn-00bfe064)
- 新版 [`00bfe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe428) · [`00bfe438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe438) · [`00bfe48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md#insn-00bfe48c)

~~~diff
- 00bfe000 ["INT_ADD", "register:40f0:8", ["const:bfe000:8", "const:4:8"]]
- 00bfe000 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe428 ["INT_ADD", "register:40f0:8", ["const:bfe428:8", "const:4:8"]]
+ 00bfe428 ["CALL", null, ["callee:00c582a0:8"]]
- 00bfe000 bytes a8670194
+ 00bfe428 bytes 9e670194
- 00bfe010 ["INT_ADD", "register:40f0:8", ["const:bfe010:8", "const:4:8"]]
- 00bfe010 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe438 ["INT_ADD", "register:40f0:8", ["const:bfe438:8", "const:4:8"]]
+ 00bfe438 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfe010 bytes 706e0194
+ 00bfe438 bytes 666e0194
- 00bfe064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe064 ["INT_ADD", "register:40f0:8", ["const:bfe064:8", "const:4:8"]]
- 00bfe064 ["CALLIND", null, ["register:0:8"]]
+ 00bfe48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe48c ["INT_ADD", "register:40f0:8", ["const:bfe48c:8", "const:4:8"]]
+ 00bfe48c ["CALLIND", null, ["register:0:8"]]
- 00bfe064 bytes 00013fd6
+ 00bfe48c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a251a0fcb2254a57a32956c98b0a2ee"></a>

### [`00bfe0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md) → [`00bfe51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md#insn-00bfe130) · [`00bfe140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md#insn-00bfe140) · [`00bfe18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md#insn-00bfe18c)
- 新版 [`00bfe558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe558) · [`00bfe568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe568) · [`00bfe5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe51c.md#insn-00bfe5b4)

~~~diff
- 00bfe130 ["INT_ADD", "register:40f0:8", ["const:bfe130:8", "const:4:8"]]
- 00bfe130 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe558 ["INT_ADD", "register:40f0:8", ["const:bfe558:8", "const:4:8"]]
+ 00bfe558 ["CALL", null, ["callee:00c582a0:8"]]
- 00bfe130 bytes 5c670194
+ 00bfe558 bytes 52670194
- 00bfe140 ["INT_ADD", "register:40f0:8", ["const:bfe140:8", "const:4:8"]]
- 00bfe140 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe568 ["INT_ADD", "register:40f0:8", ["const:bfe568:8", "const:4:8"]]
+ 00bfe568 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfe140 bytes 246e0194
+ 00bfe568 bytes 1a6e0194
- 00bfe18c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe18c ["INT_ADD", "register:40f0:8", ["const:bfe18c:8", "const:4:8"]]
- 00bfe18c ["CALLIND", null, ["register:0:8"]]
+ 00bfe5b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe5b4 ["INT_ADD", "register:40f0:8", ["const:bfe5b4:8", "const:4:8"]]
+ 00bfe5b4 ["CALLIND", null, ["register:0:8"]]
- 00bfe18c bytes 00013fd6
+ 00bfe5b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbf3bb9e1058836166d375fc14970191"></a>

### [`00bfe21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe21c.md) → [`00bfe644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe21c.md#insn-00bfe240) · [`00bfe268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe21c.md#insn-00bfe268) · [`00bfe28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe21c.md#insn-00bfe28c)
- 新版 [`00bfe668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe668) · [`00bfe690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe690) · [`00bfe6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe644.md#insn-00bfe6b4)

~~~diff
- 00bfe240 ["INT_ADD", "register:40f0:8", ["const:bfe240:8", "const:4:8"]]
- 00bfe240 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe668 ["INT_ADD", "register:40f0:8", ["const:bfe668:8", "const:4:8"]]
+ 00bfe668 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfe240 bytes e46d0194
+ 00bfe668 bytes da6d0194
- 00bfe268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe268 ["INT_ADD", "register:40f0:8", ["const:bfe268:8", "const:4:8"]]
- 00bfe268 ["CALLIND", null, ["register:0:8"]]
+ 00bfe690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe690 ["INT_ADD", "register:40f0:8", ["const:bfe690:8", "const:4:8"]]
+ 00bfe690 ["CALLIND", null, ["register:0:8"]]
- 00bfe268 bytes 00013fd6
+ 00bfe690 bytes 00013fd6
- 00bfe28c ["INT_ADD", "register:40f0:8", ["const:bfe28c:8", "const:4:8"]]
- 00bfe28c ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe6b4 ["INT_ADD", "register:40f0:8", ["const:bfe6b4:8", "const:4:8"]]
+ 00bfe6b4 ["CALL", null, ["callee:00c582a0:8"]]
- 00bfe28c bytes 05670194
+ 00bfe6b4 bytes fb660194
~~~


<a id="compare-8bc0cdffa4c92332d666e0c0392fa276"></a>

### [`00bfe30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe30c.md) → [`00bfe734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59400.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00c59800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59800.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe30c.md#insn-00bfe348) · [`00bfe358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe30c.md#insn-00bfe358) · [`00bfe388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe30c.md#insn-00bfe388)
- 新版 [`00bfe770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe770) · [`00bfe780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe780) · [`00bfe7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe734.md#insn-00bfe7b0)

~~~diff
- 00bfe348 ["INT_ADD", "register:40f0:8", ["const:bfe348:8", "const:4:8"]]
- 00bfe348 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfe770 ["INT_ADD", "register:40f0:8", ["const:bfe770:8", "const:4:8"]]
+ 00bfe770 ["CALL", null, ["callee:00c582a0:8"]]
- 00bfe348 bytes d6660194
+ 00bfe770 bytes cc660194
- 00bfe358 ["INT_ADD", "register:40f0:8", ["const:bfe358:8", "const:4:8"]]
- 00bfe358 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfe780 ["INT_ADD", "register:40f0:8", ["const:bfe780:8", "const:4:8"]]
+ 00bfe780 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfe358 bytes 9e6d0194
+ 00bfe780 bytes 946d0194
- 00bfe388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe388 ["INT_ADD", "register:40f0:8", ["const:bfe388:8", "const:4:8"]]
- 00bfe388 ["CALLIND", null, ["register:0:8"]]
+ 00bfe7b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe7b0 ["INT_ADD", "register:40f0:8", ["const:bfe7b0:8", "const:4:8"]]
+ 00bfe7b0 ["CALLIND", null, ["register:0:8"]]
- 00bfe388 bytes 00013fd6
+ 00bfe7b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ee01241f558961352fc42175685937"></a>

### [`00bfe41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe41c.md) → [`00bfe844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe844.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe41c.md#insn-00bfe454)
- 新版 [`00bfe87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe844.md#insn-00bfe87c)

~~~diff
- 00bfe454 ["INT_ADD", "register:40f0:8", ["const:bfe454:8", "const:4:8"]]
- 00bfe454 ["CALL", null, ["callee:00c581e0:8"]]
+ 00bfe87c ["INT_ADD", "register:40f0:8", ["const:bfe87c:8", "const:4:8"]]
+ 00bfe87c ["CALL", null, ["callee:00c581e0:8"]]
- 00bfe454 bytes 63660194
+ 00bfe87c bytes 59660194
~~~


<a id="compare-095965a2bb6d1402a41507fd2cf31e22"></a>

### [`00bfe4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe4e8.md) → [`00bfe910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe4e8.md#insn-00bfe518)
- 新版 [`00bfe940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md#insn-00bfe940)

~~~diff
- 00bfe518 ["INT_ADD", "register:40f0:8", ["const:bfe518:8", "const:4:8"]]
- 00bfe518 ["CALL", null, ["callee:00c5e320:8"]]
+ 00bfe940 ["INT_ADD", "register:40f0:8", ["const:bfe940:8", "const:4:8"]]
+ 00bfe940 ["CALL", null, ["callee:00c5e320:8"]]
- 00bfe518 bytes 827e0194
+ 00bfe940 bytes 787e0194
~~~


<a id="compare-e4a101ced097a24b059ec3f900057761"></a>

### [`00bfe54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe54c.md) → [`00bfe974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe974.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) · 呼出先 1件 [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md)
- 新版 呼出元 1件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) · 呼出先 1件 [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe54c.md#insn-00bfe590)
- 新版 [`00bfe9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe974.md#insn-00bfe9b8)

~~~diff
- 00bfe590 ["INT_ADD", "register:40f0:8", ["const:bfe590:8", "const:4:8"]]
- 00bfe590 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfe9b8 ["INT_ADD", "register:40f0:8", ["const:bfe9b8:8", "const:4:8"]]
+ 00bfe9b8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bfe590 bytes 58690194
+ 00bfe9b8 bytes 4e690194
~~~


<a id="compare-a013094618407d37ae17868162a3b466"></a>

### [`00bfe5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe5b0.md) → [`00bfe9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)
- 新版 呼出元 1件 [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe5b0.md#insn-00bfe5ec) · [`00bfe610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe5b0.md#insn-00bfe610) · [`00bfe634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe5b0.md#insn-00bfe634)
- 新版 [`00bfea14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea14) · [`00bfea38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea38) · [`00bfea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe9d8.md#insn-00bfea5c)

~~~diff
- 00bfe5ec ["INT_ADD", "register:40f0:8", ["const:bfe5ec:8", "const:4:8"]]
- 00bfe5ec ["CALL", null, ["callee:00c5d0f0:8"]]
+ 00bfea14 ["INT_ADD", "register:40f0:8", ["const:bfea14:8", "const:4:8"]]
+ 00bfea14 ["CALL", null, ["callee:00c5d0f0:8"]]
- 00bfe5ec bytes c1790194
+ 00bfea14 bytes b7790194
- 00bfe610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe610 ["INT_ADD", "register:40f0:8", ["const:bfe610:8", "const:4:8"]]
- 00bfe610 ["CALLIND", null, ["register:0:8"]]
+ 00bfea38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfea38 ["INT_ADD", "register:40f0:8", ["const:bfea38:8", "const:4:8"]]
+ 00bfea38 ["CALLIND", null, ["register:0:8"]]
- 00bfe610 bytes 00013fd6
+ 00bfea38 bytes 00013fd6
- 00bfe634 ["INT_ADD", "register:40f0:8", ["const:bfe634:8", "const:4:8"]]
- 00bfe634 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bfea5c ["INT_ADD", "register:40f0:8", ["const:bfea5c:8", "const:4:8"]]
+ 00bfea5c ["CALL", null, ["callee:00c582a0:8"]]
- 00bfe634 bytes 1b660194
+ 00bfea5c bytes 11660194
~~~


<a id="compare-31e457beb024957ddbc625c8c8e3a3ad"></a>

### [`00bfe664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe664.md) → [`00bfea8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfea8c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe664.md#insn-00bfe684)
- 新版 [`00bfeaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfea8c.md#insn-00bfeaac)

~~~diff
- 00bfe684 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfe684 ["INT_ADD", "register:40f0:8", ["const:bfe684:8", "const:4:8"]]
- 00bfe684 ["CALLIND", null, ["register:0:8"]]
+ 00bfeaac ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfeaac ["INT_ADD", "register:40f0:8", ["const:bfeaac:8", "const:4:8"]]
+ 00bfeaac ["CALLIND", null, ["register:0:8"]]
- 00bfe684 bytes 20003fd6
+ 00bfeaac bytes 20003fd6
~~~


<a id="compare-76ed5a9409ccee5314f3617de810aa27"></a>

### [`00bfe69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe69c.md) → [`00bfeac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfeac4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe69c.md#insn-00bfe6bc)
- 新版 [`00bfeae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfeac4.md#insn-00bfeae4)

~~~diff
- 00bfe6bc ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfe6bc ["INT_ADD", "register:40f0:8", ["const:bfe6bc:8", "const:4:8"]]
- 00bfe6bc ["CALLIND", null, ["register:0:8"]]
+ 00bfeae4 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfeae4 ["INT_ADD", "register:40f0:8", ["const:bfeae4:8", "const:4:8"]]
+ 00bfeae4 ["CALLIND", null, ["register:0:8"]]
- 00bfe6bc bytes 20003fd6
+ 00bfeae4 bytes 20003fd6
~~~


<a id="compare-30818291e3a3edd5abe1739573a0cf0e"></a>

### [`00bff03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff03c.md) → [`00bff464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff03c.md#insn-00bff060) · [`00bff0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff03c.md#insn-00bff0a8) · [`00bff0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff03c.md#insn-00bff0c8)
- 新版 [`00bff488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff488) · [`00bff4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff4d0) · [`00bff4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff464.md#insn-00bff4f0)

~~~diff
- 00bff060 ["INT_ADD", "register:40f0:8", ["const:bff060:8", "const:4:8"]]
- 00bff060 ["CALL", null, ["callee:00c58260:8"]]
+ 00bff488 ["INT_ADD", "register:40f0:8", ["const:bff488:8", "const:4:8"]]
+ 00bff488 ["CALL", null, ["callee:00c58260:8"]]
- 00bff060 bytes 80630194
+ 00bff488 bytes 76630194
- 00bff0a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff0a8 ["INT_ADD", "register:40f0:8", ["const:bff0a8:8", "const:4:8"]]
- 00bff0a8 ["CALLIND", null, ["register:0:8"]]
+ 00bff4d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff4d0 ["INT_ADD", "register:40f0:8", ["const:bff4d0:8", "const:4:8"]]
+ 00bff4d0 ["CALLIND", null, ["register:0:8"]]
- 00bff0a8 bytes 00013fd6
+ 00bff4d0 bytes 00013fd6
- 00bff0c8 ["INT_ADD", "register:40f0:8", ["const:bff0c8:8", "const:4:8"]]
- 00bff0c8 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bff4f0 ["INT_ADD", "register:40f0:8", ["const:bff4f0:8", "const:4:8"]]
+ 00bff4f0 ["CALL", null, ["callee:00c582a0:8"]]
- 00bff0c8 bytes 76630194
+ 00bff4f0 bytes 6c630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f92d142e3cfcbb37d9a87939c75228"></a>

### [`00bff134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff134.md) → [`00bff55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff55c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff134.md#insn-00bff184)
- 新版 [`00bff5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff55c.md#insn-00bff5ac)

~~~diff
- 00bff184 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff184 ["INT_ADD", "register:40f0:8", ["const:bff184:8", "const:4:8"]]
- 00bff184 ["CALLIND", null, ["register:0:8"]]
+ 00bff5ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff5ac ["INT_ADD", "register:40f0:8", ["const:bff5ac:8", "const:4:8"]]
+ 00bff5ac ["CALLIND", null, ["register:0:8"]]
- 00bff184 bytes 00013fd6
+ 00bff5ac bytes 00013fd6
~~~


<a id="compare-e83ebe52356dcf31f33d6c625f32814b"></a>

### [`00bff194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md) → [`00bff5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff1c0) · [`00bff1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff1f8) · [`00bff218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff218)
- 新版 [`00bff5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff5e8) · [`00bff620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff620) · [`00bff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff5bc.md#insn-00bff640)

~~~diff
- 00bff1c0 ["INT_ADD", "register:40f0:8", ["const:bff1c0:8", "const:4:8"]]
- 00bff1c0 ["CALL", null, ["callee:00c58260:8"]]
+ 00bff5e8 ["INT_ADD", "register:40f0:8", ["const:bff5e8:8", "const:4:8"]]
+ 00bff5e8 ["CALL", null, ["callee:00c58260:8"]]
- 00bff1c0 bytes 28630194
+ 00bff5e8 bytes 1e630194
- 00bff1f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff1f8 ["INT_ADD", "register:40f0:8", ["const:bff1f8:8", "const:4:8"]]
- 00bff1f8 ["CALLIND", null, ["register:0:8"]]
+ 00bff620 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff620 ["INT_ADD", "register:40f0:8", ["const:bff620:8", "const:4:8"]]
+ 00bff620 ["CALLIND", null, ["register:0:8"]]
- 00bff1f8 bytes 00013fd6
+ 00bff620 bytes 00013fd6
- 00bff218 ["INT_ADD", "register:40f0:8", ["const:bff218:8", "const:4:8"]]
- 00bff218 ["CALL", null, ["callee:00c582a0:8"]]
+ 00bff640 ["INT_ADD", "register:40f0:8", ["const:bff640:8", "const:4:8"]]
+ 00bff640 ["CALL", null, ["callee:00c582a0:8"]]
- 00bff218 bytes 22630194
+ 00bff640 bytes 18630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b548d6684983e401d37a3567a2f5fae1"></a>

### [`00bff258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md) → [`00bff680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c582b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff284) · [`00bff2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff2bc) · [`00bff2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff2dc)
- 新版 [`00bff6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff6ac) · [`00bff6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff6e4) · [`00bff704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff680.md#insn-00bff704)

~~~diff
- 00bff284 ["INT_ADD", "register:40f0:8", ["const:bff284:8", "const:4:8"]]
- 00bff284 ["CALL", null, ["callee:00c58260:8"]]
+ 00bff6ac ["INT_ADD", "register:40f0:8", ["const:bff6ac:8", "const:4:8"]]
+ 00bff6ac ["CALL", null, ["callee:00c58260:8"]]
- 00bff284 bytes f7620194
+ 00bff6ac bytes ed620194
- 00bff2bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff2bc ["INT_ADD", "register:40f0:8", ["const:bff2bc:8", "const:4:8"]]
- 00bff2bc ["CALLIND", null, ["register:0:8"]]
+ 00bff6e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff6e4 ["INT_ADD", "register:40f0:8", ["const:bff6e4:8", "const:4:8"]]
+ 00bff6e4 ["CALLIND", null, ["register:0:8"]]
- 00bff2bc bytes 00013fd6
+ 00bff6e4 bytes 00013fd6
- 00bff2dc ["INT_ADD", "register:40f0:8", ["const:bff2dc:8", "const:4:8"]]
- 00bff2dc ["CALL", null, ["callee:00c582a0:8"]]
+ 00bff704 ["INT_ADD", "register:40f0:8", ["const:bff704:8", "const:4:8"]]
+ 00bff704 ["CALL", null, ["callee:00c582a0:8"]]
- 00bff2dc bytes f1620194
+ 00bff704 bytes e7620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855990cb9f3b01b6b37b2cd0537ccc90"></a>

### [`00bff31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff31c.md) → [`00bff744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff744.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff31c.md#insn-00bff364)
- 新版 [`00bff78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff744.md#insn-00bff78c)

~~~diff
- 00bff364 ["INT_ADD", "register:40f0:8", ["const:bff364:8", "const:4:8"]]
- 00bff364 ["CALL", null, ["callee:00c581e0:8"]]
+ 00bff78c ["INT_ADD", "register:40f0:8", ["const:bff78c:8", "const:4:8"]]
+ 00bff78c ["CALL", null, ["callee:00c581e0:8"]]
- 00bff364 bytes 9f620194
+ 00bff78c bytes 95620194
~~~


<a id="compare-6ddcb7d515148bd1984a026089fc3e3d"></a>

### [`00bff47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff47c.md) → [`00bff8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8a4.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff47c.md#insn-00bff494)
- 新版 [`00bff8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8a4.md#insn-00bff8bc)

~~~diff
- 00bff494 ["INT_ADD", "register:40f0:8", ["const:bff494:8", "const:4:8"]]
- 00bff494 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00bff8bc ["INT_ADD", "register:40f0:8", ["const:bff8bc:8", "const:4:8"]]
+ 00bff8bc ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bff494 bytes 13760194
+ 00bff8bc bytes 09760194
~~~


<a id="compare-b44dd434d6ea72d7c94727cffd6493ae"></a>

### [`00bff4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4ac.md) → [`00bff8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8d4.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4ac.md#insn-00bff4c4)
- 新版 [`00bff8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff8d4.md#insn-00bff8ec)

~~~diff
- 00bff4c4 ["INT_ADD", "register:40f0:8", ["const:bff4c4:8", "const:4:8"]]
- 00bff4c4 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00bff8ec ["INT_ADD", "register:40f0:8", ["const:bff8ec:8", "const:4:8"]]
+ 00bff8ec ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bff4c4 bytes 07760194
+ 00bff8ec bytes fd750194
~~~


<a id="compare-7c48d16756530301a3ef0d8d4d64be6d"></a>

### [`00bff4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4dc.md) → [`00bff904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff904.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4dc.md#insn-00bff4fc)
- 新版 [`00bff924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff904.md#insn-00bff924)

~~~diff
- 00bff4fc ["INT_ADD", "register:40f0:8", ["const:bff4fc:8", "const:4:8"]]
- 00bff4fc ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00bff924 ["INT_ADD", "register:40f0:8", ["const:bff924:8", "const:4:8"]]
+ 00bff924 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bff4fc bytes f9750194
+ 00bff924 bytes ef750194
~~~


<a id="compare-ed5c2a48f05a9482a41b29e2099edc3e"></a>

### [`00bff514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff514.md) → [`00bff93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff93c.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff514.md#insn-00bff54c)
- 新版 [`00bff974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff93c.md#insn-00bff974)

~~~diff
- 00bff54c ["INT_ADD", "register:40f0:8", ["const:bff54c:8", "const:4:8"]]
- 00bff54c ["CALL", null, ["callee:00c5e320:8"]]
+ 00bff974 ["INT_ADD", "register:40f0:8", ["const:bff974:8", "const:4:8"]]
+ 00bff974 ["CALL", null, ["callee:00c5e320:8"]]
- 00bff54c bytes 757a0194
+ 00bff974 bytes 6b7a0194
~~~


<a id="compare-9e95d7ce17147589dc032750dcf2bd16"></a>

### [`00bff588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff588.md) → [`00bff9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9b0.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff588.md#insn-00bff59c)
- 新版 [`00bff9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9b0.md#insn-00bff9c4)

~~~diff
- 00bff59c ["INT_ADD", "register:40f0:8", ["const:bff59c:8", "const:4:8"]]
- 00bff59c ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bff9c4 ["INT_ADD", "register:40f0:8", ["const:bff9c4:8", "const:4:8"]]
+ 00bff9c4 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bff59c bytes 857a0194
+ 00bff9c4 bytes 7b7a0194
~~~


<a id="compare-dea141d6c7cf5e8bbcda67cff69d8cfb"></a>

### [`00bff5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md) → [`00bff9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md#insn-00bff5dc) · [`00bff5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md#insn-00bff5e8) · [`00bff604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md#insn-00bff604)
- 新版 [`00bffa04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa04) · [`00bffa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa10) · [`00bffa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa2c)

~~~diff
- 00bff5dc ["INT_ADD", "register:40f0:8", ["const:bff5dc:8", "const:4:8"]]
- 00bff5dc ["CALL", null, ["callee:00c5e2d0:8"]]
+ 00bffa04 ["INT_ADD", "register:40f0:8", ["const:bffa04:8", "const:4:8"]]
+ 00bffa04 ["CALL", null, ["callee:00c5e2d0:8"]]
- 00bff5dc bytes 3d7a0194
+ 00bffa04 bytes 337a0194
- 00bff5e8 ["INT_ADD", "register:40f0:8", ["const:bff5e8:8", "const:4:8"]]
- 00bff5e8 ["CALL", null, ["callee:00c5e310:8"]]
+ 00bffa10 ["INT_ADD", "register:40f0:8", ["const:bffa10:8", "const:4:8"]]
+ 00bffa10 ["CALL", null, ["callee:00c5e310:8"]]
- 00bff5e8 bytes 4a7a0194
+ 00bffa10 bytes 407a0194
- 00bff604 ["INT_ADD", "register:40f0:8", ["const:bff604:8", "const:4:8"]]
- 00bff604 ["CALL", null, ["callee:00c5e2d0:8"]]
+ 00bffa2c ["INT_ADD", "register:40f0:8", ["const:bffa2c:8", "const:4:8"]]
+ 00bffa2c ["CALL", null, ["callee:00c5e2d0:8"]]
- 00bff604 bytes 337a0194
+ 00bffa2c bytes 297a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd5373ec433e2cbc8e5905f083cdf30"></a>

### [`00bff648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff648.md) → [`00bffa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff648.md#insn-00bff65c)
- 新版 [`00bffa84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md#insn-00bffa84)

~~~diff
- 00bff65c ["INT_ADD", "register:40f0:8", ["const:bff65c:8", "const:4:8"]]
- 00bff65c ["CALL", null, ["callee:00c5e3d0:8"]]
+ 00bffa84 ["INT_ADD", "register:40f0:8", ["const:bffa84:8", "const:4:8"]]
+ 00bffa84 ["CALL", null, ["callee:00c5e3d0:8"]]
- 00bff65c bytes 5d7a0194
+ 00bffa84 bytes 537a0194
~~~


<a id="compare-e52bb78123c35d02284021faddd3eba8"></a>

### [`00bff674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md) → [`00bffa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md#insn-00bff69c) · [`00bff6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md#insn-00bff6a8)
- 新版 [`00bffac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md#insn-00bffac4) · [`00bffad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md#insn-00bffad0)

~~~diff
- 00bff69c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bff69c ["INT_ADD", "register:40f0:8", ["const:bff69c:8", "const:4:8"]]
- 00bff69c ["CALLIND", null, ["register:0:8"]]
+ 00bffac4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bffac4 ["INT_ADD", "register:40f0:8", ["const:bffac4:8", "const:4:8"]]
+ 00bffac4 ["CALLIND", null, ["register:0:8"]]
- 00bff69c bytes 20013fd6
+ 00bffac4 bytes 20013fd6
- 00bff6a8 ["INT_ADD", "register:40f0:8", ["const:bff6a8:8", "const:4:8"]]
- 00bff6a8 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bffad0 ["INT_ADD", "register:40f0:8", ["const:bffad0:8", "const:4:8"]]
+ 00bffad0 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bff6a8 bytes 4a6b0194
+ 00bffad0 bytes 406b0194
~~~


<a id="compare-4dc2d346d41cf692bc98443807c55979"></a>

### [`00bff740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff740.md) → [`00bffb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb68.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff740.md#insn-00bff78c)
- 新版 [`00bffbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb68.md#insn-00bffbb4)

~~~diff
- 00bff78c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff78c ["INT_ADD", "register:40f0:8", ["const:bff78c:8", "const:4:8"]]
- 00bff78c ["CALLIND", null, ["register:0:8"]]
+ 00bffbb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffbb4 ["INT_ADD", "register:40f0:8", ["const:bffbb4:8", "const:4:8"]]
+ 00bffbb4 ["CALLIND", null, ["register:0:8"]]
- 00bff78c bytes 00013fd6
+ 00bffbb4 bytes 00013fd6
~~~


<a id="compare-b5c23849e7f2c8b2d96230faf4fc4a77"></a>

### [`00bff97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff97c.md) → [`00bffda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffda4.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff97c.md#insn-00bff99c)
- 新版 [`00bffdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffda4.md#insn-00bffdc4)

~~~diff
- 00bff99c ["INT_ADD", "register:40f0:8", ["const:bff99c:8", "const:4:8"]]
- 00bff99c ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bffdc4 ["INT_ADD", "register:40f0:8", ["const:bffdc4:8", "const:4:8"]]
+ 00bffdc4 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bff99c bytes 51790194
+ 00bffdc4 bytes 47790194
~~~


<a id="compare-a222c3d59edb2456e72ade505c23cb4b"></a>

### [`00bff9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md) → [`00bffdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bff9f0) · [`00bff9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bff9fc) · [`00bffa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bffa08)
- 新版 [`00bffe18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe18) · [`00bffe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe24) · [`00bffe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe30)

~~~diff
- 00bff9f0 ["INT_ADD", "register:40f0:8", ["const:bff9f0:8", "const:4:8"]]
- 00bff9f0 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bffe18 ["INT_ADD", "register:40f0:8", ["const:bffe18:8", "const:4:8"]]
+ 00bffe18 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bff9f0 bytes 786a0194
+ 00bffe18 bytes 6e6a0194
- 00bff9fc ["INT_ADD", "register:40f0:8", ["const:bff9fc:8", "const:4:8"]]
- 00bff9fc ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bffe24 ["INT_ADD", "register:40f0:8", ["const:bffe24:8", "const:4:8"]]
+ 00bffe24 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bff9fc bytes 39790194
+ 00bffe24 bytes 2f790194
- 00bffa08 ["INT_ADD", "register:40f0:8", ["const:bffa08:8", "const:4:8"]]
- 00bffa08 ["CALL", null, ["callee:00c5e2e0:8"]]
+ 00bffe30 ["INT_ADD", "register:40f0:8", ["const:bffe30:8", "const:4:8"]]
+ 00bffe30 ["CALL", null, ["callee:00c5e2e0:8"]]
- 00bffa08 bytes 36790194
+ 00bffe30 bytes 2c790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da16c44c66da71b3282f169b92ed9fa"></a>

### [`00bffb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffb18.md) → [`00bfff40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffb18.md#insn-00bffb9c) · [`00bffbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffb18.md#insn-00bffbb4)
- 新版 [`00bfffc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md#insn-00bfffc4) · [`00bfffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md#insn-00bfffdc)

~~~diff
- 00bffb9c ["INT_ADD", "register:40f0:8", ["const:bffb9c:8", "const:4:8"]]
- 00bffb9c ["CALL", null, ["callee:00c57f40:8"]]
+ 00bfffc4 ["INT_ADD", "register:40f0:8", ["const:bfffc4:8", "const:4:8"]]
+ 00bfffc4 ["CALL", null, ["callee:00c57f40:8"]]
- 00bffb9c bytes e95f0194
+ 00bfffc4 bytes df5f0194
- 00bffbb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bffbb4 ["INT_ADD", "register:40f0:8", ["const:bffbb4:8", "const:4:8"]]
- 00bffbb4 ["CALLIND", null, ["register:0:8"]]
+ 00bfffdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfffdc ["INT_ADD", "register:40f0:8", ["const:bfffdc:8", "const:4:8"]]
+ 00bfffdc ["CALLIND", null, ["register:0:8"]]
- 00bffbb4 bytes 00013fd6
+ 00bfffdc bytes 00013fd6
~~~


<a id="compare-d1398be33b1d1d89689335cfa9ed85bf"></a>

### [`00bffbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffbf8.md) → [`00c00020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00020.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffbf8.md#insn-00bffc14)
- 新版 [`00c0003c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00020.md#insn-00c0003c)

~~~diff
- 00bffc14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bffc14 ["INT_ADD", "register:40f0:8", ["const:bffc14:8", "const:4:8"]]
- 00bffc14 ["CALLIND", null, ["register:0:8"]]
+ 00c0003c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0003c ["INT_ADD", "register:40f0:8", ["const:c0003c:8", "const:4:8"]]
+ 00c0003c ["CALLIND", null, ["register:0:8"]]
- 00bffc14 bytes 00013fd6
+ 00c0003c bytes 00013fd6
~~~


<a id="compare-fac70c3353a455888145b03439f5278f"></a>

### [`00bffc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffc48.md) → [`00c00070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffc48.md#insn-00bffcc4) · [`00bffce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffc48.md#insn-00bffce0)
- 新版 [`00c000ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md#insn-00c000ec) · [`00c00108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md#insn-00c00108)

~~~diff
- 00bffcc4 ["INT_ADD", "register:40f0:8", ["const:bffcc4:8", "const:4:8"]]
- 00bffcc4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c000ec ["INT_ADD", "register:40f0:8", ["const:c000ec:8", "const:4:8"]]
+ 00c000ec ["CALL", null, ["callee:00c57f40:8"]]
- 00bffcc4 bytes 9f5f0194
+ 00c000ec bytes 955f0194
- 00bffce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bffce0 ["INT_ADD", "register:40f0:8", ["const:bffce0:8", "const:4:8"]]
- 00bffce0 ["CALLIND", null, ["register:0:8"]]
+ 00c00108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00108 ["INT_ADD", "register:40f0:8", ["const:c00108:8", "const:4:8"]]
+ 00c00108 ["CALLIND", null, ["register:0:8"]]
- 00bffce0 bytes 00013fd6
+ 00c00108 bytes 00013fd6
~~~


<a id="compare-1c150a519c1242233bf75edc042d3881"></a>

### [`00bffd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd2c.md) → [`00c00154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00154.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd2c.md#insn-00bffd68)
- 新版 [`00c00190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00154.md#insn-00c00190)

~~~diff
- 00bffd68 ["INT_ADD", "register:40f0:8", ["const:bffd68:8", "const:4:8"]]
- 00bffd68 ["CALL", null, ["callee:00c581e0:8"]]
+ 00c00190 ["INT_ADD", "register:40f0:8", ["const:c00190:8", "const:4:8"]]
+ 00c00190 ["CALL", null, ["callee:00c581e0:8"]]
- 00bffd68 bytes 1e600194
+ 00c00190 bytes 14600194
~~~


<a id="compare-65b2142ef17cb755a6aa63e5c78206ff"></a>

### [`00bffe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe20.md) → [`00c00248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00248.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffe38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe20.md#insn-00bffe38)
- 新版 [`00c00260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00248.md#insn-00c00260)

~~~diff
- 00bffe38 ["INT_ADD", "register:40f0:8", ["const:bffe38:8", "const:4:8"]]
- 00bffe38 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00c00260 ["INT_ADD", "register:40f0:8", ["const:c00260:8", "const:4:8"]]
+ 00c00260 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bffe38 bytes aa730194
+ 00c00260 bytes a0730194
~~~


<a id="compare-98f4369a2ee420a08b62d695dbd33b08"></a>

### [`00bffe50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe50.md) → [`00c00278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00278.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffe70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe50.md#insn-00bffe70)
- 新版 [`00c00298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00278.md#insn-00c00298)

~~~diff
- 00bffe70 ["INT_ADD", "register:40f0:8", ["const:bffe70:8", "const:4:8"]]
- 00bffe70 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00c00298 ["INT_ADD", "register:40f0:8", ["const:c00298:8", "const:4:8"]]
+ 00c00298 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bffe70 bytes 9c730194
+ 00c00298 bytes 92730194
~~~


<a id="compare-131149052d37731d656b910c476445d7"></a>

### [`00bffe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe88.md) → [`00c002b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c002b0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe88.md#insn-00bffec0)
- 新版 [`00c002e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c002b0.md#insn-00c002e8)

~~~diff
- 00bffec0 ["INT_ADD", "register:40f0:8", ["const:bffec0:8", "const:4:8"]]
- 00bffec0 ["CALL", null, ["callee:00c5e320:8"]]
+ 00c002e8 ["INT_ADD", "register:40f0:8", ["const:c002e8:8", "const:4:8"]]
+ 00c002e8 ["CALL", null, ["callee:00c5e320:8"]]
- 00bffec0 bytes 18780194
+ 00c002e8 bytes 0e780194
~~~


<a id="compare-fdf25f70bc51e2ad84041c2271d87104"></a>

### [`00c000e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md) → [`00c0050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md) · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)
- 新版 呼出元 1件 [`00c5e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c00118) · [`00c0013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c0013c) · [`00c0015c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c0015c)
- 新版 [`00c00540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00540) · [`00c00564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00564) · [`00c00584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00584)

~~~diff
- 00c00118 ["INT_ADD", "register:40f0:8", ["const:c00118:8", "const:4:8"]]
- 00c00118 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c00540 ["INT_ADD", "register:40f0:8", ["const:c00540:8", "const:4:8"]]
+ 00c00540 ["CALL", null, ["callee:00c5e400:8"]]
- 00c00118 bytes ba770194
+ 00c00540 bytes b0770194
- 00c0013c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0013c ["INT_ADD", "register:40f0:8", ["const:c0013c:8", "const:4:8"]]
- 00c0013c ["CALLIND", null, ["register:0:8"]]
+ 00c00564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00564 ["INT_ADD", "register:40f0:8", ["const:c00564:8", "const:4:8"]]
+ 00c00564 ["CALLIND", null, ["register:0:8"]]
- 00c0013c bytes 00013fd6
+ 00c00564 bytes 00013fd6
- 00c0015c ["INT_ADD", "register:40f0:8", ["const:c0015c:8", "const:4:8"]]
- 00c0015c ["CALL", null, ["callee:00c582a0:8"]]
+ 00c00584 ["INT_ADD", "register:40f0:8", ["const:c00584:8", "const:4:8"]]
+ 00c00584 ["CALL", null, ["callee:00c582a0:8"]]
- 00c0015c bytes 515f0194
+ 00c00584 bytes 475f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfbce795a819fbd1cec6848aa51f02b"></a>

### [`00c001d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c001d4.md) → [`00c005fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c005fc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c001f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c001d4.md#insn-00c001f4)
- 新版 [`00c0061c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c005fc.md#insn-00c0061c)

~~~diff
- 00c001f4 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c001f4 ["INT_ADD", "register:40f0:8", ["const:c001f4:8", "const:4:8"]]
- 00c001f4 ["CALLIND", null, ["register:0:8"]]
+ 00c0061c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c0061c ["INT_ADD", "register:40f0:8", ["const:c0061c:8", "const:4:8"]]
+ 00c0061c ["CALLIND", null, ["register:0:8"]]
- 00c001f4 bytes 20003fd6
+ 00c0061c bytes 20003fd6
~~~


<a id="compare-373e657425901a482b56ff4d21331f60"></a>

### [`00c0020c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c0020c.md) → [`00c00634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00634.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0022c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c0020c.md#insn-00c0022c)
- 新版 [`00c00654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00634.md#insn-00c00654)

~~~diff
- 00c0022c ["COPY", "register:0:8", ["register:4008:8"]]
- 00c0022c ["INT_ADD", "register:40f0:8", ["const:c0022c:8", "const:4:8"]]
- 00c0022c ["CALLIND", null, ["register:0:8"]]
+ 00c00654 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c00654 ["INT_ADD", "register:40f0:8", ["const:c00654:8", "const:4:8"]]
+ 00c00654 ["CALLIND", null, ["register:0:8"]]
- 00c0022c bytes 20003fd6
+ 00c00654 bytes 20003fd6
~~~


<a id="compare-ffb88c6aaa273a00d571edcaeeeebac8"></a>

### [`00c00244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00244.md) → [`00c0066c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00244.md#insn-00c00274) · [`00c002d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00244.md#insn-00c002d8) · [`00c0030c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00244.md#insn-00c0030c)
- 新版 [`00c0069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c0069c) · [`00c00700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c00700) · [`00c00734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c00734)

~~~diff
- 00c00274 ["INT_ADD", "register:40f0:8", ["const:c00274:8", "const:4:8"]]
- 00c00274 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c0069c ["INT_ADD", "register:40f0:8", ["const:c0069c:8", "const:4:8"]]
+ 00c0069c ["CALL", null, ["callee:00c5e420:8"]]
- 00c00274 bytes 6b770194
+ 00c0069c bytes 61770194
- 00c002d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c002d8 ["INT_ADD", "register:40f0:8", ["const:c002d8:8", "const:4:8"]]
- 00c002d8 ["CALLIND", null, ["register:0:8"]]
+ 00c00700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00700 ["INT_ADD", "register:40f0:8", ["const:c00700:8", "const:4:8"]]
+ 00c00700 ["CALLIND", null, ["register:0:8"]]
- 00c002d8 bytes 00013fd6
+ 00c00700 bytes 00013fd6
- 00c0030c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0030c ["INT_ADD", "register:40f0:8", ["const:c0030c:8", "const:4:8"]]
- 00c0030c ["CALLIND", null, ["register:0:8"]]
+ 00c00734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00734 ["INT_ADD", "register:40f0:8", ["const:c00734:8", "const:4:8"]]
+ 00c00734 ["CALLIND", null, ["register:0:8"]]
- 00c0030c bytes 00013fd6
+ 00c00734 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e567af2a081e5ae17a6f63a751dc256"></a>

### [`00c01450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01450.md) → [`00c01878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e030.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c5e430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e430.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01450.md#insn-00c01478) · [`00c014d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01450.md#insn-00c014d0) · [`00c014f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01450.md#insn-00c014f8)
- 新版 [`00c018a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c018a0) · [`00c018f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c018f8) · [`00c01920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c01920)

~~~diff
- 00c01478 ["INT_ADD", "register:40f0:8", ["const:c01478:8", "const:4:8"]]
- 00c01478 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c018a0 ["INT_ADD", "register:40f0:8", ["const:c018a0:8", "const:4:8"]]
+ 00c018a0 ["CALL", null, ["callee:00c5e420:8"]]
- 00c01478 bytes ea720194
+ 00c018a0 bytes e0720194
- 00c014d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c014d0 ["INT_ADD", "register:40f0:8", ["const:c014d0:8", "const:4:8"]]
- 00c014d0 ["CALLIND", null, ["register:0:8"]]
+ 00c018f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c018f8 ["INT_ADD", "register:40f0:8", ["const:c018f8:8", "const:4:8"]]
+ 00c018f8 ["CALLIND", null, ["register:0:8"]]
- 00c014d0 bytes 00013fd6
+ 00c018f8 bytes 00013fd6
- 00c014f8 ["INT_ADD", "register:40f0:8", ["const:c014f8:8", "const:4:8"]]
- 00c014f8 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c01920 ["INT_ADD", "register:40f0:8", ["const:c01920:8", "const:4:8"]]
+ 00c01920 ["CALL", null, ["callee:00c582a0:8"]]
- 00c014f8 bytes 6a5a0194
+ 00c01920 bytes 605a0194
~~~


<a id="compare-0d25deca81e02f5efadead71fcfc5bea"></a>

### [`00c01568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01568.md) → [`00c01990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01990.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01568.md#insn-00c01580)
- 新版 [`00c019a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01990.md#insn-00c019a8)

~~~diff
- 00c01580 ["INT_ADD", "register:40f0:8", ["const:c01580:8", "const:4:8"]]
- 00c01580 ["CALL", null, ["callee:00c5e430:8"]]
+ 00c019a8 ["INT_ADD", "register:40f0:8", ["const:c019a8:8", "const:4:8"]]
+ 00c019a8 ["CALL", null, ["callee:00c5e430:8"]]
- 00c01580 bytes ac720194
+ 00c019a8 bytes a2720194
~~~


<a id="compare-a829267b0b760ad19de0b18bc8dc4b48"></a>

### [`00c01648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md) → [`00c01a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e040.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c5e440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e440.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md#insn-00c01684) · [`00c016fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md#insn-00c016fc) · [`00c01738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md#insn-00c01738)
- 新版 [`00c01aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01aac) · [`00c01b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01b24) · [`00c01b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01b60)

~~~diff
- 00c01684 ["INT_ADD", "register:40f0:8", ["const:c01684:8", "const:4:8"]]
- 00c01684 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01aac ["INT_ADD", "register:40f0:8", ["const:c01aac:8", "const:4:8"]]
+ 00c01aac ["CALL", null, ["callee:00c5e420:8"]]
- 00c01684 bytes 67720194
+ 00c01aac bytes 5d720194
- 00c016fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c016fc ["INT_ADD", "register:40f0:8", ["const:c016fc:8", "const:4:8"]]
- 00c016fc ["CALLIND", null, ["register:0:8"]]
+ 00c01b24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01b24 ["INT_ADD", "register:40f0:8", ["const:c01b24:8", "const:4:8"]]
+ 00c01b24 ["CALLIND", null, ["register:0:8"]]
- 00c016fc bytes 00013fd6
+ 00c01b24 bytes 00013fd6
- 00c01738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01738 ["INT_ADD", "register:40f0:8", ["const:c01738:8", "const:4:8"]]
- 00c01738 ["CALLIND", null, ["register:0:8"]]
+ 00c01b60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01b60 ["INT_ADD", "register:40f0:8", ["const:c01b60:8", "const:4:8"]]
+ 00c01b60 ["CALLIND", null, ["register:0:8"]]
- 00c01738 bytes 00013fd6
+ 00c01b60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74e5f8b8680afd5aa93d8f729a4a215e"></a>

### [`00c018ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c018ac.md) → [`00c01cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e050.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c5e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e450.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c018e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c018ac.md#insn-00c018e0) · [`00c01940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c018ac.md#insn-00c01940) · [`00c0197c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c018ac.md#insn-00c0197c)
- 新版 [`00c01d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01d08) · [`00c01d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01d68) · [`00c01da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01da4)

~~~diff
- 00c018e0 ["INT_ADD", "register:40f0:8", ["const:c018e0:8", "const:4:8"]]
- 00c018e0 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01d08 ["INT_ADD", "register:40f0:8", ["const:c01d08:8", "const:4:8"]]
+ 00c01d08 ["CALL", null, ["callee:00c5e420:8"]]
- 00c018e0 bytes d0710194
+ 00c01d08 bytes c6710194
- 00c01940 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01940 ["INT_ADD", "register:40f0:8", ["const:c01940:8", "const:4:8"]]
- 00c01940 ["CALLIND", null, ["register:0:8"]]
+ 00c01d68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01d68 ["INT_ADD", "register:40f0:8", ["const:c01d68:8", "const:4:8"]]
+ 00c01d68 ["CALLIND", null, ["register:0:8"]]
- 00c01940 bytes 00013fd6
+ 00c01d68 bytes 00013fd6
- 00c0197c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0197c ["INT_ADD", "register:40f0:8", ["const:c0197c:8", "const:4:8"]]
- 00c0197c ["CALLIND", null, ["register:0:8"]]
+ 00c01da4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01da4 ["INT_ADD", "register:40f0:8", ["const:c01da4:8", "const:4:8"]]
+ 00c01da4 ["CALLIND", null, ["register:0:8"]]
- 00c0197c bytes 00013fd6
+ 00c01da4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-645bcf4589b476c7e82b030affec8321"></a>

### [`00c01ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md) → [`00c01edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e060.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c5e460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e460.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md#insn-00c01af4) · [`00c01b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md#insn-00c01b4c) · [`00c01b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md#insn-00c01b94)
- 新版 [`00c01f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01f1c) · [`00c01f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01f74) · [`00c01fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01fbc)

~~~diff
- 00c01af4 ["INT_ADD", "register:40f0:8", ["const:c01af4:8", "const:4:8"]]
- 00c01af4 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01f1c ["INT_ADD", "register:40f0:8", ["const:c01f1c:8", "const:4:8"]]
+ 00c01f1c ["CALL", null, ["callee:00c5e420:8"]]
- 00c01af4 bytes 4b710194
+ 00c01f1c bytes 41710194
- 00c01b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01b4c ["INT_ADD", "register:40f0:8", ["const:c01b4c:8", "const:4:8"]]
- 00c01b4c ["CALLIND", null, ["register:0:8"]]
+ 00c01f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01f74 ["INT_ADD", "register:40f0:8", ["const:c01f74:8", "const:4:8"]]
+ 00c01f74 ["CALLIND", null, ["register:0:8"]]
- 00c01b4c bytes 00013fd6
+ 00c01f74 bytes 00013fd6
- 00c01b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01b94 ["INT_ADD", "register:40f0:8", ["const:c01b94:8", "const:4:8"]]
- 00c01b94 ["CALLIND", null, ["register:0:8"]]
+ 00c01fbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01fbc ["INT_ADD", "register:40f0:8", ["const:c01fbc:8", "const:4:8"]]
+ 00c01fbc ["CALLIND", null, ["register:0:8"]]
- 00c01b94 bytes 00013fd6
+ 00c01fbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308e107b0827f4564982d5b4a84d9656"></a>

### [`00c01cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01cf0.md) → [`00c02118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01cf0.md#insn-00c01d24) · [`00c01d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01cf0.md#insn-00c01d7c) · [`00c01de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01cf0.md#insn-00c01de4)
- 新版 [`00c0214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c0214c) · [`00c021a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c021a4) · [`00c0220c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c0220c)

~~~diff
- 00c01d24 ["INT_ADD", "register:40f0:8", ["const:c01d24:8", "const:4:8"]]
- 00c01d24 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c0214c ["INT_ADD", "register:40f0:8", ["const:c0214c:8", "const:4:8"]]
+ 00c0214c ["CALL", null, ["callee:00c5e420:8"]]
- 00c01d24 bytes bf700194
+ 00c0214c bytes b5700194
- 00c01d7c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c01d7c ["INT_ADD", "register:40f0:8", ["const:c01d7c:8", "const:4:8"]]
- 00c01d7c ["CALLIND", null, ["register:0:8"]]
+ 00c021a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c021a4 ["INT_ADD", "register:40f0:8", ["const:c021a4:8", "const:4:8"]]
+ 00c021a4 ["CALLIND", null, ["register:0:8"]]
- 00c01d7c bytes 20013fd6
+ 00c021a4 bytes 20013fd6
- 00c01de4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c01de4 ["INT_ADD", "register:40f0:8", ["const:c01de4:8", "const:4:8"]]
- 00c01de4 ["CALLIND", null, ["register:0:8"]]
+ 00c0220c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c0220c ["INT_ADD", "register:40f0:8", ["const:c0220c:8", "const:4:8"]]
+ 00c0220c ["CALLIND", null, ["register:0:8"]]
- 00c01de4 bytes 20013fd6
+ 00c0220c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401cc67d8eca3389cdb930a8637e8ae5"></a>

### [`00c01ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ea4.md) → [`00c022cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ea4.md#insn-00c01ecc) · [`00c01f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ea4.md#insn-00c01f0c) · [`00c01f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ea4.md#insn-00c01f34)
- 新版 [`00c022f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c022f4) · [`00c02334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c02334) · [`00c0235c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c0235c)

~~~diff
- 00c01ecc ["INT_ADD", "register:40f0:8", ["const:c01ecc:8", "const:4:8"]]
- 00c01ecc ["CALL", null, ["callee:00c5e420:8"]]
+ 00c022f4 ["INT_ADD", "register:40f0:8", ["const:c022f4:8", "const:4:8"]]
+ 00c022f4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c01ecc bytes 55700194
+ 00c022f4 bytes 4b700194
- 00c01f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01f0c ["INT_ADD", "register:40f0:8", ["const:c01f0c:8", "const:4:8"]]
- 00c01f0c ["CALLIND", null, ["register:0:8"]]
+ 00c02334 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02334 ["INT_ADD", "register:40f0:8", ["const:c02334:8", "const:4:8"]]
+ 00c02334 ["CALLIND", null, ["register:0:8"]]
- 00c01f0c bytes 00013fd6
+ 00c02334 bytes 00013fd6
- 00c01f34 ["INT_ADD", "register:40f0:8", ["const:c01f34:8", "const:4:8"]]
- 00c01f34 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c0235c ["INT_ADD", "register:40f0:8", ["const:c0235c:8", "const:4:8"]]
+ 00c0235c ["CALL", null, ["callee:00c582a0:8"]]
- 00c01f34 bytes db570194
+ 00c0235c bytes d1570194
~~~


<a id="compare-26c872041243d640a6446e041ad99ca0"></a>

### [`00c01fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01fa4.md) → [`00c023cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01fa4.md#insn-00c01fd4) · [`00c02000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01fa4.md#insn-00c02000) · [`00c02030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01fa4.md#insn-00c02030)
- 新版 [`00c023fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c023fc) · [`00c02428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c02428) · [`00c02458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c02458)

~~~diff
- 00c01fd4 ["INT_ADD", "register:40f0:8", ["const:c01fd4:8", "const:4:8"]]
- 00c01fd4 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c023fc ["INT_ADD", "register:40f0:8", ["const:c023fc:8", "const:4:8"]]
+ 00c023fc ["CALL", null, ["callee:00c5e420:8"]]
- 00c01fd4 bytes 13700194
+ 00c023fc bytes 09700194
- 00c02000 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02000 ["INT_ADD", "register:40f0:8", ["const:c02000:8", "const:4:8"]]
- 00c02000 ["CALLIND", null, ["register:0:8"]]
+ 00c02428 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02428 ["INT_ADD", "register:40f0:8", ["const:c02428:8", "const:4:8"]]
+ 00c02428 ["CALLIND", null, ["register:0:8"]]
- 00c02000 bytes 00013fd6
+ 00c02428 bytes 00013fd6
- 00c02030 ["INT_ADD", "register:40f0:8", ["const:c02030:8", "const:4:8"]]
- 00c02030 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02458 ["INT_ADD", "register:40f0:8", ["const:c02458:8", "const:4:8"]]
+ 00c02458 ["CALL", null, ["callee:00c582a0:8"]]
- 00c02030 bytes 9c570194
+ 00c02458 bytes 92570194
~~~


<a id="compare-68345fc48b511fb58e3ff1ddda442f15"></a>

### [`00c0209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c0209c.md) → [`00c024c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c020cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c0209c.md#insn-00c020cc) · [`00c02110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c0209c.md#insn-00c02110) · [`00c0215c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c0209c.md#insn-00c0215c)
- 新版 [`00c024f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c024f4) · [`00c02538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c02538) · [`00c02584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c02584)

~~~diff
- 00c020cc ["INT_ADD", "register:40f0:8", ["const:c020cc:8", "const:4:8"]]
- 00c020cc ["CALL", null, ["callee:00c5e420:8"]]
+ 00c024f4 ["INT_ADD", "register:40f0:8", ["const:c024f4:8", "const:4:8"]]
+ 00c024f4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c020cc bytes d56f0194
+ 00c024f4 bytes cb6f0194
- 00c02110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02110 ["INT_ADD", "register:40f0:8", ["const:c02110:8", "const:4:8"]]
- 00c02110 ["CALLIND", null, ["register:0:8"]]
+ 00c02538 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02538 ["INT_ADD", "register:40f0:8", ["const:c02538:8", "const:4:8"]]
+ 00c02538 ["CALLIND", null, ["register:0:8"]]
- 00c02110 bytes 00013fd6
+ 00c02538 bytes 00013fd6
- 00c0215c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c0215c ["INT_ADD", "register:40f0:8", ["const:c0215c:8", "const:4:8"]]
- 00c0215c ["CALLIND", null, ["register:0:8"]]
+ 00c02584 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c02584 ["INT_ADD", "register:40f0:8", ["const:c02584:8", "const:4:8"]]
+ 00c02584 ["CALLIND", null, ["register:0:8"]]
- 00c0215c bytes 20013fd6
+ 00c02584 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcac97ab6b9cdd3b8c4714c9d344e414"></a>

### [`00c021f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c021f0.md) → [`00c02618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c021f0.md#insn-00c02230) · [`00c02240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c021f0.md#insn-00c02240) · [`00c0229c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c021f0.md#insn-00c0229c)
- 新版 [`00c02658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c02658) · [`00c02668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c02668) · [`00c026c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c026c4)

~~~diff
- 00c02230 ["INT_ADD", "register:40f0:8", ["const:c02230:8", "const:4:8"]]
- 00c02230 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02658 ["INT_ADD", "register:40f0:8", ["const:c02658:8", "const:4:8"]]
+ 00c02658 ["CALL", null, ["callee:00c582a0:8"]]
- 00c02230 bytes 1c570194
+ 00c02658 bytes 12570194
- 00c02240 ["INT_ADD", "register:40f0:8", ["const:c02240:8", "const:4:8"]]
- 00c02240 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c02668 ["INT_ADD", "register:40f0:8", ["const:c02668:8", "const:4:8"]]
+ 00c02668 ["CALL", null, ["callee:00c5e420:8"]]
- 00c02240 bytes 786f0194
+ 00c02668 bytes 6e6f0194
- 00c0229c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0229c ["INT_ADD", "register:40f0:8", ["const:c0229c:8", "const:4:8"]]
- 00c0229c ["CALLIND", null, ["register:0:8"]]
+ 00c026c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c026c4 ["INT_ADD", "register:40f0:8", ["const:c026c4:8", "const:4:8"]]
+ 00c026c4 ["CALLIND", null, ["register:0:8"]]
- 00c0229c bytes 00013fd6
+ 00c026c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd4aeeffdf7b592d5102c61bb8a900d"></a>

### [`00c02330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02330.md) → [`00c02758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0236c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02330.md#insn-00c0236c) · [`00c0237c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02330.md#insn-00c0237c) · [`00c023d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02330.md#insn-00c023d0)
- 新版 [`00c02794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c02794) · [`00c027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c027a4) · [`00c027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c027f8)

~~~diff
- 00c0236c ["INT_ADD", "register:40f0:8", ["const:c0236c:8", "const:4:8"]]
- 00c0236c ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02794 ["INT_ADD", "register:40f0:8", ["const:c02794:8", "const:4:8"]]
+ 00c02794 ["CALL", null, ["callee:00c582a0:8"]]
- 00c0236c bytes cd560194
+ 00c02794 bytes c3560194
- 00c0237c ["INT_ADD", "register:40f0:8", ["const:c0237c:8", "const:4:8"]]
- 00c0237c ["CALL", null, ["callee:00c5e420:8"]]
+ 00c027a4 ["INT_ADD", "register:40f0:8", ["const:c027a4:8", "const:4:8"]]
+ 00c027a4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c0237c bytes 296f0194
+ 00c027a4 bytes 1f6f0194
- 00c023d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c023d0 ["INT_ADD", "register:40f0:8", ["const:c023d0:8", "const:4:8"]]
- 00c023d0 ["CALLIND", null, ["register:0:8"]]
+ 00c027f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c027f8 ["INT_ADD", "register:40f0:8", ["const:c027f8:8", "const:4:8"]]
+ 00c027f8 ["CALLIND", null, ["register:0:8"]]
- 00c023d0 bytes 00013fd6
+ 00c027f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62c4bf3a207acae0cd2a9ed7cd742c0f"></a>

### [`00c02464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02464.md) → [`00c0288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02464.md#insn-00c02488) · [`00c024b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02464.md#insn-00c024b0) · [`00c024d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02464.md#insn-00c024d4)
- 新版 [`00c028b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028b0) · [`00c028d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028d8) · [`00c028fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028fc)

~~~diff
- 00c02488 ["INT_ADD", "register:40f0:8", ["const:c02488:8", "const:4:8"]]
- 00c02488 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c028b0 ["INT_ADD", "register:40f0:8", ["const:c028b0:8", "const:4:8"]]
+ 00c028b0 ["CALL", null, ["callee:00c5e420:8"]]
- 00c02488 bytes e66e0194
+ 00c028b0 bytes dc6e0194
- 00c024b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c024b0 ["INT_ADD", "register:40f0:8", ["const:c024b0:8", "const:4:8"]]
- 00c024b0 ["CALLIND", null, ["register:0:8"]]
+ 00c028d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c028d8 ["INT_ADD", "register:40f0:8", ["const:c028d8:8", "const:4:8"]]
+ 00c028d8 ["CALLIND", null, ["register:0:8"]]
- 00c024b0 bytes 00013fd6
+ 00c028d8 bytes 00013fd6
- 00c024d4 ["INT_ADD", "register:40f0:8", ["const:c024d4:8", "const:4:8"]]
- 00c024d4 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c028fc ["INT_ADD", "register:40f0:8", ["const:c028fc:8", "const:4:8"]]
+ 00c028fc ["CALL", null, ["callee:00c582a0:8"]]
- 00c024d4 bytes 73560194
+ 00c028fc bytes 69560194
~~~


<a id="compare-cfb71bbf26f49b44b8607566f6c70c35"></a>

### [`00c02554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md) → [`00c0297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c02578) · [`00c025a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c025a8) · [`00c025cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c025cc)
- 新版 [`00c029a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029a0) · [`00c029d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029d0) · [`00c029f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029f4)

~~~diff
- 00c02578 ["INT_ADD", "register:40f0:8", ["const:c02578:8", "const:4:8"]]
- 00c02578 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c029a0 ["INT_ADD", "register:40f0:8", ["const:c029a0:8", "const:4:8"]]
+ 00c029a0 ["CALL", null, ["callee:00c5e420:8"]]
- 00c02578 bytes aa6e0194
+ 00c029a0 bytes a06e0194
- 00c025a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c025a8 ["INT_ADD", "register:40f0:8", ["const:c025a8:8", "const:4:8"]]
- 00c025a8 ["CALLIND", null, ["register:0:8"]]
+ 00c029d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c029d0 ["INT_ADD", "register:40f0:8", ["const:c029d0:8", "const:4:8"]]
+ 00c029d0 ["CALLIND", null, ["register:0:8"]]
- 00c025a8 bytes 00013fd6
+ 00c029d0 bytes 00013fd6
- 00c025cc ["INT_ADD", "register:40f0:8", ["const:c025cc:8", "const:4:8"]]
- 00c025cc ["CALL", null, ["callee:00c582a0:8"]]
+ 00c029f4 ["INT_ADD", "register:40f0:8", ["const:c029f4:8", "const:4:8"]]
+ 00c029f4 ["CALL", null, ["callee:00c582a0:8"]]
- 00c025cc bytes 35560194
+ 00c029f4 bytes 2b560194
~~~


<a id="compare-99c5a3f8d6b0ad163e0f331774acad3b"></a>

### [`00c02650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02650.md) → [`00c02a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0268c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02650.md#insn-00c0268c) · [`00c0269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02650.md#insn-00c0269c) · [`00c026cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02650.md#insn-00c026cc)
- 新版 [`00c02ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02ab4) · [`00c02ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02ac4) · [`00c02af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02af4)

~~~diff
- 00c0268c ["INT_ADD", "register:40f0:8", ["const:c0268c:8", "const:4:8"]]
- 00c0268c ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02ab4 ["INT_ADD", "register:40f0:8", ["const:c02ab4:8", "const:4:8"]]
+ 00c02ab4 ["CALL", null, ["callee:00c582a0:8"]]
- 00c0268c bytes 05560194
+ 00c02ab4 bytes fb550194
- 00c0269c ["INT_ADD", "register:40f0:8", ["const:c0269c:8", "const:4:8"]]
- 00c0269c ["CALL", null, ["callee:00c5e420:8"]]
+ 00c02ac4 ["INT_ADD", "register:40f0:8", ["const:c02ac4:8", "const:4:8"]]
+ 00c02ac4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c0269c bytes 616e0194
+ 00c02ac4 bytes 576e0194
- 00c026cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c026cc ["INT_ADD", "register:40f0:8", ["const:c026cc:8", "const:4:8"]]
- 00c026cc ["CALLIND", null, ["register:0:8"]]
+ 00c02af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02af4 ["INT_ADD", "register:40f0:8", ["const:c02af4:8", "const:4:8"]]
+ 00c02af4 ["CALLIND", null, ["register:0:8"]]
- 00c026cc bytes 00013fd6
+ 00c02af4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f3a103e0383762ce2760d8ec879129"></a>

### [`00c02760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md) → [`00c02b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0279c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c0279c) · [`00c027ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c027ac) · [`00c027dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c027dc)
- 新版 [`00c02bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02bc4) · [`00c02bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02bd4) · [`00c02c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02c04)

~~~diff
- 00c0279c ["INT_ADD", "register:40f0:8", ["const:c0279c:8", "const:4:8"]]
- 00c0279c ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02bc4 ["INT_ADD", "register:40f0:8", ["const:c02bc4:8", "const:4:8"]]
+ 00c02bc4 ["CALL", null, ["callee:00c582a0:8"]]
- 00c0279c bytes c1550194
+ 00c02bc4 bytes b7550194
- 00c027ac ["INT_ADD", "register:40f0:8", ["const:c027ac:8", "const:4:8"]]
- 00c027ac ["CALL", null, ["callee:00c5e420:8"]]
+ 00c02bd4 ["INT_ADD", "register:40f0:8", ["const:c02bd4:8", "const:4:8"]]
+ 00c02bd4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c027ac bytes 1d6e0194
+ 00c02bd4 bytes 136e0194
- 00c027dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c027dc ["INT_ADD", "register:40f0:8", ["const:c027dc:8", "const:4:8"]]
- 00c027dc ["CALLIND", null, ["register:0:8"]]
+ 00c02c04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02c04 ["INT_ADD", "register:40f0:8", ["const:c02c04:8", "const:4:8"]]
+ 00c02c04 ["CALLIND", null, ["register:0:8"]]
- 00c027dc bytes 00013fd6
+ 00c02c04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0619a503e42b5311cd4dcadc5ad683f"></a>

### [`00c02870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02870.md) → [`00c02c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02c98.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c028a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02870.md#insn-00c028a8)
- 新版 [`00c02cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02c98.md#insn-00c02cd0)

~~~diff
- 00c028a8 ["INT_ADD", "register:40f0:8", ["const:c028a8:8", "const:4:8"]]
- 00c028a8 ["CALL", null, ["callee:00c581e0:8"]]
+ 00c02cd0 ["INT_ADD", "register:40f0:8", ["const:c02cd0:8", "const:4:8"]]
+ 00c02cd0 ["CALL", null, ["callee:00c581e0:8"]]
- 00c028a8 bytes 4e550194
+ 00c02cd0 bytes 44550194
~~~


<a id="compare-f4d73088f0b73490f4c34c4c4d0ea33e"></a>

### [`00c02960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02960.md) → [`00c02d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02d88.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02960.md#insn-00c02978)
- 新版 [`00c02da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02d88.md#insn-00c02da0)

~~~diff
- 00c02978 ["INT_ADD", "register:40f0:8", ["const:c02978:8", "const:4:8"]]
- 00c02978 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00c02da0 ["INT_ADD", "register:40f0:8", ["const:c02da0:8", "const:4:8"]]
+ 00c02da0 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00c02978 bytes da680194
+ 00c02da0 bytes d0680194
~~~


<a id="compare-5ceb36276fd386685654ece92ecb4b78"></a>

### [`00c02990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02990.md) → [`00c02db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02db8.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c029b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02990.md#insn-00c029b0)
- 新版 [`00c02dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02db8.md#insn-00c02dd8)

~~~diff
- 00c029b0 ["INT_ADD", "register:40f0:8", ["const:c029b0:8", "const:4:8"]]
- 00c029b0 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00c02dd8 ["INT_ADD", "register:40f0:8", ["const:c02dd8:8", "const:4:8"]]
+ 00c02dd8 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00c029b0 bytes cc680194
+ 00c02dd8 bytes c2680194
~~~


<a id="compare-5527e1551a790a66d4d3d91f1144e8e1"></a>

### [`00c029c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c029c8.md) → [`00c02df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02df0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c029f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c029c8.md#insn-00c029f8)
- 新版 [`00c02e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02df0.md#insn-00c02e20)

~~~diff
- 00c029f8 ["INT_ADD", "register:40f0:8", ["const:c029f8:8", "const:4:8"]]
- 00c029f8 ["CALL", null, ["callee:00c5e320:8"]]
+ 00c02e20 ["INT_ADD", "register:40f0:8", ["const:c02e20:8", "const:4:8"]]
+ 00c02e20 ["CALL", null, ["callee:00c5e320:8"]]
- 00c029f8 bytes 4a6d0194
+ 00c02e20 bytes 406d0194
~~~


<a id="compare-9e2bad8085c8eeb92dd3b45a2306de72"></a>

### [`00c02a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a2c.md) → [`00c02e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02e54.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) · 呼出先 1件 [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a2c.md#insn-00c02a70)
- 新版 [`00c02e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02e54.md#insn-00c02e98)

~~~diff
- 00c02a70 ["INT_ADD", "register:40f0:8", ["const:c02a70:8", "const:4:8"]]
- 00c02a70 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c02e98 ["INT_ADD", "register:40f0:8", ["const:c02e98:8", "const:4:8"]]
+ 00c02e98 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c02a70 bytes 606d0194
+ 00c02e98 bytes 566d0194
~~~


<a id="compare-d494db6c10c7d2647116959246dc2bbd"></a>

### [`00c02a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a90.md) → [`00c02eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)
- 新版 呼出元 1件 [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a90.md#insn-00c02acc) · [`00c02af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a90.md#insn-00c02af0) · [`00c02b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a90.md#insn-00c02b14)
- 新版 [`00c02ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02ef4) · [`00c02f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02f18) · [`00c02f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02f3c)

~~~diff
- 00c02acc ["INT_ADD", "register:40f0:8", ["const:c02acc:8", "const:4:8"]]
- 00c02acc ["CALL", null, ["callee:00c5d0f0:8"]]
+ 00c02ef4 ["INT_ADD", "register:40f0:8", ["const:c02ef4:8", "const:4:8"]]
+ 00c02ef4 ["CALL", null, ["callee:00c5d0f0:8"]]
- 00c02acc bytes 89680194
+ 00c02ef4 bytes 7f680194
- 00c02af0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02af0 ["INT_ADD", "register:40f0:8", ["const:c02af0:8", "const:4:8"]]
- 00c02af0 ["CALLIND", null, ["register:0:8"]]
+ 00c02f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02f18 ["INT_ADD", "register:40f0:8", ["const:c02f18:8", "const:4:8"]]
+ 00c02f18 ["CALLIND", null, ["register:0:8"]]
- 00c02af0 bytes 00013fd6
+ 00c02f18 bytes 00013fd6
- 00c02b14 ["INT_ADD", "register:40f0:8", ["const:c02b14:8", "const:4:8"]]
- 00c02b14 ["CALL", null, ["callee:00c582a0:8"]]
+ 00c02f3c ["INT_ADD", "register:40f0:8", ["const:c02f3c:8", "const:4:8"]]
+ 00c02f3c ["CALL", null, ["callee:00c582a0:8"]]
- 00c02b14 bytes e3540194
+ 00c02f3c bytes d9540194
~~~


