# v16.0.0 → v16.0.1 · 要調査の変更候補 (38)

[一覧の目次](README.md)

<a id="compare-1a7301064fea289eb0744ca76dbf5702"></a>

### [`00b5db7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md) → [`00b5dfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dfa4.md) _ZN8firebase4Path11GetRelativeERKS0_S2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7e0.md) · 呼出先 6件 [`00b5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5bbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbe0.md) · 呼出先 6件 [`00b5d458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d458.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dbb0) · [`00b5dbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dbbc) · [`00b5dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dc78)
- 新版 `00b5dfd8`（命令位置の公開資料なし） · `00b5dfe4`（命令位置の公開資料なし） · `00b5e0a0`（命令位置の公開資料なし）

~~~diff
- 00b5dbb0 ["INT_ADD", "register:40f0:8", ["const:b5dbb0:8", "const:4:8"]]
- 00b5dbb0 ["CALL", null, ["callee:00c5bc00:8"]]
+ 00b5dfd8 ["INT_ADD", "register:40f0:8", ["const:b5dfd8:8", "const:4:8"]]
+ 00b5dfd8 ["CALL", null, ["callee:00c5bc00:8"]]
- 00b5dbb0 bytes 14f70394
+ 00b5dfd8 bytes 0af70394
- 00b5dbbc ["INT_ADD", "register:40f0:8", ["const:b5dbbc:8", "const:4:8"]]
- 00b5dbbc ["CALL", null, ["callee:00c5bc00:8"]]
+ 00b5dfe4 ["INT_ADD", "register:40f0:8", ["const:b5dfe4:8", "const:4:8"]]
+ 00b5dfe4 ["CALL", null, ["callee:00c5bc00:8"]]
- 00b5dbbc bytes 11f70394
+ 00b5dfe4 bytes 07f70394
- 00b5dc78 ["INT_ADD", "register:40f0:8", ["const:b5dc78:8", "const:4:8"]]
- 00b5dc78 ["CALL", null, ["callee:00c58050:8"]]
+ 00b5e0a0 ["INT_ADD", "register:40f0:8", ["const:b5e0a0:8", "const:4:8"]]
+ 00b5e0a0 ["CALL", null, ["callee:00c58050:8"]]
- 00b5dc78 bytes f6e70394
+ 00b5e0a0 bytes ece70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b5f005c15b6096be33dc4a41b183f68"></a>

### [`00b5e7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md) → [`00b5ebd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ebd4.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b880.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5bc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc80.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e7d8) · [`00b5e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e7f4) · [`00b5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e850)
- 新版 `00b5ec00`（命令位置の公開資料なし） · `00b5ec1c`（命令位置の公開資料なし） · `00b5ec78`（命令位置の公開資料なし）

~~~diff
- 00b5e7d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5e7d8 ["INT_ADD", "register:40f0:8", ["const:b5e7d8:8", "const:4:8"]]
- 00b5e7d8 ["CALLIND", null, ["register:0:8"]]
+ 00b5ec00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ec00 ["INT_ADD", "register:40f0:8", ["const:b5ec00:8", "const:4:8"]]
+ 00b5ec00 ["CALLIND", null, ["register:0:8"]]
- 00b5e7d8 bytes 00013fd6
+ 00b5ec00 bytes 00013fd6
- 00b5e7f4 ["INT_ADD", "register:40f0:8", ["const:b5e7f4:8", "const:4:8"]]
- 00b5e7f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b5ec1c ["INT_ADD", "register:40f0:8", ["const:b5ec1c:8", "const:4:8"]]
+ 00b5ec1c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b5e7f4 bytes afe40394
+ 00b5ec1c bytes a5e40394
- 00b5e850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5e850 ["INT_ADD", "register:40f0:8", ["const:b5e850:8", "const:4:8"]]
- 00b5e850 ["CALLIND", null, ["register:0:8"]]
+ 00b5ec78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ec78 ["INT_ADD", "register:40f0:8", ["const:b5ec78:8", "const:4:8"]]
+ 00b5ec78 ["CALLIND", null, ["register:0:8"]]
- 00b5e850 bytes 00013fd6
+ 00b5ec78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-555655a4f609da44f64d564743ff7df5"></a>

### [`00b5eaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eaa0.md) → [`00b5eec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5eec8.md) _ZN8firebase26ReferenceCountedFutureImplD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bcd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5eab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eaa0.md#insn-00b5eab0)
- 新版 `00b5eed8`（命令位置の公開資料なし）

~~~diff
- 00b5eab0 ["INT_ADD", "register:40f0:8", ["const:b5eab0:8", "const:4:8"]]
- 00b5eab0 ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5eed8 ["INT_ADD", "register:40f0:8", ["const:b5eed8:8", "const:4:8"]]
+ 00b5eed8 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5eab0 bytes 88f30394
+ 00b5eed8 bytes 7ef30394
~~~


<a id="compare-1b444dd5e8a9fabb37c17993a44b9d6c"></a>

### [`00b5f174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f174.md) → [`00b5f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f59c.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5aa80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa80.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae80.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f174.md#insn-00b5f194) · [`00b5f1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f174.md#insn-00b5f1e0)
- 新版 `00b5f5bc`（命令位置の公開資料なし） · `00b5f608`（命令位置の公開資料なし）

~~~diff
- 00b5f194 ["INT_ADD", "register:40f0:8", ["const:b5f194:8", "const:4:8"]]
- 00b5f194 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5f5bc ["INT_ADD", "register:40f0:8", ["const:b5f5bc:8", "const:4:8"]]
+ 00b5f5bc ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f194 bytes 1bed0394
+ 00b5f5bc bytes 11ed0394
- 00b5f1e0 ["INT_ADD", "register:40f0:8", ["const:b5f1e0:8", "const:4:8"]]
- 00b5f1e0 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b5f608 ["INT_ADD", "register:40f0:8", ["const:b5f608:8", "const:4:8"]]
+ 00b5f608 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b5f1e0 bytes 0ced0394
+ 00b5f608 bytes 02ed0394
~~~


<a id="compare-29557c6e63c488af4301eec3da0698ff"></a>

### [`00b5f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f590.md) → [`00b5f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9b8.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ac70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac70.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b070.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f590.md#insn-00b5f5a8) · [`00b5f5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f590.md#insn-00b5f5b4)
- 新版 `00b5f9d0`（命令位置の公開資料なし） · `00b5f9dc`（命令位置の公開資料なし）

~~~diff
- 00b5f5a8 ["INT_ADD", "register:40f0:8", ["const:b5f5a8:8", "const:4:8"]]
- 00b5f5a8 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5f9d0 ["INT_ADD", "register:40f0:8", ["const:b5f9d0:8", "const:4:8"]]
+ 00b5f9d0 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f5a8 bytes 16ec0394
+ 00b5f9d0 bytes 0cec0394
- 00b5f5b4 ["INT_ADD", "register:40f0:8", ["const:b5f5b4:8", "const:4:8"]]
- 00b5f5b4 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b5f9dc ["INT_ADD", "register:40f0:8", ["const:b5f9dc:8", "const:4:8"]]
+ 00b5f9dc ["CALL", null, ["callee:00c5aa10:8"]]
- 00b5f5b4 bytes 17ec0394
+ 00b5f9dc bytes 0dec0394
~~~


<a id="compare-d3442e35b5f7311f933f6bb68940a60b"></a>

### [`00b5f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f5d8.md) → [`00b5fa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa00.md) FUN_00b5fa00

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5f5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f5c8.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00b5f9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9f0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f5d8.md#insn-00b5f5e8) · [`00b5f600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f5d8.md#insn-00b5f600) · [`00b5f614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f5d8.md#insn-00b5f614)
- 新版 `00b5fa10`（命令位置の公開資料なし） · `00b5fa28`（命令位置の公開資料なし） · `00b5fa3c`（命令位置の公開資料なし）

~~~diff
- 00b5f5e8 ["INT_ADD", "register:40f0:8", ["const:b5f5e8:8", "const:4:8"]]
- 00b5f5e8 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5fa10 ["INT_ADD", "register:40f0:8", ["const:b5fa10:8", "const:4:8"]]
+ 00b5fa10 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f5e8 bytes 06ec0394
+ 00b5fa10 bytes fceb0394
- 00b5f600 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5f600 ["INT_ADD", "register:40f0:8", ["const:b5f600:8", "const:4:8"]]
- 00b5f600 ["CALLIND", null, ["register:0:8"]]
+ 00b5fa28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fa28 ["INT_ADD", "register:40f0:8", ["const:b5fa28:8", "const:4:8"]]
+ 00b5fa28 ["CALLIND", null, ["register:0:8"]]
- 00b5f600 bytes 00013fd6
+ 00b5fa28 bytes 00013fd6
- 00b5f614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5f614 ["INT_ADD", "register:40f0:8", ["const:b5f614:8", "const:4:8"]]
- 00b5f614 ["CALLIND", null, ["register:0:8"]]
+ 00b5fa3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fa3c ["INT_ADD", "register:40f0:8", ["const:b5fa3c:8", "const:4:8"]]
+ 00b5fa3c ["CALLIND", null, ["register:0:8"]]
- 00b5f614 bytes 00013fd6
+ 00b5fa3c bytes 00013fd6
~~~


<a id="compare-36f15cb895fe380198f3d8089c5efaf3"></a>

### [`00b5f7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f7f4.md) → [`00b5fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fc1c.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f7f4.md#insn-00b5f814) · [`00b5f820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f7f4.md#insn-00b5f820) · [`00b5f860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f7f4.md#insn-00b5f860)
- 新版 `00b5fc3c`（命令位置の公開資料なし） · `00b5fc48`（命令位置の公開資料なし） · `00b5fc88`（命令位置の公開資料なし）

~~~diff
- 00b5f814 ["INT_ADD", "register:40f0:8", ["const:b5f814:8", "const:4:8"]]
- 00b5f814 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5fc3c ["INT_ADD", "register:40f0:8", ["const:b5fc3c:8", "const:4:8"]]
+ 00b5fc3c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f814 bytes 7beb0394
+ 00b5fc3c bytes 71eb0394
- 00b5f820 ["INT_ADD", "register:40f0:8", ["const:b5f820:8", "const:4:8"]]
- 00b5f820 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5fc48 ["INT_ADD", "register:40f0:8", ["const:b5fc48:8", "const:4:8"]]
+ 00b5fc48 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f820 bytes 78eb0394
+ 00b5fc48 bytes 6eeb0394
- 00b5f860 ["INT_ADD", "register:40f0:8", ["const:b5f860:8", "const:4:8"]]
- 00b5f860 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b5fc88 ["INT_ADD", "register:40f0:8", ["const:b5fc88:8", "const:4:8"]]
+ 00b5fc88 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b5f860 bytes 6ceb0394
+ 00b5fc88 bytes 62eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef7e9881c3f4de52cf29cc6310fea6b"></a>

### [`00b6006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b6006c.md) → [`00b60494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60494.md) FUN_00b60494

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5fe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fe5c.md) · 呼出先 1件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md)
- 新版 呼出元 1件 [`00b60284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60284.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b600a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b6006c.md#insn-00b600a0)
- 新版 `00b604c8`（命令位置の公開資料なし）

~~~diff
- 00b600a0 ["INT_ADD", "register:40f0:8", ["const:b600a0:8", "const:4:8"]]
- 00b600a0 ["CALL", null, ["callee:00b6112c:8"]]
+ 00b604c8 ["INT_ADD", "register:40f0:8", ["const:b604c8:8", "const:4:8"]]
+ 00b604c8 ["CALL", null, ["callee:00b6112c:8"]]
- 00b600a0 bytes 19030094
+ 00b604c8 bytes 19030094
~~~


<a id="compare-bcd0024131abbbfba18b12f57f0df00d"></a>

### [`00b600a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600a4.md) → [`00b604cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b604cc.md) FUN_00b604cc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5fe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fe5c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b60284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60284.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b600e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600a4.md#insn-00b600e0)
- 新版 `00b60508`（命令位置の公開資料なし）

~~~diff
- 00b600e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b600e0 ["INT_ADD", "register:40f0:8", ["const:b600e0:8", "const:4:8"]]
- 00b600e0 ["CALLIND", null, ["register:0:8"]]
+ 00b60508 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60508 ["INT_ADD", "register:40f0:8", ["const:b60508:8", "const:4:8"]]
+ 00b60508 ["CALLIND", null, ["register:0:8"]]
- 00b600e0 bytes 00013fd6
+ 00b60508 bytes 00013fd6
~~~


<a id="compare-e6c51ae3e3fd19c12ae223f7b9b428f0"></a>

### [`00b600f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600f4.md) → [`00b6051c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b6051c.md) _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8e0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5bce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bce0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6010c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600f4.md#insn-00b6010c) · [`00b601a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600f4.md#insn-00b601a0)
- 新版 `00b60534`（命令位置の公開資料なし） · `00b605c8`（命令位置の公開資料なし）

~~~diff
- 00b6010c ["INT_ADD", "register:40f0:8", ["const:b6010c:8", "const:4:8"]]
- 00b6010c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b60534 ["INT_ADD", "register:40f0:8", ["const:b60534:8", "const:4:8"]]
+ 00b60534 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b6010c bytes 3de90394
+ 00b60534 bytes 33e90394
- 00b601a0 ["INT_ADD", "register:40f0:8", ["const:b601a0:8", "const:4:8"]]
- 00b601a0 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b605c8 ["INT_ADD", "register:40f0:8", ["const:b605c8:8", "const:4:8"]]
+ 00b605c8 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b601a0 bytes 1ce90394
+ 00b605c8 bytes 12e90394
~~~


<a id="compare-bdee3dcd1297dba0d4cd45050157d729"></a>

### [`00b601b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b601b4.md) → [`00b605dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b605dc.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b601cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b601b4.md#insn-00b601cc) · [`00b601d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b601b4.md#insn-00b601d8)
- 新版 `00b605f4`（命令位置の公開資料なし） · `00b60600`（命令位置の公開資料なし）

~~~diff
- 00b601cc ["INT_ADD", "register:40f0:8", ["const:b601cc:8", "const:4:8"]]
- 00b601cc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b605f4 ["INT_ADD", "register:40f0:8", ["const:b605f4:8", "const:4:8"]]
+ 00b605f4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b601cc bytes 0de90394
+ 00b605f4 bytes 03e90394
- 00b601d8 ["INT_ADD", "register:40f0:8", ["const:b601d8:8", "const:4:8"]]
- 00b601d8 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00b60600 ["INT_ADD", "register:40f0:8", ["const:b60600:8", "const:4:8"]]
+ 00b60600 ["CALL", null, ["callee:00c5aa10:8"]]
- 00b601d8 bytes 0ee90394
+ 00b60600 bytes 04e90394
~~~


<a id="compare-54f5a99397a93e600ee5ff687aaf2dcf"></a>

### [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) → [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) FUN_00b6112c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00b6006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b6006c.md) [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) [`00bb3be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3be8.md) [`00bc9068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9068.md) [`00bc922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 7件 [`00b60494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60494.md) [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) [`00bc9490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9490.md) [`00bc9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md#insn-00b60d0c)
- 新版 `00b61134`（命令位置の公開資料なし）

~~~diff
- 00b60d0c ["INT_ADD", "register:40f0:8", ["const:b60d0c:8", "const:4:8"]]
- 00b60d0c ["CALL", null, ["callee:00c5b140:8"]]
+ 00b61134 ["INT_ADD", "register:40f0:8", ["const:b61134:8", "const:4:8"]]
+ 00b61134 ["CALL", null, ["callee:00c5b140:8"]]
- 00b60d0c bytes 0de80394
+ 00b61134 bytes 03e80394
~~~


<a id="compare-3f079bec2f7a08e21ce358bcc6c6cd78"></a>

### [`00b61524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61524.md) → [`00b6194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6194c.md) _ZN8firebase17ModuleInitializer20InitializeLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b61554",
      "incomplete_value": true,
      "site": "00b6155c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b61558",
      "incomplete_value": false,
      "site": "00b6155c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61988",
      "incomplete_value": true,
      "site": "00b61990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6155c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61524.md#insn-00b6155c) · [`00b61568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61524.md#insn-00b61568) · [`00b61544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61524.md#insn-00b61544)
- 新版 `00b61984`（命令位置の公開資料なし） · `00b61990`（命令位置の公開資料なし） · `00b6196c`（命令位置の公開資料なし）

~~~diff
- 00b6155c ["INT_ADD", "register:40f0:8", ["const:b6155c:8", "const:4:8"]]
- 00b6155c ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b61984 ["INT_ADD", "register:40f0:8", ["const:b61984:8", "const:4:8"]]
+ 00b61984 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b6155c bytes c5e40394
+ 00b61984 bytes bbe40394
- 00b61568 ["INT_ADD", "register:40f0:8", ["const:b61568:8", "const:4:8"]]
- 00b61568 ["CALL", null, ["callee:00c5ae10:8"]]
+ 00b61990 ["INT_ADD", "register:40f0:8", ["const:b61990:8", "const:4:8"]]
+ 00b61990 ["CALL", null, ["callee:00c5ae10:8"]]
- 00b61568 bytes 2ae50394
+ 00b61990 bytes 20e50394
- 00b61544 ["INT_ADD", "register:40f0:8", ["const:b61544:8", "const:4:8"]]
- 00b61544 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b6196c ["INT_ADD", "register:40f0:8", ["const:b6196c:8", "const:4:8"]]
+ 00b6196c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b61544 bytes 2fe40394
+ 00b6196c bytes 25e40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f6f3ec3cb5b01ef7ce5d7e601a308ec"></a>

### [`00b62634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md) → [`00b62a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62a5c.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9b0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5bdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdb0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b62698) · [`00b626a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b626a4) · [`00b626d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b626d0)
- 新版 `00b62ac0`（命令位置の公開資料なし） · `00b62acc`（命令位置の公開資料なし） · `00b62af8`（命令位置の公開資料なし）

~~~diff
- 00b62698 ["INT_ADD", "register:40f0:8", ["const:b62698:8", "const:4:8"]]
- 00b62698 ["CALL", null, ["callee:00c5b140:8"]]
+ 00b62ac0 ["INT_ADD", "register:40f0:8", ["const:b62ac0:8", "const:4:8"]]
+ 00b62ac0 ["CALL", null, ["callee:00c5b140:8"]]
- 00b62698 bytes aae10394
+ 00b62ac0 bytes a0e10394
- 00b626a4 ["INT_ADD", "register:40f0:8", ["const:b626a4:8", "const:4:8"]]
- 00b626a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b62acc ["INT_ADD", "register:40f0:8", ["const:b62acc:8", "const:4:8"]]
+ 00b62acc ["CALL", null, ["callee:00c57e90:8"]]
- 00b626a4 bytes fbd40394
+ 00b62acc bytes f1d40394
- 00b626d0 ["INT_ADD", "register:40f0:8", ["const:b626d0:8", "const:4:8"]]
- 00b626d0 ["CALL", null, ["callee:00c58000:8"]]
+ 00b62af8 ["INT_ADD", "register:40f0:8", ["const:b62af8:8", "const:4:8"]]
+ 00b62af8 ["CALL", null, ["callee:00c58000:8"]]
- 00b626d0 bytes 4cd50394
+ 00b62af8 bytes 42d50394
~~~


<a id="compare-cd6979bd1baf1951137f5ec27e29c504"></a>

### [`00b6271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md) → [`00b62b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b44.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b980.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b980.md)
- 新版 呼出元 1件 [`00c5bd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd80.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62738) · [`00b62744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62744) · [`00b62754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62754)
- 新版 `00b62b60`（命令位置の公開資料なし） · `00b62b6c`（命令位置の公開資料なし） · `00b62b7c`（命令位置の公開資料なし）

~~~diff
- 00b62738 ["INT_ADD", "register:40f0:8", ["const:b62738:8", "const:4:8"]]
- 00b62738 ["CALL", null, ["callee:00c5bd80:8"]]
+ 00b62b60 ["INT_ADD", "register:40f0:8", ["const:b62b60:8", "const:4:8"]]
+ 00b62b60 ["CALL", null, ["callee:00c5bd80:8"]]
- 00b62738 bytes 92e40394
+ 00b62b60 bytes 88e40394
- 00b62744 ["INT_ADD", "register:40f0:8", ["const:b62744:8", "const:4:8"]]
- 00b62744 ["CALL", null, ["callee:00c5bd80:8"]]
+ 00b62b6c ["INT_ADD", "register:40f0:8", ["const:b62b6c:8", "const:4:8"]]
+ 00b62b6c ["CALL", null, ["callee:00c5bd80:8"]]
- 00b62744 bytes 8fe40394
+ 00b62b6c bytes 85e40394
- 00b62754 ["INT_ADD", "register:40f0:8", ["const:b62754:8", "const:4:8"]]
- 00b62754 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b62b7c ["INT_ADD", "register:40f0:8", ["const:b62b7c:8", "const:4:8"]]
+ 00b62b7c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b62754 bytes d7d40394
+ 00b62b7c bytes cdd40394
~~~


<a id="compare-d2714f19af0a5f9208f881e025db210c"></a>

### [`00b64ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md) → [`00b6531c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6531c.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)
- 新版 呼出元 1件 [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)

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
    "new": {
      "definition_site": "00b65330",
      "incomplete_value": true,
      "site": "00b65338",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b64f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64f10) · [`00b64f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64f1c) · [`00b64f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64f2c)
- 新版 `00b65338`（命令位置の公開資料なし） · `00b65344`（命令位置の公開資料なし） · `00b65354`（命令位置の公開資料なし）

~~~diff
- 00b64f10 ["INT_ADD", "register:40f0:8", ["const:b64f10:8", "const:4:8"]]
- 00b64f10 ["CALL", null, ["callee:00c5be20:8"]]
+ 00b65338 ["INT_ADD", "register:40f0:8", ["const:b65338:8", "const:4:8"]]
+ 00b65338 ["CALL", null, ["callee:00c5be20:8"]]
- 00b64f10 bytes c4da0394
+ 00b65338 bytes bada0394
- 00b64f1c ["INT_ADD", "register:40f0:8", ["const:b64f1c:8", "const:4:8"]]
- 00b64f1c ["CALL", null, ["callee:00c5be20:8"]]
+ 00b65344 ["INT_ADD", "register:40f0:8", ["const:b65344:8", "const:4:8"]]
+ 00b65344 ["CALL", null, ["callee:00c5be20:8"]]
- 00b64f1c bytes c1da0394
+ 00b65344 bytes b7da0394
- 00b64f2c ["INT_ADD", "register:40f0:8", ["const:b64f2c:8", "const:4:8"]]
- 00b64f2c ["CALL", null, ["callee:00c5a830:8"]]
+ 00b65354 ["INT_ADD", "register:40f0:8", ["const:b65354:8", "const:4:8"]]
+ 00b65354 ["CALL", null, ["callee:00c5a830:8"]]
- 00b64f2c bytes 41d50394
+ 00b65354 bytes 37d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5308299023675e62712db79e17475729"></a>

### [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) → [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3c0.md) · 呼出先 7件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5adc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adc0.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 1件 [`00c5b7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7c0.md) · 呼出先 7件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1c0.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b667e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b667e4) · [`00b667f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b667f0) · [`00b66804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b66804)
- 新版 `00b66c0c`（命令位置の公開資料なし） · `00b66c18`（命令位置の公開資料なし） · `00b66c2c`（命令位置の公開資料なし）

