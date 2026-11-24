# v16.0.2 → v16.0.3 · 要調査の変更候補 (43)

[一覧の目次](README.md)

<a id="compare-74f2fb5d62e40c0144abdfef6ba03002"></a>

### [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) → [`00c55070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md) FUN_00c55070

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) · 呼出先 4件 [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) [`00c54464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54464.md) [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md) [`00c544b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544b8.md)
- 新版 呼出元 1件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) · 呼出先 4件 [`00c55230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md) [`00c55454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55454.md) [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md) [`00c554a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c540b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md#insn-00c540b0) · [`00c540b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md#insn-00c540b8) · [`00c540dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md#insn-00c540dc)
- 新版 [`00c550a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md#insn-00c550a0) · [`00c550a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md#insn-00c550a8) · [`00c550cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md#insn-00c550cc)

~~~diff
- 00c540b0 ["INT_ADD", "register:40f0:8", ["const:c540b0:8", "const:4:8"]]
- 00c540b0 ["CALL", null, ["callee:00c55230:8"]]
+ 00c550a0 ["INT_ADD", "register:40f0:8", ["const:c550a0:8", "const:4:8"]]
+ 00c550a0 ["CALL", null, ["callee:00c55230:8"]]
- 00c540b0 bytes 64000094
+ 00c550a0 bytes 64000094
- 00c540b8 ["INT_ADD", "register:40f0:8", ["const:c540b8:8", "const:4:8"]]
- 00c540b8 ["CALL", null, ["callee:00c55454:8"]]
+ 00c550a8 ["INT_ADD", "register:40f0:8", ["const:c550a8:8", "const:4:8"]]
+ 00c550a8 ["CALL", null, ["callee:00c55454:8"]]
- 00c540b8 bytes eb000094
+ 00c550a8 bytes eb000094
- 00c540dc ["COPY", "register:0:8", ["register:4098:8"]]
- 00c540dc ["INT_ADD", "register:40f0:8", ["const:c540dc:8", "const:4:8"]]
- 00c540dc ["CALLIND", null, ["register:0:8"]]
+ 00c550cc ["COPY", "register:0:8", ["register:4098:8"]]
+ 00c550cc ["INT_ADD", "register:40f0:8", ["const:c550cc:8", "const:4:8"]]
+ 00c550cc ["CALLIND", null, ["register:0:8"]]
- 00c540dc bytes 60023fd6
+ 00c550cc bytes 60023fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a493453d0828545cfbedc5504660559"></a>

### [`00c54174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54174.md) → [`00c55164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55164.md) FUN_00c55164

採用 · 移動量 `+0xff0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) · 呼出先 1件 [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md)
- 新版 呼出元 1件 [`00c539d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md) · 呼出先 1件 [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54174.md#insn-00c54188)
- 新版 [`00c55178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55164.md#insn-00c55178)

~~~diff
- 00c54188 ["INT_ADD", "register:40f0:8", ["const:c54188:8", "const:4:8"]]
- 00c54188 ["CALL", null, ["callee:00c55468:8"]]
+ 00c55178 ["INT_ADD", "register:40f0:8", ["const:c55178:8", "const:4:8"]]
+ 00c55178 ["CALL", null, ["callee:00c55468:8"]]
- 00c54188 bytes bc000094
+ 00c55178 bytes bc000094
~~~


<a id="compare-6c2ef0fa7e14bc03caddb712daa66395"></a>

### [`00c541a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541a8.md) → [`00c55198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55198.md) FUN_00c55198

採用 · 移動量 `+0xff0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) · 呼出先 1件 [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md)
- 新版 呼出元 1件 [`00c539d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md) · 呼出先 1件 [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c541bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541a8.md#insn-00c541bc)
- 新版 [`00c551ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55198.md#insn-00c551ac)

~~~diff
- 00c541bc ["INT_ADD", "register:40f0:8", ["const:c541bc:8", "const:4:8"]]
- 00c541bc ["CALL", null, ["callee:00c55468:8"]]
+ 00c551ac ["INT_ADD", "register:40f0:8", ["const:c551ac:8", "const:4:8"]]
+ 00c551ac ["CALL", null, ["callee:00c55468:8"]]
- 00c541bc bytes af000094
+ 00c551ac bytes af000094
~~~


<a id="compare-9cda09bef201094cfc7d628a0baa1d6d"></a>

### [`00c54200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54200.md) → [`00c551f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c551f0.md) FUN_00c551f0

採用 · 移動量 `+0xff0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) · 呼出先 1件 [`00c542e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md)
- 新版 呼出元 1件 [`00c539d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md) · 呼出先 1件 [`00c552d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54200.md#insn-00c54218)
- 新版 [`00c55208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c551f0.md#insn-00c55208)

~~~diff
- 00c54218 ["INT_ADD", "register:40f0:8", ["const:c54218:8", "const:4:8"]]
- 00c54218 ["CALL", null, ["callee:00c552d8:8"]]
+ 00c55208 ["INT_ADD", "register:40f0:8", ["const:c55208:8", "const:4:8"]]
+ 00c55208 ["CALL", null, ["callee:00c552d8:8"]]
- 00c54218 bytes 34000094
+ 00c55208 bytes 34000094
~~~


<a id="compare-d6cdcefad8c32ab6954f625bc6c08bb7"></a>

### [`00c542e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md) → [`00c552d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md) FUN_00c552d8

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54200.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c551f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c551f0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md#insn-00c54310) · [`00c54328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md#insn-00c54328)
- 新版 [`00c55300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md#insn-00c55300) · [`00c55318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md#insn-00c55318)

~~~diff
- 00c54310 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54310 ["INT_ADD", "register:40f0:8", ["const:c54310:8", "const:4:8"]]
- 00c54310 ["CALLIND", null, ["register:0:8"]]
+ 00c55300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c55300 ["INT_ADD", "register:40f0:8", ["const:c55300:8", "const:4:8"]]
+ 00c55300 ["CALLIND", null, ["register:0:8"]]
- 00c54310 bytes 00013fd6
+ 00c55300 bytes 00013fd6
- 00c54328 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54328 ["INT_ADD", "register:40f0:8", ["const:c54328:8", "const:4:8"]]
- 00c54328 ["CALLIND", null, ["register:0:8"]]
+ 00c55318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c55318 ["INT_ADD", "register:40f0:8", ["const:c55318:8", "const:4:8"]]
+ 00c55318 ["CALLIND", null, ["register:0:8"]]
- 00c54328 bytes 00013fd6
+ 00c55318 bytes 00013fd6
~~~


<a id="compare-121c013dd681d3e3677a483075b3666a"></a>

### [`00c54364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54364.md) → [`00c55354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55354.md) FUN_00c55354

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c541f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541f8.md) [`00c54230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54230.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c551e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c551e8.md) [`00c55220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55220.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54364.md#insn-00c54390) · [`00c543ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54364.md#insn-00c543ac) · [`00c543c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54364.md#insn-00c543c8)
- 新版 [`00c55380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55354.md#insn-00c55380) · [`00c5539c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55354.md#insn-00c5539c) · [`00c553b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55354.md#insn-00c553b8)

~~~diff
- 00c54390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54390 ["INT_ADD", "register:40f0:8", ["const:c54390:8", "const:4:8"]]
- 00c54390 ["CALLIND", null, ["register:0:8"]]
+ 00c55380 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c55380 ["INT_ADD", "register:40f0:8", ["const:c55380:8", "const:4:8"]]
+ 00c55380 ["CALLIND", null, ["register:0:8"]]
- 00c54390 bytes 00013fd6
+ 00c55380 bytes 00013fd6
- 00c543ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00c543ac ["INT_ADD", "register:40f0:8", ["const:c543ac:8", "const:4:8"]]
- 00c543ac ["CALLIND", null, ["register:0:8"]]
+ 00c5539c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5539c ["INT_ADD", "register:40f0:8", ["const:c5539c:8", "const:4:8"]]
+ 00c5539c ["CALLIND", null, ["register:0:8"]]
- 00c543ac bytes 00013fd6
+ 00c5539c bytes 00013fd6
- 00c543c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c543c8 ["INT_ADD", "register:40f0:8", ["const:c543c8:8", "const:4:8"]]
- 00c543c8 ["CALLIND", null, ["register:0:8"]]
+ 00c553b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c553b8 ["INT_ADD", "register:40f0:8", ["const:c553b8:8", "const:4:8"]]
+ 00c553b8 ["CALLIND", null, ["register:0:8"]]
- 00c543c8 bytes 00013fd6
+ 00c553b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c768445a02933c2a2910f451bf1d2a8"></a>

### [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md) → [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md) FUN_00c55468

採用 · 移動量 `+0xff0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) [`00c54174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54174.md) [`00c541a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541a8.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c55070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md) [`00c55164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55164.md) [`00c55198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55198.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md#insn-00c54494)
- 新版 [`00c55484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md#insn-00c55484)

~~~diff
- 00c54494 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54494 ["INT_ADD", "register:40f0:8", ["const:c54494:8", "const:4:8"]]
- 00c54494 ["CALLIND", null, ["register:0:8"]]
+ 00c55484 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c55484 ["INT_ADD", "register:40f0:8", ["const:c55484:8", "const:4:8"]]
+ 00c55484 ["CALLIND", null, ["register:0:8"]]
- 00c54494 bytes 00013fd6
+ 00c55484 bytes 00013fd6
~~~


<a id="compare-9075238ee1d99242fcc9b7538d575e83"></a>

### [`00c544b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544b8.md) → [`00c554a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554a8.md) FUN_00c554a8

採用 · 移動量 `+0xff0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c55070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c544cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544b8.md#insn-00c544cc)
- 新版 [`00c554bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554a8.md#insn-00c554bc)

~~~diff
- 00c544cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c544cc ["INT_ADD", "register:40f0:8", ["const:c544cc:8", "const:4:8"]]
- 00c544cc ["CALLIND", null, ["register:0:8"]]
+ 00c554bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c554bc ["INT_ADD", "register:40f0:8", ["const:c554bc:8", "const:4:8"]]
+ 00c554bc ["CALLIND", null, ["register:0:8"]]
- 00c544cc bytes 00013fd6
+ 00c554bc bytes 00013fd6
~~~


<a id="compare-12c408e3ca8311860088c9f72882bdf8"></a>

### [`00c54b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md) → [`00c55b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55b80.md) FUN_00c55b80

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c54f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54f50.md) [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c55f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55f40.md) [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md#insn-00c54bd4) · [`00c54be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md#insn-00c54be0) · [`00c54c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md#insn-00c54c18)
- 新版 [`00c55bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55b80.md#insn-00c55bc4) · [`00c55bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55b80.md#insn-00c55bd0) · [`00c55c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55b80.md#insn-00c55c08)

~~~diff
- 00c54bd4 ["INT_ADD", "register:40f0:8", ["const:c54bd4:8", "const:4:8"]]
- 00c54bd4 ["CALL", null, ["callee:00c59130:8"]]
+ 00c55bc4 ["INT_ADD", "register:40f0:8", ["const:c55bc4:8", "const:4:8"]]
+ 00c55bc4 ["CALL", null, ["callee:00c59130:8"]]
- 00c54bd4 bytes 630d0094
+ 00c55bc4 bytes 5b0d0094
- 00c54be0 ["INT_ADD", "register:40f0:8", ["const:c54be0:8", "const:4:8"]]
- 00c54be0 ["CALL", null, ["callee:00c55f40:8"]]
+ 00c55bd0 ["INT_ADD", "register:40f0:8", ["const:c55bd0:8", "const:4:8"]]
+ 00c55bd0 ["CALL", null, ["callee:00c55f40:8"]]
- 00c54be0 bytes dc000094
+ 00c55bd0 bytes dc000094
- 00c54c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54c18 ["INT_ADD", "register:40f0:8", ["const:c54c18:8", "const:4:8"]]
- 00c54c18 ["CALLIND", null, ["register:0:8"]]
+ 00c55c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c55c08 ["INT_ADD", "register:40f0:8", ["const:c55c08:8", "const:4:8"]]
+ 00c55c08 ["CALLIND", null, ["register:0:8"]]
- 00c54c18 bytes 00013fd6
+ 00c55c08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d28c2e818fd379f0545b9948eb5bd7"></a>

### [`00c575ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md) → [`00c5859c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c5859c.md) FUN_00c5859c

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) · 呼出先 1件 [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md)
- 新版 呼出元 1件 [`00c55cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md) · 呼出先 1件 [`00c586cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c576bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md#insn-00c576bc)
- 新版 [`00c586ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c5859c.md#insn-00c586ac)

~~~diff
- 00c576bc ["INT_ADD", "register:40f0:8", ["const:c576bc:8", "const:4:8"]]
- 00c576bc ["CALL", null, ["callee:00c586cc:8"]]
+ 00c586ac ["INT_ADD", "register:40f0:8", ["const:c586ac:8", "const:4:8"]]
+ 00c586ac ["CALL", null, ["callee:00c586cc:8"]]
- 00c576bc bytes 08000094
+ 00c586ac bytes 08000094
~~~


<a id="compare-a6785738a2b5f6b83cd45a03b3596974"></a>

### [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) → [`00c587ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md) FUN_00c587ec

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) · 呼出先 3件 [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md)
- 新版 呼出元 1件 [`00c582c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md) · 呼出先 3件 [`00c55660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md) [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c578b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md#insn-00c578b4) · [`00c578dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md#insn-00c578dc) · [`00c578fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md#insn-00c578fc)
- 新版 [`00c588a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md#insn-00c588a4) · [`00c588cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md#insn-00c588cc) · [`00c588ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md#insn-00c588ec)

~~~diff
- 00c578b4 ["INT_ADD", "register:40f0:8", ["const:c578b4:8", "const:4:8"]]
- 00c578b4 ["CALL", null, ["callee:00c55660:8"]]
+ 00c588a4 ["INT_ADD", "register:40f0:8", ["const:c588a4:8", "const:4:8"]]
+ 00c588a4 ["CALL", null, ["callee:00c55660:8"]]
- 00c578b4 bytes 6ff3ff97
+ 00c588a4 bytes 6ff3ff97
- 00c578dc ["INT_ADD", "register:40f0:8", ["const:c578dc:8", "const:4:8"]]
- 00c578dc ["CALL", null, ["callee:00c573b0:8"]]
+ 00c588cc ["INT_ADD", "register:40f0:8", ["const:c588cc:8", "const:4:8"]]
+ 00c588cc ["CALL", null, ["callee:00c573b0:8"]]
- 00c578dc bytes b9faff97
+ 00c588cc bytes b9faff97
- 00c578fc ["INT_ADD", "register:40f0:8", ["const:c578fc:8", "const:4:8"]]
- 00c578fc ["CALL", null, ["callee:00c573b0:8"]]
+ 00c588ec ["INT_ADD", "register:40f0:8", ["const:c588ec:8", "const:4:8"]]
+ 00c588ec ["CALL", null, ["callee:00c573b0:8"]]
- 00c578fc bytes b1faff97
+ 00c588ec bytes b1faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da0ddb388520fedcc07c85bc70b1021f"></a>

### [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) → [`00c589b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md) FUN_00c589b4

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) · 呼出先 4件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md) [`00c57b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md)
- 新版 呼出元 1件 [`00c582c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md) · 呼出先 4件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c586cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md) [`00c58b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58b1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c57a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md#insn-00c57a0c) · [`00c57a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md#insn-00c57a24) · [`00c57a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md#insn-00c57a68)
- 新版 [`00c589fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md#insn-00c589fc) · [`00c58a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md#insn-00c58a14) · [`00c58a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md#insn-00c58a58)

~~~diff
- 00c57a0c ["INT_ADD", "register:40f0:8", ["const:c57a0c:8", "const:4:8"]]
- 00c57a0c ["CALL", null, ["callee:00c586cc:8"]]
+ 00c589fc ["INT_ADD", "register:40f0:8", ["const:c589fc:8", "const:4:8"]]
+ 00c589fc ["CALL", null, ["callee:00c586cc:8"]]
- 00c57a0c bytes 34ffff97
+ 00c589fc bytes 34ffff97
- 00c57a24 ["INT_ADD", "register:40f0:8", ["const:c57a24:8", "const:4:8"]]
- 00c57a24 ["CALL", null, ["callee:00c58b1c:8"]]
+ 00c58a14 ["INT_ADD", "register:40f0:8", ["const:c58a14:8", "const:4:8"]]
+ 00c58a14 ["CALL", null, ["callee:00c58b1c:8"]]
- 00c57a24 bytes 42000094
+ 00c58a14 bytes 42000094
- 00c57a68 ["INT_ADD", "register:40f0:8", ["const:c57a68:8", "const:4:8"]]
- 00c57a68 ["CALL", null, ["callee:00c573b0:8"]]
+ 00c58a58 ["INT_ADD", "register:40f0:8", ["const:c58a58:8", "const:4:8"]]
+ 00c58a58 ["CALL", null, ["callee:00c573b0:8"]]
- 00c57a68 bytes 56faff97
+ 00c58a58 bytes 56faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

