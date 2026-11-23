# v16.0.0 → v16.0.1 · 要調査の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-7b80642e316555d3e0d70ddae40c6a94"></a>

### [`004cb310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md) → [`004cb350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb350.md) _ZN5Botan13Threaded_Fork4sendEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c59130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md#insn-004cb348) · [`004cb358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md#insn-004cb358) · [`004cb528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md#insn-004cb528)
- 新版 `004cb388`（命令位置の公開資料なし） · `004cb398`（命令位置の公開資料なし） · `004cb568`（命令位置の公開資料なし）

~~~diff
- 004cb348 ["INT_ADD", "register:40f0:8", ["const:4cb348:8", "const:4:8"]]
- 004cb348 ["CALL", null, ["callee:00c59130:8"]]
+ 004cb388 ["INT_ADD", "register:40f0:8", ["const:4cb388:8", "const:4:8"]]
+ 004cb388 ["CALL", null, ["callee:00c59130:8"]]
- 004cb348 bytes 7a361e94
+ 004cb388 bytes 6a371e94
- 004cb358 ["INT_ADD", "register:40f0:8", ["const:4cb358:8", "const:4:8"]]
- 004cb358 ["CALL", null, ["callee:00c59130:8"]]
+ 004cb398 ["INT_ADD", "register:40f0:8", ["const:4cb398:8", "const:4:8"]]
+ 004cb398 ["CALL", null, ["callee:00c59130:8"]]
- 004cb358 bytes 76361e94
+ 004cb398 bytes 66371e94
- 004cb528 ["INT_ADD", "register:40f0:8", ["const:4cb528:8", "const:4:8"]]
- 004cb528 ["CALL", null, ["callee:005404ec:8"]]
+ 004cb568 ["INT_ADD", "register:40f0:8", ["const:4cb568:8", "const:4:8"]]
+ 004cb568 ["CALL", null, ["callee:005404ec:8"]]
- 004cb528 bytes e1d30194
+ 004cb568 bytes e1d30194
~~~


<a id="compare-6c042cb4389dbfd5aead6c13655b3069"></a>