~~~diff
- 00b667e4 ["INT_ADD", "register:40f0:8", ["const:b667e4:8", "const:4:8"]]
- 00b667e4 ["CALL", null, ["callee:00c5b760:8"]]
+ 00b66c0c ["INT_ADD", "register:40f0:8", ["const:b66c0c:8", "const:4:8"]]
+ 00b66c0c ["CALL", null, ["callee:00c5b760:8"]]
- 00b667e4 bytes dfd20394
+ 00b66c0c bytes d5d20394
- 00b667f0 ["INT_ADD", "register:40f0:8", ["const:b667f0:8", "const:4:8"]]
- 00b667f0 ["CALL", null, ["callee:00c5b3c0:8"]]
+ 00b66c18 ["INT_ADD", "register:40f0:8", ["const:b66c18:8", "const:4:8"]]
+ 00b66c18 ["CALL", null, ["callee:00c5b3c0:8"]]
- 00b667f0 bytes f4d10394
+ 00b66c18 bytes ead10394
- 00b66804 ["INT_ADD", "register:40f0:8", ["const:b66804:8", "const:4:8"]]
- 00b66804 ["CALL", null, ["callee:00c5b1c0:8"]]
+ 00b66c2c ["INT_ADD", "register:40f0:8", ["const:b66c2c:8", "const:4:8"]]
+ 00b66c2c ["CALL", null, ["callee:00c5b1c0:8"]]
- 00b66804 bytes 6fd10394
+ 00b66c2c bytes 65d10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e8f859223150a9d6e548c1312f7709a"></a>

### [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) → [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b67e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e2c) · [`00b67e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e44) · [`00b67e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e64)
- 新版 `00b68254`（命令位置の公開資料なし） · `00b6826c`（命令位置の公開資料なし） · `00b6828c`（命令位置の公開資料なし）

~~~diff
- 00b67e2c ["INT_ADD", "register:40f0:8", ["const:b67e2c:8", "const:4:8"]]
- 00b67e2c ["CALL", null, ["callee:00b66454:8"]]
+ 00b68254 ["INT_ADD", "register:40f0:8", ["const:b68254:8", "const:4:8"]]
+ 00b68254 ["CALL", null, ["callee:00b66454:8"]]
- 00b67e2c bytes 80f8ff97
+ 00b68254 bytes 80f8ff97
- 00b67e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67e44 ["INT_ADD", "register:40f0:8", ["const:b67e44:8", "const:4:8"]]
- 00b67e44 ["CALLIND", null, ["register:0:8"]]
+ 00b6826c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6826c ["INT_ADD", "register:40f0:8", ["const:b6826c:8", "const:4:8"]]
+ 00b6826c ["CALLIND", null, ["register:0:8"]]
- 00b67e44 bytes 00013fd6
+ 00b6826c bytes 00013fd6
- 00b67e64 ["INT_ADD", "register:40f0:8", ["const:b67e64:8", "const:4:8"]]
- 00b67e64 ["CALL", null, ["callee:00b6112c:8"]]
+ 00b6828c ["INT_ADD", "register:40f0:8", ["const:b6828c:8", "const:4:8"]]
+ 00b6828c ["CALL", null, ["callee:00b6112c:8"]]
- 00b67e64 bytes a8e3ff97
+ 00b6828c bytes a8e3ff97
~~~


<a id="compare-5f10a5547bd1542696cfabe18fe26d48"></a>

### [`00b6d4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md) → [`00b6d900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d900.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6c0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6c0.md)
- 新版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bac0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md#insn-00b6d4f4) · [`00b6d500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md#insn-00b6d500)
- 新版 `00b6d91c`（命令位置の公開資料なし） · `00b6d928`（命令位置の公開資料なし）

~~~diff
- 00b6d4f4 ["INT_ADD", "register:40f0:8", ["const:b6d4f4:8", "const:4:8"]]
- 00b6d4f4 ["CALL", null, ["callee:00c5bac0:8"]]
+ 00b6d91c ["INT_ADD", "register:40f0:8", ["const:b6d91c:8", "const:4:8"]]
+ 00b6d91c ["CALL", null, ["callee:00c5bac0:8"]]
- 00b6d4f4 bytes 73b80394
+ 00b6d91c bytes 69b80394
- 00b6d500 ["INT_ADD", "register:40f0:8", ["const:b6d500:8", "const:4:8"]]
- 00b6d500 ["CALL", null, ["callee:00c5bac0:8"]]
+ 00b6d928 ["INT_ADD", "register:40f0:8", ["const:b6d928:8", "const:4:8"]]
+ 00b6d928 ["CALL", null, ["callee:00c5bac0:8"]]
- 00b6d500 bytes 70b80394
+ 00b6d928 bytes 66b80394
~~~


<a id="compare-af515dce328b7f9eacc74f56548da295"></a>

### [`00b6d518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md) → [`00b6d940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d940.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6d0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6d0.md)
- 新版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bad0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md#insn-00b6d534) · [`00b6d540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md#insn-00b6d540)
- 新版 `00b6d95c`（命令位置の公開資料なし） · `00b6d968`（命令位置の公開資料なし）

~~~diff
- 00b6d534 ["INT_ADD", "register:40f0:8", ["const:b6d534:8", "const:4:8"]]
- 00b6d534 ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b6d95c ["INT_ADD", "register:40f0:8", ["const:b6d95c:8", "const:4:8"]]
+ 00b6d95c ["CALL", null, ["callee:00c5bad0:8"]]
- 00b6d534 bytes 67b80394
+ 00b6d95c bytes 5db80394
- 00b6d540 ["INT_ADD", "register:40f0:8", ["const:b6d540:8", "const:4:8"]]
- 00b6d540 ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b6d968 ["INT_ADD", "register:40f0:8", ["const:b6d968:8", "const:4:8"]]
+ 00b6d968 ["CALL", null, ["callee:00c5bad0:8"]]
- 00b6d540 bytes 64b80394
+ 00b6d968 bytes 5ab80394
~~~


<a id="compare-507226d1eaf77e537d5a447cdbb2cd86"></a>

### [`00b6d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d558.md) → [`00b6d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d980.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b610.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b610.md)
- 新版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d558.md#insn-00b6d574) · [`00b6d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d558.md#insn-00b6d580)
- 新版 `00b6d99c`（命令位置の公開資料なし） · `00b6d9a8`（命令位置の公開資料なし）

~~~diff
- 00b6d574 ["INT_ADD", "register:40f0:8", ["const:b6d574:8", "const:4:8"]]
- 00b6d574 ["CALL", null, ["callee:00c5ba10:8"]]
+ 00b6d99c ["INT_ADD", "register:40f0:8", ["const:b6d99c:8", "const:4:8"]]
+ 00b6d99c ["CALL", null, ["callee:00c5ba10:8"]]
- 00b6d574 bytes 27b80394
+ 00b6d99c bytes 1db80394
- 00b6d580 ["INT_ADD", "register:40f0:8", ["const:b6d580:8", "const:4:8"]]
- 00b6d580 ["CALL", null, ["callee:00c5ba10:8"]]
+ 00b6d9a8 ["INT_ADD", "register:40f0:8", ["const:b6d9a8:8", "const:4:8"]]
+ 00b6d9a8 ["CALL", null, ["callee:00c5ba10:8"]]
- 00b6d580 bytes 24b80394
+ 00b6d9a8 bytes 1ab80394
~~~


<a id="compare-d83b286305edf1a9f415a0f0d84b6ce4"></a>

### [`00b6d6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md) → [`00b6dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dad4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6c8) · [`00b6d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6d4) · [`00b6d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6e4)
- 新版 `00b6daf0`（命令位置の公開資料なし） · `00b6dafc`（命令位置の公開資料なし） · `00b6db0c`（命令位置の公開資料なし）

~~~diff
- 00b6d6c8 ["INT_ADD", "register:40f0:8", ["const:b6d6c8:8", "const:4:8"]]
- 00b6d6c8 ["CALL", null, ["callee:00c5ba80:8"]]
+ 00b6daf0 ["INT_ADD", "register:40f0:8", ["const:b6daf0:8", "const:4:8"]]
+ 00b6daf0 ["CALL", null, ["callee:00c5ba80:8"]]
- 00b6d6c8 bytes eeb70394
+ 00b6daf0 bytes e4b70394
- 00b6d6d4 ["INT_ADD", "register:40f0:8", ["const:b6d6d4:8", "const:4:8"]]
- 00b6d6d4 ["CALL", null, ["callee:00c5ba80:8"]]
+ 00b6dafc ["INT_ADD", "register:40f0:8", ["const:b6dafc:8", "const:4:8"]]
+ 00b6dafc ["CALL", null, ["callee:00c5ba80:8"]]
- 00b6d6d4 bytes ebb70394
+ 00b6dafc bytes e1b70394
- 00b6d6e4 ["INT_ADD", "register:40f0:8", ["const:b6d6e4:8", "const:4:8"]]
- 00b6d6e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6db0c ["INT_ADD", "register:40f0:8", ["const:b6db0c:8", "const:4:8"]]
+ 00b6db0c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d6e4 bytes f3a80394
+ 00b6db0c bytes e9a80394
~~~


<a id="compare-b2a86ea8e136f69c2f73690e6935ba36"></a>

### [`00b6d6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md) → [`00b6db24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db24.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md)
- 新版 呼出元 1件 [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d718) · [`00b6d724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d724) · [`00b6d734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d734)
- 新版 `00b6db40`（命令位置の公開資料なし） · `00b6db4c`（命令位置の公開資料なし） · `00b6db5c`（命令位置の公開資料なし）

~~~diff
- 00b6d718 ["INT_ADD", "register:40f0:8", ["const:b6d718:8", "const:4:8"]]
- 00b6d718 ["CALL", null, ["callee:00c5ba50:8"]]
+ 00b6db40 ["INT_ADD", "register:40f0:8", ["const:b6db40:8", "const:4:8"]]
+ 00b6db40 ["CALL", null, ["callee:00c5ba50:8"]]
- 00b6d718 bytes ceb70394
+ 00b6db40 bytes c4b70394
- 00b6d724 ["INT_ADD", "register:40f0:8", ["const:b6d724:8", "const:4:8"]]
- 00b6d724 ["CALL", null, ["callee:00c5ba50:8"]]
+ 00b6db4c ["INT_ADD", "register:40f0:8", ["const:b6db4c:8", "const:4:8"]]
+ 00b6db4c ["CALL", null, ["callee:00c5ba50:8"]]
- 00b6d724 bytes cbb70394
+ 00b6db4c bytes c1b70394
- 00b6d734 ["INT_ADD", "register:40f0:8", ["const:b6d734:8", "const:4:8"]]
- 00b6d734 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6db5c ["INT_ADD", "register:40f0:8", ["const:b6db5c:8", "const:4:8"]]
+ 00b6db5c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d734 bytes dfa80394
+ 00b6db5c bytes d5a80394
~~~


<a id="compare-ae6283c98fb516748fb558f5a55577b4"></a>

### [`00b6e20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md) → [`00b6e634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e634.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb40.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5bf40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf40.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6e280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md#insn-00b6e280) · [`00b6e2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e20c.md#insn-00b6e2a4)
- 新版 `00b6e6a8`（命令位置の公開資料なし） · `00b6e6cc`（命令位置の公開資料なし）

~~~diff
- 00b6e280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e280 ["INT_ADD", "register:40f0:8", ["const:b6e280:8", "const:4:8"]]
- 00b6e280 ["CALLIND", null, ["register:0:8"]]
+ 00b6e6a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e6a8 ["INT_ADD", "register:40f0:8", ["const:b6e6a8:8", "const:4:8"]]
+ 00b6e6a8 ["CALLIND", null, ["register:0:8"]]
- 00b6e280 bytes 00013fd6
+ 00b6e6a8 bytes 00013fd6
- 00b6e2a4 ["INT_ADD", "register:40f0:8", ["const:b6e2a4:8", "const:4:8"]]
- 00b6e2a4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b6e6cc ["INT_ADD", "register:40f0:8", ["const:b6e6cc:8", "const:4:8"]]
+ 00b6e6cc ["CALL", null, ["callee:00c57ee0:8"]]
- 00b6e2a4 bytes 0fa60394
+ 00b6e6cc bytes 05a60394
~~~


<a id="compare-1534e55c9905829a90a9a7b961903e8a"></a>

### [`00b6eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md) → [`00b6efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6efcc.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ebd0) · [`00b6ec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ec24) · [`00b6ec4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ec4c)
- 新版 `00b6eff8`（命令位置の公開資料なし） · `00b6f04c`（命令位置の公開資料なし） · `00b6f074`（命令位置の公開資料なし）

~~~diff
- 00b6ebd0 ["INT_ADD", "register:40f0:8", ["const:b6ebd0:8", "const:4:8"]]
- 00b6ebd0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b6eff8 ["INT_ADD", "register:40f0:8", ["const:b6eff8:8", "const:4:8"]]
+ 00b6eff8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00b6ebd0 bytes 04a40394
+ 00b6eff8 bytes faa30394
- 00b6ec24 ["INT_ADD", "register:40f0:8", ["const:b6ec24:8", "const:4:8"]]
- 00b6ec24 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b6f04c ["INT_ADD", "register:40f0:8", ["const:b6f04c:8", "const:4:8"]]
+ 00b6f04c ["CALL", null, ["callee:00c57e90:8"]]
- 00b6ec24 bytes 9ba30394
+ 00b6f04c bytes 91a30394
- 00b6ec4c ["INT_ADD", "register:40f0:8", ["const:b6ec4c:8", "const:4:8"]]
- 00b6ec4c ["CALL", null, ["callee:00c58000:8"]]
+ 00b6f074 ["INT_ADD", "register:40f0:8", ["const:b6f074:8", "const:4:8"]]
+ 00b6f074 ["CALL", null, ["callee:00c58000:8"]]
- 00b6ec4c bytes eda30394
+ 00b6f074 bytes e3a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2daca719a5c2fff3f0a4889fde6a234"></a>

