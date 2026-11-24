# v16.0.2 → v16.0.3 · 要調査の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-7b4e86a911ba71fb76409fdc78ba7bc6"></a>

### [`00883ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883ffc.md) → [`00884fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884fa8.md) FUN_00884fa8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883ffc.md#insn-00884038) · [`0088404c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883ffc.md#insn-0088404c) · [`0088406c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883ffc.md#insn-0088406c)
- 新版 [`00884fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884fa8.md#insn-00884fe4) · [`00884ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884fa8.md#insn-00884ff8) · [`00885018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884fa8.md#insn-00885018)

~~~diff
- 00884038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884038 ["INT_ADD", "register:40f0:8", ["const:884038:8", "const:4:8"]]
- 00884038 ["CALLIND", null, ["register:0:8"]]
+ 00884fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884fe4 ["INT_ADD", "register:40f0:8", ["const:884fe4:8", "const:4:8"]]
+ 00884fe4 ["CALLIND", null, ["register:0:8"]]
- 00884038 bytes 00013fd6
+ 00884fe4 bytes 00013fd6
- 0088404c ["INT_ADD", "register:40f0:8", ["const:88404c:8", "const:4:8"]]
- 0088404c ["CALL", null, ["callee:00c54d90:8"]]
+ 00884ff8 ["INT_ADD", "register:40f0:8", ["const:884ff8:8", "const:4:8"]]
+ 00884ff8 ["CALL", null, ["callee:00c54d90:8"]]
- 0088404c bytes 553f0f94
+ 00884ff8 bytes 663f0f94
- 0088406c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088406c ["INT_ADD", "register:40f0:8", ["const:88406c:8", "const:4:8"]]
- 0088406c ["CALLIND", null, ["register:0:8"]]
+ 00885018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885018 ["INT_ADD", "register:40f0:8", ["const:885018:8", "const:4:8"]]
+ 00885018 ["CALLIND", null, ["register:0:8"]]
- 0088406c bytes 00013fd6
+ 00885018 bytes 00013fd6
~~~


<a id="compare-dae2c91a03ede6e4f4e162483f5bf745"></a>

### [`00884080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884080.md) → [`0088502c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088502c.md) FUN_0088502c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008840bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884080.md#insn-008840bc) · [`008840d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884080.md#insn-008840d0) · [`008840f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884080.md#insn-008840f0)
- 新版 [`00885068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088502c.md#insn-00885068) · [`0088507c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088502c.md#insn-0088507c) · [`0088509c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088502c.md#insn-0088509c)

~~~diff
- 008840bc ["COPY", "register:0:8", ["register:4040:8"]]
- 008840bc ["INT_ADD", "register:40f0:8", ["const:8840bc:8", "const:4:8"]]
- 008840bc ["CALLIND", null, ["register:0:8"]]
+ 00885068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885068 ["INT_ADD", "register:40f0:8", ["const:885068:8", "const:4:8"]]
+ 00885068 ["CALLIND", null, ["register:0:8"]]
- 008840bc bytes 00013fd6
+ 00885068 bytes 00013fd6
- 008840d0 ["INT_ADD", "register:40f0:8", ["const:8840d0:8", "const:4:8"]]
- 008840d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088507c ["INT_ADD", "register:40f0:8", ["const:88507c:8", "const:4:8"]]
+ 0088507c ["CALL", null, ["callee:00c54d90:8"]]
- 008840d0 bytes 343f0f94
+ 0088507c bytes 453f0f94
- 008840f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008840f0 ["INT_ADD", "register:40f0:8", ["const:8840f0:8", "const:4:8"]]
- 008840f0 ["CALLIND", null, ["register:0:8"]]
+ 0088509c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088509c ["INT_ADD", "register:40f0:8", ["const:88509c:8", "const:4:8"]]
+ 0088509c ["CALLIND", null, ["register:0:8"]]
- 008840f0 bytes 00013fd6
+ 0088509c bytes 00013fd6
~~~


<a id="compare-7c56dd2573abc5e78422c0a00c8ec12b"></a>

### [`00884370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884370.md) → [`0088531c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088531c.md) FUN_0088531c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008843ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884370.md#insn-008843ac) · [`008843c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884370.md#insn-008843c0) · [`008843e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884370.md#insn-008843e0)
- 新版 [`00885358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088531c.md#insn-00885358) · [`0088536c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088531c.md#insn-0088536c) · [`0088538c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088531c.md#insn-0088538c)

~~~diff
- 008843ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008843ac ["INT_ADD", "register:40f0:8", ["const:8843ac:8", "const:4:8"]]
- 008843ac ["CALLIND", null, ["register:0:8"]]
+ 00885358 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885358 ["INT_ADD", "register:40f0:8", ["const:885358:8", "const:4:8"]]
+ 00885358 ["CALLIND", null, ["register:0:8"]]
- 008843ac bytes 00013fd6
+ 00885358 bytes 00013fd6
- 008843c0 ["INT_ADD", "register:40f0:8", ["const:8843c0:8", "const:4:8"]]
- 008843c0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088536c ["INT_ADD", "register:40f0:8", ["const:88536c:8", "const:4:8"]]
+ 0088536c ["CALL", null, ["callee:00c54d90:8"]]
- 008843c0 bytes 783e0f94
+ 0088536c bytes 893e0f94
- 008843e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008843e0 ["INT_ADD", "register:40f0:8", ["const:8843e0:8", "const:4:8"]]
- 008843e0 ["CALLIND", null, ["register:0:8"]]
+ 0088538c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088538c ["INT_ADD", "register:40f0:8", ["const:88538c:8", "const:4:8"]]
+ 0088538c ["CALLIND", null, ["register:0:8"]]
- 008843e0 bytes 00013fd6
+ 0088538c bytes 00013fd6
~~~


<a id="compare-39e0e02b56a0f66c34f85e4803f9eebc"></a>

### [`008843f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008843f4.md) → [`008853a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008853a0.md) FUN_008853a0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00884ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884ad8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008843f4.md#insn-00884430) · [`00884444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008843f4.md#insn-00884444) · [`00884458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008843f4.md#insn-00884458)
- 新版 [`008853dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008853a0.md#insn-008853dc) · [`008853f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008853a0.md#insn-008853f0) · [`00885404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008853a0.md#insn-00885404)

~~~diff
- 00884430 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884430 ["INT_ADD", "register:40f0:8", ["const:884430:8", "const:4:8"]]
- 00884430 ["CALLIND", null, ["register:0:8"]]
+ 008853dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008853dc ["INT_ADD", "register:40f0:8", ["const:8853dc:8", "const:4:8"]]
+ 008853dc ["CALLIND", null, ["register:0:8"]]
- 00884430 bytes 00013fd6
+ 008853dc bytes 00013fd6
- 00884444 ["INT_ADD", "register:40f0:8", ["const:884444:8", "const:4:8"]]
- 00884444 ["CALL", null, ["callee:00c54d90:8"]]
+ 008853f0 ["INT_ADD", "register:40f0:8", ["const:8853f0:8", "const:4:8"]]
+ 008853f0 ["CALL", null, ["callee:00c54d90:8"]]
- 00884444 bytes 573e0f94
+ 008853f0 bytes 683e0f94
- 00884458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884458 ["INT_ADD", "register:40f0:8", ["const:884458:8", "const:4:8"]]
- 00884458 ["CALLIND", null, ["register:0:8"]]
+ 00885404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885404 ["INT_ADD", "register:40f0:8", ["const:885404:8", "const:4:8"]]
+ 00885404 ["CALLIND", null, ["register:0:8"]]
- 00884458 bytes 00013fd6
+ 00885404 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513c02a030d61a7672ebf7f237561a99"></a>

### [`00884fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884fcc.md) → [`00885f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885f78.md) FUN_00885f78

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884fcc.md#insn-00885008) · [`0088501c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884fcc.md#insn-0088501c) · [`0088503c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884fcc.md#insn-0088503c)
- 新版 [`00885fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885f78.md#insn-00885fb4) · [`00885fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885f78.md#insn-00885fc8) · [`00885fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885f78.md#insn-00885fe8)

~~~diff
- 00885008 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885008 ["INT_ADD", "register:40f0:8", ["const:885008:8", "const:4:8"]]
- 00885008 ["CALLIND", null, ["register:0:8"]]
+ 00885fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885fb4 ["INT_ADD", "register:40f0:8", ["const:885fb4:8", "const:4:8"]]
+ 00885fb4 ["CALLIND", null, ["register:0:8"]]
- 00885008 bytes 00013fd6
+ 00885fb4 bytes 00013fd6
- 0088501c ["INT_ADD", "register:40f0:8", ["const:88501c:8", "const:4:8"]]
- 0088501c ["CALL", null, ["callee:00c54d90:8"]]
+ 00885fc8 ["INT_ADD", "register:40f0:8", ["const:885fc8:8", "const:4:8"]]
+ 00885fc8 ["CALL", null, ["callee:00c54d90:8"]]
- 0088501c bytes 613b0f94
+ 00885fc8 bytes 723b0f94
- 0088503c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088503c ["INT_ADD", "register:40f0:8", ["const:88503c:8", "const:4:8"]]
- 0088503c ["CALLIND", null, ["register:0:8"]]
+ 00885fe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885fe8 ["INT_ADD", "register:40f0:8", ["const:885fe8:8", "const:4:8"]]
+ 00885fe8 ["CALLIND", null, ["register:0:8"]]
- 0088503c bytes 00013fd6
+ 00885fe8 bytes 00013fd6
~~~


<a id="compare-55f9da59da3a707e2fd99b787d4ec4be"></a>

### [`00885340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885340.md) → [`008862ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008862ec.md) FUN_008862ec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00884bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884bcc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00885b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885b78.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088537c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885340.md#insn-0088537c) · [`00885390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885340.md#insn-00885390) · [`008853a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885340.md#insn-008853a4)
- 新版 [`00886328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008862ec.md#insn-00886328) · [`0088633c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008862ec.md#insn-0088633c) · [`00886350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008862ec.md#insn-00886350)

~~~diff
- 0088537c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088537c ["INT_ADD", "register:40f0:8", ["const:88537c:8", "const:4:8"]]
- 0088537c ["CALLIND", null, ["register:0:8"]]
+ 00886328 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886328 ["INT_ADD", "register:40f0:8", ["const:886328:8", "const:4:8"]]
+ 00886328 ["CALLIND", null, ["register:0:8"]]
- 0088537c bytes 00013fd6
+ 00886328 bytes 00013fd6
- 00885390 ["INT_ADD", "register:40f0:8", ["const:885390:8", "const:4:8"]]
- 00885390 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088633c ["INT_ADD", "register:40f0:8", ["const:88633c:8", "const:4:8"]]
+ 0088633c ["CALL", null, ["callee:00c54d90:8"]]
- 00885390 bytes 843a0f94
+ 0088633c bytes 953a0f94
- 008853a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008853a4 ["INT_ADD", "register:40f0:8", ["const:8853a4:8", "const:4:8"]]
- 008853a4 ["CALLIND", null, ["register:0:8"]]
+ 00886350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886350 ["INT_ADD", "register:40f0:8", ["const:886350:8", "const:4:8"]]
+ 00886350 ["CALLIND", null, ["register:0:8"]]
- 008853a4 bytes 00013fd6
+ 00886350 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7bf0850cde8f76c12e73d6e5171717c"></a>

### [`00885664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885664.md) → [`00886610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886610.md) FUN_00886610

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088568c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885664.md#insn-0088568c) · [`008856a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885664.md#insn-008856a0) · [`008856a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885664.md#insn-008856a8)
- 新版 [`00886638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886610.md#insn-00886638) · [`0088664c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886610.md#insn-0088664c) · [`00886654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886610.md#insn-00886654)

~~~diff
- 0088568c ["INT_ADD", "register:40f0:8", ["const:88568c:8", "const:4:8"]]
- 0088568c ["CALL", null, ["callee:00c54d90:8"]]
+ 00886638 ["INT_ADD", "register:40f0:8", ["const:886638:8", "const:4:8"]]
+ 00886638 ["CALL", null, ["callee:00c54d90:8"]]
- 0088568c bytes c5390f94
+ 00886638 bytes d6390f94
- 008856a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008856a0 ["INT_ADD", "register:40f0:8", ["const:8856a0:8", "const:4:8"]]
- 008856a0 ["CALLIND", null, ["register:0:8"]]
+ 0088664c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088664c ["INT_ADD", "register:40f0:8", ["const:88664c:8", "const:4:8"]]
+ 0088664c ["CALLIND", null, ["register:0:8"]]
- 008856a0 bytes 00013fd6
+ 0088664c bytes 00013fd6
- 008856a8 ["INT_ADD", "register:40f0:8", ["const:8856a8:8", "const:4:8"]]
- 008856a8 ["CALL", null, ["callee:00c58f20:8"]]
+ 00886654 ["INT_ADD", "register:40f0:8", ["const:886654:8", "const:4:8"]]
+ 00886654 ["CALL", null, ["callee:00c58f20:8"]]
- 008856a8 bytes 2a4a0f94
+ 00886654 bytes 334a0f94
~~~


<a id="compare-5af18b823367bf37545b1c44b88b6c23"></a>

### [`008856f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008856f4.md) → [`008866a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008866a0.md) FUN_008866a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00881cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881cf8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008856f4.md#insn-0088571c) · [`00885730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008856f4.md#insn-00885730) · [`00885738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008856f4.md#insn-00885738)
- 新版 [`008866c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008866a0.md#insn-008866c8) · [`008866dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008866a0.md#insn-008866dc) · [`008866e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/008866a0.md#insn-008866e4)

~~~diff
- 0088571c ["INT_ADD", "register:40f0:8", ["const:88571c:8", "const:4:8"]]
- 0088571c ["CALL", null, ["callee:00c54d90:8"]]
+ 008866c8 ["INT_ADD", "register:40f0:8", ["const:8866c8:8", "const:4:8"]]
+ 008866c8 ["CALL", null, ["callee:00c54d90:8"]]
- 0088571c bytes a1390f94
+ 008866c8 bytes b2390f94
- 00885730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885730 ["INT_ADD", "register:40f0:8", ["const:885730:8", "const:4:8"]]
- 00885730 ["CALLIND", null, ["register:0:8"]]
+ 008866dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008866dc ["INT_ADD", "register:40f0:8", ["const:8866dc:8", "const:4:8"]]
+ 008866dc ["CALLIND", null, ["register:0:8"]]
- 00885730 bytes 00013fd6
+ 008866dc bytes 00013fd6
- 00885738 ["INT_ADD", "register:40f0:8", ["const:885738:8", "const:4:8"]]
- 00885738 ["CALL", null, ["callee:00c58f20:8"]]
+ 008866e4 ["INT_ADD", "register:40f0:8", ["const:8866e4:8", "const:4:8"]]
+ 008866e4 ["CALL", null, ["callee:00c58f20:8"]]
- 00885738 bytes 064a0f94
+ 008866e4 bytes 0f4a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6c8f3dd8db2c1063e3fb6a158d4a410"></a>

### [`00886aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886aac.md) → [`00887a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a58.md) FUN_00887a58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0088275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088275c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886aac.md#insn-00886acc) · [`00886ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886aac.md#insn-00886ae0) · [`00886ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886aac.md#insn-00886ae8)
- 新版 [`00887a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a58.md#insn-00887a78) · [`00887a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a58.md#insn-00887a8c) · [`00887a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a58.md#insn-00887a94)

~~~diff
- 00886acc ["INT_ADD", "register:40f0:8", ["const:886acc:8", "const:4:8"]]
- 00886acc ["CALL", null, ["callee:00c54d90:8"]]
+ 00887a78 ["INT_ADD", "register:40f0:8", ["const:887a78:8", "const:4:8"]]
+ 00887a78 ["CALL", null, ["callee:00c54d90:8"]]
- 00886acc bytes b5340f94
+ 00887a78 bytes c6340f94
- 00886ae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886ae0 ["INT_ADD", "register:40f0:8", ["const:886ae0:8", "const:4:8"]]
- 00886ae0 ["CALLIND", null, ["register:0:8"]]
+ 00887a8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00887a8c ["INT_ADD", "register:40f0:8", ["const:887a8c:8", "const:4:8"]]
+ 00887a8c ["CALLIND", null, ["register:0:8"]]
- 00886ae0 bytes 00013fd6
+ 00887a8c bytes 00013fd6
- 00886ae8 ["INT_ADD", "register:40f0:8", ["const:886ae8:8", "const:4:8"]]
- 00886ae8 ["CALL", null, ["callee:00c58f20:8"]]
+ 00887a94 ["INT_ADD", "register:40f0:8", ["const:887a94:8", "const:4:8"]]
+ 00887a94 ["CALL", null, ["callee:00c58f20:8"]]
- 00886ae8 bytes 1a450f94
+ 00887a94 bytes 23450f94
~~~


<a id="compare-b970474c003d29208b0660088860ea37"></a>

### [`0088777c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/0088777c.md) → [`00888728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/00888728.md) FUN_00888728

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008487a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008487a8.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 4件 [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`00849754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849754.md) [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) [`008558f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00855/008558f0.md) · 呼出先 4件 [`006a2f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a2/006a2f80.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008877a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/0088777c.md#insn-008877a4) · [`008877b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/0088777c.md#insn-008877b8) · [`008877d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/0088777c.md#insn-008877d4)
- 新版 [`00888750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/00888728.md#insn-00888750) · [`00888764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/00888728.md#insn-00888764) · [`00888780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/00888728.md#insn-00888780)

~~~diff
- 008877a4 ["INT_ADD", "register:40f0:8", ["const:8877a4:8", "const:4:8"]]
- 008877a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00888750 ["INT_ADD", "register:40f0:8", ["const:888750:8", "const:4:8"]]
+ 00888750 ["CALL", null, ["callee:00c58f50:8"]]
- 008877a4 bytes f7410f94
+ 00888750 bytes 00420f94
- 008877b8 ["INT_ADD", "register:40f0:8", ["const:8877b8:8", "const:4:8"]]
- 008877b8 ["CALL", null, ["callee:006a2f80:8"]]
+ 00888764 ["INT_ADD", "register:40f0:8", ["const:888764:8", "const:4:8"]]
+ 00888764 ["CALL", null, ["callee:006a2f80:8"]]
- 008877b8 bytes 066df897
+ 00888764 bytes 076af897
- 008877d4 ["INT_ADD", "register:40f0:8", ["const:8877d4:8", "const:4:8"]]
- 008877d4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00888780 ["INT_ADD", "register:40f0:8", ["const:888780:8", "const:4:8"]]
+ 00888780 ["CALL", null, ["callee:00c58f50:8"]]
- 008877d4 bytes eb410f94
+ 00888780 bytes f4410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8f8512fbca1c22854f8474b1972b43"></a>

### [`00888084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md) → [`00889030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889030.md) FUN_00889030

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008880a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md#insn-008880a0) · [`008880c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md#insn-008880c0)
- 新版 [`0088904c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889030.md#insn-0088904c) · [`0088906c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889030.md#insn-0088906c)

~~~diff
- 008880a0 ["INT_ADD", "register:40f0:8", ["const:8880a0:8", "const:4:8"]]
- 008880a0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088904c ["INT_ADD", "register:40f0:8", ["const:88904c:8", "const:4:8"]]
+ 0088904c ["CALL", null, ["callee:00c54d90:8"]]
- 008880a0 bytes 402f0f94
+ 0088904c bytes 512f0f94
- 008880c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008880c0 ["INT_ADD", "register:40f0:8", ["const:8880c0:8", "const:4:8"]]
- 008880c0 ["CALLIND", null, ["register:0:8"]]
+ 0088906c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088906c ["INT_ADD", "register:40f0:8", ["const:88906c:8", "const:4:8"]]
+ 0088906c ["CALLIND", null, ["register:0:8"]]
- 008880c0 bytes 00013fd6
+ 0088906c bytes 00013fd6
~~~


<a id="compare-78f361442b7bb314910305d24e442bed"></a>

### [`008880d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008880d4.md) → [`00889080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889080.md) FUN_00889080

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008880f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008880d4.md#insn-008880f0) · [`00888110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008880d4.md#insn-00888110)
- 新版 [`0088909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889080.md#insn-0088909c) · [`008890bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889080.md#insn-008890bc)

~~~diff
- 008880f0 ["INT_ADD", "register:40f0:8", ["const:8880f0:8", "const:4:8"]]
- 008880f0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088909c ["INT_ADD", "register:40f0:8", ["const:88909c:8", "const:4:8"]]
+ 0088909c ["CALL", null, ["callee:00c54d90:8"]]
- 008880f0 bytes 2c2f0f94
+ 0088909c bytes 3d2f0f94
- 00888110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888110 ["INT_ADD", "register:40f0:8", ["const:888110:8", "const:4:8"]]
- 00888110 ["CALLIND", null, ["register:0:8"]]
+ 008890bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008890bc ["INT_ADD", "register:40f0:8", ["const:8890bc:8", "const:4:8"]]
+ 008890bc ["CALLIND", null, ["register:0:8"]]
- 00888110 bytes 00013fd6
+ 008890bc bytes 00013fd6
~~~


<a id="compare-be8d73cec375cb59766d52f688c2d886"></a>

### [`008881c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008881c4.md) → [`00889170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889170.md) FUN_00889170

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008881e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008881c4.md#insn-008881e0) · [`00888200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008881c4.md#insn-00888200)
- 新版 [`0088918c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889170.md#insn-0088918c) · [`008891ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889170.md#insn-008891ac)

~~~diff
- 008881e0 ["INT_ADD", "register:40f0:8", ["const:8881e0:8", "const:4:8"]]
- 008881e0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088918c ["INT_ADD", "register:40f0:8", ["const:88918c:8", "const:4:8"]]
+ 0088918c ["CALL", null, ["callee:00c54d90:8"]]
- 008881e0 bytes f02e0f94
+ 0088918c bytes 012f0f94
- 00888200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888200 ["INT_ADD", "register:40f0:8", ["const:888200:8", "const:4:8"]]
- 00888200 ["CALLIND", null, ["register:0:8"]]
+ 008891ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008891ac ["INT_ADD", "register:40f0:8", ["const:8891ac:8", "const:4:8"]]
+ 008891ac ["CALLIND", null, ["register:0:8"]]
- 00888200 bytes 00013fd6
+ 008891ac bytes 00013fd6
~~~


<a id="compare-02827c45e81b422b61c1f2ac23231308"></a>

### [`00888214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888214.md) → [`008891c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008891c0.md) FUN_008891c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888214.md#insn-00888230) · [`00888250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888214.md#insn-00888250)
- 新版 [`008891dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008891c0.md#insn-008891dc) · [`008891fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008891c0.md#insn-008891fc)

~~~diff
- 00888230 ["INT_ADD", "register:40f0:8", ["const:888230:8", "const:4:8"]]
- 00888230 ["CALL", null, ["callee:00c54d90:8"]]
+ 008891dc ["INT_ADD", "register:40f0:8", ["const:8891dc:8", "const:4:8"]]
+ 008891dc ["CALL", null, ["callee:00c54d90:8"]]
- 00888230 bytes dc2e0f94
+ 008891dc bytes ed2e0f94
- 00888250 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888250 ["INT_ADD", "register:40f0:8", ["const:888250:8", "const:4:8"]]
- 00888250 ["CALLIND", null, ["register:0:8"]]
+ 008891fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008891fc ["INT_ADD", "register:40f0:8", ["const:8891fc:8", "const:4:8"]]
+ 008891fc ["CALLIND", null, ["register:0:8"]]
- 00888250 bytes 00013fd6
+ 008891fc bytes 00013fd6
~~~


<a id="compare-bda43a850b63d967ef06ae6a8120919a"></a>

### [`00888264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888264.md) → [`00889210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889210.md) FUN_00889210

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888264.md#insn-00888280) · [`008882a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888264.md#insn-008882a0)
- 新版 [`0088922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889210.md#insn-0088922c) · [`0088924c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889210.md#insn-0088924c)

~~~diff
- 00888280 ["INT_ADD", "register:40f0:8", ["const:888280:8", "const:4:8"]]
- 00888280 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088922c ["INT_ADD", "register:40f0:8", ["const:88922c:8", "const:4:8"]]
+ 0088922c ["CALL", null, ["callee:00c54d90:8"]]
- 00888280 bytes c82e0f94
+ 0088922c bytes d92e0f94
- 008882a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008882a0 ["INT_ADD", "register:40f0:8", ["const:8882a0:8", "const:4:8"]]
- 008882a0 ["CALLIND", null, ["register:0:8"]]
+ 0088924c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088924c ["INT_ADD", "register:40f0:8", ["const:88924c:8", "const:4:8"]]
+ 0088924c ["CALLIND", null, ["register:0:8"]]
- 008882a0 bytes 00013fd6
+ 0088924c bytes 00013fd6
~~~


<a id="compare-9873b1899f97e6176a04eb3db6f4241d"></a>

### [`008882b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008882b4.md) → [`00889260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889260.md) FUN_00889260

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008882d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008882b4.md#insn-008882d0) · [`008882f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008882b4.md#insn-008882f0)
- 新版 [`0088927c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889260.md#insn-0088927c) · [`0088929c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889260.md#insn-0088929c)

~~~diff
- 008882d0 ["INT_ADD", "register:40f0:8", ["const:8882d0:8", "const:4:8"]]
- 008882d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0088927c ["INT_ADD", "register:40f0:8", ["const:88927c:8", "const:4:8"]]
+ 0088927c ["CALL", null, ["callee:00c54d90:8"]]
- 008882d0 bytes b42e0f94
+ 0088927c bytes c52e0f94
- 008882f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008882f0 ["INT_ADD", "register:40f0:8", ["const:8882f0:8", "const:4:8"]]
- 008882f0 ["CALLIND", null, ["register:0:8"]]
+ 0088929c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088929c ["INT_ADD", "register:40f0:8", ["const:88929c:8", "const:4:8"]]
+ 0088929c ["CALLIND", null, ["register:0:8"]]
- 008882f0 bytes 00013fd6
+ 0088929c bytes 00013fd6
~~~


<a id="compare-d555f19683cb61fe2c7ec2618b3ff4c4"></a>

### [`00888304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888304.md) → [`008892b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008892b0.md) FUN_008892b0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`00616990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md) [`00626504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/00626504.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00b37ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37ab4.md)
- 新版 呼出元 10件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`006107ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00610/006107ac.md) [`00616d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00616/00616d40.md) [`006268b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00626/006268b4.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`00b38aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38aa8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888304.md#insn-00888410) · [`00888418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888304.md#insn-00888418)
- 新版 [`008893bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008892b0.md#insn-008893bc) · [`008893c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008892b0.md#insn-008893c4)

~~~diff
- 00888410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888410 ["INT_ADD", "register:40f0:8", ["const:888410:8", "const:4:8"]]
- 00888410 ["CALLIND", null, ["register:0:8"]]
+ 008893bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008893bc ["INT_ADD", "register:40f0:8", ["const:8893bc:8", "const:4:8"]]
+ 008893bc ["CALLIND", null, ["register:0:8"]]
- 00888410 bytes 00013fd6
+ 008893bc bytes 00013fd6
- 00888418 ["INT_ADD", "register:40f0:8", ["const:888418:8", "const:4:8"]]
- 00888418 ["CALL", null, ["callee:00b38aa8:8"]]
+ 008893c4 ["INT_ADD", "register:40f0:8", ["const:8893c4:8", "const:4:8"]]
+ 008893c4 ["CALL", null, ["callee:00b38aa8:8"]]
- 00888418 bytes a7bd0a94
+ 008893c4 bytes b9bd0a94
~~~


<a id="compare-9f2be2b44585aa888a7b0b4c4183076f"></a>

### [`008890c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008890c8.md) → [`0088a074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a074.md) FUN_0088a074

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00889134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008890c8.md#insn-00889134) · [`00889144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008890c8.md#insn-00889144) · [`00889164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008890c8.md#insn-00889164)
- 新版 [`0088a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a074.md#insn-0088a0e0) · [`0088a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a074.md#insn-0088a0f0) · [`0088a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a074.md#insn-0088a110)

~~~diff
- 00889134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889134 ["INT_ADD", "register:40f0:8", ["const:889134:8", "const:4:8"]]
- 00889134 ["CALLIND", null, ["register:0:8"]]
+ 0088a0e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a0e0 ["INT_ADD", "register:40f0:8", ["const:88a0e0:8", "const:4:8"]]
+ 0088a0e0 ["CALLIND", null, ["register:0:8"]]
- 00889134 bytes 00013fd6
+ 0088a0e0 bytes 00013fd6
- 00889144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889144 ["INT_ADD", "register:40f0:8", ["const:889144:8", "const:4:8"]]
- 00889144 ["CALLIND", null, ["register:0:8"]]
+ 0088a0f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a0f0 ["INT_ADD", "register:40f0:8", ["const:88a0f0:8", "const:4:8"]]
+ 0088a0f0 ["CALLIND", null, ["register:0:8"]]
- 00889144 bytes 00013fd6
+ 0088a0f0 bytes 00013fd6
- 00889164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889164 ["INT_ADD", "register:40f0:8", ["const:889164:8", "const:4:8"]]
- 00889164 ["CALLIND", null, ["register:0:8"]]
+ 0088a110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a110 ["INT_ADD", "register:40f0:8", ["const:88a110:8", "const:4:8"]]
+ 0088a110 ["CALLIND", null, ["register:0:8"]]
- 00889164 bytes 00013fd6
+ 0088a110 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f89adad9ba4fd14a95af9edef804d89"></a>

### [`008895c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008895c4.md) → [`0088a570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a570.md) FUN_0088a570

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00b38c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38c18.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00889630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008895c4.md#insn-00889630) · [`00889640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008895c4.md#insn-00889640) · [`00889660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/008895c4.md#insn-00889660)
- 新版 [`0088a5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a570.md#insn-0088a5dc) · [`0088a5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a570.md#insn-0088a5ec) · [`0088a60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a570.md#insn-0088a60c)

~~~diff
- 00889630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889630 ["INT_ADD", "register:40f0:8", ["const:889630:8", "const:4:8"]]
- 00889630 ["CALLIND", null, ["register:0:8"]]
+ 0088a5dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a5dc ["INT_ADD", "register:40f0:8", ["const:88a5dc:8", "const:4:8"]]
+ 0088a5dc ["CALLIND", null, ["register:0:8"]]
- 00889630 bytes 00013fd6
+ 0088a5dc bytes 00013fd6
- 00889640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889640 ["INT_ADD", "register:40f0:8", ["const:889640:8", "const:4:8"]]
- 00889640 ["CALLIND", null, ["register:0:8"]]
+ 0088a5ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a5ec ["INT_ADD", "register:40f0:8", ["const:88a5ec:8", "const:4:8"]]
+ 0088a5ec ["CALLIND", null, ["register:0:8"]]
- 00889640 bytes 00013fd6
+ 0088a5ec bytes 00013fd6
- 00889660 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889660 ["INT_ADD", "register:40f0:8", ["const:889660:8", "const:4:8"]]
- 00889660 ["CALLIND", null, ["register:0:8"]]
+ 0088a60c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a60c ["INT_ADD", "register:40f0:8", ["const:88a60c:8", "const:4:8"]]
+ 0088a60c ["CALLIND", null, ["register:0:8"]]
- 00889660 bytes 00013fd6
+ 0088a60c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d0a44735809031100c957c4b645a7ea"></a>

### [`0088a7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a7bc.md) → [`0088b768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b768.md) FUN_0088b768

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a7bc.md#insn-0088a7ec) · [`0088a800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a7bc.md#insn-0088a800) · [`0088a808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a7bc.md#insn-0088a808)
- 新版 [`0088b798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b768.md#insn-0088b798) · [`0088b7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b768.md#insn-0088b7ac) · [`0088b7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b768.md#insn-0088b7b4)

~~~diff
- 0088a7ec ["INT_ADD", "register:40f0:8", ["const:88a7ec:8", "const:4:8"]]
- 0088a7ec ["CALL", null, ["callee:00c54d90:8"]]
+ 0088b798 ["INT_ADD", "register:40f0:8", ["const:88b798:8", "const:4:8"]]
+ 0088b798 ["CALL", null, ["callee:00c54d90:8"]]
- 0088a7ec bytes 6d250f94
+ 0088b798 bytes 7e250f94
- 0088a800 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a800 ["INT_ADD", "register:40f0:8", ["const:88a800:8", "const:4:8"]]
- 0088a800 ["CALLIND", null, ["register:0:8"]]
+ 0088b7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088b7ac ["INT_ADD", "register:40f0:8", ["const:88b7ac:8", "const:4:8"]]
+ 0088b7ac ["CALLIND", null, ["register:0:8"]]
- 0088a800 bytes 00013fd6
+ 0088b7ac bytes 00013fd6
- 0088a808 ["INT_ADD", "register:40f0:8", ["const:88a808:8", "const:4:8"]]
- 0088a808 ["CALL", null, ["callee:00c58f20:8"]]
+ 0088b7b4 ["INT_ADD", "register:40f0:8", ["const:88b7b4:8", "const:4:8"]]
+ 0088b7b4 ["CALL", null, ["callee:00c58f20:8"]]
- 0088a808 bytes d2350f94
+ 0088b7b4 bytes db350f94
~~~


<a id="compare-5bd1c495c1f8b8a564dba7cef2048a4f"></a>

### [`0088f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f058.md) → [`00890004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890004.md) FUN_00890004

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f058.md#insn-0088f09c)
- 新版 [`00890048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890004.md#insn-00890048)

~~~diff
- 0088f09c ["INT_ADD", "register:40f0:8", ["const:88f09c:8", "const:4:8"]]
- 0088f09c ["CALL", null, ["callee:00c590f0:8"]]
+ 00890048 ["INT_ADD", "register:40f0:8", ["const:890048:8", "const:4:8"]]
+ 00890048 ["CALL", null, ["callee:00c590f0:8"]]
- 0088f09c bytes 21240f94
+ 00890048 bytes 2a240f94
~~~


<a id="compare-40d5bef61f7dde833177ec5b3068fbd1"></a>

### [`0088f118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f118.md) → [`008900c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008900c4.md) FUN_008900c4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006398ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/006398ac.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f118.md#insn-0088f14c) · [`0088f160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f118.md#insn-0088f160) · [`0088f1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f118.md#insn-0088f1b0)
- 新版 [`008900f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008900c4.md#insn-008900f8) · [`0089010c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008900c4.md#insn-0089010c) · [`0089015c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008900c4.md#insn-0089015c)

~~~diff
- 0088f14c ["INT_ADD", "register:40f0:8", ["const:88f14c:8", "const:4:8"]]
- 0088f14c ["CALL", null, ["callee:006398ac:8"]]
+ 008900f8 ["INT_ADD", "register:40f0:8", ["const:8900f8:8", "const:4:8"]]
+ 008900f8 ["CALL", null, ["callee:006398ac:8"]]
- 0088f14c bytes eca8f697
+ 008900f8 bytes eda5f697
- 0088f160 ["INT_ADD", "register:40f0:8", ["const:88f160:8", "const:4:8"]]
- 0088f160 ["CALL", null, ["callee:00c58f30:8"]]
+ 0089010c ["INT_ADD", "register:40f0:8", ["const:89010c:8", "const:4:8"]]
+ 0089010c ["CALL", null, ["callee:00c58f30:8"]]
- 0088f160 bytes 80230f94
+ 0089010c bytes 89230f94
- 0088f1b0 ["INT_ADD", "register:40f0:8", ["const:88f1b0:8", "const:4:8"]]
- 0088f1b0 ["CALL", null, ["callee:0043bf04:8"]]
+ 0089015c ["INT_ADD", "register:40f0:8", ["const:89015c:8", "const:4:8"]]
+ 0089015c ["CALL", null, ["callee:0043bf04:8"]]
- 0088f1b0 bytes 8db2ee97
+ 0089015c bytes 6aafee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62aefd6ef5bcb75d9f553be2f468b16"></a>

### [`0088f1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f1f0.md) → [`0089019c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089019c.md) FUN_0089019c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f1f0.md#insn-0088f268) · [`0088f290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f1f0.md#insn-0088f290)
- 新版 [`00890214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089019c.md#insn-00890214) · [`0089023c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089019c.md#insn-0089023c)

~~~diff
- 0088f268 ["INT_ADD", "register:40f0:8", ["const:88f268:8", "const:4:8"]]
- 0088f268 ["CALL", null, ["callee:00c590f0:8"]]
+ 00890214 ["INT_ADD", "register:40f0:8", ["const:890214:8", "const:4:8"]]
+ 00890214 ["CALL", null, ["callee:00c590f0:8"]]
- 0088f268 bytes ae230f94
+ 00890214 bytes b7230f94
- 0088f290 ["INT_ADD", "register:40f0:8", ["const:88f290:8", "const:4:8"]]
- 0088f290 ["CALL", null, ["callee:00c590f0:8"]]
+ 0089023c ["INT_ADD", "register:40f0:8", ["const:89023c:8", "const:4:8"]]
+ 0089023c ["CALL", null, ["callee:00c590f0:8"]]
- 0088f290 bytes a4230f94
+ 0089023c bytes ad230f94
~~~


<a id="compare-ea40f356e872ec7c634c1ce0a4408af1"></a>

### [`0088fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb30.md) → [`00890adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890adc.md) FUN_00890adc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb30.md#insn-0088fb4c) · [`0088fb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb30.md#insn-0088fb6c)
- 新版 [`00890af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890adc.md#insn-00890af8) · [`00890b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890adc.md#insn-00890b18)

~~~diff
- 0088fb4c ["INT_ADD", "register:40f0:8", ["const:88fb4c:8", "const:4:8"]]
- 0088fb4c ["CALL", null, ["callee:00c54d90:8"]]
+ 00890af8 ["INT_ADD", "register:40f0:8", ["const:890af8:8", "const:4:8"]]
+ 00890af8 ["CALL", null, ["callee:00c54d90:8"]]
- 0088fb4c bytes 95100f94
+ 00890af8 bytes a6100f94
- 0088fb6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fb6c ["INT_ADD", "register:40f0:8", ["const:88fb6c:8", "const:4:8"]]
- 0088fb6c ["CALLIND", null, ["register:0:8"]]
+ 00890b18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890b18 ["INT_ADD", "register:40f0:8", ["const:890b18:8", "const:4:8"]]
+ 00890b18 ["CALLIND", null, ["register:0:8"]]
- 0088fb6c bytes 00013fd6
+ 00890b18 bytes 00013fd6
~~~


<a id="compare-a84d0aa9ed1773ca02a132292ba25d47"></a>

### [`0088fd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd0c.md) → [`00890cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890cb8.md) FUN_00890cb8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088f738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008906e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008906e4.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fd2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd0c.md#insn-0088fd2c) · [`0088fd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd0c.md#insn-0088fd40) · [`0088fd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd0c.md#insn-0088fd48)
- 新版 [`00890cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890cb8.md#insn-00890cd8) · [`00890cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890cb8.md#insn-00890cec) · [`00890cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890cb8.md#insn-00890cf4)

~~~diff
- 0088fd2c ["INT_ADD", "register:40f0:8", ["const:88fd2c:8", "const:4:8"]]
- 0088fd2c ["CALL", null, ["callee:00c54d90:8"]]
+ 00890cd8 ["INT_ADD", "register:40f0:8", ["const:890cd8:8", "const:4:8"]]
+ 00890cd8 ["CALL", null, ["callee:00c54d90:8"]]
- 0088fd2c bytes 1d100f94
+ 00890cd8 bytes 2e100f94
- 0088fd40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fd40 ["INT_ADD", "register:40f0:8", ["const:88fd40:8", "const:4:8"]]
- 0088fd40 ["CALLIND", null, ["register:0:8"]]
+ 00890cec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890cec ["INT_ADD", "register:40f0:8", ["const:890cec:8", "const:4:8"]]
+ 00890cec ["CALLIND", null, ["register:0:8"]]
- 0088fd40 bytes 00013fd6
+ 00890cec bytes 00013fd6
- 0088fd48 ["INT_ADD", "register:40f0:8", ["const:88fd48:8", "const:4:8"]]
- 0088fd48 ["CALL", null, ["callee:00c58f20:8"]]
+ 00890cf4 ["INT_ADD", "register:40f0:8", ["const:890cf4:8", "const:4:8"]]
+ 00890cf4 ["CALL", null, ["callee:00c58f20:8"]]
- 0088fd48 bytes 82200f94
+ 00890cf4 bytes 8b200f94
~~~


<a id="compare-4ada3aee0bb822204bb5c9ceec8b8bb2"></a>

### [`00890d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890d70.md) → [`00891d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d1c.md) FUN_00891d1c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890d70.md#insn-00890dc0) · [`00890dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890d70.md#insn-00890dd0)
- 新版 [`00891d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d1c.md#insn-00891d6c) · [`00891d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d1c.md#insn-00891d7c)

~~~diff
- 00890dc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890dc0 ["INT_ADD", "register:40f0:8", ["const:890dc0:8", "const:4:8"]]
- 00890dc0 ["CALLIND", null, ["register:0:8"]]
+ 00891d6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00891d6c ["INT_ADD", "register:40f0:8", ["const:891d6c:8", "const:4:8"]]
+ 00891d6c ["CALLIND", null, ["register:0:8"]]
- 00890dc0 bytes 00013fd6
+ 00891d6c bytes 00013fd6
- 00890dd0 ["INT_ADD", "register:40f0:8", ["const:890dd0:8", "const:4:8"]]
- 00890dd0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00891d7c ["INT_ADD", "register:40f0:8", ["const:891d7c:8", "const:4:8"]]
+ 00891d7c ["CALL", null, ["callee:00c58f50:8"]]
- 00890dd0 bytes 6c1c0f94
+ 00891d7c bytes 751c0f94
~~~


<a id="compare-708c8130dc9d1c249fda2d1684a579b8"></a>

### [`00892ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ed0.md) → [`00893e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893e7c.md) FUN_00893e7c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00892308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892308.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00892ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ed0.md#insn-00892ef0)
- 新版 [`00893e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893e7c.md#insn-00893e9c)

~~~diff
- 00892ef0 ["INT_ADD", "register:40f0:8", ["const:892ef0:8", "const:4:8"]]
- 00892ef0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00893e9c ["INT_ADD", "register:40f0:8", ["const:893e9c:8", "const:4:8"]]
+ 00893e9c ["CALL", null, ["callee:00c58f50:8"]]
- 00892ef0 bytes 24140f94
+ 00893e9c bytes 2d140f94
~~~


<a id="compare-838c351a2a585d023b4018429d3c94c4"></a>

### [`00893440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893440.md) → [`008943ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008943ec.md) FUN_008943ec

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00892d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008bb568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb568.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00893d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008bc514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc514.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0089345c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893440.md#insn-0089345c) · [`00893468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893440.md#insn-00893468) · [`00893470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893440.md#insn-00893470)
- 新版 [`00894408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008943ec.md#insn-00894408) · [`00894414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008943ec.md#insn-00894414) · [`0089441c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008943ec.md#insn-0089441c)

~~~diff
- 0089345c ["INT_ADD", "register:40f0:8", ["const:89345c:8", "const:4:8"]]
- 0089345c ["CALL", null, ["callee:008524fc:8"]]
+ 00894408 ["INT_ADD", "register:40f0:8", ["const:894408:8", "const:4:8"]]
+ 00894408 ["CALL", null, ["callee:008524fc:8"]]
- 0089345c bytes 3df8fe97
+ 00894408 bytes 3df8fe97
- 00893468 ["INT_ADD", "register:40f0:8", ["const:893468:8", "const:4:8"]]
- 00893468 ["CALL", null, ["callee:008bc514:8"]]
+ 00894414 ["INT_ADD", "register:40f0:8", ["const:894414:8", "const:4:8"]]
+ 00894414 ["CALL", null, ["callee:008bc514:8"]]
- 00893468 bytes 40a00094
+ 00894414 bytes 40a00094
- 00893470 ["INT_ADD", "register:40f0:8", ["const:893470:8", "const:4:8"]]
- 00893470 ["CALL", null, ["callee:008524fc:8"]]
+ 0089441c ["INT_ADD", "register:40f0:8", ["const:89441c:8", "const:4:8"]]
+ 0089441c ["CALL", null, ["callee:008524fc:8"]]
- 00893470 bytes 38f8fe97
+ 0089441c bytes 38f8fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9506a07ffb3103b134baefbdb80012"></a>

### [`008a3cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3cf0.md) → [`008a4c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4c9c.md) FUN_008a4c9c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0074a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0074abdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a3d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3cf0.md#insn-008a3d04) · [`008a3d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3cf0.md#insn-008a3d30)
- 新版 [`008a4cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4c9c.md#insn-008a4cb0) · [`008a4cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4c9c.md#insn-008a4cdc)

~~~diff
- 008a3d04 ["INT_ADD", "register:40f0:8", ["const:8a3d04:8", "const:4:8"]]
- 008a3d04 ["CALL", null, ["callee:0074abdc:8"]]
+ 008a4cb0 ["INT_ADD", "register:40f0:8", ["const:8a4cb0:8", "const:4:8"]]
+ 008a4cb0 ["CALL", null, ["callee:0074abdc:8"]]
- 008a3d04 bytes ca9afa97
+ 008a4cb0 bytes cb97fa97
- 008a3d30 ["INT_ADD", "register:40f0:8", ["const:8a3d30:8", "const:4:8"]]
- 008a3d30 ["CALL", null, ["callee:0043be80:8"]]
+ 008a4cdc ["INT_ADD", "register:40f0:8", ["const:8a4cdc:8", "const:4:8"]]
+ 008a4cdc ["CALL", null, ["callee:0043be80:8"]]
- 008a3d30 bytes 8c5fee97
+ 008a4cdc bytes 695cee97
~~~


<a id="compare-787ac7ac6a60298973f8807a5fade041"></a>

### [`008a3d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3d54.md) → [`008a4d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4d00.md) FUN_008a4d00

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 2件 [`00748f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a3d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3d54.md#insn-008a3d8c)
- 新版 [`008a4d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4d00.md#insn-008a4d38)

~~~diff
- 008a3d8c ["INT_ADD", "register:40f0:8", ["const:8a3d8c:8", "const:4:8"]]
- 008a3d8c ["CALL", null, ["callee:00748f38:8"]]
+ 008a4d38 ["INT_ADD", "register:40f0:8", ["const:8a4d38:8", "const:4:8"]]
+ 008a4d38 ["CALL", null, ["callee:00748f38:8"]]
- 008a3d8c bytes 7f93fa97
+ 008a4d38 bytes 8090fa97
~~~


<a id="compare-535c8ad08f1db6922e13b4adaf76de7c"></a>

### [`008b6d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6d7c.md) → [`008b7d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7d28.md) FUN_008b7d28

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008b7a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7a60.md) · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6d7c.md#insn-008b6db8) · [`008b6dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6d7c.md#insn-008b6dec) · [`008b6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6d7c.md#insn-008b6df0)
- 新版 [`008b7d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7d28.md#insn-008b7d64) · [`008b7d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7d28.md#insn-008b7d98) · [`008b7d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7d28.md#insn-008b7d9c)

~~~diff
- 008b6db8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b6db8 ["INT_ADD", "register:40f0:8", ["const:8b6db8:8", "const:4:8"]]
- 008b6db8 ["CALLIND", null, ["register:0:8"]]
+ 008b7d64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b7d64 ["INT_ADD", "register:40f0:8", ["const:8b7d64:8", "const:4:8"]]
+ 008b7d64 ["CALLIND", null, ["register:0:8"]]
- 008b6db8 bytes 00013fd6
+ 008b7d64 bytes 00013fd6
- 008b6dec ["INT_ADD", "register:40f0:8", ["const:8b6dec:8", "const:4:8"]]
- 008b6dec ["CALL", null, ["callee:0045a0d4:8"]]
+ 008b7d98 ["INT_ADD", "register:40f0:8", ["const:8b7d98:8", "const:4:8"]]
+ 008b7d98 ["CALL", null, ["callee:0045a0d4:8"]]
- 008b6dec bytes f28bee97
+ 008b7d98 bytes cf88ee97
- 008b6df0 ["INT_ADD", "register:40f0:8", ["const:8b6df0:8", "const:4:8"]]
- 008b6df0 ["CALL", null, ["callee:00c58f80:8"]]
+ 008b7d9c ["INT_ADD", "register:40f0:8", ["const:8b7d9c:8", "const:4:8"]]
+ 008b7d9c ["CALL", null, ["callee:00c58f80:8"]]
- 008b6df0 bytes 70840e94
+ 008b7d9c bytes 79840e94
~~~


<a id="compare-66b702b7c2ccfa648bc1d122c461b789"></a>

### [`008b6f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f1c.md) → [`008b7ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ec8.md) FUN_008b7ec8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00786d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786d2c.md) · 呼出先 1件 [`00814030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814030.md)
- 新版 呼出元 1件 [`00787108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787108.md) · 呼出先 1件 [`00814f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00814/00814f94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f1c.md#insn-008b6f54)
- 新版 [`008b7f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ec8.md#insn-008b7f00)

~~~diff
- 008b6f54 ["INT_ADD", "register:40f0:8", ["const:8b6f54:8", "const:4:8"]]
- 008b6f54 ["CALL", null, ["callee:00814f94:8"]]
+ 008b7f00 ["INT_ADD", "register:40f0:8", ["const:8b7f00:8", "const:4:8"]]
+ 008b7f00 ["CALL", null, ["callee:00814f94:8"]]
- 008b6f54 bytes 3774fd97
+ 008b7f00 bytes 2574fd97
~~~


<a id="compare-de9fe835461169cf1e02423bd9dea0f4"></a>

### [`008b6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fb0.md) → [`008b7f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f5c.md) FUN_008b7f5c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a9/006a97bc.md) [`007f704c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f704c.md) · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`006a9b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a9/006a9b6c.md) [`007f7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f7/007f7fb0.md) · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b7008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fb0.md#insn-008b7008) · [`008b703c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fb0.md#insn-008b703c) · [`008b7040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fb0.md#insn-008b7040)
- 新版 [`008b7fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f5c.md#insn-008b7fb4) · [`008b7fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f5c.md#insn-008b7fe8) · [`008b7fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f5c.md#insn-008b7fec)

~~~diff
- 008b7008 ["COPY", "register:0:8", ["register:4048:8"]]
- 008b7008 ["INT_ADD", "register:40f0:8", ["const:8b7008:8", "const:4:8"]]
- 008b7008 ["CALLIND", null, ["register:0:8"]]
+ 008b7fb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b7fb4 ["INT_ADD", "register:40f0:8", ["const:8b7fb4:8", "const:4:8"]]
+ 008b7fb4 ["CALLIND", null, ["register:0:8"]]
- 008b7008 bytes 20013fd6
+ 008b7fb4 bytes 20013fd6
- 008b703c ["INT_ADD", "register:40f0:8", ["const:8b703c:8", "const:4:8"]]
- 008b703c ["CALL", null, ["callee:0045a0d4:8"]]
+ 008b7fe8 ["INT_ADD", "register:40f0:8", ["const:8b7fe8:8", "const:4:8"]]
+ 008b7fe8 ["CALL", null, ["callee:0045a0d4:8"]]
- 008b703c bytes 5e8bee97
+ 008b7fe8 bytes 3b88ee97
- 008b7040 ["INT_ADD", "register:40f0:8", ["const:8b7040:8", "const:4:8"]]
- 008b7040 ["CALL", null, ["callee:00c58f80:8"]]
+ 008b7fec ["INT_ADD", "register:40f0:8", ["const:8b7fec:8", "const:4:8"]]
+ 008b7fec ["CALL", null, ["callee:00c58f80:8"]]
- 008b7040 bytes dc830e94
+ 008b7fec bytes e5830e94
~~~


<a id="compare-8582110af128e7982d3c5cf59c140b88"></a>

### [`008b7ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7ca4.md) → [`008b8c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8c50.md) FUN_008b8c50

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`008b7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7424.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008b894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md) · 呼出先 3件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`008b83d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b83d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b7d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7ca4.md#insn-008b7d54) · [`008b7d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7ca4.md#insn-008b7d5c) · [`008b7d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7ca4.md#insn-008b7d64)
- 新版 [`008b8d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8c50.md#insn-008b8d00) · [`008b8d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8c50.md#insn-008b8d08) · [`008b8d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8c50.md#insn-008b8d10)

~~~diff
- 008b7d54 ["INT_ADD", "register:40f0:8", ["const:8b7d54:8", "const:4:8"]]
- 008b7d54 ["CALL", null, ["callee:00494970:8"]]
+ 008b8d00 ["INT_ADD", "register:40f0:8", ["const:8b8d00:8", "const:4:8"]]
+ 008b8d00 ["CALL", null, ["callee:00494970:8"]]
- 008b7d54 bytes 3f72ef97
+ 008b8d00 bytes 1c6fef97
- 008b7d5c ["INT_ADD", "register:40f0:8", ["const:8b7d5c:8", "const:4:8"]]
- 008b7d5c ["CALL", null, ["callee:008b83d0:8"]]
+ 008b8d08 ["INT_ADD", "register:40f0:8", ["const:8b8d08:8", "const:4:8"]]
+ 008b8d08 ["CALL", null, ["callee:008b83d0:8"]]
- 008b7d5c bytes b2fdff97
+ 008b8d08 bytes b2fdff97
- 008b7d64 ["INT_ADD", "register:40f0:8", ["const:8b7d64:8", "const:4:8"]]
- 008b7d64 ["CALL", null, ["callee:00c58f50:8"]]
+ 008b8d10 ["INT_ADD", "register:40f0:8", ["const:8b8d10:8", "const:4:8"]]
+ 008b8d10 ["CALL", null, ["callee:00c58f50:8"]]
- 008b7d64 bytes 87800e94
+ 008b8d10 bytes 90800e94
~~~


<a id="compare-003c2ad4171b6b7cfe9f9113304cfe6c"></a>

### [`008b925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md) → [`008ba208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md) FUN_008ba208

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00a00048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00048.md) [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) [`00a03a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03a18.md) [`00a03d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03d58.md) [`00a05834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05834.md) · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`00a00ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00ff4.md) [`00a03be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03be8.md) [`00a049c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a049c4.md) [`00a04d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04d04.md) [`00a067e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a067e0.md) · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b92ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md#insn-008b92ac) · [`008b92e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md#insn-008b92e0) · [`008b92e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md#insn-008b92e4)
- 新版 [`008ba258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md#insn-008ba258) · [`008ba28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md#insn-008ba28c) · [`008ba290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md#insn-008ba290)

~~~diff
- 008b92ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008b92ac ["INT_ADD", "register:40f0:8", ["const:8b92ac:8", "const:4:8"]]
- 008b92ac ["CALLIND", null, ["register:0:8"]]
+ 008ba258 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ba258 ["INT_ADD", "register:40f0:8", ["const:8ba258:8", "const:4:8"]]
+ 008ba258 ["CALLIND", null, ["register:0:8"]]
- 008b92ac bytes 00013fd6
+ 008ba258 bytes 00013fd6
- 008b92e0 ["INT_ADD", "register:40f0:8", ["const:8b92e0:8", "const:4:8"]]
- 008b92e0 ["CALL", null, ["callee:0045a0d4:8"]]
+ 008ba28c ["INT_ADD", "register:40f0:8", ["const:8ba28c:8", "const:4:8"]]
+ 008ba28c ["CALL", null, ["callee:0045a0d4:8"]]
- 008b92e0 bytes b582ee97
+ 008ba28c bytes 927fee97
- 008b92e4 ["INT_ADD", "register:40f0:8", ["const:8b92e4:8", "const:4:8"]]
- 008b92e4 ["CALL", null, ["callee:00c58f80:8"]]
+ 008ba290 ["INT_ADD", "register:40f0:8", ["const:8ba290:8", "const:4:8"]]
+ 008ba290 ["CALL", null, ["callee:00c58f80:8"]]
- 008b92e4 bytes 337b0e94
+ 008ba290 bytes 3c7b0e94
~~~


<a id="compare-5bc51d1e8eda8690b0cf3bee6247e876"></a>

### [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) → [`008ba29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba29c.md) FUN_008ba29c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00627cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00627/00627cf4.md) [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) · 呼出先 2件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 54件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`006280a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00628/006280a4.md) [`0068eb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068e/0068eb5c.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md) [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) · 呼出先 2件 [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b9318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md#insn-008b9318) · [`008b9340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md#insn-008b9340)
- 新版 [`008ba2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba29c.md#insn-008ba2c4) · [`008ba2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba29c.md#insn-008ba2ec)

~~~diff
- 008b9318 ["INT_ADD", "register:40f0:8", ["const:8b9318:8", "const:4:8"]]
- 008b9318 ["CALL", null, ["callee:0046de54:8"]]
+ 008ba2c4 ["INT_ADD", "register:40f0:8", ["const:8ba2c4:8", "const:4:8"]]
+ 008ba2c4 ["CALL", null, ["callee:0046de54:8"]]
- 008b9318 bytes 07d2ee97
+ 008ba2c4 bytes e4ceee97
- 008b9340 ["INT_ADD", "register:40f0:8", ["const:8b9340:8", "const:4:8"]]
- 008b9340 ["CALL", null, ["callee:00c58f80:8"]]
+ 008ba2ec ["INT_ADD", "register:40f0:8", ["const:8ba2ec:8", "const:4:8"]]
+ 008ba2ec ["CALL", null, ["callee:00c58f80:8"]]
- 008b9340 bytes 1c7b0e94
+ 008ba2ec bytes 257b0e94
~~~


<a id="compare-683c43599166c0abaa7e5ff2e2015379"></a>

### [`008b9344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9344.md) → [`008ba2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba2f0.md) FUN_008ba2f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) [`00696768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696768.md) [`0069802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/0069802c.md) [`006992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006992d4.md) [`006af7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af7a0.md) · 呼出先 3件 [`0046db2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db2c.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 14件 [`00695914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695914.md) [`00696b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00696/00696b18.md) [`006983dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00698/006983dc.md) [`00699684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/00699684.md) [`006afb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006af/006afb50.md) · 呼出先 3件 [`0046de4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de4c.md) [`0046de54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b9460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9344.md#insn-008b9460) · [`008b952c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9344.md#insn-008b952c) · [`008b9554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9344.md#insn-008b9554)
- 新版 [`008ba40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba2f0.md#insn-008ba40c) · [`008ba4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba2f0.md#insn-008ba4d8) · [`008ba500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba2f0.md#insn-008ba500)

~~~diff
- 008b9460 ["INT_ADD", "register:40f0:8", ["const:8b9460:8", "const:4:8"]]
- 008b9460 ["CALL", null, ["callee:0046de4c:8"]]
+ 008ba40c ["INT_ADD", "register:40f0:8", ["const:8ba40c:8", "const:4:8"]]
+ 008ba40c ["CALL", null, ["callee:0046de4c:8"]]
- 008b9460 bytes b3d1ee97
+ 008ba40c bytes 90ceee97
- 008b952c ["INT_ADD", "register:40f0:8", ["const:8b952c:8", "const:4:8"]]
- 008b952c ["CALL", null, ["callee:0046de54:8"]]
+ 008ba4d8 ["INT_ADD", "register:40f0:8", ["const:8ba4d8:8", "const:4:8"]]
+ 008ba4d8 ["CALL", null, ["callee:0046de54:8"]]
- 008b952c bytes 82d1ee97
+ 008ba4d8 bytes 5fceee97
- 008b9554 ["INT_ADD", "register:40f0:8", ["const:8b9554:8", "const:4:8"]]
- 008b9554 ["CALL", null, ["callee:00c58f80:8"]]
+ 008ba500 ["INT_ADD", "register:40f0:8", ["const:8ba500:8", "const:4:8"]]
+ 008ba500 ["CALL", null, ["callee:00c58f80:8"]]
- 008b9554 bytes 977a0e94
+ 008ba500 bytes a07a0e94
~~~


<a id="compare-fcb40928be60dba2dcfb6c7bf897a4bd"></a>

### [`008b9624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md) → [`008ba5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md) FUN_008ba5d0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 22件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) [`0068f630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068f/0068f630.md) · 呼出先 2件 [`008bc298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc298.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 22件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0061491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/0061491c.md) [`0068eb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068e/0068eb5c.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md) [`0068f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f9e0.md) · 呼出先 2件 [`008bd244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd244.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b9664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md#insn-008b9664) · [`008b9690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md#insn-008b9690) · [`008b96a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md#insn-008b96a0)
- 新版 [`008ba610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md#insn-008ba610) · [`008ba63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md#insn-008ba63c) · [`008ba64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md#insn-008ba64c)

~~~diff
- 008b9664 ["COPY", "register:0:8", ["register:4048:8"]]
- 008b9664 ["INT_ADD", "register:40f0:8", ["const:8b9664:8", "const:4:8"]]
- 008b9664 ["CALLIND", null, ["register:0:8"]]
+ 008ba610 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008ba610 ["INT_ADD", "register:40f0:8", ["const:8ba610:8", "const:4:8"]]
+ 008ba610 ["CALLIND", null, ["register:0:8"]]
- 008b9664 bytes 20013fd6
+ 008ba610 bytes 20013fd6
- 008b9690 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b9690 ["INT_ADD", "register:40f0:8", ["const:8b9690:8", "const:4:8"]]
- 008b9690 ["CALLIND", null, ["register:0:8"]]
+ 008ba63c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ba63c ["INT_ADD", "register:40f0:8", ["const:8ba63c:8", "const:4:8"]]
+ 008ba63c ["CALLIND", null, ["register:0:8"]]
- 008b9690 bytes 00013fd6
+ 008ba63c bytes 00013fd6
- 008b96a0 ["INT_ADD", "register:40f0:8", ["const:8b96a0:8", "const:4:8"]]
- 008b96a0 ["CALL", null, ["callee:008bd244:8"]]
+ 008ba64c ["INT_ADD", "register:40f0:8", ["const:8ba64c:8", "const:4:8"]]
+ 008ba64c ["CALL", null, ["callee:008bd244:8"]]
- 008b96a0 bytes fe0a0094
+ 008ba64c bytes fe0a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f27d9ac204ae3341326dab310fea997"></a>

### [`008b96fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b96fc.md) → [`008ba6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba6a8.md) FUN_008ba6a8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 38件 [`0060e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060e104.md) [`00634aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00634/00634aa4.md) [`0066ffb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066f/0066ffb4.md) [`0068e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068e7ac.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md) · 呼出先 2件 [`008bc400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc400.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 38件 [`0060e4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060e/0060e4b4.md) [`00634e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00634/00634e54.md) [`00670364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00670/00670364.md) [`0068eb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068e/0068eb5c.md) [`0068f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068f/0068f188.md) · 呼出先 2件 [`008bd3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd3ac.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b973c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b96fc.md#insn-008b973c) · [`008b9768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b96fc.md#insn-008b9768) · [`008b9778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b96fc.md#insn-008b9778)
- 新版 [`008ba6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba6a8.md#insn-008ba6e8) · [`008ba714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba6a8.md#insn-008ba714) · [`008ba724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba6a8.md#insn-008ba724)

~~~diff
- 008b973c ["COPY", "register:0:8", ["register:4048:8"]]
- 008b973c ["INT_ADD", "register:40f0:8", ["const:8b973c:8", "const:4:8"]]
- 008b973c ["CALLIND", null, ["register:0:8"]]
+ 008ba6e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008ba6e8 ["INT_ADD", "register:40f0:8", ["const:8ba6e8:8", "const:4:8"]]
+ 008ba6e8 ["CALLIND", null, ["register:0:8"]]
- 008b973c bytes 20013fd6
+ 008ba6e8 bytes 20013fd6
- 008b9768 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b9768 ["INT_ADD", "register:40f0:8", ["const:8b9768:8", "const:4:8"]]
- 008b9768 ["CALLIND", null, ["register:0:8"]]
+ 008ba714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ba714 ["INT_ADD", "register:40f0:8", ["const:8ba714:8", "const:4:8"]]
+ 008ba714 ["CALLIND", null, ["register:0:8"]]
- 008b9768 bytes 00013fd6
+ 008ba714 bytes 00013fd6
- 008b9778 ["INT_ADD", "register:40f0:8", ["const:8b9778:8", "const:4:8"]]
- 008b9778 ["CALL", null, ["callee:008bd3ac:8"]]
+ 008ba724 ["INT_ADD", "register:40f0:8", ["const:8ba724:8", "const:4:8"]]
+ 008ba724 ["CALL", null, ["callee:008bd3ac:8"]]
- 008b9778 bytes 220b0094
+ 008ba724 bytes 220b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ef14438c4093ffe10db2d806da93f1"></a>

### [`008ba8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md) → [`008bb86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bb86c.md) FUN_008bb86c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 66件 [`005ccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md) [`005d9f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d9/005d9f8c.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`0061308c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b83ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b8/008b83ac.md) [`008bace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bace4.md) [`008bc568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc568.md)
- 新版 呼出元 66件 [`005cd0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd0f4.md) [`005da33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da33c.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`006107ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00610/006107ac.md) [`0061343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00613/0061343c.md) · 呼出先 10件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b9358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b9/008b9358.md) [`008bbc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbc90.md) [`008bd514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd514.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ba908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md#insn-008ba908) · [`008ba954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md#insn-008ba954) · [`008ba984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md#insn-008ba984)
- 新版 [`008bb8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bb86c.md#insn-008bb8b4) · [`008bb900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bb86c.md#insn-008bb900) · [`008bb930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bb86c.md#insn-008bb930)

~~~diff
- 008ba908 ["INT_ADD", "register:40f0:8", ["const:8ba908:8", "const:4:8"]]
- 008ba908 ["CALL", null, ["callee:00c58f30:8"]]
+ 008bb8b4 ["INT_ADD", "register:40f0:8", ["const:8bb8b4:8", "const:4:8"]]
+ 008bb8b4 ["CALL", null, ["callee:00c58f30:8"]]
- 008ba908 bytes 96750e94
+ 008bb8b4 bytes 9f750e94
- 008ba954 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ba954 ["INT_ADD", "register:40f0:8", ["const:8ba954:8", "const:4:8"]]
- 008ba954 ["CALLIND", null, ["register:0:8"]]
+ 008bb900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bb900 ["INT_ADD", "register:40f0:8", ["const:8bb900:8", "const:4:8"]]
+ 008bb900 ["CALLIND", null, ["register:0:8"]]
- 008ba954 bytes 00013fd6
+ 008bb900 bytes 00013fd6
- 008ba984 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ba984 ["INT_ADD", "register:40f0:8", ["const:8ba984:8", "const:4:8"]]
- 008ba984 ["CALLIND", null, ["register:0:8"]]
+ 008bb930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bb930 ["INT_ADD", "register:40f0:8", ["const:8bb930:8", "const:4:8"]]
+ 008bb930 ["CALLIND", null, ["register:0:8"]]
- 008ba984 bytes 00013fd6
+ 008bb930 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e86535eb2f3e2cdfda1a776dff6df2cf"></a>

### [`008bace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bace4.md) → [`008bbc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbc90.md) FUN_008bbc90

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008ba8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`008bb144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb144.md) · 呼出先 2件 [`00869b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`008bb86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bb86c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md) [`008bc0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc0f0.md) · 呼出先 2件 [`0086ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086ab40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bace4.md#insn-008bad00)
- 新版 [`008bbcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbc90.md#insn-008bbcac)

~~~diff
- 008bad00 ["INT_ADD", "register:40f0:8", ["const:8bad00:8", "const:4:8"]]
- 008bad00 ["CALL", null, ["callee:0086ab40:8"]]
+ 008bbcac ["INT_ADD", "register:40f0:8", ["const:8bbcac:8", "const:4:8"]]
+ 008bbcac ["CALL", null, ["callee:0086ab40:8"]]
- 008bad00 bytes a5bbfe97
+ 008bbcac bytes a5bbfe97
~~~


<a id="compare-d0434a39cf33741a3e91ee4a1f8229af"></a>

### [`008bba4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bba4c.md) → [`008bc9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc9f8.md) FUN_008bc9f8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 1件 [`008b9d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9d84.md)
- 新版 呼出元 1件 [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) · 呼出先 1件 [`008bad30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008bad30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bbaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bba4c.md#insn-008bbaa0)
- 新版 [`008bca4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc9f8.md#insn-008bca4c)

~~~diff
- 008bbaa0 ["INT_ADD", "register:40f0:8", ["const:8bbaa0:8", "const:4:8"]]
- 008bbaa0 ["CALL", null, ["callee:008bad30:8"]]
+ 008bca4c ["INT_ADD", "register:40f0:8", ["const:8bca4c:8", "const:4:8"]]
+ 008bca4c ["CALL", null, ["callee:008bad30:8"]]
- 008bbaa0 bytes b9f8ff97
+ 008bca4c bytes b9f8ff97
~~~


<a id="compare-0fc3c2c8da0275cd1a0d7da90a8b4ac4"></a>

### [`008bbcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbcc4.md) → [`008bcc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bcc70.md) FUN_008bcc70

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b83ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b8/008b83ac.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008b9358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b9/008b9358.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bbd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbcc4.md#insn-008bbd30) · [`008bbd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbcc4.md#insn-008bbd40) · [`008bbd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbcc4.md#insn-008bbd60)
- 新版 [`008bccdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bcc70.md#insn-008bccdc) · [`008bccec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bcc70.md#insn-008bccec) · [`008bcd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bcc70.md#insn-008bcd0c)

~~~diff
- 008bbd30 ["COPY", "register:0:8", ["register:4040:8"]]
- 008bbd30 ["INT_ADD", "register:40f0:8", ["const:8bbd30:8", "const:4:8"]]
- 008bbd30 ["CALLIND", null, ["register:0:8"]]
+ 008bccdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bccdc ["INT_ADD", "register:40f0:8", ["const:8bccdc:8", "const:4:8"]]
+ 008bccdc ["CALLIND", null, ["register:0:8"]]
- 008bbd30 bytes 00013fd6
+ 008bccdc bytes 00013fd6
- 008bbd40 ["COPY", "register:0:8", ["register:4040:8"]]
- 008bbd40 ["INT_ADD", "register:40f0:8", ["const:8bbd40:8", "const:4:8"]]
- 008bbd40 ["CALLIND", null, ["register:0:8"]]
+ 008bccec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bccec ["INT_ADD", "register:40f0:8", ["const:8bccec:8", "const:4:8"]]
+ 008bccec ["CALLIND", null, ["register:0:8"]]
- 008bbd40 bytes 00013fd6
+ 008bccec bytes 00013fd6
- 008bbd60 ["COPY", "register:0:8", ["register:4040:8"]]
- 008bbd60 ["INT_ADD", "register:40f0:8", ["const:8bbd60:8", "const:4:8"]]
- 008bbd60 ["CALLIND", null, ["register:0:8"]]
+ 008bcd0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bcd0c ["INT_ADD", "register:40f0:8", ["const:8bcd0c:8", "const:4:8"]]
+ 008bcd0c ["CALLIND", null, ["register:0:8"]]
- 008bbd60 bytes 00013fd6
+ 008bcd0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb7e43d47e5267fb1a9e63223917a962"></a>

### [`008bc1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc1a4.md) → [`008bd150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd150.md) FUN_008bd150

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bc218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc1a4.md#insn-008bc218) · [`008bc22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc1a4.md#insn-008bc22c) · [`008bc234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc1a4.md#insn-008bc234)
- 新版 [`008bd1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd150.md#insn-008bd1c4) · [`008bd1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd150.md#insn-008bd1d8) · [`008bd1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd150.md#insn-008bd1e0)

~~~diff
- 008bc218 ["INT_ADD", "register:40f0:8", ["const:8bc218:8", "const:4:8"]]
- 008bc218 ["CALL", null, ["callee:00c54d90:8"]]
+ 008bd1c4 ["INT_ADD", "register:40f0:8", ["const:8bd1c4:8", "const:4:8"]]
+ 008bd1c4 ["CALL", null, ["callee:00c54d90:8"]]
- 008bc218 bytes e25e0e94
+ 008bd1c4 bytes f35e0e94
- 008bc22c ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc22c ["INT_ADD", "register:40f0:8", ["const:8bc22c:8", "const:4:8"]]
- 008bc22c ["CALLIND", null, ["register:0:8"]]
+ 008bd1d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bd1d8 ["INT_ADD", "register:40f0:8", ["const:8bd1d8:8", "const:4:8"]]
+ 008bd1d8 ["CALLIND", null, ["register:0:8"]]
- 008bc22c bytes 00013fd6
+ 008bd1d8 bytes 00013fd6
- 008bc234 ["INT_ADD", "register:40f0:8", ["const:8bc234:8", "const:4:8"]]
- 008bc234 ["CALL", null, ["callee:00c58f20:8"]]
+ 008bd1e0 ["INT_ADD", "register:40f0:8", ["const:8bd1e0:8", "const:4:8"]]
+ 008bd1e0 ["CALL", null, ["callee:00c58f20:8"]]
- 008bc234 bytes 476f0e94
+ 008bd1e0 bytes 506f0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3013d6d8b24ffe06740dfc24a4b5ff6f"></a>

### [`008bc400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc400.md) → [`008bd3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd3ac.md) FUN_008bd3ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b96fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b96fc.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008ba6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba6a8.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bc46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc400.md#insn-008bc46c) · [`008bc47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc400.md#insn-008bc47c) · [`008bc49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc400.md#insn-008bc49c)
- 新版 [`008bd418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd3ac.md#insn-008bd418) · [`008bd428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd3ac.md#insn-008bd428) · [`008bd448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd3ac.md#insn-008bd448)

~~~diff
- 008bc46c ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc46c ["INT_ADD", "register:40f0:8", ["const:8bc46c:8", "const:4:8"]]
- 008bc46c ["CALLIND", null, ["register:0:8"]]
+ 008bd418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bd418 ["INT_ADD", "register:40f0:8", ["const:8bd418:8", "const:4:8"]]
+ 008bd418 ["CALLIND", null, ["register:0:8"]]
- 008bc46c bytes 00013fd6
+ 008bd418 bytes 00013fd6
- 008bc47c ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc47c ["INT_ADD", "register:40f0:8", ["const:8bc47c:8", "const:4:8"]]
- 008bc47c ["CALLIND", null, ["register:0:8"]]
+ 008bd428 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bd428 ["INT_ADD", "register:40f0:8", ["const:8bd428:8", "const:4:8"]]
+ 008bd428 ["CALLIND", null, ["register:0:8"]]
- 008bc47c bytes 00013fd6
+ 008bd428 bytes 00013fd6
- 008bc49c ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc49c ["INT_ADD", "register:40f0:8", ["const:8bc49c:8", "const:4:8"]]
- 008bc49c ["CALLIND", null, ["register:0:8"]]
+ 008bd448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bd448 ["INT_ADD", "register:40f0:8", ["const:8bd448:8", "const:4:8"]]
+ 008bd448 ["CALLIND", null, ["register:0:8"]]
- 008bc49c bytes 00013fd6
+ 008bd448 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2cc74a3d555c6eab2294934c0d63976"></a>

### [`008bf8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md) → [`008c0858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md) FUN_008c0858

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008bf604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf604.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008d05cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d05cc.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`00ac96f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md)
- 新版 呼出元 3件 [`008c05b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c05b0.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`008d1578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1578.md) · 呼出先 4件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`00aca6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca6ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bf8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md#insn-008bf8b8) · [`008bf8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md#insn-008bf8c4) · [`008bf8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md#insn-008bf8c8)
- 新版 [`008c0864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md#insn-008c0864) · [`008c0870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md#insn-008c0870) · [`008c0874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md#insn-008c0874)

~~~diff
- 008bf8b8 ["INT_ADD", "register:40f0:8", ["const:8bf8b8:8", "const:4:8"]]
- 008bf8b8 ["CALL", null, ["callee:008524fc:8"]]
+ 008c0864 ["INT_ADD", "register:40f0:8", ["const:8c0864:8", "const:4:8"]]
+ 008c0864 ["CALL", null, ["callee:008524fc:8"]]
- 008bf8b8 bytes 2647fe97
+ 008c0864 bytes 2647fe97
- 008bf8c4 ["INT_ADD", "register:40f0:8", ["const:8bf8c4:8", "const:4:8"]]
- 008bf8c4 ["CALL", null, ["callee:00aca6ec:8"]]
+ 008c0870 ["INT_ADD", "register:40f0:8", ["const:8c0870:8", "const:4:8"]]
+ 008c0870 ["CALL", null, ["callee:00aca6ec:8"]]
- 008bf8c4 bytes 8d270894
+ 008c0870 bytes 9f270894
- 008bf8c8 ["INT_ADD", "register:40f0:8", ["const:8bf8c8:8", "const:4:8"]]
- 008bf8c8 ["CALL", null, ["callee:008524fc:8"]]
+ 008c0874 ["INT_ADD", "register:40f0:8", ["const:8c0874:8", "const:4:8"]]
+ 008c0874 ["CALL", null, ["callee:008524fc:8"]]
- 008bf8c8 bytes 2247fe97
+ 008c0874 bytes 2247fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ad41a5100933155c3f7362e7fc74d7"></a>

### [`008c1ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1ef0.md) → [`008c2e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c2e9c.md) FUN_008c2e9c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005fa864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fa/005fa864.md) [`008c1534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1534.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a4203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a4203c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`005fac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fa/005fac14.md) [`008c24e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c24e0.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043eb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043eb88.md) [`0044dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044dc80.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a43030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c1f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1ef0.md#insn-008c1f24) · [`008c1f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1ef0.md#insn-008c1f88) · [`008c1fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1ef0.md#insn-008c1fc8)
- 新版 [`008c2ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c2e9c.md#insn-008c2ed0) · [`008c2f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c2e9c.md#insn-008c2f34) · [`008c2f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c2e9c.md#insn-008c2f74)

~~~diff
- 008c1f24 ["INT_ADD", "register:40f0:8", ["const:8c1f24:8", "const:4:8"]]
- 008c1f24 ["CALL", null, ["callee:008524fc:8"]]
+ 008c2ed0 ["INT_ADD", "register:40f0:8", ["const:8c2ed0:8", "const:4:8"]]
+ 008c2ed0 ["CALL", null, ["callee:008524fc:8"]]
- 008c1f24 bytes 8b3dfe97
+ 008c2ed0 bytes 8b3dfe97
- 008c1f88 ["INT_ADD", "register:40f0:8", ["const:8c1f88:8", "const:4:8"]]
- 008c1f88 ["CALL", null, ["callee:008524fc:8"]]
+ 008c2f34 ["INT_ADD", "register:40f0:8", ["const:8c2f34:8", "const:4:8"]]
+ 008c2f34 ["CALL", null, ["callee:008524fc:8"]]
- 008c1f88 bytes 723dfe97
+ 008c2f34 bytes 723dfe97
- 008c1fc8 ["INT_ADD", "register:40f0:8", ["const:8c1fc8:8", "const:4:8"]]
- 008c1fc8 ["CALL", null, ["callee:008524fc:8"]]
+ 008c2f74 ["INT_ADD", "register:40f0:8", ["const:8c2f74:8", "const:4:8"]]
+ 008c2f74 ["CALL", null, ["callee:008524fc:8"]]
- 008c1fc8 bytes 623dfe97
+ 008c2f74 bytes 623dfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97d7024134683e58e687cbb5880d7492"></a>

### [`008c2538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2538.md) → [`008c34e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c34e4.md) FUN_008c34e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) · 呼出先 11件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ad0410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0410.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) · 呼出先 11件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00ad1404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1404.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2538.md#insn-008c258c) · [`008c2594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2538.md#insn-008c2594) · [`008c25b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2538.md#insn-008c25b8)
- 新版 [`008c3538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c34e4.md#insn-008c3538) · [`008c3540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c34e4.md#insn-008c3540) · [`008c3564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c34e4.md#insn-008c3564)

~~~diff
- 008c258c ["INT_ADD", "register:40f0:8", ["const:8c258c:8", "const:4:8"]]
- 008c258c ["CALL", null, ["callee:008524fc:8"]]
+ 008c3538 ["INT_ADD", "register:40f0:8", ["const:8c3538:8", "const:4:8"]]
+ 008c3538 ["CALL", null, ["callee:008524fc:8"]]
- 008c258c bytes f13bfe97
+ 008c3538 bytes f13bfe97
- 008c2594 ["INT_ADD", "register:40f0:8", ["const:8c2594:8", "const:4:8"]]
- 008c2594 ["CALL", null, ["callee:00ad1404:8"]]
+ 008c3540 ["INT_ADD", "register:40f0:8", ["const:8c3540:8", "const:4:8"]]
+ 008c3540 ["CALL", null, ["callee:00ad1404:8"]]
- 008c2594 bytes 9f370894
+ 008c3540 bytes b1370894
- 008c25b8 ["INT_ADD", "register:40f0:8", ["const:8c25b8:8", "const:4:8"]]
- 008c25b8 ["CALL", null, ["callee:008524fc:8"]]
+ 008c3564 ["INT_ADD", "register:40f0:8", ["const:8c3564:8", "const:4:8"]]
+ 008c3564 ["CALL", null, ["callee:008524fc:8"]]
- 008c25b8 bytes e63bfe97
+ 008c3564 bytes e63bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a06a6764fc234c965cacc6b25de392c"></a>

### [`008c28c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c28c4.md) → [`008c3870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3870.md) FUN_008c3870

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c28e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c28c4.md#insn-008c28e0) · [`008c2900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c28c4.md#insn-008c2900)
- 新版 [`008c388c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3870.md#insn-008c388c) · [`008c38ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3870.md#insn-008c38ac)

~~~diff
- 008c28e0 ["INT_ADD", "register:40f0:8", ["const:8c28e0:8", "const:4:8"]]
- 008c28e0 ["CALL", null, ["callee:00c54d90:8"]]
+ 008c388c ["INT_ADD", "register:40f0:8", ["const:8c388c:8", "const:4:8"]]
+ 008c388c ["CALL", null, ["callee:00c54d90:8"]]
- 008c28e0 bytes 30450e94
+ 008c388c bytes 41450e94
- 008c2900 ["COPY", "register:0:8", ["register:4040:8"]]
- 008c2900 ["INT_ADD", "register:40f0:8", ["const:8c2900:8", "const:4:8"]]
- 008c2900 ["CALLIND", null, ["register:0:8"]]
+ 008c38ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008c38ac ["INT_ADD", "register:40f0:8", ["const:8c38ac:8", "const:4:8"]]
+ 008c38ac ["CALLIND", null, ["register:0:8"]]
- 008c2900 bytes 00013fd6
+ 008c38ac bytes 00013fd6
~~~


<a id="compare-eb94bdf82679469f91f528d2249760fd"></a>

### [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md) → [`008c38c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c38c0.md) FUN_008c38c0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008cb488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb488.md) [`008cf498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf498.md) [`008cf750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf750.md) [`008cf970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`00ac9604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md)
- 新版 呼出元 6件 [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`008cc434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008cc434.md) [`008d0444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d0/008d0444.md) [`008d06fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d0/008d06fc.md) [`008d091c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d0/008d091c.md) · 呼出先 4件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`00aca5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c2920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md#insn-008c2920) · [`008c292c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md#insn-008c292c) · [`008c2930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md#insn-008c2930)
- 新版 [`008c38cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c38c0.md#insn-008c38cc) · [`008c38d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c38c0.md#insn-008c38d8) · [`008c38dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c38c0.md#insn-008c38dc)

~~~diff
- 008c2920 ["INT_ADD", "register:40f0:8", ["const:8c2920:8", "const:4:8"]]
- 008c2920 ["CALL", null, ["callee:008524fc:8"]]
+ 008c38cc ["INT_ADD", "register:40f0:8", ["const:8c38cc:8", "const:4:8"]]
+ 008c38cc ["CALL", null, ["callee:008524fc:8"]]
- 008c2920 bytes 0c3bfe97
+ 008c38cc bytes 0c3bfe97
- 008c292c ["INT_ADD", "register:40f0:8", ["const:8c292c:8", "const:4:8"]]
- 008c292c ["CALL", null, ["callee:00aca5f8:8"]]
+ 008c38d8 ["INT_ADD", "register:40f0:8", ["const:8c38d8:8", "const:4:8"]]
+ 008c38d8 ["CALL", null, ["callee:00aca5f8:8"]]
- 008c292c bytes 361b0894
+ 008c38d8 bytes 481b0894
- 008c2930 ["INT_ADD", "register:40f0:8", ["const:8c2930:8", "const:4:8"]]
- 008c2930 ["CALL", null, ["callee:008524fc:8"]]
+ 008c38dc ["INT_ADD", "register:40f0:8", ["const:8c38dc:8", "const:4:8"]]
+ 008c38dc ["CALL", null, ["callee:008524fc:8"]]
- 008c2930 bytes 083bfe97
+ 008c38dc bytes 083bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f594e6684a34435252d6f02cd994844d"></a>

### [`008c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md) → [`008c3d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3d28.md) FUN_008c3d28

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`005afe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe48.md) [`005aff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005aff9c.md) [`005b00a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b00a4.md) [`005b0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0100.md) [`005b0180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0180.md) · 呼出先 6件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e431c.md) [`00a41fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a41fa0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 19件 [`005b01f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b01f8.md) [`005b034c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b034c.md) [`005b0454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0454.md) [`005b04b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b04b0.md) [`005b0530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0530.md) · 呼出先 6件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e52c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e52c8.md) [`00a42f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a42/00a42f94.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c2e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md#insn-008c2e4c) · [`008c2e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md#insn-008c2e60) · [`008c2e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md#insn-008c2e74)
- 新版 [`008c3df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3d28.md#insn-008c3df8) · [`008c3e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3d28.md#insn-008c3e0c) · [`008c3e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3d28.md#insn-008c3e20)

~~~diff
- 008c2e4c ["INT_ADD", "register:40f0:8", ["const:8c2e4c:8", "const:4:8"]]
- 008c2e4c ["CALL", null, ["callee:008524fc:8"]]
+ 008c3df8 ["INT_ADD", "register:40f0:8", ["const:8c3df8:8", "const:4:8"]]
+ 008c3df8 ["CALL", null, ["callee:008524fc:8"]]
- 008c2e4c bytes c139fe97
+ 008c3df8 bytes c139fe97
- 008c2e60 ["INT_ADD", "register:40f0:8", ["const:8c2e60:8", "const:4:8"]]
- 008c2e60 ["CALL", null, ["callee:00a42f94:8"]]
+ 008c3e0c ["INT_ADD", "register:40f0:8", ["const:8c3e0c:8", "const:4:8"]]
+ 008c3e0c ["CALL", null, ["callee:00a42f94:8"]]
- 008c2e60 bytes 50fc0594
+ 008c3e0c bytes 62fc0594
- 008c2e74 ["INT_ADD", "register:40f0:8", ["const:8c2e74:8", "const:4:8"]]
- 008c2e74 ["CALL", null, ["callee:008524fc:8"]]
+ 008c3e20 ["INT_ADD", "register:40f0:8", ["const:8c3e20:8", "const:4:8"]]
+ 008c3e20 ["CALL", null, ["callee:008524fc:8"]]
- 008c2e74 bytes b739fe97
+ 008c3e20 bytes b739fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a9040ef13d38664df274ae6d18c0db"></a>

### [`008c2f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2f04.md) → [`008c3eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3eb0.md) FUN_008c3eb0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e431c.md)
- 新版 呼出元 1件 [`00b010e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b01/00b010e4.md) · 呼出先 10件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e52c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e52c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c2fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2f04.md#insn-008c2fe0) · [`008c2ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2f04.md#insn-008c2ffc) · [`008c3078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2f04.md#insn-008c3078)
- 新版 [`008c3f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3eb0.md#insn-008c3f8c) · [`008c3fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3eb0.md#insn-008c3fa8) · [`008c4024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3eb0.md#insn-008c4024)

~~~diff
- 008c2fe0 ["INT_ADD", "register:40f0:8", ["const:8c2fe0:8", "const:4:8"]]
- 008c2fe0 ["CALL", null, ["callee:008524fc:8"]]
+ 008c3f8c ["INT_ADD", "register:40f0:8", ["const:8c3f8c:8", "const:4:8"]]
+ 008c3f8c ["CALL", null, ["callee:008524fc:8"]]
- 008c2fe0 bytes 5c39fe97
+ 008c3f8c bytes 5c39fe97
- 008c2ffc ["INT_ADD", "register:40f0:8", ["const:8c2ffc:8", "const:4:8"]]
- 008c2ffc ["CALL", null, ["callee:00a42f94:8"]]
+ 008c3fa8 ["INT_ADD", "register:40f0:8", ["const:8c3fa8:8", "const:4:8"]]
+ 008c3fa8 ["CALL", null, ["callee:00a42f94:8"]]
- 008c2ffc bytes e9fb0594
+ 008c3fa8 bytes fbfb0594
- 008c3078 ["INT_ADD", "register:40f0:8", ["const:8c3078:8", "const:4:8"]]
- 008c3078 ["CALL", null, ["callee:00c58f30:8"]]
+ 008c4024 ["INT_ADD", "register:40f0:8", ["const:8c4024:8", "const:4:8"]]
+ 008c4024 ["CALL", null, ["callee:00c58f30:8"]]
- 008c3078 bytes ba530e94
+ 008c4024 bytes c3530e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec409edb1302ccffac6720e1c2bb104"></a>

### [`008cb904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb904.md) → [`008cc8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008cc8b0.md) FUN_008cc8b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008cb840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb840.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008cc7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008cc7ec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cb914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb904.md#insn-008cb914)
- 新版 [`008cc8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008cc8b0.md#insn-008cc8c0)

~~~diff
- 008cb914 ["INT_ADD", "register:40f0:8", ["const:8cb914:8", "const:4:8"]]
- 008cb914 ["CALL", null, ["callee:008cc7ec:8"]]
+ 008cc8c0 ["INT_ADD", "register:40f0:8", ["const:8cc8c0:8", "const:4:8"]]
+ 008cc8c0 ["CALL", null, ["callee:008cc7ec:8"]]
- 008cb914 bytes cbffff97
+ 008cc8c0 bytes cbffff97
~~~


<a id="compare-e55ad3813a2404665a6ef2f94796a029"></a>

### [`008ceac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md) → [`008cfa74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfa74.md) FUN_008cfa74

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) · 呼出先 3件 [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008cf5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cf5c4.md) · 呼出先 3件 [`008cf5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cf5c4.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cec34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md#insn-008cec34) · [`008cec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md#insn-008cec48) · [`008cec50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md#insn-008cec50)
- 新版 [`008cfbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfa74.md#insn-008cfbe0) · [`008cfbf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfa74.md#insn-008cfbf4) · [`008cfbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfa74.md#insn-008cfbfc)

~~~diff
- 008cec34 ["INT_ADD", "register:40f0:8", ["const:8cec34:8", "const:4:8"]]
- 008cec34 ["CALL", null, ["callee:00c54d90:8"]]
+ 008cfbe0 ["INT_ADD", "register:40f0:8", ["const:8cfbe0:8", "const:4:8"]]
+ 008cfbe0 ["CALL", null, ["callee:00c54d90:8"]]
- 008cec34 bytes 5b140e94
+ 008cfbe0 bytes 6c140e94
- 008cec48 ["COPY", "register:0:8", ["register:4040:8"]]
- 008cec48 ["INT_ADD", "register:40f0:8", ["const:8cec48:8", "const:4:8"]]
- 008cec48 ["CALLIND", null, ["register:0:8"]]
+ 008cfbf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008cfbf4 ["INT_ADD", "register:40f0:8", ["const:8cfbf4:8", "const:4:8"]]
+ 008cfbf4 ["CALLIND", null, ["register:0:8"]]
- 008cec48 bytes 00013fd6
+ 008cfbf4 bytes 00013fd6
- 008cec50 ["INT_ADD", "register:40f0:8", ["const:8cec50:8", "const:4:8"]]
- 008cec50 ["CALL", null, ["callee:00c58f20:8"]]
+ 008cfbfc ["INT_ADD", "register:40f0:8", ["const:8cfbfc:8", "const:4:8"]]
+ 008cfbfc ["CALL", null, ["callee:00c58f20:8"]]
- 008cec50 bytes c0240e94
+ 008cfbfc bytes c9240e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00be5a22a006502f520077f39026e872"></a>

### [`008cfe44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfe44.md) → [`008d0df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d0/008d0df0.md) FUN_008d0df0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cfe64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfe44.md#insn-008cfe64)
- 新版 [`008d0e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d0/008d0df0.md#insn-008d0e10)

~~~diff
- 008cfe64 ["INT_ADD", "register:40f0:8", ["const:8cfe64:8", "const:4:8"]]
- 008cfe64 ["CALL", null, ["callee:00c58f50:8"]]
+ 008d0e10 ["INT_ADD", "register:40f0:8", ["const:8d0e10:8", "const:4:8"]]
+ 008d0e10 ["CALL", null, ["callee:00c58f50:8"]]
- 008cfe64 bytes 47200e94
+ 008d0e10 bytes 50200e94
~~~


<a id="compare-80c3449e7ed541b742923dde8ffb7406"></a>

### [`008d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0374.md) → [`008d1320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1320.md) FUN_008d1320

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008c7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c7/008c7b94.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`008c8b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c8/008c8b40.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d04b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0374.md#insn-008d04b0)
- 新版 [`008d145c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1320.md#insn-008d145c)

~~~diff
- 008d04b0 ["INT_ADD", "register:40f0:8", ["const:8d04b0:8", "const:4:8"]]
- 008d04b0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 008d145c ["INT_ADD", "register:40f0:8", ["const:8d145c:8", "const:4:8"]]
+ 008d145c ["CALL", null, ["callee:00c58fe0:8"]]
- 008d04b0 bytes d81e0e94
+ 008d145c bytes e11e0e94
~~~


<a id="compare-b1a179215c13a646f8dd3bc76fb40d61"></a>

### [`008d05cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d05cc.md) → [`008d1578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1578.md) FUN_008d1578

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008bf8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008c0858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d05d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d05cc.md#insn-008d05d4)
- 新版 [`008d1580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1578.md#insn-008d1580)

~~~diff
- 008d05d4 ["INT_ADD", "register:40f0:8", ["const:8d05d4:8", "const:4:8"]]
- 008d05d4 ["CALL", null, ["callee:008524fc:8"]]
+ 008d1580 ["INT_ADD", "register:40f0:8", ["const:8d1580:8", "const:4:8"]]
+ 008d1580 ["CALL", null, ["callee:008524fc:8"]]
- 008d05d4 bytes df03fe97
+ 008d1580 bytes df03fe97
~~~


<a id="compare-e02e43b2157f7061fd30cb947b6c7a24"></a>

### [`008d1ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1ec8.md) → [`008d2e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d2/008d2e74.md) FUN_008d2e74

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 3件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00a35bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a35bec.md) [`00a38c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38c40.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 3件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00a36be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36be0.md) [`00a39c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39c34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d1ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1ec8.md#insn-008d1ed8) · [`008d1ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1ec8.md#insn-008d1ee0) · [`008d1eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1ec8.md#insn-008d1eec)
- 新版 [`008d2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d2/008d2e74.md#insn-008d2e84) · [`008d2e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d2/008d2e74.md#insn-008d2e8c) · [`008d2e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d2/008d2e74.md#insn-008d2e98)

~~~diff
- 008d1ed8 ["INT_ADD", "register:40f0:8", ["const:8d1ed8:8", "const:4:8"]]
- 008d1ed8 ["CALL", null, ["callee:00a36be0:8"]]
+ 008d2e84 ["INT_ADD", "register:40f0:8", ["const:8d2e84:8", "const:4:8"]]
+ 008d2e84 ["CALL", null, ["callee:00a36be0:8"]]
- 008d1ed8 bytes 458f0594
+ 008d2e84 bytes 578f0594
- 008d1ee0 ["INT_ADD", "register:40f0:8", ["const:8d1ee0:8", "const:4:8"]]
- 008d1ee0 ["CALL", null, ["callee:0048d1e4:8"]]
+ 008d2e8c ["INT_ADD", "register:40f0:8", ["const:8d2e8c:8", "const:4:8"]]
+ 008d2e8c ["CALL", null, ["callee:0048d1e4:8"]]
- 008d1ee0 bytes f9ebee97
+ 008d2e8c bytes d6e8ee97
- 008d1eec ["INT_ADD", "register:40f0:8", ["const:8d1eec:8", "const:4:8"]]
- 008d1eec ["CALL", null, ["callee:00a39c34:8"]]
+ 008d2e98 ["INT_ADD", "register:40f0:8", ["const:8d2e98:8", "const:4:8"]]
+ 008d2e98 ["CALL", null, ["callee:00a39c34:8"]]
- 008d1eec bytes 559b0594
+ 008d2e98 bytes 679b0594
~~~


<a id="compare-1fa79f71f10f256ed8f22f5127bb69ac"></a>

### [`008d6124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6124.md) → [`008d70d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d70d0.md) FUN_008d70d0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00814f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814f80.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b3e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md)
- 新版 呼出元 2件 [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) [`00815ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00815/00815ee4.md) · 呼出先 2件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b3f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d613c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6124.md#insn-008d613c)
- 新版 [`008d70e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d70d0.md#insn-008d70e8)

~~~diff
- 008d613c ["INT_ADD", "register:40f0:8", ["const:8d613c:8", "const:4:8"]]
- 008d613c ["CALL", null, ["callee:008524fc:8"]]
+ 008d70e8 ["INT_ADD", "register:40f0:8", ["const:8d70e8:8", "const:4:8"]]
+ 008d70e8 ["CALL", null, ["callee:008524fc:8"]]
- 008d613c bytes 05edfd97
+ 008d70e8 bytes 05edfd97
~~~


<a id="compare-6aa99a343edcc0796677c6319b68ee79"></a>

### [`008d81a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81a8.md) → [`008d9154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d9154.md) FUN_008d9154

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008d7f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008d8edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d8/008d8edc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d81b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81a8.md#insn-008d81b8)
- 新版 [`008d9164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d9154.md#insn-008d9164)

~~~diff
- 008d81b8 ["INT_ADD", "register:40f0:8", ["const:8d81b8:8", "const:4:8"]]
- 008d81b8 ["CALL", null, ["callee:008d8edc:8"]]
+ 008d9164 ["INT_ADD", "register:40f0:8", ["const:8d9164:8", "const:4:8"]]
+ 008d9164 ["CALL", null, ["callee:008d8edc:8"]]
- 008d81b8 bytes 5effff97
+ 008d9164 bytes 5effff97
~~~


<a id="compare-e456d4194870ddc7352500cefcff57d9"></a>

### [`008d82a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d82a0.md) → [`008d924c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d924c.md) FUN_008d924c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008d7248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7248.md) · 呼出先 5件 [`008d828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`008d81f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d8/008d81f4.md) · 呼出先 5件 [`008d9238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d9238.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d82f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d82a0.md#insn-008d82f4) · [`008d8358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d82a0.md#insn-008d8358) · [`008d8380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d82a0.md#insn-008d8380)
- 新版 [`008d92a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d924c.md#insn-008d92a0) · [`008d9304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d924c.md#insn-008d9304) · [`008d932c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d924c.md#insn-008d932c)

~~~diff
- 008d82f4 ["INT_ADD", "register:40f0:8", ["const:8d82f4:8", "const:4:8"]]
- 008d82f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 008d92a0 ["INT_ADD", "register:40f0:8", ["const:8d92a0:8", "const:4:8"]]
+ 008d92a0 ["CALL", null, ["callee:00c58f50:8"]]
- 008d82f4 bytes 23ff0d94
+ 008d92a0 bytes 2cff0d94
- 008d8358 ["INT_ADD", "register:40f0:8", ["const:8d8358:8", "const:4:8"]]
- 008d8358 ["CALL", null, ["callee:00c58f30:8"]]
+ 008d9304 ["INT_ADD", "register:40f0:8", ["const:8d9304:8", "const:4:8"]]
+ 008d9304 ["CALL", null, ["callee:00c58f30:8"]]
- 008d8358 bytes 02ff0d94
+ 008d9304 bytes 0bff0d94
- 008d8380 ["INT_ADD", "register:40f0:8", ["const:8d8380:8", "const:4:8"]]
- 008d8380 ["CALL", null, ["callee:00c590a0:8"]]
+ 008d932c ["INT_ADD", "register:40f0:8", ["const:8d932c:8", "const:4:8"]]
+ 008d932c ["CALL", null, ["callee:00c590a0:8"]]
- 008d8380 bytes 54ff0d94
+ 008d932c bytes 5dff0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20499a8321ebc1a416238e6e162d8c47"></a>

### [`008d9a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a60.md) → [`008daa0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008daa0c.md) FUN_008daa0c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008d2b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008d3b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d3/008d3b38.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d9a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a60.md#insn-008d9a80)
- 新版 [`008daa2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008daa0c.md#insn-008daa2c)

~~~diff
- 008d9a80 ["INT_ADD", "register:40f0:8", ["const:8d9a80:8", "const:4:8"]]
- 008d9a80 ["CALL", null, ["callee:00c58f50:8"]]
+ 008daa2c ["INT_ADD", "register:40f0:8", ["const:8daa2c:8", "const:4:8"]]
+ 008daa2c ["CALL", null, ["callee:00c58f50:8"]]
- 008d9a80 bytes 40f90d94
+ 008daa2c bytes 49f90d94
~~~


<a id="compare-c8e79255fcb652c7ad839d5d98e5d692"></a>

### [`008d9a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a94.md) → [`008daa40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008daa40.md) FUN_008daa40

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008d2b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md) [`008d79e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d79e4.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008d3b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d3/008d3b38.md) [`008d8990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d8/008d8990.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d9ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a94.md#insn-008d9ac8) · [`008d9ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a94.md#insn-008d9ad0)
- 新版 [`008daa74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008daa40.md#insn-008daa74) · [`008daa7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008daa40.md#insn-008daa7c)

~~~diff
- 008d9ac8 ["INT_ADD", "register:40f0:8", ["const:8d9ac8:8", "const:4:8"]]
- 008d9ac8 ["CALL", null, ["callee:008d8990:8"]]
+ 008daa74 ["INT_ADD", "register:40f0:8", ["const:8daa74:8", "const:4:8"]]
+ 008daa74 ["CALL", null, ["callee:008d8990:8"]]
- 008d9ac8 bytes c7f7ff97
+ 008daa74 bytes c7f7ff97
- 008d9ad0 ["INT_ADD", "register:40f0:8", ["const:8d9ad0:8", "const:4:8"]]
- 008d9ad0 ["CALL", null, ["callee:008ba17c:8"]]
+ 008daa7c ["INT_ADD", "register:40f0:8", ["const:8daa7c:8", "const:4:8"]]
+ 008daa7c ["CALL", null, ["callee:008ba17c:8"]]
- 008d9ad0 bytes c07dff97
+ 008daa7c bytes c07dff97
~~~


<a id="compare-500e123813951f84e9e7e528155096f0"></a>

### [`008da7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008da7a8.md) → [`008db754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008db754.md) FUN_008db754

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008d648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d648c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008da7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008da7a8.md#insn-008da7e4)
- 新版 [`008db790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008db754.md#insn-008db790)

~~~diff
- 008da7e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008da7e4 ["INT_ADD", "register:40f0:8", ["const:8da7e4:8", "const:4:8"]]
- 008da7e4 ["CALLIND", null, ["register:0:8"]]
+ 008db790 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008db790 ["INT_ADD", "register:40f0:8", ["const:8db790:8", "const:4:8"]]
+ 008db790 ["CALLIND", null, ["register:0:8"]]
- 008da7e4 bytes 00013fd6
+ 008db790 bytes 00013fd6
~~~


<a id="compare-abd203938290840dadf6aced25eec09b"></a>

### [`008daeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daeac.md) → [`008dbe58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbe58.md) FUN_008dbe58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008d7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7ce0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008daee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daeac.md#insn-008daee8)
- 新版 [`008dbe94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbe58.md#insn-008dbe94)

~~~diff
- 008daee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008daee8 ["INT_ADD", "register:40f0:8", ["const:8daee8:8", "const:4:8"]]
- 008daee8 ["CALLIND", null, ["register:0:8"]]
+ 008dbe94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dbe94 ["INT_ADD", "register:40f0:8", ["const:8dbe94:8", "const:4:8"]]
+ 008dbe94 ["CALLIND", null, ["register:0:8"]]
- 008daee8 bytes 00013fd6
+ 008dbe94 bytes 00013fd6
~~~


<a id="compare-16781a8ddb08bedfca050b880658aa0e"></a>

### [`008daefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daefc.md) → [`008dbea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbea8.md) FUN_008dbea8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00865b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865b4c.md) [`008d615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d615c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0059728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md) [`00866af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866af8.md) [`008d7108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7108.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008daf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daefc.md#insn-008daf40) · [`008daf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daefc.md#insn-008daf58) · [`008daf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daefc.md#insn-008daf8c)
- 新版 [`008dbeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbea8.md#insn-008dbeec) · [`008dbf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbea8.md#insn-008dbf04) · [`008dbf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbea8.md#insn-008dbf38)

~~~diff
- 008daf40 ["COPY", "register:0:8", ["register:4040:8"]]
- 008daf40 ["INT_ADD", "register:40f0:8", ["const:8daf40:8", "const:4:8"]]
- 008daf40 ["CALLIND", null, ["register:0:8"]]
+ 008dbeec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dbeec ["INT_ADD", "register:40f0:8", ["const:8dbeec:8", "const:4:8"]]
+ 008dbeec ["CALLIND", null, ["register:0:8"]]
- 008daf40 bytes 00013fd6
+ 008dbeec bytes 00013fd6
- 008daf58 ["COPY", "register:0:8", ["register:4048:8"]]
- 008daf58 ["INT_ADD", "register:40f0:8", ["const:8daf58:8", "const:4:8"]]
- 008daf58 ["CALLIND", null, ["register:0:8"]]
+ 008dbf04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008dbf04 ["INT_ADD", "register:40f0:8", ["const:8dbf04:8", "const:4:8"]]
+ 008dbf04 ["CALLIND", null, ["register:0:8"]]
- 008daf58 bytes 20013fd6
+ 008dbf04 bytes 20013fd6
- 008daf8c ["COPY", "register:0:8", ["register:4040:8"]]
- 008daf8c ["INT_ADD", "register:40f0:8", ["const:8daf8c:8", "const:4:8"]]
- 008daf8c ["CALLIND", null, ["register:0:8"]]
+ 008dbf38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dbf38 ["INT_ADD", "register:40f0:8", ["const:8dbf38:8", "const:4:8"]]
+ 008dbf38 ["CALLIND", null, ["register:0:8"]]
- 008daf8c bytes 00013fd6
+ 008dbf38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27aa25e1ca64abd833057248dcc468cb"></a>

### [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md) → [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md) FUN_008e0418

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008dd084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dd084.md) [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md) [`008df938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md) [`008df938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md) [`008dfdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md)
- 新版 呼出元 3件 [`008de030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008de030.md) [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md) [`008e08e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md) · 呼出先 4件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md) [`008e08e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md) [`008e0d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008df4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md#insn-008df4c8) · [`008df4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md#insn-008df4d8) · [`008df4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md#insn-008df4e8)
- 新版 [`008e0474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md#insn-008e0474) · [`008e0484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md#insn-008e0484) · [`008e0494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md#insn-008e0494)

~~~diff
- 008df4c8 ["INT_ADD", "register:40f0:8", ["const:8df4c8:8", "const:4:8"]]
- 008df4c8 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0474 ["INT_ADD", "register:40f0:8", ["const:8e0474:8", "const:4:8"]]
+ 008e0474 ["CALL", null, ["callee:008524fc:8"]]
- 008df4c8 bytes 22c8fd97
+ 008e0474 bytes 22c8fd97
- 008df4d8 ["INT_ADD", "register:40f0:8", ["const:8df4d8:8", "const:4:8"]]
- 008df4d8 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0484 ["INT_ADD", "register:40f0:8", ["const:8e0484:8", "const:4:8"]]
+ 008e0484 ["CALL", null, ["callee:008524fc:8"]]
- 008df4d8 bytes 1ec8fd97
+ 008e0484 bytes 1ec8fd97
- 008df4e8 ["INT_ADD", "register:40f0:8", ["const:8df4e8:8", "const:4:8"]]
- 008df4e8 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0494 ["INT_ADD", "register:40f0:8", ["const:8e0494:8", "const:4:8"]]
+ 008e0494 ["CALL", null, ["callee:008524fc:8"]]
- 008df4e8 bytes 1ac8fd97
+ 008e0494 bytes 1ac8fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2d79d27814bb5e9dc1c28302a99843"></a>

### [`008df938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md) → [`008e08e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md) FUN_008e08e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md)
- 新版 呼出元 1件 [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md) · 呼出先 2件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008df980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md#insn-008df980) · [`008df990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md#insn-008df990) · [`008df9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df938.md#insn-008df9a0)
- 新版 [`008e092c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md#insn-008e092c) · [`008e093c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md#insn-008e093c) · [`008e094c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e08e4.md#insn-008e094c)

~~~diff
- 008df980 ["INT_ADD", "register:40f0:8", ["const:8df980:8", "const:4:8"]]
- 008df980 ["CALL", null, ["callee:008524fc:8"]]
+ 008e092c ["INT_ADD", "register:40f0:8", ["const:8e092c:8", "const:4:8"]]
+ 008e092c ["CALL", null, ["callee:008524fc:8"]]
- 008df980 bytes f4c6fd97
+ 008e092c bytes f4c6fd97
- 008df990 ["INT_ADD", "register:40f0:8", ["const:8df990:8", "const:4:8"]]
- 008df990 ["CALL", null, ["callee:008524fc:8"]]
+ 008e093c ["INT_ADD", "register:40f0:8", ["const:8e093c:8", "const:4:8"]]
+ 008e093c ["CALL", null, ["callee:008524fc:8"]]
- 008df990 bytes f0c6fd97
+ 008e093c bytes f0c6fd97
- 008df9a0 ["INT_ADD", "register:40f0:8", ["const:8df9a0:8", "const:4:8"]]
- 008df9a0 ["CALL", null, ["callee:008524fc:8"]]
+ 008e094c ["INT_ADD", "register:40f0:8", ["const:8e094c:8", "const:4:8"]]
+ 008e094c ["CALL", null, ["callee:008524fc:8"]]
- 008df9a0 bytes ecc6fd97
+ 008e094c bytes ecc6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a4bbe6054f9e448f464f4b7d8a8cd52"></a>

### [`008dfdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md) → [`008e0d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md) FUN_008e0d70

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008df46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008df46c.md) [`008dfdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008dfdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`008e0418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0418.md) [`008e0d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008e0d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008dfe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md#insn-008dfe28) · [`008dfe38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md#insn-008dfe38) · [`008dfe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008df/008dfdc4.md#insn-008dfe48)
- 新版 [`008e0dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md#insn-008e0dd4) · [`008e0de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md#insn-008e0de4) · [`008e0df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e0/008e0d70.md#insn-008e0df4)

~~~diff
- 008dfe28 ["INT_ADD", "register:40f0:8", ["const:8dfe28:8", "const:4:8"]]
- 008dfe28 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0dd4 ["INT_ADD", "register:40f0:8", ["const:8e0dd4:8", "const:4:8"]]
+ 008e0dd4 ["CALL", null, ["callee:008524fc:8"]]
- 008dfe28 bytes cac5fd97
+ 008e0dd4 bytes cac5fd97
- 008dfe38 ["INT_ADD", "register:40f0:8", ["const:8dfe38:8", "const:4:8"]]
- 008dfe38 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0de4 ["INT_ADD", "register:40f0:8", ["const:8e0de4:8", "const:4:8"]]
+ 008e0de4 ["CALL", null, ["callee:008524fc:8"]]
- 008dfe38 bytes c6c5fd97
+ 008e0de4 bytes c6c5fd97
- 008dfe48 ["INT_ADD", "register:40f0:8", ["const:8dfe48:8", "const:4:8"]]
- 008dfe48 ["CALL", null, ["callee:008524fc:8"]]
+ 008e0df4 ["INT_ADD", "register:40f0:8", ["const:8e0df4:8", "const:4:8"]]
+ 008e0df4 ["CALL", null, ["callee:008524fc:8"]]
- 008dfe48 bytes c2c5fd97
+ 008e0df4 bytes c2c5fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2cf18307764955cc2aefedff5e4493a"></a>

### [`008e0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md) → [`008e15f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md) FUN_008e15f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008dd148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dd148.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0086a008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a008.md) [`008e07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e07e8.md) [`008e0a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a80.md) [`008e0a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a94.md)
- 新版 呼出元 1件 [`008de0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008de0f4.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0086afb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086afb4.md) [`008e1794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1794.md) [`008e1a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a2c.md) [`008e1a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e06cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md#insn-008e06cc) · [`008e06f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md#insn-008e06f0) · [`008e0720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md#insn-008e0720)
- 新版 [`008e1678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md#insn-008e1678) · [`008e169c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md#insn-008e169c) · [`008e16cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md#insn-008e16cc)

~~~diff
- 008e06cc ["INT_ADD", "register:40f0:8", ["const:8e06cc:8", "const:4:8"]]
- 008e06cc ["CALL", null, ["callee:00c58f30:8"]]
+ 008e1678 ["INT_ADD", "register:40f0:8", ["const:8e1678:8", "const:4:8"]]
+ 008e1678 ["CALL", null, ["callee:00c58f30:8"]]
- 008e06cc bytes 25de0d94
+ 008e1678 bytes 2ede0d94
- 008e06f0 ["INT_ADD", "register:40f0:8", ["const:8e06f0:8", "const:4:8"]]
- 008e06f0 ["CALL", null, ["callee:008e1794:8"]]
+ 008e169c ["INT_ADD", "register:40f0:8", ["const:8e169c:8", "const:4:8"]]
+ 008e169c ["CALL", null, ["callee:008e1794:8"]]
- 008e06f0 bytes 3e000094
+ 008e169c bytes 3e000094
- 008e0720 ["INT_ADD", "register:40f0:8", ["const:8e0720:8", "const:4:8"]]
- 008e0720 ["CALL", null, ["callee:008e1a40:8"]]
+ 008e16cc ["INT_ADD", "register:40f0:8", ["const:8e16cc:8", "const:4:8"]]
+ 008e16cc ["CALL", null, ["callee:008e1a40:8"]]
- 008e0720 bytes dd000094
+ 008e16cc bytes dd000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f193cc87aa8ea5a8452a6e816c947ceb"></a>

### [`008e07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e07e8.md) → [`008e1794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1794.md) FUN_008e1794

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008dd148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dd148.md) [`008e0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md) · 呼出先 2件 [`006d5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 2件 [`008de0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008de0f4.md) [`008e15f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md) · 呼出先 2件 [`006d62ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e0818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e07e8.md#insn-008e0818) · [`008e084c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e07e8.md#insn-008e084c) · [`008e0870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e07e8.md#insn-008e0870)
- 新版 [`008e17c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1794.md#insn-008e17c4) · [`008e17f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1794.md#insn-008e17f8) · [`008e181c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1794.md#insn-008e181c)

~~~diff
- 008e0818 ["INT_ADD", "register:40f0:8", ["const:8e0818:8", "const:4:8"]]
- 008e0818 ["CALL", null, ["callee:00c54d60:8"]]
+ 008e17c4 ["INT_ADD", "register:40f0:8", ["const:8e17c4:8", "const:4:8"]]
+ 008e17c4 ["CALL", null, ["callee:00c54d60:8"]]
- 008e0818 bytes 56cd0d94
+ 008e17c4 bytes 67cd0d94
- 008e084c ["INT_ADD", "register:40f0:8", ["const:8e084c:8", "const:4:8"]]
- 008e084c ["CALL", null, ["callee:006d62ac:8"]]
+ 008e17f8 ["INT_ADD", "register:40f0:8", ["const:8e17f8:8", "const:4:8"]]
+ 008e17f8 ["CALL", null, ["callee:006d62ac:8"]]
- 008e084c bytes acd5f797
+ 008e17f8 bytes add2f797
- 008e0870 ["INT_ADD", "register:40f0:8", ["const:8e0870:8", "const:4:8"]]
- 008e0870 ["CALL", null, ["callee:006d62ac:8"]]
+ 008e181c ["INT_ADD", "register:40f0:8", ["const:8e181c:8", "const:4:8"]]
+ 008e181c ["CALL", null, ["callee:006d62ac:8"]]
- 008e0870 bytes a3d5f797
+ 008e181c bytes a4d2f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fccfb931d4a75122ff5bbe39958dcea"></a>

### [`008e0a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a2c.md) → [`008e19d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e19d8.md) FUN_008e19d8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a008.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086afb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086afb4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e0a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a2c.md#insn-008e0a50)
- 新版 [`008e19fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e19d8.md#insn-008e19fc)

~~~diff
- 008e0a50 ["INT_ADD", "register:40f0:8", ["const:8e0a50:8", "const:4:8"]]
- 008e0a50 ["CALL", null, ["callee:0086afb4:8"]]
+ 008e19fc ["INT_ADD", "register:40f0:8", ["const:8e19fc:8", "const:4:8"]]
+ 008e19fc ["CALL", null, ["callee:0086afb4:8"]]
- 008e0a50 bytes 6e25fe97
+ 008e19fc bytes 6e25fe97
~~~


<a id="compare-8799d76852f20595784793819f233113"></a>

### [`008e207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e207c.md) → [`008e3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e3028.md) FUN_008e3028

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e49f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`008e59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e21c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e207c.md#insn-008e21c0) · [`008e21f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e207c.md#insn-008e21f4) · [`008e2244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e207c.md#insn-008e2244)
- 新版 [`008e316c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e3028.md#insn-008e316c) · [`008e31a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e3028.md#insn-008e31a0) · [`008e31f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e3028.md#insn-008e31f0)

~~~diff
- 008e21c0 ["INT_ADD", "register:40f0:8", ["const:8e21c0:8", "const:4:8"]]
- 008e21c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e316c ["INT_ADD", "register:40f0:8", ["const:8e316c:8", "const:4:8"]]
+ 008e316c ["CALL", null, ["callee:00c58f30:8"]]
- 008e21c0 bytes 68d70d94
+ 008e316c bytes 71d70d94
- 008e21f4 ["INT_ADD", "register:40f0:8", ["const:8e21f4:8", "const:4:8"]]
- 008e21f4 ["CALL", null, ["callee:0043bf04:8"]]
+ 008e31a0 ["INT_ADD", "register:40f0:8", ["const:8e31a0:8", "const:4:8"]]
+ 008e31a0 ["CALL", null, ["callee:0043bf04:8"]]
- 008e21f4 bytes 7c66ed97
+ 008e31a0 bytes 5963ed97
- 008e2244 ["INT_ADD", "register:40f0:8", ["const:8e2244:8", "const:4:8"]]
- 008e2244 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e31f0 ["INT_ADD", "register:40f0:8", ["const:8e31f0:8", "const:4:8"]]
+ 008e31f0 ["CALL", null, ["callee:00c58f30:8"]]
- 008e2244 bytes 47d70d94
+ 008e31f0 bytes 50d70d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-051d3ce5a496aa7b129bfb47f6606fc6"></a>

### [`008e2840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2840.md) → [`008e37ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e37ec.md) FUN_008e37ec

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e49f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md) · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md) · 呼出先 3件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e2864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2840.md#insn-008e2864) · [`008e28a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2840.md#insn-008e28a0) · [`008e28bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2840.md#insn-008e28bc)
- 新版 [`008e3810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e37ec.md#insn-008e3810) · [`008e384c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e37ec.md#insn-008e384c) · [`008e3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e37ec.md#insn-008e3868)

~~~diff
- 008e2864 ["INT_ADD", "register:40f0:8", ["const:8e2864:8", "const:4:8"]]
- 008e2864 ["CALL", null, ["callee:0046db10:8"]]
+ 008e3810 ["INT_ADD", "register:40f0:8", ["const:8e3810:8", "const:4:8"]]
+ 008e3810 ["CALL", null, ["callee:0046db10:8"]]
- 008e2864 bytes e32bee97
+ 008e3810 bytes c028ee97
- 008e28a0 ["INT_ADD", "register:40f0:8", ["const:8e28a0:8", "const:4:8"]]
- 008e28a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e384c ["INT_ADD", "register:40f0:8", ["const:8e384c:8", "const:4:8"]]
+ 008e384c ["CALL", null, ["callee:00c58f30:8"]]
- 008e28a0 bytes b0d50d94
+ 008e384c bytes b9d50d94
- 008e28bc ["INT_ADD", "register:40f0:8", ["const:8e28bc:8", "const:4:8"]]
- 008e28bc ["CALL", null, ["callee:00c58f30:8"]]
+ 008e3868 ["INT_ADD", "register:40f0:8", ["const:8e3868:8", "const:4:8"]]
+ 008e3868 ["CALL", null, ["callee:00c58f30:8"]]
- 008e28bc bytes a9d50d94
+ 008e3868 bytes b2d50d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb712cf43fa719e091999bff312daa6"></a>

### [`008e3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3148.md) → [`008e40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e40f4.md) FUN_008e40f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`008e82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`008e9264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e3188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3148.md#insn-008e3188) · [`008e3198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3148.md#insn-008e3198) · [`008e31c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3148.md#insn-008e31c0)
- 新版 [`008e4134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e40f4.md#insn-008e4134) · [`008e4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e40f4.md#insn-008e4144) · [`008e416c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e40f4.md#insn-008e416c)

~~~diff
- 008e3188 ["INT_ADD", "register:40f0:8", ["const:8e3188:8", "const:4:8"]]
- 008e3188 ["CALL", null, ["callee:00487c9c:8"]]
+ 008e4134 ["INT_ADD", "register:40f0:8", ["const:8e4134:8", "const:4:8"]]
+ 008e4134 ["CALL", null, ["callee:00487c9c:8"]]
- 008e3188 bytes fd91ee97
+ 008e4134 bytes da8eee97
- 008e3198 ["INT_ADD", "register:40f0:8", ["const:8e3198:8", "const:4:8"]]
- 008e3198 ["CALL", null, ["callee:00487c9c:8"]]
+ 008e4144 ["INT_ADD", "register:40f0:8", ["const:8e4144:8", "const:4:8"]]
+ 008e4144 ["CALL", null, ["callee:00487c9c:8"]]
- 008e3198 bytes f991ee97
+ 008e4144 bytes d68eee97
- 008e31c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008e31c0 ["INT_ADD", "register:40f0:8", ["const:8e31c0:8", "const:4:8"]]
- 008e31c0 ["CALLIND", null, ["register:0:8"]]
+ 008e416c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008e416c ["INT_ADD", "register:40f0:8", ["const:8e416c:8", "const:4:8"]]
+ 008e416c ["CALLIND", null, ["register:0:8"]]
- 008e31c0 bytes 00013fd6
+ 008e416c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dfc3459b760f8d9b5ab8e185b9cdb14"></a>

### [`008e3368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3368.md) → [`008e4314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4314.md) FUN_008e4314

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 1件 [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3368.md#insn-008e338c) · [`008e339c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3368.md#insn-008e339c) · [`008e33ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3368.md#insn-008e33ac)
- 新版 [`008e4338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4314.md#insn-008e4338) · [`008e4348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4314.md#insn-008e4348) · [`008e4358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4314.md#insn-008e4358)

~~~diff
- 008e338c ["INT_ADD", "register:40f0:8", ["const:8e338c:8", "const:4:8"]]
- 008e338c ["CALL", null, ["callee:00487c9c:8"]]
+ 008e4338 ["INT_ADD", "register:40f0:8", ["const:8e4338:8", "const:4:8"]]
+ 008e4338 ["CALL", null, ["callee:00487c9c:8"]]
- 008e338c bytes 7c91ee97
+ 008e4338 bytes 598eee97
- 008e339c ["INT_ADD", "register:40f0:8", ["const:8e339c:8", "const:4:8"]]
- 008e339c ["CALL", null, ["callee:00487c9c:8"]]
+ 008e4348 ["INT_ADD", "register:40f0:8", ["const:8e4348:8", "const:4:8"]]
+ 008e4348 ["CALL", null, ["callee:00487c9c:8"]]
- 008e339c bytes 7891ee97
+ 008e4348 bytes 558eee97
- 008e33ac ["INT_ADD", "register:40f0:8", ["const:8e33ac:8", "const:4:8"]]
- 008e33ac ["CALL", null, ["callee:00487c9c:8"]]
+ 008e4358 ["INT_ADD", "register:40f0:8", ["const:8e4358:8", "const:4:8"]]
+ 008e4358 ["CALL", null, ["callee:00487c9c:8"]]
- 008e33ac bytes 7491ee97
+ 008e4358 bytes 518eee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a161fbfc8c74d3f695ddf5a6ebca811"></a>

### [`008e3ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3ce0.md) → [`008e4c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4c8c.md) FUN_008e4c8c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008e9390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9390.md) [`008e9ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9ce0.md) [`008ea310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea310.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 3件 [`008ea33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea33c.md) [`008eac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac8c.md) [`008eb2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb2bc.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e3cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3ce0.md#insn-008e3cf0) · [`008e3d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3ce0.md#insn-008e3d00) · [`008e3d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3ce0.md#insn-008e3d08)
- 新版 [`008e4c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4c8c.md#insn-008e4c9c) · [`008e4cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4c8c.md#insn-008e4cac) · [`008e4cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4c8c.md#insn-008e4cb4)

~~~diff
- 008e3cf0 ["INT_ADD", "register:40f0:8", ["const:8e3cf0:8", "const:4:8"]]
- 008e3cf0 ["CALL", null, ["callee:008524fc:8"]]
+ 008e4c9c ["INT_ADD", "register:40f0:8", ["const:8e4c9c:8", "const:4:8"]]
+ 008e4c9c ["CALL", null, ["callee:008524fc:8"]]
- 008e3cf0 bytes 18b6fd97
+ 008e4c9c bytes 18b6fd97
- 008e3d00 ["INT_ADD", "register:40f0:8", ["const:8e3d00:8", "const:4:8"]]
- 008e3d00 ["CALL", null, ["callee:008b89cc:8"]]
+ 008e4cac ["INT_ADD", "register:40f0:8", ["const:8e4cac:8", "const:4:8"]]
+ 008e4cac ["CALL", null, ["callee:008b89cc:8"]]
- 008e3d00 bytes 484fff97
+ 008e4cac bytes 484fff97
- 008e3d08 ["INT_ADD", "register:40f0:8", ["const:8e3d08:8", "const:4:8"]]
- 008e3d08 ["CALL", null, ["callee:008b7f1c:8"]]
+ 008e4cb4 ["INT_ADD", "register:40f0:8", ["const:8e4cb4:8", "const:4:8"]]
+ 008e4cb4 ["CALL", null, ["callee:008b7f1c:8"]]
- 008e3d08 bytes 9a4cff97
+ 008e4cb4 bytes 9a4cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-592abb20c29e24d9da344d3f9117c2bc"></a>

### [`008e4470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e4470.md) → [`008e541c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e541c.md) FUN_008e541c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)
- 新版 呼出元 1件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) · 呼出先 2件 [`0046eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb24.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e44d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e4470.md#insn-008e44d4) · [`008e44dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e4470.md#insn-008e44dc) · [`008e44e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e4470.md#insn-008e44e8)
- 新版 [`008e5480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e541c.md#insn-008e5480) · [`008e5488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e541c.md#insn-008e5488) · [`008e5494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e541c.md#insn-008e5494)

~~~diff
- 008e44d4 ["INT_ADD", "register:40f0:8", ["const:8e44d4:8", "const:4:8"]]
- 008e44d4 ["CALL", null, ["callee:0046f258:8"]]
+ 008e5480 ["INT_ADD", "register:40f0:8", ["const:8e5480:8", "const:4:8"]]
+ 008e5480 ["CALL", null, ["callee:0046f258:8"]]
- 008e44d4 bytes 992aee97
+ 008e5480 bytes 7627ee97
- 008e44dc ["INT_ADD", "register:40f0:8", ["const:8e44dc:8", "const:4:8"]]
- 008e44dc ["CALL", null, ["callee:0046eb24:8"]]
+ 008e5488 ["INT_ADD", "register:40f0:8", ["const:8e5488:8", "const:4:8"]]
+ 008e5488 ["CALL", null, ["callee:0046eb24:8"]]
- 008e44dc bytes ca28ee97
+ 008e5488 bytes a725ee97
- 008e44e8 ["INT_ADD", "register:40f0:8", ["const:8e44e8:8", "const:4:8"]]
- 008e44e8 ["CALL", null, ["callee:0046eb24:8"]]
+ 008e5494 ["INT_ADD", "register:40f0:8", ["const:8e5494:8", "const:4:8"]]
+ 008e5494 ["CALL", null, ["callee:0046eb24:8"]]
- 008e44e8 bytes c728ee97
+ 008e5494 bytes a425ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b61d34531b104b51caea7eca6e9bac31"></a>

### [`008e45b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45b4.md) → [`008e5560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5560.md) FUN_008e5560

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00869c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00869/00869c24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e45cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45b4.md#insn-008e45cc)
- 新版 [`008e5578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5560.md#insn-008e5578)

~~~diff
- 008e45cc ["INT_ADD", "register:40f0:8", ["const:8e45cc:8", "const:4:8"]]
- 008e45cc ["CALL", null, ["callee:00869c24:8"]]
+ 008e5578 ["INT_ADD", "register:40f0:8", ["const:8e5578:8", "const:4:8"]]
+ 008e5578 ["CALL", null, ["callee:00869c24:8"]]
- 008e45cc bytes ab11fe97
+ 008e5578 bytes ab11fe97
~~~


<a id="compare-3b749057150d5df327022dbcd875cd26"></a>

### [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) → [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) FUN_008e5590

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008e3da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md) [`008e9614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md) · 呼出先 12件 [`008e8344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8344.md) [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) [`008e8608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8608.md) [`008e8690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md) [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md)
- 新版 呼出元 2件 [`008e4d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md) [`008ea5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md) · 呼出先 12件 [`008e92f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e92f0.md) [`008e9368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md) [`008e95b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e95b4.md) [`008e963c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md) [`008e9650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e4630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md#insn-008e4630) · [`008e4684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md#insn-008e4684) · [`008e46a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md#insn-008e46a8)
- 新版 [`008e55dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md#insn-008e55dc) · [`008e5630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md#insn-008e5630) · [`008e5654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md#insn-008e5654)

~~~diff
- 008e4630 ["INT_ADD", "register:40f0:8", ["const:8e4630:8", "const:4:8"]]
- 008e4630 ["CALL", null, ["callee:008e9368:8"]]
+ 008e55dc ["INT_ADD", "register:40f0:8", ["const:8e55dc:8", "const:4:8"]]
+ 008e55dc ["CALL", null, ["callee:008e9368:8"]]
- 008e4630 bytes 630f0094
+ 008e55dc bytes 630f0094
- 008e4684 ["INT_ADD", "register:40f0:8", ["const:8e4684:8", "const:4:8"]]
- 008e4684 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e5630 ["INT_ADD", "register:40f0:8", ["const:8e5630:8", "const:4:8"]]
+ 008e5630 ["CALL", null, ["callee:00c58f30:8"]]
- 008e4684 bytes 37ce0d94
+ 008e5630 bytes 40ce0d94
- 008e46a8 ["INT_ADD", "register:40f0:8", ["const:8e46a8:8", "const:4:8"]]
- 008e46a8 ["CALL", null, ["callee:008e9650:8"]]
+ 008e5654 ["INT_ADD", "register:40f0:8", ["const:8e5654:8", "const:4:8"]]
+ 008e5654 ["CALL", null, ["callee:008e9650:8"]]
- 008e46a8 bytes ff0f0094
+ 008e5654 bytes ff0f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97b082aa4e086b512633cf17c677214f"></a>

### [`008e5108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5108.md) → [`008e60b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e60b4.md) FUN_008e60b4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008e49f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md) [`008e5fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`008e59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md) [`008e6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6f7c.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5108.md#insn-008e5188) · [`008e51e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5108.md#insn-008e51e0) · [`008e5234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5108.md#insn-008e5234)
- 新版 [`008e6134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e60b4.md#insn-008e6134) · [`008e618c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e60b4.md#insn-008e618c) · [`008e61e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e60b4.md#insn-008e61e0)

~~~diff
- 008e5188 ["INT_ADD", "register:40f0:8", ["const:8e5188:8", "const:4:8"]]
- 008e5188 ["CALL", null, ["callee:0043be80:8"]]
+ 008e6134 ["INT_ADD", "register:40f0:8", ["const:8e6134:8", "const:4:8"]]
+ 008e6134 ["CALL", null, ["callee:0043be80:8"]]
- 008e5188 bytes 765aed97
+ 008e6134 bytes 5357ed97
- 008e51e0 ["INT_ADD", "register:40f0:8", ["const:8e51e0:8", "const:4:8"]]
- 008e51e0 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e618c ["INT_ADD", "register:40f0:8", ["const:8e618c:8", "const:4:8"]]
+ 008e618c ["CALL", null, ["callee:00c58f50:8"]]
- 008e51e0 bytes 68cb0d94
+ 008e618c bytes 71cb0d94
- 008e5234 ["INT_ADD", "register:40f0:8", ["const:8e5234:8", "const:4:8"]]
- 008e5234 ["CALL", null, ["callee:00c58f80:8"]]
+ 008e61e0 ["INT_ADD", "register:40f0:8", ["const:8e61e0:8", "const:4:8"]]
+ 008e61e0 ["CALL", null, ["callee:00c58f80:8"]]
- 008e5234 bytes 5fcb0d94
+ 008e61e0 bytes 68cb0d94
~~~


<a id="compare-9ebac756ea42b2c0de82e162f7ed495f"></a>

### [`008e5da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5da8.md) → [`008e6d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6d54.md) FUN_008e6d54

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e5df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5da8.md#insn-008e5df0)
- 新版 [`008e6d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6d54.md#insn-008e6d9c)

~~~diff
- 008e5df0 ["INT_ADD", "register:40f0:8", ["const:8e5df0:8", "const:4:8"]]
- 008e5df0 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e6d9c ["INT_ADD", "register:40f0:8", ["const:8e6d9c:8", "const:4:8"]]
+ 008e6d9c ["CALL", null, ["callee:00c58f50:8"]]
- 008e5df0 bytes 64c80d94
+ 008e6d9c bytes 6dc80d94
~~~


<a id="compare-253714491a2b2351f668b15cbaf3b0c7"></a>

### [`008e5e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e20.md) → [`008e6dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6dcc.md) FUN_008e6dcc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e5e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e20.md#insn-008e5e68)
- 新版 [`008e6e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6dcc.md#insn-008e6e14)

~~~diff
- 008e5e68 ["INT_ADD", "register:40f0:8", ["const:8e5e68:8", "const:4:8"]]
- 008e5e68 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e6e14 ["INT_ADD", "register:40f0:8", ["const:8e6e14:8", "const:4:8"]]
+ 008e6e14 ["CALL", null, ["callee:00c58f50:8"]]
- 008e5e68 bytes 46c80d94
+ 008e6e14 bytes 4fc80d94
~~~


<a id="compare-9366c894f53552be04fa64ba6f5b1bf2"></a>

### [`008e5e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e98.md) → [`008e6e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6e44.md) FUN_008e6e44

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008e76ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e5f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e98.md#insn-008e5f40) · [`008e5f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e98.md#insn-008e5f64) · [`008e5fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e98.md#insn-008e5fcc)
- 新版 [`008e6eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6e44.md#insn-008e6eec) · [`008e6f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6e44.md#insn-008e6f10) · [`008e6f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6e44.md#insn-008e6f78)

~~~diff
- 008e5f40 ["INT_ADD", "register:40f0:8", ["const:8e5f40:8", "const:4:8"]]
- 008e5f40 ["CALL", null, ["callee:0043be80:8"]]
+ 008e6eec ["INT_ADD", "register:40f0:8", ["const:8e6eec:8", "const:4:8"]]
+ 008e6eec ["CALL", null, ["callee:0043be80:8"]]
- 008e5f40 bytes 0857ed97
+ 008e6eec bytes e553ed97
- 008e5f64 ["INT_ADD", "register:40f0:8", ["const:8e5f64:8", "const:4:8"]]
- 008e5f64 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e6f10 ["INT_ADD", "register:40f0:8", ["const:8e6f10:8", "const:4:8"]]
+ 008e6f10 ["CALL", null, ["callee:00c58f50:8"]]
- 008e5f64 bytes 07c80d94
+ 008e6f10 bytes 10c80d94
- 008e5fcc ["INT_ADD", "register:40f0:8", ["const:8e5fcc:8", "const:4:8"]]
- 008e5fcc ["CALL", null, ["callee:00c58f80:8"]]
+ 008e6f78 ["INT_ADD", "register:40f0:8", ["const:8e6f78:8", "const:4:8"]]
+ 008e6f78 ["CALL", null, ["callee:00c58f80:8"]]
- 008e5fcc bytes f9c70d94
+ 008e6f78 bytes 02c80d94
~~~


<a id="compare-0072d4984923e8f64afc2993234ab871"></a>

### [`008e82cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82cc.md) → [`008e9278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9278.md) FUN_008e9278

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82cc.md#insn-008e8314)
- 新版 [`008e92c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9278.md#insn-008e92c0)

~~~diff
- 008e8314 ["INT_ADD", "register:40f0:8", ["const:8e8314:8", "const:4:8"]]
- 008e8314 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e92c0 ["INT_ADD", "register:40f0:8", ["const:8e92c0:8", "const:4:8"]]
+ 008e92c0 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8314 bytes 1bbf0d94
+ 008e92c0 bytes 24bf0d94
~~~


<a id="compare-e1567d3410d8ab1e97db5a89c880729f"></a>

### [`008e8344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8344.md) → [`008e92f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e92f0.md) FUN_008e92f0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8344.md#insn-008e838c)
- 新版 [`008e9338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e92f0.md#insn-008e9338)

~~~diff
- 008e838c ["INT_ADD", "register:40f0:8", ["const:8e838c:8", "const:4:8"]]
- 008e838c ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9338 ["INT_ADD", "register:40f0:8", ["const:8e9338:8", "const:4:8"]]
+ 008e9338 ["CALL", null, ["callee:00c58f50:8"]]
- 008e838c bytes fdbe0d94
+ 008e9338 bytes 06bf0d94
~~~


<a id="compare-3b9c6cc0b59e6b6615bab3376b9817d9"></a>

### [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) → [`008e9368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md) FUN_008e9368

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e8518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8518.md) [`008e85a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`008e94c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e94c4.md) [`008e954c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md#insn-008e8408) · [`008e8488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md#insn-008e8488) · [`008e84d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md#insn-008e84d8)
- 新版 [`008e93b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md#insn-008e93b4) · [`008e9434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md#insn-008e9434) · [`008e9484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md#insn-008e9484)

~~~diff
- 008e8408 ["INT_ADD", "register:40f0:8", ["const:8e8408:8", "const:4:8"]]
- 008e8408 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e93b4 ["INT_ADD", "register:40f0:8", ["const:8e93b4:8", "const:4:8"]]
+ 008e93b4 ["CALL", null, ["callee:00c58f30:8"]]
- 008e8408 bytes d6be0d94
+ 008e93b4 bytes dfbe0d94
- 008e8488 ["INT_ADD", "register:40f0:8", ["const:8e8488:8", "const:4:8"]]
- 008e8488 ["CALL", null, ["callee:0043be80:8"]]
+ 008e9434 ["INT_ADD", "register:40f0:8", ["const:8e9434:8", "const:4:8"]]
+ 008e9434 ["CALL", null, ["callee:0043be80:8"]]
- 008e8488 bytes b64ded97
+ 008e9434 bytes 934aed97
- 008e84d8 ["INT_ADD", "register:40f0:8", ["const:8e84d8:8", "const:4:8"]]
- 008e84d8 ["CALL", null, ["callee:008e954c:8"]]
+ 008e9484 ["INT_ADD", "register:40f0:8", ["const:8e9484:8", "const:4:8"]]
+ 008e9484 ["CALL", null, ["callee:008e954c:8"]]
- 008e84d8 bytes 32000094
+ 008e9484 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c36bff036422cb4392990349e8bb4607"></a>

### [`008e8518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8518.md) → [`008e94c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e94c4.md) FUN_008e94c4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e9368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e857c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8518.md#insn-008e857c)
- 新版 [`008e9528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e94c4.md#insn-008e9528)

~~~diff
- 008e857c ["INT_ADD", "register:40f0:8", ["const:8e857c:8", "const:4:8"]]
- 008e857c ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9528 ["INT_ADD", "register:40f0:8", ["const:8e9528:8", "const:4:8"]]
+ 008e9528 ["CALL", null, ["callee:00c58f50:8"]]
- 008e857c bytes 81be0d94
+ 008e9528 bytes 8abe0d94
~~~


<a id="compare-a64e628d45c7ac6aa2bc6a85368a3288"></a>

### [`008e85b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85b4.md) → [`008e9560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9560.md) FUN_008e9560

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e85f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85b4.md#insn-008e85f4)
- 新版 [`008e95a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9560.md#insn-008e95a0)

~~~diff
- 008e85f4 ["INT_ADD", "register:40f0:8", ["const:8e85f4:8", "const:4:8"]]
- 008e85f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e95a0 ["INT_ADD", "register:40f0:8", ["const:8e95a0:8", "const:4:8"]]
+ 008e95a0 ["CALL", null, ["callee:00c58f50:8"]]
- 008e85f4 bytes 63be0d94
+ 008e95a0 bytes 6cbe0d94
~~~


<a id="compare-ccdac1f0a393ac7b65ea7cf23da574ed"></a>

### [`008e8608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8608.md) → [`008e95b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e95b4.md) FUN_008e95b4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e866c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8608.md#insn-008e866c)
- 新版 [`008e9618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e95b4.md#insn-008e9618)

~~~diff
- 008e866c ["INT_ADD", "register:40f0:8", ["const:8e866c:8", "const:4:8"]]
- 008e866c ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9618 ["INT_ADD", "register:40f0:8", ["const:8e9618:8", "const:4:8"]]
+ 008e9618 ["CALL", null, ["callee:00c58f50:8"]]
- 008e866c bytes 45be0d94
+ 008e9618 bytes 4ebe0d94
~~~


<a id="compare-73fa6977291544495ef1015d8524c575"></a>

### [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md) → [`008e9650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md) FUN_008e9650

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 7件 [`008e82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md) [`008e880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e880c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 7件 [`008e9264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md) [`008e97b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e97b8.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md#insn-008e8760) · [`008e8778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md#insn-008e8778) · [`008e87cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md#insn-008e87cc)
- 新版 [`008e970c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md#insn-008e970c) · [`008e9724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md#insn-008e9724) · [`008e9778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md#insn-008e9778)

~~~diff
- 008e8760 ["INT_ADD", "register:40f0:8", ["const:8e8760:8", "const:4:8"]]
- 008e8760 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e970c ["INT_ADD", "register:40f0:8", ["const:8e970c:8", "const:4:8"]]
+ 008e970c ["CALL", null, ["callee:00c58f30:8"]]
- 008e8760 bytes 00be0d94
+ 008e970c bytes 09be0d94
- 008e8778 ["INT_ADD", "register:40f0:8", ["const:8e8778:8", "const:4:8"]]
- 008e8778 ["CALL", null, ["callee:00c590a0:8"]]
+ 008e9724 ["INT_ADD", "register:40f0:8", ["const:8e9724:8", "const:4:8"]]
+ 008e9724 ["CALL", null, ["callee:00c590a0:8"]]
- 008e8778 bytes 56be0d94
+ 008e9724 bytes 5fbe0d94
- 008e87cc ["INT_ADD", "register:40f0:8", ["const:8e87cc:8", "const:4:8"]]
- 008e87cc ["CALL", null, ["callee:008e9264:8"]]
+ 008e9778 ["INT_ADD", "register:40f0:8", ["const:8e9778:8", "const:4:8"]]
+ 008e9778 ["CALL", null, ["callee:008e9264:8"]]
- 008e87cc bytes bbfeff97
+ 008e9778 bytes bbfeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b4152bfcc1dad7752ebf6ac1ce790c"></a>

### [`008e880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e880c.md) → [`008e97b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e97b8.md) FUN_008e97b8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e9650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e884c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e880c.md#insn-008e884c)
- 新版 [`008e97f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e97b8.md#insn-008e97f8)

~~~diff
- 008e884c ["INT_ADD", "register:40f0:8", ["const:8e884c:8", "const:4:8"]]
- 008e884c ["CALL", null, ["callee:00c58f50:8"]]
+ 008e97f8 ["INT_ADD", "register:40f0:8", ["const:8e97f8:8", "const:4:8"]]
+ 008e97f8 ["CALL", null, ["callee:00c58f50:8"]]
- 008e884c bytes cdbd0d94
+ 008e97f8 bytes d6bd0d94
~~~


<a id="compare-49eb8892311ad101e874d0a9d5771a0d"></a>

### [`008e8874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md) → [`008e9820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md) FUN_008e9820

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e89d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e89d0.md) [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`008e997c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e997c.md) [`008e9a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e88c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md#insn-008e88c0) · [`008e8940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md#insn-008e8940) · [`008e8990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md#insn-008e8990)
- 新版 [`008e986c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md#insn-008e986c) · [`008e98ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md#insn-008e98ec) · [`008e993c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md#insn-008e993c)

~~~diff
- 008e88c0 ["INT_ADD", "register:40f0:8", ["const:8e88c0:8", "const:4:8"]]
- 008e88c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e986c ["INT_ADD", "register:40f0:8", ["const:8e986c:8", "const:4:8"]]
+ 008e986c ["CALL", null, ["callee:00c58f30:8"]]
- 008e88c0 bytes a8bd0d94
+ 008e986c bytes b1bd0d94
- 008e8940 ["INT_ADD", "register:40f0:8", ["const:8e8940:8", "const:4:8"]]
- 008e8940 ["CALL", null, ["callee:0043be80:8"]]
+ 008e98ec ["INT_ADD", "register:40f0:8", ["const:8e98ec:8", "const:4:8"]]
+ 008e98ec ["CALL", null, ["callee:0043be80:8"]]
- 008e8940 bytes 884ced97
+ 008e98ec bytes 6549ed97
- 008e8990 ["INT_ADD", "register:40f0:8", ["const:8e8990:8", "const:4:8"]]
- 008e8990 ["CALL", null, ["callee:008e9a04:8"]]
+ 008e993c ["INT_ADD", "register:40f0:8", ["const:8e993c:8", "const:4:8"]]
+ 008e993c ["CALL", null, ["callee:008e9a04:8"]]
- 008e8990 bytes 32000094
+ 008e993c bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-303d84675fb840a7187ef2efcbb66682"></a>

### [`008e89d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e89d0.md) → [`008e997c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e997c.md) FUN_008e997c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e9820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e89d0.md#insn-008e8a34)
- 新版 [`008e99e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e997c.md#insn-008e99e0)

~~~diff
- 008e8a34 ["INT_ADD", "register:40f0:8", ["const:8e8a34:8", "const:4:8"]]
- 008e8a34 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e99e0 ["INT_ADD", "register:40f0:8", ["const:8e99e0:8", "const:4:8"]]
+ 008e99e0 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8a34 bytes 53bd0d94
+ 008e99e0 bytes 5cbd0d94
~~~


<a id="compare-1dcd004ef0dca4be5edd5c1a9d9fc548"></a>

### [`008e8a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a6c.md) → [`008e9a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a18.md) FUN_008e9a18

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a6c.md#insn-008e8aac)
- 新版 [`008e9a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a18.md#insn-008e9a58)

~~~diff
- 008e8aac ["INT_ADD", "register:40f0:8", ["const:8e8aac:8", "const:4:8"]]
- 008e8aac ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9a58 ["INT_ADD", "register:40f0:8", ["const:8e9a58:8", "const:4:8"]]
+ 008e9a58 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8aac bytes 35bd0d94
+ 008e9a58 bytes 3ebd0d94
~~~


<a id="compare-11bae08a7d5d62f797b9a8ba1be6482a"></a>

### [`008e8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md) → [`008e9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md) FUN_008e9a6c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8c1c.md) [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`008e9bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9bc8.md) [`008e9c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md#insn-008e8b0c) · [`008e8b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md#insn-008e8b8c) · [`008e8bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md#insn-008e8bdc)
- 新版 [`008e9ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md#insn-008e9ab8) · [`008e9b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md#insn-008e9b38) · [`008e9b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md#insn-008e9b88)

~~~diff
- 008e8b0c ["INT_ADD", "register:40f0:8", ["const:8e8b0c:8", "const:4:8"]]
- 008e8b0c ["CALL", null, ["callee:00c58f30:8"]]
+ 008e9ab8 ["INT_ADD", "register:40f0:8", ["const:8e9ab8:8", "const:4:8"]]
+ 008e9ab8 ["CALL", null, ["callee:00c58f30:8"]]
- 008e8b0c bytes 15bd0d94
+ 008e9ab8 bytes 1ebd0d94
- 008e8b8c ["INT_ADD", "register:40f0:8", ["const:8e8b8c:8", "const:4:8"]]
- 008e8b8c ["CALL", null, ["callee:0043be80:8"]]
+ 008e9b38 ["INT_ADD", "register:40f0:8", ["const:8e9b38:8", "const:4:8"]]
+ 008e9b38 ["CALL", null, ["callee:0043be80:8"]]
- 008e8b8c bytes f54bed97
+ 008e9b38 bytes d248ed97
- 008e8bdc ["INT_ADD", "register:40f0:8", ["const:8e8bdc:8", "const:4:8"]]
- 008e8bdc ["CALL", null, ["callee:008e9c50:8"]]
+ 008e9b88 ["INT_ADD", "register:40f0:8", ["const:8e9b88:8", "const:4:8"]]
+ 008e9b88 ["CALL", null, ["callee:008e9c50:8"]]
- 008e8bdc bytes 32000094
+ 008e9b88 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3990ed9caeaba7c74160a2840298d14f"></a>

### [`008e8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8c1c.md) → [`008e9bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9bc8.md) FUN_008e9bc8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8c1c.md#insn-008e8c80)
- 新版 [`008e9c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9bc8.md#insn-008e9c2c)

~~~diff
- 008e8c80 ["INT_ADD", "register:40f0:8", ["const:8e8c80:8", "const:4:8"]]
- 008e8c80 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9c2c ["INT_ADD", "register:40f0:8", ["const:8e9c2c:8", "const:4:8"]]
+ 008e9c2c ["CALL", null, ["callee:00c58f50:8"]]
- 008e8c80 bytes c0bc0d94
+ 008e9c2c bytes c9bc0d94
~~~


<a id="compare-4e0018cb149e7095bec69193c5dfff5c"></a>

### [`008e8cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8cb8.md) → [`008e9c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c64.md) FUN_008e9c64

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8cb8.md#insn-008e8cf8)
- 新版 [`008e9ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c64.md#insn-008e9ca4)

~~~diff
- 008e8cf8 ["INT_ADD", "register:40f0:8", ["const:8e8cf8:8", "const:4:8"]]
- 008e8cf8 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9ca4 ["INT_ADD", "register:40f0:8", ["const:8e9ca4:8", "const:4:8"]]
+ 008e9ca4 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8cf8 bytes a2bc0d94
+ 008e9ca4 bytes abbc0d94
~~~


<a id="compare-a7b25a73176a4269da8bb6e96ae6b893"></a>

### [`008e8d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md) → [`008e9cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9cb8.md) FUN_008e9cb8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`008e963c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md#insn-008e8d94) · [`008e8e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md#insn-008e8e50) · [`008e8e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md#insn-008e8e6c)
- 新版 [`008e9d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9cb8.md#insn-008e9d40) · [`008e9dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9cb8.md#insn-008e9dfc) · [`008e9e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9cb8.md#insn-008e9e18)

~~~diff
- 008e8d94 ["INT_ADD", "register:40f0:8", ["const:8e8d94:8", "const:4:8"]]
- 008e8d94 ["CALL", null, ["callee:00c58f30:8"]]
+ 008e9d40 ["INT_ADD", "register:40f0:8", ["const:8e9d40:8", "const:4:8"]]
+ 008e9d40 ["CALL", null, ["callee:00c58f30:8"]]
- 008e8d94 bytes 73bc0d94
+ 008e9d40 bytes 7cbc0d94
- 008e8e50 ["INT_ADD", "register:40f0:8", ["const:8e8e50:8", "const:4:8"]]
- 008e8e50 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9dfc ["INT_ADD", "register:40f0:8", ["const:8e9dfc:8", "const:4:8"]]
+ 008e9dfc ["CALL", null, ["callee:00c58f50:8"]]
- 008e8e50 bytes 4cbc0d94
+ 008e9dfc bytes 55bc0d94
- 008e8e6c ["INT_ADD", "register:40f0:8", ["const:8e8e6c:8", "const:4:8"]]
- 008e8e6c ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9e18 ["INT_ADD", "register:40f0:8", ["const:8e9e18:8", "const:4:8"]]
+ 008e9e18 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8e6c bytes 45bc0d94
+ 008e9e18 bytes 4ebc0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2a3072d000fa0c3b8edd7aa6d14a737"></a>

### [`008e8e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md) → [`008e9e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9e40.md) FUN_008e9e40

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e85a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`008e954c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md#insn-008e8efc) · [`008e8f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md#insn-008e8f98) · [`008e8fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md#insn-008e8fb4)
- 新版 [`008e9ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9e40.md#insn-008e9ea8) · [`008e9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9e40.md#insn-008e9f44) · [`008e9f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9e40.md#insn-008e9f60)

~~~diff
- 008e8efc ["INT_ADD", "register:40f0:8", ["const:8e8efc:8", "const:4:8"]]
- 008e8efc ["CALL", null, ["callee:00c58f30:8"]]
+ 008e9ea8 ["INT_ADD", "register:40f0:8", ["const:8e9ea8:8", "const:4:8"]]
+ 008e9ea8 ["CALL", null, ["callee:00c58f30:8"]]
- 008e8efc bytes 19bc0d94
+ 008e9ea8 bytes 22bc0d94
- 008e8f98 ["INT_ADD", "register:40f0:8", ["const:8e8f98:8", "const:4:8"]]
- 008e8f98 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9f44 ["INT_ADD", "register:40f0:8", ["const:8e9f44:8", "const:4:8"]]
+ 008e9f44 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8f98 bytes fabb0d94
+ 008e9f44 bytes 03bc0d94
- 008e8fb4 ["INT_ADD", "register:40f0:8", ["const:8e8fb4:8", "const:4:8"]]
- 008e8fb4 ["CALL", null, ["callee:00c58f50:8"]]
+ 008e9f60 ["INT_ADD", "register:40f0:8", ["const:8e9f60:8", "const:4:8"]]
+ 008e9f60 ["CALL", null, ["callee:00c58f50:8"]]
- 008e8fb4 bytes f3bb0d94
+ 008e9f60 bytes fcbb0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

