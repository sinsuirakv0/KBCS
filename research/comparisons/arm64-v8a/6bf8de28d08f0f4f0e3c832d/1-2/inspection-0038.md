# v16.0.1 → v16.0.2 · 要調査の変更候補 (38)

[一覧の目次](README.md)

<a id="compare-7ad541359170d1da9bc586cc24894822"></a>

### [`00b5deec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5deec.md) → [`00b5df88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md) _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5bbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5df18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5deec.md#insn-00b5df18) · [`00b5df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5deec.md#insn-00b5df50) · [`00b5df68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5deec.md#insn-00b5df68)
- 新版 [`00b5dfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5dfb4) · [`00b5dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5dfec) · [`00b5e004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5e004)

~~~diff
- 00b5df18 ["INT_ADD", "register:40f0:8", ["const:b5df18:8", "const:4:8"]]
- 00b5df18 ["CALL", null, ["callee:00c5bcb0:8"]]
+ 00b5dfb4 ["INT_ADD", "register:40f0:8", ["const:b5dfb4:8", "const:4:8"]]
+ 00b5dfb4 ["CALL", null, ["callee:00c5bcb0:8"]]
- 00b5df18 bytes 32f70394
+ 00b5dfb4 bytes 3ff70394
- 00b5df50 ["INT_ADD", "register:40f0:8", ["const:b5df50:8", "const:4:8"]]
- 00b5df50 ["CALL", null, ["callee:00c5b180:8"]]
+ 00b5dfec ["INT_ADD", "register:40f0:8", ["const:b5dfec:8", "const:4:8"]]
+ 00b5dfec ["CALL", null, ["callee:00c5b180:8"]]
- 00b5df50 bytes 58f40394
+ 00b5dfec bytes 65f40394
- 00b5df68 ["INT_ADD", "register:40f0:8", ["const:b5df68:8", "const:4:8"]]
- 00b5df68 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b5e004 ["INT_ADD", "register:40f0:8", ["const:b5e004:8", "const:4:8"]]
+ 00b5e004 ["CALL", null, ["callee:00c57f80:8"]]
- 00b5df68 bytes d2e70394
+ 00b5e004 bytes dfe70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea8ad66cd04c0c0a6b6f257539b2e75"></a>

### [`00b5dfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dfa4.md) → [`00b5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md) _ZN8firebase4Path11GetRelativeERKS0_S2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbe0.md) · 呼出先 6件 [`00b5d458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d458.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcb0.md) · 呼出先 6件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5dfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dfa4.md#insn-00b5dfd8) · [`00b5dfe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dfa4.md#insn-00b5dfe4) · [`00b5e0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dfa4.md#insn-00b5e0a0)
- 新版 [`00b5e074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e074) · [`00b5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e080) · [`00b5e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e13c)

~~~diff
- 00b5dfd8 ["INT_ADD", "register:40f0:8", ["const:b5dfd8:8", "const:4:8"]]
- 00b5dfd8 ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5e074 ["INT_ADD", "register:40f0:8", ["const:b5e074:8", "const:4:8"]]
+ 00b5e074 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5dfd8 bytes 0af70394
+ 00b5e074 bytes 17f70394
- 00b5dfe4 ["INT_ADD", "register:40f0:8", ["const:b5dfe4:8", "const:4:8"]]
- 00b5dfe4 ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5e080 ["INT_ADD", "register:40f0:8", ["const:b5e080:8", "const:4:8"]]
+ 00b5e080 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5dfe4 bytes 07f70394
+ 00b5e080 bytes 14f70394
- 00b5e0a0 ["INT_ADD", "register:40f0:8", ["const:b5e0a0:8", "const:4:8"]]
- 00b5e0a0 ["CALL", null, ["callee:00c58120:8"]]
+ 00b5e13c ["INT_ADD", "register:40f0:8", ["const:b5e13c:8", "const:4:8"]]
+ 00b5e13c ["CALL", null, ["callee:00c58120:8"]]
- 00b5e0a0 bytes ece70394
+ 00b5e13c bytes f9e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de058a448a723ebd191a8ae87c0ce921"></a>

### [`00b5e65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e65c.md) → [`00b5e6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc20.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)
- 新版 呼出元 1件 [`00c5bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcf0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e65c.md#insn-00b5e76c) · [`00b5e798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e65c.md#insn-00b5e798) · [`00b5e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e65c.md#insn-00b5e828)
- 新版 [`00b5e808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e808) · [`00b5e834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e834) · [`00b5e8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e8c4)

~~~diff
- 00b5e76c ["INT_ADD", "register:40f0:8", ["const:b5e76c:8", "const:4:8"]]
- 00b5e76c ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00b5e808 ["INT_ADD", "register:40f0:8", ["const:b5e808:8", "const:4:8"]]
+ 00b5e808 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00b5e76c bytes 5df00394
+ 00b5e808 bytes 6af00394
- 00b5e798 ["INT_ADD", "register:40f0:8", ["const:b5e798:8", "const:4:8"]]
- 00b5e798 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b5e834 ["INT_ADD", "register:40f0:8", ["const:b5e834:8", "const:4:8"]]
+ 00b5e834 ["CALL", null, ["callee:00c57f60:8"]]
- 00b5e798 bytes bee50394
+ 00b5e834 bytes cbe50394
- 00b5e828 ["INT_ADD", "register:40f0:8", ["const:b5e828:8", "const:4:8"]]
- 00b5e828 ["CALL", null, ["callee:00c5bcf0:8"]]
+ 00b5e8c4 ["INT_ADD", "register:40f0:8", ["const:b5e8c4:8", "const:4:8"]]
+ 00b5e8c4 ["CALL", null, ["callee:00c5bcf0:8"]]
- 00b5e828 bytes fef40394
+ 00b5e8c4 bytes 0bf50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7262771a5f5f231ddc7715519b6df3"></a>

### [`00b5ebd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ebd4.md) → [`00b5ec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc80.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5bd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd50.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ec00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ebd4.md#insn-00b5ec00) · [`00b5ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ebd4.md#insn-00b5ec1c) · [`00b5ec78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ebd4.md#insn-00b5ec78)
- 新版 [`00b5ec9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ec9c) · [`00b5ecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ecb8) · [`00b5ed14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ed14)

~~~diff
- 00b5ec00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ec00 ["INT_ADD", "register:40f0:8", ["const:b5ec00:8", "const:4:8"]]
- 00b5ec00 ["CALLIND", null, ["register:0:8"]]
+ 00b5ec9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ec9c ["INT_ADD", "register:40f0:8", ["const:b5ec9c:8", "const:4:8"]]
+ 00b5ec9c ["CALLIND", null, ["register:0:8"]]
- 00b5ec00 bytes 00013fd6
+ 00b5ec9c bytes 00013fd6
- 00b5ec1c ["INT_ADD", "register:40f0:8", ["const:b5ec1c:8", "const:4:8"]]
- 00b5ec1c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b5ecb8 ["INT_ADD", "register:40f0:8", ["const:b5ecb8:8", "const:4:8"]]
+ 00b5ecb8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b5ec1c bytes a5e40394
+ 00b5ecb8 bytes b2e40394
- 00b5ec78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ec78 ["INT_ADD", "register:40f0:8", ["const:b5ec78:8", "const:4:8"]]
- 00b5ec78 ["CALLIND", null, ["register:0:8"]]
+ 00b5ed14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ed14 ["INT_ADD", "register:40f0:8", ["const:b5ed14:8", "const:4:8"]]
+ 00b5ed14 ["CALLIND", null, ["register:0:8"]]
- 00b5ec78 bytes 00013fd6
+ 00b5ed14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876873d61703f77779b2bdb8775d80b6"></a>

### [`00b5eec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5eec8.md) → [`00b5ef64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ef64.md) _ZN8firebase26ReferenceCountedFutureImplD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bcd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5eed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5eec8.md#insn-00b5eed8)
- 新版 [`00b5ef74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ef64.md#insn-00b5ef74)

~~~diff
- 00b5eed8 ["INT_ADD", "register:40f0:8", ["const:b5eed8:8", "const:4:8"]]
- 00b5eed8 ["CALL", null, ["callee:00c5bda0:8"]]
+ 00b5ef74 ["INT_ADD", "register:40f0:8", ["const:b5ef74:8", "const:4:8"]]
+ 00b5ef74 ["CALL", null, ["callee:00c5bda0:8"]]
- 00b5eed8 bytes 7ef30394
+ 00b5ef74 bytes 8bf30394
~~~


<a id="compare-f6c3f5eb8031c0387be268aab89a45dd"></a>

### [`00b5f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f59c.md) → [`00b5f638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae80.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af50.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f59c.md#insn-00b5f5bc) · [`00b5f608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f59c.md#insn-00b5f608)
- 新版 [`00b5f658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md#insn-00b5f658) · [`00b5f6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md#insn-00b5f6a4)

~~~diff
- 00b5f5bc ["INT_ADD", "register:40f0:8", ["const:b5f5bc:8", "const:4:8"]]
- 00b5f5bc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5f658 ["INT_ADD", "register:40f0:8", ["const:b5f658:8", "const:4:8"]]
+ 00b5f658 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5f5bc bytes 11ed0394
+ 00b5f658 bytes 1eed0394
- 00b5f608 ["INT_ADD", "register:40f0:8", ["const:b5f608:8", "const:4:8"]]
- 00b5f608 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b5f6a4 ["INT_ADD", "register:40f0:8", ["const:b5f6a4:8", "const:4:8"]]
+ 00b5f6a4 ["CALL", null, ["callee:00c5aae0:8"]]
- 00b5f608 bytes 02ed0394
+ 00b5f6a4 bytes 0fed0394
~~~


<a id="compare-496c9d85e425bb6228ce7f2880baf31d"></a>

### [`00b5f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9b8.md) → [`00b5fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b070.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5b140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b140.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9b8.md#insn-00b5f9d0) · [`00b5f9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9b8.md#insn-00b5f9dc)
- 新版 [`00b5fa6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md#insn-00b5fa6c) · [`00b5fa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md#insn-00b5fa78)

~~~diff
- 00b5f9d0 ["INT_ADD", "register:40f0:8", ["const:b5f9d0:8", "const:4:8"]]
- 00b5f9d0 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5fa6c ["INT_ADD", "register:40f0:8", ["const:b5fa6c:8", "const:4:8"]]
+ 00b5fa6c ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5f9d0 bytes 0cec0394
+ 00b5fa6c bytes 19ec0394
- 00b5f9dc ["INT_ADD", "register:40f0:8", ["const:b5f9dc:8", "const:4:8"]]
- 00b5f9dc ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b5fa78 ["INT_ADD", "register:40f0:8", ["const:b5fa78:8", "const:4:8"]]
+ 00b5fa78 ["CALL", null, ["callee:00c5aae0:8"]]
- 00b5f9dc bytes 0dec0394
+ 00b5fa78 bytes 1aec0394
~~~


<a id="compare-d9b13bda7da3f5f9e71273bfe48dad8b"></a>

### [`00b5fa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa00.md) → [`00b5fa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md) FUN_00b5fa9c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5f9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f9f0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00b5fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa8c.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa00.md#insn-00b5fa10) · [`00b5fa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa00.md#insn-00b5fa28) · [`00b5fa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa00.md#insn-00b5fa3c)
- 新版 [`00b5faac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5faac) · [`00b5fac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5fac4) · [`00b5fad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5fad8)

~~~diff
- 00b5fa10 ["INT_ADD", "register:40f0:8", ["const:b5fa10:8", "const:4:8"]]
- 00b5fa10 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5faac ["INT_ADD", "register:40f0:8", ["const:b5faac:8", "const:4:8"]]
+ 00b5faac ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5fa10 bytes fceb0394
+ 00b5faac bytes 09ec0394
- 00b5fa28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5fa28 ["INT_ADD", "register:40f0:8", ["const:b5fa28:8", "const:4:8"]]
- 00b5fa28 ["CALLIND", null, ["register:0:8"]]
+ 00b5fac4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fac4 ["INT_ADD", "register:40f0:8", ["const:b5fac4:8", "const:4:8"]]
+ 00b5fac4 ["CALLIND", null, ["register:0:8"]]
- 00b5fa28 bytes 00013fd6
+ 00b5fac4 bytes 00013fd6
- 00b5fa3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5fa3c ["INT_ADD", "register:40f0:8", ["const:b5fa3c:8", "const:4:8"]]
- 00b5fa3c ["CALLIND", null, ["register:0:8"]]
+ 00b5fad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fad8 ["INT_ADD", "register:40f0:8", ["const:b5fad8:8", "const:4:8"]]
+ 00b5fad8 ["CALLIND", null, ["register:0:8"]]
- 00b5fa3c bytes 00013fd6
+ 00b5fad8 bytes 00013fd6
~~~


<a id="compare-896aef138702581a75b6a227fb4a6acc"></a>

### [`00b5fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fc1c.md) → [`00b5fcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fc1c.md#insn-00b5fc3c) · [`00b5fc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fc1c.md#insn-00b5fc48) · [`00b5fc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fc1c.md#insn-00b5fc88)
- 新版 [`00b5fcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fcd8) · [`00b5fce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fce4) · [`00b5fd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fd24)

~~~diff
- 00b5fc3c ["INT_ADD", "register:40f0:8", ["const:b5fc3c:8", "const:4:8"]]
- 00b5fc3c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5fcd8 ["INT_ADD", "register:40f0:8", ["const:b5fcd8:8", "const:4:8"]]
+ 00b5fcd8 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5fc3c bytes 71eb0394
+ 00b5fcd8 bytes 7eeb0394
- 00b5fc48 ["INT_ADD", "register:40f0:8", ["const:b5fc48:8", "const:4:8"]]
- 00b5fc48 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5fce4 ["INT_ADD", "register:40f0:8", ["const:b5fce4:8", "const:4:8"]]
+ 00b5fce4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5fc48 bytes 6eeb0394
+ 00b5fce4 bytes 7beb0394
- 00b5fc88 ["INT_ADD", "register:40f0:8", ["const:b5fc88:8", "const:4:8"]]
- 00b5fc88 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b5fd24 ["INT_ADD", "register:40f0:8", ["const:b5fd24:8", "const:4:8"]]
+ 00b5fd24 ["CALL", null, ["callee:00c5aae0:8"]]
- 00b5fc88 bytes 62eb0394
+ 00b5fd24 bytes 6feb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be7fd2d46a091cb35fe6004ddc52d5b"></a>

### [`00b60090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md) → [`00b6012c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b600c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md#insn-00b600c8) · [`00b600d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md#insn-00b600d4) · [`00b60114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md#insn-00b60114)
- 新版 [`00b60164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b60164) · [`00b60170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b60170) · [`00b601b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b601b0)

~~~diff
- 00b600c8 ["INT_ADD", "register:40f0:8", ["const:b600c8:8", "const:4:8"]]
- 00b600c8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b60164 ["INT_ADD", "register:40f0:8", ["const:b60164:8", "const:4:8"]]
+ 00b60164 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b600c8 bytes 4eea0394
+ 00b60164 bytes 5bea0394
- 00b600d4 ["INT_ADD", "register:40f0:8", ["const:b600d4:8", "const:4:8"]]
- 00b600d4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b60170 ["INT_ADD", "register:40f0:8", ["const:b60170:8", "const:4:8"]]
+ 00b60170 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b600d4 bytes 4bea0394
+ 00b60170 bytes 58ea0394
- 00b60114 ["INT_ADD", "register:40f0:8", ["const:b60114:8", "const:4:8"]]
- 00b60114 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b601b0 ["INT_ADD", "register:40f0:8", ["const:b601b0:8", "const:4:8"]]
+ 00b601b0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00b60114 bytes 3fea0394
+ 00b601b0 bytes 4cea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d09b5a25abc8e0950fc83bbe39e7ac3"></a>

### [`00b60494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60494.md) → [`00b60530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md) FUN_00b60530

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b60284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60284.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)
- 新版 呼出元 1件 [`00b60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b604c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60494.md#insn-00b604c8)
- 新版 [`00b60564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md#insn-00b60564)

~~~diff
- 00b604c8 ["INT_ADD", "register:40f0:8", ["const:b604c8:8", "const:4:8"]]
- 00b604c8 ["CALL", null, ["callee:00b611c8:8"]]
+ 00b60564 ["INT_ADD", "register:40f0:8", ["const:b60564:8", "const:4:8"]]
+ 00b60564 ["CALL", null, ["callee:00b611c8:8"]]
- 00b604c8 bytes 19030094
+ 00b60564 bytes 19030094
~~~


<a id="compare-fc07c7e6f8bdc70fd84e5e0be1d3766c"></a>

### [`00b604cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b604cc.md) → [`00b60568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60568.md) FUN_00b60568

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b60284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60284.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b604cc.md#insn-00b60508)
- 新版 [`00b605a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60568.md#insn-00b605a4)

~~~diff
- 00b60508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60508 ["INT_ADD", "register:40f0:8", ["const:b60508:8", "const:4:8"]]
- 00b60508 ["CALLIND", null, ["register:0:8"]]
+ 00b605a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b605a4 ["INT_ADD", "register:40f0:8", ["const:b605a4:8", "const:4:8"]]
+ 00b605a4 ["CALLIND", null, ["register:0:8"]]
- 00b60508 bytes 00013fd6
+ 00b605a4 bytes 00013fd6
~~~


<a id="compare-49be804d428decddfc7a4982f9edf3c6"></a>

### [`00b6051c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b6051c.md) → [`00b605b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md) _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bce0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5bdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdb0.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b6051c.md#insn-00b60534) · [`00b605c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b6051c.md#insn-00b605c8)
- 新版 [`00b605d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md#insn-00b605d0) · [`00b60664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md#insn-00b60664)

~~~diff
- 00b60534 ["INT_ADD", "register:40f0:8", ["const:b60534:8", "const:4:8"]]
- 00b60534 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b605d0 ["INT_ADD", "register:40f0:8", ["const:b605d0:8", "const:4:8"]]
+ 00b605d0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b60534 bytes 33e90394
+ 00b605d0 bytes 40e90394
- 00b605c8 ["INT_ADD", "register:40f0:8", ["const:b605c8:8", "const:4:8"]]
- 00b605c8 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b60664 ["INT_ADD", "register:40f0:8", ["const:b60664:8", "const:4:8"]]
+ 00b60664 ["CALL", null, ["callee:00c5aae0:8"]]
- 00b605c8 bytes 12e90394
+ 00b60664 bytes 1fe90394
~~~


<a id="compare-da7a9a09b9711f3ffb8d578cca562845"></a>

### [`00b605dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b605dc.md) → [`00b60678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b605f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b605dc.md#insn-00b605f4) · [`00b60600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b605dc.md#insn-00b60600)
- 新版 [`00b60690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md#insn-00b60690) · [`00b6069c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md#insn-00b6069c)

~~~diff
- 00b605f4 ["INT_ADD", "register:40f0:8", ["const:b605f4:8", "const:4:8"]]
- 00b605f4 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b60690 ["INT_ADD", "register:40f0:8", ["const:b60690:8", "const:4:8"]]
+ 00b60690 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b605f4 bytes 03e90394
+ 00b60690 bytes 10e90394
- 00b60600 ["INT_ADD", "register:40f0:8", ["const:b60600:8", "const:4:8"]]
- 00b60600 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00b6069c ["INT_ADD", "register:40f0:8", ["const:b6069c:8", "const:4:8"]]
+ 00b6069c ["CALL", null, ["callee:00c5aae0:8"]]
- 00b60600 bytes 04e90394
+ 00b6069c bytes 11e90394
~~~


<a id="compare-910739ebe56b3632ee87c42553e5248b"></a>

### [`00b610e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b610e4.md) → [`00b61180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md) _ZN8firebase12FutureHandle6DetachEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) · 呼出先 1件 [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 1件 [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) · 呼出先 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b61104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b610e4.md#insn-00b61104) · [`00b61118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b610e4.md#insn-00b61118)
- 新版 [`00b611a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md#insn-00b611a0) · [`00b611b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md#insn-00b611b4)

~~~diff
- 00b61104 ["INT_ADD", "register:40f0:8", ["const:b61104:8", "const:4:8"]]
- 00b61104 ["CALL", null, ["callee:00c5ace0:8"]]
+ 00b611a0 ["INT_ADD", "register:40f0:8", ["const:b611a0:8", "const:4:8"]]
+ 00b611a0 ["CALL", null, ["callee:00c5ace0:8"]]
- 00b61104 bytes c3e60394
+ 00b611a0 bytes d0e60394
- 00b61118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61118 ["INT_ADD", "register:40f0:8", ["const:b61118:8", "const:4:8"]]
- 00b61118 ["CALLIND", null, ["register:0:8"]]
+ 00b611b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b611b4 ["INT_ADD", "register:40f0:8", ["const:b611b4:8", "const:4:8"]]
+ 00b611b4 ["CALLIND", null, ["register:0:8"]]
- 00b61118 bytes 00013fd6
+ 00b611b4 bytes 00013fd6
~~~


<a id="compare-534681310095c2d4b76d5ea51bfda294"></a>

### [`00b62a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62a5c.md) → [`00b62af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdb0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5be80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be80.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62a5c.md#insn-00b62ac0) · [`00b62acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62a5c.md#insn-00b62acc) · [`00b62af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62a5c.md#insn-00b62af8)
- 新版 [`00b62b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b5c) · [`00b62b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b68) · [`00b62b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b94)

~~~diff
- 00b62ac0 ["INT_ADD", "register:40f0:8", ["const:b62ac0:8", "const:4:8"]]
- 00b62ac0 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b62b5c ["INT_ADD", "register:40f0:8", ["const:b62b5c:8", "const:4:8"]]
+ 00b62b5c ["CALL", null, ["callee:00c5b210:8"]]
- 00b62ac0 bytes a0e10394
+ 00b62b5c bytes ade10394
- 00b62acc ["INT_ADD", "register:40f0:8", ["const:b62acc:8", "const:4:8"]]
- 00b62acc ["CALL", null, ["callee:00c57f60:8"]]
+ 00b62b68 ["INT_ADD", "register:40f0:8", ["const:b62b68:8", "const:4:8"]]
+ 00b62b68 ["CALL", null, ["callee:00c57f60:8"]]
- 00b62acc bytes f1d40394
+ 00b62b68 bytes fed40394
- 00b62af8 ["INT_ADD", "register:40f0:8", ["const:b62af8:8", "const:4:8"]]
- 00b62af8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b62b94 ["INT_ADD", "register:40f0:8", ["const:b62b94:8", "const:4:8"]]
+ 00b62b94 ["CALL", null, ["callee:00c580d0:8"]]
- 00b62af8 bytes 42d50394
+ 00b62b94 bytes 4fd50394
~~~


<a id="compare-2bed4c9c98b7a89bafab1e6b4fae7e93"></a>

### [`00b62b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b44.md) → [`00b62be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd80.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd80.md)
- 新版 呼出元 1件 [`00c5be50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be50.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5be50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b44.md#insn-00b62b60) · [`00b62b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b44.md#insn-00b62b6c) · [`00b62b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b44.md#insn-00b62b7c)
- 新版 [`00b62bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62bfc) · [`00b62c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62c08) · [`00b62c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62c18)

~~~diff
- 00b62b60 ["INT_ADD", "register:40f0:8", ["const:b62b60:8", "const:4:8"]]
- 00b62b60 ["CALL", null, ["callee:00c5be50:8"]]
+ 00b62bfc ["INT_ADD", "register:40f0:8", ["const:b62bfc:8", "const:4:8"]]
+ 00b62bfc ["CALL", null, ["callee:00c5be50:8"]]
- 00b62b60 bytes 88e40394
+ 00b62bfc bytes 95e40394
- 00b62b6c ["INT_ADD", "register:40f0:8", ["const:b62b6c:8", "const:4:8"]]
- 00b62b6c ["CALL", null, ["callee:00c5be50:8"]]
+ 00b62c08 ["INT_ADD", "register:40f0:8", ["const:b62c08:8", "const:4:8"]]
+ 00b62c08 ["CALL", null, ["callee:00c5be50:8"]]
- 00b62b6c bytes 85e40394
+ 00b62c08 bytes 92e40394
- 00b62b7c ["INT_ADD", "register:40f0:8", ["const:b62b7c:8", "const:4:8"]]
- 00b62b7c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b62c18 ["INT_ADD", "register:40f0:8", ["const:b62c18:8", "const:4:8"]]
+ 00b62c18 ["CALL", null, ["callee:00c57f80:8"]]
- 00b62b7c bytes cdd40394
+ 00b62c18 bytes dad40394
~~~


<a id="compare-c3dd8b910f2ad320c3cadf2eb4bf74c7"></a>

### [`00b62dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62dc8.md) → [`00b62e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd90.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be60.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62dc8.md#insn-00b62e64) · [`00b62ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62dc8.md#insn-00b62ea4)
- 新版 [`00b62f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md#insn-00b62f00) · [`00b62f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md#insn-00b62f40)

~~~diff
- 00b62e64 ["INT_ADD", "register:40f0:8", ["const:b62e64:8", "const:4:8"]]
- 00b62e64 ["CALL", null, ["callee:00c58120:8"]]
+ 00b62f00 ["INT_ADD", "register:40f0:8", ["const:b62f00:8", "const:4:8"]]
+ 00b62f00 ["CALL", null, ["callee:00c58120:8"]]
- 00b62e64 bytes 7bd40394
+ 00b62f00 bytes 88d40394
- 00b62ea4 ["INT_ADD", "register:40f0:8", ["const:b62ea4:8", "const:4:8"]]
- 00b62ea4 ["CALL", null, ["callee:00c58120:8"]]
+ 00b62f40 ["INT_ADD", "register:40f0:8", ["const:b62f40:8", "const:4:8"]]
+ 00b62f40 ["CALL", null, ["callee:00c58120:8"]]
- 00b62ea4 bytes 6bd40394
+ 00b62f40 bytes 78d40394
~~~


<a id="compare-ce27915db98874cb457932e73083d4c2"></a>

### [`00b648f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b648f4.md) → [`00b64990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md) FUN_00b64990

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b64750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64750.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b150.md)
- 新版 呼出元 1件 [`00b647ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b648f4.md#insn-00b64964) · [`00b64988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b648f4.md#insn-00b64988)
- 新版 [`00b64a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md#insn-00b64a00) · [`00b64a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md#insn-00b64a24)

~~~diff
- 00b64964 ["INT_ADD", "register:40f0:8", ["const:b64964:8", "const:4:8"]]
- 00b64964 ["CALL", null, ["callee:00c5b220:8"]]
+ 00b64a00 ["INT_ADD", "register:40f0:8", ["const:b64a00:8", "const:4:8"]]
+ 00b64a00 ["CALL", null, ["callee:00c5b220:8"]]
- 00b64964 bytes fbd90394
+ 00b64a00 bytes 08da0394
- 00b64988 ["INT_ADD", "register:40f0:8", ["const:b64988:8", "const:4:8"]]
- 00b64988 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b64a24 ["INT_ADD", "register:40f0:8", ["const:b64a24:8", "const:4:8"]]
+ 00b64a24 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b64988 bytes 56cd0394
+ 00b64a24 bytes 63cd0394
~~~


<a id="compare-57167cc46801818d3c3961d8419aeafb"></a>

### [`00b6531c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6531c.md) → [`00b653b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)
- 新版 呼出元 1件 [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)

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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b65338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6531c.md#insn-00b65338) · [`00b65344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6531c.md#insn-00b65344) · [`00b65354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6531c.md#insn-00b65354)
- 新版 [`00b653d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653d4) · [`00b653e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653e0) · [`00b653f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653f0)

~~~diff
- 00b65338 ["INT_ADD", "register:40f0:8", ["const:b65338:8", "const:4:8"]]
- 00b65338 ["CALL", null, ["callee:00c5bef0:8"]]
+ 00b653d4 ["INT_ADD", "register:40f0:8", ["const:b653d4:8", "const:4:8"]]
+ 00b653d4 ["CALL", null, ["callee:00c5bef0:8"]]
- 00b65338 bytes bada0394
+ 00b653d4 bytes c7da0394
- 00b65344 ["INT_ADD", "register:40f0:8", ["const:b65344:8", "const:4:8"]]
- 00b65344 ["CALL", null, ["callee:00c5bef0:8"]]
+ 00b653e0 ["INT_ADD", "register:40f0:8", ["const:b653e0:8", "const:4:8"]]
+ 00b653e0 ["CALL", null, ["callee:00c5bef0:8"]]
- 00b65344 bytes b7da0394
+ 00b653e0 bytes c4da0394
- 00b65354 ["INT_ADD", "register:40f0:8", ["const:b65354:8", "const:4:8"]]
- 00b65354 ["CALL", null, ["callee:00c5a900:8"]]
+ 00b653f0 ["INT_ADD", "register:40f0:8", ["const:b653f0:8", "const:4:8"]]
+ 00b653f0 ["CALL", null, ["callee:00c5a900:8"]]
- 00b65354 bytes 37d50394
+ 00b653f0 bytes 44d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e9db58b5bcf0dc65ac8a78f71602599"></a>

### [`00b65378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65378.md) → [`00b65414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE15__emp

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be10.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)
- 新版 呼出元 1件 [`00c5bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bee0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b65394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65378.md#insn-00b65394) · [`00b653ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65378.md#insn-00b653ac) · [`00b653bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65378.md#insn-00b653bc)
- 新版 [`00b65430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65430) · [`00b65448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65448) · [`00b65458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65458)

~~~diff
- 00b65394 ["INT_ADD", "register:40f0:8", ["const:b65394:8", "const:4:8"]]
- 00b65394 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b65430 ["INT_ADD", "register:40f0:8", ["const:b65430:8", "const:4:8"]]
+ 00b65430 ["CALL", null, ["callee:00c57f60:8"]]
- 00b65394 bytes bfca0394
+ 00b65430 bytes ccca0394
- 00b653ac ["INT_ADD", "register:40f0:8", ["const:b653ac:8", "const:4:8"]]
- 00b653ac ["CALL", null, ["callee:00c5a9c0:8"]]
+ 00b65448 ["INT_ADD", "register:40f0:8", ["const:b65448:8", "const:4:8"]]
+ 00b65448 ["CALL", null, ["callee:00c5a9c0:8"]]
- 00b653ac bytes 51d50394
+ 00b65448 bytes 5ed50394
- 00b653bc ["INT_ADD", "register:40f0:8", ["const:b653bc:8", "const:4:8"]]
- 00b653bc ["CALL", null, ["callee:00c5a9c0:8"]]
+ 00b65458 ["INT_ADD", "register:40f0:8", ["const:b65458:8", "const:4:8"]]
+ 00b65458 ["CALL", null, ["callee:00c5a9c0:8"]]
- 00b653bc bytes 4dd50394
+ 00b65458 bytes 5ad50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a38c127d95c463845a800cae294ca3"></a>

### [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) → [`00b66c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7c0.md) · 呼出先 7件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1c0.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 1件 [`00c5b890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b890.md) · 呼出先 7件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b290.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b66c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md#insn-00b66c0c) · [`00b66c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md#insn-00b66c18) · [`00b66c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md#insn-00b66c2c)
- 新版 [`00b66ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66ca8) · [`00b66cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66cb4) · [`00b66cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66cc8)

~~~diff
- 00b66c0c ["INT_ADD", "register:40f0:8", ["const:b66c0c:8", "const:4:8"]]
- 00b66c0c ["CALL", null, ["callee:00c5b830:8"]]
+ 00b66ca8 ["INT_ADD", "register:40f0:8", ["const:b66ca8:8", "const:4:8"]]
+ 00b66ca8 ["CALL", null, ["callee:00c5b830:8"]]
- 00b66c0c bytes d5d20394
+ 00b66ca8 bytes e2d20394
- 00b66c18 ["INT_ADD", "register:40f0:8", ["const:b66c18:8", "const:4:8"]]
- 00b66c18 ["CALL", null, ["callee:00c5b490:8"]]
+ 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
+ 00b66cb4 ["CALL", null, ["callee:00c5b490:8"]]
- 00b66c18 bytes ead10394
+ 00b66cb4 bytes f7d10394
- 00b66c2c ["INT_ADD", "register:40f0:8", ["const:b66c2c:8", "const:4:8"]]
- 00b66c2c ["CALL", null, ["callee:00c5b290:8"]]
+ 00b66cc8 ["INT_ADD", "register:40f0:8", ["const:b66cc8:8", "const:4:8"]]
+ 00b66cc8 ["CALL", null, ["callee:00c5b290:8"]]
- 00b66c2c bytes 65d10394
+ 00b66cc8 bytes 72d10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de38c49cc32b0b51ec598be2a0fa0c2"></a>

### [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) → [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b68254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md#insn-00b68254) · [`00b6826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md#insn-00b6826c) · [`00b6828c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md#insn-00b6828c)
- 新版 [`00b682f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b682f0) · [`00b68308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b68308) · [`00b68328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b68328)

~~~diff
- 00b68254 ["INT_ADD", "register:40f0:8", ["const:b68254:8", "const:4:8"]]
- 00b68254 ["CALL", null, ["callee:00b664f0:8"]]
+ 00b682f0 ["INT_ADD", "register:40f0:8", ["const:b682f0:8", "const:4:8"]]
+ 00b682f0 ["CALL", null, ["callee:00b664f0:8"]]
- 00b68254 bytes 80f8ff97
+ 00b682f0 bytes 80f8ff97
- 00b6826c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6826c ["INT_ADD", "register:40f0:8", ["const:b6826c:8", "const:4:8"]]
- 00b6826c ["CALLIND", null, ["register:0:8"]]
+ 00b68308 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68308 ["INT_ADD", "register:40f0:8", ["const:b68308:8", "const:4:8"]]
+ 00b68308 ["CALLIND", null, ["register:0:8"]]
- 00b6826c bytes 00013fd6
+ 00b68308 bytes 00013fd6
- 00b6828c ["INT_ADD", "register:40f0:8", ["const:b6828c:8", "const:4:8"]]
- 00b6828c ["CALL", null, ["callee:00b611c8:8"]]
+ 00b68328 ["INT_ADD", "register:40f0:8", ["const:b68328:8", "const:4:8"]]
+ 00b68328 ["CALL", null, ["callee:00b611c8:8"]]
- 00b6828c bytes a8e3ff97
+ 00b68328 bytes a8e3ff97
~~~


<a id="compare-162c1997fce92001da887e31562b9fdf"></a>

### [`00b6d7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d7f4.md) → [`00b6d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba20.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md) [`00c5ba20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba20.md)
- 新版 呼出元 1件 [`00c5baf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baf0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md) [`00c5baf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d7f4.md#insn-00b6d810) · [`00b6d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d7f4.md#insn-00b6d81c) · [`00b6d828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d7f4.md#insn-00b6d828)
- 新版 [`00b6d8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8ac) · [`00b6d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8b8) · [`00b6d8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d890.md#insn-00b6d8c4)

~~~diff
- 00b6d810 ["INT_ADD", "register:40f0:8", ["const:b6d810:8", "const:4:8"]]
- 00b6d810 ["CALL", null, ["callee:00c5baf0:8"]]
+ 00b6d8ac ["INT_ADD", "register:40f0:8", ["const:b6d8ac:8", "const:4:8"]]
+ 00b6d8ac ["CALL", null, ["callee:00c5baf0:8"]]
- 00b6d810 bytes 84b80394
+ 00b6d8ac bytes 91b80394
- 00b6d81c ["INT_ADD", "register:40f0:8", ["const:b6d81c:8", "const:4:8"]]
- 00b6d81c ["CALL", null, ["callee:00c5baf0:8"]]
+ 00b6d8b8 ["INT_ADD", "register:40f0:8", ["const:b6d8b8:8", "const:4:8"]]
+ 00b6d8b8 ["CALL", null, ["callee:00c5baf0:8"]]
- 00b6d81c bytes 81b80394
+ 00b6d8b8 bytes 8eb80394
- 00b6d828 ["INT_ADD", "register:40f0:8", ["const:b6d828:8", "const:4:8"]]
- 00b6d828 ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b6d8c4 ["INT_ADD", "register:40f0:8", ["const:b6d8c4:8", "const:4:8"]]
+ 00b6d8c4 ["CALL", null, ["callee:00c5bad0:8"]]
- 00b6d828 bytes 76b80394
+ 00b6d8c4 bytes 83b80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634ce2e447828d732644d9c32b8afaa7"></a>

### [`00b6d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d850.md) → [`00b6d8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md)
- 新版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d850.md#insn-00b6d86c) · [`00b6d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d850.md#insn-00b6d878) · [`00b6d888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d850.md#insn-00b6d888)
- 新版 [`00b6d908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d908) · [`00b6d914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d914) · [`00b6d924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d8ec.md#insn-00b6d924)

~~~diff
- 00b6d86c ["INT_ADD", "register:40f0:8", ["const:b6d86c:8", "const:4:8"]]
- 00b6d86c ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b6d908 ["INT_ADD", "register:40f0:8", ["const:b6d908:8", "const:4:8"]]
+ 00b6d908 ["CALL", null, ["callee:00c5bad0:8"]]
- 00b6d86c bytes 65b80394
+ 00b6d908 bytes 72b80394
- 00b6d878 ["INT_ADD", "register:40f0:8", ["const:b6d878:8", "const:4:8"]]
- 00b6d878 ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b6d914 ["INT_ADD", "register:40f0:8", ["const:b6d914:8", "const:4:8"]]
+ 00b6d914 ["CALL", null, ["callee:00c5bad0:8"]]
- 00b6d878 bytes 62b80394
+ 00b6d914 bytes 6fb80394
- 00b6d888 ["INT_ADD", "register:40f0:8", ["const:b6d888:8", "const:4:8"]]
- 00b6d888 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6d924 ["INT_ADD", "register:40f0:8", ["const:b6d924:8", "const:4:8"]]
+ 00b6d924 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6d888 bytes 8aa90394
+ 00b6d924 bytes 97a90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a84d2497f5ced7c70782b6ddb5d7c0"></a>

### [`00b6d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d8b0.md) → [`00b6d94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md) _ZNSt6__ndk16__treeINS_12__value_typeImNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareImS8_NS_4lessImEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bab0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bab0.md)
- 新版 呼出元 1件 [`00c5bb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb80.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d8b0.md#insn-00b6d8cc) · [`00b6d8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d8b0.md#insn-00b6d8d8) · [`00b6d8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d8b0.md#insn-00b6d8e8)
- 新版 [`00b6d968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d968) · [`00b6d974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d974) · [`00b6d984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d94c.md#insn-00b6d984)

~~~diff
- 00b6d8cc ["INT_ADD", "register:40f0:8", ["const:b6d8cc:8", "const:4:8"]]
- 00b6d8cc ["CALL", null, ["callee:00c5bb80:8"]]
+ 00b6d968 ["INT_ADD", "register:40f0:8", ["const:b6d968:8", "const:4:8"]]
+ 00b6d968 ["CALL", null, ["callee:00c5bb80:8"]]
- 00b6d8cc bytes 79b80394
+ 00b6d968 bytes 86b80394
- 00b6d8d8 ["INT_ADD", "register:40f0:8", ["const:b6d8d8:8", "const:4:8"]]
- 00b6d8d8 ["CALL", null, ["callee:00c5bb80:8"]]
+ 00b6d974 ["INT_ADD", "register:40f0:8", ["const:b6d974:8", "const:4:8"]]
+ 00b6d974 ["CALL", null, ["callee:00c5bb80:8"]]
- 00b6d8d8 bytes 76b80394
+ 00b6d974 bytes 83b80394
- 00b6d8e8 ["INT_ADD", "register:40f0:8", ["const:b6d8e8:8", "const:4:8"]]
- 00b6d8e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6d984 ["INT_ADD", "register:40f0:8", ["const:b6d984:8", "const:4:8"]]
+ 00b6d984 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6d8e8 bytes 72a90394
+ 00b6d984 bytes 7fa90394
~~~


<a id="compare-e30d130e3ac8fb5aaa264a8688fa6ac2"></a>

### [`00b6d900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d900.md) → [`00b6d99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bac0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bac0.md)
- 新版 呼出元 1件 [`00c5bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d900.md#insn-00b6d91c) · [`00b6d928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d900.md#insn-00b6d928)
- 新版 [`00b6d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md#insn-00b6d9b8) · [`00b6d9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d99c.md#insn-00b6d9c4)

~~~diff
- 00b6d91c ["INT_ADD", "register:40f0:8", ["const:b6d91c:8", "const:4:8"]]
- 00b6d91c ["CALL", null, ["callee:00c5bb90:8"]]
+ 00b6d9b8 ["INT_ADD", "register:40f0:8", ["const:b6d9b8:8", "const:4:8"]]
+ 00b6d9b8 ["CALL", null, ["callee:00c5bb90:8"]]
- 00b6d91c bytes 69b80394
+ 00b6d9b8 bytes 76b80394
- 00b6d928 ["INT_ADD", "register:40f0:8", ["const:b6d928:8", "const:4:8"]]
- 00b6d928 ["CALL", null, ["callee:00c5bb90:8"]]
+ 00b6d9c4 ["INT_ADD", "register:40f0:8", ["const:b6d9c4:8", "const:4:8"]]
+ 00b6d9c4 ["CALL", null, ["callee:00c5bb90:8"]]
- 00b6d928 bytes 66b80394
+ 00b6d9c4 bytes 73b80394
~~~


<a id="compare-a90418edfb34a8f6343ec757b2a36dd7"></a>

### [`00b6d940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d940.md) → [`00b6d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bad0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bad0.md)
- 新版 呼出元 1件 [`00c5bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bba0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d940.md#insn-00b6d95c) · [`00b6d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d940.md#insn-00b6d968)
- 新版 [`00b6d9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md#insn-00b6d9f8) · [`00b6da04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d9dc.md#insn-00b6da04)

~~~diff
- 00b6d95c ["INT_ADD", "register:40f0:8", ["const:b6d95c:8", "const:4:8"]]
- 00b6d95c ["CALL", null, ["callee:00c5bba0:8"]]
+ 00b6d9f8 ["INT_ADD", "register:40f0:8", ["const:b6d9f8:8", "const:4:8"]]
+ 00b6d9f8 ["CALL", null, ["callee:00c5bba0:8"]]
- 00b6d95c bytes 5db80394
+ 00b6d9f8 bytes 6ab80394
- 00b6d968 ["INT_ADD", "register:40f0:8", ["const:b6d968:8", "const:4:8"]]
- 00b6d968 ["CALL", null, ["callee:00c5bba0:8"]]
+ 00b6da04 ["INT_ADD", "register:40f0:8", ["const:b6da04:8", "const:4:8"]]
+ 00b6da04 ["CALL", null, ["callee:00c5bba0:8"]]
- 00b6d968 bytes 5ab80394
+ 00b6da04 bytes 67b80394
~~~


<a id="compare-b701989c0649d5634869843842857f6a"></a>

### [`00b6d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d980.md) → [`00b6da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md)
- 新版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d980.md#insn-00b6d99c) · [`00b6d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d980.md#insn-00b6d9a8)
- 新版 [`00b6da38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md#insn-00b6da38) · [`00b6da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da1c.md#insn-00b6da44)

~~~diff
- 00b6d99c ["INT_ADD", "register:40f0:8", ["const:b6d99c:8", "const:4:8"]]
- 00b6d99c ["CALL", null, ["callee:00c5bae0:8"]]
+ 00b6da38 ["INT_ADD", "register:40f0:8", ["const:b6da38:8", "const:4:8"]]
+ 00b6da38 ["CALL", null, ["callee:00c5bae0:8"]]
- 00b6d99c bytes 1db80394
+ 00b6da38 bytes 2ab80394
- 00b6d9a8 ["INT_ADD", "register:40f0:8", ["const:b6d9a8:8", "const:4:8"]]
- 00b6d9a8 ["CALL", null, ["callee:00c5bae0:8"]]
+ 00b6da44 ["INT_ADD", "register:40f0:8", ["const:b6da44:8", "const:4:8"]]
+ 00b6da44 ["CALL", null, ["callee:00c5bae0:8"]]
- 00b6d9a8 bytes 1ab80394
+ 00b6da44 bytes 27b80394
~~~


<a id="compare-596b1c424a46995a1dc6557667def7c0"></a>

### [`00b6d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d9c0.md) → [`00b6da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md) _ZN11flatbuffers10DefinitionD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)
- 新版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d9c0.md#insn-00b6d9ec) · [`00b6d9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d9c0.md#insn-00b6d9f8) · [`00b6da34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d9c0.md#insn-00b6da34)
- 新版 [`00b6da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6da88) · [`00b6da94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6da94) · [`00b6dad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6da5c.md#insn-00b6dad0)

~~~diff
- 00b6d9ec ["INT_ADD", "register:40f0:8", ["const:b6d9ec:8", "const:4:8"]]
- 00b6d9ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6da88 ["INT_ADD", "register:40f0:8", ["const:b6da88:8", "const:4:8"]]
+ 00b6da88 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6d9ec bytes 31a90394
+ 00b6da88 bytes 3ea90394
- 00b6d9f8 ["INT_ADD", "register:40f0:8", ["const:b6d9f8:8", "const:4:8"]]
- 00b6d9f8 ["CALL", null, ["callee:00c5bb20:8"]]
+ 00b6da94 ["INT_ADD", "register:40f0:8", ["const:b6da94:8", "const:4:8"]]
+ 00b6da94 ["CALL", null, ["callee:00c5bb20:8"]]
- 00b6d9f8 bytes 16b80394
+ 00b6da94 bytes 23b80394
- 00b6da34 ["INT_ADD", "register:40f0:8", ["const:b6da34:8", "const:4:8"]]
- 00b6da34 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6dad0 ["INT_ADD", "register:40f0:8", ["const:b6dad0:8", "const:4:8"]]
+ 00b6dad0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6da34 bytes 1fa90394
+ 00b6dad0 bytes 2ca90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8881619325c68e1e6c90a927a1bcd268"></a>

### [`00b6dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dad4.md) → [`00b6db70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md)
- 新版 呼出元 1件 [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6daf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dad4.md#insn-00b6daf0) · [`00b6dafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dad4.md#insn-00b6dafc) · [`00b6db0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dad4.md#insn-00b6db0c)
- 新版 [`00b6db8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6db8c) · [`00b6db98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6db98) · [`00b6dba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6db70.md#insn-00b6dba8)

~~~diff
- 00b6daf0 ["INT_ADD", "register:40f0:8", ["const:b6daf0:8", "const:4:8"]]
- 00b6daf0 ["CALL", null, ["callee:00c5bb50:8"]]
+ 00b6db8c ["INT_ADD", "register:40f0:8", ["const:b6db8c:8", "const:4:8"]]
+ 00b6db8c ["CALL", null, ["callee:00c5bb50:8"]]
- 00b6daf0 bytes e4b70394
+ 00b6db8c bytes f1b70394
- 00b6dafc ["INT_ADD", "register:40f0:8", ["const:b6dafc:8", "const:4:8"]]
- 00b6dafc ["CALL", null, ["callee:00c5bb50:8"]]
+ 00b6db98 ["INT_ADD", "register:40f0:8", ["const:b6db98:8", "const:4:8"]]
+ 00b6db98 ["CALL", null, ["callee:00c5bb50:8"]]
- 00b6dafc bytes e1b70394
+ 00b6db98 bytes eeb70394
- 00b6db0c ["INT_ADD", "register:40f0:8", ["const:b6db0c:8", "const:4:8"]]
- 00b6db0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6dba8 ["INT_ADD", "register:40f0:8", ["const:b6dba8:8", "const:4:8"]]
+ 00b6dba8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6db0c bytes e9a80394
+ 00b6dba8 bytes f6a80394
~~~


<a id="compare-63e57e5da19504bb8db40a4ba7cca546"></a>

### [`00b6dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md) → [`00b6ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8d0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md)
- 新版 呼出元 1件 [`00c5b9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9a0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6dd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md#insn-00b6dd8c) · [`00b6ddac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md#insn-00b6ddac) · [`00b6ddb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md#insn-00b6ddb4)
- 新版 [`00b6de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de28) · [`00b6de48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de48) · [`00b6de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddfc.md#insn-00b6de50)

~~~diff
- 00b6dd8c ["INT_ADD", "register:40f0:8", ["const:b6dd8c:8", "const:4:8"]]
- 00b6dd8c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6de28 ["INT_ADD", "register:40f0:8", ["const:b6de28:8", "const:4:8"]]
+ 00b6de28 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6dd8c bytes 49a80394
+ 00b6de28 bytes 56a80394
- 00b6ddac ["INT_ADD", "register:40f0:8", ["const:b6ddac:8", "const:4:8"]]
- 00b6ddac ["CALL", null, ["callee:00c5b940:8"]]
+ 00b6de48 ["INT_ADD", "register:40f0:8", ["const:b6de48:8", "const:4:8"]]
+ 00b6de48 ["CALL", null, ["callee:00c5b940:8"]]
- 00b6ddac bytes b1b60394
+ 00b6de48 bytes beb60394
- 00b6ddb4 ["INT_ADD", "register:40f0:8", ["const:b6ddb4:8", "const:4:8"]]
- 00b6ddb4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6de50 ["INT_ADD", "register:40f0:8", ["const:b6de50:8", "const:4:8"]]
+ 00b6de50 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6ddb4 bytes 3fa80394
+ 00b6de50 bytes 4ca80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8da8a492e9abc55e460fab40d08b12"></a>

### [`00b6ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6ddf0.md) → [`00b6de8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md)
- 新版 呼出元 1件 [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6de0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6ddf0.md#insn-00b6de0c) · [`00b6de18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6ddf0.md#insn-00b6de18) · [`00b6de28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6ddf0.md#insn-00b6de28)
- 新版 [`00b6dea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6dea8) · [`00b6deb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6deb4) · [`00b6dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6de8c.md#insn-00b6dec4)

~~~diff
- 00b6de0c ["INT_ADD", "register:40f0:8", ["const:b6de0c:8", "const:4:8"]]
- 00b6de0c ["CALL", null, ["callee:00c5bb60:8"]]
+ 00b6dea8 ["INT_ADD", "register:40f0:8", ["const:b6dea8:8", "const:4:8"]]
+ 00b6dea8 ["CALL", null, ["callee:00c5bb60:8"]]
- 00b6de0c bytes 21b70394
+ 00b6dea8 bytes 2eb70394
- 00b6de18 ["INT_ADD", "register:40f0:8", ["const:b6de18:8", "const:4:8"]]
- 00b6de18 ["CALL", null, ["callee:00c5bb60:8"]]
+ 00b6deb4 ["INT_ADD", "register:40f0:8", ["const:b6deb4:8", "const:4:8"]]
+ 00b6deb4 ["CALL", null, ["callee:00c5bb60:8"]]
- 00b6de18 bytes 1eb70394
+ 00b6deb4 bytes 2bb70394
- 00b6de28 ["INT_ADD", "register:40f0:8", ["const:b6de28:8", "const:4:8"]]
- 00b6de28 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6dec4 ["INT_ADD", "register:40f0:8", ["const:b6dec4:8", "const:4:8"]]
+ 00b6dec4 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6de28 bytes 22a80394
+ 00b6dec4 bytes 2fa80394
~~~


<a id="compare-a15cb9725d104cffe35658aba0225658"></a>

### [`00b6de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de40.md) → [`00b6dedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md)
- 新版 呼出元 1件 [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6de5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de40.md#insn-00b6de5c) · [`00b6de68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de40.md#insn-00b6de68) · [`00b6de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de40.md#insn-00b6de78)
- 新版 [`00b6def8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6def8) · [`00b6df04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6df04) · [`00b6df14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dedc.md#insn-00b6df14)

~~~diff
- 00b6de5c ["INT_ADD", "register:40f0:8", ["const:b6de5c:8", "const:4:8"]]
- 00b6de5c ["CALL", null, ["callee:00c5bb70:8"]]
+ 00b6def8 ["INT_ADD", "register:40f0:8", ["const:b6def8:8", "const:4:8"]]
+ 00b6def8 ["CALL", null, ["callee:00c5bb70:8"]]
- 00b6de5c bytes 11b70394
+ 00b6def8 bytes 1eb70394
- 00b6de68 ["INT_ADD", "register:40f0:8", ["const:b6de68:8", "const:4:8"]]
- 00b6de68 ["CALL", null, ["callee:00c5bb70:8"]]
+ 00b6df04 ["INT_ADD", "register:40f0:8", ["const:b6df04:8", "const:4:8"]]
+ 00b6df04 ["CALL", null, ["callee:00c5bb70:8"]]
- 00b6de68 bytes 0eb70394
+ 00b6df04 bytes 1bb70394
- 00b6de78 ["INT_ADD", "register:40f0:8", ["const:b6de78:8", "const:4:8"]]
- 00b6de78 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6df14 ["INT_ADD", "register:40f0:8", ["const:b6df14:8", "const:4:8"]]
+ 00b6df14 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6de78 bytes 0ea80394
+ 00b6df14 bytes 1ba80394
~~~


<a id="compare-2c72b2f6b3fbd2c7dd07e06b73124f9e"></a>

### [`00b6de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de90.md) → [`00b6df2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba40.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba40.md)
- 新版 呼出元 1件 [`00c5bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb10.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6deac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de90.md#insn-00b6deac) · [`00b6deb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de90.md#insn-00b6deb8) · [`00b6dec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de90.md#insn-00b6dec8)
- 新版 [`00b6df48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df48) · [`00b6df54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df54) · [`00b6df64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df2c.md#insn-00b6df64)

~~~diff
- 00b6deac ["INT_ADD", "register:40f0:8", ["const:b6deac:8", "const:4:8"]]
- 00b6deac ["CALL", null, ["callee:00c5bb10:8"]]
+ 00b6df48 ["INT_ADD", "register:40f0:8", ["const:b6df48:8", "const:4:8"]]
+ 00b6df48 ["CALL", null, ["callee:00c5bb10:8"]]
- 00b6deac bytes e5b60394
+ 00b6df48 bytes f2b60394
- 00b6deb8 ["INT_ADD", "register:40f0:8", ["const:b6deb8:8", "const:4:8"]]
- 00b6deb8 ["CALL", null, ["callee:00c5bb10:8"]]
+ 00b6df54 ["INT_ADD", "register:40f0:8", ["const:b6df54:8", "const:4:8"]]
+ 00b6df54 ["CALL", null, ["callee:00c5bb10:8"]]
- 00b6deb8 bytes e2b60394
+ 00b6df54 bytes efb60394
- 00b6dec8 ["INT_ADD", "register:40f0:8", ["const:b6dec8:8", "const:4:8"]]
- 00b6dec8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6df64 ["INT_ADD", "register:40f0:8", ["const:b6df64:8", "const:4:8"]]
+ 00b6df64 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6dec8 bytes faa70394
+ 00b6df64 bytes 07a80394
~~~


<a id="compare-c5a11bd72d0b8a0f2e6fe568ef5d23cb"></a>

### [`00b6e634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e634.md) → [`00b6e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bf40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf40.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5c010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c010.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6e6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e634.md#insn-00b6e6a8) · [`00b6e6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e634.md#insn-00b6e6cc)
- 新版 [`00b6e744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md#insn-00b6e744) · [`00b6e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e6d0.md#insn-00b6e768)

~~~diff
- 00b6e6a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e6a8 ["INT_ADD", "register:40f0:8", ["const:b6e6a8:8", "const:4:8"]]
- 00b6e6a8 ["CALLIND", null, ["register:0:8"]]
+ 00b6e744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e744 ["INT_ADD", "register:40f0:8", ["const:b6e744:8", "const:4:8"]]
+ 00b6e744 ["CALLIND", null, ["register:0:8"]]
- 00b6e6a8 bytes 00013fd6
+ 00b6e744 bytes 00013fd6
- 00b6e6cc ["INT_ADD", "register:40f0:8", ["const:b6e6cc:8", "const:4:8"]]
- 00b6e6cc ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b6e768 ["INT_ADD", "register:40f0:8", ["const:b6e768:8", "const:4:8"]]
+ 00b6e768 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b6e6cc bytes 05a60394
+ 00b6e768 bytes 12a60394
~~~


<a id="compare-5f8977d24a191d8adc3a1f680136597f"></a>

### [`00b6efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6efcc.md) → [`00b6f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6efcc.md#insn-00b6eff8) · [`00b6f04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6efcc.md#insn-00b6f04c) · [`00b6f074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6efcc.md#insn-00b6f074)
- 新版 [`00b6f094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f094) · [`00b6f0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f0e8) · [`00b6f110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md#insn-00b6f110)

~~~diff
- 00b6eff8 ["INT_ADD", "register:40f0:8", ["const:b6eff8:8", "const:4:8"]]
- 00b6eff8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b6f094 ["INT_ADD", "register:40f0:8", ["const:b6f094:8", "const:4:8"]]
+ 00b6f094 ["CALL", null, ["callee:00c580b0:8"]]
- 00b6eff8 bytes faa30394
+ 00b6f094 bytes 07a40394
- 00b6f04c ["INT_ADD", "register:40f0:8", ["const:b6f04c:8", "const:4:8"]]
- 00b6f04c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b6f0e8 ["INT_ADD", "register:40f0:8", ["const:b6f0e8:8", "const:4:8"]]
+ 00b6f0e8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b6f04c bytes 91a30394
+ 00b6f0e8 bytes 9ea30394
- 00b6f074 ["INT_ADD", "register:40f0:8", ["const:b6f074:8", "const:4:8"]]
- 00b6f074 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b6f110 ["INT_ADD", "register:40f0:8", ["const:b6f110:8", "const:4:8"]]
+ 00b6f110 ["CALL", null, ["callee:00c580d0:8"]]
- 00b6f074 bytes e3a30394
+ 00b6f110 bytes f0a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c40b5ce4c473a8cf594f08641604d6"></a>

### [`00b6f2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md) → [`00b6f380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md) _ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md#insn-00b6f320) · [`00b6f334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md#insn-00b6f334) · [`00b6f344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md#insn-00b6f344)
- 新版 [`00b6f3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3bc) · [`00b6f3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3d0) · [`00b6f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f380.md#insn-00b6f3e0)

~~~diff
- 00b6f320 ["INT_ADD", "register:40f0:8", ["const:b6f320:8", "const:4:8"]]
- 00b6f320 ["CALL", null, ["callee:0054a654:8"]]
+ 00b6f3bc ["INT_ADD", "register:40f0:8", ["const:b6f3bc:8", "const:4:8"]]
+ 00b6f3bc ["CALL", null, ["callee:0054a654:8"]]
- 00b6f320 bytes bd6ce797
+ 00b6f3bc bytes a66ce797
- 00b6f334 ["INT_ADD", "register:40f0:8", ["const:b6f334:8", "const:4:8"]]
- 00b6f334 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b6f3d0 ["INT_ADD", "register:40f0:8", ["const:b6f3d0:8", "const:4:8"]]
+ 00b6f3d0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b6f334 bytes d7a20394
+ 00b6f3d0 bytes e4a20394
- 00b6f344 ["INT_ADD", "register:40f0:8", ["const:b6f344:8", "const:4:8"]]
- 00b6f344 ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6f3e0 ["INT_ADD", "register:40f0:8", ["const:b6f3e0:8", "const:4:8"]]
+ 00b6f3e0 ["CALL", null, ["callee:00c5b680:8"]]
- 00b6f344 bytes 9bb00394
+ 00b6f3e0 bytes a8b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5568b9bbbfb65344c6e8a0cc5e98f613"></a>

### [`00b6f3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f3b8.md) → [`00b6f454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca40.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb10.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f3b8.md#insn-00b6f4a0) · [`00b6f4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f3b8.md#insn-00b6f4ec) · [`00b6f514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f3b8.md#insn-00b6f514)
- 新版 [`00b6f53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f53c) · [`00b6f588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f588) · [`00b6f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f454.md#insn-00b6f5b0)

~~~diff
- 00b6f4a0 ["INT_ADD", "register:40f0:8", ["const:b6f4a0:8", "const:4:8"]]
- 00b6f4a0 ["CALL", null, ["callee:00c58050:8"]]
+ 00b6f53c ["INT_ADD", "register:40f0:8", ["const:b6f53c:8", "const:4:8"]]
+ 00b6f53c ["CALL", null, ["callee:00c58050:8"]]
- 00b6f4a0 bytes b8a20394
+ 00b6f53c bytes c5a20394
- 00b6f4ec ["INT_ADD", "register:40f0:8", ["const:b6f4ec:8", "const:4:8"]]
- 00b6f4ec ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00b6f588 ["INT_ADD", "register:40f0:8", ["const:b6f588:8", "const:4:8"]]
+ 00b6f588 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00b6f4ec bytes fdac0394
+ 00b6f588 bytes 0aad0394
- 00b6f514 ["INT_ADD", "register:40f0:8", ["const:b6f514:8", "const:4:8"]]
- 00b6f514 ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6f5b0 ["INT_ADD", "register:40f0:8", ["const:b6f5b0:8", "const:4:8"]]
+ 00b6f5b0 ["CALL", null, ["callee:00c5b680:8"]]
- 00b6f514 bytes 27b00394
+ 00b6f5b0 bytes 34b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82c5f73ad6ddf16066f050dc67397685"></a>

### [`00b71108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71108.md) → [`00b711a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71108.md#insn-00b7112c) · [`00b71170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71108.md#insn-00b71170) · [`00b71198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71108.md#insn-00b71198)
- 新版 [`00b711c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b711c8) · [`00b7120c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b7120c) · [`00b71234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b711a4.md#insn-00b71234)

~~~diff
- 00b7112c ["INT_ADD", "register:40f0:8", ["const:b7112c:8", "const:4:8"]]
- 00b7112c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b711c8 ["INT_ADD", "register:40f0:8", ["const:b711c8:8", "const:4:8"]]
+ 00b711c8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b7112c bytes ad9b0394
+ 00b711c8 bytes ba9b0394
- 00b71170 ["INT_ADD", "register:40f0:8", ["const:b71170:8", "const:4:8"]]
- 00b71170 ["CALL", null, ["callee:00c58120:8"]]
+ 00b7120c ["INT_ADD", "register:40f0:8", ["const:b7120c:8", "const:4:8"]]
+ 00b7120c ["CALL", null, ["callee:00c58120:8"]]
- 00b71170 bytes b89b0394
+ 00b7120c bytes c59b0394
- 00b71198 ["INT_ADD", "register:40f0:8", ["const:b71198:8", "const:4:8"]]
- 00b71198 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b71234 ["INT_ADD", "register:40f0:8", ["const:b71234:8", "const:4:8"]]
+ 00b71234 ["CALL", null, ["callee:00c5b210:8"]]
- 00b71198 bytes eaa70394
+ 00b71234 bytes f7a70394
~~~


<a id="compare-828185edf2cdb25b6dae6fe7ecd8b4aa"></a>

### [`00b71900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71900.md) → [`00b7199c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b7199c.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71900.md#insn-00b71914)
- 新版 [`00b719b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b7199c.md#insn-00b719b0)

~~~diff
- 00b71914 ["INT_ADD", "register:40f0:8", ["const:b71914:8", "const:4:8"]]
- 00b71914 ["CALL", null, ["callee:00c5cb80:8"]]
+ 00b719b0 ["INT_ADD", "register:40f0:8", ["const:b719b0:8", "const:4:8"]]
+ 00b719b0 ["CALL", null, ["callee:00c5cb80:8"]]
- 00b71914 bytes 67ac0394
+ 00b719b0 bytes 74ac0394
~~~


<a id="compare-20f1e0ce6ffce89304e069a5c28d0c45"></a>

### [`00b76a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76a3c.md) → [`00b76ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9f0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1b0.md) [`00c5c1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1c0.md)
- 新版 呼出元 1件 [`00c5cac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cac0.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c280.md) [`00c5c290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76a3c.md#insn-00b76a8c) · [`00b76ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76a3c.md#insn-00b76ae0) · [`00b76b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76a3c.md#insn-00b76b70)
- 新版 [`00b76b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76b28) · [`00b76b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76b7c) · [`00b76c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76ad8.md#insn-00b76c0c)

~~~diff
- 00b76a8c ["INT_ADD", "register:40f0:8", ["const:b76a8c:8", "const:4:8"]]
- 00b76a8c ["CALL", null, ["callee:00c5c290:8"]]
+ 00b76b28 ["INT_ADD", "register:40f0:8", ["const:b76b28:8", "const:4:8"]]
+ 00b76b28 ["CALL", null, ["callee:00c5c290:8"]]
- 00b76a8c bytes cd950394
+ 00b76b28 bytes da950394
- 00b76ae0 ["INT_ADD", "register:40f0:8", ["const:b76ae0:8", "const:4:8"]]
- 00b76ae0 ["CALL", null, ["callee:00c5c280:8"]]
+ 00b76b7c ["INT_ADD", "register:40f0:8", ["const:b76b7c:8", "const:4:8"]]
+ 00b76b7c ["CALL", null, ["callee:00c5c280:8"]]
- 00b76ae0 bytes b4950394
+ 00b76b7c bytes c1950394
- 00b76b70 ["INT_ADD", "register:40f0:8", ["const:b76b70:8", "const:4:8"]]
- 00b76b70 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b76c0c ["INT_ADD", "register:40f0:8", ["const:b76c0c:8", "const:4:8"]]
+ 00b76c0c ["CALL", null, ["callee:00c57fb0:8"]]
- 00b76b70 bytes dc840394
+ 00b76c0c bytes e9840394
~~~


<a id="compare-4aeb74e732c7d0d66990c267cb8c034e"></a>

### [`00b76b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76b74.md) → [`00b76c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c060.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c130.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76b74.md#insn-00b76c04) · [`00b76c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76b74.md#insn-00b76c10) · [`00b76c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76b74.md#insn-00b76c38)
- 新版 [`00b76ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76ca0) · [`00b76cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76cac) · [`00b76cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76c10.md#insn-00b76cd4)

~~~diff
- 00b76c04 ["INT_ADD", "register:40f0:8", ["const:b76c04:8", "const:4:8"]]
- 00b76c04 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b76ca0 ["INT_ADD", "register:40f0:8", ["const:b76ca0:8", "const:4:8"]]
+ 00b76ca0 ["CALL", null, ["callee:00c5b210:8"]]
- 00b76c04 bytes 4f910394
+ 00b76ca0 bytes 5c910394
- 00b76c10 ["INT_ADD", "register:40f0:8", ["const:b76c10:8", "const:4:8"]]
- 00b76c10 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b76cac ["INT_ADD", "register:40f0:8", ["const:b76cac:8", "const:4:8"]]
+ 00b76cac ["CALL", null, ["callee:00c57f60:8"]]
- 00b76c10 bytes a0840394
+ 00b76cac bytes ad840394
- 00b76c38 ["INT_ADD", "register:40f0:8", ["const:b76c38:8", "const:4:8"]]
- 00b76c38 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b76cd4 ["INT_ADD", "register:40f0:8", ["const:b76cd4:8", "const:4:8"]]
+ 00b76cd4 ["CALL", null, ["callee:00c580d0:8"]]
- 00b76c38 bytes f2840394
+ 00b76cd4 bytes ff840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0229d95c7930a3a98b4241ed2cda68a"></a>

### [`00b77190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b77190.md) → [`00b7722c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md) _ZN11flatbuffers6Parser11ParseStringERNS_5ValueEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4d0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5a0.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b77190.md#insn-00b77230) · [`00b77250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b77190.md#insn-00b77250) · [`00b77264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b77190.md#insn-00b77264)
- 新版 [`00b772cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b772cc) · [`00b772ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b772ec) · [`00b77300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b7722c.md#insn-00b77300)

~~~diff
- 00b77230 ["INT_ADD", "register:40f0:8", ["const:b77230:8", "const:4:8"]]
- 00b77230 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b772cc ["INT_ADD", "register:40f0:8", ["const:b772cc:8", "const:4:8"]]
+ 00b772cc ["CALL", null, ["callee:00c57f60:8"]]
- 00b77230 bytes 18830394
+ 00b772cc bytes 25830394
- 00b77250 ["INT_ADD", "register:40f0:8", ["const:b77250:8", "const:4:8"]]
- 00b77250 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b772ec ["INT_ADD", "register:40f0:8", ["const:b772ec:8", "const:4:8"]]
+ 00b772ec ["CALL", null, ["callee:00c580d0:8"]]
- 00b77250 bytes 6c830394
+ 00b772ec bytes 79830394
- 00b77264 ["INT_ADD", "register:40f0:8", ["const:b77264:8", "const:4:8"]]
- 00b77264 ["CALL", null, ["callee:00c5c820:8"]]
+ 00b77300 ["INT_ADD", "register:40f0:8", ["const:b77300:8", "const:4:8"]]
+ 00b77300 ["CALL", null, ["callee:00c5c820:8"]]
- 00b77264 bytes 3b950394
+ 00b77300 bytes 48950394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528433a6af889de1eb1c949ca279597a"></a>

### [`00b774e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b774e8.md) → [`00b77584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77584.md) _ZN11flatbuffers6Parser10ParseCommaEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b774e8.md#insn-00b77508)
- 新版 [`00b775a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77584.md#insn-00b775a4)

~~~diff
- 00b77508 ["INT_ADD", "register:40f0:8", ["const:b77508:8", "const:4:8"]]
- 00b77508 ["CALL", null, ["callee:00c5c820:8"]]
+ 00b775a4 ["INT_ADD", "register:40f0:8", ["const:b775a4:8", "const:4:8"]]
+ 00b775a4 ["CALL", null, ["callee:00c5c820:8"]]
- 00b77508 bytes 92940394
+ 00b775a4 bytes 9f940394
~~~


<a id="compare-8e4377a1ae7299f774f911271f239fe2"></a>

### [`00b7ced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md) → [`00b7cf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md) _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5c0.md) · 呼出先 2件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c690.md) · 呼出先 2件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md#insn-00b7cf34) · [`00b7cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md#insn-00b7cfb8) · [`00b7cfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md#insn-00b7cfdc)
- 新版 [`00b7cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7cfd0) · [`00b7d054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7d054) · [`00b7d078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cf70.md#insn-00b7d078)

~~~diff
- 00b7cf34 ["INT_ADD", "register:40f0:8", ["const:b7cf34:8", "const:4:8"]]
- 00b7cf34 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7cfd0 ["INT_ADD", "register:40f0:8", ["const:b7cfd0:8", "const:4:8"]]
+ 00b7cfd0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7cf34 bytes 9b7c0394
+ 00b7cfd0 bytes a87c0394
- 00b7cfb8 ["INT_ADD", "register:40f0:8", ["const:b7cfb8:8", "const:4:8"]]
- 00b7cfb8 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7d054 ["INT_ADD", "register:40f0:8", ["const:b7d054:8", "const:4:8"]]
+ 00b7d054 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7cfb8 bytes 7a7c0394
+ 00b7d054 bytes 877c0394
- 00b7cfdc ["INT_ADD", "register:40f0:8", ["const:b7cfdc:8", "const:4:8"]]
- 00b7cfdc ["CALL", null, ["callee:00c580d0:8"]]
+ 00b7d078 ["INT_ADD", "register:40f0:8", ["const:b7d078:8", "const:4:8"]]
+ 00b7d078 ["CALL", null, ["callee:00c580d0:8"]]
- 00b7cfdc bytes 096c0394
+ 00b7d078 bytes 166c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae289cbdcc937823ffa19f50b78a1ffa"></a>

### [`00b7dc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md) → [`00b7dcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c200.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2d0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md#insn-00b7dc68) · [`00b7dca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md#insn-00b7dca0) · [`00b7dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md#insn-00b7dcd4)
- 新版 [`00b7dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd04) · [`00b7dd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd3c) · [`00b7dd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dcac.md#insn-00b7dd70)

~~~diff
- 00b7dc68 ["INT_ADD", "register:40f0:8", ["const:b7dc68:8", "const:4:8"]]
- 00b7dc68 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7dd04 ["INT_ADD", "register:40f0:8", ["const:b7dd04:8", "const:4:8"]]
+ 00b7dd04 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7dc68 bytes 4e790394
+ 00b7dd04 bytes 5b790394
- 00b7dca0 ["INT_ADD", "register:40f0:8", ["const:b7dca0:8", "const:4:8"]]
- 00b7dca0 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7dd3c ["INT_ADD", "register:40f0:8", ["const:b7dd3c:8", "const:4:8"]]
+ 00b7dd3c ["CALL", null, ["callee:00c5c270:8"]]
- 00b7dca0 bytes 40790394
+ 00b7dd3c bytes 4d790394
- 00b7dcd4 ["INT_ADD", "register:40f0:8", ["const:b7dcd4:8", "const:4:8"]]
- 00b7dcd4 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7dd70 ["INT_ADD", "register:40f0:8", ["const:b7dd70:8", "const:4:8"]]
+ 00b7dd70 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7dcd4 bytes 33790394
+ 00b7dd70 bytes 40790394
~~~


<a id="compare-a17e48c08edf7f96cfb7438586daaa8a"></a>

### [`00b7dd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dd24.md) → [`00b7ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c210.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2e0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dd24.md#insn-00b7dd90) · [`00b7ddc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dd24.md#insn-00b7ddc8) · [`00b7ddfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dd24.md#insn-00b7ddfc)
- 新版 [`00b7de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de2c) · [`00b7de64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de64) · [`00b7de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7ddc0.md#insn-00b7de98)

~~~diff
- 00b7dd90 ["INT_ADD", "register:40f0:8", ["const:b7dd90:8", "const:4:8"]]
- 00b7dd90 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7de2c ["INT_ADD", "register:40f0:8", ["const:b7de2c:8", "const:4:8"]]
+ 00b7de2c ["CALL", null, ["callee:00c5c270:8"]]
- 00b7dd90 bytes 04790394
+ 00b7de2c bytes 11790394
- 00b7ddc8 ["INT_ADD", "register:40f0:8", ["const:b7ddc8:8", "const:4:8"]]
- 00b7ddc8 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7de64 ["INT_ADD", "register:40f0:8", ["const:b7de64:8", "const:4:8"]]
+ 00b7de64 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7ddc8 bytes f6780394
+ 00b7de64 bytes 03790394
- 00b7ddfc ["INT_ADD", "register:40f0:8", ["const:b7ddfc:8", "const:4:8"]]
- 00b7ddfc ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7de98 ["INT_ADD", "register:40f0:8", ["const:b7de98:8", "const:4:8"]]
+ 00b7de98 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7ddfc bytes e9780394
+ 00b7de98 bytes f6780394
~~~


<a id="compare-7b38546360f7f74b990cd65d2eb3fc25"></a>

### [`00b7e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e870.md) → [`00b7e90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIljEET0_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c260.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c330.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e870.md#insn-00b7e8c8) · [`00b7e924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e870.md#insn-00b7e924)
- 新版 [`00b7e964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md#insn-00b7e964) · [`00b7e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e90c.md#insn-00b7e9c0)

~~~diff
- 00b7e8c8 ["INT_ADD", "register:40f0:8", ["const:b7e8c8:8", "const:4:8"]]
- 00b7e8c8 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7e964 ["INT_ADD", "register:40f0:8", ["const:b7e964:8", "const:4:8"]]
+ 00b7e964 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7e8c8 bytes 36760394
+ 00b7e964 bytes 43760394
- 00b7e924 ["INT_ADD", "register:40f0:8", ["const:b7e924:8", "const:4:8"]]
- 00b7e924 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7e9c0 ["INT_ADD", "register:40f0:8", ["const:b7e9c0:8", "const:4:8"]]
+ 00b7e9c0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7e924 bytes 1f760394
+ 00b7e9c0 bytes 2c760394
~~~


<a id="compare-ca6fa014f999ef1fac9f4cbf0e91f51d"></a>

### [`00b7ed84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7ed84.md) → [`00b7ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementImjEET0_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c270.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c340.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7ed84.md#insn-00b7eddc) · [`00b7ee38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7ed84.md#insn-00b7ee38)
- 新版 [`00b7ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md#insn-00b7ee78) · [`00b7eed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ee20.md#insn-00b7eed4)

~~~diff
- 00b7eddc ["INT_ADD", "register:40f0:8", ["const:b7eddc:8", "const:4:8"]]
- 00b7eddc ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7ee78 ["INT_ADD", "register:40f0:8", ["const:b7ee78:8", "const:4:8"]]
+ 00b7ee78 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7eddc bytes f1740394
+ 00b7ee78 bytes fe740394
- 00b7ee38 ["INT_ADD", "register:40f0:8", ["const:b7ee38:8", "const:4:8"]]
- 00b7ee38 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7eed4 ["INT_ADD", "register:40f0:8", ["const:b7eed4:8", "const:4:8"]]
+ 00b7eed4 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7ee38 bytes da740394
+ 00b7eed4 bytes e7740394
~~~


<a id="compare-06cee3d69cfaa2c45864ab3b7d708ac0"></a>

### [`00b7f064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f064.md) → [`00b7f100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIfjEET0_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c230.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c300.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f064.md#insn-00b7f0bc) · [`00b7f118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f064.md#insn-00b7f118)
- 新版 [`00b7f158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md#insn-00b7f158) · [`00b7f1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f100.md#insn-00b7f1b4)

~~~diff
- 00b7f0bc ["INT_ADD", "register:40f0:8", ["const:b7f0bc:8", "const:4:8"]]
- 00b7f0bc ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f158 ["INT_ADD", "register:40f0:8", ["const:b7f158:8", "const:4:8"]]
+ 00b7f158 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f0bc bytes 39740394
+ 00b7f158 bytes 46740394
- 00b7f118 ["INT_ADD", "register:40f0:8", ["const:b7f118:8", "const:4:8"]]
- 00b7f118 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f1b4 ["INT_ADD", "register:40f0:8", ["const:b7f1b4:8", "const:4:8"]]
+ 00b7f1b4 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f118 bytes 22740394
+ 00b7f1b4 bytes 2f740394
~~~


<a id="compare-d395977c92b6e87a162de911fd192f43"></a>

### [`00b7f350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f350.md) → [`00b7f3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIdjEET0_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c220.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2f0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f350.md#insn-00b7f3a8) · [`00b7f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f350.md#insn-00b7f404)
- 新版 [`00b7f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md#insn-00b7f444) · [`00b7f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f3ec.md#insn-00b7f4a0)

~~~diff
- 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
- 00b7f3a8 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f444 ["INT_ADD", "register:40f0:8", ["const:b7f444:8", "const:4:8"]]
+ 00b7f444 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f3a8 bytes 7e730394
+ 00b7f444 bytes 8b730394
- 00b7f404 ["INT_ADD", "register:40f0:8", ["const:b7f404:8", "const:4:8"]]
- 00b7f404 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f4a0 ["INT_ADD", "register:40f0:8", ["const:b7f4a0:8", "const:4:8"]]
+ 00b7f4a0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f404 bytes 67730394
+ 00b7f4a0 bytes 74730394
~~~


<a id="compare-9535298d15c2e434f6e4d26194234d4e"></a>

### [`00b7f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f434.md) → [`00b7f4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_8Offset64IT_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c420.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c270.md)
- 新版 呼出元 1件 [`00c5c4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4f0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f434.md#insn-00b7f494) · [`00b7f4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f434.md#insn-00b7f4f0) · [`00b7f514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f434.md#insn-00b7f514)
- 新版 [`00b7f530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f530) · [`00b7f58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f58c) · [`00b7f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f4d0.md#insn-00b7f5b0)

~~~diff
- 00b7f494 ["INT_ADD", "register:40f0:8", ["const:b7f494:8", "const:4:8"]]
- 00b7f494 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f530 ["INT_ADD", "register:40f0:8", ["const:b7f530:8", "const:4:8"]]
+ 00b7f530 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f494 bytes 43730394
+ 00b7f530 bytes 50730394
- 00b7f4f0 ["INT_ADD", "register:40f0:8", ["const:b7f4f0:8", "const:4:8"]]
- 00b7f4f0 ["CALL", null, ["callee:00c5c340:8"]]
+ 00b7f58c ["INT_ADD", "register:40f0:8", ["const:b7f58c:8", "const:4:8"]]
+ 00b7f58c ["CALL", null, ["callee:00c5c340:8"]]
- 00b7f4f0 bytes 60730394
+ 00b7f58c bytes 6d730394
- 00b7f514 ["INT_ADD", "register:40f0:8", ["const:b7f514:8", "const:4:8"]]
- 00b7f514 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f5b0 ["INT_ADD", "register:40f0:8", ["const:b7f5b0:8", "const:4:8"]]
+ 00b7f5b0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f514 bytes 23730394
+ 00b7f5b0 bytes 30730394
~~~


<a id="compare-bd2dce8bde3f76ada0ce07930a2422c9"></a>

### [`00b7f564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f564.md) → [`00b7f600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIvEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c410.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)
- 新版 呼出元 1件 [`00c5c4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c4e0.md) · 呼出先 2件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f564.md#insn-00b7f5c4) · [`00b7f620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f564.md#insn-00b7f620) · [`00b7f644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f564.md#insn-00b7f644)
- 新版 [`00b7f660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f660) · [`00b7f6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f6bc) · [`00b7f6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f600.md#insn-00b7f6e0)

~~~diff
- 00b7f5c4 ["INT_ADD", "register:40f0:8", ["const:b7f5c4:8", "const:4:8"]]
- 00b7f5c4 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f660 ["INT_ADD", "register:40f0:8", ["const:b7f660:8", "const:4:8"]]
+ 00b7f660 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f5c4 bytes f7720394
+ 00b7f660 bytes 04730394
- 00b7f620 ["INT_ADD", "register:40f0:8", ["const:b7f620:8", "const:4:8"]]
- 00b7f620 ["CALL", null, ["callee:00c5c320:8"]]
+ 00b7f6bc ["INT_ADD", "register:40f0:8", ["const:b7f6bc:8", "const:4:8"]]
+ 00b7f6bc ["CALL", null, ["callee:00c5c320:8"]]
- 00b7f620 bytes 0c730394
+ 00b7f6bc bytes 19730394
- 00b7f644 ["INT_ADD", "register:40f0:8", ["const:b7f644:8", "const:4:8"]]
- 00b7f644 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f6e0 ["INT_ADD", "register:40f0:8", ["const:b7f6e0:8", "const:4:8"]]
+ 00b7f6e0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f644 bytes d7720394
+ 00b7f6e0 bytes e4720394
~~~


<a id="compare-de86e62206fba6681e624ffad50bc695"></a>

### [`00b7f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f694.md) → [`00b7f730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE8EndTableEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md)
- 新版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f694.md#insn-00b7f6bc) · [`00b7f700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f694.md#insn-00b7f700) · [`00b7f724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f694.md#insn-00b7f724)
- 新版 [`00b7f758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f758) · [`00b7f79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f79c) · [`00b7f7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f730.md#insn-00b7f7c0)

~~~diff
- 00b7f6bc ["INT_ADD", "register:40f0:8", ["const:b7f6bc:8", "const:4:8"]]
- 00b7f6bc ["CALL", null, ["callee:00c5c310:8"]]
+ 00b7f758 ["INT_ADD", "register:40f0:8", ["const:b7f758:8", "const:4:8"]]
+ 00b7f758 ["CALL", null, ["callee:00c5c310:8"]]
- 00b7f6bc bytes e1720394
+ 00b7f758 bytes ee720394
- 00b7f700 ["INT_ADD", "register:40f0:8", ["const:b7f700:8", "const:4:8"]]
- 00b7f700 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7f79c ["INT_ADD", "register:40f0:8", ["const:b7f79c:8", "const:4:8"]]
+ 00b7f79c ["CALL", null, ["callee:00c5c270:8"]]
- 00b7f700 bytes a8720394
+ 00b7f79c bytes b5720394
- 00b7f724 ["INT_ADD", "register:40f0:8", ["const:b7f724:8", "const:4:8"]]
- 00b7f724 ["CALL", null, ["callee:00c58160:8"]]
+ 00b7f7c0 ["INT_ADD", "register:40f0:8", ["const:b7f7c0:8", "const:4:8"]]
+ 00b7f7c0 ["CALL", null, ["callee:00c58160:8"]]
- 00b7f724 bytes 5b620394
+ 00b7f7c0 bytes 68620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4018aa58a3f241135db9a91fb961793"></a>

### [`00b7fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7fcfc.md) → [`00b7fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c280.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c350.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7fd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7fcfc.md#insn-00b7fd68) · [`00b7fdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7fcfc.md#insn-00b7fdec)
- 新版 [`00b7fe04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md#insn-00b7fe04) · [`00b7fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fd98.md#insn-00b7fe88)

~~~diff
- 00b7fd68 ["INT_ADD", "register:40f0:8", ["const:b7fd68:8", "const:4:8"]]
- 00b7fd68 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7fe04 ["INT_ADD", "register:40f0:8", ["const:b7fe04:8", "const:4:8"]]
+ 00b7fe04 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7fd68 bytes 0e710394
+ 00b7fe04 bytes 1b710394
- 00b7fdec ["INT_ADD", "register:40f0:8", ["const:b7fdec:8", "const:4:8"]]
- 00b7fdec ["CALL", null, ["callee:00c5c270:8"]]
+ 00b7fe88 ["INT_ADD", "register:40f0:8", ["const:b7fe88:8", "const:4:8"]]
+ 00b7fe88 ["CALL", null, ["callee:00c5c270:8"]]
- 00b7fdec bytes ed700394
+ 00b7fe88 bytes fa700394
~~~


<a id="compare-97bd883a00d63bc7a3fb8a7742eb9c52"></a>

### [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) → [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) FUN_00b80114

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) · 呼出先 2件 [`00b80078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) · 呼出先 2件 [`00b80114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b800e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md#insn-00b800e8) · [`00b801a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80078.md#insn-00b801a0)
- 新版 [`00b80184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md#insn-00b80184) · [`00b8023c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80114.md#insn-00b8023c)

~~~diff
- 00b800e8 ["INT_ADD", "register:40f0:8", ["const:b800e8:8", "const:4:8"]]
- 00b800e8 ["CALL", null, ["local:b0:8"]]
+ 00b80184 ["INT_ADD", "register:40f0:8", ["const:b80184:8", "const:4:8"]]
+ 00b80184 ["CALL", null, ["local:b0:8"]]
- 00b800e8 bytes e4ffff97
+ 00b80184 bytes e4ffff97
- 00b801a0 ["INT_ADD", "register:40f0:8", ["const:b801a0:8", "const:4:8"]]
- 00b801a0 ["CALL", null, ["callee:00c58120:8"]]
+ 00b8023c ["INT_ADD", "register:40f0:8", ["const:b8023c:8", "const:4:8"]]
+ 00b8023c ["CALL", null, ["callee:00c58120:8"]]
- 00b801a0 bytes ac5f0394
+ 00b8023c bytes b95f0394
~~~


<a id="compare-7cebaa113970ff545df65de2ff29ac90"></a>

### [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) → [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) FUN_00b802b4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) · 呼出先 2件 [`00b80218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md) [`00baaf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baaf0c.md)
- 新版 呼出元 2件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) · 呼出先 2件 [`00b802b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md) [`00baafa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baafa8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8027c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md#insn-00b8027c) · [`00b80318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80218.md#insn-00b80318)
- 新版 [`00b80318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md#insn-00b80318) · [`00b803b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b802b4.md#insn-00b803b4)

~~~diff
- 00b8027c ["INT_ADD", "register:40f0:8", ["const:b8027c:8", "const:4:8"]]
- 00b8027c ["CALL", null, ["local:b0:8"]]
+ 00b80318 ["INT_ADD", "register:40f0:8", ["const:b80318:8", "const:4:8"]]
+ 00b80318 ["CALL", null, ["local:b0:8"]]
- 00b8027c bytes e7ffff97
+ 00b80318 bytes e7ffff97
- 00b80318 ["INT_ADD", "register:40f0:8", ["const:b80318:8", "const:4:8"]]
- 00b80318 ["CALL", null, ["callee:00baafa8:8"]]
+ 00b803b4 ["INT_ADD", "register:40f0:8", ["const:b803b4:8", "const:4:8"]]
+ 00b803b4 ["CALL", null, ["callee:00baafa8:8"]]
- 00b80318 bytes fdaa0094
+ 00b803b4 bytes fdaa0094
~~~


<a id="compare-610610002ed10285dfd015d36e99a5c6"></a>

### [`00b807c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b807c4.md) → [`00b80860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfa0.md) · 呼出先 2件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d030.md)
- 新版 呼出元 1件 [`00c5c070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c070.md) · 呼出先 2件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b807c4.md#insn-00b80810) · [`00b80834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b807c4.md#insn-00b80834) · [`00b80868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b807c4.md#insn-00b80868)
- 新版 [`00b808ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b808ac) · [`00b808d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b808d0) · [`00b80904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80860.md#insn-00b80904)

~~~diff
- 00b80810 ["INT_ADD", "register:40f0:8", ["const:b80810:8", "const:4:8"]]
- 00b80810 ["CALL", null, ["callee:00c5b180:8"]]
+ 00b808ac ["INT_ADD", "register:40f0:8", ["const:b808ac:8", "const:4:8"]]
+ 00b808ac ["CALL", null, ["callee:00c5b180:8"]]
- 00b80810 bytes 286a0394
+ 00b808ac bytes 356a0394
- 00b80834 ["INT_ADD", "register:40f0:8", ["const:b80834:8", "const:4:8"]]
- 00b80834 ["CALL", null, ["callee:00c5b180:8"]]
+ 00b808d0 ["INT_ADD", "register:40f0:8", ["const:b808d0:8", "const:4:8"]]
+ 00b808d0 ["CALL", null, ["callee:00c5b180:8"]]
- 00b80834 bytes 1f6a0394
+ 00b808d0 bytes 2c6a0394
- 00b80868 ["INT_ADD", "register:40f0:8", ["const:b80868:8", "const:4:8"]]
- 00b80868 ["CALL", null, ["callee:00c5b180:8"]]
+ 00b80904 ["INT_ADD", "register:40f0:8", ["const:b80904:8", "const:4:8"]]
+ 00b80904 ["CALL", null, ["callee:00c5b180:8"]]
- 00b80868 bytes 126a0394
+ 00b80904 bytes 1f6a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-188ca96edb02c66dbef599d500363d97"></a>

### [`00b80be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80be8.md) → [`00b80c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf10.md) · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md) [`00c5c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6a0.md) [`00c5c7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7c0.md) [`00c5c8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8e0.md)
- 新版 呼出元 1件 [`00c5bfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfe0.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md) [`00c5c770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c770.md) [`00c5c890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c890.md) [`00c5c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80be8.md#insn-00b80c20) · [`00b80c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80be8.md#insn-00b80c44) · [`00b80c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80be8.md#insn-00b80c60)
- 新版 [`00b80cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80cbc) · [`00b80ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80ce0) · [`00b80cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80c84.md#insn-00b80cfc)

~~~diff
- 00b80c20 ["INT_ADD", "register:40f0:8", ["const:b80c20:8", "const:4:8"]]
- 00b80c20 ["CALL", null, ["callee:00c5c680:8"]]
+ 00b80cbc ["INT_ADD", "register:40f0:8", ["const:b80cbc:8", "const:4:8"]]
+ 00b80cbc ["CALL", null, ["callee:00c5c680:8"]]
- 00b80c20 bytes 646e0394
+ 00b80cbc bytes 716e0394
- 00b80c44 ["INT_ADD", "register:40f0:8", ["const:b80c44:8", "const:4:8"]]
- 00b80c44 ["CALL", null, ["callee:00c5c770:8"]]
+ 00b80ce0 ["INT_ADD", "register:40f0:8", ["const:b80ce0:8", "const:4:8"]]
+ 00b80ce0 ["CALL", null, ["callee:00c5c770:8"]]
- 00b80c44 bytes 976e0394
+ 00b80ce0 bytes a46e0394
- 00b80c60 ["INT_ADD", "register:40f0:8", ["const:b80c60:8", "const:4:8"]]
- 00b80c60 ["CALL", null, ["callee:00c5c890:8"]]
+ 00b80cfc ["INT_ADD", "register:40f0:8", ["const:b80cfc:8", "const:4:8"]]
+ 00b80cfc ["CALL", null, ["callee:00c5c890:8"]]
- 00b80c60 bytes d86e0394
+ 00b80cfc bytes e56e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c18816f0040dea495660f9256226c8c"></a>

### [`00b80ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80ca8.md) → [`00b80d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE12CreateVectorIhNS_6OffsetENS_6VectorEEET0_IJT1_IJT_EEEEPKS7_m

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c290.md) · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)
- 新版 呼出元 1件 [`00c5c360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c360.md) · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80ca8.md#insn-00b80d14) · [`00b80d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80ca8.md#insn-00b80d80) · [`00b80da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80ca8.md#insn-00b80da4)
- 新版 [`00b80db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80db0) · [`00b80e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80e1c) · [`00b80e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80d44.md#insn-00b80e40)

~~~diff
- 00b80d14 ["INT_ADD", "register:40f0:8", ["const:b80d14:8", "const:4:8"]]
- 00b80d14 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b80db0 ["INT_ADD", "register:40f0:8", ["const:b80db0:8", "const:4:8"]]
+ 00b80db0 ["CALL", null, ["callee:00c5c270:8"]]
- 00b80d14 bytes 236d0394
+ 00b80db0 bytes 306d0394
- 00b80d80 ["INT_ADD", "register:40f0:8", ["const:b80d80:8", "const:4:8"]]
- 00b80d80 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b80e1c ["INT_ADD", "register:40f0:8", ["const:b80e1c:8", "const:4:8"]]
+ 00b80e1c ["CALL", null, ["callee:00c5c270:8"]]
- 00b80d80 bytes 086d0394
+ 00b80e1c bytes 156d0394
- 00b80da4 ["INT_ADD", "register:40f0:8", ["const:b80da4:8", "const:4:8"]]
- 00b80da4 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b80e40 ["INT_ADD", "register:40f0:8", ["const:b80e40:8", "const:4:8"]]
+ 00b80e40 ["CALL", null, ["callee:00c580d0:8"]]
- 00b80da4 bytes 975c0394
+ 00b80e40 bytes a45c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b824da575cfcc1a2e1d178c7f5ec857"></a>

### [`00b8277c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8277c.md) → [`00b82818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cae0.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5cbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cbb0.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8277c.md#insn-00b82808) · [`00b8283c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8277c.md#insn-00b8283c) · [`00b8284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8277c.md#insn-00b8284c)
- 新版 [`00b828a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828a4) · [`00b828d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828d8) · [`00b828e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82818.md#insn-00b828e8)

~~~diff
- 00b82808 ["INT_ADD", "register:40f0:8", ["const:b82808:8", "const:4:8"]]
- 00b82808 ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00b828a4 ["INT_ADD", "register:40f0:8", ["const:b828a4:8", "const:4:8"]]
+ 00b828a4 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00b82808 bytes 36600394
+ 00b828a4 bytes 43600394
- 00b8283c ["INT_ADD", "register:40f0:8", ["const:b8283c:8", "const:4:8"]]
- 00b8283c ["CALL", null, ["callee:00c58010:8"]]
+ 00b828d8 ["INT_ADD", "register:40f0:8", ["const:b828d8:8", "const:4:8"]]
+ 00b828d8 ["CALL", null, ["callee:00c58010:8"]]
- 00b8283c bytes c1550394
+ 00b828d8 bytes ce550394
- 00b8284c ["INT_ADD", "register:40f0:8", ["const:b8284c:8", "const:4:8"]]
- 00b8284c ["CALL", null, ["callee:00c58160:8"]]
+ 00b828e8 ["INT_ADD", "register:40f0:8", ["const:b828e8:8", "const:4:8"]]
+ 00b828e8 ["CALL", null, ["callee:00c58160:8"]]
- 00b8284c bytes 11560394
+ 00b828e8 bytes 1e560394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07ee8af26a928bd7ddca9791f80f6130"></a>

### [`00b8288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8288c.md) → [`00b82928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0b0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c180.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8288c.md#insn-00b8291c) · [`00b82928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8288c.md#insn-00b82928) · [`00b82950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8288c.md#insn-00b82950)
- 新版 [`00b829b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829b8) · [`00b829c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829c4) · [`00b829ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82928.md#insn-00b829ec)

~~~diff
- 00b8291c ["INT_ADD", "register:40f0:8", ["const:b8291c:8", "const:4:8"]]
- 00b8291c ["CALL", null, ["callee:00c5b210:8"]]
+ 00b829b8 ["INT_ADD", "register:40f0:8", ["const:b829b8:8", "const:4:8"]]
+ 00b829b8 ["CALL", null, ["callee:00c5b210:8"]]
- 00b8291c bytes 09620394
+ 00b829b8 bytes 16620394
- 00b82928 ["INT_ADD", "register:40f0:8", ["const:b82928:8", "const:4:8"]]
- 00b82928 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b829c4 ["INT_ADD", "register:40f0:8", ["const:b829c4:8", "const:4:8"]]
+ 00b829c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b82928 bytes 5a550394
+ 00b829c4 bytes 67550394
- 00b82950 ["INT_ADD", "register:40f0:8", ["const:b82950:8", "const:4:8"]]
- 00b82950 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b829ec ["INT_ADD", "register:40f0:8", ["const:b829ec:8", "const:4:8"]]
+ 00b829ec ["CALL", null, ["callee:00c580d0:8"]]
- 00b82950 bytes ac550394
+ 00b829ec bytes b9550394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92e0232bf05459c78efdb24e13c7af3"></a>

### [`00b862ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md) → [`00b86348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md) FUN_00b86348

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b8543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8543c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a930.md) [`00c5ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca70.md)
- 新版 呼出元 1件 [`00b854d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aa00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa00.md) [`00c5cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b862f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md#insn-00b862f8) · [`00b8632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md#insn-00b8632c) · [`00b86340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b86/00b862ac.md#insn-00b86340)
- 新版 [`00b86394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b86394) · [`00b863c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b863c8) · [`00b863dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md#insn-00b863dc)

~~~diff
- 00b862f8 ["INT_ADD", "register:40f0:8", ["const:b862f8:8", "const:4:8"]]
- 00b862f8 ["CALL", null, ["callee:00c5cb40:8"]]
+ 00b86394 ["INT_ADD", "register:40f0:8", ["const:b86394:8", "const:4:8"]]
+ 00b86394 ["CALL", null, ["callee:00c5cb40:8"]]
- 00b862f8 bytes de590394
+ 00b86394 bytes eb590394
- 00b8632c ["INT_ADD", "register:40f0:8", ["const:b8632c:8", "const:4:8"]]
- 00b8632c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b863c8 ["INT_ADD", "register:40f0:8", ["const:b863c8:8", "const:4:8"]]
+ 00b863c8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b8632c bytes 81510394
+ 00b863c8 bytes 8e510394
- 00b86340 ["INT_ADD", "register:40f0:8", ["const:b86340:8", "const:4:8"]]
- 00b86340 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b863dc ["INT_ADD", "register:40f0:8", ["const:b863dc:8", "const:4:8"]]
+ 00b863dc ["CALL", null, ["callee:00c57f80:8"]]
- 00b86340 bytes dc460394
+ 00b863dc bytes e9460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f49b21b0e0c054bd792741e9048d8dc1"></a>

### [`00b871b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b871b4.md) → [`00b87250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md) _ZN11flatbuffers6Parser11SetRootTypeEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4f0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5c0.md) · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b871f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b871b4.md#insn-00b871f4) · [`00b87230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b871b4.md#insn-00b87230) · [`00b87250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b871b4.md#insn-00b87250)
- 新版 [`00b87290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b87290) · [`00b872cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b872cc) · [`00b872ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87250.md#insn-00b872ec)

~~~diff
- 00b871f4 ["INT_ADD", "register:40f0:8", ["const:b871f4:8", "const:4:8"]]
- 00b871f4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b87290 ["INT_ADD", "register:40f0:8", ["const:b87290:8", "const:4:8"]]
+ 00b87290 ["CALL", null, ["callee:00c580b0:8"]]
- 00b871f4 bytes 7b430394
+ 00b87290 bytes 88430394
- 00b87230 ["INT_ADD", "register:40f0:8", ["const:b87230:8", "const:4:8"]]
- 00b87230 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b872cc ["INT_ADD", "register:40f0:8", ["const:b872cc:8", "const:4:8"]]
+ 00b872cc ["CALL", null, ["callee:00c57f60:8"]]
- 00b87230 bytes 18430394
+ 00b872cc bytes 25430394
- 00b87250 ["INT_ADD", "register:40f0:8", ["const:b87250:8", "const:4:8"]]
- 00b87250 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b872ec ["INT_ADD", "register:40f0:8", ["const:b872ec:8", "const:4:8"]]
+ 00b872ec ["CALL", null, ["callee:00c580d0:8"]]
- 00b87250 bytes 6c430394
+ 00b872ec bytes 79430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ed60d3935d4ff5f89a6d50dbd7b4ed5"></a>

### [`00b8b16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b16c.md) → [`00b8b208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md) _ZN11flatbuffers6Parser15ParseFlexBufferEPKcS2_PN11flexbuffers7BuilderE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md) [`00c5c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6a0.md) [`00c5c8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md) [`00c5c770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c770.md) [`00c5c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b16c.md#insn-00b8b198) · [`00b8b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b16c.md#insn-00b8b1b8) · [`00b8b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b16c.md#insn-00b8b1f0)
- 新版 [`00b8b234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b234) · [`00b8b254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b254) · [`00b8b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b208.md#insn-00b8b28c)

~~~diff
- 00b8b198 ["INT_ADD", "register:40f0:8", ["const:b8b198:8", "const:4:8"]]
- 00b8b198 ["CALL", null, ["callee:00c5c680:8"]]
+ 00b8b234 ["INT_ADD", "register:40f0:8", ["const:b8b234:8", "const:4:8"]]
+ 00b8b234 ["CALL", null, ["callee:00c5c680:8"]]
- 00b8b198 bytes 06450394
+ 00b8b234 bytes 13450394
- 00b8b1b8 ["INT_ADD", "register:40f0:8", ["const:b8b1b8:8", "const:4:8"]]
- 00b8b1b8 ["CALL", null, ["callee:00c5c770:8"]]
+ 00b8b254 ["INT_ADD", "register:40f0:8", ["const:b8b254:8", "const:4:8"]]
+ 00b8b254 ["CALL", null, ["callee:00c5c770:8"]]
- 00b8b1b8 bytes 3a450394
+ 00b8b254 bytes 47450394
- 00b8b1f0 ["INT_ADD", "register:40f0:8", ["const:b8b1f0:8", "const:4:8"]]
- 00b8b1f0 ["CALL", null, ["callee:00c5c9b0:8"]]
+ 00b8b28c ["INT_ADD", "register:40f0:8", ["const:b8b28c:8", "const:4:8"]]
+ 00b8b28c ["CALL", null, ["callee:00c5c9b0:8"]]
- 00b8b1f0 bytes bc450394
+ 00b8b28c bytes c9450394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e29f14ecffd8c3e316bfa1e2e491908"></a>

### [`00b8ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md) → [`00b8ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md) _ZNK11flatbuffers9StructDef9SerializeEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca50.md) · 呼出先 13件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5cb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb20.md) · 呼出先 13件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ede8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md#insn-00b8ede8) · [`00b8ee4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md#insn-00b8ee4c) · [`00b8ee74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8ed70.md#insn-00b8ee74)
- 新版 [`00b8ee84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8ee84) · [`00b8eee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8eee8) · [`00b8ef10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8ee0c.md#insn-00b8ef10)

~~~diff
- 00b8ede8 ["INT_ADD", "register:40f0:8", ["const:b8ede8:8", "const:4:8"]]
- 00b8ede8 ["CALL", null, ["callee:00c5cb00:8"]]
+ 00b8ee84 ["INT_ADD", "register:40f0:8", ["const:b8ee84:8", "const:4:8"]]
+ 00b8ee84 ["CALL", null, ["callee:00c5cb00:8"]]
- 00b8ede8 bytes 12370394
+ 00b8ee84 bytes 1f370394
- 00b8ee4c ["INT_ADD", "register:40f0:8", ["const:b8ee4c:8", "const:4:8"]]
- 00b8ee4c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b8eee8 ["INT_ADD", "register:40f0:8", ["const:b8eee8:8", "const:4:8"]]
+ 00b8eee8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b8ee4c bytes 11240394
+ 00b8eee8 bytes 1e240394
- 00b8ee74 ["INT_ADD", "register:40f0:8", ["const:b8ee74:8", "const:4:8"]]
- 00b8ee74 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b8ef10 ["INT_ADD", "register:40f0:8", ["const:b8ef10:8", "const:4:8"]]
+ 00b8ef10 ["CALL", null, ["callee:00c580d0:8"]]
- 00b8ee74 bytes 63240394
+ 00b8ef10 bytes 70240394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4d50e80706aa052df6f8e321fa39db"></a>

### [`00b929c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b929c4.md) → [`00b92a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md) _ZN11flatbuffers7EnumVal11DeserializeERNS_6ParserEPKN10reflection7EnumValE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5c820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c820.md) · 呼出先 7件 [`00b93150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5c8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8f0.md) · 呼出先 7件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b92a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b929c4.md#insn-00b92a4c) · [`00b92a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b929c4.md#insn-00b92a6c) · [`00b92a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b929c4.md#insn-00b92a9c)
- 新版 [`00b92ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92ae8) · [`00b92b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92b08) · [`00b92b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92a60.md#insn-00b92b38)

~~~diff
- 00b92a4c ["INT_ADD", "register:40f0:8", ["const:b92a4c:8", "const:4:8"]]
- 00b92a4c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b92ae8 ["INT_ADD", "register:40f0:8", ["const:b92ae8:8", "const:4:8"]]
+ 00b92ae8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b92a4c bytes 11150394
+ 00b92ae8 bytes 1e150394
- 00b92a6c ["INT_ADD", "register:40f0:8", ["const:b92a6c:8", "const:4:8"]]
- 00b92a6c ["CALL", null, ["callee:00c580d0:8"]]
+ 00b92b08 ["INT_ADD", "register:40f0:8", ["const:b92b08:8", "const:4:8"]]
+ 00b92b08 ["CALL", null, ["callee:00c580d0:8"]]
- 00b92a6c bytes 65150394
+ 00b92b08 bytes 72150394
- 00b92a9c ["INT_ADD", "register:40f0:8", ["const:b92a9c:8", "const:4:8"]]
- 00b92a9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b92b38 ["INT_ADD", "register:40f0:8", ["const:b92b38:8", "const:4:8"]]
+ 00b92b38 ["CALL", null, ["callee:00c57f80:8"]]
- 00b92a9c bytes 05150394
+ 00b92b38 bytes 12150394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8ffcba00dd74d3166fec65841505a8"></a>

### [`00b93504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93504.md) → [`00b935a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md) _ZN10reflection13CreateEnumValERN11flatbuffers21FlatBufferBuilderImplILb0EEENS0_6OffsetINS0_6StringEEElNS4_INS_4TypeEEENS4_INS0_6VectorIS6_j

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf90.md) · 呼出先 7件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c260.md) [`00c5c340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c340.md) [`00c5c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c350.md) [`00c5c370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c370.md)
- 新版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c060.md) · 呼出先 7件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c330.md) [`00c5c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c410.md) [`00c5c420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c420.md) [`00c5c440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c440.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93504.md#insn-00b93550) · [`00b93574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93504.md#insn-00b93574) · [`00b935c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93504.md#insn-00b935c0)
- 新版 [`00b935ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b935ec) · [`00b93610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b93610) · [`00b9365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b935a0.md#insn-00b9365c)

~~~diff
- 00b93550 ["INT_ADD", "register:40f0:8", ["const:b93550:8", "const:4:8"]]
- 00b93550 ["CALL", null, ["callee:00c5c330:8"]]
+ 00b935ec ["INT_ADD", "register:40f0:8", ["const:b935ec:8", "const:4:8"]]
+ 00b935ec ["CALL", null, ["callee:00c5c330:8"]]
- 00b93550 bytes 44230394
+ 00b935ec bytes 51230394
- 00b93574 ["INT_ADD", "register:40f0:8", ["const:b93574:8", "const:4:8"]]
- 00b93574 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b93610 ["INT_ADD", "register:40f0:8", ["const:b93610:8", "const:4:8"]]
+ 00b93610 ["CALL", null, ["callee:00c5c270:8"]]
- 00b93574 bytes 0b230394
+ 00b93610 bytes 18230394
- 00b935c0 ["INT_ADD", "register:40f0:8", ["const:b935c0:8", "const:4:8"]]
- 00b935c0 ["CALL", null, ["callee:00c5c4c0:8"]]
+ 00b9365c ["INT_ADD", "register:40f0:8", ["const:b9365c:8", "const:4:8"]]
+ 00b9365c ["CALL", null, ["callee:00c5c4c0:8"]]
- 00b935c0 bytes 8c230394
+ 00b9365c bytes 99230394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82c12ef65500806b6cca8abd4de66b05"></a>

### [`00b9361c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b9361c.md) → [`00b936b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md) _ZN10reflection10CreateTypeERN11flatbuffers21FlatBufferBuilderImplILb0EEENS_8BaseTypeES4_itjj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf50.md) · 呼出先 6件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1d0.md) [`00c5c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c210.md) [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)
- 新版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c020.md) · 呼出先 6件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md) [`00c5c2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2a0.md) [`00c5c2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2e0.md) [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md) [`00c5c320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b9361c.md#insn-00b9366c) · [`00b93690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b9361c.md#insn-00b93690) · [`00b936f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b9361c.md#insn-00b936f4)
- 新版 [`00b93708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b93708) · [`00b9372c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b9372c) · [`00b93790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b936b8.md#insn-00b93790)

~~~diff
- 00b9366c ["INT_ADD", "register:40f0:8", ["const:b9366c:8", "const:4:8"]]
- 00b9366c ["CALL", null, ["callee:00c5c320:8"]]
+ 00b93708 ["INT_ADD", "register:40f0:8", ["const:b93708:8", "const:4:8"]]
+ 00b93708 ["CALL", null, ["callee:00c5c320:8"]]
- 00b9366c bytes f9220394
+ 00b93708 bytes 06230394
- 00b93690 ["INT_ADD", "register:40f0:8", ["const:b93690:8", "const:4:8"]]
- 00b93690 ["CALL", null, ["callee:00c5c270:8"]]
+ 00b9372c ["INT_ADD", "register:40f0:8", ["const:b9372c:8", "const:4:8"]]
+ 00b9372c ["CALL", null, ["callee:00c5c270:8"]]
- 00b93690 bytes c4220394
+ 00b9372c bytes d1220394
- 00b936f4 ["INT_ADD", "register:40f0:8", ["const:b936f4:8", "const:4:8"]]
- 00b936f4 ["CALL", null, ["callee:00c5c320:8"]]
+ 00b93790 ["INT_ADD", "register:40f0:8", ["const:b93790:8", "const:4:8"]]
+ 00b93790 ["CALL", null, ["callee:00c5c320:8"]]
- 00b936f4 bytes d7220394
+ 00b93790 bytes e4220394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1710ea7a61bb5d2a9bf062bb6f14c3"></a>

### [`00b94d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b94/00b94d40.md) → [`00b94ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md) FUN_00b94ddc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b93a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b93/00b93a64.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b93b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93b00.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b94e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b94/00b94d40.md#insn-00b94e08) · [`00b94e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b94/00b94d40.md#insn-00b94e28) · [`00b94e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b94/00b94d40.md#insn-00b94e90)
- 新版 [`00b94ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94ea4) · [`00b94ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94ec4) · [`00b94f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b94/00b94ddc.md#insn-00b94f2c)

~~~diff
- 00b94e08 ["INT_ADD", "register:40f0:8", ["const:b94e08:8", "const:4:8"]]
- 00b94e08 ["CALL", null, ["callee:00c5d030:8"]]
+ 00b94ea4 ["INT_ADD", "register:40f0:8", ["const:b94ea4:8", "const:4:8"]]
+ 00b94ea4 ["CALL", null, ["callee:00c5d030:8"]]
- 00b94e08 bytes 56200394
+ 00b94ea4 bytes 63200394
- 00b94e28 ["INT_ADD", "register:40f0:8", ["const:b94e28:8", "const:4:8"]]
- 00b94e28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b94ec4 ["INT_ADD", "register:40f0:8", ["const:b94ec4:8", "const:4:8"]]
+ 00b94ec4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b94e28 bytes 1a0c0394
+ 00b94ec4 bytes 270c0394
- 00b94e90 ["INT_ADD", "register:40f0:8", ["const:b94e90:8", "const:4:8"]]
- 00b94e90 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b94f2c ["INT_ADD", "register:40f0:8", ["const:b94f2c:8", "const:4:8"]]
+ 00b94f2c ["CALL", null, ["callee:00c57f60:8"]]
- 00b94e90 bytes 000c0394
+ 00b94f2c bytes 0d0c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c79a20d25430ddf7354d25bc5fad8e4f"></a>

### [`00b95b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95b48.md) → [`00b95be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) · 呼出先 2件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)
- 新版 呼出元 1件 [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) · 呼出先 2件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b95bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95b48.md#insn-00b95bb4) · [`00b95bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95b48.md#insn-00b95bd8)
- 新版 [`00b95c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md#insn-00b95c50) · [`00b95c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95be4.md#insn-00b95c74)

~~~diff
- 00b95bb4 ["INT_ADD", "register:40f0:8", ["const:b95bb4:8", "const:4:8"]]
- 00b95bb4 ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00b95c50 ["INT_ADD", "register:40f0:8", ["const:b95c50:8", "const:4:8"]]
+ 00b95c50 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00b95bb4 bytes 4b130394
+ 00b95c50 bytes 58130394
- 00b95bd8 ["INT_ADD", "register:40f0:8", ["const:b95bd8:8", "const:4:8"]]
- 00b95bd8 ["CALL", null, ["callee:00c58160:8"]]
+ 00b95c74 ["INT_ADD", "register:40f0:8", ["const:b95c74:8", "const:4:8"]]
+ 00b95c74 ["CALL", null, ["callee:00c58160:8"]]
- 00b95bd8 bytes 2e090394
+ 00b95c74 bytes 3b090394
~~~


<a id="compare-1c8e9f7bf645f7ff6825eaef63b8b583"></a>

### [`00b98c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c08.md) → [`00b98ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ca4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c08.md#insn-00b98c1c)
- 新版 [`00b98cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ca4.md#insn-00b98cb8)

~~~diff
- 00b98c1c ["INT_ADD", "register:40f0:8", ["const:b98c1c:8", "const:4:8"]]
- 00b98c1c ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00b98cb8 ["INT_ADD", "register:40f0:8", ["const:b98cb8:8", "const:4:8"]]
+ 00b98cb8 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00b98c1c bytes 31110394
+ 00b98cb8 bytes 3e110394
~~~


<a id="compare-8a472cc16c1f9c2a1b296ca72cb6e370"></a>

### [`00b98c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c44.md) → [`00b98ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ce0.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98c44.md#insn-00b98c60)
- 新版 [`00b98cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98ce0.md#insn-00b98cfc)

~~~diff
- 00b98c60 ["INT_ADD", "register:40f0:8", ["const:b98c60:8", "const:4:8"]]
- 00b98c60 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00b98cfc ["INT_ADD", "register:40f0:8", ["const:b98cfc:8", "const:4:8"]]
+ 00b98cfc ["CALL", null, ["callee:00c5d1b0:8"]]
- 00b98c60 bytes 20110394
+ 00b98cfc bytes 2d110394
~~~


<a id="compare-3fba2e73302309872cdfc68b7cac5678"></a>

### [`00b990c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b990c4.md) → [`00b99160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b990c4.md#insn-00b99144) · [`00b99158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b990c4.md#insn-00b99158)
- 新版 [`00b991e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md#insn-00b991e0) · [`00b991f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99160.md#insn-00b991f4)

~~~diff
- 00b99144 ["INT_ADD", "register:40f0:8", ["const:b99144:8", "const:4:8"]]
- 00b99144 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b991e0 ["INT_ADD", "register:40f0:8", ["const:b991e0:8", "const:4:8"]]
+ 00b991e0 ["CALL", null, ["callee:00c580d0:8"]]
- 00b99144 bytes affb0294
+ 00b991e0 bytes bcfb0294
- 00b99158 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99158 ["INT_ADD", "register:40f0:8", ["const:b99158:8", "const:4:8"]]
- 00b99158 ["CALLIND", null, ["register:0:8"]]
+ 00b991f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b991f4 ["INT_ADD", "register:40f0:8", ["const:b991f4:8", "const:4:8"]]
+ 00b991f4 ["CALLIND", null, ["register:0:8"]]
- 00b99158 bytes 00013fd6
+ 00b991f4 bytes 00013fd6
~~~


<a id="compare-473d0101c366e5654c86330b7de66f58"></a>

### [`00b991dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b991dc.md) → [`00b99278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99278.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b991f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b991dc.md#insn-00b991f4)
- 新版 [`00b99290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99278.md#insn-00b99290)

~~~diff
- 00b991f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b991f4 ["INT_ADD", "register:40f0:8", ["const:b991f4:8", "const:4:8"]]
- 00b991f4 ["CALLIND", null, ["register:0:8"]]
+ 00b99290 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99290 ["INT_ADD", "register:40f0:8", ["const:b99290:8", "const:4:8"]]
+ 00b99290 ["CALLIND", null, ["register:0:8"]]
- 00b991f4 bytes 00013fd6
+ 00b99290 bytes 00013fd6
~~~


<a id="compare-1fcb44d68aa23f28f50b446e2babcb4b"></a>

### [`00b9928c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9928c.md) → [`00b99328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9928c.md#insn-00b99300) · [`00b99318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9928c.md#insn-00b99318)
- 新版 [`00b9939c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md#insn-00b9939c) · [`00b993b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99328.md#insn-00b993b4)

~~~diff
- 00b99300 ["INT_ADD", "register:40f0:8", ["const:b99300:8", "const:4:8"]]
- 00b99300 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b9939c ["INT_ADD", "register:40f0:8", ["const:b9939c:8", "const:4:8"]]
+ 00b9939c ["CALL", null, ["callee:00c580d0:8"]]
- 00b99300 bytes 40fb0294
+ 00b9939c bytes 4dfb0294
- 00b99318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99318 ["INT_ADD", "register:40f0:8", ["const:b99318:8", "const:4:8"]]
- 00b99318 ["CALLIND", null, ["register:0:8"]]
+ 00b993b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b993b4 ["INT_ADD", "register:40f0:8", ["const:b993b4:8", "const:4:8"]]
+ 00b993b4 ["CALLIND", null, ["register:0:8"]]
- 00b99318 bytes 00013fd6
+ 00b993b4 bytes 00013fd6
~~~


<a id="compare-2da566ae1977dcb90d5eee51393a19f2"></a>

### [`00b9a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9a9d4.md) → [`00b9aa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md) _ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc10.md) · 呼出先 2件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md) [`00c5d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d090.md)
- 新版 呼出元 1件 [`00c5cce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cce0.md) · 呼出先 2件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9aa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9a9d4.md#insn-00b9aa0c) · [`00b9aa5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9a9d4.md#insn-00b9aa5c) · [`00b9aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9a9d4.md#insn-00b9aaa0)
- 新版 [`00b9aaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9aaa8) · [`00b9aaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9aaf8) · [`00b9ab3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9a/00b9aa70.md#insn-00b9ab3c)

~~~diff
- 00b9aa0c ["INT_ADD", "register:40f0:8", ["const:b9aa0c:8", "const:4:8"]]
- 00b9aa0c ["CALL", null, ["callee:00c5d160:8"]]
+ 00b9aaa8 ["INT_ADD", "register:40f0:8", ["const:b9aaa8:8", "const:4:8"]]
+ 00b9aaa8 ["CALL", null, ["callee:00c5d160:8"]]
- 00b9aa0c bytes a1090394
+ 00b9aaa8 bytes ae090394
- 00b9aa5c ["INT_ADD", "register:40f0:8", ["const:b9aa5c:8", "const:4:8"]]
- 00b9aa5c ["CALL", null, ["callee:00c5b920:8"]]
+ 00b9aaf8 ["INT_ADD", "register:40f0:8", ["const:b9aaf8:8", "const:4:8"]]
+ 00b9aaf8 ["CALL", null, ["callee:00c5b920:8"]]
- 00b9aa5c bytes 7d030394
+ 00b9aaf8 bytes 8a030394
- 00b9aaa0 ["INT_ADD", "register:40f0:8", ["const:b9aaa0:8", "const:4:8"]]
- 00b9aaa0 ["CALL", null, ["callee:00c5b920:8"]]
+ 00b9ab3c ["INT_ADD", "register:40f0:8", ["const:b9ab3c:8", "const:4:8"]]
+ 00b9ab3c ["CALL", null, ["callee:00c5b920:8"]]
- 00b9aaa0 bytes 6c030394
+ 00b9ab3c bytes 79030394
~~~


<a id="compare-3127137523e452b2e7734284f9c2389f"></a>

### [`00b9b818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b818.md) → [`00b9b8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS1

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfc0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)
- 新版 呼出元 1件 [`00c5d090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d090.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9b87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b818.md#insn-00b9b87c) · [`00b9b8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b818.md#insn-00b9b8b8) · [`00b9b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b818.md#insn-00b9b908)
- 新版 [`00b9b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b918) · [`00b9b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b954) · [`00b9b9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9b/00b9b8b4.md#insn-00b9b9a4)

~~~diff
- 00b9b87c ["INT_ADD", "register:40f0:8", ["const:b9b87c:8", "const:4:8"]]
- 00b9b87c ["CALL", null, ["callee:00c58120:8"]]
+ 00b9b918 ["INT_ADD", "register:40f0:8", ["const:b9b918:8", "const:4:8"]]
+ 00b9b918 ["CALL", null, ["callee:00c58120:8"]]
- 00b9b87c bytes f5f10294
+ 00b9b918 bytes 02f20294
- 00b9b8b8 ["INT_ADD", "register:40f0:8", ["const:b9b8b8:8", "const:4:8"]]
- 00b9b8b8 ["CALL", null, ["callee:00c58120:8"]]
+ 00b9b954 ["INT_ADD", "register:40f0:8", ["const:b9b954:8", "const:4:8"]]
+ 00b9b954 ["CALL", null, ["callee:00c58120:8"]]
- 00b9b8b8 bytes e6f10294
+ 00b9b954 bytes f3f10294
- 00b9b908 ["INT_ADD", "register:40f0:8", ["const:b9b908:8", "const:4:8"]]
- 00b9b908 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b9b9a4 ["INT_ADD", "register:40f0:8", ["const:b9b9a4:8", "const:4:8"]]
+ 00b9b9a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b9b908 bytes 62f10294
+ 00b9b9a4 bytes 6ff10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3f19dd7539b9e8d87e18a37484d03f5"></a>

### [`00b9caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9caa4.md) → [`00b9cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_EEEEvT

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb40.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb40.md) [`00c5cbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbd0.md) [`00c5cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc70.md)
- 新版 呼出元 1件 [`00c5cc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc10.md) · 呼出先 4件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc10.md) [`00c5cca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cca0.md) [`00c5cd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cd40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9caa4.md#insn-00b9cb40) · [`00b9cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9caa4.md#insn-00b9cc2c) · [`00b9cc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9caa4.md#insn-00b9cc94)
- 新版 [`00b9cbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9cbdc) · [`00b9ccc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9ccc8) · [`00b9cd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9c/00b9cb40.md#insn-00b9cd30)

~~~diff
- 00b9cb40 ["INT_ADD", "register:40f0:8", ["const:b9cb40:8", "const:4:8"]]
- 00b9cb40 ["CALL", null, ["callee:00c58120:8"]]
+ 00b9cbdc ["INT_ADD", "register:40f0:8", ["const:b9cbdc:8", "const:4:8"]]
+ 00b9cbdc ["CALL", null, ["callee:00c58120:8"]]
- 00b9cb40 bytes 44ed0294
+ 00b9cbdc bytes 51ed0294
- 00b9cc2c ["INT_ADD", "register:40f0:8", ["const:b9cc2c:8", "const:4:8"]]
- 00b9cc2c ["CALL", null, ["callee:00c58120:8"]]
+ 00b9ccc8 ["INT_ADD", "register:40f0:8", ["const:b9ccc8:8", "const:4:8"]]
+ 00b9ccc8 ["CALL", null, ["callee:00c58120:8"]]
- 00b9cc2c bytes 09ed0294
+ 00b9ccc8 bytes 16ed0294
- 00b9cc94 ["INT_ADD", "register:40f0:8", ["const:b9cc94:8", "const:4:8"]]
- 00b9cc94 ["CALL", null, ["callee:00c5cc10:8"]]
+ 00b9cd30 ["INT_ADD", "register:40f0:8", ["const:b9cd30:8", "const:4:8"]]
+ 00b9cd30 ["CALL", null, ["callee:00c5cc10:8"]]
- 00b9cc94 bytes abff0294
+ 00b9cd30 bytes b8ff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b298d706d233cd9ce7f27f7b5822cb2"></a>

### [`00b9dbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dbd8.md) → [`00b9dc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9dc74.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ccd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccd0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cda0.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9dc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dbd8.md#insn-00b9dc9c)
- 新版 [`00b9dd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9dc74.md#insn-00b9dd38)

~~~diff
- 00b9dc9c ["INT_ADD", "register:40f0:8", ["const:b9dc9c:8", "const:4:8"]]
- 00b9dc9c ["CALL", null, ["callee:00c58120:8"]]
+ 00b9dd38 ["INT_ADD", "register:40f0:8", ["const:b9dd38:8", "const:4:8"]]
+ 00b9dd38 ["CALL", null, ["callee:00c58120:8"]]
- 00b9dc9c bytes ede80294
+ 00b9dd38 bytes fae80294
~~~


<a id="compare-bfc3fd90b7909d4c7805771c3f229448"></a>

### [`00b9dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dd10.md) → [`00b9ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md) FUN_00b9ddac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9d31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9d31c.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00b9d3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9d3b8.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dd10.md#insn-00b9ddd0) · [`00b9ddfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dd10.md#insn-00b9ddfc)
- 新版 [`00b9de6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md#insn-00b9de6c) · [`00b9de98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b9d/00b9ddac.md#insn-00b9de98)

~~~diff
- 00b9ddd0 ["INT_ADD", "register:40f0:8", ["const:b9ddd0:8", "const:4:8"]]
- 00b9ddd0 ["CALL", null, ["callee:00c58010:8"]]
+ 00b9de6c ["INT_ADD", "register:40f0:8", ["const:b9de6c:8", "const:4:8"]]
+ 00b9de6c ["CALL", null, ["callee:00c58010:8"]]
- 00b9ddd0 bytes 5ce80294
+ 00b9de6c bytes 69e80294
- 00b9ddfc ["INT_ADD", "register:40f0:8", ["const:b9ddfc:8", "const:4:8"]]
- 00b9ddfc ["CALL", null, ["callee:00c58010:8"]]
+ 00b9de98 ["INT_ADD", "register:40f0:8", ["const:b9de98:8", "const:4:8"]]
+ 00b9de98 ["CALL", null, ["callee:00c58010:8"]]
- 00b9ddfc bytes 51e80294
+ 00b9de98 bytes 5ee80294
~~~


<a id="compare-3759512f9e4d2998a6cc5c0bfd251dcc"></a>

### [`00ba199c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba1/00ba199c.md) → [`00ba1a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf60.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d030.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba1a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba1/00ba199c.md#insn-00ba1a38) · [`00ba1a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba1/00ba199c.md#insn-00ba1a78)
- 新版 [`00ba1ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md#insn-00ba1ad4) · [`00ba1b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1a38.md#insn-00ba1b14)

~~~diff
- 00ba1a38 ["INT_ADD", "register:40f0:8", ["const:ba1a38:8", "const:4:8"]]
- 00ba1a38 ["CALL", null, ["callee:00c58120:8"]]
+ 00ba1ad4 ["INT_ADD", "register:40f0:8", ["const:ba1ad4:8", "const:4:8"]]
+ 00ba1ad4 ["CALL", null, ["callee:00c58120:8"]]
- 00ba1a38 bytes 86d90294
+ 00ba1ad4 bytes 93d90294
- 00ba1a78 ["INT_ADD", "register:40f0:8", ["const:ba1a78:8", "const:4:8"]]
- 00ba1a78 ["CALL", null, ["callee:00c58120:8"]]
+ 00ba1b14 ["INT_ADD", "register:40f0:8", ["const:ba1b14:8", "const:4:8"]]
+ 00ba1b14 ["CALL", null, ["callee:00c58120:8"]]
- 00ba1a78 bytes 76d90294
+ 00ba1b14 bytes 83d90294
~~~


<a id="compare-7a906da7fc0e42887a733fc52fc5b4da"></a>

### [`00ba2b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md) → [`00ba2bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cba0.md) · 呼出先 4件 [`00ba3544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba3/00ba3544.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cba0.md) [`00c5cd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd60.md)
- 新版 呼出元 1件 [`00c5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc70.md) · 呼出先 4件 [`00ba35e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba3/00ba35e0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cc70.md) [`00c5ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba2c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md#insn-00ba2c1c) · [`00ba2cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md#insn-00ba2cf4) · [`00ba2de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md#insn-00ba2de0)
- 新版 [`00ba2cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2cb8) · [`00ba2d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2d90) · [`00ba2e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba2/00ba2bec.md#insn-00ba2e7c)

~~~diff
- 00ba2c1c ["INT_ADD", "register:40f0:8", ["const:ba2c1c:8", "const:4:8"]]
- 00ba2c1c ["CALL", null, ["callee:00c58120:8"]]
+ 00ba2cb8 ["INT_ADD", "register:40f0:8", ["const:ba2cb8:8", "const:4:8"]]
+ 00ba2cb8 ["CALL", null, ["callee:00c58120:8"]]
- 00ba2c1c bytes 0dd50294
+ 00ba2cb8 bytes 1ad50294
- 00ba2cf4 ["INT_ADD", "register:40f0:8", ["const:ba2cf4:8", "const:4:8"]]
- 00ba2cf4 ["CALL", null, ["callee:00c58120:8"]]
+ 00ba2d90 ["INT_ADD", "register:40f0:8", ["const:ba2d90:8", "const:4:8"]]
+ 00ba2d90 ["CALL", null, ["callee:00c58120:8"]]
- 00ba2cf4 bytes d7d40294
+ 00ba2d90 bytes e4d40294
- 00ba2de0 ["INT_ADD", "register:40f0:8", ["const:ba2de0:8", "const:4:8"]]
- 00ba2de0 ["CALL", null, ["callee:00c58120:8"]]
+ 00ba2e7c ["INT_ADD", "register:40f0:8", ["const:ba2e7c:8", "const:4:8"]]
+ 00ba2e7c ["CALL", null, ["callee:00c58120:8"]]
- 00ba2de0 bytes 9cd40294
+ 00ba2e7c bytes a9d40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcde5646db60a284409d65d0175931d8"></a>

### [`00bae86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae86c.md) → [`00bae908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf10.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfe0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae86c.md#insn-00bae904) · [`00bae94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae86c.md#insn-00bae94c)
- 新版 [`00bae9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md#insn-00bae9a0) · [`00bae9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md#insn-00bae9e8)

~~~diff
- 00bae904 ["INT_ADD", "register:40f0:8", ["const:bae904:8", "const:4:8"]]
- 00bae904 ["CALL", null, ["callee:00c58120:8"]]
+ 00bae9a0 ["INT_ADD", "register:40f0:8", ["const:bae9a0:8", "const:4:8"]]
+ 00bae9a0 ["CALL", null, ["callee:00c58120:8"]]
- 00bae904 bytes d3a50294
+ 00bae9a0 bytes e0a50294
- 00bae94c ["INT_ADD", "register:40f0:8", ["const:bae94c:8", "const:4:8"]]
- 00bae94c ["CALL", null, ["callee:00c58120:8"]]
+ 00bae9e8 ["INT_ADD", "register:40f0:8", ["const:bae9e8:8", "const:4:8"]]
+ 00bae9e8 ["CALL", null, ["callee:00c58120:8"]]
- 00bae94c bytes c1a50294
+ 00bae9e8 bytes cea50294
~~~


<a id="compare-5ec2b571d0386ce5a96ede43ed8482a5"></a>

### [`00bae980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae980.md) → [`00baea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf00.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cfd0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae980.md#insn-00baea1c) · [`00baea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae980.md#insn-00baea5c)
- 新版 [`00baeab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md#insn-00baeab8) · [`00baeaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baea1c.md#insn-00baeaf8)

~~~diff
- 00baea1c ["INT_ADD", "register:40f0:8", ["const:baea1c:8", "const:4:8"]]
- 00baea1c ["CALL", null, ["callee:00c58120:8"]]
+ 00baeab8 ["INT_ADD", "register:40f0:8", ["const:baeab8:8", "const:4:8"]]
+ 00baeab8 ["CALL", null, ["callee:00c58120:8"]]
- 00baea1c bytes 8da50294
+ 00baeab8 bytes 9aa50294
- 00baea5c ["INT_ADD", "register:40f0:8", ["const:baea5c:8", "const:4:8"]]
- 00baea5c ["CALL", null, ["callee:00c58120:8"]]
+ 00baeaf8 ["INT_ADD", "register:40f0:8", ["const:baeaf8:8", "const:4:8"]]
+ 00baeaf8 ["CALL", null, ["callee:00c58120:8"]]
- 00baea5c bytes 7da50294
+ 00baeaf8 bytes 8aa50294
~~~


<a id="compare-670c34508eee0e97947f2191fb5320ab"></a>

### [`00baeaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeaa0.md) → [`00baeb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md) _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfb0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5cfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfb0.md)
- 新版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d080.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeaa0.md#insn-00baeabc) · [`00baeac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeaa0.md#insn-00baeac8)
- 新版 [`00baeb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md#insn-00baeb58) · [`00baeb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md#insn-00baeb64)

~~~diff
- 00baeabc ["INT_ADD", "register:40f0:8", ["const:baeabc:8", "const:4:8"]]
- 00baeabc ["CALL", null, ["callee:00c5d080:8"]]
+ 00baeb58 ["INT_ADD", "register:40f0:8", ["const:baeb58:8", "const:4:8"]]
+ 00baeb58 ["CALL", null, ["callee:00c5d080:8"]]
- 00baeabc bytes 3db90294
+ 00baeb58 bytes 4ab90294
- 00baeac8 ["INT_ADD", "register:40f0:8", ["const:baeac8:8", "const:4:8"]]
- 00baeac8 ["CALL", null, ["callee:00c5d080:8"]]
+ 00baeb64 ["INT_ADD", "register:40f0:8", ["const:baeb64:8", "const:4:8"]]
+ 00baeb64 ["CALL", null, ["callee:00c5d080:8"]]
- 00baeac8 bytes 3ab90294
+ 00baeb64 bytes 47b90294
~~~


<a id="compare-3c7fd51b104f3cf348b294283d998dd7"></a>

### [`00baebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baebf4.md) → [`00baec90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce80.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf50.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baec90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baebf4.md#insn-00baec90) · [`00baecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baebf4.md#insn-00baecd0)
- 新版 [`00baed2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md#insn-00baed2c) · [`00baed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md#insn-00baed6c)

~~~diff
- 00baec90 ["INT_ADD", "register:40f0:8", ["const:baec90:8", "const:4:8"]]
- 00baec90 ["CALL", null, ["callee:00c58120:8"]]
+ 00baed2c ["INT_ADD", "register:40f0:8", ["const:baed2c:8", "const:4:8"]]
+ 00baed2c ["CALL", null, ["callee:00c58120:8"]]
- 00baec90 bytes f0a40294
+ 00baed2c bytes fda40294
- 00baecd0 ["INT_ADD", "register:40f0:8", ["const:baecd0:8", "const:4:8"]]
- 00baecd0 ["CALL", null, ["callee:00c58120:8"]]
+ 00baed6c ["INT_ADD", "register:40f0:8", ["const:baed6c:8", "const:4:8"]]
+ 00baed6c ["CALL", null, ["callee:00c58120:8"]]
- 00baecd0 bytes e0a40294
+ 00baed6c bytes eda40294
~~~


<a id="compare-fe69244121f6817490c4463b1a6fd39d"></a>

### [`00baed14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baed14.md) → [`00baedb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4le

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca60.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cb30.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baedac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baed14.md#insn-00baedac) · [`00baedf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baed14.md#insn-00baedf4)
- 新版 [`00baee48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md#insn-00baee48) · [`00baee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md#insn-00baee90)

~~~diff
- 00baedac ["INT_ADD", "register:40f0:8", ["const:baedac:8", "const:4:8"]]
- 00baedac ["CALL", null, ["callee:00c58120:8"]]
+ 00baee48 ["INT_ADD", "register:40f0:8", ["const:baee48:8", "const:4:8"]]
+ 00baee48 ["CALL", null, ["callee:00c58120:8"]]
- 00baedac bytes a9a40294
+ 00baee48 bytes b6a40294
- 00baedf4 ["INT_ADD", "register:40f0:8", ["const:baedf4:8", "const:4:8"]]
- 00baedf4 ["CALL", null, ["callee:00c58120:8"]]
+ 00baee90 ["INT_ADD", "register:40f0:8", ["const:baee90:8", "const:4:8"]]
+ 00baee90 ["CALL", null, ["callee:00c58120:8"]]
- 00baedf4 bytes 97a40294
+ 00baee90 bytes a4a40294
~~~


<a id="compare-d58568f37efaaeca73766e8abdbbedc3"></a>

### [`00baf340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md) → [`00baf3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md#insn-00baf374) · [`00baf38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md#insn-00baf38c) · [`00baf3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md#insn-00baf3d0)
- 新版 [`00baf410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf410) · [`00baf428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf428) · [`00baf46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf3dc.md#insn-00baf46c)

~~~diff
- 00baf374 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf374 ["INT_ADD", "register:40f0:8", ["const:baf374:8", "const:4:8"]]
- 00baf374 ["CALLIND", null, ["register:0:8"]]
+ 00baf410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf410 ["INT_ADD", "register:40f0:8", ["const:baf410:8", "const:4:8"]]
+ 00baf410 ["CALLIND", null, ["register:0:8"]]
- 00baf374 bytes 00013fd6
+ 00baf410 bytes 00013fd6
- 00baf38c ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf38c ["INT_ADD", "register:40f0:8", ["const:baf38c:8", "const:4:8"]]
- 00baf38c ["CALLIND", null, ["register:0:8"]]
+ 00baf428 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf428 ["INT_ADD", "register:40f0:8", ["const:baf428:8", "const:4:8"]]
+ 00baf428 ["CALLIND", null, ["register:0:8"]]
- 00baf38c bytes 20013fd6
+ 00baf428 bytes 20013fd6
- 00baf3d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf3d0 ["INT_ADD", "register:40f0:8", ["const:baf3d0:8", "const:4:8"]]
- 00baf3d0 ["CALLIND", null, ["register:0:8"]]
+ 00baf46c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf46c ["INT_ADD", "register:40f0:8", ["const:baf46c:8", "const:4:8"]]
+ 00baf46c ["CALLIND", null, ["register:0:8"]]
- 00baf3d0 bytes 00013fd6
+ 00baf46c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a55eec212dac6ca797a0df1bac828aba"></a>

### [`00baf4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md) → [`00baf560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md) FUN_00baf560

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00baee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baee28.md) [`00baf728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf728.md) · 呼出先 1件 [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md)
- 新版 呼出元 2件 [`00baeec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md) [`00baf7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md) · 呼出先 1件 [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md#insn-00baf4f8) · [`00baf510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md#insn-00baf510) · [`00baf534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md#insn-00baf534)
- 新版 [`00baf594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf594) · [`00baf5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf5ac) · [`00baf5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md#insn-00baf5d0)

~~~diff
- 00baf4f8 ["INT_ADD", "register:40f0:8", ["const:baf4f8:8", "const:4:8"]]
- 00baf4f8 ["CALL", null, ["callee:00c5d180:8"]]
+ 00baf594 ["INT_ADD", "register:40f0:8", ["const:baf594:8", "const:4:8"]]
+ 00baf594 ["CALL", null, ["callee:00c5d180:8"]]
- 00baf4f8 bytes eeb60294
+ 00baf594 bytes fbb60294
- 00baf510 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf510 ["INT_ADD", "register:40f0:8", ["const:baf510:8", "const:4:8"]]
- 00baf510 ["CALLIND", null, ["register:0:8"]]
+ 00baf5ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf5ac ["INT_ADD", "register:40f0:8", ["const:baf5ac:8", "const:4:8"]]
+ 00baf5ac ["CALLIND", null, ["register:0:8"]]
- 00baf510 bytes 20013fd6
+ 00baf5ac bytes 20013fd6
- 00baf534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf534 ["INT_ADD", "register:40f0:8", ["const:baf534:8", "const:4:8"]]
- 00baf534 ["CALLIND", null, ["register:0:8"]]
+ 00baf5d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf5d0 ["INT_ADD", "register:40f0:8", ["const:baf5d0:8", "const:4:8"]]
+ 00baf5d0 ["CALLIND", null, ["register:0:8"]]
- 00baf534 bytes 00013fd6
+ 00baf5d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-785942314583bd29095077d28595eb52"></a>

### [`00baf5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf5cc.md) → [`00baf668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5cbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbf0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccc0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf5cc.md#insn-00baf5fc) · [`00baf618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf5cc.md#insn-00baf618) · [`00baf654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf5cc.md#insn-00baf654)
- 新版 [`00baf698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf698) · [`00baf6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf6b4) · [`00baf6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md#insn-00baf6f0)

~~~diff
- 00baf5fc ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf5fc ["INT_ADD", "register:40f0:8", ["const:baf5fc:8", "const:4:8"]]
- 00baf5fc ["CALLIND", null, ["register:0:8"]]
+ 00baf698 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf698 ["INT_ADD", "register:40f0:8", ["const:baf698:8", "const:4:8"]]
+ 00baf698 ["CALLIND", null, ["register:0:8"]]
- 00baf5fc bytes 20013fd6
+ 00baf698 bytes 20013fd6
- 00baf618 ["COPY", "register:0:8", ["register:4048:8"]]
- 00baf618 ["INT_ADD", "register:40f0:8", ["const:baf618:8", "const:4:8"]]
- 00baf618 ["CALLIND", null, ["register:0:8"]]
+ 00baf6b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf6b4 ["INT_ADD", "register:40f0:8", ["const:baf6b4:8", "const:4:8"]]
+ 00baf6b4 ["CALLIND", null, ["register:0:8"]]
- 00baf618 bytes 20013fd6
+ 00baf6b4 bytes 20013fd6
- 00baf654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf654 ["INT_ADD", "register:40f0:8", ["const:baf654:8", "const:4:8"]]
- 00baf654 ["CALLIND", null, ["register:0:8"]]
+ 00baf6f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf6f0 ["INT_ADD", "register:40f0:8", ["const:baf6f0:8", "const:4:8"]]
+ 00baf6f0 ["CALLIND", null, ["register:0:8"]]
- 00baf654 bytes 00013fd6
+ 00baf6f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb47807f90e9247e7b38dfbfd0cffea5"></a>

### [`00bafc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafc0c.md) → [`00bafca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf30.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5d000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d000.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafc0c.md#insn-00bafca4) · [`00bafcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafc0c.md#insn-00bafcec)
- 新版 [`00bafd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md#insn-00bafd40) · [`00bafd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md#insn-00bafd88)

~~~diff
- 00bafca4 ["INT_ADD", "register:40f0:8", ["const:bafca4:8", "const:4:8"]]
- 00bafca4 ["CALL", null, ["callee:00c58120:8"]]
+ 00bafd40 ["INT_ADD", "register:40f0:8", ["const:bafd40:8", "const:4:8"]]
+ 00bafd40 ["CALL", null, ["callee:00c58120:8"]]
- 00bafca4 bytes eba00294
+ 00bafd40 bytes f8a00294
- 00bafcec ["INT_ADD", "register:40f0:8", ["const:bafcec:8", "const:4:8"]]
- 00bafcec ["CALL", null, ["callee:00c58120:8"]]
+ 00bafd88 ["INT_ADD", "register:40f0:8", ["const:bafd88:8", "const:4:8"]]
+ 00bafd88 ["CALL", null, ["callee:00c58120:8"]]
- 00bafcec bytes d9a00294
+ 00bafd88 bytes e6a00294
~~~


<a id="compare-e5782cae51a842a54e27322637b7dd43"></a>

### [`00bb01c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb01c4.md) → [`00bb0260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_ite

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cfe0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0b0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb01c4.md#insn-00bb0214) · [`00bb0238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb01c4.md#insn-00bb0238) · [`00bb0278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb01c4.md#insn-00bb0278)
- 新版 [`00bb02b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb02b0) · [`00bb02d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb02d4) · [`00bb0314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0260.md#insn-00bb0314)

~~~diff
- 00bb0214 ["INT_ADD", "register:40f0:8", ["const:bb0214:8", "const:4:8"]]
- 00bb0214 ["CALL", null, ["callee:00c5b920:8"]]
+ 00bb02b0 ["INT_ADD", "register:40f0:8", ["const:bb02b0:8", "const:4:8"]]
+ 00bb02b0 ["CALL", null, ["callee:00c5b920:8"]]
- 00bb0214 bytes 8fad0294
+ 00bb02b0 bytes 9cad0294
- 00bb0238 ["INT_ADD", "register:40f0:8", ["const:bb0238:8", "const:4:8"]]
- 00bb0238 ["CALL", null, ["callee:00c5b920:8"]]
+ 00bb02d4 ["INT_ADD", "register:40f0:8", ["const:bb02d4:8", "const:4:8"]]
+ 00bb02d4 ["CALL", null, ["callee:00c5b920:8"]]
- 00bb0238 bytes 86ad0294
+ 00bb02d4 bytes 93ad0294
- 00bb0278 ["INT_ADD", "register:40f0:8", ["const:bb0278:8", "const:4:8"]]
- 00bb0278 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bb0314 ["INT_ADD", "register:40f0:8", ["const:bb0314:8", "const:4:8"]]
+ 00bb0314 ["CALL", null, ["callee:00c57f60:8"]]
- 00bb0278 bytes 069f0294
+ 00bb0314 bytes 139f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fbfd705b86daf6d60788e9630d79e0f"></a>

### [`00bb02e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb02e4.md) → [`00bb0380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5cf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf90.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5d060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d060.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb02e4.md#insn-00bb037c) · [`00bb03c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb02e4.md#insn-00bb03c4)
- 新版 [`00bb0418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md#insn-00bb0418) · [`00bb0460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0380.md#insn-00bb0460)

~~~diff
- 00bb037c ["INT_ADD", "register:40f0:8", ["const:bb037c:8", "const:4:8"]]
- 00bb037c ["CALL", null, ["callee:00c58120:8"]]
+ 00bb0418 ["INT_ADD", "register:40f0:8", ["const:bb0418:8", "const:4:8"]]
+ 00bb0418 ["CALL", null, ["callee:00c58120:8"]]
- 00bb037c bytes 359f0294
+ 00bb0418 bytes 429f0294
- 00bb03c4 ["INT_ADD", "register:40f0:8", ["const:bb03c4:8", "const:4:8"]]
- 00bb03c4 ["CALL", null, ["callee:00c58120:8"]]
+ 00bb0460 ["INT_ADD", "register:40f0:8", ["const:bb0460:8", "const:4:8"]]
+ 00bb0460 ["CALL", null, ["callee:00c58120:8"]]
- 00bb03c4 bytes 239f0294
+ 00bb0460 bytes 309f0294
~~~


<a id="compare-6bf2d881ba15ea070f8accff12843754"></a>

### [`00bb03f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb03f8.md) → [`00bb0494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce50.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cf20.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb03f8.md#insn-00bb0494) · [`00bb04d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb03f8.md#insn-00bb04d4)
- 新版 [`00bb0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md#insn-00bb0530) · [`00bb0570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0494.md#insn-00bb0570)

~~~diff
- 00bb0494 ["INT_ADD", "register:40f0:8", ["const:bb0494:8", "const:4:8"]]
- 00bb0494 ["CALL", null, ["callee:00c58120:8"]]
+ 00bb0530 ["INT_ADD", "register:40f0:8", ["const:bb0530:8", "const:4:8"]]
+ 00bb0530 ["CALL", null, ["callee:00c58120:8"]]
- 00bb0494 bytes ef9e0294
+ 00bb0530 bytes fc9e0294
- 00bb04d4 ["INT_ADD", "register:40f0:8", ["const:bb04d4:8", "const:4:8"]]
- 00bb04d4 ["CALL", null, ["callee:00c58120:8"]]
+ 00bb0570 ["INT_ADD", "register:40f0:8", ["const:bb0570:8", "const:4:8"]]
+ 00bb0570 ["CALL", null, ["callee:00c58120:8"]]
- 00bb04d4 bytes df9e0294
+ 00bb0570 bytes ec9e0294
~~~


<a id="compare-a8a1e24d8248bd85c034ef3b5f478208"></a>

### [`00bb0518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0518.md) → [`00bb05b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d020.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d0f0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0518.md#insn-00bb0598) · [`00bb05b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0518.md#insn-00bb05b0) · [`00bb062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0518.md#insn-00bb062c)
- 新版 [`00bb0634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb0634) · [`00bb064c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb064c) · [`00bb06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb05b4.md#insn-00bb06c8)

~~~diff
- 00bb0598 ["INT_ADD", "register:40f0:8", ["const:bb0598:8", "const:4:8"]]
- 00bb0598 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bb0634 ["INT_ADD", "register:40f0:8", ["const:bb0634:8", "const:4:8"]]
+ 00bb0634 ["CALL", null, ["callee:00c57f60:8"]]
- 00bb0598 bytes 3e9e0294
+ 00bb0634 bytes 4b9e0294
- 00bb05b0 ["INT_ADD", "register:40f0:8", ["const:bb05b0:8", "const:4:8"]]
- 00bb05b0 ["CALL", null, ["callee:00c5b680:8"]]
+ 00bb064c ["INT_ADD", "register:40f0:8", ["const:bb064c:8", "const:4:8"]]
+ 00bb064c ["CALL", null, ["callee:00c5b680:8"]]
- 00bb05b0 bytes 00ac0294
+ 00bb064c bytes 0dac0294
- 00bb062c ["INT_ADD", "register:40f0:8", ["const:bb062c:8", "const:4:8"]]
- 00bb062c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb06c8 ["INT_ADD", "register:40f0:8", ["const:bb06c8:8", "const:4:8"]]
+ 00bb06c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb062c bytes 219e0294
+ 00bb06c8 bytes 2e9e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6fc78f3e559f3a5a0da49e2aed98f8b"></a>

### [`00bb074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb074c.md) → [`00bb07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE12__find_equalIS2_EERPNS_16__tree_node_baseIPvEERPNS_15__

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce20.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5cef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cef0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb07ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb074c.md#insn-00bb07ec) · [`00bb082c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb074c.md#insn-00bb082c)
- 新版 [`00bb0888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md#insn-00bb0888) · [`00bb08c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb07e8.md#insn-00bb08c8)

~~~diff
- 00bb07ec ["INT_ADD", "register:40f0:8", ["const:bb07ec:8", "const:4:8"]]
- 00bb07ec ["CALL", null, ["callee:00c58120:8"]]
+ 00bb0888 ["INT_ADD", "register:40f0:8", ["const:bb0888:8", "const:4:8"]]
+ 00bb0888 ["CALL", null, ["callee:00c58120:8"]]
- 00bb07ec bytes 199e0294
+ 00bb0888 bytes 269e0294
- 00bb082c ["INT_ADD", "register:40f0:8", ["const:bb082c:8", "const:4:8"]]
- 00bb082c ["CALL", null, ["callee:00c58120:8"]]
+ 00bb08c8 ["INT_ADD", "register:40f0:8", ["const:bb08c8:8", "const:4:8"]]
+ 00bb08c8 ["CALL", null, ["callee:00c58120:8"]]
- 00bb082c bytes 099e0294
+ 00bb08c8 bytes 169e0294
~~~


<a id="compare-8924aabad88dc7f02a3250c50efd3a28"></a>

### [`00bb0fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0fa8.md) → [`00bb1044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb0fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0fa8.md#insn-00bb0fdc) · [`00bb0ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0fa8.md#insn-00bb0ff4) · [`00bb1038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0fa8.md#insn-00bb1038)
- 新版 [`00bb1078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb1078) · [`00bb1090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb1090) · [`00bb10d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1044.md#insn-00bb10d4)

~~~diff
- 00bb0fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0fdc ["INT_ADD", "register:40f0:8", ["const:bb0fdc:8", "const:4:8"]]
- 00bb0fdc ["CALLIND", null, ["register:0:8"]]
+ 00bb1078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb1078 ["INT_ADD", "register:40f0:8", ["const:bb1078:8", "const:4:8"]]
+ 00bb1078 ["CALLIND", null, ["register:0:8"]]
- 00bb0fdc bytes 00013fd6
+ 00bb1078 bytes 00013fd6
- 00bb0ff4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb0ff4 ["INT_ADD", "register:40f0:8", ["const:bb0ff4:8", "const:4:8"]]
- 00bb0ff4 ["CALLIND", null, ["register:0:8"]]
+ 00bb1090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1090 ["INT_ADD", "register:40f0:8", ["const:bb1090:8", "const:4:8"]]
+ 00bb1090 ["CALLIND", null, ["register:0:8"]]
- 00bb0ff4 bytes 20013fd6
+ 00bb1090 bytes 20013fd6
- 00bb1038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1038 ["INT_ADD", "register:40f0:8", ["const:bb1038:8", "const:4:8"]]
- 00bb1038 ["CALLIND", null, ["register:0:8"]]
+ 00bb10d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb10d4 ["INT_ADD", "register:40f0:8", ["const:bb10d4:8", "const:4:8"]]
+ 00bb10d4 ["CALLIND", null, ["register:0:8"]]
- 00bb1038 bytes 00013fd6
+ 00bb10d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af458a6e75d5d70b868138483651873"></a>

### [`00bb112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md) → [`00bb11c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md) FUN_00bb11c8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bb0a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0a90.md) [`00bb1390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1390.md) · 呼出先 1件 [`00c5d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0c0.md)
- 新版 呼出元 2件 [`00bb0b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md) [`00bb142c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md) · 呼出先 1件 [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md#insn-00bb1160) · [`00bb1178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md#insn-00bb1178) · [`00bb119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md#insn-00bb119c)
- 新版 [`00bb11fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb11fc) · [`00bb1214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb1214) · [`00bb1238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md#insn-00bb1238)

~~~diff
- 00bb1160 ["INT_ADD", "register:40f0:8", ["const:bb1160:8", "const:4:8"]]
- 00bb1160 ["CALL", null, ["callee:00c5d190:8"]]
+ 00bb11fc ["INT_ADD", "register:40f0:8", ["const:bb11fc:8", "const:4:8"]]
+ 00bb11fc ["CALL", null, ["callee:00c5d190:8"]]
- 00bb1160 bytes d8af0294
+ 00bb11fc bytes e5af0294
- 00bb1178 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bb1178 ["INT_ADD", "register:40f0:8", ["const:bb1178:8", "const:4:8"]]
- 00bb1178 ["CALLIND", null, ["register:0:8"]]
+ 00bb1214 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb1214 ["INT_ADD", "register:40f0:8", ["const:bb1214:8", "const:4:8"]]
+ 00bb1214 ["CALLIND", null, ["register:0:8"]]
- 00bb1178 bytes 20013fd6
+ 00bb1214 bytes 20013fd6
- 00bb119c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb119c ["INT_ADD", "register:40f0:8", ["const:bb119c:8", "const:4:8"]]
- 00bb119c ["CALLIND", null, ["register:0:8"]]
+ 00bb1238 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb1238 ["INT_ADD", "register:40f0:8", ["const:bb1238:8", "const:4:8"]]
+ 00bb1238 ["CALLIND", null, ["register:0:8"]]
- 00bb119c bytes 00013fd6
+ 00bb1238 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