### [`00b6eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md) → [`00b6f2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md) _ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md#insn-00b6eef8) · [`00b6ef0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md#insn-00b6ef0c) · [`00b6ef1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md#insn-00b6ef1c)
- 新版 `00b6f320`（命令位置の公開資料なし） · `00b6f334`（命令位置の公開資料なし） · `00b6f344`（命令位置の公開資料なし）

~~~diff
- 00b6eef8 ["INT_ADD", "register:40f0:8", ["const:b6eef8:8", "const:4:8"]]
- 00b6eef8 ["CALL", null, ["callee:0054a614:8"]]
+ 00b6f320 ["INT_ADD", "register:40f0:8", ["const:b6f320:8", "const:4:8"]]
+ 00b6f320 ["CALL", null, ["callee:0054a614:8"]]
- 00b6eef8 bytes b76de797
+ 00b6f320 bytes bd6ce797
- 00b6ef0c ["INT_ADD", "register:40f0:8", ["const:b6ef0c:8", "const:4:8"]]
- 00b6ef0c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b6f334 ["INT_ADD", "register:40f0:8", ["const:b6f334:8", "const:4:8"]]
+ 00b6f334 ["CALL", null, ["callee:00c57e90:8"]]
- 00b6ef0c bytes e1a20394
+ 00b6f334 bytes d7a20394
- 00b6ef1c ["INT_ADD", "register:40f0:8", ["const:b6ef1c:8", "const:4:8"]]
- 00b6ef1c ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00b6f344 ["INT_ADD", "register:40f0:8", ["const:b6f344:8", "const:4:8"]]
+ 00b6f344 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00b6ef1c bytes a5b00394
+ 00b6f344 bytes 9bb00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f643a841553537f8d094363331e2dff1"></a>

### [`00b6ef90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ef90.md) → [`00b6f3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f3b8.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c640.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca40.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ef90.md#insn-00b6f078) · [`00b6f0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ef90.md#insn-00b6f0c4) · [`00b6f0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ef90.md#insn-00b6f0ec)
- 新版 `00b6f4a0`（命令位置の公開資料なし） · `00b6f4ec`（命令位置の公開資料なし） · `00b6f514`（命令位置の公開資料なし）

~~~diff
- 00b6f078 ["INT_ADD", "register:40f0:8", ["const:b6f078:8", "const:4:8"]]
- 00b6f078 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6f4a0 ["INT_ADD", "register:40f0:8", ["const:b6f4a0:8", "const:4:8"]]
+ 00b6f4a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6f078 bytes c2a20394
+ 00b6f4a0 bytes b8a20394
- 00b6f0c4 ["INT_ADD", "register:40f0:8", ["const:b6f0c4:8", "const:4:8"]]
- 00b6f0c4 ["CALL", null, ["callee:00c5a8e0:8"]]
+ 00b6f4ec ["INT_ADD", "register:40f0:8", ["const:b6f4ec:8", "const:4:8"]]
+ 00b6f4ec ["CALL", null, ["callee:00c5a8e0:8"]]
- 00b6f0c4 bytes 07ad0394
+ 00b6f4ec bytes fdac0394
- 00b6f0ec ["INT_ADD", "register:40f0:8", ["const:b6f0ec:8", "const:4:8"]]
- 00b6f0ec ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00b6f514 ["INT_ADD", "register:40f0:8", ["const:b6f514:8", "const:4:8"]]
+ 00b6f514 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00b6f0ec bytes 31b00394
+ 00b6f514 bytes 27b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51e442fd1ab81d1cf7f61f37562b2b3b"></a>

### [`00b76d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76d68.md) → [`00b77190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b77190.md) _ZN11flatbuffers6Parser11ParseStringERNS_5ValueEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0d0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4d0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76d68.md#insn-00b76e08) · [`00b76e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76d68.md#insn-00b76e28) · [`00b76e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76d68.md#insn-00b76e3c)
- 新版 `00b77230`（命令位置の公開資料なし） · `00b77250`（命令位置の公開資料なし） · `00b77264`（命令位置の公開資料なし）

~~~diff
- 00b76e08 ["INT_ADD", "register:40f0:8", ["const:b76e08:8", "const:4:8"]]
- 00b76e08 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b77230 ["INT_ADD", "register:40f0:8", ["const:b77230:8", "const:4:8"]]
+ 00b77230 ["CALL", null, ["callee:00c57e90:8"]]
- 00b76e08 bytes 22830394
+ 00b77230 bytes 18830394
- 00b76e28 ["INT_ADD", "register:40f0:8", ["const:b76e28:8", "const:4:8"]]
- 00b76e28 ["CALL", null, ["callee:00c58000:8"]]
+ 00b77250 ["INT_ADD", "register:40f0:8", ["const:b77250:8", "const:4:8"]]
+ 00b77250 ["CALL", null, ["callee:00c58000:8"]]
- 00b76e28 bytes 76830394
+ 00b77250 bytes 6c830394
- 00b76e3c ["INT_ADD", "register:40f0:8", ["const:b76e3c:8", "const:4:8"]]
- 00b76e3c ["CALL", null, ["callee:00c5c750:8"]]
+ 00b77264 ["INT_ADD", "register:40f0:8", ["const:b77264:8", "const:4:8"]]
+ 00b77264 ["CALL", null, ["callee:00c5c750:8"]]
- 00b76e3c bytes 45950394
+ 00b77264 bytes 3b950394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd4dcbeab65f7291d93b39f988eec8c"></a>

### [`00b770c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b770c0.md) → [`00b774e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b774e8.md) _ZN11flatbuffers6Parser10ParseCommaEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b770e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b770c0.md#insn-00b770e0)
- 新版 `00b77508`（命令位置の公開資料なし）

~~~diff
- 00b770e0 ["INT_ADD", "register:40f0:8", ["const:b770e0:8", "const:4:8"]]
- 00b770e0 ["CALL", null, ["callee:00c5c750:8"]]
+ 00b77508 ["INT_ADD", "register:40f0:8", ["const:b77508:8", "const:4:8"]]
+ 00b77508 ["CALL", null, ["callee:00c5c750:8"]]
- 00b770e0 bytes 9c940394
+ 00b77508 bytes 92940394
~~~


<a id="compare-bb25a4461ac850a1e1801ddd00f8da0b"></a>

### [`00b7e95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e95c.md) → [`00b7ed84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7ed84.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementImjEET0_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be70.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c270.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e95c.md#insn-00b7e9b4) · [`00b7ea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e95c.md#insn-00b7ea10)
- 新版 `00b7eddc`（命令位置の公開資料なし） · `00b7ee38`（命令位置の公開資料なし）

~~~diff
- 00b7e9b4 ["INT_ADD", "register:40f0:8", ["const:b7e9b4:8", "const:4:8"]]
- 00b7e9b4 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7eddc ["INT_ADD", "register:40f0:8", ["const:b7eddc:8", "const:4:8"]]
+ 00b7eddc ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7e9b4 bytes fb740394
+ 00b7eddc bytes f1740394
- 00b7ea10 ["INT_ADD", "register:40f0:8", ["const:b7ea10:8", "const:4:8"]]
- 00b7ea10 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7ee38 ["INT_ADD", "register:40f0:8", ["const:b7ee38:8", "const:4:8"]]
+ 00b7ee38 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7ea10 bytes e4740394
+ 00b7ee38 bytes da740394
~~~


<a id="compare-53a3dd06a50ff1954efc3b7e9c421350"></a>

### [`00b7ec3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ec3c.md) → [`00b7f064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f064.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIfjEET0_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be30.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c230.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ec3c.md#insn-00b7ec94) · [`00b7ecf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ec3c.md#insn-00b7ecf0)
- 新版 `00b7f0bc`（命令位置の公開資料なし） · `00b7f118`（命令位置の公開資料なし）

~~~diff
- 00b7ec94 ["INT_ADD", "register:40f0:8", ["const:b7ec94:8", "const:4:8"]]
- 00b7ec94 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f0bc ["INT_ADD", "register:40f0:8", ["const:b7f0bc:8", "const:4:8"]]
+ 00b7f0bc ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7ec94 bytes 43740394
+ 00b7f0bc bytes 39740394
- 00b7ecf0 ["INT_ADD", "register:40f0:8", ["const:b7ecf0:8", "const:4:8"]]
- 00b7ecf0 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f118 ["INT_ADD", "register:40f0:8", ["const:b7f118:8", "const:4:8"]]
+ 00b7f118 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7ecf0 bytes 2c740394
+ 00b7f118 bytes 22740394
~~~


<a id="compare-4f8785462cc80982b36e145e8fd010dc"></a>

### [`00b7ef28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ef28.md) → [`00b7f350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f350.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIdjEET0_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be20.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c220.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ef28.md#insn-00b7ef80) · [`00b7efdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ef28.md#insn-00b7efdc)
- 新版 `00b7f3a8`（命令位置の公開資料なし） · `00b7f404`（命令位置の公開資料なし）

~~~diff
- 00b7ef80 ["INT_ADD", "register:40f0:8", ["const:b7ef80:8", "const:4:8"]]
- 00b7ef80 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
+ 00b7f3a8 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7ef80 bytes 88730394
+ 00b7f3a8 bytes 7e730394
- 00b7efdc ["INT_ADD", "register:40f0:8", ["const:b7efdc:8", "const:4:8"]]
- 00b7efdc ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f404 ["INT_ADD", "register:40f0:8", ["const:b7f404:8", "const:4:8"]]
+ 00b7f404 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7efdc bytes 71730394
+ 00b7f404 bytes 67730394
~~~


<a id="compare-c3817859e177757bbb64033488de23ea"></a>

