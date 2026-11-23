# v15.7.4 → v16.0.0 · 要調査の変更候補 (20)

[一覧の目次](README.md)

<a id="compare-0a0f22e130d8ade3be5a4073bdf2d1f9"></a>

### [`00b7c7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c7d0.md) → [`00bf9218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9218.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb520.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c7d0.md#insn-00b7c7e4)
- 新版 `00bf922c`（命令位置の公開資料なし）

~~~diff
- 00b7c7e4 ["INT_ADD", "register:40f0:8", ["const:b7c7e4:8", "const:4:8"]]
- 00b7c7e4 ["CALL", null, ["callee:00c57f70:8"]]
+ 00bf922c ["INT_ADD", "register:40f0:8", ["const:bf922c:8", "const:4:8"]]
+ 00bf922c ["CALL", null, ["callee:00c57f70:8"]]
- 00b7c7e4 bytes 4f7b0194
+ 00bf922c bytes 517b0194
~~~


<a id="compare-4eb760121c3962dc08b3a19c97b713aa"></a>

### [`00b7ca74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md) → [`00bf94bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf94bc.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1250.md) · 呼出先 3件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00c5de50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de50.md) · 呼出先 3件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md#insn-00b7ca8c) · [`00b7caa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md#insn-00b7caa0)
- 新版 `00bf94d4`（命令位置の公開資料なし） · `00bf94e8`（命令位置の公開資料なし）

~~~diff
- 00b7ca8c ["INT_ADD", "register:40f0:8", ["const:b7ca8c:8", "const:4:8"]]
- 00b7ca8c ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf94d4 ["INT_ADD", "register:40f0:8", ["const:bf94d4:8", "const:4:8"]]
+ 00bf94d4 ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7ca8c bytes 017a0194
+ 00bf94d4 bytes 037a0194
- 00b7caa0 ["INT_ADD", "register:40f0:8", ["const:b7caa0:8", "const:4:8"]]
- 00b7caa0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf94e8 ["INT_ADD", "register:40f0:8", ["const:bf94e8:8", "const:4:8"]]
+ 00bf94e8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7caa0 bytes a47a0194
+ 00bf94e8 bytes a67a0194
~~~


<a id="compare-705043f7be24eb1049c335c995abdf1c"></a>

### [`00b7cc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md) → [`00bf9678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9678.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6e0.md) · 呼出先 3件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) · 呼出先 3件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc5c) · [`00b7cc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc74) · [`00b7cc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc8c)
- 新版 `00bf96a4`（命令位置の公開資料なし） · `00bf96bc`（命令位置の公開資料なし） · `00bf96d4`（命令位置の公開資料なし）

~~~diff
- 00b7cc5c ["INT_ADD", "register:40f0:8", ["const:b7cc5c:8", "const:4:8"]]
- 00b7cc5c ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf96a4 ["INT_ADD", "register:40f0:8", ["const:bf96a4:8", "const:4:8"]]
+ 00bf96a4 ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7cc5c bytes 8d790194
+ 00bf96a4 bytes 8f790194
- 00b7cc74 ["INT_ADD", "register:40f0:8", ["const:b7cc74:8", "const:4:8"]]
- 00b7cc74 ["CALL", null, ["callee:00c58080:8"]]
+ 00bf96bc ["INT_ADD", "register:40f0:8", ["const:bf96bc:8", "const:4:8"]]
+ 00bf96bc ["CALL", null, ["callee:00c58080:8"]]
- 00b7cc74 bytes 6f7a0194
+ 00bf96bc bytes 717a0194
- 00b7cc8c ["INT_ADD", "register:40f0:8", ["const:b7cc8c:8", "const:4:8"]]
- 00b7cc8c ["CALL", null, ["callee:00c57cf0:8"]]
+ 00bf96d4 ["INT_ADD", "register:40f0:8", ["const:bf96d4:8", "const:4:8"]]
+ 00bf96d4 ["CALL", null, ["callee:00c57cf0:8"]]
- 00b7cc8c bytes 85790194
+ 00bf96d4 bytes 87790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-700fbb716249c13dd10436d6e07705e7"></a>

### [`00b7ccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ccd4.md) → [`00bf971c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf971c.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ccd4.md#insn-00b7cce4)
- 新版 `00bf972c`（命令位置の公開資料なし）

~~~diff
- 00b7cce4 ["INT_ADD", "register:40f0:8", ["const:b7cce4:8", "const:4:8"]]
- 00b7cce4 ["CALL", null, ["callee:0045a694:8"]]
+ 00bf972c ["INT_ADD", "register:40f0:8", ["const:bf972c:8", "const:4:8"]]
+ 00bf972c ["CALL", null, ["callee:0045a694:8"]]
- 00b7cce4 bytes c6eae297
+ 00bf972c bytes da83e197
~~~


<a id="compare-1bd5ec794d0ad72b68c0e89b571d25bb"></a>

### [`00b7cce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md) → [`00bf9730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9730.md) _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6d0.md) · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 1件 [`00c58120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58120.md) · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd04) · [`00b7cd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd18) · [`00b7cd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd3c)
- 新版 `00bf974c`（命令位置の公開資料なし） · `00bf9760`（命令位置の公開資料なし） · `00bf9784`（命令位置の公開資料なし）

~~~diff
- 00b7cd04 ["INT_ADD", "register:40f0:8", ["const:b7cd04:8", "const:4:8"]]
- 00b7cd04 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf974c ["INT_ADD", "register:40f0:8", ["const:bf974c:8", "const:4:8"]]
+ 00bf974c ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7cd04 bytes 63790194
+ 00bf974c bytes 65790194
- 00b7cd18 ["INT_ADD", "register:40f0:8", ["const:b7cd18:8", "const:4:8"]]
- 00b7cd18 ["CALL", null, ["callee:00c538b0:8"]]
+ 00bf9760 ["INT_ADD", "register:40f0:8", ["const:bf9760:8", "const:4:8"]]
+ 00bf9760 ["CALL", null, ["callee:00c538b0:8"]]
- 00b7cd18 bytes 52680194
+ 00bf9760 bytes 54680194
- 00b7cd3c ["INT_ADD", "register:40f0:8", ["const:b7cd3c:8", "const:4:8"]]
- 00b7cd3c ["CALL", null, ["callee:0045a694:8"]]
+ 00bf9784 ["INT_ADD", "register:40f0:8", ["const:bf9784:8", "const:4:8"]]
+ 00bf9784 ["CALL", null, ["callee:0045a694:8"]]
- 00b7cd3c bytes b0eae297
+ 00bf9784 bytes c483e197
~~~


<a id="compare-f85a92c4cc3f14f5de4ee32e94059b96"></a>

### [`00b7cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cd54.md) → [`00bf979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf979c.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cd54.md#insn-00b7cd74)
- 新版 `00bf97bc`（命令位置の公開資料なし）

~~~diff
- 00b7cd74 ["INT_ADD", "register:40f0:8", ["const:b7cd74:8", "const:4:8"]]
- 00b7cd74 ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf97bc ["INT_ADD", "register:40f0:8", ["const:bf97bc:8", "const:4:8"]]
+ 00bf97bc ["CALL", null, ["callee:00c538e0:8"]]
- 00b7cd74 bytes 47680194
+ 00bf97bc bytes 49680194
~~~


<a id="compare-a8717a2d577c58e762db3c5c2b1bd072"></a>

### [`00b7cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md) → [`00bf97f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be1260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md#insn-00b7cdc4) · [`00b7cdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md#insn-00b7cdd0)
- 新版 `00bf980c`（命令位置の公開資料なし） · `00bf9818`（命令位置の公開資料なし）

~~~diff
- 00b7cdc4 ["INT_ADD", "register:40f0:8", ["const:b7cdc4:8", "const:4:8"]]
- 00b7cdc4 ["CALL", null, ["callee:00c5de60:8"]]
+ 00bf980c ["INT_ADD", "register:40f0:8", ["const:bf980c:8", "const:4:8"]]
+ 00bf980c ["CALL", null, ["callee:00c5de60:8"]]
- 00b7cdc4 bytes 27910194
+ 00bf980c bytes 95910194
- 00b7cdd0 ["INT_ADD", "register:40f0:8", ["const:b7cdd0:8", "const:4:8"]]
- 00b7cdd0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf9818 ["INT_ADD", "register:40f0:8", ["const:bf9818:8", "const:4:8"]]
+ 00bf9818 ["CALL", null, ["callee:00c538e0:8"]]
- 00b7cdd0 bytes 30680194
+ 00bf9818 bytes 32680194
~~~


<a id="compare-98d43638fa51f7a1bbd6eb80857568e2"></a>

### [`00b7d044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d044.md) → [`00bf9a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9a8c.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d044.md#insn-00b7d064)
- 新版 `00bf9aac`（命令位置の公開資料なし）

~~~diff
- 00b7d064 ["INT_ADD", "register:40f0:8", ["const:b7d064:8", "const:4:8"]]
- 00b7d064 ["CALL", null, ["callee:0045a694:8"]]
+ 00bf9aac ["INT_ADD", "register:40f0:8", ["const:bf9aac:8", "const:4:8"]]
+ 00bf9aac ["CALL", null, ["callee:0045a694:8"]]
- 00b7d064 bytes e6e9e297
+ 00bf9aac bytes fa82e197
~~~


<a id="compare-27a3694e0b259a38c98a13639494183b"></a>

### [`00b7d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0c8.md) → [`00bf9b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b10.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00be1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c5de20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0c8.md#insn-00b7d0e8)
- 新版 `00bf9b30`（命令位置の公開資料なし）

~~~diff
- 00b7d0e8 ["INT_ADD", "register:40f0:8", ["const:b7d0e8:8", "const:4:8"]]
- 00b7d0e8 ["CALL", null, ["callee:0045a694:8"]]
+ 00bf9b30 ["INT_ADD", "register:40f0:8", ["const:bf9b30:8", "const:4:8"]]
+ 00bf9b30 ["CALL", null, ["callee:0045a694:8"]]
- 00b7d0e8 bytes c5e9e297
+ 00bf9b30 bytes d982e197
~~~


<a id="compare-a4390f3f0dc5f67625c0c011864bef16"></a>

### [`00b7d14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d14c.md) → [`00bf9b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d14c.md#insn-00b7d16c)
- 新版 `00bf9bb4`（命令位置の公開資料なし）

~~~diff
- 00b7d16c ["INT_ADD", "register:40f0:8", ["const:b7d16c:8", "const:4:8"]]
- 00b7d16c ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf9bb4 ["INT_ADD", "register:40f0:8", ["const:bf9bb4:8", "const:4:8"]]
+ 00bf9bb4 ["CALL", null, ["callee:00c538e0:8"]]
- 00b7d16c bytes 49670194
+ 00bf9bb4 bytes 4b670194
~~~


<a id="compare-55cced7b0ab3800c9ca320c3f0772295"></a>

### [`00b7d1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md) → [`00bf9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9be8.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1cc) · [`00b7d1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1e0) · [`00b7d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1f4)
- 新版 `00bf9c14`（命令位置の公開資料なし） · `00bf9c28`（命令位置の公開資料なし） · `00bf9c3c`（命令位置の公開資料なし）

~~~diff
- 00b7d1cc ["INT_ADD", "register:40f0:8", ["const:b7d1cc:8", "const:4:8"]]
- 00b7d1cc ["CALL", null, ["callee:00c538b0:8"]]
+ 00bf9c14 ["INT_ADD", "register:40f0:8", ["const:bf9c14:8", "const:4:8"]]
+ 00bf9c14 ["CALL", null, ["callee:00c538b0:8"]]
- 00b7d1cc bytes 25670194
+ 00bf9c14 bytes 27670194
- 00b7d1e0 ["INT_ADD", "register:40f0:8", ["const:b7d1e0:8", "const:4:8"]]
- 00b7d1e0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf9c28 ["INT_ADD", "register:40f0:8", ["const:bf9c28:8", "const:4:8"]]
+ 00bf9c28 ["CALL", null, ["callee:00c538e0:8"]]
- 00b7d1e0 bytes 2c670194
+ 00bf9c28 bytes 2e670194
- 00b7d1f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7d1f4 ["INT_ADD", "register:40f0:8", ["const:b7d1f4:8", "const:4:8"]]
- 00b7d1f4 ["CALLIND", null, ["register:0:8"]]
+ 00bf9c3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf9c3c ["INT_ADD", "register:40f0:8", ["const:bf9c3c:8", "const:4:8"]]
+ 00bf9c3c ["CALLIND", null, ["register:0:8"]]
- 00b7d1f4 bytes 00013fd6
+ 00bf9c3c bytes 00013fd6
~~~


<a id="compare-c9fe70aee13fcdd0812b4e90adb849ab"></a>

### [`00b7d2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2ec.md) → [`00bf9d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d34.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2ec.md#insn-00b7d2f8)
- 新版 `00bf9d40`（命令位置の公開資料なし）

~~~diff
- 00b7d2f8 ["INT_ADD", "register:40f0:8", ["const:b7d2f8:8", "const:4:8"]]
- 00b7d2f8 ["CALL", null, ["callee:00c5de70:8"]]
+ 00bf9d40 ["INT_ADD", "register:40f0:8", ["const:bf9d40:8", "const:4:8"]]
+ 00bf9d40 ["CALL", null, ["callee:00c5de70:8"]]
- 00b7d2f8 bytes de8f0194
+ 00bf9d40 bytes 4c900194
~~~


<a id="compare-ba982ebfac51e219ae9dd7114b9bd030"></a>

### [`00b7d314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d314.md) → [`00bf9d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d5c.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 1件 [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d314.md#insn-00b7d320)
- 新版 `00bf9d68`（命令位置の公開資料なし）

~~~diff
- 00b7d320 ["INT_ADD", "register:40f0:8", ["const:b7d320:8", "const:4:8"]]
- 00b7d320 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bf9d68 ["INT_ADD", "register:40f0:8", ["const:bf9d68:8", "const:4:8"]]
+ 00bf9d68 ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b7d320 bytes 44850194
+ 00bf9d68 bytes 52850194
~~~


<a id="compare-c7961d48611742d97e427c0652594799"></a>

