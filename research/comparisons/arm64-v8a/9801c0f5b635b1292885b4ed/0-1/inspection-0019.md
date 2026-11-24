# v15.7.4 → v16.0.0 · 要調査の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-01ca017c6f5a9f67e3d028d5e25bb8fd"></a>

### [`00b0d5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d5b4.md) → [`00b6d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebb0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebb0.md)
- 新版 呼出元 1件 [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d5b4.md#insn-00b0d5d0) · [`00b0d5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d5b4.md#insn-00b0d5dc) · [`00b0d5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d5b4.md#insn-00b0d5ec)
- 新版 [`00b6d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d904) · [`00b6d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d910) · [`00b6d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d920)

~~~diff
- 00b0d5d0 ["INT_ADD", "register:40f0:8", ["const:b0d5d0:8", "const:4:8"]]
- 00b0d5d0 ["CALL", null, ["callee:00c5b660:8"]]
+ 00b6d904 ["INT_ADD", "register:40f0:8", ["const:b6d904:8", "const:4:8"]]
+ 00b6d904 ["CALL", null, ["callee:00c5b660:8"]]
- 00b0d5d0 bytes 78450394
+ 00b6d904 bytes 57b70394
- 00b0d5dc ["INT_ADD", "register:40f0:8", ["const:b0d5dc:8", "const:4:8"]]
- 00b0d5dc ["CALL", null, ["callee:00c5b660:8"]]
+ 00b6d910 ["INT_ADD", "register:40f0:8", ["const:b6d910:8", "const:4:8"]]
+ 00b6d910 ["CALL", null, ["callee:00c5b660:8"]]
- 00b0d5dc bytes 75450394
+ 00b6d910 bytes 54b70394
- 00b0d5ec ["INT_ADD", "register:40f0:8", ["const:b0d5ec:8", "const:4:8"]]
- 00b0d5ec ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b6d920 ["INT_ADD", "register:40f0:8", ["const:b6d920:8", "const:4:8"]]
+ 00b6d920 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b0d5ec bytes 9d360394
+ 00b6d920 bytes 64a80394
~~~


<a id="compare-f4aa249c6feead93e75fe9dbffb582cb"></a>

### [`00b0ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0ded8.md) → [`00b6e20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf090.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5bb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb40.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0ded8.md#insn-00b0df4c) · [`00b0df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0ded8.md#insn-00b0df70)
- 新版 [`00b6e280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md#insn-00b6e280) · [`00b6e2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md#insn-00b6e2a4)

~~~diff
- 00b0df4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0df4c ["INT_ADD", "register:40f0:8", ["const:b0df4c:8", "const:4:8"]]
- 00b0df4c ["CALLIND", null, ["register:0:8"]]
+ 00b6e280 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e280 ["INT_ADD", "register:40f0:8", ["const:b6e280:8", "const:4:8"]]
+ 00b6e280 ["CALLIND", null, ["register:0:8"]]
- 00b0df4c bytes 00013fd6
+ 00b6e280 bytes 00013fd6
- 00b0df70 ["INT_ADD", "register:40f0:8", ["const:b0df70:8", "const:4:8"]]
- 00b0df70 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00b6e2a4 ["INT_ADD", "register:40f0:8", ["const:b6e2a4:8", "const:4:8"]]
+ 00b6e2a4 ["CALL", null, ["callee:00c57ae0:8"]]
- 00b0df70 bytes 48340394
+ 00b6e2a4 bytes 0fa60394
~~~


<a id="compare-1045f67a75361a82771d5741b601422d"></a>

### [`00b20e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20e94.md) → [`00b843e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x6354c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf210.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc50.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20e94.md#insn-00b20f24) · [`00b20f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20e94.md#insn-00b20f30) · [`00b20f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20e94.md#insn-00b20f58)
- 新版 [`00b84470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md#insn-00b84470) · [`00b8447c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md#insn-00b8447c) · [`00b844a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md#insn-00b844a4)

~~~diff
- 00b20f24 ["INT_ADD", "register:40f0:8", ["const:b20f24:8", "const:4:8"]]
- 00b20f24 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b84470 ["INT_ADD", "register:40f0:8", ["const:b84470:8", "const:4:8"]]
+ 00b84470 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b20f24 bytes e7f40294
+ 00b84470 bytes 345a0394
- 00b20f30 ["INT_ADD", "register:40f0:8", ["const:b20f30:8", "const:4:8"]]
- 00b20f30 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b8447c ["INT_ADD", "register:40f0:8", ["const:b8447c:8", "const:4:8"]]
+ 00b8447c ["CALL", null, ["callee:00c57a90:8"]]
- 00b20f30 bytes 44e80294
+ 00b8447c bytes 854d0394
- 00b20f58 ["INT_ADD", "register:40f0:8", ["const:b20f58:8", "const:4:8"]]
- 00b20f58 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b844a4 ["INT_ADD", "register:40f0:8", ["const:b844a4:8", "const:4:8"]]
+ 00b844a4 ["CALL", null, ["callee:00c57c00:8"]]
- 00b20f58 bytes 96e80294
+ 00b844a4 bytes d74d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2541081fc53838a86d675a55a6d7a626"></a>

### [`00b22cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22cbc.md) → [`00b86a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x63d60` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf200.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc40.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22cbc.md#insn-00b22d4c) · [`00b22d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22cbc.md#insn-00b22d58) · [`00b22d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22cbc.md#insn-00b22d80)
- 新版 [`00b86aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86aac) · [`00b86ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86ab8) · [`00b86ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86a1c.md#insn-00b86ae0)

~~~diff
- 00b22d4c ["INT_ADD", "register:40f0:8", ["const:b22d4c:8", "const:4:8"]]
- 00b22d4c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b86aac ["INT_ADD", "register:40f0:8", ["const:b86aac:8", "const:4:8"]]
+ 00b86aac ["CALL", null, ["callee:00c5ad40:8"]]
- 00b22d4c bytes 5ded0294
+ 00b86aac bytes a5500394
- 00b22d58 ["INT_ADD", "register:40f0:8", ["const:b22d58:8", "const:4:8"]]
- 00b22d58 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b86ab8 ["INT_ADD", "register:40f0:8", ["const:b86ab8:8", "const:4:8"]]
+ 00b86ab8 ["CALL", null, ["callee:00c57a90:8"]]
- 00b22d58 bytes bae00294
+ 00b86ab8 bytes f6430394
- 00b22d80 ["INT_ADD", "register:40f0:8", ["const:b22d80:8", "const:4:8"]]
- 00b22d80 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b86ae0 ["INT_ADD", "register:40f0:8", ["const:b86ae0:8", "const:4:8"]]
+ 00b86ae0 ["CALL", null, ["callee:00c57c00:8"]]
- 00b22d80 bytes 0ce10294
+ 00b86ae0 bytes 48440394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bc292a7ef830351b9ac0e59ba025bf4"></a>

### [`00b25f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25f6c.md) → [`00b8abe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0x64c7c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb60.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bdfb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb00.md)
- 新版 呼出元 1件 [`00c5c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c510.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5c4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25f6c.md#insn-00b25fb8) · [`00b25fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25f6c.md#insn-00b25fe4) · [`00b26054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25f6c.md#insn-00b26054)
- 新版 [`00b8ac34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8ac34) · [`00b8ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8ac60) · [`00b8acd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8acd0)

~~~diff
- 00b25fb8 ["INT_ADD", "register:40f0:8", ["const:b25fb8:8", "const:4:8"]]
- 00b25fb8 ["CALL", null, ["callee:00c5c4b0:8"]]
+ 00b8ac34 ["INT_ADD", "register:40f0:8", ["const:b8ac34:8", "const:4:8"]]
+ 00b8ac34 ["CALL", null, ["callee:00c5c4b0:8"]]
- 00b25fb8 bytes d2e60294
+ 00b8ac34 bytes 1f460394
- 00b25fe4 ["INT_ADD", "register:40f0:8", ["const:b25fe4:8", "const:4:8"]]
- 00b25fe4 ["CALL", null, ["callee:00c5cc10:8"]]
+ 00b8ac60 ["INT_ADD", "register:40f0:8", ["const:b8ac60:8", "const:4:8"]]
+ 00b8ac60 ["CALL", null, ["callee:00c5cc10:8"]]
- 00b25fe4 bytes 23e80294
+ 00b8ac60 bytes ec470394
- 00b26054 ["INT_ADD", "register:40f0:8", ["const:b26054:8", "const:4:8"]]
- 00b26054 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b8acd0 ["INT_ADD", "register:40f0:8", ["const:b8acd0:8", "const:4:8"]]
+ 00b8acd0 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b26054 bytes 9be00294
+ 00b8acd0 bytes 1c400394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc836f94a69aafd3bedfb17de79cce5a"></a>

### [`00b314a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314a0.md) → [`00b9881c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9881c.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b314bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314a0.md#insn-00b314bc)
- 新版 [`00b98838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9881c.md#insn-00b98838)

~~~diff
- 00b314bc ["INT_ADD", "register:40f0:8", ["const:b314bc:8", "const:4:8"]]
- 00b314bc ["CALL", null, ["callee:00c5cce0:8"]]
+ 00b98838 ["INT_ADD", "register:40f0:8", ["const:b98838:8", "const:4:8"]]
+ 00b98838 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b314bc bytes 49bb0294
+ 00b98838 bytes 2a110394
~~~


<a id="compare-6655722eaa45a28e29f39f293449d3b9"></a>

### [`00b31920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31920.md) → [`00b98c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b319a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31920.md#insn-00b319a0) · [`00b319b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31920.md#insn-00b319b4)
- 新版 [`00b98d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md#insn-00b98d1c) · [`00b98d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md#insn-00b98d30)

~~~diff
- 00b319a0 ["INT_ADD", "register:40f0:8", ["const:b319a0:8", "const:4:8"]]
- 00b319a0 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b98d1c ["INT_ADD", "register:40f0:8", ["const:b98d1c:8", "const:4:8"]]
+ 00b98d1c ["CALL", null, ["callee:00c57c00:8"]]
- 00b319a0 bytes 04a60294
+ 00b98d1c bytes b9fb0294
- 00b319b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b319b4 ["INT_ADD", "register:40f0:8", ["const:b319b4:8", "const:4:8"]]
- 00b319b4 ["CALLIND", null, ["register:0:8"]]
+ 00b98d30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b98d30 ["INT_ADD", "register:40f0:8", ["const:b98d30:8", "const:4:8"]]
+ 00b98d30 ["CALLIND", null, ["register:0:8"]]
- 00b319b4 bytes 00013fd6
+ 00b98d30 bytes 00013fd6
~~~


<a id="compare-b329c1f6bf1bccad8853351588e65b6a"></a>

### [`00b31a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31a38.md) → [`00b98db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98db4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31a38.md#insn-00b31a50)
- 新版 [`00b98dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98db4.md#insn-00b98dcc)

~~~diff
- 00b31a50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31a50 ["INT_ADD", "register:40f0:8", ["const:b31a50:8", "const:4:8"]]
- 00b31a50 ["CALLIND", null, ["register:0:8"]]
+ 00b98dcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b98dcc ["INT_ADD", "register:40f0:8", ["const:b98dcc:8", "const:4:8"]]
+ 00b98dcc ["CALLIND", null, ["register:0:8"]]
- 00b31a50 bytes 00013fd6
+ 00b98dcc bytes 00013fd6
~~~


<a id="compare-dd8998ceabcc47dfd53cdba8cdfabd88"></a>

### [`00b31ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31ae8.md) → [`00b98e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31ae8.md#insn-00b31b5c) · [`00b31b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31ae8.md#insn-00b31b74)
- 新版 [`00b98ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md#insn-00b98ed8) · [`00b98ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md#insn-00b98ef0)

~~~diff
- 00b31b5c ["INT_ADD", "register:40f0:8", ["const:b31b5c:8", "const:4:8"]]
- 00b31b5c ["CALL", null, ["callee:00c57c00:8"]]
+ 00b98ed8 ["INT_ADD", "register:40f0:8", ["const:b98ed8:8", "const:4:8"]]
+ 00b98ed8 ["CALL", null, ["callee:00c57c00:8"]]
- 00b31b5c bytes 95a50294
+ 00b98ed8 bytes 4afb0294
- 00b31b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31b74 ["INT_ADD", "register:40f0:8", ["const:b31b74:8", "const:4:8"]]
- 00b31b74 ["CALLIND", null, ["register:0:8"]]
+ 00b98ef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b98ef0 ["INT_ADD", "register:40f0:8", ["const:b98ef0:8", "const:4:8"]]
+ 00b98ef0 ["CALLIND", null, ["register:0:8"]]
- 00b31b74 bytes 00013fd6
+ 00b98ef0 bytes 00013fd6
~~~


<a id="compare-388efb0d7c10c248fc1a1919c91c4b01"></a>

### [`00b43864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md) → [`00baf1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdfd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd90.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7f0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b43894) · [`00b438b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b438b0) · [`00b438ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b438ec)
- 新版 [`00baf1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf1d4) · [`00baf1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf1f0) · [`00baf22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf22c)

~~~diff
- 00b43894 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b43894 ["INT_ADD", "register:40f0:8", ["const:b43894:8", "const:4:8"]]
- 00b43894 ["CALLIND", null, ["register:0:8"]]
+ 00baf1d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf1d4 ["INT_ADD", "register:40f0:8", ["const:baf1d4:8", "const:4:8"]]
+ 00baf1d4 ["CALLIND", null, ["register:0:8"]]
- 00b43894 bytes 20013fd6
+ 00baf1d4 bytes 20013fd6
- 00b438b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b438b0 ["INT_ADD", "register:40f0:8", ["const:b438b0:8", "const:4:8"]]
- 00b438b0 ["CALLIND", null, ["register:0:8"]]
+ 00baf1f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf1f0 ["INT_ADD", "register:40f0:8", ["const:baf1f0:8", "const:4:8"]]
+ 00baf1f0 ["CALLIND", null, ["register:0:8"]]
- 00b438b0 bytes 20013fd6
+ 00baf1f0 bytes 20013fd6
- 00b438ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b438ec ["INT_ADD", "register:40f0:8", ["const:b438ec:8", "const:4:8"]]
- 00b438ec ["CALLIND", null, ["register:0:8"]]
+ 00baf22c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf22c ["INT_ADD", "register:40f0:8", ["const:baf22c:8", "const:4:8"]]
+ 00baf22c ["CALLIND", null, ["register:0:8"]]
- 00b438ec bytes 00013fd6
+ 00baf22c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36d03739f356e5f51a0ecc70e86c2590"></a>

### [`00b43c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md) → [`00baf5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff00.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5ca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca70.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md#insn-00b43d08) · [`00b43d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md#insn-00b43d50)
- 新版 [`00baf648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md#insn-00baf648) · [`00baf690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md#insn-00baf690)

~~~diff
- 00b43d08 ["INT_ADD", "register:40f0:8", ["const:b43d08:8", "const:4:8"]]
- 00b43d08 ["CALL", null, ["callee:00c57c50:8"]]
+ 00baf648 ["INT_ADD", "register:40f0:8", ["const:baf648:8", "const:4:8"]]
+ 00baf648 ["CALL", null, ["callee:00c57c50:8"]]
- 00b43d08 bytes 3e5d0294
+ 00baf648 bytes 82a10294
- 00b43d50 ["INT_ADD", "register:40f0:8", ["const:b43d50:8", "const:4:8"]]
- 00b43d50 ["CALL", null, ["callee:00c57c50:8"]]
+ 00baf690 ["INT_ADD", "register:40f0:8", ["const:baf690:8", "const:4:8"]]
+ 00baf690 ["CALL", null, ["callee:00c57c50:8"]]
- 00b43d50 bytes 2c5d0294
+ 00baf690 bytes 70a10294
~~~


<a id="compare-739c7879ab9ac038707574cb978761e5"></a>

### [`00b46478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md) → [`00b9c568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0x560f0` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `reordered`

- 旧版 呼出元 1件 [`00bdfce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfce0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6c0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md#insn-00b46510) · [`00b46558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md#insn-00b46558)
- 新版 [`00b9c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md#insn-00b9c600) · [`00b9c648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md#insn-00b9c648)

~~~diff
- 00b46510 ["INT_ADD", "register:40f0:8", ["const:b46510:8", "const:4:8"]]
- 00b46510 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b9c600 ["INT_ADD", "register:40f0:8", ["const:b9c600:8", "const:4:8"]]
+ 00b9c600 ["CALL", null, ["callee:00c57c50:8"]]
- 00b46510 bytes 3c530294
+ 00b9c600 bytes 94ed0294
- 00b46558 ["INT_ADD", "register:40f0:8", ["const:b46558:8", "const:4:8"]]
- 00b46558 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b9c648 ["INT_ADD", "register:40f0:8", ["const:b9c648:8", "const:4:8"]]
+ 00b9c648 ["CALL", null, ["callee:00c57c50:8"]]
- 00b46558 bytes 2a530294
+ 00b9c648 bytes 82ed0294
~~~


<a id="compare-15baa9a8ce7dbdb6b33351b55b0d9af2"></a>

### [`00b47860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47860.md) → [`00bb3994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md) _ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x6c134` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 local_def_use, operands_and_dependencies

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4789c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47860.md#insn-00b4789c)
- 新版 [`00bb39d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md#insn-00bb39d0)

~~~diff
- 00b4789c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b4789c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00b4789c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00b4789c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bb39d0 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bb39d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb39d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb39d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b4789c bytes 4901098b
+ 00bb39d0 bytes 29010a8b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a038ce5f8addd454f3b50c876e9b8da"></a>

### [`00b478bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md) → [`00bb39f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb39f0.md) _ZN11flatbuffers19SetGlobalTestLocaleEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x6c134` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b478e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b478e0) · [`00b478f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b478f8) · [`00b47934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b47934)
- 新版 [`00bb3a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb39f0.md#insn-00bb3a14) · [`00bb3a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb39f0.md#insn-00bb3a2c) · [`00bb3a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb39f0.md#insn-00bb3a68)

~~~diff
- 00b478e0 ["INT_ADD", "register:40f0:8", ["const:b478e0:8", "const:4:8"]]
- 00b478e0 ["CALL", null, ["callee:00c5ce40:8"]]
+ 00bb3a14 ["INT_ADD", "register:40f0:8", ["const:bb3a14:8", "const:4:8"]]
+ 00bb3a14 ["CALL", null, ["callee:00c5ce40:8"]]
- 00b478e0 bytes 84620294
+ 00bb3a14 bytes 0ba50294
- 00b478f8 ["INT_ADD", "register:40f0:8", ["const:b478f8:8", "const:4:8"]]
- 00b478f8 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bb3a2c ["INT_ADD", "register:40f0:8", ["const:bb3a2c:8", "const:4:8"]]
+ 00bb3a2c ["CALL", null, ["callee:00c57be0:8"]]
- 00b478f8 bytes 264e0294
+ 00bb3a2c bytes 6d900294
- 00b47934 ["INT_ADD", "register:40f0:8", ["const:b47934:8", "const:4:8"]]
- 00b47934 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bb3a68 ["INT_ADD", "register:40f0:8", ["const:bb3a68:8", "const:4:8"]]
+ 00bb3a68 ["CALL", null, ["callee:00c57a90:8"]]
- 00b47934 bytes c34d0294
+ 00bb3a68 bytes 0a900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ce3d022565edb4ff677d4b735af855"></a>

### [`00b47c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47c38.md) → [`00bb5484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5484.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x6d84c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47c38.md#insn-00b47c48)
- 新版 [`00bb5494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5484.md#insn-00bb5494)

~~~diff
- 00b47c48 ["INT_ADD", "register:40f0:8", ["const:b47c48:8", "const:4:8"]]
- 00b47c48 ["CALL", null, ["callee:00c5cdb0:8"]]
+ 00bb5494 ["INT_ADD", "register:40f0:8", ["const:bb5494:8", "const:4:8"]]
+ 00bb5494 ["CALL", null, ["callee:00c5cdb0:8"]]
- 00b47c48 bytes 96610294
+ 00bb5494 bytes 479e0294
~~~


<a id="compare-916572bef313b0486ecc3f3ab01dae45"></a>

### [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) → [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) FUN_00bb5ec4

採用 · 移動量 `+0x6d84c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md) [`00b48164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md) [`00b48440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 4件 [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md) [`00bb57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md) [`00bb59b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md) [`00bb5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md#insn-00b48680)
- 新版 [`00bb5ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md#insn-00bb5ecc)

~~~diff
- 00b48680 ["INT_ADD", "register:40f0:8", ["const:b48680:8", "const:4:8"]]
- 00b48680 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bb5ecc ["INT_ADD", "register:40f0:8", ["const:bb5ecc:8", "const:4:8"]]
+ 00bb5ecc ["CALL", null, ["callee:00c5ad40:8"]]
- 00b48680 bytes 10570294
+ 00bb5ecc bytes 9d930294
~~~


<a id="compare-eb186e0b6ca96c7ff68a94c8575dc4c3"></a>

### [`00b48708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48708.md) → [`00bb5ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ed8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x6d7d0` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48708.md#insn-00b4871c)
- 新版 [`00bb5eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ed8.md#insn-00bb5eec)

~~~diff
- 00b4871c ["INT_ADD", "register:40f0:8", ["const:b4871c:8", "const:4:8"]]
- 00b4871c ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bb5eec ["INT_ADD", "register:40f0:8", ["const:bb5eec:8", "const:4:8"]]
+ 00bb5eec ["CALL", null, ["callee:00c5cce0:8"]]
- 00b4871c bytes b15e0294
+ 00bb5eec bytes 7d9b0294
~~~


<a id="compare-f928a6dcfa2a0d6849d7900e7bb0223e"></a>

### [`00b48744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48744.md) → [`00bb5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f14.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x6d7d0` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48744.md#insn-00b48760)
- 新版 [`00bb5f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f14.md#insn-00bb5f30)

~~~diff
- 00b48760 ["INT_ADD", "register:40f0:8", ["const:b48760:8", "const:4:8"]]
- 00b48760 ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bb5f30 ["INT_ADD", "register:40f0:8", ["const:bb5f30:8", "const:4:8"]]
+ 00bb5f30 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b48760 bytes a05e0294
+ 00bb5f30 bytes 6c9b0294
~~~


<a id="compare-91da03e123bce60a45861bc96083a846"></a>

### [`00b4935c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4935c.md) → [`00bb6e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6e4c.md) _ZN8firebase9messaging16PollableListener21PollRegistrationTokenEPb

採用 · 移動量 `+0x6daf0` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be03c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4935c.md#insn-00b49380)
- 新版 [`00bb6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6e4c.md#insn-00bb6e70)

~~~diff
- 00b49380 ["INT_ADD", "register:40f0:8", ["const:b49380:8", "const:4:8"]]
- 00b49380 ["CALL", null, ["callee:00c5cf40:8"]]
+ 00bb6e70 ["INT_ADD", "register:40f0:8", ["const:bb6e70:8", "const:4:8"]]
+ 00bb6e70 ["CALL", null, ["callee:00c5cf40:8"]]
- 00b49380 bytes 105c0294
+ 00bb6e70 bytes 34980294
~~~


<a id="compare-ec034af956527c570566f5a6c0925933"></a>

### [`00b4b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b4ec.md) → [`00bb9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9210.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be05a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4b50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b4ec.md#insn-00b4b50c)
- 新版 [`00bb9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9210.md#insn-00bb9230)

~~~diff
- 00b4b50c ["INT_ADD", "register:40f0:8", ["const:b4b50c:8", "const:4:8"]]
- 00b4b50c ["CALL", null, ["callee:00c5d180:8"]]
+ 00bb9230 ["INT_ADD", "register:40f0:8", ["const:bb9230:8", "const:4:8"]]
+ 00bb9230 ["CALL", null, ["callee:00c5d180:8"]]
- 00b4b50c bytes 25540294
+ 00bb9230 bytes d48f0294
~~~


<a id="compare-baa9c05653a434bf292291b0aa7c711c"></a>

### [`00b52318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52318.md) → [`00bc0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0570.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d160.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b523b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52318.md#insn-00b523b4) · [`00b524a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52318.md#insn-00b524a0) · [`00b524dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52318.md#insn-00b524dc)
- 新版 [`00bc0d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0d18) · [`00bc0e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0e04) · [`00bc0e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0e40)

~~~diff
- 00b523b4 ["INT_ADD", "register:40f0:8", ["const:b523b4:8", "const:4:8"]]
- 00b523b4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc0d18 ["INT_ADD", "register:40f0:8", ["const:bc0d18:8", "const:4:8"]]
+ 00bc0d18 ["CALL", null, ["callee:00c57a90:8"]]
- 00b523b4 bytes 23230294
+ 00bc0d18 bytes 5e5b0294
- 00b524a0 ["INT_ADD", "register:40f0:8", ["const:b524a0:8", "const:4:8"]]
- 00b524a0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bc0e04 ["INT_ADD", "register:40f0:8", ["const:bc0e04:8", "const:4:8"]]
+ 00bc0e04 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b524a0 bytes f0220294
+ 00bc0e04 bytes 2b5b0294
- 00b524dc ["INT_ADD", "register:40f0:8", ["const:b524dc:8", "const:4:8"]]
- 00b524dc ["CALL", null, ["callee:00c5a910:8"]]
+ 00bc0e40 ["INT_ADD", "register:40f0:8", ["const:bc0e40:8", "const:4:8"]]
+ 00bc0e40 ["CALL", null, ["callee:00c5a910:8"]]
- 00b524dc bytes 752e0294
+ 00bc0e40 bytes b4660294
~~~


<a id="compare-c1a75b2638160121db8fe6d87d523236"></a>

### [`00b52a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52a5c.md) → [`00bc13c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc13c0.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52a5c.md#insn-00b52a64)
- 新版 [`00bc13c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc13c0.md#insn-00bc13c8)

~~~diff
- 00b52a64 ["INT_ADD", "register:40f0:8", ["const:b52a64:8", "const:4:8"]]
- 00b52a64 ["CALL", null, ["callee:00c5d2b0:8"]]
+ 00bc13c8 ["INT_ADD", "register:40f0:8", ["const:bc13c8:8", "const:4:8"]]
+ 00bc13c8 ["CALL", null, ["callee:00c5d2b0:8"]]
- 00b52a64 bytes 1b370294
+ 00bc13c8 bytes ba6f0294
~~~


<a id="compare-3c0f407c090e632e4a464a4560d13556"></a>

### [`00b52bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52bbc.md) → [`00bc1530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00be07a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52bbc.md#insn-00b52c00) · [`00b52c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52bbc.md#insn-00b52c28) · [`00b52c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52bbc.md#insn-00b52c3c)
- 新版 [`00bc1574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc1574) · [`00bc159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc159c) · [`00bc15b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc15b0)

~~~diff
- 00b52c00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52c00 ["INT_ADD", "register:40f0:8", ["const:b52c00:8", "const:4:8"]]
- 00b52c00 ["CALLIND", null, ["register:0:8"]]
+ 00bc1574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1574 ["INT_ADD", "register:40f0:8", ["const:bc1574:8", "const:4:8"]]
+ 00bc1574 ["CALLIND", null, ["register:0:8"]]
- 00b52c00 bytes 00013fd6
+ 00bc1574 bytes 00013fd6
- 00b52c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52c28 ["INT_ADD", "register:40f0:8", ["const:b52c28:8", "const:4:8"]]
- 00b52c28 ["CALLIND", null, ["register:0:8"]]
+ 00bc159c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc159c ["INT_ADD", "register:40f0:8", ["const:bc159c:8", "const:4:8"]]
+ 00bc159c ["CALLIND", null, ["register:0:8"]]
- 00b52c28 bytes 00013fd6
+ 00bc159c bytes 00013fd6
- 00b52c3c ["INT_ADD", "register:40f0:8", ["const:b52c3c:8", "const:4:8"]]
- 00b52c3c ["CALL", null, ["callee:00c5d390:8"]]
+ 00bc15b0 ["INT_ADD", "register:40f0:8", ["const:bc15b0:8", "const:4:8"]]
+ 00bc15b0 ["CALL", null, ["callee:00c5d390:8"]]
- 00b52c3c bytes d9360294
+ 00bc15b0 bytes 786f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1b8f0f73984e8cc7cc31a1cd9d72beb"></a>

### [`00b52cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cfc.md) → [`00bc1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08b0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08b0.md)
- 新版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4b0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cfc.md#insn-00b52d18) · [`00b52d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cfc.md#insn-00b52d24)
- 新版 [`00bc168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md#insn-00bc168c) · [`00bc1698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md#insn-00bc1698)

~~~diff
- 00b52d18 ["INT_ADD", "register:40f0:8", ["const:b52d18:8", "const:4:8"]]
- 00b52d18 ["CALL", null, ["callee:00c5d4b0:8"]]
+ 00bc168c ["INT_ADD", "register:40f0:8", ["const:bc168c:8", "const:4:8"]]
+ 00bc168c ["CALL", null, ["callee:00c5d4b0:8"]]
- 00b52d18 bytes e6360294
+ 00bc168c bytes 896f0294
- 00b52d24 ["INT_ADD", "register:40f0:8", ["const:b52d24:8", "const:4:8"]]
- 00b52d24 ["CALL", null, ["callee:00c5d4b0:8"]]
+ 00bc1698 ["INT_ADD", "register:40f0:8", ["const:bc1698:8", "const:4:8"]]
+ 00bc1698 ["CALL", null, ["callee:00c5d4b0:8"]]
- 00b52d24 bytes e3360294
+ 00bc1698 bytes 866f0294
~~~


<a id="compare-6cbc75a7543a9c21fa76c06bef51768b"></a>

### [`00b55670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55670.md) → [`00bc43dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0x6ed6c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0970.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d570.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b556c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55670.md#insn-00b556c0) · [`00b556fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55670.md#insn-00b556fc) · [`00b55720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55670.md#insn-00b55720)
- 新版 [`00bc442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md#insn-00bc442c) · [`00bc4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md#insn-00bc4468) · [`00bc448c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md#insn-00bc448c)

~~~diff
- 00b556c0 ["INT_ADD", "register:40f0:8", ["const:b556c0:8", "const:4:8"]]
- 00b556c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc442c ["INT_ADD", "register:40f0:8", ["const:bc442c:8", "const:4:8"]]
+ 00bc442c ["CALL", null, ["callee:00c57a90:8"]]
- 00b556c0 bytes 60160294
+ 00bc442c bytes 994d0294
- 00b556fc ["INT_ADD", "register:40f0:8", ["const:b556fc:8", "const:4:8"]]
- 00b556fc ["CALL", null, ["callee:00c57c00:8"]]
+ 00bc4468 ["INT_ADD", "register:40f0:8", ["const:bc4468:8", "const:4:8"]]
+ 00bc4468 ["CALL", null, ["callee:00c57c00:8"]]
- 00b556fc bytes ad160294
+ 00bc4468 bytes e64d0294
- 00b55720 ["INT_ADD", "register:40f0:8", ["const:b55720:8", "const:4:8"]]
- 00b55720 ["CALL", null, ["callee:00c5a910:8"]]
+ 00bc448c ["INT_ADD", "register:40f0:8", ["const:bc448c:8", "const:4:8"]]
+ 00bc448c ["CALL", null, ["callee:00c5a910:8"]]
- 00b55720 bytes e4210294
+ 00bc448c bytes 21590294
~~~


<a id="compare-79033b5134bcad91bfb2efd65c82cec6"></a>

### [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) → [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b571a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md) [`00b57438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md) [`00b57b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08c0.md)
- 新版 呼出元 3件 [`00bc5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md) [`00bc61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md) [`00bc6904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md#insn-00b56234) · [`00b56280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md#insn-00b56280) · [`00b5628c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md#insn-00b5628c)
- 新版 [`00bc4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc4fec) · [`00bc5038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc5038) · [`00bc5044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc5044)

~~~diff
- 00b56234 ["INT_ADD", "register:40f0:8", ["const:b56234:8", "const:4:8"]]
- 00b56234 ["CALL", null, ["callee:00c5d4c0:8"]]
+ 00bc4fec ["INT_ADD", "register:40f0:8", ["const:bc4fec:8", "const:4:8"]]
+ 00bc4fec ["CALL", null, ["callee:00c5d4c0:8"]]
- 00b56234 bytes a3290294
+ 00bc4fec bytes 35610294
- 00b56280 ["INT_ADD", "register:40f0:8", ["const:b56280:8", "const:4:8"]]
- 00b56280 ["CALL", null, ["callee:00c5d580:8"]]
+ 00bc5038 ["INT_ADD", "register:40f0:8", ["const:bc5038:8", "const:4:8"]]
+ 00bc5038 ["CALL", null, ["callee:00c5d580:8"]]
- 00b56280 bytes c0290294
+ 00bc5038 bytes 52610294
- 00b5628c ["INT_ADD", "register:40f0:8", ["const:b5628c:8", "const:4:8"]]
- 00b5628c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc5044 ["INT_ADD", "register:40f0:8", ["const:bc5044:8", "const:4:8"]]
+ 00bc5044 ["CALL", null, ["callee:00c5a600:8"]]
- 00b5628c bytes 651e0294
+ 00bc5044 bytes 6f550294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91de32d997350eb09f1d5f5ac5d767fd"></a>

### [`00b563d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b563d0.md) → [`00bc5188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0980.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00c5d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d580.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b563d0.md#insn-00b56420) · [`00b5644c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b563d0.md#insn-00b5644c) · [`00b56478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b563d0.md#insn-00b56478)
- 新版 [`00bc51d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc51d8) · [`00bc5204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc5204) · [`00bc5230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc5230)

~~~diff
- 00b56420 ["INT_ADD", "register:40f0:8", ["const:b56420:8", "const:4:8"]]
- 00b56420 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc51d8 ["INT_ADD", "register:40f0:8", ["const:bc51d8:8", "const:4:8"]]
+ 00bc51d8 ["CALL", null, ["callee:00c57a90:8"]]
- 00b56420 bytes 08130294
+ 00bc51d8 bytes 2e4a0294
- 00b5644c ["INT_ADD", "register:40f0:8", ["const:b5644c:8", "const:4:8"]]
- 00b5644c ["CALL", null, ["callee:00c5b1b0:8"]]
+ 00bc5204 ["INT_ADD", "register:40f0:8", ["const:bc5204:8", "const:4:8"]]
+ 00bc5204 ["CALL", null, ["callee:00c5b1b0:8"]]
- 00b5644c bytes b9200294
+ 00bc5204 bytes eb570294
- 00b56478 ["INT_ADD", "register:40f0:8", ["const:b56478:8", "const:4:8"]]
- 00b56478 ["CALL", null, ["callee:00c5a910:8"]]
+ 00bc5230 ["INT_ADD", "register:40f0:8", ["const:bc5230:8", "const:4:8"]]
+ 00bc5230 ["CALL", null, ["callee:00c5a910:8"]]
- 00b56478 bytes 8e1e0294
+ 00bc5230 bytes b8550294
~~~


<a id="compare-1617c7f51578c159ab49a9d5354a6941"></a>

### [`00b5908c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b5908c.md) → [`00bc858c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc858c.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0940.md) · 呼出先 1件 [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d540.md) · 呼出先 1件 [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b5908c.md#insn-00b59098)
- 新版 [`00bc8598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc858c.md#insn-00bc8598)

~~~diff
- 00b59098 ["INT_ADD", "register:40f0:8", ["const:b59098:8", "const:4:8"]]
- 00b59098 ["CALL", null, ["callee:00c5a610:8"]]
+ 00bc8598 ["INT_ADD", "register:40f0:8", ["const:bc8598:8", "const:4:8"]]
+ 00bc8598 ["CALL", null, ["callee:00c5a610:8"]]
- 00b59098 bytes e6120294
+ 00bc8598 bytes 1e480294
~~~


<a id="compare-519ffb46e433d086c0a5433ded06bd7f"></a>

### [`00b59d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md) → [`00bc922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md#insn-00b59d7c) · [`00b59db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md#insn-00b59db8) · [`00b59dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md#insn-00b59dd0)
- 新版 [`00bc927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc927c) · [`00bc92b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc92b8) · [`00bc92d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc92d0)

~~~diff
- 00b59d7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59d7c ["INT_ADD", "register:40f0:8", ["const:b59d7c:8", "const:4:8"]]
- 00b59d7c ["CALLIND", null, ["register:0:8"]]
+ 00bc927c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc927c ["INT_ADD", "register:40f0:8", ["const:bc927c:8", "const:4:8"]]
+ 00bc927c ["CALLIND", null, ["register:0:8"]]
- 00b59d7c bytes 00013fd6
+ 00bc927c bytes 00013fd6
- 00b59db8 ["INT_ADD", "register:40f0:8", ["const:b59db8:8", "const:4:8"]]
- 00b59db8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bc92b8 ["INT_ADD", "register:40f0:8", ["const:bc92b8:8", "const:4:8"]]
+ 00bc92b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b59db8 bytes aa040294
+ 00bc92b8 bytes fe390294
- 00b59dd0 ["INT_ADD", "register:40f0:8", ["const:b59dd0:8", "const:4:8"]]
- 00b59dd0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bc92d0 ["INT_ADD", "register:40f0:8", ["const:bc92d0:8", "const:4:8"]]
+ 00bc92d0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b59dd0 bytes a4040294
+ 00bc92d0 bytes f8390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553a774de6260422a1837db015a7f01c"></a>

### [`00b59e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59e60.md) → [`00bc9360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0960.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00be0950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0950.md)
- 新版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d560.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59e60.md#insn-00b59e94) · [`00b59eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59e60.md#insn-00b59eb0) · [`00b59ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59e60.md#insn-00b59ed8)
- 新版 [`00bc9394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc9394) · [`00bc93b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc93b0) · [`00bc93d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc93d8)

~~~diff
- 00b59e94 ["INT_ADD", "register:40f0:8", ["const:b59e94:8", "const:4:8"]]
- 00b59e94 ["CALL", null, ["callee:00c5d550:8"]]
+ 00bc9394 ["INT_ADD", "register:40f0:8", ["const:bc9394:8", "const:4:8"]]
+ 00bc9394 ["CALL", null, ["callee:00c5d550:8"]]
- 00b59e94 bytes af1a0294
+ 00bc9394 bytes 6f500294
- 00b59eb0 ["INT_ADD", "register:40f0:8", ["const:b59eb0:8", "const:4:8"]]
- 00b59eb0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc93b0 ["INT_ADD", "register:40f0:8", ["const:bc93b0:8", "const:4:8"]]
+ 00bc93b0 ["CALL", null, ["callee:00c57a90:8"]]
- 00b59eb0 bytes 64040294
+ 00bc93b0 bytes b8390294
- 00b59ed8 ["INT_ADD", "register:40f0:8", ["const:b59ed8:8", "const:4:8"]]
- 00b59ed8 ["CALL", null, ["callee:00c5a440:8"]]
+ 00bc93d8 ["INT_ADD", "register:40f0:8", ["const:bc93d8:8", "const:4:8"]]
+ 00bc93d8 ["CALL", null, ["callee:00c5a440:8"]]
- 00b59ed8 bytes c60e0294
+ 00bc93d8 bytes 1a440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65ae23b2535e87833786b9c694e0d0a"></a>

### [`00b5a070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a070.md) → [`00bc9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md) FUN_00bc9570

採用 · 移動量 `+0x6f500` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b598cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be06b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06b0.md)
- 新版 呼出元 1件 [`00bc8dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a070.md#insn-00b5a084)
- 新版 [`00bc9584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md#insn-00bc9584)

~~~diff
- 00b5a084 ["INT_ADD", "register:40f0:8", ["const:b5a084:8", "const:4:8"]]
- 00b5a084 ["CALL", null, ["callee:00c5d290:8"]]
+ 00bc9584 ["INT_ADD", "register:40f0:8", ["const:bc9584:8", "const:4:8"]]
+ 00bc9584 ["CALL", null, ["callee:00c5d290:8"]]
- 00b5a084 bytes 8b190294
+ 00bc9584 bytes 434f0294
~~~


<a id="compare-a27e0893772688337380b0ea426b2297"></a>

### [`00b5aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md) → [`00bc9fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be06b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06b0.md) · 呼出先 1件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md)
- 新版 呼出元 1件 [`00c5d290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d290.md) · 呼出先 1件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md#insn-00b5aadc) · [`00b5ab20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md#insn-00b5ab20)
- 新版 [`00bc9fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md#insn-00bc9fdc) · [`00bca020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md#insn-00bca020)

~~~diff
- 00b5aadc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5aadc ["INT_ADD", "register:40f0:8", ["const:b5aadc:8", "const:4:8"]]
- 00b5aadc ["CALLIND", null, ["register:0:8"]]
+ 00bc9fdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc9fdc ["INT_ADD", "register:40f0:8", ["const:bc9fdc:8", "const:4:8"]]
+ 00bc9fdc ["CALLIND", null, ["register:0:8"]]
- 00b5aadc bytes 00013fd6
+ 00bc9fdc bytes 00013fd6
- 00b5ab20 ["INT_ADD", "register:40f0:8", ["const:b5ab20:8", "const:4:8"]]
- 00b5ab20 ["CALL", null, ["callee:00b60d04:8"]]
+ 00bca020 ["INT_ADD", "register:40f0:8", ["const:bca020:8", "const:4:8"]]
+ 00bca020 ["CALL", null, ["callee:00b60d04:8"]]
- 00b5ab20 bytes 7399fe97
+ 00bca020 bytes 395bfe97
~~~


<a id="compare-43ceeeb225a333ea47f309a6cfe430fe"></a>

### [`00b5b4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4bc.md) → [`00bca9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9bc.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4bc.md#insn-00b5b4c4)
- 新版 [`00bca9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9bc.md#insn-00bca9c4)

~~~diff
- 00b5b4c4 ["INT_ADD", "register:40f0:8", ["const:b5b4c4:8", "const:4:8"]]
- 00b5b4c4 ["CALL", null, ["callee:00c5d630:8"]]
+ 00bca9c4 ["INT_ADD", "register:40f0:8", ["const:bca9c4:8", "const:4:8"]]
+ 00bca9c4 ["CALL", null, ["callee:00c5d630:8"]]
- 00b5b4c4 bytes 5b150294
+ 00bca9c4 bytes 1b4b0294
~~~


<a id="compare-0da6418e8f6994fe2b0e20b0b9181cdb"></a>

### [`00b5c97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c97c.md) → [`00bcbe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c97c.md#insn-00b5c98c) · [`00b5c998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c97c.md#insn-00b5c998)
- 新版 [`00bcbe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md#insn-00bcbe8c) · [`00bcbe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md#insn-00bcbe98)

~~~diff
- 00b5c98c ["INT_ADD", "register:40f0:8", ["const:b5c98c:8", "const:4:8"]]
- 00b5c98c ["CALL", null, ["callee:00c5a660:8"]]
+ 00bcbe8c ["INT_ADD", "register:40f0:8", ["const:bcbe8c:8", "const:4:8"]]
+ 00bcbe8c ["CALL", null, ["callee:00c5a660:8"]]
- 00b5c98c bytes 99040294
+ 00bcbe8c bytes f5390294
- 00b5c998 ["INT_ADD", "register:40f0:8", ["const:b5c998:8", "const:4:8"]]
- 00b5c998 ["CALL", null, ["callee:00c5a660:8"]]
+ 00bcbe98 ["INT_ADD", "register:40f0:8", ["const:bcbe98:8", "const:4:8"]]
+ 00bcbe98 ["CALL", null, ["callee:00c5a660:8"]]
- 00b5c998 bytes 96040294
+ 00bcbe98 bytes f2390294
~~~


<a id="compare-43ade96bd95729efa387ef77804cd81d"></a>

### [`00b5c9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md) → [`00bcbeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md#insn-00b5c9c0) · [`00b5c9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md#insn-00b5c9cc)
- 新版 [`00bcbec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md#insn-00bcbec0) · [`00bcbecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md#insn-00bcbecc)

~~~diff
- 00b5c9c0 ["INT_ADD", "register:40f0:8", ["const:b5c9c0:8", "const:4:8"]]
- 00b5c9c0 ["CALL", null, ["callee:00c5a660:8"]]
+ 00bcbec0 ["INT_ADD", "register:40f0:8", ["const:bcbec0:8", "const:4:8"]]
+ 00bcbec0 ["CALL", null, ["callee:00c5a660:8"]]
- 00b5c9c0 bytes 8c040294
+ 00bcbec0 bytes e8390294
- 00b5c9cc ["INT_ADD", "register:40f0:8", ["const:b5c9cc:8", "const:4:8"]]
- 00b5c9cc ["CALL", null, ["callee:00c5a660:8"]]
+ 00bcbecc ["INT_ADD", "register:40f0:8", ["const:bcbecc:8", "const:4:8"]]
+ 00bcbecc ["CALL", null, ["callee:00c5a660:8"]]
- 00b5c9cc bytes 89040294
+ 00bcbecc bytes e5390294
~~~


<a id="compare-1e72997ba4ed1987cecc4829bbae7da3"></a>

### [`00b5e21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e21c.md) → [`00bcd71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd71c.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a10.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e21c.md#insn-00b5e230)
- 新版 [`00bcd730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd71c.md#insn-00bcd730)

~~~diff
- 00b5e230 ["INT_ADD", "register:40f0:8", ["const:b5e230:8", "const:4:8"]]
- 00b5e230 ["CALL", null, ["callee:00c5d830:8"]]
+ 00bcd730 ["INT_ADD", "register:40f0:8", ["const:bcd730:8", "const:4:8"]]
+ 00bcd730 ["CALL", null, ["callee:00c5d830:8"]]
- 00b5e230 bytes 800a0294
+ 00bcd730 bytes 40400294
~~~


<a id="compare-15e0ac20caff34d08ec801a9f0d9e436"></a>

### [`00b69948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69948.md) → [`00bd8e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e48.md) _ZN8firebase4auth10CredentialC2ERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69948.md#insn-00b6996c)
- 新版 [`00bd8e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e48.md#insn-00bd8e6c)

~~~diff
- 00b6996c ["INT_ADD", "register:40f0:8", ["const:b6996c:8", "const:4:8"]]
- 00b6996c ["CALL", null, ["callee:00c5d960:8"]]
+ 00bd8e6c ["INT_ADD", "register:40f0:8", ["const:bd8e6c:8", "const:4:8"]]
+ 00bd8e6c ["CALL", null, ["callee:00c5d960:8"]]
- 00b6996c bytes fddc0194
+ 00bd8e6c bytes bd120294
~~~


<a id="compare-b3240ad336c9c15ee57935091c335f34"></a>

### [`00b69dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69dec.md) → [`00bd92ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e30.md) · 呼出先 2件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md)
- 新版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da30.md) · 呼出先 2件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b69e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69dec.md#insn-00b69e00) · [`00b69e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69dec.md#insn-00b69e2c)
- 新版 [`00bd9300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md#insn-00bd9300) · [`00bd932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md#insn-00bd932c)

~~~diff
- 00b69e00 ["INT_ADD", "register:40f0:8", ["const:b69e00:8", "const:4:8"]]
- 00b69e00 ["CALL", null, ["callee:00c5d960:8"]]
+ 00bd9300 ["INT_ADD", "register:40f0:8", ["const:bd9300:8", "const:4:8"]]
+ 00bd9300 ["CALL", null, ["callee:00c5d960:8"]]
- 00b69e00 bytes d8db0194
+ 00bd9300 bytes 98110294
- 00b69e2c ["INT_ADD", "register:40f0:8", ["const:b69e2c:8", "const:4:8"]]
- 00b69e2c ["CALL", null, ["callee:00c5acb0:8"]]
+ 00bd932c ["INT_ADD", "register:40f0:8", ["const:bd932c:8", "const:4:8"]]
+ 00bd932c ["CALL", null, ["callee:00c5acb0:8"]]
- 00b69e2c bytes 01d10194
+ 00bd932c bytes 61060294
~~~


<a id="compare-1262ba1b0af48d49d87ac427fdc4e3e4"></a>

### [`00b6ad50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad50.md) → [`00bda250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda250.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ad64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad50.md#insn-00b6ad64)
- 新版 [`00bda264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda250.md#insn-00bda264)

~~~diff
- 00b6ad64 ["INT_ADD", "register:40f0:8", ["const:b6ad64:8", "const:4:8"]]
- 00b6ad64 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bda264 ["INT_ADD", "register:40f0:8", ["const:bda264:8", "const:4:8"]]
+ 00bda264 ["CALL", null, ["callee:00c57a90:8"]]
- 00b6ad64 bytes b7c00194
+ 00bda264 bytes 0bf60194
~~~


<a id="compare-009e2a8ffc4f00afa39565c89cc79078"></a>

### [`00b6ade8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ade8.md) → [`00bda2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda2e8.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ae00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ade8.md#insn-00b6ae00)
- 新版 [`00bda300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda2e8.md#insn-00bda300)

~~~diff
- 00b6ae00 ["INT_ADD", "register:40f0:8", ["const:b6ae00:8", "const:4:8"]]
- 00b6ae00 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bda300 ["INT_ADD", "register:40f0:8", ["const:bda300:8", "const:4:8"]]
+ 00bda300 ["CALL", null, ["callee:00c57a90:8"]]
- 00b6ae00 bytes 90c00194
+ 00bda300 bytes e4f50194
~~~


<a id="compare-6bd8fb21f4f1c1f6a0b660a5ff3305e9"></a>

### [`00b6aec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aec4.md) → [`00bda3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6aee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aec4.md#insn-00b6aee0)
- 新版 [`00bda3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md#insn-00bda3e0)

~~~diff
- 00b6aee0 ["INT_ADD", "register:40f0:8", ["const:b6aee0:8", "const:4:8"]]
- 00b6aee0 ["CALL", null, ["callee:00c5da40:8"]]
+ 00bda3e0 ["INT_ADD", "register:40f0:8", ["const:bda3e0:8", "const:4:8"]]
+ 00bda3e0 ["CALL", null, ["callee:00c5da40:8"]]
- 00b6aee0 bytes d8d70194
+ 00bda3e0 bytes 980d0294
~~~


<a id="compare-9988d11624f6ef893d963f9f36c09bf2"></a>

### [`00b6b9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md) → [`00bdaeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6b9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md#insn-00b6b9e0) · [`00b6b9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md#insn-00b6b9f4) · [`00b6ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md#insn-00b6ba04)
- 新版 [`00bdaee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaee0) · [`00bdaef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaef4) · [`00bdaf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaf04)

~~~diff
- 00b6b9e0 ["INT_ADD", "register:40f0:8", ["const:b6b9e0:8", "const:4:8"]]
- 00b6b9e0 ["CALL", null, ["callee:00c5ab20:8"]]
+ 00bdaee0 ["INT_ADD", "register:40f0:8", ["const:bdaee0:8", "const:4:8"]]
+ 00bdaee0 ["CALL", null, ["callee:00c5ab20:8"]]
- 00b6b9e0 bytes b0c90194
+ 00bdaee0 bytes 10ff0194
- 00b6b9f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6b9f4 ["INT_ADD", "register:40f0:8", ["const:b6b9f4:8", "const:4:8"]]
- 00b6b9f4 ["CALLIND", null, ["register:0:8"]]
+ 00bdaef4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdaef4 ["INT_ADD", "register:40f0:8", ["const:bdaef4:8", "const:4:8"]]
+ 00bdaef4 ["CALLIND", null, ["register:0:8"]]
- 00b6b9f4 bytes 00013fd6
+ 00bdaef4 bytes 00013fd6
- 00b6ba04 ["INT_ADD", "register:40f0:8", ["const:b6ba04:8", "const:4:8"]]
- 00b6ba04 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bdaf04 ["INT_ADD", "register:40f0:8", ["const:bdaf04:8", "const:4:8"]]
+ 00bdaf04 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b6ba04 bytes 97bd0194
+ 00bdaf04 bytes ebf20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18bddc7a72080fa063e7f3287a5827c4"></a>

### [`00b6ccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6ccd4.md) → [`00bdc1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0df0.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbd0.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) [`00be0e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e20.md)
- 新版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9f0.md) · 呼出先 3件 [`00c5a640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a640.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) [`00c5da20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6ccd4.md#insn-00b6ccec) · [`00b6cd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6ccd4.md#insn-00b6cd10) · [`00b6cd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6ccd4.md#insn-00b6cd1c)
- 新版 [`00bdc1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md#insn-00bdc1ec) · [`00bdc210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md#insn-00bdc210) · [`00bdc21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md#insn-00bdc21c)

~~~diff
- 00b6ccec ["INT_ADD", "register:40f0:8", ["const:b6ccec:8", "const:4:8"]]
- 00b6ccec ["CALL", null, ["callee:00c5da20:8"]]
+ 00bdc1ec ["INT_ADD", "register:40f0:8", ["const:bdc1ec:8", "const:4:8"]]
+ 00bdc1ec ["CALL", null, ["callee:00c5da20:8"]]
- 00b6ccec bytes 4dd00194
+ 00bdc1ec bytes 0d060294
- 00b6cd10 ["INT_ADD", "register:40f0:8", ["const:b6cd10:8", "const:4:8"]]
- 00b6cd10 ["CALL", null, ["callee:00c5d960:8"]]
+ 00bdc210 ["INT_ADD", "register:40f0:8", ["const:bdc210:8", "const:4:8"]]
+ 00bdc210 ["CALL", null, ["callee:00c5d960:8"]]
- 00b6cd10 bytes 14d00194
+ 00bdc210 bytes d4050294
- 00b6cd1c ["INT_ADD", "register:40f0:8", ["const:b6cd1c:8", "const:4:8"]]
- 00b6cd1c ["CALL", null, ["callee:00c5a640:8"]]
+ 00bdc21c ["INT_ADD", "register:40f0:8", ["const:bdc21c:8", "const:4:8"]]
+ 00bdc21c ["CALL", null, ["callee:00c5a640:8"]]
- 00b6cd1c bytes adc30194
+ 00bdc21c bytes 09f90194
~~~


<a id="compare-12cec5c8cc16df23b38c0f320b979f1c"></a>

### [`00b6cda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cda4.md) → [`00bdc2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e20.md) · 呼出先 3件 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) [`00be0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e70.md)
- 新版 呼出元 1件 [`00c5da20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da20.md) · 呼出先 3件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) [`00c5da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cda4.md#insn-00b6cdc4) · [`00b6cdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cda4.md#insn-00b6cdd4) · [`00b6ce1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cda4.md#insn-00b6ce1c)
- 新版 [`00bdc2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc2c4) · [`00bdc2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc2d4) · [`00bdc31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc31c)

~~~diff
- 00b6cdc4 ["INT_ADD", "register:40f0:8", ["const:b6cdc4:8", "const:4:8"]]
- 00b6cdc4 ["CALL", null, ["callee:00c5b1b0:8"]]
+ 00bdc2c4 ["INT_ADD", "register:40f0:8", ["const:bdc2c4:8", "const:4:8"]]
+ 00bdc2c4 ["CALL", null, ["callee:00c5b1b0:8"]]
- 00b6cdc4 bytes 5bc60194
+ 00bdc2c4 bytes bbfb0194
- 00b6cdd4 ["INT_ADD", "register:40f0:8", ["const:b6cdd4:8", "const:4:8"]]
- 00b6cdd4 ["CALL", null, ["callee:00c5b1b0:8"]]
+ 00bdc2d4 ["INT_ADD", "register:40f0:8", ["const:bdc2d4:8", "const:4:8"]]
+ 00bdc2d4 ["CALL", null, ["callee:00c5b1b0:8"]]
- 00b6cdd4 bytes 57c60194
+ 00bdc2d4 bytes b7fb0194
- 00b6ce1c ["INT_ADD", "register:40f0:8", ["const:b6ce1c:8", "const:4:8"]]
- 00b6ce1c ["CALL", null, ["callee:00c5da70:8"]]
+ 00bdc31c ["INT_ADD", "register:40f0:8", ["const:bdc31c:8", "const:4:8"]]
+ 00bdc31c ["CALL", null, ["callee:00c5da70:8"]]
- 00b6ce1c bytes 15d00194
+ 00bdc31c bytes d5050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da5ca295949de88db63072fe13913ac9"></a>

### [`00b6d498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d498.md) → [`00bdc998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc998.md) _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d498.md#insn-00b6d4bc)
- 新版 [`00bdc9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc998.md#insn-00bdc9bc)

~~~diff
- 00b6d4bc ["INT_ADD", "register:40f0:8", ["const:b6d4bc:8", "const:4:8"]]
- 00b6d4bc ["CALL", null, ["callee:00c5da30:8"]]
+ 00bdc9bc ["INT_ADD", "register:40f0:8", ["const:bdc9bc:8", "const:4:8"]]
+ 00bdc9bc ["CALL", null, ["callee:00c5da30:8"]]
- 00b6d4bc bytes 5dce0194
+ 00bdc9bc bytes 1d040294
~~~


<a id="compare-6cd6cf1e6555aa42e58f5294bdd43949"></a>

### [`00b728b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b728b8.md) → [`00be1db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1db8.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b728c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b728b8.md#insn-00b728c8)
- 新版 [`00be1dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1db8.md#insn-00be1dc8)

~~~diff
- 00b728c8 ["INT_ADD", "register:40f0:8", ["const:b728c8:8", "const:4:8"]]
- 00b728c8 ["CALL", null, ["callee:00c5d780:8"]]
+ 00be1dc8 ["INT_ADD", "register:40f0:8", ["const:be1dc8:8", "const:4:8"]]
+ 00be1dc8 ["CALL", null, ["callee:00c5d780:8"]]
- 00b728c8 bytes aeb80194
+ 00be1dc8 bytes 6eee0194
~~~


<a id="compare-9ba23e787d6dae3e462f7dd6222d7b50"></a>

### [`00b72a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a80.md) → [`00bef688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f30.md) · 呼出先 2件 [`00be0f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f10.md) [`00be0f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f20.md)
- 新版 呼出元 1件 [`00c5db30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db30.md) · 呼出先 2件 [`00c5db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db10.md) [`00c5db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a80.md#insn-00b72aa8) · [`00b72ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a80.md#insn-00b72ab0)
- 新版 [`00bef6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md#insn-00bef6b0) · [`00bef6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md#insn-00bef6b8)

~~~diff
- 00b72aa8 ["INT_ADD", "register:40f0:8", ["const:b72aa8:8", "const:4:8"]]
- 00b72aa8 ["CALL", null, ["callee:00c5db20:8"]]
+ 00bef6b0 ["INT_ADD", "register:40f0:8", ["const:bef6b0:8", "const:4:8"]]
+ 00bef6b0 ["CALL", null, ["callee:00c5db20:8"]]
- 00b72aa8 bytes 1eb90194
+ 00bef6b0 bytes 1cb90194
- 00b72ab0 ["INT_ADD", "register:40f0:8", ["const:b72ab0:8", "const:4:8"]]
- 00b72ab0 ["CALL", null, ["callee:00c5db10:8"]]
+ 00bef6b8 ["INT_ADD", "register:40f0:8", ["const:bef6b8:8", "const:4:8"]]
+ 00bef6b8 ["CALL", null, ["callee:00c5db10:8"]]
- 00b72ab0 bytes 18b90194
+ 00bef6b8 bytes 16b90194
~~~


<a id="compare-c4871f238b082411cfbd0b575416323e"></a>

### [`00b72b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b18.md) → [`00bef720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef720.md) _ZSt17current_exceptionv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb710.md) · 呼出先 1件 [`00be0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f40.md)
- 新版 呼出元 1件 [`00c58160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58160.md) · 呼出先 1件 [`00c5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b18.md#insn-00b72b2c)
- 新版 [`00bef734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef720.md#insn-00bef734)

~~~diff
- 00b72b2c ["INT_ADD", "register:40f0:8", ["const:b72b2c:8", "const:4:8"]]
- 00b72b2c ["CALL", null, ["callee:00c5db40:8"]]
+ 00bef734 ["INT_ADD", "register:40f0:8", ["const:bef734:8", "const:4:8"]]
+ 00bef734 ["CALL", null, ["callee:00c5db40:8"]]
- 00b72b2c bytes 05b90194
+ 00bef734 bytes 03b90194
~~~


<a id="compare-46a84b3a15c8c1d06fcf093bb49365e7"></a>

### [`00b72be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72be0.md) → [`00bef7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb670.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be0f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00c580c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580c0.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72be0.md#insn-00b72bf0) · [`00b72bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72be0.md#insn-00b72bf4)
- 新版 [`00bef7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md#insn-00bef7f8) · [`00bef7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md#insn-00bef7fc)

~~~diff
- 00b72bf0 ["INT_ADD", "register:40f0:8", ["const:b72bf0:8", "const:4:8"]]
- 00b72bf0 ["CALL", null, ["callee:00c5db60:8"]]
+ 00bef7f8 ["INT_ADD", "register:40f0:8", ["const:bef7f8:8", "const:4:8"]]
+ 00bef7f8 ["CALL", null, ["callee:00c5db60:8"]]
- 00b72bf0 bytes dcb80194
+ 00bef7f8 bytes dab80194
- 00b72bf4 ["INT_ADD", "register:40f0:8", ["const:b72bf4:8", "const:4:8"]]
- 00b72bf4 ["CALL", null, ["callee:00c57c20:8"]]
+ 00bef7fc ["INT_ADD", "register:40f0:8", ["const:bef7fc:8", "const:4:8"]]
+ 00bef7fc ["CALL", null, ["callee:00c57c20:8"]]
- 00b72bf4 bytes 77a10194
+ 00bef7fc bytes 09a10194
~~~


<a id="compare-f8eadf1e3013e6f26550e8b0d9217580"></a>

### [`00b73400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73400.md) → [`00bf0008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0008.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73400.md#insn-00b73414)
- 新版 [`00bf001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0008.md#insn-00bf001c)

~~~diff
- 00b73414 ["INT_ADD", "register:40f0:8", ["const:b73414:8", "const:4:8"]]
- 00b73414 ["CALL", null, ["callee:00c538b0:8"]]
+ 00bf001c ["INT_ADD", "register:40f0:8", ["const:bf001c:8", "const:4:8"]]
+ 00bf001c ["CALL", null, ["callee:00c538b0:8"]]
- 00b73414 bytes 938e0194
+ 00bf001c bytes 258e0194
~~~


<a id="compare-2663ed51b52e1053004fd1197fe67d0a"></a>

### [`00b73474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73474.md) → [`00bf007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf007c.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73474.md#insn-00b73488)
- 新版 [`00bf0090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf007c.md#insn-00bf0090)

~~~diff
- 00b73488 ["INT_ADD", "register:40f0:8", ["const:b73488:8", "const:4:8"]]
- 00b73488 ["CALL", null, ["callee:00c538b0:8"]]
+ 00bf0090 ["INT_ADD", "register:40f0:8", ["const:bf0090:8", "const:4:8"]]
+ 00bf0090 ["CALL", null, ["callee:00c538b0:8"]]
- 00b73488 bytes 768e0194
+ 00bf0090 bytes 088e0194
~~~


<a id="compare-1c9143f0fcf6bb7809c1418bc46b98d2"></a>

### [`00b73498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73498.md) → [`00bf00a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00a0.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b734ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73498.md#insn-00b734ac)
- 新版 [`00bf00b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00a0.md#insn-00bf00b4)

~~~diff
- 00b734ac ["INT_ADD", "register:40f0:8", ["const:b734ac:8", "const:4:8"]]
- 00b734ac ["CALL", null, ["callee:00c538b0:8"]]
+ 00bf00b4 ["INT_ADD", "register:40f0:8", ["const:bf00b4:8", "const:4:8"]]
+ 00bf00b4 ["CALL", null, ["callee:00c538b0:8"]]
- 00b734ac bytes 6d8e0194
+ 00bf00b4 bytes ff8d0194
~~~


<a id="compare-404272c7d8fcc280ce199034cb3891cf"></a>

### [`00b73590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73590.md) → [`00bf0198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0198.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6a0.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00c580f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580f0.md) · 呼出先 1件 [`00c537e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c537e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b735c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73590.md#insn-00b735c0)
- 新版 [`00bf01c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0198.md#insn-00bf01c8)

~~~diff
- 00b735c0 ["INT_ADD", "register:40f0:8", ["const:b735c0:8", "const:4:8"]]
- 00b735c0 ["CALL", null, ["callee:00c537e0:8"]]
+ 00bf01c8 ["INT_ADD", "register:40f0:8", ["const:bf01c8:8", "const:4:8"]]
+ 00bf01c8 ["CALL", null, ["callee:00c537e0:8"]]
- 00b735c0 bytes f48d0194
+ 00bf01c8 bytes 868d0194
~~~


<a id="compare-a6692035c2654972613566ee0fc1202d"></a>

### [`00b735fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b735fc.md) → [`00bf0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0204.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7360c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b735fc.md#insn-00b7360c)
- 新版 [`00bf0214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0204.md#insn-00bf0214)

~~~diff
- 00b7360c ["INT_ADD", "register:40f0:8", ["const:b7360c:8", "const:4:8"]]
- 00b7360c ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bf0214 ["INT_ADD", "register:40f0:8", ["const:bf0214:8", "const:4:8"]]
+ 00bf0214 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7360c bytes 85ac0194
+ 00bf0214 bytes 23ac0194
~~~


<a id="compare-a8f86280c5f08c41f5ce7fd1d8ee85b9"></a>

### [`00b73620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73620.md) → [`00bf0228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0228.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73620.md#insn-00b73630)
- 新版 [`00bf0238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0228.md#insn-00bf0238)

~~~diff
- 00b73630 ["INT_ADD", "register:40f0:8", ["const:b73630:8", "const:4:8"]]
- 00b73630 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bf0238 ["INT_ADD", "register:40f0:8", ["const:bf0238:8", "const:4:8"]]
+ 00bf0238 ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b73630 bytes 80ac0194
+ 00bf0238 bytes 1eac0194
~~~


<a id="compare-e33be418b14251309de2f2a6abc513c9"></a>

### [`00b73644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73644.md) → [`00bf024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf024c.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf0298",
      "incomplete_value": true,
      "site": "00bf029c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca42e8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73690",
      "incomplete_value": true,
      "site": "00b73694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24808:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b73684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73644.md#insn-00b73684)
- 新版 [`00bf028c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf024c.md#insn-00bf028c)

~~~diff
- 00b73684 ["COPY", "register:4048:8", ["const:c24808:8"]]
+ 00bf028c ["COPY", "register:4048:8", ["const:ca42e8:8"]]
- 00b73684 bytes 298c5810
+ 00bf028c bytes e9025a10
~~~


<a id="compare-0e128b76ff76b04d63eb00b95cca6e33"></a>

### [`00b73874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md) → [`00bf047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7389c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md#insn-00b7389c) · [`00b738a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md#insn-00b738a8) · [`00b738b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md#insn-00b738b8)
- 新版 [`00bf04a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04a4) · [`00bf04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04b0) · [`00bf04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04c0)

~~~diff
- 00b7389c ["INT_ADD", "register:40f0:8", ["const:b7389c:8", "const:4:8"]]
- 00b7389c ["CALL", null, ["callee:00c53880:8"]]
+ 00bf04a4 ["INT_ADD", "register:40f0:8", ["const:bf04a4:8", "const:4:8"]]
+ 00bf04a4 ["CALL", null, ["callee:00c53880:8"]]
- 00b7389c bytes 658d0194
+ 00bf04a4 bytes f78c0194
- 00b738a8 ["INT_ADD", "register:40f0:8", ["const:b738a8:8", "const:4:8"]]
- 00b738a8 ["CALL", null, ["callee:00c53880:8"]]
+ 00bf04b0 ["INT_ADD", "register:40f0:8", ["const:bf04b0:8", "const:4:8"]]
+ 00bf04b0 ["CALL", null, ["callee:00c53880:8"]]
- 00b738a8 bytes 628d0194
+ 00bf04b0 bytes f48c0194
- 00b738b8 ["INT_ADD", "register:40f0:8", ["const:b738b8:8", "const:4:8"]]
- 00b738b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bf04c0 ["INT_ADD", "register:40f0:8", ["const:bf04c0:8", "const:4:8"]]
+ 00bf04c0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b738b8 bytes ea9d0194
+ 00bf04c0 bytes 7c9d0194
~~~


<a id="compare-d5273695d6c10822b03322e7dae3abad"></a>

### [`00b73d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73d60.md) → [`00bf0968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73d60.md#insn-00b73dbc) · [`00b73de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73d60.md#insn-00b73de0) · [`00b73e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73d60.md#insn-00b73e00)
- 新版 [`00bf09c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf09c4) · [`00bf09e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf09e8) · [`00bf0a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf0a08)

~~~diff
- 00b73dbc ["INT_ADD", "register:40f0:8", ["const:b73dbc:8", "const:4:8"]]
- 00b73dbc ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf09c4 ["INT_ADD", "register:40f0:8", ["const:bf09c4:8", "const:4:8"]]
+ 00bf09c4 ["CALL", null, ["callee:00c57a90:8"]]
- 00b73dbc bytes a19c0194
+ 00bf09c4 bytes 339c0194
- 00b73de0 ["INT_ADD", "register:40f0:8", ["const:b73de0:8", "const:4:8"]]
- 00b73de0 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf09e8 ["INT_ADD", "register:40f0:8", ["const:bf09e8:8", "const:4:8"]]
+ 00bf09e8 ["CALL", null, ["callee:00c57b40:8"]]
- 00b73de0 bytes c49c0194
+ 00bf09e8 bytes 569c0194
- 00b73e00 ["INT_ADD", "register:40f0:8", ["const:b73e00:8", "const:4:8"]]
- 00b73e00 ["CALL", null, ["callee:0043b724:8"]]
+ 00bf0a08 ["INT_ADD", "register:40f0:8", ["const:bf0a08:8", "const:4:8"]]
+ 00bf0a08 ["CALL", null, ["callee:0043b724:8"]]
- 00b73e00 bytes 8993e297
+ 00bf0a08 bytes 472be197
~~~


<a id="compare-7ccc9cbe09a105102ae5081f7c2aed70"></a>

### [`00b73e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73e30.md) → [`00bf0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0a38.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb230.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md)
- 新版 呼出元 1件 [`00c57c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c80.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73e30.md#insn-00b73e58)
- 新版 [`00bf0a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0a38.md#insn-00bf0a60)

~~~diff
- 00b73e58 ["INT_ADD", "register:40f0:8", ["const:b73e58:8", "const:4:8"]]
- 00b73e58 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf0a60 ["INT_ADD", "register:40f0:8", ["const:bf0a60:8", "const:4:8"]]
+ 00bf0a60 ["CALL", null, ["callee:00c57be0:8"]]
- 00b73e58 bytes ce9c0194
+ 00bf0a60 bytes 609c0194
~~~


<a id="compare-7a25ada34c67f56b73cb187b5941529b"></a>

### [`00b742fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b742fc.md) → [`00bf0d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b742fc.md#insn-00b74358) · [`00b74378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b742fc.md#insn-00b74378) · [`00b74398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b742fc.md#insn-00b74398)
- 新版 [`00bf0da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0da0) · [`00bf0dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0dc0) · [`00bf0de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0de0)

~~~diff
- 00b74358 ["INT_ADD", "register:40f0:8", ["const:b74358:8", "const:4:8"]]
- 00b74358 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf0da0 ["INT_ADD", "register:40f0:8", ["const:bf0da0:8", "const:4:8"]]
+ 00bf0da0 ["CALL", null, ["callee:00c57a90:8"]]
- 00b74358 bytes 3a9b0194
+ 00bf0da0 bytes 3c9b0194
- 00b74378 ["INT_ADD", "register:40f0:8", ["const:b74378:8", "const:4:8"]]
- 00b74378 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf0dc0 ["INT_ADD", "register:40f0:8", ["const:bf0dc0:8", "const:4:8"]]
+ 00bf0dc0 ["CALL", null, ["callee:00c57b40:8"]]
- 00b74378 bytes 5e9b0194
+ 00bf0dc0 bytes 609b0194
- 00b74398 ["INT_ADD", "register:40f0:8", ["const:b74398:8", "const:4:8"]]
- 00b74398 ["CALL", null, ["callee:0043b724:8"]]
+ 00bf0de0 ["INT_ADD", "register:40f0:8", ["const:bf0de0:8", "const:4:8"]]
+ 00bf0de0 ["CALL", null, ["callee:0043b724:8"]]
- 00b74398 bytes 2392e297
+ 00bf0de0 bytes 512ae197
~~~


<a id="compare-6be584a925c3943d841cd09c83d70da5"></a>

### [`00b7439c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7439c.md) → [`00bf0de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0de4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b743dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7439c.md#insn-00b743dc)
- 新版 [`00bf0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0de4.md#insn-00bf0e24)

~~~diff
- 00b743dc ["INT_ADD", "register:40f0:8", ["const:b743dc:8", "const:4:8"]]
- 00b743dc ["CALL", null, ["callee:004428dc:8"]]
+ 00bf0e24 ["INT_ADD", "register:40f0:8", ["const:bf0e24:8", "const:4:8"]]
+ 00bf0e24 ["CALL", null, ["callee:004428dc:8"]]
- 00b743dc bytes 80aee297
+ 00bf0e24 bytes ae46e197
~~~


<a id="compare-95d9d98fa427724632e211436a08a33d"></a>

### [`00b7445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md) → [`00bf0ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b744f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md#insn-00b744f4) · [`00b7452c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md#insn-00b7452c) · [`00b74540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md#insn-00b74540)
- 新版 [`00bf0f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f3c) · [`00bf0f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f74) · [`00bf0f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f88)

~~~diff
- 00b744f4 ["INT_ADD", "register:40f0:8", ["const:b744f4:8", "const:4:8"]]
- 00b744f4 ["CALL", null, ["callee:00bf0bdc:8"]]
+ 00bf0f3c ["INT_ADD", "register:40f0:8", ["const:bf0f3c:8", "const:4:8"]]
+ 00bf0f3c ["CALL", null, ["callee:00bf0bdc:8"]]
- 00b744f4 bytes 28ffff97
+ 00bf0f3c bytes 28ffff97
- 00b7452c ["INT_ADD", "register:40f0:8", ["const:b7452c:8", "const:4:8"]]
- 00b7452c ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf0f74 ["INT_ADD", "register:40f0:8", ["const:bf0f74:8", "const:4:8"]]
+ 00bf0f74 ["CALL", null, ["callee:00c57b40:8"]]
- 00b7452c bytes f19a0194
+ 00bf0f74 bytes f39a0194
- 00b74540 ["INT_ADD", "register:40f0:8", ["const:b74540:8", "const:4:8"]]
- 00b74540 ["CALL", null, ["callee:00c57c90:8"]]
+ 00bf0f88 ["INT_ADD", "register:40f0:8", ["const:bf0f88:8", "const:4:8"]]
+ 00bf0f88 ["CALL", null, ["callee:00c57c90:8"]]
- 00b74540 bytes 409b0194
+ 00bf0f88 bytes 429b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c82366cf695f58a247e338158e8e760"></a>

### [`00b746dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b746dc.md) → [`00bf1124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b746dc.md#insn-00b74728)
- 新版 [`00bf1170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md#insn-00bf1170)

~~~diff
- 00b74728 ["INT_ADD", "register:40f0:8", ["const:b74728:8", "const:4:8"]]
- 00b74728 ["CALL", null, ["callee:004428dc:8"]]
+ 00bf1170 ["INT_ADD", "register:40f0:8", ["const:bf1170:8", "const:4:8"]]
+ 00bf1170 ["CALL", null, ["callee:004428dc:8"]]
- 00b74728 bytes adade297
+ 00bf1170 bytes db45e197
~~~


<a id="compare-75e9b43819d6103ed46f23f8a5c790c3"></a>

### [`00b7472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7472c.md) → [`00bf1174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7472c.md#insn-00b74780) · [`00b74798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7472c.md#insn-00b74798)
- 新版 [`00bf11c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md#insn-00bf11c8) · [`00bf11e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md#insn-00bf11e0)

~~~diff
- 00b74780 ["INT_ADD", "register:40f0:8", ["const:b74780:8", "const:4:8"]]
- 00b74780 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf11c8 ["INT_ADD", "register:40f0:8", ["const:bf11c8:8", "const:4:8"]]
+ 00bf11c8 ["CALL", null, ["callee:00c57b40:8"]]
- 00b74780 bytes 5c9a0194
+ 00bf11c8 bytes 5e9a0194
- 00b74798 ["INT_ADD", "register:40f0:8", ["const:b74798:8", "const:4:8"]]
- 00b74798 ["CALL", null, ["callee:004428dc:8"]]
+ 00bf11e0 ["INT_ADD", "register:40f0:8", ["const:bf11e0:8", "const:4:8"]]
+ 00bf11e0 ["CALL", null, ["callee:004428dc:8"]]
- 00b74798 bytes 91ade297
+ 00bf11e0 bytes bf45e197
~~~


<a id="compare-d2bf01f468e2d754d261dc0c2bb64384"></a>

### [`00b74878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74878.md) → [`00bf12c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf12c0.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb780.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00c581d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581d0.md) · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b748c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74878.md#insn-00b748c0)
- 新版 [`00bf1308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf12c0.md#insn-00bf1308)

~~~diff
- 00b748c0 ["INT_ADD", "register:40f0:8", ["const:b748c0:8", "const:4:8"]]
- 00b748c0 ["CALL", null, ["callee:00c57bd0:8"]]
+ 00bf1308 ["INT_ADD", "register:40f0:8", ["const:bf1308:8", "const:4:8"]]
+ 00bf1308 ["CALL", null, ["callee:00c57bd0:8"]]
- 00b748c0 bytes 309a0194
+ 00bf1308 bytes 329a0194
~~~


<a id="compare-8ba9011a0f2bfed77f7f7e84b6c30673"></a>

### [`00b748e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b748e8.md) → [`00bf1330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b748e8.md#insn-00b74944) · [`00b74964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b748e8.md#insn-00b74964) · [`00b74984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b748e8.md#insn-00b74984)
- 新版 [`00bf138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf138c) · [`00bf13ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf13ac) · [`00bf13cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf13cc)

~~~diff
- 00b74944 ["INT_ADD", "register:40f0:8", ["const:b74944:8", "const:4:8"]]
- 00b74944 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf138c ["INT_ADD", "register:40f0:8", ["const:bf138c:8", "const:4:8"]]
+ 00bf138c ["CALL", null, ["callee:00c57a90:8"]]
- 00b74944 bytes bf990194
+ 00bf138c bytes c1990194
- 00b74964 ["INT_ADD", "register:40f0:8", ["const:b74964:8", "const:4:8"]]
- 00b74964 ["CALL", null, ["callee:00c57c90:8"]]
+ 00bf13ac ["INT_ADD", "register:40f0:8", ["const:bf13ac:8", "const:4:8"]]
+ 00bf13ac ["CALL", null, ["callee:00c57c90:8"]]
- 00b74964 bytes 379a0194
+ 00bf13ac bytes 399a0194
- 00b74984 ["INT_ADD", "register:40f0:8", ["const:b74984:8", "const:4:8"]]
- 00b74984 ["CALL", null, ["callee:0043b724:8"]]
+ 00bf13cc ["INT_ADD", "register:40f0:8", ["const:bf13cc:8", "const:4:8"]]
+ 00bf13cc ["CALL", null, ["callee:0043b724:8"]]
- 00b74984 bytes a890e297
+ 00bf13cc bytes d628e197
~~~


<a id="compare-22565ed53f5cfa2b1dde66a3dc611d59"></a>

### [`00b74988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74988.md) → [`00bf13d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf13d0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 1件 [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b749ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74988.md#insn-00b749ac)
- 新版 [`00bf13f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf13d0.md#insn-00bf13f4)

~~~diff
- 00b749ac ["INT_ADD", "register:40f0:8", ["const:b749ac:8", "const:4:8"]]
- 00b749ac ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf13f4 ["INT_ADD", "register:40f0:8", ["const:bf13f4:8", "const:4:8"]]
+ 00bf13f4 ["CALL", null, ["callee:00c57be0:8"]]
- 00b749ac bytes f9990194
+ 00bf13f4 bytes fb990194
~~~


<a id="compare-6f129976c22d9f6c17eb1e8d45eed1e7"></a>

### [`00b749d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b749d4.md) → [`00bf141c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf141c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b749d4.md#insn-00b74a30)
- 新版 [`00bf1478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf141c.md#insn-00bf1478)

~~~diff
- 00b74a30 ["INT_ADD", "register:40f0:8", ["const:b74a30:8", "const:4:8"]]
- 00b74a30 ["CALL", null, ["callee:00c57bd0:8"]]
+ 00bf1478 ["INT_ADD", "register:40f0:8", ["const:bf1478:8", "const:4:8"]]
+ 00bf1478 ["CALL", null, ["callee:00c57bd0:8"]]
- 00b74a30 bytes d4990194
+ 00bf1478 bytes d6990194
~~~


<a id="compare-77b949d737f17665316d63c6fec8d43d"></a>

### [`00b74a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74a5c.md) → [`00bf14a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74a5c.md#insn-00b74b28) · [`00b74b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74a5c.md#insn-00b74b38) · [`00b74b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74a5c.md#insn-00b74b48)
- 新版 [`00bf1570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1570) · [`00bf1580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1580) · [`00bf1590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1590)

~~~diff
- 00b74b28 ["INT_ADD", "register:40f0:8", ["const:b74b28:8", "const:4:8"]]
- 00b74b28 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf1570 ["INT_ADD", "register:40f0:8", ["const:bf1570:8", "const:4:8"]]
+ 00bf1570 ["CALL", null, ["callee:00c57a90:8"]]
- 00b74b28 bytes 46990194
+ 00bf1570 bytes 48990194
- 00b74b38 ["INT_ADD", "register:40f0:8", ["const:b74b38:8", "const:4:8"]]
- 00b74b38 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf1580 ["INT_ADD", "register:40f0:8", ["const:bf1580:8", "const:4:8"]]
+ 00bf1580 ["CALL", null, ["callee:00c57b40:8"]]
- 00b74b38 bytes 6e990194
+ 00bf1580 bytes 70990194
- 00b74b48 ["INT_ADD", "register:40f0:8", ["const:b74b48:8", "const:4:8"]]
- 00b74b48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bf1590 ["INT_ADD", "register:40f0:8", ["const:bf1590:8", "const:4:8"]]
+ 00bf1590 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b74b48 bytes 46990194
+ 00bf1590 bytes 48990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d72e7f691af244752a7814dc15e29b"></a>

### [`00b74be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74be0.md) → [`00bf1628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd890.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c5a2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a2e0.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74be0.md#insn-00b74cbc) · [`00b74ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74be0.md#insn-00b74ccc) · [`00b74ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74be0.md#insn-00b74ce8)
- 新版 [`00bf1704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1704) · [`00bf1714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1714) · [`00bf1730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1730)

~~~diff
- 00b74cbc ["INT_ADD", "register:40f0:8", ["const:b74cbc:8", "const:4:8"]]
- 00b74cbc ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf1704 ["INT_ADD", "register:40f0:8", ["const:bf1704:8", "const:4:8"]]
+ 00bf1704 ["CALL", null, ["callee:00c57a90:8"]]
- 00b74cbc bytes e1980194
+ 00bf1704 bytes e3980194
- 00b74ccc ["INT_ADD", "register:40f0:8", ["const:b74ccc:8", "const:4:8"]]
- 00b74ccc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bf1714 ["INT_ADD", "register:40f0:8", ["const:bf1714:8", "const:4:8"]]
+ 00bf1714 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b74ccc bytes e5980194
+ 00bf1714 bytes e7980194
- 00b74ce8 ["INT_ADD", "register:40f0:8", ["const:b74ce8:8", "const:4:8"]]
- 00b74ce8 ["CALL", null, ["callee:00c57c90:8"]]
+ 00bf1730 ["INT_ADD", "register:40f0:8", ["const:bf1730:8", "const:4:8"]]
+ 00bf1730 ["CALL", null, ["callee:00c57c90:8"]]
- 00b74ce8 bytes 56990194
+ 00bf1730 bytes 58990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fed1788ac7bc6bd6bc216a18e6193f1"></a>

### [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md) → [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md) FUN_00bf17e4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b74d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md) [`00bb9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`00bf176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md) [`00c35c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md#insn-00b74df4)
- 新版 [`00bf183c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md#insn-00bf183c)

~~~diff
- 00b74df4 ["INT_ADD", "register:40f0:8", ["const:b74df4:8", "const:4:8"]]
- 00b74df4 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf183c ["INT_ADD", "register:40f0:8", ["const:bf183c:8", "const:4:8"]]
+ 00bf183c ["CALL", null, ["callee:00c57b40:8"]]
- 00b74df4 bytes bf980194
+ 00bf183c bytes c1980194
~~~


<a id="compare-ca575c96939d9fa453e41fe3eaaf6a29"></a>

### [`00b74e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74e30.md) → [`00bf1878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74e30.md#insn-00b74ecc) · [`00b74ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74e30.md#insn-00b74ef4) · [`00b74f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74e30.md#insn-00b74f34)
- 新版 [`00bf1914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf1914) · [`00bf193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf193c) · [`00bf197c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf197c)

~~~diff
- 00b74ecc ["INT_ADD", "register:40f0:8", ["const:b74ecc:8", "const:4:8"]]
- 00b74ecc ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bf1914 ["INT_ADD", "register:40f0:8", ["const:bf1914:8", "const:4:8"]]
+ 00bf1914 ["CALL", null, ["callee:00c5aca0:8"]]
- 00b74ecc bytes d5a40194
+ 00bf1914 bytes e3a40194
- 00b74ef4 ["INT_ADD", "register:40f0:8", ["const:b74ef4:8", "const:4:8"]]
- 00b74ef4 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf193c ["INT_ADD", "register:40f0:8", ["const:bf193c:8", "const:4:8"]]
+ 00bf193c ["CALL", null, ["callee:00c57b40:8"]]
- 00b74ef4 bytes 7f980194
+ 00bf193c bytes 81980194
- 00b74f34 ["INT_ADD", "register:40f0:8", ["const:b74f34:8", "const:4:8"]]
- 00b74f34 ["CALL", null, ["callee:004428dc:8"]]
+ 00bf197c ["INT_ADD", "register:40f0:8", ["const:bf197c:8", "const:4:8"]]
+ 00bf197c ["CALL", null, ["callee:004428dc:8"]]
- 00b74f34 bytes aaabe297
+ 00bf197c bytes d843e197
~~~


<a id="compare-cc779f64414c63fc1f7ca7d9bbd72bcf"></a>

### [`00b74f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74f38.md) → [`00bf1980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74f38.md#insn-00b74f54) · [`00b74f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74f38.md#insn-00b74f90) · [`00b74fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74f38.md#insn-00b74fb0)
- 新版 [`00bf199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf199c) · [`00bf19d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf19d8) · [`00bf19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf19f8)

~~~diff
- 00b74f54 ["INT_ADD", "register:40f0:8", ["const:b74f54:8", "const:4:8"]]
- 00b74f54 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf199c ["INT_ADD", "register:40f0:8", ["const:bf199c:8", "const:4:8"]]
+ 00bf199c ["CALL", null, ["callee:00c57be0:8"]]
- 00b74f54 bytes 8f980194
+ 00bf199c bytes 91980194
- 00b74f90 ["INT_ADD", "register:40f0:8", ["const:b74f90:8", "const:4:8"]]
- 00b74f90 ["CALL", null, ["callee:00c57c50:8"]]
+ 00bf19d8 ["INT_ADD", "register:40f0:8", ["const:bf19d8:8", "const:4:8"]]
+ 00bf19d8 ["CALL", null, ["callee:00c57c50:8"]]
- 00b74f90 bytes 9c980194
+ 00bf19d8 bytes 9e980194
- 00b74fb0 ["INT_ADD", "register:40f0:8", ["const:b74fb0:8", "const:4:8"]]
- 00b74fb0 ["CALL", null, ["callee:004428dc:8"]]
+ 00bf19f8 ["INT_ADD", "register:40f0:8", ["const:bf19f8:8", "const:4:8"]]
+ 00bf19f8 ["CALL", null, ["callee:004428dc:8"]]
- 00b74fb0 bytes 8babe297
+ 00bf19f8 bytes b943e197
~~~


<a id="compare-62f9c7d7b6591b6ae222d464a5ea35d2"></a>

### [`00b74fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74fb8.md) → [`00bf1a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74fb8.md#insn-00b75018) · [`00b75034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74fb8.md#insn-00b75034)
- 新版 [`00bf1a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md#insn-00bf1a60) · [`00bf1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md#insn-00bf1a7c)

~~~diff
- 00b75018 ["INT_ADD", "register:40f0:8", ["const:b75018:8", "const:4:8"]]
- 00b75018 ["CALL", null, ["callee:00c57c50:8"]]
+ 00bf1a60 ["INT_ADD", "register:40f0:8", ["const:bf1a60:8", "const:4:8"]]
+ 00bf1a60 ["CALL", null, ["callee:00c57c50:8"]]
- 00b75018 bytes 7a980194
+ 00bf1a60 bytes 7c980194
- 00b75034 ["INT_ADD", "register:40f0:8", ["const:b75034:8", "const:4:8"]]
- 00b75034 ["CALL", null, ["callee:004428dc:8"]]
+ 00bf1a7c ["INT_ADD", "register:40f0:8", ["const:bf1a7c:8", "const:4:8"]]
+ 00bf1a7c ["CALL", null, ["callee:004428dc:8"]]
- 00b75034 bytes 6aabe297
+ 00bf1a7c bytes 9843e197
~~~


<a id="compare-7ad3b3792b1e8ed0f4e88e96c2715875"></a>

### [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) → [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) FUN_00bf1b70

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b75120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75120.md) [`00baf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf3b8.md) [`00baf7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf7b4.md) [`00bb3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb3c00.md) [`00bb5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5c14.md) · 呼出先 2件 [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 8件 [`00bf1b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b68.md) [`00c2be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md) [`00c2c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md) [`00c30648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md) [`00c3265c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md) · 呼出先 2件 [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md#insn-00b75144)
- 新版 [`00bf1b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md#insn-00bf1b8c)

~~~diff
- 00b75144 ["INT_ADD", "register:40f0:8", ["const:b75144:8", "const:4:8"]]
- 00b75144 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf1b8c ["INT_ADD", "register:40f0:8", ["const:bf1b8c:8", "const:4:8"]]
+ 00bf1b8c ["CALL", null, ["callee:00c57be0:8"]]
- 00b75144 bytes 13980194
+ 00bf1b8c bytes 15980194
~~~


<a id="compare-09d8fc89fe3784c311c7f0340b8dd614"></a>

### [`00b75164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md) → [`00bf1bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md#insn-00b75204) · [`00b75218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md#insn-00b75218)
- 新版 [`00bf1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md#insn-00bf1c4c) · [`00bf1c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md#insn-00bf1c60)

~~~diff
- 00b75204 ["INT_ADD", "register:40f0:8", ["const:b75204:8", "const:4:8"]]
- 00b75204 ["CALL", null, ["callee:00c57bd0:8"]]
+ 00bf1c4c ["INT_ADD", "register:40f0:8", ["const:bf1c4c:8", "const:4:8"]]
+ 00bf1c4c ["CALL", null, ["callee:00c57bd0:8"]]
- 00b75204 bytes df970194
+ 00bf1c4c bytes e1970194
- 00b75218 ["INT_ADD", "register:40f0:8", ["const:b75218:8", "const:4:8"]]
- 00b75218 ["CALL", null, ["callee:00c57c50:8"]]
+ 00bf1c60 ["INT_ADD", "register:40f0:8", ["const:bf1c60:8", "const:4:8"]]
+ 00bf1c60 ["CALL", null, ["callee:00c57c50:8"]]
- 00b75218 bytes fa970194
+ 00bf1c60 bytes fc970194
~~~


<a id="compare-bd6229c653af6368ad0744088f8eeefb"></a>

### [`00b75338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md) → [`00bf1d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md) FUN_00bf1d80

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b752e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b752e4.md) [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00bf1d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d2c.md) [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md#insn-00b75378) · [`00b753a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md#insn-00b753a4) · [`00b753b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md#insn-00b753b4)
- 新版 [`00bf1dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dc0) · [`00bf1dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dec) · [`00bf1dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dfc)

~~~diff
- 00b75378 ["INT_ADD", "register:40f0:8", ["const:b75378:8", "const:4:8"]]
- 00b75378 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf1dc0 ["INT_ADD", "register:40f0:8", ["const:bf1dc0:8", "const:4:8"]]
+ 00bf1dc0 ["CALL", null, ["callee:00c57b40:8"]]
- 00b75378 bytes 5e970194
+ 00bf1dc0 bytes 60970194
- 00b753a4 ["INT_ADD", "register:40f0:8", ["const:b753a4:8", "const:4:8"]]
- 00b753a4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf1dec ["INT_ADD", "register:40f0:8", ["const:bf1dec:8", "const:4:8"]]
+ 00bf1dec ["CALL", null, ["callee:00c57a90:8"]]
- 00b753a4 bytes 27970194
+ 00bf1dec bytes 29970194
- 00b753b4 ["INT_ADD", "register:40f0:8", ["const:b753b4:8", "const:4:8"]]
- 00b753b4 ["CALL", null, ["callee:00c57c00:8"]]
+ 00bf1dfc ["INT_ADD", "register:40f0:8", ["const:bf1dfc:8", "const:4:8"]]
+ 00bf1dfc ["CALL", null, ["callee:00c57c00:8"]]
- 00b753b4 bytes 7f970194
+ 00bf1dfc bytes 81970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24950de1b38d24e93518436d6e8ef1d3"></a>

### [`00b75840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75840.md) → [`00bf2288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2288.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7588c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75840.md#insn-00b7588c)
- 新版 [`00bf22d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2288.md#insn-00bf22d4)

~~~diff
- 00b7588c ["INT_ADD", "register:40f0:8", ["const:b7588c:8", "const:4:8"]]
- 00b7588c ["CALL", null, ["callee:004428dc:8"]]
+ 00bf22d4 ["INT_ADD", "register:40f0:8", ["const:bf22d4:8", "const:4:8"]]
+ 00bf22d4 ["CALL", null, ["callee:004428dc:8"]]
- 00b7588c bytes 54a9e297
+ 00bf22d4 bytes 8241e197
~~~


<a id="compare-3d15d6325af5857f9df4be7cec5b30c8"></a>

### [`00b75ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75ed0.md) → [`00bf2918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2918.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75ed0.md#insn-00b75f30)
- 新版 [`00bf2978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2918.md#insn-00bf2978)

~~~diff
- 00b75f30 ["INT_ADD", "register:40f0:8", ["const:b75f30:8", "const:4:8"]]
- 00b75f30 ["CALL", null, ["callee:00c58050:8"]]
+ 00bf2978 ["INT_ADD", "register:40f0:8", ["const:bf2978:8", "const:4:8"]]
+ 00bf2978 ["CALL", null, ["callee:00c58050:8"]]
- 00b75f30 bytes b4950194
+ 00bf2978 bytes b6950194
~~~


<a id="compare-ffb2ce43818a5ac9859b26dc82adb102"></a>

### [`00b760f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b760f8.md) → [`00bf2b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b760f8.md#insn-00b76164) · [`00b76184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b760f8.md#insn-00b76184) · [`00b761a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b760f8.md#insn-00b761a4)
- 新版 [`00bf2bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bac) · [`00bf2bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bcc) · [`00bf2bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bec)

~~~diff
- 00b76164 ["INT_ADD", "register:40f0:8", ["const:b76164:8", "const:4:8"]]
- 00b76164 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf2bac ["INT_ADD", "register:40f0:8", ["const:bf2bac:8", "const:4:8"]]
+ 00bf2bac ["CALL", null, ["callee:00c57a90:8"]]
- 00b76164 bytes b7930194
+ 00bf2bac bytes b9930194
- 00b76184 ["INT_ADD", "register:40f0:8", ["const:b76184:8", "const:4:8"]]
- 00b76184 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf2bcc ["INT_ADD", "register:40f0:8", ["const:bf2bcc:8", "const:4:8"]]
+ 00bf2bcc ["CALL", null, ["callee:00c57b40:8"]]
- 00b76184 bytes db930194
+ 00bf2bcc bytes dd930194
- 00b761a4 ["INT_ADD", "register:40f0:8", ["const:b761a4:8", "const:4:8"]]
- 00b761a4 ["CALL", null, ["callee:006d7660:8"]]
+ 00bf2bec ["INT_ADD", "register:40f0:8", ["const:bf2bec:8", "const:4:8"]]
+ 00bf2bec ["CALL", null, ["callee:006d7660:8"]]
- 00b761a4 bytes c0ddec97
+ 00bf2bec bytes 9d92eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c3700bf0627d89e8b3ccc017f3350a"></a>

### [`00b761ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761ac.md) → [`00bf2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b761f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761ac.md#insn-00b761f0)
- 新版 [`00bf2c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md#insn-00bf2c38)

~~~diff
- 00b761f0 ["INT_ADD", "register:40f0:8", ["const:b761f0:8", "const:4:8"]]
- 00b761f0 ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf2c38 ["INT_ADD", "register:40f0:8", ["const:bf2c38:8", "const:4:8"]]
+ 00bf2c38 ["CALL", null, ["callee:00bf24b0:8"]]
- 00b761f0 bytes 1efeff97
+ 00bf2c38 bytes 1efeff97
~~~


<a id="compare-dbfe96776c0971e25e8c18ee0ebe5888"></a>

### [`00b76530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md) → [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md) FUN_00bf2f78

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00b76528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76528.md) [`00b768b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b768b0.md) [`00b77584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77584.md) [`00bb0124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0124.md) [`00bb0bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0bb8.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)
- 新版 呼出元 5件 [`00bf2f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f70.md) [`00bf32f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf32f8.md) [`00bf3fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3fcc.md) [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md#insn-00b76598) · [`00b765c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md#insn-00b765c0)
- 新版 [`00bf2fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md#insn-00bf2fe0) · [`00bf3008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md#insn-00bf3008)

~~~diff
- 00b76598 ["INT_ADD", "register:40f0:8", ["const:b76598:8", "const:4:8"]]
- 00b76598 ["CALL", null, ["callee:00c5dbf0:8"]]
+ 00bf2fe0 ["INT_ADD", "register:40f0:8", ["const:bf2fe0:8", "const:4:8"]]
+ 00bf2fe0 ["CALL", null, ["callee:00c5dbf0:8"]]
- 00b76598 bytes 9aaa0194
+ 00bf2fe0 bytes 04ab0194
- 00b765c0 ["INT_ADD", "register:40f0:8", ["const:b765c0:8", "const:4:8"]]
- 00b765c0 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf3008 ["INT_ADD", "register:40f0:8", ["const:bf3008:8", "const:4:8"]]
+ 00bf3008 ["CALL", null, ["callee:00c57b40:8"]]
- 00b765c0 bytes cc920194
+ 00bf3008 bytes ce920194
~~~


<a id="compare-e6387c4f012bcdd351efb06af25c17f0"></a>

### [`00b765f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b765f8.md) → [`00bf3040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b76694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf30dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b765f8.md#insn-00b76690)
- 新版 [`00bf30d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md#insn-00bf30d8)

~~~diff
- 00b76690 ["INT_ADD", "register:40f0:8", ["const:b76690:8", "const:4:8"]]
- 00b76690 ["CALL", null, ["callee:006d7660:8"]]
+ 00bf30d8 ["INT_ADD", "register:40f0:8", ["const:bf30d8:8", "const:4:8"]]
+ 00bf30d8 ["CALL", null, ["callee:006d7660:8"]]
- 00b76690 bytes 85dcec97
+ 00bf30d8 bytes 6291eb97
~~~


<a id="compare-8bc48ed9e0168b3bd9596c8e18f74145"></a>

### [`00b76904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76904.md) → [`00bf334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7695c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76904.md#insn-00b7695c) · [`00b76974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76904.md#insn-00b76974)
- 新版 [`00bf33a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md#insn-00bf33a4) · [`00bf33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md#insn-00bf33bc)

~~~diff
- 00b7695c ["INT_ADD", "register:40f0:8", ["const:b7695c:8", "const:4:8"]]
- 00b7695c ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf33a4 ["INT_ADD", "register:40f0:8", ["const:bf33a4:8", "const:4:8"]]
+ 00bf33a4 ["CALL", null, ["callee:00c57b40:8"]]
- 00b7695c bytes e5910194
+ 00bf33a4 bytes e7910194
- 00b76974 ["INT_ADD", "register:40f0:8", ["const:b76974:8", "const:4:8"]]
- 00b76974 ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf33bc ["INT_ADD", "register:40f0:8", ["const:bf33bc:8", "const:4:8"]]
+ 00bf33bc ["CALL", null, ["callee:00bf24b0:8"]]
- 00b76974 bytes 3dfcff97
+ 00bf33bc bytes 3dfcff97
~~~


<a id="compare-99ff47165ecf3b5582ff63770e743265"></a>

### [`00b76978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76978.md) → [`00bf33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddac0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a510.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76978.md#insn-00b76a18) · [`00b76a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76978.md#insn-00b76a38) · [`00b76a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76978.md#insn-00b76a5c)
- 新版 [`00bf3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf3460) · [`00bf3480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf3480) · [`00bf34a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf34a4)

~~~diff
- 00b76a18 ["INT_ADD", "register:40f0:8", ["const:b76a18:8", "const:4:8"]]
- 00b76a18 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf3460 ["INT_ADD", "register:40f0:8", ["const:bf3460:8", "const:4:8"]]
+ 00bf3460 ["CALL", null, ["callee:00c57a90:8"]]
- 00b76a18 bytes 8a910194
+ 00bf3460 bytes 8c910194
- 00b76a38 ["INT_ADD", "register:40f0:8", ["const:b76a38:8", "const:4:8"]]
- 00b76a38 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf3480 ["INT_ADD", "register:40f0:8", ["const:bf3480:8", "const:4:8"]]
+ 00bf3480 ["CALL", null, ["callee:00c57b40:8"]]
- 00b76a38 bytes ae910194
+ 00bf3480 bytes b0910194
- 00b76a5c ["INT_ADD", "register:40f0:8", ["const:b76a5c:8", "const:4:8"]]
- 00b76a5c ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf34a4 ["INT_ADD", "register:40f0:8", ["const:bf34a4:8", "const:4:8"]]
+ 00bf34a4 ["CALL", null, ["callee:00bf24b0:8"]]
- 00b76a5c bytes 03fcff97
+ 00bf34a4 bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fe5c21b31769b151b3e92d0e7637e6d"></a>

### [`00b76bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76bd0.md) → [`00bf3618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3618.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) [`00be1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md) [`00c5dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76bd0.md#insn-00b76bf4)
- 新版 [`00bf363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3618.md#insn-00bf363c)

~~~diff
- 00b76bf4 ["INT_ADD", "register:40f0:8", ["const:b76bf4:8", "const:4:8"]]
- 00b76bf4 ["CALL", null, ["callee:00c5dc00:8"]]
+ 00bf363c ["INT_ADD", "register:40f0:8", ["const:bf363c:8", "const:4:8"]]
+ 00bf363c ["CALL", null, ["callee:00c5dc00:8"]]
- 00b76bf4 bytes 07a90194
+ 00bf363c bytes 71a90194
~~~


<a id="compare-7ffaf4dfc0285309baf27296267eea52"></a>

### [`00b77534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77534.md) → [`00bf3f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3f7c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77534.md#insn-00b77578)
- 新版 [`00bf3fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3f7c.md#insn-00bf3fc0)

~~~diff
- 00b77578 ["INT_ADD", "register:40f0:8", ["const:b77578:8", "const:4:8"]]
- 00b77578 ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf3fc0 ["INT_ADD", "register:40f0:8", ["const:bf3fc0:8", "const:4:8"]]
+ 00bf3fc0 ["CALL", null, ["callee:00bf24b0:8"]]
- 00b77578 bytes 3cf9ff97
+ 00bf3fc0 bytes 3cf9ff97
~~~


<a id="compare-9179d9ccc295cce49499ccfcd936a41d"></a>

### [`00b77884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77884.md) → [`00bf42cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md) FUN_00bf42cc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b77758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77758.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)
- 新版 呼出元 1件 [`00bf41a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41a0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b778cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77884.md#insn-00b778cc) · [`00b778f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77884.md#insn-00b778f8)
- 新版 [`00bf4314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md#insn-00bf4314) · [`00bf4340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md#insn-00bf4340)

~~~diff
- 00b778cc ["INT_ADD", "register:40f0:8", ["const:b778cc:8", "const:4:8"]]
- 00b778cc ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf4314 ["INT_ADD", "register:40f0:8", ["const:bf4314:8", "const:4:8"]]
+ 00bf4314 ["CALL", null, ["callee:00c57b40:8"]]
- 00b778cc bytes 098e0194
+ 00bf4314 bytes 0b8e0194
- 00b778f8 ["INT_ADD", "register:40f0:8", ["const:b778f8:8", "const:4:8"]]
- 00b778f8 ["CALL", null, ["callee:00c5dbf0:8"]]
+ 00bf4340 ["INT_ADD", "register:40f0:8", ["const:bf4340:8", "const:4:8"]]
+ 00bf4340 ["CALL", null, ["callee:00c5dbf0:8"]]
- 00b778f8 bytes c2a50194
+ 00bf4340 bytes 2ca60194
~~~


<a id="compare-418f4c37f9c2f5bbbe9219b38883d43d"></a>

### [`00b77914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77914.md) → [`00bf435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77914.md#insn-00b77938) · [`00b77994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77914.md#insn-00b77994) · [`00b779bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77914.md#insn-00b779bc)
- 新版 [`00bf4380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf4380) · [`00bf43dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf43dc) · [`00bf4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf4404)

~~~diff
- 00b77938 ["INT_ADD", "register:40f0:8", ["const:b77938:8", "const:4:8"]]
- 00b77938 ["CALL", null, ["callee:00c5dc00:8"]]
+ 00bf4380 ["INT_ADD", "register:40f0:8", ["const:bf4380:8", "const:4:8"]]
+ 00bf4380 ["CALL", null, ["callee:00c5dc00:8"]]
- 00b77938 bytes b6a50194
+ 00bf4380 bytes 20a60194
- 00b77994 ["INT_ADD", "register:40f0:8", ["const:b77994:8", "const:4:8"]]
- 00b77994 ["CALL", null, ["callee:00c5dbf0:8"]]
+ 00bf43dc ["INT_ADD", "register:40f0:8", ["const:bf43dc:8", "const:4:8"]]
+ 00bf43dc ["CALL", null, ["callee:00c5dbf0:8"]]
- 00b77994 bytes 9ba50194
+ 00bf43dc bytes 05a60194
- 00b779bc ["INT_ADD", "register:40f0:8", ["const:b779bc:8", "const:4:8"]]
- 00b779bc ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf4404 ["INT_ADD", "register:40f0:8", ["const:bf4404:8", "const:4:8"]]
+ 00bf4404 ["CALL", null, ["callee:00c57b40:8"]]
- 00b779bc bytes cd8d0194
+ 00bf4404 bytes cf8d0194
~~~


<a id="compare-17052a5612f6543621cca45d2d5c8ae4"></a>

### [`00b779fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b779fc.md) → [`00bf4444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4444.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be0ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b779fc.md#insn-00b77a48)
- 新版 [`00bf4490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4444.md#insn-00bf4490)

~~~diff
- 00b77a48 ["INT_ADD", "register:40f0:8", ["const:b77a48:8", "const:4:8"]]
- 00b77a48 ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf4490 ["INT_ADD", "register:40f0:8", ["const:bf4490:8", "const:4:8"]]
+ 00bf4490 ["CALL", null, ["callee:00bf24b0:8"]]
- 00b77a48 bytes 08f8ff97
+ 00bf4490 bytes 08f8ff97
~~~


<a id="compare-aadb010405bfe8b513ce2ba51be437f1"></a>

### [`00b77a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77a4c.md) → [`00bf4494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77a4c.md#insn-00b77acc) · [`00b77afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77a4c.md#insn-00b77afc)
- 新版 [`00bf4514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md#insn-00bf4514) · [`00bf4544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md#insn-00bf4544)

~~~diff
- 00b77acc ["INT_ADD", "register:40f0:8", ["const:b77acc:8", "const:4:8"]]
- 00b77acc ["CALL", null, ["callee:00c5a4a0:8"]]
+ 00bf4514 ["INT_ADD", "register:40f0:8", ["const:bf4514:8", "const:4:8"]]
+ 00bf4514 ["CALL", null, ["callee:00c5a4a0:8"]]
- 00b77acc bytes e1970194
+ 00bf4514 bytes e3970194
- 00b77afc ["INT_ADD", "register:40f0:8", ["const:b77afc:8", "const:4:8"]]
- 00b77afc ["CALL", null, ["callee:00c57b40:8"]]
+ 00bf4544 ["INT_ADD", "register:40f0:8", ["const:bf4544:8", "const:4:8"]]
+ 00bf4544 ["CALL", null, ["callee:00c57b40:8"]]
- 00b77afc bytes 7d8d0194
+ 00bf4544 bytes 7f8d0194
~~~


<a id="compare-277de4cbc981b0d97adfbbc28db74785"></a>

### [`00b77b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77b50.md) → [`00bf4598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4598.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda40.md) · 呼出先 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)
- 新版 呼出元 1件 [`00c5a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a490.md) · 呼出先 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77b50.md#insn-00b77bd4)
- 新版 [`00bf461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4598.md#insn-00bf461c)

~~~diff
- 00b77bd4 ["INT_ADD", "register:40f0:8", ["const:b77bd4:8", "const:4:8"]]
- 00b77bd4 ["CALL", null, ["callee:00c5a4a0:8"]]
+ 00bf461c ["INT_ADD", "register:40f0:8", ["const:bf461c:8", "const:4:8"]]
+ 00bf461c ["CALL", null, ["callee:00c5a4a0:8"]]
- 00b77bd4 bytes 9f970194
+ 00bf461c bytes a1970194
~~~


<a id="compare-d36c11f8fb9e8a15859fc0d621f5b921"></a>

### [`00b77cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77cb0.md) → [`00bf46f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf46f8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77cb0.md#insn-00b77cfc)
- 新版 [`00bf4744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf46f8.md#insn-00bf4744)

~~~diff
- 00b77cfc ["INT_ADD", "register:40f0:8", ["const:b77cfc:8", "const:4:8"]]
- 00b77cfc ["CALL", null, ["callee:00bf24b0:8"]]
+ 00bf4744 ["INT_ADD", "register:40f0:8", ["const:bf4744:8", "const:4:8"]]
+ 00bf4744 ["CALL", null, ["callee:00bf24b0:8"]]
- 00b77cfc bytes 5bf7ff97
+ 00bf4744 bytes 5bf7ff97
~~~


<a id="compare-c6c3f28c15411f3cc2f13b1765bcd9a1"></a>

### [`00b79858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md) → [`00bf62a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b79880) · [`00b798c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b798c4) · [`00b798f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b798f0)
- 新版 [`00bf62c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf62c8) · [`00bf630c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf630c) · [`00bf6338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf6338)

~~~diff
- 00b79880 ["INT_ADD", "register:40f0:8", ["const:b79880:8", "const:4:8"]]
- 00b79880 ["CALL", null, ["callee:00bf7e30:8"]]
+ 00bf62c8 ["INT_ADD", "register:40f0:8", ["const:bf62c8:8", "const:4:8"]]
+ 00bf62c8 ["CALL", null, ["callee:00bf7e30:8"]]
- 00b79880 bytes da060094
+ 00bf62c8 bytes da060094
- 00b798c4 ["INT_ADD", "register:40f0:8", ["const:b798c4:8", "const:4:8"]]
- 00b798c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf630c ["INT_ADD", "register:40f0:8", ["const:bf630c:8", "const:4:8"]]
+ 00bf630c ["CALL", null, ["callee:00c57a90:8"]]
- 00b798c4 bytes df850194
+ 00bf630c bytes e1850194
- 00b798f0 ["INT_ADD", "register:40f0:8", ["const:b798f0:8", "const:4:8"]]
- 00b798f0 ["CALL", null, ["callee:00c57c00:8"]]
+ 00bf6338 ["INT_ADD", "register:40f0:8", ["const:bf6338:8", "const:4:8"]]
+ 00bf6338 ["CALL", null, ["callee:00c57c00:8"]]
- 00b798f0 bytes 30860194
+ 00bf6338 bytes 32860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94d95d35b37842d63e3036d66b237127"></a>

### [`00b7c1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1cc.md) → [`00bf8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c14.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1cc.md#insn-00b7c1e0)
- 新版 [`00bf8c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c14.md#insn-00bf8c28)

~~~diff
- 00b7c1e0 ["INT_ADD", "register:40f0:8", ["const:b7c1e0:8", "const:4:8"]]
- 00b7c1e0 ["CALL", null, ["callee:00c5dd80:8"]]
+ 00bf8c28 ["INT_ADD", "register:40f0:8", ["const:bf8c28:8", "const:4:8"]]
+ 00bf8c28 ["CALL", null, ["callee:00c5dd80:8"]]
- 00b7c1e0 bytes e8930194
+ 00bf8c28 bytes 56940194
~~~


<a id="compare-8808f7d84574b4fcb564a27909ec03f2"></a>

### [`00b7c314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c314.md) → [`00bf8d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8d5c.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c314.md#insn-00b7c330)
- 新版 [`00bf8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8d5c.md#insn-00bf8d78)

~~~diff
- 00b7c330 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7c330 ["INT_ADD", "register:40f0:8", ["const:b7c330:8", "const:4:8"]]
- 00b7c330 ["CALLIND", null, ["register:0:8"]]
+ 00bf8d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf8d78 ["INT_ADD", "register:40f0:8", ["const:bf8d78:8", "const:4:8"]]
+ 00bf8d78 ["CALLIND", null, ["register:0:8"]]
- 00b7c330 bytes 00013fd6
+ 00bf8d78 bytes 00013fd6
~~~


<a id="compare-eff88aa618e72bbd1bdcbd725684ce41"></a>

### [`00b7c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c374.md) → [`00bf8dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dbc.md) _ZNSt6__ndk118condition_variableD2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) · 呼出先 1件 [`00be0640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0640.md)
- 新版 呼出元 1件 [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) · 呼出先 1件 [`00c5d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c374.md#insn-00b7c380)
- 新版 [`00bf8dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dbc.md#insn-00bf8dc8)

~~~diff
- 00b7c380 ["INT_ADD", "register:40f0:8", ["const:b7c380:8", "const:4:8"]]
- 00b7c380 ["CALL", null, ["callee:00c5d220:8"]]
+ 00bf8dc8 ["INT_ADD", "register:40f0:8", ["const:bf8dc8:8", "const:4:8"]]
+ 00bf8dc8 ["CALL", null, ["callee:00c5d220:8"]]
- 00b7c380 bytes b0900194
+ 00bf8dc8 bytes 16910194
~~~


<a id="compare-c3f6b0741182facaf29543181368491b"></a>

### [`00b7c394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c394.md) → [`00bf8ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8ddc.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) · 呼出先 1件 [`00be0650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0650.md)
- 新版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) · 呼出先 1件 [`00c5d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c394.md#insn-00b7c3a0)
- 新版 [`00bf8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8ddc.md#insn-00bf8de8)

~~~diff
- 00b7c3a0 ["INT_ADD", "register:40f0:8", ["const:b7c3a0:8", "const:4:8"]]
- 00b7c3a0 ["CALL", null, ["callee:00c5d230:8"]]
+ 00bf8de8 ["INT_ADD", "register:40f0:8", ["const:bf8de8:8", "const:4:8"]]
+ 00bf8de8 ["CALL", null, ["callee:00c5d230:8"]]
- 00b7c3a0 bytes ac900194
+ 00bf8de8 bytes 12910194
~~~


<a id="compare-51bc210bb55d0b725e50112a1f29305c"></a>

### [`00b7c3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c3b4.md) → [`00bf8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dfc.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) · 呼出先 1件 [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)
- 新版 呼出元 1件 [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) · 呼出先 1件 [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c3b4.md#insn-00b7c3c0)
- 新版 [`00bf8e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dfc.md#insn-00bf8e08)

~~~diff
- 00b7c3c0 ["INT_ADD", "register:40f0:8", ["const:b7c3c0:8", "const:4:8"]]
- 00b7c3c0 ["CALL", null, ["callee:00c5ddc0:8"]]
+ 00bf8e08 ["INT_ADD", "register:40f0:8", ["const:bf8e08:8", "const:4:8"]]
+ 00bf8e08 ["CALL", null, ["callee:00c5ddc0:8"]]
- 00b7c3c0 bytes 80930194
+ 00bf8e08 bytes ee930194
~~~


<a id="compare-77f3729607928adc43b7e250a900b2ad"></a>

### [`00b7c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md) → [`00bf8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00be11f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c5ddf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4dc) · [`00b7c4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4e8) · [`00b7c4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4f4)
- 新版 [`00bf8f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f24) · [`00bf8f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f30) · [`00bf8f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f3c)

~~~diff
- 00b7c4dc ["INT_ADD", "register:40f0:8", ["const:b7c4dc:8", "const:4:8"]]
- 00b7c4dc ["CALL", null, ["callee:00c57d30:8"]]
+ 00bf8f24 ["INT_ADD", "register:40f0:8", ["const:bf8f24:8", "const:4:8"]]
+ 00bf8f24 ["CALL", null, ["callee:00c57d30:8"]]
- 00b7c4dc bytes 817b0194
+ 00bf8f24 bytes 837b0194
- 00b7c4e8 ["INT_ADD", "register:40f0:8", ["const:b7c4e8:8", "const:4:8"]]
- 00b7c4e8 ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00bf8f30 ["INT_ADD", "register:40f0:8", ["const:bf8f30:8", "const:4:8"]]
+ 00bf8f30 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00b7c4e8 bytes 42930194
+ 00bf8f30 bytes b0930194
- 00b7c4f4 ["INT_ADD", "register:40f0:8", ["const:b7c4f4:8", "const:4:8"]]
- 00b7c4f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf8f3c ["INT_ADD", "register:40f0:8", ["const:bf8f3c:8", "const:4:8"]]
+ 00bf8f3c ["CALL", null, ["callee:00c57a90:8"]]
- 00b7c4f4 bytes d37a0194
+ 00bf8f3c bytes d57a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