### [`00b7f00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f00c.md) → [`00b7f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f434.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_8Offset64IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c020.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be70.md)
- 新版 呼出元 1件 [`00c5c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c420.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f00c.md#insn-00b7f06c) · [`00b7f0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f00c.md#insn-00b7f0c8) · [`00b7f0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f00c.md#insn-00b7f0ec)
- 新版 `00b7f494`（命令位置の公開資料なし） · `00b7f4f0`（命令位置の公開資料なし） · `00b7f514`（命令位置の公開資料なし）

~~~diff
- 00b7f06c ["INT_ADD", "register:40f0:8", ["const:b7f06c:8", "const:4:8"]]
- 00b7f06c ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f494 ["INT_ADD", "register:40f0:8", ["const:b7f494:8", "const:4:8"]]
+ 00b7f494 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f06c bytes 4d730394
+ 00b7f494 bytes 43730394
- 00b7f0c8 ["INT_ADD", "register:40f0:8", ["const:b7f0c8:8", "const:4:8"]]
- 00b7f0c8 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f4f0 ["INT_ADD", "register:40f0:8", ["const:b7f4f0:8", "const:4:8"]]
+ 00b7f4f0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f0c8 bytes 6a730394
+ 00b7f4f0 bytes 60730394
- 00b7f0ec ["INT_ADD", "register:40f0:8", ["const:b7f0ec:8", "const:4:8"]]
- 00b7f0ec ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f514 ["INT_ADD", "register:40f0:8", ["const:b7f514:8", "const:4:8"]]
+ 00b7f514 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f0ec bytes 2d730394
+ 00b7f514 bytes 23730394
~~~


<a id="compare-f48887b7602bbf99007b4cbd1c7c01c0"></a>

### [`00b7f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f13c.md) → [`00b7f564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f564.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c010.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c410.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f13c.md#insn-00b7f19c) · [`00b7f1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f13c.md#insn-00b7f1f8) · [`00b7f21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f13c.md#insn-00b7f21c)
- 新版 `00b7f5c4`（命令位置の公開資料なし） · `00b7f620`（命令位置の公開資料なし） · `00b7f644`（命令位置の公開資料なし）

~~~diff
- 00b7f19c ["INT_ADD", "register:40f0:8", ["const:b7f19c:8", "const:4:8"]]
- 00b7f19c ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f5c4 ["INT_ADD", "register:40f0:8", ["const:b7f5c4:8", "const:4:8"]]
+ 00b7f5c4 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f19c bytes 01730394
+ 00b7f5c4 bytes f7720394
- 00b7f1f8 ["INT_ADD", "register:40f0:8", ["const:b7f1f8:8", "const:4:8"]]
- 00b7f1f8 ["CALL", null, ["callee:00c5c250:8"]]
+ 00b7f620 ["INT_ADD", "register:40f0:8", ["const:b7f620:8", "const:4:8"]]
+ 00b7f620 ["CALL", null, ["callee:00c5c250:8"]]
- 00b7f1f8 bytes 16730394
+ 00b7f620 bytes 0c730394
- 00b7f21c ["INT_ADD", "register:40f0:8", ["const:b7f21c:8", "const:4:8"]]
- 00b7f21c ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f644 ["INT_ADD", "register:40f0:8", ["const:b7f644:8", "const:4:8"]]
+ 00b7f644 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f21c bytes e1720394
+ 00b7f644 bytes d7720394
~~~


<a id="compare-c5f1d5718442e9be28d177707e3da577"></a>

### [`00b7f26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f26c.md) → [`00b7f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f694.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE8EndTableEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf40.md) · 呼出先 4件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be40.md)
- 新版 呼出元 1件 [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f26c.md#insn-00b7f294) · [`00b7f2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f26c.md#insn-00b7f2d8) · [`00b7f2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f26c.md#insn-00b7f2fc)
- 新版 `00b7f6bc`（命令位置の公開資料なし） · `00b7f700`（命令位置の公開資料なし） · `00b7f724`（命令位置の公開資料なし）

~~~diff
- 00b7f294 ["INT_ADD", "register:40f0:8", ["const:b7f294:8", "const:4:8"]]
- 00b7f294 ["CALL", null, ["callee:00c5c240:8"]]
+ 00b7f6bc ["INT_ADD", "register:40f0:8", ["const:b7f6bc:8", "const:4:8"]]
+ 00b7f6bc ["CALL", null, ["callee:00c5c240:8"]]
- 00b7f294 bytes eb720394
+ 00b7f6bc bytes e1720394
- 00b7f2d8 ["INT_ADD", "register:40f0:8", ["const:b7f2d8:8", "const:4:8"]]
- 00b7f2d8 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7f700 ["INT_ADD", "register:40f0:8", ["const:b7f700:8", "const:4:8"]]
+ 00b7f700 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f2d8 bytes b2720394
+ 00b7f700 bytes a8720394
- 00b7f2fc ["INT_ADD", "register:40f0:8", ["const:b7f2fc:8", "const:4:8"]]
- 00b7f2fc ["CALL", null, ["callee:00c58090:8"]]
+ 00b7f724 ["INT_ADD", "register:40f0:8", ["const:b7f724:8", "const:4:8"]]
+ 00b7f724 ["CALL", null, ["callee:00c58090:8"]]
- 00b7f2fc bytes 65620394
+ 00b7f724 bytes 5b620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd4801346ad865fef406be0f8d7544e"></a>

### [`00b7f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f8d4.md) → [`00b7fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7fcfc.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be80.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c280.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f8d4.md#insn-00b7f940) · [`00b7f9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f8d4.md#insn-00b7f9c4)
- 新版 `00b7fd68`（命令位置の公開資料なし） · `00b7fdec`（命令位置の公開資料なし）

~~~diff
- 00b7f940 ["INT_ADD", "register:40f0:8", ["const:b7f940:8", "const:4:8"]]
- 00b7f940 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7fd68 ["INT_ADD", "register:40f0:8", ["const:b7fd68:8", "const:4:8"]]
+ 00b7fd68 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f940 bytes 18710394
+ 00b7fd68 bytes 0e710394
- 00b7f9c4 ["INT_ADD", "register:40f0:8", ["const:b7f9c4:8", "const:4:8"]]
- 00b7f9c4 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7fdec ["INT_ADD", "register:40f0:8", ["const:b7fdec:8", "const:4:8"]]
+ 00b7fdec ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7f9c4 bytes f7700394
+ 00b7fdec bytes ed700394
~~~


<a id="compare-1dd284c8eb4cccdcc8008bacb63fc842"></a>

### [`00b7fc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fc50.md) → [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) FUN_00b80078

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7fc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fc50.md) · 呼出先 2件 [`00b7fc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fc50.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) · 呼出先 2件 [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fc50.md#insn-00b7fcc0) · [`00b7fd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fc50.md#insn-00b7fd78)
- 新版 `00b800e8`（命令位置の公開資料なし） · `00b801a0`（命令位置の公開資料なし）

~~~diff
- 00b7fcc0 ["INT_ADD", "register:40f0:8", ["const:b7fcc0:8", "const:4:8"]]
- 00b7fcc0 ["CALL", null, ["local:b0:8"]]
+ 00b800e8 ["INT_ADD", "register:40f0:8", ["const:b800e8:8", "const:4:8"]]
+ 00b800e8 ["CALL", null, ["local:b0:8"]]
- 00b7fcc0 bytes e4ffff97
+ 00b800e8 bytes e4ffff97
- 00b7fd78 ["INT_ADD", "register:40f0:8", ["const:b7fd78:8", "const:4:8"]]
- 00b7fd78 ["CALL", null, ["callee:00c58050:8"]]
+ 00b801a0 ["INT_ADD", "register:40f0:8", ["const:b801a0:8", "const:4:8"]]
+ 00b801a0 ["CALL", null, ["callee:00c58050:8"]]
- 00b7fd78 bytes b65f0394
+ 00b801a0 bytes ac5f0394
~~~


<a id="compare-70227711d6452a7f2ff10d9110a2b49b"></a>

### [`00b7fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fdf0.md) → [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) FUN_00b80218

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fdf0.md) · 呼出先 2件 [`00b7fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fdf0.md) [`00baaae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baaae4.md)
- 新版 呼出元 2件 [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) · 呼出先 2件 [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) [`00baaf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baaf0c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7fe54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fdf0.md#insn-00b7fe54) · [`00b7fef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7fdf0.md#insn-00b7fef0)
- 新版 `00b8027c`（命令位置の公開資料なし） · `00b80318`（命令位置の公開資料なし）

~~~diff
- 00b7fe54 ["INT_ADD", "register:40f0:8", ["const:b7fe54:8", "const:4:8"]]
- 00b7fe54 ["CALL", null, ["local:b0:8"]]
+ 00b8027c ["INT_ADD", "register:40f0:8", ["const:b8027c:8", "const:4:8"]]
+ 00b8027c ["CALL", null, ["local:b0:8"]]
- 00b7fe54 bytes e7ffff97
+ 00b8027c bytes e7ffff97
- 00b7fef0 ["INT_ADD", "register:40f0:8", ["const:b7fef0:8", "const:4:8"]]
- 00b7fef0 ["CALL", null, ["callee:00baaf0c:8"]]
+ 00b80318 ["INT_ADD", "register:40f0:8", ["const:b80318:8", "const:4:8"]]
+ 00b80318 ["CALL", null, ["callee:00baaf0c:8"]]
- 00b7fef0 bytes fdaa0094
+ 00b80318 bytes fdaa0094
~~~


<a id="compare-497b1b75153d2b481133b0e38ecaac7d"></a>

### [`00b8039c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b8039c.md) → [`00b807c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b807c4.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bba0.md) · 呼出先 2件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc30.md)
- 新版 呼出元 1件 [`00c5bfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfa0.md) · 呼出先 2件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b803e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b8039c.md#insn-00b803e8) · [`00b8040c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b8039c.md#insn-00b8040c) · [`00b80440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b8039c.md#insn-00b80440)
- 新版 `00b80810`（命令位置の公開資料なし） · `00b80834`（命令位置の公開資料なし） · `00b80868`（命令位置の公開資料なし）

~~~diff
- 00b803e8 ["INT_ADD", "register:40f0:8", ["const:b803e8:8", "const:4:8"]]
- 00b803e8 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00b80810 ["INT_ADD", "register:40f0:8", ["const:b80810:8", "const:4:8"]]
+ 00b80810 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00b803e8 bytes 326a0394
+ 00b80810 bytes 286a0394
- 00b8040c ["INT_ADD", "register:40f0:8", ["const:b8040c:8", "const:4:8"]]
- 00b8040c ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00b80834 ["INT_ADD", "register:40f0:8", ["const:b80834:8", "const:4:8"]]
+ 00b80834 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00b8040c bytes 296a0394
+ 00b80834 bytes 1f6a0394
- 00b80440 ["INT_ADD", "register:40f0:8", ["const:b80440:8", "const:4:8"]]
- 00b80440 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00b80868 ["INT_ADD", "register:40f0:8", ["const:b80868:8", "const:4:8"]]
+ 00b80868 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00b80440 bytes 1c6a0394
+ 00b80868 bytes 126a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5212e7a3b8f1c4dfa609cbad17bc0ae1"></a>

### [`00b807c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md) → [`00b80be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80be8.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb10.md) · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1b0.md) [`00c5c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2a0.md) [`00c5c3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3c0.md) [`00c5c4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4e0.md)
- 新版 呼出元 1件 [`00c5bf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf10.md) · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md) [`00c5c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6a0.md) [`00c5c7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7c0.md) [`00c5c8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b807f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b807f8) · [`00b8081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b8081c) · [`00b80838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b80838)
- 新版 `00b80c20`（命令位置の公開資料なし） · `00b80c44`（命令位置の公開資料なし） · `00b80c60`（命令位置の公開資料なし）

~~~diff
- 00b807f8 ["INT_ADD", "register:40f0:8", ["const:b807f8:8", "const:4:8"]]
- 00b807f8 ["CALL", null, ["callee:00c5c5b0:8"]]
+ 00b80c20 ["INT_ADD", "register:40f0:8", ["const:b80c20:8", "const:4:8"]]
+ 00b80c20 ["CALL", null, ["callee:00c5c5b0:8"]]
- 00b807f8 bytes 6e6e0394
+ 00b80c20 bytes 646e0394
- 00b8081c ["INT_ADD", "register:40f0:8", ["const:b8081c:8", "const:4:8"]]
- 00b8081c ["CALL", null, ["callee:00c5c6a0:8"]]
+ 00b80c44 ["INT_ADD", "register:40f0:8", ["const:b80c44:8", "const:4:8"]]
+ 00b80c44 ["CALL", null, ["callee:00c5c6a0:8"]]
- 00b8081c bytes a16e0394
+ 00b80c44 bytes 976e0394
- 00b80838 ["INT_ADD", "register:40f0:8", ["const:b80838:8", "const:4:8"]]
- 00b80838 ["CALL", null, ["callee:00c5c7c0:8"]]
+ 00b80c60 ["INT_ADD", "register:40f0:8", ["const:b80c60:8", "const:4:8"]]
+ 00b80c60 ["CALL", null, ["callee:00c5c7c0:8"]]
- 00b80838 bytes e26e0394
+ 00b80c60 bytes d86e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa79a99d46582d7119b41592b812f0ec"></a>

### [`00b80880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80880.md) → [`00b80ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80ca8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE12CreateVectorIhNS_6OffsetENS_6VectorEEET0_IJT1_IJT_EEEEPKS7_m

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be90.md) · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c290.md) · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b808ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80880.md#insn-00b808ec) · [`00b80958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80880.md#insn-00b80958) · [`00b8097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80880.md#insn-00b8097c)
- 新版 `00b80d14`（命令位置の公開資料なし） · `00b80d80`（命令位置の公開資料なし） · `00b80da4`（命令位置の公開資料なし）

~~~diff
- 00b808ec ["INT_ADD", "register:40f0:8", ["const:b808ec:8", "const:4:8"]]
- 00b808ec ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b80d14 ["INT_ADD", "register:40f0:8", ["const:b80d14:8", "const:4:8"]]
+ 00b80d14 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b808ec bytes 2d6d0394
+ 00b80d14 bytes 236d0394
- 00b80958 ["INT_ADD", "register:40f0:8", ["const:b80958:8", "const:4:8"]]
- 00b80958 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b80d80 ["INT_ADD", "register:40f0:8", ["const:b80d80:8", "const:4:8"]]
+ 00b80d80 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b80958 bytes 126d0394
+ 00b80d80 bytes 086d0394
- 00b8097c ["INT_ADD", "register:40f0:8", ["const:b8097c:8", "const:4:8"]]
- 00b8097c ["CALL", null, ["callee:00c58000:8"]]
+ 00b80da4 ["INT_ADD", "register:40f0:8", ["const:b80da4:8", "const:4:8"]]
+ 00b80da4 ["CALL", null, ["callee:00c58000:8"]]
- 00b8097c bytes a15c0394
+ 00b80da4 bytes 975c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-957ffea2fdfb657ef936accfa28566c4"></a>

### [`00b82354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82354.md) → [`00b8277c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8277c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6e0.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cae0.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b823e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82354.md#insn-00b823e0) · [`00b82414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82354.md#insn-00b82414) · [`00b82424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82354.md#insn-00b82424)
- 新版 `00b82808`（命令位置の公開資料なし） · `00b8283c`（命令位置の公開資料なし） · `00b8284c`（命令位置の公開資料なし）

~~~diff
- 00b823e0 ["INT_ADD", "register:40f0:8", ["const:b823e0:8", "const:4:8"]]
- 00b823e0 ["CALL", null, ["callee:00c5a8e0:8"]]
+ 00b82808 ["INT_ADD", "register:40f0:8", ["const:b82808:8", "const:4:8"]]
+ 00b82808 ["CALL", null, ["callee:00c5a8e0:8"]]
- 00b823e0 bytes 40600394
+ 00b82808 bytes 36600394
- 00b82414 ["INT_ADD", "register:40f0:8", ["const:b82414:8", "const:4:8"]]
- 00b82414 ["CALL", null, ["callee:00c57f40:8"]]
+ 00b8283c ["INT_ADD", "register:40f0:8", ["const:b8283c:8", "const:4:8"]]
+ 00b8283c ["CALL", null, ["callee:00c57f40:8"]]
- 00b82414 bytes cb550394
+ 00b8283c bytes c1550394
- 00b82424 ["INT_ADD", "register:40f0:8", ["const:b82424:8", "const:4:8"]]
- 00b82424 ["CALL", null, ["callee:00c58090:8"]]
+ 00b8284c ["INT_ADD", "register:40f0:8", ["const:b8284c:8", "const:4:8"]]
+ 00b8284c ["CALL", null, ["callee:00c58090:8"]]
- 00b82424 bytes 1b560394
+ 00b8284c bytes 11560394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-101a201dd804c2ed09ffb77ee64c2a66"></a>

### [`00b92a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a54.md) → [`00b92e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e7c.md) _ZNK11flatbuffers7EnumVal19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b92a54.md#insn-00b92a60)
- 新版 `00b92e88`（命令位置の公開資料なし）

~~~diff
- 00b92a60 ["INT_ADD", "register:40f0:8", ["const:b92a60:8", "const:4:8"]]
- 00b92a60 ["CALL", null, ["callee:00b92e98:8"]]
+ 00b92e88 ["INT_ADD", "register:40f0:8", ["const:b92e88:8", "const:4:8"]]
+ 00b92e88 ["CALL", null, ["callee:00b92e98:8"]]
- 00b92a60 bytes 04000094
+ 00b92e88 bytes 04000094
~~~


<a id="compare-6379b9aaede84ae983102905f47f550a"></a>

### [`00b930dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b930dc.md) → [`00b93504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93504.md) _ZN10reflection13CreateEnumValERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEElNS4_INS_4TypeEEENS4_INS0_6VectorIS6_j

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb90.md) · 呼出先 7件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be60.md) [`00c5bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf40.md) [`00c5bf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf50.md) [`00c5bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf70.md)
- 新版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf90.md) · 呼出先 7件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c260.md) [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) [`00c5c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c350.md) [`00c5c370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b930dc.md#insn-00b93128) · [`00b9314c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b930dc.md#insn-00b9314c) · [`00b93198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b930dc.md#insn-00b93198)
- 新版 `00b93550`（命令位置の公開資料なし） · `00b93574`（命令位置の公開資料なし） · `00b935c0`（命令位置の公開資料なし）

~~~diff
- 00b93128 ["INT_ADD", "register:40f0:8", ["const:b93128:8", "const:4:8"]]
- 00b93128 ["CALL", null, ["callee:00c5c260:8"]]
+ 00b93550 ["INT_ADD", "register:40f0:8", ["const:b93550:8", "const:4:8"]]
+ 00b93550 ["CALL", null, ["callee:00c5c260:8"]]
- 00b93128 bytes 4e230394
+ 00b93550 bytes 44230394
- 00b9314c ["INT_ADD", "register:40f0:8", ["const:b9314c:8", "const:4:8"]]
- 00b9314c ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b93574 ["INT_ADD", "register:40f0:8", ["const:b93574:8", "const:4:8"]]
+ 00b93574 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b9314c bytes 15230394
+ 00b93574 bytes 0b230394
- 00b93198 ["INT_ADD", "register:40f0:8", ["const:b93198:8", "const:4:8"]]
- 00b93198 ["CALL", null, ["callee:00c5c3f0:8"]]
+ 00b935c0 ["INT_ADD", "register:40f0:8", ["const:b935c0:8", "const:4:8"]]
+ 00b935c0 ["CALL", null, ["callee:00c5c3f0:8"]]
- 00b93198 bytes 96230394
+ 00b935c0 bytes 8c230394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-919b3d9805dcaded33a2a06d83538536"></a>

### [`00b931f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b931f4.md) → [`00b9361c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b9361c.md) _ZN10reflection10CreateTypeERN11flatbuffers21FlatBufferBuilderImplILb0EEENS_8BaseTypeES4_itjj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb50.md) · 呼出先 6件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdd0.md) [`00c5be10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be10.md) [`00c5be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be40.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf50.md) · 呼出先 6件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1d0.md) [`00c5c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c210.md) [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b931f4.md#insn-00b93244) · [`00b93268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b931f4.md#insn-00b93268) · [`00b932cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b931f4.md#insn-00b932cc)
- 新版 `00b9366c`（命令位置の公開資料なし） · `00b93690`（命令位置の公開資料なし） · `00b936f4`（命令位置の公開資料なし）

~~~diff
- 00b93244 ["INT_ADD", "register:40f0:8", ["const:b93244:8", "const:4:8"]]
- 00b93244 ["CALL", null, ["callee:00c5c250:8"]]
+ 00b9366c ["INT_ADD", "register:40f0:8", ["const:b9366c:8", "const:4:8"]]
+ 00b9366c ["CALL", null, ["callee:00c5c250:8"]]
- 00b93244 bytes 03230394
+ 00b9366c bytes f9220394
- 00b93268 ["INT_ADD", "register:40f0:8", ["const:b93268:8", "const:4:8"]]
- 00b93268 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b93690 ["INT_ADD", "register:40f0:8", ["const:b93690:8", "const:4:8"]]
+ 00b93690 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b93268 bytes ce220394
+ 00b93690 bytes c4220394
- 00b932cc ["INT_ADD", "register:40f0:8", ["const:b932cc:8", "const:4:8"]]
- 00b932cc ["CALL", null, ["callee:00c5c250:8"]]
+ 00b936f4 ["INT_ADD", "register:40f0:8", ["const:b936f4:8", "const:4:8"]]
+ 00b936f4 ["CALL", null, ["callee:00c5c250:8"]]
- 00b932cc bytes e1220394
+ 00b936f4 bytes d7220394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ae1894468e8aed1b67c0896e423939"></a>

### [`00b94918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94918.md) → [`00b94d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b94/00b94d40.md) FUN_00b94d40

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b9363c.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b93a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93a64.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b949e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94918.md#insn-00b949e0) · [`00b94a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94918.md#insn-00b94a00) · [`00b94a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b94/00b94918.md#insn-00b94a68)
- 新版 `00b94e08`（命令位置の公開資料なし） · `00b94e28`（命令位置の公開資料なし） · `00b94e90`（命令位置の公開資料なし）

~~~diff
- 00b949e0 ["INT_ADD", "register:40f0:8", ["const:b949e0:8", "const:4:8"]]
- 00b949e0 ["CALL", null, ["callee:00c5cf60:8"]]
+ 00b94e08 ["INT_ADD", "register:40f0:8", ["const:b94e08:8", "const:4:8"]]
+ 00b94e08 ["CALL", null, ["callee:00c5cf60:8"]]
- 00b949e0 bytes 60200394
+ 00b94e08 bytes 56200394
- 00b94a00 ["INT_ADD", "register:40f0:8", ["const:b94a00:8", "const:4:8"]]
- 00b94a00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b94e28 ["INT_ADD", "register:40f0:8", ["const:b94e28:8", "const:4:8"]]
+ 00b94e28 ["CALL", null, ["callee:00c57e90:8"]]
- 00b94a00 bytes 240c0394
+ 00b94e28 bytes 1a0c0394
- 00b94a68 ["INT_ADD", "register:40f0:8", ["const:b94a68:8", "const:4:8"]]
- 00b94a68 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b94e90 ["INT_ADD", "register:40f0:8", ["const:b94e90:8", "const:4:8"]]
+ 00b94e90 ["CALL", null, ["callee:00c57e90:8"]]
- 00b94a68 bytes 0a0c0394
+ 00b94e90 bytes 000c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c6d9fd570c989aa3207521d2ca7dc94"></a>

### [`00b95720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md) → [`00b95b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95b48.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) · 呼出先 2件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)
- 新版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) · 呼出先 2件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md#insn-00b9578c) · [`00b957b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md#insn-00b957b0)
- 新版 `00b95bb4`（命令位置の公開資料なし） · `00b95bd8`（命令位置の公開資料なし）

~~~diff
- 00b9578c ["INT_ADD", "register:40f0:8", ["const:b9578c:8", "const:4:8"]]
- 00b9578c ["CALL", null, ["callee:00c5a8e0:8"]]
+ 00b95bb4 ["INT_ADD", "register:40f0:8", ["const:b95bb4:8", "const:4:8"]]
+ 00b95bb4 ["CALL", null, ["callee:00c5a8e0:8"]]
- 00b9578c bytes 55130394
+ 00b95bb4 bytes 4b130394
- 00b957b0 ["INT_ADD", "register:40f0:8", ["const:b957b0:8", "const:4:8"]]
- 00b957b0 ["CALL", null, ["callee:00c58090:8"]]
+ 00b95bd8 ["INT_ADD", "register:40f0:8", ["const:b95bd8:8", "const:4:8"]]
+ 00b95bd8 ["CALL", null, ["callee:00c58090:8"]]
- 00b957b0 bytes 38090394
+ 00b95bd8 bytes 2e090394
~~~


<a id="compare-d633ffc7eca2196f2d0d83412faf60d4"></a>

### [`00b9881c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9881c.md) → [`00b98c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c44.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b9881c.md#insn-00b98838)
- 新版 `00b98c60`（命令位置の公開資料なし）

~~~diff
- 00b98838 ["INT_ADD", "register:40f0:8", ["const:b98838:8", "const:4:8"]]
- 00b98838 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00b98c60 ["INT_ADD", "register:40f0:8", ["const:b98c60:8", "const:4:8"]]
+ 00b98c60 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00b98838 bytes 2a110394
+ 00b98c60 bytes 20110394
~~~


<a id="compare-23aecf6413417c17685fa65654fbcfb2"></a>

### [`00b98c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md) → [`00b990c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b990c4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md#insn-00b98d1c) · [`00b98d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98c9c.md#insn-00b98d30)
- 新版 `00b99144`（命令位置の公開資料なし） · `00b99158`（命令位置の公開資料なし）

~~~diff
- 00b98d1c ["INT_ADD", "register:40f0:8", ["const:b98d1c:8", "const:4:8"]]
- 00b98d1c ["CALL", null, ["callee:00c58000:8"]]
+ 00b99144 ["INT_ADD", "register:40f0:8", ["const:b99144:8", "const:4:8"]]
+ 00b99144 ["CALL", null, ["callee:00c58000:8"]]
- 00b98d1c bytes b9fb0294
+ 00b99144 bytes affb0294
- 00b98d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b98d30 ["INT_ADD", "register:40f0:8", ["const:b98d30:8", "const:4:8"]]
- 00b98d30 ["CALLIND", null, ["register:0:8"]]
+ 00b99158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99158 ["INT_ADD", "register:40f0:8", ["const:b99158:8", "const:4:8"]]
+ 00b99158 ["CALLIND", null, ["register:0:8"]]
- 00b98d30 bytes 00013fd6
+ 00b99158 bytes 00013fd6
~~~