### [`00b7d3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3d8.md) → [`00bf9e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e20.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd280.md) · 呼出先 1件 [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md)
- 新版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cd0.md) · 呼出先 1件 [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3d8.md#insn-00b7d3e4)
- 新版 `00bf9e2c`（命令位置の公開資料なし）

~~~diff
- 00b7d3e4 ["INT_ADD", "register:40f0:8", ["const:b7d3e4:8", "const:4:8"]]
- 00b7d3e4 ["CALL", null, ["callee:00c5b290:8"]]
+ 00bf9e2c ["INT_ADD", "register:40f0:8", ["const:bf9e2c:8", "const:4:8"]]
+ 00bf9e2c ["CALL", null, ["callee:00c5b290:8"]]
- 00b7d3e4 bytes 0b850194
+ 00bf9e2c bytes 19850194
~~~


<a id="compare-e88ce09f895f400b535135cd1e52accd"></a>

### [`00b7d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md) → [`00bf9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e6c.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md) · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md) · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md#insn-00b7d430)
- 新版 `00bf9e78`（命令位置の公開資料なし）

~~~diff
- 00b7d430 ["INT_ADD", "register:40f0:8", ["const:b7d430:8", "const:4:8"]]
- 00b7d430 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bf9e78 ["INT_ADD", "register:40f0:8", ["const:bf9e78:8", "const:4:8"]]
+ 00bf9e78 ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b7d430 bytes 00850194
+ 00bf9e78 bytes 0e850194
~~~


<a id="compare-7c920d1f5acf8525702d589b554c985e"></a>

### [`00b7d444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d444.md) → [`00bf9e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e8c.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d444.md#insn-00b7d450)
- 新版 `00bf9e98`（命令位置の公開資料なし）

~~~diff
- 00b7d450 ["INT_ADD", "register:40f0:8", ["const:b7d450:8", "const:4:8"]]
- 00b7d450 ["CALL", null, ["callee:00c5de70:8"]]
+ 00bf9e98 ["INT_ADD", "register:40f0:8", ["const:bf9e98:8", "const:4:8"]]
+ 00bf9e98 ["CALL", null, ["callee:00c5de70:8"]]
- 00b7d450 bytes 888f0194
+ 00bf9e98 bytes f68f0194
~~~


<a id="compare-56cf770055200d096dfbb2491bbc27b9"></a>

### [`00b7d56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md) → [`00bf9fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md#insn-00b7d580) · [`00b7d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md#insn-00b7d5ac)
- 新版 `00bf9fc8`（命令位置の公開資料なし） · `00bf9ff4`（命令位置の公開資料なし）

~~~diff
- 00b7d580 ["INT_ADD", "register:40f0:8", ["const:b7d580:8", "const:4:8"]]
- 00b7d580 ["CALL", null, ["callee:00c5de70:8"]]
+ 00bf9fc8 ["INT_ADD", "register:40f0:8", ["const:bf9fc8:8", "const:4:8"]]
+ 00bf9fc8 ["CALL", null, ["callee:00c5de70:8"]]
- 00b7d580 bytes 3c8f0194
+ 00bf9fc8 bytes aa8f0194
- 00b7d5ac ["INT_ADD", "register:40f0:8", ["const:b7d5ac:8", "const:4:8"]]
- 00b7d5ac ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bf9ff4 ["INT_ADD", "register:40f0:8", ["const:bf9ff4:8", "const:4:8"]]
+ 00bf9ff4 ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b7d5ac bytes a1840194
+ 00bf9ff4 bytes af840194
~~~


<a id="compare-9eb319aa2c01fc211bf1765a93bcc3b8"></a>

### [`00b7d770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md) → [`00bfa1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa1b8.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d788) · [`00b7d794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d794) · [`00b7d7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d7d4)
- 新版 `00bfa1d0`（命令位置の公開資料なし） · `00bfa1dc`（命令位置の公開資料なし） · `00bfa21c`（命令位置の公開資料なし）

~~~diff
- 00b7d788 ["INT_ADD", "register:40f0:8", ["const:b7d788:8", "const:4:8"]]
- 00b7d788 ["CALL", null, ["callee:00c58220:8"]]
+ 00bfa1d0 ["INT_ADD", "register:40f0:8", ["const:bfa1d0:8", "const:4:8"]]
+ 00bfa1d0 ["CALL", null, ["callee:00c58220:8"]]
- 00b7d788 bytes 12780194
+ 00bfa1d0 bytes 14780194
- 00b7d794 ["INT_ADD", "register:40f0:8", ["const:b7d794:8", "const:4:8"]]
- 00b7d794 ["CALL", null, ["callee:00c5de70:8"]]
+ 00bfa1dc ["INT_ADD", "register:40f0:8", ["const:bfa1dc:8", "const:4:8"]]
+ 00bfa1dc ["CALL", null, ["callee:00c5de70:8"]]
- 00b7d794 bytes b78e0194
+ 00bfa1dc bytes 258f0194
- 00b7d7d4 ["INT_ADD", "register:40f0:8", ["const:b7d7d4:8", "const:4:8"]]
- 00b7d7d4 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bfa21c ["INT_ADD", "register:40f0:8", ["const:bfa21c:8", "const:4:8"]]
+ 00bfa21c ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b7d7d4 bytes 17840194
+ 00bfa21c bytes 25840194
~~~


<a id="compare-a5b60ffbe170ba9dff013543ae9bf93f"></a>

### [`00b7d874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md) → [`00bfa2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2bc.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md) · 呼出先 1件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md) · 呼出先 1件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md#insn-00b7d890)
- 新版 `00bfa2d8`（命令位置の公開資料なし）

~~~diff
- 00b7d890 ["INT_ADD", "register:40f0:8", ["const:b7d890:8", "const:4:8"]]
- 00b7d890 ["CALL", null, ["callee:00c57c20:8"]]
+ 00bfa2d8 ["INT_ADD", "register:40f0:8", ["const:bfa2d8:8", "const:4:8"]]
+ 00bfa2d8 ["CALL", null, ["callee:00c57c20:8"]]
- 00b7d890 bytes 50760194
+ 00bfa2d8 bytes 52760194
~~~


<a id="compare-81b6db9614596b0132cf27b263b66bce"></a>

### [`00b7d928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d928.md) → [`00bfa370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa370.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d928.md#insn-00b7d938)
- 新版 `00bfa380`（命令位置の公開資料なし）

~~~diff
- 00b7d938 ["INT_ADD", "register:40f0:8", ["const:b7d938:8", "const:4:8"]]
- 00b7d938 ["CALL", null, ["callee:00c5de90:8"]]
+ 00bfa380 ["INT_ADD", "register:40f0:8", ["const:bfa380:8", "const:4:8"]]
+ 00bfa380 ["CALL", null, ["callee:00c5de90:8"]]
- 00b7d938 bytes 568e0194
+ 00bfa380 bytes c48e0194
~~~


<a id="compare-b1edba1a44c90ad5f90efb177c81b4e5"></a>

### [`00b7d954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md) → [`00bfa39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa39c.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb640.md) · 呼出先 2件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be12a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12a0.md)
- 新版 呼出元 1件 [`00c58090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58090.md) · 呼出先 2件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md#insn-00b7d9a8) · [`00b7d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md#insn-00b7d9b4)
- 新版 `00bfa3f0`（命令位置の公開資料なし） · `00bfa3fc`（命令位置の公開資料なし）

~~~diff
- 00b7d9a8 ["INT_ADD", "register:40f0:8", ["const:b7d9a8:8", "const:4:8"]]
- 00b7d9a8 ["CALL", null, ["callee:00c5dea0:8"]]
+ 00bfa3f0 ["INT_ADD", "register:40f0:8", ["const:bfa3f0:8", "const:4:8"]]
+ 00bfa3f0 ["CALL", null, ["callee:00c5dea0:8"]]
- 00b7d9a8 bytes 3e8e0194
+ 00bfa3f0 bytes ac8e0194
- 00b7d9b4 ["INT_ADD", "register:40f0:8", ["const:b7d9b4:8", "const:4:8"]]
- 00b7d9b4 ["CALL", null, ["callee:00c57cc0:8"]]
+ 00bfa3fc ["INT_ADD", "register:40f0:8", ["const:bfa3fc:8", "const:4:8"]]
+ 00bfa3fc ["CALL", null, ["callee:00c57cc0:8"]]
- 00b7d9b4 bytes 2f760194
+ 00bfa3fc bytes 31760194
~~~


<a id="compare-856b018b2c3dafa38cd9975c6d87feec"></a>

### [`00b7db58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md) → [`00bfa5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md) FUN_00bfa5a0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7ddc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddc4.md) · 呼出先 4件 [`00b7dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bfa80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa80c.md) · 呼出先 4件 [`00bfa824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dbd4) · [`00b7dc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dc18) · [`00b7dc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dc2c)
- 新版 `00bfa61c`（命令位置の公開資料なし） · `00bfa660`（命令位置の公開資料なし） · `00bfa674`（命令位置の公開資料なし）

~~~diff
- 00b7dbd4 ["INT_ADD", "register:40f0:8", ["const:b7dbd4:8", "const:4:8"]]
- 00b7dbd4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bfa61c ["INT_ADD", "register:40f0:8", ["const:bfa61c:8", "const:4:8"]]
+ 00bfa61c ["CALL", null, ["callee:00c57a90:8"]]
- 00b7dbd4 bytes 1b750194
+ 00bfa61c bytes 1d750194
- 00b7dc18 ["INT_ADD", "register:40f0:8", ["const:b7dc18:8", "const:4:8"]]
- 00b7dc18 ["CALL", null, ["callee:00c57c00:8"]]
+ 00bfa660 ["INT_ADD", "register:40f0:8", ["const:bfa660:8", "const:4:8"]]
+ 00bfa660 ["CALL", null, ["callee:00c57c00:8"]]
- 00b7dc18 bytes 66750194
+ 00bfa660 bytes 68750194
- 00b7dc2c ["INT_ADD", "register:40f0:8", ["const:b7dc2c:8", "const:4:8"]]
- 00b7dc2c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bfa674 ["INT_ADD", "register:40f0:8", ["const:bfa674:8", "const:4:8"]]
+ 00bfa674 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b7dc2c bytes 0d750194
+ 00bfa674 bytes 0f750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-589a30453166735863ea0d54eaf14053"></a>

### [`00b7dc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md) → [`00bfa69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) FUN_00bfa69c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7ddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddd0.md) · 呼出先 5件 [`00b7ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bfa818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa818.md) · 呼出先 5件 [`00bfa83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dcc8) · [`00b7dcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dcfc) · [`00b7dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dd10)
- 新版 `00bfa710`（命令位置の公開資料なし） · `00bfa744`（命令位置の公開資料なし） · `00bfa758`（命令位置の公開資料なし）

~~~diff
- 00b7dcc8 ["INT_ADD", "register:40f0:8", ["const:b7dcc8:8", "const:4:8"]]
- 00b7dcc8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bfa710 ["INT_ADD", "register:40f0:8", ["const:bfa710:8", "const:4:8"]]
+ 00bfa710 ["CALL", null, ["callee:00c57a90:8"]]
- 00b7dcc8 bytes de740194
+ 00bfa710 bytes e0740194
- 00b7dcfc ["INT_ADD", "register:40f0:8", ["const:b7dcfc:8", "const:4:8"]]
- 00b7dcfc ["CALL", null, ["callee:00c57c00:8"]]
+ 00bfa744 ["INT_ADD", "register:40f0:8", ["const:bfa744:8", "const:4:8"]]
+ 00bfa744 ["CALL", null, ["callee:00c57c00:8"]]
- 00b7dcfc bytes 2d750194
+ 00bfa744 bytes 2f750194
- 00b7dd10 ["INT_ADD", "register:40f0:8", ["const:b7dd10:8", "const:4:8"]]
- 00b7dd10 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bfa758 ["INT_ADD", "register:40f0:8", ["const:bfa758:8", "const:4:8"]]
+ 00bfa758 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b7dd10 bytes d4740194
+ 00bfa758 bytes d6740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-343e82707c8ecec23b92264d45f385e5"></a>

### [`00b7dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md) → [`00bfa930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa930.md) _ZNSt6__ndk113random_deviceD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md) [`00bdb580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb580.md) · 呼出先 1件 [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md)
- 新版 呼出元 2件 [`0056074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md) [`00c57fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fd0.md) · 呼出先 1件 [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7def8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md#insn-00b7def8)
- 新版 `00bfa940`（命令位置の公開資料なし）

~~~diff
- 00b7def8 ["INT_ADD", "register:40f0:8", ["const:b7def8:8", "const:4:8"]]
- 00b7def8 ["CALL", null, ["callee:00c593d0:8"]]
+ 00bfa940 ["INT_ADD", "register:40f0:8", ["const:bfa940:8", "const:4:8"]]
+ 00bfa940 ["CALL", null, ["callee:00c593d0:8"]]
- 00b7def8 bytes a27a0194
+ 00bfa940 bytes a47a0194
~~~


<a id="compare-0fd1040abb191528adcccd5ea57b04cf"></a>

### [`00b7e154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e154.md) → [`00bfab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab9c.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be12c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e154.md#insn-00b7e168)
- 新版 `00bfabb0`（命令位置の公開資料なし）

~~~diff
- 00b7e168 ["INT_ADD", "register:40f0:8", ["const:b7e168:8", "const:4:8"]]
- 00b7e168 ["CALL", null, ["callee:00c5dec0:8"]]
+ 00bfabb0 ["INT_ADD", "register:40f0:8", ["const:bfabb0:8", "const:4:8"]]
+ 00bfabb0 ["CALL", null, ["callee:00c5dec0:8"]]
- 00b7e168 bytes 568c0194
+ 00bfabb0 bytes c48c0194
~~~


<a id="compare-1150b1fa3f51fae46f93c3ffc82a8438"></a>

### [`00b7e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e180.md) → [`00bfabc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfabc8.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e180.md#insn-00b7e1c0)
- 新版 `00bfac08`（命令位置の公開資料なし）

~~~diff
- 00b7e1c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e1c0 ["INT_ADD", "register:40f0:8", ["const:b7e1c0:8", "const:4:8"]]
- 00b7e1c0 ["CALLIND", null, ["register:0:8"]]
+ 00bfac08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfac08 ["INT_ADD", "register:40f0:8", ["const:bfac08:8", "const:4:8"]]
+ 00bfac08 ["CALLIND", null, ["register:0:8"]]
- 00b7e1c0 bytes 00013fd6
+ 00bfac08 bytes 00013fd6
~~~


<a id="compare-567ca5ce0e4fc03671df7fd953fe6259"></a>

### [`00b7e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e668.md) → [`00bfb0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0b0.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be12f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5def0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e668.md#insn-00b7e67c)
- 新版 `00bfb0c4`（命令位置の公開資料なし）

~~~diff
- 00b7e67c ["INT_ADD", "register:40f0:8", ["const:b7e67c:8", "const:4:8"]]
- 00b7e67c ["CALL", null, ["callee:00c5def0:8"]]
+ 00bfb0c4 ["INT_ADD", "register:40f0:8", ["const:bfb0c4:8", "const:4:8"]]
+ 00bfb0c4 ["CALL", null, ["callee:00c5def0:8"]]
- 00b7e67c bytes 1d8b0194
+ 00bfb0c4 bytes 8b8b0194
~~~


<a id="compare-3ded34fad98b3c601f78fb5056e977bb"></a>

### [`00b7e7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md) → [`00bfb208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb208.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md) · 呼出先 5件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md) · 呼出先 5件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e7f4) · [`00b7e804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e804) · [`00b7e830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e830)
- 新版 `00bfb23c`（命令位置の公開資料なし） · `00bfb24c`（命令位置の公開資料なし） · `00bfb278`（命令位置の公開資料なし）

~~~diff
- 00b7e7f4 ["INT_ADD", "register:40f0:8", ["const:b7e7f4:8", "const:4:8"]]
- 00b7e7f4 ["CALL", null, ["callee:00c59c20:8"]]
+ 00bfb23c ["INT_ADD", "register:40f0:8", ["const:bfb23c:8", "const:4:8"]]
+ 00bfb23c ["CALL", null, ["callee:00c59c20:8"]]
- 00b7e7f4 bytes 777a0194
+ 00bfb23c bytes 797a0194
- 00b7e804 ["INT_ADD", "register:40f0:8", ["const:b7e804:8", "const:4:8"]]
- 00b7e804 ["CALL", null, ["callee:00c59c20:8"]]
+ 00bfb24c ["INT_ADD", "register:40f0:8", ["const:bfb24c:8", "const:4:8"]]
+ 00bfb24c ["CALL", null, ["callee:00c59c20:8"]]
- 00b7e804 bytes 737a0194
+ 00bfb24c bytes 757a0194
- 00b7e830 ["INT_ADD", "register:40f0:8", ["const:b7e830:8", "const:4:8"]]
- 00b7e830 ["CALL", null, ["callee:00c59c20:8"]]
+ 00bfb278 ["INT_ADD", "register:40f0:8", ["const:bfb278:8", "const:4:8"]]
+ 00bfb278 ["CALL", null, ["callee:00c59c20:8"]]
- 00b7e830 bytes 687a0194
+ 00bfb278 bytes 6a7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734ddaaa84fd40a105069286bfd6ae05"></a>

### [`00b7ea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ea80.md) → [`00bfb4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb4c8.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ea80.md#insn-00b7eabc)
- 新版 `00bfb504`（命令位置の公開資料なし）

~~~diff
- 00b7eabc ["INT_ADD", "register:40f0:8", ["const:b7eabc:8", "const:4:8"]]
- 00b7eabc ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfb504 ["INT_ADD", "register:40f0:8", ["const:bfb504:8", "const:4:8"]]
+ 00bfb504 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7eabc bytes b17b0194
+ 00bfb504 bytes b37b0194
~~~


<a id="compare-7a71e06440280a879885188eed0e53bc"></a>

### [`00b7ec38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec38.md) → [`00bfb680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb680.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb470.md) · 呼出先 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md)
- 新版 呼出元 1件 [`00c57ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ec0.md) · 呼出先 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec38.md#insn-00b7ec60)
- 新版 `00bfb6a8`（命令位置の公開資料なし）

~~~diff
- 00b7ec60 ["INT_ADD", "register:40f0:8", ["const:b7ec60:8", "const:4:8"]]
- 00b7ec60 ["CALL", null, ["callee:00c58100:8"]]
+ 00bfb6a8 ["INT_ADD", "register:40f0:8", ["const:bfb6a8:8", "const:4:8"]]
+ 00bfb6a8 ["CALL", null, ["callee:00c58100:8"]]
- 00b7ec60 bytes 94720194
+ 00bfb6a8 bytes 96720194
~~~


<a id="compare-696f31e15d0853d335de88ec087b3f45"></a>

### [`00b7ec64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md) → [`00bfb6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6ac.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1330.md) · 呼出先 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md)
- 新版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df30.md) · 呼出先 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md#insn-00b7ec8c)
- 新版 `00bfb6d4`（命令位置の公開資料なし）

~~~diff
- 00b7ec8c ["INT_ADD", "register:40f0:8", ["const:b7ec8c:8", "const:4:8"]]
- 00b7ec8c ["CALL", null, ["callee:00c58100:8"]]
+ 00bfb6d4 ["INT_ADD", "register:40f0:8", ["const:bfb6d4:8", "const:4:8"]]
+ 00bfb6d4 ["CALL", null, ["callee:00c58100:8"]]
- 00b7ec8c bytes 89720194
+ 00bfb6d4 bytes 8b720194
~~~


<a id="compare-bccbf5e79dbc96fbc5bddda73be63def"></a>

### [`00b7ece0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ece0.md) → [`00bfb728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb728.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5df40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ecf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ece0.md#insn-00b7ecf4)
- 新版 `00bfb73c`（命令位置の公開資料なし）

~~~diff
- 00b7ecf4 ["INT_ADD", "register:40f0:8", ["const:b7ecf4:8", "const:4:8"]]
- 00b7ecf4 ["CALL", null, ["callee:00c5df40:8"]]
+ 00bfb73c ["INT_ADD", "register:40f0:8", ["const:bfb73c:8", "const:4:8"]]
+ 00bfb73c ["CALL", null, ["callee:00c5df40:8"]]
- 00b7ecf4 bytes 93890194
+ 00bfb73c bytes 018a0194
~~~


<a id="compare-deacd4114ba05e5ad8be459070fbd210"></a>

### [`00b7ed0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md) → [`00bfb754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ed34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed34) · [`00b7ed40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed40) · [`00b7ed5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed5c)
- 新版 `00bfb77c`（命令位置の公開資料なし） · `00bfb788`（命令位置の公開資料なし） · `00bfb7a4`（命令位置の公開資料なし）

~~~diff
- 00b7ed34 ["INT_ADD", "register:40f0:8", ["const:b7ed34:8", "const:4:8"]]
- 00b7ed34 ["CALL", null, ["callee:00c5ded0:8"]]
+ 00bfb77c ["INT_ADD", "register:40f0:8", ["const:bfb77c:8", "const:4:8"]]
+ 00bfb77c ["CALL", null, ["callee:00c5ded0:8"]]
- 00b7ed34 bytes 67890194
+ 00bfb77c bytes d5890194
- 00b7ed40 ["INT_ADD", "register:40f0:8", ["const:b7ed40:8", "const:4:8"]]
- 00b7ed40 ["CALL", null, ["callee:00c5df10:8"]]
+ 00bfb788 ["INT_ADD", "register:40f0:8", ["const:bfb788:8", "const:4:8"]]
+ 00bfb788 ["CALL", null, ["callee:00c5df10:8"]]
- 00b7ed40 bytes 74890194
+ 00bfb788 bytes e2890194
- 00b7ed5c ["INT_ADD", "register:40f0:8", ["const:b7ed5c:8", "const:4:8"]]
- 00b7ed5c ["CALL", null, ["callee:00c5ded0:8"]]
+ 00bfb7a4 ["INT_ADD", "register:40f0:8", ["const:bfb7a4:8", "const:4:8"]]
+ 00bfb7a4 ["CALL", null, ["callee:00c5ded0:8"]]
- 00b7ed5c bytes 5d890194
+ 00bfb7a4 bytes cb890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98247dc242092b3eec83097b0236c43a"></a>

### [`00b7eda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eda0.md) → [`00bfb7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb7e8.md) FUN_00bfb7e8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1350.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5df50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7edb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eda0.md#insn-00b7edb4)
- 新版 `00bfb7fc`（命令位置の公開資料なし）

~~~diff
- 00b7edb4 ["INT_ADD", "register:40f0:8", ["const:b7edb4:8", "const:4:8"]]
- 00b7edb4 ["CALL", null, ["callee:00c5df50:8"]]
+ 00bfb7fc ["INT_ADD", "register:40f0:8", ["const:bfb7fc:8", "const:4:8"]]
+ 00bfb7fc ["CALL", null, ["callee:00c5df50:8"]]
- 00b7edb4 bytes 67890194
+ 00bfb7fc bytes d5890194
~~~


<a id="compare-623bf948f5c53912a54bd4f8f2068097"></a>

### [`00b7edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md) → [`00bfb814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb814.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7edf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md#insn-00b7edf4) · [`00b7ee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md#insn-00b7ee00)
- 新版 `00bfb83c`（命令位置の公開資料なし） · `00bfb848`（命令位置の公開資料なし）

~~~diff
- 00b7edf4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7edf4 ["INT_ADD", "register:40f0:8", ["const:b7edf4:8", "const:4:8"]]
- 00b7edf4 ["CALLIND", null, ["register:0:8"]]
+ 00bfb83c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfb83c ["INT_ADD", "register:40f0:8", ["const:bfb83c:8", "const:4:8"]]
+ 00bfb83c ["CALLIND", null, ["register:0:8"]]
- 00b7edf4 bytes 20013fd6
+ 00bfb83c bytes 20013fd6
- 00b7ee00 ["INT_ADD", "register:40f0:8", ["const:b7ee00:8", "const:4:8"]]
- 00b7ee00 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfb848 ["INT_ADD", "register:40f0:8", ["const:bfb848:8", "const:4:8"]]
+ 00bfb848 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7ee00 bytes e07a0194
+ 00bfb848 bytes e27a0194
~~~


<a id="compare-7ea928567c39733de5ee232b99559666"></a>

### [`00b7ee94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee94.md) → [`00bfb8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb8dc.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee94.md#insn-00b7eed4)
- 新版 `00bfb91c`（命令位置の公開資料なし）

~~~diff
- 00b7eed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7eed4 ["INT_ADD", "register:40f0:8", ["const:b7eed4:8", "const:4:8"]]
- 00b7eed4 ["CALLIND", null, ["register:0:8"]]
+ 00bfb91c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb91c ["INT_ADD", "register:40f0:8", ["const:bfb91c:8", "const:4:8"]]
+ 00bfb91c ["CALLIND", null, ["register:0:8"]]
- 00b7eed4 bytes 00013fd6
+ 00bfb91c bytes 00013fd6
~~~


<a id="compare-4eb398ad71d765a8aeb8511e93909227"></a>

### [`00b7f0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f0c8.md) → [`00bfbb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb10.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f0c8.md#insn-00b7f0e8)
- 新版 `00bfbb30`（命令位置の公開資料なし）

~~~diff
- 00b7f0e8 ["INT_ADD", "register:40f0:8", ["const:b7f0e8:8", "const:4:8"]]
- 00b7f0e8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bfbb30 ["INT_ADD", "register:40f0:8", ["const:bfbb30:8", "const:4:8"]]
+ 00bfbb30 ["CALL", null, ["callee:00c5dee0:8"]]
- 00b7f0e8 bytes 7e880194
+ 00bfbb30 bytes ec880194
~~~


<a id="compare-81c79bb81feafdf2345e8c296107192f"></a>

### [`00b7f21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f21c.md) → [`00bfbc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbc64.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f21c.md#insn-00b7f258)
- 新版 `00bfbca0`（命令位置の公開資料なし）

~~~diff
- 00b7f258 ["INT_ADD", "register:40f0:8", ["const:b7f258:8", "const:4:8"]]
- 00b7f258 ["CALL", null, ["callee:00c57de0:8"]]
+ 00bfbca0 ["INT_ADD", "register:40f0:8", ["const:bfbca0:8", "const:4:8"]]
+ 00bfbca0 ["CALL", null, ["callee:00c57de0:8"]]
- 00b7f258 bytes 4e700194
+ 00bfbca0 bytes 50700194
~~~


<a id="compare-07747e723b7310e4e17798647325b3f5"></a>

### [`00b7f2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f2ec.md) → [`00bfbd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbd34.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f2ec.md#insn-00b7f324)
- 新版 `00bfbd6c`（命令位置の公開資料なし）

~~~diff
- 00b7f324 ["INT_ADD", "register:40f0:8", ["const:b7f324:8", "const:4:8"]]
- 00b7f324 ["CALL", null, ["callee:00c5df20:8"]]
+ 00bfbd6c ["INT_ADD", "register:40f0:8", ["const:bfbd6c:8", "const:4:8"]]
+ 00bfbd6c ["CALL", null, ["callee:00c5df20:8"]]
- 00b7f324 bytes ff870194
+ 00bfbd6c bytes 6d880194
~~~


<a id="compare-436960e40ec61f53d0c721d474a054c5"></a>

### [`00b7f53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f53c.md) → [`00bfbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbf84.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f53c.md#insn-00b7f55c)
- 新版 `00bfbfa4`（命令位置の公開資料なし）

~~~diff
- 00b7f55c ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f55c ["INT_ADD", "register:40f0:8", ["const:b7f55c:8", "const:4:8"]]
- 00b7f55c ["CALLIND", null, ["register:0:8"]]
+ 00bfbfa4 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfbfa4 ["INT_ADD", "register:40f0:8", ["const:bfbfa4:8", "const:4:8"]]
+ 00bfbfa4 ["CALLIND", null, ["register:0:8"]]
- 00b7f55c bytes 20003fd6
+ 00bfbfa4 bytes 20003fd6
~~~


<a id="compare-1c6c3236b0aa419775f794be39cfc251"></a>

### [`00b7f574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f574.md) → [`00bfbfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbfbc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f574.md#insn-00b7f594)
- 新版 `00bfbfdc`（命令位置の公開資料なし）

~~~diff
- 00b7f594 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f594 ["INT_ADD", "register:40f0:8", ["const:b7f594:8", "const:4:8"]]
- 00b7f594 ["CALLIND", null, ["register:0:8"]]
+ 00bfbfdc ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfbfdc ["INT_ADD", "register:40f0:8", ["const:bfbfdc:8", "const:4:8"]]
+ 00bfbfdc ["CALLIND", null, ["register:0:8"]]
- 00b7f594 bytes 20003fd6
+ 00bfbfdc bytes 20003fd6
~~~


<a id="compare-6b334ebd5007db8b60b2763a3cc7ecca"></a>

### [`00b808d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b808d4.md) → [`00bfd31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd31c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b808ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b808d4.md#insn-00b808ec)
- 新版 `00bfd334`（命令位置の公開資料なし）

~~~diff
- 00b808ec ["INT_ADD", "register:40f0:8", ["const:b808ec:8", "const:4:8"]]
- 00b808ec ["CALL", null, ["callee:00c5df60:8"]]
+ 00bfd334 ["INT_ADD", "register:40f0:8", ["const:bfd334:8", "const:4:8"]]
+ 00bfd334 ["CALL", null, ["callee:00c5df60:8"]]
- 00b808ec bytes 9d820194
+ 00bfd334 bytes 0b830194
~~~


<a id="compare-5d9b1b48732569dddc74f229215d0f3d"></a>

### [`00b81b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md) → [`00bfe5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe5b0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)
- 新版 呼出元 1件 [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81ba4) · [`00b81bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81bc8) · [`00b81bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81bec)
- 新版 `00bfe5ec`（命令位置の公開資料なし） · `00bfe610`（命令位置の公開資料なし） · `00bfe634`（命令位置の公開資料なし）

~~~diff
- 00b81ba4 ["INT_ADD", "register:40f0:8", ["const:b81ba4:8", "const:4:8"]]
- 00b81ba4 ["CALL", null, ["callee:00c5ccf0:8"]]
+ 00bfe5ec ["INT_ADD", "register:40f0:8", ["const:bfe5ec:8", "const:4:8"]]
+ 00bfe5ec ["CALL", null, ["callee:00c5ccf0:8"]]
- 00b81ba4 bytes 93790194
+ 00bfe5ec bytes c1790194
- 00b81bc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81bc8 ["INT_ADD", "register:40f0:8", ["const:b81bc8:8", "const:4:8"]]
- 00b81bc8 ["CALLIND", null, ["register:0:8"]]
+ 00bfe610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe610 ["INT_ADD", "register:40f0:8", ["const:bfe610:8", "const:4:8"]]
+ 00bfe610 ["CALLIND", null, ["register:0:8"]]
- 00b81bc8 bytes 00013fd6
+ 00bfe610 bytes 00013fd6
- 00b81bec ["INT_ADD", "register:40f0:8", ["const:b81bec:8", "const:4:8"]]
- 00b81bec ["CALL", null, ["callee:00c57ea0:8"]]
+ 00bfe634 ["INT_ADD", "register:40f0:8", ["const:bfe634:8", "const:4:8"]]
+ 00bfe634 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b81bec bytes 19660194
+ 00bfe634 bytes 1b660194
~~~


<a id="compare-849dced6df96da36265dc9eab760339a"></a>

### [`00b81c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c1c.md) → [`00bfe664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe664.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c1c.md#insn-00b81c3c)
- 新版 `00bfe684`（命令位置の公開資料なし）

~~~diff
- 00b81c3c ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81c3c ["INT_ADD", "register:40f0:8", ["const:b81c3c:8", "const:4:8"]]
- 00b81c3c ["CALLIND", null, ["register:0:8"]]
+ 00bfe684 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfe684 ["INT_ADD", "register:40f0:8", ["const:bfe684:8", "const:4:8"]]
+ 00bfe684 ["CALLIND", null, ["register:0:8"]]
- 00b81c3c bytes 20003fd6
+ 00bfe684 bytes 20003fd6
~~~


<a id="compare-41e05c2e342d9fd97afeb57b6ee43d92"></a>

### [`00b81c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c54.md) → [`00bfe69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe69c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c54.md#insn-00b81c74)
- 新版 `00bfe6bc`（命令位置の公開資料なし）

~~~diff
- 00b81c74 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81c74 ["INT_ADD", "register:40f0:8", ["const:b81c74:8", "const:4:8"]]
- 00b81c74 ["CALLIND", null, ["register:0:8"]]
+ 00bfe6bc ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfe6bc ["INT_ADD", "register:40f0:8", ["const:bfe6bc:8", "const:4:8"]]
+ 00bfe6bc ["CALLIND", null, ["register:0:8"]]
- 00b81c74 bytes 20003fd6
+ 00bfe6bc bytes 20003fd6
~~~


<a id="compare-0a919c954000d9b02173680111c04c85"></a>

### [`00b828d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b828d4.md) → [`00bff31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff31c.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8291c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b828d4.md#insn-00b8291c)
- 新版 `00bff364`（命令位置の公開資料なし）

~~~diff
- 00b8291c ["INT_ADD", "register:40f0:8", ["const:b8291c:8", "const:4:8"]]
- 00b8291c ["CALL", null, ["callee:00c57de0:8"]]
+ 00bff364 ["INT_ADD", "register:40f0:8", ["const:bff364:8", "const:4:8"]]
+ 00bff364 ["CALL", null, ["callee:00c57de0:8"]]
- 00b8291c bytes 9d620194
+ 00bff364 bytes 9f620194
~~~


<a id="compare-09c4854b0644e550dba285b5a683e7ce"></a>

### [`00b82a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a64.md) → [`00bff4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4ac.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a64.md#insn-00b82a7c)
- 新版 `00bff4c4`（命令位置の公開資料なし）

~~~diff
- 00b82a7c ["INT_ADD", "register:40f0:8", ["const:b82a7c:8", "const:4:8"]]
- 00b82a7c ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bff4c4 ["INT_ADD", "register:40f0:8", ["const:bff4c4:8", "const:4:8"]]
+ 00bff4c4 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b82a7c bytes d9750194
+ 00bff4c4 bytes 07760194
~~~


<a id="compare-161d4cb4c9eaebbc4183d52d079ccce4"></a>

### [`00b82b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md) → [`00bff5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ded0.md) [`00c5df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82b94) · [`00b82ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82ba0) · [`00b82bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82bbc)
- 新版 `00bff5dc`（命令位置の公開資料なし） · `00bff5e8`（命令位置の公開資料なし） · `00bff604`（命令位置の公開資料なし）

~~~diff
- 00b82b94 ["INT_ADD", "register:40f0:8", ["const:b82b94:8", "const:4:8"]]
- 00b82b94 ["CALL", null, ["callee:00c5ded0:8"]]
+ 00bff5dc ["INT_ADD", "register:40f0:8", ["const:bff5dc:8", "const:4:8"]]
+ 00bff5dc ["CALL", null, ["callee:00c5ded0:8"]]
- 00b82b94 bytes cf790194
+ 00bff5dc bytes 3d7a0194
- 00b82ba0 ["INT_ADD", "register:40f0:8", ["const:b82ba0:8", "const:4:8"]]
- 00b82ba0 ["CALL", null, ["callee:00c5df10:8"]]
+ 00bff5e8 ["INT_ADD", "register:40f0:8", ["const:bff5e8:8", "const:4:8"]]
+ 00bff5e8 ["CALL", null, ["callee:00c5df10:8"]]
- 00b82ba0 bytes dc790194
+ 00bff5e8 bytes 4a7a0194
- 00b82bbc ["INT_ADD", "register:40f0:8", ["const:b82bbc:8", "const:4:8"]]
- 00b82bbc ["CALL", null, ["callee:00c5ded0:8"]]
+ 00bff604 ["INT_ADD", "register:40f0:8", ["const:bff604:8", "const:4:8"]]
+ 00bff604 ["CALL", null, ["callee:00c5ded0:8"]]
- 00b82bbc bytes c5790194
+ 00bff604 bytes 337a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb631bac3cc1a095b9635f04c7940bcd"></a>

### [`00b82c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md) → [`00bff674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md#insn-00b82c54) · [`00b82c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md#insn-00b82c60)
- 新版 `00bff69c`（命令位置の公開資料なし） · `00bff6a8`（命令位置の公開資料なし）

~~~diff
- 00b82c54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b82c54 ["INT_ADD", "register:40f0:8", ["const:b82c54:8", "const:4:8"]]
- 00b82c54 ["CALLIND", null, ["register:0:8"]]
+ 00bff69c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bff69c ["INT_ADD", "register:40f0:8", ["const:bff69c:8", "const:4:8"]]
+ 00bff69c ["CALLIND", null, ["register:0:8"]]
- 00b82c54 bytes 20013fd6
+ 00bff69c bytes 20013fd6
- 00b82c60 ["INT_ADD", "register:40f0:8", ["const:b82c60:8", "const:4:8"]]
- 00b82c60 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bff6a8 ["INT_ADD", "register:40f0:8", ["const:bff6a8:8", "const:4:8"]]
+ 00bff6a8 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b82c60 bytes 486b0194
+ 00bff6a8 bytes 4a6b0194
~~~


<a id="compare-0d3dee73566e7ea500b941a10237234a"></a>

### [`00b82cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82cf8.md) → [`00bff740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff740.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82cf8.md#insn-00b82d44)
- 新版 `00bff78c`（命令位置の公開資料なし）

~~~diff
- 00b82d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82d44 ["INT_ADD", "register:40f0:8", ["const:b82d44:8", "const:4:8"]]
- 00b82d44 ["CALLIND", null, ["register:0:8"]]
+ 00bff78c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff78c ["INT_ADD", "register:40f0:8", ["const:bff78c:8", "const:4:8"]]
+ 00bff78c ["CALLIND", null, ["register:0:8"]]
- 00b82d44 bytes 00013fd6
+ 00bff78c bytes 00013fd6
~~~


<a id="compare-d75aefd4597223b34a94d0fdb0c7e5b1"></a>

### [`00b82f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f34.md) → [`00bff97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff97c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f34.md#insn-00b82f54)
- 新版 `00bff99c`（命令位置の公開資料なし）

~~~diff
- 00b82f54 ["INT_ADD", "register:40f0:8", ["const:b82f54:8", "const:4:8"]]
- 00b82f54 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bff99c ["INT_ADD", "register:40f0:8", ["const:bff99c:8", "const:4:8"]]
+ 00bff99c ["CALL", null, ["callee:00c5dee0:8"]]
- 00b82f54 bytes e3780194
+ 00bff99c bytes 51790194
~~~


<a id="compare-40fcdafca011ed504c866f86a0cd52f6"></a>

### [`00b830d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md) → [`00bffb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffb18.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md#insn-00b83154) · [`00b8316c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md#insn-00b8316c)
- 新版 `00bffb9c`（命令位置の公開資料なし） · `00bffbb4`（命令位置の公開資料なし）

~~~diff
- 00b83154 ["INT_ADD", "register:40f0:8", ["const:b83154:8", "const:4:8"]]
- 00b83154 ["CALL", null, ["callee:00c57b40:8"]]
+ 00bffb9c ["INT_ADD", "register:40f0:8", ["const:bffb9c:8", "const:4:8"]]
+ 00bffb9c ["CALL", null, ["callee:00c57b40:8"]]
- 00b83154 bytes e75f0194
+ 00bffb9c bytes e95f0194
- 00b8316c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8316c ["INT_ADD", "register:40f0:8", ["const:b8316c:8", "const:4:8"]]
- 00b8316c ["CALLIND", null, ["register:0:8"]]
+ 00bffbb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffbb4 ["INT_ADD", "register:40f0:8", ["const:bffbb4:8", "const:4:8"]]
+ 00bffbb4 ["CALLIND", null, ["register:0:8"]]
- 00b8316c bytes 00013fd6
+ 00bffbb4 bytes 00013fd6
~~~


<a id="compare-5a4348cf1ecdbf6d034a98240a990b28"></a>

### [`00b831b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b831b0.md) → [`00bffbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffbf8.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b831cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b831b0.md#insn-00b831cc)
- 新版 `00bffc14`（命令位置の公開資料なし）

~~~diff
- 00b831cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b831cc ["INT_ADD", "register:40f0:8", ["const:b831cc:8", "const:4:8"]]
- 00b831cc ["CALLIND", null, ["register:0:8"]]
+ 00bffc14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffc14 ["INT_ADD", "register:40f0:8", ["const:bffc14:8", "const:4:8"]]
+ 00bffc14 ["CALLIND", null, ["register:0:8"]]
- 00b831cc bytes 00013fd6
+ 00bffc14 bytes 00013fd6
~~~


<a id="compare-31f5e74724656e71aeffdbefce22ca68"></a>

### [`00b83200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md) → [`00bffc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffc48.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8327c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md#insn-00b8327c) · [`00b83298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md#insn-00b83298)
- 新版 `00bffcc4`（命令位置の公開資料なし） · `00bffce0`（命令位置の公開資料なし）

~~~diff
- 00b8327c ["INT_ADD", "register:40f0:8", ["const:b8327c:8", "const:4:8"]]
- 00b8327c ["CALL", null, ["callee:00c57b40:8"]]
+ 00bffcc4 ["INT_ADD", "register:40f0:8", ["const:bffcc4:8", "const:4:8"]]
+ 00bffcc4 ["CALL", null, ["callee:00c57b40:8"]]
- 00b8327c bytes 9d5f0194
+ 00bffcc4 bytes 9f5f0194
- 00b83298 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83298 ["INT_ADD", "register:40f0:8", ["const:b83298:8", "const:4:8"]]
- 00b83298 ["CALLIND", null, ["register:0:8"]]
+ 00bffce0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffce0 ["INT_ADD", "register:40f0:8", ["const:bffce0:8", "const:4:8"]]
+ 00bffce0 ["CALLIND", null, ["register:0:8"]]
- 00b83298 bytes 00013fd6
+ 00bffce0 bytes 00013fd6
~~~


<a id="compare-95abff390c4e68d30c491441b557d1c5"></a>

### [`00b832e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b832e4.md) → [`00bffd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd2c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b832e4.md#insn-00b83320)
- 新版 `00bffd68`（命令位置の公開資料なし）

~~~diff
- 00b83320 ["INT_ADD", "register:40f0:8", ["const:b83320:8", "const:4:8"]]
- 00b83320 ["CALL", null, ["callee:00c57de0:8"]]
+ 00bffd68 ["INT_ADD", "register:40f0:8", ["const:bffd68:8", "const:4:8"]]
+ 00bffd68 ["CALL", null, ["callee:00c57de0:8"]]
- 00b83320 bytes 1c600194
+ 00bffd68 bytes 1e600194
~~~


<a id="compare-54e166ab3171bc130903c39cca7ac753"></a>

### [`00b833d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b833d8.md) → [`00bffe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe20.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b833f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b833d8.md#insn-00b833f0)
- 新版 `00bffe38`（命令位置の公開資料なし）

~~~diff
- 00b833f0 ["INT_ADD", "register:40f0:8", ["const:b833f0:8", "const:4:8"]]
- 00b833f0 ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bffe38 ["INT_ADD", "register:40f0:8", ["const:bffe38:8", "const:4:8"]]
+ 00bffe38 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b833f0 bytes 7c730194
+ 00bffe38 bytes aa730194
~~~


<a id="compare-5a4efbc63f59bbb00aa27ff109676390"></a>

### [`00b83408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83408.md) → [`00bffe50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe50.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83408.md#insn-00b83428)
- 新版 `00bffe70`（命令位置の公開資料なし）

~~~diff
- 00b83428 ["INT_ADD", "register:40f0:8", ["const:b83428:8", "const:4:8"]]
- 00b83428 ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bffe70 ["INT_ADD", "register:40f0:8", ["const:bffe70:8", "const:4:8"]]
+ 00bffe70 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b83428 bytes 6e730194
+ 00bffe70 bytes 9c730194
~~~


<a id="compare-907af1d4a368929d37fa262ef61407d1"></a>

### [`00b83440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83440.md) → [`00bffe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffe88.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83440.md#insn-00b83478)
- 新版 `00bffec0`（命令位置の公開資料なし）

~~~diff
- 00b83478 ["INT_ADD", "register:40f0:8", ["const:b83478:8", "const:4:8"]]
- 00b83478 ["CALL", null, ["callee:00c5df20:8"]]
+ 00bffec0 ["INT_ADD", "register:40f0:8", ["const:bffec0:8", "const:4:8"]]
+ 00bffec0 ["CALL", null, ["callee:00c5df20:8"]]
- 00b83478 bytes aa770194
+ 00bffec0 bytes 18780194
~~~


<a id="compare-3ddfb4170b897adaff0b83d9984fd866"></a>

### [`00b8378c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8378c.md) → [`00c001d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c001d4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b837ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8378c.md#insn-00b837ac)
- 新版 `00c001f4`（命令位置の公開資料なし）

~~~diff
- 00b837ac ["COPY", "register:0:8", ["register:4008:8"]]
- 00b837ac ["INT_ADD", "register:40f0:8", ["const:b837ac:8", "const:4:8"]]
- 00b837ac ["CALLIND", null, ["register:0:8"]]
+ 00c001f4 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c001f4 ["INT_ADD", "register:40f0:8", ["const:c001f4:8", "const:4:8"]]
+ 00c001f4 ["CALLIND", null, ["register:0:8"]]
- 00b837ac bytes 20003fd6
+ 00c001f4 bytes 20003fd6
~~~


<a id="compare-1125e16f95a39b5e43991bc218073f26"></a>

### [`00b837c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837c4.md) → [`00c0020c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c0020c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b837e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837c4.md#insn-00b837e4)
- 新版 `00c0022c`（命令位置の公開資料なし）

~~~diff
- 00b837e4 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b837e4 ["INT_ADD", "register:40f0:8", ["const:b837e4:8", "const:4:8"]]
- 00b837e4 ["CALLIND", null, ["register:0:8"]]
+ 00c0022c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c0022c ["INT_ADD", "register:40f0:8", ["const:c0022c:8", "const:4:8"]]
+ 00c0022c ["CALLIND", null, ["register:0:8"]]
- 00b837e4 bytes 20003fd6
+ 00c0022c bytes 20003fd6
~~~


<a id="compare-7e8bb7b3e3ea74d10545ffdf7e311cb5"></a>

### [`00b837fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md) → [`00c00244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00244.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8382c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b8382c) · [`00b83890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b83890) · [`00b838c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b838c4)
- 新版 `00c00274`（命令位置の公開資料なし） · `00c002d8`（命令位置の公開資料なし） · `00c0030c`（命令位置の公開資料なし）

~~~diff
- 00b8382c ["INT_ADD", "register:40f0:8", ["const:b8382c:8", "const:4:8"]]
- 00b8382c ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00274 ["INT_ADD", "register:40f0:8", ["const:c00274:8", "const:4:8"]]
+ 00c00274 ["CALL", null, ["callee:00c5e020:8"]]
- 00b8382c bytes fd760194
+ 00c00274 bytes 6b770194
- 00b83890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83890 ["INT_ADD", "register:40f0:8", ["const:b83890:8", "const:4:8"]]
- 00b83890 ["CALLIND", null, ["register:0:8"]]
+ 00c002d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c002d8 ["INT_ADD", "register:40f0:8", ["const:c002d8:8", "const:4:8"]]
+ 00c002d8 ["CALLIND", null, ["register:0:8"]]
- 00b83890 bytes 00013fd6
+ 00c002d8 bytes 00013fd6
- 00b838c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b838c4 ["INT_ADD", "register:40f0:8", ["const:b838c4:8", "const:4:8"]]
- 00b838c4 ["CALLIND", null, ["register:0:8"]]
+ 00c0030c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0030c ["INT_ADD", "register:40f0:8", ["const:c0030c:8", "const:4:8"]]
+ 00c0030c ["CALLIND", null, ["register:0:8"]]
- 00b838c4 bytes 00013fd6
+ 00c0030c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dbc9380b714e75aa57d8b14c497da13"></a>

### [`00b84a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md) → [`00c01450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01450.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1430.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c5e030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e030.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84a30) · [`00b84a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84a88) · [`00b84ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84ab0)
- 新版 `00c01478`（命令位置の公開資料なし） · `00c014d0`（命令位置の公開資料なし） · `00c014f8`（命令位置の公開資料なし）

~~~diff
- 00b84a30 ["INT_ADD", "register:40f0:8", ["const:b84a30:8", "const:4:8"]]
- 00b84a30 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01478 ["INT_ADD", "register:40f0:8", ["const:c01478:8", "const:4:8"]]
+ 00c01478 ["CALL", null, ["callee:00c5e020:8"]]
- 00b84a30 bytes 7c720194
+ 00c01478 bytes ea720194
- 00b84a88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84a88 ["INT_ADD", "register:40f0:8", ["const:b84a88:8", "const:4:8"]]
- 00b84a88 ["CALLIND", null, ["register:0:8"]]
+ 00c014d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c014d0 ["INT_ADD", "register:40f0:8", ["const:c014d0:8", "const:4:8"]]
+ 00c014d0 ["CALLIND", null, ["register:0:8"]]
- 00b84a88 bytes 00013fd6
+ 00c014d0 bytes 00013fd6
- 00b84ab0 ["INT_ADD", "register:40f0:8", ["const:b84ab0:8", "const:4:8"]]
- 00b84ab0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c014f8 ["INT_ADD", "register:40f0:8", ["const:c014f8:8", "const:4:8"]]
+ 00c014f8 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b84ab0 bytes 685a0194
+ 00c014f8 bytes 6a5a0194
~~~


<a id="compare-dc7ff9c88e112637c942487b9286ee98"></a>

### [`00b84b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b20.md) → [`00c01568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01568.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b20.md#insn-00b84b38)
- 新版 `00c01580`（命令位置の公開資料なし）

~~~diff
- 00b84b38 ["INT_ADD", "register:40f0:8", ["const:b84b38:8", "const:4:8"]]
- 00b84b38 ["CALL", null, ["callee:00c5e030:8"]]
+ 00c01580 ["INT_ADD", "register:40f0:8", ["const:c01580:8", "const:4:8"]]
+ 00c01580 ["CALL", null, ["callee:00c5e030:8"]]
- 00b84b38 bytes 3e720194
+ 00c01580 bytes ac720194
~~~


<a id="compare-6ae0e5c133c610cde4b474b923b90d34"></a>

### [`00b84e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md) → [`00c018ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c018ac.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1450.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c5e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e050.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84e98) · [`00b84ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84ef8) · [`00b84f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84f34)
- 新版 `00c018e0`（命令位置の公開資料なし） · `00c01940`（命令位置の公開資料なし） · `00c0197c`（命令位置の公開資料なし）

~~~diff
- 00b84e98 ["INT_ADD", "register:40f0:8", ["const:b84e98:8", "const:4:8"]]
- 00b84e98 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c018e0 ["INT_ADD", "register:40f0:8", ["const:c018e0:8", "const:4:8"]]
+ 00c018e0 ["CALL", null, ["callee:00c5e020:8"]]
- 00b84e98 bytes 62710194
+ 00c018e0 bytes d0710194
- 00b84ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84ef8 ["INT_ADD", "register:40f0:8", ["const:b84ef8:8", "const:4:8"]]
- 00b84ef8 ["CALLIND", null, ["register:0:8"]]
+ 00c01940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01940 ["INT_ADD", "register:40f0:8", ["const:c01940:8", "const:4:8"]]
+ 00c01940 ["CALLIND", null, ["register:0:8"]]
- 00b84ef8 bytes 00013fd6
+ 00c01940 bytes 00013fd6
- 00b84f34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84f34 ["INT_ADD", "register:40f0:8", ["const:b84f34:8", "const:4:8"]]
- 00b84f34 ["CALLIND", null, ["register:0:8"]]
+ 00c0197c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0197c ["INT_ADD", "register:40f0:8", ["const:c0197c:8", "const:4:8"]]
+ 00c0197c ["CALLIND", null, ["register:0:8"]]
- 00b84f34 bytes 00013fd6
+ 00c0197c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62dfc59896a84ec0cd5d2bff7c0eded5"></a>

### [`00b8555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md) → [`00c01fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01fa4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b8558c) · [`00b855b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b855b8) · [`00b855e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b855e8)
- 新版 `00c01fd4`（命令位置の公開資料なし） · `00c02000`（命令位置の公開資料なし） · `00c02030`（命令位置の公開資料なし）

~~~diff
- 00b8558c ["INT_ADD", "register:40f0:8", ["const:b8558c:8", "const:4:8"]]
- 00b8558c ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01fd4 ["INT_ADD", "register:40f0:8", ["const:c01fd4:8", "const:4:8"]]
+ 00c01fd4 ["CALL", null, ["callee:00c5e020:8"]]
- 00b8558c bytes a56f0194
+ 00c01fd4 bytes 13700194
- 00b855b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b855b8 ["INT_ADD", "register:40f0:8", ["const:b855b8:8", "const:4:8"]]
- 00b855b8 ["CALLIND", null, ["register:0:8"]]
+ 00c02000 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02000 ["INT_ADD", "register:40f0:8", ["const:c02000:8", "const:4:8"]]
+ 00c02000 ["CALLIND", null, ["register:0:8"]]
- 00b855b8 bytes 00013fd6
+ 00c02000 bytes 00013fd6
- 00b855e8 ["INT_ADD", "register:40f0:8", ["const:b855e8:8", "const:4:8"]]
- 00b855e8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c02030 ["INT_ADD", "register:40f0:8", ["const:c02030:8", "const:4:8"]]
+ 00c02030 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b855e8 bytes 9a570194
+ 00c02030 bytes 9c570194
~~~


<a id="compare-508ccb47fa29523ea492f4ab6476fc87"></a>

### [`00b85654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md) → [`00c0209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c0209c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b85684) · [`00b856c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b856c8) · [`00b85714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b85714)
- 新版 `00c020cc`（命令位置の公開資料なし） · `00c02110`（命令位置の公開資料なし） · `00c0215c`（命令位置の公開資料なし）

~~~diff
- 00b85684 ["INT_ADD", "register:40f0:8", ["const:b85684:8", "const:4:8"]]
- 00b85684 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c020cc ["INT_ADD", "register:40f0:8", ["const:c020cc:8", "const:4:8"]]
+ 00c020cc ["CALL", null, ["callee:00c5e020:8"]]
- 00b85684 bytes 676f0194
+ 00c020cc bytes d56f0194
- 00b856c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b856c8 ["INT_ADD", "register:40f0:8", ["const:b856c8:8", "const:4:8"]]
- 00b856c8 ["CALLIND", null, ["register:0:8"]]
+ 00c02110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02110 ["INT_ADD", "register:40f0:8", ["const:c02110:8", "const:4:8"]]
+ 00c02110 ["CALLIND", null, ["register:0:8"]]
- 00b856c8 bytes 00013fd6
+ 00c02110 bytes 00013fd6
- 00b85714 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85714 ["INT_ADD", "register:40f0:8", ["const:b85714:8", "const:4:8"]]
- 00b85714 ["CALLIND", null, ["register:0:8"]]
+ 00c0215c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c0215c ["INT_ADD", "register:40f0:8", ["const:c0215c:8", "const:4:8"]]
+ 00c0215c ["CALLIND", null, ["register:0:8"]]
- 00b85714 bytes 20013fd6
+ 00c0215c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d37e41391221bed2c42b7fc3cadeb86"></a>

### [`00b857a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md) → [`00c021f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c021f0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b857e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b857e8) · [`00b857f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b857f8) · [`00b85854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b85854)
- 新版 `00c02230`（命令位置の公開資料なし） · `00c02240`（命令位置の公開資料なし） · `00c0229c`（命令位置の公開資料なし）

~~~diff
- 00b857e8 ["INT_ADD", "register:40f0:8", ["const:b857e8:8", "const:4:8"]]
- 00b857e8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c02230 ["INT_ADD", "register:40f0:8", ["const:c02230:8", "const:4:8"]]
+ 00c02230 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b857e8 bytes 1a570194
+ 00c02230 bytes 1c570194
- 00b857f8 ["INT_ADD", "register:40f0:8", ["const:b857f8:8", "const:4:8"]]
- 00b857f8 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c02240 ["INT_ADD", "register:40f0:8", ["const:c02240:8", "const:4:8"]]
+ 00c02240 ["CALL", null, ["callee:00c5e020:8"]]
- 00b857f8 bytes 0a6f0194
+ 00c02240 bytes 786f0194
- 00b85854 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85854 ["INT_ADD", "register:40f0:8", ["const:b85854:8", "const:4:8"]]
- 00b85854 ["CALLIND", null, ["register:0:8"]]
+ 00c0229c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0229c ["INT_ADD", "register:40f0:8", ["const:c0229c:8", "const:4:8"]]
+ 00c0229c ["CALLIND", null, ["register:0:8"]]
- 00b85854 bytes 00013fd6
+ 00c0229c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-048805ceb89bbbb4e69577cfafff151f"></a>

### [`00b858e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md) → [`00c02330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02330.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85924) · [`00b85934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85934) · [`00b85988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85988)
- 新版 `00c0236c`（命令位置の公開資料なし） · `00c0237c`（命令位置の公開資料なし） · `00c023d0`（命令位置の公開資料なし）

~~~diff
- 00b85924 ["INT_ADD", "register:40f0:8", ["const:b85924:8", "const:4:8"]]
- 00b85924 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c0236c ["INT_ADD", "register:40f0:8", ["const:c0236c:8", "const:4:8"]]
+ 00c0236c ["CALL", null, ["callee:00c57ea0:8"]]
- 00b85924 bytes cb560194
+ 00c0236c bytes cd560194
- 00b85934 ["INT_ADD", "register:40f0:8", ["const:b85934:8", "const:4:8"]]
- 00b85934 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c0237c ["INT_ADD", "register:40f0:8", ["const:c0237c:8", "const:4:8"]]
+ 00c0237c ["CALL", null, ["callee:00c5e020:8"]]
- 00b85934 bytes bb6e0194
+ 00c0237c bytes 296f0194
- 00b85988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85988 ["INT_ADD", "register:40f0:8", ["const:b85988:8", "const:4:8"]]
- 00b85988 ["CALLIND", null, ["register:0:8"]]
+ 00c023d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c023d0 ["INT_ADD", "register:40f0:8", ["const:c023d0:8", "const:4:8"]]
+ 00c023d0 ["CALLIND", null, ["register:0:8"]]
- 00b85988 bytes 00013fd6
+ 00c023d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e09590b8372327b601aff1f6ce82926"></a>

### [`00b85a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md) → [`00c02464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02464.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a40) · [`00b85a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a68) · [`00b85a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a8c)
- 新版 `00c02488`（命令位置の公開資料なし） · `00c024b0`（命令位置の公開資料なし） · `00c024d4`（命令位置の公開資料なし）

~~~diff
- 00b85a40 ["INT_ADD", "register:40f0:8", ["const:b85a40:8", "const:4:8"]]
- 00b85a40 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c02488 ["INT_ADD", "register:40f0:8", ["const:c02488:8", "const:4:8"]]
+ 00c02488 ["CALL", null, ["callee:00c5e020:8"]]
- 00b85a40 bytes 786e0194
+ 00c02488 bytes e66e0194
- 00b85a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85a68 ["INT_ADD", "register:40f0:8", ["const:b85a68:8", "const:4:8"]]
- 00b85a68 ["CALLIND", null, ["register:0:8"]]
+ 00c024b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c024b0 ["INT_ADD", "register:40f0:8", ["const:c024b0:8", "const:4:8"]]
+ 00c024b0 ["CALLIND", null, ["register:0:8"]]
- 00b85a68 bytes 00013fd6
+ 00c024b0 bytes 00013fd6
- 00b85a8c ["INT_ADD", "register:40f0:8", ["const:b85a8c:8", "const:4:8"]]
- 00b85a8c ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c024d4 ["INT_ADD", "register:40f0:8", ["const:c024d4:8", "const:4:8"]]
+ 00c024d4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b85a8c bytes 71560194
+ 00c024d4 bytes 73560194
~~~


<a id="compare-1e911e359bed6bb54319826ec88e6cc7"></a>

### [`00b85c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md) → [`00c02650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02650.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c44) · [`00b85c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c54) · [`00b85c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c84)
- 新版 `00c0268c`（命令位置の公開資料なし） · `00c0269c`（命令位置の公開資料なし） · `00c026cc`（命令位置の公開資料なし）

~~~diff
- 00b85c44 ["INT_ADD", "register:40f0:8", ["const:b85c44:8", "const:4:8"]]
- 00b85c44 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c0268c ["INT_ADD", "register:40f0:8", ["const:c0268c:8", "const:4:8"]]
+ 00c0268c ["CALL", null, ["callee:00c57ea0:8"]]
- 00b85c44 bytes 03560194
+ 00c0268c bytes 05560194
- 00b85c54 ["INT_ADD", "register:40f0:8", ["const:b85c54:8", "const:4:8"]]
- 00b85c54 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c0269c ["INT_ADD", "register:40f0:8", ["const:c0269c:8", "const:4:8"]]
+ 00c0269c ["CALL", null, ["callee:00c5e020:8"]]
- 00b85c54 bytes f36d0194
+ 00c0269c bytes 616e0194
- 00b85c84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85c84 ["INT_ADD", "register:40f0:8", ["const:b85c84:8", "const:4:8"]]
- 00b85c84 ["CALLIND", null, ["register:0:8"]]
+ 00c026cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c026cc ["INT_ADD", "register:40f0:8", ["const:c026cc:8", "const:4:8"]]
+ 00c026cc ["CALLIND", null, ["register:0:8"]]
- 00b85c84 bytes 00013fd6
+ 00c026cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cdf75a1032726dfe32bde9d1825177f"></a>

### [`00b85e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e28.md) → [`00c02870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02870.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e28.md#insn-00b85e60)
- 新版 `00c028a8`（命令位置の公開資料なし）

~~~diff
- 00b85e60 ["INT_ADD", "register:40f0:8", ["const:b85e60:8", "const:4:8"]]
- 00b85e60 ["CALL", null, ["callee:00c57de0:8"]]
+ 00c028a8 ["INT_ADD", "register:40f0:8", ["const:c028a8:8", "const:4:8"]]
+ 00c028a8 ["CALL", null, ["callee:00c57de0:8"]]
- 00b85e60 bytes 4c550194
+ 00c028a8 bytes 4e550194
~~~


<a id="compare-6968c362c230a9a1c14a417414ecb301"></a>

### [`00b85f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f48.md) → [`00c02990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02990.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f48.md#insn-00b85f68)
- 新版 `00c029b0`（命令位置の公開資料なし）

~~~diff
- 00b85f68 ["INT_ADD", "register:40f0:8", ["const:b85f68:8", "const:4:8"]]
- 00b85f68 ["CALL", null, ["callee:00c5cce0:8"]]
+ 00c029b0 ["INT_ADD", "register:40f0:8", ["const:c029b0:8", "const:4:8"]]
+ 00c029b0 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b85f68 bytes 9e680194
+ 00c029b0 bytes cc680194
~~~


<a id="compare-549b5424c7d18f6c750bcf22873b08fa"></a>

### [`00b85f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f80.md) → [`00c029c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c029c8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f80.md#insn-00b85fb0)
- 新版 `00c029f8`（命令位置の公開資料なし）

~~~diff
- 00b85fb0 ["INT_ADD", "register:40f0:8", ["const:b85fb0:8", "const:4:8"]]
- 00b85fb0 ["CALL", null, ["callee:00c5df20:8"]]
+ 00c029f8 ["INT_ADD", "register:40f0:8", ["const:c029f8:8", "const:4:8"]]
+ 00c029f8 ["CALL", null, ["callee:00c5df20:8"]]
- 00b85fb0 bytes dc6c0194
+ 00c029f8 bytes 4a6d0194
~~~


<a id="compare-7b1a7a93cff0f279166da498775585db"></a>

### [`00b85fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85fe4.md) → [`00c02a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a2c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) · 呼出先 1件 [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md)
- 新版 呼出元 1件 [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) · 呼出先 1件 [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85fe4.md#insn-00b86028)
- 新版 `00c02a70`（命令位置の公開資料なし）

~~~diff
- 00b86028 ["INT_ADD", "register:40f0:8", ["const:b86028:8", "const:4:8"]]
- 00b86028 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00c02a70 ["INT_ADD", "register:40f0:8", ["const:c02a70:8", "const:4:8"]]
+ 00c02a70 ["CALL", null, ["callee:00c5dff0:8"]]
- 00b86028 bytes f26c0194
+ 00c02a70 bytes 606d0194
~~~


<a id="compare-c5a1317587c0c68ea207adcd5d1ff98c"></a>

### [`00b86048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md) → [`00c02a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02a90.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)
- 新版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b86084) · [`00b860a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b860a8) · [`00b860cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b860cc)
- 新版 `00c02acc`（命令位置の公開資料なし） · `00c02af0`（命令位置の公開資料なし） · `00c02b14`（命令位置の公開資料なし）

~~~diff
- 00b86084 ["INT_ADD", "register:40f0:8", ["const:b86084:8", "const:4:8"]]
- 00b86084 ["CALL", null, ["callee:00c5ccf0:8"]]
+ 00c02acc ["INT_ADD", "register:40f0:8", ["const:c02acc:8", "const:4:8"]]
+ 00c02acc ["CALL", null, ["callee:00c5ccf0:8"]]
- 00b86084 bytes 5b680194
+ 00c02acc bytes 89680194
- 00b860a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b860a8 ["INT_ADD", "register:40f0:8", ["const:b860a8:8", "const:4:8"]]
- 00b860a8 ["CALLIND", null, ["register:0:8"]]
+ 00c02af0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02af0 ["INT_ADD", "register:40f0:8", ["const:c02af0:8", "const:4:8"]]
+ 00c02af0 ["CALLIND", null, ["register:0:8"]]
- 00b860a8 bytes 00013fd6
+ 00c02af0 bytes 00013fd6
- 00b860cc ["INT_ADD", "register:40f0:8", ["const:b860cc:8", "const:4:8"]]
- 00b860cc ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c02b14 ["INT_ADD", "register:40f0:8", ["const:c02b14:8", "const:4:8"]]
+ 00c02b14 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b860cc bytes e1540194
+ 00c02b14 bytes e3540194
~~~


<a id="compare-37c6abeca51d295b76f236bd5aa28f86"></a>

### [`00b860fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b860fc.md) → [`00c02b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02b44.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8611c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b860fc.md#insn-00b8611c)
- 新版 `00c02b64`（命令位置の公開資料なし）

~~~diff
- 00b8611c ["COPY", "register:0:8", ["register:4008:8"]]
- 00b8611c ["INT_ADD", "register:40f0:8", ["const:b8611c:8", "const:4:8"]]
- 00b8611c ["CALLIND", null, ["register:0:8"]]
+ 00c02b64 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c02b64 ["INT_ADD", "register:40f0:8", ["const:c02b64:8", "const:4:8"]]
+ 00c02b64 ["CALLIND", null, ["register:0:8"]]
- 00b8611c bytes 20003fd6
+ 00c02b64 bytes 20003fd6
~~~


<a id="compare-489398cdd5afe27aef8cb8c6d1111c17"></a>

### [`00b86134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86134.md) → [`00c02b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02b7c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86134.md#insn-00b86154)
- 新版 `00c02b9c`（命令位置の公開資料なし）

~~~diff
- 00b86154 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b86154 ["INT_ADD", "register:40f0:8", ["const:b86154:8", "const:4:8"]]
- 00b86154 ["CALLIND", null, ["register:0:8"]]
+ 00c02b9c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c02b9c ["INT_ADD", "register:40f0:8", ["const:c02b9c:8", "const:4:8"]]
+ 00c02b9c ["CALLIND", null, ["register:0:8"]]
- 00b86154 bytes 20003fd6
+ 00c02b9c bytes 20003fd6
~~~


<a id="compare-b881b2d878c51d07dd9fda6c6e27e05c"></a>

### [`00b879d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b879d4.md) → [`00c0441c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c0441c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5tellpEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b879d4.md#insn-00b87a24)
- 新版 `00c0446c`（命令位置の公開資料なし）

~~~diff
- 00b87a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87a24 ["INT_ADD", "register:40f0:8", ["const:b87a24:8", "const:4:8"]]
- 00b87a24 ["CALLIND", null, ["register:0:8"]]
+ 00c0446c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0446c ["INT_ADD", "register:40f0:8", ["const:c0446c:8", "const:4:8"]]
+ 00c0446c ["CALLIND", null, ["register:0:8"]]
- 00b87a24 bytes 00013fd6
+ 00c0446c bytes 00013fd6
~~~


<a id="compare-287b0aaf0ce9fa79f9ae03e6cb41a00e"></a>

### [`00b884b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md) → [`00c04f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04f00.md) _ZNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md) [`00c5e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b884fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md#insn-00b884fc) · [`00b88528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md#insn-00b88528)
- 新版 `00c04f44`（命令位置の公開資料なし） · `00c04f70`（命令位置の公開資料なし）

~~~diff
- 00b884fc ["INT_ADD", "register:40f0:8", ["const:b884fc:8", "const:4:8"]]
- 00b884fc ["CALL", null, ["callee:00c5df20:8"]]
+ 00c04f44 ["INT_ADD", "register:40f0:8", ["const:c04f44:8", "const:4:8"]]
+ 00c04f44 ["CALL", null, ["callee:00c5df20:8"]]
- 00b884fc bytes 89630194
+ 00c04f44 bytes f7630194
- 00b88528 ["INT_ADD", "register:40f0:8", ["const:b88528:8", "const:4:8"]]
- 00b88528 ["CALL", null, ["callee:00c5e070:8"]]
+ 00c04f70 ["INT_ADD", "register:40f0:8", ["const:c04f70:8", "const:4:8"]]
+ 00c04f70 ["CALL", null, ["callee:00c5e070:8"]]
- 00b88528 bytes d2630194
+ 00c04f70 bytes 40640194
~~~


<a id="compare-e70dcd527d3e4111cea3ac7182b4c02b"></a>

### [`00b88544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md) → [`00c04f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04f8c.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b8859c) · [`00b885ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b885ac) · [`00b885c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b885c8)
- 新版 `00c04fe4`（命令位置の公開資料なし） · `00c04ff4`（命令位置の公開資料なし） · `00c05010`（命令位置の公開資料なし）

~~~diff
- 00b8859c ["INT_ADD", "register:40f0:8", ["const:b8859c:8", "const:4:8"]]
- 00b8859c ["CALL", null, ["callee:00c059a4:8"]]
+ 00c04fe4 ["INT_ADD", "register:40f0:8", ["const:c04fe4:8", "const:4:8"]]
+ 00c04fe4 ["CALL", null, ["callee:00c059a4:8"]]
- 00b8859c bytes 70020094
+ 00c04fe4 bytes 70020094
- 00b885ac ["INT_ADD", "register:40f0:8", ["const:b885ac:8", "const:4:8"]]
- 00b885ac ["CALL", null, ["callee:00c59c90:8"]]
+ 00c04ff4 ["INT_ADD", "register:40f0:8", ["const:c04ff4:8", "const:4:8"]]
+ 00c04ff4 ["CALL", null, ["callee:00c59c90:8"]]
- 00b885ac bytes 25530194
+ 00c04ff4 bytes 27530194
- 00b885c8 ["INT_ADD", "register:40f0:8", ["const:b885c8:8", "const:4:8"]]
- 00b885c8 ["CALL", null, ["callee:00c59c60:8"]]
+ 00c05010 ["INT_ADD", "register:40f0:8", ["const:c05010:8", "const:4:8"]]
+ 00c05010 ["CALL", null, ["callee:00c59c60:8"]]
- 00b885c8 bytes 12530194
+ 00c05010 bytes 14530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f7c359abaa402254aabe322d004aea"></a>

### [`00b88760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md) → [`00c051a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c051a8.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b887c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887c4) · [`00b887d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887d4) · [`00b887f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887f0)
- 新版 `00c0520c`（命令位置の公開資料なし） · `00c0521c`（命令位置の公開資料なし） · `00c05238`（命令位置の公開資料なし）

~~~diff
- 00b887c4 ["INT_ADD", "register:40f0:8", ["const:b887c4:8", "const:4:8"]]
- 00b887c4 ["CALL", null, ["callee:00c059a4:8"]]
+ 00c0520c ["INT_ADD", "register:40f0:8", ["const:c0520c:8", "const:4:8"]]
+ 00c0520c ["CALL", null, ["callee:00c059a4:8"]]
- 00b887c4 bytes e6010094
+ 00c0520c bytes e6010094
- 00b887d4 ["INT_ADD", "register:40f0:8", ["const:b887d4:8", "const:4:8"]]
- 00b887d4 ["CALL", null, ["callee:00c59c90:8"]]
+ 00c0521c ["INT_ADD", "register:40f0:8", ["const:c0521c:8", "const:4:8"]]
+ 00c0521c ["CALL", null, ["callee:00c59c90:8"]]
- 00b887d4 bytes 9b520194
+ 00c0521c bytes 9d520194
- 00b887f0 ["INT_ADD", "register:40f0:8", ["const:b887f0:8", "const:4:8"]]
- 00b887f0 ["CALL", null, ["callee:00c59c60:8"]]
+ 00c05238 ["INT_ADD", "register:40f0:8", ["const:c05238:8", "const:4:8"]]
+ 00c05238 ["CALL", null, ["callee:00c59c60:8"]]
- 00b887f0 bytes 88520194
+ 00c05238 bytes 8a520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-029fc62154cca29c817869b672305b6d"></a>

### [`00b88ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md) → [`00c055f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c055f0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE5closeEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88bd0) · [`00b88bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88bdc) · [`00b88c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88c04)
- 新版 `00c05618`（命令位置の公開資料なし） · `00c05624`（命令位置の公開資料なし） · `00c0564c`（命令位置の公開資料なし）

~~~diff
- 00b88bd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88bd0 ["INT_ADD", "register:40f0:8", ["const:b88bd0:8", "const:4:8"]]
- 00b88bd0 ["CALLIND", null, ["register:0:8"]]
+ 00c05618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05618 ["INT_ADD", "register:40f0:8", ["const:c05618:8", "const:4:8"]]
+ 00c05618 ["CALLIND", null, ["register:0:8"]]
- 00b88bd0 bytes 00013fd6
+ 00c05618 bytes 00013fd6
- 00b88bdc ["INT_ADD", "register:40f0:8", ["const:b88bdc:8", "const:4:8"]]
- 00b88bdc ["CALL", null, ["callee:00c59c00:8"]]
+ 00c05624 ["INT_ADD", "register:40f0:8", ["const:c05624:8", "const:4:8"]]
+ 00c05624 ["CALL", null, ["callee:00c59c00:8"]]
- 00b88bdc bytes 75510194
+ 00c05624 bytes 77510194
- 00b88c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88c04 ["INT_ADD", "register:40f0:8", ["const:b88c04:8", "const:4:8"]]
- 00b88c04 ["CALLIND", null, ["register:0:8"]]
+ 00c0564c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0564c ["INT_ADD", "register:40f0:8", ["const:c0564c:8", "const:4:8"]]
+ 00c0564c ["CALLIND", null, ["register:0:8"]]
- 00b88c04 bytes 00013fd6
+ 00c0564c bytes 00013fd6
~~~


<a id="compare-c0ed894e4cf8cf1f73b7b1cd9d72c2d1"></a>

### [`00b899a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899a0.md) → [`00c063e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c063e8.md) FUN_00c063e8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b899b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899a0.md#insn-00b899b4)
- 新版 `00c063fc`（命令位置の公開資料なし）

~~~diff
- 00b899b4 ["INT_ADD", "register:40f0:8", ["const:b899b4:8", "const:4:8"]]
- 00b899b4 ["CALL", null, ["callee:00c57ba0:8"]]
+ 00c063fc ["INT_ADD", "register:40f0:8", ["const:c063fc:8", "const:4:8"]]
+ 00c063fc ["CALL", null, ["callee:00c57ba0:8"]]
- 00b899b4 bytes e7450194
+ 00c063fc bytes e9450194
~~~


<a id="compare-1101d0ed1410c9c2b096b2e2707a95e1"></a>

### [`00b89d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d34.md) → [`00c0677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0677c.md) FUN_00c0677c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d34.md#insn-00b89d48)
- 新版 `00c06790`（命令位置の公開資料なし）

~~~diff
- 00b89d48 ["INT_ADD", "register:40f0:8", ["const:b89d48:8", "const:4:8"]]
- 00b89d48 ["CALL", null, ["callee:00c57ba0:8"]]
+ 00c06790 ["INT_ADD", "register:40f0:8", ["const:c06790:8", "const:4:8"]]
+ 00c06790 ["CALL", null, ["callee:00c57ba0:8"]]
- 00b89d48 bytes 02450194
+ 00c06790 bytes 04450194
~~~


<a id="compare-24a46879606ea313df2013fa146c0360"></a>

### [`00b89dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md) → [`00c06804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06804.md) FUN_00c06804

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89df4) · [`00b89e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89e14) · [`00b89e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89e3c)
- 新版 `00c0683c`（命令位置の公開資料なし） · `00c0685c`（命令位置の公開資料なし） · `00c06884`（命令位置の公開資料なし）

~~~diff
- 00b89df4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89df4 ["INT_ADD", "register:40f0:8", ["const:b89df4:8", "const:4:8"]]
- 00b89df4 ["CALLIND", null, ["register:0:8"]]
+ 00c0683c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0683c ["INT_ADD", "register:40f0:8", ["const:c0683c:8", "const:4:8"]]
+ 00c0683c ["CALLIND", null, ["register:0:8"]]
- 00b89df4 bytes 00013fd6
+ 00c0683c bytes 00013fd6
- 00b89e14 ["INT_ADD", "register:40f0:8", ["const:b89e14:8", "const:4:8"]]
- 00b89e14 ["CALL", null, ["callee:00c59e20:8"]]
+ 00c0685c ["INT_ADD", "register:40f0:8", ["const:c0685c:8", "const:4:8"]]
+ 00c0685c ["CALL", null, ["callee:00c59e20:8"]]
- 00b89e14 bytes 6f4d0194
+ 00c0685c bytes 714d0194
- 00b89e3c ["INT_ADD", "register:40f0:8", ["const:b89e3c:8", "const:4:8"]]
- 00b89e3c ["CALL", null, ["callee:00c59db0:8"]]
+ 00c06884 ["INT_ADD", "register:40f0:8", ["const:c06884:8", "const:4:8"]]
+ 00c06884 ["CALL", null, ["callee:00c59db0:8"]]
- 00b89e3c bytes 494d0194
+ 00c06884 bytes 4b4d0194
~~~


<a id="compare-ea97657950ecd97143e88f6d2d42f8ca"></a>

### [`00b89e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89e60.md) → [`00c068a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c068a8.md) FUN_00c068a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89e60.md#insn-00b89ec8)
- 新版 `00c06910`（命令位置の公開資料なし）

~~~diff
- 00b89ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89ec8 ["INT_ADD", "register:40f0:8", ["const:b89ec8:8", "const:4:8"]]
- 00b89ec8 ["CALLIND", null, ["register:0:8"]]
+ 00c06910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06910 ["INT_ADD", "register:40f0:8", ["const:c06910:8", "const:4:8"]]
+ 00c06910 ["CALLIND", null, ["register:0:8"]]
- 00b89ec8 bytes 00013fd6
+ 00c06910 bytes 00013fd6
~~~


<a id="compare-c4d1c9d15db89ddfba1ec7469869023a"></a>

### [`00b89f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md) → [`00c0694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0694c.md) FUN_00c0694c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89f50) · [`00b89f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89f9c) · [`00b89fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89fd8)
- 新版 `00c06998`（命令位置の公開資料なし） · `00c069e4`（命令位置の公開資料なし） · `00c06a20`（命令位置の公開資料なし）

~~~diff
- 00b89f50 ["INT_ADD", "register:40f0:8", ["const:b89f50:8", "const:4:8"]]
- 00b89f50 ["CALL", null, ["callee:00c59e20:8"]]
+ 00c06998 ["INT_ADD", "register:40f0:8", ["const:c06998:8", "const:4:8"]]
+ 00c06998 ["CALL", null, ["callee:00c59e20:8"]]
- 00b89f50 bytes 204d0194
+ 00c06998 bytes 224d0194
- 00b89f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89f9c ["INT_ADD", "register:40f0:8", ["const:b89f9c:8", "const:4:8"]]
- 00b89f9c ["CALLIND", null, ["register:0:8"]]
+ 00c069e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c069e4 ["INT_ADD", "register:40f0:8", ["const:c069e4:8", "const:4:8"]]
+ 00c069e4 ["CALLIND", null, ["register:0:8"]]
- 00b89f9c bytes 00013fd6
+ 00c069e4 bytes 00013fd6
- 00b89fd8 ["INT_ADD", "register:40f0:8", ["const:b89fd8:8", "const:4:8"]]
- 00b89fd8 ["CALL", null, ["callee:00c59e20:8"]]
+ 00c06a20 ["INT_ADD", "register:40f0:8", ["const:c06a20:8", "const:4:8"]]
+ 00c06a20 ["CALL", null, ["callee:00c59e20:8"]]
- 00b89fd8 bytes fe4c0194
+ 00c06a20 bytes 004d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3b11a29ef00a625d07511b52d1d5382"></a>

### [`00b8a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md) → [`00c06b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06b40.md) FUN_00c06b40

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0a0.md) [`00c5e0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a138) · [`00b8a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a198) · [`00b8a1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a1e4)
- 新版 `00c06b80`（命令位置の公開資料なし） · `00c06be0`（命令位置の公開資料なし） · `00c06c2c`（命令位置の公開資料なし）

~~~diff
- 00b8a138 ["INT_ADD", "register:40f0:8", ["const:b8a138:8", "const:4:8"]]
- 00b8a138 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00c06b80 ["INT_ADD", "register:40f0:8", ["const:c06b80:8", "const:4:8"]]
+ 00c06b80 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00b8a138 bytes e25c0194
+ 00c06b80 bytes 505d0194
- 00b8a198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a198 ["INT_ADD", "register:40f0:8", ["const:b8a198:8", "const:4:8"]]
- 00b8a198 ["CALLIND", null, ["register:0:8"]]
+ 00c06be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06be0 ["INT_ADD", "register:40f0:8", ["const:c06be0:8", "const:4:8"]]
+ 00c06be0 ["CALLIND", null, ["register:0:8"]]
- 00b8a198 bytes 00013fd6
+ 00c06be0 bytes 00013fd6
- 00b8a1e4 ["INT_ADD", "register:40f0:8", ["const:b8a1e4:8", "const:4:8"]]
- 00b8a1e4 ["CALL", null, ["callee:00c5e0a0:8"]]
+ 00c06c2c ["INT_ADD", "register:40f0:8", ["const:c06c2c:8", "const:4:8"]]
+ 00c06c2c ["CALL", null, ["callee:00c5e0a0:8"]]
- 00b8a1e4 bytes af5c0194
+ 00c06c2c bytes 1d5d0194
~~~


<a id="compare-f2b57c8b769cd23ecee30c570baa826c"></a>

### [`00b8a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md) → [`00c06e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e90.md) FUN_00c06e90

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a480) · [`00b8a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a4a0) · [`00b8a4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a4c8)
- 新版 `00c06ec8`（命令位置の公開資料なし） · `00c06ee8`（命令位置の公開資料なし） · `00c06f10`（命令位置の公開資料なし）

~~~diff
- 00b8a480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a480 ["INT_ADD", "register:40f0:8", ["const:b8a480:8", "const:4:8"]]
- 00b8a480 ["CALLIND", null, ["register:0:8"]]
+ 00c06ec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06ec8 ["INT_ADD", "register:40f0:8", ["const:c06ec8:8", "const:4:8"]]
+ 00c06ec8 ["CALLIND", null, ["register:0:8"]]
- 00b8a480 bytes 00013fd6
+ 00c06ec8 bytes 00013fd6
- 00b8a4a0 ["INT_ADD", "register:40f0:8", ["const:b8a4a0:8", "const:4:8"]]
- 00b8a4a0 ["CALL", null, ["callee:00c59e20:8"]]
+ 00c06ee8 ["INT_ADD", "register:40f0:8", ["const:c06ee8:8", "const:4:8"]]
+ 00c06ee8 ["CALL", null, ["callee:00c59e20:8"]]
- 00b8a4a0 bytes cc4b0194
+ 00c06ee8 bytes ce4b0194
- 00b8a4c8 ["INT_ADD", "register:40f0:8", ["const:b8a4c8:8", "const:4:8"]]
- 00b8a4c8 ["CALL", null, ["callee:00c59db0:8"]]
+ 00c06f10 ["INT_ADD", "register:40f0:8", ["const:c06f10:8", "const:4:8"]]
+ 00c06f10 ["CALL", null, ["callee:00c59db0:8"]]
- 00b8a4c8 bytes a64b0194
+ 00c06f10 bytes a84b0194
~~~


<a id="compare-d9bf39ed85a25a6275832744290f5cbe"></a>

### [`00b8a4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a4ec.md) → [`00c06f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06f34.md) FUN_00c06f34

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a4ec.md#insn-00b8a554)
- 新版 `00c06f9c`（命令位置の公開資料なし）

~~~diff
- 00b8a554 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a554 ["INT_ADD", "register:40f0:8", ["const:b8a554:8", "const:4:8"]]
- 00b8a554 ["CALLIND", null, ["register:0:8"]]
+ 00c06f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06f9c ["INT_ADD", "register:40f0:8", ["const:c06f9c:8", "const:4:8"]]
+ 00c06f9c ["CALLIND", null, ["register:0:8"]]
- 00b8a554 bytes 00013fd6
+ 00c06f9c bytes 00013fd6
~~~


<a id="compare-61e74ecb0b573a53c882d46757612160"></a>

### [`00b8a590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md) → [`00c06fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06fd8.md) FUN_00c06fd8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md) [`00be14e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md) [`00c5e0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a5d0) · [`00b8a61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a61c) · [`00b8a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a658)
- 新版 `00c07018`（命令位置の公開資料なし） · `00c07064`（命令位置の公開資料なし） · `00c070a0`（命令位置の公開資料なし）

~~~diff
- 00b8a5d0 ["INT_ADD", "register:40f0:8", ["const:b8a5d0:8", "const:4:8"]]
- 00b8a5d0 ["CALL", null, ["callee:00c5e0e0:8"]]
+ 00c07018 ["INT_ADD", "register:40f0:8", ["const:c07018:8", "const:4:8"]]
+ 00c07018 ["CALL", null, ["callee:00c5e0e0:8"]]
- 00b8a5d0 bytes c45b0194
+ 00c07018 bytes 325c0194
- 00b8a61c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a61c ["INT_ADD", "register:40f0:8", ["const:b8a61c:8", "const:4:8"]]
- 00b8a61c ["CALLIND", null, ["register:0:8"]]
+ 00c07064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07064 ["INT_ADD", "register:40f0:8", ["const:c07064:8", "const:4:8"]]
+ 00c07064 ["CALLIND", null, ["register:0:8"]]
- 00b8a61c bytes 00013fd6
+ 00c07064 bytes 00013fd6
- 00b8a658 ["INT_ADD", "register:40f0:8", ["const:b8a658:8", "const:4:8"]]
- 00b8a658 ["CALL", null, ["callee:00c59e20:8"]]
+ 00c070a0 ["INT_ADD", "register:40f0:8", ["const:c070a0:8", "const:4:8"]]
+ 00c070a0 ["CALL", null, ["callee:00c59e20:8"]]
- 00b8a658 bytes 5e4b0194
+ 00c070a0 bytes 604b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c78fe64cc5ce62dc9e61a8b91c8c186c"></a>

### [`00b8a700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a700.md) → [`00c07148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07148.md) _ZNSt6__ndk17collateIcED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1500.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a700.md#insn-00b8a714)
- 新版 `00c0715c`（命令位置の公開資料なし）

~~~diff
- 00b8a714 ["INT_ADD", "register:40f0:8", ["const:b8a714:8", "const:4:8"]]
- 00b8a714 ["CALL", null, ["callee:00c5e100:8"]]
+ 00c0715c ["INT_ADD", "register:40f0:8", ["const:c0715c:8", "const:4:8"]]
+ 00c0715c ["CALL", null, ["callee:00c5e100:8"]]
- 00b8a714 bytes 7b5b0194
+ 00c0715c bytes e95b0194
~~~


<a id="compare-0af01d7d9eb76cdbd23b90e80922de2f"></a>

### [`00b8a790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md) → [`00c071d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c071d8.md) _ZNKSt6__ndk17collateIcE12do_transformEPKcS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a7f8) · [`00b8a820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a820) · [`00b8a848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a848)
- 新版 `00c07240`（命令位置の公開資料なし） · `00c07268`（命令位置の公開資料なし） · `00c07290`（命令位置の公開資料なし）

~~~diff
- 00b8a7f8 ["INT_ADD", "register:40f0:8", ["const:b8a7f8:8", "const:4:8"]]
- 00b8a7f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00c07240 ["INT_ADD", "register:40f0:8", ["const:c07240:8", "const:4:8"]]
+ 00c07240 ["CALL", null, ["callee:00c57a90:8"]]
- 00b8a7f8 bytes 12420194
+ 00c07240 bytes 14420194
- 00b8a820 ["INT_ADD", "register:40f0:8", ["const:b8a820:8", "const:4:8"]]
- 00b8a820 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c07268 ["INT_ADD", "register:40f0:8", ["const:c07268:8", "const:4:8"]]
+ 00c07268 ["CALL", null, ["callee:00c57c00:8"]]
- 00b8a820 bytes 64420194
+ 00c07268 bytes 66420194
- 00b8a848 ["INT_ADD", "register:40f0:8", ["const:b8a848:8", "const:4:8"]]
- 00b8a848 ["CALL", null, ["callee:0043b724:8"]]
+ 00c07290 ["INT_ADD", "register:40f0:8", ["const:c07290:8", "const:4:8"]]
+ 00c07290 ["CALL", null, ["callee:0043b724:8"]]
- 00b8a848 bytes f738e297
+ 00c07290 bytes 25d1e097
~~~


<a id="compare-e7c22fc163d56145c70bb2fb794b05ca"></a>

### [`00b8ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md) → [`00c094cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c094cc.md) FUN_00c094cc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8ca7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca7c.md) · 呼出先 6件 [`00bb9a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9a88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00c094c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c094c4.md) · 呼出先 6件 [`00c364d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8cad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8cad0) · [`00b8caec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8caec) · [`00b8cb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8cb7c)
- 新版 `00c09518`（命令位置の公開資料なし） · `00c09534`（命令位置の公開資料なし） · `00c095c4`（命令位置の公開資料なし）

~~~diff
- 00b8cad0 ["INT_ADD", "register:40f0:8", ["const:b8cad0:8", "const:4:8"]]
- 00b8cad0 ["CALL", null, ["callee:00c5e150:8"]]
+ 00c09518 ["INT_ADD", "register:40f0:8", ["const:c09518:8", "const:4:8"]]
+ 00c09518 ["CALL", null, ["callee:00c5e150:8"]]
- 00b8cad0 bytes a0520194
+ 00c09518 bytes 0e530194
- 00b8caec ["INT_ADD", "register:40f0:8", ["const:b8caec:8", "const:4:8"]]
- 00b8caec ["CALL", null, ["callee:00c5ba70:8"]]
+ 00c09534 ["INT_ADD", "register:40f0:8", ["const:c09534:8", "const:4:8"]]
+ 00c09534 ["CALL", null, ["callee:00c5ba70:8"]]
- 00b8caec bytes 35490194
+ 00c09534 bytes 4f490194
- 00b8cb7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8cb7c ["INT_ADD", "register:40f0:8", ["const:b8cb7c:8", "const:4:8"]]
- 00b8cb7c ["CALLIND", null, ["register:0:8"]]
+ 00c095c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c095c4 ["INT_ADD", "register:40f0:8", ["const:c095c4:8", "const:4:8"]]
+ 00c095c4 ["CALLIND", null, ["register:0:8"]]
- 00b8cb7c bytes 00013fd6
+ 00c095c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2312c32fcb1aae447b6e74e37cb50d1"></a>

### [`00b8d2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md) → [`00c09cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09cfc.md) FUN_00c09cfc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8d2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2ac.md) · 呼出先 6件 [`00bb9cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9cb8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00c09cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09cf4.md) · 呼出先 6件 [`00c36700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d300) · [`00b8d31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d31c) · [`00b8d3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d3ac)
- 新版 `00c09d48`（命令位置の公開資料なし） · `00c09d64`（命令位置の公開資料なし） · `00c09df4`（命令位置の公開資料なし）

~~~diff
- 00b8d300 ["INT_ADD", "register:40f0:8", ["const:b8d300:8", "const:4:8"]]
- 00b8d300 ["CALL", null, ["callee:00c5e150:8"]]
+ 00c09d48 ["INT_ADD", "register:40f0:8", ["const:c09d48:8", "const:4:8"]]
+ 00c09d48 ["CALL", null, ["callee:00c5e150:8"]]
- 00b8d300 bytes 94500194
+ 00c09d48 bytes 02510194
- 00b8d31c ["INT_ADD", "register:40f0:8", ["const:b8d31c:8", "const:4:8"]]
- 00b8d31c ["CALL", null, ["callee:00c5ba70:8"]]
+ 00c09d64 ["INT_ADD", "register:40f0:8", ["const:c09d64:8", "const:4:8"]]
+ 00c09d64 ["CALL", null, ["callee:00c5ba70:8"]]
- 00b8d31c bytes 29470194
+ 00c09d64 bytes 43470194
- 00b8d3ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8d3ac ["INT_ADD", "register:40f0:8", ["const:b8d3ac:8", "const:4:8"]]
- 00b8d3ac ["CALLIND", null, ["register:0:8"]]
+ 00c09df4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09df4 ["INT_ADD", "register:40f0:8", ["const:c09df4:8", "const:4:8"]]
+ 00c09df4 ["CALLIND", null, ["register:0:8"]]
- 00b8d3ac bytes 00013fd6
+ 00c09df4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c674824497ad5369f0eb9878ca77369b"></a>

### [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) → [`00c0a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) FUN_00c0a800

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1590.md)
- 新版 呼出元 2件 [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de1c) · [`00b8de38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de38) · [`00b8de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de48)
- 新版 `00c0a864`（命令位置の公開資料なし） · `00c0a880`（命令位置の公開資料なし） · `00c0a890`（命令位置の公開資料なし）

~~~diff
- 00b8de1c ["INT_ADD", "register:40f0:8", ["const:b8de1c:8", "const:4:8"]]
- 00b8de1c ["CALL", null, ["callee:00c5e170:8"]]
+ 00c0a864 ["INT_ADD", "register:40f0:8", ["const:c0a864:8", "const:4:8"]]
+ 00c0a864 ["CALL", null, ["callee:00c5e170:8"]]
- 00b8de1c bytes d94d0194
+ 00c0a864 bytes 434e0194
- 00b8de38 ["INT_ADD", "register:40f0:8", ["const:b8de38:8", "const:4:8"]]
- 00b8de38 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c0a880 ["INT_ADD", "register:40f0:8", ["const:c0a880:8", "const:4:8"]]
+ 00c0a880 ["CALL", null, ["callee:00c5e180:8"]]
- 00b8de38 bytes d64d0194
+ 00c0a880 bytes 404e0194
- 00b8de48 ["INT_ADD", "register:40f0:8", ["const:b8de48:8", "const:4:8"]]
- 00b8de48 ["CALL", null, ["callee:00c5e170:8"]]
+ 00c0a890 ["INT_ADD", "register:40f0:8", ["const:c0a890:8", "const:4:8"]]
+ 00c0a890 ["CALL", null, ["callee:00c5e170:8"]]
- 00b8de48 bytes ce4d0194
+ 00c0a890 bytes 384e0194
~~~


<a id="compare-d09569240942d01a8bf7391fa883d45a"></a>

### [`00b90328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md) → [`00c0cd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0cd70.md) FUN_00c0cd70

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b90320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90320.md) · 呼出先 6件 [`00bb9ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ba0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)
- 新版 呼出元 1件 [`00c0cd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0cd68.md) · 呼出先 6件 [`00c365e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b90374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90374) · [`00b90390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90390) · [`00b90410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90410)
- 新版 `00c0cdbc`（命令位置の公開資料なし） · `00c0cdd8`（命令位置の公開資料なし） · `00c0ce58`（命令位置の公開資料なし）

~~~diff
- 00b90374 ["INT_ADD", "register:40f0:8", ["const:b90374:8", "const:4:8"]]
- 00b90374 ["CALL", null, ["callee:00c5e1b0:8"]]
+ 00c0cdbc ["INT_ADD", "register:40f0:8", ["const:c0cdbc:8", "const:4:8"]]
+ 00c0cdbc ["CALL", null, ["callee:00c5e1b0:8"]]
- 00b90374 bytes 93440194
+ 00c0cdbc bytes fd440194
- 00b90390 ["INT_ADD", "register:40f0:8", ["const:b90390:8", "const:4:8"]]
- 00b90390 ["CALL", null, ["callee:00c5ba70:8"]]
+ 00c0cdd8 ["INT_ADD", "register:40f0:8", ["const:c0cdd8:8", "const:4:8"]]
+ 00c0cdd8 ["CALL", null, ["callee:00c5ba70:8"]]
- 00b90390 bytes 0c3b0194
+ 00c0cdd8 bytes 263b0194
- 00b90410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b90410 ["INT_ADD", "register:40f0:8", ["const:b90410:8", "const:4:8"]]
- 00b90410 ["CALLIND", null, ["register:0:8"]]
+ 00c0ce58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0ce58 ["INT_ADD", "register:40f0:8", ["const:c0ce58:8", "const:4:8"]]
+ 00c0ce58 ["CALLIND", null, ["register:0:8"]]
- 00b90410 bytes 00013fd6
+ 00c0ce58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c20dc3faf7d5ab6ce72c4c46b32570d"></a>

### [`00b97288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md) → [`00c13cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13cd0.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b972b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md#insn-00b972b4)
- 新版 `00c13cfc`（命令位置の公開資料なし）

~~~diff
- 00b972b4 ["INT_ADD", "register:40f0:8", ["const:b972b4:8", "const:4:8"]]
- 00b972b4 ["CALL", null, ["callee:00c14484:8"]]
+ 00c13cfc ["INT_ADD", "register:40f0:8", ["const:c13cfc:8", "const:4:8"]]
+ 00c13cfc ["CALL", null, ["callee:00c14484:8"]]
- 00b972b4 bytes e2010094
+ 00c13cfc bytes e2010094
~~~


<a id="compare-bec61be763a1f2de654fe5de1c384dc1"></a>

### [`00b97410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97410.md) → [`00c13e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13e58.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9743c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97410.md#insn-00b9743c)
- 新版 `00c13e84`（命令位置の公開資料なし）

~~~diff
- 00b9743c ["INT_ADD", "register:40f0:8", ["const:b9743c:8", "const:4:8"]]
- 00b9743c ["CALL", null, ["callee:00c14484:8"]]
+ 00c13e84 ["INT_ADD", "register:40f0:8", ["const:c13e84:8", "const:4:8"]]
+ 00c13e84 ["CALL", null, ["callee:00c14484:8"]]
- 00b9743c bytes 80010094
+ 00c13e84 bytes 80010094
~~~


<a id="compare-8d77ad3d6f8e3729be43e961f34e8143"></a>

### [`00b97740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97740.md) → [`00c14188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14188.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97740.md#insn-00b9776c)
- 新版 `00c141b4`（命令位置の公開資料なし）

~~~diff
- 00b9776c ["INT_ADD", "register:40f0:8", ["const:b9776c:8", "const:4:8"]]
- 00b9776c ["CALL", null, ["callee:00c14484:8"]]
+ 00c141b4 ["INT_ADD", "register:40f0:8", ["const:c141b4:8", "const:4:8"]]
+ 00c141b4 ["CALL", null, ["callee:00c14484:8"]]
- 00b9776c bytes b4000094
+ 00c141b4 bytes b4000094
~~~