### [`004cb580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md) → [`004cb5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb5c0.md) _ZN5Botan13Threaded_Fork20thread_delegate_workEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)
- 新版 呼出元 1件 [`00c59130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59130.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md#insn-004cb5c4) · [`004cb5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md#insn-004cb5dc) · [`004cb5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md#insn-004cb5fc)
- 新版 `004cb604`（命令位置の公開資料なし） · `004cb61c`（命令位置の公開資料なし） · `004cb63c`（命令位置の公開資料なし）

~~~diff
- 004cb5c4 ["INT_ADD", "register:40f0:8", ["const:4cb5c4:8", "const:4:8"]]
- 004cb5c4 ["CALL", null, ["callee:00c580e0:8"]]
+ 004cb604 ["INT_ADD", "register:40f0:8", ["const:4cb604:8", "const:4:8"]]
+ 004cb604 ["CALL", null, ["callee:00c580e0:8"]]
- 004cb5c4 bytes c7311e94
+ 004cb604 bytes b7321e94
- 004cb5dc ["INT_ADD", "register:40f0:8", ["const:4cb5dc:8", "const:4:8"]]
- 004cb5dc ["CALL", null, ["callee:00c580f0:8"]]
+ 004cb61c ["INT_ADD", "register:40f0:8", ["const:4cb61c:8", "const:4:8"]]
+ 004cb61c ["CALL", null, ["callee:00c580f0:8"]]
- 004cb5dc bytes c5311e94
+ 004cb61c bytes b5321e94
- 004cb5fc ["INT_ADD", "register:40f0:8", ["const:4cb5fc:8", "const:4:8"]]
- 004cb5fc ["CALL", null, ["callee:00c580f0:8"]]
+ 004cb63c ["INT_ADD", "register:40f0:8", ["const:4cb63c:8", "const:4:8"]]
+ 004cb63c ["CALL", null, ["callee:00c580f0:8"]]
- 004cb5fc bytes bd311e94
+ 004cb63c bytes ad321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7da43005ed0b5d20f341f52dc825962"></a>

### [`004cbe40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) → [`004cbe80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md) _ZN5Botan12HashFunction9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004cc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cbed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md#insn-004cbed0) · [`004cbee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md#insn-004cbee0) · [`004cbf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md#insn-004cbf1c)
- 新版 `004cbf10`（命令位置の公開資料なし） · `004cbf20`（命令位置の公開資料なし） · `004cbf5c`（命令位置の公開資料なし）

~~~diff
- 004cbed0 ["INT_ADD", "register:40f0:8", ["const:4cbed0:8", "const:4:8"]]
- 004cbed0 ["CALL", null, ["callee:00473540:8"]]
+ 004cbf10 ["INT_ADD", "register:40f0:8", ["const:4cbf10:8", "const:4:8"]]
+ 004cbf10 ["CALL", null, ["callee:00473540:8"]]
- 004cbed0 bytes 8c9dfe97
+ 004cbf10 bytes 8c9dfe97
- 004cbee0 ["INT_ADD", "register:40f0:8", ["const:4cbee0:8", "const:4:8"]]
- 004cbee0 ["CALL", null, ["callee:004cc04c:8"]]
+ 004cbf20 ["INT_ADD", "register:40f0:8", ["const:4cbf20:8", "const:4:8"]]
+ 004cbf20 ["CALL", null, ["callee:004cc04c:8"]]
- 004cbee0 bytes 4b000094
+ 004cbf20 bytes 4b000094
- 004cbf1c ["INT_ADD", "register:40f0:8", ["const:4cbf1c:8", "const:4:8"]]
- 004cbf1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004cbf5c ["INT_ADD", "register:40f0:8", ["const:4cbf5c:8", "const:4:8"]]
+ 004cbf5c ["CALL", null, ["callee:00c57eb0:8"]]
- 004cbf1c bytes e52e1e94
+ 004cbf5c bytes d52f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd6bf28c1a27777a610574a263e80759"></a>

### [`004cc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) → [`004cc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md) FUN_004cc04c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004cbe40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)
- 新版 呼出元 1件 [`004cbe80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbe80.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md#insn-004cc05c) · [`004cc070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md#insn-004cc070) · [`004cc08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md#insn-004cc08c)
- 新版 `004cc09c`（命令位置の公開資料なし） · `004cc0b0`（命令位置の公開資料なし） · `004cc0cc`（命令位置の公開資料なし）

~~~diff
- 004cc05c ["INT_ADD", "register:40f0:8", ["const:4cc05c:8", "const:4:8"]]
- 004cc05c ["CALL", null, ["callee:00540d7c:8"]]
+ 004cc09c ["INT_ADD", "register:40f0:8", ["const:4cc09c:8", "const:4:8"]]
+ 004cc09c ["CALL", null, ["callee:00540d7c:8"]]
- 004cc05c bytes 38d30194
+ 004cc09c bytes 38d30194
- 004cc070 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cc070 ["INT_ADD", "register:40f0:8", ["const:4cc070:8", "const:4:8"]]
- 004cc070 ["CALLIND", null, ["register:0:8"]]
+ 004cc0b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cc0b0 ["INT_ADD", "register:40f0:8", ["const:4cc0b0:8", "const:4:8"]]
+ 004cc0b0 ["CALLIND", null, ["register:0:8"]]
- 004cc070 bytes 00013fd6
+ 004cc0b0 bytes 00013fd6
- 004cc08c ["INT_ADD", "register:40f0:8", ["const:4cc08c:8", "const:4:8"]]
- 004cc08c ["CALL", null, ["callee:00c58df0:8"]]
+ 004cc0cc ["INT_ADD", "register:40f0:8", ["const:4cc0cc:8", "const:4:8"]]
+ 004cc0cc ["CALL", null, ["callee:00c58df0:8"]]
- 004cc08c bytes 59321e94
+ 004cc0cc bytes 49331e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-899a223335b13692677810f981ad1e04"></a>

### [`004cc14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md) → [`004cc18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md) FUN_004cc18c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c0ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`004c0be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md#insn-004cc17c) · [`004cc194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md#insn-004cc194) · [`004cc1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md#insn-004cc1b0)
- 新版 `004cc1bc`（命令位置の公開資料なし） · `004cc1d4`（命令位置の公開資料なし） · `004cc1f0`（命令位置の公開資料なし）

~~~diff
- 004cc17c ["INT_ADD", "register:40f0:8", ["const:4cc17c:8", "const:4:8"]]
- 004cc17c ["CALL", null, ["callee:00c57e90:8"]]
+ 004cc1bc ["INT_ADD", "register:40f0:8", ["const:4cc1bc:8", "const:4:8"]]
+ 004cc1bc ["CALL", null, ["callee:00c57e90:8"]]
- 004cc17c bytes 452e1e94
+ 004cc1bc bytes 352f1e94
- 004cc194 ["INT_ADD", "register:40f0:8", ["const:4cc194:8", "const:4:8"]]
- 004cc194 ["CALL", null, ["callee:00c58000:8"]]
+ 004cc1d4 ["INT_ADD", "register:40f0:8", ["const:4cc1d4:8", "const:4:8"]]
+ 004cc1d4 ["CALL", null, ["callee:00c58000:8"]]
- 004cc194 bytes 9b2e1e94
+ 004cc1d4 bytes 8b2f1e94
- 004cc1b0 ["INT_ADD", "register:40f0:8", ["const:4cc1b0:8", "const:4:8"]]
- 004cc1b0 ["CALL", null, ["callee:0049f42c:8"]]
+ 004cc1f0 ["INT_ADD", "register:40f0:8", ["const:4cc1f0:8", "const:4:8"]]
+ 004cc1f0 ["CALL", null, ["callee:0049f42c:8"]]
- 004cc1b0 bytes 8f4cff97
+ 004cc1f0 bytes 8f4cff97
~~~


<a id="compare-fc0e961a8499e09b1a57c2408ca57fd0"></a>

### [`004cc71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md) → [`004cc75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc75c.md) _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md#insn-004cc758) · [`004cc76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md#insn-004cc76c) · [`004cc784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md#insn-004cc784)
- 新版 `004cc798`（命令位置の公開資料なし） · `004cc7ac`（命令位置の公開資料なし） · `004cc7c4`（命令位置の公開資料なし）

~~~diff
- 004cc758 ["INT_ADD", "register:40f0:8", ["const:4cc758:8", "const:4:8"]]
- 004cc758 ["CALL", null, ["callee:004b3508:8"]]
+ 004cc798 ["INT_ADD", "register:40f0:8", ["const:4cc798:8", "const:4:8"]]
+ 004cc798 ["CALL", null, ["callee:004b3508:8"]]
- 004cc758 bytes 5c9bff97
+ 004cc798 bytes 5c9bff97
- 004cc76c ["INT_ADD", "register:40f0:8", ["const:4cc76c:8", "const:4:8"]]
- 004cc76c ["CALL", null, ["callee:00c58ae0:8"]]
+ 004cc7ac ["INT_ADD", "register:40f0:8", ["const:4cc7ac:8", "const:4:8"]]
+ 004cc7ac ["CALL", null, ["callee:00c58ae0:8"]]
- 004cc76c bytes dd2f1e94
+ 004cc7ac bytes cd301e94
- 004cc784 ["INT_ADD", "register:40f0:8", ["const:4cc784:8", "const:4:8"]]
- 004cc784 ["CALL", null, ["callee:005404ec:8"]]
+ 004cc7c4 ["INT_ADD", "register:40f0:8", ["const:4cc7c4:8", "const:4:8"]]
+ 004cc7c4 ["CALL", null, ["callee:005404ec:8"]]
- 004cc784 bytes 4acf0194
+ 004cc7c4 bytes 4acf0194
~~~


<a id="compare-21b050adbf6fe0c00a304db074ea6b05"></a>

### [`004cc7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md) → [`004cc7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc7fc.md) _ZN5Botan10hex_decodeEPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d50.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c59150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59150.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md#insn-004cc7fc) · [`004cc818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md#insn-004cc818) · [`004cc830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md#insn-004cc830)
- 新版 `004cc83c`（命令位置の公開資料なし） · `004cc858`（命令位置の公開資料なし） · `004cc870`（命令位置の公開資料なし）

~~~diff
- 004cc7fc ["INT_ADD", "register:40f0:8", ["const:4cc7fc:8", "const:4:8"]]
- 004cc7fc ["CALL", null, ["callee:00c57e90:8"]]
+ 004cc83c ["INT_ADD", "register:40f0:8", ["const:4cc83c:8", "const:4:8"]]
+ 004cc83c ["CALL", null, ["callee:00c57e90:8"]]
- 004cc7fc bytes a52c1e94
+ 004cc83c bytes 952d1e94
- 004cc818 ["INT_ADD", "register:40f0:8", ["const:4cc818:8", "const:4:8"]]
- 004cc818 ["CALL", null, ["callee:00c58090:8"]]
+ 004cc858 ["INT_ADD", "register:40f0:8", ["const:4cc858:8", "const:4:8"]]
+ 004cc858 ["CALL", null, ["callee:00c58090:8"]]
- 004cc818 bytes 1e2d1e94
+ 004cc858 bytes 0e2e1e94
- 004cc830 ["INT_ADD", "register:40f0:8", ["const:4cc830:8", "const:4:8"]]
- 004cc830 ["CALL", null, ["callee:00c58ae0:8"]]
+ 004cc870 ["INT_ADD", "register:40f0:8", ["const:4cc870:8", "const:4:8"]]
+ 004cc870 ["CALL", null, ["callee:00c58ae0:8"]]
- 004cc830 bytes ac2f1e94
+ 004cc870 bytes 9c301e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afe2ca3f617e3228754e8d0d9ddca0e7"></a>

### [`004cd100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md) → [`004cd140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd140.md) _ZN5Botan4HMAC5clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d80.md) · 呼出先 2件 [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c59180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59180.md) · 呼出先 2件 [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md#insn-004cd11c) · [`004cd134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md#insn-004cd134) · [`004cd144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md#insn-004cd144)
- 新版 `004cd15c`（命令位置の公開資料なし） · `004cd174`（命令位置の公開資料なし） · `004cd184`（命令位置の公開資料なし）

~~~diff
- 004cd11c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cd11c ["INT_ADD", "register:40f0:8", ["const:4cd11c:8", "const:4:8"]]
- 004cd11c ["CALLIND", null, ["register:0:8"]]
+ 004cd15c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd15c ["INT_ADD", "register:40f0:8", ["const:4cd15c:8", "const:4:8"]]
+ 004cd15c ["CALLIND", null, ["register:0:8"]]
- 004cd11c bytes 00013fd6
+ 004cd15c bytes 00013fd6
- 004cd134 ["INT_ADD", "register:40f0:8", ["const:4cd134:8", "const:4:8"]]
- 004cd134 ["CALL", null, ["callee:00c58090:8"]]
+ 004cd174 ["INT_ADD", "register:40f0:8", ["const:4cd174:8", "const:4:8"]]
+ 004cd174 ["CALL", null, ["callee:00c58090:8"]]
- 004cd134 bytes d72a1e94
+ 004cd174 bytes c72b1e94
- 004cd144 ["INT_ADD", "register:40f0:8", ["const:4cd144:8", "const:4:8"]]
- 004cd144 ["CALL", null, ["callee:00540b78:8"]]
+ 004cd184 ["INT_ADD", "register:40f0:8", ["const:4cd184:8", "const:4:8"]]
+ 004cd184 ["CALL", null, ["callee:00540b78:8"]]
- 004cd144 bytes 7dce0194
+ 004cd184 bytes 7dce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4a0ffa0139d33a00733ed817f0f815"></a>

### [`004cd29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md) → [`004cd2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd2dc.md) _ZNK5Botan4HMAC5cloneEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58da0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c591a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2b0) · [`004cd2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2c8) · [`004cd2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2d4)
- 新版 `004cd2f0`（命令位置の公開資料なし） · `004cd308`（命令位置の公開資料なし） · `004cd314`（命令位置の公開資料なし）

~~~diff
- 004cd2b0 ["INT_ADD", "register:40f0:8", ["const:4cd2b0:8", "const:4:8"]]
- 004cd2b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004cd2f0 ["INT_ADD", "register:40f0:8", ["const:4cd2f0:8", "const:4:8"]]
+ 004cd2f0 ["CALL", null, ["callee:00c57e90:8"]]
- 004cd2b0 bytes f8291e94
+ 004cd2f0 bytes e82a1e94
- 004cd2c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd2c8 ["INT_ADD", "register:40f0:8", ["const:4cd2c8:8", "const:4:8"]]
- 004cd2c8 ["CALLIND", null, ["register:0:8"]]
+ 004cd308 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cd308 ["INT_ADD", "register:40f0:8", ["const:4cd308:8", "const:4:8"]]
+ 004cd308 ["CALLIND", null, ["register:0:8"]]
- 004cd2c8 bytes 20013fd6
+ 004cd308 bytes 20013fd6
- 004cd2d4 ["INT_ADD", "register:40f0:8", ["const:4cd2d4:8", "const:4:8"]]
- 004cd2d4 ["CALL", null, ["callee:00c591a0:8"]]
+ 004cd314 ["INT_ADD", "register:40f0:8", ["const:4cd314:8", "const:4:8"]]
+ 004cd314 ["CALL", null, ["callee:00c591a0:8"]]
- 004cd2d4 bytes b32e1e94
+ 004cd314 bytes a32f1e94
~~~


<a id="compare-9217cdc1f46515c3a3bb8ad975a6024a"></a>

### [`004cd4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md) → [`004cd4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd4fc.md) _ZN5Botan3KDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)
- 新版 呼出元 1件 [`00c591b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591b0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md#insn-004cd504) · [`004cd510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md#insn-004cd510) · [`004cd520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md#insn-004cd520)
- 新版 `004cd544`（命令位置の公開資料なし） · `004cd550`（命令位置の公開資料なし） · `004cd560`（命令位置の公開資料なし）

~~~diff
- 004cd504 ["INT_ADD", "register:40f0:8", ["const:4cd504:8", "const:4:8"]]
- 004cd504 ["CALL", null, ["callee:0043bb20:8"]]
+ 004cd544 ["INT_ADD", "register:40f0:8", ["const:4cd544:8", "const:4:8"]]
+ 004cd544 ["CALL", null, ["callee:0043bb20:8"]]
- 004cd504 bytes 77b9fd97
+ 004cd544 bytes 77b9fd97
- 004cd510 ["INT_ADD", "register:40f0:8", ["const:4cd510:8", "const:4:8"]]
- 004cd510 ["CALL", null, ["callee:00c58d40:8"]]
+ 004cd550 ["INT_ADD", "register:40f0:8", ["const:4cd550:8", "const:4:8"]]
+ 004cd550 ["CALL", null, ["callee:00c58d40:8"]]
- 004cd510 bytes 0c2d1e94
+ 004cd550 bytes fc2d1e94
- 004cd520 ["INT_ADD", "register:40f0:8", ["const:4cd520:8", "const:4:8"]]
- 004cd520 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004cd560 ["INT_ADD", "register:40f0:8", ["const:4cd560:8", "const:4:8"]]
+ 004cd560 ["CALL", null, ["callee:00c57eb0:8"]]
- 004cd520 bytes 64291e94
+ 004cd560 bytes 542a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd108b9dd7ccc2ef91b064e24d3c239"></a>

### [`004cd748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) → [`004cd788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md) _ZN5Botan3KDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004cd8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md#insn-004cd794) · [`004cd7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md#insn-004cd7a4) · [`004cd7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md#insn-004cd7e0)
- 新版 `004cd7d4`（命令位置の公開資料なし） · `004cd7e4`（命令位置の公開資料なし） · `004cd820`（命令位置の公開資料なし）

~~~diff
- 004cd794 ["INT_ADD", "register:40f0:8", ["const:4cd794:8", "const:4:8"]]
- 004cd794 ["CALL", null, ["callee:00473540:8"]]
+ 004cd7d4 ["INT_ADD", "register:40f0:8", ["const:4cd7d4:8", "const:4:8"]]
+ 004cd7d4 ["CALL", null, ["callee:00473540:8"]]
- 004cd794 bytes 5b97fe97
+ 004cd7d4 bytes 5b97fe97
- 004cd7a4 ["INT_ADD", "register:40f0:8", ["const:4cd7a4:8", "const:4:8"]]
- 004cd7a4 ["CALL", null, ["callee:004cd8a8:8"]]
+ 004cd7e4 ["INT_ADD", "register:40f0:8", ["const:4cd7e4:8", "const:4:8"]]
+ 004cd7e4 ["CALL", null, ["callee:004cd8a8:8"]]
- 004cd7a4 bytes 31000094
+ 004cd7e4 bytes 31000094
- 004cd7e0 ["INT_ADD", "register:40f0:8", ["const:4cd7e0:8", "const:4:8"]]
- 004cd7e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004cd820 ["INT_ADD", "register:40f0:8", ["const:4cd820:8", "const:4:8"]]
+ 004cd820 ["CALL", null, ["callee:00c57eb0:8"]]
- 004cd7e0 bytes b4281e94
+ 004cd820 bytes a4291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fce9f21b1230cbb6eb475113b90601f"></a>

### [`004cd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) → [`004cd8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md) FUN_004cd8a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004cd748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md)
- 新版 呼出元 1件 [`004cd788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd788.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c591b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md#insn-004cd8b8) · [`004cd8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md#insn-004cd8cc) · [`004cd8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md#insn-004cd8e4)
- 新版 `004cd8f8`（命令位置の公開資料なし） · `004cd90c`（命令位置の公開資料なし） · `004cd924`（命令位置の公開資料なし）

~~~diff
- 004cd8b8 ["INT_ADD", "register:40f0:8", ["const:4cd8b8:8", "const:4:8"]]
- 004cd8b8 ["CALL", null, ["callee:00540d7c:8"]]
+ 004cd8f8 ["INT_ADD", "register:40f0:8", ["const:4cd8f8:8", "const:4:8"]]
+ 004cd8f8 ["CALL", null, ["callee:00540d7c:8"]]
- 004cd8b8 bytes 21cd0194
+ 004cd8f8 bytes 21cd0194
- 004cd8cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004cd8cc ["INT_ADD", "register:40f0:8", ["const:4cd8cc:8", "const:4:8"]]
- 004cd8cc ["CALLIND", null, ["register:0:8"]]
+ 004cd90c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd90c ["INT_ADD", "register:40f0:8", ["const:4cd90c:8", "const:4:8"]]
+ 004cd90c ["CALLIND", null, ["register:0:8"]]
- 004cd8cc bytes 00013fd6
+ 004cd90c bytes 00013fd6
- 004cd8e4 ["INT_ADD", "register:40f0:8", ["const:4cd8e4:8", "const:4:8"]]
- 004cd8e4 ["CALL", null, ["callee:00c591b0:8"]]
+ 004cd924 ["INT_ADD", "register:40f0:8", ["const:4cd924:8", "const:4:8"]]
+ 004cd924 ["CALL", null, ["callee:00c591b0:8"]]
- 004cd8e4 bytes 332d1e94
+ 004cd924 bytes 232e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f736e268f59d742c5e8bb0c5f73e9b9"></a>

### [`004ce010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce010.md) → [`004ce050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce050.md) _ZNK5Botan16PK_Encryptor_EME18maximum_input_sizeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce010.md#insn-004ce024)
- 新版 `004ce064`（命令位置の公開資料なし）

~~~diff
- 004ce024 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ce024 ["INT_ADD", "register:40f0:8", ["const:4ce024:8", "const:4:8"]]
- 004ce024 ["CALLIND", null, ["register:0:8"]]
+ 004ce064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce064 ["INT_ADD", "register:40f0:8", ["const:4ce064:8", "const:4:8"]]
+ 004ce064 ["CALLIND", null, ["register:0:8"]]
- 004ce024 bytes 00013fd6
+ 004ce064 bytes 00013fd6
~~~


<a id="compare-b7814eb2fb7b41bea1109042e193fcd5"></a>

### [`004ce034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md) → [`004ce074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce074.md) _ZN5Botan7KeyPair27signature_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringIc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e20.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e30.md) [`00c58e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e40.md)
- 新版 呼出元 1件 [`00c59220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59220.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59230.md) [`00c59240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce078) · [`004ce088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce088) · [`004ce0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce0a4)
- 新版 `004ce0b8`（命令位置の公開資料なし） · `004ce0c8`（命令位置の公開資料なし） · `004ce0e4`（命令位置の公開資料なし）

~~~diff
- 004ce078 ["INT_ADD", "register:40f0:8", ["const:4ce078:8", "const:4:8"]]
- 004ce078 ["CALL", null, ["callee:00c59230:8"]]
+ 004ce0b8 ["INT_ADD", "register:40f0:8", ["const:4ce0b8:8", "const:4:8"]]
+ 004ce0b8 ["CALL", null, ["callee:00c59230:8"]]
- 004ce078 bytes 6e2b1e94
+ 004ce0b8 bytes 5e2c1e94
- 004ce088 ["INT_ADD", "register:40f0:8", ["const:4ce088:8", "const:4:8"]]
- 004ce088 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ce0c8 ["INT_ADD", "register:40f0:8", ["const:4ce0c8:8", "const:4:8"]]
+ 004ce0c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ce088 bytes 8a261e94
+ 004ce0c8 bytes 7a271e94
- 004ce0a4 ["INT_ADD", "register:40f0:8", ["const:4ce0a4:8", "const:4:8"]]
- 004ce0a4 ["CALL", null, ["callee:00c59240:8"]]
+ 004ce0e4 ["INT_ADD", "register:40f0:8", ["const:4ce0e4:8", "const:4:8"]]
+ 004ce0e4 ["CALL", null, ["callee:00c59240:8"]]
- 004ce0a4 bytes 672b1e94
+ 004ce0e4 bytes 572c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121f613ebf28fd30721e6ea7b7a539cd"></a>

### [`004ce28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md) → [`004ce2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce2cc.md) _ZN5Botan25MessageAuthenticationCode6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md)
- 新版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce2d8) · [`004ce2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce2e4) · [`004ce2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce2f4)
- 新版 `004ce318`（命令位置の公開資料なし） · `004ce324`（命令位置の公開資料なし） · `004ce334`（命令位置の公開資料なし）

~~~diff
- 004ce2d8 ["INT_ADD", "register:40f0:8", ["const:4ce2d8:8", "const:4:8"]]
- 004ce2d8 ["CALL", null, ["callee:0043bb20:8"]]
+ 004ce318 ["INT_ADD", "register:40f0:8", ["const:4ce318:8", "const:4:8"]]
+ 004ce318 ["CALL", null, ["callee:0043bb20:8"]]
- 004ce2d8 bytes 02b6fd97
+ 004ce318 bytes 02b6fd97
- 004ce2e4 ["INT_ADD", "register:40f0:8", ["const:4ce2e4:8", "const:4:8"]]
- 004ce2e4 ["CALL", null, ["callee:00c58d40:8"]]
+ 004ce324 ["INT_ADD", "register:40f0:8", ["const:4ce324:8", "const:4:8"]]
+ 004ce324 ["CALL", null, ["callee:00c58d40:8"]]
- 004ce2e4 bytes 97291e94
+ 004ce324 bytes 872a1e94
- 004ce2f4 ["INT_ADD", "register:40f0:8", ["const:4ce2f4:8", "const:4:8"]]
- 004ce2f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ce334 ["INT_ADD", "register:40f0:8", ["const:4ce334:8", "const:4:8"]]
+ 004ce334 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ce2f4 bytes ef251e94
+ 004ce334 bytes df261e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d3d261c310dcdfc42bac328c0336029"></a>

### [`004ce544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) → [`004ce584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md) _ZN5Botan25MessageAuthenticationCode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004ce6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004ce6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md#insn-004ce5b4) · [`004ce5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md#insn-004ce5c4) · [`004ce600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md#insn-004ce600)
- 新版 `004ce5f4`（命令位置の公開資料なし） · `004ce604`（命令位置の公開資料なし） · `004ce640`（命令位置の公開資料なし）

~~~diff
- 004ce5b4 ["INT_ADD", "register:40f0:8", ["const:4ce5b4:8", "const:4:8"]]
- 004ce5b4 ["CALL", null, ["callee:00473540:8"]]
+ 004ce5f4 ["INT_ADD", "register:40f0:8", ["const:4ce5f4:8", "const:4:8"]]
+ 004ce5f4 ["CALL", null, ["callee:00473540:8"]]
- 004ce5b4 bytes d393fe97
+ 004ce5f4 bytes d393fe97
- 004ce5c4 ["INT_ADD", "register:40f0:8", ["const:4ce5c4:8", "const:4:8"]]
- 004ce5c4 ["CALL", null, ["callee:004ce6e8:8"]]
+ 004ce604 ["INT_ADD", "register:40f0:8", ["const:4ce604:8", "const:4:8"]]
+ 004ce604 ["CALL", null, ["callee:004ce6e8:8"]]
- 004ce5c4 bytes 39000094
+ 004ce604 bytes 39000094
- 004ce600 ["INT_ADD", "register:40f0:8", ["const:4ce600:8", "const:4:8"]]
- 004ce600 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ce640 ["INT_ADD", "register:40f0:8", ["const:4ce640:8", "const:4:8"]]
+ 004ce640 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ce600 bytes 2c251e94
+ 004ce640 bytes 1c261e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b7035e37f017fcc9c7bc88d44ddebba"></a>

### [`004ce6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) → [`004ce6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md) FUN_004ce6e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ce544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md)
- 新版 呼出元 1件 [`004ce584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce584.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md#insn-004ce6f8) · [`004ce70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md#insn-004ce70c) · [`004ce728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md#insn-004ce728)
- 新版 `004ce738`（命令位置の公開資料なし） · `004ce74c`（命令位置の公開資料なし） · `004ce768`（命令位置の公開資料なし）

~~~diff
- 004ce6f8 ["INT_ADD", "register:40f0:8", ["const:4ce6f8:8", "const:4:8"]]
- 004ce6f8 ["CALL", null, ["callee:00540d7c:8"]]
+ 004ce738 ["INT_ADD", "register:40f0:8", ["const:4ce738:8", "const:4:8"]]
+ 004ce738 ["CALL", null, ["callee:00540d7c:8"]]
- 004ce6f8 bytes 91c90194
+ 004ce738 bytes 91c90194
- 004ce70c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ce70c ["INT_ADD", "register:40f0:8", ["const:4ce70c:8", "const:4:8"]]
- 004ce70c ["CALLIND", null, ["register:0:8"]]
+ 004ce74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce74c ["INT_ADD", "register:40f0:8", ["const:4ce74c:8", "const:4:8"]]
+ 004ce74c ["CALLIND", null, ["register:0:8"]]
- 004ce70c bytes 00013fd6
+ 004ce74c bytes 00013fd6
- 004ce728 ["INT_ADD", "register:40f0:8", ["const:4ce728:8", "const:4:8"]]
- 004ce728 ["CALL", null, ["callee:00c58e90:8"]]
+ 004ce768 ["INT_ADD", "register:40f0:8", ["const:4ce768:8", "const:4:8"]]
+ 004ce768 ["CALL", null, ["callee:00c58e90:8"]]
- 004ce728 bytes da281e94
+ 004ce768 bytes ca291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ac5c5afc08d8c3ac2c3019198912df"></a>

### [`004cea38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004cea38.md) → [`004cea78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004cea78.md) _ZN5Botan3MD510compress_nEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004cea38.md#insn-004cf450)
- 新版 `004cf490`（命令位置の公開資料なし）

~~~diff
- 004cf450 ["INT_ADD", "register:40f0:8", ["const:4cf450:8", "const:4:8"]]
- 004cf450 ["CALL", null, ["callee:00c58000:8"]]
+ 004cf490 ["INT_ADD", "register:40f0:8", ["const:4cf490:8", "const:4:8"]]
+ 004cf490 ["CALL", null, ["callee:00c58000:8"]]
- 004cf450 bytes ec211e94
+ 004cf490 bytes dc221e94
~~~


<a id="compare-3c0ec76e863e41a316992f4b5f130eae"></a>

### [`004cf510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf510.md) → [`004cf550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf550.md) _ZN5Botan16MDx_HashFunction5clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf510.md#insn-004cf534)
- 新版 `004cf574`（命令位置の公開資料なし）

~~~diff
- 004cf534 ["INT_ADD", "register:40f0:8", ["const:4cf534:8", "const:4:8"]]
- 004cf534 ["CALL", null, ["callee:00c58090:8"]]
+ 004cf574 ["INT_ADD", "register:40f0:8", ["const:4cf574:8", "const:4:8"]]
+ 004cf574 ["CALL", null, ["callee:00c58090:8"]]
- 004cf534 bytes d7211e94
+ 004cf574 bytes c7221e94
~~~


<a id="compare-7cebcb1968056b23993a6e41d7675912"></a>

### [`004cf59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md) → [`004cf5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf5dc.md) _ZN5Botan16MDx_HashFunction8add_dataEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md#insn-004cf5ec) · [`004cf618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md#insn-004cf618) · [`004cf66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md#insn-004cf66c)
- 新版 `004cf62c`（命令位置の公開資料なし） · `004cf658`（命令位置の公開資料なし） · `004cf6ac`（命令位置の公開資料なし）

~~~diff
- 004cf5ec ["INT_ADD", "register:40f0:8", ["const:4cf5ec:8", "const:4:8"]]
- 004cf5ec ["CALL", null, ["callee:00c57f40:8"]]
+ 004cf62c ["INT_ADD", "register:40f0:8", ["const:4cf62c:8", "const:4:8"]]
+ 004cf62c ["CALL", null, ["callee:00c57f40:8"]]
- 004cf5ec bytes 55211e94
+ 004cf62c bytes 45221e94
- 004cf618 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf618 ["INT_ADD", "register:40f0:8", ["const:4cf618:8", "const:4:8"]]
- 004cf618 ["CALLIND", null, ["register:0:8"]]
+ 004cf658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf658 ["INT_ADD", "register:40f0:8", ["const:4cf658:8", "const:4:8"]]
+ 004cf658 ["CALLIND", null, ["register:0:8"]]
- 004cf618 bytes 00013fd6
+ 004cf658 bytes 00013fd6
- 004cf66c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf66c ["INT_ADD", "register:40f0:8", ["const:4cf66c:8", "const:4:8"]]
- 004cf66c ["CALLIND", null, ["register:0:8"]]
+ 004cf6ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf6ac ["INT_ADD", "register:40f0:8", ["const:4cf6ac:8", "const:4:8"]]
+ 004cf6ac ["CALLIND", null, ["register:0:8"]]
- 004cf66c bytes 00013fd6
+ 004cf6ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-559b645cd6fc8830ccf671702d0c0c41"></a>

### [`004cf6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md) → [`004cf708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf708.md) _ZN5Botan16MDx_HashFunction12final_resultEPh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cf754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md#insn-004cf754) · [`004cf768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md#insn-004cf768) · [`004cf784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md#insn-004cf784)
- 新版 `004cf794`（命令位置の公開資料なし） · `004cf7a8`（命令位置の公開資料なし） · `004cf7c4`（命令位置の公開資料なし）

~~~diff
- 004cf754 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf754 ["INT_ADD", "register:40f0:8", ["const:4cf754:8", "const:4:8"]]
- 004cf754 ["CALLIND", null, ["register:0:8"]]
+ 004cf794 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cf794 ["INT_ADD", "register:40f0:8", ["const:4cf794:8", "const:4:8"]]
+ 004cf794 ["CALLIND", null, ["register:0:8"]]
- 004cf754 bytes 20013fd6
+ 004cf794 bytes 20013fd6
- 004cf768 ["INT_ADD", "register:40f0:8", ["const:4cf768:8", "const:4:8"]]
- 004cf768 ["CALL", null, ["callee:00c58090:8"]]
+ 004cf7a8 ["INT_ADD", "register:40f0:8", ["const:4cf7a8:8", "const:4:8"]]
+ 004cf7a8 ["CALL", null, ["callee:00c58090:8"]]
- 004cf768 bytes 4a211e94
+ 004cf7a8 bytes 3a221e94
- 004cf784 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf784 ["INT_ADD", "register:40f0:8", ["const:4cf784:8", "const:4:8"]]
- 004cf784 ["CALLIND", null, ["register:0:8"]]
+ 004cf7c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf7c4 ["INT_ADD", "register:40f0:8", ["const:4cf7c4:8", "const:4:8"]]
+ 004cf7c4 ["CALLIND", null, ["register:0:8"]]
- 004cf784 bytes 00013fd6
+ 004cf7c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d2144d8c7aa62e5ebb6ab6cdc74fd92"></a>

### [`004cfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfd88.md) → [`004cfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfdc8.md) _ZNK5Botan13PKCS7_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00544c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00544cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544cdc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cfdf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfd88.md#insn-004cfdf4) · [`004cfe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfd88.md#insn-004cfe20)
- 新版 `004cfe34`（命令位置の公開資料なし） · `004cfe60`（命令位置の公開資料なし）

~~~diff
- 004cfdf4 ["INT_ADD", "register:40f0:8", ["const:4cfdf4:8", "const:4:8"]]
- 004cfdf4 ["CALL", null, ["callee:00544cdc:8"]]
+ 004cfe34 ["INT_ADD", "register:40f0:8", ["const:4cfe34:8", "const:4:8"]]
+ 004cfe34 ["CALL", null, ["callee:00544cdc:8"]]
- 004cfdf4 bytes aad30194
+ 004cfe34 bytes aad30194
- 004cfe20 ["INT_ADD", "register:40f0:8", ["const:4cfe20:8", "const:4:8"]]
- 004cfe20 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004cfe60 ["INT_ADD", "register:40f0:8", ["const:4cfe60:8", "const:4:8"]]
+ 004cfe60 ["CALL", null, ["callee:00c57ee0:8"]]
- 004cfe20 bytes 301f1e94
+ 004cfe60 bytes 20201e94
~~~


<a id="compare-3893bf7e66bd05f07ced730b48c4e4b5"></a>

### [`004d024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md) → [`004d028c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d028c.md) _ZNK5Botan17ANSI_X923_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00544c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00544cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544cdc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d029c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md#insn-004d029c) · [`004d02e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md#insn-004d02e8) · [`004d0314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md#insn-004d0314)
- 新版 `004d02dc`（命令位置の公開資料なし） · `004d0328`（命令位置の公開資料なし） · `004d0354`（命令位置の公開資料なし）

~~~diff
- 004d029c ["INT_ADD", "register:40f0:8", ["const:4d029c:8", "const:4:8"]]
- 004d029c ["CALL", null, ["callee:005411a4:8"]]
+ 004d02dc ["INT_ADD", "register:40f0:8", ["const:4d02dc:8", "const:4:8"]]
+ 004d02dc ["CALL", null, ["callee:005411a4:8"]]
- 004d029c bytes b2c30194
+ 004d02dc bytes b2c30194
- 004d02e8 ["INT_ADD", "register:40f0:8", ["const:4d02e8:8", "const:4:8"]]
- 004d02e8 ["CALL", null, ["callee:00544cdc:8"]]
+ 004d0328 ["INT_ADD", "register:40f0:8", ["const:4d0328:8", "const:4:8"]]
+ 004d0328 ["CALL", null, ["callee:00544cdc:8"]]
- 004d02e8 bytes 6dd20194
+ 004d0328 bytes 6dd20194
- 004d0314 ["INT_ADD", "register:40f0:8", ["const:4d0314:8", "const:4:8"]]
- 004d0314 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004d0354 ["INT_ADD", "register:40f0:8", ["const:4d0354:8", "const:4:8"]]
+ 004d0354 ["CALL", null, ["callee:00c57ee0:8"]]
- 004d0314 bytes f31d1e94
+ 004d0354 bytes e31e1e94
~~~


<a id="compare-d26ceb4882827178dce1e9ec64989ced"></a>

### [`004d0714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md) → [`004d0754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0754.md) _ZNK5Botan19OneAndZeros_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d0764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md#insn-004d0764) · [`004d07b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md#insn-004d07b8) · [`004d07e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md#insn-004d07e4)
- 新版 `004d07a4`（命令位置の公開資料なし） · `004d07f8`（命令位置の公開資料なし） · `004d0824`（命令位置の公開資料なし）

~~~diff
- 004d0764 ["INT_ADD", "register:40f0:8", ["const:4d0764:8", "const:4:8"]]
- 004d0764 ["CALL", null, ["callee:005411a4:8"]]
+ 004d07a4 ["INT_ADD", "register:40f0:8", ["const:4d07a4:8", "const:4:8"]]
+ 004d07a4 ["CALL", null, ["callee:005411a4:8"]]
- 004d0764 bytes 80c20194
+ 004d07a4 bytes 80c20194
- 004d07b8 ["INT_ADD", "register:40f0:8", ["const:4d07b8:8", "const:4:8"]]
- 004d07b8 ["CALL", null, ["callee:005411a4:8"]]
+ 004d07f8 ["INT_ADD", "register:40f0:8", ["const:4d07f8:8", "const:4:8"]]
+ 004d07f8 ["CALL", null, ["callee:005411a4:8"]]
- 004d07b8 bytes 6bc20194
+ 004d07f8 bytes 6bc20194
- 004d07e4 ["INT_ADD", "register:40f0:8", ["const:4d07e4:8", "const:4:8"]]
- 004d07e4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004d0824 ["INT_ADD", "register:40f0:8", ["const:4d0824:8", "const:4:8"]]
+ 004d0824 ["CALL", null, ["callee:00c57ee0:8"]]
- 004d07e4 bytes bf1c1e94
+ 004d0824 bytes af1d1e94
~~~


<a id="compare-20495e452c217e04ca6eacec01a0e3e6"></a>

### [`004d088c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d088c.md) → [`004d08cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d08cc.md) _ZNK5Botan11ESP_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d08cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d088c.md#insn-004d08cc) · [`004d091c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d088c.md#insn-004d091c)
- 新版 `004d090c`（命令位置の公開資料なし） · `004d095c`（命令位置の公開資料なし）

~~~diff
- 004d08cc ["INT_ADD", "register:40f0:8", ["const:4d08cc:8", "const:4:8"]]
- 004d08cc ["CALL", null, ["callee:005411a4:8"]]
+ 004d090c ["INT_ADD", "register:40f0:8", ["const:4d090c:8", "const:4:8"]]
+ 004d090c ["CALL", null, ["callee:005411a4:8"]]
- 004d08cc bytes 26c20194
+ 004d090c bytes 26c20194
- 004d091c ["INT_ADD", "register:40f0:8", ["const:4d091c:8", "const:4:8"]]
- 004d091c ["CALL", null, ["callee:00c57ee0:8"]]
+ 004d095c ["INT_ADD", "register:40f0:8", ["const:4d095c:8", "const:4:8"]]
+ 004d095c ["CALL", null, ["callee:00c57ee0:8"]]
- 004d091c bytes 711c1e94
+ 004d095c bytes 611d1e94
~~~


<a id="compare-ed8e4aa4e73aa6c35dbf62b41aac5fd2"></a>

### [`004d0d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md) → [`004d0d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0d70.md) _ZN5Botan12StreamCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a60.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)
- 新版 呼出元 1件 [`00c58e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e60.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d0d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md#insn-004d0d78) · [`004d0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md#insn-004d0d84) · [`004d0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md#insn-004d0d94)
- 新版 `004d0db8`（命令位置の公開資料なし） · `004d0dc4`（命令位置の公開資料なし） · `004d0dd4`（命令位置の公開資料なし）

~~~diff
- 004d0d78 ["INT_ADD", "register:40f0:8", ["const:4d0d78:8", "const:4:8"]]
- 004d0d78 ["CALL", null, ["callee:0043bb20:8"]]
+ 004d0db8 ["INT_ADD", "register:40f0:8", ["const:4d0db8:8", "const:4:8"]]
+ 004d0db8 ["CALL", null, ["callee:0043bb20:8"]]
- 004d0d78 bytes 5aabfd97
+ 004d0db8 bytes 5aabfd97
- 004d0d84 ["INT_ADD", "register:40f0:8", ["const:4d0d84:8", "const:4:8"]]
- 004d0d84 ["CALL", null, ["callee:00c58d40:8"]]
+ 004d0dc4 ["INT_ADD", "register:40f0:8", ["const:4d0dc4:8", "const:4:8"]]
+ 004d0dc4 ["CALL", null, ["callee:00c58d40:8"]]
- 004d0d84 bytes ef1e1e94
+ 004d0dc4 bytes df1f1e94
- 004d0d94 ["INT_ADD", "register:40f0:8", ["const:4d0d94:8", "const:4:8"]]
- 004d0d94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004d0dd4 ["INT_ADD", "register:40f0:8", ["const:4d0dd4:8", "const:4:8"]]
+ 004d0dd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004d0d94 bytes 471b1e94
+ 004d0dd4 bytes 371c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1696d0c0a491ddd2438ae22639e78a1"></a>

### [`004d1c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md) → [`004d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1c40.md) _ZN5Botan11Cipher_Mode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d1c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md#insn-004d1c78) · [`004d1c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md#insn-004d1c88) · [`004d1c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md#insn-004d1c98)
- 新版 `004d1cb8`（命令位置の公開資料なし） · `004d1cc8`（命令位置の公開資料なし） · `004d1cd8`（命令位置の公開資料なし）

~~~diff
- 004d1c78 ["INT_ADD", "register:40f0:8", ["const:4d1c78:8", "const:4:8"]]
- 004d1c78 ["CALL", null, ["callee:00473540:8"]]
+ 004d1cb8 ["INT_ADD", "register:40f0:8", ["const:4d1cb8:8", "const:4:8"]]
+ 004d1cb8 ["CALL", null, ["callee:00473540:8"]]
- 004d1c78 bytes 2286fe97
+ 004d1cb8 bytes 2286fe97
- 004d1c88 ["INT_ADD", "register:40f0:8", ["const:4d1c88:8", "const:4:8"]]
- 004d1c88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004d1cc8 ["INT_ADD", "register:40f0:8", ["const:4d1cc8:8", "const:4:8"]]
+ 004d1cc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004d1c88 bytes 8a171e94
+ 004d1cc8 bytes 7a181e94
- 004d1c98 ["INT_ADD", "register:40f0:8", ["const:4d1c98:8", "const:4:8"]]
- 004d1c98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004d1cd8 ["INT_ADD", "register:40f0:8", ["const:4d1cd8:8", "const:4:8"]]
+ 004d1cd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004d1c98 bytes 86171e94
+ 004d1cd8 bytes 76181e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1324fba518bda69a2072ab9856b38b3d"></a>

### [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) → [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) FUN_004d6e68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 10件 [`004b90a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004d1f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1f50.md) [`004d235c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md) [`004d3724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3724.md)
- 新版 呼出元 5件 [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) [`004ba1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba1f4.md) [`004db6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db6a0.md) [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) · 呼出先 10件 [`004b90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b90e0.md) [`004d1f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1f90.md) [`004d239c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d239c.md) [`004d2b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2b90.md) [`004d3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d3/004d3764.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md#insn-004d6e74) · [`004d706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md#insn-004d706c)
- 新版 `004d6eb4`（命令位置の公開資料なし） · `004d70ac`（命令位置の公開資料なし）

~~~diff
- 004d6e74 ["INT_ADD", "register:40f0:8", ["const:4d6e74:8", "const:4:8"]]
- 004d6e74 ["CALL", null, ["callee:00c58090:8"]]
+ 004d6eb4 ["INT_ADD", "register:40f0:8", ["const:4d6eb4:8", "const:4:8"]]
+ 004d6eb4 ["CALL", null, ["callee:00c58090:8"]]
- 004d6e74 bytes 87031e94
+ 004d6eb4 bytes 77041e94
- 004d706c ["INT_ADD", "register:40f0:8", ["const:4d706c:8", "const:4:8"]]
- 004d706c ["CALL", null, ["callee:004d72bc:8"]]
+ 004d70ac ["INT_ADD", "register:40f0:8", ["const:4d70ac:8", "const:4:8"]]
+ 004d70ac ["CALL", null, ["callee:004d72bc:8"]]
- 004d706c bytes 84000094
+ 004d70ac bytes 84000094
~~~


<a id="compare-857d2dd999c1ad6dbee0a00c2167984e"></a>

### [`004d70d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d70d4.md) → [`004d7114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7114.md) FUN_004d7114

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 4件 [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d7110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d70d4.md#insn-004d7110)
- 新版 `004d7150`（命令位置の公開資料なし）

~~~diff
- 004d7110 ["INT_ADD", "register:40f0:8", ["const:4d7110:8", "const:4:8"]]
- 004d7110 ["CALL", null, ["callee:00c58090:8"]]
+ 004d7150 ["INT_ADD", "register:40f0:8", ["const:4d7150:8", "const:4:8"]]
+ 004d7150 ["CALL", null, ["callee:00c58090:8"]]
- 004d7110 bytes e0021e94
+ 004d7150 bytes d0031e94
~~~


<a id="compare-6c118a6999979f490fa8048ab8651bf6"></a>

### [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) → [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) FUN_004d7390

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) · 呼出先 11件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d235c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md)
- 新版 呼出元 2件 [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) · 呼出先 11件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d239c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d239c.md) [`004d2b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d73a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md#insn-004d73a8) · [`004d73c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md#insn-004d73c0) · [`004d73d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md#insn-004d73d8)
- 新版 `004d73e8`（命令位置の公開資料なし） · `004d7400`（命令位置の公開資料なし） · `004d7418`（命令位置の公開資料なし）

~~~diff
- 004d73a8 ["INT_ADD", "register:40f0:8", ["const:4d73a8:8", "const:4:8"]]
- 004d73a8 ["CALL", null, ["callee:004b87b4:8"]]
+ 004d73e8 ["INT_ADD", "register:40f0:8", ["const:4d73e8:8", "const:4:8"]]
+ 004d73e8 ["CALL", null, ["callee:004b87b4:8"]]
- 004d73a8 bytes f384ff97
+ 004d73e8 bytes f384ff97
- 004d73c0 ["INT_ADD", "register:40f0:8", ["const:4d73c0:8", "const:4:8"]]
- 004d73c0 ["CALL", null, ["callee:004b87b4:8"]]
+ 004d7400 ["INT_ADD", "register:40f0:8", ["const:4d7400:8", "const:4:8"]]
+ 004d7400 ["CALL", null, ["callee:004b87b4:8"]]
- 004d73c0 bytes ed84ff97
+ 004d7400 bytes ed84ff97
- 004d73d8 ["INT_ADD", "register:40f0:8", ["const:4d73d8:8", "const:4:8"]]
- 004d73d8 ["CALL", null, ["callee:00c58090:8"]]
+ 004d7418 ["INT_ADD", "register:40f0:8", ["const:4d7418:8", "const:4:8"]]
+ 004d7418 ["CALL", null, ["callee:00c58090:8"]]
- 004d73d8 bytes 2e021e94
+ 004d7418 bytes 1e031e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb39e732b97a7e186b6a287a2e1cbfe4"></a>

### [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) → [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) FUN_004d7908

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 11件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d20d8.md) [`004d26d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d26d4.md)
- 新版 呼出元 2件 [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 11件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d2118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2118.md) [`004d2714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2714.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d791c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md#insn-004d791c) · [`004d7934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md#insn-004d7934) · [`004d79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md#insn-004d79a4)
- 新版 `004d795c`（命令位置の公開資料なし） · `004d7974`（命令位置の公開資料なし） · `004d79e4`（命令位置の公開資料なし）

~~~diff
- 004d791c ["INT_ADD", "register:40f0:8", ["const:4d791c:8", "const:4:8"]]
- 004d791c ["CALL", null, ["callee:004b87b4:8"]]
+ 004d795c ["INT_ADD", "register:40f0:8", ["const:4d795c:8", "const:4:8"]]
+ 004d795c ["CALL", null, ["callee:004b87b4:8"]]
- 004d791c bytes 9683ff97
+ 004d795c bytes 9683ff97
- 004d7934 ["INT_ADD", "register:40f0:8", ["const:4d7934:8", "const:4:8"]]
- 004d7934 ["CALL", null, ["callee:00c58090:8"]]
+ 004d7974 ["INT_ADD", "register:40f0:8", ["const:4d7974:8", "const:4:8"]]
+ 004d7974 ["CALL", null, ["callee:00c58090:8"]]
- 004d7934 bytes d7001e94
+ 004d7974 bytes c7011e94
- 004d79a4 ["INT_ADD", "register:40f0:8", ["const:4d79a4:8", "const:4:8"]]
- 004d79a4 ["CALL", null, ["callee:004b894c:8"]]
+ 004d79e4 ["INT_ADD", "register:40f0:8", ["const:4d79e4:8", "const:4:8"]]
+ 004d79e4 ["CALL", null, ["callee:004b894c:8"]]
- 004d79a4 bytes da83ff97
+ 004d79e4 bytes da83ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-844dd7f126933bb04c2b38996f364e55"></a>

### [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) → [`004d7b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7b6c.md) FUN_004d7b6c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 2件 [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d7d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md#insn-004d7d8c)
- 新版 `004d7dcc`（命令位置の公開資料なし）

~~~diff
- 004d7d8c ["INT_ADD", "register:40f0:8", ["const:4d7d8c:8", "const:4:8"]]
- 004d7d8c ["CALL", null, ["callee:00c57f40:8"]]
+ 004d7dcc ["INT_ADD", "register:40f0:8", ["const:4d7dcc:8", "const:4:8"]]
+ 004d7dcc ["CALL", null, ["callee:00c57f40:8"]]
- 004d7d8c bytes 6dff1d94
+ 004d7dcc bytes 5d001e94
~~~


<a id="compare-07de58c2e592b88f210139f25038321c"></a>

### [`004d93d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d93d8.md) → [`004d9418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9418.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c592b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d942c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d93d8.md#insn-004d942c) · [`004d9448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d93d8.md#insn-004d9448) · [`004d9464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d93d8.md#insn-004d9464)
- 新版 `004d946c`（命令位置の公開資料なし） · `004d9488`（命令位置の公開資料なし） · `004d94a4`（命令位置の公開資料なし）

~~~diff
- 004d942c ["INT_ADD", "register:40f0:8", ["const:4d942c:8", "const:4:8"]]
- 004d942c ["CALL", null, ["callee:00c57e90:8"]]
+ 004d946c ["INT_ADD", "register:40f0:8", ["const:4d946c:8", "const:4:8"]]
+ 004d946c ["CALL", null, ["callee:00c57e90:8"]]
- 004d942c bytes 99f91d94
+ 004d946c bytes 89fa1d94
- 004d9448 ["INT_ADD", "register:40f0:8", ["const:4d9448:8", "const:4:8"]]
- 004d9448 ["CALL", null, ["callee:00c58090:8"]]
+ 004d9488 ["INT_ADD", "register:40f0:8", ["const:4d9488:8", "const:4:8"]]
+ 004d9488 ["CALL", null, ["callee:00c58090:8"]]
- 004d9448 bytes 12fa1d94
+ 004d9488 bytes 02fb1d94
- 004d9464 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d9464 ["INT_ADD", "register:40f0:8", ["const:4d9464:8", "const:4:8"]]
- 004d9464 ["CALLIND", null, ["register:0:8"]]
+ 004d94a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004d94a4 ["INT_ADD", "register:40f0:8", ["const:4d94a4:8", "const:4:8"]]
+ 004d94a4 ["CALLIND", null, ["register:0:8"]]
- 004d9464 bytes 00013fd6
+ 004d94a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fbccd8ee71ee6ea2d4714040123dd3d"></a>

### [`004dc648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc648.md) → [`004dc688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dc/004dc688.md) _ZN5Botan29normalized_montgomery_inverseERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md) [`00c58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md) [`00c593a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc648.md#insn-004dc680) · [`004dc6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc648.md#insn-004dc6c8)
- 新版 `004dc6c0`（命令位置の公開資料なし） · `004dc708`（命令位置の公開資料なし）

~~~diff
- 004dc680 ["INT_ADD", "register:40f0:8", ["const:4dc680:8", "const:4:8"]]
- 004dc680 ["CALL", null, ["callee:00c593a0:8"]]
+ 004dc6c0 ["INT_ADD", "register:40f0:8", ["const:4dc6c0:8", "const:4:8"]]
+ 004dc6c0 ["CALL", null, ["callee:00c593a0:8"]]
- 004dc680 bytes 48f21d94
+ 004dc6c0 bytes 38f31d94
- 004dc6c8 ["INT_ADD", "register:40f0:8", ["const:4dc6c8:8", "const:4:8"]]
- 004dc6c8 ["CALL", null, ["callee:00c58ad0:8"]]
+ 004dc708 ["INT_ADD", "register:40f0:8", ["const:4dc708:8", "const:4:8"]]
+ 004dc708 ["CALL", null, ["callee:00c58ad0:8"]]
- 004dc6c8 bytes 02f01d94
+ 004dc708 bytes f2f01d94
~~~


<a id="compare-893bc9dca6b9e659ab13371a2e3db2cd"></a>

### [`004de9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de9dc.md) → [`004dea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004dea1c.md) _ZN5Botan9Power_ModaSERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de9dc.md#insn-004dea04) · [`004dea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de9dc.md#insn-004dea20)
- 新版 `004dea44`（命令位置の公開資料なし） · `004dea60`（命令位置の公開資料なし）

~~~diff
- 004dea04 ["COPY", "register:0:8", ["register:4040:8"]]
- 004dea04 ["INT_ADD", "register:40f0:8", ["const:4dea04:8", "const:4:8"]]
- 004dea04 ["CALLIND", null, ["register:0:8"]]
+ 004dea44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004dea44 ["INT_ADD", "register:40f0:8", ["const:4dea44:8", "const:4:8"]]
+ 004dea44 ["CALLIND", null, ["register:0:8"]]
- 004dea04 bytes 00013fd6
+ 004dea44 bytes 00013fd6
- 004dea20 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dea20 ["INT_ADD", "register:40f0:8", ["const:4dea20:8", "const:4:8"]]
- 004dea20 ["CALLIND", null, ["register:0:8"]]
+ 004dea60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dea60 ["INT_ADD", "register:40f0:8", ["const:4dea60:8", "const:4:8"]]
+ 004dea60 ["CALLIND", null, ["register:0:8"]]
- 004dea20 bytes 20013fd6
+ 004dea60 bytes 20013fd6
~~~


<a id="compare-39afc51d33b61337b03c693b970f41d6"></a>

### [`004deec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004deec4.md) → [`004def04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004def04.md) FUN_004def04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004deef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004deec4.md#insn-004deef0)
- 新版 `004def30`（命令位置の公開資料なし）

~~~diff
- 004deef0 ["INT_ADD", "register:40f0:8", ["const:4deef0:8", "const:4:8"]]
- 004deef0 ["CALL", null, ["callee:005436dc:8"]]
+ 004def30 ["INT_ADD", "register:40f0:8", ["const:4def30:8", "const:4:8"]]
+ 004def30 ["CALL", null, ["callee:005436dc:8"]]
- 004deef0 bytes eb910194
+ 004def30 bytes eb910194
~~~


<a id="compare-d6cbb299e8c3fa1f719fa2abfd40650e"></a>

### [`004df5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df5e0.md) → [`004df620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df620.md) FUN_004df620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df5e0.md#insn-004df60c)
- 新版 `004df64c`（命令位置の公開資料なし）

~~~diff
- 004df60c ["INT_ADD", "register:40f0:8", ["const:4df60c:8", "const:4:8"]]
- 004df60c ["CALL", null, ["callee:005436dc:8"]]
+ 004df64c ["INT_ADD", "register:40f0:8", ["const:4df64c:8", "const:4:8"]]
+ 004df64c ["CALL", null, ["callee:005436dc:8"]]
- 004df60c bytes 24900194
+ 004df64c bytes 24900194
~~~


<a id="compare-d6569e26699a3195cbaaed612cc4dc12"></a>

### [`004e23b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md) → [`004e23f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e23f8.md) _ZN5Botan13pbes2_encryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e23ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md#insn-004e23ec) · [`004e2410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md#insn-004e2410)
- 新版 `004e242c`（命令位置の公開資料なし） · `004e2450`（命令位置の公開資料なし）

~~~diff
- 004e23ec ["INT_ADD", "register:40f0:8", ["const:4e23ec:8", "const:4:8"]]
- 004e23ec ["CALL", null, ["callee:004e2454:8"]]
+ 004e242c ["INT_ADD", "register:40f0:8", ["const:4e242c:8", "const:4:8"]]
+ 004e242c ["CALL", null, ["callee:004e2454:8"]]
- 004e23ec bytes 0a000094
+ 004e242c bytes 0a000094
- 004e2410 ["INT_ADD", "register:40f0:8", ["const:4e2410:8", "const:4:8"]]
- 004e2410 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004e2450 ["INT_ADD", "register:40f0:8", ["const:4e2450:8", "const:4:8"]]
+ 004e2450 ["CALL", null, ["callee:00c57ee0:8"]]
- 004e2410 bytes b4d51d94
+ 004e2450 bytes a4d61d94
~~~


<a id="compare-35315eb538251bfad0f3662c6ae10ee1"></a>

### [`004e33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md) → [`004e33f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e33f8.md) _ZN5Botan18pbes2_encrypt_msecERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e33e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md#insn-004e33e4) · [`004e3414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md#insn-004e3414)
- 新版 `004e3424`（命令位置の公開資料なし） · `004e3454`（命令位置の公開資料なし）

~~~diff
- 004e33e4 ["INT_ADD", "register:40f0:8", ["const:4e33e4:8", "const:4:8"]]
- 004e33e4 ["CALL", null, ["callee:004e2454:8"]]
+ 004e3424 ["INT_ADD", "register:40f0:8", ["const:4e3424:8", "const:4:8"]]
+ 004e3424 ["CALL", null, ["callee:004e2454:8"]]
- 004e33e4 bytes 0cfcff97
+ 004e3424 bytes 0cfcff97
- 004e3414 ["INT_ADD", "register:40f0:8", ["const:4e3414:8", "const:4:8"]]
- 004e3414 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004e3454 ["INT_ADD", "register:40f0:8", ["const:4e3454:8", "const:4:8"]]
+ 004e3454 ["CALL", null, ["callee:00c57ee0:8"]]
- 004e3414 bytes b3d11d94
+ 004e3454 bytes a3d21d94
~~~


<a id="compare-5c9bfd1106b1cbec5f8a5d2d0a20623f"></a>

### [`004e3418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3418.md) → [`004e3458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e3458.md) FUN_004e3458

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e3434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3418.md#insn-004e3434) · [`004e3444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3418.md#insn-004e3444)
- 新版 `004e3474`（命令位置の公開資料なし） · `004e3484`（命令位置の公開資料なし）

~~~diff
- 004e3434 ["INT_ADD", "register:40f0:8", ["const:4e3434:8", "const:4:8"]]
- 004e3434 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e3474 ["INT_ADD", "register:40f0:8", ["const:4e3474:8", "const:4:8"]]
+ 004e3474 ["CALL", null, ["callee:00c57eb0:8"]]
- 004e3434 bytes 9fd11d94
+ 004e3474 bytes 8fd21d94
- 004e3444 ["INT_ADD", "register:40f0:8", ["const:4e3444:8", "const:4:8"]]
- 004e3444 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e3484 ["INT_ADD", "register:40f0:8", ["const:4e3484:8", "const:4:8"]]
+ 004e3484 ["CALL", null, ["callee:00c57eb0:8"]]
- 004e3444 bytes 9bd11d94
+ 004e3484 bytes 8bd21d94
~~~


<a id="compare-8c990e0781931f15b992fbb370794424"></a>

### [`004e4614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4614.md) → [`004e4654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4654.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c59030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c59430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e464c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4614.md#insn-004e464c) · [`004e466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4614.md#insn-004e466c)
- 新版 `004e468c`（命令位置の公開資料なし） · `004e46ac`（命令位置の公開資料なし）

~~~diff
- 004e464c ["INT_ADD", "register:40f0:8", ["const:4e464c:8", "const:4:8"]]
- 004e464c ["CALL", null, ["callee:004b3508:8"]]
+ 004e468c ["INT_ADD", "register:40f0:8", ["const:4e468c:8", "const:4:8"]]
+ 004e468c ["CALL", null, ["callee:004b3508:8"]]
- 004e464c bytes 9f3bff97
+ 004e468c bytes 9f3bff97
- 004e466c ["INT_ADD", "register:40f0:8", ["const:4e466c:8", "const:4:8"]]
- 004e466c ["CALL", null, ["callee:00c59430:8"]]
+ 004e46ac ["INT_ADD", "register:40f0:8", ["const:4e46ac:8", "const:4:8"]]
+ 004e46ac ["CALL", null, ["callee:00c59430:8"]]
- 004e466c bytes 71d21d94
+ 004e46ac bytes 61d31d94
~~~


<a id="compare-3f5d368ce372c5511e0dc4012d835860"></a>

### [`004e4bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md) → [`004e4bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md) _ZN5Botan5PBKDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004e4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004e4d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md#insn-004e4c1c) · [`004e4c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md#insn-004e4c2c) · [`004e4c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md#insn-004e4c68)
- 新版 `004e4c5c`（命令位置の公開資料なし） · `004e4c6c`（命令位置の公開資料なし） · `004e4ca8`（命令位置の公開資料なし）

~~~diff
- 004e4c1c ["INT_ADD", "register:40f0:8", ["const:4e4c1c:8", "const:4:8"]]
- 004e4c1c ["CALL", null, ["callee:00473540:8"]]
+ 004e4c5c ["INT_ADD", "register:40f0:8", ["const:4e4c5c:8", "const:4:8"]]
+ 004e4c5c ["CALL", null, ["callee:00473540:8"]]
- 004e4c1c bytes 393afe97
+ 004e4c5c bytes 393afe97
- 004e4c2c ["INT_ADD", "register:40f0:8", ["const:4e4c2c:8", "const:4:8"]]
- 004e4c2c ["CALL", null, ["callee:004e4d50:8"]]
+ 004e4c6c ["INT_ADD", "register:40f0:8", ["const:4e4c6c:8", "const:4:8"]]
+ 004e4c6c ["CALL", null, ["callee:004e4d50:8"]]
- 004e4c2c bytes 39000094
+ 004e4c6c bytes 39000094
- 004e4c68 ["INT_ADD", "register:40f0:8", ["const:4e4c68:8", "const:4:8"]]
- 004e4c68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e4ca8 ["INT_ADD", "register:40f0:8", ["const:4e4ca8:8", "const:4:8"]]
+ 004e4ca8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004e4c68 bytes 92cb1d94
+ 004e4ca8 bytes 82cc1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed0e44e7f474e9a28ab52e53868b8ae"></a>

### [`004e4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md) → [`004e4d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4d50.md) FUN_004e4d50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e4bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59020.md)
- 新版 呼出元 1件 [`004e4bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4bec.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md#insn-004e4d60) · [`004e4d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md#insn-004e4d74) · [`004e4d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md#insn-004e4d90)
- 新版 `004e4da0`（命令位置の公開資料なし） · `004e4db4`（命令位置の公開資料なし） · `004e4dd0`（命令位置の公開資料なし）

~~~diff
- 004e4d60 ["INT_ADD", "register:40f0:8", ["const:4e4d60:8", "const:4:8"]]
- 004e4d60 ["CALL", null, ["callee:00540d7c:8"]]
+ 004e4da0 ["INT_ADD", "register:40f0:8", ["const:4e4da0:8", "const:4:8"]]
+ 004e4da0 ["CALL", null, ["callee:00540d7c:8"]]
- 004e4d60 bytes f76f0194
+ 004e4da0 bytes f76f0194
- 004e4d74 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e4d74 ["INT_ADD", "register:40f0:8", ["const:4e4d74:8", "const:4:8"]]
- 004e4d74 ["CALLIND", null, ["register:0:8"]]
+ 004e4db4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4db4 ["INT_ADD", "register:40f0:8", ["const:4e4db4:8", "const:4:8"]]
+ 004e4db4 ["CALLIND", null, ["register:0:8"]]
- 004e4d74 bytes 00013fd6
+ 004e4db4 bytes 00013fd6
- 004e4d90 ["INT_ADD", "register:40f0:8", ["const:4e4d90:8", "const:4:8"]]
- 004e4d90 ["CALL", null, ["callee:00c59420:8"]]
+ 004e4dd0 ["INT_ADD", "register:40f0:8", ["const:4e4dd0:8", "const:4:8"]]
+ 004e4dd0 ["CALL", null, ["callee:00c59420:8"]]
- 004e4d90 bytes a4d01d94
+ 004e4dd0 bytes 94d11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf52c940a33410365a34cefd7e7e4c7"></a>

### [`004e4e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e50.md) → [`004e4e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4e90.md) _ZNK5Botan5PBKDF11pbkdf_timedEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmNS2_6chrono8durationIxNS2_5ratioIL

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e50.md#insn-004e4e70)
- 新版 `004e4eb0`（命令位置の公開資料なし）

~~~diff
- 004e4e70 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e4e70 ["INT_ADD", "register:40f0:8", ["const:4e4e70:8", "const:4:8"]]
- 004e4e70 ["CALLIND", null, ["register:0:8"]]
+ 004e4eb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4eb0 ["INT_ADD", "register:40f0:8", ["const:4e4eb0:8", "const:4:8"]]
+ 004e4eb0 ["CALLIND", null, ["register:0:8"]]
- 004e4e70 bytes 00013fd6
+ 004e4eb0 bytes 00013fd6
~~~


<a id="compare-69e3bd7dc7d8f02bef783a5c00a57991"></a>

### [`004e5028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5028.md) → [`004e5068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5068.md) _ZNK5Botan5PBKDF11pbkdf_timedEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmNS1_6chrono8durationIxNS1_5ratioILl1

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e5064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5028.md#insn-004e5064) · [`004e5090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5028.md#insn-004e5090)
- 新版 `004e50a4`（命令位置の公開資料なし） · `004e50d0`（命令位置の公開資料なし）

~~~diff
- 004e5064 ["INT_ADD", "register:40f0:8", ["const:4e5064:8", "const:4:8"]]
- 004e5064 ["CALL", null, ["callee:004b3508:8"]]
+ 004e50a4 ["INT_ADD", "register:40f0:8", ["const:4e50a4:8", "const:4:8"]]
+ 004e50a4 ["CALL", null, ["callee:004b3508:8"]]
- 004e5064 bytes 1939ff97
+ 004e50a4 bytes 1939ff97
- 004e5090 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e5090 ["INT_ADD", "register:40f0:8", ["const:4e5090:8", "const:4:8"]]
- 004e5090 ["CALLIND", null, ["register:0:8"]]
+ 004e50d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e50d0 ["INT_ADD", "register:40f0:8", ["const:4e50d0:8", "const:4:8"]]
+ 004e50d0 ["CALLIND", null, ["register:0:8"]]
- 004e5090 bytes 00013fd6
+ 004e50d0 bytes 00013fd6
~~~


<a id="compare-d52922e970c54b8e13a953c5f4847780"></a>

### [`004e7274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7274.md) → [`004e72b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e72b4.md) _ZN5Botan13hash_for_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59140.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)
- 新版 呼出元 1件 [`00c59540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59540.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e72bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7274.md#insn-004e72bc) · [`004e72c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7274.md#insn-004e72c8) · [`004e72d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7274.md#insn-004e72d8)
- 新版 `004e72fc`（命令位置の公開資料なし） · `004e7308`（命令位置の公開資料なし） · `004e7318`（命令位置の公開資料なし）

~~~diff
- 004e72bc ["INT_ADD", "register:40f0:8", ["const:4e72bc:8", "const:4:8"]]
- 004e72bc ["CALL", null, ["callee:0043bb20:8"]]
+ 004e72fc ["INT_ADD", "register:40f0:8", ["const:4e72fc:8", "const:4:8"]]
+ 004e72fc ["CALL", null, ["callee:0043bb20:8"]]
- 004e72bc bytes 0952fd97
+ 004e72fc bytes 0952fd97
- 004e72c8 ["INT_ADD", "register:40f0:8", ["const:4e72c8:8", "const:4:8"]]
- 004e72c8 ["CALL", null, ["callee:00c58d40:8"]]
+ 004e7308 ["INT_ADD", "register:40f0:8", ["const:4e7308:8", "const:4:8"]]
+ 004e7308 ["CALL", null, ["callee:00c58d40:8"]]
- 004e72c8 bytes 9ec51d94
+ 004e7308 bytes 8ec61d94
- 004e72d8 ["INT_ADD", "register:40f0:8", ["const:4e72d8:8", "const:4:8"]]
- 004e72d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e7318 ["INT_ADD", "register:40f0:8", ["const:4e7318:8", "const:4:8"]]
+ 004e7318 ["CALL", null, ["callee:00c57eb0:8"]]
- 004e72d8 bytes f6c11d94
+ 004e7318 bytes e6c21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745b2a4dc07f7f0cb4b8d24bfed26a7d"></a>

### [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) → [`004e7494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md) FUN_004e7494

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) [`00545434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0054f430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005451d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md) [`00545474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e74a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md#insn-004e74a4) · [`004e74d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md#insn-004e74d4) · [`004e74f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md#insn-004e74f0)
- 新版 `004e74e4`（命令位置の公開資料なし） · `004e7514`（命令位置の公開資料なし） · `004e7530`（命令位置の公開資料なし）

~~~diff
- 004e74a4 ["INT_ADD", "register:40f0:8", ["const:4e74a4:8", "const:4:8"]]
- 004e74a4 ["CALL", null, ["callee:0043bba4:8"]]
+ 004e74e4 ["INT_ADD", "register:40f0:8", ["const:4e74e4:8", "const:4:8"]]
+ 004e74e4 ["CALL", null, ["callee:0043bba4:8"]]
- 004e74a4 bytes b051fd97
+ 004e74e4 bytes b051fd97
- 004e74d4 ["INT_ADD", "register:40f0:8", ["const:4e74d4:8", "const:4:8"]]
- 004e74d4 ["CALL", null, ["callee:005451d8:8"]]
+ 004e7514 ["INT_ADD", "register:40f0:8", ["const:4e7514:8", "const:4:8"]]
+ 004e7514 ["CALL", null, ["callee:005451d8:8"]]
- 004e74d4 bytes 31770194
+ 004e7514 bytes 31770194
- 004e74f0 ["INT_ADD", "register:40f0:8", ["const:4e74f0:8", "const:4:8"]]
- 004e74f0 ["CALL", null, ["callee:00545474:8"]]
+ 004e7530 ["INT_ADD", "register:40f0:8", ["const:4e7530:8", "const:4:8"]]
+ 004e7530 ["CALL", null, ["callee:00545474:8"]]
- 004e74f0 bytes d1770194
+ 004e7530 bytes d1770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89bc07ea1d35451c7266e9b55f3da956"></a>

### [`004e7570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7570.md) → [`004e75b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e75b0.md) FUN_004e75b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e75bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7570.md#insn-004e75bc) · [`004e75cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7570.md#insn-004e75cc)
- 新版 `004e75fc`（命令位置の公開資料なし） · `004e760c`（命令位置の公開資料なし）

~~~diff
- 004e75bc ["INT_ADD", "register:40f0:8", ["const:4e75bc:8", "const:4:8"]]
- 004e75bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e75fc ["INT_ADD", "register:40f0:8", ["const:4e75fc:8", "const:4:8"]]
+ 004e75fc ["CALL", null, ["callee:00c57eb0:8"]]
- 004e75bc bytes 3dc11d94
+ 004e75fc bytes 2dc21d94
- 004e75cc ["INT_ADD", "register:40f0:8", ["const:4e75cc:8", "const:4:8"]]
- 004e75cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e760c ["INT_ADD", "register:40f0:8", ["const:4e760c:8", "const:4:8"]]
+ 004e760c ["CALL", null, ["callee:00c57eb0:8"]]
- 004e75cc bytes 39c11d94
+ 004e760c bytes 29c21d94
~~~


<a id="compare-695f084c65d551d8162b9693ef78ec11"></a>

### [`004e8ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md) → [`004e8d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8d28.md) _ZN5Botan18create_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS_21RandomNumberGeneratorES8_S8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md) [`00c591b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c587f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md) [`00c595b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md#insn-004e8d78) · [`004e8d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md#insn-004e8d8c) · [`004e8da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md#insn-004e8da0)
- 新版 `004e8db8`（命令位置の公開資料なし） · `004e8dcc`（命令位置の公開資料なし） · `004e8de0`（命令位置の公開資料なし）

~~~diff
- 004e8d78 ["INT_ADD", "register:40f0:8", ["const:4e8d78:8", "const:4:8"]]
- 004e8d78 ["CALL", null, ["callee:00c587f0:8"]]
+ 004e8db8 ["INT_ADD", "register:40f0:8", ["const:4e8db8:8", "const:4:8"]]
+ 004e8db8 ["CALL", null, ["callee:00c587f0:8"]]
- 004e8d78 bytes 9ebd1d94
+ 004e8db8 bytes 8ebe1d94
- 004e8d8c ["INT_ADD", "register:40f0:8", ["const:4e8d8c:8", "const:4:8"]]
- 004e8d8c ["CALL", null, ["callee:00c57e90:8"]]
+ 004e8dcc ["INT_ADD", "register:40f0:8", ["const:4e8dcc:8", "const:4:8"]]
+ 004e8dcc ["CALL", null, ["callee:00c57e90:8"]]
- 004e8d8c bytes 41bb1d94
+ 004e8dcc bytes 31bc1d94
- 004e8da0 ["INT_ADD", "register:40f0:8", ["const:4e8da0:8", "const:4:8"]]
- 004e8da0 ["CALL", null, ["callee:00c595b0:8"]]
+ 004e8de0 ["INT_ADD", "register:40f0:8", ["const:4e8de0:8", "const:4:8"]]
+ 004e8de0 ["CALL", null, ["callee:00c595b0:8"]]
- 004e8da0 bytes 04c11d94
+ 004e8de0 bytes f4c11d94
~~~


<a id="compare-aa1e9ac9490ba6ee04aecbb55fb9ac65"></a>

### [`004e99e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e99e8.md) → [`004e9a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e9/004e9a28.md) _ZN5Botan26probe_provider_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_6vectorIS6_NS4_IS6_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e99e8.md#insn-004e9a8c) · [`004e9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e99e8.md#insn-004e9aa0)
- 新版 `004e9acc`（命令位置の公開資料なし） · `004e9ae0`（命令位置の公開資料なし）

~~~diff
- 004e9a8c ["INT_ADD", "register:40f0:8", ["const:4e9a8c:8", "const:4:8"]]
- 004e9a8c ["CALL", null, ["callee:0043bb20:8"]]
+ 004e9acc ["INT_ADD", "register:40f0:8", ["const:4e9acc:8", "const:4:8"]]
+ 004e9acc ["CALL", null, ["callee:0043bb20:8"]]
- 004e9a8c bytes 1548fd97
+ 004e9acc bytes 1548fd97
- 004e9aa0 ["INT_ADD", "register:40f0:8", ["const:4e9aa0:8", "const:4:8"]]
- 004e9aa0 ["CALL", null, ["callee:00540d7c:8"]]
+ 004e9ae0 ["INT_ADD", "register:40f0:8", ["const:4e9ae0:8", "const:4:8"]]
+ 004e9ae0 ["CALL", null, ["callee:00540d7c:8"]]
- 004e9aa0 bytes a75c0194
+ 004e9ae0 bytes a75c0194
~~~


<a id="compare-05cbd3c6c405de724d6a3d6adfd2e2e8"></a>

### [`004e9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e9fd0.md) → [`004ea010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea010.md) _ZNK5Botan10Public_Key7get_oidEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ea004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e9fd0.md#insn-004ea004) · [`004ea010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e9fd0.md#insn-004ea010) · [`004ea020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e9fd0.md#insn-004ea020)
- 新版 `004ea044`（命令位置の公開資料なし） · `004ea050`（命令位置の公開資料なし） · `004ea060`（命令位置の公開資料なし）

~~~diff
- 004ea004 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea004 ["INT_ADD", "register:40f0:8", ["const:4ea004:8", "const:4:8"]]
- 004ea004 ["CALLIND", null, ["register:0:8"]]
+ 004ea044 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea044 ["INT_ADD", "register:40f0:8", ["const:4ea044:8", "const:4:8"]]
+ 004ea044 ["CALLIND", null, ["register:0:8"]]
- 004ea004 bytes 20013fd6
+ 004ea044 bytes 20013fd6
- 004ea010 ["INT_ADD", "register:40f0:8", ["const:4ea010:8", "const:4:8"]]
- 004ea010 ["CALL", null, ["callee:00c58680:8"]]
+ 004ea050 ["INT_ADD", "register:40f0:8", ["const:4ea050:8", "const:4:8"]]
+ 004ea050 ["CALL", null, ["callee:00c58680:8"]]
- 004ea010 bytes 9cb81d94
+ 004ea050 bytes 8cb91d94
- 004ea020 ["INT_ADD", "register:40f0:8", ["const:4ea020:8", "const:4:8"]]
- 004ea020 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ea060 ["INT_ADD", "register:40f0:8", ["const:4ea060:8", "const:4:8"]]
+ 004ea060 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ea020 bytes a4b61d94
+ 004ea060 bytes 94b71d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d7b522a649c4bed1ee5a14965637951"></a>

### [`004ea4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea4b0.md) → [`004ea4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea4f0.md) _ZNK5Botan10Public_Key18fingerprint_publicERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c591c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591c0.md) [`00c591d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c595c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595c0.md) [`00c595d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ea4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea4b0.md#insn-004ea4dc) · [`004ea4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea4b0.md#insn-004ea4f0) · [`004ea500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea4b0.md#insn-004ea500)
- 新版 `004ea51c`（命令位置の公開資料なし） · `004ea530`（命令位置の公開資料なし） · `004ea540`（命令位置の公開資料なし）

~~~diff
- 004ea4dc ["INT_ADD", "register:40f0:8", ["const:4ea4dc:8", "const:4:8"]]
- 004ea4dc ["CALL", null, ["callee:00c595d0:8"]]
+ 004ea51c ["INT_ADD", "register:40f0:8", ["const:4ea51c:8", "const:4:8"]]
+ 004ea51c ["CALL", null, ["callee:00c595d0:8"]]
- 004ea4dc bytes 3dbb1d94
+ 004ea51c bytes 2dbc1d94
- 004ea4f0 ["INT_ADD", "register:40f0:8", ["const:4ea4f0:8", "const:4:8"]]
- 004ea4f0 ["CALL", null, ["callee:00c595c0:8"]]
+ 004ea530 ["INT_ADD", "register:40f0:8", ["const:4ea530:8", "const:4:8"]]
+ 004ea530 ["CALL", null, ["callee:00c595c0:8"]]
- 004ea4f0 bytes 34bb1d94
+ 004ea530 bytes 24bc1d94
- 004ea500 ["INT_ADD", "register:40f0:8", ["const:4ea500:8", "const:4:8"]]
- 004ea500 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ea540 ["INT_ADD", "register:40f0:8", ["const:4ea540:8", "const:4:8"]]
+ 004ea540 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ea500 bytes 6cb51d94
+ 004ea540 bytes 5cb61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49049540171fe27ef1dff85e68f462f5"></a>

### [`004ec218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec218.md) → [`004ec258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec258.md) FUN_004ec258

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec218.md#insn-004ec234)
- 新版 `004ec274`（命令位置の公開資料なし）

~~~diff
- 004ec234 ["INT_ADD", "register:40f0:8", ["const:4ec234:8", "const:4:8"]]
- 004ec234 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ec274 ["INT_ADD", "register:40f0:8", ["const:4ec274:8", "const:4:8"]]
+ 004ec274 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ec234 bytes 1fae1d94
+ 004ec274 bytes 0faf1d94
~~~


<a id="compare-a6355401adf546928a7b3bc0d47babb6"></a>

### [`004ecba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md) → [`004ecbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceENSt6__ndk18functionIFNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEvEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ecbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md#insn-004ecbe8) · [`004ecc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md#insn-004ecc14) · [`004ecc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md#insn-004ecc2c)
- 新版 `004ecc28`（命令位置の公開資料なし） · `004ecc54`（命令位置の公開資料なし） · `004ecc6c`（命令位置の公開資料なし）

~~~diff
- 004ecbe8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ecbe8 ["INT_ADD", "register:40f0:8", ["const:4ecbe8:8", "const:4:8"]]
- 004ecbe8 ["CALLIND", null, ["register:0:8"]]
+ 004ecc28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecc28 ["INT_ADD", "register:40f0:8", ["const:4ecc28:8", "const:4:8"]]
+ 004ecc28 ["CALLIND", null, ["register:0:8"]]
- 004ecbe8 bytes 00013fd6
+ 004ecc28 bytes 00013fd6
- 004ecc14 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ecc14 ["INT_ADD", "register:40f0:8", ["const:4ecc14:8", "const:4:8"]]
- 004ecc14 ["CALLIND", null, ["register:0:8"]]
+ 004ecc54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecc54 ["INT_ADD", "register:40f0:8", ["const:4ecc54:8", "const:4:8"]]
+ 004ecc54 ["CALLIND", null, ["register:0:8"]]
- 004ecc14 bytes 00013fd6
+ 004ecc54 bytes 00013fd6
- 004ecc2c ["INT_ADD", "register:40f0:8", ["const:4ecc2c:8", "const:4:8"]]
- 004ecc2c ["CALL", null, ["callee:004ecd10:8"]]
+ 004ecc6c ["INT_ADD", "register:40f0:8", ["const:4ecc6c:8", "const:4:8"]]
+ 004ecc6c ["CALL", null, ["callee:004ecd10:8"]]
- 004ecc2c bytes 29000094
+ 004ecc6c bytes 29000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b617b36540e3d456ac84982f375f69"></a>

### [`004edfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md) → [`004ee018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorENSt6__ndk18functionIFNS5_12basic_stringIcNS5_11char_traitsIcEENS5_9all

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md#insn-004ee014) · [`004ee034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md#insn-004ee034) · [`004ee064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md#insn-004ee064)
- 新版 `004ee054`（命令位置の公開資料なし） · `004ee074`（命令位置の公開資料なし） · `004ee0a4`（命令位置の公開資料なし）

~~~diff
- 004ee014 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ee014 ["INT_ADD", "register:40f0:8", ["const:4ee014:8", "const:4:8"]]
- 004ee014 ["CALLIND", null, ["register:0:8"]]
+ 004ee054 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ee054 ["INT_ADD", "register:40f0:8", ["const:4ee054:8", "const:4:8"]]
+ 004ee054 ["CALLIND", null, ["register:0:8"]]
- 004ee014 bytes 20013fd6
+ 004ee054 bytes 20013fd6
- 004ee034 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee034 ["INT_ADD", "register:40f0:8", ["const:4ee034:8", "const:4:8"]]
- 004ee034 ["CALLIND", null, ["register:0:8"]]
+ 004ee074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee074 ["INT_ADD", "register:40f0:8", ["const:4ee074:8", "const:4:8"]]
+ 004ee074 ["CALLIND", null, ["register:0:8"]]
- 004ee034 bytes 00013fd6
+ 004ee074 bytes 00013fd6
- 004ee064 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee064 ["INT_ADD", "register:40f0:8", ["const:4ee064:8", "const:4:8"]]
- 004ee064 ["CALLIND", null, ["register:0:8"]]
+ 004ee0a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee0a4 ["INT_ADD", "register:40f0:8", ["const:4ee0a4:8", "const:4:8"]]
+ 004ee0a4 ["CALLIND", null, ["register:0:8"]]
- 004ee064 bytes 00013fd6
+ 004ee0a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c81d2b3d66c6691d523b6e026f09e072"></a>

### [`004ee1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee1c4.md) → [`004ee204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee204.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59230.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee1c4.md#insn-004ee1e8) · [`004ee210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee1c4.md#insn-004ee210)
- 新版 `004ee228`（命令位置の公開資料なし） · `004ee250`（命令位置の公開資料なし）

~~~diff
- 004ee1e8 ["INT_ADD", "register:40f0:8", ["const:4ee1e8:8", "const:4:8"]]
- 004ee1e8 ["CALL", null, ["callee:00c59630:8"]]
+ 004ee228 ["INT_ADD", "register:40f0:8", ["const:4ee228:8", "const:4:8"]]
+ 004ee228 ["CALL", null, ["callee:00c59630:8"]]
- 004ee1e8 bytes 12ac1d94
+ 004ee228 bytes 02ad1d94
- 004ee210 ["INT_ADD", "register:40f0:8", ["const:4ee210:8", "const:4:8"]]
- 004ee210 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004ee250 ["INT_ADD", "register:40f0:8", ["const:4ee250:8", "const:4:8"]]
+ 004ee250 ["CALL", null, ["callee:00c57ee0:8"]]
- 004ee210 bytes 34a61d94
+ 004ee250 bytes 24a71d94
~~~


<a id="compare-572fb1331c64e21112e1f97a42b685ef"></a>

### [`004ee2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md) → [`004ee334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee334.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorENS1_8functionIFS7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md#insn-004ee320) · [`004ee33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md#insn-004ee33c) · [`004ee36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md#insn-004ee36c)
- 新版 `004ee360`（命令位置の公開資料なし） · `004ee37c`（命令位置の公開資料なし） · `004ee3ac`（命令位置の公開資料なし）

~~~diff
- 004ee320 ["INT_ADD", "register:40f0:8", ["const:4ee320:8", "const:4:8"]]
- 004ee320 ["CALL", null, ["callee:00c59660:8"]]
+ 004ee360 ["INT_ADD", "register:40f0:8", ["const:4ee360:8", "const:4:8"]]
+ 004ee360 ["CALL", null, ["callee:00c59660:8"]]
- 004ee320 bytes d0ab1d94
+ 004ee360 bytes c0ac1d94
- 004ee33c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee33c ["INT_ADD", "register:40f0:8", ["const:4ee33c:8", "const:4:8"]]
- 004ee33c ["CALLIND", null, ["register:0:8"]]
+ 004ee37c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee37c ["INT_ADD", "register:40f0:8", ["const:4ee37c:8", "const:4:8"]]
+ 004ee37c ["CALLIND", null, ["register:0:8"]]
- 004ee33c bytes 00013fd6
+ 004ee37c bytes 00013fd6
- 004ee36c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee36c ["INT_ADD", "register:40f0:8", ["const:4ee36c:8", "const:4:8"]]
- 004ee36c ["CALLIND", null, ["register:0:8"]]
+ 004ee3ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee3ac ["INT_ADD", "register:40f0:8", ["const:4ee3ac:8", "const:4:8"]]
+ 004ee3ac ["CALLIND", null, ["register:0:8"]]
- 004ee36c bytes 00013fd6
+ 004ee3ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af480b417b3711efa754a95d315aad08"></a>

### [`004ee808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee808.md) → [`004ee848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee848.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee808.md#insn-004ee828) · [`004ee850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee808.md#insn-004ee850)
- 新版 `004ee868`（命令位置の公開資料なし） · `004ee890`（命令位置の公開資料なし）

~~~diff
- 004ee828 ["INT_ADD", "register:40f0:8", ["const:4ee828:8", "const:4:8"]]
- 004ee828 ["CALL", null, ["callee:00c59650:8"]]
+ 004ee868 ["INT_ADD", "register:40f0:8", ["const:4ee868:8", "const:4:8"]]
+ 004ee868 ["CALL", null, ["callee:00c59650:8"]]
- 004ee828 bytes 8aaa1d94
+ 004ee868 bytes 7aab1d94
- 004ee850 ["INT_ADD", "register:40f0:8", ["const:4ee850:8", "const:4:8"]]
- 004ee850 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004ee890 ["INT_ADD", "register:40f0:8", ["const:4ee890:8", "const:4:8"]]
+ 004ee890 ["CALL", null, ["callee:00c57ee0:8"]]
- 004ee850 bytes a4a41d94
+ 004ee890 bytes 94a51d94
~~~


<a id="compare-6cc997efd65eee081d28ce85438489ec"></a>

### [`004eeefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeefc.md) → [`004eef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eef3c.md) _ZN5Botan16PK_Encryptor_EMED0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eef0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeefc.md#insn-004eef0c)
- 新版 `004eef4c`（命令位置の公開資料なし）

~~~diff
- 004eef0c ["INT_ADD", "register:40f0:8", ["const:4eef0c:8", "const:4:8"]]
- 004eef0c ["CALL", null, ["callee:00c59210:8"]]
+ 004eef4c ["INT_ADD", "register:40f0:8", ["const:4eef4c:8", "const:4:8"]]
+ 004eef4c ["CALL", null, ["callee:00c59210:8"]]
- 004eef0c bytes c1a71d94
+ 004eef4c bytes b1a81d94
~~~


<a id="compare-a73445e9f82f826e1667c35c314c7797"></a>

### [`004ef2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2c0.md) → [`004ef300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef300.md) _ZN5Botan16PK_Decryptor_EMED0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2c0.md#insn-004ef2d0)
- 新版 `004ef310`（命令位置の公開資料なし）

~~~diff
- 004ef2d0 ["INT_ADD", "register:40f0:8", ["const:4ef2d0:8", "const:4:8"]]
- 004ef2d0 ["CALL", null, ["callee:00c59200:8"]]
+ 004ef310 ["INT_ADD", "register:40f0:8", ["const:4ef310:8", "const:4:8"]]
+ 004ef310 ["CALL", null, ["callee:00c59200:8"]]
- 004ef2d0 bytes cca61d94
+ 004ef310 bytes bca71d94
~~~


<a id="compare-ec37115a5521fd42945d593caf61f330"></a>

### [`004efa14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efa14.md) → [`004efa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efa54.md) _ZN5Botan16PK_Key_AgreementaSEOS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004efa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efa14.md#insn-004efa4c)
- 新版 `004efa8c`（命令位置の公開資料なし）

~~~diff
- 004efa4c ["COPY", "register:0:8", ["register:4048:8"]]
- 004efa4c ["INT_ADD", "register:40f0:8", ["const:4efa4c:8", "const:4:8"]]
- 004efa4c ["CALLIND", null, ["register:0:8"]]
+ 004efa8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004efa8c ["INT_ADD", "register:40f0:8", ["const:4efa8c:8", "const:4:8"]]
+ 004efa8c ["CALLIND", null, ["register:0:8"]]
- 004efa4c bytes 20013fd6
+ 004efa8c bytes 20013fd6
~~~


<a id="compare-f7bd8e337f6aac9df35aa9f4e221c4b9"></a>

### [`004f06ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f06ac.md) → [`004f06ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f06ec.md) _ZN5Botan11PK_Verifier14verify_messageEPKhmS2_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c592a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592a0.md) · 呼出先 1件 [`00c58e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e60.md)
- 新版 呼出元 1件 [`00c596a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596a0.md) · 呼出先 1件 [`00c59260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f06d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f06ac.md#insn-004f06d4)
- 新版 `004f0714`（命令位置の公開資料なし）

~~~diff
- 004f06d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f06d4 ["INT_ADD", "register:40f0:8", ["const:4f06d4:8", "const:4:8"]]
- 004f06d4 ["CALLIND", null, ["register:0:8"]]
+ 004f0714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f0714 ["INT_ADD", "register:40f0:8", ["const:4f0714:8", "const:4:8"]]
+ 004f0714 ["CALLIND", null, ["register:0:8"]]
- 004f06d4 bytes 00013fd6
+ 004f0714 bytes 00013fd6
~~~


<a id="compare-f8e5da57f28c1fedca78e866b81f074a"></a>

### [`004f0b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md) → [`004f0b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md) FUN_004f0b80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f0704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`004f0744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f0bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md#insn-004f0bb8) · [`004f0bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md#insn-004f0bd4) · [`004f0be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md#insn-004f0be4)
- 新版 `004f0bf8`（命令位置の公開資料なし） · `004f0c14`（命令位置の公開資料なし） · `004f0c24`（命令位置の公開資料なし）

~~~diff
- 004f0bb8 ["INT_ADD", "register:40f0:8", ["const:4f0bb8:8", "const:4:8"]]
- 004f0bb8 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f0bf8 ["INT_ADD", "register:40f0:8", ["const:4f0bf8:8", "const:4:8"]]
+ 004f0bf8 ["CALL", null, ["callee:00c57e90:8"]]
- 004f0bb8 bytes b69b1d94
+ 004f0bf8 bytes a69c1d94
- 004f0bd4 ["INT_ADD", "register:40f0:8", ["const:4f0bd4:8", "const:4:8"]]
- 004f0bd4 ["CALL", null, ["callee:00c58090:8"]]
+ 004f0c14 ["INT_ADD", "register:40f0:8", ["const:4f0c14:8", "const:4:8"]]
+ 004f0c14 ["CALL", null, ["callee:00c58090:8"]]
- 004f0bd4 bytes 2f9c1d94
+ 004f0c14 bytes 1f9d1d94
- 004f0be4 ["INT_ADD", "register:40f0:8", ["const:4f0be4:8", "const:4:8"]]
- 004f0be4 ["CALL", null, ["callee:00c58000:8"]]
+ 004f0c24 ["INT_ADD", "register:40f0:8", ["const:4f0c24:8", "const:4:8"]]
+ 004f0c24 ["CALL", null, ["callee:00c58000:8"]]
- 004f0be4 bytes 079c1d94
+ 004f0c24 bytes f79c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ccf4ed3caa62816a6f07d57027db8b"></a>

### [`004f1508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md) → [`004f1548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1548.md) _ZN5Botan4X5098load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md) [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md#insn-004f1530) · [`004f1538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md#insn-004f1538) · [`004f1544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md#insn-004f1544)
- 新版 `004f1570`（命令位置の公開資料なし） · `004f1578`（命令位置の公開資料なし） · `004f1584`（命令位置の公開資料なし）

~~~diff
- 004f1530 ["INT_ADD", "register:40f0:8", ["const:4f1530:8", "const:4:8"]]
- 004f1530 ["CALL", null, ["callee:00c59660:8"]]
+ 004f1570 ["INT_ADD", "register:40f0:8", ["const:4f1570:8", "const:4:8"]]
+ 004f1570 ["CALL", null, ["callee:00c59660:8"]]
- 004f1530 bytes 4c9f1d94
+ 004f1570 bytes 3ca01d94
- 004f1538 ["INT_ADD", "register:40f0:8", ["const:4f1538:8", "const:4:8"]]
- 004f1538 ["CALL", null, ["callee:00c596d0:8"]]
+ 004f1578 ["INT_ADD", "register:40f0:8", ["const:4f1578:8", "const:4:8"]]
+ 004f1578 ["CALL", null, ["callee:00c596d0:8"]]
- 004f1538 bytes 669f1d94
+ 004f1578 bytes 56a01d94
- 004f1544 ["INT_ADD", "register:40f0:8", ["const:4f1544:8", "const:4:8"]]
- 004f1544 ["CALL", null, ["callee:00c59670:8"]]
+ 004f1584 ["INT_ADD", "register:40f0:8", ["const:4f1584:8", "const:4:8"]]
+ 004f1584 ["CALL", null, ["callee:00c59670:8"]]
- 004f1544 bytes 4b9f1d94
+ 004f1584 bytes 3ba01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-913319ceebfb4ffa38a9c3d8b1170161"></a>

### [`004f175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f175c.md) → [`004f179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f179c.md) _ZN5Botan21RandomNumberGenerator23randomize_with_ts_inputEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md) [`00c59310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59310.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md) [`00c59710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f175c.md#insn-004f1790) · [`004f1798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f175c.md#insn-004f1798) · [`004f17bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f175c.md#insn-004f17bc)
- 新版 `004f17d0`（命令位置の公開資料なし） · `004f17d8`（命令位置の公開資料なし） · `004f17fc`（命令位置の公開資料なし）

~~~diff
- 004f1790 ["INT_ADD", "register:40f0:8", ["const:4f1790:8", "const:4:8"]]
- 004f1790 ["CALL", null, ["callee:00c59700:8"]]
+ 004f17d0 ["INT_ADD", "register:40f0:8", ["const:4f17d0:8", "const:4:8"]]
+ 004f17d0 ["CALL", null, ["callee:00c59700:8"]]
- 004f1790 bytes dc9e1d94
+ 004f17d0 bytes cc9f1d94
- 004f1798 ["INT_ADD", "register:40f0:8", ["const:4f1798:8", "const:4:8"]]
- 004f1798 ["CALL", null, ["callee:00c58580:8"]]
+ 004f17d8 ["INT_ADD", "register:40f0:8", ["const:4f17d8:8", "const:4:8"]]
+ 004f17d8 ["CALL", null, ["callee:00c58580:8"]]
- 004f1798 bytes 7a9a1d94
+ 004f17d8 bytes 6a9b1d94
- 004f17bc ["INT_ADD", "register:40f0:8", ["const:4f17bc:8", "const:4:8"]]
- 004f17bc ["CALL", null, ["callee:00c59710:8"]]
+ 004f17fc ["INT_ADD", "register:40f0:8", ["const:4f17fc:8", "const:4:8"]]
+ 004f17fc ["CALL", null, ["callee:00c59710:8"]]
- 004f17bc bytes d59e1d94
+ 004f17fc bytes c59f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2a781357b24cee41365d3386732d605"></a>

### [`004f180c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f180c.md) → [`004f184c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f184c.md) _ZN5Botan2OS23get_system_timestamp_nsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f180c.md#insn-004f1830) · [`004f1838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f180c.md#insn-004f1838) · [`004f1878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f180c.md#insn-004f1878)
- 新版 `004f1870`（命令位置の公開資料なし） · `004f1878`（命令位置の公開資料なし） · `004f18b8`（命令位置の公開資料なし）

~~~diff
- 004f1830 ["INT_ADD", "register:40f0:8", ["const:4f1830:8", "const:4:8"]]
- 004f1830 ["CALL", null, ["callee:00c59700:8"]]
+ 004f1870 ["INT_ADD", "register:40f0:8", ["const:4f1870:8", "const:4:8"]]
+ 004f1870 ["CALL", null, ["callee:00c59700:8"]]
- 004f1830 bytes b49e1d94
+ 004f1870 bytes a49f1d94
- 004f1838 ["INT_ADD", "register:40f0:8", ["const:4f1838:8", "const:4:8"]]
- 004f1838 ["CALL", null, ["callee:00c58580:8"]]
+ 004f1878 ["INT_ADD", "register:40f0:8", ["const:4f1878:8", "const:4:8"]]
+ 004f1878 ["CALL", null, ["callee:00c58580:8"]]
- 004f1838 bytes 529a1d94
+ 004f1878 bytes 429b1d94
- 004f1878 ["INT_ADD", "register:40f0:8", ["const:4f1878:8", "const:4:8"]]
- 004f1878 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004f18b8 ["INT_ADD", "register:40f0:8", ["const:4f18b8:8", "const:4:8"]]
+ 004f18b8 ["CALL", null, ["callee:00c57ee0:8"]]
- 004f1878 bytes 9a981d94
+ 004f18b8 bytes 8a991d94
~~~


<a id="compare-3a16a1ccb7ac98919ed26a193e5455bd"></a>

### [`004f187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f187c.md) → [`004f18bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f18bc.md) _ZN5Botan2OS25get_high_resolution_clockEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59310.md) · 呼出先 3件 [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)
- 新版 呼出元 1件 [`00c59710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59710.md) · 呼出先 3件 [`00c57ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ec0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f18a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f187c.md#insn-004f18a0) · [`004f18b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f187c.md#insn-004f18b0) · [`004f18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f187c.md#insn-004f18c0)
- 新版 `004f18e0`（命令位置の公開資料なし） · `004f18f0`（命令位置の公開資料なし） · `004f1900`（命令位置の公開資料なし）

~~~diff
- 004f18a0 ["INT_ADD", "register:40f0:8", ["const:4f18a0:8", "const:4:8"]]
- 004f18a0 ["CALL", null, ["callee:00c59700:8"]]
+ 004f18e0 ["INT_ADD", "register:40f0:8", ["const:4f18e0:8", "const:4:8"]]
+ 004f18e0 ["CALL", null, ["callee:00c59700:8"]]
- 004f18a0 bytes 989e1d94
+ 004f18e0 bytes 889f1d94
- 004f18b0 ["INT_ADD", "register:40f0:8", ["const:4f18b0:8", "const:4:8"]]
- 004f18b0 ["CALL", null, ["callee:00c59700:8"]]
+ 004f18f0 ["INT_ADD", "register:40f0:8", ["const:4f18f0:8", "const:4:8"]]
+ 004f18f0 ["CALL", null, ["callee:00c59700:8"]]
- 004f18b0 bytes 949e1d94
+ 004f18f0 bytes 849f1d94
- 004f18c0 ["INT_ADD", "register:40f0:8", ["const:4f18c0:8", "const:4:8"]]
- 004f18c0 ["CALL", null, ["callee:00c59700:8"]]
+ 004f1900 ["INT_ADD", "register:40f0:8", ["const:4f1900:8", "const:4:8"]]
+ 004f1900 ["CALL", null, ["callee:00c59700:8"]]
- 004f18c0 bytes 909e1d94
+ 004f1900 bytes 809f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e47aaa0644d32fdbb9c06e7fe916edcc"></a>

### [`004f191c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f191c.md) → [`004f195c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f195c.md) _ZN5Botan21RandomNumberGenerator20randomize_with_inputEPhmPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f191c.md#insn-004f1948)
- 新版 `004f1988`（命令位置の公開資料なし）

~~~diff
- 004f1948 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f1948 ["INT_ADD", "register:40f0:8", ["const:4f1948:8", "const:4:8"]]
- 004f1948 ["CALLIND", null, ["register:0:8"]]
+ 004f1988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1988 ["INT_ADD", "register:40f0:8", ["const:4f1988:8", "const:4:8"]]
+ 004f1988 ["CALLIND", null, ["register:0:8"]]
- 004f1948 bytes 00013fd6
+ 004f1988 bytes 00013fd6
~~~


<a id="compare-aa4c7fd74d1ba0cd4f3a1ed022289720"></a>

### [`004f1970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1970.md) → [`004f19b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f19b0.md) _ZN5Botan21RandomNumberGenerator6reseedERNS_15Entropy_SourcesEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1970.md#insn-004f1994) · [`004f19c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1970.md#insn-004f19c4) · [`004f19d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1970.md#insn-004f19d4)
- 新版 `004f19d4`（命令位置の公開資料なし） · `004f1a04`（命令位置の公開資料なし） · `004f1a14`（命令位置の公開資料なし）

~~~diff
- 004f1994 ["INT_ADD", "register:40f0:8", ["const:4f1994:8", "const:4:8"]]
- 004f1994 ["CALL", null, ["callee:00c58580:8"]]
+ 004f19d4 ["INT_ADD", "register:40f0:8", ["const:4f19d4:8", "const:4:8"]]
+ 004f19d4 ["CALL", null, ["callee:00c58580:8"]]
- 004f1994 bytes fb991d94
+ 004f19d4 bytes eb9a1d94
- 004f19c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f19c4 ["INT_ADD", "register:40f0:8", ["const:4f19c4:8", "const:4:8"]]
- 004f19c4 ["CALLIND", null, ["register:0:8"]]
+ 004f1a04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1a04 ["INT_ADD", "register:40f0:8", ["const:4f1a04:8", "const:4:8"]]
+ 004f1a04 ["CALLIND", null, ["register:0:8"]]
- 004f19c4 bytes 00013fd6
+ 004f1a04 bytes 00013fd6
- 004f19d4 ["INT_ADD", "register:40f0:8", ["const:4f19d4:8", "const:4:8"]]
- 004f19d4 ["CALL", null, ["callee:00c58580:8"]]
+ 004f1a14 ["INT_ADD", "register:40f0:8", ["const:4f1a14:8", "const:4:8"]]
+ 004f1a14 ["CALL", null, ["callee:00c58580:8"]]
- 004f19d4 bytes eb991d94
+ 004f1a14 bytes db9a1d94
~~~


<a id="compare-d343ee5187e41c2f4a9f0d4e7376ada0"></a>

### [`004f1f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md) → [`004f1f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1f44.md) _ZNK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md#insn-004f1f3c) · [`004f1f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md#insn-004f1f4c) · [`004f1f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md#insn-004f1f5c)
- 新版 `004f1f7c`（命令位置の公開資料なし） · `004f1f8c`（命令位置の公開資料なし） · `004f1f9c`（命令位置の公開資料なし）

~~~diff
- 004f1f3c ["COPY", "register:0:8", ["register:4050:8"]]
- 004f1f3c ["INT_ADD", "register:40f0:8", ["const:4f1f3c:8", "const:4:8"]]
- 004f1f3c ["CALLIND", null, ["register:0:8"]]
+ 004f1f7c ["COPY", "register:0:8", ["register:4050:8"]]
+ 004f1f7c ["INT_ADD", "register:40f0:8", ["const:4f1f7c:8", "const:4:8"]]
+ 004f1f7c ["CALLIND", null, ["register:0:8"]]
- 004f1f3c bytes 40013fd6
+ 004f1f7c bytes 40013fd6
- 004f1f4c ["INT_ADD", "register:40f0:8", ["const:4f1f4c:8", "const:4:8"]]
- 004f1f4c ["CALL", null, ["callee:00c59720:8"]]
+ 004f1f8c ["INT_ADD", "register:40f0:8", ["const:4f1f8c:8", "const:4:8"]]
+ 004f1f8c ["CALL", null, ["callee:00c59720:8"]]
- 004f1f4c bytes f59c1d94
+ 004f1f8c bytes e59d1d94
- 004f1f5c ["INT_ADD", "register:40f0:8", ["const:4f1f5c:8", "const:4:8"]]
- 004f1f5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004f1f9c ["INT_ADD", "register:40f0:8", ["const:4f1f9c:8", "const:4:8"]]
+ 004f1f9c ["CALL", null, ["callee:00c57eb0:8"]]
- 004f1f5c bytes d5961d94
+ 004f1f9c bytes c5971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e0b091f37f125500c2f5a3aa146bd77"></a>

### [`004f1fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md) → [`004f1ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ff4.md) _ZTv0_n72_NK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md#insn-004f1ff8) · [`004f2008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md#insn-004f2008) · [`004f2018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md#insn-004f2018)
- 新版 `004f2038`（命令位置の公開資料なし） · `004f2048`（命令位置の公開資料なし） · `004f2058`（命令位置の公開資料なし）

~~~diff
- 004f1ff8 ["COPY", "register:0:8", ["register:4058:8"]]
- 004f1ff8 ["INT_ADD", "register:40f0:8", ["const:4f1ff8:8", "const:4:8"]]
- 004f1ff8 ["CALLIND", null, ["register:0:8"]]
+ 004f2038 ["COPY", "register:0:8", ["register:4058:8"]]
+ 004f2038 ["INT_ADD", "register:40f0:8", ["const:4f2038:8", "const:4:8"]]
+ 004f2038 ["CALLIND", null, ["register:0:8"]]
- 004f1ff8 bytes 60013fd6
+ 004f2038 bytes 60013fd6
- 004f2008 ["INT_ADD", "register:40f0:8", ["const:4f2008:8", "const:4:8"]]
- 004f2008 ["CALL", null, ["callee:00c59720:8"]]
+ 004f2048 ["INT_ADD", "register:40f0:8", ["const:4f2048:8", "const:4:8"]]
+ 004f2048 ["CALL", null, ["callee:00c59720:8"]]
- 004f2008 bytes c69c1d94
+ 004f2048 bytes b69d1d94
- 004f2018 ["INT_ADD", "register:40f0:8", ["const:4f2018:8", "const:4:8"]]
- 004f2018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004f2058 ["INT_ADD", "register:40f0:8", ["const:4f2058:8", "const:4:8"]]
+ 004f2058 ["CALL", null, ["callee:00c57eb0:8"]]
- 004f2018 bytes a6961d94
+ 004f2058 bytes 96971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3de83467834b6bfd3bbe36668bbd4363"></a>

### [`004f51c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51c8.md) → [`004f5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5208.md) _ZTv0_n104_NK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9a

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f51dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51c8.md#insn-004f51dc)
- 新版 `004f521c`（命令位置の公開資料なし）

~~~diff
- 004f51dc ["INT_ADD", "register:40f0:8", ["const:4f51dc:8", "const:4:8"]]
- 004f51dc ["CALL", null, ["callee:00c59760:8"]]
+ 004f521c ["INT_ADD", "register:40f0:8", ["const:4f521c:8", "const:4:8"]]
+ 004f521c ["CALL", null, ["callee:00c59760:8"]]
- 004f51dc bytes 61901d94
+ 004f521c bytes 51911d94
~~~


<a id="compare-cea1a52de5fd9342fca60eb94bbb43e9"></a>

### [`004f5b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5b08.md) → [`004f5b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5b48.md) _ZN5Botan7SHA_16010compress_nEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f5b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5b08.md#insn-004f5b68)
- 新版 `004f5ba8`（命令位置の公開資料なし）

~~~diff
- 004f5b68 ["INT_ADD", "register:40f0:8", ["const:4f5b68:8", "const:4:8"]]
- 004f5b68 ["CALL", null, ["callee:00540920:8"]]
+ 004f5ba8 ["INT_ADD", "register:40f0:8", ["const:4f5ba8:8", "const:4:8"]]
+ 004f5ba8 ["CALL", null, ["callee:00540920:8"]]
- 004f5b68 bytes 5e2b0194
+ 004f5ba8 bytes 5e2b0194
~~~


<a id="compare-583cb732e8ab63bdaac9a3806754e373"></a>

### [`004f8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md) → [`004f8b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md) _ZN5Botan12StreamCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004f8c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004f8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md#insn-004f8b38) · [`004f8b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md#insn-004f8b48) · [`004f8b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md#insn-004f8b84)
- 新版 `004f8b78`（命令位置の公開資料なし） · `004f8b88`（命令位置の公開資料なし） · `004f8bc4`（命令位置の公開資料なし）

~~~diff
- 004f8b38 ["INT_ADD", "register:40f0:8", ["const:4f8b38:8", "const:4:8"]]
- 004f8b38 ["CALL", null, ["callee:00473540:8"]]
+ 004f8b78 ["INT_ADD", "register:40f0:8", ["const:4f8b78:8", "const:4:8"]]
+ 004f8b78 ["CALL", null, ["callee:00473540:8"]]
- 004f8b38 bytes 72eafd97
+ 004f8b78 bytes 72eafd97
- 004f8b48 ["INT_ADD", "register:40f0:8", ["const:4f8b48:8", "const:4:8"]]
- 004f8b48 ["CALL", null, ["callee:004f8c6c:8"]]
+ 004f8b88 ["INT_ADD", "register:40f0:8", ["const:4f8b88:8", "const:4:8"]]
+ 004f8b88 ["CALL", null, ["callee:004f8c6c:8"]]
- 004f8b48 bytes 39000094
+ 004f8b88 bytes 39000094
- 004f8b84 ["INT_ADD", "register:40f0:8", ["const:4f8b84:8", "const:4:8"]]
- 004f8b84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004f8bc4 ["INT_ADD", "register:40f0:8", ["const:4f8bc4:8", "const:4:8"]]
+ 004f8bc4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004f8b84 bytes cb7b1d94
+ 004f8bc4 bytes bb7c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970af3ac74e7910a0d76eb1eba9bf91e"></a>

### [`004f8c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md) → [`004f8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8c6c.md) FUN_004f8c6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a60.md)
- 新版 呼出元 1件 [`004f8b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8b08.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md#insn-004f8c7c) · [`004f8c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md#insn-004f8c90) · [`004f8ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md#insn-004f8ca8)
- 新版 `004f8cbc`（命令位置の公開資料なし） · `004f8cd0`（命令位置の公開資料なし） · `004f8ce8`（命令位置の公開資料なし）

~~~diff
- 004f8c7c ["INT_ADD", "register:40f0:8", ["const:4f8c7c:8", "const:4:8"]]
- 004f8c7c ["CALL", null, ["callee:00540d7c:8"]]
+ 004f8cbc ["INT_ADD", "register:40f0:8", ["const:4f8cbc:8", "const:4:8"]]
+ 004f8cbc ["CALL", null, ["callee:00540d7c:8"]]
- 004f8c7c bytes 30200194
+ 004f8cbc bytes 30200194
- 004f8c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f8c90 ["INT_ADD", "register:40f0:8", ["const:4f8c90:8", "const:4:8"]]
- 004f8c90 ["CALLIND", null, ["register:0:8"]]
+ 004f8cd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f8cd0 ["INT_ADD", "register:40f0:8", ["const:4f8cd0:8", "const:4:8"]]
+ 004f8cd0 ["CALLIND", null, ["register:0:8"]]
- 004f8c90 bytes 00013fd6
+ 004f8cd0 bytes 00013fd6
- 004f8ca8 ["INT_ADD", "register:40f0:8", ["const:4f8ca8:8", "const:4:8"]]
- 004f8ca8 ["CALL", null, ["callee:00c58e60:8"]]
+ 004f8ce8 ["INT_ADD", "register:40f0:8", ["const:4f8ce8:8", "const:4:8"]]
+ 004f8ce8 ["CALL", null, ["callee:00c58e60:8"]]
- 004f8ca8 bytes 6e7f1d94
+ 004f8ce8 bytes 5e801d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54dab3be2e9ec4fac3b58beb616c3335"></a>

### [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) → [`004f8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md) FUN_004f8f6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) · 呼出先 1件 [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)
- 新版 呼出元 2件 [`004f8da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md) [`00535f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md) · 呼出先 1件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md#insn-004f8f40)
- 新版 `004f8f80`（命令位置の公開資料なし）

~~~diff
- 004f8f40 ["INT_ADD", "register:40f0:8", ["const:4f8f40:8", "const:4:8"]]
- 004f8f40 ["CALL", null, ["callee:00c597d0:8"]]
+ 004f8f80 ["INT_ADD", "register:40f0:8", ["const:4f8f80:8", "const:4:8"]]
+ 004f8f80 ["CALL", null, ["callee:00c597d0:8"]]
- 004f8f40 bytes 24811d94
+ 004f8f80 bytes 14821d94
~~~


<a id="compare-7addb792977f22d3823bc240f7bf4514"></a>

### [`004f9944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9944.md) → [`004f9984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9984.md) _ZN5Botan10DataSource12discard_nextEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9944.md#insn-004f99a0) · [`004f99dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9944.md#insn-004f99dc)
- 新版 `004f99e0`（命令位置の公開資料なし） · `004f9a1c`（命令位置の公開資料なし）

~~~diff
- 004f99a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f99a0 ["INT_ADD", "register:40f0:8", ["const:4f99a0:8", "const:4:8"]]
- 004f99a0 ["CALLIND", null, ["register:0:8"]]
+ 004f99e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f99e0 ["INT_ADD", "register:40f0:8", ["const:4f99e0:8", "const:4:8"]]
+ 004f99e0 ["CALLIND", null, ["register:0:8"]]
- 004f99a0 bytes 00013fd6
+ 004f99e0 bytes 00013fd6
- 004f99dc ["INT_ADD", "register:40f0:8", ["const:4f99dc:8", "const:4:8"]]
- 004f99dc ["CALL", null, ["callee:00c57ee0:8"]]
+ 004f9a1c ["INT_ADD", "register:40f0:8", ["const:4f9a1c:8", "const:4:8"]]
+ 004f9a1c ["CALL", null, ["callee:00c57ee0:8"]]
- 004f99dc bytes 41781d94
+ 004f9a1c bytes 31791d94
~~~


<a id="compare-3b18e6bd9da239b32f776e7a16102b0d"></a>

### [`004f99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f99e0.md) → [`004f9a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md) _ZN5Botan17DataSource_Memory4readEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f99e0.md#insn-004f9a18)
- 新版 `004f9a58`（命令位置の公開資料なし）

~~~diff
- 004f9a18 ["INT_ADD", "register:40f0:8", ["const:4f9a18:8", "const:4:8"]]
- 004f9a18 ["CALL", null, ["callee:00c57f40:8"]]
+ 004f9a58 ["INT_ADD", "register:40f0:8", ["const:4f9a58:8", "const:4:8"]]
+ 004f9a58 ["CALL", null, ["callee:00c57f40:8"]]
- 004f9a18 bytes 4a781d94
+ 004f9a58 bytes 3a791d94
~~~


<a id="compare-eb3e246e44791b4fda9951ce10673f11"></a>

### [`004f9a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9a54.md) → [`004f9a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a94.md) _ZNK5Botan17DataSource_Memory4peekEPhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9a54.md#insn-004f9a94)
- 新版 `004f9ad4`（命令位置の公開資料なし）

~~~diff
- 004f9a94 ["INT_ADD", "register:40f0:8", ["const:4f9a94:8", "const:4:8"]]
- 004f9a94 ["CALL", null, ["callee:00c57f40:8"]]
+ 004f9ad4 ["INT_ADD", "register:40f0:8", ["const:4f9ad4:8", "const:4:8"]]
+ 004f9ad4 ["CALL", null, ["callee:00c57f40:8"]]
- 004f9a94 bytes 2b781d94
+ 004f9ad4 bytes 1b791d94
~~~


<a id="compare-687d42dbc66de3602c5fb09ec6e25f00"></a>

### [`004f9c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9c4c.md) → [`004f9c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9c8c.md) _ZN5Botan17DataSource_Stream15check_availableEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c593e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593e0.md) [`00c593f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593f0.md) [`00c59400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59400.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c597e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597e0.md) [`00c597f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597f0.md) [`00c59800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9c4c.md#insn-004f9c68) · [`004f9c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9c4c.md#insn-004f9c80) · [`004f9c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9c4c.md#insn-004f9c88)
- 新版 `004f9ca8`（命令位置の公開資料なし） · `004f9cc0`（命令位置の公開資料なし） · `004f9cc8`（命令位置の公開資料なし）

~~~diff
- 004f9c68 ["INT_ADD", "register:40f0:8", ["const:4f9c68:8", "const:4:8"]]
- 004f9c68 ["CALL", null, ["callee:00c597e0:8"]]
+ 004f9ca8 ["INT_ADD", "register:40f0:8", ["const:4f9ca8:8", "const:4:8"]]
+ 004f9ca8 ["CALL", null, ["callee:00c597e0:8"]]
- 004f9c68 bytes de7d1d94
+ 004f9ca8 bytes ce7e1d94
- 004f9c80 ["INT_ADD", "register:40f0:8", ["const:4f9c80:8", "const:4:8"]]
- 004f9c80 ["CALL", null, ["callee:00c597f0:8"]]
+ 004f9cc0 ["INT_ADD", "register:40f0:8", ["const:4f9cc0:8", "const:4:8"]]
+ 004f9cc0 ["CALL", null, ["callee:00c597f0:8"]]
- 004f9c80 bytes dc7d1d94
+ 004f9cc0 bytes cc7e1d94
- 004f9c88 ["INT_ADD", "register:40f0:8", ["const:4f9c88:8", "const:4:8"]]
- 004f9c88 ["CALL", null, ["callee:00c597e0:8"]]
+ 004f9cc8 ["INT_ADD", "register:40f0:8", ["const:4f9cc8:8", "const:4:8"]]
+ 004f9cc8 ["CALL", null, ["callee:00c597e0:8"]]
- 004f9c88 bytes d67d1d94
+ 004f9cc8 bytes c67e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12c1d09efbe429d792399f89d401b5a"></a>

### [`004fa344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa344.md) → [`004fa384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa384.md) _ZN5Botan17DataSource_StreamD1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fa368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa344.md#insn-004fa368)
- 新版 `004fa3a8`（命令位置の公開資料なし）

~~~diff
- 004fa368 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fa368 ["INT_ADD", "register:40f0:8", ["const:4fa368:8", "const:4:8"]]
- 004fa368 ["CALLIND", null, ["register:0:8"]]
+ 004fa3a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fa3a8 ["INT_ADD", "register:40f0:8", ["const:4fa3a8:8", "const:4:8"]]
+ 004fa3a8 ["CALLIND", null, ["register:0:8"]]
- 004fa368 bytes 00013fd6
+ 004fa3a8 bytes 00013fd6
~~~


<a id="compare-7e4873af66da3bfb22eec9049d8bed30"></a>

### [`004fa390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa390.md) → [`004fa3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3d0.md) _ZN5Botan17DataSource_StreamD0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fa3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa390.md#insn-004fa3a0)
- 新版 `004fa3e0`（命令位置の公開資料なし）

~~~diff
- 004fa3a0 ["INT_ADD", "register:40f0:8", ["const:4fa3a0:8", "const:4:8"]]
- 004fa3a0 ["CALL", null, ["callee:00c59670:8"]]
+ 004fa3e0 ["INT_ADD", "register:40f0:8", ["const:4fa3e0:8", "const:4:8"]]
+ 004fa3e0 ["CALL", null, ["callee:00c59670:8"]]
- 004fa3a0 bytes b47b1d94
+ 004fa3e0 bytes a47c1d94
~~~


<a id="compare-d9b3dc23eeff199045ca11623a072212"></a>

### [`004fc69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc69c.md) → [`004fc6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc6dc.md) FUN_004fc6dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fc6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc69c.md#insn-004fc6ec) · [`004fc6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc69c.md#insn-004fc6fc)
- 新版 `004fc72c`（命令位置の公開資料なし） · `004fc73c`（命令位置の公開資料なし）

~~~diff
- 004fc6ec ["INT_ADD", "register:40f0:8", ["const:4fc6ec:8", "const:4:8"]]
- 004fc6ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 004fc72c ["INT_ADD", "register:40f0:8", ["const:4fc72c:8", "const:4:8"]]
+ 004fc72c ["CALL", null, ["callee:00c57eb0:8"]]
- 004fc6ec bytes f16c1d94
+ 004fc72c bytes e16d1d94
- 004fc6fc ["INT_ADD", "register:40f0:8", ["const:4fc6fc:8", "const:4:8"]]
- 004fc6fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004fc73c ["INT_ADD", "register:40f0:8", ["const:4fc73c:8", "const:4:8"]]
+ 004fc73c ["CALL", null, ["callee:00c57eb0:8"]]
- 004fc6fc bytes ed6c1d94
+ 004fc73c bytes dd6d1d94
~~~


<a id="compare-2abf90ee860810e3ea40a769fe3240fe"></a>

### [`004fd6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd6dc.md) → [`004fd71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd71c.md) _ZN5Botan11erase_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd6dc.md#insn-004fd724)
- 新版 `004fd764`（命令位置の公開資料なし）

~~~diff
- 004fd724 ["INT_ADD", "register:40f0:8", ["const:4fd724:8", "const:4:8"]]
- 004fd724 ["CALL", null, ["callee:00c58600:8"]]
+ 004fd764 ["INT_ADD", "register:40f0:8", ["const:4fd764:8", "const:4:8"]]
+ 004fd764 ["CALL", null, ["callee:00c58600:8"]]
- 004fd724 bytes b76a1d94
+ 004fd764 bytes a76b1d94
~~~


<a id="compare-03ab9f93148b2916d149bf99c19b9ddc"></a>

### [`004fd794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd794.md) → [`004fd7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd7d4.md) _ZN5Botan13replace_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd794.md#insn-004fd7d4)
- 新版 `004fd814`（命令位置の公開資料なし）

~~~diff
- 004fd7d4 ["INT_ADD", "register:40f0:8", ["const:4fd7d4:8", "const:4:8"]]
- 004fd7d4 ["CALL", null, ["callee:0043bb20:8"]]
+ 004fd814 ["INT_ADD", "register:40f0:8", ["const:4fd814:8", "const:4:8"]]
+ 004fd814 ["CALL", null, ["callee:0043bb20:8"]]
- 004fd7d4 bytes c3f8fc97
+ 004fd814 bytes c3f8fc97
~~~


<a id="compare-7a9c3a603a4f058cad01f10d95c7acb0"></a>

### [`004fd878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd878.md) → [`004fd8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd8b8.md) _ZN5Botan12replace_charERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEcc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd878.md#insn-004fd8b8)
- 新版 `004fd8f8`（命令位置の公開資料なし）

~~~diff
- 004fd8b8 ["INT_ADD", "register:40f0:8", ["const:4fd8b8:8", "const:4:8"]]
- 004fd8b8 ["CALL", null, ["callee:0043bb20:8"]]
+ 004fd8f8 ["INT_ADD", "register:40f0:8", ["const:4fd8f8:8", "const:4:8"]]
+ 004fd8f8 ["CALL", null, ["callee:0043bb20:8"]]
- 004fd8b8 bytes 8af8fc97
+ 004fd8f8 bytes 8af8fc97
~~~


<a id="compare-7689d87d866a41245524ad0caacab82f"></a>

### [`004fe260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe260.md) → [`004fe2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe2a0.md) _ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59540.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c59940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59940.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fe398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe260.md#insn-004fe398) · [`004fe3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe260.md#insn-004fe3b8) · [`004fe3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe260.md#insn-004fe3dc)
- 新版 `004fe3d8`（命令位置の公開資料なし） · `004fe3f8`（命令位置の公開資料なし） · `004fe41c`（命令位置の公開資料なし）

~~~diff
- 004fe398 ["INT_ADD", "register:40f0:8", ["const:4fe398:8", "const:4:8"]]
- 004fe398 ["CALL", null, ["callee:00c57e90:8"]]
+ 004fe3d8 ["INT_ADD", "register:40f0:8", ["const:4fe3d8:8", "const:4:8"]]
+ 004fe3d8 ["CALL", null, ["callee:00c57e90:8"]]
- 004fe398 bytes be651d94
+ 004fe3d8 bytes ae661d94
- 004fe3b8 ["INT_ADD", "register:40f0:8", ["const:4fe3b8:8", "const:4:8"]]
- 004fe3b8 ["CALL", null, ["callee:00c57f40:8"]]
+ 004fe3f8 ["INT_ADD", "register:40f0:8", ["const:4fe3f8:8", "const:4:8"]]
+ 004fe3f8 ["CALL", null, ["callee:00c57f40:8"]]
- 004fe3b8 bytes e2651d94
+ 004fe3f8 bytes d2661d94
- 004fe3dc ["INT_ADD", "register:40f0:8", ["const:4fe3dc:8", "const:4:8"]]
- 004fe3dc ["CALL", null, ["callee:0044291c:8"]]
+ 004fe41c ["INT_ADD", "register:40f0:8", ["const:4fe41c:8", "const:4:8"]]
+ 004fe41c ["CALL", null, ["callee:0044291c:8"]]
- 004fe3dc bytes 4011fd97
+ 004fe41c bytes 4011fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e5c5aec7ea6bb44e6eb65891759633f"></a>

### [`004ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) → [`004ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md) _ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59550.md) · 呼出先 3件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c59950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59950.md) · 呼出先 3件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md#insn-004ff058) · [`004ff0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md#insn-004ff0ec)
- 新版 `004ff098`（命令位置の公開資料なし） · `004ff12c`（命令位置の公開資料なし）

~~~diff
- 004ff058 ["INT_ADD", "register:40f0:8", ["const:4ff058:8", "const:4:8"]]
- 004ff058 ["CALL", null, ["callee:00547bb0:8"]]
+ 004ff098 ["INT_ADD", "register:40f0:8", ["const:4ff098:8", "const:4:8"]]
+ 004ff098 ["CALL", null, ["callee:00547bb0:8"]]
- 004ff058 bytes c6220194
+ 004ff098 bytes c6220194
- 004ff0ec ["INT_ADD", "register:40f0:8", ["const:4ff0ec:8", "const:4:8"]]
- 004ff0ec ["CALL", null, ["callee:00c58050:8"]]
+ 004ff12c ["INT_ADD", "register:40f0:8", ["const:4ff12c:8", "const:4:8"]]
+ 004ff12c ["CALL", null, ["callee:00c58050:8"]]
- 004ff0ec bytes d9621d94
+ 004ff12c bytes c9631d94
~~~


<a id="compare-9c0bf38c845e9deeb1b6f3a73689fc7f"></a>

### [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) → [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) FUN_004ff1a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`004ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) [`004ff3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md) [`00504984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504984.md) [`00504988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md) [`00504a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504a30.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 18件 [`004ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md) [`004ff428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md) [`005049c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c4.md) [`005049c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md) [`00504a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504a70.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md#insn-004ff1b0) · [`004ff1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md#insn-004ff1dc) · [`004ff1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md#insn-004ff1e8)
- 新版 `004ff1f0`（命令位置の公開資料なし） · `004ff21c`（命令位置の公開資料なし） · `004ff228`（命令位置の公開資料なし）

~~~diff
- 004ff1b0 ["INT_ADD", "register:40f0:8", ["const:4ff1b0:8", "const:4:8"]]
- 004ff1b0 ["CALL", null, ["callee:0043bb20:8"]]
+ 004ff1f0 ["INT_ADD", "register:40f0:8", ["const:4ff1f0:8", "const:4:8"]]
+ 004ff1f0 ["CALL", null, ["callee:0043bb20:8"]]
- 004ff1b0 bytes 4cf2fc97
+ 004ff1f0 bytes 4cf2fc97
- 004ff1dc ["INT_ADD", "register:40f0:8", ["const:4ff1dc:8", "const:4:8"]]
- 004ff1dc ["CALL", null, ["callee:0043bb20:8"]]
+ 004ff21c ["INT_ADD", "register:40f0:8", ["const:4ff21c:8", "const:4:8"]]
+ 004ff21c ["CALL", null, ["callee:0043bb20:8"]]
- 004ff1dc bytes 41f2fc97
+ 004ff21c bytes 41f2fc97
- 004ff1e8 ["INT_ADD", "register:40f0:8", ["const:4ff1e8:8", "const:4:8"]]
- 004ff1e8 ["CALL", null, ["callee:005490d4:8"]]
+ 004ff228 ["INT_ADD", "register:40f0:8", ["const:4ff228:8", "const:4:8"]]
+ 004ff228 ["CALL", null, ["callee:005490d4:8"]]
- 004ff1e8 bytes ab270194
+ 004ff228 bytes ab270194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca5cc14cccd09190a72f4f3c74da9e1"></a>

### [`004ff270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md) → [`004ff2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md) _ZN5Botan15AlternativeName13add_othernameERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59560.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2bc) · [`004ff2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2cc) · [`004ff2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2dc)
- 新版 `004ff2fc`（命令位置の公開資料なし） · `004ff30c`（命令位置の公開資料なし） · `004ff31c`（命令位置の公開資料なし）

~~~diff
- 004ff2bc ["INT_ADD", "register:40f0:8", ["const:4ff2bc:8", "const:4:8"]]
- 004ff2bc ["CALL", null, ["callee:00c59960:8"]]
+ 004ff2fc ["INT_ADD", "register:40f0:8", ["const:4ff2fc:8", "const:4:8"]]
+ 004ff2fc ["CALL", null, ["callee:00c59960:8"]]
- 004ff2bc bytes a9681d94
+ 004ff2fc bytes 99691d94
- 004ff2cc ["INT_ADD", "register:40f0:8", ["const:4ff2cc:8", "const:4:8"]]
- 004ff2cc ["CALL", null, ["callee:004ff37c:8"]]
+ 004ff30c ["INT_ADD", "register:40f0:8", ["const:4ff30c:8", "const:4:8"]]
+ 004ff30c ["CALL", null, ["callee:004ff37c:8"]]
- 004ff2cc bytes 1c000094
+ 004ff30c bytes 1c000094
- 004ff2dc ["INT_ADD", "register:40f0:8", ["const:4ff2dc:8", "const:4:8"]]
- 004ff2dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ff31c ["INT_ADD", "register:40f0:8", ["const:4ff31c:8", "const:4:8"]]
+ 004ff31c ["CALL", null, ["callee:00c57eb0:8"]]
- 004ff2dc bytes f5611d94
+ 004ff31c bytes e5621d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a50d29ac164944153bebb8ed335aa98"></a>

### [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) → [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) FUN_004ff37c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004ff270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md) [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) [`00514078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) [`0052e00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e00c.md) · 呼出先 4件 [`00547d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md) [`00547eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`004ff2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff2b0.md) [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) [`005140b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md) [`0052de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md) · 呼出先 4件 [`00547dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md) [`00547f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md#insn-004ff360) · [`004ff36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md#insn-004ff36c) · [`004ff37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md#insn-004ff37c)
- 新版 `004ff3a0`（命令位置の公開資料なし） · `004ff3ac`（命令位置の公開資料なし） · `004ff3bc`（命令位置の公開資料なし）

~~~diff
- 004ff360 ["INT_ADD", "register:40f0:8", ["const:4ff360:8", "const:4:8"]]
- 004ff360 ["CALL", null, ["callee:00547f2c:8"]]
+ 004ff3a0 ["INT_ADD", "register:40f0:8", ["const:4ff3a0:8", "const:4:8"]]
+ 004ff3a0 ["CALL", null, ["callee:00547f2c:8"]]
- 004ff360 bytes e3220194
+ 004ff3a0 bytes e3220194
- 004ff36c ["INT_ADD", "register:40f0:8", ["const:4ff36c:8", "const:4:8"]]
- 004ff36c ["CALL", null, ["callee:00547dc4:8"]]
+ 004ff3ac ["INT_ADD", "register:40f0:8", ["const:4ff3ac:8", "const:4:8"]]
+ 004ff3ac ["CALL", null, ["callee:00547dc4:8"]]
- 004ff36c bytes 86220194
+ 004ff3ac bytes 86220194
- 004ff37c ["INT_ADD", "register:40f0:8", ["const:4ff37c:8", "const:4:8"]]
- 004ff37c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ff3bc ["INT_ADD", "register:40f0:8", ["const:4ff3bc:8", "const:4:8"]]
+ 004ff3bc ["CALL", null, ["callee:00c57eb0:8"]]
- 004ff37c bytes cd611d94
+ 004ff3bc bytes bd621d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b73261a67e114152529d08ddeccacc0a"></a>

### [`004ff3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md) → [`004ff428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff428.md) _ZNK5Botan15AlternativeName8contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md) · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md)
- 新版 呼出元 1件 [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md) · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md#insn-004ff484) · [`004ff4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md#insn-004ff4cc) · [`004ff4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md#insn-004ff4dc)
- 新版 `004ff4c4`（命令位置の公開資料なし） · `004ff50c`（命令位置の公開資料なし） · `004ff51c`（命令位置の公開資料なし）

~~~diff
- 004ff484 ["INT_ADD", "register:40f0:8", ["const:4ff484:8", "const:4:8"]]
- 004ff484 ["CALL", null, ["callee:004ff1a0:8"]]
+ 004ff4c4 ["INT_ADD", "register:40f0:8", ["const:4ff4c4:8", "const:4:8"]]
+ 004ff4c4 ["CALL", null, ["callee:004ff1a0:8"]]
- 004ff484 bytes 37ffff97
+ 004ff4c4 bytes 37ffff97
- 004ff4cc ["INT_ADD", "register:40f0:8", ["const:4ff4cc:8", "const:4:8"]]
- 004ff4cc ["CALL", null, ["callee:00c588b0:8"]]
+ 004ff50c ["INT_ADD", "register:40f0:8", ["const:4ff50c:8", "const:4:8"]]
+ 004ff50c ["CALL", null, ["callee:00c588b0:8"]]
- 004ff4cc bytes f9631d94
+ 004ff50c bytes e9641d94
- 004ff4dc ["INT_ADD", "register:40f0:8", ["const:4ff4dc:8", "const:4:8"]]
- 004ff4dc ["CALL", null, ["callee:004ff1a0:8"]]
+ 004ff51c ["INT_ADD", "register:40f0:8", ["const:4ff51c:8", "const:4:8"]]
+ 004ff51c ["CALL", null, ["callee:004ff1a0:8"]]
- 004ff4dc bytes 21ffff97
+ 004ff51c bytes 21ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf29f10baea5e7dc405a3a3c679e038e"></a>

### [`004ff568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff568.md) → [`004ff5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5a8.md) _ZNK5Botan15AlternativeName9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff568.md#insn-004ff574)
- 新版 `004ff5b4`（命令位置の公開資料なし）

~~~diff
- 004ff574 ["INT_ADD", "register:40f0:8", ["const:4ff574:8", "const:4:8"]]
- 004ff574 ["CALL", null, ["callee:00548098:8"]]
+ 004ff5b4 ["INT_ADD", "register:40f0:8", ["const:4ff5b4:8", "const:4:8"]]
+ 004ff5b4 ["CALL", null, ["callee:00548098:8"]]
- 004ff574 bytes b9220194
+ 004ff5b4 bytes b9220194
~~~


<a id="compare-625d4b204cb79aff187d5133947276b0"></a>

### [`004ff588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff588.md) → [`004ff5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5c8.md) _ZNK5Botan15AlternativeName19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff588.md#insn-004ff5f8) · [`004ff680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff588.md#insn-004ff680)
- 新版 `004ff638`（命令位置の公開資料なし） · `004ff6c0`（命令位置の公開資料なし）

~~~diff
- 004ff5f8 ["INT_ADD", "register:40f0:8", ["const:4ff5f8:8", "const:4:8"]]
- 004ff5f8 ["CALL", null, ["callee:00c58050:8"]]
+ 004ff638 ["INT_ADD", "register:40f0:8", ["const:4ff638:8", "const:4:8"]]
+ 004ff638 ["CALL", null, ["callee:00c58050:8"]]
- 004ff5f8 bytes 96611d94
+ 004ff638 bytes 86621d94
- 004ff680 ["INT_ADD", "register:40f0:8", ["const:4ff680:8", "const:4:8"]]
- 004ff680 ["CALL", null, ["callee:00c58050:8"]]
+ 004ff6c0 ["INT_ADD", "register:40f0:8", ["const:4ff6c0:8", "const:4:8"]]
+ 004ff6c0 ["CALL", null, ["callee:00c58050:8"]]
- 004ff680 bytes 74611d94
+ 004ff6c0 bytes 64621d94
~~~


<a id="compare-f30a5fdd9ca05ac7474eb5d861a6a9e5"></a>

### [`004ff6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md) → [`004ff724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md) _ZNK5Botan15AlternativeName13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59580.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)
- 新版 呼出元 1件 [`00c59980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59980.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md#insn-004ff704) · [`004ff75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md#insn-004ff75c) · [`004ff770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md#insn-004ff770)
- 新版 `004ff744`（命令位置の公開資料なし） · `004ff79c`（命令位置の公開資料なし） · `004ff7b0`（命令位置の公開資料なし）

~~~diff
- 004ff704 ["INT_ADD", "register:40f0:8", ["const:4ff704:8", "const:4:8"]]
- 004ff704 ["CALL", null, ["callee:00548098:8"]]
+ 004ff744 ["INT_ADD", "register:40f0:8", ["const:4ff744:8", "const:4:8"]]
+ 004ff744 ["CALL", null, ["callee:00548098:8"]]
- 004ff704 bytes 55220194
+ 004ff744 bytes 55220194
- 004ff75c ["INT_ADD", "register:40f0:8", ["const:4ff75c:8", "const:4:8"]]
- 004ff75c ["CALL", null, ["callee:00540d7c:8"]]
+ 004ff79c ["INT_ADD", "register:40f0:8", ["const:4ff79c:8", "const:4:8"]]
+ 004ff79c ["CALL", null, ["callee:00540d7c:8"]]
- 004ff75c bytes 78050194
+ 004ff79c bytes 78050194
- 004ff770 ["INT_ADD", "register:40f0:8", ["const:4ff770:8", "const:4:8"]]
- 004ff770 ["CALL", null, ["callee:0043bb20:8"]]
+ 004ff7b0 ["INT_ADD", "register:40f0:8", ["const:4ff7b0:8", "const:4:8"]]
+ 004ff7b0 ["CALL", null, ["callee:0043bb20:8"]]
- 004ff770 bytes dcf0fc97
+ 004ff7b0 bytes dcf0fc97
~~~


<a id="compare-9145a611c829617513a3d99a59612425"></a>

### [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) → [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) FUN_00500f0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00500ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md#insn-00500ee8)
- 新版 `00500f28`（命令位置の公開資料なし）

~~~diff
- 00500ee8 ["INT_ADD", "register:40f0:8", ["const:500ee8:8", "const:4:8"]]
- 00500ee8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00500f28 ["INT_ADD", "register:40f0:8", ["const:500f28:8", "const:4:8"]]
+ 00500f28 ["CALL", null, ["callee:00c57eb0:8"]]
- 00500ee8 bytes f25a1d94
+ 00500f28 bytes e25b1d94
~~~


<a id="compare-af89d1b4d709667f2f922aec14afb3e2"></a>

### [`00501534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501534.md) → [`00501574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501574.md) _ZNK5Botan16X509_CertificateeqERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501534.md#insn-00501560) · [`00501570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501534.md#insn-00501570) · [`00501590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501534.md#insn-00501590)
- 新版 `005015a0`（命令位置の公開資料なし） · `005015b0`（命令位置の公開資料なし） · `005015d0`（命令位置の公開資料なし）

~~~diff
- 00501560 ["INT_ADD", "register:40f0:8", ["const:501560:8", "const:4:8"]]
- 00501560 ["CALL", null, ["callee:00c58050:8"]]
+ 005015a0 ["INT_ADD", "register:40f0:8", ["const:5015a0:8", "const:4:8"]]
+ 005015a0 ["CALL", null, ["callee:00c58050:8"]]
- 00501560 bytes bc591d94
+ 005015a0 bytes ac5a1d94
- 00501570 ["INT_ADD", "register:40f0:8", ["const:501570:8", "const:4:8"]]
- 00501570 ["CALL", null, ["callee:00c586a0:8"]]
+ 005015b0 ["INT_ADD", "register:40f0:8", ["const:5015b0:8", "const:4:8"]]
+ 005015b0 ["CALL", null, ["callee:00c586a0:8"]]
- 00501570 bytes 4c5b1d94
+ 005015b0 bytes 3c5c1d94
- 00501590 ["INT_ADD", "register:40f0:8", ["const:501590:8", "const:4:8"]]
- 00501590 ["CALL", null, ["callee:00c58050:8"]]
+ 005015d0 ["INT_ADD", "register:40f0:8", ["const:5015d0:8", "const:4:8"]]
+ 005015d0 ["CALL", null, ["callee:00c58050:8"]]
- 00501590 bytes b0591d94
+ 005015d0 bytes a05a1d94
~~~


<a id="compare-9448e8e800e6d6f2c6c3d5a29f64aa2a"></a>

### [`005015b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005015b0.md) → [`005015f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md) FUN_005015f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005015cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005015b0.md#insn-005015cc) · [`005015ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005015b0.md#insn-005015ec)
- 新版 `0050160c`（命令位置の公開資料なし） · `0050162c`（命令位置の公開資料なし）

~~~diff
- 005015cc ["INT_ADD", "register:40f0:8", ["const:5015cc:8", "const:4:8"]]
- 005015cc ["CALL", null, ["callee:00c53d00:8"]]
+ 0050160c ["INT_ADD", "register:40f0:8", ["const:50160c:8", "const:4:8"]]
+ 0050160c ["CALL", null, ["callee:00c53d00:8"]]
- 005015cc bytes c5481d94
+ 0050160c bytes bd491d94
- 005015ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005015ec ["INT_ADD", "register:40f0:8", ["const:5015ec:8", "const:4:8"]]
- 005015ec ["CALLIND", null, ["register:0:8"]]
+ 0050162c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050162c ["INT_ADD", "register:40f0:8", ["const:50162c:8", "const:4:8"]]
+ 0050162c ["CALLIND", null, ["register:0:8"]]
- 005015ec bytes 00013fd6
+ 0050162c bytes 00013fd6
~~~


<a id="compare-d9010444eeb6f883d2c69a4369ffec28"></a>

### [`00501600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md) → [`00501640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateENSt6__ndk110shared_ptrIKNS_16X509_CertificateEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c595e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595e0.md) · 呼出先 4件 [`00548558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)
- 新版 呼出元 1件 [`00c599e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599e0.md) · 呼出先 4件 [`00548598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050166c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md#insn-0050166c) · [`0050167c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md#insn-0050167c) · [`0050169c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md#insn-0050169c)
- 新版 `005016ac`（命令位置の公開資料なし） · `005016bc`（命令位置の公開資料なし） · `005016dc`（命令位置の公開資料なし）

~~~diff
- 0050166c ["INT_ADD", "register:40f0:8", ["const:50166c:8", "const:4:8"]]
- 0050166c ["CALL", null, ["callee:00c58050:8"]]
+ 005016ac ["INT_ADD", "register:40f0:8", ["const:5016ac:8", "const:4:8"]]
+ 005016ac ["CALL", null, ["callee:00c58050:8"]]
- 0050166c bytes 79591d94
+ 005016ac bytes 695a1d94
- 0050167c ["INT_ADD", "register:40f0:8", ["const:50167c:8", "const:4:8"]]
- 0050167c ["CALL", null, ["callee:00c586a0:8"]]
+ 005016bc ["INT_ADD", "register:40f0:8", ["const:5016bc:8", "const:4:8"]]
+ 005016bc ["CALL", null, ["callee:00c586a0:8"]]
- 0050167c bytes 095b1d94
+ 005016bc bytes f95b1d94
- 0050169c ["INT_ADD", "register:40f0:8", ["const:50169c:8", "const:4:8"]]
- 0050169c ["CALL", null, ["callee:00c58050:8"]]
+ 005016dc ["INT_ADD", "register:40f0:8", ["const:5016dc:8", "const:4:8"]]
+ 005016dc ["CALL", null, ["callee:00c58050:8"]]
- 0050169c bytes 6d591d94
+ 005016dc bytes 5d5a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14702c488ec6f9f000612066533ff8c5"></a>

### [`00501700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) → [`00501740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md) _ZNK5Botan27Certificate_Store_In_Memory12all_subjectsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md#insn-00501734) · [`0050174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md#insn-0050174c) · [`00501764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md#insn-00501764)
- 新版 `00501774`（命令位置の公開資料なし） · `0050178c`（命令位置の公開資料なし） · `005017a4`（命令位置の公開資料なし）

~~~diff
- 00501734 ["INT_ADD", "register:40f0:8", ["const:501734:8", "const:4:8"]]
- 00501734 ["CALL", null, ["callee:005486f4:8"]]
+ 00501774 ["INT_ADD", "register:40f0:8", ["const:501774:8", "const:4:8"]]
+ 00501774 ["CALL", null, ["callee:005486f4:8"]]
- 00501734 bytes e01b0194
+ 00501774 bytes e01b0194
- 0050174c ["INT_ADD", "register:40f0:8", ["const:50174c:8", "const:4:8"]]
- 0050174c ["CALL", null, ["callee:00c599f0:8"]]
+ 0050178c ["INT_ADD", "register:40f0:8", ["const:50178c:8", "const:4:8"]]
+ 0050178c ["CALL", null, ["callee:00c599f0:8"]]
- 0050174c bytes a95f1d94
+ 0050178c bytes 99601d94
- 00501764 ["INT_ADD", "register:40f0:8", ["const:501764:8", "const:4:8"]]
- 00501764 ["CALL", null, ["callee:005027f8:8"]]
+ 005017a4 ["INT_ADD", "register:40f0:8", ["const:5017a4:8", "const:4:8"]]
+ 005017a4 ["CALL", null, ["callee:005027f8:8"]]
- 00501764 bytes 15040094
+ 005017a4 bytes 15040094
~~~