<a id="compare-4fa29f4ddd9fc5c7d7d2926a4145a8a0"></a>

### [`00b98db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98db4.md) → [`00b991dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b991dc.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98db4.md#insn-00b98dcc)
- 新版 `00b991f4`（命令位置の公開資料なし）

~~~diff
- 00b98dcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b98dcc ["INT_ADD", "register:40f0:8", ["const:b98dcc:8", "const:4:8"]]
- 00b98dcc ["CALLIND", null, ["register:0:8"]]
+ 00b991f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b991f4 ["INT_ADD", "register:40f0:8", ["const:b991f4:8", "const:4:8"]]
+ 00b991f4 ["CALLIND", null, ["register:0:8"]]
- 00b98dcc bytes 00013fd6
+ 00b991f4 bytes 00013fd6
~~~


<a id="compare-04e5b189bd1be975f7e2523d87aee9ba"></a>

### [`00b98e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md) → [`00b9928c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9928c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md#insn-00b98ed8) · [`00b98ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98e64.md#insn-00b98ef0)
- 新版 `00b99300`（命令位置の公開資料なし） · `00b99318`（命令位置の公開資料なし）

~~~diff
- 00b98ed8 ["INT_ADD", "register:40f0:8", ["const:b98ed8:8", "const:4:8"]]
- 00b98ed8 ["CALL", null, ["callee:00c58000:8"]]
+ 00b99300 ["INT_ADD", "register:40f0:8", ["const:b99300:8", "const:4:8"]]
+ 00b99300 ["CALL", null, ["callee:00c58000:8"]]
- 00b98ed8 bytes 4afb0294
+ 00b99300 bytes 40fb0294
- 00b98ef0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b98ef0 ["INT_ADD", "register:40f0:8", ["const:b98ef0:8", "const:4:8"]]
- 00b98ef0 ["CALLIND", null, ["register:0:8"]]
+ 00b99318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99318 ["INT_ADD", "register:40f0:8", ["const:b99318:8", "const:4:8"]]
+ 00b99318 ["CALLIND", null, ["register:0:8"]]
- 00b98ef0 bytes 00013fd6
+ 00b99318 bytes 00013fd6
~~~


<a id="compare-52976dc8a6aa83be7896637483758b21"></a>

### [`00b9b8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b8e0.md) → [`00b9bd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9bd08.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection7ServiceEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bfe0.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c3e0.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b8e0.md#insn-00b9b940) · [`00b9b99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b8e0.md#insn-00b9b99c) · [`00b9b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b8e0.md#insn-00b9b9c0)
- 新版 `00b9bd68`（命令位置の公開資料なし） · `00b9bdc4`（命令位置の公開資料なし） · `00b9bde8`（命令位置の公開資料なし）

~~~diff
- 00b9b940 ["INT_ADD", "register:40f0:8", ["const:b9b940:8", "const:4:8"]]
- 00b9b940 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b9bd68 ["INT_ADD", "register:40f0:8", ["const:b9bd68:8", "const:4:8"]]
+ 00b9bd68 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b9b940 bytes 18010394
+ 00b9bd68 bytes 0e010394
- 00b9b99c ["INT_ADD", "register:40f0:8", ["const:b9b99c:8", "const:4:8"]]
- 00b9b99c ["CALL", null, ["callee:00c5c250:8"]]
+ 00b9bdc4 ["INT_ADD", "register:40f0:8", ["const:b9bdc4:8", "const:4:8"]]
+ 00b9bdc4 ["CALL", null, ["callee:00c5c250:8"]]
- 00b9b99c bytes 2d010394
+ 00b9bdc4 bytes 23010394
- 00b9b9c0 ["INT_ADD", "register:40f0:8", ["const:b9b9c0:8", "const:4:8"]]
- 00b9b9c0 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b9bde8 ["INT_ADD", "register:40f0:8", ["const:b9bde8:8", "const:4:8"]]
+ 00b9bde8 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b9b9c0 bytes f8000394
+ 00b9bde8 bytes ee000394
~~~


<a id="compare-df4b3b589e7dd921706b8320d325e8ff"></a>

### [`00b9c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c67c.md) → [`00b9caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9caa4.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_EEEEvT

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c740.md) · 呼出先 4件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c740.md) [`00c5c7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7d0.md) [`00c5c870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c870.md)
- 新版 呼出元 1件 [`00c5cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb40.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb40.md) [`00c5cbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbd0.md) [`00c5cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c67c.md#insn-00b9c718) · [`00b9c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c67c.md#insn-00b9c804) · [`00b9c86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c67c.md#insn-00b9c86c)
- 新版 `00b9cb40`（命令位置の公開資料なし） · `00b9cc2c`（命令位置の公開資料なし） · `00b9cc94`（命令位置の公開資料なし）

~~~diff
- 00b9c718 ["INT_ADD", "register:40f0:8", ["const:b9c718:8", "const:4:8"]]
- 00b9c718 ["CALL", null, ["callee:00c58050:8"]]
+ 00b9cb40 ["INT_ADD", "register:40f0:8", ["const:b9cb40:8", "const:4:8"]]
+ 00b9cb40 ["CALL", null, ["callee:00c58050:8"]]
- 00b9c718 bytes 4eed0294
+ 00b9cb40 bytes 44ed0294
- 00b9c804 ["INT_ADD", "register:40f0:8", ["const:b9c804:8", "const:4:8"]]
- 00b9c804 ["CALL", null, ["callee:00c58050:8"]]
+ 00b9cc2c ["INT_ADD", "register:40f0:8", ["const:b9cc2c:8", "const:4:8"]]
+ 00b9cc2c ["CALL", null, ["callee:00c58050:8"]]
- 00b9c804 bytes 13ed0294
+ 00b9cc2c bytes 09ed0294
- 00b9c86c ["INT_ADD", "register:40f0:8", ["const:b9c86c:8", "const:4:8"]]
- 00b9c86c ["CALL", null, ["callee:00c5cb40:8"]]
+ 00b9cc94 ["INT_ADD", "register:40f0:8", ["const:b9cc94:8", "const:4:8"]]
+ 00b9cc94 ["CALL", null, ["callee:00c5cb40:8"]]
- 00b9c86c bytes b5ff0294
+ 00b9cc94 bytes abff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30d4d8b7dfc4db4dab28ff03d0061f3f"></a>

### [`00b9d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9d/00b9d7b0.md) → [`00b9dbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dbd8.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8d0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ccd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccd0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9d/00b9d7b0.md#insn-00b9d874)
- 新版 `00b9dc9c`（命令位置の公開資料なし）

~~~diff
- 00b9d874 ["INT_ADD", "register:40f0:8", ["const:b9d874:8", "const:4:8"]]
- 00b9d874 ["CALL", null, ["callee:00c58050:8"]]
+ 00b9dc9c ["INT_ADD", "register:40f0:8", ["const:b9dc9c:8", "const:4:8"]]
+ 00b9dc9c ["CALL", null, ["callee:00c58050:8"]]
- 00b9d874 bytes f7e80294
+ 00b9dc9c bytes ede80294
~~~


<a id="compare-835ac5cf51f9f14c0e52600ebc7fbf02"></a>

### [`00b9d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9d/00b9d8e8.md) → [`00b9dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dd10.md) FUN_00b9dd10

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9cef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9cef4.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00b9d31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9d31c.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9d9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9d/00b9d8e8.md#insn-00b9d9a8) · [`00b9d9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9d/00b9d8e8.md#insn-00b9d9d4)
- 新版 `00b9ddd0`（命令位置の公開資料なし） · `00b9ddfc`（命令位置の公開資料なし）

~~~diff
- 00b9d9a8 ["INT_ADD", "register:40f0:8", ["const:b9d9a8:8", "const:4:8"]]
- 00b9d9a8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00b9ddd0 ["INT_ADD", "register:40f0:8", ["const:b9ddd0:8", "const:4:8"]]
+ 00b9ddd0 ["CALL", null, ["callee:00c57f40:8"]]
- 00b9d9a8 bytes 66e80294
+ 00b9ddd0 bytes 5ce80294
- 00b9d9d4 ["INT_ADD", "register:40f0:8", ["const:b9d9d4:8", "const:4:8"]]
- 00b9d9d4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00b9ddfc ["INT_ADD", "register:40f0:8", ["const:b9ddfc:8", "const:4:8"]]
+ 00b9ddfc ["CALL", null, ["callee:00c57f40:8"]]
- 00b9d9d4 bytes 5be80294
+ 00b9ddfc bytes 51e80294
~~~


<a id="compare-76e2de8e655a96b19171abe6b0d7db9b"></a>

### [`00ba1574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md) → [`00ba199c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba1/00ba199c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb60.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf60.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md#insn-00ba1610) · [`00ba1650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md#insn-00ba1650)
- 新版 `00ba1a38`（命令位置の公開資料なし） · `00ba1a78`（命令位置の公開資料なし）

~~~diff
- 00ba1610 ["INT_ADD", "register:40f0:8", ["const:ba1610:8", "const:4:8"]]
- 00ba1610 ["CALL", null, ["callee:00c58050:8"]]
+ 00ba1a38 ["INT_ADD", "register:40f0:8", ["const:ba1a38:8", "const:4:8"]]
+ 00ba1a38 ["CALL", null, ["callee:00c58050:8"]]
- 00ba1610 bytes 90d90294
+ 00ba1a38 bytes 86d90294
- 00ba1650 ["INT_ADD", "register:40f0:8", ["const:ba1650:8", "const:4:8"]]
- 00ba1650 ["CALL", null, ["callee:00c58050:8"]]
+ 00ba1a78 ["INT_ADD", "register:40f0:8", ["const:ba1a78:8", "const:4:8"]]
+ 00ba1a78 ["CALL", null, ["callee:00c58050:8"]]
- 00ba1650 bytes 80d90294
+ 00ba1a78 bytes 76d90294
~~~


<a id="compare-d5522bd104f9bee51c7eff028d450f0d"></a>

### [`00bae444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md) → [`00bae86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae86c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb10.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf10.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md#insn-00bae4dc) · [`00bae524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md#insn-00bae524)
- 新版 `00bae904`（命令位置の公開資料なし） · `00bae94c`（命令位置の公開資料なし）

~~~diff
- 00bae4dc ["INT_ADD", "register:40f0:8", ["const:bae4dc:8", "const:4:8"]]
- 00bae4dc ["CALL", null, ["callee:00c58050:8"]]
+ 00bae904 ["INT_ADD", "register:40f0:8", ["const:bae904:8", "const:4:8"]]
+ 00bae904 ["CALL", null, ["callee:00c58050:8"]]
- 00bae4dc bytes dda50294
+ 00bae904 bytes d3a50294
- 00bae524 ["INT_ADD", "register:40f0:8", ["const:bae524:8", "const:4:8"]]
- 00bae524 ["CALL", null, ["callee:00c58050:8"]]
+ 00bae94c ["INT_ADD", "register:40f0:8", ["const:bae94c:8", "const:4:8"]]
+ 00bae94c ["CALL", null, ["callee:00c58050:8"]]
- 00bae524 bytes cba50294
+ 00bae94c bytes c1a50294
~~~


<a id="compare-f5fbd4980e4f79b8c0576ffd3975d5ca"></a>

### [`00bae558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae558.md) → [`00bae980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae980.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb00.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf00.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae558.md#insn-00bae5f4) · [`00bae634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae558.md#insn-00bae634)
- 新版 `00baea1c`（命令位置の公開資料なし） · `00baea5c`（命令位置の公開資料なし）

~~~diff
- 00bae5f4 ["INT_ADD", "register:40f0:8", ["const:bae5f4:8", "const:4:8"]]
- 00bae5f4 ["CALL", null, ["callee:00c58050:8"]]
+ 00baea1c ["INT_ADD", "register:40f0:8", ["const:baea1c:8", "const:4:8"]]
+ 00baea1c ["CALL", null, ["callee:00c58050:8"]]
- 00bae5f4 bytes 97a50294
+ 00baea1c bytes 8da50294
- 00bae634 ["INT_ADD", "register:40f0:8", ["const:bae634:8", "const:4:8"]]
- 00bae634 ["CALL", null, ["callee:00c58050:8"]]
+ 00baea5c ["INT_ADD", "register:40f0:8", ["const:baea5c:8", "const:4:8"]]
+ 00baea5c ["CALL", null, ["callee:00c58050:8"]]
- 00bae634 bytes 87a50294
+ 00baea5c bytes 7da50294
~~~


<a id="compare-ffb6c09e3725ab68cee8fe0e8ce9f0ad"></a>

### [`00bae678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae678.md) → [`00baeaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeaa0.md) _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbb0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbb0.md)
- 新版 呼出元 1件 [`00c5cfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfb0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae678.md#insn-00bae694) · [`00bae6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae678.md#insn-00bae6a0)
- 新版 `00baeabc`（命令位置の公開資料なし） · `00baeac8`（命令位置の公開資料なし）

~~~diff
- 00bae694 ["INT_ADD", "register:40f0:8", ["const:bae694:8", "const:4:8"]]
- 00bae694 ["CALL", null, ["callee:00c5cfb0:8"]]
+ 00baeabc ["INT_ADD", "register:40f0:8", ["const:baeabc:8", "const:4:8"]]
+ 00baeabc ["CALL", null, ["callee:00c5cfb0:8"]]
- 00bae694 bytes 47b90294
+ 00baeabc bytes 3db90294
- 00bae6a0 ["INT_ADD", "register:40f0:8", ["const:bae6a0:8", "const:4:8"]]
- 00bae6a0 ["CALL", null, ["callee:00c5cfb0:8"]]
+ 00baeac8 ["INT_ADD", "register:40f0:8", ["const:baeac8:8", "const:4:8"]]
+ 00baeac8 ["CALL", null, ["callee:00c5cfb0:8"]]
- 00bae6a0 bytes 44b90294
+ 00baeac8 bytes 3ab90294
~~~


<a id="compare-aacb268365590ef8ecb5f985e60e7af0"></a>

### [`00bae6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae6b8.md) → [`00baeae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeae0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca90.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce90.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae6b8.md#insn-00bae750) · [`00bae798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae6b8.md#insn-00bae798)
- 新版 `00baeb78`（命令位置の公開資料なし） · `00baebc0`（命令位置の公開資料なし）

~~~diff
- 00bae750 ["INT_ADD", "register:40f0:8", ["const:bae750:8", "const:4:8"]]
- 00bae750 ["CALL", null, ["callee:00c58050:8"]]
+ 00baeb78 ["INT_ADD", "register:40f0:8", ["const:baeb78:8", "const:4:8"]]
+ 00baeb78 ["CALL", null, ["callee:00c58050:8"]]
- 00bae750 bytes 40a50294
+ 00baeb78 bytes 36a50294
- 00bae798 ["INT_ADD", "register:40f0:8", ["const:bae798:8", "const:4:8"]]
- 00bae798 ["CALL", null, ["callee:00c58050:8"]]
+ 00baebc0 ["INT_ADD", "register:40f0:8", ["const:baebc0:8", "const:4:8"]]
+ 00baebc0 ["CALL", null, ["callee:00c58050:8"]]
- 00bae798 bytes 2ea50294
+ 00baebc0 bytes 24a50294
~~~


<a id="compare-a82e46adb10c5e94fcbfcf914fdde51b"></a>

### [`00bae7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md) → [`00baebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baebf4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca80.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce80.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md#insn-00bae868) · [`00bae8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md#insn-00bae8a8)
- 新版 `00baec90`（命令位置の公開資料なし） · `00baecd0`（命令位置の公開資料なし）

~~~diff
- 00bae868 ["INT_ADD", "register:40f0:8", ["const:bae868:8", "const:4:8"]]
- 00bae868 ["CALL", null, ["callee:00c58050:8"]]
+ 00baec90 ["INT_ADD", "register:40f0:8", ["const:baec90:8", "const:4:8"]]
+ 00baec90 ["CALL", null, ["callee:00c58050:8"]]
- 00bae868 bytes faa40294
+ 00baec90 bytes f0a40294
- 00bae8a8 ["INT_ADD", "register:40f0:8", ["const:bae8a8:8", "const:4:8"]]
- 00bae8a8 ["CALL", null, ["callee:00c58050:8"]]
+ 00baecd0 ["INT_ADD", "register:40f0:8", ["const:baecd0:8", "const:4:8"]]
+ 00baecd0 ["CALL", null, ["callee:00c58050:8"]]
- 00bae8a8 bytes eaa40294
+ 00baecd0 bytes e0a40294
~~~


<a id="compare-1ec3d32667d4c216f18955d5bc87b2c8"></a>

### [`00baef18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baef18.md) → [`00baf340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baef18.md#insn-00baef4c) · [`00baef64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baef18.md#insn-00baef64) · [`00baefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baef18.md#insn-00baefa8)
- 新版 `00baf374`（命令位置の公開資料なし） · `00baf38c`（命令位置の公開資料なし） · `00baf3d0`（命令位置の公開資料なし）

~~~diff
- 00baef4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baef4c ["INT_ADD", "register:40f0:8", ["const:baef4c:8", "const:4:8"]]
- 00baef4c ["CALLIND", null, ["register:0:8"]]
+ 00baf374 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf374 ["INT_ADD", "register:40f0:8", ["const:baf374:8", "const:4:8"]]
+ 00baf374 ["CALLIND", null, ["register:0:8"]]
- 00baef4c bytes 00013fd6
+ 00baf374 bytes 00013fd6
- 00baef64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baef64 ["INT_ADD", "register:40f0:8", ["const:baef64:8", "const:4:8"]]
- 00baef64 ["CALLIND", null, ["register:0:8"]]
+ 00baf38c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf38c ["INT_ADD", "register:40f0:8", ["const:baf38c:8", "const:4:8"]]
+ 00baf38c ["CALLIND", null, ["register:0:8"]]
- 00baef64 bytes 20013fd6
+ 00baf38c bytes 20013fd6
- 00baefa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baefa8 ["INT_ADD", "register:40f0:8", ["const:baefa8:8", "const:4:8"]]
- 00baefa8 ["CALLIND", null, ["register:0:8"]]
+ 00baf3d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf3d0 ["INT_ADD", "register:40f0:8", ["const:baf3d0:8", "const:4:8"]]
+ 00baf3d0 ["CALLIND", null, ["register:0:8"]]
- 00baefa8 bytes 00013fd6
+ 00baf3d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb012dde268d817d267e134e5fd812d"></a>

### [`00baf09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md) → [`00baf4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md) FUN_00baf4c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00baea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md) [`00baf300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md) · 呼出先 1件 [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md)
- 新版 呼出元 2件 [`00baee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baee28.md) [`00baf728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf728.md) · 呼出先 1件 [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md#insn-00baf0d0) · [`00baf0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md#insn-00baf0e8) · [`00baf10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md#insn-00baf10c)
- 新版 `00baf4f8`（命令位置の公開資料なし） · `00baf510`（命令位置の公開資料なし） · `00baf534`（命令位置の公開資料なし）

~~~diff
- 00baf0d0 ["INT_ADD", "register:40f0:8", ["const:baf0d0:8", "const:4:8"]]
- 00baf0d0 ["CALL", null, ["callee:00c5d0b0:8"]]
+ 00baf4f8 ["INT_ADD", "register:40f0:8", ["const:baf4f8:8", "const:4:8"]]
+ 00baf4f8 ["CALL", null, ["callee:00c5d0b0:8"]]
- 00baf0d0 bytes f8b60294
+ 00baf4f8 bytes eeb60294
- 00baf0e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf0e8 ["INT_ADD", "register:40f0:8", ["const:baf0e8:8", "const:4:8"]]
- 00baf0e8 ["CALLIND", null, ["register:0:8"]]
+ 00baf510 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf510 ["INT_ADD", "register:40f0:8", ["const:baf510:8", "const:4:8"]]
+ 00baf510 ["CALLIND", null, ["register:0:8"]]
- 00baf0e8 bytes 20013fd6
+ 00baf510 bytes 20013fd6
- 00baf10c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf10c ["INT_ADD", "register:40f0:8", ["const:baf10c:8", "const:4:8"]]
- 00baf10c ["CALLIND", null, ["register:0:8"]]
+ 00baf534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf534 ["INT_ADD", "register:40f0:8", ["const:baf534:8", "const:4:8"]]
+ 00baf534 ["CALLIND", null, ["register:0:8"]]
- 00baf10c bytes 00013fd6
+ 00baf534 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4073deac5b9db64f6c44b84856ae1d6d"></a>

### [`00baf1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md) → [`00baf5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf5cc.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7f0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5cbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbf0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf1d4) · [`00baf1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf1f0) · [`00baf22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md#insn-00baf22c)
- 新版 `00baf5fc`（命令位置の公開資料なし） · `00baf618`（命令位置の公開資料なし） · `00baf654`（命令位置の公開資料なし）

~~~diff
- 00baf1d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf1d4 ["INT_ADD", "register:40f0:8", ["const:baf1d4:8", "const:4:8"]]
- 00baf1d4 ["CALLIND", null, ["register:0:8"]]
+ 00baf5fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf5fc ["INT_ADD", "register:40f0:8", ["const:baf5fc:8", "const:4:8"]]
+ 00baf5fc ["CALLIND", null, ["register:0:8"]]
- 00baf1d4 bytes 20013fd6
+ 00baf5fc bytes 20013fd6
- 00baf1f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf1f0 ["INT_ADD", "register:40f0:8", ["const:baf1f0:8", "const:4:8"]]
- 00baf1f0 ["CALLIND", null, ["register:0:8"]]
+ 00baf618 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf618 ["INT_ADD", "register:40f0:8", ["const:baf618:8", "const:4:8"]]
+ 00baf618 ["CALLIND", null, ["register:0:8"]]
- 00baf1f0 bytes 20013fd6
+ 00baf618 bytes 20013fd6
- 00baf22c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf22c ["INT_ADD", "register:40f0:8", ["const:baf22c:8", "const:4:8"]]
- 00baf22c ["CALLIND", null, ["register:0:8"]]
+ 00baf654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf654 ["INT_ADD", "register:40f0:8", ["const:baf654:8", "const:4:8"]]
+ 00baf654 ["CALLIND", null, ["register:0:8"]]
- 00baf22c bytes 00013fd6
+ 00baf654 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1812a0e763448aa2a714b38e50f09a39"></a>

### [`00bafebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafebc.md) → [`00bb02e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb02e4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb90.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf90.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafebc.md#insn-00baff54) · [`00baff9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafebc.md#insn-00baff9c)
- 新版 `00bb037c`（命令位置の公開資料なし） · `00bb03c4`（命令位置の公開資料なし）

~~~diff
- 00baff54 ["INT_ADD", "register:40f0:8", ["const:baff54:8", "const:4:8"]]
- 00baff54 ["CALL", null, ["callee:00c58050:8"]]
+ 00bb037c ["INT_ADD", "register:40f0:8", ["const:bb037c:8", "const:4:8"]]
+ 00bb037c ["CALL", null, ["callee:00c58050:8"]]
- 00baff54 bytes 3f9f0294
+ 00bb037c bytes 359f0294
- 00baff9c ["INT_ADD", "register:40f0:8", ["const:baff9c:8", "const:4:8"]]
- 00baff9c ["CALL", null, ["callee:00c58050:8"]]
+ 00bb03c4 ["INT_ADD", "register:40f0:8", ["const:bb03c4:8", "const:4:8"]]
+ 00bb03c4 ["CALL", null, ["callee:00c58050:8"]]
- 00baff9c bytes 2d9f0294
+ 00bb03c4 bytes 239f0294
~~~


<a id="compare-9bb325c974b6f82c47addc87be2a159f"></a>

### [`00baffd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baffd0.md) → [`00bb03f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb03f8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca50.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce50.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baffd0.md#insn-00bb006c) · [`00bb00ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baffd0.md#insn-00bb00ac)
- 新版 `00bb0494`（命令位置の公開資料なし） · `00bb04d4`（命令位置の公開資料なし）

~~~diff
- 00bb006c ["INT_ADD", "register:40f0:8", ["const:bb006c:8", "const:4:8"]]
- 00bb006c ["CALL", null, ["callee:00c58050:8"]]
+ 00bb0494 ["INT_ADD", "register:40f0:8", ["const:bb0494:8", "const:4:8"]]
+ 00bb0494 ["CALL", null, ["callee:00c58050:8"]]
- 00bb006c bytes f99e0294
+ 00bb0494 bytes ef9e0294
- 00bb00ac ["INT_ADD", "register:40f0:8", ["const:bb00ac:8", "const:4:8"]]
- 00bb00ac ["CALL", null, ["callee:00c58050:8"]]
+ 00bb04d4 ["INT_ADD", "register:40f0:8", ["const:bb04d4:8", "const:4:8"]]
+ 00bb04d4 ["CALL", null, ["callee:00c58050:8"]]
- 00bb00ac bytes e99e0294
+ 00bb04d4 bytes df9e0294
~~~


<a id="compare-2257fa925113a6b8449e83cfc25a8ae5"></a>

### [`00bb00f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb00f0.md) → [`00bb0518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0518.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc20.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d020.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb00f0.md#insn-00bb0170) · [`00bb0188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb00f0.md#insn-00bb0188) · [`00bb0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb00f0.md#insn-00bb0204)
- 新版 `00bb0598`（命令位置の公開資料なし） · `00bb05b0`（命令位置の公開資料なし） · `00bb062c`（命令位置の公開資料なし）

~~~diff
- 00bb0170 ["INT_ADD", "register:40f0:8", ["const:bb0170:8", "const:4:8"]]
- 00bb0170 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bb0598 ["INT_ADD", "register:40f0:8", ["const:bb0598:8", "const:4:8"]]
+ 00bb0598 ["CALL", null, ["callee:00c57e90:8"]]
- 00bb0170 bytes 489e0294
+ 00bb0598 bytes 3e9e0294
- 00bb0188 ["INT_ADD", "register:40f0:8", ["const:bb0188:8", "const:4:8"]]
- 00bb0188 ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00bb05b0 ["INT_ADD", "register:40f0:8", ["const:bb05b0:8", "const:4:8"]]
+ 00bb05b0 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00bb0188 bytes 0aac0294
+ 00bb05b0 bytes 00ac0294
- 00bb0204 ["INT_ADD", "register:40f0:8", ["const:bb0204:8", "const:4:8"]]
- 00bb0204 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb062c ["INT_ADD", "register:40f0:8", ["const:bb062c:8", "const:4:8"]]
+ 00bb062c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb0204 bytes 2b9e0294
+ 00bb062c bytes 219e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8e3007337d3457c960a1b8e23493ec8"></a>

### [`00bb0240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0240.md) → [`00bb0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0668.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__t

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca30.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca20.md)
- 新版 呼出元 1件 [`00c5ce30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce30.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0240.md#insn-00bb0274) · [`00bb0290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0240.md#insn-00bb0290) · [`00bb02a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0240.md#insn-00bb02a0)
- 新版 `00bb069c`（命令位置の公開資料なし） · `00bb06b8`（命令位置の公開資料なし） · `00bb06c8`（命令位置の公開資料なし）

~~~diff
- 00bb0274 ["INT_ADD", "register:40f0:8", ["const:bb0274:8", "const:4:8"]]
- 00bb0274 ["CALL", null, ["callee:00c5ce20:8"]]
+ 00bb069c ["INT_ADD", "register:40f0:8", ["const:bb069c:8", "const:4:8"]]
+ 00bb069c ["CALL", null, ["callee:00c5ce20:8"]]
- 00bb0274 bytes ebb10294
+ 00bb069c bytes e1b10294
- 00bb0290 ["INT_ADD", "register:40f0:8", ["const:bb0290:8", "const:4:8"]]
- 00bb0290 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bb06b8 ["INT_ADD", "register:40f0:8", ["const:bb06b8:8", "const:4:8"]]
+ 00bb06b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00bb0290 bytes 009e0294
+ 00bb06b8 bytes f69d0294
- 00bb02a0 ["INT_ADD", "register:40f0:8", ["const:bb02a0:8", "const:4:8"]]
- 00bb02a0 ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00bb06c8 ["INT_ADD", "register:40f0:8", ["const:bb06c8:8", "const:4:8"]]
+ 00bb06c8 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00bb02a0 bytes c4ab0294
+ 00bb06c8 bytes baab0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df4a2875e9aa269a9316e83c8c565026"></a>

### [`00bb0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0324.md) → [`00bb074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb074c.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE12__find_equalIS2_EERPNS_16__tree_node_baseIPvEERPNS_15__

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca20.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce20.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb03c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0324.md#insn-00bb03c4) · [`00bb0404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0324.md#insn-00bb0404)
- 新版 `00bb07ec`（命令位置の公開資料なし） · `00bb082c`（命令位置の公開資料なし）

~~~diff
- 00bb03c4 ["INT_ADD", "register:40f0:8", ["const:bb03c4:8", "const:4:8"]]
- 00bb03c4 ["CALL", null, ["callee:00c58050:8"]]
+ 00bb07ec ["INT_ADD", "register:40f0:8", ["const:bb07ec:8", "const:4:8"]]
+ 00bb07ec ["CALL", null, ["callee:00c58050:8"]]
- 00bb03c4 bytes 239e0294
+ 00bb07ec bytes 199e0294
- 00bb0404 ["INT_ADD", "register:40f0:8", ["const:bb0404:8", "const:4:8"]]
- 00bb0404 ["CALL", null, ["callee:00c58050:8"]]
+ 00bb082c ["INT_ADD", "register:40f0:8", ["const:bb082c:8", "const:4:8"]]
+ 00bb082c ["CALL", null, ["callee:00c58050:8"]]
- 00bb0404 bytes 139e0294
+ 00bb082c bytes 099e0294
~~~


<a id="compare-8cc78aaf82cc87cd9801410557010490"></a>

### [`00bb0d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md) → [`00bb112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md) FUN_00bb112c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bb0668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0668.md) [`00bb0f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md) · 呼出先 1件 [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md)
- 新版 呼出元 2件 [`00bb0a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0a90.md) [`00bb1390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1390.md) · 呼出先 1件 [`00c5d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md#insn-00bb0d38) · [`00bb0d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md#insn-00bb0d50) · [`00bb0d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md#insn-00bb0d74)
- 新版 `00bb1160`（命令位置の公開資料なし） · `00bb1178`（命令位置の公開資料なし） · `00bb119c`（命令位置の公開資料なし）

~~~diff
- 00bb0d38 ["INT_ADD", "register:40f0:8", ["const:bb0d38:8", "const:4:8"]]
- 00bb0d38 ["CALL", null, ["callee:00c5d0c0:8"]]
+ 00bb1160 ["INT_ADD", "register:40f0:8", ["const:bb1160:8", "const:4:8"]]
+ 00bb1160 ["CALL", null, ["callee:00c5d0c0:8"]]
- 00bb0d38 bytes e2af0294
+ 00bb1160 bytes d8af0294
- 00bb0d50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb0d50 ["INT_ADD", "register:40f0:8", ["const:bb0d50:8", "const:4:8"]]
- 00bb0d50 ["CALLIND", null, ["register:0:8"]]
+ 00bb1178 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1178 ["INT_ADD", "register:40f0:8", ["const:bb1178:8", "const:4:8"]]
+ 00bb1178 ["CALLIND", null, ["register:0:8"]]
- 00bb0d50 bytes 20013fd6
+ 00bb1178 bytes 20013fd6
- 00bb0d74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0d74 ["INT_ADD", "register:40f0:8", ["const:bb0d74:8", "const:4:8"]]
- 00bb0d74 ["CALLIND", null, ["register:0:8"]]
+ 00bb119c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb119c ["INT_ADD", "register:40f0:8", ["const:bb119c:8", "const:4:8"]]
+ 00bb119c ["CALLIND", null, ["register:0:8"]]
- 00bb0d74 bytes 00013fd6
+ 00bb119c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-104d0020c81f3b0e86501a2d34f42857"></a>

### [`00bb0e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md) → [`00bb1234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1234.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5c800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c800.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5cc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc00.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md#insn-00bb0e3c) · [`00bb0e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md#insn-00bb0e58) · [`00bb0e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md#insn-00bb0e94)
- 新版 `00bb1264`（命令位置の公開資料なし） · `00bb1280`（命令位置の公開資料なし） · `00bb12bc`（命令位置の公開資料なし）

~~~diff
- 00bb0e3c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb0e3c ["INT_ADD", "register:40f0:8", ["const:bb0e3c:8", "const:4:8"]]
- 00bb0e3c ["CALLIND", null, ["register:0:8"]]
+ 00bb1264 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1264 ["INT_ADD", "register:40f0:8", ["const:bb1264:8", "const:4:8"]]
+ 00bb1264 ["CALLIND", null, ["register:0:8"]]
- 00bb0e3c bytes 20013fd6
+ 00bb1264 bytes 20013fd6
- 00bb0e58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb0e58 ["INT_ADD", "register:40f0:8", ["const:bb0e58:8", "const:4:8"]]
- 00bb0e58 ["CALLIND", null, ["register:0:8"]]
+ 00bb1280 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1280 ["INT_ADD", "register:40f0:8", ["const:bb1280:8", "const:4:8"]]
+ 00bb1280 ["CALLIND", null, ["register:0:8"]]
- 00bb0e58 bytes 20013fd6
+ 00bb1280 bytes 20013fd6
- 00bb0e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0e94 ["INT_ADD", "register:40f0:8", ["const:bb0e94:8", "const:4:8"]]
- 00bb0e94 ["CALLIND", null, ["register:0:8"]]
+ 00bb12bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb12bc ["INT_ADD", "register:40f0:8", ["const:bb12bc:8", "const:4:8"]]
+ 00bb12bc ["CALLIND", null, ["register:0:8"]]
- 00bb0e94 bytes 00013fd6
+ 00bb12bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7aa84872b8190d3b96300962691be33"></a>

### [`00bb1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md) → [`00bb1640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1640.md) FUN_00bb1640

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8dcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c640.md)
- 新版 呼出元 1件 [`00b8e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8e0dc.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb125c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md#insn-00bb125c) · [`00bb1274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md#insn-00bb1274) · [`00bb12d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md#insn-00bb12d0)
- 新版 `00bb1684`（命令位置の公開資料なし） · `00bb169c`（命令位置の公開資料なし） · `00bb16f8`（命令位置の公開資料なし）

~~~diff
- 00bb125c ["INT_ADD", "register:40f0:8", ["const:bb125c:8", "const:4:8"]]
- 00bb125c ["CALL", null, ["callee:00c5ca40:8"]]
+ 00bb1684 ["INT_ADD", "register:40f0:8", ["const:bb1684:8", "const:4:8"]]
+ 00bb1684 ["CALL", null, ["callee:00c5ca40:8"]]
- 00bb125c bytes f9ac0294
+ 00bb1684 bytes efac0294
- 00bb1274 ["INT_ADD", "register:40f0:8", ["const:bb1274:8", "const:4:8"]]
- 00bb1274 ["CALL", null, ["callee:00c5ca40:8"]]
+ 00bb169c ["INT_ADD", "register:40f0:8", ["const:bb169c:8", "const:4:8"]]
+ 00bb169c ["CALL", null, ["callee:00c5ca40:8"]]
- 00bb1274 bytes f3ac0294
+ 00bb169c bytes e9ac0294
- 00bb12d0 ["INT_ADD", "register:40f0:8", ["const:bb12d0:8", "const:4:8"]]
- 00bb12d0 ["CALL", null, ["callee:00c58050:8"]]
+ 00bb16f8 ["INT_ADD", "register:40f0:8", ["const:bb16f8:8", "const:4:8"]]
+ 00bb16f8 ["CALL", null, ["callee:00c58050:8"]]
- 00bb12d0 bytes 609a0294
+ 00bb16f8 bytes 569a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd71b4d27ed7b9c36469dc1ebb045dad"></a>

### [`00bb20cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb20cc.md) → [`00bb24f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb24f4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb70.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb70.md)
- 新版 呼出元 1件 [`00c5cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf70.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb20e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb20cc.md#insn-00bb20e8) · [`00bb20f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb20cc.md#insn-00bb20f4) · [`00bb2104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb20cc.md#insn-00bb2104)
- 新版 `00bb2510`（命令位置の公開資料なし） · `00bb251c`（命令位置の公開資料なし） · `00bb252c`（命令位置の公開資料なし）

~~~diff
- 00bb20e8 ["INT_ADD", "register:40f0:8", ["const:bb20e8:8", "const:4:8"]]
- 00bb20e8 ["CALL", null, ["callee:00c5cf70:8"]]
+ 00bb2510 ["INT_ADD", "register:40f0:8", ["const:bb2510:8", "const:4:8"]]
+ 00bb2510 ["CALL", null, ["callee:00c5cf70:8"]]
- 00bb20e8 bytes a2aa0294
+ 00bb2510 bytes 98aa0294
- 00bb20f4 ["INT_ADD", "register:40f0:8", ["const:bb20f4:8", "const:4:8"]]
- 00bb20f4 ["CALL", null, ["callee:00c5cf70:8"]]
+ 00bb251c ["INT_ADD", "register:40f0:8", ["const:bb251c:8", "const:4:8"]]
+ 00bb251c ["CALL", null, ["callee:00c5cf70:8"]]
- 00bb20f4 bytes 9faa0294
+ 00bb251c bytes 95aa0294
- 00bb2104 ["INT_ADD", "register:40f0:8", ["const:bb2104:8", "const:4:8"]]
- 00bb2104 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb252c ["INT_ADD", "register:40f0:8", ["const:bb252c:8", "const:4:8"]]
+ 00bb252c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb2104 bytes 6b960294
+ 00bb252c bytes 61960294
~~~


<a id="compare-b9c530d3cb6da5c8decc09b89a534665"></a>

### [`00bb2230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2230.md) → [`00bb2658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2658.md) _ZNSt6__ndk16__treeIPN11flatbuffers8FieldDefENS_4lessIS3_EENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbd0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cbd0.md)
- 新版 呼出元 1件 [`00c5cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfd0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb224c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2230.md#insn-00bb224c) · [`00bb2258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2230.md#insn-00bb2258)
- 新版 `00bb2674`（命令位置の公開資料なし） · `00bb2680`（命令位置の公開資料なし）

~~~diff
- 00bb224c ["INT_ADD", "register:40f0:8", ["const:bb224c:8", "const:4:8"]]
- 00bb224c ["CALL", null, ["callee:00c5cfd0:8"]]
+ 00bb2674 ["INT_ADD", "register:40f0:8", ["const:bb2674:8", "const:4:8"]]
+ 00bb2674 ["CALL", null, ["callee:00c5cfd0:8"]]
- 00bb224c bytes 61aa0294
+ 00bb2674 bytes 57aa0294
- 00bb2258 ["INT_ADD", "register:40f0:8", ["const:bb2258:8", "const:4:8"]]
- 00bb2258 ["CALL", null, ["callee:00c5cfd0:8"]]
+ 00bb2680 ["INT_ADD", "register:40f0:8", ["const:bb2680:8", "const:4:8"]]
+ 00bb2680 ["CALL", null, ["callee:00c5cfd0:8"]]
- 00bb2258 bytes 5eaa0294
+ 00bb2680 bytes 54aa0294
~~~


<a id="compare-1372a371ae40c29952973b0490e4294b"></a>

### [`00bb2d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d8c.md) → [`00bb31b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb31b4.md) _ZN11flatbuffers18ConCatPathFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c340.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c740.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d8c.md#insn-00bb2dac) · [`00bb2e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d8c.md#insn-00bb2e40) · [`00bb2e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d8c.md#insn-00bb2e90)
- 新版 `00bb31d4`（命令位置の公開資料なし） · `00bb3268`（命令位置の公開資料なし） · `00bb32b8`（命令位置の公開資料なし）

~~~diff
- 00bb2dac ["INT_ADD", "register:40f0:8", ["const:bb2dac:8", "const:4:8"]]
- 00bb2dac ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00bb31d4 ["INT_ADD", "register:40f0:8", ["const:bb31d4:8", "const:4:8"]]
+ 00bb31d4 ["CALL", null, ["callee:00c5b5b0:8"]]
- 00bb2dac bytes 01a10294
+ 00bb31d4 bytes f7a00294
- 00bb2e40 ["INT_ADD", "register:40f0:8", ["const:bb2e40:8", "const:4:8"]]
- 00bb2e40 ["CALL", null, ["callee:00c5a8e0:8"]]
+ 00bb3268 ["INT_ADD", "register:40f0:8", ["const:bb3268:8", "const:4:8"]]
+ 00bb3268 ["CALL", null, ["callee:00c5a8e0:8"]]
- 00bb2e40 bytes a89d0294
+ 00bb3268 bytes 9e9d0294
- 00bb2e90 ["INT_ADD", "register:40f0:8", ["const:bb2e90:8", "const:4:8"]]
- 00bb2e90 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb32b8 ["INT_ADD", "register:40f0:8", ["const:bb32b8:8", "const:4:8"]]
+ 00bb32b8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb2e90 bytes 3c930294
+ 00bb32b8 bytes 32930294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa256132930ce383f2074936f22c355"></a>

### [`00bb4d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4d28.md) → [`00bb5150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5150.md) _ZN11flatbuffers11CharToUpperEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb3be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3be8.md) · 呼出先 1件 [`00c5ce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce60.md)
- 新版 呼出元 1件 [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) · 呼出先 1件 [`00c5d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb4d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4d28.md#insn-00bb4d34)
- 新版 `00bb515c`（命令位置の公開資料なし）

~~~diff
- 00bb4d34 ["INT_ADD", "register:40f0:8", ["const:bb4d34:8", "const:4:8"]]
- 00bb4d34 ["CALL", null, ["callee:00c5d260:8"]]
+ 00bb515c ["INT_ADD", "register:40f0:8", ["const:bb515c:8", "const:4:8"]]
+ 00bb515c ["CALL", null, ["callee:00c5d260:8"]]
- 00bb4d34 bytes 4ba00294
+ 00bb515c bytes 41a00294
~~~


<a id="compare-839600beca0b9070f4b377c73c9ef1d2"></a>

### [`00bb5484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5484.md) → [`00bb58ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb58ac.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5484.md#insn-00bb5494)
- 新版 `00bb58bc`（命令位置の公開資料なし）

~~~diff
- 00bb5494 ["INT_ADD", "register:40f0:8", ["const:bb5494:8", "const:4:8"]]
- 00bb5494 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb58bc ["INT_ADD", "register:40f0:8", ["const:bb58bc:8", "const:4:8"]]
+ 00bb58bc ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb5494 bytes 479e0294
+ 00bb58bc bytes 3d9e0294
~~~


<a id="compare-a325c46655d0c435d52e9e3f40b8a1a2"></a>

### [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) → [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE6setbufEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md) [`00bb53e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md) [`00c05264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md) [`00c0551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md) · 呼出先 2件 [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md)
- 新版 呼出元 4件 [`00bb54e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md) [`00bb5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md) [`00c0568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0568c.md) [`00c05944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05944.md) · 呼出先 2件 [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb55d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md#insn-00bb55d0) · [`00bb55e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md#insn-00bb55e4) · [`00bb5638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md#insn-00bb5638)
- 新版 `00bb59f8`（命令位置の公開資料なし） · `00bb5a0c`（命令位置の公開資料なし） · `00bb5a60`（命令位置の公開資料なし）

~~~diff
- 00bb55d0 ["INT_ADD", "register:40f0:8", ["const:bb55d0:8", "const:4:8"]]
- 00bb55d0 ["CALL", null, ["callee:00c5be40:8"]]
+ 00bb59f8 ["INT_ADD", "register:40f0:8", ["const:bb59f8:8", "const:4:8"]]
+ 00bb59f8 ["CALL", null, ["callee:00c5be40:8"]]
- 00bb55d0 bytes 1c990294
+ 00bb59f8 bytes 12990294
- 00bb55e4 ["INT_ADD", "register:40f0:8", ["const:bb55e4:8", "const:4:8"]]
- 00bb55e4 ["CALL", null, ["callee:00c5be40:8"]]
+ 00bb5a0c ["INT_ADD", "register:40f0:8", ["const:bb5a0c:8", "const:4:8"]]
+ 00bb5a0c ["CALL", null, ["callee:00c5be40:8"]]
- 00bb55e4 bytes 17990294
+ 00bb5a0c bytes 0d990294
- 00bb5638 ["INT_ADD", "register:40f0:8", ["const:bb5638:8", "const:4:8"]]
- 00bb5638 ["CALL", null, ["callee:00c5be50:8"]]
+ 00bb5a60 ["INT_ADD", "register:40f0:8", ["const:bb5a60:8", "const:4:8"]]
+ 00bb5a60 ["CALL", null, ["callee:00c5be50:8"]]
- 00bb5638 bytes 06990294
+ 00bb5a60 bytes fc980294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18082ffea000298507064410735f9fd8"></a>

### [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) → [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) FUN_00bb62ec

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md) [`00bb57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md) [`00bb59b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md) [`00bb5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 4件 [`00bb5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md) [`00bb5be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md) [`00bb5dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md) [`00bb60b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md#insn-00bb5ecc)
- 新版 `00bb62f4`（命令位置の公開資料なし）

~~~diff
- 00bb5ecc ["INT_ADD", "register:40f0:8", ["const:bb5ecc:8", "const:4:8"]]
- 00bb5ecc ["CALL", null, ["callee:00c5b140:8"]]
+ 00bb62f4 ["INT_ADD", "register:40f0:8", ["const:bb62f4:8", "const:4:8"]]
+ 00bb62f4 ["CALL", null, ["callee:00c5b140:8"]]
- 00bb5ecc bytes 9d930294
+ 00bb62f4 bytes 93930294
~~~


<a id="compare-fb1f6ef28d5deb0862a358aac92cd6c6"></a>

### [`00bb5ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ed8.md) → [`00bb6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6300.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ed8.md#insn-00bb5eec)
- 新版 `00bb6314`（命令位置の公開資料なし）

~~~diff
- 00bb5eec ["INT_ADD", "register:40f0:8", ["const:bb5eec:8", "const:4:8"]]
- 00bb5eec ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00bb6314 ["INT_ADD", "register:40f0:8", ["const:bb6314:8", "const:4:8"]]
+ 00bb6314 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bb5eec bytes 7d9b0294
+ 00bb6314 bytes 739b0294
~~~


<a id="compare-ea6a228d16fd7665c33074d9c87bbac3"></a>

### [`00bb5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f14.md) → [`00bb633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb633c.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f14.md#insn-00bb5f30)
- 新版 `00bb6358`（命令位置の公開資料なし）

~~~diff
- 00bb5f30 ["INT_ADD", "register:40f0:8", ["const:bb5f30:8", "const:4:8"]]
- 00bb5f30 ["CALL", null, ["callee:00c5d0e0:8"]]
+ 00bb6358 ["INT_ADD", "register:40f0:8", ["const:bb6358:8", "const:4:8"]]
+ 00bb6358 ["CALL", null, ["callee:00c5d0e0:8"]]
- 00bb5f30 bytes 6c9b0294
+ 00bb6358 bytes 629b0294
~~~


<a id="compare-ab7cec4ea4194c4a4df13e9ae836911b"></a>

### [`00bb62bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md) → [`00bb66e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66e4.md) FUN_00bb66e4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 呼出先 2件 [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md) [`00c5d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d040.md)
- 新版 呼出元 1件 [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) · 呼出先 2件 [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md) [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb62cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md#insn-00bb62cc)
- 新版 `00bb66f4`（命令位置の公開資料なし）

~~~diff
- 00bb62cc ["INT_ADD", "register:40f0:8", ["const:bb62cc:8", "const:4:8"]]
- 00bb62cc ["CALL", null, ["callee:00c5ac60:8"]]
+ 00bb66f4 ["INT_ADD", "register:40f0:8", ["const:bb66f4:8", "const:4:8"]]
+ 00bb66f4 ["CALL", null, ["callee:00c5ac60:8"]]
- 00bb62cc bytes 65910294
+ 00bb66f4 bytes 5b910294
~~~


<a id="compare-58f06c77bffdb782946978a8e8e88ed9"></a>

### [`00bb69d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md) → [`00bb6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6dfc.md) _ZN8firebase9messaging20PollableListenerImplD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf80.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d060.md)
- 新版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb69f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md#insn-00bb69f0) · [`00bb6a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md#insn-00bb6a04) · [`00bb6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md#insn-00bb6a38)
- 新版 `00bb6e18`（命令位置の公開資料なし） · `00bb6e2c`（命令位置の公開資料なし） · `00bb6e60`（命令位置の公開資料なし）

~~~diff
- 00bb69f0 ["INT_ADD", "register:40f0:8", ["const:bb69f0:8", "const:4:8"]]
- 00bb69f0 ["CALL", null, ["callee:00c5d460:8"]]
+ 00bb6e18 ["INT_ADD", "register:40f0:8", ["const:bb6e18:8", "const:4:8"]]
+ 00bb6e18 ["CALL", null, ["callee:00c5d460:8"]]
- 00bb69f0 bytes 9c990294
+ 00bb6e18 bytes 92990294
- 00bb6a04 ["INT_ADD", "register:40f0:8", ["const:bb6a04:8", "const:4:8"]]
- 00bb6a04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb6e2c ["INT_ADD", "register:40f0:8", ["const:bb6e2c:8", "const:4:8"]]
+ 00bb6e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb6a04 bytes 2b840294
+ 00bb6e2c bytes 21840294
- 00bb6a38 ["INT_ADD", "register:40f0:8", ["const:bb6a38:8", "const:4:8"]]
- 00bb6a38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb6e60 ["INT_ADD", "register:40f0:8", ["const:bb6e60:8", "const:4:8"]]
+ 00bb6e60 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb6a38 bytes 1e840294
+ 00bb6e60 bytes 14840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e1583fa297773d403dfcfb9f819729b"></a>

### [`00bb6aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md) → [`00bb6f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md) _ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf70.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfe0.md) [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md)
- 新版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d370.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3e0.md) [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md#insn-00bb6b14) · [`00bb6b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md#insn-00bb6b1c) · [`00bb6b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md#insn-00bb6b48)
- 新版 `00bb6f3c`（命令位置の公開資料なし） · `00bb6f44`（命令位置の公開資料なし） · `00bb6f70`（命令位置の公開資料なし）

~~~diff
- 00bb6b14 ["INT_ADD", "register:40f0:8", ["const:bb6b14:8", "const:4:8"]]
- 00bb6b14 ["CALL", null, ["callee:00c5d3e0:8"]]
+ 00bb6f3c ["INT_ADD", "register:40f0:8", ["const:bb6f3c:8", "const:4:8"]]
+ 00bb6f3c ["CALL", null, ["callee:00c5d3e0:8"]]
- 00bb6b14 bytes 33990294
+ 00bb6f3c bytes 29990294
- 00bb6b1c ["INT_ADD", "register:40f0:8", ["const:bb6b1c:8", "const:4:8"]]
- 00bb6b1c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb6f44 ["INT_ADD", "register:40f0:8", ["const:bb6f44:8", "const:4:8"]]
+ 00bb6f44 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6b1c bytes b98e0294
+ 00bb6f44 bytes af8e0294
- 00bb6b48 ["INT_ADD", "register:40f0:8", ["const:bb6b48:8", "const:4:8"]]
- 00bb6b48 ["CALL", null, ["callee:00c5d4b0:8"]]
+ 00bb6f70 ["INT_ADD", "register:40f0:8", ["const:bb6f70:8", "const:4:8"]]
+ 00bb6f70 ["CALL", null, ["callee:00c5d4b0:8"]]
- 00bb6b48 bytes 5a990294
+ 00bb6f70 bytes 50990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49a86e94abe9b555fe474ad64446732"></a>

### [`00bb6c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c00.md) → [`00bb7028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7028.md) _ZN8firebase9messaging20PollableListenerImpl15OnTokenReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf10.md) · 呼出先 4件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d310.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c00.md#insn-00bb6c18) · [`00bb6c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c00.md#insn-00bb6c24) · [`00bb6c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c00.md#insn-00bb6c34)
- 新版 `00bb7040`（命令位置の公開資料なし） · `00bb704c`（命令位置の公開資料なし） · `00bb705c`（命令位置の公開資料なし）

~~~diff
- 00bb6c18 ["INT_ADD", "register:40f0:8", ["const:bb6c18:8", "const:4:8"]]
- 00bb6c18 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb7040 ["INT_ADD", "register:40f0:8", ["const:bb7040:8", "const:4:8"]]
+ 00bb7040 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6c18 bytes 7a8e0294
+ 00bb7040 bytes 708e0294
- 00bb6c24 ["INT_ADD", "register:40f0:8", ["const:bb6c24:8", "const:4:8"]]
- 00bb6c24 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bb704c ["INT_ADD", "register:40f0:8", ["const:bb704c:8", "const:4:8"]]
+ 00bb704c ["CALL", null, ["callee:00c57fe0:8"]]
- 00bb6c24 bytes ef830294
+ 00bb704c bytes e5830294
- 00bb6c34 ["INT_ADD", "register:40f0:8", ["const:bb6c34:8", "const:4:8"]]
- 00bb6c34 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb705c ["INT_ADD", "register:40f0:8", ["const:bb705c:8", "const:4:8"]]
+ 00bb705c ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb6c34 bytes 1f900294
+ 00bb705c bytes 15900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab560f72016c4284d22a2eeed43a0cd0"></a>

### [`00bb6c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c74.md) → [`00bb709c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb709c.md) _ZN8firebase9messaging20PollableListenerImpl22OnRegistrationReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf50.md) · 呼出先 4件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d350.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c74.md#insn-00bb6c8c) · [`00bb6c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c74.md#insn-00bb6c98) · [`00bb6ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6c74.md#insn-00bb6ca8)
- 新版 `00bb70b4`（命令位置の公開資料なし） · `00bb70c0`（命令位置の公開資料なし） · `00bb70d0`（命令位置の公開資料なし）

~~~diff
- 00bb6c8c ["INT_ADD", "register:40f0:8", ["const:bb6c8c:8", "const:4:8"]]
- 00bb6c8c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb70b4 ["INT_ADD", "register:40f0:8", ["const:bb70b4:8", "const:4:8"]]
+ 00bb70b4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6c8c bytes 5d8e0294
+ 00bb70b4 bytes 538e0294
- 00bb6c98 ["INT_ADD", "register:40f0:8", ["const:bb6c98:8", "const:4:8"]]
- 00bb6c98 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bb70c0 ["INT_ADD", "register:40f0:8", ["const:bb70c0:8", "const:4:8"]]
+ 00bb70c0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bb6c98 bytes d2830294
+ 00bb70c0 bytes c8830294
- 00bb6ca8 ["INT_ADD", "register:40f0:8", ["const:bb6ca8:8", "const:4:8"]]
- 00bb6ca8 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb70d0 ["INT_ADD", "register:40f0:8", ["const:bb70d0:8", "const:4:8"]]
+ 00bb70d0 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb6ca8 bytes 02900294
+ 00bb70d0 bytes f88f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84432d9b4ab4ffd7191b42dfe49dff10"></a>

### [`00bb6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ce8.md) → [`00bb7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7110.md) _ZN8firebase9messaging20PollableListenerImpl24OnUnregistrationReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf60.md) · 呼出先 4件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d360.md) · 呼出先 4件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ce8.md#insn-00bb6d00) · [`00bb6d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ce8.md#insn-00bb6d0c) · [`00bb6d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ce8.md#insn-00bb6d1c)
- 新版 `00bb7128`（命令位置の公開資料なし） · `00bb7134`（命令位置の公開資料なし） · `00bb7144`（命令位置の公開資料なし）

~~~diff
- 00bb6d00 ["INT_ADD", "register:40f0:8", ["const:bb6d00:8", "const:4:8"]]
- 00bb6d00 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb7128 ["INT_ADD", "register:40f0:8", ["const:bb7128:8", "const:4:8"]]
+ 00bb7128 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6d00 bytes 408e0294
+ 00bb7128 bytes 368e0294
- 00bb6d0c ["INT_ADD", "register:40f0:8", ["const:bb6d0c:8", "const:4:8"]]
- 00bb6d0c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bb7134 ["INT_ADD", "register:40f0:8", ["const:bb7134:8", "const:4:8"]]
+ 00bb7134 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bb6d0c bytes b5830294
+ 00bb7134 bytes ab830294
- 00bb6d1c ["INT_ADD", "register:40f0:8", ["const:bb6d1c:8", "const:4:8"]]
- 00bb6d1c ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb7144 ["INT_ADD", "register:40f0:8", ["const:bb7144:8", "const:4:8"]]
+ 00bb7144 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb6d1c bytes e58f0294
+ 00bb7144 bytes db8f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea0c78fb1ae1e579781c21490c83c2e"></a>

### [`00bb6e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6e4c.md) → [`00bb7274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7274.md) _ZN8firebase9messaging16PollableListener21PollRegistrationTokenEPb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6e4c.md#insn-00bb6e70)
- 新版 `00bb7298`（命令位置の公開資料なし）

~~~diff
- 00bb6e70 ["INT_ADD", "register:40f0:8", ["const:bb6e70:8", "const:4:8"]]
- 00bb6e70 ["CALL", null, ["callee:00c5d340:8"]]
+ 00bb7298 ["INT_ADD", "register:40f0:8", ["const:bb7298:8", "const:4:8"]]
+ 00bb7298 ["CALL", null, ["callee:00c5d340:8"]]
- 00bb6e70 bytes 34980294
+ 00bb7298 bytes 2a980294
~~~


<a id="compare-89aaa9c5721be5faa77d3c52937f2634"></a>

### [`00bb6ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md) → [`00bb72cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb72cc.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf40.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d340.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md#insn-00bb6ebc) · [`00bb6ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md#insn-00bb6ef4) · [`00bb6f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md#insn-00bb6f2c)
- 新版 `00bb72e4`（命令位置の公開資料なし） · `00bb731c`（命令位置の公開資料なし） · `00bb7354`（命令位置の公開資料なし）

~~~diff
- 00bb6ebc ["INT_ADD", "register:40f0:8", ["const:bb6ebc:8", "const:4:8"]]
- 00bb6ebc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb72e4 ["INT_ADD", "register:40f0:8", ["const:bb72e4:8", "const:4:8"]]
+ 00bb72e4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6ebc bytes d18d0294
+ 00bb72e4 bytes c78d0294
- 00bb6ef4 ["INT_ADD", "register:40f0:8", ["const:bb6ef4:8", "const:4:8"]]
- 00bb6ef4 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb731c ["INT_ADD", "register:40f0:8", ["const:bb731c:8", "const:4:8"]]
+ 00bb731c ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb6ef4 bytes 6f8f0294
+ 00bb731c bytes 658f0294
- 00bb6f2c ["INT_ADD", "register:40f0:8", ["const:bb6f2c:8", "const:4:8"]]
- 00bb6f2c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bb7354 ["INT_ADD", "register:40f0:8", ["const:bb7354:8", "const:4:8"]]
+ 00bb7354 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bb6f2c bytes b98d0294
+ 00bb7354 bytes af8d0294
~~~


<a id="compare-93432fc9b5661a15f080f2e900cfb303"></a>

### [`00bb6f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6f60.md) → [`00bb7388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7388.md) _ZN8firebase9messaging16PollableListener16PollRegistrationEPb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cf20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6f60.md#insn-00bb6f84)
- 新版 `00bb73ac`（命令位置の公開資料なし）

~~~diff
- 00bb6f84 ["INT_ADD", "register:40f0:8", ["const:bb6f84:8", "const:4:8"]]
- 00bb6f84 ["CALL", null, ["callee:00c5d320:8"]]
+ 00bb73ac ["INT_ADD", "register:40f0:8", ["const:bb73ac:8", "const:4:8"]]
+ 00bb73ac ["CALL", null, ["callee:00c5d320:8"]]
- 00bb6f84 bytes e7970294
+ 00bb73ac bytes dd970294
~~~


<a id="compare-432ac841d4377a71e88ec908a2d06acd"></a>

### [`00bb6fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6fb8.md) → [`00bb73e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb73e0.md) _ZN8firebase9messaging20PollableListenerImpl16PollRegistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf20.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d320.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6fb8.md#insn-00bb6fd0) · [`00bb7008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6fb8.md#insn-00bb7008) · [`00bb7040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6fb8.md#insn-00bb7040)
- 新版 `00bb73f8`（命令位置の公開資料なし） · `00bb7430`（命令位置の公開資料なし） · `00bb7468`（命令位置の公開資料なし）

~~~diff
- 00bb6fd0 ["INT_ADD", "register:40f0:8", ["const:bb6fd0:8", "const:4:8"]]
- 00bb6fd0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb73f8 ["INT_ADD", "register:40f0:8", ["const:bb73f8:8", "const:4:8"]]
+ 00bb73f8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6fd0 bytes 8c8d0294
+ 00bb73f8 bytes 828d0294
- 00bb7008 ["INT_ADD", "register:40f0:8", ["const:bb7008:8", "const:4:8"]]
- 00bb7008 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb7430 ["INT_ADD", "register:40f0:8", ["const:bb7430:8", "const:4:8"]]
+ 00bb7430 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb7008 bytes 2a8f0294
+ 00bb7430 bytes 208f0294
- 00bb7040 ["INT_ADD", "register:40f0:8", ["const:bb7040:8", "const:4:8"]]
- 00bb7040 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bb7468 ["INT_ADD", "register:40f0:8", ["const:bb7468:8", "const:4:8"]]
+ 00bb7468 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bb7040 bytes 748d0294
+ 00bb7468 bytes 6a8d0294
~~~


<a id="compare-9f1ee7cbf20309acba029560846676dc"></a>

### [`00bb7074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7074.md) → [`00bb749c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb749c.md) _ZN8firebase9messaging16PollableListener18PollUnregistrationEPb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7074.md#insn-00bb7098)
- 新版 `00bb74c0`（命令位置の公開資料なし）

~~~diff
- 00bb7098 ["INT_ADD", "register:40f0:8", ["const:bb7098:8", "const:4:8"]]
- 00bb7098 ["CALL", null, ["callee:00c5d330:8"]]
+ 00bb74c0 ["INT_ADD", "register:40f0:8", ["const:bb74c0:8", "const:4:8"]]
+ 00bb74c0 ["CALL", null, ["callee:00c5d330:8"]]
- 00bb7098 bytes a6970294
+ 00bb74c0 bytes 9c970294
~~~


<a id="compare-6ce48192803e3168d9961fbde6049220"></a>

### [`00bb70cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb70cc.md) → [`00bb74f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb74f4.md) _ZN8firebase9messaging20PollableListenerImpl18PollUnregistrationEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf30.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d330.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb70e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb70cc.md#insn-00bb70e4) · [`00bb711c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb70cc.md#insn-00bb711c) · [`00bb7154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb70cc.md#insn-00bb7154)
- 新版 `00bb750c`（命令位置の公開資料なし） · `00bb7544`（命令位置の公開資料なし） · `00bb757c`（命令位置の公開資料なし）

~~~diff
- 00bb70e4 ["INT_ADD", "register:40f0:8", ["const:bb70e4:8", "const:4:8"]]
- 00bb70e4 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb750c ["INT_ADD", "register:40f0:8", ["const:bb750c:8", "const:4:8"]]
+ 00bb750c ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb70e4 bytes 478d0294
+ 00bb750c bytes 3d8d0294
- 00bb711c ["INT_ADD", "register:40f0:8", ["const:bb711c:8", "const:4:8"]]
- 00bb711c ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bb7544 ["INT_ADD", "register:40f0:8", ["const:bb7544:8", "const:4:8"]]
+ 00bb7544 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bb711c bytes e58e0294
+ 00bb7544 bytes db8e0294
- 00bb7154 ["INT_ADD", "register:40f0:8", ["const:bb7154:8", "const:4:8"]]
- 00bb7154 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bb757c ["INT_ADD", "register:40f0:8", ["const:bb757c:8", "const:4:8"]]
+ 00bb757c ["CALL", null, ["callee:00c5aa10:8"]]
- 00bb7154 bytes 2f8d0294
+ 00bb757c bytes 258d0294
~~~


<a id="compare-fdd02d4e564e6d96ffb9a1febe274212"></a>

### [`00bb7250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7250.md) → [`00bb7678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7678.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d060.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md)
- 新版 呼出元 1件 [`00c5d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d460.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb72d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7250.md#insn-00bb72d0) · [`00bb7314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7250.md#insn-00bb7314)
- 新版 `00bb76f8`（命令位置の公開資料なし） · `00bb773c`（命令位置の公開資料なし）

~~~diff
- 00bb72d0 ["INT_ADD", "register:40f0:8", ["const:bb72d0:8", "const:4:8"]]
- 00bb72d0 ["CALL", null, ["callee:00c5d3f0:8"]]
+ 00bb76f8 ["INT_ADD", "register:40f0:8", ["const:bb76f8:8", "const:4:8"]]
+ 00bb76f8 ["CALL", null, ["callee:00c5d3f0:8"]]
- 00bb72d0 bytes 48970294
+ 00bb76f8 bytes 3e970294
- 00bb7314 ["INT_ADD", "register:40f0:8", ["const:bb7314:8", "const:4:8"]]
- 00bb7314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb773c ["INT_ADD", "register:40f0:8", ["const:bb773c:8", "const:4:8"]]
+ 00bb773c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb7314 bytes e7810294
+ 00bb773c bytes dd810294
~~~


<a id="compare-70b9fe29234ea9315a28b04cea90dfbe"></a>

### [`00bb7368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md) → [`00bb7790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7790.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md) · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ced0.md)
- 新版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3f0.md) · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md#insn-00bb7384) · [`00bb738c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md#insn-00bb738c) · [`00bb73d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md#insn-00bb73d4)
- 新版 `00bb77ac`（命令位置の公開資料なし） · `00bb77b4`（命令位置の公開資料なし） · `00bb77fc`（命令位置の公開資料なし）

~~~diff
- 00bb7384 ["INT_ADD", "register:40f0:8", ["const:bb7384:8", "const:4:8"]]
- 00bb7384 ["CALL", null, ["callee:00c5d2d0:8"]]
+ 00bb77ac ["INT_ADD", "register:40f0:8", ["const:bb77ac:8", "const:4:8"]]
+ 00bb77ac ["CALL", null, ["callee:00c5d2d0:8"]]
- 00bb7384 bytes d3960294
+ 00bb77ac bytes c9960294
- 00bb738c ["INT_ADD", "register:40f0:8", ["const:bb738c:8", "const:4:8"]]
- 00bb738c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb77b4 ["INT_ADD", "register:40f0:8", ["const:bb77b4:8", "const:4:8"]]
+ 00bb77b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb738c bytes c9810294
+ 00bb77b4 bytes bf810294
- 00bb73d4 ["INT_ADD", "register:40f0:8", ["const:bb73d4:8", "const:4:8"]]
- 00bb73d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb77fc ["INT_ADD", "register:40f0:8", ["const:bb77fc:8", "const:4:8"]]
+ 00bb77fc ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb73d4 bytes b7810294
+ 00bb77fc bytes ad810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5425ae848194481c0a025943bd0cd2b"></a>

### [`00bb74ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb74ac.md) → [`00bb78d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb78d4.md) _ZN8firebase9messaging12NotificationD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ced0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb74d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb74ac.md#insn-00bb74d4) · [`00bb74dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb74ac.md#insn-00bb74dc) · [`00bb7518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb74ac.md#insn-00bb7518)
- 新版 `00bb78fc`（命令位置の公開資料なし） · `00bb7904`（命令位置の公開資料なし） · `00bb7940`（命令位置の公開資料なし）

~~~diff
- 00bb74d4 ["INT_ADD", "register:40f0:8", ["const:bb74d4:8", "const:4:8"]]
- 00bb74d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb78fc ["INT_ADD", "register:40f0:8", ["const:bb78fc:8", "const:4:8"]]
+ 00bb78fc ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb74d4 bytes 77810294
+ 00bb78fc bytes 6d810294
- 00bb74dc ["INT_ADD", "register:40f0:8", ["const:bb74dc:8", "const:4:8"]]
- 00bb74dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb7904 ["INT_ADD", "register:40f0:8", ["const:bb7904:8", "const:4:8"]]
+ 00bb7904 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb74dc bytes 75810294
+ 00bb7904 bytes 6b810294
- 00bb7518 ["INT_ADD", "register:40f0:8", ["const:bb7518:8", "const:4:8"]]
- 00bb7518 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb7940 ["INT_ADD", "register:40f0:8", ["const:bb7940:8", "const:4:8"]]
+ 00bb7940 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb7518 bytes 66810294
+ 00bb7940 bytes 5c810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e3d36214ae42444c184bd8bc4ae8caa"></a>

### [`00bb7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7684.md) → [`00bb7aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7aac.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfe0.md) · 呼出先 1件 [`00c5d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d000.md)
- 新版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3e0.md) · 呼出先 1件 [`00c5d400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb76f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7684.md#insn-00bb76f4)
- 新版 `00bb7b1c`（命令位置の公開資料なし）

~~~diff
- 00bb76f4 ["INT_ADD", "register:40f0:8", ["const:bb76f4:8", "const:4:8"]]
- 00bb76f4 ["CALL", null, ["callee:00c5d400:8"]]
+ 00bb7b1c ["INT_ADD", "register:40f0:8", ["const:bb7b1c:8", "const:4:8"]]
+ 00bb7b1c ["CALL", null, ["callee:00c5d400:8"]]
- 00bb76f4 bytes 43960294
+ 00bb7b1c bytes 39960294
~~~


<a id="compare-62fe88cbcec1a676a1e71aba802c9852"></a>

### [`00bb7a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md) → [`00bb7e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7e80.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cec0.md) · 呼出先 1件 [`00c5cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cee0.md)
- 新版 呼出元 1件 [`00c5d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2c0.md) · 呼出先 1件 [`00c5d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md#insn-00bb7a98)
- 新版 `00bb7ec0`（命令位置の公開資料なし）

~~~diff
- 00bb7a98 ["INT_ADD", "register:40f0:8", ["const:bb7a98:8", "const:4:8"]]
- 00bb7a98 ["CALL", null, ["callee:00c5d2e0:8"]]
+ 00bb7ec0 ["INT_ADD", "register:40f0:8", ["const:bb7ec0:8", "const:4:8"]]
+ 00bb7ec0 ["CALL", null, ["callee:00c5d2e0:8"]]
- 00bb7a98 bytes 12950294
+ 00bb7ec0 bytes 08950294
~~~


<a id="compare-4fc163bbef44f97d874b9c39451763c1"></a>

### [`00bb7c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md) → [`00bb8070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8070.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0c0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4c0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md#insn-00bb7c8c) · [`00bb7ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md#insn-00bb7ce8) · [`00bb7d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md#insn-00bb7d10)
- 新版 `00bb80b4`（命令位置の公開資料なし） · `00bb8110`（命令位置の公開資料なし） · `00bb8138`（命令位置の公開資料なし）

~~~diff
- 00bb7c8c ["INT_ADD", "register:40f0:8", ["const:bb7c8c:8", "const:4:8"]]
- 00bb7c8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb80b4 ["INT_ADD", "register:40f0:8", ["const:bb80b4:8", "const:4:8"]]
+ 00bb80b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb7c8c bytes 897f0294
+ 00bb80b4 bytes 7f7f0294
- 00bb7ce8 ["INT_ADD", "register:40f0:8", ["const:bb7ce8:8", "const:4:8"]]
- 00bb7ce8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bb8110 ["INT_ADD", "register:40f0:8", ["const:bb8110:8", "const:4:8"]]
+ 00bb8110 ["CALL", null, ["callee:00c57f40:8"]]
- 00bb7ce8 bytes 967f0294
+ 00bb8110 bytes 8c7f0294
- 00bb7d10 ["INT_ADD", "register:40f0:8", ["const:bb7d10:8", "const:4:8"]]
- 00bb7d10 ["CALL", null, ["callee:00c58000:8"]]
+ 00bb8138 ["INT_ADD", "register:40f0:8", ["const:bb8138:8", "const:4:8"]]
+ 00bb8138 ["CALL", null, ["callee:00c58000:8"]]
- 00bb7d10 bytes bc7f0294
+ 00bb8138 bytes b27f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-374695906177440833a76d853a648241"></a>

### [`00bb9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9210.md) → [`00bb9638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9638.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9210.md#insn-00bb9230)
- 新版 `00bb9658`（命令位置の公開資料なし）

~~~diff
- 00bb9230 ["INT_ADD", "register:40f0:8", ["const:bb9230:8", "const:4:8"]]
- 00bb9230 ["CALL", null, ["callee:00c5d580:8"]]
+ 00bb9658 ["INT_ADD", "register:40f0:8", ["const:bb9658:8", "const:4:8"]]
+ 00bb9658 ["CALL", null, ["callee:00c5d580:8"]]
- 00bb9230 bytes d48f0294
+ 00bb9658 bytes ca8f0294
~~~


